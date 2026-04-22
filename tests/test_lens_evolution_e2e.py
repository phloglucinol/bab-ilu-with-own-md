"""End-to-end LENS EVOLUTION integration — simulates Claude's role.

Post-refactor (2026-04-21, Phoenix correction): Python no longer drives
the full pipeline. The SKILL.md playbook orchestrates it, with Claude
performing all LLM reasoning inline. These tests simulate Claude's role
by producing canned responses at each stage, then verifying the Python
tools (prepare → parse_candidate → parse_verification → operationalize
→ record events) wire together correctly.

This test file is the "does it run end-to-end" proof for the Python
side of the contract. Claude's actual reasoning quality is tested via
skill invocation in a real session, not here.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.lens_evolution import observer
from tools.lens_evolution.evolver import (
    EvolutionOutcome,
    below_threshold,
    prepare_evolution,
    record_user_acceptance,
    record_user_rejection,
    record_verifier_drop,
)
from tools.lens_evolution.matcher import (
    TheoryCandidate,
    parse_candidate,
)
from tools.lens_evolution.operationalizer import operationalize
from tools.lens_evolution.verifier import (
    is_accepted,
    parse_verification,
)


# ---------------------------------------------------------------------------
# Canned Claude responses (what Claude would emit given the prompt)
# ---------------------------------------------------------------------------


def _claude_matcher_response() -> str:
    return json.dumps({
        "theory_name": "Reflection-on-action (Schön)",
        "author": "Donald A. Schön",
        "year": 1983,
        "primary_source": "The Reflective Practitioner",
        "core_concept": "reflection-on-action",
        "why_matches": (
            "The user's recent entity 'knowing-in-action' and query "
            "'tacit knowledge in engineering decisions' instantiate "
            "different tiers of Schön's three-layer framework — first "
            "the unreflected practical wisdom, second the in-the-moment "
            "frame-switch."
        ),
        "structural_elements": [
            "knowing-in-action",
            "reflection-in-action",
            "reflection-on-action",
        ],
        "confidence": 0.82,
    })


def _claude_verifier_response(status: str = "confirmed") -> str:
    return json.dumps({
        "status": status,
        "reasoning": {
            "confirmed": (
                "Schön's The Reflective Practitioner (Basic Books, 1983) "
                "is foundational in organizational learning."
            ),
            "uncertain": "could not confirm publisher or year",
            "rejected": "author did not write this book",
        }[status],
    })


CLAUDE_PROMPTS_MD = (
    "## Tone\n"
    "Write with attention to when the practitioner's frame itself becomes visible.\n\n"
    "## Rubrics\n"
    "- Which layer — knowing, in-action reflection, on-action reflection?\n"
    "- What tacit frame was disrupted?\n"
    "- What surprised the practitioner into reflection?\n\n"
    "## Traps\n"
    "- Don't equate post-hoc analysis with reflection-on-action.\n"
    "- Don't treat knowing-in-action as mere intuition.\n"
)

CLAUDE_EXAMPLES_MD = (
    "## Example 1 — debugging session\n\n"
    "The engineer traced a race to a missing debounce. Before this "
    "moment his fix pattern (knowing-in-action) was lock-defensive. "
    "The fix surprised him into reflection-on-action.\n"
)


def _seed_behavior(vault: Path) -> None:
    """Simulate a user who's been working on tacit-knowledge notes."""
    for title in [
        "knowing-in-action", "practice-moments",
        "expert-debounce-intuition", "case-methods",
    ]:
        observer.record_event(
            vault, "entity_named", "general-zettelkasten",
            {"title": title, "slug": title, "tier": "note"},
        )
    for q in [
        "tacit knowledge in engineering decisions",
        "when do experts notice their own assumptions",
    ]:
        observer.record_event(
            vault, "ask_query", "general-zettelkasten",
            {"query": q, "winning_step": "step1_title", "cited_count": 2},
        )


# ---------------------------------------------------------------------------
# End-to-end happy path (simulating Claude in each stage)
# ---------------------------------------------------------------------------


