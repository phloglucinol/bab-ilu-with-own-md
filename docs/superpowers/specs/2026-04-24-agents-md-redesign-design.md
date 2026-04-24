# AGENTS.md Redesign Spec

Date: 2026-04-24
Status: Approved in chat, pending written-spec review
Owner: Codex

## Summary

This change rewrites the root `AGENTS.md` so it matches the role, structure,
and constraint level of `CLAUDE.md` while still speaking to Codex and other
agent runtimes.

The core decision is to keep project guidance aligned across entry files:

- `CLAUDE.md` remains the Claude Code-oriented project guide
- `AGENTS.md` becomes the Codex-oriented project guide
- both files share the same project theory, architecture, hard rules, and
  session discipline
- runtime-specific differences are limited to workflow entry syntax and skill
  loading notes

The intended result is that `AGENTS.md` stops being a short compatibility note
and becomes a full project contract for agents entering the repository through
Codex.

## Problem

The current `AGENTS.md` is much thinner than `CLAUDE.md`.

It correctly explains the Claude Code versus Codex syntax difference, but it
does not carry the project's hard constraints at the same level as
`CLAUDE.md`. That creates two problems:

- Codex may enter the repo without the same theory and operating rules that
  Claude Code gets at session start
- future edits can drift the two files apart semantically, making one agent
  surface stricter or more complete than the other

## Goals

- Rewrite `AGENTS.md` so it has the same structural coverage as `CLAUDE.md`
- Preserve the same project-level constraints, theory, and architecture
- Keep Codex-specific instructions explicit where runtime behavior differs
- Make `AGENTS.md` usable as a standalone session-start guide for Codex

## Non-Goals

- Do not change the authoritative meaning of the project rules
- Do not weaken or reinterpret the theory inherited from `PRD-v2.1-zh.md`
- Do not turn `AGENTS.md` into a README or quickstart tutorial
- Do not duplicate all prose mechanically if a small runtime-specific edit is
  enough

## Chosen Approach

Three approaches were considered:

1. Keep `AGENTS.md` short and only document syntax differences.
2. Rewrite `AGENTS.md` to mirror the `CLAUDE.md` structure while adapting the
   runtime-specific parts.
3. Copy `CLAUDE.md` almost verbatim and swap only a few keywords.

Approach 2 is selected.

It preserves parity at the project-contract level without forcing a
word-for-word mirror. The two files will share the same sections and same
substantive rules, but `AGENTS.md` will explicitly document Codex-facing
workflow entrypoints such as `$genesis`.

## Design

## 1. Match `CLAUDE.md` Section Skeleton

`AGENTS.md` should use the same top-level structure as `CLAUDE.md`:

- title and authority-source introduction
- `0. 理论基础`
- `What Bab-ilu Is`
- `Three-Layer Architecture`
- `Vault Language`
- `Hard Rules`
- `Commands`
- `Prohibited`
- `When Things Go Wrong`
- `Session Start Checklist`

This keeps both entry files aligned in how they teach the repo to an agent.

## 2. Preserve Theory and Hard Constraints

The rewritten `AGENTS.md` should carry the same substantive constraints as
`CLAUDE.md`, including:

- the core value proposition
- the five operational principles
- the Karpathy inheritance points
- session startup ordering
- three-layer architecture
- non-negotiable writing rules and prohibitions

These sections should stay semantically equivalent unless there is a
runtime-specific reason to diverge.

## 3. Codex-Specific Runtime Adaptation

`AGENTS.md` must explicitly call out the runtime differences that matter for
Codex:

- Claude Code uses slash-style workflow entrypoints such as `/genesis`
- Codex uses skill-style entrypoints such as `$genesis`
- these are agent-conversation entrypoints, not shell commands
- `.claude/skills/` remains the single Bab-ilu skill source
- `setup.sh` only installs dependencies and links skills; runtime behavior
  still belongs to the skills

The runtime note should be integrated into the larger guide, not left as a
separate mini-document.

## 4. Command Table Adaptation

The `Commands` section in `AGENTS.md` should be adapted so the command table
does not imply Claude-only syntax.

Recommended shape:

- one column for Claude Code syntax
- one column for Codex syntax
- one column for purpose

This makes the mapping explicit without changing command semantics.

## 5. Keep Scope Tight

The rewrite should not introduce additional product behavior.

Specifically, it should not:

- add new commands
- redefine command semantics
- move operational details from skills into `AGENTS.md`
- duplicate quickstart or installation walkthrough content already covered in
  the README or Codex quickstart doc

## File Plan

Files to update:

- `AGENTS.md`

Files intentionally unchanged:

- `CLAUDE.md`
- `.claude/skills/**`
- `README.md`
- `README.en.md`
- `setup.sh`

## Success Criteria

- `AGENTS.md` exposes the same project-level constraints as `CLAUDE.md`
- a Codex session entering the repo receives the same architectural and
  theoretical guidance as a Claude Code session
- runtime-specific syntax differences are explicit and accurate
- `AGENTS.md` remains concise enough to serve as an entry file, not a second
  README

## Risks and Mitigations

Risk: the rewrite drifts from `CLAUDE.md` and creates subtle rule mismatches.
Mitigation: keep section order and substantive content closely aligned; only
adapt runtime-specific wording.

Risk: `AGENTS.md` becomes a generic mirror that ignores Codex-specific usage.
Mitigation: make entry syntax, skill source, and shell-vs-conversation rules
explicit.

Risk: the file becomes bloated with onboarding material.
Mitigation: keep setup and quickstart detail out of scope unless required to
explain runtime behavior.

## Verification Plan

- Read `CLAUDE.md` and the rewritten `AGENTS.md` side by side
- Confirm the same major sections exist in both files
- Confirm Codex entry syntax appears wherever command invocation is described
- Confirm no shell-command wording suggests `$genesis` or `/genesis` should be
  run in bash
