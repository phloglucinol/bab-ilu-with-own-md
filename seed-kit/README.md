# Bab-ilu Seed Kit (v2.1 · multi-lens)

> Optional starter content for `/genesis --lens=<id> --seeded`. Each lens
> has its own curated public-domain seed set so that first-run demos are
> domain-appropriate.

## Lens-Specific Seed Kits

| Lens | Directory | Status | Populated by |
|---|---|---|---|
| 🎨 Aesthetic · Warburg | [`aesthetic-warburg/`](aesthetic-warburg/) | **complete** (v2.0 Sprint 1) | already shipped |
| 🏗️ Engineering · Alexander | [`engineering-alexander/`](engineering-alexander/) | scaffold only | Sprint 2 · C2 |
| 📚 General · Zettelkasten | [`general-zettelkasten/`](general-zettelkasten/) | scaffold only | Sprint 2 · C3 |

Future lenses (science-kuhn / finance-minsky / law-irac / medicine-soap)
will land their seed kits in v2.2 Sprint 5-6 as additional top-level
folders here.

## Theoretical Basis per Lens

- **Aesthetic · Warburg** — Aby Warburg *Mnemosyne Atlas*, Erwin Panofsky's
  three iconological layers, Ernst Gombrich *The Story of Art*.
- **Engineering · Alexander** — Christopher Alexander *A Pattern Language*
  and *The Timeless Way of Building*; GoF *Design Patterns* as applied
  layer; authoritative post-mortems (AWS, Cloudflare, Google SRE Book).
- **General · Zettelkasten** — Niklas Luhmann's Zettelkasten method,
  Benjamin Bloom cognitive hierarchy, Tiago Forte Progressive
  Summarization.

Each lens's README documents its subfolder conventions and seed counts.

## Aesthetic · Warburg Contents (v2.0, shipped)

- **8 works** — specific public-domain artifacts (pre-1926 paintings; brief verifiably-usable film references)
- **15 motifs** — named visual operations extracted from the 8 works
- **2 pathosformel** — demonstration emergent clusters (quiet-interior-light, sublime-solitude-landscape)
- **8 people** — creators of the 8 works
- **3 sources** — Warburg Mnemosyne Atlas, Panofsky Studies in Iconology, Getty AAT

## Usage

`/genesis --lens=<id> --seeded` copies **only the matching lens subfolder**
into the user's `wiki/`. Example:

```
/genesis --lens=aesthetic-warburg --seeded
  → copies seed-kit/aesthetic-warburg/**  →  wiki/
/genesis --lens=engineering-alexander --seeded
  → copies seed-kit/engineering-alexander/**  →  wiki/
```

Every seed file carries `seed: true` frontmatter and the `#seed` tag so
users can filter or bulk-delete. `/reset --seeds` removes every
`seed: true` entry in one operation, regardless of which lens seeded them.

`--seeded` without `--lens` is rejected; the lens must be chosen first
so the right scaffold and seeds land in `wiki/`.

## License

All seed content is derived from public-domain sources. For the
aesthetic lens specifically:

- Wikimedia Commons public-domain files (pre-1926 paintings)
- Architectural photographs released under Creative Commons
- No film frames included (copyright risk); film references are text-only

Engineering and general lenses will follow the same public-domain-only
rule when their seeds land in Sprint 2.

## Updating

To contribute a new seed entry, open a PR with:

1. New work/motif/person/incident/force/pattern/note/concept/… MD file
   in the appropriate **lens**'s subfolder
2. `seed: true` in frontmatter
3. Full AAT/Iconclass/ULAN/CVE/RFC/DOI/… anchor resolution where
   possible (the lens's `lens.yaml` declares which anchors count)
4. Source citation (Wikimedia Commons URL, CVE record, DOI, etc.)
5. Justification in the PR description: why this entry earns seed status

See `docs/seed-contribute.md` (produced Sprint 5).
