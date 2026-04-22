"""Operationalizer — converts an accepted theory candidate into a lens dir.

Input: a TheoryCandidate + VerificationResult + Claude-authored
prose for prompts.md and examples.md.
Output: a new directory at `<vault>/.agent/lenses/<lens-id>/` containing
the four files that define a lens in v2.1:

  lens.yaml    — structural configuration (deterministic, no LLM)
  prompts.md   — tone, rubrics, traps for this lens (Claude-authored)
  examples.md  — 2-3 seed examples (Claude-authored)
  candidate.json — metadata: origin, verifier status, status=candidate

Architecture contract (per Phoenix 2026-04-21 correction, aligned with
Bab-ilu's Claude Code skill pattern):

  THIS MODULE DOES NOT CALL ANY LLM. Claude (the Bab-ilu session
  agent) authors the prose content for prompts.md and examples.md
  directly in its own turn — guided by SKILL.md's prompt templates —
  and then passes the finished markdown strings into
  `operationalize(..., prompts_md=..., examples_md=...)`. This keeps
  all LLM work inside the current Claude Code session and avoids
  reaching for ANTHROPIC_API_KEY.

Design choices (locked per PRD §0.5.4 + Phoenix 2026-04-21 discussion):

  - Generated lens is status=candidate. Never auto-promoted to the
    active lens or the pre-installed slot.
  - lens.yaml is DETERMINISTIC (template + slot-fill). The critical
    config file is never authored by an LLM — it can't invent an
    unknown entity_model key and break the whole vault.
  - Structural_elements map to entity_model (compatibility shim) AND
    to extensions.candidate.structural_model (native view per arch
    audit principle 2).
  - Anchors omitted by default. Candidate lenses ship without
    institutional authority fields until the user declares them.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Optional

from tools.lens_evolution.matcher import TheoryCandidate
from tools.lens_evolution.verifier import VerificationResult

__all__ = [
    "OperationalizationResult",
    "OperationalizationError",
    "operationalize",
    "lens_id_for_theory",
    "PROMPTS_MD_TEMPLATE_INSTRUCTIONS",
    "EXAMPLES_MD_TEMPLATE_INSTRUCTIONS",
]

_SLUG_CLEAN_RE = re.compile(r"[^a-z0-9]+")

# CRITICAL: any LLM-sourced string injected into lens.yaml must pass
# through _sanitize_for_yaml first. An unsanitized newline turns a
# comment line or description scalar into an arbitrary new YAML node,
# which is exploitable: the matcher's JSON parses `\n` into a real
# newline, and a hostile prompt-injected candidate could inject keys
# like `id: stolen` that clobber the canonical top-level id.
# Detected by python-reviewer audit 2026-04-21.
_YAML_UNSAFE_CHARS = ("\n", "\r", "\u2028", "\u2029")


def _sanitize_for_yaml(s: str) -> str:
    if not isinstance(s, str):
        return s
    out = s
    for ch in _YAML_UNSAFE_CHARS:
        out = out.replace(ch, " ")
    return out


class OperationalizationError(Exception):
    """Raised when a candidate cannot be turned into a lens directory."""


@dataclass(frozen=True)
class OperationalizationResult:
    lens_id: str
    lens_dir: Path
    files_written: tuple[Path, ...]


def _slugify(text: str, max_len: int = 50) -> str:
    # ASCII-fold first: "Schön" → "Schon", "müller" → "muller", "Piñera" → "Pinera".
    # Combining marks are decomposed then stripped; the base Latin letter survives.
    # Non-Latin scripts (Cyrillic, CJK, Arabic) decompose to nothing after this and
    # fall through to the non-alnum regex — the final slug gets "candidate" fallback.
    folded = unicodedata.normalize("NFKD", text)
    ascii_only = folded.encode("ascii", "ignore").decode("ascii")
    s = _SLUG_CLEAN_RE.sub("-", ascii_only.lower()).strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "candidate"


def lens_id_for_theory(candidate: TheoryCandidate) -> str:
    """Derive a stable, human-readable lens id from the theory.

    Format: `<surname-slug>-<token-slug>`, e.g.
    `schon-reflection-on-action`.

    The second token is derived in priority order:
      1. `structural_elements[0]` if it's short (≤ 5 words). Warburg-grade
         theories name their canonical atoms as single terms
         (Pathosformel / Knowing-in-action / Habitus), which makes a
         much better slug than the prose core_concept field.
      2. Otherwise fall back to `core_concept`, trimmed to max_len.

    This was changed in 2026-04-21 after the FTG test produced
    `warburg-pathosformel-emotionally-charged-visual-formula-wh`
    from a verbose core_concept — the matcher prompt cannot always
    enforce terse core_concept, so we read the cleaner term from
    structural_elements first.

    Non-ASCII characters (Schön → schon) are simplified via NFKD
    normalization; the full name stays in lens.yaml:name.
    """
    # Surname — take the comma-first branch for "Surname, Firstname"
    # author ordering (py-reviewer audit), else last token for western.
    author = candidate.author
    if "," in author:
        surname = author.split(",")[0].strip()
    else:
        name_parts = [p for p in author.split() if p]
        surname = name_parts[-1] if name_parts else author

    # Prefer a terse structural term over the prose core_concept.
    token_candidate = None
    if candidate.structural_elements:
        first = candidate.structural_elements[0]
        if first and len(first.split()) <= 5:
            token_candidate = first
    if not token_candidate:
        token_candidate = candidate.core_concept

    return f"{_slugify(surname)}-{_slugify(token_candidate)}"


def _build_lens_yaml(
    candidate: TheoryCandidate,
    lens_id: str,
    today: date,
) -> str:
    """Deterministic YAML — no LLM, no hallucination risk on config.

    The YAML emits two parallel structural views:

    - `entity_model` with tier_0 / tier_1_atom / tier_1_cluster keys
      is a COMPATIBILITY SHIM for existing v2.1 consumers
      (graph_analyzer, gap_runner, ask_runner) which expect those
      three keys. For 2-element theories we generate a synthetic
      cluster name; this is honestly labeled in comments so the
      compatibility concession doesn't hide as truth.
    - `extensions.candidate.structural_model` is the NATIVE view: a
      dict of `{theory_native_name: {position, source_label}}` that
      preserves the theory's own ontology without forcing 3 tiers.
      Future consumers — and LENS EVOLUTION's own evolver in later
      sprints — should read THIS view.

    Per architecture audit (2026-04-21) on PRD §0.5.3 principle 2
    (anti-essentialism, family resemblance): the native structural
    model is the truth; the 3-tier entity_model is a temporary shim
    documented as such.
    """
    # Sanitize every LLM-sourced string field before it enters the YAML.
    # CRITICAL fix from python-reviewer audit 2026-04-21: prevents a
    # newline-laden matcher response from injecting arbitrary YAML keys.
    safe = TheoryCandidate(
        theory_name=_sanitize_for_yaml(candidate.theory_name),
        author=_sanitize_for_yaml(candidate.author),
        year=candidate.year,
        primary_source=_sanitize_for_yaml(candidate.primary_source),
        core_concept=_sanitize_for_yaml(candidate.core_concept),
        why_matches=_sanitize_for_yaml(candidate.why_matches),
        structural_elements=[_sanitize_for_yaml(s)
                             for s in candidate.structural_elements],
        confidence=candidate.confidence,
    )
    candidate = safe
    elements = list(candidate.structural_elements)
    tier_0 = _slugify(elements[0])
    tier_1_atom = _slugify(elements[1]) if len(elements) >= 2 else tier_0
    # Synthetic cluster name for theories with fewer than 3 elements —
    # this is the essentialism shim the architecture audit flagged.
    # Kept for consumer compatibility; future consumers should prefer
    # `extensions.candidate.structural_model`.
    if len(elements) >= 3:
        tier_1_cluster = _slugify(elements[2])
        cluster_is_synthetic = False
    else:
        tier_1_cluster = f"{tier_1_atom}-cluster"
        cluster_is_synthetic = True
    extras = elements[3:] if len(elements) > 3 else []

    def _yaml_str(s: str) -> str:
        if not s:
            return "''"
        # Double-quoted with explicit escaping — safe for YAML 1.2.
        # Newline / CR / unicode-line-separator sanitization already
        # happened above; this keeps backslash + quote escaping as
        # defense in depth against any upstream lapse.
        escaped = (
            s.replace("\\", "\\\\")
             .replace('"', '\\"')
             .replace("\n", "\\n")
             .replace("\r", "\\r")
        )
        return '"' + escaped + '"'

    lines: list[str] = [
        f"# {lens_id} lens — generated by LENS EVOLUTION",
        f"# Origin: {candidate.author} ({candidate.year}), "
        f"{candidate.primary_source}",
        f"# Core concept: {candidate.core_concept}",
        f"# Status: candidate — NOT promoted to active or pre-installed slot",
        f"# Generated: {today.isoformat()}",
        "#",
        "# Structural model: see extensions.candidate.structural_model for the",
        "# NATIVE theory view. The tier_0/tier_1_atom/tier_1_cluster keys",
        "# below are a compatibility shim for existing v2.1 consumers; do",
        "# not read essentialism into the 3-tier layout.",
        "",
        f"id: {lens_id}",
        'version: "0.1.0-candidate"',
        f"name: {_yaml_str(candidate.theory_name)}",
        "description: >-",
        f"  Candidate lens generated from the user's behavioral pattern.",
        f"  Traces to {candidate.author} ({candidate.year}), "
        f"{candidate.primary_source}.",
        f"  Core concept: {candidate.core_concept}.",
        "",
        "deliverable_types:",
        "  - candidate-summary     # LENS EVOLUTION default; evolve per theory later",
        "",
        "entity_model:  # compatibility shim — see extensions.candidate.structural_model",
        f"  tier_0: {tier_0}",
        f"  tier_1_atom: {tier_1_atom}",
        f"  tier_1_cluster: {tier_1_cluster}"
        + ("  # synthetic — theory has <3 native elements"
           if cluster_is_synthetic else ""),
        "",
        "# No activation triggers set — candidate lenses must be explicitly",
        "# selected via /genesis or by editing .agent/lenses/active/.",
        "",
        "thresholds:",
        "  cluster_member_min: 3",
        "  cluster_min_size: 3",
        "  density_multiplier: 2.5",
        "  orphan_min_degree: 2",
        "",
        "# No authority_fields — candidate lenses do not ship institutional",
        "# anchors until the user declares which external IDs matter.",
        "",
        "analysis_contract:",
        "  gap:",
        "    - orphan_node",
        "    - one_way_link",
        "    - disconnected_cluster",
        "  taste:",
        "    - entity_frequency",
        "    - cluster_emergence",
        "",
        "extensions:",
        "  candidate:",
        f"    origin_theory: {_yaml_str(candidate.theory_name)}",
        f"    origin_author: {_yaml_str(candidate.author)}",
        f"    origin_year: {candidate.year}",
        f"    origin_source: {_yaml_str(candidate.primary_source)}",
        f"    origin_core_concept: {_yaml_str(candidate.core_concept)}",
        f"    generated_at: {today.isoformat()}",
        f"    native_element_count: {len(elements)}",
        f"    compatibility_shim_applied: {str(cluster_is_synthetic).lower()}",
        "    # structural_model: the THEORY-NATIVE ontology. Unlike the",
        "    # fixed 3-tier entity_model above, this preserves arbitrary",
        "    # element counts with native names. Forward-compatible view.",
        "    structural_model:",
    ]
    for i, e in enumerate(elements):
        lines.append(f"      {_slugify(e)}:")
        lines.append(f"        position: {i}")
        lines.append(f"        source_label: {_yaml_str(e)}")
    lines.append("    structural_elements:")
    for e in elements:
        lines.append(f"      - {_yaml_str(e)}")
    if extras:
        lines.append("    elements_outside_compat_shim:")
        for e in extras:
            lines.append(f"      - {_yaml_str(e)}")
    lines.append("")
    return "\n".join(lines)


# These instructions are what Claude reads (via SKILL.md) when authoring
# prompts.md and examples.md for an accepted candidate lens. They used
# to be formatted into literal LLM API prompts inside this module; now
# Claude reads them directly as part of the skill playbook. We still
# expose them as module constants so the skill doc can reference a
# single source of truth.

PROMPTS_MD_TEMPLATE_INSTRUCTIONS = """\
When you (Claude) author `prompts.md` for a newly-accepted candidate
lens based on {theory_name} by {author} ({year}, {primary_source}),
follow this structure. Its purpose: guide a future agent running under
this lens to write wiki entries that genuinely embody the theory's
distinctions, not generic encyclopedia prose.

