"""Evolver — stage helpers for the Claude-driven /evolve-lens flow.

Architecture contract (per Phoenix 2026-04-21 correction, aligned with
Bab-ilu's Claude Code skill pattern):

  This module does NOT orchestrate an end-to-end pipeline from Python.
  The orchestration happens in `.claude/skills/evolve-lens/SKILL.md` —
  Claude reads the playbook and calls these Python helpers at each stage.
  All LLM reasoning happens in Claude's own turn, inside the current
  Claude Code session, NOT through an API call to another Anthropic
  endpoint.

Stage functions exposed (each one is pure w.r.t. vault state except
where noted):

  prepare_evolution(vault) → EvolutionContext
      Step 1: load the digest; short-circuit to EMPTY_VAULT outcome if
      the user has no behavioral events yet. Otherwise returns a
      context containing the matcher prompt for Claude to read.

  below_threshold(candidate, threshold=None) → bool
      Stage helper: has the matcher's self-confidence cleared the bar?

  record_verifier_drop(vault, candidate, verification, lens_override)
      Stage side-effect: when Claude decides verifier status is not
      'confirmed', this records a reject event into the observer log
      so the next matcher pass does not re-propose this citation.

  record_user_rejection(vault, candidate, reason, lens_override)
      Stage side-effect: when the user says no to a confirmed
      candidate, this records a reject event with the user's reason.

  record_user_acceptance(vault, candidate, op_result, lens_override)
      Stage side-effect: when the user says yes, this records an
      accept event (so the matcher doesn't re-propose) AND is called
      AFTER `operationalize()` has already installed the lens dir.
      This module does not call operationalize directly — Claude does,
      passing prompts.md / examples.md content it authored itself.

Threshold (principle 1 late binding — kept configurable per-call):

  CONFIDENCE_THRESHOLD = 0.60

  Matcher's self-reported confidence < threshold → drop candidate.
  Claude applies this gate via `below_threshold()` in the SKILL.md
  playbook.
"""

from __future__ import annotations

import enum
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from tools.lens_evolution.matcher import (
    TheoryCandidate,
    build_matcher_prompt,
)
from tools.lens_evolution.observer import (
    ObserverDigest,
    load_digest,
    record_event,
)
from tools.lens_evolution.operationalizer import OperationalizationResult
from tools.lens_evolution.verifier import VerificationResult

__all__ = [
    "CONFIDENCE_THRESHOLD",
    "EvolutionOutcome",
    "EvolutionContext",
    "prepare_evolution",
    "below_threshold",
    "format_candidate_for_user",
    "record_verifier_drop",
    "record_user_rejection",
    "record_user_acceptance",
]

CONFIDENCE_THRESHOLD = 0.60


class EvolutionOutcome(str, enum.Enum):
    """Terminal outcomes for a /evolve-lens run.

    Used by the SKILL.md playbook to tag what happened at each
    abortive or successful path.
    """
    EMPTY_VAULT = "empty_vault"
    NO_MATCH = "no_match"
    BELOW_THRESHOLD = "below_threshold"
    FAILED_VERIFICATION = "failed_verification"
    USER_REJECTED = "user_rejected"
    ACCEPTED_AND_INSTALLED = "accepted_and_installed"
    ERROR = "error"


@dataclass(frozen=True)
class EvolutionContext:
    """Stage 1 output: what Claude needs to make a matcher decision.

    `outcome` is populated when the pipeline should short-circuit
    without a matcher prompt — e.g. the digest is empty. Claude checks
    `outcome` first; if set, skip to the final report. If not set,
    the matcher prompt is in `matcher_prompt` and Claude runs the
    matcher stage in its own turn.
    """
    digest: ObserverDigest
    matcher_prompt: Optional[str]
    outcome: Optional[EvolutionOutcome]
    message: str


# ---------------------------------------------------------------------------
# Stage helpers
# ---------------------------------------------------------------------------


