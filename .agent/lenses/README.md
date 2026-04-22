# `.agent/lenses/` — Bab-ilu v2.1 Lens Configurations

Each subdirectory here defines one **lens**: a discipline-specific ontology
scheme that plugs into Bab-ilu's horizontal tools (slash commands, graph
analyzer, vault structure).

## Files

- [`schema.json`](schema.json) — JSON Schema (Draft 07) for `lens.yaml`
  validation. Every lens config must pass this schema.
- `<lens-id>/lens.yaml` — per-lens config. Slug must match directory name.
- `<lens-id>/prompts.md` — lens-specific prompt templates used by `/genesis`
  et al.
- `<lens-id>/examples.md` — worked examples for users learning this lens.
- `<lens-id>/glossary.md` — lens-specific terminology (motif vs force vs note,
  etc.).

## Current lenses (Sprint 2)

- **aesthetic-warburg** — v2.0 default; Pathosformel from motif bundles;
  authority anchors (AAT, Iconclass, Wikidata, ULAN).
- **engineering-alexander** — incidents + forces → patterns → pattern
  languages; IEEE/ACM/RFC authority.
- **general-zettelkasten** *(pending Phoenix approval of `-bloom` suffix per
  PRD §8.1)* — Luhmann-plus-Bloom hybrid; fleeting+permanent notes → indexes.

## Validation

```bash
python -c "
import json, yaml, jsonschema, pathlib
schema = json.load(open('.agent/lenses/schema.json'))
for lens in pathlib.Path('.agent/lenses').glob('*/lens.yaml'):
    cfg = yaml.safe_load(open(lens))
    jsonschema.validate(cfg, schema)
    print(f'OK: {lens}')
"
```

## Adding a new lens

1. Create `<lens-id>/` directory with kebab-case id matching the `id:` field.
2. Copy `aesthetic-warburg/lens.yaml` as a starting template.
3. Adjust `entity_model`, `deliverable_types`, `activation`, `thresholds`,
   `anchors.authority_fields`, `allowed_subdomains`, and
   `analysis_contract` to match your discipline.
4. Run the validation snippet above to confirm schema compliance.
5. Populate the optional files (`prompts.md`, `examples.md`, `glossary.md`).

## Status banner

**Provisional.** B1 schema was materialized by the Ralph loop main agent
using 7 default decisions while Phoenix was unavailable. Clear revert path:
`git revert <commit>` if Phoenix rejects any default.
