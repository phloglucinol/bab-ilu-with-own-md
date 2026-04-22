"""Tests for tools/lens_evolution/observer.py — Track L MVP.

Covers:
  - Record → persist → digest roundtrip
  - Event log append-only contract
  - Digest rebuild from corrupted file
  - Empty vault returns fresh digest (no crash)
  - Recency cap (tail-kept after exceeding window)
  - User accept/reject signals surface to digest
  - Concurrency safety (advisory lock prevents torn lines)
"""

from __future__ import annotations

import json
import threading
from pathlib import Path

import pytest

from tools.lens_evolution.observer import (
    BehavioralEvent,
    DIGEST_PATH,
    EVENT_LOG_PATH,
    ObserverDigest,
    clear_state,
    load_digest,
    rebuild_digest_from_log,
    record_event,
)


# ---------------------------------------------------------------------------
# Core roundtrip
# ---------------------------------------------------------------------------


class TestRecordAndLoad:

    def test_first_event_creates_log_and_digest(self, tmp_path: Path):
        event = record_event(
            tmp_path, "entity_named", "aesthetic-warburg",
            {"slug": "mirror", "title": "Mirror Motif", "tier": "motifs"},
        )
        assert isinstance(event, BehavioralEvent)
        assert (tmp_path / EVENT_LOG_PATH).exists()
        assert (tmp_path / DIGEST_PATH).exists()

        digest = load_digest(tmp_path)
        assert digest.total_events == 1
        assert digest.recent_entity_names == ["Mirror Motif"]

    def test_multiple_events_all_captured(self, tmp_path: Path):
        record_event(tmp_path, "entity_named", "aesthetic-warburg",
                     {"title": "Pathosformel A"})
        record_event(tmp_path, "ask_query", "aesthetic-warburg",
                     {"query": "how does X relate to Y"})
        record_event(tmp_path, "ingest", "aesthetic-warburg",
                     {"raw_type": "image", "slug": "rembrandt-1634"})

        digest = load_digest(tmp_path)
        assert digest.total_events == 3
        assert "Pathosformel A" in digest.recent_entity_names
        assert "how does X relate to Y" in digest.recent_queries
        assert "image" in digest.recent_ingest_types

    def test_event_log_is_append_only(self, tmp_path: Path):
        record_event(tmp_path, "entity_named", "aesthetic-warburg",
                     {"title": "A"})
        record_event(tmp_path, "entity_named", "aesthetic-warburg",
                     {"title": "B"})
        log = (tmp_path / EVENT_LOG_PATH).read_text(encoding="utf-8")
        lines = [l for l in log.splitlines() if l.strip()]
        assert len(lines) == 2
        assert json.loads(lines[0])["data"]["title"] == "A"
        assert json.loads(lines[1])["data"]["title"] == "B"


# ---------------------------------------------------------------------------
# Empty-state safety (principle 3 — never break foreground)
# ---------------------------------------------------------------------------


class TestEmptyState:

    def test_empty_vault_load_returns_fresh_digest(self, tmp_path: Path):
        digest = load_digest(tmp_path)
        assert isinstance(digest, ObserverDigest)
        assert digest.total_events == 0
        assert digest.recent_entity_names == []

    def test_missing_log_but_existing_digest_still_loads(
        self, tmp_path: Path,
    ):
        (tmp_path / DIGEST_PATH).parent.mkdir(parents=True)
        (tmp_path / DIGEST_PATH).write_text(
            json.dumps({"total_events": 5, "recent_entity_names": ["x"]}),
            encoding="utf-8",
        )
        digest = load_digest(tmp_path)
        assert digest.total_events == 5

    def test_corrupted_digest_falls_back_to_log_rebuild(
        self, tmp_path: Path,
    ):
        record_event(tmp_path, "entity_named", "aesthetic-warburg",
                     {"title": "Recoverable"})
        # Now corrupt the digest
        (tmp_path / DIGEST_PATH).write_text("{ broken json",
                                            encoding="utf-8")
        # load_digest must rebuild from log
        digest = load_digest(tmp_path)
        assert "Recoverable" in digest.recent_entity_names


# ---------------------------------------------------------------------------
# Recency cap
# ---------------------------------------------------------------------------


class TestRecencyCaps:

    def test_entity_names_capped_to_recent_tail(self, tmp_path: Path):
        from tools.lens_evolution import observer
        for i in range(observer._RECENT_ENTITY_NAMES_CAP + 10):
            record_event(tmp_path, "entity_named", "aesthetic-warburg",
                         {"title": f"entity-{i}"})
        digest = load_digest(tmp_path)
        assert len(digest.recent_entity_names) == observer._RECENT_ENTITY_NAMES_CAP
        # Tail kept — oldest dropped, newest present
        assert digest.recent_entity_names[0] == "entity-10"
        assert digest.recent_entity_names[-1] == (
            f"entity-{observer._RECENT_ENTITY_NAMES_CAP + 9}"
        )

    def test_queries_and_ingests_also_capped(self, tmp_path: Path):
        from tools.lens_evolution import observer
        for i in range(60):
            record_event(tmp_path, "ask_query", "aesthetic-warburg",
                         {"query": f"q-{i}"})
        digest = load_digest(tmp_path)
        assert len(digest.recent_queries) == observer._RECENT_QUERIES_CAP


