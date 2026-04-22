"""Seed-kit ↔ lens entity-model contract tests.

For every lens that ships a seed kit under `seed-kit/<id>/`, the frontmatter
`type:` values in the seed files must match the lens's `entity_model` tiers
(tier_0 / tier_1_atom / tier_1_cluster). If they drift, downstream tools
(ingest_runner, graph_analyzer) silently filter the seeds out and the vault
looks empty after `/genesis --seeded`.

This caught the Wave 14 aesthetic-warburg regression where works/*.md shipped
`type: work` and pathosformel/*.md shipped `type: pathosformel` — pre-v2.1
terminology that no longer matched tier_0='aesthetic' / tier_1_cluster='panel'.
"""
from pathlib import Path

import pytest
import yaml


LENS_IDS = ("aesthetic-warburg", "engineering-alexander", "general-zettelkasten")


def _load_lens_yaml(repo_root: Path, lens_id: str) -> dict:
    lens_path = repo_root / ".agent" / "lenses" / lens_id / "lens.yaml"
    assert lens_path.is_file(), f"lens yaml missing: {lens_path}"
    return yaml.safe_load(lens_path.read_text(encoding="utf-8"))


def _seed_type_distribution(seed_dir: Path, frontmatter_parser) -> dict[str, int]:
    dist: dict[str, int] = {}
    for md_file in seed_dir.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        fm = frontmatter_parser(md_file)
        t = fm.get("type")
        if isinstance(t, str):
            dist[t] = dist.get(t, 0) + 1
    return dist


@pytest.mark.parametrize("lens_id", LENS_IDS)
def test_seed_kit_has_tier_0_entries(lens_id: str, repo_root: Path, frontmatter_parser):
    """At least one seed file must carry `type: <tier_0>` for the lens.

    Without tier_0 entries, ingest_runner writes nothing usable for this lens
    and graph_analyzer's tier_0 filter returns an empty node set.
    """
    lens = _load_lens_yaml(repo_root, lens_id)
    tier_0 = lens["entity_model"]["tier_0"]

    seed_dir = repo_root / "seed-kit" / lens_id
    if not seed_dir.is_dir():
        pytest.skip(f"seed-kit/{lens_id}/ not present")

    dist = _seed_type_distribution(seed_dir, frontmatter_parser)
    count = dist.get(tier_0, 0)
    assert count > 0, (
        f"seed-kit/{lens_id}/ has 0 files with `type: {tier_0}` "
        f"(lens entity_model.tier_0). Observed type distribution: {dist}. "
        f"Downstream graph_analyzer filters on data['type'] == tier_0 — "
        f"0 tier_0 entries means an empty graph after /genesis --seeded."
    )


@pytest.mark.parametrize("lens_id", LENS_IDS)
def test_seed_kit_contributes_to_lens_ontology(
    lens_id: str, repo_root: Path, frontmatter_parser
):
    """Every seed type must be one of the lens's declared tier slots or an
    accepted auxiliary type (person / source / question / force / prompt template).

    This catches drift where a lens's tiers are renamed but seed frontmatter
    still references the old names.
    """
    lens = _load_lens_yaml(repo_root, lens_id)
    em = lens["entity_model"]
    tier_types = {em.get("tier_0"), em.get("tier_1_atom"), em.get("tier_1_cluster")}
    tier_types.discard(None)

    # Auxiliary types permitted across all lenses (not part of entity_model
    # but legitimate seed-kit scaffolding: people, sources, forces, questions,
    # and prompt/template cards used by /prompt).
    aux_types = {
        "person",
        "source",
        "question",
        "force",
        "prompt",
    }

    def is_aux(t: str) -> bool:
        # Accept explicit aux types plus any "*-template" used by /prompt cards.
        return t in aux_types or t.endswith("-template")

    seed_dir = repo_root / "seed-kit" / lens_id
    if not seed_dir.is_dir():
        pytest.skip(f"seed-kit/{lens_id}/ not present")

    dist = _seed_type_distribution(seed_dir, frontmatter_parser)
    unknown = {t: n for t, n in dist.items() if t not in tier_types and not is_aux(t)}
    assert not unknown, (
        f"seed-kit/{lens_id}/ uses types not in lens entity_model "
        f"(tier_0={em.get('tier_0')}, tier_1_atom={em.get('tier_1_atom')}, "
        f"tier_1_cluster={em.get('tier_1_cluster')}) and not in aux set "
        f"{sorted(aux_types)}: {unknown}. Either add them to entity_model "
        f"or migrate frontmatter to a declared type."
    )
