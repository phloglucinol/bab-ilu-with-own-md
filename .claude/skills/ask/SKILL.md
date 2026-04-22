---
name: ask
description: Lens-aware natural-language query over the vault. Injects the active lens's prompts.md + entity_model into the LLM context so answers use lens-appropriate terminology (aesthetic-warburg → Pathosformel vocabulary; engineering-alexander → Alexander pattern vocabulary; general-zettelkasten → Bloom-indexed notes). Read-only; consumes `/gap`'s `.agent/todos/` candidates and `wiki/questions/` stubs when relevant.
allowed-tools: [Read, Glob, Grep]
---

# /ask — Lens-aware vault query

## Lens awareness (v2.1)

`/ask` traverses the same graph every lens writes, but what counts as
a *good answer* varies sharply by lens — aesthetic answers cite
motifs and Panofsky layers, engineering answers cite patterns and
incident cross-refs, zettelkasten answers cite Bloom-indexed notes
and concept-clusters.

Runtime wiring:

1. Resolve the active lens via `tools/lens_loader.load_lens()`; honor
   `--lens <id>` override. Missing lens is fatal.
2. Inject `tools.lens_context.active_lens_preamble()` at the top of
   the answer-synthesis LLM call. This is the single most important
   step — without the lens's judgment rules in context, the synthesis
   falls back to generic "encyclopedia voice" and loses lens identity.
3. Prefer entries whose frontmatter `lens:` field matches the active
   lens id. Cross-lens entries are visible but flagged in the answer
   ("cited from a different lens's index — may not use current
   vocabulary").
4. Use `lens.entity_model` to type search results: "show me all
   tier_1_cluster under active lens" maps to searching the
   `{tier_1_cluster}` type.

### Retrieval order (lens-aware)

For each candidate query term, search in this priority:

0. **`wiki/syntheses/*.md`** — filed-back answers from prior `/ask`
   sessions (K1, Sprint 4). Lens-filtered. Substring match on
   frontmatter `question:` or `title:`. **Highest priority** because
   these are curated bundles representing the wiki's compounding
   knowledge, per Karpathy原教旨 (PRD §0.5.4).
1. Exact title match in frontmatter of `tier_0 / tier_1_atom / tier_1_cluster`
   files under the active lens
2. `aliases:` match
3. `original_terms:` match (bilingual queries)
4. `.agent/todos/<tier_1_cluster>-candidates.md` (A4 gap_runner output;
   unaccepted candidates are still knowledge)
5. `wiki/questions/*.md` (A4 bridge-candidate stubs; open questions
   ARE answers when the asker wants gaps)
6. `grep -i` across markdown body for unique phrases

Steps 4-5 are new in v2.1 — they surface *the system's own
uncertainty* as part of the answer, lens-neutral (every lens benefits
from "here's what we don't know yet").

Step 0 is new in Sprint 4 (K1) — it closes Karpathy's core compounding
loop: "good answers can be filed back into the wiki as new pages...
your explorations compound in the knowledge base just like ingested
sources do." A filed-back synthesis is lens-scoped; a synthesis written
under lens X is invisible under lens Y.

### Filed-back (archive the answer)

After `/ask` returns, the interactive wrapper
(`run_ask_interactive`) asks:

```
Archive as synthesis? (Y/n/edit title):
```

- **Y** (or empty) → writes `wiki/syntheses/<slug>.md` with
  frontmatter `type: synthesis, title, question, lens, date, cited`.
- **n** → returns without writing.
- *any other string* → archives with the string as the custom title
  (the original question is preserved separately in frontmatter).

`EOFError` (non-TTY, piped invocation) is treated as **no archive** —
never fails hard on scripted use. Slug collisions get `-2`, `-3`...
suffixes. Body over 8000 chars is truncated with a `[truncated]` marker.

### Depth × lens interaction

`--depth=hook` under aesthetic-warburg returns the cognitive anchor
sentence; under engineering returns the pattern's Context sentence;
under zettelkasten returns the note's first paragraph (Ahrens's
"atomic statement"). The CLI flag is unchanged; the answer shape
follows the lens.

### Citing format

