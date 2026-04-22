"""Tests for tools/prompt_tester.py — G1 Sprint 4 lens-guard only.

The body of prompt_tester.py is v1.4-era code (vault directory walking,
gen_client integration, vision scoring). Sprint 4 G1 only adds the
aesthetic-lens guard at `main()` — per PRD §0.5.4 and the module
docstring, the v2.1 adaptation of the body defers to Sprint 5.

These tests validate the narrow slice that landed:
  - guard exits 2 with clear message on non-aesthetic vaults
  - guard accepts aesthetic vaults without error

Integration tests that actually generate images or score vision responses
need a real aesthetic v2.1 vault + gen_client credentials and belong to
a later Sprint 5 suite.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROMPT_TESTER = PROJECT_ROOT / "tools" / "prompt_tester.py"


def _seed_active_lens(vault: Path, lens_id: str) -> None:
    active = vault / ".agent" / "lenses" / "active"
    active.mkdir(parents=True, exist_ok=True)
    (active / "lens.yaml").write_text(f"id: {lens_id}\n", encoding="utf-8")


class TestLensGuard:

    def test_non_aesthetic_vault_exits_with_error(self, tmp_path: Path):
        """Running under engineering-alexander must exit 2 with diagnostic."""
        _seed_active_lens(tmp_path, "engineering-alexander")
        proc = subprocess.run(
            [sys.executable, str(PROMPT_TESTER),
             "--vault", str(tmp_path),
             "--slug", "anything", "--modality", "image",
             "--dry-run"],
            capture_output=True, text=True, timeout=20,
        )
        assert proc.returncode == 2
        assert "aesthetic-only" in proc.stderr
        # The guard should reference Track L for context
        assert "LENS EVOLUTION" in proc.stderr or "lens" in proc.stderr.lower()

    def test_missing_active_lens_exits_with_diagnostic(
        self, tmp_path: Path,
    ):
        """No active/lens.yaml → clear error about running /genesis first.

        Populate .agent/ and wiki/ subdirectories so the vault validator
        (added in Wave 5 to fail fast on non-vault paths) lets execution
        proceed to the lens-resolution stage, which is what this test
        actually exercises.
        """
        (tmp_path / ".agent").mkdir()
        (tmp_path / "wiki").mkdir()
        proc = subprocess.run(
            [sys.executable, str(PROMPT_TESTER),
             "--vault", str(tmp_path),
             "--slug", "anything", "--modality", "image"],
            capture_output=True, text=True, timeout=20,
        )
        assert proc.returncode == 2
        assert "no active lens" in proc.stderr

    def test_explicit_lens_override_accepted(self, tmp_path: Path):
        """Passing --lens=aesthetic-warburg explicitly bypasses vault resolution."""
        # Vault has NO active lens file, but --lens override is explicit.
        proc = subprocess.run(
            [sys.executable, str(PROMPT_TESTER),
             "--vault", str(tmp_path),
             "--lens", "aesthetic-warburg",
             "--slug", "nonexistent-slug",
             "--modality", "image",
             "--dry-run"],
            capture_output=True, text=True, timeout=20,
        )
        # Guard passes → runner proceeds → fails later (slug not found or
        # gen_client missing), NOT with the aesthetic-only guard.
        assert "aesthetic-only" not in proc.stderr
        assert "no active lens" not in proc.stderr

    def test_zettelkasten_also_rejected(self, tmp_path: Path):
        """Every non-aesthetic lens must be rejected, not just engineering."""
        _seed_active_lens(tmp_path, "general-zettelkasten")
        proc = subprocess.run(
            [sys.executable, str(PROMPT_TESTER),
             "--vault", str(tmp_path),
             "--slug", "anything", "--modality", "image"],
            capture_output=True, text=True, timeout=20,
        )
        assert proc.returncode == 2
        assert "general-zettelkasten" in proc.stderr
