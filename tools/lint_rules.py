"""K2 · /lint active-suggestion rules — Karpathy 原教旨 upgrade.

PRD §0.5.4 Karpathy inheritance ledger names three /lint capabilities as
Karpathy-明示 (原话: "Look for: contradictions between pages, stale claims
that newer sources have superseded... data gaps that could be filled with
a web search. The LLM is good at suggesting new questions to investigate
and new sources to look for.") but not implemented in v2.1.

This module ships the **structural MVP** of all three rules:

  Rule A · Contradictions
    Same entity (by normalized title) with mismatched authority-field
    values across pages. Structural only — the LLM tier (semantic
    contradictions across bodies) defers to Sprint 5 per PRD §0.5.3
    principle 1 (late binding).

  Rule B · Stale claims
    Pages that cite a target that `[retracts-<code>]` edges have
    invalidated in `.agent/graph/*.md`. Emits 🟡; no auto-mutation of
    downstream pages in MVP (defers to --fix in Sprint 5).

  Rule C · Material requests
    Wikilink targets that are missing AND appear in ≥ 2 distinct pages.
    These graduate from individual broken-link noise to a material gap:
    "something deserves ingest."

All three are pure file ops — no LLM calls. Safe to run by default.
Each emits `LintIssue` entries; they do NOT write files in MVP. A
Sprint 5 follow-up will add `--suggest` side-effects that write
`wiki/questions/{contradiction,material-request}-*.md` stubs.

Integration: import and call from tools/lint.py's `lint()` function.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

try:
    from lens_loader import LensConfig
except ImportError:  # allow tools/ to be importable as a package
    from tools.lens_loader import LensConfig  # type: ignore[no-redef]

try:
    from lint import LintIssue, WIKILINK_RE, extract_frontmatter
except ImportError:
    from tools.lint import LintIssue, WIKILINK_RE, extract_frontmatter  # type: ignore[no-redef]

__all__ = [
    "check_contradictions",
    "check_stale_claims",
    "check_material_requests",
]

# Retraction-edge grammar used in .agent/graph/*.md files. Lines of the
# form `[[a]] [retracts-<code>] [[b]]` flag `b` as retracted with the
# reason coded in `<code>`. Grammar source: `.agent/spec/gap-algorithm.md §2`.
_RETRACTS_RE = re.compile(
    r"\[\[(?P<from>[^\]|]+)\]\]\s*\[retracts-(?P<code>[\w-]+)\]\s*\[\[(?P<to>[^\]|]+)\]\]"
)

# Titles normalized to lowercase and stripped for cross-page equivalence.
def _norm_title(s: str) -> str:
    return s.strip().lower()


# ---------------------------------------------------------------------------
# Rule A · Contradiction detection (structural tier only)
# ---------------------------------------------------------------------------


def check_contradictions(
    wiki_dir: Path,
    pages: dict[str, Path],
    lens: Optional[LensConfig] = None,
) -> list[LintIssue]:
    """Detect same-titled pages with mismatched authority-field values.

    Only fires when a lens is active AND the lens declares
    `anchors.authority_fields`. Without a lens, the project has no
    declaration of which fields are "the source of truth" for an
    entity — so structural contradiction is undefined.

    False-positive mitigation: a motif cited with two different AAT
    IDs is not necessarily an error (it may span multiple AAT
    concepts). Severity is 🟡 — the user decides whether to reconcile,
    annotate, or acknowledge.
    """
    issues: list[LintIssue] = []
    if lens is None or lens.anchors is None:
        return issues
    authority_fields = list(lens.anchors.get("authority_fields") or [])
    if not authority_fields:
        return issues

    # Map normalized title → list of (page_path, authority_values_dict)
    by_title: dict[str, list[tuple[Path, dict]]] = {}
    for slug, fpath in pages.items():
        try:
            fm = extract_frontmatter(fpath.read_text(encoding="utf-8"))
        except OSError:
            continue
        title_raw = fm.get("title") or slug
        if not isinstance(title_raw, str):
            continue
        key = _norm_title(title_raw)
        anchors = {
            f: fm[f] for f in authority_fields
            if f in fm and fm[f] not in (None, "", [])
        }
        if not anchors:
            continue  # No authority data to compare against; skip silently.
        by_title.setdefault(key, []).append((fpath, anchors))

    for title_key, entries in by_title.items():
        if len(entries) < 2:
            continue
        # Gather all authority values per field across the pages sharing this title
        per_field: dict[str, set] = {}
        for _, anchors in entries:
            for field, value in anchors.items():
                # Hashable coercion: lists → tuple
                hv = tuple(value) if isinstance(value, list) else value
                per_field.setdefault(field, set()).add(hv)
        conflict_fields = [f for f, vals in per_field.items() if len(vals) > 1]
        if not conflict_fields:
            continue
        # Emit one issue per page in the cluster so the user sees both
        # sides — lint output grouped by file is the native UX.
        for fpath, _ in entries:
            rel = str(fpath.relative_to(wiki_dir))
            other_paths = [
                str(p.relative_to(wiki_dir)) for p, _ in entries if p != fpath
            ]
            issues.append(
                LintIssue(
                    "🟡", "contradiction", rel,
                    f"title '{title_key}' appears with conflicting "
                    f"{', '.join(conflict_fields)} across: "
                    f"{', '.join(other_paths)}",
                    suggestion=(
                        "Reconcile the conflicting field value(s), OR add a "
                        "[contradicts] edge in graph/edges.jsonl to acknowledge "
                        "the divergence, OR mark the conflicting claim with "
                        "`lint-ignore: contradiction` if intentional."
                    ),
                )
            )
    return issues


# ---------------------------------------------------------------------------
# Rule B · Stale claim detection
# ---------------------------------------------------------------------------


def _find_retracted_targets(vault_root: Path) -> set[str]:
    """Scan `<vault>/.agent/graph/*.md` for retracts-<code> edges.

    Returns the set of `to` slugs that have been retracted at least once.
    Lenient: a single retraction is enough — we don't count dissents.
    Retraction grammar: `[[from]] [retracts-<code>] [[to]]` per
    `.agent/spec/gap-algorithm.md §2`.
    """
    graph_dir = vault_root / ".agent" / "graph"
    if not graph_dir.exists():
        return set()
    retracted: set[str] = set()
    for md in graph_dir.glob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in _RETRACTS_RE.finditer(text):
            retracted.add(m.group("to").strip())
    return retracted


def check_stale_claims(
    wiki_dir: Path,
    pages: dict[str, Path],
) -> list[LintIssue]:
    """Pages citing a retracted target get a 🟡 stale-claim warning.

    `vault_root = wiki_dir.parent` — the retraction index lives in
    `.agent/graph/`, parallel to `wiki/`.

    A page is itself retracted if it appears as the `to` of any
    retraction edge. We do NOT warn about the retracted page itself
    (that's correct, by design — it's already acknowledged). We only
    warn about downstream pages that cite it without acknowledging the
    retraction.

    MVP skips body-mutation (appending `[RETRACTED-PENDING]` markers);
    that belongs to --fix and defers to Sprint 5.
    """
    issues: list[LintIssue] = []
    vault_root = wiki_dir.parent
    retracted = _find_retracted_targets(vault_root)
    if not retracted:
        return issues
    for slug, fpath in pages.items():
        if slug in retracted:
            continue  # Don't warn the retracted page about itself.
        try:
            content = fpath.read_text(encoding="utf-8")
        except OSError:
            continue
        rel = str(fpath.relative_to(wiki_dir))
        stale_refs_reported = set()
        for m in WIKILINK_RE.finditer(content):
            target = m.group(1).strip()
            if target in retracted and target not in stale_refs_reported:
                stale_refs_reported.add(target)
                issues.append(
                    LintIssue(
                        "🟡", "stale-claim", rel,
                        f"cites [[{target}]] which is retracted in "
                        ".agent/graph/*.md",
                        suggestion=(
                            f"Either drop the [[{target}]] citation, "
                            "replace with the superseding entity, or "
                            f"annotate the cite as `[[{target}]] "
                            "[RETRACTED-PENDING]` acknowledging the staleness."
                        ),
                    )
                )
    return issues


# ---------------------------------------------------------------------------
# Rule C · Material request generation (entity-gap trigger)
# ---------------------------------------------------------------------------


# Minimum number of pages a missing target must appear in before it
# graduates from "broken-link noise" to "material gap." Below this, the
# existing broken-link check is sufficient.
_MATERIAL_REQUEST_MIN_REFS = 2


def check_material_requests(
    wiki_dir: Path,
    pages: dict[str, Path],
) -> list[LintIssue]:
    """Missing wikilink targets referenced by ≥ 2 pages graduate to material gap.

    Rationale (K2 audit, PRD §0.5.4): single broken links are localized
    noise — the user may just delete the link. Multiple pages reaching
    for the same missing target is a signal: something in the vault
    *wants* a page for that slug, and the wiki's own structure has
    stated the need. Karpathy 原文: "data gaps that could be filled with
    a web search."

    MVP emits 🔵 (informational) LintIssues only. A Sprint 5 `--suggest`
    follow-up will write `wiki/questions/material-request-<slug>-<date>.md`
    with lens-specific search query templates.
    """
    issues: list[LintIssue] = []
    # target slug → set of referencing pages (rel paths)
    missing_refs: dict[str, set[str]] = {}
    for slug, fpath in pages.items():
        try:
            content = fpath.read_text(encoding="utf-8")
        except OSError:
            continue
        rel = str(fpath.relative_to(wiki_dir))
        for m in WIKILINK_RE.finditer(content):
            target = m.group(1).strip()
            if target in pages:
                continue
            missing_refs.setdefault(target, set()).add(rel)

    for target, referrers in sorted(missing_refs.items()):
        if len(referrers) < _MATERIAL_REQUEST_MIN_REFS:
            continue
        sample = sorted(referrers)[:3]
        issues.append(
            LintIssue(
                "🔵", "material-request", f"(missing: {target})",
                f"[[{target}]] is referenced by {len(referrers)} pages but "
                f"no page exists — this is a material gap, not just a "
                f"broken link",
                suggestion=(
                    f"Ingest source material about '{target}' and let "
                    f"/ingest create the page. Referenced by: "
                    f"{', '.join(sample)}"
                    + (f" (and {len(referrers) - 3} more)"
                       if len(referrers) > 3 else "")
                ),
            )
        )
    return issues
