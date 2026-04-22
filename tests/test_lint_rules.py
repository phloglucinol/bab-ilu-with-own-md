"""Tests for tools/lint_rules.py — K2 active-suggestion checks.

Covers the three Karpathy原教旨 rules that land in Sprint 4 (PRD §0.5.4):
  Rule A · contradiction detection (lens-scoped, authority-field based)
  Rule B · stale-claim detection (retracts-<code> edge scan)
  Rule C · material-request generation (entity-gap trigger, ≥2 refs)

All three are structural — no LLM. LLM-backed tiers and --fix mutation
defer to Sprint 5 per PRD §0.5.3 principle 1 (late binding).
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = PROJECT_ROOT / "tools"
REAL_LENSES = PROJECT_ROOT / ".agent" / "lenses"

# Matches the existing test_lint.py import pattern: tools/ on sys.path,
# then `import lint_rules` directly.
sys.path.insert(0, str(TOOLS_DIR))

from lint_rules import (  # noqa: E402
    check_contradictions,
    check_material_requests,
    check_stale_claims,
)
from lens_loader import load_lens  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write_page(path: Path, frontmatter: dict, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---"]
    for k, v in frontmatter.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    lines.append(body)
    path.write_text("\n".join(lines), encoding="utf-8")


def _copy_real_lens(vault: Path, lens_id: str):
    """Install the real repo lens config into a tmp vault.

    Returns the loaded LensConfig.
    """
    dst = vault / ".agent" / "lenses"
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copy(REAL_LENSES / "schema.json", dst / "schema.json")
    shutil.copytree(REAL_LENSES / lens_id, dst / lens_id)
    return load_lens(lens_id, base=dst)


def _make_pages_dict(wiki_dir: Path) -> dict[str, Path]:
    """Mirror lint.find_all_pages for wiki directories that don't match
    the OmegaWiki ENTITY_DIRS layout. For lens-scoped fixtures we walk
    every .md under wiki/ and key by stem."""
    pages: dict[str, Path] = {}
    for md in wiki_dir.rglob("*.md"):
        if md.is_file():
            pages[md.stem] = md
    return pages


# ---------------------------------------------------------------------------
# Rule A · Contradictions
# ---------------------------------------------------------------------------


class TestContradictions:

    def test_no_lens_returns_empty(self, tmp_path: Path):
        """Without a lens, there's no declaration of authority fields,
        so structural contradiction is undefined."""
        wiki = tmp_path / "wiki"
        wiki.mkdir()
        pages = _make_pages_dict(wiki)
        assert check_contradictions(wiki, pages, lens=None) == []

    def test_lens_without_authority_fields_returns_empty(
        self, tmp_path: Path,
    ):
        """Zettelkasten lens has no institutional authority fields —
        absence is intentional per spec, not an incomplete lens."""
        lens = _copy_real_lens(tmp_path, "general-zettelkasten")
        wiki = tmp_path / "wiki"
        wiki.mkdir()
        pages = _make_pages_dict(wiki)
        assert check_contradictions(wiki, pages, lens=lens) == []

    def test_same_title_matching_authority_no_issue(
        self, tmp_path: Path,
    ):
        """Two pages with the same title and identical aat_id is fine —
        it's redundant but not contradictory."""
        lens = _copy_real_lens(tmp_path, "aesthetic-warburg")
        wiki = tmp_path / "wiki"
        _write_page(wiki / "motifs" / "mirror-a.md",
                    {"title": "Mirror Motif", "aat_id": "aat:300186906",
                     "lens": "aesthetic-warburg"})
        _write_page(wiki / "motifs" / "mirror-b.md",
                    {"title": "Mirror Motif", "aat_id": "aat:300186906",
                     "lens": "aesthetic-warburg"})
        pages = _make_pages_dict(wiki)
        issues = check_contradictions(wiki, pages, lens=lens)
        assert issues == []

    def test_same_title_conflicting_authority_flagged(
        self, tmp_path: Path,
    ):
        """The core positive case: same title, different aat_id
        across two pages → both flagged as contradictions."""
        lens = _copy_real_lens(tmp_path, "aesthetic-warburg")
        wiki = tmp_path / "wiki"
        _write_page(wiki / "motifs" / "mirror-a.md",
                    {"title": "Mirror Motif", "aat_id": "aat:300186906",
                     "lens": "aesthetic-warburg"})
        _write_page(wiki / "motifs" / "mirror-b.md",
                    {"title": "Mirror Motif", "aat_id": "aat:300186905",
                     "lens": "aesthetic-warburg"})
        pages = _make_pages_dict(wiki)
        issues = check_contradictions(wiki, pages, lens=lens)
        assert len(issues) == 2  # one per page in the conflict cluster
        categories = {i.category for i in issues}
        assert categories == {"contradiction"}
        levels = {i.level for i in issues}
        assert levels == {"🟡"}
        # Every issue must cite at least one authority field name in message
        for issue in issues:
            assert "aat_id" in issue.message

    def test_missing_authority_field_skipped(self, tmp_path: Path):
        """A page without any authority field populated is silently
        skipped — it has nothing to contradict."""
        lens = _copy_real_lens(tmp_path, "aesthetic-warburg")
        wiki = tmp_path / "wiki"
        # Page A has aat_id; Page B has nothing. No contradiction because
        # we can't compare.
        _write_page(wiki / "motifs" / "mirror-a.md",
                    {"title": "Mirror Motif", "aat_id": "aat:300186906",
                     "lens": "aesthetic-warburg"})
        _write_page(wiki / "motifs" / "mirror-b.md",
                    {"title": "Mirror Motif", "lens": "aesthetic-warburg"})
        pages = _make_pages_dict(wiki)
        issues = check_contradictions(wiki, pages, lens=lens)
        assert issues == []

    def test_different_titles_not_cross_conflated(
        self, tmp_path: Path,
    ):
        """Two pages with different titles but same authority values
        should not be flagged — same id across disjoint concepts is
        a data modeling smell but not a contradiction we detect."""
        lens = _copy_real_lens(tmp_path, "aesthetic-warburg")
        wiki = tmp_path / "wiki"
        _write_page(wiki / "motifs" / "mirror.md",
                    {"title": "Mirror", "aat_id": "aat:300186906",
                     "lens": "aesthetic-warburg"})
        _write_page(wiki / "motifs" / "reflection.md",
                    {"title": "Reflection", "aat_id": "aat:300186906",
                     "lens": "aesthetic-warburg"})
        pages = _make_pages_dict(wiki)
        issues = check_contradictions(wiki, pages, lens=lens)
        assert issues == []


