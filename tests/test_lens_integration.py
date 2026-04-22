"""End-to-end integration: B1 schema × B2 loader × C1 aesthetic-warburg lens.yaml.

This test proves the v2.1 lens stack reads real content correctly:

    .agent/lenses/schema.json  (B1)
          │
          ▼
    tools/lens_loader.py       (B2)  — schema-validates every lens.yaml
          │
          ▼
    .agent/lenses/aesthetic-warburg/lens.yaml  (C1 — migrated v2.0 rules)

Kept small and fast: no NetworkX, no seed-kit walking. Just confirms that
a consumer (e.g. future /taste, /gap, /ingest) can `load_lens("aesthetic-warburg")`
and get a usable, immutable config.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from tools.lens_loader import (
    LensConfig,
    LensValidationError,
    activate_for_file,
    load_all_lenses,
    load_lens,
)

REPO_ROOT = Path(__file__).parent.parent
LENSES_DIR = REPO_ROOT / ".agent" / "lenses"


def test_aesthetic_warburg_lens_yaml_loads():
    cfg = load_lens("aesthetic-warburg", base=LENSES_DIR)
    assert isinstance(cfg, LensConfig)
    assert cfg.id == "aesthetic-warburg"
    assert cfg.version == "1.0.0"


def test_aesthetic_warburg_entity_model_is_tri_tiered():
    cfg = load_lens("aesthetic-warburg", base=LENSES_DIR)
    assert cfg.entity_model["tier_0"] == "aesthetic"
    assert cfg.entity_model["tier_1_atom"] == "motif"
    assert cfg.entity_model["tier_1_cluster"] == "panel"


def test_aesthetic_warburg_thresholds_match_v2_defaults():
    cfg = load_lens("aesthetic-warburg", base=LENSES_DIR)
    assert cfg.thresholds["cluster_member_min"] == 3
    assert cfg.thresholds["cluster_min_size"] == 3
    assert cfg.thresholds["density_multiplier"] == pytest.approx(3.0)


def test_aesthetic_warburg_community_detection_is_louvain():
    cfg = load_lens("aesthetic-warburg", base=LENSES_DIR)
    assert cfg.community_detection["algorithm"] == "louvain"


def test_aesthetic_warburg_allowed_subdomains_include_v2_list():
    cfg = load_lens("aesthetic-warburg", base=LENSES_DIR)
    for expected in ("cinema", "photo", "painting", "architecture"):
        assert expected in cfg.allowed_subdomains


def test_load_all_discovers_aesthetic_warburg():
    lenses = load_all_lenses(base=LENSES_DIR)
    assert "aesthetic-warburg" in lenses


def test_pathosformel_shaped_file_activates_lens():
    """A file tagged #aesthetic AND citing 2+ motif slugs activates the lens."""
    lenses = load_all_lenses(base=LENSES_DIR)
    fm = {"type": "pathosformel", "tags": ["aesthetic", "motif"]}
    content = (
        "#aesthetic\n"
        "[[motif]] of quiet interior light binds "
        "[[motif]] sublime-solitude-landscape.\n"
    )
    active = activate_for_file(content, fm, lenses)
    assert "aesthetic-warburg" in active


def test_plain_note_does_not_activate_lens():
    lenses = load_all_lenses(base=LENSES_DIR)
    fm = {"type": "note"}
    content = "Random note on build systems. No aesthetic or motif refs."
    active = activate_for_file(content, fm, lenses)
    assert active == []


def test_aesthetic_work_alone_does_not_activate():
    """A work file (tier-0) that tags #aesthetic once but cites 0 motifs
    must NOT activate: AND semantics require BOTH triggers."""
    lenses = load_all_lenses(base=LENSES_DIR)
    fm = {"type": "work", "tags": ["aesthetic"]}
    content = "#aesthetic\n[[caspar-david-friedrich]] painted this work."
    active = activate_for_file(content, fm, lenses)
    assert "aesthetic-warburg" not in active


def test_lens_yaml_id_matches_directory():
    """Loader already enforces this, but pin it as a C1 invariant."""
    cfg = load_lens("aesthetic-warburg", base=LENSES_DIR)
    assert cfg.source_path.parent.name == cfg.id


def test_lens_config_is_immutable():
    """Wrapping via MappingProxyType (B2-fix sha 7826621) must hold
    at the C1 integration boundary too."""
    cfg = load_lens("aesthetic-warburg", base=LENSES_DIR)
    with pytest.raises(TypeError):
        cfg.thresholds["cluster_member_min"] = 99  # type: ignore[index]


def test_invalid_lens_id_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_lens("nonexistent-lens", base=LENSES_DIR)
