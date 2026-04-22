---
name: genesis
description: Initialize a Bab-ilu v2.1 vault with a chosen lens. Interactive 5-question flow (or --lens=<id> skip), creates wiki/ directory structure per the lens's entity_model, copies the active lens config to .agent/lenses/active/, optionally imports the seed kit. Run once per fresh clone.
allowed-tools: [Bash, Read, Write, Edit, Glob]
---

# /genesis — Initialize the Vault (v2.1 lens-aware)

## Synopsis

```
/genesis                         # fully interactive (asks 5 questions)
/genesis --lens=aesthetic-warburg         # skip the lens question
/genesis --lens=engineering-alexander --seeded   # lens + import seed kit
/genesis --lens=general-zettelkasten --no-seeds  # skip seed kit
```

## What this skill does

Sets up a fresh Bab-ilu v2.1 vault on the user's machine. **Lens-aware** — the
chosen lens determines the `wiki/` subdirectory names and the seed kit source.
Idempotent: safe to re-run; skips anything that already exists.

## Step 1 — Parse flags + ask the 5 questions (PRD §3.1)

Read any `--lens=<id>`, `--seeded`, `--no-seeds` flags passed as arguments.
Unanswered items drop into an interactive prompt:

1. **Vault main language?** (zh / en / es / fr / ja / other) → writes
   `vault_language:` to `.agent/CLAUDE.md`. Reused on every `/ingest`.
2. **Vault lens?** (choose one)
   - `aesthetic-warburg` — visual aesthetics (cinema/photo/UI/UX/graphic/game/architecture/illustration/painting)
   - `engineering-alexander` — incidents → forces → patterns → pattern languages
   - `general-zettelkasten` — fleeting notes → permanent notes → indexes (Luhmann + Bloom)
   - (custom — user supplies a lens id from `.agent/lenses/`)
3. **Work subdomain within the lens?** Suggest the lens's `allowed_subdomains`
   if any; otherwise "综合 / general". For aesthetic-warburg the options come
   from the lens config: cinema / photo / ui / ux / graphic / game /
   architecture / illustration / painting. For engineering-alexander:
   distributed / frontend / ml / embedded / security / general. For
   general-zettelkasten: open.
4. **Import the demo seed kit?** (yes → copies seed kit tagged to the chosen
   lens from `seed-kit/<lens-id>/` into `wiki/`; no → empty vault). `--seeded`
   answers yes; `--no-seeds` answers no.
5. **Do you already have raw material?** If yes, offer to run `/ingest`
   immediately after genesis finishes.

Persist the answers into `.agent/CLAUDE.md`:

```yaml
---
vault_language: zh
vault_lens: aesthetic-warburg
vault_subdomain: cinema
seeded: true
---
```

## Step 2 — Validate the chosen lens

Invoke `tools.lens_loader.load_lens(<lens-id>)`:

```bash
python -m tools.lens_loader --validate <lens-id>
```

If the lens fails validation, STOP, print the error, and ask the user to
either pick a different lens or fix `.agent/lenses/<id>/lens.yaml`.

## Step 3 — Three-layer scaffolding (idempotent)

Confirm each path; create if missing:

- `raw/` (user-owned, immutable)
  - `raw/articles/` `raw/images/{inbox,processed}/` `raw/videos/`
- `output/` (generated deliverables)
  - `output/panels/` `output/prompts/` `output/distills/`
- `wiki/` (LLM-owned) — **lens-specific subdirectories derived from
  `lens.entity_model`**. The scaffold creates ONE directory per tier
  using the singular names the lens declares; `/ingest` writes into
  these exact directories. Do NOT scaffold pluralised or sub-domained
  variants — `wiki/works/cinema/` and `wiki/aesthetic/` would create
  two parallel trees and break every downstream reader.
  - Always: `index.md` · `log.md` · `_glossary.md` · `_evals/` · `_index/` · `_log/` · `my/` · `questions/`
  - Resolved from `lens.entity_model` at scaffold time (singular, canonical):
    ```
    wiki/<tier_0>/          # aesthetic-warburg: aesthetic ·
                            # engineering-alexander: incident ·
                            # general-zettelkasten: note
    wiki/<tier_1_atom>/     # aesthetic-warburg: motif ·
                            # engineering-alexander: pattern ·
                            # general-zettelkasten: concept
    wiki/<tier_1_cluster>/  # aesthetic-warburg: panel ·
                            # engineering-alexander: pattern-language ·
                            # general-zettelkasten: concept-cluster
    wiki/source/            # shared across lenses (raw-material anchors)
    wiki/people/            # shared across lenses (human-anchor entities)
    ```
- `.agent/` (agent configuration)
  - `.agent/CLAUDE.md` — vault main config written in Step 1
  - `.agent/lenses/` — all installed lens configs (read-only reference)
  - `.agent/lenses/active/` — **copy** of the chosen lens config (runtime use)
  - `.agent/spec/` — algorithm specs (gap-algorithm.md etc.)
- `schema.md` (project root) — canonical conventions file. If missing, the
  clone is broken; STOP and report.

Read `wiki/<tier-0>`, `wiki/<tier-1-atom>`, `wiki/<tier-1-cluster>` paths from
the lens's `entity_model` rather than hardcoding them here — the examples
above are the three launch lenses, but any new lens pluggable through
`.agent/lenses/` is supported.

## Step 4 — Initial index files

