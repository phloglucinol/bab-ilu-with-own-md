"""Tests for tools/gap_runner.py — D2 §9 commitments + A4 contract.

Covers:
  - Deterministic sort of qualifying candidates (same input = same
    output bytes)
  - Adaptive k = max{3, ⌈log₂(N)⌉} formula boundaries
  - Reproducibility across runs on the same vault state
  - User-content preservation below AGENT_MARKER in candidate files
  - Bridge-candidate filtering (zero-shared-tier_0 invariant)
  - Question-stub idempotence (existing files not overwritten)
  - Lens-parameterization: same graph produces different outputs under
    different lens thresholds
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.gap_runner import (
    AGENT_MARKER,
    adaptive_k,
    bridge_candidates,
    format_candidate_block,
    qualify_tier1_candidates,
    write_question_stubs,
    write_tier1_candidates,
)


# ---------------------------------------------------------------------------
# Fixtures — minimal in-memory graph matching graph_analyzer's node/cluster API
# ---------------------------------------------------------------------------


class FakeLens:
    """Minimal stand-in for LensConfig sufficient for gap_runner.

    gap_runner only reads `.id`, `.entity_model`, `.thresholds`. Using a
    fake avoids the lens_loader fixture setup cost for the qualification
    logic tests — the integration tests in test_graph_analyzer_lens.py
    already cover real-lens loading.
    """

    def __init__(
        self,
        lens_id: str = "test-lens",
        *,
        tier_0: str = "work",
        tier_1_atom: str = "motif",
        tier_1_cluster: str = "pathosformel",
        density_multiplier: float = 2.0,
    ):
        self.id = lens_id
        self.entity_model = {
            "tier_0": tier_0,
            "tier_1_atom": tier_1_atom,
            "tier_1_cluster": tier_1_cluster,
        }
        self.thresholds = {
            "cluster_member_min": 3,
            "cluster_min_size": 3,
            "density_multiplier": density_multiplier,
            "orphan_min_degree": 1,
            "domain_min": 3,
        }


def make_node(node_type: str, *, exemplifies: list[str] | None = None) -> dict:
    """Build a node dict matching graph_analyzer.load_wiki's shape."""
    return {
        "type": node_type,
        "frontmatter": {"type": node_type},
        "relations": [
            {"type": "exemplifies", "target": t} for t in (exemplifies or [])
        ],
        "domain": None,
    }


# ---------------------------------------------------------------------------
# adaptive_k
# ---------------------------------------------------------------------------


class TestAdaptiveK:

    def test_k_is_3_for_small_n(self):
        assert adaptive_k(1) == 3
        assert adaptive_k(5) == 3
        assert adaptive_k(8) == 3

    def test_k_grows_with_log2(self):
        # ceil(log2(17)) == 5 so adaptive_k(17) should be 5
        assert adaptive_k(17) == 5
        # ceil(log2(100)) == 7
        assert adaptive_k(100) == 7
        # ceil(log2(5000)) == 13
        assert adaptive_k(5000) == 13

    def test_guards_zero_and_negative(self):
        assert adaptive_k(0) == 3
        assert adaptive_k(-5) == 3


# ---------------------------------------------------------------------------
# qualify_tier1_candidates — D2 §3.3 three-rule filter
# ---------------------------------------------------------------------------


