# Contributing to Bab-ilu

Thank you for your interest in contributing.

## How to contribute

1. **Report bugs**: open an issue with steps to reproduce — ideally the
   vault state, the lens you're running under, and the exact command.
2. **Extend a lens's seed-kit**: add real-world cards (incidents,
   pathosformels, notes) to `seed-kit/<lens>/` with honest wikilinks
   that actually resolve to files in the same tree.
3. **Improve authority anchors** (aesthetic-warburg): if you spot a
   wrong Getty AAT / Iconclass / Wikidata / ULAN ID, submit a PR
   replacing it with a verified value, or mark it `*_uncertainty: []`
   per the lens's uncertainty protocol — never fabricate.
4. **Propose a new lens**: run `/evolve-lens` in your own vault,
   capture the generated candidate lens, and open a PR under
   `.agent/lenses/<id>/` with the matcher + verifier transcripts.
5. **Write tests**: new features ship with pytest tests in `tests/`.

## Development setup

```bash
git clone <repo-url>
cd bab-ilu
bash setup.sh             # installs Python deps, copies .env, links agents
pytest -q                 # current: 662 pass, 420 skipped, 0 failed
```

The skipped count is intentional — v1.4 OmegaWiki-era tests against
surfaces that Bab-ilu has since rewritten. Each skip carries a
`reason=` string pointing to the v2.3 rewrite tracked in
[ROADMAP.md](ROADMAP.md). Do not remove `@pytest.mark.skip` decorators
without first updating the test to the current v2.1+ surface.

If `pytest` reports a *new* failure, that's a regression. If it
reports a *new* skip, the skip reason must be tracked in ROADMAP.

## Code style

- **Python**: PEP 8, type hints, 800-line file max. Public API of
  `tools/` stays Claude-drive — Python owns deterministic IO; the
  invoking Claude Code session owns LLM reasoning. Do not reintroduce
  an `import anthropic` / `ANTHROPIC_API_KEY` path inside `tools/`.
- **Markdown**: YAML frontmatter per `schema.md` contract.
- **Commits**: conventional commits
  (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`).

## Vault content guidelines

Per active lens. Read `.agent/lenses/<id>/prompts.md` and
`.agent/lenses/<id>/examples.md` before authoring content under that
lens — they calibrate tone, judgment rules, and traps.

Cross-cutting rules:
- Never fabricate authority identifiers. If you don't know the real
  ID, mark the field null and list candidates in
  `<field>_uncertainty: []`.
- Every wikilink must resolve, or be explicitly marked as a proposal.
- Respect tier boundaries: `tier_0` is the source-anchored atom,
  `tier_1_atom` is the recurring unit, `tier_1_cluster` requires ≥3
  atoms before promotion.

## Pull request process

1. Fork, branch from `main`.
2. `pytest -q` — no new failures.
3. `python3 tools/quality_gates.py` — no new regressions if it runs.
4. PR description: what + why, with a one-line paste of the before/after
   `pytest` summary and a link to the ROADMAP entry if you're closing
   one.

Small, focused PRs merge faster than bundled rewrites.
