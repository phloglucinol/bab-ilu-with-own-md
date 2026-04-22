# Bab-ilu Vault — Agent Project Guide

> This file is read by Claude Code and other AI agents in THIS vault.

## Vault Metadata

```yaml
vault_language: {{VAULT_LANGUAGE}}     # Set at /genesis: zh, en, ja, es, fr, ...
created: {{GENESIS_DATE}}
seed_imported: {{SEED_IMPORTED}}        # true if /genesis --seeded was used
```

## Three-Layer Architecture

| Layer | Directory |
|-------|-----------|
| Raw sources | `raw/` (immutable) |
| Human knowledge | `wiki/` |
| Agent memory | `.agent/` (hidden) |

## Hard Rules

1. Read `.agent/schema.md` before writing `wiki/`
2. Never modify `raw/`
3. Atomic writes only
4. Wikilinks in prose, not in frontmatter
5. Wikilinks use `[[display|slug]]` pattern; slugs stable after creation
6. Dual anchor (AAT/Iconclass/ULAN): both prose footnote AND `.agent/graph/anchors.md`
7. Panofsky three-layer contract for `/taste` and `/prompt`

## Commands

See the Bab-ilu source repo's `CLAUDE.md` §Commands for the 9 available skills (set `$BABILU_REPO` to your local clone).

## Vault-Specific Conventions

<!-- User adds project-specific rules here as they emerge -->

## Session Start Checklist

1. Read `.agent/schema.md`
2. Read `vault_language:` above → use that language for prose output
3. Check `.agent/state/` for pending uncertainty
4. Note command the user's request maps to