class TestQualifyTier1Candidates:

    def _make_qualifying_vault(self, n_atoms: int = 3, n_works: int = 8):
        """Build a vault with N_atoms atoms each exemplified by ≥k works.

        Default n_works=8 keeps `adaptive_k(n_works) == 3`, so each
        atom's 3 exemplifiers satisfy rule 2. The exemplifier sets are
        wrapped (`w0..w7` cycled) to guarantee rule 3 passes with
        density_multiplier=2.0 while fitting into only 8 works.
        """
        nodes: dict[str, dict] = {}
        work_slugs = [f"w{i}" for i in range(n_works)]
        for w in work_slugs:
            nodes[w] = make_node("work")
        # Each atom gets 3 exemplifiers with wraparound — union converges
        # to n_works so density_proxy = n_works/n_atoms.
        for i in range(n_atoms):
            atom = f"a{i}"
            exemplifiers = [
                work_slugs[(i * 3 + k) % n_works] for k in range(3)
            ]
            nodes[atom] = make_node("motif", exemplifies=exemplifiers)
        clusters = {f"a{i}": 0 for i in range(n_atoms)}
        return nodes, clusters

    def test_minimal_qualifying_cluster_passes(self):
        nodes, clusters = self._make_qualifying_vault(3, 8)
        lens = FakeLens(density_multiplier=2.0)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        assert len(cands) == 1
        assert sorted(cands[0]["atoms"]) == ["a0", "a1", "a2"]
        # With n_works=8 and cyclic assignment, the union covers all 8
        assert len(cands[0]["tier_0_spanning"]) == 8

    def test_rule_1_fails_when_too_few_atoms(self):
        """2-atom cluster below adaptive_k=3 rejected."""
        nodes, clusters = self._make_qualifying_vault(2, 6)
        lens = FakeLens(density_multiplier=2.0)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        assert cands == []

    def test_rule_2_fails_when_atom_has_too_few_exemplifiers(self):
        """Each atom needs ≥ k_tier0 exemplifiers; give one atom 0."""
        nodes, clusters = self._make_qualifying_vault(3, 8)
        nodes["a2"]["relations"] = []  # a2 now has 0 exemplifiers
        lens = FakeLens(density_multiplier=2.0)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        assert cands == []

    def test_rule_3_fails_when_density_proxy_too_low(self):
        """All atoms share the same 3 works → union is 3, density_proxy
        = 3/3 = 1.0 which is below density_multiplier=2.0."""
        nodes: dict[str, dict] = {}
        shared = ["w0", "w1", "w2"]
        for w in shared:
            nodes[w] = make_node("work")
        for i in range(3):
            nodes[f"a{i}"] = make_node("motif", exemplifies=shared)
        clusters = {f"a{i}": 0 for i in range(3)}
        lens = FakeLens(density_multiplier=2.0)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        assert cands == []

    def test_sort_is_deterministic(self):
        """Two communities sort by (size desc, smallest_slug asc).

        Uses disjoint tier-0 sets per cluster so the Chung-Lu null model
        sees meaningful intra-cluster concentration (D2 §3.3 rule 3).
        """
        nodes: dict[str, dict] = {}
        # 14 works — adaptive_k(14)=4, so atoms need ≥4 exemplifiers each.
        for i in range(14):
            nodes[f"w{i}"] = make_node("work")
        # cluster 0 (slug prefix z-): 4 atoms, each with 4 exemplifiers
        # all drawn from w0..w6 (disjoint from cluster 1's pool).
        for i in range(4):
            exs = [f"w{k}" for k in range(4)] if i == 0 else [
                f"w{(i + k) % 7}" for k in range(4)
            ]
            nodes[f"z-a{i}"] = make_node("motif", exemplifies=exs)
        # cluster 1 (slug prefix a-): 3 atoms, 4 exemplifiers each from w7..w13
        for i in range(3):
            exs = [f"w{7 + (i + k) % 7}" for k in range(4)]
            nodes[f"a-a{i}"] = make_node("motif", exemplifies=exs)
        clusters: dict[str, int] = {}
        for i in range(4):
            clusters[f"z-a{i}"] = 0
        for i in range(3):
            clusters[f"a-a{i}"] = 1
        lens = FakeLens(density_multiplier=1.5)
        cands = qualify_tier1_candidates(nodes, clusters, lens)
        # Larger cluster (4 atoms, cluster_id=0) first, even though its
        # smallest slug z-a0 sorts later alphabetically — size-first sort.
        assert [c["cluster_id"] for c in cands] == [0, 1]


# ---------------------------------------------------------------------------
# format_candidate_block — D2 §3.3 exact markdown format
# ---------------------------------------------------------------------------


