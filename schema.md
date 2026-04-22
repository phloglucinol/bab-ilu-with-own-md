# Bab-ilu Schema v2.1

> **Authoritative ontology contract.** Read by LLM agents at every session.
> **Schema version:** `2.1.0` (valid for project v2.2-alpha)
> **Source of truth for:** entity types, relation codes, frontmatter contracts, academic anchor prompts, lens scoping.
> **Derived from:** `PRD-v2.1-zh.md` (product positioning) and `PRD-v2-zh.md` (original design rationale).

## 0. Changelog

### 2.1.0 — 2026-04 (v2.1 Sprint 1–2, public in v2.2-alpha)

Backward-compatible additions. A vault authored against 2.0.0 continues to validate.

- **New entity type `synthesis`** (§2). `/ask` can file its answers back as
  `wiki/syntheses/<slug>.md`. Emitted by `tools/ask_runner.write_synthesis`.
  Schema-required frontmatter: `type`, `title`, `question`, `lens`, `date`,
  `cited` (list of source paths). Optional: `truncated: true` when body was
  capped. This operationalizes the Karpathy "query回存" mechanism — good
  answers compound into the wiki alongside ingested sources.
- **New optional frontmatter field `lens:`** (§4.2) on any entity. Declares
  which lens the entry belongs to. Entries without `lens:` are treated as
  owned by the currently active lens (`tools.ask_runner._frontmatter_matches_lens`).
- **Lens layer acknowledged** (§0.1). Schema.md now scopes its entity /
  relation contract to a *lens*. The aesthetic-warburg lens (this file's
  original subject matter — motif / pathosformel / topos / Panofsky
  three-layer output / academic anchors) is one of three first-wave lenses
  shipped in Sprint 2; `engineering-alexander` and `general-zettelkasten`
  carry their own entity vocabularies under `.agent/lenses/<lens-id>/`.
  See `docs/lens-spec.md` for the cross-lens contract.

### 2.0.0 — 2026-03

Original schema. Pathosformel-centric. Defined the 6 entity types (work,
motif, pathosformel, topos, person, source — plus `question` from `/gap`),
the relation codes, the Panofsky three-layer output contract, the dual
academic anchor layer, and the tier-1/tier-2 emergence rules.

## 0.1 Scope: this document describes the aesthetic-warburg lens

The entity types in §2 and the relation codes in §3 below describe the
**aesthetic-warburg lens**, which was Bab-ilu's first lens and carries the
visual-art-history vocabulary (motif / Pathosformel / Topos / Panofsky).
Other lenses define their own entities via `.agent/lenses/<lens-id>/lens.yaml`:

- `engineering-alexander` — post-mortem → pattern → pattern-language
- `general-zettelkasten` — source → atomic-note → concept-cluster

Cross-lens invariants — `synthesis` entity, `lens:` frontmatter field,
wikilink conventions (§5), authoring rules (§11) — apply to every lens.

## 1. Three-Layer Architecture

| Layer | Directory | Owner | Mutability |
|-------|-----------|-------|------------|
| Raw sources | `raw/` | User | Immutable — LLM never modifies |
| Human knowledge | `wiki/` | LLM writes; user curates | Read in Obsidian |
| Agent memory | `.agent/` | LLM owns | Hidden from Obsidian |

If a mechanism cannot land in one of these three layers, it does not belong in Bab-ilu.

## 2. Entity Types

Declared in frontmatter as `type:`.

**Aesthetic-warburg lens entities (the lens this doc describes):**

| Type | Purpose |
|------|---------|
| `work` | A specific visual artifact: painting, film frame, UI screenshot, photograph |
| `motif` | A named visual operation: reusable across works; atomic unit of Pathosformel |
| `pathosformel` | A tier-1 emergent cluster of motifs sharing works (Warburg term) |
| `topos` | A tier-2 emergent cluster of Pathosformel sharing motifs (classical term) |
| `person` | A creator: artist, director, designer, photographer |
| `source` | A book, paper, institutional archive, design methodology document |
| `question` | An open question surfaced by `/gap` analysis |

**Cross-lens entities (valid under every lens):**

| Type | Purpose |
|------|---------|
| `synthesis` | A filed-back `/ask` answer. Lives under `wiki/syntheses/<slug>.md`. Emitted by `tools/ask_runner.write_synthesis` when the user accepts the archive prompt. Always lens-scoped via the `lens:` frontmatter field. |

## 3. Relation Codes (in `.agent/graph/*.md`)

Syntax: `[[node-a]] [relationCode] [[node-b]]`

| Code | From type | To type | Semantics |
|------|-----------|---------|-----------|
| `exemplifiedBy` | motif | work | Work visually instantiates motif |
| `coOccurs` | motif | motif | Derived: two motifs appear in ≥1 common work |
| `cluster` | pathosformel/topos | motif/pathosformel | Aggregate contains member |
| `anchoredTo` | motif/work/person | external URI | AAT / Iconclass / ULAN / museum ID |
| `authoredBy` | work | person | Work's creator |
| `derivedFrom` | summary/source | source | Provenance chain |
| `retracts-<code>` | any | any | Retracts a prior asserted edge |

## 4. Frontmatter Contract

### 4.1 Common fields (all entities)

```yaml
---
type: <entity type>
---
```

That's the minimum. Most pages require nothing else.

### 4.2 Optional common fields

