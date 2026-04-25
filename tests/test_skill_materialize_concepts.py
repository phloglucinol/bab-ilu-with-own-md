from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = REPO_ROOT / ".claude" / "skills" / "materialize-concepts" / "SKILL.md"


def test_materialize_concepts_skill_exists_and_mentions_tool():
    text = SKILL_PATH.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    assert "name: materialize-concepts" in text
    assert "tools.materialize_concepts" in text
    assert "general-zettelkasten" in text
    assert "--dry-run" in text
    assert "$gap" in text


def test_command_tables_document_materialize_concepts():
    files = [
        REPO_ROOT / "AGENTS.md",
        REPO_ROOT / "README.md",
        REPO_ROOT / "README.en.md",
        REPO_ROOT / "docs" / "codex-quickstart.md",
    ]
    for path in files:
        text = path.read_text(encoding="utf-8")
        assert "$materialize-concepts" in text, f"{path} missing Codex entry"
        if path.name != "codex-quickstart.md":
            assert "/materialize-concepts" in text, f"{path} missing Claude entry"