def prepare_evolution(vault: Path) -> EvolutionContext:
    """Stage 1: load digest, short-circuit if empty, else produce prompt.

    Claude (under SKILL.md) calls this first. It does NO LLM work —
    it just reads the observer state and builds the prompt text Claude
    will reason over in the next turn.
    """
    digest = load_digest(vault)
    if digest.total_events == 0:
        return EvolutionContext(
            digest=digest,
            matcher_prompt=None,
            outcome=EvolutionOutcome.EMPTY_VAULT,
            message=(
                "No behavioral events recorded yet. "
                "Use the vault — ingest materials, run /ask queries, "
                "name entities — and LENS EVOLUTION will have data to "
                "work on."
            ),
        )
    # Pass vault so build_matcher_prompt auto-discovers installed lenses
    # (pre-installed + previously evolved) and adds them to the
    # "do not re-propose" list. Fix for FTG-test gap 2026-04-21.
    prompt = build_matcher_prompt(digest, vault=vault)
    return EvolutionContext(
        digest=digest,
        matcher_prompt=prompt,
        outcome=None,
        message="matcher prompt ready for Claude's reasoning turn",
    )


def below_threshold(
    candidate: TheoryCandidate,
    threshold: Optional[float] = None,
) -> bool:
    """True when Claude's self-confidence on the candidate is below
    the acceptance gate. SKILL.md playbook uses this to drop a
    low-confidence match without showing it to the user.
    """
    t = CONFIDENCE_THRESHOLD if threshold is None else threshold
    return candidate.confidence < t


def format_candidate_for_user(cand: TheoryCandidate) -> str:
    """Pretty print for terminal presentation. Keeps the four-piece
    citation prominent — the user's eye goes to that first.

    Claude reads this output and shows it to the user as part of the
    accept/reject UI in SKILL.md's playbook.
    """
    lines = [
        "",
        "═══════════════════════════════════════════════════════════════",
        "  LENS EVOLUTION · candidate theory match",
        "═══════════════════════════════════════════════════════════════",
        "",
        f"  THEORY       {cand.theory_name}",
        f"  CITATION     {cand.author} ({cand.year})",
        f"               {cand.primary_source}",
        f"  CORE CONCEPT {cand.core_concept}",
        "",
        "  WHY THIS MATCHES YOUR PRACTICE:",
        f"    {cand.why_matches}",
        "",
        "  STRUCTURAL ELEMENTS (would become entity tiers):",
    ]
    for i, elem in enumerate(cand.structural_elements, 1):
        lines.append(f"    {i}. {elem}")
    lines.extend([
        "",
        f"  Matcher self-confidence: {cand.confidence:.2f}",
        "",
    ])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Feedback event recording — closed-loop glue
# ---------------------------------------------------------------------------


def record_verifier_drop(
    vault: Path,
    candidate: TheoryCandidate,
    verification: VerificationResult,
    lens_override: Optional[str] = None,
) -> None:
    """Called by SKILL.md playbook when Claude's verifier pass produces
    status != 'confirmed'. Records the reject so the next matcher pass
    sees it in the 'do not re-propose' list. Principle 3 (closed-loop
    first) relies on this hook firing — without it the system would
    repropose the same bad citation every call.
    """
    record_event(
        vault, "lens_evolution_reject", lens_override or "unknown",
        {
            "theory": candidate.theory_name,
            "citation_ref": candidate.citation_ref,
            "reason": f"verifier-{verification.status}",
        },
    )


def record_user_rejection(
    vault: Path,
    candidate: TheoryCandidate,
    reason: str,
    lens_override: Optional[str] = None,
) -> None:
    """Called by SKILL.md playbook when the user says no to a verified
    candidate. `reason` is free-form: the user's typed explanation
    (empty string if none). Carried into the matcher's next prompt.
    """
    record_event(
        vault, "lens_evolution_reject", lens_override or "unknown",
        {
            "theory": candidate.theory_name,
            "citation_ref": candidate.citation_ref,
            "reason": reason or "user-rejected",
        },
    )


def record_user_acceptance(
    vault: Path,
    candidate: TheoryCandidate,
    op_result: OperationalizationResult,
    lens_override: Optional[str] = None,
) -> None:
    """Called by SKILL.md playbook AFTER `operationalize()` has written
    the lens dir. Closes the accept half of the feedback loop.
    """
    record_event(
        vault, "lens_evolution_accept", lens_override or "unknown",
        {
            "theory": candidate.theory_name,
            "citation_ref": candidate.citation_ref,
            "lens_id": op_result.lens_id,
        },
    )
