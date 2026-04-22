---
description: Interactive configuration guide for Bab-ilu's optional Review LLM. Checks `.env` state, walks through LLM_API_KEY / LLM_BASE_URL / LLM_MODEL, and offers auto-registration or skip.
---

# /setup

> Bab-ilu's configuration surface is intentionally tiny: Claude Code
> handles its own auth via `claude login`, and one optional MCP
> second-opinion LLM can be wired up if you want cross-model review.
> That's it. `/setup` walks you through the Review LLM.
>
> Safe to re-run at any time — only updates keys you choose to configure.

## Inputs

- No arguments required.
- Reads: `.env` (current state), `config/setup-guide.md` (reference).

## Outputs

- Updated `.env` with any newly configured `LLM_*` keys.
- A summary of current configuration status.

## Wiki Interaction

- None. `/setup` runs before any vault exists and never writes to `wiki/`.

## Workflow

### Step 1: Read configuration reference

Read `config/setup-guide.md` for the complete description of the Review
LLM setup, provider table, and verification script.

### Step 2: Detect current state

```bash
python3 -c "
import sys, os
sys.path.insert(0, 'tools')
try:
    import _env  # loads .env into os.environ
except Exception:
    pass
keys = {
    'LLM_API_KEY':  'Review LLM (API key)',
    'LLM_BASE_URL': 'Review LLM (base URL)',
    'LLM_MODEL':    'Review LLM (model)',
}
for k, label in keys.items():
    v = os.environ.get(k, '').strip()
    print(f'SET:{k}' if v else f'UNSET:{k}')
"
```

Also detect the Python environment:

```bash
ls .venv/ 2>/dev/null && echo "venv:present" || echo "venv:absent"
python3 --version
```

### Step 3: Show configuration status

Present a concise status summary:

```
Bab-ilu Configuration Status
============================
✓  Claude Code auth          — managed by `claude login`

Optional:
✗  Review LLM (LLM_* ×3)     — not set  (cross-model MCP review unavailable)
```

Ask: *"Configure the Review LLM now, or skip?"*

### Step 4: Configure Review LLM (if user opts in)

**Explain**: "The Review LLM powers `mcp-servers/llm-review` — a
second model that critiques Bab-ilu artifacts independently of
Claude. Works with any OpenAI-compatible API. Without it the MCP
server simply does not start; no Bab-ilu skill hard-depends on it."

**Present the provider table** from `config/setup-guide.md`.

**Clarify "OpenAI-compatible"** if asked: any API accepting
`POST /chat/completions` with
`{"model": "...", "messages": [...]}` in the OpenAI format.

**Ask for**:

1. `LLM_BASE_URL` — e.g. `https://api.deepseek.com/v1`
2. `LLM_API_KEY` — provider API key
3. `LLM_MODEL` — model name, e.g. `deepseek-chat`

**Validate format**: base URL should start with `http://` or `https://`
and typically ends with `/v1`. If it looks off, confirm before writing.

**Write all three** to `.env` via the Edit tool after the user confirms.

**Remind**: the MCP server reads `.env` at Claude Code startup —
restart Claude Code for Review LLM changes to take effect.

### Step 5: Verify configuration

Run the verification script from `config/setup-guide.md` and show the
final summary. For keys still unset, briefly note what they unlock and
that the user can re-run `/setup` anytime.

### Step 6: Next steps

If this is a fresh install (no `wiki/` directory):

```
Configuration done. Next:
  • Run: /genesis <vault-name>   (scaffolds raw/ wiki/ .agent/ per active lens)
  • Run: /ingest <material>      (first real entry, lens-aware routing)
```

If `wiki/` already exists:

```
Configuration updated. Restart Claude Code so the MCP review server picks up LLM_* changes.
```

## Constraints

- **Never overwrite an existing non-empty value** without asking first.
- **Never expose the full key value** in output — show only the first
  8 characters + `...`.
- **Write only to `.env`** — never to `~/.env` or elsewhere.
- **No wiki reads or writes** — this skill runs before the vault exists.
- **Skip gracefully**: if the user says "skip all", print the status
  summary and exit cleanly.

## Error Handling

- **`.env` missing**: inform the user `setup.sh` was not run yet; offer
  to create `.env` from `config/.env.example`:

  ```bash
  cp config/.env.example .env
  ```

  Then continue.

- **`config/setup-guide.md` missing**: fall back to the descriptions
  in this SKILL.md itself.

- **Python env issue** (`tools/_env.py` not importable): note that
  `.venv` may not be active, but still read `.env` directly via plain
  shell or Python file I/O.

## Dependencies

### Tools (via Bash)
- `python3 -c "import _env; ..."` — read current `.env` state.

### Files read
- `config/setup-guide.md` — reference for Review LLM keys.
- `.env` — current configuration (read + write).

### Files written
- `.env` — updated with new `LLM_*` keys (via Edit tool).

### No MCP servers, no wiki, no external skills called.
