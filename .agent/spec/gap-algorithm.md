# /gap Algorithm Specification (v2.1 — lens-parameterized)

> **Status:** v2.1 Sprint 2 authoritative. Supersedes the v2.0 draft.
> **Consumed by:** `tools/graph_analyzer.py` (lens-aware since D1),
>                   `/gap` skill, `/lint` (via `--rebuild-graph`).
> **Referenced from:** `PRD-v2.1-zh.md §4.3`, `schema.md §7`, `docs/lens-spec.md`.
> **Changes from v2.0:** terminology generalized to tier labels
> (`tier_0` / `tier_1_atom` / `tier_1_cluster` / `tier_2_cluster`);
> thresholds and output paths now sourced from `lens.yaml`; community
> detection algorithm is per-lens configurable; aesthetic-warburg
> examples preserved inline as the worked case.

## 0. Lens insertion points

All parameters below resolve against the **active lens** (`.agent/lenses/active/lens.yaml`).
Any field reference like `lens.X` refers to that file. The algorithm is
defined once; the three first-wave lenses instantiate it as:

| Tier label       | aesthetic-warburg (landed) | engineering-alexander (proposed) | general-zettelkasten (proposed) |
|------------------|----------------------------|----------------------------------|--------------------------------|
| `tier_0`         | `aesthetic`                | `incident`                       | `source`                       |
| `tier_1_atom`    | `motif`                    | `pattern`                        | `note`                         |
| `tier_1_cluster` | `panel` *(Pathosformel bundle)* | `pattern-language`         | `concept-cluster`              |
| `tier_2_cluster` | *(proposed `topos`)*       | *(proposed `meta-pattern`)*      | *(proposed `theme`)*           |

The aesthetic-warburg column reproduces
`.agent/lenses/aesthetic-warburg/lens.yaml` verbatim (landed in
Sprint 1). Engineering and general-zettelkasten columns are proposed
for Sprint 2+ lens.yaml files; the algorithm is generic and those
specific values enter once the lens.yaml ships. `tier_2_cluster` is a
schema extension the graph_analyzer will honor when present — the
current aesthetic-warburg lens.yaml does not yet declare it, so tier-2
clustering silently skips until a lens opts in.

Wherever the v2.0 spec said "motif" / "pathosformel" / "works", read
the corresponding row of this table. The aesthetic-warburg column is
used throughout as the worked example because it was the driving case;
note that what v2.0 prose called "a work" is `tier_0 = aesthetic` in
the v2.1 schema, and what v2.0 called "a pathosformel" is
`tier_1_cluster = panel`.

## 1. Inputs

**Tier 1:**
- `wiki/{tier_0}/*.md` and `wiki/{tier_1_atom}/*.md` as node set
- `.agent/graph/{tier_1_atom}.md` for `exemplifiedBy` and `coOccurs` edges
  (append-only, with retractions applied in pre-pass)
- Aesthetic-warburg example: `wiki/aesthetic/` + `wiki/motif/` +
  `.agent/graph/motifs.md`.

**Tier 2:**
- `wiki/{tier_1_cluster}/*.md` as node set
- `.agent/graph/{tier_1_cluster}.md` for `cluster` edges (tier 1 output)
- Derived: cluster-cluster edges with weight = Jaccard of shared atom sets
- Aesthetic-warburg example: `wiki/panel/` +
  `.agent/graph/pathosformel.md`.

## 2. Pre-pass: Retraction Resolution

For each relation code `r`, scan ontology files for pairs of lines:

```
[[a]] [r] [[b]]
[[a]] [retracts-r] [[b]]
```

Drop the original line if a matching retraction exists. Retraction must
appear *after* the original in file order. Lens-agnostic — the retraction
grammar is part of the shared ontology convention, not the lens.

## 3. Tier 1 Clustering

### 3.1 Projection

From bipartite `{tier_0} × {tier_1_atom}` graph, project onto the
atom-atom weighted graph:

```
For each pair (a_i, a_j):
  weight(a_i, a_j) = |tier_0(a_i) ∩ tier_0(a_j)| / |tier_0(a_i) ∪ tier_0(a_j)|   # Jaccard
```

