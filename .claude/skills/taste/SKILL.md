---
name: taste
description: Lens-aware taste/analysis entry point. Under aesthetic-warburg, runs the Panofsky/Warburg pipeline on a visual input and produces an Aesthetic MD. Under engineering-alexander or general-zettelkasten, runs the lens's own taste contract — reports over the vault's tier-0/tier-1 distribution, not a creative deliverable. Behavior is driven by the active lens's `analysis_contract.taste`.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep, WebFetch, Task]
---

# /taste — Lens-aware taste and vault diagnostics

## Lens awareness (v2.1)

`/taste` dispatches on the active lens's `analysis_contract.taste` field.
That field is a list of report types the lens commits to produce. The
same command name serves three very different deliverables because
"what counts as taste" is a lens-level judgment, not a Bab-ilu-level one.

Runtime wiring (shared by every mode):

1. Read the active lens at `.agent/lenses/active/lens.yaml` via
   `tools/lens_loader.load_lens(lens_id)` — or honor `--lens <id>` when
   the user explicitly overrides.
2. Inject the lens's `prompts.md` via
   `tools.lens_context.active_lens_preamble()` at the top of every
   LLM-facing call. The preamble carries the lens's judgment rules, tone
   hints, and traps. Commands that skip this step will produce
   lens-shaped output with lens-neutral voice — a silent quality bug.
3. Resolve tier labels from `lens.entity_model` (`tier_0`, `tier_1_atom`,
   `tier_1_cluster`) and anchor rules from `lens.anchors.authority_fields`.
   Every downstream stage reads these, never hardcodes "work"/"motif".

### Dispatch table

| Lens                    | `analysis_contract.taste` contents                               | Behavior                                                  |
|-------------------------|-------------------------------------------------------------------|-----------------------------------------------------------|
| `aesthetic-warburg`     | `aesthetic_density_by_domain`, `motif_frequency_top20`, `panel_emergence_heatmap` | **Creative mode (legacy v2.0):** walk the Panofsky pipeline on the visual input, write an Aesthetic MD + optional Warburg panel. See the body of this skill below. |
| `engineering-alexander` | (lens-defined list)                                               | **Diagnostic mode:** report coverage of `incident × pattern` bipartite graph — which incidents lack patterns, which patterns have too few incidents, which pattern-languages are emergent. **No write to vault.** |
| `general-zettelkasten`  | (lens-defined list)                                               | **Diagnostic mode:** report Bloom-level distribution of notes, under-linked notes, concept-cluster gaps. **No write to vault.** |

The aesthetic-warburg mode is the only one that writes vault files —
because creative deliverables are its explicit contract. Non-aesthetic
lenses treat `/taste` as a read-only analytic pass. Their contract is
"surface what's interesting about the vault's current state", not
"produce a creative artifact".

### Flag summary (lens-aware)

- `--lens <id>` — override the active lens for this run
- `--report <name>` — run only one of the lens's declared taste reports
- `--panel` — aesthetic-warburg only; aggregate across ≥2 inputs into a
  Warburg panel (triggers an error under other lenses)
- `--domain <d>` — explicit domain hint for aesthetic mode
- `--regenerate` — aesthetic mode only; re-run the pipeline on an
  existing Aesthetic wikilink

If the caller passes a flag unsupported by the active lens, fail with a
clear message naming the lens — never silently ignore.

### Authority anchors are lens-scoped

Under aesthetic-warburg: `aat_id`, `iconclass`, `wikidata` are the
recognized authorities; the creative-mode pipeline performs AAT
substitution as part of `taste-synthesis`. Under
engineering-alexander: `rfc_id`, `cve_id`, `postmortem_url` are
expected — an incident page missing all of them surfaces as a
lens-anchor warning in `/lint --lens=engineering-alexander`. Under
general-zettelkasten: `authority_fields` is empty; no anchor checks fire
(the whole philosophy is "notes stand on their own logic").

Do not invent anchor checks inside `/taste` — the lint pass owns that.
`/taste` only reads anchors to decide whether enough provenance exists
to proceed.

---

## Aesthetic-warburg mode (worked example — legacy v2.0 body)

The remainder of this file documents the aesthetic-warburg
implementation, kept in full as the canonical creative-mode example.
Engineering and general modes read their deliverable contracts from
`lens.yaml` and do not need this section.

## What this command produces

For each visual input, `/taste` writes:

