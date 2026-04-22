"""Shared fixtures for Bab-ilu v2.1 tests."""
from pathlib import Path
import yaml
import pytest


REPO_ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def schema_path(repo_root: Path) -> Path:
    return repo_root / "schema.md"


@pytest.fixture(scope="session")
def claude_md_path(repo_root: Path) -> Path:
    return repo_root / "CLAUDE.md"


@pytest.fixture(scope="session")
def gap_spec_path(repo_root: Path) -> Path:
    return repo_root / ".agent" / "spec" / "gap-algorithm.md"


@pytest.fixture(scope="session")
def templates_dir(repo_root: Path) -> Path:
    return repo_root / "templates"


@pytest.fixture(scope="session")
def seed_kit_dir(repo_root: Path) -> Path:
    return repo_root / "seed-kit"


@pytest.fixture(scope="session")
def aesthetic_seed_dir(seed_kit_dir: Path) -> Path:
    """Aesthetic · Warburg lens seed subdir; holds the v2.0 seed content."""
    return seed_kit_dir / "aesthetic-warburg"


@pytest.fixture(scope="session")
def engineering_seed_dir(seed_kit_dir: Path) -> Path:
    """Engineering · Alexander lens seed subdir; scaffold only until Sprint 2 · C2."""
    return seed_kit_dir / "engineering-alexander"


@pytest.fixture(scope="session")
def general_seed_dir(seed_kit_dir: Path) -> Path:
    """General · Zettelkasten lens seed subdir; scaffold only until Sprint 2 · C3."""
    return seed_kit_dir / "general-zettelkasten"


def parse_frontmatter(md_path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file; return {} if none."""
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    return yaml.safe_load(text[4:end]) or {}


@pytest.fixture(scope="session")
def frontmatter_parser():
    return parse_frontmatter
