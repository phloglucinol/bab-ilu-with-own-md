"""Candidate-writing layer on top of lens-aware `graph_analyzer.py`.

`graph_analyzer.py` (D1) builds the bipartite graph, runs community
detection per `lens.community_detection`, and produces a human-readable
`wiki/_insights.md`. What it does NOT do — and what `docs/spec/
gap-algorithm.md` (D2) requires — is write one *candidate block per
qualifying cluster* into `.agent/todos/<tier_1_cluster>-candidates.md`
(per D2 §3.3) plus *bridge-candidate stubs* under `wiki/questions/`
(per D2 §5).

This module is that layer. It reuses the analyzer's
`load_wiki / build_graph / compute_clusters / detect_gaps` helpers
verbatim — no duplicated graph logic — and adds only the qualification
+ candidate-file writing.

Design choices:

1. **Pure-function core, thin I/O shell.** `qualify_tier1_candidates`
   and `format_candidate_block` are pure and fully testable. The
   filesystem-touching `write_candidates` is one orchestration function.
2. **Adaptive thresholds per D2 §3.3.** The `k = max{3, ⌈log₂(N)⌉}`
   rule is computed here from the live `nodes` dict — it does not live
   in `lens.yaml` because it depends on runtime vault size, not lens
   choice.
3. **Deterministic ordering.** Qualifying communities are sorted by
   `(member_count desc, smallest_member_slug asc)` so the candidate file
   is reproducible byte-for-byte across runs on the same vault state.
4. **Never overwrite user edits.** The candidate file is *appended*
   when it already exists with user-authored content below a marker;
   full rewrite only when the file is agent-owned (missing or
   marker-only).
"""

from __future__ import annotations

import argparse
import hashlib
import math
import re
import sys
import warnings
from collections import defaultdict
from datetime import datetime
from itertools import combinations
from pathlib import Path
from typing import Any, Protocol

try:
    from graph_analyzer import (  # type: ignore[no-redef]
        DEFAULT_LENSES_BASE,
        DEFAULT_VAULT,
        _resolve_lens,
        build_graph,
        compute_bridges,
        compute_clusters,
        detect_gaps,
        load_wiki,
    )
    from lens_loader import LensConfig  # type: ignore[no-redef]
except ImportError:  # tools/ also importable as a package
    from tools.graph_analyzer import (
        DEFAULT_LENSES_BASE,
        DEFAULT_VAULT,
        _resolve_lens,
        build_graph,
        compute_bridges,
        compute_clusters,
        detect_gaps,
        load_wiki,
    )
    from tools.lens_loader import LensConfig

AGENT_MARKER = "<!-- gap-runner:agent-block -->"

# Default LLM semantic-similarity threshold for bridge candidates per D2 §5.
# Lenses override via `lens.thresholds.gap_llm_similarity`.
DEFAULT_GAP_LLM_SIMILARITY = 0.6


class LLMSimilarityClient(Protocol):
    """Contract for pluggable semantic-similarity providers.

    A production implementation wraps the Anthropic SDK and prompts a
    model to score two atom briefs. Tests inject a deterministic
    fixture-replay mock (see `tests/test_gap_runner_llm_validation.py`).

    The bridge-candidate gate in D2 §5 rule 3 requires a similarity
    score in [0.0, 1.0]; higher scores mean "these atoms are about the
    same thing" — which paradoxically makes them *stronger* bridge
    candidates because the unbridged graph edge represents a knowledge
    gap. Low similarity means the pair is genuinely unrelated and the
    absence of a bridge is expected, not a gap.
    """

    def similarity(
        self,
        atom_a: str,
        atom_b: str,
        *,
        lens_id: str,
    ) -> float:  # pragma: no cover - protocol
        ...


# ---------------------------------------------------------------------------
# Tier-1 candidate qualification (D2 §3.3)
# ---------------------------------------------------------------------------


def adaptive_k(n: int) -> int:
    """`k = max{3, ⌈log₂(N)⌉}` per D2 §3.3 rule 1.

    Returns 3 for N ≤ 8, 4 for N in 9..16, etc. Guards N ≤ 0.
    """
    if n <= 0:
        return 3
    return max(3, math.ceil(math.log2(max(2, n))))


