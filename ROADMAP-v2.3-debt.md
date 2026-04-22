# Bab-ilu v2.3 — Carried Debt from v2.2 Convergence Loop

This file collects WARNING-level items surfaced by the Round 2 and Round 3
release-audit passes during the v2.2-oss-public convergence loop. None of
these items blocked the v2.2 public release; each is deferred to v2.3 for
resolution.

Source: `.local-release-audit/CONVERGENCE-LOG.md` (archived at RELEASE
ACTION) — the loop log is not shipped in public history.

---

## Round 2 warnings (2026-04-22, MODE_B auditor)

1. **Sanity regex blind spot — uppercase user-home prefix.**
   `scripts/pre-push-sanity.sh` uses `HOME_RE` with `/Users/[a-z]+/`
   (lowercase first char only). A leaked path like `/Users/Foo/…` would
   slip past. No current hits, but the blind spot is real.
   *Fix direction (v2.3):* broaden to `[A-Za-z][A-Za-z0-9_-]*`.

2. **Binary tarball evades PII sweeps.**
   `archive/v1.4-vault-20260417.tar.gz` is a 13 MB binary. Future PII
   dropped inside tarballs would bypass git-grep sweeps. Consider
   `.gitattributes` text filter or pre-commit archive-content scan.

3. **Uncovered secret classes.**
   Sanity script does NOT check for: AWS/GitHub/OpenAI/Anthropic/Slack/
   Stripe/JWT tokens, PEM private keys, IPv6, MAC addresses, phone,
   SSN, credit-card numbers. Manual sweep today returned zero hits, but
   detection is absent. Consider integrating `truffleHog`, `detect-secrets`,
   or similar entropy-based detection in CI.

4. **Tag metadata PII by policy.**
   5 annotated tags carry `P1-103n1x@proton.me` tagger email. `proton.me`
   is in `EMAIL_EXCLUDE` by project policy. No action needed unless the
   policy changes.

---

## Round 3 warnings (2026-04-22, MODE_C auditor)

5. **CLAUDE.md — `/genesis` question-count drift.**
   CLAUDE.md says "4 interactive questions" but `/genesis` SKILL.md and
   the implementation use 5 questions (confirmed by
   `tests/test_genesis_command.py`).
   *Fix direction (v2.3):* update CLAUDE.md §"Commands (8 total)" row
   for `/genesis` to read 5.

6. **CLAUDE.md — command-count drift.**
   CLAUDE.md says "Commands (8 total)" and lists 8 commands, but the
   actual v2.1+ repo also ships `/evolve-lens` and `/evolve` (10 total).
   *Fix direction (v2.3):* rewrite the Commands table to match the live
   skill roster or note explicitly which are v2.1 extensions.

7. **README.md — seed-kit count drift.**
   README.md says "29 份 seed-kit markdown" (Chinese-language doc) but
   `seed-kits/default/` now contains 40 markdown files.
   *Fix direction (v2.3):* make the README number dynamic
   (`wc -l`-driven during release) or update to 40 with a note about
   future growth.

8. **CONTRIBUTING.md — test-count drift.**
   CONTRIBUTING.md says "662 pass, 420 skipped" but current baseline is
   "671 pass, 420 skipped".
   *Fix direction (v2.3):* regenerate the baseline line from actual
   pytest output at release cut.

9. **Seed-kit wikilink stubs — Chinese-language question stubs.**
   13 `wiki/questions/*.md` stubs in the seed-kit are Chinese-only.
   This is intentional per `/gap` material-request semantics (a vault
   user with `vault_language: zh` produces Chinese stubs), but an
   English-reader encountering the seed-kit could see it as an
   inconsistency.
   *Fix direction (v2.3):* add a one-line note to the seed-kit README
   explaining that stubs inherit the seeding author's vault language.

10. **README.md — `claude /genesis` UX ambiguity.**
    README.md's install flow shows `claude /genesis` as if it were a
    shell command. New users may try to run it as `$ claude /genesis`
    rather than as a slash command inside the Claude Code REPL.
    *Fix direction (v2.3):* clarify with "inside Claude Code, run
    `/genesis`" plus a visible REPL prompt glyph.

---

## Round 4 warnings (2026-04-22, MODE_D auditor)

11. **`graph_analyzer.py --json` emits `insights.json` despite v2.3-planned note.**
    `.claude/skills/gap/SKILL.md` documents the `--json` analyzer flag as
    "v2.3-planned / preview" but `tools/graph_analyzer.py` already writes
    `wiki/_insights.json` when invoked with `--json`. Either the SKILL.md
    wording is stale or the code shipped early.
    *Fix direction (v2.3):* pick a source of truth — if the flag is stable,
    drop the "v2.3-planned" qualifier in SKILL.md; if it is provisional,
    gate the write behind an explicit opt-in env/flag.

12. **`evolve/SKILL.md` vs `gap/SKILL.md` disagree about insights.json in v2.2.**
    `/evolve` references `wiki/_insights.json` as a first-class input, while
    `/gap` treats it as optional/preview. Two skills documenting the same
    artifact with different stability guarantees confuses users.
    *Fix direction (v2.3):* reconcile the two SKILL.md files — align on
    whether `_insights.json` is a v2.2 shipping contract or a v2.3 preview.

13. **`prompt_tester.py` reads CLAUDE.md-prohibited frontmatter fields tolerantly.**
    `tools/prompt_tester.py` accepts legacy fields like `panofsky_layer` and
    `warburg_panel` without erroring, even though `CLAUDE.md` lists them as
    prohibited in v2.1. Tolerant reads soften the prohibition into a guideline.
    *Fix direction (v2.3):* either remove the tolerant paths so prompt_tester
    enforces CLAUDE.md, or relax CLAUDE.md's absolutist wording to "discouraged."

---

## v2.2 release decision

None of warnings 1–13 block the v2.2 public release. Each is tracked
here for v2.3 resolution. The convergence loop's Class-A/B/C blocker
slots remained empty or were closed in Waves 12 and 13. Wave 14 closed
the last Class-D blocker (seed-kit frontmatter drift) and added a
writer/reader contract test to prevent regression.

<!-- llm:section-end wave-13-debt-roll -->