# ---------------------------------------------------------------------------
# User feedback signals (accepted/rejected hypotheses in digest)
# ---------------------------------------------------------------------------


class TestFeedbackSignals:

    def test_accepted_hypothesis_surfaces(self, tmp_path: Path):
        record_event(
            tmp_path, "lens_evolution_accept", "general-zettelkasten",
            {"theory": "Schön — reflection-on-action",
             "citation_ref": "Schön 1983 The Reflective Practitioner"},
        )
        digest = load_digest(tmp_path)
        assert len(digest.accepted_hypotheses) == 1
        assert "Schön" in digest.accepted_hypotheses[0]["theory"]

    def test_rejected_hypothesis_surfaces_with_reason(
        self, tmp_path: Path,
    ):
        record_event(
            tmp_path, "lens_evolution_reject", "general-zettelkasten",
            {"theory": "Some pop framework",
             "citation_ref": "Medium blog 2023",
             "reason": "pop-framework-no-academic-backing"},
        )
        digest = load_digest(tmp_path)
        assert len(digest.rejected_hypotheses) == 1
        assert digest.rejected_hypotheses[0]["reason"] == (
            "pop-framework-no-academic-backing"
        )

    def test_accepted_and_rejected_coexist(self, tmp_path: Path):
        record_event(tmp_path, "lens_evolution_accept",
                     "general-zettelkasten",
                     {"theory": "A", "citation_ref": "a"})
        record_event(tmp_path, "lens_evolution_reject",
                     "general-zettelkasten",
                     {"theory": "B", "citation_ref": "b",
                      "reason": "not-rigorous"})
        digest = load_digest(tmp_path)
        assert len(digest.accepted_hypotheses) == 1
        assert len(digest.rejected_hypotheses) == 1


# ---------------------------------------------------------------------------
# Behavioral, not declarative (principle 5)
# ---------------------------------------------------------------------------


class TestBehavioralOnly:

    def test_no_directive_channel_exists(self, tmp_path: Path):
        """There is deliberately no function like 'set_interest_direction'
        or 'bias_observer_toward'. The observer does not accept user
        declarations of interest. This test documents the design as a
        regression guard: if someone adds such an interface the test
        makes them justify it."""
        import tools.lens_evolution.observer as obs
        public = [n for n in dir(obs) if not n.startswith("_")]
        forbidden_substrings = [
            "set_interest", "bias", "prefer_direction",
            "hint_theory", "seed_hypothesis",
        ]
        for name in public:
            for bad in forbidden_substrings:
                assert bad not in name.lower(), (
                    f"Observer has '{name}' — this violates the "
                    "'behavior over declaration' contract. If you genuinely "
                    "need this, update PRD §0.5.3 principle 5 first."
                )


# ---------------------------------------------------------------------------
# Concurrency (flock protects event log)
# ---------------------------------------------------------------------------


class TestConcurrency:

    def test_parallel_record_produces_valid_jsonl(self, tmp_path: Path):
        def spam():
            for i in range(20):
                record_event(tmp_path, "entity_named", "aesthetic-warburg",
                             {"title": f"{threading.current_thread().name}-{i}"})

        threads = [threading.Thread(target=spam, name=f"t{i}")
                   for i in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        log = (tmp_path / EVENT_LOG_PATH).read_text(encoding="utf-8")
        lines = [l for l in log.splitlines() if l.strip()]
        assert len(lines) == 80
        # Every line must parse — no torn writes
        for line in lines:
            rec = json.loads(line)
            assert rec["type"] == "entity_named"


# ---------------------------------------------------------------------------
# Housekeeping
# ---------------------------------------------------------------------------


class TestClearState:

    def test_clear_state_removes_both_files(self, tmp_path: Path):
        record_event(tmp_path, "entity_named", "aesthetic-warburg",
                     {"title": "x"})
        assert (tmp_path / EVENT_LOG_PATH).exists()
        assert (tmp_path / DIGEST_PATH).exists()
        clear_state(tmp_path)
        assert not (tmp_path / EVENT_LOG_PATH).exists()
        assert not (tmp_path / DIGEST_PATH).exists()

    def test_clear_on_empty_vault_no_error(self, tmp_path: Path):
        # Should not raise
        clear_state(tmp_path)
