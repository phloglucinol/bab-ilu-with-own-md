---
name: lint
description: Structural + lens-aware validation for the vault. Runs v2.0 entity checks plus (with `--lens <id>`) authority-anchor coverage and tier-1-cluster consistency. `--rebuild-graph` delegates to graph_analyzer. Safe to run any time; non-destructive without `--fix`.
allowed-tools: [Bash, Read, Edit, Glob]
---

# /lint — Vault structural + lens-aware validator (v2.1)

## Synopsis

```
/lint                                            # v2.0 entity checks only
/lint --lens=aesthetic-warburg                   # + anchor + tier consistency
/lint --lens=general-zettelkasten --json         # machine-readable output
/lint --fix                                      # auto-fix deterministic issues
/lint --fix --dry-run                            # preview fixes only
/lint --rebuild-graph --lens=aesthetic-warburg   # re-run graph_analyzer after lint
/lint --suggest                                  # show remediation hints for non-fixable
```

## What this skill does

`/lint` is the vault's structural gatekeeper. It runs before `/prompt`, before
`/distill`, and before any release to catch broken links, missing fields,
stale cross-references, and (when a lens is active) lens-specific drift.

Four layers of checks run in order:

1. **v2.0 entity checks** — always on. Validates `papers/`, `concepts/`,
   `topics/`, `people/`, `ideas/`, `experiments/`, `claims/`, `foundations/`
   per `tools/_schemas.py` (required fields, enum values, idea/experiment
   completeness, xref symmetry, graph edge consistency, content quality).
2. **Karpathy active-suggestion checks** (K2, Sprint 4; PRD §0.5.4) —
   always on, lens-agnostic parts. Structural MVP — LLM-backed tiers
   defer to Sprint 5 per principle 1 (late binding):
   - `stale-claim` — pages citing a target whose slug appears as the
     `to` of any `[[x]] [retracts-<code>] [[target]]` line in
     `.agent/graph/*.md`. Per `.agent/spec/gap-algorithm.md §2`.
   - `material-request` — a missing wikilink target referenced by ≥ 2
     distinct pages. Below 2 references is ordinary broken-link noise;
     at 2+ the wiki itself is *asking for* a page on that slug.
3. **Lens-aware checks** — opt-in via `--lens <id>`. Adds:
   - `lens-anchor` — tier-0 pages missing every authority field the lens
     declares in `anchors.authority_fields`. Lenses without anchors
     (e.g. zettelkasten) silently skip this check.
   - `lens-tier` — tier-1-cluster pages whose wikilinks resolve to EXISTING
     pages of the wrong type. Broken-target wikilinks are intentionally
     not double-reported here — `check_broken_links` already covers them.
   - `contradiction` (K2 Rule A, Sprint 4) — same normalized title across
     ≥ 2 pages with mismatched values for the lens's
     `anchors.authority_fields`. Lenses without authority fields (e.g.
     zettelkasten) silently skip. Severity 🟡 — users decide whether to
     reconcile, add a `contradicts` edge, or mark as intentional.
4. **Graph rebuild** — opt-in via `--rebuild-graph`. After lint completes
   (and after `--fix` if requested), delegates to `tools/graph_analyzer.py`
   as a subprocess, forwarding `--lens` and `--lenses-base` unchanged.

## Step 1 — Parse arguments

Accept:

- `--wiki-dir <path>` (default `wiki/`)
- `--json` — emit machine-readable output (list when no `--fix`, dict when `--fix`)
- `--fix` — apply auto-fixes for deterministic issues (xref reverse links,
  missing field defaults per `FIELD_DEFAULTS`). Non-destructive for fields
  without a safe default (e.g. `title`).
- `--dry-run` — requires `--fix`; previews without modifying files.
- `--suggest` — include remediation hints on the human-readable output.
- `--lens <id>` — activate lens-aware checks.
- `--lenses-base <path>` — override default `.agent/lenses/`. Mainly for
  tests and power users experimenting with alternate lens packs.
- `--rebuild-graph` — run `tools/graph_analyzer.py` after lint output.

## Step 2 — Run the v2.0 pipeline

Call `lint(wiki_dir)` which internally runs, in order:

```
check_missing_fields
check_broken_links
check_orphan_pages
check_field_values
check_idea_failure_reason
check_experiment_claim_link
check_xref_asymmetry
check_graph_edges
check_content_quality
```

Each yields `LintIssue(level, category, file, message, fixable, suggestion)`.

## Step 3 — Lens-aware extension (only when `--lens` is supplied)

1. Resolve the lens:
   ```python
   base = Path(args.lenses_base) if args.lenses_base else Path(".agent/lenses")
   lens = load_lens(args.lens, base=base)
   ```
   Missing lens id or schema violation is **fatal** — exit 1 with a clear
   error. We refuse to silently fall back to v2.0-only because the user
   explicitly asked for lens awareness.
2. Append `check_lens_anchors(wiki_dir, pages, lens)` — yellow per tier-0
   page without any populated authority field.
