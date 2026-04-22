"""Validates templates/ directory structure and content."""
from pathlib import Path


def test_templates_dir_exists(templates_dir: Path):
    assert templates_dir.is_dir(), f"{templates_dir} missing"


def test_vault_schema_template_exists(templates_dir: Path):
    assert (templates_dir / "vault-schema.md").is_file()


def test_vault_claude_template_exists(templates_dir: Path):
    p = templates_dir / "vault-CLAUDE.md"
    assert p.is_file()
    text = p.read_text(encoding="utf-8")
    assert "{{VAULT_LANGUAGE}}" in text, "vault-CLAUDE.md must have {{VAULT_LANGUAGE}} placeholder"
    assert "{{GENESIS_DATE}}" in text, "vault-CLAUDE.md must have {{GENESIS_DATE}} placeholder"


def test_gap_algorithm_template_exists(templates_dir: Path):
    assert (templates_dir / "vault-gap-algorithm.md").is_file()


def test_wiki_templates(templates_dir: Path):
    wiki = templates_dir / "wiki"
    for f in ("index.md", "log.md", "_glossary.md"):
        assert (wiki / f).is_file(), f"templates/wiki/{f} missing"


def test_glossary_is_bilingual(templates_dir: Path):
    text = (templates_dir / "wiki" / "_glossary.md").read_text(encoding="utf-8")
    # Core terms must have both English and Chinese entries
    assert "Work" in text and "作品" in text, "glossary must have Work / 作品 entry"
    assert "Pathosformel" in text and "情感公式" in text, "glossary must have bilingual Pathosformel entry"
    assert "Nachleben" in text and "来世" in text, "glossary must have bilingual Nachleben entry"


def test_obsidian_templates(templates_dir: Path):
    obs = templates_dir / ".obsidian"
    assert (obs / "app.json").is_file()
    assert (obs / "graph.json").is_file()


def test_obsidian_app_excludes_agent_dir(templates_dir: Path):
    import json
    text = (templates_dir / ".obsidian" / "app.json").read_text(encoding="utf-8")
    cfg = json.loads(text)
    assert "userIgnoreFilters" in cfg
    assert any(".agent" in f for f in cfg["userIgnoreFilters"]), (
        "Obsidian app.json must exclude .agent/ from sync/view"
    )


def test_obsidian_graph_has_seven_color_groups(templates_dir: Path):
    import json
    text = (templates_dir / ".obsidian" / "graph.json").read_text(encoding="utf-8")
    cfg = json.loads(text)
    color_groups = cfg.get("colorGroups", [])
    assert len(color_groups) == 7, f"expected 7 color groups, got {len(color_groups)}"
    queries = [g["query"] for g in color_groups]
    for folder in ("works/", "motifs/", "pathosformel/", "topoi/", "people/", "sources/", "questions/"):
        assert any(folder in q for q in queries), f"missing graph color for {folder}"
