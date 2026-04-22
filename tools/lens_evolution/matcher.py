"""Matcher — prompt-construction and response-parsing tools.

Architecture contract (aligned with Bab-ilu's Claude Code skill pattern,
per Phoenix 2026-04-21 correction): this module is a PURE-FUNCTION
helper. It does not call any LLM. Claude (the current session agent,
running under `.claude/skills/evolve-lens/SKILL.md`) is the LLM. This
module provides:

  - `build_matcher_prompt(digest)` — composes the prompt text Claude
    reads (including the Warburg-grade rigor bar, base-rate calibration,
    academic-laundering refusal list, anti-fluff gates, and the user's
    behavioral digest).
  - `parse_candidate(response_text)` — parses Claude's JSON-format
    response into a `TheoryCandidate` or `None`.
  - `TheoryCandidate` — the immutable result type used by downstream
    operationalizer.

The previous architecture (Python wrapping anthropic SDK, called
`default_llm_callable` + `match_theory`) was an independent-SaaS shape.
Bab-ilu's skills never do that — they run INSIDE a Claude Code session;
the agent doing the reasoning is Claude, not Python-Claude-over-API.

Rigor bar (PRD §0.5.4 — "就像瓦尔堡之于美学那样"):
  - Only theories with PRIMARY academic sources (books/papers)
  - Only theories with AT LEAST 30 years of continuous use OR
    foundational status in a recognized discipline
  - AT LEAST two structural concepts that can be operationalized
    as entity_model tiers (lowered from 3 per architecture audit
    principle 2 — some genuine traditions have only 2 poles)

Exclusion (encoded in the prompt):
  - Pop management frameworks (from business-trade books, HBR articles)
  - TED-talk-level thought frameworks
  - Medium / Substack "mental models"
  - Self-help taxonomies
  - Frameworks whose primary citation is a blog or podcast
  - Academic-laundered pop frameworks (Simon → Design Thinking,
    Aristotle → First Principles, Drucker → OKRs, etc.)

Verifier — this module does NOT self-verify. Its output flows into
`verifier.py` which Claude then applies as an independent second pass.
Keeping verification out of the matcher keeps the matcher's prompt
focused on matching skill, not meta-skepticism.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

from tools.lens_evolution.observer import ObserverDigest

__all__ = [
    "TheoryCandidate",
    "MatcherError",
    "build_matcher_prompt",
    "parse_candidate",
    "discover_installed_lenses",
]


# ---------------------------------------------------------------------------
# Contracts
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TheoryCandidate:
    """A single academic-theory proposal.

    The five-piece citation contract (PRD §0.5.4 discussion with Phoenix):
      author + year + primary_source + core_concept + why_matches.
    Any missing piece invalidates the candidate.
    """
    theory_name: str           # e.g. "Reflection-on-action (Schön)"
    author: str                # "Donald Schön"
    year: int                  # 1983
    primary_source: str        # "The Reflective Practitioner"
    core_concept: str          # "reflection-on-action"
    why_matches: str           # 1-3 sentences connecting practice to theory
    structural_elements: list[str] = field(default_factory=list)
    # structural_elements: 3+ concepts that could become entity tiers
    confidence: float = 0.0    # matcher's self-reported confidence 0-1

    @property
    def citation_ref(self) -> str:
        return f"{self.author} ({self.year}), {self.primary_source}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "theory_name": self.theory_name,
            "author": self.author,
            "year": self.year,
            "primary_source": self.primary_source,
            "core_concept": self.core_concept,
            "why_matches": self.why_matches,
            "structural_elements": list(self.structural_elements),
            "confidence": self.confidence,
            "citation_ref": self.citation_ref,
        }


class MatcherError(Exception):
    """Raised when Claude's response cannot be parsed into a well-formed
    TheoryCandidate. Pure-function concern — no LLM call ever happens
    in this module, so this is strictly a parse-error sentinel."""


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------


# The rigor bar is the single highest-leverage prompt element — everything
# else flows from how tightly it's framed. Kept as a module-level constant
# so multi-agent audits can point at a stable location.
#
# Iteration 2 (2026-04-21) after academic-rigor audit: rewritten around
# null-by-default with explicit base rate, academic-laundering clause,
# and anti-fluff gates on structural_elements + why_matches. Named
# thinker list removed — it was acting as a permissive prime
# ("surely one of these fits"). Replaced with a provenance criterion.
RIGOR_BAR = """\
You are a reference consultant for an academic-grade knowledge tool
called Bab-ilu. You are evaluating whether a user's unselfconscious
working pattern matches a specific academic tradition.

