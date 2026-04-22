---
name: prompt
description: Lens-aware deliverable producer. Reads the active lens's `deliverable_types` list and emits the lens-specific creative output — aesthetic-warburg produces four-segment UI/image/video generation prompts, engineering-alexander produces Pattern cards (problem-solution-context triads), general-zettelkasten produces Progressive Summaries. Behavior switches on the active lens; the v2.0 aesthetic body is preserved as the worked example.
allowed-tools: [Read, Write, Edit, Glob, Grep, Task]
---

# /prompt — Lens-aware deliverable generator

## Lens awareness (v2.1)

`/prompt` is the lens-specific *deliverable* producer. Each lens declares
what "a useful creative output" means for its domain via
`lens.deliverable_types`. The same command name produces three very
different artifacts because deliverables are a lens-level value
judgment, not a Bab-ilu-level one.

Runtime wiring (shared by every mode):

1. Resolve the active lens via `tools/lens_loader.load_lens(lens_id)` —
   honor `--lens <id>` when explicitly overridden.
2. Inject `tools.lens_context.active_lens_preamble()` at the top of
   every LLM-facing stage. The lens's `prompts.md` carries the tone,
   rubrics, and traps specific to this deliverable form.
3. Pull `tier_0` / `tier_1_atom` / `tier_1_cluster` from
   `lens.entity_model` — the input wikilink shape and its downstream
   resolution are all tier-typed, not hardcoded to "aesthetic" or
   "panel".
4. Emit exactly one deliverable per invocation, shaped by the first
   entry of `lens.deliverable_types` unless the user passes
   `--type <name>` to select a different one the lens declared.

### Deliverable table

| Lens                    | `deliverable_types` declared in lens.yaml | Output shape                                                                                                                           |
|-------------------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `aesthetic-warburg`     | `[aesthetic, panel]` (landed)              | `aesthetic` → four-segment labeled prompt (Subject / Style / Composition / Motion) for UI/image/video sub-modalities; `panel` → Warburg panel-level prompt |
| `engineering-alexander` | `[pattern-card]` (proposed)                | Alexander-style Pattern card: `Context → Problem → Forces → Solution → Resulting-context` with incident citations as Examples          |
| `general-zettelkasten`  | `[progressive-summary]` (proposed)         | Three-layer Progressive Summary: bold-highlighted key sentence in layer 1, 3–5 bold fragments in layer 2, one-sentence thesis in layer 3 |

`aesthetic-warburg` is the landed lens — its `deliverable_types` field
in `.agent/lenses/aesthetic-warburg/lens.yaml` declares exactly two
deliverables (`aesthetic`, `panel`). The UI / image / video
distinction within the `aesthetic` deliverable is *internal dispatch*
handled by the v2.0 modality flag below, not a separate top-level
`deliverable_types` entry. Engineering-alexander and
general-zettelkasten are proposed lenses — their `deliverable_types`
above are the shape this skill commits to emit when those lens.yaml
files ship.

`/prompt` reads `lens.deliverable_types` at runtime. If the active
lens does not declare the deliverable the user requested (via
`--type <name>`), fail loudly with the list of declared types. Each
deliverable's section order / field names come from the lens's prompts
(tone + rubric) plus this skill's body (worked aesthetic-warburg
markup); if the lens wants a different section order, it should ship a
lens-specific overlay of this skill rather than mutate the skill
itself.

### Mode × lens compatibility

The four v2.0 modes (`<slug> <modality>`, `--panel`, `--use`,
`--promote`) are aesthetic-warburg-shaped and remain the aesthetic
implementation. Under other lenses:

- Engineering mode has a single invocation form:
  `/prompt <incident-slug>` or
  `/prompt --pattern-language <cluster-slug>` for cross-pattern
  emergence prompts. `--use` and `--promote` still apply — the Pattern
  card accumulates incident citations and can be promoted to a
  standalone `type: pattern` entity in `wiki/pattern/`.
- Zettelkasten mode: `/prompt <note-slug>` produces a Progressive
  Summary for that note. `--cluster` expands to summarize a
  concept-cluster. `--use` logs review events; `--promote` turns a
  frequently-reviewed summary into a standalone `type: summary` entity.

If the caller passes a flag the active lens's `deliverable_types` does
not recognize, fail with a message naming the lens and listing the
accepted flags — never silently run the wrong mode.

### Log events are lens-tagged

Every write to `wiki/_log/usage.jsonl` includes a `lens` field so the
log can be replayed under the same lens later. Without this tag,
`/gap` and `/taste` diagnostic mode cannot tell which deliverables
were produced under which regime.

```jsonl
{"action": "prompt.generate", "lens": "engineering-alexander", "entity": "incident-2024-09-s3-region-a", "type": "pattern-card", "ts": "..."}
```

---

## Aesthetic-warburg mode (worked example — legacy v2.0 body)

The remainder of this file documents the aesthetic-warburg
implementation in full. Engineering and zettelkasten modes pull their
output schemas from `lens.deliverable_types.<name>.schema` and do not
share this section's markup.

