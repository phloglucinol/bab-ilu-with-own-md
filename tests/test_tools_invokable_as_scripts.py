"""Regression guard: every tools/*.py that ships with a CLI must run both
as a bare script (`python3 tools/<name>.py --help`) AND as a module
(`python3 -m tools.<name> --help`) without ModuleNotFoundError.

This test exists because prior audits repeatedly caught the same class of
bug: a tool used `from tools.X import Y`, which only works when the tool
is imported as a package member (e.g. via `python -m tools.X`). Running
it as `python3 tools/X.py` — which is what every SKILL.md and setup.sh
tells users to do — fails with `ModuleNotFoundError: No module named
'tools'`.

Unit tests that monkeypatch `subprocess.run` don't catch this because
the analyzer binary is never actually executed. This test runs the
command verbatim, which is the only way to prove the skill-invoked form
works.

The `-m` form is tested separately and is equally important — lint.py
specifically invokes `python -m tools.graph_analyzer` via subprocess,
and a regression in either direction (adding a `from tools.X` without a
fallback, OR adding a bare `from X` that only works as a script) breaks
one of the two callers.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = REPO_ROOT / "tools"


def _bare_script_tools() -> list[Path]:
    """Return every tools/*.py that has an `argparse` CLI."""
    out = []
    for script in TOOLS_DIR.glob("*.py"):
        if script.name in ("__init__.py",):
            continue
        try:
            text = script.read_text(encoding="utf-8")
        except OSError:
            continue
        if "ArgumentParser(" in text or "argparse.ArgumentParser" in text:
            out.append(script)
    return sorted(out)


@pytest.mark.parametrize("tool", _bare_script_tools(), ids=lambda p: p.name)
def test_tool_runs_as_bare_script(tool: Path) -> None:
    """`python3 tools/<name>.py --help` must exit 0 with no ModuleNotFoundError."""
    result = subprocess.run(
        [sys.executable, str(tool), "--help"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=30,
    )
    combined = result.stdout + result.stderr
    assert "ModuleNotFoundError" not in combined, (
        f"{tool.name} fails as bare script:\n{combined[:400]}"
    )
    assert result.returncode == 0, (
        f"{tool.name} --help returned {result.returncode}:\n{combined[:400]}"
    )


@pytest.mark.parametrize("tool", _bare_script_tools(), ids=lambda p: p.name)
def test_tool_runs_as_module_form(tool: Path) -> None:
    """`python3 -m tools.<name> --help` must exit 0. This is how lint.py
    invokes graph_analyzer, and it's the form Python-packaging purists
    recommend. A regression in either direction (bare-script-only or
    -m-only) breaks one of the two callers.
    """
    module_name = f"tools.{tool.stem}"
    result = subprocess.run(
        [sys.executable, "-m", module_name, "--help"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=30,
    )
    combined = result.stdout + result.stderr
    assert "ModuleNotFoundError" not in combined, (
        f"{module_name} fails as `python -m` form:\n{combined[:400]}"
    )
    assert result.returncode == 0, (
        f"{module_name} --help returned {result.returncode}:\n{combined[:400]}"
    )
