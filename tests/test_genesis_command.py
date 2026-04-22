"""Structural tests for the v2.1 lens-aware /genesis skill.

The genesis skill lives at `.claude/skills/genesis/SKILL.md` as an
LLM-executed markdown directive. These tests verify structural contract
points: the 5-question flow, lens-awareness, and the three launch lenses
are all mentioned. No runtime execution is tested — /genesis is invoked by
Claude Code against the live filesystem."""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
GENESIS_PATH = REPO_ROOT / ".claude" / "skills" / "genesis" / "SKILL.md"


@pytest.fixture(scope="module")
def genesis_text() -> str:
    assert GENESIS_PATH.exists(), f"genesis skill not found at {GENESIS_PATH}"
    return GENESIS_PATH.read_text(encoding="utf-8")


def test_genesis_command_file_exists():
    """The skill file must be present at the canonical location."""
    assert GENESIS_PATH.exists()


def test_genesis_command_references_lens_discovery(genesis_text: str):
    """The skill must demonstrate lens discovery/validation awareness."""
    markers = [
        ".agent/lenses",
        "lens.yaml",
        "lens_loader",
    ]
    hits = [m for m in markers if m in genesis_text]
    assert len(hits) >= 2, (
        f"expected >=2 lens-discovery markers, found {hits}"
    )


def test_genesis_command_covers_three_lenses(genesis_text: str):
    """All three launch lenses must be named so users see them in the menu."""
    assert "aesthetic-warburg" in genesis_text
    assert "engineering-alexander" in genesis_text
    # Accept `general-zettelkasten` or the `-bloom` variant per PRD §8.1.
    assert (
        "general-zettelkasten-bloom" in genesis_text
        or "general-zettelkasten" in genesis_text
    )


def test_genesis_command_frontmatter_keys(genesis_text: str):
    """Documented CLAUDE.md persistence block must carry the 4 answer keys."""
    for key in ("vault_language:", "vault_lens:", "vault_subdomain:", "seeded:"):
        assert key in genesis_text, f"missing persisted key: {key}"


def test_genesis_command_not_hardcoded_aesthetic_only(genesis_text: str):
    """The skill must NOT treat aesthetic as the only choice. It must branch
    the wiki/ scaffolding by lens or show a menu.

    Names the singular canonical `tier_0` / `tier_1_atom` / `tier_1_cluster`
    directory names that /ingest actually writes to (per each lens's
    `lens.entity_model`). Prior revisions of this test asserted pluralised
    + subdomained forms (incidents/, patterns/, notes/) which matched a
    v1.4-era genesis draft that conflicted with every code path that
    writes tier-0 content — round-4 audit flagged the drift."""
    # engineering-alexander evidence:
    assert "engineering-alexander" in genesis_text
    assert "incident" in genesis_text  # singular tier_0 name
    assert "pattern" in genesis_text   # singular tier_1_atom name
    # general-zettelkasten evidence:
    assert "general-zettelkasten" in genesis_text
    assert "note" in genesis_text      # singular tier_0 name
    assert "concept" in genesis_text   # singular tier_1_atom name


def test_genesis_command_five_question_flow(genesis_text: str):
    """PRD §3.1 requires exactly 5 interactive questions."""
    q_markers = [
        "Vault main language",
        "Vault lens",
        "Work subdomain",
        "seed kit",
        "raw material",
    ]
    hits = [m for m in q_markers if m in genesis_text]
    assert len(hits) == 5, (
        f"expected all 5 question markers, found: {hits}"
    )


def test_genesis_command_cli_flags(genesis_text: str):
    """Must document --lens=<id>, --seeded, --no-seeds flags."""
    assert "--lens=" in genesis_text
    assert "--seeded" in genesis_text
    assert "--no-seeds" in genesis_text