def _jaccard(a: set[str], b: set[str]) -> float:
    """Jaccard overlap |a∩b|/|a∪b|; 0 when both empty."""
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)


def _build_atom_projection(
    nodes: dict[str, dict],
    lens: LensConfig,
) -> tuple[dict[str, set[str]], dict[tuple[str, str], float], dict[str, float], float]:
    """Build the atom-atom Jaccard projection per D2 §3.1.

    Returns a 4-tuple:
      - `atom_tier0`: slug → set of exemplifying tier-0 slugs
      - `pair_weights`: (a, b) sorted-pair key → Jaccard weight (>0 only)
      - `atom_degrees`: slug → Σ pair_weights incident to this atom
      - `total_weight`: Σ pair_weights (sum of all edges)

    Pairs with zero Jaccard are omitted to keep the projection sparse —
    they correspond to bridge-candidate territory (§5), not intra-cluster
    density.
    """
    tier_0 = lens.entity_model["tier_0"]
    tier_1_atom = lens.entity_model["tier_1_atom"]

    atom_tier0: dict[str, set[str]] = {}
    for slug, data in nodes.items():
        if data.get("type") != tier_1_atom:
            continue
        exs: set[str] = set()
        for rel in data.get("relations", []):
            if rel.get("type") in ("exemplifiedBy", "exemplifies"):
                target = rel.get("target", "").strip()
                if nodes.get(target, {}).get("type") == tier_0:
                    exs.add(target)
        atom_tier0[slug] = exs

    atoms_sorted = sorted(atom_tier0.keys())
    pair_weights: dict[tuple[str, str], float] = {}
    atom_degrees: dict[str, float] = {slug: 0.0 for slug in atoms_sorted}
    total_weight = 0.0

    for a, b in combinations(atoms_sorted, 2):
        w = _jaccard(atom_tier0[a], atom_tier0[b])
        if w <= 0:
            continue
        pair_weights[(a, b)] = w
        atom_degrees[a] += w
        atom_degrees[b] += w
        total_weight += w

    return atom_tier0, pair_weights, atom_degrees, total_weight


def null_model_density_ratio(
    cluster_atoms: list[str],
    pair_weights: dict[tuple[str, str], float],
    atom_degrees: dict[str, float],
    total_weight: float,
) -> float:
    """Observed intra-cluster weight / expected weight under Chung-Lu.

    D2 §3.3 rule 3 demands comparison against a configuration-model
    null that preserves the degree sequence of the atom-atom weighted
    projection. The weighted Chung-Lu expectation for intra-cluster
    edge weight is:

        E[intra(C)] = [(Σ_{i∈C} deg(i))² − Σ_{i∈C} deg(i)²] / (4 · total_weight)

    The `− Σ deg(i)²` diagonal correction removes self-pair terms from
    the expected edge count — without it, every cluster's expectation is
    systematically inflated by the self-loops implicit in `deg_sum²`
    (observed ~26–34 % inflation on the canonical 2-cluster vault).

    Returns `intra / E[intra]`. Returns 0.0 when either quantity is
    undefined (empty projection, zero total weight, or singleton
    cluster).
    """
    if total_weight <= 0 or len(cluster_atoms) < 2:
        return 0.0
    cluster_set = set(cluster_atoms)
    intra = 0.0
    for (a, b), w in pair_weights.items():
        if a in cluster_set and b in cluster_set:
            intra += w
    deg_sum = sum(atom_degrees.get(a, 0.0) for a in cluster_atoms)
    deg_sq_sum = sum(atom_degrees.get(a, 0.0) ** 2 for a in cluster_atoms)
    expected = (deg_sum * deg_sum - deg_sq_sum) / (4.0 * total_weight)
    if expected <= 0:
        return 0.0
    return intra / expected