## Four operating modes

```
/prompt <aesthetic-slug> <modality>               # regenerate prompt for one modality
/prompt --panel <panel-slug> <modality>           # cross-motif panel-level prompt
/prompt --use <aesthetic-slug> <modality>         # log a usage event + optional score
/prompt --promote <aesthetic-slug> <modality>     # promote prompt to standalone type:prompt entity
```

Modalities: `ui | image | video`.

## Mode 1 — Regenerate prompt

Use when an Aesthetic exists but its prompt for a given modality is absent, stale (> 30 days without testing), or underperforming (`test_score < 0.7`).

Execution:
- Read the Aesthetic MD
- Invoke `taste-synthesis` subagent with the modality flag — it reads the existing Core observation and Academic Lineage to produce a fresh prompt
- Replace the corresponding `### {modality} prompt` block inside `<!-- llm:section-start prompts -->` markers atomically
- Update `prompts.<modality>.generated` date in frontmatter; reset `last_tested` and `test_score` to null

## Mode 2 — Panel-level prompt

Use when a Warburg panel has reached `generator_ready: true` (≥5 members, ≥0.7 scored prompts). The output is a prompt that operates **within the Pathosformel tradition** rather than imitating any single member — the Nachleben mechanism operationalized.

Execution:
- Read the panel MD and every member's Aesthetic MD
- Invoke `taste-synthesis` with the full set as context
- Synthesize the shared motifs, substituting AAT-canonical terms for folk labels
- Write or update the panel's `## Cross-panel prompts` section inside llm:section markers
- The output prompt does NOT cite a single signature author — it cites the panel: `[lineage] Warburg panel: [[{panel}]] · AAT: {term} (aat:{id})`

Panel-level prompts are the strongest generation output Bab-ilu produces. Surface this in the report.

## Mode 3 — Log usage

Records that a prompt was actually used in a generator. Interactive: prompts the user for:

- Which model was used (from the `compatible_models` list, or new)
- Subjective score 0.0–1.0 (optional)
- Free-text note about the run (optional)

Appends to the Aesthetic's `prompts.<modality>`:
- Updates `last_tested` to today
- Updates `test_score` (rolling average or latest, per config — default latest)

Also appends to `wiki/_log/usage.jsonl`:

```jsonl
{"action": "prompt.use", "aesthetic": "{slug}", "modality": "{m}", "model": "{name}", "score": <float>, "ts": "<ISO-8601>"}
```

## Mode 4 — Promote

Promotes a favored prompt to a standalone `type: prompt` entity. Use when a prompt has proven reusable across projects and deserves library citizenship.

Execution:
- Read the Aesthetic MD and extract the modality-specific prompt from its Prompts section
- Attach the generated prompt body under the parent cluster's `## Prompts` section in the tier_1_cluster MD that owns it (e.g. for aesthetic-warburg, the Warburg `wiki/panel/<panel-slug>.md` file; for engineering-alexander, the `wiki/pattern-language/<language-slug>.md` file). Do not write to a separate `wiki/_prompts/` directory — that v1.4 auxiliary path is not declared by any lens. Frontmatter within the attached block uses:

```yaml
---
id: {prompt-slug}
type: prompt
title: {human-readable name}
modality: ui | image | video
promoted_from: [[{aesthetic-slug}]]
compatible_models: [<inherited from Aesthetic>]
panofsky_structure: true
aat_anchors: [<list of AAT IDs cited in the prompt>]
warburg_panels: [[[{panel-slug}]], ...]
usage_count: 0
tested_runs: []
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
schema_version: "2.1.0"
relations:
  - {type: derived_from, target: [[{aesthetic-slug}]]}
  - {type: exemplifies, target: [[{panel-slug}]]}
---
```

Body:

```markdown
# {title}

## Purpose
<1–2 sentences: what this prompt is for and what kind of work it serves best.>

## The prompt
{full prompt text with all four [labeled] segments}

## Recommended generators
<list with any model-specific tuning notes>

## Lineage
<brief summary of Warburg panel and academic anchors this prompt participates in>

## Test history
<rolling log of runs with model, score, note>
```

- Append a log entry to `wiki/_log/usage.jsonl` with `action: prompt.promote`

## Atomic writes

All mutations to Aesthetic MDs go through temp-file-plus-rename. Section content inside `<!-- llm:section-start prompts -->` markers is replaced as a unit — never partially.

## Schema reference

- `schema.md §4` — Prompt entity frontmatter contract
- `schema.md §5.4` — prompt generation rules
- `schema.md §6` — panel with generator_ready flag
- `schema.md §9` — generative_regression evaluation method

## Ground rules

- Never fabricate a `test_score`. Scores come from actual user runs (`--use`) or from `generative_regression` eval runs — never from the LLM's own inspection of the prompt text.
- Promoted prompts are not deleted from source Aesthetic MDs. The Aesthetic always carries the prompt; promotion is a cross-reference, not a move.
- Panel-level prompts may cite multiple panels when a subject's Pathosformel genuinely bridges panels; do not force single-panel attribution.