# ---------------------------------------------------------------------------
# Rule B · Stale claims
# ---------------------------------------------------------------------------


class TestStaleClaims:

    def test_no_retractions_returns_empty(self, tmp_path: Path):
        wiki = tmp_path / "wiki"
        _write_page(wiki / "a.md", {"title": "A"}, body="Cites [[b]].")
        _write_page(wiki / "b.md", {"title": "B"})
        pages = _make_pages_dict(wiki)
        assert check_stale_claims(wiki, pages) == []

    def test_citing_retracted_target_flagged(self, tmp_path: Path):
        wiki = tmp_path / "wiki"
        graph = tmp_path / ".agent" / "graph"
        graph.mkdir(parents=True)
        # Retraction grammar: [[evidence]] [retracts-code] [[target]]
        (graph / "motifs.md").write_text(
            "# retractions\n\n[[new-source]] [retracts-superseded] "
            "[[old-motif]]\n",
            encoding="utf-8",
        )
        _write_page(wiki / "a.md", {"title": "A"},
                    body="The analysis relies on [[old-motif]] heavily.")
        _write_page(wiki / "old-motif.md", {"title": "Old Motif"})
        _write_page(wiki / "new-source.md", {"title": "New Source"})
        pages = _make_pages_dict(wiki)
        issues = check_stale_claims(wiki, pages)
        assert len(issues) == 1
        assert issues[0].category == "stale-claim"
        assert issues[0].level == "🟡"
        assert "old-motif" in issues[0].message

    def test_retracted_page_itself_not_warned(self, tmp_path: Path):
        """The retracted page is already acknowledged; we don't warn it
        about itself."""
        wiki = tmp_path / "wiki"
        graph = tmp_path / ".agent" / "graph"
        graph.mkdir(parents=True)
        (graph / "motifs.md").write_text(
            "[[x]] [retracts-r] [[old-motif]]\n", encoding="utf-8",
        )
        # old-motif doesn't cite itself but it is the target of retraction
        _write_page(wiki / "old-motif.md", {"title": "Old"},
                    body="Standalone content.")
        pages = _make_pages_dict(wiki)
        issues = check_stale_claims(wiki, pages)
        assert issues == []

    def test_multiple_retractions_dedup_per_page(self, tmp_path: Path):
        """If page A cites [[old]] twice, emit one warning, not two."""
        wiki = tmp_path / "wiki"
        graph = tmp_path / ".agent" / "graph"
        graph.mkdir(parents=True)
        (graph / "motifs.md").write_text(
            "[[x]] [retracts-r] [[old]]\n", encoding="utf-8",
        )
        _write_page(
            wiki / "a.md", {"title": "A"},
            body="Discusses [[old]] and [[old]] and [[old]] at length.",
        )
        _write_page(wiki / "old.md", {"title": "Old"})
        pages = _make_pages_dict(wiki)
        issues = check_stale_claims(wiki, pages)
        assert len(issues) == 1

    def test_no_agent_graph_dir_no_crash(self, tmp_path: Path):
        wiki = tmp_path / "wiki"
        _write_page(wiki / "a.md", {"title": "A"}, body="[[b]]")
        pages = _make_pages_dict(wiki)
        # No .agent/graph/ directory → no retractions → no issues
        assert check_stale_claims(wiki, pages) == []


