"""Tests for tools/lens_evolution/verifier.py — Track L MVP.

Verifier is pure prompt + response-parse tooling. Claude (under
SKILL.md) performs the actual citation fact-check. Tests therefore
cover prompt construction and response parsing only — no LLM call.
"""

from __future__ import annotations

import json

import pytest

from tools.lens_evolution.matcher import TheoryCandidate
from tools.lens_evolution.verifier import (
    VerificationResult,
    VerifierError,
    build_verifier_prompt,
    is_accepted,
    parse_verification,
)


def _sample_candidate() -> TheoryCandidate:
    return TheoryCandidate(
        theory_name="Reflection-on-action (Schön)",
        author="Donald A. Schön",
        year=1983,
        primary_source="The Reflective Practitioner",
        core_concept="reflection-on-action",
        why_matches="pattern tracks Schön's three layers",
        structural_elements=["knowing-in-action", "reflection-in-action",
                             "reflection-on-action"],
        confidence=0.82,
    )


class TestBuildVerifierPrompt:

    def test_prompt_contains_bibliographic_fact_check_framing(self):
        prompt = build_verifier_prompt(_sample_candidate())
        assert "reference librarian" in prompt or "fact-check" in prompt
        assert "uncertain" in prompt.lower()
        # Bias toward uncertainty stated explicitly
        assert ("prefer" in prompt.lower() and "uncertain" in prompt.lower())

    def test_prompt_includes_all_four_citation_pieces(self):
        prompt = build_verifier_prompt(_sample_candidate())
        assert "Donald A. Schön" in prompt
        assert "1983" in prompt
        assert "The Reflective Practitioner" in prompt
        assert "reflection-on-action" in prompt

    def test_prompt_tells_verifier_not_to_judge_match_quality(self):
        """The verifier should NOT debate whether the match is tight.
        Only facts about the citation."""
        prompt = build_verifier_prompt(_sample_candidate())
        # 'NOT' used to mark out-of-scope verifier concerns
        assert "NOT asked" in prompt or "not asked" in prompt.lower()


class TestParseVerification:

    def test_parses_confirmed_status(self):
        response = json.dumps({
            "status": "confirmed",
            "reasoning": "Schön 1983 is a standard citation in management "
                         "and organizational-learning textbooks.",
        })
        r = parse_verification(response)
        assert r.status == "confirmed"
        assert "standard" in r.reasoning

    def test_parses_uncertain_status(self):
        response = json.dumps({
            "status": "uncertain",
            "reasoning": "I cannot confidently confirm the year.",
        })
        r = parse_verification(response)
        assert r.status == "uncertain"

    def test_parses_rejected_status(self):
        response = json.dumps({
            "status": "rejected",
            "reasoning": "This book was published in 1983 by Basic Books, "
                         "but its core concept is not 'reflection-on-action' "
                         "— that phrase is Schön 1987 (Educating the "
                         "Reflective Practitioner).",
        })
        r = parse_verification(response)
        assert r.status == "rejected"

    def test_tolerates_json_fence(self):
        wrapped = '```json\n{"status": "confirmed", "reasoning": "ok"}\n```'
        r = parse_verification(wrapped)
        assert r.status == "confirmed"

    def test_rejects_invalid_status(self):
        with pytest.raises(VerifierError, match="status must be one of"):
            parse_verification('{"status": "maybe", "reasoning": "x"}')

    def test_rejects_missing_reasoning(self):
        with pytest.raises(VerifierError):
            parse_verification('{"status": "confirmed"}')

    def test_rejects_empty_reasoning(self):
        with pytest.raises(VerifierError):
            parse_verification(
                '{"status": "confirmed", "reasoning": "   "}'
            )

    def test_rejects_non_json(self):
        with pytest.raises(VerifierError):
            parse_verification("totally not json")


class TestVerifierRoundTrip:
    """Simulates the Claude-driven verifier flow: prompt built, Claude's
    reasoning represented as a string response, parsed into a
    VerificationResult."""

    def test_confirmed_path_accepts(self):
        prompt = build_verifier_prompt(_sample_candidate())
        assert "fact-check" in prompt or "reference librarian" in prompt
        # Claude (under SKILL.md) produces a confirmed response:
        response = json.dumps({
            "status": "confirmed",
            "reasoning": "real work, real author, real year",
        })
        r = parse_verification(response)
        assert is_accepted(r) is True

    def test_uncertain_path_not_accepted(self):
        r = parse_verification(json.dumps({
            "status": "uncertain",
            "reasoning": "not confident about year",
        }))
        assert is_accepted(r) is False

    def test_rejected_path_not_accepted(self):
        r = parse_verification(json.dumps({
            "status": "rejected",
            "reasoning": "author wrote no such book",
        }))
        assert is_accepted(r) is False

    def test_uncertain_is_valid_parse(self):
        """The verifier prompt biases Claude toward uncertain. Verify
        that the parser recognizes uncertain as a first-class output
        (not an error path)."""
        r = parse_verification(
            '{"status": "uncertain", "reasoning": "default bias"}'
        )
        assert r.status == "uncertain"
        assert not is_accepted(r)
