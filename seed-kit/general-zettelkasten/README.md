# General · Zettelkasten Lens · Seed Kit

> Placeholder directory. Sprint 2 unit **C3** will populate this with
> ~25 cross-domain Zettel seeds demonstrating Luhmann-style note linking
> annotated with Bloom cognitive levels.

## Theoretical Basis

- Niklas Luhmann, Zettelkasten methodology
- Benjamin Bloom, cognitive hierarchy
  (remember / understand / apply / analyze / evaluate / create)
- Tiago Forte, Progressive Summarization (as deliverable format)

## Target Structure (after C3 lands)

| Subfolder | Purpose | Target count |
|---|---|---|
| `notes/` | Atomic Zettel notes spanning several domains | ~10 |
| `concepts/` | Named concepts extracted from notes | ~8 |
| `concept-clusters/` | Tier-1 emergent clusters (Luhmann threads) | ~4 |
| `people/` | Creators / thinkers referenced | ~2 |
| `sources/` | Core references (Luhmann archive, Bloom taxonomy, Forte PS) | ~2 |

## Scope (per PRD §8.1)

- Structure: Note × Concept → Concept-Cluster (tier 1, annotated by Bloom level) → Meta-Understanding (tier 2)
- Anchors: Wikipedia / Wikidata / DOI / ISBN
- Analysis contract: Luhmann's three questions (What / Why / So-what) + Bloom level classification

## Role

This lens is the **fallback** when no domain-specific lens fits. It
keeps the vault productive even when the user is doing cross-domain
synthesis rather than art / engineering / science work.

## Current Status

**Empty scaffold.** The five subfolders contain only `.gitkeep`. Unit C3
(Sprint 2 Track C) is responsible for filling each with public-domain
seeds that carry `seed: true` frontmatter and the `#seed` tag. Until
then, `/genesis --lens=general-zettelkasten --seeded` copies only this
README and the empty scaffold.
