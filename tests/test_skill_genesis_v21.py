"""v2.1 tests for .claude/skills/genesis/SKILL.md

Asserts against the CURRENT v2.1 surface — lens-aware scaffolding, three-layer
structure, entity_model tier bindings, idempotency, no v1.4 artifacts.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SKILL = PROJECT_ROOT / ".claude" / "skills" / "genesis" / "SKILL.md"
LENSES_DIR = PROJECT_ROOT / ".agent" / "lenses"


@pytest.fixture(scope="module")
def skill_text() -> str:
    return SKILL.read_text(encoding="utf-8")


def _load_lens(lens_id: str) -> dict:
    """Load a lens.yaml as a dict."""
    path = LENSES_DIR / lens_id / "lens.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# File exists and is readable
# ---------------------------------------------------------------------------


def test_skill_file_exists():
    assert SKILL.exists(), f"/genesis SKILL.md not found at {SKILL}"


# ---------------------------------------------------------------------------
# Frontmatter with name: genesis
# ---------------------------------------------------------------------------


def test_frontmatter_present(skill_text):
    assert skill_text.startswith("---"), "SKILL.md must begin with YAML frontmatter"


def test_frontmatter_has_name_genesis(skill_text):
    """Frontmatter name field must be 'genesis'."""
    end = skill_text.find("\n---\n", 4)
    frontmatter = skill_text[4:end] if end > 4 else skill_text[:300]
    assert "name: genesis" in frontmatter, \
        "Frontmatter must include 'name: genesis'"


def test_frontmatter_has_allowed_tools(skill_text):
    """Frontmatter should list allowed-tools so Claude Code gates tool use."""
    assert "allowed-tools:" in skill_text, \
        "Frontmatter should declare 'allowed-tools:'"


# ---------------------------------------------------------------------------
# Three-layer scaffolding: raw/ wiki/ .agent/
# ---------------------------------------------------------------------------


def test_scaffolds_raw_layer(skill_text):
    assert "raw/" in skill_text, "SKILL.md must describe scaffolding raw/"


def test_scaffolds_wiki_layer(skill_text):
    assert "wiki/" in skill_text, "SKILL.md must describe scaffolding wiki/"


def test_scaffolds_agent_layer(skill_text):
    assert ".agent/" in skill_text, "SKILL.md must describe scaffolding .agent/"


# ---------------------------------------------------------------------------
# Lens-awareness: reads from entity_model, not hardcoded paths
# ---------------------------------------------------------------------------


def test_references_tier_0_from_entity_model(skill_text):
    """SKILL.md must reference entity_model.tier_0 dynamically, not hardcode."""
    assert "tier_0" in skill_text, \
        "SKILL.md must reference entity_model.tier_0 from the active lens"


def test_references_tier_1_atom_from_entity_model(skill_text):
    assert "tier_1_atom" in skill_text, \
        "SKILL.md must reference entity_model.tier_1_atom from the active lens"


def test_references_tier_1_cluster_from_entity_model(skill_text):
    assert "tier_1_cluster" in skill_text, \
        "SKILL.md must reference entity_model.tier_1_cluster from the active lens"


def test_references_lens_loader(skill_text):
    """genesis must use lens_loader (or equivalent) to validate the chosen lens."""
    assert "lens_loader" in skill_text or "lens.yaml" in skill_text, \
        "SKILL.md must reference lens_loader or lens.yaml for lens validation"


# ---------------------------------------------------------------------------
# Lens-specific wiki subdirectories — entity_model contract
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("lens_id,expected_dir", [
    ("aesthetic-warburg", "motif"),        # tier_1_atom
    ("aesthetic-warburg", "panel"),        # tier_1_cluster
    ("engineering-alexander", "incident"), # tier_0
    ("engineering-alexander", "pattern"),  # tier_1_atom
    ("general-zettelkasten", "note"),      # tier_0
    ("general-zettelkasten", "concept"),   # tier_1_atom
])
def test_skill_mentions_lens_specific_entity(lens_id, expected_dir, skill_text):
    """Each launch-lens entity directory must be mentioned in SKILL.md examples."""
    assert expected_dir in skill_text, \
        f"SKILL.md must mention '{expected_dir}' (from lens {lens_id} entity_model)"


def test_lens_entity_model_matches_yaml(tmp_path):
    """entity_model in every lens.yaml must have all three tier keys."""
    for lens_id in ("aesthetic-warburg", "engineering-alexander", "general-zettelkasten"):
        cfg = _load_lens(lens_id)
        em = cfg.get("entity_model", {})
        assert "tier_0" in em, f"{lens_id}: entity_model missing tier_0"
        assert "tier_1_atom" in em, f"{lens_id}: entity_model missing tier_1_atom"
        assert "tier_1_cluster" in em, f"{lens_id}: entity_model missing tier_1_cluster"


# ---------------------------------------------------------------------------
# Regression guard: raw/papers/ must NOT be created
# ---------------------------------------------------------------------------


def test_no_raw_papers_directory_created(skill_text):
    """raw/papers/ was the v1.4 store — genesis must not create it."""
    # Exclude occurrences inside comments or headings that warn against it
    # A direct match inside a code block or mkdir call is the red flag
    # We look for `raw/papers` as a path being created (mkdir, touch, etc.)
    # Simple approach: it must not appear at all in the skill
    assert "raw/papers" not in skill_text, \
        "v1.4 regression: genesis must not reference raw/papers/"


# ---------------------------------------------------------------------------
# Idempotency contract
# ---------------------------------------------------------------------------


def test_describes_idempotency(skill_text):
    """genesis must document its idempotency guarantee."""
    lowered = skill_text.lower()
    assert "idempotent" in lowered or "safe to re-run" in lowered or "already exists" in lowered, \
        "SKILL.md must document the idempotency contract"


# ---------------------------------------------------------------------------
# Active lens activation
# ---------------------------------------------------------------------------


def test_describes_active_lens_copy(skill_text):
    """genesis must copy chosen lens config into .agent/lenses/active/."""
    assert "active" in skill_text, \
        "SKILL.md must describe copying the chosen lens to .agent/lenses/active/"


def test_describes_lens_context_injection(skill_text):
    """genesis must reference the B3 lens-context preamble injection."""
    lowered = skill_text.lower()
    assert "lens_context" in lowered or "preamble" in lowered or "prompts.md" in lowered, \
        "SKILL.md must describe the lens-context preamble injection (B3 protocol)"