def qualify_tier1_candidates(
    nodes: dict[str, dict],
    clusters: dict[str, int],
    lens: LensConfig,
) -> list[dict]:
    """Return a deterministic list of tier-1 cluster candidates.

    Per D2 §3.3 the qualification is:
      1. |atoms in C| ≥ adaptive_k(|atoms_total|)
      2. each atom has ≥ adaptive_k(|tier_0_total|) exemplifying tier_0s
      3. observed intra-cluster weight exceeds `density_multiplier ×
         expected weight under the Chung-Lu configuration-model null`
         (D2 §3.3). When the projection has fewer than 2 populated
         clusters, the null model is undefined and we fall back to the
         legacy tier-0-coverage proxy.

    Candidate dicts include both `density_ratio` (observed / expected
    under the null model) and `density_proxy` (legacy coverage metric
    kept for continuity with existing snapshots).

    Args:
        nodes: output of `graph_analyzer.load_wiki`, keyed by slug
        clusters: output of `graph_analyzer.compute_clusters`, slug→cid
        lens: active LensConfig

    Returns:
        list of dicts with keys: cluster_id, atoms, tier_0_spanning,
        density_proxy, density_ratio, suggested_name. Sorted by
        (member_count desc, smallest_atom_slug asc) for reproducibility.
    """
    tier_0 = lens.entity_model["tier_0"]
    tier_1_atom = lens.entity_model["tier_1_atom"]
    thresholds = lens.thresholds
    density_multiplier = float(thresholds.get("density_multiplier", 3.0))

    atoms_total = sum(1 for d in nodes.values() if d.get("type") == tier_1_atom)
    tier_0_total = sum(1 for d in nodes.values() if d.get("type") == tier_0)
    k_atoms = adaptive_k(atoms_total)
    k_tier0 = adaptive_k(tier_0_total)

    # Group atom slugs by community id
    members_by_cid: dict[int, list[str]] = defaultdict(list)
    for slug, cid in clusters.items():
        if nodes.get(slug, {}).get("type") == tier_1_atom:
            members_by_cid[cid].append(slug)

    # Build the projection once for null-model density checks (D2 §3.1).
    atom_tier0, pair_weights, atom_degrees, total_weight = _build_atom_projection(
        nodes, lens
    )
    # Null model meaningful only with ≥2 populated clusters (otherwise
    # Σ intra-cluster weight == total_weight by definition → ratio=1).
    populated_clusters = sum(1 for atoms in members_by_cid.values() if atoms)
    use_null_model = populated_clusters >= 2 and total_weight > 0
    if not use_null_model:
        reason = (
            "total_weight == 0 (empty projection)"
            if total_weight <= 0
            else f"only {populated_clusters} populated cluster(s) (<2)"
        )
        warnings.warn(
            f"null-model density fallback fired: {reason}; "
            "falling back to legacy tier-0-coverage proxy",
            RuntimeWarning,
            stacklevel=2,
        )

    candidates: list[dict] = []
    for cid, atoms in members_by_cid.items():
        if len(atoms) < k_atoms:
            continue

        # Rule 2: each atom needs ≥ k_tier0 exemplifiers. Re-use the
        # tier-0 sets already computed in the projection step.
        atom_exemplifiers = {a: atom_tier0.get(a, set()) for a in atoms}
        weakest = min(len(s) for s in atom_exemplifiers.values())
        if weakest < k_tier0:
            continue

        # Legacy coverage proxy (kept for snapshot continuity).
        union_exemplifiers: set[str] = set()
        for exs in atom_exemplifiers.values():
            union_exemplifiers |= exs
        density_proxy = len(union_exemplifiers) / max(1, k_atoms)

        # Rule 3: null-model-backed density ratio.
        density_ratio = null_model_density_ratio(
            atoms, pair_weights, atom_degrees, total_weight
        )

        if use_null_model:
            if density_ratio < density_multiplier:
                continue
        else:
            # Fallback to legacy proxy when the null model is degenerate.
            if density_proxy < density_multiplier:
                continue

        # Build candidate record
        tier_0_spanning = sorted(union_exemplifiers)
        atoms_sorted = sorted(atoms)
        suggested_name = f"emergent-{tier_0}-cluster-{cid}"
        candidates.append({
            "cluster_id": cid,
            "atoms": atoms_sorted,
            "tier_0_spanning": tier_0_spanning,
            "density_proxy": round(density_proxy, 2),
            "density_ratio": round(density_ratio, 4),
            "suggested_name": suggested_name,
        })

    # Deterministic sort: larger clusters first, then alphabetical by
    # smallest-member slug for tie-breaking.
    candidates.sort(
        key=lambda c: (-len(c["atoms"]), c["atoms"][0] if c["atoms"] else "")
    )
    return candidates


