"""LENS EVOLUTION — Bab-ilu v2.2 Track L MVP.

The subsystem that fulfills Bab-ilu's central differentiation from
Karpathy's LLM-Wiki and from llm-wiki-agent: it grows new lenses from
the user's practice, matching their unselfconscious work patterns to
pre-existing academic traditions (Warburg, Schön, Polanyi, Kuhn,
Merleau-Ponty, Bourdieu, …).

See PRD-v2.1-zh.md §0.5.4 — LENS EVOLUTION is "Karpathy 未提, Bab-ilu
扩展", positioned as the engineering realization of schema co-evolution
extended from field-level (Karpathy) to entire-lens-level (Bab-ilu).

Architecture (locked per Phoenix 2026-04-21 conversation):

  · Observer — persistent background watcher. Appends behavioral events
    to .agent/state/lens_observer.jsonl; maintains running hypothesis
    state at .agent/state/lens_hypotheses.json. Does NOT listen to
    user declarations/directives — only actual behavior. This is the
    "second pair of eyes" stance: trust behavior over self-report.

  · Matcher — LLM pass that reads hypothesis state and proposes a
    top-1 candidate academic theory matching the user's practice.
    Output must carry the four-piece citation set: author + year +
    primary source + core concept + why-this-matches. Prompt carries
    the Warburg-grade rigor bar (anti pop-framework).

  · Verifier — independent second LLM pass that confirms the citation
    is a real academic work. Prompt stance: "answer 'uncertain' rather
    than confirm speculatively."

  · Evolver — the user-facing /evolve-lens command. Presents one
    hypothesis at a time above a confidence threshold; accepts
    y/n/rename/edit. Accepted flows to the operationalizer.

  · Operationalizer — converts an accepted theory + citation into a
    full lens.yaml + prompts.md + examples.md bundle under
    <vault>/.agent/lenses/<new-lens-id>/, status: candidate (not
    auto-promoted to active or pre-installed slot).

Shared state (vault-scoped, never cross-vault):

  <vault>/.agent/state/lens_observer.jsonl       append-only event log
  <vault>/.agent/state/lens_hypotheses.json      running hypothesis state
  <vault>/.agent/state/lens_evolution_log.jsonl  acceptances/rejections

Five operational principles (PRD §0.5.3) each module must honor:
  1. Late binding
  2. Anti-essentialism (family resemblance; loose lens.yaml schema)
  3. Closed-loop first
  4. Variety matching (Ashby)
  5. Practice over rules (behavior, not self-declaration)
"""

from __future__ import annotations

# Explicitly import submodules so `from tools.lens_evolution import *`
# and `hasattr(pkg, 'observer')` behave consistently regardless of
# import order. Without these lines, `__all__` is a lie per
# python-reviewer audit 2026-04-21.
from tools.lens_evolution import (  # noqa: F401
    evolver,
    matcher,
    observer,
    operationalizer,
    verifier,
)

__all__ = [
    "observer",
    "matcher",
    "verifier",
    "evolver",
    "operationalizer",
]
