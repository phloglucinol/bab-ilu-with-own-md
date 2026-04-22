"""Tests for tools/note_extractor.py.

Six tests covering the note-extractor contract:

1. URL input  → wiki/note/<slug>.md, kind=article, source_url set
2. PDF input  → kind=paper, source_path set
3. Markdown   → kind=other, source_path set
4. Collision  → existing user content + force=False returns (None, "exists-user-content")
5. Force      → existing user content + force=True overwrites
6. Bad vault  → non-existent vault returns (None, error_msg)

Architecture: no LLM, no HTTP. All deterministic.
"""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from tools.note_extractor import AGENT_MARKER, LENS_ID, run_note_extractor


# ---------------------------------------------------------------------------
# Fake lens fixture matching general-zettelkasten entity_model
# ---------------------------------------------------------------------------


class FakeZettelLens:
    """Minimal LensConfig stand-in for general-zettelkasten."""

    def __init__(self) -> None:
        self.id = LENS_ID
        self.entity_model = {
            "tier_0": "note",
            "tier_1_atom": "concept",
            "tier_1_cluster": "concept-cluster",
        }
        self.anchors = None  # zettelkasten has no authority_fields


@pytest.fixture
def lens() -> FakeZettelLens:
    return FakeZettelLens()


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    """Create a minimal vault directory."""
    (tmp_path / "wiki").mkdir()
    return tmp_path


# ---------------------------------------------------------------------------
# Helper: parse frontmatter from written file
# ---------------------------------------------------------------------------


def _read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), "file has no frontmatter"
    end = text.find("\n---\n", 4)
    assert end > 0, "frontmatter closing --- not found"
    return yaml.safe_load(text[4:end]) or {}


# ---------------------------------------------------------------------------
# Test 1: URL input → article kind + source_url
# ---------------------------------------------------------------------------


class TestURLInput:
    def test_url_writes_article_kind_and_source_url(self, vault, lens):
        url = "https://example.com/blog/some-post"
        output_path, err = run_note_extractor(vault, lens, url, "url")

        assert err is None
        assert output_path is not None
        assert output_path.exists()

        # Path should be wiki/note/<slug>.md
        assert output_path.parent == vault / "wiki" / "note"
        assert output_path.suffix == ".md"

        fm = _read_frontmatter(output_path)
        assert fm["kind"] == "article"
        assert fm["source_url"] == url
        assert "source_path" not in fm
        assert fm["lens"] == LENS_ID
        assert fm["bloom"] is None
        assert fm["concepts"] == []
        assert fm["layer_1_bolds"] == []
        assert fm["layer_2_fragments"] == []
        assert fm["layer_3_thesis"] is None

        # Body contains agent marker and TODO template sections
        body = output_path.read_text(encoding="utf-8")
        assert AGENT_MARKER in body
        assert "## Layer 1 — bold key sentences" in body
        assert "## Layer 2 — bold fragments" in body
        assert "## Layer 3 — one-sentence thesis" in body
        assert "## Concepts (tier_1_atoms)" in body
        assert "## Back-references" in body


# ---------------------------------------------------------------------------
# Test 2: PDF input → paper kind + source_path
# ---------------------------------------------------------------------------


class TestPDFInput:
    def test_pdf_writes_paper_kind_and_source_path(self, vault, lens):
        path = "/research/papers/ahrens-smart-notes.pdf"
        output_path, err = run_note_extractor(vault, lens, path, "pdf")

        assert err is None
        assert output_path is not None

        fm = _read_frontmatter(output_path)
        assert fm["kind"] == "paper"
        assert fm["source_path"] == path
        assert "source_url" not in fm


# ---------------------------------------------------------------------------
# Test 3: Markdown input → other kind + source_path
# ---------------------------------------------------------------------------


class TestMarkdownInput:
    def test_markdown_writes_other_kind_and_source_path(self, vault, lens):
        md_path = "/notes/fleeting/observation.md"
        output_path, err = run_note_extractor(vault, lens, md_path, "markdown")

        assert err is None
        assert output_path is not None

        fm = _read_frontmatter(output_path)
        assert fm["kind"] == "other"
        assert fm["source_path"] == md_path
        assert "source_url" not in fm


# ---------------------------------------------------------------------------
# Test 4: Slug collision with user content + force=False
# ---------------------------------------------------------------------------


class TestSlugCollisionNoForce:
    def test_existing_user_content_returns_none_and_error(self, vault, lens):
        # Pre-create the target file with user content (no AGENT_MARKER).
        (vault / "wiki" / "note").mkdir(parents=True, exist_ok=True)
        url = "https://example.com/blog/some-post"
        # derive the slug the same way the extractor does
        from tools.note_extractor import _slug_from_input
        slug = _slug_from_input(url)
        target = vault / "wiki" / "note" / f"{slug}.md"
        target.write_text("# Hand-authored note\n\nUser content here.", encoding="utf-8")

        output_path, err = run_note_extractor(vault, lens, url, "url", force=False)

        assert output_path is None
        assert err == "exists-user-content"
        # User content must be preserved exactly.
        assert target.read_text(encoding="utf-8") == "# Hand-authored note\n\nUser content here."


# ---------------------------------------------------------------------------
# Test 5: Force overwrite of user content
# ---------------------------------------------------------------------------


class TestForceOverwrite:
    def test_force_true_overwrites_user_content(self, vault, lens):
        (vault / "wiki" / "note").mkdir(parents=True, exist_ok=True)
        url = "https://example.com/blog/some-post"
        from tools.note_extractor import _slug_from_input
        slug = _slug_from_input(url)
        target = vault / "wiki" / "note" / f"{slug}.md"
        target.write_text("# Old user note", encoding="utf-8")

        output_path, err = run_note_extractor(vault, lens, url, "url", force=True)

        assert err is None
        assert output_path is not None
        assert output_path == target
        # File should now be the extractor stub, not the old user content.
        body = target.read_text(encoding="utf-8")
        assert AGENT_MARKER in body
        assert "# Old user note" not in body


# ---------------------------------------------------------------------------
# Test 6: Non-existent vault → error, no crash
# ---------------------------------------------------------------------------


class TestNonExistentVault:
    def test_nonexistent_vault_returns_error(self, tmp_path, lens):
        bad_vault = tmp_path / "does-not-exist"
        # Do NOT create bad_vault — it must not exist.

        output_path, err = run_note_extractor(
            bad_vault, lens, "https://example.com/x", "url"
        )

        assert output_path is None
        assert err is not None
        assert "does not exist" in err.lower() or "vault" in err.lower()
