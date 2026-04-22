# Pre-push checklist for v2.2-oss-public

**Status**: working tree is clean of PII; the branch's own git-log
still carries pre-scrub strings in earlier Wave-N commit message
bodies. History rewriting is required before the first `git push`.

**Enforcement**: `scripts/pre-push-sanity.sh` is authoritative. The
regex and exclusion strings in the code blocks below are *human-
readable projections* of what the script does; when this markdown
drifts from the script, trust the script and ignore the markdown.
Install the script as a git pre-push hook:

```bash
HOOKS=$(git rev-parse --git-path hooks)   # portable across worktrees
if [ -e "$HOOKS/pre-push" ] && [ ! -L "$HOOKS/pre-push" ]; then
    echo "warning: $HOOKS/pre-push already exists (non-symlink) — back up or merge before overwriting"
fi
ln -sfn "$(pwd)/scripts/pre-push-sanity.sh" "$HOOKS/pre-push"
```

**IMPORTANT**: `git push --no-verify` bypasses ALL pre-push hooks
including this one. That flag is a deliberate escape hatch in git
itself; the only defense against its abuse is maintainer discipline.
If you use `--no-verify` during an emergency, log it in the release
notes so a post-hoc audit can reconstruct the bypass.

You can also invoke the script manually:

```bash
bash scripts/pre-push-sanity.sh
```

The script does *per-match* exclusion (each matched string is
evaluated against the exclusion list independently), not *per-line*.
Earlier revisions used `grep -nE | grep -vE`, which operated on
whole lines and allowed an attackable match to hide on a line that
also contained a private/excluded match. Round-9 audit caught this
co-location exfil path; fixed in Wave 11.

## Why this file exists

Prior audits repeatedly caught the same pattern: scrub discipline was
applied only to the working tree. Commit message bodies live in
immutable git refs and retain the scrubbed strings in the prose
describing the scrub. Codifying the discipline in this file is a
defense against the pattern; keeping this file free of the same
PII classes it's designed to catch is a defense against *this* file
being the next leak surface.

## Pre-push blocking checklist

Every step here uses **pattern classes**, not literal known strings.
Do not paste raw PII into this file while documenting a scrub — the
file itself becomes the leak.

### 1. Broad PII sweep of the working tree

Run and confirm empty output:

```bash
# --- Emails ---
# Matches the general [local]@[domain].[tld] shape. Excludes RFC 2606
# reserved domains (example.*), GitHub's noreply relay, and the
# privacy-relay email used as the git-commit author.
# TLD list intentionally broad — keep expanding it as new OSS
# participants use different TLDs. Source of truth: `scripts/pre-push-sanity.sh`.
git grep -nE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net|io|me|org|co|biz|dev|ai|app|xyz|tech|info|us|uk|de|fr|cn|jp|ca|edu|gov|pro|club|tv|au|eu|nl|ru|so|im|se|no|fi|dk|at|ch|be|pt|gr|ie|nz|tr|ua|mx|ar|cl|ve|pe|br|in|kr|il|sg|pl)" \
  | grep -vE "(example\.(com|org|net)|@users\.noreply\.github\.com|@proton\.me|git@github\.com:|@gpu\.lab\.edu|@.+\.lab\.edu)"

# --- IPv4 literals ---
# Excludes 0.0.0.0, 127.0.0.1, RFC 1918 private blocks (10/8, 172.16/12,
# 192.168/16), and link-local/metadata range 169.254/16. Does NOT use \b
# word boundaries — BSD grep / macOS ugrep silently ignore \b in ERE
# and return false-negatives. Explicit `(^|[^0-9])` / `([^0-9]|$)` char
# classes are used instead and are portable to both BSD and GNU grep.
git grep -nE "(^|[^0-9])[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}([^0-9]|$)" \
  | grep -vE "(0\.0\.0\.0|127\.0\.0\.1|(^|[^0-9])192\.168\.[0-9]+\.[0-9]+|(^|[^0-9])172\.(1[6-9]|2[0-9]|3[01])\.[0-9]+\.[0-9]+|(^|[^0-9])10\.[0-9]+\.[0-9]+\.[0-9]+|(^|[^0-9])169\.254\.[0-9]+\.[0-9]+)"

# --- Internal-looking hostnames ---
git grep -nE "https?://[a-z0-9-]+\.(internal|local|lan|corp|intranet)"

# --- Absolute user-home paths (substitute your own username or drop
#     the guard if your path is acceptable). Exclude known test-fixture
#     placeholder usernames (alice/bob/charlie/dave/eve). ---
git grep -nE "/Users/[a-z]+/|/home/[a-z]+/" \
  | grep -vE "(example|<[a-z-]+>|/home/(alice|bob|charlie|dave|eve)/|/Users/(alice|bob|charlie)/)"
```

