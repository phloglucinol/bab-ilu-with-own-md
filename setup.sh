#!/usr/bin/env bash
# Bab-ilu — one-shot install helper.
#
# Does the small amount of work that has to happen OUTSIDE a Claude Code
# session: Python deps, .env template, agent symlinks. All vault
# scaffolding (raw/, wiki/, .agent/) is lens-aware and belongs to the
# /genesis skill, not to this script. Do NOT re-introduce hardcoded
# lens-specific directory layouts here — that was the v1.4 mistake.
#
# Idempotent: re-running is safe and does not overwrite existing state.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$REPO_ROOT/.claude/skills"

log()  { printf "[bab-ilu] %s\n" "$*"; }
warn() { printf "[bab-ilu] WARN: %s\n" "$*" >&2; }
err()  { printf "[bab-ilu] ERR:  %s\n" "$*" >&2; }

# ---- 1. Sanity check: repo is a valid Bab-ilu clone ----
if [[ ! -f "$REPO_ROOT/schema.md" ]]; then
  err "schema.md missing at project root — this clone is incomplete."
  exit 1
fi
if [[ ! -d "$REPO_ROOT/.agent/lenses" ]]; then
  err ".agent/lenses/ missing — this clone is incomplete."
  exit 1
fi
log "repo contract files present ✓"

# ---- 2. Python dependencies ----
log "checking Python..."
if command -v python3 &>/dev/null; then
  PYVER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  log "python3 $PYVER found ✓"
  if [[ -f "$REPO_ROOT/requirements.txt" ]]; then
    log "installing dependencies (pip --user)..."
    python3 -m pip install --user -q -r "$REPO_ROOT/requirements.txt" 2>/dev/null \
      || warn "pip install had warnings (non-fatal)"
    log "dependencies installed ✓"
  fi
else
  warn "python3 not found — /ingest, /gap, /lint won't work. Install Python 3.10+."
fi

# ---- 3. .env template ----
if [[ ! -f "$REPO_ROOT/.env" ]]; then
  if [[ -f "$REPO_ROOT/config/.env.example" ]]; then
    cp "$REPO_ROOT/config/.env.example" "$REPO_ROOT/.env"
    log ".env created from config/.env.example"
    log "  Auth:      run \`claude login\` (managed by Claude Code)"
    log "  Optional:  LLM_API_KEY / LLM_BASE_URL / LLM_MODEL (MCP llm-review)"
  fi
else
  log ".env already exists ✓"
fi

# ---- 4. Agent detection + symlinking (for non-Claude-Code agents) ----
log "detecting installed AI agents..."

DETECTED=()

link_skills() {
  local target="$1"
  local name="$2"
  mkdir -p "$(dirname "$target")"
  if [[ -L "$target" || -d "$target" ]]; then
    log "  $name: symlink already present — preserved"
  else
    ln -s "$SKILLS_DIR" "$target" && log "  $name: symlinked ✓"
  fi
}

if [[ -d "$REPO_ROOT/.claude" ]]; then
  DETECTED+=("claude-code (native)")
  log "  claude-code: native, no symlink needed"
fi
if [[ -d "$HOME/.hermes"  ]]; then DETECTED+=("hermes");   link_skills "$HOME/.hermes/skills/bab-ilu"  "hermes";  fi
if [[ -d "$HOME/.codex"   ]]; then DETECTED+=("codex");    link_skills "$HOME/.codex/skills/bab-ilu"   "codex";   fi
if [[ -d "$REPO_ROOT/.agents" || -d "$HOME/.openclaw" ]]; then
  DETECTED+=("openclaw"); link_skills "$REPO_ROOT/.agents/skills/bab-ilu" "openclaw"
fi
if [[ -d "$REPO_ROOT/.cursor" ]]; then DETECTED+=("cursor"); link_skills "$REPO_ROOT/.cursor/skills/bab-ilu" "cursor"; fi
if [[ -d "$HOME/.gemini"   ]]; then DETECTED+=("gemini");  link_skills "$HOME/.gemini/skills/bab-ilu"  "gemini";  fi

if [[ ${#DETECTED[@]} -eq 0 ]]; then
  warn "no AI agents detected. Install Claude Code or Codex to use Bab-ilu."
fi

# ---- 5. Report ----
printf "\n"
log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log "Bab-ilu install ready at $REPO_ROOT"
log ""
if [[ ${#DETECTED[@]} -gt 0 ]]; then
  log "Detected agents: ${DETECTED[*]}"
else
  log "No agents detected yet. Install Claude Code or Codex and re-run setup.sh."
fi
log ""
log "Next step — open Claude Code or Codex in this repo, then inside your agent session run:"
log "  /genesis               (interactive; scaffolds raw/ wiki/ .agent/"
log "                          per the lens you pick: aesthetic / engineering / zettelkasten)"
log ""
log "Then: /ingest <material>  and /ask \"<your question>\""
log "Do not run /genesis in bash; enter it in the agent conversation."
log ""
log "Commands: /genesis /ingest /ask /gap /lint /distill /prompt /taste /evolve /evolve-lens"
log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
