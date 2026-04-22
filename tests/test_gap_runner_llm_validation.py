"""R2 · LLM validation layer + null-model density tests for gap_runner.

Covers:
  - Chung-Lu null-model density ratio computed per D2 §3.3 rule 3
  - Null model degenerates gracefully (empty projection, single
    cluster) and falls back to the legacy tier-0 coverage proxy
  - Bridge-candidate LLM gate per D2 §5 rule 3:
      * accepted when similarity ≥ threshold
      * rejected below threshold
      * threshold per lens via lens.thresholds.gap_llm_similarity
      * backwards compatible when no llm_client is supplied
  - MockLLMClient replays frozen fixture responses (CI hermetic)
  - Snapshot regression on canonical 2-cluster vault
"""

from __future__ import annotations

import json
import warnings
from pathlib import Path
from typing import Any

import pytest

from tools.gap_runner import (
    DEFAULT_GAP_LLM_SIMILARITY,
    _build_atom_projection,
    bridge_candidates,
    null_model_density_ratio,
    qualify_tier1_candidates,
)


FIXTURES = Path(__file__).parent / "fixtures" / "llm_responses" / "R2"


# ---------------------------------------------------------------------------
# Test doubles
# ---------------------------------------------------------------------------


class FakeLens:
    """Mirrors the minimal LensConfig surface gap_runner reads."""

    def __init__(
        self,
        lens_id: str = "test-lens",
        *,
        tier_0: str = "work",
        tier_1_atom: str = "motif",
        tier_1_cluster: str = "pathosformel",
        density_multiplier: float = 2.0,
        gap_llm_similarity: float | None = None,
    ):
        self.id = lens_id
        self.entity_model = {
            "tier_0": tier_0,
            "tier_1_atom": tier_1_atom,
            "tier_1_cluster": tier_1_cluster,
        }
        self.thresholds: dict[str, Any] = {
            "cluster_member_min": 3,
            "cluster_min_size": 3,
            "density_multiplier": density_multiplier,
            "orphan_min_degree": 1,
            "domain_min": 3,
        }
        if gap_llm_similarity is not None:
            self.thresholds["gap_llm_similarity"] = gap_llm_similarity


class MockLLMClient:
    """Replays frozen similarity scores from a fixture JSON file.

    Fixture format: `{"pairs": {"<a>|<b>": float}, "lens_id": str}`.
    Keys are sorted lexicographically so lookups are order-independent.
    Missing pairs return 0.0 — CI-hermetic, no real LLM call.
    """

    def __init__(self, fixture_path: Path):
        data = json.loads(fixture_path.read_text(encoding="utf-8"))
        self.pairs: dict[str, float] = data.get("pairs", {})
        self.fixture_lens_id: str | None = data.get("lens_id")
        self.calls: list[tuple[str, str, str]] = []

    def similarity(self, atom_a: str, atom_b: str, *, lens_id: str) -> float:
        key = "|".join(sorted([atom_a, atom_b]))
        self.calls.append((atom_a, atom_b, lens_id))
        return float(self.pairs.get(key, 0.0))


def make_node(node_type: str, *, exemplifies: list[str] | None = None) -> dict:
    return {
        "type": node_type,
        "frontmatter": {"type": node_type},
        "relations": [
            {"type": "exemplifies", "target": t} for t in (exemplifies or [])
        ],
        "domain": None,
    }


def _build_two_cluster_vault() -> tuple[dict[str, dict], dict[str, int]]:
    """Canonical vault used by snapshot + multi-cluster tests.

    14 works split in two disjoint pools; 4 atoms cluster over w0..w6,
    3 atoms cluster over w7..w13. Each atom has 4 exemplifiers (matches
    adaptive_k(14) = 4).
    """
    nodes: dict[str, dict] = {}
    for i in range(14):
        nodes[f"w{i}"] = make_node("work")
    for i in range(4):
        exs = (
            [f"w{k}" for k in range(4)]
            if i == 0
            else [f"w{(i + k) % 7}" for k in range(4)]
        )
        nodes[f"z-a{i}"] = make_node("motif", exemplifies=exs)
    for i in range(3):
        exs = [f"w{7 + (i + k) % 7}" for k in range(4)]
        nodes[f"a-a{i}"] = make_node("motif", exemplifies=exs)
    clusters = {f"z-a{i}": 0 for i in range(4)}
    clusters.update({f"a-a{i}": 1 for i in range(3)})
    return nodes, clusters


# ---------------------------------------------------------------------------
# Null-model density
# ---------------------------------------------------------------------------


