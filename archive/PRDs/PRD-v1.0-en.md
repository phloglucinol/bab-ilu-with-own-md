# Bab-ilu — An Aesthetic Knowledge System for the AI Generation Era

> PRD v1.3 | 2026-04-16
> **Form**: Hard fork of [skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki) v0.1.0, independently evolving.
> OmegaWiki provides the academic research pipeline base. Bab-ilu's differentiation is in **high-quality creation prompts with declared academic lineage** — when users do UI design, generate images, or generate video, Bab-ilu produces prompts that are sourced, traceable, and scholarly, rather than generic style-tag slop.
>
> Three hard constraints: **Karpathy three-layer architecture** (`raw/` · `wiki/` · `schema.md`), **everything as Markdown**, **heavy-dose academic lineage at zero user cost**.
>
> This is the English mirror of the authoritative Chinese `PRD-zh.md`.

---

## 0. Core Positioning

Bab-ilu is an **aesthetic knowledge system for the AI generation era**.

When users run `/taste` on a reference image in the terminal, or open an Aesthetic card in Obsidian, they see:
- Structured aesthetic analysis (Panofsky three layers)
- Cross-era visual motif membership (Warburg Nachleben / image afterlife)
- **High-quality prompts** directly usable in Midjourney / Flux / Nano Banana / Runway / Sora / Kling
- Each prompt declares its academic provenance (Getty AAT terms, Warburg panels, signature authors)

**Aesthetic archaeology (TASTE) is the engine, academic anchors (Warburg / Panofsky / Getty AAT) are the lineage source, prompts are the terminal deliverable.**

Analysis and archaeology are means. **Better generation output is the end.** Every mechanism in this system must be justified against that end.

---

## 1. Product Overview and Vision

### 1.1 What Bab-ilu is

Bab-ilu is an Obsidian-based, agent-human co-evolution aesthetic knowledge framework. The user clones the repo, runs `/genesis`, and all installed AI agents (Claude Code, Hermes, Codex, OpenClaw, ...) auto-wire into the shared structured knowledge base.

The framework operates on two levels:
- **Runtime**: When the user does UI design / image generation / video generation, agents produce prompts with academic lineage and write them into Aesthetic cards. Users may also use `/ask` to query across the vault.
- **Evolution**: Through repeated use, generative regression testing, and user curation, the knowledge base and agent capability compound over time. Validated prompts are promoted to reusable recipes.

Users drop materials into `raw/` (images, videos, links, notes). Agents handle organization, cross-linking, prompt generation, and academic provenance tracking. The true platform is the filesystem (markdown + YAML frontmatter). Obsidian is the recommended viewer.

### 1.2 Why build this

Andrej Karpathy's LLM Wiki pattern established one thing: LLMs excel at the bookkeeping — summarizing, cross-referencing, maintaining a knowledge base. [OmegaWiki](https://github.com/skyllwt/OmegaWiki) took the academic research path to completion: 8 entities, 23 skills, 2263 tests, a full academic closed loop.

But in an era when AI-generated content is a mainstream tool for design and imagery, an entire territory remains unaddressed:

1. **Prompts are still generic style-tag soup** — "cinematic, moody, teal and orange." Generic tags produce vague, homogeneous output on Midjourney v6+, Flux, Sora, and Kling; there is no authorship.
2. **Aesthetic knowledge has no structured base** — OmegaWiki's schema is built for textual knowledge. Images in the wiki are only cited as sources; they are not structured knowledge units that can be understood and reused.
3. **Cognitive reconstruction for native-language users is missing** — OmegaWiki translates agent instructions (L1 localization via `setup.sh --lang=zh`), but the knowledge content itself is written in whatever language the LLM picks. For users who build mental models in their native language, L1 localization alone is not enough.

Bab-ilu does not rewrite OmegaWiki; it **adds two layers on top**:
- **Aesthetic archaeology and creation prompts (TASTE)** — core differentiator
- **Cognitive reconstruction localization (L2)** — auxiliary differentiator

### 1.3 Relationship to the base (OmegaWiki) and adjacent systems

> **Positioning**: OmegaWiki is not a competitor. It is Bab-ilu's base.

