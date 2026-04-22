"""Validates .agent/spec/gap-algorithm.md structural invariants."""
from pathlib import Path


REQUIRED_SECTIONS = [
    "## 1. Inputs",
    "## 2. Pre-pass: Retraction Resolution",
    "## 3. Tier 1 Clustering",
    "## 4. Tier 2 Clustering",
    "## 5. Gap Discovery",
    "## 6. LLM Validation Layer",
    "## 7. Reproducibility Contract",
    "## 8. Performance Envelope",
    "## 9. Test Commitments",
]


def test_gap_spec_exists(gap_spec_path: Path):
    assert gap_spec_path.exists(), f"{gap_spec_path} missing"


def test_gap_spec_has_all_sections(gap_spec_path: Path):
    text = gap_spec_path.read_text(encoding="utf-8")
    for section in REQUIRED_SECTIONS:
        assert section in text, f"gap-algorithm.md missing section: {section}"


def test_gap_spec_names_leiden(gap_spec_path: Path):
    text = gap_spec_path.read_text(encoding="utf-8")
    assert "Leiden" in text, "gap-algorithm.md must name Leiden as clustering method"


def test_gap_spec_names_jaccard(gap_spec_path: Path):
    text = gap_spec_path.read_text(encoding="utf-8")
    assert "Jaccard" in text, "gap-algorithm.md must name Jaccard projection"


def test_gap_spec_defines_adaptive_threshold(gap_spec_path: Path):
    text = gap_spec_path.read_text(encoding="utf-8")
    assert "max{3, ⌈log₂" in text or "log₂" in text, (
        "gap-algorithm.md must define adaptive threshold formula"
    )


def test_gap_spec_defines_retraction_protocol(gap_spec_path: Path):
    text = gap_spec_path.read_text(encoding="utf-8")
    assert "retracts-" in text, "gap-algorithm.md must define retraction protocol"


def test_gap_spec_defines_tier2_gating(gap_spec_path: Path):
    text = gap_spec_path.read_text(encoding="utf-8")
    assert "15" in text and "pathosformel" in text, (
        "gap-algorithm.md must define tier 2 activation condition (|pathosformel| ≥ 15)"
    )