1. `wiki/aesthetic/{slug}.md` — Aesthetic MD with:
   - Frontmatter (aat_id, wikidata, warburg_panel, panofsky_layer, domain, prompts block)
   - Core observation prose (1–3 paragraphs, language = user's authoring language)
   - **Prompts section** (UI / image / video, each with Panofsky-structured skeleton)
   - **Academic Lineage section** (Warburg panel, Panofsky layer, AAT, Wikidata, cross-tradition notes)
2. Optionally: a new or updated `wiki/panel/{panel-slug}.md`

## Invocation

- `/taste` — **no argument**: picks the **newest file** in `raw/images/inbox/` (populated by the `ingest-image` hook when users paste images in chat). This is the canonical user path — **users only send images; the system handles everything else.**
- `/taste <path-to-image-or-video>` — single item at explicit path
- `/taste <directory>` — iterate over visual contents of a directory
- `/taste <wikilink-to-existing-aesthetic>` — regenerate prompts or update lineage for an existing card

Input must live in `raw/` (never analyze content outside the immutable layer — transient analysis violates the three-layer contract). The `raw/images/inbox/` entry point is populated automatically by `.claude/hooks/ingest-image.sh` so the user never touches the filesystem.

### Post-processing the consumed image

After `taste-synthesis` successfully writes the Aesthetic MD, it SHOULD move the consumed image from `raw/images/inbox/` to `raw/images/processed/{YYYY-MM}/{aesthetic-slug}.{ext}` — this keeps `inbox/` clean and creates a stable path that the Aesthetic MD's frontmatter `relations.derived_from` can point to. If the move fails (permissions, etc.), leave the file in inbox and log — the Aesthetic MD is still valid, the inbox just stays a little dirty.

## Flags

- `--domain <domain>` — explicit domain hint, skips taste-eye detection
- `--panel` — after producing Aesthetic MD(s), synthesize or update a Warburg panel covering the input set (requires ≥2 visuals to be meaningful)
- `--regenerate` — for existing Aesthetic wikilinks, re-run the pipeline and replace sections within llm:section markers
- `--modality <ui|image|video|all>` — restrict prompt generation to one modality (default: all three)

## Orchestration

Dispatches subagents per `schema.md §5.2`:

```
1. taste-eye (optional, when domain ambiguous)
   → detects domain, writes first-impression paragraph

2. taste-icon
   → Panofsky layer 1 (pre-iconographic) + layer 2 (iconographic)
   → outputs salient_motifs list for taste-lineage

3. taste-lineage
   → reads taste-icon's salient_motifs
   → scans wiki/panel/ for matching Warburg panels
   → outputs panel assignment (or proposes new panel) + cross-tradition notes

4. taste-synthesis
   → produces Panofsky layer 3 (iconological)
   → assembles three-modality prompts with labeled segments
   → performs Getty AAT vocabulary substitution pass
   → writes Aesthetic MD to wiki/aesthetic/
   → creates or updates wiki/panel/{panel-slug}.md
```

On Claude Code: invoke via the Task tool with `subagent_type` in order. On agents without native subagent support: fall back to sequential prompt chain with the same named stages.

## Panel synthesis (with --panel flag)

After all individual Aesthetic MDs are written, call `taste-synthesis` one more time with the full set of MDs as context. Task: produce or update a single Warburg panel MD covering shared Pathosformel.

Panel membership is recorded in the panel's `members:` frontmatter field. `generator_ready` flips to `true` when:
- Members ≥ 5, AND
- At least one member's prompts have `test_score ≥ 0.7` from `generative_regression` evaluation

When `generator_ready: true`, the panel MD also gets a "Cross-panel prompts" section synthesizing prompts across the panel's Pathosformel — the Nachleben mechanism operationalized.

## AAT / Wikidata resolution policy

Per `schema.md §5.3`:

- `taste-synthesis` attempts resolution. High confidence → fill `aat_id` and `wikidata` in frontmatter. Low confidence → `null` with `aat_uncertainty` / `wikidata_uncertainty` recording candidates.
- Never guess. Null is acceptable; `/check` surfaces unresolved items for user confirmation after 14 days.

## Output language policy

- Core observation prose: user's authoring language (default zh for Chinese users, en for international)
- Prompts section body: **English** regardless of prose language (generation models are English-trained; AAT terms are English) — see `schema.md §8` prompt language exception
- Academic Lineage section: authoring language for bullet text, but AAT/Wikidata links and IDs are English-canonical

## Section markers

All auto-generated sections use `<!-- llm:section-start {name} -->` and `<!-- llm:section-end {name} -->` markers per `schema.md §11`. User edits outside markers are preserved on regeneration. User edits inside markers signal disagreement and flag for `/check` reconciliation.

## Atomic writes

Every MD write is atomic (temp file + rename). Frontmatter is validated against Aesthetic frontmatter contract in `schema.md §4` before commit.

## Reporting

After completion, print:

```
/taste complete.

Wrote:
  wiki/aesthetic/{slug}.md
  wiki/panel/{panel-slug}.md  (new | updated)

Prompts generated:
  UI    ✓   cost: ~{N} tokens
  image ✓   compatible: <list of models>
  video ✓   compatible: <list of models>

Academic lineage resolved:
  Getty AAT: {id} | pending
  Wikidata:  {QID} | pending

Next step:
  - Open the Aesthetic MD in Obsidian to review
  - Copy the image/video prompt to your generator
  - After generation, run: /prompt --use {slug} <modality>
```

## Error modes

- Input not in `raw/` → halt with message to move the file into `raw/` first (three-layer contract)
- Input is not visual (plain text passed) → suggest `/ingest` instead
- taste-eye returns `domain: unknown` → halt, surface the error
- Existing Aesthetic MD at target path and no `--regenerate` flag → halt to avoid accidental overwrite

## Schema reference

- `schema.md §5` — academic anchor prompts (Warburg / Panofsky / AAT)
- `schema.md §5.2` — subagent definitions
- `schema.md §5.4` — prompt generation rules
- `schema.md §5.5` — Aesthetic MD terminal-section templates
