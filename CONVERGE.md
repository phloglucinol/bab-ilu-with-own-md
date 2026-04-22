# BAB-ILU v2.2 · FINAL CONVERGENCE LOOP

Repo: <repo-root> · Branch: v2.2-oss-public · HEAD at loop start: cc21614

## Goal

Drive the branch to a state where an independent cold-eyes auditor
returns SHIP on **two consecutive rounds**, then execute the release
action (orphan-squash + tag + first push). Token budget unconstrained;
quality bar maximal. No hard round cap — loop until convergence or
until a blocker class proves genuinely un-remediable.

---

## Convergence rubric (non-negotiable)

An issue is a **BLOCKER** if and only if it satisfies at least one of:

  (A) **First-run break.** `git clone <repo> && cd <repo> && pip install
      -r requirements.txt && pytest` fails or `bash scripts/pre-push-
      sanity.sh` exits non-zero on the working tree.
  (B) **PII leak.** `scripts/pre-push-sanity.sh` finds non-excluded
      public-class PII (email / IPv4 / internal-hostname / non-
      placeholder user-home) in either the working tree OR the commit-
      message bodies OR any git tag blob.
  (C) **Documented-feature-missing.** README or a SKILL.md file claims
      a behavior that no code path actually supports (copy-paste command
      that crashes, wikilink that doesn't resolve, tool flag that
      doesn't exist).
  (D) **Silent data corruption.** A pytest-green code path writes to a
      location different from where its reader reads, or silently
      accepts invalid input without logging.

Everything else — doc drift, inconsistent prose, unaudited skip
reasons, style inconsistencies, portability concerns on untested
platforms — is a **WARNING** and does NOT block ship. Warnings go
to ROADMAP v2.3.

---

## Loop architecture

The orchestrator (the invoked Claude Code session) spawns sub-agents
per iteration. Sub-agents are isolated: they do not share state with
the orchestrator or with each other; the orchestrator is the only
node that holds the loop invariants.

### Per iteration

1. **Spawn ADVERSARIAL AUDITOR (sub-agent, general-purpose subagent_type)**.
   Rotate prompt mode across iterations so the same blind spot is
   not repeated:

     - Iteration 1 mode: **MODE_A · first-run break** — run verbatim
       commands in a fresh /tmp clone, catch crashes
     - Iteration 2 mode: **MODE_B · PII leak** — broad regex sweep
       against working tree, commit bodies, tag blobs
     - Iteration 3 mode: **MODE_C · feature/doc mismatch** — SKILL.md
       bash snippets vs tool reality, README claims vs code
     - Iteration 4 mode: **MODE_D · silent corruption** — writer path
       vs reader path; skills that produce output no reader consumes
     - Iteration 5+: cycle back through A→D, each time asking the
       auditor to find issues the previous round's mode missed

   Auditor returns: BLOCKERS list + WARNINGS list + NOT-VERIFIED list.
   Only BLOCKERS affect the loop; warnings go to `ROADMAP-v2.3-debt.md`
   for post-release follow-up.

2. **If BLOCKERS is empty** → record SHIP vote. Continue to next
   iteration for the second SHIP vote. Convergence requires **two
   consecutive SHIP votes from two different modes**.

3. **If BLOCKERS is non-empty** → reset the consecutive-SHIP counter
   to 0. Spawn FIXER (sub-agent) with the blocker list. Fixer hard
   constraints:

     - MUST run `pytest -q` and confirm 0 failed / 0 errors before
       committing
     - MUST run `bash scripts/pre-push-sanity.sh` and confirm working-
       tree sweeps pass (exit 1 is acceptable ONLY if the hits are all
       pre-existing Wave 5-11 commit-body leaks — script names these;
       any NEW working-tree hit or NEW commit-body hit is a hard fail)
     - MUST verify its own commit body against the class-regex before
       writing the commit (write msg to /tmp/, grep, then commit)
     - MUST use placeholder tokens (`<private-email-redacted>`,
       `<host-ip-redacted>`) when referring to any scrubbed literal
     - Commit message header: `fix: Wave N — <summary>`

4. **After fixer commits** → append a round record to
   `CONVERGENCE-LOG.md`:

     ```
     ## Round <N> · mode=<MODE> · <timestamp>

     - auditor verdict: <SHIP|NO-SHIP>
     - blockers found: <count>
     - fixer response: <committed|escalated|skipped>
     - commit hash: <sha1>
     - pytest: <N pass, M skip, F fail, E errors>
     - sanity: <working_tree_clean|working_tree_fails>
     - consecutive_ship: <0|1|2>
     ```

5. **Loop back to step 1.**

### Termination

- **SHIP × 2 consecutive** → exit to RELEASE ACTION.
- **Fixer escalates same blocker 3 times in a row** (cannot auto-fix
  → needs human judgment) → mark that specific blocker as "converged
  with known exception," append to `CONVERGENCE-ESCALATION.md`,
  continue loop treating it as a warning.
- **100 iterations reached with no two-consecutive-SHIP** → hard
  stop, write `CONVERGENCE-ESCALATION.md` summarizing the recurring
  blocker class, exit 1.

---

## Adversarial auditor prompt template

Spawn a fresh sub-agent per iteration:

```
subagent_type: general-purpose
description: Round <N> adversarial audit · mode <MODE>
prompt: |
  You are a cold-eyes adversarial auditor, round <N> of a convergence
  loop. Repo: <repo-root> · HEAD: <current-HEAD>.

  **Mode for this iteration**: <MODE_A|MODE_B|MODE_C|MODE_D>

  **Blocker rubric**: an issue is a BLOCKER if and only if it
  satisfies at least one of (A) first-run break, (B) PII leak, (C)
  documented-feature-missing, (D) silent data corruption. See the
  orchestrator's CONVERGE.md for full definitions. Anything that
  doesn't clearly satisfy A-D is a WARNING, not a blocker.

  **Prior rounds' findings (for context, not a prescription)**:
  <orchestrator pastes last 1-3 rounds of log here>

  **Specific for this mode**:
    - MODE_A (first-run break): build a fresh clone in /tmp, pip
      install, run pytest, run the sanity script. Any non-zero exit
      or unhandled exception = blocker.
    - MODE_B (PII leak): run `bash scripts/pre-push-sanity.sh`, plus
      `git log --all --format=%B | grep -E <PII-class-regex>`, plus
      `git tag -l` followed by per-tag blob scan. Any non-excluded
      hit = blocker. Commit-body leaks from Waves 5-11 are
      pre-existing and known; flag them only if there are NEW ones.
    - MODE_C (feature/doc mismatch): for every `## Commands` row in
      README.md and every bash snippet in `.claude/skills/*/SKILL.md`,
      verify the commands resolve. Pick 3 snippets per round (rotate
      through the set across rounds). Run each verbatim against a
      fresh vault. Any crash, any "returns 0 but did nothing," any
      wikilink that doesn't resolve = blocker.
    - MODE_D (silent corruption): grep every tool's write path
      (`Write(`, `open(..., 'w')`, `>` redirect in SKILL.md Bash
      blocks) and every Read path. Any mismatch = blocker. Also
      check that tools reading `lens.entity_model.tier_0` and
      writing to `wiki/<tier_0>/` agree across the full tool set.

  **Output format**: return STRICTLY the following JSON object — no
  preamble, no markdown fences, no prose. The orchestrator parses
  this directly.

  ```
  {
    "verdict": "SHIP" | "NO-SHIP",
    "mode": "<mode name>",
    "blockers": [
      {"file": "<path>", "line": <int or null>,
       "class": "A" | "B" | "C" | "D",
       "proof": "<exact command executed + relevant output excerpt>",
       "fix_hint": "<one-line suggested remediation>"},
      ...
    ],
    "warnings": [
      {"summary": "<one line>", "file": "<path>"},
      ...
    ],
    "not_verified": [
      "<one line per item>", ...
    ]
  }
  ```

  If `blockers` is empty, verdict is SHIP. If non-empty, NO-SHIP.
  Spend at least 50 tool calls. Actually run every command you claim
  to have run — no inferred results.
```

---

## Fixer prompt template

```
subagent_type: general-purpose
description: Round <N> fixer · blockers=<count>
prompt: |
  You are a remediator in a convergence loop. Repo:
  <repo-root> · HEAD: <current-HEAD>.

  **Blockers to fix** (JSON from auditor):
  <paste auditor's blockers array here>

  **Hard pre-commit constraints** (checked by the orchestrator —
  failing any of these aborts your commit):
    1. `pytest -q` returns `N passed, M skipped, 0 failed, 0 errors`.
    2. `bash scripts/pre-push-sanity.sh` shows working-tree sweeps
       all clean. Commit-message sweeps may flag pre-existing Wave
       5-11 leaks — those are OK. NEW working-tree or NEW
       commit-body hits = hard fail.
    3. Your commit message body passes the class-regex itself:

         MSG=/tmp/wave-msg.txt
         printf '%s' "<your message>" > $MSG
         TLDS='com|net|io|me|org|co|biz|dev|ai|app|xyz|tech|info|us|uk|de|fr|cn|jp|ca|edu|gov|pro|club|tv|au|eu|nl|ru|so|im|se|no|fi|dk|at|ch|be|pt|gr|ie|nz|tr|ua|mx|ar|cl|ve|pe|br|in|kr|il|sg|pl'
         grep -nE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.($TLDS)|(^|[^0-9])[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}([^0-9]|$)" $MSG \
           | grep -vE "(example\.(com|org|net|edu)|@users\.noreply\.github\.com|@proton\.me|git@github\.com|@.+\.lab\.edu|0\.0\.0\.0|127\.0\.0\.1|(^|[^0-9])192\.168\.[0-9]+\.[0-9]+|(^|[^0-9])172\.(1[6-9]|2[0-9]|3[01])\.[0-9]+\.[0-9]+|(^|[^0-9])10\.[0-9]+\.[0-9]+\.[0-9]+|(^|[^0-9])169\.254\.[0-9]+\.[0-9]+)"

       must return no output.

    4. Use placeholder tokens (`<private-email-redacted>`,
       `<host-ip-redacted>`) when describing scrubbed literals.
    5. For any blocker that requires architectural judgment Phoenix
       must make (e.g., deleting a whole feature, changing an API
       contract), emit a structured record to
       `CONVERGENCE-ESCALATION.md` and skip — do NOT commit a
       half-fix.

  Commit message header convention: `fix: Wave <N> — <summary>`.

  **Output format**: return STRICTLY the following JSON object:

  ```
  {
    "fixed": [
      {"blocker_class": "A|B|C|D",
       "file": "<path>",
       "change_summary": "<one line>"},
      ...
    ],
    "escalated": [
      {"blocker_class": "...",
       "reason": "<why auto-fix is unsafe>"},
      ...
    ],
    "pytest_result": "N passed, M skipped, 0 failed, 0 errors",
    "sanity_result": "working_tree_clean" | "working_tree_fails: <detail>",
    "commit_hash": "<sha1>" | null,
    "wave_number": <int>
  }
  ```

  If you could not fix any blocker AND escalate none, return
  commit_hash=null and explain in an `abort_reason` field.
```

---

## Orchestrator logic (executable pseudocode — adapt to Agent tool calls)

```python
consecutive_ship = 0
round_num = 0
escalation_retry_count = {}  # blocker signature → consecutive-fail count
mode_cycle = ["MODE_A", "MODE_B", "MODE_C", "MODE_D"]
MAX_ROUNDS = 100

while round_num < MAX_ROUNDS:
    round_num += 1
    mode = mode_cycle[(round_num - 1) % 4]
    prior_summary = read_last_n_rounds(3, "CONVERGENCE-LOG.md")
    current_head = git("rev-parse HEAD")

    audit = spawn_auditor(
        mode=mode,
        round_n=round_num,
        prior=prior_summary,
        head=current_head,
    )
    append_log(round_num, mode, audit)

    if audit["verdict"] == "SHIP":
        consecutive_ship += 1
        if consecutive_ship >= 2:
            break
        continue

    consecutive_ship = 0

    fix = spawn_fixer(
        blockers=audit["blockers"],
        round_n=round_num,
        head=current_head,
    )
    append_log_fix(round_num, fix)

    # Track blockers that keep getting escalated
    for e in fix.get("escalated", []):
        sig = f"{e['blocker_class']}:{e.get('file', '')}"
        escalation_retry_count[sig] = escalation_retry_count.get(sig, 0) + 1
        if escalation_retry_count[sig] >= 3:
            append_escalation(sig, e, audit)
            # After 3 escalations, promote to "known exception" — the
            # auditor should stop flagging it as a blocker from now on.

if consecutive_ship >= 2:
    release_action()
else:
    print(f"CONVERGENCE FAILED after {round_num} rounds")
    print("See CONVERGENCE-ESCALATION.md for the recurring blocker class")
    exit(1)
```

---

## RELEASE ACTION (runs only after two-consecutive-SHIP)

```bash
cd "$(git rev-parse --show-toplevel)"
git checkout v2.2-oss-public

# 1. Snapshot the pytest + sanity state for the final commit message
PYTEST_RESULT=$(python3 -m pytest tests/ -q --tb=no 2>&1 | tail -1)
FINAL_HEAD=$(git rev-parse HEAD)
FINAL_WAVE=$(git log --format=%s | grep -oE "Wave [0-9]+" | head -1 | awk '{print $2}')
ROUND_COUNT=$(grep -c "^## Round" CONVERGENCE-LOG.md)

# 2. Sanity check: working tree must be clean (commit-body hits OK)
bash scripts/pre-push-sanity.sh || echo "(commit-body leaks expected — orphan-squash removes them)"

# 3. Orphan-squash: collapse every Wave commit into ONE release commit
git checkout --orphan v2.2-oss-release
git add -A
git commit -m "v2.2.0-alpha · initial public release

Forked from skyllwt/OmegaWiki v0.1.0. See docs/UPSTREAM.md for the
fork lineage and PRD-v2.1-zh.md for the v2.0 → v2.1 architectural
pivot.

Test baseline: ${PYTEST_RESULT}
Converged after ${ROUND_COUNT} adversarial audit rounds (final wave
was ${FINAL_WAVE}). Round-by-round log preserved locally at
CONVERGENCE-LOG.md and not shipped in the public history.

🤖 Generated with [Claude Code](https://claude.com/claude-code)"

# 4. Replace the old branch pointer
git branch -D v2.2-oss-public
git branch -m v2.2-oss-public

# 5. Verify: commit-body sweep should now pass
bash scripts/pre-push-sanity.sh
SCRIPT_EXIT=$?
if [ "$SCRIPT_EXIT" != "0" ]; then
    echo "ERROR: post-squash sanity script still exits $SCRIPT_EXIT"
    echo "Investigate — orphan-squash should have cleared commit-body leaks"
    exit 1
fi

# 6. Tag the release
git tag v2.2.0-alpha

# 7. Archive the convergence artifacts locally (not pushed)
mkdir -p .local-release-audit
git log --all --oneline > .local-release-audit/pre-squash-commits.txt
mv CONVERGENCE-LOG.md .local-release-audit/ 2>/dev/null || true
mv CONVERGENCE-ESCALATION.md .local-release-audit/ 2>/dev/null || true
echo ".local-release-audit/" >> .gitignore
git add .gitignore && git commit --amend --no-edit

# 8. Stop — Phoenix runs the push manually
cat <<'EOF'
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONVERGENCE COMPLETE · v2.2-oss-public is ready to push.

Before pushing:
  1. Install the pre-push hook:
     HOOKS=$(git rev-parse --git-path hooks)
     ln -sfn "$(pwd)/scripts/pre-push-sanity.sh" "$HOOKS/pre-push"

  2. Set the remote:
     git remote add origin git@github.com:<your-username>/bab-ilu.git

  3. Push:
     git push -u origin v2.2-oss-public
     git push origin v2.2.0-alpha

Post-push: treat CONVERGENCE-ESCALATION.md (if any) as v2.3 ROADMAP
input. Do not push .local-release-audit/ — it's gitignored.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF
```

---

## Invariants the loop maintains

1. Every wave commit is atomic — never partial.
2. `pytest` is green at every round boundary.
3. `bash scripts/pre-push-sanity.sh` working-tree sweep is clean at
   every round boundary.
4. No commit body introduces a new PII-class string (old ones from
   Waves 5-11 persist until orphan-squash).
5. Warnings are collected separately in `ROADMAP-v2.3-debt.md` — they
   do NOT block ship.
6. Every round is logged to `CONVERGENCE-LOG.md` with timestamp,
   mode, verdict, and commit hash.

---

## Anti-meta-pattern defenses

Eleven prior waves demonstrated that "Round N's fix becomes Round
N+1's leak surface." Defenses baked into this loop:

1. **Rubric-bounded auditor** — issues outside A-D are warnings. The
   auditor cannot promote doc drift or style inconsistency to blocker.
2. **Mode rotation** — A → B → C → D → A. The same blind spot is
   not hit twice consecutively.
3. **Fixer pre-commit guards** — pytest + sanity + class-regex msg
   check all run before commit. Commits that would introduce the
   pattern are rejected at the tool level.
4. **Two-consecutive-SHIP requirement** — convergence is only declared
   when two different-mode audits both return SHIP. Catches the case
   where Round N's fix creates Round N+1's blocker.
5. **Orphan-squash at release** — the public branch becomes one
   commit. The full wave history (with all the self-referential
   audit prose) stays local in `.local-release-audit/`.
6. **Escalation promotion** — after 3 consecutive failed auto-fixes
   on the same blocker signature, the blocker is promoted to
   "known exception" and no longer blocks. Prevents infinite loops
   on architecturally-hard issues.

---

## When Phoenix runs this

1. Open a fresh Claude Code session in the repo root (`<repo-root>`).
2. Paste the trigger prompt that accompanies this file (see chat).
3. Walk away. Come back when the session reports either convergence
   + release readiness, or escalation needing human judgment.

Expected runtime: 2-12 hours, unbounded by design. Token usage: high.
The goal is release quality, not efficiency.
