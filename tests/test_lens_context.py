"""Tests for tools.lens_context — runtime lens prompt loader with caching.

B3 acceptance:
- load_active_prompts() reads .agent/lenses/active/prompts.md
- In-process cache; invalidates on mtime change
- BABILU_LENS_PROMPTS_PATH env var overrides the default path
- Missing active lens → empty string + single warning (no exception)
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import lens_context  # noqa: E402
from tools.lens_context import (  # noqa: E402
    DEFAULT_ACTIVE_PROMPTS_PATH,
    ENV_OVERRIDE_KEY,
    active_lens_preamble,
    clear_cache,
    load_active_prompts,
)


# ---------- fixtures / helpers ----------


@pytest.fixture(autouse=True)
def _reset_cache():
    """Ensure cache + warn-once state are clean between tests."""
    clear_cache()
    yield
    clear_cache()


@pytest.fixture(autouse=True)
def _clear_env(monkeypatch):
    monkeypatch.delenv(ENV_OVERRIDE_KEY, raising=False)


def _write_prompts(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ---------- happy path ----------


def test_reads_prompts_from_default_path(tmp_path, monkeypatch):
    active_dir = tmp_path / ".agent" / "lenses" / "active"
    prompts = active_dir / "prompts.md"
    _write_prompts(prompts, "# Pathosformel judgment\nTrust motif recurrence over single frames.\n")

    monkeypatch.chdir(tmp_path)
    result = load_active_prompts()
    assert "Pathosformel judgment" in result
    assert "motif recurrence" in result


def test_default_path_constant_is_documented():
    assert str(DEFAULT_ACTIVE_PROMPTS_PATH).endswith(".agent/lenses/active/prompts.md")


# ---------- caching ----------


def test_cache_avoids_re_reading(tmp_path, monkeypatch):
    prompts = tmp_path / ".agent" / "lenses" / "active" / "prompts.md"
    _write_prompts(prompts, "v1")
    monkeypatch.chdir(tmp_path)

    read_calls = {"count": 0}
    real_read = Path.read_text

    def counting_read(self, *args, **kwargs):
        if Path(self).name == "prompts.md":
            read_calls["count"] += 1
        return real_read(self, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", counting_read)

    a = load_active_prompts()
    b = load_active_prompts()
    c = load_active_prompts()
    assert a == b == c == "v1"
    assert read_calls["count"] == 1, "expected exactly one filesystem read due to cache"


def test_cache_invalidates_on_mtime_change(tmp_path, monkeypatch):
    prompts = tmp_path / ".agent" / "lenses" / "active" / "prompts.md"
    _write_prompts(prompts, "old")
    monkeypatch.chdir(tmp_path)

    assert load_active_prompts() == "old"

    time.sleep(0.01)  # ensure a new mtime
    prompts.write_text("new", encoding="utf-8")
    os.utime(prompts, None)  # force mtime bump

    assert load_active_prompts() == "new"


# ---------- env override ----------


def test_env_var_overrides_default_path(tmp_path, monkeypatch):
    override = tmp_path / "custom_prompts.md"
    override.write_text("override wins\n", encoding="utf-8")

    # cwd has a "default" file to prove env override takes precedence
    default_path = tmp_path / ".agent" / "lenses" / "active" / "prompts.md"
    _write_prompts(default_path, "default loses\n")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv(ENV_OVERRIDE_KEY, str(override))

    assert load_active_prompts() == "override wins\n"


def test_env_var_missing_file_still_empty_no_raise(tmp_path, monkeypatch, caplog):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv(ENV_OVERRIDE_KEY, str(tmp_path / "does-not-exist.md"))

    import logging

    caplog.set_level(logging.WARNING)
    result = load_active_prompts()
    assert result == ""
    assert any("does-not-exist.md" in rec.message for rec in caplog.records)


# ---------- missing file / warn-once ----------


def test_missing_active_lens_returns_empty(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert load_active_prompts() == ""


def test_missing_active_lens_warns_only_once(tmp_path, monkeypatch, caplog):
    monkeypatch.chdir(tmp_path)
    import logging

    caplog.set_level(logging.WARNING)
    for _ in range(3):
        load_active_prompts()

    warn_records = [
        r for r in caplog.records if "lens" in r.message.lower() or "prompts" in r.message.lower()
    ]
    assert len(warn_records) == 1, (
        f"expected exactly 1 warning across 3 calls, got {len(warn_records)}: "
        f"{[r.message for r in warn_records]}"
    )


# ---------- preamble helper ----------


def test_active_lens_preamble_wraps_content(tmp_path, monkeypatch):
    prompts = tmp_path / ".agent" / "lenses" / "active" / "prompts.md"
    _write_prompts(prompts, "rule 1\nrule 2\n")
    monkeypatch.chdir(tmp_path)

    preamble = active_lens_preamble()
    assert preamble.startswith("<lens-context>")
    assert preamble.rstrip().endswith("</lens-context>")
    assert "rule 1" in preamble
    assert "rule 2" in preamble


def test_active_lens_preamble_empty_when_no_lens(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert active_lens_preamble() == ""


# ---------- module surface ----------


def test_public_surface_stable():
    # guard against accidental symbol removal
    for name in (
        "DEFAULT_ACTIVE_PROMPTS_PATH",
        "ENV_OVERRIDE_KEY",
        "active_lens_preamble",
        "clear_cache",
        "load_active_prompts",
    ):
        assert hasattr(lens_context, name), f"tools.lens_context missing '{name}'"