All four commands must return empty output (exit code 1 from the
final grep in the pipeline).

### 2. Commit-message sweep

Run and confirm empty output:

```bash
# Emails in any commit body (TLD list matches §1; keep in sync).
git log --format="%H %B" v2.2-oss-public \
  | grep -nE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net|io|me|org|co|biz|dev|ai|app|xyz|tech|info|us|uk|de|fr|cn|jp|ca|edu|gov|pro|club|tv|au|eu|nl|ru|so|im|se|no|fi|dk|at|ch|be|pt|gr|ie|nz|tr|ua|mx|ar|cl|ve|pe|br|in|kr|il|sg|pl)" \
  | grep -vE "(example\.(com|org|net)|@users\.noreply\.github\.com|@proton\.me|git@github\.com:)"

# IPv4 in any commit body. Same \b-free regex as §1 for the same
# BSD-grep portability reason.
git log --format="%H %B" v2.2-oss-public \
  | grep -nE "(^|[^0-9])[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}([^0-9]|$)" \
  | grep -vE "(0\.0\.0\.0|127\.0\.0\.1|(^|[^0-9])192\.168\.[0-9]+\.[0-9]+|(^|[^0-9])172\.(1[6-9]|2[0-9]|3[01])\.[0-9]+\.[0-9]+|(^|[^0-9])10\.[0-9]+\.[0-9]+\.[0-9]+|(^|[^0-9])169\.254\.[0-9]+\.[0-9]+)"
```

If either returns hits, **do not push**. Use one of the remediations
below.

### 3. Remediation A (preferred): orphan-squash

Collapses every wave-N commit into a single "initial public release"
commit, discarding the pre-scrub prose entirely:

```bash
git checkout v2.2-oss-public

# Create an orphan branch with zero ancestors — clean slate.
git checkout --orphan v2.2-oss-clean
git commit -m "v2.2.0-alpha · initial public release

Forked from skyllwt/OmegaWiki v0.1.0. See docs/UPSTREAM.md for the
fork lineage and PRD-v2.1-zh.md for the v2.0 → v2.1 architectural
pivot. Test baseline: 671 pass / 420 skipped (pytest)."

# Replace the old branch.
git branch -D v2.2-oss-public
git branch -m v2.2-oss-public

# Sanity: exactly 1 commit.
git log --oneline

# Re-run section-1 and section-2 sweeps. Both must return empty.
```

### 4. Remediation B (keep wave history locally)

```bash
# Rewrite commit-message prose via interactive rebase + reword.
git rebase -i --root

# For every commit flagged by the section-2 sweep, change "pick" to
# "reword". When the editor opens the commit body, replace any raw
# PII literal with a placeholder token of the form
#   <private-email-redacted>
#   <private-host-ip-redacted>
#   <internal-hostname-redacted>

# Re-run sweeps; re-rebase if any pass was missed.
```

### 5. Tag blobs