Write in English. Be concise. Include THREE sections:

## Tone
Two sentences on what "writing under this lens" should sound like.
What does {author}'s actual scholarly voice do that a generic summary
doesn't?

## Rubrics
A short list of 3-5 questions a wiki entry under this lens MUST answer.
Each rubric item should reference the theory's concrete distinctions
({structural_elements}), not generic "what is this" questions.

## Traps
3-5 pitfalls specific to this theory — places where a naive LLM would
write prose that LOOKS like the theory but misses its actual move.
Example for Schön: "Don't call generic 'post-hoc thinking'
reflection-on-action — Schön specifically requires the practitioner
to surface tacit frames they were previously unaware of."

Do NOT invent concepts not from the primary source. If you need a
concept to make a rubric work and it's not from this theory, write
a generic rubric instead.
"""

EXAMPLES_MD_TEMPLATE_INSTRUCTIONS = """\
When you (Claude) author `examples.md` for a newly-accepted candidate
lens based on {theory_name} by {author} ({year}, {primary_source}),
follow this structure. Write 2-3 worked examples showing how to
compose a tier_1_atom entry under this lens. Each example should:

  - Pick a plausible subject matter the user might study under this
    theory
  - Show the entity frontmatter (minimal — title, slug, lens id)
  - Show a ~100-word body that visibly uses the theory's distinctions
    ({structural_elements})

