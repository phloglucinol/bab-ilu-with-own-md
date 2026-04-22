"""Tests for tools/ask_runner.py — R1 Sprint 3.

Covers the SKILL.md 6-step retrieval order, short-circuit behaviour, lens
preamble injection for all three shipped lenses, lens-boundary errors,
idempotency, and journal integration.

Tests materialize a tiny vault under `tmp_path` by copying the repo's real
lens configs into `<tmp>/.agent/lenses/<id>/lens.yaml` — exercising the
real `load_lens` rather than a FakeLens. The only I/O fakes are the
`BABILU_LENS_PROMPTS_PATH` env var and tmp-path markdown files.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from tools import lens_context
from tools.ask_runner import (
    AskResult,
    AskRunnerError,
    JOURNAL_PATH,
    parse_frontmatter,
    run_ask,
)

REPO_ROOT = Path(__file__).parent.parent
REAL_LENSES = REPO_ROOT / ".agent" / "lenses"


# ---------------------------------------------------------------------------
# Vault fixture helpers
# ---------------------------------------------------------------------------


def _copy_lenses(tmp_vault: Path, active_id: str) -> Path:
    """Copy repo lens dirs into `<tmp>/.agent/lenses/` + set `active/`.

    Returns the lenses_base path (useful when run_ask needs an explicit
    override).
    """
    dst = tmp_vault / ".agent" / "lenses"
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copy(REAL_LENSES / "schema.json", dst / "schema.json")
    for lens_id in ("aesthetic-warburg", "engineering-alexander",
                    "general-zettelkasten"):
        src = REAL_LENSES / lens_id
        shutil.copytree(src, dst / lens_id)
    active = dst / "active"
    active.mkdir(exist_ok=True)
    shutil.copy(dst / active_id / "lens.yaml", active / "lens.yaml")
    return dst


def _write_md(path: Path, frontmatter: dict, body: str = "") -> None:
    """Emit a tiny YAML frontmatter + body at `path`."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---"]
    for k, v in frontmatter.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    lines.append(body)
    path.write_text("\n".join(lines), encoding="utf-8")


@pytest.fixture
def aesthetic_vault(tmp_path: Path) -> Path:
    _copy_lenses(tmp_path, "aesthetic-warburg")
    # Sparse skeleton: caller adds files as needed per test.
    return tmp_path


@pytest.fixture
def engineering_vault(tmp_path: Path) -> Path:
    _copy_lenses(tmp_path, "engineering-alexander")
    return tmp_path


@pytest.fixture
def zettel_vault(tmp_path: Path) -> Path:
    _copy_lenses(tmp_path, "general-zettelkasten")
    return tmp_path


@pytest.fixture(autouse=True)
def _clear_prompts_cache(monkeypatch):
    """Each test gets a clean lens-context cache + env var."""
    monkeypatch.delenv(lens_context.ENV_OVERRIDE_KEY, raising=False)
    lens_context.clear_cache()
    yield
    lens_context.clear_cache()


def _set_prompts_fixture(monkeypatch, tmp_path: Path, text: str) -> Path:
    """Write a prompts.md fixture and point the env var at it."""
    p = tmp_path / "fixture-prompts.md"
    p.write_text(text, encoding="utf-8")
    monkeypatch.setenv(lens_context.ENV_OVERRIDE_KEY, str(p))
    lens_context.clear_cache()
    return p


# ---------------------------------------------------------------------------
# parse_frontmatter — spot-check the vendored parser
# ---------------------------------------------------------------------------


class TestParseFrontmatter:

    def test_basic_kv(self):
        fm, body = parse_frontmatter("---\ntitle: Hello\n---\nbody here")
        assert fm == {"title": "Hello"}
        assert body == "body here"

    def test_inline_list(self):
        fm, _ = parse_frontmatter("---\naliases: [a, b, c]\n---\n")
        assert fm["aliases"] == ["a", "b", "c"]

    def test_block_list(self):
        fm, _ = parse_frontmatter(
            "---\naliases:\n  - zone\n  - stalker\n---\n"
        )
        assert fm["aliases"] == ["zone", "stalker"]

    def test_no_frontmatter(self):
        fm, body = parse_frontmatter("just body text")
        assert fm == {}
        assert body == "just body text"