Sparsification: keep only edges with
`weight ≥ lens.thresholds.tier1_weight_min` AND at least
`lens.thresholds.tier1_min_shared_tier_0` shared tier-0 nodes. Defaults
`0.15` and `2` come from the v2.0 aesthetic-warburg run. These
granular threshold keys are Sprint 2+ additions; the landed
aesthetic-warburg lens.yaml uses the coarser v2.0 names
(`cluster_member_min`, `cluster_min_size`, `density_multiplier`,
`orphan_min_degree`, `domain_min`) and the graph_analyzer continues to
honor them until the lens schema expands. See `lens-spec.md` for the
proposed migration.

### 3.2 Community Detection

The algorithm is per-lens configurable via `lens.community_detection`:

- `algorithm`: one of `louvain` / `leiden`
- `resolution`: γ value (default `1.0`), exposed as `/gap --resolution`
- `random_state`: fixed per-run for reproducibility; `/gap --seed N`
  overrides

The landed aesthetic-warburg lens ships with `louvain` (via
`python-louvain`) — that is what `tools/graph_analyzer.py` exercises
today and what the reproducibility tests in
`tests/test_graph_analyzer_lens.py` assert against. Proposed lenses may
choose the Leiden algorithm (via `leidenalg`, config key `leiden`) when
their graph characteristics benefit from resolution-tunable modularity
with stronger well-connectedness guarantees than Louvain; the loader
simply passes the declared algorithm through.

### 3.3 Tier-1 Cluster Qualification

A community `C` qualifies as a `tier_1_cluster` candidate iff all hold:

1. `|atoms in C| ≥ k` where `k = max{3, ⌈log₂(|atoms_total|)⌉}`
2. Each atom in `C` has `≥ l` exemplifying tier-0 nodes, where
   `l = max{3, ⌈log₂(|tier_0_total|)⌉}`
3. Internal density > `lens.thresholds.density_vs_null × E[null_model_density]`
   where null model = bipartite configuration model preserving degree
   sequence. Default multiplier: `3`.

Candidates written to `.agent/todos/{tier_1_cluster}-candidates.md` in format:

```markdown
## Candidate YYYY-MM-DD-HHMM

Atoms: [[a1]], [[a2]], [[a3]]
Tier-0 spanning: [[x1]] (1657), [[x2]] (1900), [[x3]] (2019)
Density ratio: 4.2
Suggested name: "quiet-interior-light" (LLM suggestion — user may rename)
Status: [ ] accept [ ] refine [ ] reject
```

Aesthetic-warburg example: atoms = motifs, tier-0 = works, file =
`.agent/todos/pathosformel-candidates.md`.

## 4. Tier 2 Clustering

### 4.1 Activation Condition

Tier 2 runs iff `|{tier_1_cluster}| ≥ lens.thresholds.tier2_activation_min`
OR the user invokes `/gap --tier=2` (with override warning if below
threshold). Default activation threshold: `15`.

### 4.2 Projection

From the tier-1-cluster set, project onto the cluster-cluster graph:

```
For each pair (c_i, c_j):
  weight(c_i, c_j) = |atoms(c_i) ∩ atoms(c_j)| / |atoms(c_i) ∪ atoms(c_j)|
```

Sparsification: keep edges with
`weight ≥ lens.thresholds.tier2_weight_min` AND at least
`lens.thresholds.tier2_min_shared_tier_1_atom` shared atoms. Defaults:
`0.20` and `2`.

### 4.3 Community Detection

Same algorithm as §3.2. The resolution parameter is shared by default;
lenses may override via `lens.community_detection.tier2_resolution`.

### 4.4 Tier-2 Cluster Qualification

A community `C` qualifies iff `|{tier_1_cluster} in C| ≥ 3` AND each
cluster in `C` shares `≥ 2` atoms with at least one other cluster in `C`.

Candidates written to `.agent/todos/{tier_2_cluster}-candidates.md`
(same format as §3.3).

Aesthetic-warburg example: `.agent/todos/topoi-candidates.md`.

## 5. Gap Discovery (independent of cluster output)