```yaml
schema_version: 2.1.0        # only if the page was auto-generated by a versioned tool
lens: <lens-id>              # lens this entry belongs to; if omitted,
                             # treated as owned by the currently active lens
created: YYYY-MM-DD          # for works: creation date of the artifact
seed: true                   # if imported from Bab-ilu seed kit
```

### 4.3 Per-type optional fields

**work:**
```yaml
medium: oil-on-canvas | film | photograph | digital | ...   # optional
```

**person:**
```yaml
active: YYYY-YYYY            # creator's active period, optional
```

**synthesis** (required contract — emitted by `/ask` archive):
```yaml
---
type: synthesis
title: <human-readable title>
question: <the original /ask query>
lens: <lens-id this synthesis was produced under>
date: YYYY-MM-DD
cited:                       # list of source paths the answer drew from;
  - wiki/...                 # empty list `cited: []` when no sources cited
  - wiki/...
truncated: true              # optional; present only if body was capped
---
```

No other fields are required on the aesthetic-warburg entities. All semantic information — motifs referenced, academic anchors, creators, related Pathosformel — lives in prose + `[[wikilinks]]`.

## 5. Wikilink Conventions

### 5.1 Syntax

- Bare: `[[slug]]` — display equals slug
- Aliased: `[[display|slug]]` — display is vault-language; slug is stable machine id

### 5.2 Slugs

- kebab-case English (or pinyin / romanization when appropriate)
- Stable after creation — never renamed without `/rename` atomic refactor
- Unique across the vault

### 5.3 Display names

- Vault language (`vault_language:` in CLAUDE.md)
- May be multi-word natural text
- May be edited freely — never affects the graph

## 6. Academic Anchors (Dual Layer)

### 6.1 Human layer (prose footnote)

Motif pages: subtitle line cites AAT ID and Iconclass where applicable.
Work pages: footer line cites museum/institutional ID and Iconclass.
Person pages: footer line cites ULAN.

### 6.2 Machine layer (`.agent/graph/anchors.md`)

Same information, structured:
```
[[motif-slug]] [anchoredTo] aat:300015650
[[work-slug]] [anchoredTo] rijks:SK-A-2344
[[work-slug]] [anchoredTo] iconclass:41C32
[[person-slug]] [anchoredTo] ulan:500024067
```

`/lint` verifies the two layers are consistent.

## 7. Graph Emergence Rules

See `.agent/spec/gap-algorithm.md` for the formal algorithm. Informal summary:

- **Tier 1 activates immediately.** Input: Work × Motif bipartite graph, projected onto motif-motif weighted graph (Jaccard / Newman-normalized). Algorithm: Leiden at resolution γ (default 1.0). Threshold: adaptive — candidate cluster qualifies as Pathosformel iff `|motifs| ≥ k` and each motif has `≥ l` exemplifying works, where `k, l = max{3, ⌈log₂(|motifs_total|)⌉}`. Pathosformel candidates written to `.agent/todos/` pending user naming.
- **Tier 2 activates at `|pathosformel| ≥ 15`** or manual `/gap --tier=2`. Input: Pathosformel-Pathosformel graph, edge weight = shared motif count (Jaccard). Same algorithm, produces Topos candidates.
- **Aggregate nodes** (`pathosformel`, `topos`) are excluded from being clustered in subsequent runs. Prevents self-cycle.
- **Retraction** of bad inferences via append-only `retracts-<code>` lines.

## 8. Panofsky Output Contract

`/taste` and `/prompt` must produce output structurally separated into three layers:

- **`[pre-iconographic]`** — concrete visual description (color, light, composition, material, framing)
- **`[iconographic]`** — cultural/period/genre markers
- **`[iconological]`** — mood, worldview, symbolic meaning

Plus a fourth segment:
- **`[lineage]`** — Pathosformel wikilink · AAT/Iconclass term · signature author

`/lint` checks motif prose visibly separates these three layers (not collapsed into adjective soup).

## 9. Vault Language

Declared once at `/genesis` time in `.agent/CLAUDE.md`:
```yaml
vault_language: zh  # or: en, es, fr, ja, ...
```

All agent output to user (prose, explanations, question text) uses this language. Cross-language source material is processed via `/distill` (cognitive reconstruction, not translation).

Generated prompts for AI models (Midjourney, Sora, etc.) remain English regardless of vault language — generation models are English-trained and AAT vocabulary is English-canonical.

## 10. Glossary

`wiki/_glossary.md` is a first-class bilingual term reference. Populated at `/genesis`, extended as vault-specific conventions emerge. Non-native English readers read this first when encountering Pathosformel/Topos/Nachleben/etc.

## 11. Authoring Rules

- Atomic writes (temp file + rename). Never partial writes.
- `wiki/` is authoritative source for wikilinks; `.agent/graph/` is derived + LLM inferences, append-only.
- Never silently overwrite user-authored prose. LLM sections use `<!-- llm:section-start <name> -->` / `<!-- llm:section-end <name> -->` markers.
- Uncertainty recorded in `.agent/state/vocabulary_resolution.md`, not guessed.
- Every `type: pathosformel` and `type: topos` page must cite its member wikilinks in prose.

## 12. Version

Current: `2.1.0` (valid for project v2.2-alpha). Patches bump patch version. Additive field or entity-type additions bump minor (2.0.0 → 2.1.0 added the `synthesis` entity and the `lens:` field). Breaking changes require major bump + migration doc in `archive/MIGRATIONS/`.
