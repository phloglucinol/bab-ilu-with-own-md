---
name: ingest
description: Lens-aware entry point for any raw material (image / video / URL / PDF / text). Auto-detects type, resolves the output tier_0 directory from the active lens's entity_model, and dispatches to the lens-appropriate downstream skill (aesthetic-warburg → /taste; engineering-alexander → pattern-extraction; general-zettelkasten → note-capture). Supports partial failure with a resume journal. Ontology + log append on every write.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep, WebFetch, Task]
---

# /ingest — Lens-aware ingestion entry point

## Lens awareness (v2.1)

`/ingest` is the universal material intake point for the vault. It does
NOT itself produce deliverables — it classifies and routes. The same
raw input (e.g. a PDF post-mortem) is a tier-0 `incident` under
engineering-alexander but an irrelevant input under aesthetic-warburg
(which wants visual material). The active lens decides.

Runtime wiring (shared by every input type):

1. Resolve the active lens via `tools/lens_loader.load_lens()`; honor
   `--lens <id>` override. Missing lens is fatal (exit 1) — `/ingest`
   refuses to guess tier_0 routing.
2. Inject `tools.lens_context.active_lens_preamble()` at the top of
   every LLM call during classification. The lens's `prompts.md`
   carries judgment rules for what counts as a valid tier-0 source.
3. Route the input based on `lens.entity_model.tier_0` and its declared
   content types. Under aesthetic-warburg, visual content is the
   primary tier_0; under engineering-alexander, post-mortem text
   (HTML/PDF/MD) is primary; under general-zettelkasten, any source is
   valid (books/papers/conversations/videos).
4. Write the tier-0 entry to `wiki/{tier_0}/<slug>.md` with
   lens-appropriate frontmatter (see `docs/lens-spec.md §2.8` for
   authority anchors per lens).
5. Run `tools/ingest_runner.py` for orchestration — the runner owns
   the partial-failure journal at `.agent/state/ingest-journal.jsonl`
   so an interrupted batch can resume without duplicate writes.

### Dispatch table

| Lens                    | Primary input types (tier_0)                           | Downstream                                                              | Output path                                          |
|-------------------------|--------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------|
| `aesthetic-warburg`     | Image, short video, visual panel                       | `/taste` → Panofsky pipeline → Aesthetic MD + optional Warburg panel    | `wiki/aesthetic/<slug>.md` + `wiki/panel/<slug>.md`  |
| `engineering-alexander` | Post-mortem URL, RFC PDF, incident report (HTML/MD)    | Pattern extraction pipeline (scaffolded) → Incident + ≥2 pattern drafts | `wiki/incident/<slug>.md` + `wiki/pattern/<atom>.md` |
| `general-zettelkasten`  | Any source (book, paper, video transcript, URL)        | Note-capture pipeline via `tools/note_extractor.py` → populated tier_0 note, Claude fills Layer 1/2/3 in-session | `wiki/note/<slug>.md` (note_extractor writes tier_0 = "note" per lens.yaml; it does NOT write to `wiki/source/` — that path was in an earlier SKILL.md draft and no code path produced it) |

The aesthetic-warburg path reuses the v2.0 `/taste` pipeline unchanged
(preserved below as the canonical worked example). Engineering and
general modes are scaffolded in v2.1 — `tools/ingest_runner.py`
performs type detection, frontmatter generation, and partial-failure
journaling; the *content extraction* (LLM-driven pattern distillation
or note extraction) is delegated to future per-lens pipelines.

### Authority-anchor scoping

`/ingest` does NOT enforce anchor presence — `/lint --lens=<id>` owns
that check. But `/ingest` populates lens-appropriate anchor fields in
the generated frontmatter when they can be inferred from the source:

- aesthetic-warburg: `aat_id`, `iconclass`, `wikidata` (when resolvable
  via Getty/Wikidata lookup)
- engineering-alexander: `postmortem_url`, `service_name`, `rfc_id`,
  `cve_id` (from URL pattern matching + page metadata)
- general-zettelkasten: no institutional anchors — records only the
  `source_url` or file path in frontmatter

### Partial-failure resume journal

Every `/ingest` run writes one line per input to
`.agent/state/ingest-journal.jsonl`:

```jsonl
{"action": "ingest.start", "input": "<path-or-url>", "lens": "...", "ts": "..."}
{"action": "ingest.success", "input": "...", "outputs": ["wiki/..."], "ts": "..."}
{"action": "ingest.fail", "input": "...", "error": "...", "ts": "..."}
```

On re-invocation, the runner reads the journal, skips completed inputs
(`ingest.success` in journal + output file exists), and retries failed
inputs. Idempotency is enforced by the input path being the journal
key — same URL ingested twice = second call is a no-op.

`--retry-failed` reruns only the inputs with `ingest.fail` in the
journal. `--force` ignores the journal (re-ingests all).

### Log event tagging

Every successful `/ingest` appends to `wiki/_log/usage.jsonl`:

```jsonl
{"action": "ingest", "lens": "engineering-alexander", "input": "...", "outputs": [...], "tier_0_written": 1, "tier_1_atoms_drafted": 3, "ts": "..."}
```

The `lens:` tag is critical — `/taste` diagnostic mode and `/gap`
replay historical ingestions under the correct rubric.

---

