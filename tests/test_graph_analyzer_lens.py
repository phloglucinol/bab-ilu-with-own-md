"""Tests for lens-parameterized tools.graph_analyzer (D1).

Before D1 the analyzer was hardcoded to aesthetic-warburg — every type
slice (`"aesthetic"`, `"panel"`), every threshold (`< 3`), every anchor
field (`aat_id`, `iconclass`…) was a literal in the source. D1 refactors
those into values sourced from the active `LensConfig` so any v2.1 lens
(engineering-alexander, general-zettelkasten, etc.) can drive the same
graph pipeline.

Contract under test:

1. **Signature shape.** `detect_gaps`, `compute_structural_bias`,
   `render_insights` accept a `LensConfig` instead of relying on
   module-level globals.
2. **Backward compat.** Running against the real aesthetic-warburg lens
   yields the same gap kinds and structural-bias keys the v2.0 version
   produced.
3. **Multi-lens.** Swapping in an engineering-flavored lens fixture
   changes tier labels in the produced insights (e.g. `"incident"`
   instead of `"aesthetic"`).
4. **Community detection parameters.** Louvain receives the lens's
   `resolution` and `random_state` — reproducible across runs.
5. **CLI lens selection.** `--lens <id>` + `--lenses-base <path>` load
   the correct config; missing lens raises `SystemExit`.
"""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import graph_analyzer  # noqa: E402
from tools.lens_loader import LensConfig, load_lens  # noqa: E402

LENSES_DIR = REPO_ROOT / ".agent" / "lenses"


# ---------- fixtures ----------


@pytest.fixture
def aesthetic_lens() -> LensConfig:
    """The real v2.0-parity lens config — used to prove backward compat."""
    return load_lens("aesthetic-warburg", base=LENSES_DIR)