# ---------------------------------------------------------------------------
# Retrieval steps 1-6 in isolation
# ---------------------------------------------------------------------------


class TestRetrievalSteps:

    def test_step1_title_match(self, aesthetic_vault: Path):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "stalker-zone.md",
            {"title": "Stalker Zone", "lens": "aesthetic-warburg"},
            body="Tarkovsky's film.",
        )
        result = run_ask("Stalker Zone", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step1_title"
        assert result.sources[0]["title"] == "Stalker Zone"

    def test_step2_alias_match(self, aesthetic_vault: Path):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "stalker-zone.md",
            {"title": "Stalker Zone",
             "aliases": ["zone", "the-zone"],
             "lens": "aesthetic-warburg"},
            body="No matching body phrase.",
        )
        result = run_ask("zone", aesthetic_vault, lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step2_aliases"

    def test_step3_original_terms_match(self, aesthetic_vault: Path):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "stalker-zone.md",
            {"title": "Stalker Zone",
             "original_terms": ["潜行者"],
             "lens": "aesthetic-warburg"},
            body="No english body phrase here.",
        )
        result = run_ask("潜行者", aesthetic_vault, lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step3_original_terms"

    def test_step4_a4_candidate_match(self, aesthetic_vault: Path):
        # gap_runner writes panel-candidates.md (cluster=panel for aesthetic)
        todos = aesthetic_vault / ".agent" / "todos"
        todos.mkdir(parents=True, exist_ok=True)
        (todos / "panel-candidates.md").write_text(
            "# panel candidates\n\n- Sublime Solitude (3 motifs)\n",
            encoding="utf-8",
        )
        result = run_ask("Sublime Solitude", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step4_a4_candidates"

    def test_step4_heading_is_not_false_positive(self, aesthetic_vault: Path):
        """A heading like `# Panel Candidates` must not match query `panel`.

        Regression guard: earlier implementation did a substring scan over
        the entire file, so the heading itself tripped the match. Only
        bullet list items (the real candidates) should be considered.
        """
        todos = aesthetic_vault / ".agent" / "todos"
        todos.mkdir(parents=True, exist_ok=True)
        (todos / "panel-candidates.md").write_text(
            "# Panel Candidates\n\n"
            "- Sublime Solitude (3 motifs)\n"
            "- Mirror Study (2 motifs)\n",
            encoding="utf-8",
        )
        # Also add a title-only entry so step1 stays empty for "panel"
        result = run_ask("panel", aesthetic_vault, lens="aesthetic-warburg")
        # Must NOT match via step4 — heading-only mention is not a candidate
        step4_hits = [s for s in result.sources
                      if s["step"] == "step4_a4_candidates"]
        assert step4_hits == []

    def test_step5_question_stub_match(self, aesthetic_vault: Path):
        qdir = aesthetic_vault / "wiki" / "questions"
        _write_md(
            qdir / "does-bridge-exist.md",
            {"title": "Does x bridge y?"},
            body="Open question: does the mirror motif bridge Warburg panels?",
        )
        result = run_ask("mirror motif", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step5_questions"

    def test_step6_grep_body_fallback(self, aesthetic_vault: Path):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "some-entry.md",
            {"title": "Some Entry", "lens": "aesthetic-warburg"},
            body="Body contains uniquephrase42 somewhere inside.",
        )
        result = run_ask("uniquephrase42", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step6_grep_body"
        assert "uniquephrase42" in result.sources[0]["snippet"]

    def test_no_match_returns_empty_sources(self, aesthetic_vault: Path):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="completely unrelated content",
        )
        result = run_ask("nonexistent query xyz", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert result.sources == ()
        assert "no vault entries matched" in result.answer

    def test_short_circuit_higher_priority_wins(self, aesthetic_vault: Path):
        # Title hit AND body hit on same term — step 1 must win.
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "winner.md",
            {"title": "Winner", "lens": "aesthetic-warburg"},
            body="does not contain the target",
        )
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "loser.md",
            {"title": "Loser", "lens": "aesthetic-warburg"},
            body="The body has winner buried inside.",
        )
        result = run_ask("Winner", aesthetic_vault, lens="aesthetic-warburg")
        # Exactly one match from step 1
        assert all(s["step"] == "step1_title" for s in result.sources)
        # Trace should show step 6 not attempted
        trace_by_name = {t["step_name"]: t for t in result.retrieval_trace}
        assert trace_by_name["step1_title"]["attempted"] is True
        assert trace_by_name["step6_grep_body"]["attempted"] is False


# ---------------------------------------------------------------------------
# Lens preamble injection — all 3 lenses
# ---------------------------------------------------------------------------


class TestLensPreamble:

    def test_aesthetic_preamble_injected(self, aesthetic_vault: Path,
                                          monkeypatch, tmp_path: Path):
        _set_prompts_fixture(
            monkeypatch, tmp_path,
            "# aesthetic-warburg prompts\nPathosformel rules apply.",
        )
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )
        result = run_ask("Foo", aesthetic_vault, lens="aesthetic-warburg")
        assert "<lens-context>" in result.answer
        assert "Pathosformel" in result.answer

    def test_engineering_preamble_injected(self, engineering_vault: Path,
                                            monkeypatch, tmp_path: Path):
        _set_prompts_fixture(
            monkeypatch, tmp_path,
            "# engineering-alexander prompts\nAlexander pattern Context rule.",
        )
        _write_md(
            engineering_vault / "wiki" / "incident" / "foo.md",
            {"title": "Foo", "lens": "engineering-alexander"},
            body="body",
        )
        result = run_ask("Foo", engineering_vault,
                         lens="engineering-alexander")
        assert "<lens-context>" in result.answer
        assert "Alexander pattern" in result.answer

    def test_zettelkasten_preamble_injected(self, zettel_vault: Path,
                                             monkeypatch, tmp_path: Path):
        _set_prompts_fixture(
            monkeypatch, tmp_path,
            "# general-zettelkasten prompts\nAhrens atomic statement rule.",
        )
        _write_md(
            zettel_vault / "wiki" / "note" / "foo.md",
            {"title": "Foo", "lens": "general-zettelkasten"},
            body="body",
        )
        result = run_ask("Foo", zettel_vault, lens="general-zettelkasten")
        assert "<lens-context>" in result.answer
        assert "Ahrens" in result.answer

    def test_missing_prompts_yields_empty_preamble(
        self, aesthetic_vault: Path, monkeypatch, tmp_path: Path,
    ):
        """No prompts.md — answer still rendered, no <lens-context> block."""
        missing = tmp_path / "does-not-exist.md"
        monkeypatch.setenv(lens_context.ENV_OVERRIDE_KEY, str(missing))
        lens_context.clear_cache()
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )
        result = run_ask("Foo", aesthetic_vault, lens="aesthetic-warburg")
        assert "<lens-context>" not in result.answer


