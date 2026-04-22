"""Tests for tools/lens_evolution/evolver.py — Track L MVP.

Post-refactor (2026-04-21, Phoenix correction): evolver is no longer
an end-to-end Python pipeline. It exposes stage helpers that the
SKILL.md playbook calls. Tests therefore cover:
  - prepare_evolution (stage 1: digest → context)
  - below_threshold (stage gate)
  - format_candidate_for_user (UX output)
  - record_verifier_drop / record_user_rejection /
    record_user_acceptance (feedback-loop side effects)

No LLM calls anywhere. Claude's role is represented by test stubs
that inject pre-authored TheoryCandidate / VerificationResult objects.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.lens_evolution import observer
from tools.lens_evolution.evolver import (
    CONFIDENCE_THRESHOLD,
    EvolutionContext,
    EvolutionOutcome,
    below_threshold,
    format_candidate_for_user,
    prepare_evolution,
    record_user_acceptance,
    record_user_rejection,
    record_verifier_drop,
)
from tools.lens_evolution.matcher import TheoryCandidate
from tools.lens_evolution.operationalizer import OperationalizationResult
from tools.lens_evolution.verifier import VerificationResult


def _candidate(confidence: float = 0.8) -> TheoryCandidate:
    return TheoryCandidate(
        theory_name="Reflection-on-action (Schön)",
        author="Donald A. Schön",
        year=1983,
        primary_source="The Reflective Practitioner",
        core_concept="reflection-on-action",
        why_matches="user's recent entities and queries line up with Schön's layers",
        structural_elements=[
            "knowing-in-action",
            "reflection-in-action",
            "reflection-on-action",
        ],
        confidence=confidence,
    )


class TestPrepareEvolution:

    def test_empty_vault_short_circuits_to_empty_outcome(
        self, tmp_path: Path,
    ):
        ctx = prepare_evolution(tmp_path)
        assert isinstance(ctx, EvolutionContext)
        assert ctx.outcome == EvolutionOutcome.EMPTY_VAULT
        assert ctx.matcher_prompt is None
        assert "No behavioral events" in ctx.message

    def test_populated_vault_yields_prompt_no_outcome(
        self, tmp_path: Path,
    ):
        observer.record_event(
            tmp_path, "entity_named", "general-zettelkasten",
            {"title": "practice-moment"},
        )
        ctx = prepare_evolution(tmp_path)
        assert ctx.outcome is None  # not short-circuited
        assert ctx.matcher_prompt is not None
        assert len(ctx.matcher_prompt) > 100
        assert "practice-moment" in ctx.matcher_prompt

    def test_prompt_carries_rigor_bar(self, tmp_path: Path):
        observer.record_event(
            tmp_path, "entity_named", "general-zettelkasten",
            {"title": "sample"},
        )
        ctx = prepare_evolution(tmp_path)
        assert ctx.matcher_prompt is not None
        # Warburg-grade rigor bar present
        assert ("Warburg" in ctx.matcher_prompt
                or "瓦尔堡" in ctx.matcher_prompt)


class TestBelowThreshold:

    def test_low_confidence_below(self):
        assert below_threshold(_candidate(confidence=0.3)) is True

    def test_high_confidence_above(self):
        assert below_threshold(_candidate(confidence=0.9)) is False

    def test_exact_threshold_not_below(self):
        assert below_threshold(
            _candidate(confidence=CONFIDENCE_THRESHOLD)
        ) is False

    def test_custom_threshold_override(self):
        cand = _candidate(confidence=0.5)
        assert below_threshold(cand, threshold=0.3) is False
        assert below_threshold(cand, threshold=0.7) is True


class TestFormatCandidateForUser:

    def test_output_names_all_citation_pieces(self):
        text = format_candidate_for_user(_candidate())
        assert "Reflection-on-action (Schön)" in text
        assert "Donald A. Schön" in text
        assert "1983" in text
        assert "The Reflective Practitioner" in text
        assert "reflection-on-action" in text

    def test_output_lists_structural_elements(self):
        text = format_candidate_for_user(_candidate())
        for elem in ("knowing-in-action", "reflection-in-action",
                     "reflection-on-action"):
            assert elem in text


class TestFeedbackRecording:

    def test_verifier_drop_records_reject_event(self, tmp_path: Path):
        verification = VerificationResult(
            status="uncertain",
            reasoning="not sure about year",
            raw_response="",
        )
        record_verifier_drop(
            tmp_path, _candidate(), verification,
            lens_override="general-zettelkasten",
        )
        digest = observer.load_digest(tmp_path)
        assert len(digest.rejected_hypotheses) == 1
        assert "verifier-uncertain" in digest.rejected_hypotheses[0]["reason"]

    def test_user_rejection_records_reason(self, tmp_path: Path):
        record_user_rejection(
            tmp_path, _candidate(),
            reason="already familiar with Schön",
            lens_override="general-zettelkasten",
        )
        digest = observer.load_digest(tmp_path)
        assert len(digest.rejected_hypotheses) == 1
        assert "already familiar" in digest.rejected_hypotheses[0]["reason"]

    def test_user_rejection_empty_reason_gets_default(
        self, tmp_path: Path,
    ):
        record_user_rejection(
            tmp_path, _candidate(), reason="",
            lens_override="general-zettelkasten",
        )
        digest = observer.load_digest(tmp_path)
        assert digest.rejected_hypotheses[0]["reason"] == "user-rejected"

    def test_user_acceptance_records_accept_event(self, tmp_path: Path):
        op_result = OperationalizationResult(
            lens_id="schon-reflection-on-action",
            lens_dir=tmp_path / ".agent/lenses/schon-reflection-on-action",
            files_written=(),
        )
        record_user_acceptance(
            tmp_path, _candidate(), op_result,
            lens_override="general-zettelkasten",
        )
        digest = observer.load_digest(tmp_path)
        assert len(digest.accepted_hypotheses) == 1
        assert "Schön" in digest.accepted_hypotheses[0]["theory"]