class TestFormatCandidateBlock:

    def test_stable_format_with_fixed_stamp(self):
        cand = {
            "cluster_id": 0,
            "atoms": ["m1", "m2", "m3"],
            "tier_0_spanning": ["w1", "w2", "w3"],
            "density_proxy": 4.2,
            "suggested_name": "quiet-interior-light",
        }
        out = format_candidate_block(cand, now_stamp="2026-04-19-1030")
        assert "## Candidate 2026-04-19-1030" in out
        assert "Atoms: [[m1]], [[m2]], [[m3]]" in out
        assert "Tier-0 spanning: [[w1]], [[w2]], [[w3]]" in out
        assert "Density ratio: 4.2" in out
        assert '"quiet-interior-light"' in out
        assert "Status: [ ] accept [ ] refine [ ] reject" in out


# ---------------------------------------------------------------------------
# write_tier1_candidates — preserves user edits + reproducible bytes
# ---------------------------------------------------------------------------


class TestWriteTier1Candidates:

    def _build_vault(self, tmp_path: Path) -> Path:
        (tmp_path / "wiki").mkdir()
        return tmp_path

    def test_zero_candidates_emits_placeholder(self, tmp_path):
        vault = self._build_vault(tmp_path)
        lens = FakeLens()
        path = write_tier1_candidates(vault, lens, [], now_stamp="x")
        text = path.read_text(encoding="utf-8")
        assert "no qualifying candidates" in text
        assert AGENT_MARKER in text

    def test_reproducible_bytes(self, tmp_path):
        vault = self._build_vault(tmp_path)
        lens = FakeLens()
        cand = {
            "cluster_id": 0, "atoms": ["m1", "m2", "m3"],
            "tier_0_spanning": ["w1", "w2"], "density_proxy": 3.0,
            "suggested_name": "x",
        }
        p1 = write_tier1_candidates(vault, lens, [cand], now_stamp="2026-01-01-0000")
        bytes1 = p1.read_bytes()
        p2 = write_tier1_candidates(vault, lens, [cand], now_stamp="2026-01-01-0000")
        bytes2 = p2.read_bytes()
        assert bytes1 == bytes2

    def test_preserves_user_content_below_marker(self, tmp_path):
        vault = self._build_vault(tmp_path)
        lens = FakeLens()
        # First write — creates agent block + marker
        write_tier1_candidates(vault, lens, [], now_stamp="s")
        # User appends notes below the marker
        target = vault / ".agent" / "todos" / "pathosformel-candidates.md"
        text = target.read_text(encoding="utf-8")
        target.write_text(text + "\n## User notes\n\nI'm keeping this.\n",
                           encoding="utf-8")
        # Re-run with new candidate — agent block rewrites, user block survives
        cand = {"cluster_id": 0, "atoms": ["a1", "a2", "a3"],
                "tier_0_spanning": ["w"], "density_proxy": 3.0,
                "suggested_name": "new"}
        write_tier1_candidates(vault, lens, [cand], now_stamp="t")
        updated = target.read_text(encoding="utf-8")
        assert "I'm keeping this." in updated
        assert "## Candidate t" in updated

    def test_aesthetic_warburg_uses_legacy_filename(self, tmp_path):
        vault = self._build_vault(tmp_path)
        lens = FakeLens(
            lens_id="aesthetic-warburg",
            tier_1_cluster="panel",
        )
        write_tier1_candidates(vault, lens, [], now_stamp="x")
        legacy = vault / ".agent" / "todos" / "pathosformel-candidates.md"
        assert legacy.exists()
        # And NOT panel-candidates.md
        assert not (vault / ".agent" / "todos" / "panel-candidates.md").exists()

    def test_non_aesthetic_uses_tier_1_cluster_name(self, tmp_path):
        vault = self._build_vault(tmp_path)
        lens = FakeLens(
            lens_id="engineering-alexander",
            tier_1_cluster="pattern-language",
        )
        write_tier1_candidates(vault, lens, [], now_stamp="x")
        assert (vault / ".agent" / "todos" / "pattern-language-candidates.md").exists()


# ---------------------------------------------------------------------------
# bridge_candidates + write_question_stubs — D2 §5
# ---------------------------------------------------------------------------