# ---------------------------------------------------------------------------
# Lens boundary + error handling
# ---------------------------------------------------------------------------


class TestLensBoundary:

    def test_invalid_lens_raises_askrunnererror(self, aesthetic_vault: Path):
        with pytest.raises(AskRunnerError) as exc_info:
            run_ask("anything", aesthetic_vault, lens="nonexistent-lens-id")
        assert "nonexistent-lens-id" in str(exc_info.value)

    def test_no_active_lens_raises(self, tmp_path: Path):
        # No .agent/lenses at all + nonexistent lenses_base
        bogus_base = tmp_path / "no-lenses"
        with pytest.raises(AskRunnerError):
            run_ask("q", tmp_path, lenses_base=bogus_base)

    def test_empty_query_raises_valueerror(self, aesthetic_vault: Path):
        with pytest.raises(ValueError):
            run_ask("   ", aesthetic_vault, lens="aesthetic-warburg")

    def test_null_byte_query_raises_valueerror(self, aesthetic_vault: Path):
        """Defence in depth: null bytes are not valid in query strings and
        could mask path / log content downstream. Reject at the boundary."""
        with pytest.raises(ValueError, match="null byte"):
            run_ask("hello\x00world", aesthetic_vault,
                    lens="aesthetic-warburg")

    def test_lens_filter_excludes_other_lens_entries(
        self, aesthetic_vault: Path,
    ):
        # Entry tagged with a different lens is NOT returned for step 1
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "cross-lens.md",
            {"title": "Shared", "lens": "engineering-alexander"},
            body="body",
        )
        result = run_ask("Shared", aesthetic_vault, lens="aesthetic-warburg")
        # Nothing matches under aesthetic-warburg
        assert result.sources == ()


