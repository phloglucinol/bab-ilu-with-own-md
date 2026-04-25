---
name: wx2md-worker
description: Capture a WeChat Official Account article into raw/articles/*.md via the public wx2md-worker service. Use this whenever the user mentions mp.weixin.qq.com links, WeChat articles, wx2md, or wants a WeChat article preserved into raw/ as Markdown even if direct fetch is blocked locally.
---

# /wx2md-worker — WeChat article to raw Markdown via worker

`/wx2md-worker` (Codex: `$wx2md-worker`) is a WeChat-specific raw capture
entrypoint. It is the only Bab-ilu remote-article capture skill currently
shipped: it exists for `mp.weixin.qq.com` links that should be converted into
Markdown through the worker-backed path and written to
`raw/articles/<slug>.md`.

## When To Use

Use this skill when:

- the input is a WeChat Official Account article link
- the user explicitly mentions `wx2md-worker`
- the user wants a WeChat article saved to `raw/` as Markdown
- direct fetch is blocked by WeChat verification and Codex should use the
  worker-backed capture path

Do not use this for generic non-WeChat URLs. Bab-ilu currently ships no generic
remote-article capture skill.

## Implementation

This skill relies on the helper implemented in `tools/wx2md_worker.py`:

```python
from pathlib import Path
from tools.wx2md_worker import materialize_wechat_via_worker

result = materialize_wechat_via_worker("<wechat-url>", vault=Path("."))
print(result.status, result.output_path)
```

Default worker endpoint:

```text
https://mp.084817.xyz/md?url=<encoded-wechat-url>
```

The helper:

1. sends the WeChat URL to the worker service
2. receives parsed Markdown
3. strips worker-side frontmatter
4. wraps the body in Bab-ilu `raw_article` frontmatter
5. writes `raw/articles/<slug>.md`
6. preserves idempotency and `-v2` conflict behavior

## Output Contract

Successful output is a local file:

```text
raw/articles/<slug>.md
```

with Bab-ilu frontmatter including:

- `type: raw_article`
- `source_url`
- `canonical_url`
- `source_domain`
- `title`
- `extractor: wechat_worker`
- `content_hash`

## Status Handling

Possible result statuses include:

- `captured`
- `unchanged`
- `write_conflict_resolved`
- `unsupported_url`
- `fetch_failed`
- `render_failed`

If the worker returns valid Markdown, the next step remains:

```text
$ingest raw/articles/<slug>.md
```

## Boundaries

- Do not auto-run `$ingest`
- Do not use this for non-WeChat URLs
- Do not overwrite raw evidence silently; keep versioned variants when content
  differs
- Treat the worker as an external dependency: if it fails, surface that failure
  clearly instead of pretending capture succeeded