REFERENCE STANDARD: Aby Warburg's Pathosformel for art history.
That is the class of theory the user calibrated their expectation
against — decades-old, primary-source-grounded, structurally
operationalizable. If the theory you are considering is not in that
class, return null. Warburg is not on a whitelist of acceptable
thinkers — it is the floor for what "academic rigor" means to this
user.

BASE RATE CALIBRATION: In typical conditions, the correct output is
`null`. Expect to return `null` in roughly 4 out of 5 cases. Only
return a theory candidate when the user's behavior SPECIFICALLY and
NON-TRIVIALLY instantiates a structural theory from a recognized
humanistic or social-scientific tradition. "Reminds me of" is not a
match. "Is structurally isomorphic to three or more named,
canonically-attested constructs" is a match.

SELF-TEST BEFORE EMITTING A CANDIDATE:
  1. "If I removed the user's behavior digest and just read my
     `why_matches` paragraph, would it still sound plausible?"
     → If yes, your match is generic. Return null.
  2. "Can I name the three structural_elements verbatim from
     memory of the primary source?"
     → If you're paraphrasing or inventing labels, return null.
  3. "Does the primary source actually belong to a recognized
     humanistic or social-scientific discipline whose graduate-level
     syllabi predate 2010?"
     → If the answer is "I'm not sure" or "it depends on the
     syllabus," return null.

ACADEMIC LAUNDERING — THE CENTRAL FAILURE MODE TO AVOID:

You will be tempted to take a pop or business-origin framework and
justify it by citing a legitimate primary source its proponents
invoke. DO NOT DO THIS. Specific patterns to refuse:

  - Citing Herbert Simon (The Sciences of the Artificial, 1969) to
    justify "Design Thinking" — return null.
  - Citing Aristotle (Posterior Analytics) or Descartes (Meditations)
    to justify "First Principles Thinking à la Musk/SpaceX" — return null.
  - Citing Drucker (The Practice of Management, 1954) to justify
    "OKRs" or "Four Disciplines of Execution" — return null.
  - Citing William James (Principles of Psychology, 1890) or BJ Fogg
    to justify "Atomic Habits" / "Tiny Habits" — return null.
  - Citing Senge (The Fifth Discipline, 1990) or Meadows to justify
    "Systems Thinking workshops" — return null.
  - Citing Christensen (The Innovator's Dilemma, 1997) to justify
    "Jobs-to-be-Done" as a working framework — return null.
  - Citing Dweck (Mindset, 2006) if the framework's actual cultural
    provenance is self-help or edu-trade — return null.

If the framework's actual cultural provenance is a business school
press, a TED talk, a management consultancy, an entrepreneur's
memoir, or a self-help trade book — RETURN NULL regardless of what
primary source you could technically attach to it.

ADDITIONAL REFUSALS:

  - A framework whose primary citation is a blog, podcast, or
    business-trade book.
  - A mental-model taxonomy (Shane Parrish / Farnam Street style).
  - An LLM-introduced concept with no pre-2020 academic literature.
  - A "recognized discipline" you are not genuinely confident is
    cited in standard graduate-level curricula.

RECOGNIZED PROVENANCE (inclusive criterion, not a name whitelist):

A theory's provenance counts as recognized academic when ALL hold:
  - It is cited in graduate-level syllabi of at least one humanistic
    or social-scientific discipline (philosophy, sociology, cognitive
    science, art history, anthropology, linguistics, psychology,
    political theory, science-and-technology studies, etc.)
  - Its primary source is a peer-reviewed book/paper, OR a
    pre-peer-review primary text whose discipline still treats it as
    canonical (e.g. Peirce, Wittgenstein, Husserl).
  - The theory has been continuously cited in serious scholarly work
    for at least thirty years from the present date (i.e. primary
    source ≤ 1995 for a tradition still taught today), OR is the
    foundational theory of a recognized discipline.

Return null if you are not solidly confident the candidate satisfies
ALL of the above. Do NOT invent theories. Do NOT hallucinate citations.

Returning null is a PROFESSIONAL RESPONSE. The user has explicitly
calibrated their expectation around null-by-default. A false match
costs much more than a missed match.
"""


OUTPUT_FORMAT = """\
Return a single JSON object (no prose, no markdown fence) matching this
schema. ALL string fields have anti-fluff gates below — a response
that satisfies the schema but not the gates is a failure mode we are
designed to catch. Read the gates CAREFULLY before emitting.

{
  "theory_name": "<tradition name including thinker, e.g. 'Reflection-on-action (Schön)'>",
  "author": "<thinker's full name>",
  "year": <integer year of primary source>,
  "primary_source": "<book or paper title>",
  "core_concept": "<the most load-bearing concept — what the user would read first>",
  "why_matches": "<must cite at least TWO SPECIFIC ITEMS from the behavioral digest (a specific entity name, a specific query phrase, or a specific wikilink edge) and explain how each one instantiates a DIFFERENT structural_element. See gate below.>",
  "structural_elements": ["<concept A>", "<concept B>", "<optionally more>"],
  "confidence": <float 0.0-1.0 — your own assessment of match strength>
}

ANTI-FLUFF GATES (a candidate that violates any of these must return null):

  · `structural_elements`: 2 OR MORE named constructs that all satisfy:
    (a) appear verbatim — or in direct published translation — in the
        primary source,
    (b) are hierarchically or functionally distinct from each other
        (NOT synonyms, NOT three labels for the same concept),
    (c) could each plausibly serve as a different entity tier for a
        user organizing notes under this theory.

    If you cannot name 2 such constructs from memory of the primary
    source — meaning you would have to guess labels or invent them —
    return null. Never pad with invented concepts to hit a count.

    Example OK (Schön): ["knowing-in-action", "reflection-in-action",
    "reflection-on-action"] — three distinct time-phases named
    verbatim in The Reflective Practitioner.

    Example VIOLATES (a) & (b) ("First Principles Thinking"):
    ["premises", "deductions", "conclusions"] — these are just the
    definition of deduction, not three operationalizable tiers.

    Example VIOLATES (b) (Taylor's Sources of the Self if used to
    describe a journaler): ["authenticity", "self-expression",
    "inwardness"] — three synonyms for one gesture.

  · `why_matches`: Must cite AT LEAST TWO specific items from the
    behavioral digest (entity name, query phrase, or wikilink edge)
    and explain how each one instantiates a DIFFERENT entry in
    `structural_elements`. Generic sentences like "the user engages
    in iterative reflection" are DISQUALIFYING. Sentences like "the
    user's entity 'locksmith-tacit-skill' and their query 'can you
    teach reflection-in-action directly' each instantiate different
    structural elements (knowing-in-action and reflection-in-action
    respectively) because the first is a named-skill without explicit
    rules, the second is a question specifically about the in-the-
    moment frame-switch" are acceptable.

    If you cannot cite two specific items from the digest that each
    map to a DIFFERENT structural element, return null. Do not pad
    with generic sentences.

  · `theory_name`: Must name both the tradition and its primary
    thinker (e.g. "Reflection-on-action (Schön)"), never just a bare
    concept ("reflection-on-action"). If you're unsure who gets
    priority citation in the scholarly tradition, return null.

OR, if no theory at the required rigor bar AND anti-fluff gates
matches, return exactly:

  null
"""


def discover_installed_lenses(vault: Optional[Path]) -> list[dict[str, Any]]:
    """Scan `<vault>/.agent/lenses/` for lens directories and extract
    minimal identity (id, name, origin_theory, origin_author).

    Used by `build_matcher_prompt` to automatically populate the
    "DO NOT RE-PROPOSE" list with lenses already installed on this
    vault — covers both pre-installed lenses (shipped with Bab-ilu)
    and previously-evolved candidate lenses. Closes the architecture
    gap found by the FTG test (2026-04-21) where the matcher would
    re-propose an already-installed aesthetic-warburg because the
    observer's accepted_hypotheses only tracked LENS EVOLUTION
    decisions, not pre-installed lenses.

    Returns [] for missing vault, empty dir, or unreadable lens files.
    Never raises — this is a best-effort observation channel.
    """
    if vault is None:
        return []
    lenses_dir = Path(vault) / ".agent" / "lenses"
    if not lenses_dir.is_dir():
        return []
    results: list[dict[str, Any]] = []
    for child in sorted(lenses_dir.iterdir()):
        if not child.is_dir():
            continue
        if child.name in ("active", "schema.json", "__pycache__"):
            # Skip the active-pointer dir and schema file — they're not lenses.
            continue
        lens_yaml = child / "lens.yaml"
        if not lens_yaml.is_file():
            continue
        try:
            import yaml  # local import — only used here
            parsed = yaml.safe_load(lens_yaml.read_text(encoding="utf-8"))
        except Exception:
            # Malformed YAML — skip. Never break the matcher on bad lens file.
            continue
        if not isinstance(parsed, dict):
            continue
        info: dict[str, Any] = {
            "id": parsed.get("id", child.name),
            "name": parsed.get("name", child.name),
        }
        extensions = parsed.get("extensions") or {}
        candidate_meta = (extensions.get("candidate") or {}
                          if isinstance(extensions, dict) else {})
        if candidate_meta.get("origin_theory"):
            info["origin_theory"] = candidate_meta["origin_theory"]
        if candidate_meta.get("origin_author"):
            info["origin_author"] = candidate_meta["origin_author"]
        if candidate_meta.get("origin_year"):
            info["origin_year"] = candidate_meta["origin_year"]
        if candidate_meta.get("origin_source"):
            info["origin_source"] = candidate_meta["origin_source"]
        results.append(info)
    return results


def build_matcher_prompt(
    digest: ObserverDigest,
    *,
    vault: Optional[Path] = None,
) -> str:
    """Compose the full prompt string from digest. Pure — no I/O except
    the optional lens-directory scan when `vault` is provided.

    `vault` enables the "auto-detect installed lenses" path (the
    discover_installed_lenses scan). When omitted, only the observer
    digest's accepted_hypotheses feeds the "do not re-propose" list.
    Tests that care only about prompt content pass vault=None.
    """
    parts: list[str] = [RIGOR_BAR, ""]

    # Installed lenses (pre-installed + previously evolved) —
    # auto-discovered from <vault>/.agent/lenses/, not only from
    # observer.accepted_hypotheses. This closes the FTG-test gap where
    # the matcher would re-propose aesthetic-warburg because it wasn't
    # surfaced through the accept event channel.
    installed = discover_installed_lenses(vault)
    if installed:
        parts.append(
            "ALREADY-INSTALLED LENSES ON THIS VAULT "
            "(do NOT re-propose these — the user already has them):"
        )
        for lens in installed:
            origin = lens.get("origin_theory") or lens.get("name")
            author = lens.get("origin_author", "")
            year = lens.get("origin_year", "")
            source = lens.get("origin_source", "")
            line = f"  - {lens['id']}: {origin}"
            if author and year:
                line += f" [{author} ({year})"
                if source:
                    line += f", {source}"
                line += "]"
            parts.append(line)
        parts.append("")

    # Feedback history — if the user already accepted or rejected
    # theories via LENS EVOLUTION itself, surface them too.
    if digest.accepted_hypotheses:
        parts.append("ALREADY ACCEPTED THEORIES (user adopted these — do NOT re-propose):")
        for a in digest.accepted_hypotheses:
            parts.append(f"  - {a.get('theory', '?')} [{a.get('citation_ref', '')}]")
        parts.append("")

    if digest.rejected_hypotheses:
        parts.append("ALREADY REJECTED THEORIES (user rejected — do NOT re-propose, but learn from reasons):")
        for r in digest.rejected_hypotheses:
            line = f"  - {r.get('theory', '?')} [{r.get('citation_ref', '')}]"
            reason = r.get("reason")
            if reason:
                line += f" (reason: {reason})"
            parts.append(line)
        parts.append("")

    parts.append("USER'S BEHAVIORAL DIGEST:")
    parts.append(f"  total_events: {digest.total_events}")
    parts.append(f"  observed from {digest.first_event_ts} to {digest.last_event_ts}")
    parts.append("")

    if digest.recent_entity_names:
        parts.append("Entities the user named/created recently (most recent last):")
        for name in digest.recent_entity_names[-50:]:
            parts.append(f"  - {name}")
        parts.append("")

    if digest.recent_queries:
        parts.append("Natural-language queries the user ran recently (most recent last):")
        for q in digest.recent_queries[-30:]:
            parts.append(f"  - {q}")
        parts.append("")

    if digest.recent_ingest_types:
        types = {}
        for t in digest.recent_ingest_types:
            types[t] = types.get(t, 0) + 1
        parts.append("Types of raw material the user has ingested:")
        for t, count in sorted(types.items(), key=lambda kv: -kv[1]):
            parts.append(f"  - {t}: {count}")
        parts.append("")

    if digest.wikilink_edges:
        parts.append(
            f"Wikilink topology: {len(digest.wikilink_edges)} edges "
            "(sample — up to 40 edges):"
        )
        for edge in digest.wikilink_edges[-40:]:
            if isinstance(edge, (list, tuple)) and len(edge) == 2:
                parts.append(f"  - {edge[0]} → {edge[1]}")
        parts.append("")

    parts.append(OUTPUT_FORMAT)
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Response parsing
# ---------------------------------------------------------------------------


_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)


def _strip_json_fence(text: str) -> str:
    """Tolerate a model that wraps its response in ```json … ``` despite the
    "no markdown fence" instruction."""
    t = text.strip()
    if t.startswith("```"):
        lines = t.splitlines()
        # drop first fence line
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        # drop trailing fence if present
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        t = "\n".join(lines).strip()
    return t


def parse_candidate(response: str) -> Optional[TheoryCandidate]:
    """Parse Claude's matcher response text into a TheoryCandidate or None.

    Claude, reading the SKILL.md playbook, produces a JSON response
    following the OUTPUT_FORMAT schema. This function is Claude's
    handoff point — it validates the JSON structure, enforces the
    anti-fluff gates (≥2 structural_elements, integer year), and
    returns either a frozen TheoryCandidate or None (when Claude
    correctly declined to match at the rigor bar).
    """
    text = _strip_json_fence(response).strip()
    if text == "" or text.lower() in ("null", "none"):
        return None
    # If extra prose slipped in, try to extract the first JSON object
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        m = _JSON_OBJECT_RE.search(text)
        if not m:
            raise MatcherError(
                f"matcher LLM returned non-JSON: {text[:200]!r}"
            )
        try:
            parsed = json.loads(m.group(0))
        except json.JSONDecodeError as exc:
            raise MatcherError(
                f"matcher LLM embedded malformed JSON: {exc}"
            ) from exc
    if parsed is None:
        return None
    if not isinstance(parsed, dict):
        raise MatcherError(f"matcher LLM returned non-object: {parsed!r}")

    required = ("theory_name", "author", "year", "primary_source",
                "core_concept", "why_matches")
    for key in required:
        if key not in parsed or parsed[key] in (None, ""):
            raise MatcherError(
                f"matcher response missing required field {key!r}"
            )
    structural = parsed.get("structural_elements") or []
    # Lowered from 3 → 2 per architecture audit (principle 2,
    # anti-essentialism): some genuine traditions have only 2
    # load-bearing poles (Polanyi tacit/explicit, subject/object
    # dualisms, …). Forcing 3 would exclude them.
    if not isinstance(structural, list) or len(structural) < 2:
        raise MatcherError(
            "matcher response must carry ≥ 2 structural_elements "
            f"(got {len(structural) if isinstance(structural, list) else 0})"
        )
    try:
        year = int(parsed["year"])
    except (TypeError, ValueError) as exc:
        raise MatcherError(f"matcher year must be an integer: {exc}") from exc
    confidence = float(parsed.get("confidence") or 0.0)
    if not (0.0 <= confidence <= 1.0):
        confidence = max(0.0, min(1.0, confidence))

    return TheoryCandidate(
        theory_name=str(parsed["theory_name"]),
        author=str(parsed["author"]),
        year=year,
        primary_source=str(parsed["primary_source"]),
        core_concept=str(parsed["core_concept"]),
        why_matches=str(parsed["why_matches"]),
        structural_elements=[str(s) for s in structural],
        confidence=confidence,
    )


# No LLM plumbing lives in this module. Claude, executing under the
# SKILL.md playbook, is the LLM. See .claude/skills/evolve-lens/SKILL.md
# for the call sequence that Claude runs:
#
#   1. tools.lens_evolution.observer.load_digest(vault)
#   2. if digest.total_events == 0:  # short-circuit — no LLM needed
#          report EMPTY_VAULT
#      else:
#          prompt = tools.lens_evolution.matcher.build_matcher_prompt(digest)
#   3. Claude (self) reads `prompt` and produces JSON response following
#      OUTPUT_FORMAT. This is Claude doing the LLM work natively — no
#      API call, no ANTHROPIC_API_KEY.
#   4. candidate = tools.lens_evolution.matcher.parse_candidate(response)
#   5. if candidate is None:  report NO_MATCH
#   6. else:  proceed to verifier stage (same shape — build prompt,
#             Claude reasons, parse_verification)
#   7. if verification confirmed:  operationalize(...)