# ---------------------------------------------------------------------------
# Idempotency + journal
# ---------------------------------------------------------------------------


class TestIdempotencyAndJournal:

    def test_same_query_twice_returns_equal_sources(
        self, aesthetic_vault: Path,
    ):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )
        r1 = run_ask("Foo", aesthetic_vault, lens="aesthetic-warburg")
        r2 = run_ask("Foo", aesthetic_vault, lens="aesthetic-warburg")
        assert r1.sources == r2.sources
        assert r1.retrieval_trace == r2.retrieval_trace

    def test_journal_entry_appended_with_lens_tag(
        self, aesthetic_vault: Path,
    ):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )
        run_ask("Foo", aesthetic_vault, lens="aesthetic-warburg")
        journal_path = aesthetic_vault / JOURNAL_PATH
        assert journal_path.exists()
        lines = [
            json.loads(line)
            for line in journal_path.read_text().splitlines()
            if line.strip()
        ]
        ask_entries = [r for r in lines if r.get("action") == "ask"]
        assert len(ask_entries) == 1
        entry = ask_entries[0]
        assert entry["lens"] == "aesthetic-warburg"
        assert entry["query"] == "Foo"
        assert entry["cited_count"] == 1
        assert entry["step"] == "step1_title"

    def test_journal_records_no_match_with_step_sentinel(
        self, aesthetic_vault: Path,
    ):
        run_ask("nothing matches", aesthetic_vault, lens="aesthetic-warburg")
        journal_path = aesthetic_vault / JOURNAL_PATH
        lines = [
            json.loads(line)
            for line in journal_path.read_text().splitlines()
            if line.strip()
        ]
        assert len(lines) == 1
        assert lines[0]["step"] == "no_match"
        assert lines[0]["cited_count"] == 0

    def test_journal_append_uses_lock_and_preserves_jsonl(
        self, aesthetic_vault: Path,
    ):
        """Two sequential run_ask calls must produce exactly two well-formed
        JSONL lines on the journal. This exercises the fcntl.flock path
        end-to-end — the lock is acquired and released without corrupting
        the file, and each line round-trips through json.loads cleanly.
        """
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )
        run_ask("Foo", aesthetic_vault, lens="aesthetic-warburg")
        run_ask("Foo", aesthetic_vault, lens="aesthetic-warburg")
        journal_path = aesthetic_vault / JOURNAL_PATH
        raw_lines = [
            line for line in journal_path.read_text().splitlines()
            if line.strip()
        ]
        assert len(raw_lines) == 2
        # Each line must be valid JSON on its own
        parsed = [json.loads(line) for line in raw_lines]
        assert all(p["action"] == "ask" for p in parsed)
        assert all(p["lens"] == "aesthetic-warburg" for p in parsed)

    def test_askresult_is_frozen(self, aesthetic_vault: Path):
        result = run_ask("anything", aesthetic_vault, lens="aesthetic-warburg")
        assert isinstance(result, AskResult)
        with pytest.raises(Exception):
            # Frozen dataclass: assigning raises FrozenInstanceError
            result.answer = "mutated"  # type: ignore[misc]


# ---------------------------------------------------------------------------
# Retrieval trace shape — helps debugging and satisfies contract
# ---------------------------------------------------------------------------