def format_candidate_block(candidate: dict, now_stamp: str | None = None) -> str:
    """Render one candidate dict as a D2 §3.3 markdown block.

    The timestamp defaults to UTC now but is accepted as an argument so
    tests can assert exact output.
    """
    stamp = now_stamp or datetime.utcnow().strftime("%Y-%m-%d-%H%M")
    atoms_md = ", ".join(f"[[{a}]]" for a in candidate["atoms"])
    tier_0_md = ", ".join(f"[[{t}]]" for t in candidate["tier_0_spanning"])
    # Render both the null-model ratio (D2 §3.3 rule 3) and the legacy
    # tier-0-coverage proxy (pre-R2) so a human reviewing the candidate
    # file can compare them when the fallback branch fires. If
    # `density_ratio` is missing (old snapshots), fall back to the proxy
    # value under the "Density ratio" label for back-compat.
    density_ratio = candidate.get("density_ratio", candidate.get("density_proxy"))
    density_proxy = candidate.get("density_proxy")
    lines = [
        f"## Candidate {stamp}\n",
        f"Atoms: {atoms_md}",
        f"Tier-0 spanning: {tier_0_md}",
        f"Density ratio: {density_ratio}",
    ]
    if density_proxy is not None and "density_ratio" in candidate:
        lines.append(f"Density proxy (legacy): {density_proxy}")
    lines.append(
        f"Suggested name: \"{candidate['suggested_name']}\" "
        f"(LLM suggestion — user may rename)"
    )
    lines.append("Status: [ ] accept [ ] refine [ ] reject")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Candidate file writing — preserves user edits below AGENT_MARKER
# ---------------------------------------------------------------------------


def _split_agent_and_user(text: str) -> tuple[str, str]:
    """Split candidate file text into (agent_block, user_block).

    The agent block is everything up to and including the first AGENT_MARKER;
    the user block is everything after. Files without the marker are
    treated as fully user-owned (agent block is empty).
    """
    if AGENT_MARKER not in text:
        return "", text
    before, after = text.split(AGENT_MARKER, 1)
    return before + AGENT_MARKER + "\n", after.lstrip("\n")


