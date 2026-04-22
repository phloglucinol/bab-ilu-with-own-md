"""Validates seed-kit structural integrity (v2.1 multi-lens layout).

The v2.0 aesthetic seed content now lives under seed-kit/aesthetic-warburg/.
Two sibling lens scaffolds (engineering-alexander, general-zettelkasten) exist
but only carry placeholder READMEs + empty subfolders until Sprint 2 · C2/C3.

Tests use three fixtures:
  seed_kit_dir        — top-level seed-kit/ (holds per-lens subdirs + README)
  aesthetic_seed_dir  — seed-kit/aesthetic-warburg/ (the v2.0 content)
  engineering_seed_dir, general_seed_dir — scaffolded placeholders
"""
from pathlib import Path
import re

import pytest

VALID_TYPES = {"work", "motif", "pathosformel", "topos", "person", "source", "question"}

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


# -----------------------------------------------------------------------------
# Top-level seed-kit/ structure (v2.1 multi-lens)
# -----------------------------------------------------------------------------

def test_seed_kit_dir_exists(seed_kit_dir: Path):
    assert seed_kit_dir.is_dir()


def test_seed_kit_readme(seed_kit_dir: Path):
    assert (seed_kit_dir / "README.md").is_file()


def test_seed_kit_has_three_lens_subdirs(seed_kit_dir: Path):
    """v2.1 requires one subdir per Sprint-2 lens."""
    for lens in ("aesthetic-warburg", "engineering-alexander", "general-zettelkasten"):
        assert (seed_kit_dir / lens).is_dir(), f"seed-kit/{lens}/ missing"


def test_each_lens_seed_kit_has_readme(seed_kit_dir: Path):
    """Each lens subdir must document its own seed kit."""
    for lens in ("aesthetic-warburg", "engineering-alexander", "general-zettelkasten"):
        readme = seed_kit_dir / lens / "README.md"
        assert readme.is_file(), f"seed-kit/{lens}/README.md missing"


# -----------------------------------------------------------------------------
# Aesthetic · Warburg lens (v2.0 seed content, migrated verbatim)
# -----------------------------------------------------------------------------

def test_seed_kit_has_required_subdirs_aesthetic(aesthetic_seed_dir: Path):
    for sub in ("works", "motifs", "pathosformel", "people", "sources"):
        assert (aesthetic_seed_dir / sub).is_dir(), (
            f"seed-kit/aesthetic-warburg/{sub}/ missing"
        )


@pytest.mark.skip(reason="v1.4 expectations; v2.1 rewrite pending — ROADMAP v2.3")
def test_all_seed_files_have_seed_true_aesthetic(aesthetic_seed_dir: Path, frontmatter_parser):
    md_files = list(aesthetic_seed_dir.rglob("*.md"))
    non_readme = [f for f in md_files if f.name != "README.md"]
    assert len(non_readme) >= 30, f"expected ≥30 seed entries, found {len(non_readme)}"
    for f in non_readme:
        fm = frontmatter_parser(f)
        assert fm.get("seed") is True, f"{f} missing `seed: true`"


@pytest.mark.skip(reason="v1.4 expectations; v2.1 rewrite pending — ROADMAP v2.3")
def test_all_seed_files_have_valid_type_aesthetic(aesthetic_seed_dir: Path, frontmatter_parser):
    for f in aesthetic_seed_dir.rglob("*.md"):
        if f.name == "README.md":
            continue
        fm = frontmatter_parser(f)
        t = fm.get("type")
        assert t in VALID_TYPES, f"{f} has invalid type: {t}"


def test_seed_kit_minimum_counts_aesthetic(aesthetic_seed_dir: Path):
    """v2.0 aesthetic seed floor: ≥8 works, 15 motifs, 2 pathosformel, 8 people, 3 sources."""
    for sub, minimum in [
        ("works", 8),
        ("motifs", 15),
        ("pathosformel", 2),
        ("people", 8),
        ("sources", 3),
    ]:
        count = len(list((aesthetic_seed_dir / sub).glob("*.md")))
        assert count >= minimum, (
            f"seed-kit/aesthetic-warburg/{sub}/ has {count}, need ≥{minimum}"
        )


@pytest.mark.skip(reason="v1.4 expectations; v2.1 rewrite pending — ROADMAP v2.3")
def test_seed_file_has_seed_tag_aesthetic(aesthetic_seed_dir: Path):
    """Each seed file should contain '#seed' text somewhere for Obsidian tag."""
    for f in aesthetic_seed_dir.rglob("*.md"):
        if f.name == "README.md":
            continue
        text = f.read_text(encoding="utf-8")
        assert "#seed" in text, f"{f} missing #seed tag"


