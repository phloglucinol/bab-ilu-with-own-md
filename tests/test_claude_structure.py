"""Validates CLAUDE.md v2.1 structural invariants."""
from pathlib import Path


def test_claude_md_exists(claude_md_path: Path):
    assert claude_md_path.exists(), f"{claude_md_path} missing"


def test_claude_md_under_180_lines(claude_md_path: Path):
    # v2.1 raised the ceiling from 100 → 180 to accommodate §0 theoretical
    # foundation preamble (synced from PRD-v2.1-zh.md §0.5). The §0 block
    # is a hard constraint per PRD §0.5.5 and cannot be trimmed without
    # re-aligning cybernetics + late Wittgenstein theoretical bases.
    lines = claude_md_path.read_text(encoding="utf-8").splitlines()
    assert len(lines) <= 180, f"CLAUDE.md has {len(lines)} lines, must be ≤180"


def test_claude_md_has_vault_language_reference(claude_md_path: Path):
    text = claude_md_path.read_text(encoding="utf-8")
    assert "vault_language" in text, "CLAUDE.md must reference vault_language"


def test_claude_md_lists_eight_commands(claude_md_path: Path):
    text = claude_md_path.read_text(encoding="utf-8")
    commands = [
        "/genesis",
        "/ingest",
        "/taste",
        "/gap",
        "/ask",
        "/prompt",
        "/distill",
        "/lint",
    ]
    for cmd in commands:
        assert cmd in text, f"CLAUDE.md missing command: {cmd}"


def test_claude_md_has_hard_rules_section(claude_md_path: Path):
    text = claude_md_path.read_text(encoding="utf-8")
    assert "Hard Rules" in text, "CLAUDE.md must have Hard Rules section"


def test_claude_md_has_three_layer_architecture(claude_md_path: Path):
    text = claude_md_path.read_text(encoding="utf-8")
    for dirname in ("raw/", "wiki/", ".agent/"):
        assert dirname in text, f"CLAUDE.md must mention layer directory: {dirname}"
