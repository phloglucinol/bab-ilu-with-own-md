from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from tools.lens_loader import load_lens


REPO_ROOT = Path(__file__).resolve().parents[1]
LENSES_DIR = REPO_ROOT / ".agent" / "lenses"


def _write_note(
    vault: Path,
    slug: str,
    *,
    concepts: list[str] | None = None,
    body: str = "",
) -> Path:
    note_dir = vault / "wiki" / "note"
    note_dir.mkdir(parents=True, exist_ok=True)
    concept_lines = "\n".join(f"  - {c}" for c in (concepts or []))
    concepts_block = "concepts:\n" + concept_lines if concepts else "concepts: []"
    text = f"""---
type: note
lens: general-zettelkasten
slug: {slug}
bloom: understand
{concepts_block}
---

# {slug}

{body}
"""
    path = note_dir / f"{slug}.md"
    path.write_text(text, encoding="utf-8")
    return path


def _read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    end = text.find("\n---\n", 4)
    assert end > 0
    return yaml.safe_load(text[4:end]) or {}


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    (tmp_path / "wiki" / "note").mkdir(parents=True)
    (tmp_path / "wiki" / "concept").mkdir(parents=True)
    (tmp_path / ".agent" / "lenses").mkdir(parents=True)
    return tmp_path


@pytest.fixture
def zettel_lens():
    return load_lens("general-zettelkasten", base=LENSES_DIR)


@pytest.fixture
def aesthetic_lens():
    return load_lens("aesthetic-warburg", base=LENSES_DIR)


def test_extracts_only_canonical_concept_sources(vault: Path, zettel_lens):
    from tools.materialize_concepts import discover_concepts

    _write_note(
        vault,
        "note-a",
        concepts=["[[shared-frontmatter]]", "single-frontmatter"],
        body="""
## Concepts (tier_1_atoms)

- [[shared-body]]: real concept source
- `[[shared-code-span]]`: real concept source

## Back-references

- [[not-a-concept-backref]]

<!-- [[not-a-concept-comment]] -->
""",
    )
    _write_note(
        vault,
        "note-b",
        concepts=["shared-frontmatter"],
        body="""
## Concepts (tier_1_atoms)

- [[shared-body|Shared body]]: alias form
- `[[shared-code-span]]`: code-span form
- [[concept-slug]]: template example must not count

## Source

- [[not-a-concept-source]]
""",
    )

    result = discover_concepts(vault, zettel_lens)

    assert result.notes_scanned == 2
    assert result.references["shared-frontmatter"] == {"note-a", "note-b"}
    assert result.references["shared-body"] == {"note-a", "note-b"}
    assert result.references["shared-code-span"] == {"note-a", "note-b"}
    assert "single-frontmatter" in result.singletons
    assert "not-a-concept-backref" not in result.references
    assert "not-a-concept-comment" not in result.references
    assert "not-a-concept-source" not in result.references
    assert "concept-slug" not in result.references


def test_ignores_existing_note_slugs_invalid_links_and_duplicate_mentions(vault: Path, zettel_lens):
    from tools.materialize_concepts import discover_concepts

    _write_note(vault, "existing-note", concepts=["keep-existing-note-present"])
    _write_note(
        vault,
        "note-a",
        concepts=["reused-concept", "reused-concept", "existing-note", "Bad Slug"],
        body="""
## Concepts (tier_1_atoms)

- [[reused-concept]]
- [[existing-note]]
- [[diagram.png]]
- [[reused-concept#section]]
""",
    )
    _write_note(vault, "note-b", concepts=["reused-concept"])

    result = discover_concepts(vault, zettel_lens)

    assert result.references["reused-concept"] == {"note-a", "note-b"}
    assert "existing-note" not in result.references
    assert "diagram.png" not in result.references
    assert "Bad Slug" not in result.references


def test_materializes_only_reused_concepts_and_reports_singletons(vault: Path, zettel_lens):
    from tools.materialize_concepts import materialize_concepts

    _write_note(vault, "note-b", concepts=["shared-concept", "lonely-concept"])
    _write_note(vault, "note-a", concepts=["shared-concept"])

    summary = materialize_concepts(vault, zettel_lens)

    created_path = vault / "wiki" / "concept" / "shared-concept.md"
    singleton_path = vault / "wiki" / "concept" / "lonely-concept.md"
    assert created_path.exists()
    assert not singleton_path.exists()
    assert summary.created == ["wiki/concept/shared-concept.md"]
    assert summary.reported_singleton == 1
    assert summary.singleton_slugs == ["lonely-concept"]

    text = created_path.read_text(encoding="utf-8")
    fm = _read_frontmatter(created_path)
    assert fm == {
        "type": "concept",
        "lens": "general-zettelkasten",
        "created": summary.date,
        "status": "stub",
    }
    assert "relations:" not in yaml.safe_dump(fm)
    assert "<!-- llm:section-start materialize-concepts-relations -->" in text
    assert "- {type: exemplifiedBy, target: [[note-a]]}" in text
    assert "- {type: exemplifiedBy, target: [[note-b]]}" in text
    assert text.index("[[note-a]]") < text.index("[[note-b]]")
    assert "## Referenced By" in text


def test_dry_run_reports_without_writing(vault: Path, zettel_lens):
    from tools.materialize_concepts import materialize_concepts

    _write_note(vault, "note-a", concepts=["shared-concept"])
    _write_note(vault, "note-b", concepts=["shared-concept"])

    summary = materialize_concepts(vault, zettel_lens, dry_run=True)

    assert summary.created == ["wiki/concept/shared-concept.md"]
    assert not (vault / "wiki" / "concept" / "shared-concept.md").exists()


def test_existing_concept_is_not_overwritten(vault: Path, zettel_lens):
    from tools.materialize_concepts import materialize_concepts

    concept_dir = vault / "wiki" / "concept"
    concept_dir.mkdir(parents=True, exist_ok=True)
    existing = concept_dir / "shared-concept.md"
    existing.write_text("# hand written\n", encoding="utf-8")
    _write_note(vault, "note-a", concepts=["shared-concept"])
    _write_note(vault, "note-b", concepts=["shared-concept"])

    summary = materialize_concepts(vault, zettel_lens)

    assert existing.read_text(encoding="utf-8") == "# hand written\n"
    assert summary.created == []
    assert summary.skipped_existing == 1


def test_rejects_non_zettelkasten_lens(vault: Path, aesthetic_lens):
    from tools.materialize_concepts import materialize_concepts

    _write_note(vault, "note-a", concepts=["shared-concept"])

    with pytest.raises(ValueError, match="general-zettelkasten"):
        materialize_concepts(vault, aesthetic_lens)


def test_json_cli_outputs_machine_readable_summary(vault: Path):
    _write_note(vault, "note-a", concepts=["shared-concept"])
    _write_note(vault, "note-b", concepts=["shared-concept"])

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "tools.materialize_concepts",
            "--vault",
            str(vault),
            "--lens",
            "general-zettelkasten",
            "--json",
        ],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["lens"] == "general-zettelkasten"
    assert payload["created"] == 1
    assert payload["created_paths"] == ["wiki/concept/shared-concept.md"]


def test_human_cli_next_command_uses_requested_vault(vault: Path):
    _write_note(vault, "note-a", concepts=["shared-concept"])
    _write_note(vault, "note-b", concepts=["shared-concept"])

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "tools.materialize_concepts",
            "--vault",
            str(vault),
            "--lens",
            "general-zettelkasten",
            "--dry-run",
        ],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert (
        f"next: python3 -m tools.gap_runner --vault {vault.resolve()} "
        "--lens general-zettelkasten"
    ) in result.stdout
