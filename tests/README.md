# Bab-ilu Test Suite

Inherited from OmegaWiki v0.1.0 via v1.4 fork. **33 test modules, 2,170 tests total.**

## How to run

```bash
# Install deps
pip install -r requirements.txt pytest

# Run default suite (Bab-ilu-relevant tests, 1,842 tests)
pytest

# Run full suite (including upstream OmegaWiki content validation)
pytest -m ""

# Run a specific module
pytest tests/test_research_wiki.py -v
```

## What tests do

| Module | Validates | Portable? |
|---|---|---|
| `test_fetch_arxiv.py` | arXiv URL parsing, ID extraction | ✅ code |
| `test_fetch_s2.py` | Semantic Scholar API wrapper | ✅ code |
| `test_fetch_deepxiv.py` | DeepXiv semantic search wrapper | ✅ code |
| `test_fetch_wikipedia.py` | Wikipedia ingest for /prefill | ✅ code |
| `test_lint.py` | Wiki health checker | ✅ code |
| `test_remote.py` | SSH experiment deployment | ✅ code |
| `test_research_wiki.py` | Core wiki manipulation (slug, log, maturity, graph) | ✅ code |
| `test_reset_wiki.py` | Scoped wiki reset | ✅ code |
| `test_skill_*.py` | Per-skill structural validation | ⚠️ partial |
| `test_skill_validation.py` | CLAUDE.md / schema contract checks | ❌ OmegaWiki-specific |
| `test_shared_references.py` | Cross-skill reference consistency | ❌ OmegaWiki-specific |

## Why some tests fail on Bab-ilu

Tests marked `omegawiki_content` validate that specific *phrases* appear in `CLAUDE.md`
or `<skill>/SKILL.md` files — phrases that are exact text from OmegaWiki upstream.

Bab-ilu intentionally has **different** text (different entity types, different
section headers, different product framing) so these tests fail by design.

They are **excluded by default** via the `not omegawiki_content` filter in `pytest.ini`.

To see them anyway: `pytest -m "" -k validation`

## What passes by default (1,842 / 2,170 = 85%)

- ✅ All `tools/` unit tests (fetch_*, lint, remote, research_wiki, reset_wiki)
- ✅ Skill structure (file exists, frontmatter well-formed, allowed-tools declared)
- ✅ Shared reference integrity (within portable subset)
- ✅ Parametrized field-constraint tests on common entity types

## CI integration

See `.github/workflows/test.yml` (v1.4 pending — todo) for continuous validation.

## Adding Bab-ilu-specific tests

Place new tests in `tests/` and mark OmegaWiki-incompatible ones:

```python
import pytest

@pytest.mark.omegawiki_content
def test_expects_upstream_content():
    """This test validates phrasing only present in upstream OmegaWiki."""
    ...
```
