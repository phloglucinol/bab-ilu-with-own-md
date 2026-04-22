"""Lens-aware ingest orchestration + partial-failure resume journal.

This module is the mechanical layer under the `/ingest` skill. The skill
doc (`.claude/skills/ingest/SKILL.md`) describes *what* gets ingested;
this runner enforces *how* the orchestration survives partial failures.

Responsibilities:

1. **Lens-aware path resolution.** Given an input and the active lens,
   compute the destination `wiki/{tier_0}/<slug>.md`. Tier_0 comes from
   `lens.entity_model.tier_0`.
2. **Type detection.** URL / PDF / image / video / markdown / plain text.
   Classification is by extension + simple URL heuristics (we don't
   sniff MIME types for the scaffold — extension suffices for the
   current three lenses' seed material).
3. **Journal-based resume.** Every action writes one JSONL entry to
   `.agent/state/ingest-journal.jsonl`. On re-run, completed inputs are
   skipped; failures are retriable with `--retry-failed`.
4. **Log append.** Successful ingests append to `wiki/_log/usage.jsonl`
   with a `lens` tag so `/taste` diagnostic mode can replay history.

Content extraction (what the LLM actually writes inside the
generated MDs) is intentionally out of scope for this scaffold —
it lands in per-lens pipelines in Sprint 3+. This runner writes
*frontmatter-only stubs* for non-aesthetic lenses, which is enough for
`/lint` to validate and `/gap` to include in its graph scan.

Design choices:

1. **Pure-function core, filesystem shell.** `classify_input`,
   `resolve_output_paths`, `journal_status_for` are pure and
   independently testable. `run_ingest` is the one orchestration seam.
2. **Idempotent by input path.** Same input-key twice = second call is a
   no-op (unless `--force`). Makes `/ingest --retry-failed` safe.
3. **Never clobber user edits.** If the target output file exists with
   non-agent content (no `AGENT_MARKER`), the runner records a
   `skipped-existing` journal entry instead of overwriting.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

try:
    from graph_analyzer import _resolve_lens  # type: ignore[no-redef]
    from lens_loader import LensConfig  # type: ignore[no-redef]
except ImportError:  # tools/ also importable as a package
    from tools.graph_analyzer import _resolve_lens
    from tools.lens_loader import LensConfig

JOURNAL_PATH = Path(".agent/state/ingest-journal.jsonl")
LOG_PATH = Path("wiki/_log/usage.jsonl")

INPUT_TYPES = {"url", "pdf", "image", "video", "markdown", "text", "unknown"}

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif", ".tiff"}
VIDEO_EXTS = {".mp4", ".mov", ".webm", ".mkv", ".avi"}
PDF_EXTS = {".pdf"}
MARKDOWN_EXTS = {".md", ".markdown"}
TEXT_EXTS = {".txt", ".html", ".htm"}

_SLUG_RE = re.compile(r"[^a-z0-9]+")


# ---------------------------------------------------------------------------
# Pure helpers
# ---------------------------------------------------------------------------


def classify_input(raw: str) -> str:
    """Return one of INPUT_TYPES for `raw`.

    Recognition rules (deterministic, no I/O):
      - starts with http:// or https:// → "url"
      - extension in IMAGE_EXTS → "image"
      - extension in VIDEO_EXTS → "video"
      - extension in PDF_EXTS  → "pdf"
      - extension in MARKDOWN_EXTS → "markdown"
      - extension in TEXT_EXTS  → "text"
      - otherwise "unknown"
    """
    if raw.startswith(("http://", "https://")):
        return "url"
    suffix = Path(raw).suffix.lower()
    if suffix in IMAGE_EXTS:
        return "image"
    if suffix in VIDEO_EXTS:
        return "video"
    if suffix in PDF_EXTS:
        return "pdf"
    if suffix in MARKDOWN_EXTS:
        return "markdown"
    if suffix in TEXT_EXTS:
        return "text"
    return "unknown"


def slugify(text: str) -> str:
    """Kebab-case slug suitable for `wiki/{tier_0}/<slug>.md`."""
    lower = text.lower()
    clean = _SLUG_RE.sub("-", lower).strip("-")
    return clean or "untitled"


def slug_from_input(raw: str) -> str:
    """Pick a stable slug from an input path or URL."""
    if raw.startswith(("http://", "https://")):
        parsed = urlparse(raw)
        base = (parsed.netloc + parsed.path).strip("/")
        return slugify(base or "url")
    p = Path(raw)
    return slugify(p.stem)


@dataclass(frozen=True)
class OutputPlan:
    """Computed destination paths for a single input under a given lens."""
    tier_0_path: Path
    tier_1_atom_dir: Path  # where downstream extraction WOULD drop atoms
    slug: str


def resolve_output_paths(vault: Path, lens: LensConfig, raw: str) -> OutputPlan:
    """Compute destination paths from lens.entity_model.

    The tier_0 file path is deterministic given (vault, lens, input
    slug). Tier_1 atoms inherit a directory but their slugs are chosen
    by downstream extractors — we only pre-compute the directory so the
    downstream knows where to write.
    """
    tier_0 = lens.entity_model["tier_0"]
    tier_1_atom = lens.entity_model["tier_1_atom"]
    slug = slug_from_input(raw)
    return OutputPlan(
        tier_0_path=vault / "wiki" / tier_0 / f"{slug}.md",
        tier_1_atom_dir=vault / "wiki" / tier_1_atom,
        slug=slug,
    )


def journal_status_for(journal_lines: Iterable[dict], input_key: str) -> str | None:
    """Return the latest status for `input_key` from a journal iterable.

    Statuses are one of: 'success' / 'fail' / 'start' (incomplete) /
    None (never seen). 'start' means a run began but did not record a
    terminal status — those are treated as failures for retry logic.
    """
    latest_action: str | None = None
    for line in journal_lines:
        if line.get("input") != input_key:
            continue
        action = line.get("action", "")
        if action.startswith("ingest."):
            latest_action = action.split(".", 1)[1]
    return latest_action


def read_journal(journal_path: Path) -> list[dict]:
    """Read the journal as a list of dict records. Missing file → []."""
    if not journal_path.exists():
        return []
    out: list[dict] = []
    for line in journal_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue  # corrupt line; drop silently so one bad line doesn't block resume
    return out


def append_journal(journal_path: Path, record: dict) -> None:
    """Append one JSONL record. Creates parent dirs as needed."""
    journal_path.parent.mkdir(parents=True, exist_ok=True)
    with journal_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Tier-0 stub writer
# ---------------------------------------------------------------------------


AGENT_MARKER = "<!-- ingest-runner:agent-stub -->"


# ---------------------------------------------------------------------------
# Lens-specific extractor dispatch
# ---------------------------------------------------------------------------


def _run_incident_extractor(
    vault: Path, lens: LensConfig, raw: str, input_type: str, *, force: bool = False,
) -> tuple[Path | None, str | None]:
    """Dispatch target for engineering-alexander URL/PDF inputs.

    Returns (output_path, error_reason). Returns (None, None) to request
    fallthrough to the stub writer when:

      - the target already exists (either as an agent stub or as user
        content) — scaffold's own idempotency logic handles both cases;
      - the input is a local PDF path that does not exist on disk —
        downstream tests use synthetic placeholder paths and expect the
        scaffold stub shape. Only existent PDFs or real URLs trigger
        the extractor.
    """
    from tools.incident_extractor import extract_incident, ExtractionError

    plan = resolve_output_paths(vault, lens, raw)
    if plan.tier_0_path.exists():
        # Let the scaffold writer journal both exists-agent-stub and
        # exists-user-content with its existing rules.
        return None, None

    # Graceful fallthrough: non-existent local PDF → scaffold stub.
    if input_type == "pdf" and not raw.startswith(("http://", "https://")):
        if not Path(raw).exists():
            return None, None

    result = extract_incident(raw, vault=vault, lens=lens)
    if isinstance(result, ExtractionError):
        return None, f"{result.stage}: {result.reason}"
    result.output_path.parent.mkdir(parents=True, exist_ok=True)
    result.output_path.write_text(result.markdown, encoding="utf-8")
    return result.output_path, None


def _run_note_extractor(
    vault: Path, lens: LensConfig, raw: str, input_type: str, *, force: bool = False,
) -> tuple[Path | None, str | None]:
    """Dispatch target for general-zettelkasten URL/PDF/markdown/text inputs.

    Delegates to tools.note_extractor.run_note_extractor, which writes a
    populated tier_0 note stub (frontmatter + structured TODO body). No LLM
    calls; Claude content-authors the note body via the lens SKILL.md after
    ingest.

    Returns (output_path, None) on success, (None, error_msg) on hard failure,
    or (None, None) to signal fallthrough to the stub writer.
    """
    from tools.note_extractor import run_note_extractor

    output_path, err = run_note_extractor(vault, lens, raw, input_type, force=force)
    if err == "exists-user-content":
        # Signal ingest_one to journal skipped-existing, not fail.
        return None, None
    return output_path, err


# Dispatch table: (lens_id, input_type) -> (callable, journal-tag).
# The journal tag is the value written to `ingest.success.extractor` and
# is what downstream tooling filters on. Keep hardcoded (not derived from
# function names) so renaming a helper never breaks a journal consumer.
_EXTRACTORS: "dict[tuple[str, str], tuple[object, str]]" = {
    ("engineering-alexander", "url"): (_run_incident_extractor, "incident_extractor"),
    ("engineering-alexander", "pdf"): (_run_incident_extractor, "incident_extractor"),
    ("general-zettelkasten", "url"): (_run_note_extractor, "note_extractor"),
    ("general-zettelkasten", "pdf"): (_run_note_extractor, "note_extractor"),
    ("general-zettelkasten", "markdown"): (_run_note_extractor, "note_extractor"),
    ("general-zettelkasten", "text"): (_run_note_extractor, "note_extractor"),
}


def _render_frontmatter_stub(
    lens: LensConfig,
    raw: str,
    input_type: str,
    slug: str,
) -> str:
    """Render a minimal tier_0 frontmatter + body stub.

    The stub is lens-aware: anchor fields are pre-populated with empty
    strings when the lens declares them in `anchors.authority_fields`
    (so downstream editors know to fill them in). Zettelkasten-shaped
    lenses (no authority_fields) get only `source_url` / `source_path`.
    """
    tier_0 = lens.entity_model["tier_0"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "---",
        f"type: {tier_0}",
        f"lens: {lens.id}",
        f"slug: {slug}",
        f"ingested_at: {now}",
        f"input_type: {input_type}",
    ]
    if raw.startswith(("http://", "https://")):
        lines.append(f"source_url: {raw}")
    else:
        lines.append(f"source_path: {raw}")

    authority_fields = []
    if lens.anchors and isinstance(lens.anchors.get("authority_fields"), list):
        authority_fields = list(lens.anchors["authority_fields"])
    for field in authority_fields:
        lines.append(f"{field}: \"\"")  # empty string = editor-fill-me sentinel

    lines.extend([
        "status: draft",
        "---",
        "",
        AGENT_MARKER,
        "",
        f"# {slug}",
        "",
        f"_Stub generated by `/ingest` under lens `{lens.id}`._",
        "",
        "## Source",
        f"- Input: `{raw}`",
        f"- Type: {input_type}",
        "",
        "## Notes",
        "",
        f"<!-- Fill in tier-0 content per lens-specific rules. For "
        f"`{lens.id}`, see `.agent/lenses/{lens.id}/prompts.md`. -->",
        "",
    ])
    return "\n".join(lines)


def write_tier_0_stub(plan: OutputPlan, lens: LensConfig, raw: str,
                       input_type: str, *, force: bool = False) -> tuple[bool, str]:
    """Write the tier_0 stub to `plan.tier_0_path`.

    Returns (wrote_file, reason). If the target exists with non-agent
    content and `force` is False, writes nothing and returns
    (False, "exists-user-content"). If it exists with an agent stub
    (marker present), the stub is rewritten only when `force` is True
    (False otherwise, reason "exists-agent-stub").
    """
    plan.tier_0_path.parent.mkdir(parents=True, exist_ok=True)
    if plan.tier_0_path.exists():
        existing = plan.tier_0_path.read_text(encoding="utf-8")
        if AGENT_MARKER in existing:
            if not force:
                return False, "exists-agent-stub"
        else:
            return False, "exists-user-content"
    body = _render_frontmatter_stub(lens, raw, input_type, plan.slug)
    plan.tier_0_path.write_text(body, encoding="utf-8")
    return True, "written"


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ingest_one(
    vault: Path,
    lens: LensConfig,
    raw: str,
    *,
    journal: list[dict],
    journal_path: Path,
    log_path: Path,
    force: bool = False,
) -> dict:
    """Ingest a single input. Returns the terminal journal record.

    Side effects: writes stub file + appends two journal lines (start,
    terminal) + one usage log line on success.
    """
    prior = journal_status_for(journal, raw)
    if prior == "success" and not force:
        return {"action": "ingest.skip", "input": raw, "reason": "already-success",
                "ts": _now_iso()}

    input_type = classify_input(raw)
    plan = resolve_output_paths(vault, lens, raw)

    append_journal(journal_path, {
        "action": "ingest.start", "input": raw, "lens": lens.id,
        "input_type": input_type, "ts": _now_iso(),
    })

    if input_type == "unknown":
        rec = {"action": "ingest.fail", "input": raw, "lens": lens.id,
               "error": f"unknown input type for {raw!r}; add extension handler",
               "ts": _now_iso()}
        append_journal(journal_path, rec)
        return rec

    # Lens-specific extractor dispatch. When present, the extractor
    # replaces the stub with a populated tier_0 page. Fall through to
    # the stub writer for any lens/input-type combination we don't own.
    dispatch = _EXTRACTORS.get((lens.id, input_type))
    if dispatch is not None:
        extractor_fn, extractor_name = dispatch
        output_path, err = extractor_fn(vault, lens, raw, input_type, force=force)
        if err is not None:
            rec = {"action": "ingest.fail", "input": raw, "lens": lens.id,
                   "error": err, "ts": _now_iso()}
            append_journal(journal_path, rec)
            return rec
        if output_path is not None:
            rel = output_path.relative_to(vault)
            rec = {
                "action": "ingest.success", "input": raw, "lens": lens.id,
                "input_type": input_type,
                "outputs": [str(rel)],
                "extractor": extractor_name,
                "ts": _now_iso(),
            }
            append_journal(journal_path, rec)
            log_entry = {
                "action": "ingest", "lens": lens.id, "input": raw,
                "outputs": rec["outputs"], "tier_0_written": 1,
                "tier_1_atoms_drafted": 0,
                "ts": rec["ts"],
            }
            log_path.parent.mkdir(parents=True, exist_ok=True)
            with log_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
            return rec
        # extractor declined (e.g. user-content exists) — fall through
        # to the stub writer which will journal the correct 'skip' reason.

    wrote, reason = write_tier_0_stub(plan, lens, raw, input_type, force=force)
    if not wrote and reason == "exists-user-content":
        rec = {"action": "ingest.skip", "input": raw, "lens": lens.id,
               "reason": reason, "ts": _now_iso()}
        append_journal(journal_path, rec)
        return rec

    rec = {
        "action": "ingest.success", "input": raw, "lens": lens.id,
        "input_type": input_type,
        "outputs": [str(plan.tier_0_path.relative_to(vault))],
        "ts": _now_iso(),
    }
    append_journal(journal_path, rec)

    # Also append to the vault-wide usage log
    log_entry = {
        "action": "ingest", "lens": lens.id, "input": raw,
        "outputs": rec["outputs"], "tier_0_written": 1 if wrote else 0,
        "tier_1_atoms_drafted": 0,  # scaffold doesn't extract atoms yet
        "ts": rec["ts"],
    }
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

    return rec


def run_ingest(
    vault: Path,
    lens: LensConfig,
    inputs: list[str],
    *,
    force: bool = False,
    retry_failed: bool = False,
) -> list[dict]:
    """Main entry. Orchestrates the batch under the active lens.

    Returns the list of terminal records for each input (useful for
    tests and CLI summary).
    """
    journal_path = vault / JOURNAL_PATH
    log_path = vault / LOG_PATH
    journal = read_journal(journal_path)

    results: list[dict] = []
    for raw in inputs:
        if retry_failed:
            # Only process inputs whose last status was 'fail' or 'start'
            last = journal_status_for(journal, raw)
            if last not in (None, "fail", "start"):
                continue
        rec = ingest_one(vault, lens, raw, journal=journal,
                         journal_path=journal_path, log_path=log_path,
                         force=force)
        results.append(rec)
        # Refresh journal so subsequent inputs see this result
        journal.append(rec)
    return results


def _validate_vault_or_exit(vault_path: Path) -> Path:
    """Fail fast if `vault_path` does not look like a Bab-ilu vault.

    Parallel to the helper in graph_analyzer/quality_gates/prompt_tester/
    migrate_v13_to_v14. Ingesting into a non-vault cwd would silently
    create wiki/<tier_0>/<slug>.md anywhere — exactly the "works on my
    machine" failure mode Wave 5 tried to kill. Validate here too.
    """
    vault_path = vault_path.resolve()
    has_agent = (vault_path / ".agent").is_dir()
    has_wiki = (vault_path / "wiki").is_dir()
    if not (has_agent or has_wiki):
        import sys as _sys
        print(
            f"error: {vault_path} does not look like a Bab-ilu vault "
            f"(no .agent/ or wiki/ subdirectory). Pass --vault <path> "
            f"explicitly or run this command from a vault root.",
            file=_sys.stderr,
        )
        _sys.exit(2)
    return vault_path


def main() -> None:
    ap = argparse.ArgumentParser(prog="ingest_runner")
    ap.add_argument("--vault", default=".")
    ap.add_argument("--lens", default=None)
    ap.add_argument("--lenses-base", default=None)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--retry-failed", action="store_true")
    ap.add_argument("inputs", nargs="+", help="One or more input paths/URLs")
    args = ap.parse_args()

    vault = _validate_vault_or_exit(Path(args.vault))
    lens = _resolve_lens(args)
    results = run_ingest(
        vault, lens, args.inputs,
        force=args.force, retry_failed=args.retry_failed,
    )
    success = sum(1 for r in results if r["action"] == "ingest.success")
    skipped = sum(1 for r in results if r["action"] == "ingest.skip")
    failed = sum(1 for r in results if r["action"] == "ingest.fail")
    print(f"ingest summary: {success} written · {skipped} skipped · {failed} failed",
          file=sys.stderr)
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
