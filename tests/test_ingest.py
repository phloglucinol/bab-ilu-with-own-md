"""Tests for tools/ingest_runner.py — A2 contract + plan §22 acceptance.

Covers:
- classify_input dispatch across URL / image / video / PDF / markdown / text / unknown
- slug_from_input stability (same input → same slug)
- resolve_output_paths uses lens.entity_model.tier_0 for routing
- journal read/write round-trip + status tracking
- ingest_one partial failure: unknown input type produces ingest.fail record
- ingest_one skips already-succeeded inputs unless --force
- ingest_one preserves user-authored files (no marker → skipped-existing)
- Log append has the `lens` tag for replay
- Lens-awareness: three different lenses route to three different tier_0 dirs
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.ingest_runner import (
    AGENT_MARKER,
    JOURNAL_PATH,
    LOG_PATH,
    append_journal,
    classify_input,
    ingest_one,
    journal_status_for,
    read_journal,
    resolve_output_paths,
    run_ingest,
    slug_from_input,
    slugify,
    write_tier_0_stub,
)


# ---------------------------------------------------------------------------
# FakeLens — minimal stand-in covering the fields ingest_runner reads
# ---------------------------------------------------------------------------


class FakeLens:
    def __init__(
        self,
        lens_id: str = "test-lens",
        *,
        tier_0: str = "aesthetic",
        tier_1_atom: str = "motif",
        tier_1_cluster: str = "panel",
        authority_fields: list[str] | None = None,
    ):
        self.id = lens_id
        self.entity_model = {
            "tier_0": tier_0,
            "tier_1_atom": tier_1_atom,
            "tier_1_cluster": tier_1_cluster,
        }
        if authority_fields is None:
            self.anchors = None
        else:
            self.anchors = {"authority_fields": authority_fields}


# ---------------------------------------------------------------------------
# classify_input
# ---------------------------------------------------------------------------


class TestClassifyInput:

    @pytest.mark.parametrize("raw,expected", [
        ("https://example.com/foo", "url"),
        ("http://example.com", "url"),
        ("/path/to/pic.jpg", "image"),
        ("pic.PNG", "image"),
        ("clip.mp4", "video"),
        ("doc.pdf", "pdf"),
        ("note.md", "markdown"),
        ("transcript.txt", "text"),
        ("readme.html", "text"),
        ("no-extension", "unknown"),
        ("weird.xyz", "unknown"),
    ])
    def test_classify(self, raw, expected):
        assert classify_input(raw) == expected


class TestSlugify:

    def test_basic(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_chars(self):
        assert slugify("FOO_bar baz!") == "foo-bar-baz"

    def test_empty(self):
        assert slugify("") == "untitled"
        assert slugify("!!!") == "untitled"

    def test_slug_from_url(self):
        s = slug_from_input("https://aws.amazon.com/message/41926/")
        # domain+path are kebabed
        assert "aws-amazon-com" in s

    def test_slug_from_path(self):
        assert slug_from_input("/tmp/foo/Bar Baz.pdf") == "bar-baz"


# ---------------------------------------------------------------------------
# resolve_output_paths — lens-aware routing
# ---------------------------------------------------------------------------


class TestResolveOutputPaths:

    def test_aesthetic_routes_to_aesthetic_dir(self, tmp_path):
        lens = FakeLens(lens_id="aesthetic-warburg",
                        tier_0="aesthetic", tier_1_atom="motif")
        plan = resolve_output_paths(tmp_path, lens, "pic.jpg")
        assert plan.tier_0_path == tmp_path / "wiki" / "aesthetic" / "pic.md"
        assert plan.tier_1_atom_dir == tmp_path / "wiki" / "motif"
        assert plan.slug == "pic"

    def test_engineering_routes_to_incident_dir(self, tmp_path):
        lens = FakeLens(lens_id="engineering-alexander",
                        tier_0="incident", tier_1_atom="pattern")
        plan = resolve_output_paths(
            tmp_path, lens, "https://aws.amazon.com/message/41926/")
        assert plan.tier_0_path.parent == tmp_path / "wiki" / "incident"
        assert plan.tier_1_atom_dir == tmp_path / "wiki" / "pattern"
        assert "aws-amazon-com" in plan.slug

    def test_zettelkasten_routes_to_note_dir(self, tmp_path):
        lens = FakeLens(lens_id="general-zettelkasten",
                        tier_0="note", tier_1_atom="concept")
        plan = resolve_output_paths(tmp_path, lens, "my-note.md")
        assert plan.tier_0_path == tmp_path / "wiki" / "note" / "my-note.md"


# ---------------------------------------------------------------------------
# write_tier_0_stub — frontmatter fidelity + user-edit safety
# ---------------------------------------------------------------------------


class TestWriteTier0Stub:

    def _make_plan(self, tmp_path, lens):
        from tools.ingest_runner import resolve_output_paths
        return resolve_output_paths(tmp_path, lens, "test.jpg")

    def test_writes_with_frontmatter(self, tmp_path):
        lens = FakeLens(authority_fields=["aat_id", "wikidata"])
        plan = self._make_plan(tmp_path, lens)
        wrote, reason = write_tier_0_stub(plan, lens, "test.jpg", "image")
        assert wrote is True
        assert reason == "written"
        body = plan.tier_0_path.read_text(encoding="utf-8")
        assert "type: aesthetic" in body
        assert "lens: test-lens" in body
        assert 'aat_id: ""' in body
        assert 'wikidata: ""' in body
        assert AGENT_MARKER in body

    def test_zettelkasten_omits_anchor_fields(self, tmp_path):
        lens = FakeLens(lens_id="zk", tier_0="note",
                        authority_fields=None)  # None = no anchors block
        plan = self._make_plan(tmp_path, lens)
        write_tier_0_stub(plan, lens, "x.md", "markdown")
        body = plan.tier_0_path.read_text(encoding="utf-8")
        assert "aat_id" not in body
        assert "wikidata" not in body

    def test_skips_user_content_without_marker(self, tmp_path):
        lens = FakeLens()
        plan = self._make_plan(tmp_path, lens)
        plan.tier_0_path.parent.mkdir(parents=True, exist_ok=True)
        plan.tier_0_path.write_text("user's hand-written file", encoding="utf-8")
        wrote, reason = write_tier_0_stub(plan, lens, "x.jpg", "image")
        assert wrote is False
        assert reason == "exists-user-content"
        # User content preserved
        assert plan.tier_0_path.read_text(encoding="utf-8") == "user's hand-written file"

    def test_overwrites_agent_stub_only_with_force(self, tmp_path):
        lens = FakeLens()
        plan = self._make_plan(tmp_path, lens)
        write_tier_0_stub(plan, lens, "x.jpg", "image")
        first = plan.tier_0_path.read_text(encoding="utf-8")
        # Re-run without force → returns False, file unchanged
        wrote, reason = write_tier_0_stub(plan, lens, "x.jpg", "image", force=False)
        assert wrote is False
        assert reason == "exists-agent-stub"
        assert plan.tier_0_path.read_text(encoding="utf-8") == first
        # With force → rewrites
        wrote, reason = write_tier_0_stub(plan, lens, "x.jpg", "image", force=True)
        assert wrote is True


# ---------------------------------------------------------------------------
# Journal read/write/status
# ---------------------------------------------------------------------------


class TestJournal:

    def test_empty_journal_returns_none_status(self, tmp_path):
        journal_path = tmp_path / "journal.jsonl"
        assert read_journal(journal_path) == []
        assert journal_status_for([], "any-input") is None

    def test_append_and_read_roundtrip(self, tmp_path):
        journal_path = tmp_path / "journal.jsonl"
        append_journal(journal_path, {"action": "ingest.start", "input": "a"})
        append_journal(journal_path, {"action": "ingest.success", "input": "a"})
        records = read_journal(journal_path)
        assert len(records) == 2
        assert records[0]["action"] == "ingest.start"
        assert records[1]["action"] == "ingest.success"

    def test_status_returns_latest(self, tmp_path):
        lines = [
            {"action": "ingest.start", "input": "x"},
            {"action": "ingest.fail", "input": "x"},
            {"action": "ingest.start", "input": "x"},
            {"action": "ingest.success", "input": "x"},
        ]
        assert journal_status_for(lines, "x") == "success"
        assert journal_status_for(lines, "other") is None

    def test_corrupt_line_dropped_silently(self, tmp_path):
        journal_path = tmp_path / "journal.jsonl"
        journal_path.parent.mkdir(parents=True, exist_ok=True)
        journal_path.write_text(
            '{"action":"ingest.start","input":"a"}\nNOT VALID JSON\n'
            '{"action":"ingest.success","input":"a"}\n',
            encoding="utf-8",
        )
        records = read_journal(journal_path)
        assert len(records) == 2  # corrupt line dropped


# ---------------------------------------------------------------------------
# ingest_one — end-to-end single-input ingestion
# ---------------------------------------------------------------------------


class TestIngestOne:

    def _make_vault(self, tmp_path: Path) -> Path:
        (tmp_path / "wiki").mkdir()
        return tmp_path

    def test_success_writes_stub_and_records_journal_entry(self, tmp_path):
        vault = self._make_vault(tmp_path)
        lens = FakeLens()
        journal_path = vault / JOURNAL_PATH
        log_path = vault / LOG_PATH
        rec = ingest_one(vault, lens, "test.jpg",
                         journal=[], journal_path=journal_path,
                         log_path=log_path)
        assert rec["action"] == "ingest.success"
        assert rec["input"] == "test.jpg"
        assert rec["outputs"] == ["wiki/aesthetic/test.md"]
        # Stub written
        assert (vault / "wiki" / "aesthetic" / "test.md").exists()
        # Journal has start + success
        records = read_journal(journal_path)
        actions = [r["action"] for r in records]
        assert "ingest.start" in actions
        assert "ingest.success" in actions
        # Log has entry with lens tag
        log_records = read_journal(log_path)
        assert any(r.get("lens") == "test-lens" for r in log_records)

    def test_unknown_type_records_failure(self, tmp_path):
        vault = self._make_vault(tmp_path)
        lens = FakeLens()
        rec = ingest_one(vault, lens, "gibberish",
                         journal=[],
                         journal_path=vault / JOURNAL_PATH,
                         log_path=vault / LOG_PATH)
        assert rec["action"] == "ingest.fail"
        assert "unknown input type" in rec["error"]
        # No file written
        assert not any((vault / "wiki").rglob("gibberish*"))

    def test_skip_when_already_success(self, tmp_path):
        vault = self._make_vault(tmp_path)
        lens = FakeLens()
        prior_journal = [{"action": "ingest.success", "input": "x.jpg"}]
        rec = ingest_one(vault, lens, "x.jpg",
                         journal=prior_journal,
                         journal_path=vault / JOURNAL_PATH,
                         log_path=vault / LOG_PATH)
        assert rec["action"] == "ingest.skip"
        assert rec["reason"] == "already-success"

    def test_force_bypasses_prior_success(self, tmp_path):
        vault = self._make_vault(tmp_path)
        lens = FakeLens()
        # First run succeeds
        ingest_one(vault, lens, "x.jpg", journal=[],
                   journal_path=vault / JOURNAL_PATH,
                   log_path=vault / LOG_PATH)
        # Second run with force re-ingests
        journal = read_journal(vault / JOURNAL_PATH)
        rec = ingest_one(vault, lens, "x.jpg", journal=journal,
                         journal_path=vault / JOURNAL_PATH,
                         log_path=vault / LOG_PATH, force=True)
        assert rec["action"] == "ingest.success"


# ---------------------------------------------------------------------------
# run_ingest — batch orchestration + --retry-failed
# ---------------------------------------------------------------------------


class TestRunIngest:

    def test_batch_mixed_types(self, tmp_path):
        (tmp_path / "wiki").mkdir()
        lens = FakeLens()
        results = run_ingest(tmp_path, lens,
                              ["a.jpg", "b.pdf", "gibberish", "c.mp4"])
        actions = [r["action"] for r in results]
        assert actions.count("ingest.success") == 3
        assert actions.count("ingest.fail") == 1

    def test_retry_failed_skips_successes(self, tmp_path):
        (tmp_path / "wiki").mkdir()
        lens = FakeLens()
        # First batch: 2 succeed, 1 fails
        run_ingest(tmp_path, lens, ["a.jpg", "b.pdf", "gibberish"])
        # Retry-failed: only "gibberish" is retried (and still fails)
        results = run_ingest(tmp_path, lens,
                              ["a.jpg", "b.pdf", "gibberish"],
                              retry_failed=True)
        # Only the failed input was reprocessed
        processed = {r["input"] for r in results}
        assert processed == {"gibberish"}
        assert results[0]["action"] == "ingest.fail"


# ---------------------------------------------------------------------------
# Lens-awareness — three different lenses route three different ways
# ---------------------------------------------------------------------------


class TestLensAwareness:

    def test_same_input_three_lenses_three_output_dirs(self, tmp_path):
        (tmp_path / "wiki").mkdir()
        input_path = "material.md"
        aesthetic = FakeLens(lens_id="aesthetic-warburg", tier_0="aesthetic")
        engineering = FakeLens(lens_id="engineering-alexander", tier_0="incident")
        zettel = FakeLens(lens_id="general-zettelkasten", tier_0="note")

        for lens, expected_dir in [
            (aesthetic, "aesthetic"),
            (engineering, "incident"),
            (zettel, "note"),
        ]:
            # Isolate each run in its own vault to avoid journal collision
            sub = tmp_path / f"vault-{lens.id}"
            (sub / "wiki").mkdir(parents=True)
            rec = ingest_one(sub, lens, input_path, journal=[],
                             journal_path=sub / JOURNAL_PATH,
                             log_path=sub / LOG_PATH)
            assert rec["action"] == "ingest.success"
            assert rec["outputs"] == [f"wiki/{expected_dir}/material.md"]