```bash
# List remaining tags.
git tag -l

# Confirm no tag points at a pre-scrub blob. The class-of-string
# regex must live in this script, not in this file's prose.
# The TLD list must match §1 + §2 + scripts/pre-push-sanity.sh. The
# IPv4 pattern uses the \b-free form so it works under BSD grep.
CHECK_REGEX='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net|io|me|org|co|biz|dev|ai|app|xyz|tech|info|us|uk|de|fr|cn|jp|ca|edu|gov|pro|club|tv|au|eu|nl|ru|so|im|se|no|fi|dk|at|ch|be|pt|gr|ie|nz|tr|ua|mx|ar|cl|ve|pe|br|in|kr|il|sg|pl)|(^|[^0-9])[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}([^0-9]|$)'
for t in $(git tag -l); do
  if git grep -E "$CHECK_REGEX" "$t" 2>/dev/null \
       | grep -vE "(example\.(com|org|net)|@users\.noreply\.github\.com|@proton\.me|git@github\.com:|0\.0\.0\.0|127\.0\.0\.1|(^|[^0-9])192\.168\.[0-9]+\.[0-9]+|(^|[^0-9])172\.(1[6-9]|2[0-9]|3[01])\.[0-9]+\.[0-9]+|(^|[^0-9])10\.[0-9]+\.[0-9]+\.[0-9]+|(^|[^0-9])169\.254\.[0-9]+\.[0-9]+)" \
       | grep -q .; then
    echo "TAG CARRIES PRE-SCRUB BLOB: $t"
  fi
done

# Delete any flagged tag:
#   git tag -d <name>
```

### 6. Git author config

```bash
# Every commit on this branch should use the public relay email,
# not the personal inbox. Confirm:
git log --format="%an <%ae>" v2.2-oss-public | sort -u

# If a personal email shows up, either orphan-squash (section 3) or
# rewrite history with git-filter-repo --email-callback.
```

### 7. First push

Only after all six steps above return clean:

```bash
git remote add origin git@github.com:<your-username>/bab-ilu.git
git push -u origin v2.2-oss-public
git push origin --tags
```

### Bypass warning: `git push --no-verify`

Git's `--no-verify` flag skips ALL pre-push hooks, including the
`scripts/pre-push-sanity.sh` check installed in §0. If a maintainer
uses `git push --no-verify` during an emergency, the sanity check
does not run. This is a deliberate escape hatch in git itself; the
only defense is discipline. If you are the maintainer, treat
`--no-verify` as a paper trail that needs to be logged in the
release notes.

## If any audit finds something after push

Force-push is the only remediation if history is wrong. Prefer
orphan-squash pre-push so this never comes up.

## Self-check for this file

Run this command against PRE-PUSH.md itself. It must return empty
(the file describes regex patterns but should contain no actual
PII literals):

```bash
# Regexes mirror §1 + §2 + scripts/pre-push-sanity.sh. TLD list is the
# expanded 57-entry list; IPv4 uses the \b-free BSD-safe boundaries.
grep -nE "([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net|io|me|org|co|biz|dev|ai|app|xyz|tech|info|us|uk|de|fr|cn|jp|ca|edu|gov|pro|club|tv|au|eu|nl|ru|so|im|se|no|fi|dk|at|ch|be|pt|gr|ie|nz|tr|ua|mx|ar|cl|ve|pe|br|in|kr|il|sg|pl))|((^|[^0-9])[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}([^0-9]|$))" \
  PRE-PUSH.md \
  | grep -vE "(example\.(com|org|net)|@users\.noreply\.github\.com|@proton\.me|git@github\.com:|@gpu\.lab\.edu|0\.0\.0\.0|127\.0\.0\.1|(^|[^0-9])192\.168\.[0-9]+\.[0-9]+|(^|[^0-9])172\.(1[6-9]|2[0-9]|3[01])\.[0-9]+\.[0-9]+|(^|[^0-9])10\.[0-9]+\.[0-9]+\.[0-9]+|(^|[^0-9])169\.254\.[0-9]+\.[0-9]+)"
```

If this returns a hit, PRE-PUSH.md itself has leaked. Treat as a
blocker; rewrite the offending line to use placeholder tokens.
