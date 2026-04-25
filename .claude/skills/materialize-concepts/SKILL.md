---
name: materialize-concepts
description: Use when the active lens is general-zettelkasten and concept wikilinks in wiki/note/*.md should be turned into real wiki/concept/*.md pages before running /gap, especially when Obsidian shows dangling concept links or concept-cluster discovery is weak.
---

# /materialize-concepts — Create Zettelkasten concept pages

`/materialize-concepts` (Codex: `$materialize-concepts`) wraps
`tools.materialize_concepts`. It materializes repeated concept references
from `wiki/note/*.md` into minimal `wiki/concept/*.md` pages so Obsidian
and `$gap` both see real tier-1 concept nodes.

## Synopsis

```text
/materialize-concepts
/materialize-concepts --dry-run
/materialize-concepts --json
/materialize-concepts --vault=<path>
/materialize-concepts --lens=general-zettelkasten
```

Codex users invoke the same workflow as `$materialize-concepts`.

## When To Use

Use this under `general-zettelkasten` when:

- notes already contain `concepts:` frontmatter or a `## Concepts (tier_1_atoms)` section
- Obsidian shows many concept wikilinks as dangling links
- `$gap` produces weak or empty concept-cluster candidates because concept pages do not exist yet
- the user asks to materialize, instantiate, create, or land concept pages

Do not use this for `aesthetic-warburg` motifs or `engineering-alexander`
patterns. The tool fails loud outside `general-zettelkasten`.

## What It Writes

For each concept referenced by at least two different notes, it creates:

```text
wiki/concept/<slug>.md
```

Each page contains minimal frontmatter plus two LLM-owned body sections:

- `materialize-concepts-relations` — `relations:` edges with
  `exemplifiedBy` targets that `tools.gap_runner.py` can read
- `materialize-concepts-stub` — a definition stub and `Referenced By`
  wikilinks for Obsidian reading

Singleton concepts are only reported. They are not written to
`wiki/concept/`, preserving the Zettelkasten two-independent-notes bar.

## How To Run

Prefer a dry run first:

```bash
python3 -m tools.materialize_concepts --vault . --dry-run
```

If the counts look right, run:

```bash
python3 -m tools.materialize_concepts --vault .
```

For automation:

```bash
python3 -m tools.materialize_concepts --vault . --json
```

After successful materialization, suggest:

```text
$gap --lens general-zettelkasten
```

## Boundaries

- Never modifies `raw/`.
- Never modifies existing `wiki/note/*.md`.
- Never overwrites existing `wiki/concept/*.md`.
- Never writes singleton concept pages.
- Never updates `wiki/index.md` or `.agent/graph/*`.
- Writes concept pages atomically.