class TestBridgeCandidates:

    def test_zero_shared_tier_0_and_different_cluster_qualifies(self):
        nodes: dict[str, dict] = {
            "w1": make_node("work"),
            "w2": make_node("work"),
            "a1": make_node("motif", exemplifies=["w1"]),
            "a2": make_node("motif", exemplifies=["w2"]),
        }
        clusters = {"a1": 0, "a2": 1}
        lens = FakeLens()
        pairs = bridge_candidates(None, nodes, clusters, lens)
        assert len(pairs) == 1
        assert pairs[0]["atom_a"] == "a1"
        assert pairs[0]["atom_b"] == "a2"

    def test_shared_tier_0_disqualifies(self):
        nodes: dict[str, dict] = {
            "w1": make_node("work"),
            "a1": make_node("motif", exemplifies=["w1"]),
            "a2": make_node("motif", exemplifies=["w1"]),  # share w1
        }
        clusters = {"a1": 0, "a2": 1}
        lens = FakeLens()
        assert bridge_candidates(None, nodes, clusters, lens) == []

    def test_same_cluster_disqualifies(self):
        nodes: dict[str, dict] = {
            "w1": make_node("work"), "w2": make_node("work"),
            "a1": make_node("motif", exemplifies=["w1"]),
            "a2": make_node("motif", exemplifies=["w2"]),
        }
        clusters = {"a1": 0, "a2": 0}  # same cluster
        lens = FakeLens()
        assert bridge_candidates(None, nodes, clusters, lens) == []


class TestWriteQuestionStubs:

    def test_creates_stub_with_bridge_hash(self, tmp_path):
        (tmp_path / "wiki").mkdir()
        lens = FakeLens(lens_id="test-lens")
        pairs = [{
            "atom_a": "a1", "atom_b": "a2",
            "cluster_a": 0, "cluster_b": 1,
            "slug": "bridge-a1-a2",
        }]
        written = write_question_stubs(tmp_path, lens, pairs)
        assert len(written) == 1
        body = written[0].read_text(encoding="utf-8")
        assert "type: question" in body
        assert "lens: test-lens" in body
        assert "bridge_hash:" in body
        assert "atom_a: a1" in body
        assert "[[a1]]" in body

    def test_idempotent_skips_existing(self, tmp_path):
        (tmp_path / "wiki").mkdir()
        lens = FakeLens()
        pairs = [{
            "atom_a": "a1", "atom_b": "a2",
            "cluster_a": 0, "cluster_b": 1,
            "slug": "bridge-a1-a2",
        }]
        write_question_stubs(tmp_path, lens, pairs)
        # User edits the stub
        path = tmp_path / "wiki" / "questions" / "bridge-a1-a2.md"
        path.write_text("user wrote this", encoding="utf-8")
        # Re-run — existing file not overwritten
        written = write_question_stubs(tmp_path, lens, pairs)
        assert written == []
        assert path.read_text(encoding="utf-8") == "user wrote this"


# ---------------------------------------------------------------------------
# Lens-parameterization — same graph, different thresholds, different output
# ---------------------------------------------------------------------------


class TestLensParameterization:

    def test_same_graph_different_density_multiplier_different_result(self):
        """Density multiplier = the lens-configurable filter between
        qualifying and non-qualifying."""
        nodes: dict[str, dict] = {}
        # 8 works so adaptive_k(8)=3 passes rule 2 for 3-exemplifier atoms
        for i in range(8):
            nodes[f"W{i}"] = make_node("work")
        # 3 atoms with wrapped 3-exemplifier sets — union covers all 8
        # works, density_proxy = 8 / 3 ≈ 2.67
        for i, atom in enumerate(["A1", "A2", "A3"]):
            exs = [f"W{(i * 3 + k) % 8}" for k in range(3)]
            nodes[atom] = make_node("motif", exemplifies=exs)
        clusters = {"A1": 0, "A2": 0, "A3": 0}

        # Strict lens: density_multiplier=5.0 → 2.67 < 5.0 → fail rule 3
        strict = FakeLens(density_multiplier=5.0)
        assert qualify_tier1_candidates(nodes, clusters, strict) == []

        # Loose lens: density_multiplier=2.0 → 2.67 ≥ 2.0 → pass
        loose = FakeLens(density_multiplier=2.0)
        cands = qualify_tier1_candidates(nodes, clusters, loose)
        assert len(cands) == 1
        assert set(cands[0]["atoms"]) == {"A1", "A2", "A3"}