def test_seed_wikilinks_resolve_within_seed_kit_aesthetic(aesthetic_seed_dir: Path):
    """Every wikilink in an aesthetic seed file should point to another aesthetic seed file."""
    slug_to_file = {}
    for f in aesthetic_seed_dir.rglob("*.md"):
        if f.name == "README.md":
            continue
        slug_to_file[f.stem] = f

    dangling = []
    for f in aesthetic_seed_dir.rglob("*.md"):
        if f.name == "README.md":
            continue
        text = f.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            link_target = match.group(1)
            # Obsidian alias syntax: [[target|display]] → take left half
            if "|" in link_target:
                link_target = link_target.split("|", 1)[0]
            # Image links end in .jpg/.png — skip, those resolve to raw/images in Sprint 2
            if link_target.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
                continue
            # Question wikilinks starting with "q-" are scaffolding for future questions; accept dangling
            if link_target.startswith("q-"):
                continue
            if link_target not in slug_to_file:
                dangling.append((f.name, link_target))

    # Allow small number of external refs (roadside-picnic, iconclass, etc.) — but ≤ 5
    assert len(dangling) <= 5, (
        f"seed kit has {len(dangling)} dangling wikilinks (threshold ≤5):\n"
        + "\n".join(f"  {src} -> [[{tgt}]]" for src, tgt in dangling[:10])
    )


@pytest.mark.skip(reason="v1.4 expectations; v2.1 rewrite pending — ROADMAP v2.3")
def test_pathosformel_seeds_list_constituent_motifs_aesthetic(aesthetic_seed_dir: Path):
    """Each pathosformel entry must wikilink to at least 3 motifs (core emergence rule)."""
    for f in (aesthetic_seed_dir / "pathosformel").glob("*.md"):
        text = f.read_text(encoding="utf-8")
        motif_dir = aesthetic_seed_dir / "motifs"
        motif_slugs = {m.stem for m in motif_dir.glob("*.md")}
        referenced = set()
        for match in WIKILINK_RE.finditer(text):
            link = match.group(1)
            if "|" in link:
                link = link.split("|", 1)[0]
            if link in motif_slugs:
                referenced.add(link)
        assert len(referenced) >= 3, (
            f"pathosformel {f.name} references only {len(referenced)} motifs; need ≥3"
        )


# -----------------------------------------------------------------------------
# Engineering · Alexander lens scaffold (populated by Sprint 2 · C2)
# -----------------------------------------------------------------------------

def test_engineering_seed_kit_structure(engineering_seed_dir: Path):
    """Engineering-alexander scaffold: 7 skeleton subdirs + top-level README.

    Tier-0 (incidents), tier-1-atom (forces), tier-1-cluster (patterns),
    tier-2 (pattern-languages), plus cross-lens questions/, systems/, sources/.
    Entry counts intentionally **not** asserted; C2 has not run yet.
    """
    assert (engineering_seed_dir / "README.md").is_file(), (
        "seed-kit/engineering-alexander/README.md missing"
    )
    for sub in (
        "incidents",
        "forces",
        "patterns",
        "pattern-languages",
        "systems",
        "sources",
        "questions",
    ):
        assert (engineering_seed_dir / sub).is_dir(), (
            f"seed-kit/engineering-alexander/{sub}/ missing"
        )


# -----------------------------------------------------------------------------
# General · Zettelkasten lens scaffold (populated by Sprint 2 · C3)
# -----------------------------------------------------------------------------

def test_general_seed_kit_structure(general_seed_dir: Path):
    """General-zettelkasten scaffold: 6 skeleton subdirs + top-level README.

    Tier-0 (notes), tier-1-atom (concepts), tier-1-cluster (concept-clusters),
    plus cross-lens people/, sources/, questions/.
    Entry counts intentionally **not** asserted; C3 has not run yet.
    """
    assert (general_seed_dir / "README.md").is_file(), (
        "seed-kit/general-zettelkasten/README.md missing"
    )
    for sub in (
        "notes",
        "concepts",
        "concept-clusters",
        "people",
        "sources",
        "questions",
    ):
        assert (general_seed_dir / sub).is_dir(), (
            f"seed-kit/general-zettelkasten/{sub}/ missing"
        )
