#!/usr/bin/env bash
# Pre-push sanity check — runs the PRE-PUSH.md §1 and §2 sweeps
# programmatically and exits non-zero on hits. Markdown checklists
# don't enforce; this script does.
#
# Install as a git pre-push hook:
#     HOOKS=$(git rev-parse --git-path hooks)
#     if [ -e "$HOOKS/pre-push" ] && [ ! -L "$HOOKS/pre-push" ]; then
#         echo "warning: $HOOKS/pre-push already exists (non-symlink) — back up or merge"
#     fi
#     ln -sfn "$(pwd)/scripts/pre-push-sanity.sh" "$HOOKS/pre-push"
#
# (Using `git rev-parse --git-path hooks` is portable across normal
# clones AND git worktrees, where `.git/hooks/` is redirected to the
# main clone's hooks dir.)
#
# Or invoke manually from the repo root:
#     bash scripts/pre-push-sanity.sh
#
# WARNING: `git push --no-verify` bypasses ALL pre-push hooks. Treat
# `--no-verify` as a manual override that loses PII protection.
#
# Portability:
#   - Uses POSIX ERE (grep -E + git grep -E). `\b` word boundaries are
#     avoided because BSD grep / macOS ugrep silently ignore `\b` and
#     return false-negatives. Explicit `(^|[^0-9])`/`([^0-9]|$)` char
#     classes are used instead; both BSD and GNU grep honor them.
#   - Per-MATCH exclusion (round-9 audit fix): earlier revisions used
#     `grep -nE $R | grep -vE $X`, which operates on whole lines. A
#     line containing both an excluded private IP AND an attackable
#     public IP would be dropped entirely, hiding the public IP. This
#     revision extracts each match with `grep -oE` and filters per
#     match; the file:line context is looked up separately for
#     reporting.
#
# Exit codes:
#   0  all checks passed
#   1  hits found in working tree or commit messages (push blocked)
#   2  internal error

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "[pre-push] error: not inside a git worktree" >&2
    exit 2
}
cd "$REPO_ROOT"

fail=0

# --- Regex classes — single source of truth for the whole repo. Keep
# --- PRE-PUSH.md prose-copies in sync with these strings. ---

TLDS='com|net|io|me|org|co|biz|dev|ai|app|xyz|tech|info|us|uk|de|fr|cn|jp|ca|edu|gov|pro|club|tv|au|eu|nl|ru|so|im|se|no|fi|dk|at|ch|be|pt|gr|ie|nz|tr|ua|mx|ar|cl|ve|pe|br|in|kr|il|sg|pl'
EMAIL_RE="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.(${TLDS})"

# Valid IPv4: each octet 0-255 via (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]).
# Using this over `[0-9]{1,3}` rejects obvious junk like `10.999.0.0`
# while still matching real IPs. Version-string false-positives for
# all-small-octet strings (e.g. `<semver-4-segment>`) are handled by
# VERSION_CONTEXT pre-filter below.
OCTET='(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])'
IPV4_RE="(^|[^0-9])${OCTET}\\.${OCTET}\\.${OCTET}\\.${OCTET}([^0-9]|$)"

HOME_RE='/Users/[a-z]+/|/home/[a-z]+/'
INTERNAL_HOST_RE='https?://[a-z0-9-]+\.(internal|local|lan|corp|intranet)'

# Exclusions (applied PER MATCH, not per line).
# Per-match exclusion: `git@github\.com` (no colon) — the `:` in the
# SSH remote form isn't part of the email regex match. Similarly
# `@.+\.lab\.edu` handles both @gpu.lab.edu and @research.lab.edu.
EMAIL_EXCLUDE='example\.(com|org|net|edu)|@users\.noreply\.github\.com|@proton\.me|git@github\.com|@.+\.lab\.edu'

IP_EXCLUDE='0\.0\.0\.0|127\.0\.0\.1|(^|[^0-9])192\.168\.[0-9]+\.[0-9]+|(^|[^0-9])172\.(1[6-9]|2[0-9]|3[01])\.[0-9]+\.[0-9]+|(^|[^0-9])10\.[0-9]+\.[0-9]+\.[0-9]+|(^|[^0-9])169\.254\.[0-9]+\.[0-9]+'

