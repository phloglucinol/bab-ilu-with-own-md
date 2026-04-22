---
name: distill
description: Lens-aware cognitive reconstruction of foreign-language sources into the user's vault language. Not translation — rewrites content using the target language's conceptual vocabulary while preserving key original terms as bilingual anchors. The set of *anchor types* to preserve is per-lens (aesthetic-warburg keeps AAT/Iconclass/Wikidata verbatim; engineering-alexander keeps RFC/CVE/post-mortem IDs; general-zettelkasten keeps no institutional anchors but records all proper nouns). Feeds the lens's terminology ledger.
allowed-tools: [Read, Write, Edit, Glob, Grep]
---

# /distill — Lens-aware L2 cognitive reconstruction

## Lens awareness (v2.1)

`/distill` is lens-agnostic in its *core mechanic* (source language →
vault language, preserving key terms as bilingual anchors), but
lens-specific in **which terms qualify as anchors** and **where the
distilled output lives in the vault**.

Runtime wiring:

1. Resolve the active lens at `.agent/lenses/active/lens.yaml` via
   `tools/lens_loader.load_lens(lens_id)`; honor `--lens <id>`.
2. Inject `tools.lens_context.active_lens_preamble()` at the top of the
   distillation LLM call — the lens's `prompts.md` encodes
   domain-appropriate reconstruction judgment (e.g. aesthetic-warburg
   forbids swapping AAT-canonical terms for folk labels; engineering
   requires preserving version numbers and CVE IDs verbatim).
3. Read anchor rules from `lens.anchors.authority_fields` — the same
   fields `/lint --lens=…` enforces on tier-0 pages — and use them to
   decide which source-language terms must be kept verbatim (with the
   vault-language gloss in parentheses) versus distilled into
   target-language phrasing.
4. Resolve the output folder from `lens.entity_model.tier_0` (or the
   relevant tier depending on the source's shape). Default:
   `wiki/{tier_0}/{slug}.md`. Aesthetic-warburg continues to use
   `wiki/aesthetic/` implicitly because tier_0 = work; no change visible
   to the user.

### Anchor preservation by lens

| Lens                    | Authority fields preserved verbatim                            | Additional verbatim rules                                      |
|-------------------------|------------------------------------------------------------------|-----------------------------------------------------------------|
| `aesthetic-warburg`     | AAT ID, Iconclass code, Wikidata QID                            | Warburg panel names (German titles); Pathosformel phrases       |
| `engineering-alexander` | RFC number, CVE ID, CWE ID, postmortem URL hash, service names | Version numbers; error codes; config keys (kebab/snake case kept) |
| `general-zettelkasten`  | (none declared)                                                 | Quoted source fragments; named methodologies; author names      |

"Verbatim" means the source-language token appears unchanged in the
distilled body, with the vault-language gloss in parentheses on first
mention. On second mention, use whichever form is more natural for a
native reader of the vault language — usually the gloss, unless the
token carries precision the gloss loses.

### Terminology ledger is lens-scoped

Each lens owns its own terminology file:

- `wiki/_glossary.md` — aesthetic-warburg (legacy v2.0 location,
  preserved for back-compat)
- `wiki/_terminology/<lens-id>.md` — all other lenses (keeps per-lens
  vocabularies from cross-contaminating when a vault uses multiple
  lenses across sessions)

`/distill` appends new term mappings to the lens-appropriate file. Under
aesthetic-warburg it keeps writing to `_glossary.md`; under engineering
or zettelkasten it writes to `_terminology/<lens-id>.md` and ensures
the file exists (creating with a minimal header on first run).

### Schema-reference output header

The distilled MD's frontmatter gains a `lens:` field:

```yaml
lens: engineering-alexander
```

This lets `/lint --lens=<id>` confirm the distilled entry was produced
under a compatible lens. Mismatched lens = yellow warning (not a block
— a distillation produced under a different lens may still be useful),
with suggestion to re-run under the current lens.

### Flag summary (lens-aware)

- `--lens <id>` — override active lens
- `--preserve-all` — keep every proper noun verbatim (overrides
  lens-level rules upward; never downward)
- `--output-dir <path>` — escape hatch for the default `wiki/{tier_0}/`
  resolution; surfaces as a warning because it breaks lens discovery

If the source is already in the target language, exit no-op as before.

---

## What this is NOT

- Not word-for-word translation
- Not summarization (summary keeps the original framing; distillation reconstructs it)
- Not a replacement for reading the original (the `raw/` source is preserved)

## What it IS

Rewriting a foreign-language source as if the author had been thinking in the target language from the start. The result feels native in the target language's conceptual vocabulary while preserving key foreign-language terms as bilingual anchors where precise meaning would otherwise be lost.

## Invocation

```
/distill raw/articles/<file>           # explicit target
/distill <url>                         # fetch to raw/ first, then distill
```

Usually called automatically by `/ingest` when the input language ≠ vault authoring language. Direct invocation is for on-demand re-processing.

## Execution

### Step 1 — Detect source and target language

- Source: frontmatter of the raw file, or language detection on body
- Target: user's vault authoring language (from first-time setup; typically `zh` for this repo's primary user, but any language is valid)

