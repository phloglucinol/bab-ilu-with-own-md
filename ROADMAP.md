# Roadmap

Bab-ilu follows semantic versioning. Current: **v2.2.0-alpha** (see
[README](README.md) for what's shipped). What's below is deferred,
listed so you know what's intentional, not missing.

## v2.3 — Karpathy flywheel completion + small-model path

Expected: [intentionally no date — Bab-ilu is open source, not a
startup. Ships when stable.]

Pulled from PRD §0.5 Sprint 4-5 plan.

### Technical debt (from Wave 1–3 cleanup, 2026-04-22)

Wave 1 (cleanup):
- ✅ **OmegaWiki academic pipeline removal** — fetch_*, research_wiki, reset_wiki, daily-arxiv workflow, legacy-academic skills removed
- ✅ **engineering-alexander reverse-prompt seed-kit** — 3 pattern cards
- ✅ **general-zettelkasten reverse-prompt seed-kit** — 3 progressive-summaries
- ✅ **tools/prompt_tester.py adapted** — from v1.4 hardcoded wiki/aesthetics/ to v2.1 lens.entity_model.tier_1_cluster resolution

Wave 2 (补齐):
- ✅ **examples.md for all 3 lenses** — Claude calibration layer; Sutton + Varol (zettelkasten), Cloudflare + AWS S3 (engineering), Friedrich + Tarkovsky (aesthetic)
- ✅ **tools/note_extractor.py** — zettelkasten /ingest extractor, parallel to incident_extractor
- ✅ **v2.1 active tests for /setup /reset /genesis** — 47 new tests replacing skip-marked v1.4 tests

Wave 3 (architectural + first-run fixes, post cold-eyes audit):
- ✅ **tools/incident_extractor rewritten Claude-drive** — removed anthropic SDK dependency + ANTHROPIC_API_KEY requirement (contradicted README's headline no-API-key promise)
- ✅ **requirements.txt reconciled** — added networkx, python-louvain, jsonschema, pypdf (all had live imports); removed requests, markdown-it-py (zero imports). Verified clean-venv reproducibility.
- ✅ **.claude/skills/shared-references/ deleted** — 3 files all scoped to deleted academic-lifecycle skills
- ✅ **.claude/skills/setup/SKILL.md fully rewritten** — removed ΩmegaWiki branding + references to 10 deleted skills; scope narrowed to Claude Code auth + optional Review LLM
- ✅ **config/setup-guide.md + .env.example fully rewritten** — dropped SEMANTIC_SCHOLAR_API_KEY and DEEPXIV_TOKEN (zero v2.1 users); deleted a `<private-email-redacted>` of unknown origin
- ✅ **setup.sh rewritten lens-aware** — removed v1.4 aesthetic-only vault scaffolding (wiki/aesthetics/{cinema,photo,ui,…}, _panels, _prompts); now routes users to /genesis
- ✅ **Active skill cross-refs cleaned** — evolve/SKILL.md + distill/SKILL.md + ingest/SKILL.md no longer reference /research /cross-link /compile skills
- ✅ **docs/UPSTREAM.md + PRD-v2.1-zh.md** — legacy-academic path references updated to reflect v2.2 removal
- ✅ **CONTRIBUTING.md test count corrected** — was "1717+" (fabricated); real is 651 pass + 420 skip
- ✅ **Fake Iconclass 48C7144 replaced** — 48 is "art/style" branch; seascape with figure is 25H1121. Updated Friedrich works/ file + all 3 sublime-solitude-landscape prompt seeds.

Wave 10 (eighth cold-eyes audit, 2026-04-22 — "the enforcement mechanism had a silent regex bug on the author's own platform"):
- ✅ **`\b` word-boundary false-negative in `scripts/pre-push-sanity.sh`** — the IPv4 regex used `\b...\b` boundaries. BSD grep (the default on macOS) and ugrep silently ignore `\b` in ERE mode and return zero hits on real public IPs. The script, on the maintainer's own platform, would have passed a push carrying `<example-public-ip>` style literals. Replaced with explicit `(^|[^0-9])...([^0-9]|$)` character-class boundaries that work on both BSD and GNU grep. Verified by adversarial-file repro: staging a public-IP-bearing file and running the script now fails with exit 1.
- ✅ **TLD/exclusion drift between script and PRE-PUSH.md** — Round 8 audit found three regex locations in PRE-PUSH.md carrying the pre-Wave-9 TLD list (§5 tag sweep, §1 IP exclusions using `^.*#.*10\.` comment-only private filter, §6 self-check with the old 31-entry TLD list). The script was Wave-9-current; the markdown was not. Synced both: TLD list expanded to 57 entries in all 4 locations, IP exclusion rewritten to `(^|[^0-9])10\.[0-9]+\.[0-9]+\.[0-9]+` form (matches only real 10/8 addresses, not "102.x" substrings), and 169.254/16 link-local range added to excludes (AWS metadata service address 169.254.169.254 was a legitimate SSRF-guard string in tools/incident_extractor.py that the prior IP sweep was flagging as a leak).
- ✅ **Redundant `_validate_vault_or_exit` in `tools/graph_analyzer.py`** — Wave 9 inserted the validator in `main()` (line 706) but left the original call in `_run_pipeline` (line 641). Both ran in the same path; the second was dead-code once main() wired up. Removed the duplicate with a docstring note explaining why the duplicate was removed (so the next round doesn't reintroduce it).
- ✅ **`git push --no-verify` bypass documented** — prior waves installed the pre-push hook but said nothing about git's built-in bypass flag. A maintainer using `--no-verify` skips ALL pre-push hooks, including this one. Added a dedicated warning section to PRE-PUSH.md §7 explaining the bypass as a deliberate git escape hatch requiring manual discipline.

Wave 9 (seventh cold-eyes audit, 2026-04-22 — "the fix to the bulk-label failed in the same shape as the bulk-label"):
- ✅ **Per-test manual audit of 9 Wave-8 relabels** — Wave 8's bulk-relabel attached reasons to the adjacent test (off-by-one). The ARXIV_CATEGORIES reason landed on `test_en_skill_wiki_interaction_is_none` instead of the actual parametrized ARXIV test; 7 `papers/` and `claims/` reasons landed on `test_has_reads_subsection`, `test_has_writes_subsection`, `test_reads_index`, `test_s2_api_failure`, `test_slug_conflict`, `test_deepxiv_failure`, and `test_paper_to_concept_backlink` instead of the real `test_reads_papers`, `test_writes_papers`, `test_writes_claims`, and the papers→people / papers→claims backlink tests. Wave 9 reverted the misattached reasons to the i18n blanket where appropriate and attached semantically-correct reasons to the actual papers/claims/S2/DeepXiv tests; each change was verified by reading the individual test body (not by bulk regex substitution, which has now failed three times).
- ✅ **schema_version unified across active write-time templates** — Wave 8 claimed 3 surfaces unified on 2.1.0 but missed 3 more: `.claude/agents/taste-synthesis.md:213` (stamped 1.4.0 into generated aesthetic MDs), `.claude/skills/distill/SKILL.md:162` (stamped 1.3.0 into distilled outputs), `.claude/skills/prompt/SKILL.md:175` (stamped 1.3.0 into generated prompts). These are *copy-paste frontmatter templates inside active skill bodies* — the exact write-time surface the prior sweeps missed because grep hits inside fenced code blocks read as "archival." All three unified to 2.1.0.
- ✅ **Remaining `(v1.4)` version stamps removed** — 4 `(v1.4)` tokens survived Wave 8's "W6 v1.4-stamp removal" claim, at `.claude/skills/check/SKILL.md` lines 22, 115, 121, 169. All four now corrected to lens-agnostic phrasing.
- ✅ **`scripts/pre-push-sanity.sh` — programmatic enforcement for PRE-PUSH.md** — prior waves documented the class-of-string discipline as a markdown checklist; a maintainer forgetting to run it would ship the commit-body leaks. Wave 9 adds an executable that runs every §1/§2 sweep and exits non-zero on hits, installable as a git pre-push hook via `ln -sfn ../../scripts/pre-push-sanity.sh .git/hooks/pre-push`. Verified: against the current branch, it exits 1 and names the specific Wave 5/6/7/8 commit-body lines still leaking. Installing the hook blocks `git push` at the git plumbing layer.
- ✅ **graph_analyzer.main() ordering fixed** — Wave 8 owned in NOT-VERIFIED that graph_analyzer's own main() still resolved lens before validating vault. Fixed: `_validate_vault_or_exit(Path(args.vault))` now fires first, so a user running `--vault /tmp/nonexistent` sees the vault error pointing at their path, not a lens error pointing at the repo. All three `--vault` runners (ingest, gap, graph_analyzer) now validate vault before resolving lens.
- ✅ **gap_runner duplicate validation block removed** — Wave 8 inserted a new validation block at line 586 but left the original duplicate at line 602 untouched. Removed the dead duplicate (and its misleading "kept for vault-exists-but-empty case" comment, which was itself inaccurate because both blocks checked the same condition).
- ✅ **TLD list expanded and user-home exclusion added** — Round 7 flagged that the PRE-PUSH.md regex missed `.au / .eu / .nl / .ru / .so / .im` (real TLDs with real users). Added those plus a broader list (`.se / .no / .fi / .dk / .at / .ch / .be / .pt / .gr / .ie / .nz / .tr / .ua / .mx / .ar / .cl / .ve / .pe / .br / .in / .kr / .il / .sg / .pl`). Round 7 also flagged that §1.4's user-home sweep hit 3 lines in `tests/test_remote.py` (`/home/alice`, `/home/charlie`) — added `/home/(alice|bob|charlie|dave|eve)/` and `/Users/(alice|bob|charlie)/` to the exclusion list for test-fixture placeholder usernames.
- ⏳ **~228 remaining blanket-labeled skips** — the bulk-label approach has now failed in three distinct shapes (Round 5: wrong uniform reason; Round 6: scope overreach; Round 7: attention-drift off-by-one). Per-test manual audit is the only path that actually works. Tracked as v2.3 debt with the explicit note: do not bulk-relabel; read each test body and match reason to assertion.

Wave 8 (sixth cold-eyes audit, 2026-04-22 — "the checklist file became the leak surface"):
- ✅ **PRE-PUSH.md self-leaked** — the file codifying class-of-string discipline embedded the very literals it was supposed to catch (a `chien.io` email on line 43, two `64.186.` fragments on lines 46 + 101). Wave 8 rewrites PRE-PUSH.md to parameterize the regex patterns entirely, use placeholder tokens in prose, and adds a self-check command at the bottom that grep's this file itself against the class-regex. Verified: the self-check returns empty.
- ✅ **PRE-PUSH.md email regex false-positive on its own GitHub remote line** — `git@github.com:` matches the email regex and would have triggered a false alarm on the checklist user. Added `git@github\.com:` to the exclusion list.
- ✅ **PRE-PUSH.md TLD list too narrow** — original `com|net|io|me|org|co|biz|dev` missed `.ai / .app / .xyz / .tech / .info / .us / .uk / .de / .fr / .cn / .jp / .ca / .edu / .gov / .pro / .club / .tv`. Added. A leak in one of these TLDs would have slipped past the documented sweep.
- ✅ **Wave 7's 237-skip-reason bulk-rewrite over-applied the i18n label** — not every v1.4/v2.0-era test is about the i18n draft. Round 6 caught three specific semantic classes where the i18n label was wrong: `ARXIV_CATEGORIES` env var (removed with daily-arxiv pipeline), `papers/` + `claims/` directory assertions (removed entity types in v2.1), `REQUIRED_SECTIONS` list (curated against pre-v2.1 headers). Wave 8 replaces the blanket reason on those 9 specific tests with per-class reason strings naming the real cause.
- ✅ **Test fixtures encoded plural paths** — `tests/test_graph_analyzer_lens.py` had 8 fixture `relative_path` values using plural/subdomained paths (`wiki/works/cinema/`, `wiki/motifs/`, `wiki/pathosformel/`, `wiki/incidents/distributed/`, etc.). Tests passed because they were self-consistent, but readers copying from them would have hit the real-code singular path. Fixed.
- ✅ **`seed-kit/engineering-alexander/sources/nygard-2018-release-it.md` prose had `wiki/patterns/`** — Wave 7 exempted the seed-kit directory names (correctly — those are categorical groupings), but did not sweep seed-kit *prose* that referenced vault tier paths. Now references `wiki/pattern/` (singular) per `lens.entity_model.tier_1_atom`.
- ✅ **`.claude/skills/prompt/SKILL.md` still wrote to `wiki/_prompts/`** — no lens declares `prompt` or `_prompts` as a tier; this path has no code path reading it. Rewrote the skill so generated prompts attach to the parent tier_1_cluster MD's `## Prompts` section instead of a separate directory.
- ✅ **`.claude/skills/check/SKILL.md` Category 9/10 treated v1.4 structure as hard requirement** — `wiki/index.md` + `wiki/log.md` existence were "hard requirements in v1.4," and `--rebuild-index` hardcoded `wiki/_prompts/`, `wiki/people/{domain}/`, etc. Relaxed to soft requirements and rewrote `--rebuild-index` to scan tiers declared by `lens.entity_model`, with the v1.4 `wiki/_prompts/` branch removed (prompts now attach to parent clusters per the `/prompt` skill rewrite).
- ✅ **Dangling-symlink detection in graph_analyzer** — prior code called `active_file.is_symlink()` on `<base>/active/lens.yaml`, but the dangling symlink is the `active` directory itself; Python's `Path.is_symlink()` returns False for a non-existent path. Rewrote to check `active_dir.is_symlink()` and, when true, print the symlink target (via `readlink`) so the user knows what was deleted.
- ✅ **Schema version fractured across 3 surfaces** — `schema.md` said 2.1.0; `templates/vault-schema.md` said 2.0.0; `tools/graph_analyzer.py` stamped generated `_insights.md` with 1.4.0. Unified on 2.1.0 in all three places.
- ✅ **`tools/quality_gates.py` Gate 1 was named "Schema v1.4 compliance"** — the version label was stale by two bumps. Renamed to "Schema version floor compliance (≥ 1.4.0)" — the floor check is still useful as a "no unversioned page" gate, but no longer claims to be v1.4-specific.
- ✅ **Error path ordering — lens resolution fired before vault validation** — user running `ingest_runner --vault /tmp/nonexistent` got a lens error pointing at the repo's `.agent/lenses/active/lens.yaml`, not a vault error pointing at `/tmp/nonexistent`. Swapped the order in `ingest_runner.main()` and `gap_runner.run_gap()` so vault validation fires first.

Wave 7 (fifth cold-eyes audit, 2026-04-22 — "grep one string, miss the class"):
- ✅ **Class-of-string PII sweep** — prior rounds grep'd only the one specific string each audit flagged. Round 5 expanded the vocabulary and found a private-email string surviving on ROADMAP.md:32 through 5 prior rounds. Wave 7 rewrites that line to use `<private-email-redacted>`, sweeps for any email/IP/internal-host regex class before committing, and documents the class-sweep as the required discipline going forward (see PRE-PUSH.md).
- ✅ **Singular tier_0 alignment extended across every active doc surface** — Wave 6 fixed /genesis SKILL.md scaffolding but 13 other active docs still instructed Claude to write to plural/subdomained paths (the lens prompts.md files inject into EVERY LLM call, so the drift there silently countermanded the skill fix). Wave 7 rewrote path references across: `.agent/lenses/aesthetic-warburg/prompts.md`, `.agent/lenses/engineering-alexander/prompts.md`, `.agent/spec/gap-algorithm.md`, `templates/vault-gap-algorithm.md`, `.claude/agents/taste-lineage.md`, `.claude/agents/taste-synthesis.md`, `.claude/skills/taste/SKILL.md`, `.claude/skills/check/SKILL.md`, `.claude/skills/distill/SKILL.md`, `.claude/skills/evolve/SKILL.md`, `.claude/skills/prompt/SKILL.md`, `README.en.md`. All now name singular tier directories (wiki/aesthetic/, wiki/motif/, wiki/panel/, wiki/incident/, wiki/pattern/, wiki/note/, wiki/concept/) matching lens.entity_model. seed-kit/ directories stay plural — those are categorical groupings for seed material, not vault tier paths.
- ✅ **graph_analyzer lens-base no longer hardcoded to repo** — `_resolve_lens` now prefers `<args.vault>/.agent/lenses/` when it exists, falling back to the repo-relative `DEFAULT_LENSES_BASE` only as last resort. Verified end-to-end: `python3 -m tools.graph_analyzer --vault /tmp/fresh` (with /tmp/fresh/.agent/lenses/active populated) now loads the user's vault lens and writes `_insights.md` correctly. Previously `--vault` was surface-only — lens config always read from the installed repo, breaking foreign-vault users.
- ✅ **gap_runner validator added** — the audit called out this as the one `--vault` tool Wave 6 missed. Now validates `.agent/` or `wiki/` subdir exists before proceeding, with a second-line-of-defense message for vaults scaffolded but not yet ingested.
- ✅ **prompt_tester.py sys.path.insert replaced with try/except idiom** — matches the pattern used in every other tool (Wave 6 had this as an own'd NOT-VERIFIED item). Both bare-script and `-m` invocation still verified.
- ✅ **100+ misleading skip reasons corrected** — test_skill_{setup,ask,ingest,init,check,reset,validation}.py had 237 skip decorators with reason="v1.4 expectations; v2.1 rewrite pending". The actual cause is that these tests assert an `i18n/en/` + `i18n/zh/` layout that was a v2.0/v2.1 draft and never shipped — not a v1.4 mismatch. Reason strings now name the real cause.
- ✅ **`<private-email-redacted>` removed from ROADMAP.md:32** — Wave 3 claimed to delete this email; the delete landed in setup-guide.md / .env.example but Wave 3's ROADMAP bullet quoted the email verbatim, re-seeding it. The email survived 5 audits because grep discipline only ever targeted the single string each round was told about. Fixed.
- ✅ **PRE-PUSH.md checklist created** — codifies the class-of-string sweep (not just literal-string), commit-message-prose scan, orphan-squash workflow, and tag-blob verification. Wave 5's NOT-VERIFIED item "Wave 5 itself not yet audited" generalized: any scrub commit is suspect until its own prose is re-grep'd AFTER the edit lands. PRE-PUSH.md blocks `git push` until that discipline runs.

Wave 6 (fourth cold-eyes audit, 2026-04-22 — "the commit message failed its own check"):
- ✅ **ROADMAP.md:42 itself contained the raw private-host string** Wave 5 claimed to scrub. `git grep <host-ip-redacted>` returned 1 hit inside the very bullet documenting the scrub. Rewrote the bullet without quoting the raw string; post-fix grep returns 0 hits, verified AFTER writing the new ROADMAP entry (not before).
- ✅ **3 pre-scrub tags deleted** — `v2.0-sprint1-complete`, `v2.1-sprint2-complete`, `v2.2.0-alpha-pre-p0` pinned blobs with the IP. Since they are pre-OSS milestones with no external consumers, `git tag -d` removes them cleanly. The v1.0* and v3-foundation-base tags predate the IP (verified: zero hits). Remaining step before first `git push`: orphan-squash the branch.
- ✅ **`narrative-filling.md` Kahneman attribution honesty** — the exact quote "We cannot live in a permanent state of doubt..." could not be verified against *Thinking, Fast and Slow* (Kahneman's actual terms are "WYSIATI" and "narrative fallacy" — which he himself credits to Taleb). File now labels the phrasing explicitly as a Varol gloss, not a Kahneman quote.
- ✅ **`illusion-of-expertise.md` renamed to `illusion-of-knowledge.md`** — Boorstin's published phrase is "illusion of knowledge"; the prior slug renamed it to "expertise," a Bab-ilu-author reframing. File renamed via `git mv`; 3 downstream wikilinks updated (examples.md + cluster + drunkard-under-streetlight cross-ref).
- ✅ **/ingest SKILL.md dispatch table corrected** — zettelkasten row claimed output at `wiki/source/<slug>.md + wiki/note/<atom>.md`; the actual note_extractor writes only `wiki/note/<slug>.md` (tier_0 per lens.yaml). Table now reflects the code path and calls out the prior-draft discrepancy.
- ✅ **/genesis SKILL.md scaffolding aligned with /ingest output** — prior genesis section scaffolded pluralised+subdomained directories (`wiki/works/cinema/`, `wiki/incidents/distributed/`) while ingest_runner writes singular tier_0 (`wiki/aesthetic/`, `wiki/incident/`). After first ingest users had two parallel trees. Scaffold now names singular canonical directories resolved from `lens.entity_model` with an explicit "do NOT scaffold plural variants" note.
- ✅ **/evolve SKILL.md stale rationale fixed** — Step 1 still said graph_analyzer "fails as a bare script" (true before Wave 4, false after). Replaced with accurate "both forms work; -m is canonical because immune to PYTHONPATH surprises."
- ✅ **Vault validator extended to ingest_runner + flip_wikilinks** — Wave 5 applied the helper to 4 of the then-believed "8" `--vault`-accepting tools. Round-5 audit called out that the real set is 7 (no `remote` tool, `gen_client` has no `--vault`). Wave 6 added ingest_runner + flip_wikilinks (flip_wikilinks via inline validator with a different error string — tracked in ROADMAP v2.3 as a consistency item). Wave 7 adds the missing gap_runner validator; all 7 `--vault` tools now fail fast on non-vault paths.
- ✅ **test_schema_structure.py skip reasons corrected** — 3 tests had skip reason="v1.4 expectations" but were actually testing live v2.1 invariants: schema.md ≤200 lines (currently 234), schema_version 2.0.0 (currently 2.1.0), required-sections list. Skip reasons now name the real reason per test.
- ✅ **test_genesis_command_not_hardcoded_aesthetic_only updated** — was asserting plural forms that encoded the v1.4 scaffolding bug. Now asserts singular canonical tier_0/tier_1 names that match the /ingest output contract.

Wave 5 (third cold-eyes audit, 2026-04-22 — "honesty about testing"):
- ✅ **tools/lint.py `from _schemas` wrapped in try/except** — Wave 4 claimed "every tool -m form exits 0" but lint.py had a sibling import without the fallback. `python -m tools.lint --help` crashed with `ModuleNotFoundError: No module named '_schemas'`. Fixed with the same idiom applied one line up.
- ✅ **Regression test parametrized across `-m` form too** — tests/test_tools_invokable_as_scripts.py previously hardcoded a single `-m` check on graph_analyzer. Now parametrized across every CLI tool in both forms (bare + module), which would have caught the lint.py regression above.
- ✅ **Private-proxy IP scrubbed** — a private-gateway `<host>:<port>` string appeared in 3 source comments (gen_client.py ×2, prompt_tester.py ×1). Comments rewritten to reference the generic `IMAGE_GEN_BASE_URL` contract without leaking the author's internal hostname. Note: the raw string still lives in earlier local commits and in 3 pre-release tags (v2.0-sprint1-complete, v2.1-sprint2-complete, v2.2.0-alpha-pre-p0); the tags are deleted in Wave 6 and a git-history orphan-squash is the release prerequisite before the first `git push`.
- ✅ **DEFAULT_VAULT Path.cwd() now validated, not silently accepted** — Wave 4 changed the author-hardcode to `Path.cwd()`, which traded a loud "works on my machine" failure for a silent "passes on any directory" success (e.g. quality_gates reported 6/9 PASS when run from /tmp). Wave 5 adds `_validate_vault_or_exit` helper called in main(): if --vault is unset and cwd has no `.agent/` or `wiki/` subdir, print a clear error and exit 2. Applied in 4 tools (graph_analyzer, quality_gates, prompt_tester, migrate_v13_to_v14).
- ✅ **`config/.env.example` documents IMAGE_GEN_***  — `/prompt --test` reaches `gen_client._openai_compatible_image` which crashes without IMAGE_GEN_BASE_URL + IMAGE_GEN_API_KEY. Neither was documented. Added a dedicated stanza mirroring the LLM_* block.
- ✅ **`scaling-hypothesis.md` attribution corrected** — prior wording attributed the phrase to Sutton; the phenomenon is Sutton's, but the phrase "scaling hypothesis" was coined by Gwern Branwen (2020). Separated the two claims explicitly.
- ✅ **Zettelkasten examples.md line-53 fictional reference removed** — "see wiki/notes/deep-blue-1997.md and wiki/notes/alphago-2016.md for [[search-and-learning]]; none are speculative" named two files that don't exist in the repo. Replaced with an honest statement: "slugs not marked (proposed) resolve to real files in seed-kit/; (proposed) slugs are candidates awaiting a second independent reference".
- ✅ **lint.py::rebuild_graph docstring rot fixed** — Wave 4 added try/except to graph_analyzer, so bare-script invocation no longer fails. The docstring still claimed it did, which was stale. Corrected.

Wave 4 (second cold-eyes audit, 2026-04-22 — "actually run the command"):
- ✅ **Bare-script invocation fixed** — `python3 tools/graph_analyzer.py` was broken by `from tools.X import Y`. Same pattern affected gap_runner, ingest_runner, ask_runner, incident_extractor, note_extractor. Fixed with try-first/fallback import idiom matching tools/lint.py; verified by running each script's `--help` and asserting no ModuleNotFoundError.
- ✅ **lint.py `rebuild_graph` rewritten** — uses `python3 -m tools.graph_analyzer --vault <path>` (module form + correct flag name) instead of the broken `tools/graph_analyzer.py --wiki-dir <...>`. Prior unit tests monkeypatched subprocess.run so this blocker was never exercised.
- ✅ **DEFAULT_VAULT hardcoded author path removed** — 4 tools (graph_analyzer, migrate_v13_to_v14, prompt_tester, quality_gates) used `REPO/../../Documents/Bab-ilu` which silently read the author's private vault on his machine, masking "works on my machine" bugs. Now defaults to `Path.cwd()`.
- ✅ **tests/test_tools_invokable_as_scripts.py added** — regression guard parametrized across every tools/*.py with an ArgumentParser; asserts bare-script invocation and `-m` module form both exit 0. This is the test shape the auditor specifically requested: run the command verbatim, don't mock subprocess.
- ✅ **PRD-v2.1-zh.md stale legacy-academic reference corrected** — line 645 said "legacy skill 保留在 .claude/skills/legacy-academic/ 可选启用", a path deleted in Wave 1. Line 704 listed `/research /survey /novelty` as v2.3+ roadmap items — those skills were removed, not deferred. Both corrected.
- ✅ **Iconclass 25H1121 gloss made consistent** — was "seascape with figures" in 2 places and "coastal landscape with breaking waves" in 4 places. Unified to the latter.
- ✅ **Zettelkasten examples.md honesty protocol adopted** — 13 wikilinks originally claimed "every wikilink points to a concept that actually earns its place" but 5 didn't resolve. Created 10 real seed-kit files (sutton-bitter-lesson-2019, varol-uncertainty-2020, bitter-lesson, scaling-hypothesis, human-centrism-as-epistemic-trap, search-and-learning, drunkard-under-streetlight, illusion-of-expertise, narrative-filling, uncertainty-literacy, + epistemic-humility-under-uncertainty cluster) that the examples surface; remaining 8 links (first-principles-thinking, moores-law, etc.) explicitly tagged `(proposed)` per the engineering-examples pattern.

Remaining debt (v2.3):
- **Expand engineering-alexander + general-zettelkasten seed-kits** — 3 → 10+ templates each (reach aesthetic-warburg's depth)
- **Complete prompt_tester.py v2.1 adaptation** — full refactor to read lens.yaml directly in all code paths (currently fallback tier_1_cluster default of `panel`)
- **Lens-aware rewrite of `/evolve` per-kind executors** — gap-action playbook currently v1.4-shaped around aesthetic-warburg; needs per-lens strategies for engineering (incident DB) and zettelkasten (no institutional anchors)
- **Port-or-archive legacy v1.4 skills** — `/research`, `/compile`, `/cross-link`, `/daily-feed` fully removed from active skill bodies but still referenced in historical/provenance notes in evolve/SKILL.md lines 202, ingest/SKILL.md header comments. Consider a single legacy-glossary doc.
- **Fix test_skill_file_exists** — `tests/test_remote.py::TestSkillReferences::test_skill_file_exists` references removed `.claude/skills/exp-run/SKILL.md`; delete or update test
- **Rewrite skipped v1.4 tests** — 420 skipped tests covering /setup, /reset, /init, /validation, /schema_structure, /seed_kit, /skill_ask, /skill_ingest, /skill_check. Each has a `reason=` string; rewrite against current v2.1 surface.
- **Verify all other authority IDs in .agent/lenses/aesthetic-warburg/** — the Iconclass 48C7144 fabrication caught post-hoc; ULAN / Wikidata / TGN IDs in examples.md should be re-verified against live Getty/Wikidata records

### Flywheel items (F*)

- **F1 · `wiki/overview.md` live synthesis** — after each `/ingest`,
  LLM rewrites a vault-level 3-5 paragraph prose synthesis naming
  the dominant tier-1 clusters. This is the "homepage" of a vault.
  Karpathy's gist mentions this pattern; Bab-ilu v2.2 deferred it.
- **F3 · L1/L2 context caching** — formalize which files auto-load
  at session start (L1: rules, identity, active-lens) vs. JIT
  retrieval (L2: wiki pages ≤3 at a time). Today everything is L2
  effectively, which bloats context for small models.

### Small-model items (S*)

- **S1-S4 · small-model compensation** — few-shot auto-injection,
  self-consistency resampling, task decomposition, post-verification.
  Goal: Haiku 4.5 at ≥ 80% Opus quality on aesthetic-warburg,
  ≥ 65% on open-source 30B models.
- **S5 · model routing** — route small tasks to Haiku, large
  synthesis to Opus, per `.env` configured model IDs.

## v2.4 — Closed-loop adaptivity

Expected: after v2.3 lands.

Pulled from PRD §0.5 Sprint 6 plan.

- **C2 · Adaptive thresholds** — `CONFIDENCE_THRESHOLD` learned
  from accept/reject history in feedback.jsonl instead of
  hard-coded 0.60.
- **C5 · Retraction propagation** — when `retracts-<code>` edge is
  added, downstream wiki pages get `[RETRACTED-PENDING]` markers
  so /ask, /prompt, /distill avoid them.
- **C6 · Cross-session lessons** — Stop-hook captures session-level
  user preferences, promotes them after N sessions into lens
  prompts.md candidates.

## Long-term (not promised, discussion open)

- More pre-installed lenses (musicology? mathematical proof?
  experimental physics?) — by community RFC, not central
  curation. Stress-test criteria defined in PRD §0.5.4.
- Visualization tools — deliberately deprioritized. Bab-ilu's
  thesis is the graph is the LLM's internal mechanism; users
  experience it semantically via `/gap` / `/ask` / `/evolve-lens`,
  not visually. If community PRs land a viewer, fine. We don't
  build one.
- v1.4 → v2.x vault migration tooling — only affects existing
  Bab-ilu users upgrading. Low priority since the v1.4 user
  base is ~1 person (the author).

## Principles for what gets in

Items added to ROADMAP must satisfy at least 3 of PRD §0.5.3's
five operational principles:
1. Late binding — defer until evidence accumulates
2. Anti-essentialism — family resemblance over shared essence
3. Closed-loop first — feedback loops before features
4. Variety matching (Ashby) — lens variety scales with use variety
5. Practice over rules — behavioral evidence, not declarations

Items failing these principles get rejected regardless of how
interesting they sound.
