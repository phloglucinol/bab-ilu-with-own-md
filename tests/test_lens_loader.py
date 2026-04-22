"""Tests for tools.lens_loader — discovery, validation, activation."""

from __future__ import annotations

import dataclasses
import json
import shutil
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.lens_loader import (  # noqa: E402
    LensConfig,
    LensValidationError,
    activate_for_file,
    load_all_lenses,
    load_lens,
)

LENSES_BASE = REPO_ROOT / ".agent" / "lenses"


def _copy_lens_base(tmp_path: Path) -> Path:
    """Copy .agent/lenses/ into tmp_path so tests that mutate cannot
    pollute the real workspace."""
    dest = tmp_path / "lenses"
    shutil.copytree(LENSES_BASE, dest)
    return dest


def test_load_aesthetic_warburg_lens():
    cfg = load_lens("aesthetic-warburg", base=LENSES_BASE)
    assert isinstance(cfg, LensConfig)
    assert cfg.id == "aesthetic-warburg"
    assert cfg.entity_model["tier_0"] == "aesthetic"
    assert cfg.entity_model["tier_1_atom"] == "motif"
    assert cfg.entity_model["tier_1_cluster"] == "panel"
    assert "aesthetic" in cfg.deliverable_types
    assert cfg.version.count(".") == 2  # semver


def test_load_all_lenses():
    lenses = load_all_lenses(base=LENSES_BASE)
    assert isinstance(lenses, dict)
    assert "aesthetic-warburg" in lenses
    assert len(lenses) >= 1
    for lens_id, cfg in lenses.items():
        assert cfg.id == lens_id


def test_missing_lens_raises():
    with pytest.raises(FileNotFoundError):
        load_lens("definitely-not-a-lens", base=LENSES_BASE)


def test_invalid_schema_raises_lens_validation_error(tmp_path: Path):
    base = _copy_lens_base(tmp_path)
    bad_dir = base / "broken-lens"
    bad_dir.mkdir()
    # Missing required field `id`.
    (bad_dir / "lens.yaml").write_text(
        "version: 1.0.0\n"
        "name: broken\n"
        "description: missing id\n"
        "deliverable_types: [thing]\n"
        "entity_model:\n"
        "  tier_0: thing\n"
        "  tier_1_atom: subthing\n"
        "  tier_1_cluster: cluster\n"
        "activation:\n"
        "  mode: always\n"
        "analysis_contract:\n"
        "  taste: [x]\n",
        encoding="utf-8",
    )
    with pytest.raises(LensValidationError) as exc_info:
        load_lens("broken-lens", base=base)
    assert "id" in str(exc_info.value).lower()


def test_defaults_applied_when_thresholds_missing(tmp_path: Path):
    base = _copy_lens_base(tmp_path)
    minimal_dir = base / "minimal-lens"
    minimal_dir.mkdir()
    (minimal_dir / "lens.yaml").write_text(
        "id: minimal-lens\n"
        "version: 0.1.0\n"
        "name: Minimal\n"
        "description: no thresholds set\n"
        "deliverable_types: [thing]\n"
        "entity_model:\n"
        "  tier_0: thing\n"
        "  tier_1_atom: subthing\n"
        "  tier_1_cluster: cluster\n"
        "activation:\n"
        "  mode: always\n"
        "analysis_contract:\n"
        "  taste: [count]\n",
        encoding="utf-8",
    )
    cfg = load_lens("minimal-lens", base=base)
    assert cfg.thresholds["cluster_member_min"] == 3
    assert cfg.thresholds["density_multiplier"] == 3.0
    assert cfg.thresholds["domain_min"] == 5
    assert cfg.community_detection["algorithm"] == "louvain"
    assert cfg.community_detection["resolution"] == 1.0


def test_activate_for_file_always_mode(tmp_path: Path):
    base = _copy_lens_base(tmp_path)
    always_dir = base / "always-lens"
    always_dir.mkdir()
    (always_dir / "lens.yaml").write_text(
        "id: always-lens\n"
        "version: 0.1.0\n"
        "name: Always\n"
        "description: always on\n"
        "deliverable_types: [thing]\n"
        "entity_model:\n"
        "  tier_0: thing\n"
        "  tier_1_atom: subthing\n"
        "  tier_1_cluster: cluster\n"
        "activation:\n"
        "  mode: always\n"
        "analysis_contract:\n"
        "  taste: [count]\n",
        encoding="utf-8",
    )
    lenses = load_all_lenses(base=base)
    ids = activate_for_file("some random prose", {}, lenses)
    assert "always-lens" in ids


def test_activate_for_file_triggers_mode():
    """aesthetic-warburg uses AND over two triggers:
    `|aesthetic| >= 1` AND `|motif| >= 2`. Both must fire.
    Loader matches the literal slug inside `[[...]]` / `#...` / frontmatter,
    not type-class membership."""
    lenses = load_all_lenses(base=LENSES_BASE)
    cfg = lenses["aesthetic-warburg"]
    assert cfg.activation["mode"] == "triggers"

    # Both triggers satisfied: 1 aesthetic tag + 2 motif tags.
    content_yes = "#aesthetic discusses #motif and another #motif reference"
    assert "aesthetic-warburg" in activate_for_file(content_yes, {}, lenses)

    # Only motifs, no aesthetic slug → first trigger fails → not active.
    content_no = "[[motif]] [[motif]] without aesthetic tag"
    assert "aesthetic-warburg" not in activate_for_file(content_no, {}, lenses)

    # Only aesthetic tag, <2 motifs → second trigger fails.
    content_half = "#aesthetic [[motif]] alone"
    assert "aesthetic-warburg" not in activate_for_file(content_half, {}, lenses)


def test_activate_for_file_multiple_triggers_and(tmp_path: Path):
    base = _copy_lens_base(tmp_path)
    multi_dir = base / "multi-trig"
    multi_dir.mkdir()
    (multi_dir / "lens.yaml").write_text(
        "id: multi-trig\n"
        "version: 0.1.0\n"
        "name: Multi\n"
        "description: AND triggers\n"
        "deliverable_types: [thing]\n"
        "entity_model:\n"
        "  tier_0: thing\n"
        "  tier_1_atom: subthing\n"
        "  tier_1_cluster: cluster\n"
        "activation:\n"
        "  mode: triggers\n"
        "  triggers:\n"
        '    - "|alpha| >= 1"\n'
        '    - "|beta| >= 1"\n'
        "analysis_contract:\n"
        "  taste: [count]\n",
        encoding="utf-8",
    )
    lenses = load_all_lenses(base=base)
    both = "[[alpha]] and [[beta]]"
    only_alpha = "just [[alpha]] here"
    assert "multi-trig" in activate_for_file(both, {}, lenses)
    assert "multi-trig" not in activate_for_file(only_alpha, {}, lenses)


def test_source_path_preserved():
    cfg = load_lens("aesthetic-warburg", base=LENSES_BASE)
    assert cfg.source_path.is_absolute()
    assert cfg.source_path.name == "lens.yaml"
    assert cfg.source_path.parent.name == "aesthetic-warburg"


def test_frozen_dataclass():
    cfg = load_lens("aesthetic-warburg", base=LENSES_BASE)
    with pytest.raises(dataclasses.FrozenInstanceError):
        cfg.id = "changed"  # type: ignore[misc]