Wikilinks embed the lens-declared type for reader clarity:

- Aesthetic: `[[aesthetic|stalker-zone-crossing]] (aesthetic-warburg)`
- Engineering: `[[incident|aws-s3-2017-us-east-1]] (engineering-alexander)`
- Zettelkasten: `[[note|atomic-note-principle]] (general-zettelkasten)`

### Cross-lens queries

`/ask --all-lenses <question>` searches across every activated lens's
indices. The answer splits by lens and cites each slice separately,
with a synthesis paragraph if lenses agree (rare — the value is
usually in the disagreement).

### Read-only contract

`/ask` never writes to `wiki/` or `.agent/`. The log update
(`wiki/_log/usage.jsonl`) is lens-tagged:

```jsonl
{"action": "ask", "lens": "aesthetic-warburg", "query": "...",
 "depth": "summary", "cited_count": 5, "ts": "..."}
```

If the user aborts mid-query (Ctrl-C), no log entry appears —
completed interactions only.

---

## Invocation

```
/ask <natural language question>
/ask --depth <hook | summary | full> <question>
/ask --domain <domain> <question>       # restrict scope
```

Default depth: `summary`.

## Depth modes

| Depth | What you get |
|-------|--------------|
| `hook` | One-line "cognitive anchor" per relevant entry — the compressed thesis of that entry. Use for fast orientation across many entries. |
| `summary` | A synthesized answer (~3 paragraphs) citing supporting entries. The default mode. |
| `full` | Full supporting prose from each relevant entry, assembled and annotated. Use when you want the receipts. |

## Execution

### Step 1 — Parse the question

Identify:
- Candidate entity names (proper nouns, quoted terms)
- Relation types implied ("影响了" → `inspired_by`, "是..的实例" → `exemplifies`, etc.)
- Domain hints in the question (e.g., "在电影里..." → domain: cinema)

### Step 2 — Retrieve candidate entries

Use Glob/Grep across `wiki/`. Retrieval order:

1. Exact title match in frontmatter
2. `aliases:` match in frontmatter
3. `original_terms:` match (bilingual queries)
4. `grep -i` across markdown body for unique phrases

Limit first pass to ~20 candidate entries to avoid context overflow.

### Step 3 — Traverse relations

Read `wiki/_index/edges.jsonl` (rebuild lazily if stale — per `schema.md §2.4`). Follow relation edges from candidate entries to find:

- Upstream: what this entry `extends` / `derived_from` / `inspired_by`
- Downstream: what `extends` / `derived_from` / `applies` this entry
- Contradictions and supports
- For aesthetic queries: `exemplifies` edges pointing to Warburg panels; panel member lists

### Step 4 — Synthesize

Compose the answer per depth mode. Always cite specific entries via `[[wikilinks]]`. Never cite without a link.

For aesthetic queries, favor Warburg panels as organizing frames. "Which Aesthetics sit in the 'Sublime Solitude' panel?" should return the panel's members with per-entry one-liners (hook depth) or full iconological summaries (full depth).

### Step 5 — Uncertainty handling

- If no entries match: say so. Suggest related vault domains or a `/ingest` as next step.
- If entries conflict: surface the contradiction. Cite both sides with `[[wikilinks]]`.
- If entries are stale (`freshness_class: volatile` or `dated` with old `last_validated`): flag inline.

## Output format

```
Q: <user's question>

A: <synthesized answer at requested depth>

Sources:
  - [[entry-1]] — <one-line role in the answer>
  - [[entry-2]] — <one-line role>
  ...

Related:
  - [[entry-x]] (might be relevant but not cited)
```

For `hook` depth, replace the synthesized answer with a bulleted list of hooks per matched entry.

## Schema reference

- `schema.md §2` — entity types and relations
- `schema.md §4` — edges.jsonl structure
- PRD §6.3 — example `/ask` flow

## Ground rules

- Never fabricate a wikilink. If an entry does not exist, do not link to it — say "no vault entry for this yet; consider `/ingest`".
- Do not invoke `/taste`, `/ingest`, or other writes during `/ask`. Read-only.
- Do not modify `_log/usage.jsonl` during `/ask` — logging is for write operations.
