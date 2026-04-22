---
name: check
description: Health audit across the vault. Reads schema.md as the contract and reports divergences — schema-version drift, missing auto-generated sections, stale AAT/Wikidata resolutions, expired prompt tests, unstable Warburg panels, glossary drift, broken links, orphan pages, and freshness violations. Produces an actionable report.
allowed-tools: [Read, Glob, Grep, Bash]
---

# /check — Vault Health Audit

## Philosophy

`/check` treats `schema.md` as the contract and `wiki/` as the implementation. Its job is to surface every place the implementation diverges from the contract — so the user (or `/taste` / `/ingest` re-runs) can reconcile.

`/check` is read-only. It never auto-fixes. Each finding comes with a suggested next step.

## Invocation

```
/check                     # full audit
/check --aesthetics        # only aesthetics/_panels/_prompts
/check --stale             # only freshness / AAT 14-day grace / prompt 30-day
/check --fix-safe          # apply ONLY the fixes where no human judgment is required
/check --rebuild-index     # full scan, rewrite wiki/index.md from wiki/ state
/check --migrate           # additive schema bump (e.g. 1.3 → 1.4 → 2.1) — adds null fields, never rewrites content
```

`--fix-safe` is the single exception to read-only — and it applies only to mechanical rebuilds (edges.jsonl, wikilink regeneration), never to content.

## Check categories

### Category 1 — Schema conformance

Read `schema.md` to get current `schema_version`. For every MD under `wiki/`:

- Frontmatter has all required fields for its `type:` — per `schema.md §4`
- `schema_version` in the MD matches or is ≤ current (missing → flag for migration)
- Frontmatter YAML parses — malformed YAML is a hard error

### Category 2 — Aesthetic-specific

For every `type: aesthetic`:

- `aat_id` resolved OR `aat_uncertainty` present (past 14-day grace window = surface)
- `wikidata` resolved OR `wikidata_uncertainty` present (same grace policy)
- `panofsky_layer` declared
- Body contains `<!-- llm:section-start prompts -->` ... `<!-- llm:section-end prompts -->` markers
- Body contains `<!-- llm:section-start academic-lineage -->` ... markers
- Each modality in `prompts:` frontmatter block has at least a `generated:` date
- `warburg_panel` wikilinks resolve to existing panel MDs

### Category 3 — Prompt freshness

For every `type: aesthetic` with `prompts.<modality>.last_tested`:

- If `last_tested` is null AND `generated` was > 30 days ago → flag "prompts never tested"
- If `last_tested` was > 30 days ago → flag "prompt tests stale, recommend generative_regression run"
- If `test_score < 0.7` → flag "prompts underperforming; consider regeneration"

For `type: prompt` (standalone, promoted):

- At least one `tested_runs` entry present within 30 days
- `compatible_models` list non-empty

### Category 4 — Warburg panels

For every `type: panel` in `wiki/panel/`:

- `members` list has ≥ 3 entries (panels with 1–2 members are "potentially unstable")
- If `generator_ready: true`, cross-panel prompts section exists
- If `generator_ready: false` but members ≥ 5 AND at least one member has `test_score ≥ 0.7` → recommend setting generator_ready true
- Pathosformel statement present and non-empty

### Category 5 — Bilingual glossary

- Parse `wiki/_glossary.md` into term pairs
- Scan all MDs for `original_terms` in frontmatter; every term there must appear in `_glossary.md`
- Surface drift: terms in MDs but missing from glossary; glossary entries unreferenced anywhere

### Category 6 — Graph integrity

- Every `[[wikilink]]` resolves (broken links listed)
- Every `relations:` target resolves
- Orphan pages: MDs with zero inbound relations AND zero inbound wikilinks (potential forgotten pages)
- `edges.jsonl` staleness: if last rebuild is older than a frontmatter mutation, flag

### Category 7 — Freshness

For every entry with `freshness_class` and `last_validated`:

- `evergreen`: never stale
- `stable`: stale if `last_validated > 365 days ago`
- `volatile`: stale if `last_validated > 90 days ago`
- `dated`: recommend archive to `wiki/_archive/` if unreferenced for 90+ days

### Category 8 — Evaluation coverage

- Does `wiki/_evals/` have samples for each domain (`cinema/photo/ui/ux/graphic/game/architecture/illustration/painting` — v1.4 adds `ux` and `painting`)?
- Do any domains have < 5 samples (well below the 20-per-domain v1 target)?
- Are there eval samples with missing `inter_coder_agreement` scores past 30 days?

### Category 9 — Karpathy primitives

