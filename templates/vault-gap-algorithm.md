# /gap Algorithm Specification

> **Status:** v2.0 Sprint 1 authoritative.
> **Consumed by:** `tools/graph_analyzer.py` (implemented Sprint 2), `/gap` skill, `/lint`.
> **Referenced from:** `PRD-v2-zh.md §4.3`, `schema.md §7`.

## 1. Inputs

**Tier 1:**
- `wiki/aesthetic/*.md` and `wiki/motif/*.md` as node set
- `.agent/graph/motifs.md` for `exemplifiedBy` and `coOccurs` edges (append-only, with retractions applied in pre-pass)

**Tier 2:**
- `wiki/panel/*.md` as node set
- `.agent/graph/pathosformel.md` for `cluster` edges (tier 1 output)
- Derived: Pathosformel-Pathosformel edges with weight = Jaccard of shared motif sets

## 2. Pre-pass: Retraction Resolution

For each relation code `r`, scan ontology files for pairs of lines:
```
[[a]] [r] [[b]]
[[a]] [retracts-r] [[b]]
```
Drop the original line if a matching retraction exists. Retraction must appear *after* the original in file order.

## 3. Tier 1 Clustering

### 3.1 Projection

From bipartite Work × Motif graph, project onto motif-motif weighted graph:

```
For each pair (m_i, m_j):
  weight(m_i, m_j) = |works(m_i) ∩ works(m_j)| / |works(m_i) ∪ works(m_j)|    # Jaccard
```

Sparsification: keep only edges with `weight ≥ 0.15` AND at least 2 shared works.

### 3.2 Community Detection

Run Leiden algorithm on projection graph:
- Library: `leidenalg` (Python) or `igraph` equivalent
- Resolution γ: default `1.0`, exposed as `/gap --resolution`
- Random seed: fixed per-run for reproducibility; user can re-run with different seed via `/gap --seed N`

### 3.3 Pathosformel Candidate Qualification

A Leiden community `C` qualifies as Pathosformel candidate iff:

1. `|motifs in C| ≥ k` where `k = max{3, ⌈log₂(|motifs_total|)⌉}`
2. Each motif in `C` has `≥ l` exemplifying works, where `l = max{3, ⌈log₂(|works_total|)⌉}`
3. Internal density > `3 × E[null_model_density]` where null model = bipartite configuration model preserving degree sequence

Candidates written to `.agent/todos/pathosformel-candidates.md` in format:

```markdown
## Candidate YYYY-MM-DD-HHMM

Motifs: [[m1]], [[m2]], [[m3]]
Works spanning: [[w1]] (1657), [[w2]] (1900), [[w3]] (2019)
Density ratio: 4.2
Suggested name: "quiet-interior-light" (LLM suggestion — user may rename)
Status: [ ] accept [ ] refine [ ] reject
```

## 4. Tier 2 Clustering

### 4.1 Activation Condition

Tier 2 runs iff `|pathosformel| ≥ 15` OR user invokes `/gap --tier=2` (with override warning if count < 15).

### 4.2 Projection

From Pathosformel set P, project onto P-P graph:

```
For each pair (p_i, p_j):
  weight(p_i, p_j) = |motifs(p_i) ∩ motifs(p_j)| / |motifs(p_i) ∪ motifs(p_j)|
```

Sparsification: keep edges with `weight ≥ 0.20` AND at least 2 shared motifs.

### 4.3 Community Detection

Same Leiden algorithm, resolution `1.0` (tuneable).

### 4.4 Topos Qualification

A community qualifies iff `|pathosformel in C| ≥ 3` AND each pathosformel in C shares ≥ 2 motifs with at least one other pathosformel in C.

Candidates written to `.agent/todos/topoi-candidates.md` (same format).

## 5. Gap Discovery (independent of cluster output)

After clustering, find **bridge candidates**: motif pairs `(m_i, m_j)` where:

1. `m_i ∈ community A`, `m_j ∈ community B`, `A ≠ B`
2. `weight(m_i, m_j) = 0` (no shared works)
3. LLM semantic similarity score > `τ = 0.6` (LLM validation pass)

These become `wiki/questions/<slug>.md` entries describing the unbridged gap.

## 6. LLM Validation Layer

For every algorithmic cluster candidate, run LLM validation pass:

**Prompt structure:**
```
Given motifs: {m1, m2, m3}
Sharing works across eras: {w1 (1657), w2 (1900), w3 (2019)}

Evaluate:
1. Does this cluster represent a coherent visual-emotional formula (Pathosformel)?
2. Suggest a name (Warburg style: evocative phrase, not category label).
3. Flag any motif that doesn't belong (semantic outlier detection).

Return: {coherent: bool, suggested_name: str|null, outliers: [slug]}
```

LLM output appended to candidate block in `.agent/todos/`. User makes final decision.

## 7. Reproducibility Contract

- Given same ontology state + same `--seed N`, `/gap` must produce identical cluster assignments.
- LLM validation layer is non-deterministic but logged: each run appends to `.agent/state/gap-runs.log` with timestamp + input hash + LLM output for audit.
- `/gap --dry-run` reports what would change without writing to todos/.

## 8. Performance Envelope

Safe range (no engineering work):
- ≤ 2,000 motifs
- ≤ 10,000 works
- ≤ 250,000 bipartite edges
- Tier 1 runtime < 30 seconds on modern laptop

Past this range: projection sparsification mandatory, Obsidian Graph View degrades (switch to external d3/sigma.js viewer in v2.x).

## 9. Test Commitments (Sprint 2)

- Deterministic: `test_tier1_clustering_reproducible` — same input + seed = same output
- Threshold: `test_adaptive_threshold_scales` — k, l computed correctly at n=50/500/5000
- Aggregate filter: `test_pathosformel_excluded_from_tier1` — loading synthetic pathosformel node does not affect tier 1 cluster output
- Retraction: `test_retraction_applied_in_prepass` — retracted edge absent from clustering input
- Tier 2 gating: `test_tier2_inactive_below_15_pathosformel` — `/gap --tier=2` returns "insufficient data"
- LLM snapshot: `test_llm_validation_pass_fixture` — replay frozen LLM response against fixture cluster

These go in `tests/test_gap_algorithm.py` (created Sprint 2).
