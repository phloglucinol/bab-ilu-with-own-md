# Bab-ilu v2.1 Lens Specification

> **Authoritative reference** for `.agent/lenses/<lens-id>/lens.yaml`.
> The JSON Schema that validates every `lens.yaml` lives at
> `.agent/lenses/schema.json` and is consumed by
> `tools/lens_loader.load_lens`. This document explains each field —
> what it means, where it's used downstream, what a good value looks
> like, and what mistakes look like.

A lens is how Bab-ilu's horizontal tooling (commands, graph analyzer,
linter, vault structure) knows what "a useful observation", "a
recurring atom", and "an emergent cluster" mean inside one discipline.
Three first-wave lenses ship in Sprint 2:

| Lens id                | Worked example in this doc                                          |
|------------------------|---------------------------------------------------------------------|
| `aesthetic-warburg`    | *Landed in Sprint 1.* Visual aesthetics → motifs → Pathosformel bundles. |
| `engineering-alexander` | *Landed in Sprint 2.* Post-mortems → patterns → pattern-languages. |
| `general-zettelkasten` | *Landed in Sprint 2.* Sources → atomic notes → concept-clusters.    |

## 1. File location and lifecycle

- Every lens lives at `.agent/lenses/<lens-id>/` containing at minimum:
  - `lens.yaml` — structured config (this spec covers it)
  - `prompts.md` — freeform judgment rules, tone, traps; injected into
    LLM context at runtime by `tools/lens_context.py` (B3)
- `/genesis <lens-id>` materializes `.agent/lenses/active/` as a copy of
  the chosen lens; commands resolve against `active/` at runtime
- `lens.yaml` is read once per process and cached by
  `tools.lens_loader.load_lens` keyed on file mtime
- A vault can carry many lens source directories but only one `active/`

## 2. Required top-level fields

The schema requires every `lens.yaml` to include all of these:

- `id` — slug, kebab-case, must match parent directory name
- `version` — semver
- `name` — human-readable label
- `description` — one paragraph explaining what the lens does
- `deliverable_types` — non-empty list of top-level deliverable strings
- `entity_model` — `{tier_0, tier_1_atom, tier_1_cluster}`
- `activation` — `{mode: "always" | "triggers", triggers?: […]}`
- `analysis_contract` — optional `gap` + required-if-present `taste`

Omitting any of these causes `load_lens` to raise
`LensValidationError`; `/genesis`, `/lint --lens`, and the graph
analyzer all exit non-zero when this happens. No silent fallback.

### 2.1 `id` (string, kebab-case)

Must match `^[a-z][a-z0-9-]*[a-z0-9]$` and equal the parent directory
name. `aesthetic-warburg` is the landed canonical form;
`engineering-alexander` and `general-zettelkasten` are the Sprint 2
additions. Short-form slugs (e.g. `general-zettelkasten` rather than
`general-zettelkasten-bloom`) are preferred — they keep CLI invocations
readable and reviewer reports compact.

### 2.2 `version` (semver string)

`MAJOR.MINOR.PATCH(-prerelease)?`. Bumping the MAJOR invalidates the
lens's seed kit's compatibility; bumping MINOR adds fields compatibly;
PATCH is pure prose/weighting changes. The current landed lenses ship
at `1.0.0`.

### 2.3 `name` and `description`

Human reads these. `name` appears in `/genesis` prompts and `/lint`
warnings; `description` appears in `/genesis` when picking between
lenses. Keep `description` to one paragraph and include *what* the lens
emerges (e.g. "emerges Pathosformel panels from recurrent motifs") not
just the domain.

### 2.4 `deliverable_types` (list of strings, ≥1)

What `/prompt` and `/ingest` can be told to produce under this lens.
Each string is a top-level deliverable the vault commits to. Example
values:

- Landed `aesthetic-warburg`: `[aesthetic, panel]`
- Landed `engineering-alexander`: `[pattern-card, pattern-language-brief]`
- Landed `general-zettelkasten`: `[progressive-summary, zettel-cluster-map]`

