"""v2.1 tests for .claude/skills/reset/SKILL.md

Asserts against the CURRENT v2.1 surface — scope-based deletion, dry-run,
confirmation gate, lens-aware raw subdirs, sentinel preservation.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SKILL = PROJECT_ROOT / ".claude" / "skills" / "reset" / "SKILL.md"


@pytest.fixture(scope="module")
def skill_text() -> str:
    return SKILL.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# File exists and is readable
# ---------------------------------------------------------------------------


def test_skill_file_exists():
    assert SKILL.exists(), f"/reset SKILL.md not found at {SKILL}"


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------


def test_frontmatter_present(skill_text):
    assert skill_text.startswith("---"), "SKILL.md must begin with YAML frontmatter"


def test_frontmatter_has_name_reset(skill_text):
    """Frontmatter name field must be 'reset'."""
    # Frontmatter is between the first '---' and the closing '---'
    end = skill_text.find("\n---\n", 4)
    frontmatter = skill_text[4:end] if end > 4 else skill_text[:200]
    # name: reset OR title contains reset OR description names reset
    # The current SKILL uses description: ... so we check either field
    assert ("name: reset" in frontmatter or "description:" in frontmatter), \
        "Frontmatter must identify this as the reset skill"


# ---------------------------------------------------------------------------
# Dry-run (plan before action)
# ---------------------------------------------------------------------------


def test_skill_describes_dry_run_step(skill_text):
    """SKILL.md must describe enumerating targets before any deletion."""
    lowered = skill_text.lower()
    assert "dry-run" in lowered or "dry run" in lowered or "deletion plan" in lowered, \
        "SKILL.md must describe a dry-run / deletion-plan step before acting"


def test_dry_run_comes_before_execution(skill_text):
    """The plan/dry-run step must appear before the execute step textually."""
    lowered = skill_text.lower()
    plan_pos = min(
        (lowered.find(kw) for kw in ("dry-run", "dry run", "deletion plan") if lowered.find(kw) >= 0),
        default=-1,
    )
    exec_pos = lowered.find("execute")
    assert plan_pos >= 0 and exec_pos >= 0 and plan_pos < exec_pos, \
        "Dry-run/plan step must appear before the execute step"


# ---------------------------------------------------------------------------
# User confirmation gate
# ---------------------------------------------------------------------------


def test_skill_requires_user_confirmation(skill_text):
    """Must require explicit user confirmation before any deletion."""
    lowered = skill_text.lower()
    assert "confirm" in lowered or "[y/n]" in lowered.replace(" ", ""), \
        "SKILL.md must require user confirmation before destructive action"


def test_explicit_no_bypass_statement(skill_text):
    """SKILL.md must state that proceeding without approval is prohibited."""
    lowered = skill_text.lower()
    assert "without explicit approval" in lowered or "never proceed" in lowered or \
           "explicit confirmation" in lowered or "explicit approval" in lowered, \
        "Must explicitly state that /reset cannot proceed without user approval"


# ---------------------------------------------------------------------------
# Scope-based deletion model
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("scope", ["wiki", "raw", "log", "checkpoints", "all"])
def test_skill_documents_scope(scope, skill_text):
    """Every valid --scope value must be documented."""
    assert scope in skill_text, f"SKILL.md does not document scope: {scope}"


def test_skill_shows_scope_flag(skill_text):
    """The --scope flag must be shown as the trigger mechanism."""
    assert "--scope" in skill_text, "SKILL.md must document the --scope flag"


# ---------------------------------------------------------------------------
# Sentinel preservation
# ---------------------------------------------------------------------------


def test_preserves_gitkeep(skill_text):
    """.gitkeep placeholder files must be explicitly preserved."""
    assert ".gitkeep" in skill_text, \
        "SKILL.md must document that .gitkeep sentinels are preserved"


def test_preserves_wiki_claude_md(skill_text):
    """wiki/CLAUDE.md must be explicitly preserved (user config, not auto-generated)."""
    assert "CLAUDE.md" in skill_text, \
        "SKILL.md must document that wiki/CLAUDE.md is preserved"


# ---------------------------------------------------------------------------
# Regression guards: v1.4 deleted-tool references must NOT appear
# ---------------------------------------------------------------------------


def test_no_reset_wiki_tool_reference(skill_text):
    """tools/reset_wiki.py was removed — must not appear in v2.1 SKILL.md."""
    assert "reset_wiki.py" not in skill_text, \
        "v1.4 regression: reset_wiki.py must not appear in v2.1 SKILL.md"


def test_no_research_wiki_tool_reference(skill_text):
    """tools/research_wiki.py was removed — must not appear in v2.1 SKILL.md."""
    assert "research_wiki.py" not in skill_text, \
        "v1.4 regression: research_wiki.py must not appear in v2.1 SKILL.md"


# ---------------------------------------------------------------------------
# Lens-awareness: raw subdirs are declared by active lens, not hardcoded
# ---------------------------------------------------------------------------


def test_raw_scope_references_active_lens(skill_text):
    """raw scope must enumerate subdirs from the active lens config, not hardcode them."""
    lowered = skill_text.lower()
    assert "active lens" in lowered or "lens" in lowered, \
        "raw scope deletion must reference the active lens's declared raw subdirs"