class TestRetrievalTrace:

    def test_trace_has_all_seven_steps(self, aesthetic_vault: Path):
        """Step 0 (syntheses) was added in K1 per PRD §0.5.4 Karpathy
        inheritance ledger: filed-back answers take retrieval priority
        over raw entries so the wiki compounds across sessions."""
        result = run_ask("anything", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.retrieval_trace) == 7
        names = [t["step_name"] for t in result.retrieval_trace]
        assert names == [
            "step0_syntheses",
            "step1_title", "step2_aliases", "step3_original_terms",
            "step4_a4_candidates", "step5_questions", "step6_grep_body",
        ]

    def test_trace_marks_lower_steps_not_attempted_after_win(
        self, aesthetic_vault: Path,
    ):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )
        result = run_ask("Foo", aesthetic_vault, lens="aesthetic-warburg")
        trace = result.retrieval_trace
        # step0 attempted but no syntheses exist → match_count 0
        assert trace[0]["step_name"] == "step0_syntheses"
        assert trace[0]["attempted"] is True
        assert trace[0]["match_count"] == 0
        # step1 wins on title match
        assert trace[1]["step_name"] == "step1_title"
        assert trace[1]["attempted"] is True
        assert trace[1]["match_count"] >= 1
        # steps 2-6 skipped
        for t in trace[2:]:
            assert t["attempted"] is False


# ---------------------------------------------------------------------------
# K1 · Filed-back syntheses — closes Karpathy's compounding loop
#
# PRD §0.5.4 Karpathy inheritance ledger names /ask filed-back as "未实现"
# in v2.1 and requires Sprint 4 to close the gap. These tests guard that
# the gap stays closed.
# ---------------------------------------------------------------------------


from datetime import date as _date

from tools.ask_runner import (  # noqa: E402
    SYNTHESES_DIRNAME,
    _slugify,
    run_ask_interactive,
    write_synthesis,
)


class TestSlugify:

    def test_lowercase_kebab(self):
        assert _slugify("Hello World") == "hello-world"

    def test_truncates_at_max_len(self):
        long = "a" * 100
        out = _slugify(long, max_len=10)
        assert len(out) <= 10
        assert out == "a" * 10

    def test_non_ascii_collapses_to_hyphens(self):
        # "潜行者 · zone" → non-ASCII + punctuation all collapse; result
        # should contain only the ASCII portion.
        out = _slugify("潜行者 · zone")
        assert out == "zone"

    def test_empty_returns_fallback(self):
        assert _slugify("") == "synthesis"
        assert _slugify("   ") == "synthesis"
        assert _slugify("!!!") == "synthesis"

    def test_trailing_hyphens_stripped(self):
        assert _slugify("Hello!!!") == "hello"

    def test_truncation_strips_trailing_hyphen(self):
        # "ab-cd-ef" truncated at 6 → "ab-cd-" → strip → "ab-cd"
        out = _slugify("ab cd ef", max_len=6)
        assert out == "ab-cd"


class TestWriteSynthesis:

    def _ask_and_write(self, aesthetic_vault: Path, query: str,
                       body_source: str = "Tarkovsky's film.",
                       **kw) -> Path:
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "stalker-zone.md",
            {"title": "Stalker Zone", "lens": "aesthetic-warburg"},
            body=body_source,
        )
        result = run_ask(query, aesthetic_vault, lens="aesthetic-warburg")
        return write_synthesis(result, aesthetic_vault, **kw)

    def test_creates_file_with_correct_frontmatter(
        self, aesthetic_vault: Path,
    ):
        path = self._ask_and_write(aesthetic_vault, "Stalker Zone")
        assert path.exists()
        assert path.parent.name == SYNTHESES_DIRNAME
        fm, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        assert fm["type"] == "synthesis"
        assert fm["question"] == "Stalker Zone"
        assert fm["lens"] == "aesthetic-warburg"
        assert fm["date"] == _date.today().isoformat()
        # cited list recorded; >= 1 because step1 found the entry
        assert isinstance(fm["cited"], list)
        assert len(fm["cited"]) >= 1
        # body carries the answer
        assert "Stalker Zone" in body

    def test_slug_collision_appends_suffix(
        self, aesthetic_vault: Path,
    ):
        path1 = self._ask_and_write(aesthetic_vault, "Stalker Zone")
        path2 = self._ask_and_write(aesthetic_vault, "Stalker Zone")
        assert path1 != path2
        assert path1.stem == "stalker-zone"
        assert path2.stem == "stalker-zone-2"

    def test_respects_max_char_cap(self, aesthetic_vault: Path):
        # Force a huge answer by making the body snippet long; the actual
        # body cap lives in write_synthesis, so build a synthetic result
        # and bypass run_ask.
        from tools.ask_runner import _SYNTHESIS_MAX_CHARS
        huge_answer = "A" * (_SYNTHESIS_MAX_CHARS + 500)
        result = AskResult(
            answer=huge_answer,
            sources=(),
            retrieval_trace=(),
            lens="aesthetic-warburg",
            query="big",
        )
        path = write_synthesis(result, aesthetic_vault)
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        assert fm.get("truncated") in ("true", True)
        assert "[truncated]" in body
        assert len(body) < len(huge_answer)

    def test_custom_title_used_when_provided(
        self, aesthetic_vault: Path,
    ):
        path = self._ask_and_write(
            aesthetic_vault, "Stalker Zone",
            custom_title="Tarkovsky's Zone and Threshold Crossings",
        )
        assert "tarkovsky" in path.stem
        fm, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        assert fm["title"] == "Tarkovsky's Zone and Threshold Crossings"
        # Original question preserved in frontmatter even with custom title
        assert fm["question"] == "Stalker Zone"

    def test_cold_start_empty_sources_still_writes(
        self, aesthetic_vault: Path,
    ):
        """A synthesis of a no-match answer is a valid record per K1 audit."""
        result = run_ask("nonexistent-topic", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.sources) == 0
        path = write_synthesis(result, aesthetic_vault)
        fm, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        assert fm["cited"] == []

    def test_lens_field_tracks_active_lens(
        self, engineering_vault: Path,
    ):
        # Under engineering lens, synthesis must record lens=engineering-alexander
        _write_md(
            engineering_vault / "wiki" / "incidents" / "some.md",
            {"title": "Some Incident", "lens": "engineering-alexander"},
            body="body",
        )
        result = run_ask("Some Incident", engineering_vault,
                         lens="engineering-alexander")
        path = write_synthesis(result, engineering_vault)
        fm, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        assert fm["lens"] == "engineering-alexander"