Not every tier label is a deliverable — most lenses treat `tier_0` as
the *observation* (you author it by hand) and name only the *emergent*
outputs here. The aesthetic-warburg landed value of `[aesthetic, panel]`
treats both the raw aesthetic MD and the Pathosformel panel as
deliverables because both are produced by a `/prompt` invocation.

### 2.5 `entity_model` (object)

Three required string values:

```yaml
entity_model:
  tier_0: aesthetic          # or incident / source / observation
  tier_1_atom: motif         # or pattern / note / anomaly
  tier_1_cluster: panel      # or pattern-language / concept-cluster
```

These strings become:

- Frontmatter `type:` values on seed and vault entries under that lens
- Directory names under `wiki/` (e.g. `wiki/aesthetic/`, `wiki/motif/`,
  `wiki/panel/`) — by convention; the schema does not enforce this
- Keys in every downstream pipeline doc: the `/gap` algorithm spec
  (`docs/superpowers/plans/` or `.agent/spec/gap-algorithm.md`), `/lint`
  anchor checks, and the graph analyzer's clustering output

`tier_2_cluster` is **not** required — it's a proposed Sprint 2+
extension to the schema. Lenses that don't declare it silently skip
tier-2 clustering (the graph analyzer reads `.tier_2_cluster` via
`getattr(…, None)`).

### 2.6 `activation` (object)

Controls when a file activates this lens (for multi-lens vaults where
different files belong to different lenses).

```yaml
activation:
  mode: always        # OR
  mode: triggers
  triggers:
    - "|aesthetic| >= 1"
    - "|motif| >= 2"
```