## Aesthetic-warburg mode (worked example — legacy v2.0 body)

The remainder of this file documents the aesthetic-warburg
implementation in full. Engineering and zettelkasten modes call
`tools/ingest_runner.py` for type detection + journaling, then delegate
content extraction to their own lens-specific downstream (scaffolded;
`ingest_runner.py` lives in v2.1 but full content-extraction pipelines
are a Sprint 3+ target).

## Input modes

`/ingest` accepts:

1. **No argument** — consumes `raw/images/inbox/` (populated by the `ingest-image` hook when users paste images in chat). With `--panel`, the entire current inbox is processed as one set. This is the canonical user path.
2. A URL: `/ingest https://...` — current v2.2 behavior routes directly into the lens-specific ingest path. For WeChat Official Account links that must be preserved as raw evidence first, run `/wx2md-worker` (Codex: `$wx2md-worker`) and then `/ingest raw/articles/<slug>.md`
3. A path already in `raw/`: `/ingest raw/images/wkw/`
4. A directory of mixed materials: `/ingest raw/images/demo/`
5. Plain text piped in (rare; for ad-hoc notes): `/ingest - < notes.txt`

## Flags

- `--panel` — after per-item ingestion, synthesize or update a Warburg panel covering the set. Relevant when input is a coherent image/video set (e.g. multiple stills from one film, or one designer's portfolio).
- `--domain <domain>` — explicit domain hint, skips `taste-eye`
- `--since <year>` — for URL feeds; pass recency bias
- `--no-distill` — skip L2 cognitive reconstruction even for English sources

## Execution flow

### Step 1 — Resolve input

| Input | Action |
|-------|--------|
| URL | current `/ingest <url>` behavior routes into the lens-specific pipeline rather than providing full raw materialization; for `mp.weixin.qq.com` evidence capture, use `/wx2md-worker` to write `raw/articles/*.md` first |
| Path to directory | enumerate files, bucket by type (image / video / text / pdf) |
| Path to single file | single-item pipeline |

For WeChat Official Account URLs that should be preserved into `raw/articles/`,
use `/wx2md-worker` first. Bab-ilu currently ships no generic remote-article
capture skill for non-WeChat article URLs.

### Step 2 — Dispatch by type

**Visual (image / video)**:
- Delegate to `/taste` (which runs the taste-* subagent chain)
- If `--panel` flag: `/taste` is called once per item, then `taste-synthesis` is asked to produce a panel-level synthesis across all members (or update an existing panel's membership)
- Result: one Aesthetic MD per visual input, plus optional panel updates

**Text (article / paper / transcript)**:
- Detect language
- If non-native and `--no-distill` is not set: run `/distill` to produce native-language knowledge card
- Run the lens-appropriate extraction pass (general-zettelkasten: `concept` / `source` / `person` via `tools/note_extractor.py`; engineering-alexander: `pattern` / `force` / `incident` via `tools/incident_extractor.py`) to extract entities and relations
- Result: entries under `wiki/{domain}/` with proper frontmatter and cross-links

**PDF**:
- Extract text via external PDF tooling (e.g. `pdftotext`), then follow text pipeline

**Mixed directory**:
- Process each file independently
- If `--panel` and ≥3 visuals in the directory: run panel synthesis at end

### Step 3 — Cross-link and index

After writes, run the vault cross-link pass (direct Grep for aliases across `wiki/{tier_0,tier_1_*}/`) to find and add `[[wikilinks]]` for any newly-mentioned entities that already exist in the vault.

Trigger lazy rebuild of `wiki/_index/edges.jsonl`.

### Step 4 — Record usage

Append a line to `wiki/_log/usage.jsonl`:

```jsonl
{"action": "ingest", "input": "<input>", "outputs": ["<wiki-path>", ...], "timestamp": "<ISO-8601>"}
```

### Step 5 — Report

Print to user:
- Input(s) processed
- Entities created (by type)
- Any unresolved AAT/Wikidata IDs surfaced for later `/check`
- Next-step hint if relevant (e.g., "5 images ingested — run `/prompt --panel <slug>` to generate panel-level prompts once member count reaches 5")

## Error handling

- URL fetch fails → log error, skip, do not halt batch
- Image corruption / unreadable → log, skip
- Unknown file type → log with recommendation to user (e.g., ".docx — convert to .pdf or .md first")

## Atomic safety

Every wiki write is atomic (temp file + rename). Frontmatter validated against `schema.md` entity type specs before commit. Per `schema.md §11`.

## Raw preservation

`raw/` is never modified by `/ingest`. Fetched URLs write to `raw/` at ingestion time; subsequent ingestions of the same URL skip re-fetch if the file exists (user can `rm` to force re-fetch).

## Delegation detail

For visual inputs, invoke the Task tool with `subagent_type: "taste-eye"` → `"taste-icon"` → `"taste-lineage"` → `"taste-synthesis"` per the orchestration topology in `schema.md §5.2`.

Claude Code with native subagent support runs these in sequence with shared context. Other agents receive a sequential prompt chain that produces equivalent output.

## Provenance

Forked from OmegaWiki v0.1.0 (skyllwt/OmegaWiki). v2.1 lens-awareness block at top supersedes the legacy v2.0 aesthetic-warburg body, which is preserved below as a worked example pending lens-aware rerouting of PDF/text pipelines in Sprint 3+.