3. Append `check_lens_tier_consistency(wiki_dir, pages, lens)` — yellow
   per tier-1-cluster wikilink resolving to the wrong type.

Both helpers walk `wiki_dir.rglob("*.md")` via `_scan_all_markdown` rather
than the v2.0 `ENTITY_DIRS` set — tier directories (`aesthetic/`, `panel/`,
`patterns/`, `note/`, …) vary per lens and should not require schema edits.

## Step 4 — Optional `--fix` pass

Same contract as v2.0:

- Fixable categories (`xref`, `missing-field`) are repaired when a safe
  default exists.
- `--dry-run` previews only — files are not modified.
- Fix output appears as `FixResult` entries alongside the lint issues.

Lens-aware issues are **not auto-fixable** — adding an authority ID or
rewriting a cluster's wikilinks is an editorial decision, not a mechanical
one. They appear as yellow warnings with targeted suggestions.

## Step 5 — Optional `--rebuild-graph` delegation

After lint (and `--fix`) complete:

```python
rebuild_graph(wiki_dir, lens_id=args.lens, lenses_base=rg_lenses_base)
```

Delegates to `tools/graph_analyzer.py` via `subprocess.run`. The analyzer
owns its own CLI contract (writes `wiki/_index/edges.jsonl`, clusters,
gaps) and must succeed independently — lint surfaces a non-zero exit via
`[rebuild-graph]` stderr but does not override lint's own exit code.

## Step 6 — Output + exit code

### Human-readable (default)

```
Lint: 2 🔴, 5 🟡, 1 🔵

🔴 [missing-field] papers/foo.md: importance required
🟡 [lens-anchor] aesthetic/naked.md: tier-0 'naked' has no authority anchor (lens 'aesthetic-warburg' expects one of: aat_id, iconclass, wikidata, …)
🟡 [lens-tier] panel/bad.md: tier-1-cluster 'bad' links to 'some-source' of type 'source' (lens expects ['aesthetic', 'motif'])
…
```

`--suggest` appends remediation hints after each issue.

### JSON

```
/lint --json
```
returns `list[dict]` of issues.

```
/lint --fix --json
```
returns `{issues, fixes, dry_run}`.

### Exit code

- `0` — no red issues
- `1` — at least one red issue, OR the lens id is missing/invalid when
  `--lens` was requested, OR `wiki_dir` does not exist.
- Graph analyzer exit codes from `--rebuild-graph` are logged but do NOT
  override lint's own exit code — lint is authoritative for "is the
  vault structurally valid".

## Categories reference

| Category | Level | Fixable | Meaning |
|---|---|---|---|
| `missing-field` | 🔴/🟡 | sometimes | Required frontmatter field absent |
| `broken-link` | 🟡 | no | Wikilink target does not exist |
| `orphan` | 🔵 | no | Zero incoming links |
| `field-value` | 🔴/🟡 | no | Enum violation or out-of-range value |
| `idea-failure` | 🔴 | no | `status: failed` without `failure_reason` |
| `experiment-claim` | 🔴 | no | Experiment missing `target_claim` |
| `xref` | 🟡 | yes | Asymmetric cross-reference |
| `graph-edge` | 🔴 | no | Edge endpoints missing as wiki pages |
| `quality` | 🔵 | no | Empty sections in canonical templates |
| `lens-anchor` | 🟡 | no | Tier-0 page without any authority field |
| `lens-tier` | 🟡 | no | Tier-1-cluster wikilink of wrong type |

## Error modes

- Missing `wiki_dir` → exit 1 with `Error: <path> does not exist`.
- Unknown `--lens` id → exit 1 with `Error: lens '<id>' not found: …`.
- `LensValidationError` on `--lens` → exit 1 with validation message.
- Graph analyzer non-zero exit under `--rebuild-graph` → stderr warning,
  lint's own exit code preserved.

## When to run

- **Before every commit** on the vault repo (local pre-commit hook).
- **Before `/prompt`, `/distill`, `/gap`** — those tools trust the index,
  so structural inconsistencies should be caught first.
- **After `/ingest`** — new entries frequently arrive with partial
  frontmatter; `--fix` can patch the defaultable gaps.
- **After activating or switching a lens** — `--lens` surfaces
  lens-specific drift that v2.0 checks cannot see.

## Implementation notes

- `check_lens_anchors` short-circuits when `lens.anchors is None` or
  `authority_fields` is empty — zettelkasten-shaped lenses get no
  spurious yellow warnings.
- `check_lens_tier_consistency` ignores broken wikilinks to avoid
  double-reporting with `check_broken_links`.
- `rebuild_graph` uses `capture_output=True` so the analyzer's stdout
  doesn't interleave with lint's own JSON. Errors surface via stderr
  only when the analyzer exits non-zero.
- Keep lens id / lenses-base resolution consistent between lint and
  the rebuild-graph subprocess: if `--lenses-base` is passed to lint,
  it must also be forwarded to graph_analyzer so both resolve the same
  lens.