class TestStep0Syntheses:

    def _seed_synthesis(self, vault: Path, lens_id: str, question: str,
                        title: str = "Stored Answer"):
        """Write a pre-existing synthesis to the vault for retrieval tests."""
        syn_dir = vault / "wiki" / SYNTHESES_DIRNAME
        syn_dir.mkdir(parents=True, exist_ok=True)
        (syn_dir / "stored.md").write_text(
            f"---\ntype: synthesis\n"
            f"title: {title}\nquestion: {question}\n"
            f"lens: {lens_id}\n"
            f"date: 2026-04-20\ncited: []\n---\n"
            f"Body of stored synthesis about {question}.\n",
            encoding="utf-8",
        )

    def test_step0_hits_take_priority_over_step1(
        self, aesthetic_vault: Path,
    ):
        # Both an entry titled "Stalker Zone" AND a synthesis for that
        # question exist. Step 0 should win.
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "stalker-zone.md",
            {"title": "Stalker Zone", "lens": "aesthetic-warburg"},
            body="raw entry",
        )
        self._seed_synthesis(
            aesthetic_vault, "aesthetic-warburg", "Stalker Zone",
        )
        result = run_ask("Stalker Zone", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step0_syntheses"

    def test_step0_filters_by_lens(self, aesthetic_vault: Path):
        """A synthesis written under a different lens must NOT be returned."""
        self._seed_synthesis(
            aesthetic_vault, "engineering-alexander", "Cross-lens Query",
        )
        result = run_ask("Cross-lens Query", aesthetic_vault,
                         lens="aesthetic-warburg")
        # No aesthetic entry exists either, so no match
        assert len(result.sources) == 0

    def test_step0_no_syntheses_dir_no_crash(
        self, aesthetic_vault: Path,
    ):
        """Cold vault with no syntheses/ dir must still run cleanly."""
        result = run_ask("anything", aesthetic_vault,
                         lens="aesthetic-warburg")
        # step0 attempted with 0 matches
        trace = result.retrieval_trace
        assert trace[0]["step_name"] == "step0_syntheses"
        assert trace[0]["attempted"] is True
        assert trace[0]["match_count"] == 0

    def test_step0_matches_on_question_field(
        self, aesthetic_vault: Path,
    ):
        # Synthesis with a distinct title from the question — matching
        # on `question:` should still succeed.
        self._seed_synthesis(
            aesthetic_vault, "aesthetic-warburg",
            question="Threshold Crossings",
            title="A Long Prose Title",
        )
        result = run_ask("Threshold Crossings", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step0_syntheses"

    def test_step0_substring_match_allowed(
        self, aesthetic_vault: Path,
    ):
        """Per design: substring match on title/question (syntheses are
        bundles, exact match would be too strict)."""
        self._seed_synthesis(
            aesthetic_vault, "aesthetic-warburg",
            question="How do threshold crossings recur in Tarkovsky?",
        )
        result = run_ask("threshold crossings", aesthetic_vault,
                         lens="aesthetic-warburg")
        assert len(result.sources) == 1
        assert result.sources[0]["step"] == "step0_syntheses"


class TestRunAskInteractive:

    def _stub_inputs(self, *replies: str):
        """Return an input_fn that yields successive replies."""
        it = iter(replies)

        def _reader(_prompt: str) -> str:
            return next(it)
        return _reader

    def _capture_outputs(self):
        bucket: list[str] = []
        return bucket, lambda line: bucket.append(str(line))

    def test_accepts_y_writes_synthesis(self, aesthetic_vault: Path):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "stalker-zone.md",
            {"title": "Stalker Zone", "lens": "aesthetic-warburg"},
            body="body",
        )
        outputs, out_fn = self._capture_outputs()
        result, path = run_ask_interactive(
            "Stalker Zone", aesthetic_vault, lens="aesthetic-warburg",
            input_fn=self._stub_inputs("y"), output_fn=out_fn,
        )
        assert path is not None
        assert path.exists()
        assert path.parent.name == SYNTHESES_DIRNAME
        # Output announced the archive
        assert any("archived →" in o for o in outputs)

    def test_accepts_n_skips_write(self, aesthetic_vault: Path):
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "stalker-zone.md",
            {"title": "Stalker Zone", "lens": "aesthetic-warburg"},
            body="body",
        )
        outputs, out_fn = self._capture_outputs()
        result, path = run_ask_interactive(
            "Stalker Zone", aesthetic_vault, lens="aesthetic-warburg",
            input_fn=self._stub_inputs("n"), output_fn=out_fn,
        )
        assert path is None
        syn_dir = aesthetic_vault / "wiki" / SYNTHESES_DIRNAME
        # dir may or may not be auto-created; either way, no file in it
        if syn_dir.exists():
            assert list(syn_dir.glob("*.md")) == []

    def test_empty_reply_defaults_to_yes(self, aesthetic_vault: Path):
        """Empty reply — the (Y/n/edit title) "Y" is the default."""
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )
        _, out_fn = self._capture_outputs()
        _, path = run_ask_interactive(
            "Foo", aesthetic_vault, lens="aesthetic-warburg",
            input_fn=self._stub_inputs(""), output_fn=out_fn,
        )
        assert path is not None
        assert path.exists()

    def test_eof_treated_as_no_archive(self, aesthetic_vault: Path):
        """Non-TTY (piped/scripted) input raises EOFError; must not crash."""
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )

        def _eof(_prompt: str) -> str:
            raise EOFError()

        outputs, out_fn = self._capture_outputs()
        result, path = run_ask_interactive(
            "Foo", aesthetic_vault, lens="aesthetic-warburg",
            input_fn=_eof, output_fn=out_fn,
        )
        assert path is None
        assert any("no tty" in o for o in outputs)

    def test_custom_title_reply_uses_custom_title(
        self, aesthetic_vault: Path,
    ):
        """Any reply other than y/n/empty becomes the custom title."""
        _write_md(
            aesthetic_vault / "wiki" / "aesthetic" / "foo.md",
            {"title": "Foo", "lens": "aesthetic-warburg"},
            body="body",
        )
        _, out_fn = self._capture_outputs()
        _, path = run_ask_interactive(
            "Foo", aesthetic_vault, lens="aesthetic-warburg",
            input_fn=self._stub_inputs("My Custom Bundle Title"),
            output_fn=out_fn,
        )
        assert path is not None
        assert "my-custom-bundle-title" in path.stem
        fm, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        assert fm["title"] == "My Custom Bundle Title"
        # question preserved separately from title
        assert fm["question"] == "Foo"
