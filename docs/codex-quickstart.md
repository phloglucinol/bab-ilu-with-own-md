# Codex Quickstart

## Prerequisites

- Python 3.10+
- Codex installed on this machine

## 1. Run setup

```bash
./setup.sh
```

## 2. Verify the Codex skill link

Expected target:

```text
~/.codex/skills/bab-ilu -> <repo>/.claude/skills
```

## 3. Start Codex in this repo

Open Codex with this repository as the working directory.

## 4. Invoke Bab-ilu skills in the Codex conversation

Start with:

```text
$genesis
```

Then continue with `$ingest`, `$ask`, `$gap`, or `$lint`.

## Common mistakes

- Do not run `$genesis` in bash.
- Do not use Claude Code slash syntax like `/genesis` in Codex.
- Do not create a second `.codex/skills/` tree inside the repo.