Create the following only if they don't exist:
- `wiki/_index/entry-index.yaml` — machine-readable full index (empty list).
- `wiki/_index/edges.jsonl` — machine-readable relation graph (empty).
- `wiki/_log/usage.jsonl` — machine-readable action log (empty).
- `wiki/_glossary.md` — starts with `# Glossary` header.
- `wiki/index.md` — Karpathy-style human catalog. Scaffold with frontmatter
  `lens: <id>` + top-level sections keyed by the lens's
  `entity_model.tier_1_cluster` (e.g. "## Pathosformel" for aesthetic, "##
  Patterns" for engineering).
- `wiki/log.md` — append-only chronological record. First line: `<today>
  /genesis initialized lens=<id> subdomain=<domain>`.

## Step 5 — Activate the lens

Copy `.agent/lenses/<chosen-id>/` into `.agent/lenses/active/`:

```bash
rm -rf .agent/lenses/active
cp -R .agent/lenses/<chosen-id> .agent/lenses/active
```

All runtime consumers (graph_analyzer, the 8 slash skills) read from
`.agent/lenses/active/lens.yaml` so the vault stays lens-coherent even when
multiple lenses are installed in `.agent/lenses/`.

### Runtime lens-context injection (B3 protocol)

Beyond `lens.yaml` (structured config), each lens carries a freeform
`prompts.md` — judgment rules, traps, tone hints. The `/ingest`, `/taste`,
`/ask`, `/prompt`, `/distill`, `/gap`, `/lint` skills inject this preamble
at the top of their LLM context by calling `tools.lens_context`:

```python
from tools.lens_context import active_lens_preamble
preamble = active_lens_preamble()   # "<lens-context>…</lens-context>" or ""
```

Or from a pure-markdown skill (no Python interpreter):

```bash
python -m tools.lens_context    # prints preamble or nothing
```

The reader caches the file in-process (mtime-invalidated) and honors
`BABILU_LENS_PROMPTS_PATH` for tests and power-user overrides. Missing
active lens → empty preamble + one log warning; never a crash.

## Step 6 — Optional seed kit import

If Q4 answered yes (or `--seeded`):
- Source: `seed-kit/<chosen-lens-id>/`
- **Error mode:** if `seed-kit/<chosen-lens-id>/` does not exist or contains
  no `.md` files (other than `README.md`), STOP with an actionable error —
  never silently import an empty kit. Suggest either `--no-seeds` or picking
  a lens whose seed kit has been populated.
- Destination: merge into `wiki/` preserving per-tier subdirectories.
- Mark every imported file's frontmatter `seed: true` so `/reset --seeds` can
  remove them cleanly.
- After import, run `/lint --fix` to normalize any slug/anchor drift.

## Step 7 — Agent detection and symlinking

Detect installed AI agent tooling and symlink `.claude/skills/` so every agent
can call Bab-ilu skills. Run idempotently (check existence before `ln -s`):

| Agent | Detection | Symlink |
|---|---|---|
| Claude Code | `.claude/` present | native, no symlink |
| Hermes | `~/.hermes/` | `~/.hermes/skills/bab-ilu` → repo `.claude/skills/` |
| Codex | `~/.codex/` | `~/.codex/skills/bab-ilu` → repo `.claude/skills/` |
| OpenClaw | `.agents/` | `.agents/skills/bab-ilu` → `.claude/skills/` |
| Cursor | `.cursor/` | `.cursor/skills/bab-ilu` → `.claude/skills/` |
| Gemini | `~/.gemini/` | `~/.gemini/skills/bab-ilu` → `.claude/skills/` |

## Step 8 — Report + next-step hint

Tailor output by empty vs populated vault:

**Empty vault (after seeding: false)**:
```
Bab-ilu vault initialized at <repo-path>
Lens: <lens-id>     Language: <lang>     Subdomain: <domain>

Structure:
  raw/      不可变素材(你拥有)
  wiki/     LLM 维护的知识层
            - <tier_0 dir>/        底层节点
            - <tier_1_atom dir>/   中层节点
            - <tier_1_cluster dir>/ 涌现聚类
  output/   可拿走的交付物
  schema.md 约定 + 学术锚点 prompt

Detected agents: <list>
──────────────────────────────────────────────
空 vault 第一步:
  1. 把素材丢进 raw/
  2. 说: /ingest
  3. 刷新 Obsidian 查看 wiki/<tier_0 dir>/
──────────────────────────────────────────────

替代入口:
  /ingest <URL>
  /taste        — aesthetic lens only
  /gap --tier=1 — after 20+ entries
```

**Populated vault (on re-run)**:
```
Bab-ilu vault at <repo-path> — lens=<id>, <N> tier-0 entries, <M> clusters

最近动作 (wiki/log.md):
  <last 5 lines>

入口:
  /ingest  /ask  /taste  /gap  /prompt  /distill  /lint
```

## Error modes

- `schema.md` missing → STOP; repo clone is incomplete.
- Lens validation fails → STOP; print the `LensValidationError` message.
- `.agent/lenses/<chosen-id>/` not present → STOP; list available lenses from
  `ls .agent/lenses/` and ask user to pick one.
- Cannot write to vault directories → report permissions issue; no workaround.

## Idempotency contract

Running `/genesis` twice must never destroy user data. Every creation is
guarded by an existence check. Never overwrite `schema.md`, `.agent/CLAUDE.md`,
any file under `wiki/`, or the user's answers to the 5 questions (stored in
`.agent/CLAUDE.md`). Re-running with `--lens=<different-id>` is a lens
migration — STOP and ask the user to confirm; do NOT silently overwrite the
existing `vault_lens` field.

## Implementation notes

- `mkdir -p` for directories.
- `ln -sfn` for agent symlinks (refresh target).
- `touch` + `echo` for empty index files.
- For Step 5 (lens activation) prefer `rsync -a --delete` if available; fall
  back to `rm -rf` + `cp -R`.
- Do NOT invoke `tools/graph_analyzer.py` during genesis — that tool reads
  `.agent/lenses/active/lens.yaml` which is only populated after Step 5.
