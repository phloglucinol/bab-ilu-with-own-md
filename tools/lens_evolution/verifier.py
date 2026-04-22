"""Verifier — prompt construction + response parsing for citation audit.

Architecture contract (per Phoenix 2026-04-21 correction, aligned with
Bab-ilu's Claude Code skill pattern): pure-function helpers. This
module does NOT call any LLM. Claude, running under SKILL.md, is the
LLM and executes the verifier pass after the matcher pass —
deliberately in a FRESH reasoning context (new user turn, different
prompt framing) so confirmation bias across the two passes is reduced.

Why the verifier exists at all:
  Matcher asks Claude "find the best match."
  Verifier asks Claude "is this citation really a real academic work?"
  Different question, different prompt framing, different failure mode
  caught. A single pass can fluently hallucinate a citation; a second
  pass explicitly prompted toward "answer uncertain unless confident"
  catches a meaningful fraction of those hallucinations.

Outcome states:
  confirmed — Claude is confident the work exists and the author-year
              pairing is correct. Candidate advances.
  uncertain — Claude is not confident. Candidate is dropped.
  rejected  — Claude actively believes the citation is wrong
              (e.g. year doesn't match, title garbled, author doesn't
              write on that topic). Candidate is dropped.

In both uncertain and rejected states we drop — the difference is
telemetry (rejected = Claude had a specific contradiction; uncertain =
Claude couldn't decide).
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any

from tools.lens_evolution.matcher import TheoryCandidate

__all__ = [
    "VerificationResult",
    "VerifierError",
    "build_verifier_prompt",
    "parse_verification",
    "is_accepted",
]


@dataclass(frozen=True)
class VerificationResult:
    status: str          # "confirmed" | "uncertain" | "rejected"
    reasoning: str       # 1-3 sentences from the verifier
    raw_response: str    # for audit / debugging

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "reasoning": self.reasoning,
            # raw omitted — too large for persistence; keep in-process only
        }


class VerifierError(Exception):
    """Raised when the verifier LLM returns a malformed response."""


VERIFIER_RIGOR = """\
You are a reference librarian / bibliographic fact-checker. A previous
AI agent proposed that a user's working pattern matches a specific
academic theory, citing a specific primary source. Your ONLY job is
to verify whether that citation refers to a real, well-established
academic work.

You are NOT asked whether the match is insightful. You are NOT asked
whether the theory is a good fit. You are only asked: does this
book/paper exist, written by this author, around this year, focused
on this concept?

CRITICALLY: your default stance is UNCERTAIN, not CONFIRMED. You
should only mark a citation as "confirmed" if you have specific,
stable confidence that:
  - The book/paper is cited in standard disciplinary textbooks
  - The author wrote it around the stated year (±2 years is fine,
    beyond that mark uncertain)
  - The core concept named is genuinely central to that work

If any of the above is not solidly confirmable, return "uncertain".
If you have positive reason to believe the citation is WRONG (e.g.
the author is real but this is not one of their books; the book
exists but wasn't published in that year; the concept named is
not from this work), return "rejected" with the specific contradiction.

Do NOT reason about whether the match is tight or loose. Do NOT
opinionate on the theory's value. Just fact-check the citation.

Prefer "uncertain" 20x over "confirmed" — false confirmations are
far more damaging than false uncertains. A real match that gets
flagged uncertain can be revisited next pass; a hallucinated
citation marked confirmed pollutes the user's vault forever.
"""


VERIFIER_OUTPUT = """\
Return a single JSON object (no prose, no markdown fence):

{
  "status": "confirmed" | "uncertain" | "rejected",
  "reasoning": "<1-3 sentences explaining your conclusion>"
}
"""


def build_verifier_prompt(candidate: TheoryCandidate) -> str:
    """Pure prompt construction. No I/O. No LLM calls."""
    return "\n".join([
        VERIFIER_RIGOR,
        "",
        "CITATION TO VERIFY:",
        f"  author: {candidate.author}",
        f"  year: {candidate.year}",
        f"  primary_source: {candidate.primary_source}",
        f"  core_concept: {candidate.core_concept}",
        f"  theory_name (for context only): {candidate.theory_name}",
        "",
        VERIFIER_OUTPUT,
    ])


_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)
_VALID_STATUSES = frozenset({"confirmed", "uncertain", "rejected"})


def _strip_json_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        lines = t.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        t = "\n".join(lines).strip()
    return t


def parse_verification(response: str) -> VerificationResult:
    text = _strip_json_fence(response).strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        m = _JSON_OBJECT_RE.search(text)
        if not m:
            raise VerifierError(
                f"verifier returned non-JSON: {text[:200]!r}"
            )
        try:
            parsed = json.loads(m.group(0))
        except json.JSONDecodeError as exc:
            raise VerifierError(
                f"verifier embedded malformed JSON: {exc}"
            ) from exc
    if not isinstance(parsed, dict):
        raise VerifierError(f"verifier returned non-object: {parsed!r}")

    status = parsed.get("status")
    reasoning = parsed.get("reasoning")
    if status not in _VALID_STATUSES:
        raise VerifierError(
            f"verifier status must be one of {sorted(_VALID_STATUSES)}, "
            f"got {status!r}"
        )
    if not isinstance(reasoning, str) or not reasoning.strip():
        raise VerifierError("verifier reasoning must be a non-empty string")

    return VerificationResult(
        status=str(status),
        reasoning=str(reasoning).strip(),
        raw_response=response,
    )


# No LLM call lives here. Claude (the Bab-ilu session agent, running
# under .claude/skills/evolve-lens/SKILL.md) runs this pass by:
#
#   1. prompt = build_verifier_prompt(candidate)
#   2. Claude reads the prompt in a FRESH user turn (so the matcher
#      context doesn't leak). Claude produces a JSON response.
#   3. result = parse_verification(response_text)
#   4. if is_accepted(result): proceed; else drop.


def is_accepted(result: VerificationResult) -> bool:
    """Predicate used to decide whether to advance past the verifier gate."""
    return result.status == "confirmed"