class TestNullModelDensity:

    def test_null_model_ratio_exceeds_one_for_dense_cluster(self):
        """In the canonical 2-cluster vault both clusters are dense
        relative to the degree-preserving null."""
        nodes, clusters = _build_two_cluster_vault()
        lens = FakeLens(density_multiplier=1.5)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        ratios = {c["cluster_id"]: c["density_ratio"] for c in cands}
        assert ratios[0] > 1.0
        assert ratios[1] > 1.0

    def test_null_model_ratio_zero_when_projection_empty(self):
        """Empty projection → ratio 0.0 (undefined)."""
        assert null_model_density_ratio([], {}, {}, 0.0) == 0.0
        assert null_model_density_ratio(["a1", "a2"], {}, {}, 0.0) == 0.0

    def test_null_model_ratio_zero_for_singleton_cluster(self):
        """Single-atom cluster has no internal edges → ratio 0.0."""
        pair_weights = {("a1", "a2"): 0.5}
        degrees = {"a1": 0.5, "a2": 0.5}
        assert null_model_density_ratio(["a1"], pair_weights, degrees, 0.5) == 0.0

    def test_density_ratio_in_candidate_dict(self):
        """Candidate dicts carry the new density_ratio key alongside
        the legacy density_proxy key for snapshot continuity."""
        nodes, clusters = _build_two_cluster_vault()
        lens = FakeLens(density_multiplier=1.5)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        for c in cands:
            assert "density_ratio" in c
            assert "density_proxy" in c

    def test_null_model_gate_rejects_cluster_below_multiplier(self):
        """Strict density_multiplier filters out clusters that pass the
        legacy proxy but fail the null-model comparison."""
        nodes, clusters = _build_two_cluster_vault()
        # Cluster 0's ratio ≈ 2.14, cluster 1's ≈ 4.08 under the
        # diagonal-corrected Chung-Lu formula (see snapshot fixture).
        # Multiplier 3.0 sits between them and rejects cluster 0 only.
        lens = FakeLens(density_multiplier=3.0)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        ids = {c["cluster_id"] for c in cands}
        assert ids == {1}, f"expected only cluster 1 to pass, got {ids}"

    def test_legacy_density_proxy_still_populated(self):
        """Back-compat: the old density_proxy key stays present so older
        snapshots / docs referencing it do not break."""
        nodes, clusters = _build_two_cluster_vault()
        lens = FakeLens(density_multiplier=1.0)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        assert all(c["density_proxy"] > 0 for c in cands)

    def test_null_model_active_on_canonical_vault(self):
        """The canonical 2-cluster vault has ≥2 populated clusters and a
        non-empty projection → the null-model branch MUST be active and
        the legacy-proxy fallback warning MUST NOT fire. Guards against
        a silent regression where the fallback cutoff masks real null-
        model behavior."""
        nodes, clusters = _build_two_cluster_vault()
        lens = FakeLens(density_multiplier=1.0)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            qualify_tier1_candidates(nodes, clusters, lens)
        fallback_warnings = [
            w for w in caught
            if issubclass(w.category, RuntimeWarning)
            and "null-model density fallback" in str(w.message)
        ]
        assert fallback_warnings == [], (
            "null-model fallback fired on canonical two-cluster vault; "
            "expected the null-model branch to be active"
        )


# ---------------------------------------------------------------------------
# Bridge LLM validation
# ---------------------------------------------------------------------------


