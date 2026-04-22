# Aesthetic · Warburg Lens · Seed Kit

> Curated public-domain aesthetic seed content covering painting, cinema,
> architecture, and photography. Shipped with v2.0 Sprint 1.

## Theoretical Basis

- Aby Warburg, *Mnemosyne Atlas* (1924–29) — the bilderatlas method
- Erwin Panofsky, *Studies in Iconology* (1939) — three-layer image reading
  (pre-iconographic / iconographic / iconological)
- Ernst Gombrich, *The Story of Art* (1950) — canonical narrative

## Contents

| Subfolder | Count | Purpose |
|---|---|---|
| `works/` | 8 | Specific public-domain artifacts (pre-1926 paintings; brief verifiably-usable film references) |
| `motifs/` | 15 | Named visual operations extracted from the 8 works |
| `pathosformel/` | 2 | Demonstration emergent clusters (quiet-interior-light, sublime-solitude-landscape) |
| `people/` | 8 | Creators of the 8 works |
| `sources/` | 3 | Warburg Mnemosyne Atlas, Panofsky Studies in Iconology, Getty AAT |

## Scope (per PRD §8.1)

- Structure: Work × Motif → Pathosformel (tier 1) → Topoi (tier 2)
- Anchors: AAT / Iconclass / ULAN
- Analysis contract: Panofsky three layers
- Deliverable: generative-model prompt (Midjourney / Sora four-segment skeleton)

## License

All seed content is derived from public-domain sources:

- Wikimedia Commons public-domain files (pre-1926 paintings)
- Architectural photographs released under Creative Commons
- No film frames included (copyright risk); film references are text-only

## Wikilinks

Every wikilink inside this seed kit resolves within the folder except for
a small number of intentionally dangling refs (questions prefixed `q-`,
external references). The structural test `test_seed_wikilinks_resolve_within_seed_kit_aesthetic`
allows ≤ 5 dangling links.

## Current Status

**Complete.** Further seeds would be added in v2.2 Sprint 5-6 alongside the
tier-1 lens roadmap (science-kuhn / finance-minsky / law-irac / medicine-soap).