# ---------------------------------------------------------------------------
# Rule C · Material requests
# ---------------------------------------------------------------------------


class TestMaterialRequests:

    def test_single_broken_link_not_flagged(self, tmp_path: Path):
        """A missing target with only one referrer is ordinary broken-link
        noise — below the material-gap threshold."""
        wiki = tmp_path / "wiki"
        _write_page(wiki / "a.md", {"title": "A"}, body="Cites [[missing]].")
        pages = _make_pages_dict(wiki)
        issues = check_material_requests(wiki, pages)
        assert issues == []

    def test_broken_link_in_two_pages_flagged(self, tmp_path: Path):
        """Two independent pages reaching for the same missing target =
        material gap."""
        wiki = tmp_path / "wiki"
        _write_page(wiki / "a.md", {"title": "A"},
                    body="Depends on [[missing-entity]] analysis.")
        _write_page(wiki / "b.md", {"title": "B"},
                    body="Also references [[missing-entity]].")
        pages = _make_pages_dict(wiki)
        issues = check_material_requests(wiki, pages)
        assert len(issues) == 1
        issue = issues[0]
        assert issue.category == "material-request"
        assert issue.level == "🔵"
        assert "missing-entity" in issue.message

    def test_existing_target_never_flagged(self, tmp_path: Path):
        """Wikilinks that resolve to actual pages are never material requests."""
        wiki = tmp_path / "wiki"
        _write_page(wiki / "a.md", {"title": "A"}, body="Cites [[b]]")
        _write_page(wiki / "c.md", {"title": "C"}, body="Also cites [[b]]")
        _write_page(wiki / "b.md", {"title": "B"})
        pages = _make_pages_dict(wiki)
        issues = check_material_requests(wiki, pages)
        assert issues == []

    def test_referrers_in_suggestion(self, tmp_path: Path):
        """The suggestion should list the referring pages so the user
        can triage which gap to fill first."""
        wiki = tmp_path / "wiki"
        _write_page(wiki / "a.md", {"title": "A"}, body="[[gap]]")
        _write_page(wiki / "b.md", {"title": "B"}, body="[[gap]]")
        pages = _make_pages_dict(wiki)
        issues = check_material_requests(wiki, pages)
        assert len(issues) == 1
        suggestion = issues[0].suggestion
        assert "a.md" in suggestion
        assert "b.md" in suggestion

    def test_many_referrers_summarized(self, tmp_path: Path):
        """When > 3 pages reference a gap, suggestion caps sample at 3
        and notes the overflow to keep lint output readable."""
        wiki = tmp_path / "wiki"
        for name in ["a", "b", "c", "d", "e"]:
            _write_page(wiki / f"{name}.md",
                        {"title": name.upper()}, body="[[popular-gap]]")
        pages = _make_pages_dict(wiki)
        issues = check_material_requests(wiki, pages)
        assert len(issues) == 1
        suggestion = issues[0].suggestion
        assert "and 2 more" in suggestion