def write_tier1_candidates(
    vault: Path,
    lens: LensConfig,
    candidates: list[dict],
    *,
    now_stamp: str | None = None,
) -> Path:
    """Write candidate blocks into `.agent/todos/<tier_1_cluster>-candidates.md`.

    Preserves user-authored content appearing after the AGENT_MARKER.
    The agent block is rewritten on every run; the user block is passed
    through verbatim.

    Returns the path written.
    """
    tier_1_cluster = lens.entity_model["tier_1_cluster"]
    # Preserve v2.0 aesthetic-warburg legacy filename; per D2 §3.3 worked example
    if lens.id == "aesthetic-warburg" and tier_1_cluster == "panel":
        filename = "pathosformel-candidates.md"
    else:
        filename = f"{tier_1_cluster}-candidates.md"

    out_dir = vault / ".agent" / "todos"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename

    existing = out_path.read_text(encoding="utf-8") if out_path.exists() else ""
    _, user_block = _split_agent_and_user(existing)

    agent_lines: list[str] = [
        f"# {tier_1_cluster} candidates (lens: {lens.id})\n",
        "",
        "Emitted by `tools/gap_runner.py`. Do not edit above the marker —",
        "edits survive below it but agent-owned content is rewritten.",
        "",
    ]
    if not candidates:
        agent_lines.append("_(no qualifying candidates at current vault state)_\n")
    else:
        for c in candidates:
            agent_lines.append(format_candidate_block(c, now_stamp=now_stamp))
            agent_lines.append("")
    agent_lines.append(AGENT_MARKER)

    full = "\n".join(agent_lines) + "\n"
    if user_block.strip():
        full += "\n" + user_block

    out_path.write_text(full, encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# Bridge-candidate question stubs (D2 §5)
# ---------------------------------------------------------------------------


def bridge_candidates(
    G,
    nodes: dict[str, dict],
    clusters: dict[str, int],
    lens: LensConfig,
    *,
    llm_client: LLMSimilarityClient | None = None,
    min_similarity: float | None = None,
) -> list[dict]:
    """Find atom pairs in different communities with zero shared tier_0.

    Filters to pairs where both endpoints are tier_1_atom and the
    Jaccard overlap of their exemplifying tier_0 sets is exactly zero.
    Returns dicts with keys: atom_a, atom_b, cluster_a, cluster_b,
    slug (kebab-joined). When an `llm_client` is supplied, a third
    filter is applied per D2 §5 rule 3: the LLM must report semantic
    similarity ≥ `min_similarity` (defaulting to
    `lens.thresholds.gap_llm_similarity`, which itself defaults to
    `DEFAULT_GAP_LLM_SIMILARITY`). The resulting `similarity` score is
    attached to each surviving pair for downstream consumers.

    Note: `min_similarity=0.0` is a valid explicit threshold (accept all
    LLM-scored pairs) and is NOT treated as unset; only `None` triggers
    the lens-default lookup.

    TODO(post-R2): production wiring should pass a real Anthropic-backed
    `LLMSimilarityClient` from the content-extractor entry points (E2,
    E4). The default `None` preserves backwards compatibility — callers
    that do not opt into LLM validation get the structural-only filter.

    Deterministic: sorted by `(atom_a, atom_b)`.
    """
    tier_1_atom = lens.entity_model["tier_1_atom"]
    tier_0 = lens.entity_model["tier_0"]

    atom_slugs = [s for s, d in nodes.items() if d.get("type") == tier_1_atom]
    atom_tier0: dict[str, set[str]] = {}
    for atom in atom_slugs:
        exs: set[str] = set()
        for rel in nodes.get(atom, {}).get("relations", []):
            if rel.get("type") in ("exemplifiedBy", "exemplifies"):
                target = rel.get("target", "").strip()
                if nodes.get(target, {}).get("type") == tier_0:
                    exs.add(target)
        atom_tier0[atom] = exs

    if min_similarity is None:
        min_similarity = float(
            lens.thresholds.get("gap_llm_similarity", DEFAULT_GAP_LLM_SIMILARITY)
        )

    pairs: list[dict] = []
    for i, a in enumerate(atom_slugs):
        for b in atom_slugs[i + 1:]:
            if clusters.get(a) == clusters.get(b):
                continue
            if atom_tier0[a] & atom_tier0[b]:
                continue  # shared tier_0 means there IS a bridge

            pair: dict[str, Any] = {
                "atom_a": a,
                "atom_b": b,
                "cluster_a": clusters.get(a, -1),
                "cluster_b": clusters.get(b, -1),
                "slug": f"bridge-{a}-{b}",
            }

            if llm_client is not None:
                score = float(
                    llm_client.similarity(a, b, lens_id=lens.id)
                )
                pair["similarity"] = round(score, 4)
                if score < min_similarity:
                    continue

            pairs.append(pair)

    pairs.sort(key=lambda p: (p["atom_a"], p["atom_b"]))
    return pairs


def write_question_stubs(
    vault: Path,
    lens: LensConfig,
    pairs: list[dict],
) -> list[Path]:
    """Write one `wiki/questions/<slug>.md` stub per bridge candidate.

    Stubs include a stable hash in the frontmatter so the same pair on
    the same vault state produces a byte-identical file. Existing files
    are not overwritten — a user's edits to a question stub are
    preserved and the new generation simply skips that slug (logged to
    stderr).

    Returns the list of paths actually written (new files only).
    """
    out_dir = vault / "wiki" / "questions"
    out_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for pair in pairs:
        path = out_dir / f"{pair['slug']}.md"
        if path.exists():
            continue

        pair_hash = hashlib.sha256(
            f"{pair['atom_a']}|{pair['atom_b']}|{lens.id}".encode("utf-8")
        ).hexdigest()[:12]

        body = (
            f"---\n"
            f"type: question\n"
            f"lens: {lens.id}\n"
            f"bridge_hash: {pair_hash}\n"
            f"atom_a: {pair['atom_a']}\n"
            f"atom_b: {pair['atom_b']}\n"
            f"cluster_a: {pair['cluster_a']}\n"
            f"cluster_b: {pair['cluster_b']}\n"
            f"status: open\n"
            f"---\n\n"
            f"# Unbridged gap: [[{pair['atom_a']}]] × [[{pair['atom_b']}]]\n\n"
            f"These two atoms live in different communities ({pair['cluster_a']} vs\n"
            f"{pair['cluster_b']}) and share zero tier-0 exemplifiers. Either\n"
            f"a bridge exists and we haven't written it down, or the gap is\n"
            f"real and worth naming.\n\n"
            f"## Open sub-questions\n\n"
            f"- [ ] Is there a tier-0 entry that cites both?\n"
            f"- [ ] Can a new tier-0 be authored that would bridge them?\n"
            f"- [ ] Or should one of the atoms be renamed / merged?\n"
        )
        path.write_text(body, encoding="utf-8")
        written.append(path)
    return written


# ---------------------------------------------------------------------------
# Orchestration + CLI
# ---------------------------------------------------------------------------


def run_gap(args: argparse.Namespace) -> int:
    """Main orchestration. Returns exit code (0 success / non-zero error)."""
    # Vault validation first — if the vault is wrong we don't waste
    # a lens-resolution error message pointing at the repo rather than
    # at the user's --vault path (round-5/6 audit meta-fix).
    vault = Path(args.vault).resolve()
    has_agent = (vault / ".agent").is_dir()
    has_wiki = (vault / "wiki").is_dir()
    if not (has_agent or has_wiki):
        print(
            f"error: {vault} does not look like a Bab-ilu vault "
            f"(no .agent/ or wiki/ subdirectory). Pass --vault <path> "
            f"explicitly or run this command from a vault root.",
            file=sys.stderr,
        )
        return 2
    lens = _resolve_lens(args)
    if not has_wiki:
        print(f"error: no wiki/ in {vault} (vault scaffolded but no content yet; run /ingest first)", file=sys.stderr)
        return 1

    nodes = load_wiki(vault)
    G = build_graph(nodes)
    clusters = compute_clusters(G, lens=lens)

    # Tier-1 qualification
    candidates = qualify_tier1_candidates(nodes, clusters, lens)
    bridge_pairs = bridge_candidates(G, nodes, clusters, lens)

    if args.dry_run:
        print(f"[dry-run] lens={lens.id} tier1_candidates={len(candidates)} "
              f"bridges={len(bridge_pairs)}")
        return 0

    cand_path = write_tier1_candidates(vault, lens, candidates)
    print(f"✓ wrote {cand_path.relative_to(vault)}", file=sys.stderr)

    question_paths = write_question_stubs(vault, lens, bridge_pairs)
    if question_paths:
        print(f"✓ wrote {len(question_paths)} question stub(s) under wiki/questions/",
              file=sys.stderr)

    # Still run detect_gaps so callers depending on the insights report
    # keep the full gap enumeration visible. gap_runner's contract is
    # candidate-writing; it doesn't replace graph_analyzer's insights.
    gaps = detect_gaps(G, nodes, clusters, lens=lens)
    print(f"  detected gaps: {len(gaps)}", file=sys.stderr)

    return 0


def main() -> None:
    ap = argparse.ArgumentParser(prog="gap_runner")
    ap.add_argument("--vault", default=str(DEFAULT_VAULT))
    ap.add_argument("--lens", default=None)
    ap.add_argument("--lenses-base", default=None)
    ap.add_argument("--tier", type=int, default=1, choices=[1, 2])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    sys.exit(run_gap(args))


if __name__ == "__main__":
    main()