class TestBridgeLLMValidation:

    def _build_bridge_vault(self) -> tuple[dict, dict]:
        """3 atoms, 2 works; atoms live in 3 different clusters; no two
        atoms share a tier-0 exemplifier → 3 candidate bridge pairs."""
        nodes: dict[str, dict] = {
            "wa": make_node("work"),
            "wb": make_node("work"),
            "wc": make_node("work"),
            "crouching-figure": make_node("motif", exemplifies=["wa"]),
            "nymph-in-motion": make_node("motif", exemplifies=["wb"]),
            "storm-at-sea": make_node("motif", exemplifies=["wc"]),
        }
        clusters = {
            "crouching-figure": 0,
            "nymph-in-motion": 1,
            "storm-at-sea": 2,
        }
        return nodes, clusters

    def test_bridge_accepted_when_similarity_above_threshold(self):
        nodes, clusters = self._build_bridge_vault()
        lens = FakeLens(lens_id="aesthetic-warburg", gap_llm_similarity=0.6)
        client = MockLLMClient(FIXTURES / "aesthetic_warburg_bridges.json")
        pairs = bridge_candidates(None, nodes, clusters, lens, llm_client=client)
        # Only crouching-figure × nymph-in-motion has similarity 0.82 ≥ 0.6.
        assert len(pairs) == 1
        assert {pairs[0]["atom_a"], pairs[0]["atom_b"]} == {
            "crouching-figure",
            "nymph-in-motion",
        }
        assert pairs[0]["similarity"] == 0.82

    def test_bridge_rejected_when_similarity_below_threshold(self):
        nodes, clusters = self._build_bridge_vault()
        lens = FakeLens(lens_id="aesthetic-warburg", gap_llm_similarity=0.9)
        client = MockLLMClient(FIXTURES / "aesthetic_warburg_bridges.json")
        pairs = bridge_candidates(None, nodes, clusters, lens, llm_client=client)
        assert pairs == []

    def test_mock_llm_client_replays_fixture(self):
        """MockLLMClient returns deterministic scores from the fixture;
        the `calls` log captures what was asked."""
        client = MockLLMClient(FIXTURES / "aesthetic_warburg_bridges.json")
        score_hit = client.similarity(
            "crouching-figure", "nymph-in-motion", lens_id="aesthetic-warburg"
        )
        score_miss = client.similarity(
            "unknown-a", "unknown-b", lens_id="aesthetic-warburg"
        )
        assert score_hit == 0.82
        assert score_miss == 0.0
        assert len(client.calls) == 2
        # Order-independence: swapping arguments hits the same fixture key.
        score_swapped = client.similarity(
            "nymph-in-motion", "crouching-figure", lens_id="aesthetic-warburg"
        )
        assert score_swapped == 0.82

    def test_lens_specific_similarity_threshold_used(self):
        """Same bridge vault, two lenses with different thresholds yields
        different bridge-candidate output even though the LLM fixture
        returns identical scores."""
        nodes, clusters = self._build_bridge_vault()
        client = MockLLMClient(FIXTURES / "aesthetic_warburg_bridges.json")

        strict = FakeLens(lens_id="aesthetic-warburg", gap_llm_similarity=0.85)
        lenient = FakeLens(lens_id="aesthetic-warburg", gap_llm_similarity=0.5)

        strict_pairs = bridge_candidates(
            None, nodes, clusters, strict, llm_client=client
        )
        lenient_pairs = bridge_candidates(
            None, nodes, clusters, lenient, llm_client=client
        )
        assert len(strict_pairs) == 0
        assert len(lenient_pairs) == 1

    def test_explicit_min_similarity_override_wins_over_lens_default(self):
        nodes, clusters = self._build_bridge_vault()
        lens = FakeLens(lens_id="aesthetic-warburg", gap_llm_similarity=0.2)
        client = MockLLMClient(FIXTURES / "aesthetic_warburg_bridges.json")
        # Caller passes an explicit higher threshold.
        pairs = bridge_candidates(
            None, nodes, clusters, lens,
            llm_client=client, min_similarity=0.95,
        )
        assert pairs == []

    def test_no_llm_client_is_backwards_compatible(self):
        """When llm_client is None the gate is skipped entirely — same
        output as pre-R2 behavior."""
        nodes, clusters = self._build_bridge_vault()
        lens = FakeLens(lens_id="aesthetic-warburg")
        pairs = bridge_candidates(None, nodes, clusters, lens)
        assert len(pairs) == 3
        assert all("similarity" not in p for p in pairs)

    def test_default_threshold_matches_spec_default(self):
        """D2 §5 pins the default gap_llm_similarity at 0.6. When a lens
        omits the threshold, the module constant must equal that default
        so the spec and implementation never drift."""
        assert DEFAULT_GAP_LLM_SIMILARITY == 0.6

    def test_min_similarity_zero_explicit_is_respected(self):
        """`min_similarity=0.0` is a valid explicit threshold (accept
        every LLM-scored pair) and MUST NOT be treated as unset / fall
        back to the lens default. Guards against a classic
        `if not min_similarity:` truthiness bug."""
        nodes, clusters = self._build_bridge_vault()
        # Lens default is 0.6 — if 0.0 were silently treated as unset,
        # the lens default would apply and drop every pair scored below
        # 0.6. With explicit 0.0 we expect all 3 pairs retained.
        lens = FakeLens(lens_id="aesthetic-warburg", gap_llm_similarity=0.6)
        client = MockLLMClient(FIXTURES / "aesthetic_warburg_bridges.json")
        pairs = bridge_candidates(
            None, nodes, clusters, lens,
            llm_client=client, min_similarity=0.0,
        )
        # Every structural bridge survives because 0.0 is the actual
        # threshold; missing fixture pairs score 0.0 which still satisfies >=.
        assert len(pairs) == 3
        # similarity annotation present on every surviving pair
        assert all("similarity" in p for p in pairs)


# ---------------------------------------------------------------------------
# Snapshot regression
# ---------------------------------------------------------------------------


class TestSnapshotRegression:

    def test_snapshot_density_ratio_matches_fixture(self):
        """Freezes the null-model ratios on the canonical 2-cluster
        vault so algorithmic tweaks that change the numerics require a
        deliberate fixture refresh."""
        snapshot = json.loads(
            (FIXTURES / "density_snapshot.json").read_text(encoding="utf-8")
        )
        expected = snapshot["density_ratios"]
        nodes, clusters = _build_two_cluster_vault()
        lens = FakeLens(density_multiplier=1.0)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        actual = {c["cluster_id"]: c["density_ratio"] for c in cands}
        assert actual[0] == pytest.approx(expected["cluster_0"], abs=1e-4)
        assert actual[1] == pytest.approx(expected["cluster_1"], abs=1e-4)

    def test_projection_is_deterministic(self):
        """Same nodes/lens → byte-identical projection."""
        nodes, _ = _build_two_cluster_vault()
        lens = FakeLens()
        a1, p1, d1, t1 = _build_atom_projection(nodes, lens)
        a2, p2, d2, t2 = _build_atom_projection(nodes, lens)
        assert a1 == a2
        assert p1 == p2
        assert d1 == d2
        assert t1 == t2