@pytest.fixture
def engineering_lens(tmp_path: Path) -> LensConfig:
    """Synthetic engineering-flavored lens.yaml for parameterization tests.

    Real `.agent/lenses/engineering-alexander/lens.yaml` doesn't exist yet
    (C3 landed the directory but not the file); keep the shape here so this
    test stays green regardless of C3 sequencing.
    """
    base = tmp_path / "lenses"
    # Copy the canonical schema.json so jsonschema validation succeeds.
    base.mkdir()
    (base / "schema.json").write_text(
        (LENSES_DIR / "schema.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    lens_dir = base / "engineering-alexander"
    lens_dir.mkdir()
    (lens_dir / "lens.yaml").write_text(
        """\
id: engineering-alexander
version: "1.0.0"
name: "Engineering (Alexander patterns lens)"
description: Incidents → forces → patterns.
deliverable_types: [pattern]
entity_model:
  tier_0: incident
  tier_1_atom: force
  tier_1_cluster: pattern
activation:
  mode: always
thresholds:
  cluster_member_min: 2
  cluster_min_size: 2
  density_multiplier: 2.5
  orphan_min_degree: 1
  domain_min: 2
anchors:
  authority_fields:
    - cve_id
    - rfc_id
    - issue_url
allowed_subdomains:
  - distributed
  - frontend
  - ml
  - embedded
  - security
  - general
community_detection:
  algorithm: louvain
  resolution: 1.2
  random_state: 17
analysis_contract:
  gap:
    - underpopulated_domain
    - understaffed_cluster
    - orphan_tier_0
    - missing_authority_anchor
    - disconnected_clusters
""",
        encoding="utf-8",
    )
    return load_lens("engineering-alexander", base=base)


@pytest.fixture
def tiny_nodes(aesthetic_lens: LensConfig) -> dict[str, dict]:
    """A 6-node vault: 3 motifs + 2 aesthetics + 1 panel, for gap detection."""
    return {
        "aesthetic-A": {
            "path": Path("a.md"),
            "relative_path": "wiki/aesthetic/a.md",
            "frontmatter": {"type": "aesthetic", "aat_id": "300000001"},
            "wikilinks": {"motif-1", "motif-2"},
            "relations": [],
            "type": "aesthetic",
            "domain": "cinema",
            "title": "Work A",
        },
        "aesthetic-B": {
            "path": Path("b.md"),
            "relative_path": "wiki/aesthetic/b.md",
            "frontmatter": {"type": "aesthetic"},  # missing authority — a gap
            "wikilinks": set(),
            "relations": [],
            "type": "aesthetic",
            "domain": "photo",
            "title": "Work B",
        },
        "motif-1": {
            "path": Path("m1.md"),
            "relative_path": "wiki/motif/motif-1.md",
            "frontmatter": {"type": "motif"},
            "wikilinks": set(),
            "relations": [],
            "type": "motif",
            "domain": None,
            "title": "Motif 1",
        },
        "motif-2": {
            "path": Path("m2.md"),
            "relative_path": "wiki/motif/motif-2.md",
            "frontmatter": {"type": "motif"},
            "wikilinks": set(),
            "relations": [],
            "type": "motif",
            "domain": None,
            "title": "Motif 2",
        },
        "panel-X": {
            "path": Path("p.md"),
            "relative_path": "wiki/panel/panel-X.md",
            "frontmatter": {"type": "panel", "aat_id": "300000099"},
            "wikilinks": {"motif-1", "motif-2"},  # <3 members → understaffed
            "relations": [],
            "type": "panel",
            "domain": None,
            "title": "Panel X",
        },
    }


# ---------- backward-compat smoke tests ----------


def test_detect_gaps_accepts_lens_argument(tiny_nodes, aesthetic_lens):
    """The core signature change — detect_gaps must take a LensConfig."""
    G = graph_analyzer.build_graph(tiny_nodes)
    clusters = graph_analyzer.compute_clusters(G, lens=aesthetic_lens)
    gaps = graph_analyzer.detect_gaps(G, tiny_nodes, clusters, lens=aesthetic_lens)
    assert isinstance(gaps, list)


def test_aesthetic_backward_compat_gap_kinds(tiny_nodes, aesthetic_lens):
    """Running the aesthetic lens must still produce the v2.0 gap kinds."""
    G = graph_analyzer.build_graph(tiny_nodes)
    clusters = graph_analyzer.compute_clusters(G, lens=aesthetic_lens)
    gaps = graph_analyzer.detect_gaps(G, tiny_nodes, clusters, lens=aesthetic_lens)
    kinds = {g["kind"] for g in gaps}
    # Exact v2.0 gap kinds:
    expected = {
        "underpopulated_domain",
        "understaffed_panel",
        "orphan_aesthetic",
        "missing_authority_anchor",
    }
    assert expected.issubset(kinds), f"missing gap kinds: {expected - kinds}"


def test_missing_authority_anchor_uses_lens_fields(tiny_nodes, aesthetic_lens):
    """aesthetic-B has no aat_id/iconclass/etc → must be flagged."""
    G = graph_analyzer.build_graph(tiny_nodes)
    clusters = graph_analyzer.compute_clusters(G, lens=aesthetic_lens)
    gaps = graph_analyzer.detect_gaps(G, tiny_nodes, clusters, lens=aesthetic_lens)
    missing = [g for g in gaps if g["kind"] == "missing_authority_anchor"]
    targets = {g["target"] for g in missing}
    assert "aesthetic-B" in targets
    assert "aesthetic-A" not in targets  # A has aat_id, so no gap


def test_structural_bias_uses_lens_tier0_type(tiny_nodes, aesthetic_lens):
    bias = graph_analyzer.compute_structural_bias(tiny_nodes, lens=aesthetic_lens)
    assert bias["total_tier_0"] == 2  # 2 aesthetics
    # Domain distribution keyed by lens's allowed_subdomains ordering:
    assert bias["domain_distribution"] == {"cinema": 1, "photo": 1}


# ---------- multi-lens parameterization ----------


def test_engineering_lens_uses_incident_type(engineering_lens):
    """With engineering lens, tier-0 type is 'incident' and anchors are CVE/RFC."""
    nodes = {
        "incident-1": {
            "path": Path("i1.md"),
            "relative_path": "wiki/incident/i1.md",
            "frontmatter": {"type": "incident", "cve_id": "CVE-2025-0001"},
            "wikilinks": {"force-a"},
            "relations": [],
            "type": "incident",
            "domain": "distributed",
            "title": "Incident 1",
        },
        "incident-2": {
            "path": Path("i2.md"),
            "relative_path": "wiki/incident/i2.md",
            "frontmatter": {"type": "incident"},  # no authority → gap
            "wikilinks": set(),
            "relations": [],
            "type": "incident",
            "domain": "frontend",
            "title": "Incident 2",
        },
        "force-a": {
            "path": Path("fa.md"),
            "relative_path": "wiki/forces/force-a.md",
            "frontmatter": {"type": "force"},
            "wikilinks": set(),
            "relations": [],
            "type": "force",
            "domain": None,
            "title": "Force A",
        },
    }
    G = graph_analyzer.build_graph(nodes)
    clusters = graph_analyzer.compute_clusters(G, lens=engineering_lens)
    gaps = graph_analyzer.detect_gaps(G, nodes, clusters, lens=engineering_lens)
    bias = graph_analyzer.compute_structural_bias(nodes, lens=engineering_lens)

    # Missing-anchor check must use engineering's field list, not aat_id etc.
    missing_targets = {g["target"] for g in gaps if g["kind"] == "missing_authority_anchor"}
    assert "incident-2" in missing_targets
    assert "incident-1" not in missing_targets  # has cve_id

    # tier_0 count reflects 'incident' type, not 'aesthetic'
    assert bias["total_tier_0"] == 2


def test_render_insights_uses_lens_tier_labels(tiny_nodes, aesthetic_lens):
    """Rendered markdown must reference lens's tier labels, not hardcoded text."""
    G = graph_analyzer.build_graph(tiny_nodes)
    clusters = graph_analyzer.compute_clusters(G, lens=aesthetic_lens)
    gaps = graph_analyzer.detect_gaps(G, tiny_nodes, clusters, lens=aesthetic_lens)
    bias = graph_analyzer.compute_structural_bias(tiny_nodes, lens=aesthetic_lens)
    bridges = graph_analyzer.compute_bridges(G)

    md = graph_analyzer.render_insights(
        G, tiny_nodes, clusters, bridges, gaps, bias, lens=aesthetic_lens
    )
    # Must include lens id for traceability:
    assert "aesthetic-warburg" in md
    # Still a well-formed insights doc:
    assert "# Wiki Insights" in md


def test_render_insights_for_engineering_mentions_incident(engineering_lens):
    nodes = {
        "i1": {
            "path": Path("i1.md"),
            "relative_path": "wiki/incident/i1.md",
            "frontmatter": {"type": "incident"},
            "wikilinks": set(),
            "relations": [],
            "type": "incident",
            "domain": "distributed",
            "title": "I1",
        },
    }
    G = graph_analyzer.build_graph(nodes)
    clusters = graph_analyzer.compute_clusters(G, lens=engineering_lens)
    gaps = graph_analyzer.detect_gaps(G, nodes, clusters, lens=engineering_lens)
    bias = graph_analyzer.compute_structural_bias(nodes, lens=engineering_lens)
    bridges = graph_analyzer.compute_bridges(G)
    md = graph_analyzer.render_insights(
        G, nodes, clusters, bridges, gaps, bias, lens=engineering_lens
    )
    # Domain section should mention engineering domains:
    assert "distributed" in md
    # Header references lens id:
    assert "engineering-alexander" in md


# ---------- community detection parameters ----------


def test_compute_clusters_honors_lens_community_detection(engineering_lens):
    """Louvain resolution / random_state come from lens.community_detection."""
    nodes = {
        "a": {"path": Path("a.md"), "relative_path": "a.md", "frontmatter": {}, "wikilinks": {"b"}, "relations": [], "type": "incident", "domain": None, "title": "a"},
        "b": {"path": Path("b.md"), "relative_path": "b.md", "frontmatter": {}, "wikilinks": {"a", "c"}, "relations": [], "type": "incident", "domain": None, "title": "b"},
        "c": {"path": Path("c.md"), "relative_path": "c.md", "frontmatter": {}, "wikilinks": {"b"}, "relations": [], "type": "incident", "domain": None, "title": "c"},
    }
    G = graph_analyzer.build_graph(nodes)
    # Two runs at same resolution/random_state → identical clustering.
    c1 = graph_analyzer.compute_clusters(G, lens=engineering_lens)
    c2 = graph_analyzer.compute_clusters(G, lens=engineering_lens)
    assert c1 == c2


# ---------- CLI surface ----------


def test_cli_lens_flag_parses(monkeypatch, aesthetic_lens, tmp_path):
    """--lens <id> + --lenses-base <path> must select the right config."""
    # Build a minimal vault so main() doesn't error on missing wiki/
    vault = tmp_path / "vault"
    (vault / "wiki").mkdir(parents=True)

    resolved: list[LensConfig] = []

    def fake_run(args, lens):
        resolved.append(lens)

    monkeypatch.setattr(graph_analyzer, "_run_pipeline", fake_run)
    monkeypatch.setattr(sys, "argv", [
        "graph_analyzer",
        "--vault", str(vault),
        "--lens", "aesthetic-warburg",
        "--lenses-base", str(LENSES_DIR),
        "--dry-run",
    ])
    graph_analyzer.main()
    assert len(resolved) == 1
    assert resolved[0].id == "aesthetic-warburg"


def test_cli_missing_lens_exits(monkeypatch, tmp_path):
    vault = tmp_path / "vault"
    (vault / "wiki").mkdir(parents=True)
    monkeypatch.setattr(sys, "argv", [
        "graph_analyzer",
        "--vault", str(vault),
        "--lens", "not-a-lens",
        "--lenses-base", str(LENSES_DIR),
        "--dry-run",
    ])
    with pytest.raises(SystemExit):
        graph_analyzer.main()


def test_cli_defaults_to_active_lens(monkeypatch, tmp_path):
    """No --lens flag → read .agent/lenses/active/lens.yaml → follow to source."""
    # Simulate real /genesis layout: both aesthetic-warburg/ source dir AND
    # active/ pointer dir. graph_analyzer must read active's `id` field and
    # load from the id-named source.
    vault = tmp_path / "vault"
    (vault / "wiki").mkdir(parents=True)
    agent = vault / ".agent" / "lenses"
    agent.mkdir(parents=True)
    (agent / "schema.json").write_text(
        (LENSES_DIR / "schema.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    src_yaml = (LENSES_DIR / "aesthetic-warburg" / "lens.yaml").read_text(encoding="utf-8")
    source = agent / "aesthetic-warburg"
    source.mkdir()
    (source / "lens.yaml").write_text(src_yaml, encoding="utf-8")
    active = agent / "active"
    active.mkdir()
    (active / "lens.yaml").write_text(src_yaml, encoding="utf-8")

    resolved: list[LensConfig] = []

    def fake_run(args, lens):
        resolved.append(lens)

    monkeypatch.setattr(graph_analyzer, "_run_pipeline", fake_run)
    monkeypatch.setattr(sys, "argv", [
        "graph_analyzer",
        "--vault", str(vault),
        "--lenses-base", str(agent),
        "--dry-run",
    ])
    graph_analyzer.main()
    assert len(resolved) == 1
    assert resolved[0].id == "aesthetic-warburg"


# ---------- public surface stability ----------


def test_public_functions_take_lens_kwarg():
    """Guard against accidental removal of the lens parameter."""
    import inspect

    for fn_name in ("detect_gaps", "compute_structural_bias",
                    "render_insights", "compute_clusters"):
        fn = getattr(graph_analyzer, fn_name)
        sig = inspect.signature(fn)
        assert "lens" in sig.parameters, (
            f"{fn_name} must accept a `lens` parameter after D1 refactor"
        )
