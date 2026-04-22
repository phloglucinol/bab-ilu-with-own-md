---
name: gap
description: Lens-aware gap discovery for the vault. Runs community detection (louvain or leiden per lens) over the vault's bipartite graph, qualifies tier-1 cluster candidates per D2 spec thresholds, surfaces unbridged gaps, and writes candidate files to `.agent/todos/`. Delegates to `tools/gap_runner.py` which wraps the lens-aware `tools/graph_analyzer.py` (D1) and adds the candidate-writing layer from `.agent/spec/gap-algorithm.md` (D2).
allowed-tools: [Bash, Read, Write, Edit, Glob]
---

# /gap — Lens-aware gap discovery

## Synopsis

```
/gap                             # tier 1; active lens; write candidates
/gap --tier=1                    # explicit tier 1 (default)
/gap --tier=2                    # activate tier 2 clustering (gated)
/gap --lens=<id>                 # override active lens
/gap --dry-run                   # print plan to stdout, do not write
/gap --vault=<path>              # non-default vault root
```

## What `/gap` produces

Per `.agent/spec/gap-algorithm.md` (D2 landed):

1. **`.agent/todos/<tier_1_cluster>-candidates.md`** — one block per
   qualifying community emerging from tier-1 clustering. Format per D2
   §3.3:
   ```markdown
   ## Candidate YYYY-MM-DD-HHMM

   Atoms: [[a1]], [[a2]], [[a3]]
   Tier-0 spanning: [[x1]] (1657), [[x2]] (1900), [[x3]] (2019)
   Density ratio: 4.2
   Suggested name: "quiet-interior-light" (LLM suggestion — user may rename)
   Status: [ ] accept [ ] refine [ ] reject
   ```
   Under aesthetic-warburg: `pathosformel-candidates.md`. Under
   engineering-alexander: `pattern-language-candidates.md`. Under
   general-zettelkasten: `concept-cluster-candidates.md`.

2. **`.agent/todos/<tier_2_cluster>-candidates.md`** — tier-2 output,
   only when `--tier=2` AND `|tier_1_cluster| ≥ lens.thresholds.tier2_activation_min`
   (default 15, or override warning when below).

3. **`wiki/questions/<slug>.md`** — one stub per unbridged gap per D2
   §5. Bridge candidates are atom pairs in different communities with
   zero shared tier-0s and LLM semantic similarity > the lens threshold.

4. **`wiki/_insights.md`** — human-readable overview (inherited from
   graph_analyzer). Contains cluster summary, bridge candidates, gap
   list, bias signals.

5. Planned (v2.3): **`wiki/_index/insights.json`** — machine-readable
   companion output. Not emitted in v2.2.

## How it works (one screen)

```
Parse args → resolve lens (honor --lens; else .agent/lenses/active/)
           ↓
Delegate to tools/gap_runner.py which:
  1. Imports graph_analyzer.{load_wiki, build_graph, compute_clusters,
                              compute_bridges, detect_gaps}
  2. Runs the pipeline under the lens (D1 lens-parameterized)
  3. Qualifies clusters against D2 §3.3 criteria:
     - |atoms in C| ≥ max{3, ⌈log₂(|atoms_total|)⌉}
     - each atom has ≥ max{3, ⌈log₂(|tier_0_total|)⌉} tier_0 exemplifiers
     - internal_density > lens.thresholds.density_multiplier × E[null_density]
  4. For each qualifying cluster, writes the Candidate block to
     .agent/todos/<tier_1_cluster>-candidates.md
  5. For each unbridged pair (community-i-atom, community-j-atom) with
     weight=0 and LLM semantic similarity > 0.6, writes wiki/questions/
     stub
  6. If --tier=2 requested and gated threshold met, runs the same
     qualification on tier_1_cluster × tier_1_cluster projection and
     writes <tier_2_cluster>-candidates.md
           ↓
Write _insights.md
           ↓
Exit 0 (success) | 1 (no wiki/) | 2 (lens resolution failure)
```

## Lens-specific behavior (landed lenses)

| Lens | tier_0 | tier_1_atom | tier_1_cluster | algorithm | candidates file |
|---|---|---|---|---|---|
| aesthetic-warburg | aesthetic | motif | panel | louvain | `pathosformel-candidates.md` (v2.0 name preserved) |
| engineering-alexander | incident | pattern | pattern-language | leiden | `pattern-language-candidates.md` |
| general-zettelkasten | note | concept | concept-cluster | louvain | `concept-cluster-candidates.md` |

The lens determines:
- Which wiki directories are scanned as tier_0 / tier_1_atom
- Which community-detection algorithm runs (per `lens.community_detection.algorithm`)
- Which thresholds qualify a cluster (per `lens.thresholds`)
- Which authority anchors factor into `missing_authority_anchor` gap
  (Zettelkasten omits, so that gap category is silent)
- Which judgment rules govern the LLM validation pass (per `lens.prompts.md`
  injected by `tools/lens_context.py`)

## Tier 2 gating

Tier 2 runs iff:
- User explicitly passes `--tier=2`, AND
- `|tier_1_cluster entries in vault| ≥ lens.thresholds.tier2_activation_min`
  (default 15)

When the threshold is unmet and `--tier=2` is passed, `/gap` prints a
warning to stderr and still runs tier 2 (override semantics, per D2
§4.1). Without `--tier=2`, the tier-2 qualification is silently skipped.

Aesthetic-warburg's tier-2 (topoi) and engineering-alexander's tier-2
(meta-patterns) are both proposed — no landed lens declares
`tier_2_cluster` yet, so tier-2 qualification gracefully skips until a
lens opts in.

## Reproducibility

Given same vault state + same `lens.community_detection.random_state`,
`/gap` produces byte-identical `_insights.md` and candidate files. The
LLM validation layer is non-deterministic but logged to
`.agent/state/gap-runs.log` with timestamp + vault-state hash + lens id
for audit replay.

## Exit codes

- `0` — completed, even if zero candidates found
- `1` — vault root lacks `wiki/`
- `2` — lens resolution failed (unknown id, invalid lens.yaml, missing
  active lens without explicit `--lens`)

Non-zero never silently falls back — `/gap` is authoritative for "is
the graph in a state that would discover new patterns", so ambiguous
runs must fail loud.

## When to run

- After `/ingest` adds ≥3 new tier_0 entries (the graph shape changed
  meaningfully)
- After `/lint --fix` (so candidate writes see a clean graph)
- Weekly scan via cron (see `docs/superpowers/` for the suggested
  schedule)
- Before any /prompt invocation that depends on discovered clusters

## Implementation notes

- `tools/gap_runner.py` is the callable entry; skills invoke via
  `python -m tools.gap_runner <args>`
- The runner imports from `tools.graph_analyzer` and adds only the D2
  candidate-writing layer; the heavy lifting (load_wiki, build_graph,
  compute_clusters, detect_gaps) stays in graph_analyzer for single-
  responsibility
- Tests live in `tests/test_gap_algorithm.py` covering D2 §9 commitments
