# Engineering · Alexander Lens · Seed Kit

> Placeholder directory. Sprint 2 unit **C2** will populate this with
> ~25 public-domain engineering seeds covering post-mortems, RFCs, and
> design patterns.

## Theoretical Basis

- Christopher Alexander, *A Pattern Language* (1977) and
  *The Timeless Way of Building* (1979)
- Gang of Four, *Design Patterns* (1994) — used as applied-example layer
- Published post-mortems from AWS / Cloudflare / Google SRE Book

## Target Structure (after C2 lands)

| Subfolder | Purpose | Target count |
|---|---|---|
| `incidents/` | Tier-0. Specific public outages, CVEs, RFC discussions | ~8 |
| `forces/` | Tier-1 atom. Named engineering forces ("strong consistency vs. availability", "p99 vs. throughput") | ~8 |
| `patterns/` | Tier-1 cluster. Alexander patterns emergent from incidents × forces | ~5 |
| `pattern-languages/` | Tier-2 emergence. Pattern-of-patterns (gated, promoted post-analysis) | 0 at seed time |
| `systems/` | Creator/system actors (referenced systems) | ~2 |
| `sources/` | Authoritative references (Pattern Language, SRE Book, CVE DB) | ~2 |
| `questions/` | Open questions arising from incidents (cross-lens entity type) | as needed |

## Scope (per PRD §8.1)

- Structure: Incident × Force → Pattern (tier 1) → Pattern-Language (tier 2)
- Anchors: CVE / RFC / IETF / W3C / well-known post-mortems
- Analysis contract: Alexander Problem-Context-Forces-Solution-Consequences

## Current Status

**Empty scaffold.** The seven subfolders contain only `.gitkeep`. Unit C2
(Sprint 2 Track C) is responsible for filling each with public-domain
seeds that carry `seed: true` frontmatter and the `#seed` tag. Until
then, `/genesis --lens=engineering-alexander --seeded` copies only this
README and the empty scaffold.
