# Upstream baseline

Bab-ilu is a **hard fork** of [skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki) (released as OmegaWiki v0.1.0). Independent evolution; no periodic upstream merge.

Rationale and strategy: `PRD-v2.1-zh.md` §11 ("外部依赖"), which records that OmegaWiki is no longer treated as a live dependency and that its academic-lifecycle skills are preserved off the main path as opt-in legacy.

## Fork baseline commit SHA

The `references/OmegaWiki/` snapshot currently in this tree points at:

```
commit 4bef77d04375bfeeb32ecccb8cf735ac50dd2f4e
Date:   2026-04-12 11:08:25 +0800
Subject: Merge pull request #8 from skyllwt/fix/init-spec-consistency
Tag:    (untagged in local snapshot; matches post-v0.1.0 main)
```

> **TODO (before v1.0 release):** pin the *actual* fork-baseline SHA. The reference snapshot above is the current HEAD of the vendored clone, not necessarily the commit Bab-ilu forked from. Before v1.0 ships, confirm the exact OmegaWiki commit Bab-ilu diverged at (likely the `v0.1.0` tag) and replace this block.

Verification command:

```bash
git -C references/OmegaWiki log -1 --format="%H%n%ai%n%s"
```

## Port log

Future OmegaWiki changes are evaluated case-by-case for **porting** (not merging). Every port is recorded here with provenance.

| Date | OmegaWiki SHA | Ported to Bab-ilu SHA | Files touched | Notes |
|------|---------------|----------------------|---------------|-------|
| — | — | — | — | — |

No upstream ports have landed since the fork. Each future port will be recorded here with provenance (date, OmegaWiki SHA, Bab-ilu commit, files touched, rationale).

## License compatibility

OmegaWiki is released under the **MIT License** (`references/OmegaWiki/LICENSE`, "Copyright (c) 2026 OmegaWiki Contributors"). Bab-ilu is also MIT-licensed. The licenses are compatible: MIT permits redistribution and modification with attribution, and inherited files retain their original copyright notice where applicable.

No additional compliance work is required for the current inheritance scope.

## Inherited surface area

### 9 v2.1-native commands (`.claude/skills/`)

These are the primary user-facing commands in the v2.1 pivot. They are domain-agnostic and driven by the active lens configuration (see `PRD-v2.1-zh.md` §5 "命令表"):

| Command | Role |
|---|---|
| `/genesis` | Interactive vault init (language, lens, seed kit) |
| `/ingest` | Consume raw material → tier-0 / tier-1-atom pages + ontology updates |
| `/taste` | Structured single-item analysis per the active lens's `analysis_contract` |
| `/gap` | Run gap analysis → propose questions, write todos |
| `/ask` | Vault-grounded question answering with citations |
| `/prompt` | Lens-specific downstream deliverable (image prompt / pattern card / hypothesis / SBAR / …) |
| `/distill` | Cross-language cognitive reconstruction + `terminology.md` update |
| `/lint` | Health check (orphans, ontology/wiki drift, graph rebuild) |
| `/evolve-lens` | Evolve an existing lens or propose a new one (v2.1 distinctive capability) |

> The `.claude/skills/` tree also contains auxiliary entries (`setup`, `reset`, `check`, `evolve`) that support harness wiring. These are not first-class user commands.

### Legacy academic-lifecycle skills (removed in v2.2)

Earlier Bab-ilu releases preserved 16 OmegaWiki academic-lifecycle skills under `.agent/skills/legacy-academic/` as opt-in scaffolding. v2.2 removed them entirely because:

- None of them were wired to a v2.1 lens (they assumed OmegaWiki's single academic framing).
- Their Python backends (`tools/fetch_arxiv.py`, `fetch_s2.py`, `research_wiki.py`, etc.) were also removed in v2.2 — the skills pointed at nothing.
- Users who need the academic-research workflow can fork OmegaWiki directly; Bab-ilu's value is the lens-aware architecture, not the academic pipeline.

Removed skills (for reference): `paper-compile`, `paper-draft`, `paper-plan`, `rebuttal`, `refine`, `exp-design`, `exp-run`, `exp-eval`, `exp-status`, `daily-arxiv`, `ideate`, `novelty`, `prefill`, `research`, `survey`, `review`.

### Entity types

OmegaWiki v0.1.0 shipped 9 entity types: Papers, Concepts, Topics, People, Ideas, Experiments, Claims, Summaries, Foundations/Question. Bab-ilu:

- **Collapses** academic-specific types (Papers / Experiments / Claims / Summaries / Foundations) into a generic `concept` entity with a `role:` discriminator, so the schema remains domain-agnostic.
- **Preserves** Concepts, Topics, People, Ideas (as `concept` + role).
- **Adds** `aesthetic` (Warburg-style visual/affective knowledge) and `prompt` (generative deliverable).

### Relation types

OmegaWiki v0.1.0 shipped 9 relation types. Bab-ilu preserves them and extends with `applies`, `exemplifies`, `frames` to support lens-driven analysis contracts (e.g., Panofsky three-level, Alexander Problem-Context-Forces-Solution, Kuhn Observation-Anomaly-Paradigm).

### Python infrastructure & tooling

- `tools/research_wiki.py` (CLI surface — removed in v2.2 along with the academic skills)
- `mcp-servers/` scaffolding
- `tests/` harness
- `i18n/` and `requirements.txt`
- `setup.sh` (agent detection + symlink install)

### Conceptual patterns

- Academic research loop (literature scan → novelty check → ideation → experiment → paper → peer review) — *not* inherited. Fork OmegaWiki directly if you need this workflow.
- Tier-based page model and ontology separation — generalized in v2.1.

## What Bab-ilu does NOT inherit (by design)

- OmegaWiki's schema hardcoding in Python — externalized to `.agent/schema.md` and lens-specific `.agent/lenses/<id>/prompts.md`.
- OmegaWiki's L0 / L1 / L2 token-tier architecture — removed in v1.3 as incompatible with Karpathy's three-layer constraint.
- OmegaWiki's text-only knowledge assumption — Bab-ilu treats visual/aesthetic knowledge as first-class via the `aesthetic` entity and Warburg panels (see lens `aesthetic-warburg`).
- OmegaWiki's single-domain academic framing — replaced by the v2.1 multi-lens model (see `PRD-v2.1-zh.md` §8 "透镜库").
