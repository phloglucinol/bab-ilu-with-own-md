# Git Submit Rules

Last updated: 2026-04-25

This file records the current split between the personal storage branch and
the code-only PR worktree. It replaces ad-hoc notes such as `tmp_log.md` as
the durable reference for future agents.

## Current Branches

Storage workspace:

- Path: `/home/liurd/bab-ilu`
- Branch: `llm-wiki-storge`
- Remote: `fork-llm-wiki-storge`
- Push command: `git push fork-llm-wiki-storge llm-wiki-storge`

Code-only PR worktree:

- Path: `/home/liurd/bab-ilu-wx2md-pr`
- Branch: `pr/wx2md-worker-20260425`
- Remote: `fork`
- Push command: `git push -u fork pr/wx2md-worker-20260425`

## 2026-04-25 Commit Record

Storage branch commits:

- `78c3f18 Add wx2md worker capture and LigPath note`
- `4391909 Add materialize concepts and gap-derived wiki updates`

Code-only PR branch commits:

- `1b6dac0 Add wx2md worker capture skill`
- `2dd6ad5 Add materialize concepts skill`

Note: `4391909` is a historical combined storage commit containing both
tooling and vault content. Future storage commits must split these surfaces
even when both belong on `llm-wiki-storge`.

## Commit Separation Rule

Always separate code/tool changes from knowledge-base changes.

Code/tool commit includes only public or reusable project surfaces:

- `.claude/skills/<skill>/`
- `tools/`
- `tests/`
- `AGENTS.md`
- `README.md`
- `README.en.md`
- `docs/`
- `schema.md`
- lens definitions under `.agent/lenses/` when they are product code

Knowledge-base commit includes vault/runtime content:

- `raw/`
- `wiki/`
- `.agent/state/`
- `.agent/todos/`
- `.agent/graph/`
- `wiki/_log/`

If a feature produces both surfaces on `llm-wiki-storge`, use two commits:

```bash
git add .claude/skills/<skill>/ tools/<tool>.py tests/<tests>.py README.md README.en.md AGENTS.md docs/<doc>.md
git diff --cached --name-status
pytest <focused-tests> -q
git commit -m "Add <feature> tool"

git add raw/<sources> wiki/<pages> .agent/state/<logs> .agent/todos/<todos> wiki/_log/<logs>
git diff --cached --name-status
git commit -m "Add <feature> wiki updates"
```

The code/tool commit should be cherry-pickable into a code-only PR branch.
The knowledge-base commit must stay on the storage branch unless explicitly
requested otherwise.

## Push Rules

Storage branch:

- Push `llm-wiki-storge` only to `fork-llm-wiki-storge`.
- Do not push personal `raw/`, `wiki/`, `.agent/state/`, `.agent/todos/`,
  or `.agent/graph/` content to `origin` or the public code fork.
- Verify before pushing:

```bash
git status --short --branch
git log --oneline --decorate --max-count=5
git show --stat --oneline --summary HEAD
git push fork-llm-wiki-storge llm-wiki-storge
```

Code-only PR branch:

- Push only reusable code, skill, tests, and public docs to `fork`.
- Before committing, check that no vault paths are staged:

```bash
git diff --cached --name-status
```

- The staged list must not contain `raw/`, `wiki/`, `.agent/state/`,
  `.agent/todos/`, `.agent/graph/`, or `wiki/_log/`.
- Verify focused tests before push:

```bash
pytest <focused-tests> -q
git push -u fork <pr-branch>
```

Never force-push either branch unless the user explicitly asks for it.

## Known Local Leftovers

These were intentionally not committed in the 2026-04-25 cleanup:

- `.codex`
- `tmp_log.md`
- `bab-ilu/` nested directory if it reappears
- deletion of `raw/articles/_debug/*render_failed.md`

Do not stage these unless the user explicitly asks.
