"""v2.1 tests for .claude/skills/setup/SKILL.md

Asserts against the CURRENT v2.1 surface — no i18n/ paths, no v1.4 tooling.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SKILL = PROJECT_ROOT / ".claude" / "skills" / "setup" / "SKILL.md"


@pytest.fixture(scope="module")
def skill_text() -> str:
    return SKILL.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# File exists and is readable
# ---------------------------------------------------------------------------


def test_skill_file_exists():
    assert SKILL.exists(), f"/setup SKILL.md not found at {SKILL}"


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------


def test_frontmatter_present(skill_text):
    """SKILL.md must open with YAML frontmatter."""
    assert skill_text.startswith("---"), "SKILL.md must begin with YAML frontmatter (---)"


def test_frontmatter_has_description(skill_text):
    """Frontmatter must include a description field."""
    assert "description:" in skill_text, "Frontmatter missing 'description:' field"


# ---------------------------------------------------------------------------
# Env keys — tools/_env.py defines the authoritative list
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("key", [
    "LLM_API_KEY",
    "LLM_BASE_URL",
    "LLM_MODEL",
])
def test_skill_mentions_env_key(key, skill_text):
    """/setup walks users through the Review LLM env keys. Legacy academic
    keys (SEMANTIC_SCHOLAR_API_KEY, DEEPXIV_TOKEN) were removed in v2.2
    along with their tool users."""
    assert key in skill_text, f"SKILL.md does not mention env key: {key}"


# ---------------------------------------------------------------------------
# .env file reference
# ---------------------------------------------------------------------------


def test_skill_references_dot_env_file(skill_text):
    """.env must be mentioned — setup reads and writes this file."""
    assert ".env" in skill_text, "SKILL.md does not reference .env"


def test_skill_writes_only_dot_env_not_global(skill_text):
    """Constraint: setup must document that writes go to .env only, not ~/.env."""
    # The SKILL.md may mention ~/.env as a forbidden target in a constraint statement.
    # What we assert is that the Constraints section explicitly prohibits writing there.
    lowered = skill_text.lower()
    assert "write only to" in lowered or "never to" in lowered, \
        "SKILL.md Constraints must explicitly state writes go only to .env, not global locations"


# ---------------------------------------------------------------------------
# Next-step pointer — /genesis
# ---------------------------------------------------------------------------


def test_skill_references_genesis_as_next_step(skill_text):
    """/genesis must appear as the next step after setup for fresh installs."""
    assert "/genesis" in skill_text, \
        "SKILL.md must mention /genesis as the next step after configuration"


# ---------------------------------------------------------------------------
# Regression guards: no v1.4 surface must leak into SKILL.md
# ---------------------------------------------------------------------------



def _bash_block_lines(text: str) -> list[str]:
    """Return only lines that appear inside ```bash ... ``` fences."""
    lines: list[str] = []
    in_bash = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```bash"):
            in_bash = True
            continue
        if in_bash and stripped == "```":
            in_bash = False
            continue
        if in_bash:
            lines.append(line)
    return lines


def test_no_paper_star_invocation_in_workflow(skill_text):
    """/paper-* commands must not be _executed_ in Workflow bash blocks.

    They may appear in prose as downstream skill names, but setup must never
    shell-invoke them as part of its own workflow.
    """
    wf_start = skill_text.find("## Workflow")
    wf_end = skill_text.find("\n## ", wf_start + 1)
    workflow = skill_text[wf_start:wf_end] if wf_end > wf_start else skill_text[wf_start:]
    bad = [l for l in _bash_block_lines(workflow) if re.search(r"/paper-\w+", l)]
    assert not bad, f"v1.4 regression: /paper-* invoked in Workflow bash: {bad}"


def test_no_exp_star_invocation_in_workflow(skill_text):
    """/exp-* commands must not be _executed_ in Workflow bash blocks."""
    wf_start = skill_text.find("## Workflow")
    wf_end = skill_text.find("\n## ", wf_start + 1)
    workflow = skill_text[wf_start:wf_end] if wf_end > wf_start else skill_text[wf_start:]
    bad = [l for l in _bash_block_lines(workflow) if re.search(r"/exp-\w+", l)]
    assert not bad, f"v1.4 regression: /exp-* invoked in Workflow bash: {bad}"


def test_no_daily_arxiv_anywhere(skill_text):
    """/daily-arxiv was entirely removed in v2.0 — must not appear anywhere."""
    assert "/daily-arxiv" not in skill_text, \
        "v1.4 regression: /daily-arxiv must not appear in v2.1 SKILL.md"


def test_no_raw_papers_reference(skill_text):
    """raw/papers/ was the v1.4 paper store — must not appear in v2.1."""
    assert "raw/papers" not in skill_text, \
        "v1.4 regression: raw/papers must not appear in v2.1 SKILL.md"


# ---------------------------------------------------------------------------
# Bash snippet syntax check
# ---------------------------------------------------------------------------


def _extract_bash_blocks(text: str) -> list[str]:
    """Return the content of every ```bash ... ``` block in text."""
    return re.findall(r"```bash\n(.*?)```", text, re.DOTALL)


def test_bash_snippets_are_syntactically_valid(skill_text):
    """All ```bash``` blocks must pass `bash -n` (syntax check only, no exec)."""
    blocks = _extract_bash_blocks(skill_text)
    assert blocks, "Expected at least one ```bash``` block in SKILL.md"
    for i, block in enumerate(blocks):
        result = subprocess.run(
            ["bash", "-n"],
            input=block,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"Bash block #{i + 1} has a syntax error:\n"
            f"{block[:200]}\nSTDERR: {result.stderr}"
        )
