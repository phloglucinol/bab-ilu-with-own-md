"""Python backing for the `/ask` skill — lens-aware vault retrieval.

This module implements the 6-step retrieval order specified in
`.claude/skills/ask/SKILL.md`:

    1. Exact title in frontmatter of tier_0 / tier_1_atom / tier_1_cluster
    2. `aliases:` frontmatter match
    3. `original_terms:` frontmatter match (bilingual queries)
    4. `.agent/todos/<tier_1_cluster>-candidates.md` (A4 gap_runner output)
    5. `wiki/questions/*.md` (A4 bridge-candidate stubs)
    6. case-insensitive substring scan across markdown body

Higher-priority steps short-circuit lower ones — once step N returns hits,
steps N+1..6 are skipped. The `retrieval_trace` field on `AskResult` records
every step's attempt so callers can debug why a particular step won.

No LLM calls occur here. `_synthesize` produces a mechanical answer body that
embeds the active lens's `prompts.md` as a `<lens-context>` preamble. A
downstream wrapper may send `AskResult.answer` to an LLM for polishing; the
core retrieval + lens-tagging contract does not require it.
"""

from __future__ import annotations

import fcntl
import json
import re
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Optional

try:
    from lens_context import active_lens_preamble  # type: ignore[no-redef]
    from lens_loader import (  # type: ignore[no-redef]
        DEFAULT_BASE,
        LensConfig,
        LensValidationError,
        load_lens,
    )
except ImportError:  # tools/ also importable as a package
    from tools.lens_context import active_lens_preamble
    from tools.lens_loader import (
        DEFAULT_BASE,
        LensConfig,
        LensValidationError,
        load_lens,
    )

__all__ = [
    "AskResult",
    "AskRunnerError",
    "JOURNAL_PATH",
    "SYNTHESES_DIRNAME",
    "parse_frontmatter",
    "run_ask",
    "run_ask_interactive",
    "write_synthesis",
]

JOURNAL_PATH = Path(".agent/state/ingest-journal.jsonl")
ACTIVE_LENS_DIRNAME = "active"
# Directory under wiki/ where /ask filed-back syntheses live. Karpathy:
# "good answers can be filed back into the wiki as new pages... your
# explorations compound in the knowledge base just like ingested sources do."
SYNTHESES_DIRNAME = "syntheses"

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
# Max chars kept per source snippet — keeps AskResult bounded.
_SNIPPET_LIMIT = 200
# Hard cap on synthesis file body length. Prevents a runaway LLM polish
# step from writing unbounded files. Named constant per K1 audit risk.
_SYNTHESIS_MAX_CHARS = 8000
# Slug length cap for synthesis filenames. Deliberately short — filename is
# a hint, not a title; the real title lives in frontmatter.
_SYNTHESIS_SLUG_MAX = 40
# Lowercase + ASCII-safe; everything else collapses to "-".
_SLUG_CLEAN_RE = re.compile(r"[^a-z0-9]+")


class AskRunnerError(Exception):
    """Raised when /ask cannot run (bad lens, unreadable vault)."""


@dataclass(frozen=True)
class AskResult:
    """Return value of `run_ask`.

    Tuple-typed fields keep the dataclass hashable + immutable so callers
    can cache results across identical queries during a session.

    `query` is preserved so downstream filing (`write_synthesis`) does not
    need an out-of-band argument to recover the original question.
    """
    answer: str
    sources: tuple[dict, ...]
    retrieval_trace: tuple[dict, ...]
    lens: str
    query: str = ""