| Layer | Capability | OmegaWiki v0.1.0 base | Bab-ilu additions |
|-------|------------|-----------------------|-------------------|
| Schema | Entity types | 8 | +2 (aesthetic / prompt) + question = **11** |
| Schema | Relation types | 9 | +3 (applies / exemplifies / frames) = **12** |
| Skill | Research-lifecycle skills | 23 | Inherit 21, rename 2, move to appendix |
| Skill | Core commands | — | **7 Bab-ilu core commands** (+2 optional) |
| Agent | Multi-agent support | Claude Code primary | + Hermes primary; Codex/OpenClaw/Cursor/Gemini best-effort |
| Language | Localization level | L1 | L2 cognitive reconstruction + bilingual anchors |
| Visual | Visual / aesthetic knowledge | None | Aesthetic entity + 3–5 taste-* subagents + Warburg panel library |
| Creation | Generation prompts | None | **Three-modality auto-generation** (UI / image / video) |
| Academic | Academic anchors | Scholarly citation graph | + Warburg Nachleben + Panofsky three-layer + Getty AAT / Wikidata |

**Academic benchmarks** (not adjacent systems — the scholarly ecosystem Bab-ilu enters):

| Benchmark | Significance |
|-----------|-------------|
| [Warburg Institute Mnemosyne Atlas digital archive](https://warburg.sas.ac.uk/archive/archive-collections/mnemosyne-atlas) | Aby Warburg's 1924–29 image archaeology — Bab-ilu's Warburg panels directly inherit the tradition |
| [Getty AAT](http://vocab.getty.edu/aat/) | 55,000 controlled art & architecture concepts, 40 years of stewardship — Bab-ilu's Aesthetic frontmatter cites AAT IDs |
| [Wikidata LOD](https://www.wikidata.org/) | Linked Open Data backbone — Bab-ilu participates via `wikidata` QIDs |
| [Panofsky three-layer iconology](https://en.wikipedia.org/wiki/Iconology) | 1939 methodology for visual interpretation — Bab-ilu's prompt skeleton maps directly to the three layers |

**Adjacent knowledge frameworks** (reference points, not base):

| Project | Form | Relation to Bab-ilu |
|---------|------|---------------------|
| [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | Minimal multi-agent skill architecture | Borrowed setup pattern |
| [MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki) | L1/L2 cache architecture | Inspirational, no inheritance |
| [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Original pattern (raw / wiki / schema three layers) | **Philosophical base**, Bab-ilu core aligns with it |

### 1.4 Target users

- **Primary**: Designers, directors, visual practitioners doing UI design, AI image generation, AI video generation — they need high-quality prompts
- **Secondary**: Developers and researchers using AI coding agents daily and managing a personal knowledge base
- **Secondary**: Non-English speakers consuming English content (served by L2 localization)

### 1.5 Distribution

Open-source repository. Users clone, run setup, start using. No cloud dependency. Obsidian is a viewer; the filesystem is the database; agents are the workers.

### 1.6 Platform Philosophy — Karpathy Three Layers

Bab-ilu's true platform is the filesystem, strictly aligned with Karpathy's LLM Wiki three-layer architecture:

| Layer | Directory | Owner | Mutability |
|-------|-----------|-------|------------|
| Raw sources | `raw/` | User | Immutable; LLM never modifies |
| Knowledge | `wiki/` | LLM | LLM writes and maintains; user may curate |
| Conventions | `schema.md` (project root) | LLM reads; human project lead edits | Changes only with explicit decision, versioned |

**Any proposed mechanism must land in one of these three layers, else cut.** This is v1.3's major shift from v1.2 — v1.2's L0/L1/L2 token tiering did not belong to any of the three layers and has been removed.

### 1.7 Why Bab-ilu is resilient to LLM evolution

1. **Multi-agent consistency.** Model-native memory is per-agent. Bab-ilu is the shared knowledge layer across agents.
2. **User ownership and portability.** Knowledge follows Bab-ilu, not the model.
3. **Auditability and provenance.** Every generated prompt carries academic lineage (Warburg / Panofsky / AAT / Wikidata) — traceable, falsifiable.
4. **Prompt quality decoupled from generator generation.** Academic anchors are structural constants of visual culture, stable across model generations. Bab-ilu bets on this constant.

### 1.8 Upstream (fork strategy)

Bab-ilu is a **hard fork of OmegaWiki v0.1.0**, evolving independently. No periodic upstream merge.

**Why a hard fork**: differentiation requires schema changes, rewritten command set, new directories. Evolution paths diverge — OmegaWiki deepens academic pipelines; Bab-ilu deepens aesthetic creation.

**Practical implications**:
- Bab-ilu freely rewrites any inherited file
- Inherited Python infrastructure (`tools/research_wiki.py` 20 CLIs, `mcp-servers/`, `tests/` 2263 tests) is maintained as **internal implementation dependency**, not product narrative
- Future OmegaWiki changes evaluated case-by-case for porting (not merging)
- `references/OmegaWiki/` preserved as historical snapshot
- Record baseline commit SHA in `docs/UPSTREAM.md` before v1.0 release

### 1.9 Academic Lineage Statement

Bab-ilu explicitly inherits three aesthetic-scholarly lineages as the genetic basis of the TASTE engine:

**Lineage 1: Aby Warburg — Mnemosyne Atlas (1924–1929) and the Nachleben principle**
> Visual motifs do not belong to a single period or author; they migrate, mutate, and resurface across centuries.

Warburg's unfinished image archive of 63 black panels juxtaposed images sharing visual gestures, compositional tensions, or emotional formulas (*Pathosformel*). Bab-ilu's Warburg panels (`wiki/_panels/`) are the digital continuation in the LLM era — and the most powerful "generate within a lineage" tool for downstream creators.

**Lineage 2: Erwin Panofsky — Studies in Iconology (1939), three-layer iconology**
> pre-iconographic → iconographic → iconological

Panofsky's three strata of visual interpretation are the direct source of Bab-ilu's prompt skeleton. A high-quality image/video prompt must address all three layers — this is the property that makes MJ v6+, Flux, Sora, Kling respond with specificity rather than blending style tags.

**Lineage 3: Getty AAT + Wikidata LOD — controlled vocabulary and linked open data**
> 55,000 art and architecture concepts, 40 years of maintenance.

AAT terms are heavily represented in generation-model training data (museum metadata → Wikipedia → LAION image captions). **AAT-anchored prompts produce measurably more specific outputs than prompts citing folk style labels.** Bab-ilu's Aesthetic entities cite AAT IDs and gain LOD interoperability as byproduct.

**Heavy-dose commitment**: Every Aesthetic MD terminates in an auto-generated "Academic Lineage" section explicitly citing the Warburg panel, Panofsky layer, AAT ID, and Wikidata QID — legible to scholars, ignorable by general users, and a commitment to intellectual honesty.

---

## 2. Schema Design

Full schema definition in `schema.md` — read by LLM at every session. This section is a summary.

### 2.1 Entity types (11)

| Type | Inherited from OmegaWiki | Description |
|------|--------------------------|-------------|
| `source` | yes | Any ingested material with provenance |
| `concept` | yes | Named knowledge unit; `role` metadata disambiguates methodology / philosophy / foundation / etc. |
| `topic` | yes | Subject-area cluster |
| `person` | yes | Author, researcher, artist, director, designer |
| `idea` | yes | Speculative hypothesis with `maturity`: seed / developing / mature / failed |
| `experiment` | yes | Reproducible trial with process and result |
| `claim` | yes | Falsifiable proposition |
| `summary` | yes | Compressed overview |
| `question` | yes | Open question, knowledge gap |
| `aesthetic` | **new** | Visual / aesthetic unit. TASTE core. Auto-generates three-modality prompts |
| `prompt` | **new** | Validated, reusable prompt recipe promoted from an Aesthetic's auto-generated prompts. Lives in `wiki/_prompts/` |

**Merge note**: v1.2's Methodology / Prompt / Philosophy / Foundations are consolidated. Methodology / Philosophy / Foundations become `concept` with a `role` field. Prompt becomes independent due to its first-class creation-output role.

### 2.2 Relation types (12)

Inherited 9: `extends` · `contradicts` · `supports` · `inspired_by` · `tested_by` · `invalidates` · `supersedes` · `addresses_gap` · `derived_from`

New 3:
- `applies` — abstract applied to concrete
- `exemplifies` — concrete is instance of abstract (Aesthetic → Warburg panel)
- `frames` — philosophical / aesthetic lens

**Removed from v1.2**: `composes` / `categorized_by` / `authored_by` — overlap with other relations or frontmatter fields.

### 2.3 Frontmatter contract

See `schema.md §4` for canonical spec. Aesthetic extensions summary:

```yaml
type: aesthetic
aat_id: "300015650"
wikidata: "Q4692"
warburg_panel: [[[panel-id]]]
panofsky_layer: pre_iconographic | iconographic | iconological
domain: cinema | photo | ui | graphic | game | architecture
prompts:
  ui:    {generated, last_tested, test_score}
  image: {generated, last_tested, test_score, compatible_models}
  video: {generated, last_tested, test_score, compatible_models}
```

### 2.4 Relation storage

**Authoritative**: frontmatter YAML. **Generated**: `_index/edges.jsonl` (lazily rebuilt), inline wikilinks in `## Relations` sections.

### 2.5 Schema evolution

**Additive-only**. Adding types or optional fields never breaks existing entries. `schema_version: 1.3.0`.

---

## 3. Core Command Set

> **Fork lens**: OmegaWiki v0.1.0 provides 23 skills. v1.3 narrows Bab-ilu core to **7** (+2 optional); OmegaWiki's 21 academic skills move to appendix §3.A.

### 3.1 Core commands (7)

| # | Command | Description |
|---|---------|-------------|
| 1 | `/genesis` | Initialize three-layer vault, detect agents, create symlinks, print next-step hint |
| 2 | `/ingest` | Ingest material from `raw/`; auto-trigger `/compile` and `/distill`. `--panel` triggers Warburg panel synthesis |
| 3 | `/ask` | Cross-vault query with synthesized answer + entry links. `--depth hook | summary | full` |
| 4 | `/taste` | Aesthetic archaeology: dispatch 3–5 taste-* subagents, produce Aesthetic MD (with prompts + lineage). See §5.2 |
| 5 | `/distill` | English → native-language card via cognitive reconstruction with bilingual anchors. See §5.5 |
| 6 | `/check` | Health audit: schema, AAT IDs, lineage sections, prompt tests, broken links. See §9 |
| 7 | `/prompt` | From Aesthetic or Warburg panel, regenerate or promote prompts per modality. Promoted prompts become `wiki/_prompts/` entities |

### 3.2 Optional commands (2)

| # | Command | Description |
|---|---------|-------------|
| 8 | `/panel` | Explicitly curate Warburg panels |
| 9 | `/glossary` | Manage bilingual term mapping table (`wiki/_glossary.md`) |

### 3.A Appendix: OmegaWiki-inherited academic commands (21)

Serving the academic research loop. Bab-ilu does not re-describe; see OmegaWiki's canonical docs.

| Category | Commands |
|----------|----------|
| Core pipeline | `/setup` `/compile` `/cross-link` `/export` `/reset` `/status` `/edit` `/refine` |
| Research discovery | `/research` `/survey` `/novelty` `/ideate` `/daily-feed` (renamed from `/daily-arxiv`) |
| Experiment lifecycle | `/exp-design` `/exp-run` `/exp-eval` `/exp-status` |
| Knowledge output | `/paper-plan` `/paper-draft` `/paper-compile` `/rebuttal` `/review` `/prefill` |

**Removed in v1.3**: `/lineage` (absorbed into `taste-lineage` subagent), `/lens` (replaced by taste-* subagents), `/mood-board` (covered by panels).

---

## 4. Architecture

### 4.1 Karpathy three-layer architecture

```
Bab-ilu/                         # Repository root
├── raw/                         # [Layer 1] Immutable sources (user-owned)
│   ├── articles/
│   ├── images/                  # user-dropped reference images, stills
│   ├── videos/
│   └── papers/
├── wiki/                        # [Layer 2] Knowledge (LLM-owned)
│   ├── aesthetics/              # Aesthetic entities (with three-modality prompts + academic lineage)
│   │   ├── cinema/
│   │   ├── photo/
│   │   ├── ui/
│   │   └── ...
│   ├── _panels/                 # Warburg panels (cross-era visual motifs)
│   ├── _prompts/                # Prompt entities promoted to standalone reuse
│   ├── _evals/                  # Evaluation samples (~120)
│   ├── _glossary.md             # Bilingual term governance
│   ├── _index/                  # Auto-generated indices
│   │   ├── entry-index.yaml
│   │   └── edges.jsonl          # Lazily rebuilt
│   └── _log/
│       └── usage.jsonl          # Append-only log
└── schema.md                    # [Layer 3] Conventions + academic anchor prompts
```

**Internal implementation dependencies** (not layers, not main narrative):

```
.claude/
├── skills/                      # 7 core + optional commands
└── agents/                      # 3–5 taste-* subagents
.agents/skills/                  # Symlinks for OpenClaw/Hermes
tools/                           # OmegaWiki-inherited Python CLIs
mcp-servers/                     # OmegaWiki-inherited
tests/                           # OmegaWiki-inherited (2263 tests)
i18n/                            # L1 agent-instruction translation
docs/UPSTREAM.md                 # Fork baseline commit SHA
requirements.txt                 # Python deps
setup.sh                         # One-command setup
CLAUDE.md                        # Claude Code project schema
```

### 4.2 Vault organization

Files organized by **domain**, not by entity type. Type lives in frontmatter `type:`. Domains grow organically.

### 4.3 Bilingual content architecture

**Scheme C**: monolingual files + bilingual term anchors + `/glossary` governance.

- Files in user's native language
- English sources pass through `/distill` before entering `wiki/`
- `original_terms` stores bilingual mappings (follows Getty AAT multilingual convention)
- Search covers both languages

**Positioning correction**: v1.2 wrongly claimed OmegaWiki is monolingual. Bab-ilu's actual delta is L2 cognitive reconstruction, not filling an L1 void.

**Prompt language exception**: auto-generated prompt bodies remain in English (generation models are English-trained, AAT is English). Chinese prose wraps English prompts.

### 4.4 Multi-agent support

**Primary**: Claude Code, Hermes. **Best-effort**: Codex, OpenClaw, Cursor, Gemini. One skill source, symlinked via `setup.sh`.

Claude Code supports subagents natively; others degrade to sequential prompt chain.

### 4.5 Internal implementation dependencies

OmegaWiki-inherited Python toolchain maintained as internal dependency, **not a selling point**. Cross-language agents invoke Python tools via CLI boundaries.

---

## 5. Differentiation — TASTE

Fully rewritten from v1.2. Structure: academic lineage → operating mechanism → user output form → L2 localization → evaluation.

### 5.1 Academic lineage and genetic basis

TASTE is **three aesthetic-scholarly lineages extended into the LLM era**. Prompt-level definitions in `schema.md §5`.

**Lineage 1: Warburg Nachleben** — drives `taste-lineage`. Identifies cross-era visual genealogies; places subject into Warburg panel. Forbidden: pure style labeling, chronological placement without motif, influence-graph speculation.

**Lineage 2: Panofsky three-layer iconology** — drives `taste-icon` and `taste-synthesis`. Strict separation of pre-iconographic / iconographic / iconological is the structural source of prompt quality.

**Lineage 3: Getty AAT + Wikidata** — drives external anchors and vocabulary. AAT terms in training data means AAT-anchored prompts produce order-of-magnitude more specific output.

### 5.2 Operating mechanism

`/taste` orchestrator dispatches 3–5 taste-* subagents in `.claude/agents/`:

| Subagent | Responsibility |
|----------|---------------|
| `taste-icon` | Panofsky pre-iconographic + iconographic layers |
| `taste-lineage` | Warburg Nachleben + cross-era motif genealogy |
| `taste-synthesis` | Panofsky iconological layer + three-modality prompt assembly + AAT vocabulary check |
| `taste-eye` (optional) | Domain detection when input is ambiguous |

**v1.2 → v1.3**: 15 subagents down to 3–5. The 6-domain × 2-role matrix was engineering structure, not problem essence. Domain info moves to frontmatter hint.

#### Orchestration topology

```
[user: /taste + visual material]
       ↓
  taste-eye (optional) → {domain hint}
       ↓
  taste-icon → pre-iconographic + iconographic layers
       ↓
  taste-lineage reads icon output → motif membership → Warburg panel wikilink
       ↓
  taste-synthesis merges → iconological layer + three-modality prompt + AAT check
       ↓
  writes wiki/aesthetics/{domain}/<slug>.md (with prompts + academic-lineage sections)
  updates or creates wiki/_panels/<panel>.md as needed
```

### 5.3 User output form

Aesthetic MD terminates in two auto-generated sections (**Prompts first, Academic Lineage second** — users reach creation output before citation).

#### Aesthetic MD example

Input: user drops 10 Wong Kar-wai stills, runs `/ingest --panel`.

Output: `wiki/aesthetics/cinema/wong-kar-wai-chromatic-nostalgia.md`:

```markdown
---
type: aesthetic
title: Wong Kar-wai Chromatic Nostalgia
aat_id: "300015541"
wikidata: "Q1398191"
warburg_panel: [[[saturation-as-memory]]]
panofsky_layer: iconological
domain: cinema
prompts:
  ui:    {generated: 2026-04-16, last_tested: null, test_score: null}
  image: {generated: 2026-04-16, compatible_models: [midjourney-v6, flux-1.1-pro, nano-banana]}
  video: {generated: 2026-04-16, compatible_models: [runway-gen3, kling-1.6]}
schema_version: 1.3.0
---

## Core observation
<LLM-written prose ~3 paragraphs>

<!-- llm:section-start prompts -->
## Prompts

### UI prompt
[pre-iconographic] saturated teal and amber palette (primary #1a1a2e · accent #e94560), OKLCH split-complementary, Helvetica Neue condensed, grid-breaking vertical rhythm, warm paper texture overlay
[iconographic] late-1990s Hong Kong editorial web / contemporary narrative product UI
[iconological] chromatic nostalgia — saturation as memory
[lineage] Warburg panel: [[saturation-as-memory]] · AAT: Expressive Color (aat:300056452) · signature: Wong Kar-wai

### Image prompt (compatible: midjourney v6+, flux-1.1-pro, nano-banana)
[pre-iconographic] saturated teal and amber, handheld slight sway, slow zoom on corridor, wet neon reflection, step-printed motion blur, 35mm telephoto compression
[iconographic] 1960s-90s Hong Kong tenement corridor, cheongsam silhouette, steam from noodle stall, neon signage in Traditional Chinese
[iconological] chromatic nostalgia — saturation as memory, compressed time, romantic solitude
[lineage] Warburg panel: [[saturation-as-memory]] · AAT: Chinese Modern (aat:300015541) · signature: Wong Kar-wai / Christopher Doyle cinematography
--ar 16:9 --style raw

### Video prompt (compatible: runway gen-3, sora, kling 1.6, pika)
[pre-iconographic] handheld telephoto, step-printed motion blur 6fps within 24fps base, slow zoom, wet neon reflection
[iconographic] Hong Kong corridor, passing cheongsam figure, mirror reflection
[iconological] chromatic nostalgia arc — from hope to resignation across 6 seconds
[lineage] Warburg panel: [[saturation-as-memory]] · AAT: Chinese Modern (aat:300015541) · director signature: Wong Kar-wai
duration: 6s · transition: dissolve with saturation lift
<!-- llm:section-end prompts -->

<!-- llm:section-start academic-lineage -->
## Academic Lineage

- **Warburg panel**: [[saturation-as-memory]] — saturation-as-time-sediment Pathosformel bridging Vermeer interior light, Matisse expressive color, Wong Kar-wai Hong Kong nightscape
- **Panofsky layer**: iconological — color here functions not as visual attribute but as symbolic structure of cultural memory
- **Getty AAT**: [aat:300015541](http://vocab.getty.edu/aat/300015541) — Styles and Periods > Asian > East Asian > Chinese Modern
- **Wikidata**: [wikidata:Q1398191](https://www.wikidata.org/wiki/Q1398191)
- **Cross-tradition notes**: Pathosformel traces back to Vermeer (Dutch Golden Age) and Matisse (Fauvism); contemporary Nachleben in Wong Kar-wai cinema, parts of Nan Goldin photography, Disco Elysium game art.
<!-- llm:section-end academic-lineage -->
```

Also creates/updates `wiki/_panels/saturation-as-memory.md` with `generator_ready: false` (needs ≥5 members).

**What the user does**: drops images, runs `/ingest --panel`, reads output. **Never touches aat_id, never reads who Warburg is, never writes prompt skeleton** — yet output carries academic lineage; prompts paste directly into Midjourney/Runway.

### 5.4 Prompts as core deliverable

v1.3's key repositioning — TASTE's endpoint is creation, not analysis.

**Structural skeleton** (all modalities): four labeled segments:
- `[pre-iconographic]` — concrete sensory
- `[iconographic]` — cultural markers
- `[iconological]` — mood / worldview
- `[lineage]` — Warburg panel + AAT term + signature

Labels are literal text. **Their presence alone forces generation models out of "style tag blending" into compositional thinking.** This is the scholarly version of the "layering" technique Midjourney communities reverse-engineered over three years.

**Modality differences**:
- **UI prompts**: design tokens (HEX+OKLCH palette, real typeface names, spacing rhythm, interaction motifs) + lineage. For AI coding agents implementing frontend.
- **Image prompts**: for Midjourney v6+, Flux, Nano Banana, SD. Include aspect ratio, focal treatment, light direction, negative space. AAT verbatim.
- **Video prompts**: for Runway, Sora, Kling, Pika. Add temporal specs. Name director when Pathosformel has cinematic provenance.

**Panel-level prompts**: when panel `generator_ready: true` (≥5 members, ≥0.7 score), `/prompt --panel <panel>` synthesizes across panel members, producing prompts that **operate in the tradition rather than imitate a single reference** — Nachleben operationalized.

**Prompt lifecycle**:
1. Auto-generated at `/taste` or `/ingest`
2. User uses prompt; `/prompt --use` logs usage
3. `generative_regression` evaluates (§5.6)
4. High-quality prompts **promoted** to `wiki/_prompts/` standalone entities, `derived_from` source Aesthetic

### 5.5 L2 localization

Downgraded from v1.2 ("core differentiator") to "deep L2" (no L1 void claim). `/distill` reconstructs English to native-language via cognitive restructuring; `/glossary` manages term mapping following Getty AAT multilingual convention. **Prompt bodies remain English** for generator compatibility; prose may be native language.

### 5.6 Evaluation methods

Three methods, all samples as markdown in `wiki/_evals/`:

**(a) Reverse identification** — `taste-lineage` accuracy. 6 × 20 = 120 stimuli. Top-3 accuracy ≥ 0.7 via inter-coder agreement.

**(b) Blind comparison** — human expert vs subagent set. Cross-check against Getty AAT / Wikidata. Divergences flagged for review, not auto-rejected.

**(c) Generative regression** — **core user validation method** (elevated in v1.3). Auto-generated prompts run on declared compatible models; output shown to human reviewers who guess the source Aesthetic. Identification accuracy ≥ 0.7 = prompt passes. This validates the actual product promise.

### 5.7 Evaluation-set curation

LLM pulls candidates from public canon (AFI Top 100, Apple Design Award, TDC, Pritzker, Magnum, D.I.C.E.). Human approves/modifies/deletes (no from-scratch picking). Approved → `wiki/_evals/<method>/<slug>.md`. Auto-promotion scan adds exemplary new Aesthetics to eval set. **This workflow is itself a miniature instance of agent-human co-evolution.**

---

## 6. User Flows

### 6.1 Installation

```
user clones → /genesis → detect agents → symlink skills →
initialize raw/ wiki/ schema.md → build empty indices → ready.
Hint: "try /ingest <url> or drop images into raw/images/ then /taste."
```

### 6.2 End-to-end: Wong Kar-wai chromatic nostalgia → video generation

```
1. user drops 10 Chungking Express stills into raw/images/wkw/
2. user runs /ingest --panel raw/images/wkw/
   system: taste-eye → taste-icon → taste-lineage → taste-synthesis
           → wiki/aesthetics/cinema/wong-kar-wai-chromatic-nostalgia.md
             (prompts + academic-lineage sections)
           → wiki/_panels/saturation-as-memory.md (new panel)
3. user opens Obsidian → sees new Aesthetic card
4. user copies video prompt to Runway → gets 6s clip
   (optional) /prompt --use wong-kar-wai-chromatic-nostalgia video
5. (optional) user promotes favored prompt:
   /prompt --promote wong-kar-wai-chromatic-nostalgia video
   → creates wiki/_prompts/saturation-nostalgia-video.md
```

**Concepts the user encounters**: drop images, `/ingest --panel`, open MD, copy prompt, optionally `/prompt`. **Equivalent surface area to Karpathy original** plus one action (copy to generator), which is where product value lives.

### 6.3 Query flow

```
user: /ask which Aesthetics use the "Saturation as Memory" panel?

reply: "3 Aesthetics sit in this Pathosformel:
  · [[Wong Kar-wai Chromatic Nostalgia]] — cinema, iconological
  · [[Nan Goldin Nightscape]] — photography, iconological
  · [[Disco Elysium Narrative Scenes]] — game art, iconological
  panel details at [[Saturation as Memory]]."
```

### 6.4 English-article ingestion (auxiliary)

```
/ingest https://anthropic.com/engineering/harness-design
→ raw/articles/harness-design.md
→ /distill (English → Chinese)
→ /compile → concept (role: methodology), concept, person
→ auto cross-link, rebuild index
```

---

## 7. Related Work and Academic Benchmarks

### 7.1 Academic benchmarks (Bab-ilu's ecosystem)

| Benchmark | Form | Relation |
|-----------|------|----------|
| [Warburg Institute Mnemosyne Atlas](https://warburg.sas.ac.uk/) | Scholarly image archive | `wiki/_panels/` inherits Warburg panel tradition |
| [Getty AAT](http://vocab.getty.edu/aat/) | Controlled vocabulary | Aesthetic `aat_id` cites directly |
| [Wikidata LOD](https://www.wikidata.org/) | Global linked open data | `wikidata` field, future federation |
| [Europeana](https://www.europeana.eu/) | European digital heritage | Potential future federation partner |

### 7.2 Adjacent systems (not base)

| Project | Strength | Relation |
|---------|----------|----------|
| [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | Minimal multi-agent | Few skills, no aesthetics; borrowed setup |
| [MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki) | Dual-platform | Simpler schema, no aesthetics |
| [Obsidian LLM Wiki plugin](https://forum.obsidian.md/t/new-plugin-llm-wiki-turn-your-vault-into-a-queryable-knowledge-base-privately/113223) | Local privacy (Ollama) | Plugin only, no multi-agent |

---

## 8. Technical References

### Cloned references (`references/`)

| Directory | Source | Why |
|-----------|--------|-----|
| `references/OmegaWiki/` | [skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki) v0.1.0 | **Fork base**, historical snapshot |
| `references/obsidian-wiki/` | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | Multi-agent skill architecture |
| `references/llm-wiki/` | [MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki) | Dual-platform idea |
| `references/llm-wiki-agent/` | [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | Lightweight markdown pipeline |
| `references/obsidian-claude-code-mcp/` | [iansinnott/obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp) | MCP integration pattern |
| `references/claude-code-analysis/` | [liuup/claude-code-analysis](https://github.com/liuup/claude-code-analysis) | Claude Code internals |

### External references

- [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — **three-layer philosophical base**
- [Panofsky, *Studies in Iconology* (1939)](https://en.wikipedia.org/wiki/Iconology) — three-layer iconology
- [Warburg Institute Mnemosyne Atlas](https://warburg.sas.ac.uk/archive/archive-collections/mnemosyne-atlas) — panel tradition
- [Getty AAT Online](http://vocab.getty.edu/aat/) — AAT online thesaurus
- [Wikidata](https://www.wikidata.org/) — LOD
- [Anthropic Harness Design](https://www.anthropic.com/engineering/harness-design-long-running-apps) — multi-agent methodology

---

## 9. Error Recovery and Maintenance

### 9.1 Recovery model

**Immutable raw + rebuildable wiki + stable schema.md**:
- `raw/` immutable
- `wiki/` re-derivable from `raw/` via `/ingest`
- `_index/` rebuildable from frontmatter via `tools/rebuild-index.sh`
- `schema.md` versioned, stable anchor of LLM behavior
- Subagent prompts in `.claude/agents/` reference `schema.md §x.y`; schema updates propagate

### 9.2 Common recovery scenarios

| Scenario | Recovery |
|----------|----------|
| Ingestion error | Delete `wiki/` entries, re-run `/ingest` |
| Index corruption | `tools/rebuild-index.sh` |
| Aesthetic missing "Academic Lineage" | `/check` → auto re-run `/taste` |
| `aat_id: null` > 14 days | `/check` surfaces candidates |
| Prompt tests > 30 days stale | `/check` triggers generative_regression |
| Panel members < 3 | `/check` flags "potentially unstable" |
| Glossary drift | `/check` → `/glossary` fix |
| schema_version drift | `/check` offers migration |

### 9.3 `/check` specification

Reads `schema.md`, reports divergences: AAT IDs, missing sections, expired prompt tests, thin panels, glossary drift, eval sample gaps, schema_version mismatches.

### 9.4 Scale ceiling

v1 targets ≤ **10,000 entries**. `edges.jsonl` lazy rebuild ≈ 30K edges, 3MB.

### 9.5 Backup philosophy

**No git dependency.** `raw/` immutable + `schema.md` stable + `wiki/` rebuildable ≡ complete system. Users may add git but it is user choice.

---

> PRD v1.3 end. Authoritative version is `PRD-zh.md` (Chinese). This English file is a mirror; content must stay consistent.
> Schema details (read by LLM) live in `schema.md`. This PRD cites schema sections by number but does not re-describe content.