Trigger strings follow the DSL `|<slug>| >= <int>` and are
AND-combined (per `lens_loader._evaluate_triggers`, locked in Pass 3
by C1's integration test). `always` mode skips the triggers check.

`triggers` is required when `mode: triggers` and forbidden when
`mode: always` — the conditional is encoded in the JSON Schema's
`allOf`/`if`/`then` block.

### 2.7 `thresholds` (object, optional)

Five number fields with defaults. Used by the graph analyzer and
`/lint`:

- `cluster_member_min` (int ≥1, default 3) — minimum tier_1_atom count
  a tier_1_cluster entry must wikilink to
- `cluster_min_size` (int ≥1, default 3) — community detection drops
  clusters smaller than this
- `density_multiplier` (float >0, default 3.0) —
  `density_min = multiplier × baseline_density`
- `orphan_min_degree` (int ≥0, default 1) — tier_0 below this degree is
  flagged orphan by `/gap`
- `domain_min` (int ≥1, default 5) — each `allowed_subdomain` must have
  this many tier_0 entries or `/gap` warns

Omit the whole block to use all defaults.

### 2.8 `anchors` (object, optional)

```yaml
anchors:
  authority_fields:
    - aat_id
    - wikidata
  external_vocabularies:
    - id: aat
      url: https://www.getty.edu/research/tools/vocabularies/aat/
```

`authority_fields` is the list of frontmatter field names `/lint
--lens=<id>` treats as valid institutional anchors. A tier-0 page
missing *all* of these fires a yellow `lens-anchor` warning.
Zettelkasten-shaped lenses omit this block entirely, silently skipping
the anchor check (by design — notes stand on their own logic).

`external_vocabularies` is advisory metadata for documentation and
`/ingest` hints.

### 2.9 `allowed_subdomains` (list of kebab strings, optional)

Permitted values for the `domain` frontmatter field on tier-0 entries.
Aesthetic-warburg declares `[cinema, photo, ui, ux, graphic, game,
architecture, illustration, painting]`. Engineering-alexander would
declare runtime/build/storage/network etc. General-zettelkasten leaves
it empty (open domain).

An empty or missing list tells `/gap` to skip the
`underpopulated_domain` check for this lens.

### 2.10 `community_detection` (object, optional)

```yaml
community_detection:
  algorithm: louvain     # or: leiden
  resolution: 1.0
  random_state: 42
```

Only two algorithms are accepted. `louvain` is the landed default —
aesthetic-warburg uses it and `tests/test_graph_analyzer_lens.py`
asserts reproducibility under the landed config. Lenses may opt into
`leiden` when their graph characteristics benefit from resolution-tunable
modularity.

### 2.11 `analysis_contract` (object, required)

```yaml
analysis_contract:
  gap:
    - underpopulated_domain
    - orphan_aesthetic
    - disconnected_clusters
  taste:
    - aesthetic_density_by_domain
    - motif_frequency_top20
```

- `gap` is the list of gap categories this lens exposes to the `/gap`
  command. Order matters only for presentation — `/gap` reports in
  declared order.
- `taste` is the list of analytical reports `/taste --report <name>`
  can produce. Must be non-empty if the key is present.

### 2.12 `extensions` (object, optional)

Free-form dictionary for lens-private config. `additionalProperties:
true`. Aesthetic-warburg uses it for
`warburg.mnemosyne_panel_target_count: 63`. Do not depend on another
lens's `extensions` values — treat it as private.

## 3. `prompts.md` (companion file, not covered by schema)

Beside `lens.yaml`, every lens MUST ship a `prompts.md` containing
freeform judgment rules, tone hints, traps, and lens-specific
vocabulary. `tools/lens_context.py` reads this at runtime and wraps it
in a `<lens-context>…</lens-context>` envelope injected at the top of
every LLM call initiated by a Bab-ilu command.

Minimum sections:

- **Judgment rules** — rubrics for deciding when a candidate qualifies
  (e.g. "a Pathosformel requires ≥3 motifs across ≥2 eras")
- **Tone and voice** — how the lens wants the LLM to write
  (e.g. "Warburg is evocative, avoid category labels")
- **Traps** — known failure modes (e.g. "do not confuse a folk symbol
  with an AAT-canonical term")

The companion file is what makes a lens feel *distinctive* at runtime.
A lens that ships identical boilerplate prompts.md across disciplines
loses the one thing that can't be expressed in YAML. Reviewers should
flag prompts.md that reads like a generic template.

## 4. Validation

At any time:

```
python -m tools.lens_loader --validate .agent/lenses/<lens-id>
```

Exits 0 with "ok" if the lens.yaml conforms to the schema and the
activation trigger DSL parses. Exits non-zero with the validation error
on any deviation. CI and `/lint` both run this on every pass.

## 5. Adding a new lens

Bootstrap checklist:

1. Pick a short-form id (`kebab-case`, aim for 1–3 tokens)
2. Copy an existing lens dir as scaffolding; rename
3. Fill in `entity_model` — this is the decision that locks the rest
   (wiki/ directory names, /lint checks, graph analyzer output)
4. Write `prompts.md` — the hard part; don't skimp
5. Populate `seed-kit/<lens-id>/` with ≥25 exemplary entries
6. Run `python -m tools.lens_loader --validate .agent/lenses/<lens-id>`
7. Run `/genesis <lens-id> --dry-run` to confirm materialization works
8. Add an integration test in `tests/test_lens_integration.py`

## 6. Schema evolution

The schema is versioned implicitly via its own git history. Additions
that are `additionalProperties: false` breaks are a MINOR bump of
every lens's `version`. Removing a required field is a MAJOR bump.
There is no compat shim — the schema plus landed lens.yaml files are
one atomic unit.

## 7. Reference

- Schema file: `.agent/lenses/schema.json`
- Loader: `tools/lens_loader.py`
- Runtime injector: `tools/lens_context.py`
- Integration tests: `tests/test_lens_loader.py`,
  `tests/test_lens_integration.py`, `tests/test_lens_context.py`
- `/genesis` activation hook: `.claude/skills/genesis/SKILL.md`
- `/lint` lens-aware extension: `.claude/skills/lint/SKILL.md`