Do NOT over-specify subject matter — keep the examples generic enough
that they serve as a pattern, not a field-specific template.
"""


def render_prompts_instructions(candidate: TheoryCandidate) -> str:
    """Return the prompts.md authoring instructions for Claude to read."""
    return PROMPTS_MD_TEMPLATE_INSTRUCTIONS.format(
        theory_name=candidate.theory_name,
        author=candidate.author,
        year=candidate.year,
        primary_source=candidate.primary_source,
        structural_elements=", ".join(candidate.structural_elements),
    )


def render_examples_instructions(candidate: TheoryCandidate) -> str:
    """Return the examples.md authoring instructions for Claude to read."""
    return EXAMPLES_MD_TEMPLATE_INSTRUCTIONS.format(
        theory_name=candidate.theory_name,
        author=candidate.author,
        year=candidate.year,
        primary_source=candidate.primary_source,
        structural_elements=", ".join(candidate.structural_elements),
    )


def operationalize(
    candidate: TheoryCandidate,
    verification: VerificationResult,
    vault: Path,
    *,
    prompts_md: str,
    examples_md: str,
    today: Optional[date] = None,
    lenses_base: Optional[Path] = None,
    overwrite: bool = False,
) -> OperationalizationResult:
    """Write a complete candidate lens directory from a TheoryCandidate.

    `prompts_md` and `examples_md` are Claude-authored markdown strings
    (the SKILL.md playbook guides Claude to produce them using
    `render_prompts_instructions` / `render_examples_instructions`).
    This module NEVER calls an LLM; the prose arrives already formed.

    Safety:
      - Refuses to run unless verification.status == 'confirmed'. Drops
        uncertain / rejected candidates here, defense in depth beyond
        the evolver's gate.
      - Refuses to overwrite an existing lens directory unless
        `overwrite=True`. Candidate lens id collisions (two theories
        generating the same surname-slug) surface loud rather than
        silently clobber.
      - Empty prompts_md / examples_md is rejected — skill must supply
        real content; empty files would ship a dead lens.
    """
    if verification.status != "confirmed":
        raise OperationalizationError(
            "cannot operationalize candidate with verification status "
            f"{verification.status!r}; required: 'confirmed'"
        )
    if len(candidate.structural_elements) < 2:
        raise OperationalizationError(
            "candidate must have ≥ 2 structural elements to map onto "
            f"entity_model (has {len(candidate.structural_elements)})"
        )
    # Defense-in-depth (architecture audit): the evolver already enforces
    # the confidence threshold but a direct call to operationalize() would
    # bypass it. Import the threshold here to keep a single source of truth.
    from tools.lens_evolution.evolver import CONFIDENCE_THRESHOLD
    if candidate.confidence < CONFIDENCE_THRESHOLD:
        raise OperationalizationError(
            f"candidate confidence {candidate.confidence:.2f} below "
            f"threshold {CONFIDENCE_THRESHOLD:.2f}; direct-call bypass blocked"
        )
    if not (prompts_md and prompts_md.strip()):
        raise OperationalizationError(
            "prompts_md must be a non-empty Claude-authored markdown string"
        )
    if not (examples_md and examples_md.strip()):
        raise OperationalizationError(
            "examples_md must be a non-empty Claude-authored markdown string"
        )

    vault = Path(vault).resolve()
    lenses_root = (
        Path(lenses_base) if lenses_base is not None
        else vault / ".agent" / "lenses"
    )
    lens_id = lens_id_for_theory(candidate)
    lens_dir = lenses_root / lens_id

    # Defense-in-depth: _slugify should prevent any traversal character
    # from surviving into lens_id, but assert the containment invariant
    # regardless. Security audit 2026-04-21.
    resolved_lens_dir = (lenses_root / lens_id).resolve() if lenses_root.exists() else (lenses_root / lens_id)
    try:
        resolved_lens_dir.relative_to(lenses_root.resolve() if lenses_root.exists() else lenses_root)
    except ValueError:
        raise OperationalizationError(
            f"lens_id produced a path outside lenses_root: "
            f"{resolved_lens_dir!r} not under {lenses_root!r}"
        )

    if lens_dir.exists() and not overwrite:
        raise OperationalizationError(
            f"lens dir already exists: {lens_dir}. "
            "Pass overwrite=True to regenerate."
        )

    lens_dir.mkdir(parents=True, exist_ok=True)
    today = today or date.today()

    # 1. lens.yaml (deterministic — never LLM-authored)
    yaml_path = lens_dir / "lens.yaml"
    yaml_path.write_text(
        _build_lens_yaml(candidate, lens_id, today),
        encoding="utf-8",
    )

    # 2. prompts.md (Claude-authored, passed in)
    prompts_path = lens_dir / "prompts.md"
    prompts_path.write_text(
        prompts_md.rstrip() + "\n", encoding="utf-8",
    )

    # 3. examples.md (Claude-authored, passed in)
    examples_path = lens_dir / "examples.md"
    examples_path.write_text(
        examples_md.rstrip() + "\n", encoding="utf-8",
    )

    # 4. candidate.json (metadata)
    candidate_meta = {
        "status": "candidate",
        "generated_at": datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "theory": candidate.to_dict(),
        "verification": verification.to_dict(),
        "files": ["lens.yaml", "prompts.md", "examples.md"],
    }
    candidate_path = lens_dir / "candidate.json"
    candidate_path.write_text(
        json.dumps(candidate_meta, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return OperationalizationResult(
        lens_id=lens_id,
        lens_dir=lens_dir,
        files_written=(yaml_path, prompts_path, examples_path, candidate_path),
    )