After clustering, find **bridge candidates**: atom pairs `(a_i, a_j)` where:

1. `a_i ∈ community A`, `a_j ∈ community B`, `A ≠ B`
2. `weight(a_i, a_j) = 0` (no shared tier-0 nodes)
3. LLM semantic similarity score > `lens.thresholds.gap_llm_similarity`
   (LLM validation pass). Default: `0.6`.

These become `wiki/questions/<slug>.md` entries describing the unbridged
gap. The `questions/` folder is lens-neutral — every lens uses the same
output path because "what don't we know yet" is a cross-cutting meta-domain.

## 6. LLM Validation Layer

For every algorithmic cluster candidate, run an LLM validation pass using
the lens's `analysis_contract.gap` prompt template. The lens's
`prompts.md` (injected at runtime by `tools/lens_context.py`) supplies
the judgment rules and tone.

Template variables the prompt must fill:

```
Given {tier_1_atom}s: {atoms}
Sharing {tier_0}s across eras: {tier_0_refs_with_dates}

Evaluate (per lens.analysis_contract.gap rubric):
1. Does this cluster represent a coherent {tier_1_cluster}?
2. Suggest a name per the lens's naming convention.
3. Flag any atom that doesn't belong (semantic outlier detection).

Return JSON: {coherent: bool, suggested_name: str|null, outliers: [slug]}
```

Aesthetic-warburg rubric: "coherent visual-emotional formula
(Pathosformel); Warburg-style evocative phrase, not category label".
Engineering-alexander rubric: "problem-solution-context triad forms a
reusable pattern; name follows Alexander's 'noun phrase indicating
context'". General-zettelkasten rubric: "concept cluster organized by
Bloom verb level; name is the dominant Bloom action".

LLM output appended to the candidate block. User makes final decision.

## 7. Reproducibility Contract

- Given same ontology state + same `--seed N`, `/gap` must produce
  identical cluster assignments. Lens-independent.
- LLM validation layer is non-deterministic but logged: each run appends
  to `.agent/state/gap-runs.log` with timestamp + input hash + lens id +
  LLM output for audit.
- `/gap --dry-run` reports what would change without writing to `todos/`.

## 8. Performance Envelope

Safe range (no engineering work), per lens:

- ≤ `lens.thresholds.max_atoms_safe` (default 2,000)
- ≤ `lens.thresholds.max_tier_0_safe` (default 10,000)
- ≤ `lens.thresholds.max_bipartite_edges_safe` (default 250,000)
- Tier 1 runtime < 30 seconds on modern laptop

Past this range: projection sparsification mandatory; Obsidian Graph View
degrades. Consider external d3/sigma.js viewer in v2.x.

Aesthetic-warburg uses defaults. Engineering-alexander lowers
`max_atoms_safe` to `800` because pattern cards are more information-dense
per node; general-zettelkasten raises it to `5,000` because notes are
typically short and per-note degree is low.

## 9. Test Commitments (Sprint 2)

- Deterministic: `test_tier1_clustering_reproducible` — same input + seed
  + same lens = same output.
- Threshold: `test_adaptive_threshold_scales` — k, l computed correctly
  at n=50/500/5000 under each lens.
- Aggregate filter: `test_tier_1_cluster_excluded_from_tier1` — loading a
  synthetic tier_1_cluster node does not affect tier 1 cluster output
  under any lens.
- Retraction: `test_retraction_applied_in_prepass` — retracted edge
  absent from clustering input (lens-agnostic).
- Tier 2 gating: `test_tier2_inactive_below_activation_min` —
  `/gap --tier=2` returns "insufficient data" below the lens's threshold.
- LLM snapshot: `test_llm_validation_pass_fixture` — replay frozen LLM
  response against fixture cluster under each lens's rubric.
- Lens parameterization: `test_lens_thresholds_honored` — explicitly
  swap the active lens and verify the algorithm uses the new thresholds
  without code changes (covered by `tests/test_graph_analyzer_lens.py`).

These live in `tests/test_gap_algorithm.py` (created Sprint 2) plus the
lens-parameterization coverage in `tests/test_graph_analyzer_lens.py`
(landed in D1).