If source = target, exit with no-op — distill is translation + re-structuring, not a same-language rewrite.

### Step 2 — Build a term glossary for this source

Before writing the distilled output, scan the source for:

- Named technical terms (camelCase, PascalCase, or phrases introduced with scare quotes)
- Proper nouns (authors, systems, methodologies)
- Discipline-specific vocabulary

For each, record the (source_term → target_term) mapping. Consult `wiki/_glossary.md` for any existing mappings; reuse rather than re-create. New mappings get appended to `_glossary.md` after the distill run.

### Step 3 — Reconstruct

Write a new markdown file in `wiki/{domain}/{slug}.md` (domain inferred from content; slug kebab-cased from title).

Conventions for the reconstructed body:

- **First occurrence of a term pair**: `注意力机制 (Attention Mechanism)`. Parenthetical preserved.
- **Subsequent occurrences**: `注意力机制` alone.
- **Sentences restructured** to match target language's natural rhythm — do not keep source-language syntax awkwardly intact.
- **Examples or analogies** may be re-chosen to fit target culture when the source's examples are opaque out-of-culture. Never invent examples that distort technical content.

Structure of the distilled MD:

```markdown
---
id: {slug}
type: {concept | methodology-flavored concept | summary — per content}
title: {target-language title}
aliases: [{source-language title}]
language: {target}
original_terms:
  - term: "{source-term-1}"
    target: "{target-term-1}"
    lang: {source-lang}
source_material:
  - url: "<original URL>"
    path: "raw/articles/<filename>"
    lang: {source-lang}
    ingestion_date: "{YYYY-MM-DD}"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
freshness_class: stable
confidence: 0.9
last_validated: "{YYYY-MM-DD}"
schema_version: "2.1.0"
relations:
  - {type: derived_from, target: [[raw/articles/<filename>]]}
---

# {target-language title}

## 认知钩子 (Cognitive anchor)
<One sentence, 15–30 words: the compressed thesis. This is what /ask --depth hook returns.>

## 正文
<Reconstructed prose in target language.>

## 关键术语锚 (Key term anchors)
| 本文术语 | 原文术语 | Note |
|---|---|---|
| 注意力机制 | Attention Mechanism | — |
| ... | ... | — |

## 溯源 (Provenance)
- 来源:[原始材料](raw/articles/{filename})
- URL:{url}
- 摄入日期:{YYYY-MM-DD}
```

### Step 4 — Update glossary

Append new term mappings to `wiki/_glossary.md`. Deduplicate against existing entries. Sort alphabetically by target term.

### Step 5 — Report

Print to user:
- Path to distilled MD
- Number of terms added to glossary
- Confidence level (based on source clarity, term recognition rate)

## Ground rules

- Preserve technical accuracy above idiomatic smoothness when they conflict
- When a target-language term does not yet exist for a concept, keep the source term and record the gap in `_glossary.md` with a `status: no-target-yet` flag
- Do NOT distill prompts or code blocks — pass them through verbatim
- Do NOT distill proper nouns (names of people, companies, products) — keep in original
- For aesthetic sources (prose about a visual work), distill the prose but DO NOT transform the work into an Aesthetic MD — that requires `/taste` on the visual input, not the prose about it

## Schema reference

- `schema.md §8` — bilingual architecture
- `schema.md §4` — frontmatter contract including `original_terms`
- `schema.md §8` — prompt language exception (distilled MD's prose is target-language; embedded prompts stay English)