class TestFullPipelineHappyPath:

    def test_empty_vault_short_circuits(self, tmp_path: Path):
        ctx = prepare_evolution(tmp_path)
        assert ctx.outcome == EvolutionOutcome.EMPTY_VAULT

    def test_accept_path_installs_candidate_lens(self, tmp_path: Path):
        # --- Stage 1: prepare ---
        _seed_behavior(tmp_path)
        ctx = prepare_evolution(tmp_path)
        assert ctx.outcome is None  # not short-circuited
        assert ctx.matcher_prompt is not None

        # --- Stage 2: Claude reasons as matcher ---
        candidate = parse_candidate(_claude_matcher_response())
        assert candidate is not None

        # --- Stage 3: threshold gate ---
        assert not below_threshold(candidate)

        # --- Stage 4: Claude reasons as verifier ---
        verification = parse_verification(_claude_verifier_response("confirmed"))
        assert is_accepted(verification)

        # --- Stage 6-7: Claude authors prose; operationalize installs ---
        op_result = operationalize(
            candidate, verification, tmp_path,
            prompts_md=CLAUDE_PROMPTS_MD,
            examples_md=CLAUDE_EXAMPLES_MD,
        )

        # --- Stage 8: record accept event ---
        record_user_acceptance(
            tmp_path, candidate, op_result,
            lens_override="general-zettelkasten",
        )

        # --- Verify final state ---
        assert op_result.lens_id == "schon-knowing-in-action"
        for name in ("lens.yaml", "prompts.md", "examples.md",
                     "candidate.json"):
            assert (op_result.lens_dir / name).exists()

        yaml_text = (op_result.lens_dir / "lens.yaml").read_text()
        assert "schon-knowing-in-action" in yaml_text
        assert "knowing-in-action" in yaml_text

        meta = json.loads(
            (op_result.lens_dir / "candidate.json").read_text()
        )
        assert meta["status"] == "candidate"

        # Closed loop: accept event feeds back to digest
        digest = observer.load_digest(tmp_path)
        assert len(digest.accepted_hypotheses) == 1

    def test_user_rejection_closes_loop(self, tmp_path: Path):
        _seed_behavior(tmp_path)
        ctx = prepare_evolution(tmp_path)
        candidate = parse_candidate(_claude_matcher_response())
        verification = parse_verification(
            _claude_verifier_response("confirmed")
        )

        # User says no
        record_user_rejection(
            tmp_path, candidate, reason="already read Schön",
            lens_override="general-zettelkasten",
        )
        digest = observer.load_digest(tmp_path)
        assert len(digest.rejected_hypotheses) == 1
        assert "already read" in digest.rejected_hypotheses[0]["reason"]


# ---------------------------------------------------------------------------
# Failure paths
# ---------------------------------------------------------------------------


class TestFullPipelineFailures:

    def test_verifier_uncertain_blocks_installation(self, tmp_path: Path):
        _seed_behavior(tmp_path)
        candidate = parse_candidate(_claude_matcher_response())
        verification = parse_verification(
            _claude_verifier_response("uncertain")
        )
        assert not is_accepted(verification)
        # SKILL.md playbook would record the drop:
        record_verifier_drop(
            tmp_path, candidate, verification,
            lens_override="general-zettelkasten",
        )
        # No lens dir should exist
        lens_dir = (
            tmp_path / ".agent/lenses/schon-knowing-in-action"
        )
        assert not lens_dir.exists()
        # And the observer has learned to not re-propose this citation
        digest = observer.load_digest(tmp_path)
        assert len(digest.rejected_hypotheses) == 1
        assert "verifier-uncertain" in digest.rejected_hypotheses[0]["reason"]

    def test_matcher_null_response_yields_no_candidate(
        self, tmp_path: Path,
    ):
        _seed_behavior(tmp_path)
        # Claude correctly declined — null response
        candidate = parse_candidate("null")
        assert candidate is None

    def test_low_confidence_candidate_gets_blocked_at_threshold(
        self, tmp_path: Path,
    ):
        _seed_behavior(tmp_path)
        response = json.dumps({
            "theory_name": "Reflection-on-action (Schön)",
            "author": "Donald A. Schön",
            "year": 1983,
            "primary_source": "The Reflective Practitioner",
            "core_concept": "reflection-on-action",
            "why_matches": "weak match",
            "structural_elements": [
                "knowing-in-action",
                "reflection-in-action",
                "reflection-on-action",
            ],
            "confidence": 0.2,
        })
        candidate = parse_candidate(response)
        assert candidate is not None
        assert below_threshold(candidate) is True
