---
description: Reset wiki state to a clean scaffold by scope (wiki / raw / log / checkpoints / all). Useful during development or carefree restarts after a botched setup.
argument-hint: "--scope wiki|raw|log|checkpoints|all"
---

# /reset

> Resets the wiki to a clean scaffold by scope. Designed for development iteration and recovery after a failed setup — not a routine operation.

## Trigger

Manual: `/reset --scope wiki` / `--scope raw` / `--scope log` / `--scope checkpoints` / `--scope all`. Multiple scopes may be combined comma-separated: `--scope wiki,log`.

## Inputs

- `--scope` *(required)*: one of
  - `wiki` — delete every `*.md` under `wiki/<entity>/` and `wiki/outputs/`, regenerate `wiki/index.md` and empty `wiki/graph/` files. Preserves `.gitkeep`, `wiki/CLAUDE.md`, `wiki/log.md`.
  - `raw` — delete every file under each `raw/<sub>/` directory declared by the active lens (e.g. `raw/articles/`, `raw/images/{inbox,processed}/`, `raw/videos/`), except `.gitkeep`.
  - `log` — reset `wiki/log.md` to the empty header.
  - `checkpoints` — clear `wiki/.checkpoints/*.json` directly.
  - `all` — every scope above.

## Outputs

- Cleared / reset files on disk.
- Console summary of deleted files and reset files.

## Wiki Interaction

### Reads
- All `wiki/<entity>/*.md` (to enumerate the deletion plan).
- `raw/<sub>/*` (to enumerate raw deletions).

### Writes
- Deletes `wiki/<entity>/*.md` (preserves `.gitkeep`).
- Rewrites `wiki/index.md`, `wiki/graph/*`, optionally `wiki/log.md`.
- Deletes `raw/<sub>/*` (except `.gitkeep`).

## Workflow

**Pre-conditions**: working directory contains `wiki/`, `tools/`. Set `WIKI_ROOT=wiki/`.

### Step 1: Build the deletion plan (dry-run)

Claude enumerates deletion targets directly — no external helper is invoked.

For each requested scope, use `Glob` and `Bash ls/find` to list the files that WOULD be deleted, then present them to the user grouped by scope (wiki entity dirs, raw subdirs, log, checkpoints). Example enumeration:

```bash
# wiki scope
find wiki -type f -name "*.md" ! -name ".gitkeep" ! -name "CLAUDE.md" ! -name "log.md"
# raw scope (per active lens's declared raw subdirs)
find raw -type f ! -name ".gitkeep"
# checkpoints scope
ls wiki/.checkpoints/*.json 2>/dev/null
```

Display counts and a truncated file list. Do NOT delete yet.

### Step 2: Confirm with the user

Print the plan summary and ask for explicit confirmation:

```
About to delete N files and reset M files. Continue? [y/N]
```

If the user says no, exit. **Never proceed without explicit approval** — `/reset` is destructive and `raw/` deletions are not tracked by git.

### Step 3: Execute

Apply the plan via direct Bash, preserving sentinels (`.gitkeep`, `wiki/CLAUDE.md`, `wiki/log.md` when `log` is not in scope):

```bash
# wiki scope (example)
find wiki -type f -name "*.md" ! -name ".gitkeep" ! -name "CLAUDE.md" ! -name "log.md" -delete
# raw scope (iterate declared raw subdirs)
find raw/articles raw/images raw/videos -type f ! -name ".gitkeep" -delete 2>/dev/null
# log scope
printf '# Wiki Log\n\n' > wiki/log.md
# checkpoints scope
rm -f wiki/.checkpoints/*.json
```

After execution, regenerate `wiki/index.md` via the Write tool (empty scaffold) and leave `wiki/graph/` placeholders intact. Report the file counts to the user.

### Step 4: Log (unless `log` scope was reset)

If the executed scope did not include `log`, append a log entry so future sessions can see the reset happened. Use the Edit tool to append a dated line to `wiki/log.md`:

```
- YYYY-MM-DD reset | scope: <scope>
```

### Step 5: Report

Print the result and suggest next steps:

```
## Reset complete — scope: <scope>

Deleted: N files
Reset:   M files

Next steps:
- /init       — bootstrap wiki from raw/
- /prefill    — seed foundational background
- /ingest     — add a single source manually
```

## Constraints

- **Confirm before destructive action**: never call `--yes` without showing the plan and asking the user.
- **Preserves**: `.gitkeep` placeholders, `wiki/CLAUDE.md`, `.claude/` (skills are never touched).
- **`raw/` deletes are irreversible**: PDFs are not in git history. Warn the user before executing `raw` or `all` scopes.
- **`/reset` does not touch `tools/`, `mcp-servers/`, `i18n/`, `.env`, or git state.**
- **Scope is required**: no default action (`/reset` with no flag prompts for scope rather than guessing).

## Error Handling

- **Unknown scope**: print valid scopes and exit nonzero.
- **Missing wiki directory**: report and suggest running `/init`.
- **`checkpoint-clear` failure**: log a warning but do not fail other scopes.

## Dependencies

### Tools (via Bash)
- `find ... -delete` / `rm -f` — direct deletion with sentinel preservation
- Write tool — regenerate `wiki/index.md` empty scaffold after `wiki` scope
- Edit tool — append dated log entries to `wiki/log.md`