**`wiki/index.md`**:
- File exists at `wiki/index.md` (soft requirement — treated as the vault's human-facing table of contents; absent is a warning, not a block)
- Scan every `wiki/<tier>/` directory declared by `lens.entity_model` (`tier_0`, `tier_1_atom`, `tier_1_cluster`) plus the shared `wiki/people/` and `wiki/source/` directories; compare to listed wikilinks in `index.md`
- Flag: files on disk not in index (missing entries) · wikilinks in index pointing to non-existent files (dead links)
- Offer `--rebuild-index`

**`wiki/log.md`**:
- File exists at `wiki/log.md` (soft requirement — human-readable audit trail)
- Count entries in `wiki/_log/usage.jsonl` for `action: ingest|taste|distill|compile|prompt` since last rebuild date
- Count entries in `wiki/log.md` since same date
- If mismatch > 3 entries → flag "log.md out of sync with usage.jsonl"
- Offer `--rebuild-log` (append missing entries, never reorder)

### Category 10 — Authoritative citation

For every `type: aesthetic` and `type: panel` (aesthetic-warburg lens):

- At least one of these fields must be non-null: `aat_id` · `wikidata` · `iconclass` · `ulan_id` · any museum/institution ID (`met_id`, `moma_id`, `cooperhewitt_id`, `rijks_id`, `tate_id`, `nga_id`, `bfi_id`, `magnum_id`, `archnet_id`, `riba_id`, `loc_cai`, `gcd_id`, `moby_id`, `igdb_id`) · `iso_standard` · `nng_url`
- If all null past 14-day grace window → surface "no authoritative anchor"
- Enforces `schema.md` §11's authoritative-anchor rule for the aesthetic-warburg lens; other lenses declare their own anchor fields in `.agent/lenses/<id>/lens.yaml` and have their own variants of this check.

For `type: source` in `wiki/_refs/`:

- `canonical: true` requires human confirmation (never LLM-autonomous). Flag any `canonical: true` entry that was created by an LLM write skill in the last 7 days without a human commit.

## Output format

A concise, actionable report — not a dump.

```
Bab-ilu vault health: {SCORE}  (reports: {N} items)

Schema: {PASS | FAIL}
Aesthetic integrity: {N/M conformant}
Prompt freshness: {N stale · N never tested}
Warburg panels: {N stable · M unstable}
Bilingual glossary: {N drift items}
Graph: {N broken links · M orphans}
Freshness: {N stale entries}
Evaluation coverage: {per-domain counts}

Top priority items (resolve first):
  1. [{severity}] {one-line finding} — suggested: {action}
  2. ...

Full report written to: docs/check-{YYYY-MM-DD-HHMM}.md
```

`--fix-safe` applied actions (if flag given):
- `edges.jsonl` rebuilt from frontmatter
- `## Relations` sections regenerated from frontmatter relations blocks
- `wiki/index.md` / `wiki/log.md` scaffold re-created if missing (empty headers only, never content)

`--rebuild-index`: full scan rewrites `wiki/index.md` using paths resolved from `lens.entity_model`:
- Scan `wiki/<tier_0>/*.md` → one-line entry per file with title + first body paragraph's first sentence as hook
- Scan `wiki/<tier_1_cluster>/*.md` → list with member count + `generator_ready` state
- Scan `wiki/people/*.md` → list by declared domain frontmatter (no hardcoded subdirs)
- Prompt deliverables are attached to the parent cluster MD's `## Prompts` section (they do NOT live under a separate `wiki/_prompts/` directory — that path was a v1.4 auxiliary no lens declares)
- Scan `wiki/_refs/_spine/` / `_institutions/` / `_domains/` → list with `canonical:` state (these three aux dirs are still vault-wide references, not tier paths)
- Preserve the `## Empty-state Guide` and `## Maintenance` sections (they are boilerplate, not auto-generated)

`--rebuild-log`: append-only reconciliation:
- Read `wiki/_log/usage.jsonl`
- Compare to entries already in `wiki/log.md`
- Append missing entries in chronological order under today's date heading
- Never reorder, never delete existing entries

`--migrate`: additive schema bump (cross-version; current target is 2.1.0):
- Read `schema.md` top version
- For every MD with older `schema_version:`, add new optional fields as `null` per schema diff
- Bump `schema_version:` to current
- Never rewrite body content; never change existing field values
- Report diff per file before applying; `--dry-run` flag supported

## Error modes

- `schema.md` missing or malformed → halt; the vault has no contract to check against
- `wiki/` empty → report nothing-to-check and exit cleanly

## Schema reference

- `schema.md §10` — maintenance command specification
- `schema.md §11` — conventions including section markers
- `schema.md §12` — versioning