# Placeholder usernames used in test fixtures + config examples.
# Extended to cover generic "user" / "researcher" which ship in
# config/server.yaml.example as common documentation placeholders.
HOME_EXCLUDE='example|<[a-z-]+>|/home/(alice|bob|charlie|dave|eve|user|researcher)/|/Users/(alice|bob|charlie)/'

# Lines matching this pattern are skipped entirely — they look like
# version-string context (Python 3.12.7.1, Ruby 2.7.1.1, SemVer 1.0.0.0,
# "release 4.1.2.3", "v1.0.0.0"). Real public-IP references don't
# typically carry these precedents, so dropping these lines before
# per-match evaluation eliminates the false-positive without widening
# the actual IP exclusion.
VERSION_CONTEXT='(^|[^A-Za-z])(Python|python|Ruby|ruby|Node|node|npm|Go|Rust|rust|SemVer|semver|build|Build|release|Release|version|Version|v[0-9]+\.|bump|Bump|upgrade|Upgrade|tag[s]? v?[0-9])'

# run_check: per-match exclusion, line-context reporting.
# Pipeline:
#   1. source_cmd produces lines (one or many).
#   2. Pre-filter: drop lines that look like version-string context.
#   3. For each remaining line, extract all matches of $regex via -oE.
#   4. For each match, if it does NOT match $exclude, record the line
#      in the hits list (once per line, not per match — good enough
#      for reporting context).
#   5. If hits list is non-empty, block + report.
run_check() {
    local label="$1" regex="$2" exclude="$3" source_cmd="$4"
    local skip_version="${5:-0}"
    local tmp; tmp=$(mktemp)
    local input_tmp; input_tmp=$(mktemp)
    eval "$source_cmd" 2>/dev/null > "$input_tmp" || true
    if [ "$skip_version" = "1" ]; then
        grep -vE "$VERSION_CONTEXT" "$input_tmp" > "$input_tmp.v" 2>/dev/null || true
        mv "$input_tmp.v" "$input_tmp"
    fi
    # Per-match evaluation. For each line, if ANY extracted match
    # survives the exclusion, keep the line.
    while IFS= read -r line; do
        local matches
        matches=$(printf '%s\n' "$line" | grep -oE "$regex" 2>/dev/null || true)
        [ -z "$matches" ] && continue
        local keep=0
        while IFS= read -r m; do
            [ -z "$m" ] && continue
            if ! printf '%s\n' "$m" | grep -qE "$exclude"; then
                keep=1
                break
            fi
        done <<< "$matches"
        if [ "$keep" = "1" ]; then
            printf '%s\n' "$line" >> "$tmp"
        fi
    done < "$input_tmp"
    rm -f "$input_tmp"
    if [ -s "$tmp" ]; then
        echo "[pre-push] BLOCKED: $label" >&2
        head -10 "$tmp" >&2
        fail=1
    fi
    rm -f "$tmp"
}

echo "[pre-push] Working-tree sweeps..."
run_check "email matching public-TLD class in working tree" "$EMAIL_RE" "$EMAIL_EXCLUDE" "git grep -nE \"$EMAIL_RE\"" 0
run_check "public IPv4 literal in working tree" "$IPV4_RE" "$IP_EXCLUDE" "git grep -nE \"$IPV4_RE\"" 1
run_check "internal-hostname URL in working tree" "$INTERNAL_HOST_RE" "^$" "git grep -nE \"$INTERNAL_HOST_RE\"" 0
run_check "absolute user-home path in working tree" "$HOME_RE" "$HOME_EXCLUDE" "git grep -nE \"$HOME_RE\"" 0

echo "[pre-push] Commit-message sweeps..."
current_branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo HEAD)
run_check "email in commit message bodies (run orphan-squash or rebase-reword)" "$EMAIL_RE" "$EMAIL_EXCLUDE" "git log --format='%H %B' '$current_branch'" 0
run_check "public IPv4 in commit message bodies (run orphan-squash or rebase-reword)" "$IPV4_RE" "$IP_EXCLUDE" "git log --format='%H %B' '$current_branch'" 1

if [ $fail -ne 0 ]; then
    echo "" >&2
    echo "[pre-push] Push BLOCKED by sanity check. See PRE-PUSH.md for remediations." >&2
    exit 1
fi

echo "[pre-push] All sanity checks passed."
exit 0
