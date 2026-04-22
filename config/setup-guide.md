# Bab-ilu — Configuration Guide

> Read by the `/setup` skill. Bab-ilu has a very small configuration
> surface: Claude Code handles its own auth via `claude login`, and one
> optional MCP second-opinion LLM can be wired up if you want
> cross-model review.

---

## How Configuration Works

All optional keys live in the project-root `.env` file (created from
`config/.env.example`). The MCP review server reads `.env` at startup;
Bab-ilu's Python tools and skills do not require any of these keys.

The `/setup` skill checks current state, explains the keys, and writes
values into `.env` using the Edit tool.

---

## Claude Code auth (required, but not via .env)

All Bab-ilu LLM reasoning happens inside the Claude Code session — no
Python-side SDK calls, no outbound Anthropic requests from `tools/`.
Auth is handled by Claude Code itself:

```bash
claude login
```

You do not set `ANTHROPIC_API_KEY` manually. If `claude login` has
succeeded, Bab-ilu is ready to run.

---

## Review LLM (optional — enables cross-model MCP review)

| Field | Value |
|-------|-------|
| `.env` variables | `LLM_API_KEY`, `LLM_BASE_URL`, `LLM_MODEL` |
| Required? | No |
| Free? | Depends on provider |

**What it does**: connects `mcp-servers/llm-review` to a second LLM
(independent of Claude) for adversarial review. The reviewer critiques
artifacts without seeing Claude's prior analysis, improving quality
via genuine independence.

**Without these keys**: the MCP server simply does not start. No
Bab-ilu skill hard-depends on cross-model review.

**Works with any OpenAI-compatible API**:

| Provider | `LLM_BASE_URL` | Example `LLM_MODEL` |
|----------|-------------|-------------------|
| DeepSeek | `https://api.deepseek.com/v1` | `deepseek-chat` |
| OpenAI | `https://api.openai.com/v1` | `gpt-4o` |
| OpenRouter | `https://openrouter.ai/api/v1` | any model slug |
| Qwen (DashScope) | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-max` |
| SiliconFlow | `https://api.siliconflow.cn/v1` | see their docs |
| Local (Ollama) | `http://localhost:11434/v1` | `llama3.2` |

**How to set up**:
1. Get an API key from your chosen provider
2. Set all three `LLM_*` variables in `.env`
3. Restart Claude Code so the MCP server re-reads `.env`

**Optional**: `LLM_FALLBACK_MODEL` — fallback if primary fails
(defaults to `LLM_MODEL`).

---

## Configuration Verification

After setting `LLM_*` keys, verify they are loaded correctly:

```bash
python3 -c "
import os, sys
sys.path.insert(0, 'tools')
try:
    import _env  # loads .env
except Exception:
    pass
for k in ('LLM_API_KEY', 'LLM_BASE_URL', 'LLM_MODEL'):
    v = os.environ.get(k, '')
    print(f'{\"✓ set\" if v else \"✗ unset\"}  {k}')
"
```

After adding `LLM_*` variables, restart Claude Code so the MCP server
picks them up.