# ---------------------------------------------------------------------------
# Frontmatter parser — small, vendored; mirrors graph_analyzer.parse_frontmatter
# but kept private so /ask has no cross-module coupling on graph internals.
# ---------------------------------------------------------------------------


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Return (frontmatter_dict, body). Missing frontmatter -> ({}, text).

    Handles a small YAML subset sufficient for Bab-ilu vault files:
      - `key: value`
      - `key: [a, b, c]` inline lists
      - `key:` followed by `  - item` block lists
      - quoted string values
    """
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    out: dict[str, Any] = {}
    current_key: str | None = None
    for line in fm_raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and current_key is not None:
            val = stripped[2:].strip().strip('"').strip("'")
            existing = out.get(current_key)
            if isinstance(existing, list):
                existing.append(val)
            else:
                out[current_key] = [val]
            continue
        top = re.match(r"^([\w_-]+):\s*(.*)$", line)
        if not top:
            continue
        key, val = top.group(1), top.group(2).strip()
        if val == "":
            out[key] = []
            current_key = key
            continue
        if val.startswith("[") and val.endswith("]"):
            items = [
                s.strip().strip('"').strip("'")
                for s in val[1:-1].split(",")
                if s.strip()
            ]
            out[key] = items
        else:
            # YAML single-quote style: internal `''` encodes a literal `'`.
            # We handle this specifically (not the generic strip-and-forget
            # path) because write_synthesis emits titles/questions in
            # single-quote style so apostrophes round-trip correctly.
            if (len(val) >= 2 and val.startswith("'") and val.endswith("'")):
                inner = val[1:-1]
                out[key] = inner.replace("''", "'")
            elif (len(val) >= 2 and val.startswith('"')
                  and val.endswith('"')):
                out[key] = val[1:-1]
            else:
                out[key] = val
        current_key = key
    return out, body


def _read_md(path: Path) -> tuple[dict[str, Any], str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}, ""
    return parse_frontmatter(text)


# ---------------------------------------------------------------------------
# Lens resolution
# ---------------------------------------------------------------------------


def _resolve_active_lens(vault: Path, lens: Optional[str],
                         lenses_base: Optional[Path]) -> LensConfig:
    """Pick lens from explicit arg or active pointer. Fail loudly on missing.

    Precedence for lens-config location:
      1. Explicit `lenses_base` arg (tests, custom hosts) — honored verbatim,
         never falls back, so a bogus path surfaces as a clean error instead
         of silently loading the cwd's `.agent/lenses/`.
      2. `<vault>/.agent/lenses` when that dir exists.
      3. Package-level `DEFAULT_BASE` as a last-resort for bare scripts.
    """
    if lenses_base is not None:
        base = Path(lenses_base)
    else:
        candidate = vault / ".agent" / "lenses"
        base = candidate if candidate.exists() else DEFAULT_BASE
    if lens:
        try:
            return load_lens(lens, base=base)
        except FileNotFoundError as exc:
            raise AskRunnerError(f"lens '{lens}' not found: {exc}") from exc
        except LensValidationError as exc:
            raise AskRunnerError(f"lens '{lens}' invalid: {exc}") from exc

    active_yaml = base / ACTIVE_LENS_DIRNAME / "lens.yaml"
    if not active_yaml.exists():
        raise AskRunnerError(
            f"no lens specified and no active lens at {active_yaml}. "
            "Run /genesis to activate one, or pass lens=<id>."
        )
    import yaml  # local import — only needed when active pointer is used
    try:
        parsed = yaml.safe_load(active_yaml.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise AskRunnerError(f"cannot parse {active_yaml}: {exc}") from exc
    active_id = parsed.get("id")
    if not isinstance(active_id, str) or not active_id:
        raise AskRunnerError(f"{active_yaml} missing 'id' field")
    try:
        return load_lens(active_id, base=base)
    except (FileNotFoundError, LensValidationError) as exc:
        raise AskRunnerError(
            f"active lens '{active_id}' unreadable: {exc}"
        ) from exc


# ---------------------------------------------------------------------------
# Step helpers — each returns a list of source dicts with uniform shape
# ---------------------------------------------------------------------------


def _source(path: Path, vault: Path, step: str, title: str,
            snippet: str) -> dict:
    """Build a canonical source record. Path is stored vault-relative so
    AskResult is portable across cwd — absolute paths leak host layout."""
    try:
        rel = path.relative_to(vault)
    except ValueError:
        rel = path
    return {
        "path": str(rel),
        "step": step,
        "title": title,
        "snippet": snippet[:_SNIPPET_LIMIT],
    }


def _lens_entry_dirs(vault: Path, lens: LensConfig) -> list[Path]:
    """The three directories a lens owns for tier_0 / tier_1_atom / tier_1_cluster."""
    em = lens.entity_model
    return [
        vault / "wiki" / em["tier_0"],
        vault / "wiki" / em["tier_1_atom"],
        vault / "wiki" / em["tier_1_cluster"],
    ]


def _iter_entry_files(vault: Path, lens: LensConfig) -> Iterable[Path]:
    for d in _lens_entry_dirs(vault, lens):
        if not d.exists():
            continue
        for md in sorted(d.glob("*.md")):
            yield md


def _frontmatter_matches_lens(fm: dict, lens_id: str) -> bool:
    """Entries with no `lens:` field are treated as current-lens-owned
    (pre-v2.1 vaults, cross-lens shared references). Entries with a
    different lens id are excluded from retrieval — consistent with
    SKILL.md "Prefer entries whose frontmatter lens field matches"."""
    entry_lens = fm.get("lens")
    if entry_lens is None:
        return True
    if isinstance(entry_lens, list):
        return lens_id in entry_lens or not entry_lens
    return entry_lens == lens_id


def _title_from_fm(fm: dict, fallback: str) -> str:
    for key in ("title", "name", "slug"):
        v = fm.get(key)
        if isinstance(v, str) and v:
            return v
    return fallback


def _normalize(s: str) -> str:
    return s.strip().lower()


def _step0_syntheses(vault: Path, lens: LensConfig, query: str) -> list[dict]:
    """Scan `wiki/syntheses/` for prior filed-back answers matching the query.

    Syntheses are lens-scoped: a synthesis written under lens X is invisible
    under lens Y. This mirrors the retrieval-side half of the citation guard
    from `write_synthesis`.

    A synthesis matches if its frontmatter `question` or `title` normalizes
    to the query, OR the query appears as a case-insensitive substring of
    either field. The broader substring match is deliberate — syntheses are
    user-authored bundles ("How does X relate to Y?"), so exact-title match
    would be too strict.
    """
    syn_dir = vault / "wiki" / SYNTHESES_DIRNAME
    if not syn_dir.exists():
        return []
    hits: list[dict] = []
    q = _normalize(query)
    for md in sorted(syn_dir.glob("*.md")):
        fm, body = _read_md(md)
        if not _frontmatter_matches_lens(fm, lens.id):
            continue
        question = str(fm.get("question", "") or "")
        title = _title_from_fm(fm, md.stem)
        hay_question = _normalize(question)
        hay_title = _normalize(title)
        if (q == hay_question or q == hay_title
                or (q and (q in hay_question or q in hay_title))):
            hits.append(_source(md, vault, "step0_syntheses", title, body))
    return hits


def _step1_title(vault: Path, lens: LensConfig, query: str) -> list[dict]:
    q = _normalize(query)
    hits: list[dict] = []
    for md in _iter_entry_files(vault, lens):
        fm, body = _read_md(md)
        if not _frontmatter_matches_lens(fm, lens.id):
            continue
        title = _title_from_fm(fm, md.stem)
        if _normalize(title) == q or _normalize(md.stem) == q:
            hits.append(_source(md, vault, "step1_title", title, body))
    return hits


def _match_list_field(fm: dict, key: str, query: str) -> bool:
    val = fm.get(key)
    q = _normalize(query)
    if isinstance(val, list):
        return any(_normalize(str(v)) == q for v in val)
    if isinstance(val, str):
        return _normalize(val) == q
    return False


def _step2_aliases(vault: Path, lens: LensConfig, query: str) -> list[dict]:
    hits: list[dict] = []
    for md in _iter_entry_files(vault, lens):
        fm, body = _read_md(md)
        if not _frontmatter_matches_lens(fm, lens.id):
            continue
        if _match_list_field(fm, "aliases", query):
            title = _title_from_fm(fm, md.stem)
            hits.append(_source(md, vault, "step2_aliases", title, body))
    return hits


def _step3_original_terms(vault: Path, lens: LensConfig, query: str) -> list[dict]:
    hits: list[dict] = []
    for md in _iter_entry_files(vault, lens):
        fm, body = _read_md(md)
        if not _frontmatter_matches_lens(fm, lens.id):
            continue
        if _match_list_field(fm, "original_terms", query):
            title = _title_from_fm(fm, md.stem)
            hits.append(_source(md, vault, "step3_original_terms", title, body))
    return hits


def _step4_a4_candidates(vault: Path, lens: LensConfig, query: str) -> list[dict]:
    """Scan `.agent/todos/<tier_1_cluster>-candidates.md` for the query.

    Gap-runner writes one file per candidate set (see
    gap_runner.write_tier1_candidates); filename uses the lens's
    tier_1_cluster term, so we look for any file matching
    `*{cluster}-candidates.md` under `.agent/todos/`. If the query substring
    (case-insensitive) appears anywhere in the file, we emit one source —
    the file itself is "the answer" since the user asked about an open
    candidate.
    """
    todos_dir = vault / ".agent" / "todos"
    if not todos_dir.exists():
        return []
    cluster = lens.entity_model["tier_1_cluster"]
    pattern = f"*{cluster}-candidates.md"
    hits: list[dict] = []
    q = _normalize(query)
    for md in sorted(todos_dir.glob(pattern)):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        # Constrain the match to list-item lines so a heading like
        # `# Panel Candidates` never produces a false-positive for query
        # "panel". gap_runner always emits candidates as `- item` bullets.
        matched = False
        for raw_line in text.splitlines():
            stripped = raw_line.lstrip()
            if not (stripped.startswith("- ")
                    or stripped.startswith("* ")
                    or stripped.startswith("+ ")):
                continue
            if q in stripped.lower():
                matched = True
                break
        if matched:
            hits.append(_source(md, vault, "step4_a4_candidates", md.stem, text))
    return hits


def _step5_questions(vault: Path, query: str) -> list[dict]:
    questions_dir = vault / "wiki" / "questions"
    if not questions_dir.exists():
        return []
    hits: list[dict] = []
    q = _normalize(query)
    for md in sorted(questions_dir.glob("*.md")):
        fm, body = _read_md(md)
        title = _title_from_fm(fm, md.stem)
        haystack = f"{title}\n{body}".lower()
        if q in haystack:
            hits.append(_source(md, vault, "step5_questions", title, body))
    return hits


def _step6_grep_body(vault: Path, lens: LensConfig, query: str) -> list[dict]:
    hits: list[dict] = []
    q = _normalize(query)
    for md in _iter_entry_files(vault, lens):
        fm, body = _read_md(md)
        if not _frontmatter_matches_lens(fm, lens.id):
            continue
        if q in body.lower():
            title = _title_from_fm(fm, md.stem)
            # Extract a window around the match for a better snippet.
            idx = body.lower().find(q)
            start = max(0, idx - 40)
            end = min(len(body), idx + len(q) + 120)
            snippet = body[start:end]
            hits.append(_source(md, vault, "step6_grep_body", title, snippet))
    return hits


_STEP_FNS = (
    # step0 — Karpathy filed-back syntheses; highest priority because they
    # are curated answers to prior questions and let the wiki compound.
    ("step0_syntheses", _step0_syntheses),
    ("step1_title", _step1_title),
    ("step2_aliases", _step2_aliases),
    ("step3_original_terms", _step3_original_terms),
    ("step4_a4_candidates", _step4_a4_candidates),
    ("step5_questions", _step5_questions),  # lens-agnostic; wrapper below
    ("step6_grep_body", _step6_grep_body),
)


def _run_retrieval(vault: Path, lens: LensConfig, query: str
                   ) -> tuple[list[dict], list[dict]]:
    """Execute steps 1..6 with short-circuit. Always return full trace.

    Returns (sources, trace). `sources` holds only the winning step's hits;
    `trace` has one dict per step with `{step, step_name, attempted,
    match_count}` — attempted=False when a higher-priority step already won.
    """
    sources: list[dict] = []
    trace: list[dict] = []
    winning_step_index = -1
    for idx, (name, fn) in enumerate(_STEP_FNS):
        if winning_step_index >= 0:
            trace.append({"step": idx + 1, "step_name": name,
                          "attempted": False, "match_count": 0})
            continue
        if name == "step5_questions":
            result = fn(vault, query)  # no lens param
        else:
            result = fn(vault, lens, query)
        trace.append({"step": idx + 1, "step_name": name,
                      "attempted": True, "match_count": len(result)})
        if result:
            sources = result
            winning_step_index = idx
    return sources, trace


# ---------------------------------------------------------------------------
# Synthesis
# ---------------------------------------------------------------------------


def _synthesize(query: str, preamble: str, sources: list[dict],
                lens_id: str) -> str:
    """Assemble the answer string. Mechanical (no LLM)."""
    parts: list[str] = []
    if preamble:
        parts.append(preamble)
        parts.append("")
    parts.append(f"Q: {query}")
    parts.append("")
    if not sources:
        parts.append(
            "A: no vault entries matched this query under lens "
            f"`{lens_id}`. Consider `/ingest` for source material, or "
            "rephrase the query."
        )
        return "\n".join(parts)

    step_name = sources[0]["step"]
    parts.append(
        f"A: Found {len(sources)} match(es) via `{step_name}` under lens "
        f"`{lens_id}`."
    )
    parts.append("")
    parts.append("Sources:")
    for src in sources:
        parts.append(f"- [[{src['title']}]] — {src['path']}")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Journal
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _append_ask_journal(vault: Path, lens_id: str, query: str,
                        sources: list[dict], winning_step: str) -> None:
    journal_path = vault / JOURNAL_PATH
    journal_path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "action": "ask",
        "lens": lens_id,
        "query": query,
        "cited_count": len(sources),
        "sources": [s["path"] for s in sources],
        "step": winning_step,
        "ts": _now_iso(),
    }
    with journal_path.open("a", encoding="utf-8") as f:
        # Advisory lock so concurrent /ask invocations serialize journal
        # writes and never produce interleaved/partial JSONL lines. Released
        # on close by the `with` block.
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def run_ask(
    query: str,
    vault: Path,
    lens: Optional[str] = None,
    *,
    lenses_base: Optional[Path] = None,
    prompts_path: Optional[Path] = None,
) -> AskResult:
    """Execute /ask against `vault` under the active (or explicit) lens.

    Args:
        query: natural-language query from the user.
        vault: vault root containing `wiki/` and `.agent/`.
        lens: optional lens id override; default = active lens pointer.
        lenses_base: override for `<vault>/.agent/lenses` (tests).
        prompts_path: override for active `prompts.md` path (tests; also
            respected via `BABILU_LENS_PROMPTS_PATH` env var).

    Returns:
        AskResult with .answer (lens preamble + synthesized body),
        .sources tuple, .retrieval_trace tuple, and .lens id.

    Raises:
        AskRunnerError: when the lens cannot be resolved or is invalid.
        ValueError: when `query` is empty/whitespace.
    """
    if not query or not query.strip():
        raise ValueError("query must be a non-empty string")
    if "\x00" in query:
        raise ValueError("query contains null byte")

    vault = Path(vault).resolve()
    lens_cfg = _resolve_active_lens(vault, lens, lenses_base)

    sources, trace = _run_retrieval(vault, lens_cfg, query)

    preamble = active_lens_preamble(prompts_path)
    answer = _synthesize(query, preamble, sources, lens_cfg.id)

    winning_step = sources[0]["step"] if sources else "no_match"
    _append_ask_journal(vault, lens_cfg.id, query, sources, winning_step)

    # Track L · LENS EVOLUTION observer hook. Behavioral signal: user
    # asked something. The observer is dumb about what the query means;
    # it just records it, the matcher reads the digest later.
    # Non-mandatory — observer import failure must NOT break /ask.
    try:
        from tools.lens_evolution.observer import record_event as _le_record
        _le_record(
            vault, "ask_query", lens_cfg.id,
            {"query": query, "winning_step": winning_step,
             "cited_count": len(sources)},
        )
    except Exception:  # pragma: no cover — never break foreground
        pass

    return AskResult(
        answer=answer,
        sources=tuple(sources),
        retrieval_trace=tuple(trace),
        lens=lens_cfg.id,
        query=query,
    )


# ---------------------------------------------------------------------------
# K1 · Filed-back syntheses (Karpathy 原教旨: /ask answers compound into wiki)
# ---------------------------------------------------------------------------


def _slugify(text: str, max_len: int = _SYNTHESIS_SLUG_MAX) -> str:
    """ASCII-safe kebab slug. Non-alnum collapses to `-`. Truncated at `max_len`.

    Empty text (or text with zero alnum chars) returns `"synthesis"` so the
    resulting filename is always legal. Leading/trailing hyphens stripped.
    """
    s = _SLUG_CLEAN_RE.sub("-", text.lower()).strip("-")
    if not s:
        s = "synthesis"
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "synthesis"


def _yaml_escape(val: str) -> str:
    """Inline-safe single-quoted YAML scalar. Doubles interior single-quotes."""
    return "'" + val.replace("'", "''") + "'"


def write_synthesis(
    result: AskResult,
    vault: Path,
    *,
    custom_title: Optional[str] = None,
    today: Optional[date] = None,
) -> Path:
    """File an `AskResult` as `wiki/syntheses/<slug>.md` and return the path.

    Behavior (per K1 audit, PRD §0.5.4 Karpathy inheritance ledger):
      - Writes frontmatter: type, title, question, lens, date, cited.
      - `cited:` is derived from `result.sources` paths (lens-filtered at
        retrieval time, so no additional cross-lens scan is needed).
      - Hard cap body at `_SYNTHESIS_MAX_CHARS`; oversize bodies get a
        `[truncated]` marker rather than writing unbounded files.
      - Slug collisions get `-2`, `-3`, ... suffixes. The write is not atomic
        across the (stat, write) pair; two concurrent callers racing to file
        the same question could both pick slug `foo`, but the second write
        would overwrite the first. Filed-back is user-initiated and single-
        session, so this is acceptable for K1 MVP.
      - Empty sources are still written — a "no match" answer is a valid
        record of having asked the question. `cited:` becomes an empty list.

    Does NOT do (deferred per K1 MVP scope):
      - LLM polish of body text.
      - Cross-lens citation scanning of wikilinks inside the answer body
        (sources are already lens-filtered by retrieval).
      - Stale-source flag propagation (belongs to /lint K2 upgrade).
    """
    syn_dir = vault / "wiki" / SYNTHESES_DIRNAME
    syn_dir.mkdir(parents=True, exist_ok=True)

    raw_title = (custom_title or result.query or "synthesis").strip()
    title_for_slug = raw_title or "synthesis"
    base_slug = _slugify(title_for_slug)

    # Collision resolution
    slug = base_slug
    counter = 2
    while (syn_dir / f"{slug}.md").exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    body = result.answer
    truncated = False
    if len(body) > _SYNTHESIS_MAX_CHARS:
        body = body[:_SYNTHESIS_MAX_CHARS] + "\n\n[truncated]"
        truncated = True

    today = today or date.today()
    cited_paths = [src["path"] for src in result.sources]

    lines: list[str] = ["---"]
    lines.append("type: synthesis")
    lines.append(f"title: {_yaml_escape(raw_title)}")
    lines.append(f"question: {_yaml_escape(result.query)}")
    lines.append(f"lens: {result.lens}")
    lines.append(f"date: {today.isoformat()}")
    if cited_paths:
        lines.append("cited:")
        for path in cited_paths:
            lines.append(f"  - {path}")
    else:
        lines.append("cited: []")
    if truncated:
        lines.append("truncated: true")
    lines.append("---")
    lines.append("")
    lines.append(body)
    lines.append("")

    out = syn_dir / f"{slug}.md"
    out.write_text("\n".join(lines), encoding="utf-8")

    # Track L · LENS EVOLUTION observer hook — archiving is a strong
    # behavioral signal (user endorsed this answer enough to compound).
    try:
        from tools.lens_evolution.observer import record_event as _le_record
        _le_record(
            vault, "synthesis_accepted", result.lens,
            {"slug": slug, "question": result.query, "title": raw_title},
        )
    except Exception:  # pragma: no cover
        pass
    return out


def run_ask_interactive(
    query: str,
    vault: Path,
    lens: Optional[str] = None,
    *,
    lenses_base: Optional[Path] = None,
    prompts_path: Optional[Path] = None,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> tuple[AskResult, Optional[Path]]:
    """Interactive `/ask` wrapper: run, present answer, offer filed-back.

    Contract (per PRD §0.5.4: Karpathy's "file back good answers" is the
    core compounding mechanism, not an optional enhancement):

      1. Call `run_ask(...)` and print `result.answer` via `output_fn`.
      2. Prompt "Archive as synthesis? (Y/n/edit title):" via `input_fn`.
      3. Empty reply or "y"/"yes" → archive with default title (question).
         "n"/"no" → return (result, None).
         Any other string → archive with that string as custom_title.
      4. `EOFError` (non-TTY, piped input) is treated as "no archive" —
         never fail hard on non-interactive invocation.

    Returns (AskResult, synthesis_path_or_None).

    `input_fn` / `output_fn` are injectable for tests. Default `input`/`print`
    works in real interactive CLI usage.
    """
    result = run_ask(
        query, vault, lens,
        lenses_base=lenses_base, prompts_path=prompts_path,
    )
    output_fn(result.answer)

    try:
        reply = input_fn("Archive as synthesis? (Y/n/edit title): ")
    except EOFError:
        output_fn("(no tty — skipping archive)")
        return result, None

    reply = (reply or "").strip()
    if reply.lower() in ("n", "no"):
        return result, None
    if reply == "" or reply.lower() in ("y", "yes"):
        path = write_synthesis(result, vault)
    else:
        path = write_synthesis(result, vault, custom_title=reply)
    output_fn(f"archived → {path}")
    return result, path
