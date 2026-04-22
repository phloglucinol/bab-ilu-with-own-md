---
name: evolve-lens
description: LENS EVOLUTION — behavioral matcher that proposes an academic theory (Warburg-grade rigor) whose structure matches the user's unselfconscious working pattern. If accepted, operationalizes the theory as a new candidate lens installed at `<vault>/.agent/lenses/<id>/`. Reads observer state built silently from prior /ingest, /ask, synthesis-accept events. Never listens to user directives — behavior only. PRD §0.5.4 Track L MVP. Runs entirely in-session: Claude (this agent) is the matcher + verifier; no external API calls.
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

# /evolve-lens — the second pair of eyes

## What this does

`/evolve-lens` fulfills Bab-ilu's central philosophical claim from
PRD §0.5.2: *"Bab-ilu 不是一个'知道规则'的系统，是一个'从实践中长出规则'的系统"*.

While the user works (ingests material, runs /ask, accepts syntheses,
names entities), a background observer accumulates their behavioral
pattern **without listening to anything they say** about what they're
doing — only what they *do*. When they invoke `/evolve-lens`, you
(Claude, the current session agent) perform a three-stage reasoning
pass over the observed behavior, looking for an academic tradition
whose structure is isomorphic to the user's unselfconscious pattern.

If you find one, you present the candidate theory with its four-piece
citation, the user decides whether to accept it, and on acceptance
Python tools install a new `status: candidate` lens under
`<vault>/.agent/lenses/<id>/`.

**This skill runs entirely inside the current Claude Code session. No
ANTHROPIC_API_KEY, no outbound LLM calls. Python tools provide
deterministic work (file IO, prompt construction, response parsing);
you provide all the LLM reasoning.**

## What this does NOT do

- **Does not listen to directives.** If the user runs `/evolve-lens
  find me something about phenomenology`, the phrase "phenomenology"
  is ignored. The observer infers from behavior only. If the user
  wants output biased toward a specific direction, they must practice
  in that direction — ingest, query, take notes in that mode.
- **Does not invent new concepts.** The rigor bar (see matcher prompt)
  excludes pop frameworks, TED-talk mental models, LLM-introduced
  concepts with no pre-2020 academic literature, and academic-laundered
  frameworks (Simon→Design Thinking, Aristotle→First Principles, etc.).
- **Does not auto-activate.** Generated lenses land at
  `.agent/lenses/<id>/` with `status: candidate`. Switching to them
  is the user's explicit act via `/genesis` or by editing the active
  pointer.

## Execution playbook — follow each step in order

Assume you have been invoked as `/evolve-lens` (no arguments; argument
strings, if any, MUST be ignored per the "no directives" contract).

### Step 1 — prepare

Load the observer digest and check for the short-circuit case:

```python
from tools.lens_evolution.evolver import prepare_evolution, EvolutionOutcome
ctx = prepare_evolution(vault)
if ctx.outcome == EvolutionOutcome.EMPTY_VAULT:
    # Report ctx.message to the user and stop.
```

If `ctx.outcome is None`, `ctx.matcher_prompt` holds the prompt you
will reason over in Step 2.

### Step 2 — matcher pass (you are the matcher)

Read `ctx.matcher_prompt`. It contains the Warburg-grade rigor bar,
the base-rate calibration ("expect null 4 out of 5 times"), the
academic-laundering refusal list, and the user's behavioral digest.

Reason over it in your own turn. Honestly apply the self-tests the
prompt names (generic-sounding why_matches test, verbatim-source test,
recognized-provenance test). Bias hard toward `null`.

Produce a response in the OUTPUT_FORMAT JSON schema:

```
{"theory_name": "...", "author": "...", "year": ..., "primary_source": "...",
 "core_concept": "...", "why_matches": "...",
 "structural_elements": ["...", "..."], "confidence": 0.x}
```

Or `null` if no theory at the rigor bar matches.

Parse your response back into a `TheoryCandidate`:

```python
from tools.lens_evolution.matcher import parse_candidate
candidate = parse_candidate(your_response_text)
```

If `candidate is None`, report `NO_MATCH` to the user with a "keep
building your practice" message and stop.

### Step 3 — confidence threshold gate

```python
from tools.lens_evolution.evolver import below_threshold
if below_threshold(candidate):
    # Report BELOW_THRESHOLD with candidate.theory_name and confidence.
    # Do NOT show the candidate to the user — the rigor bar requires
    # both a rigor-compliant match AND sufficient confidence.
    # Stop.
```

### Step 4 — verifier pass (you are the verifier, in a fresh context)

This is the key second-pass guard against hallucinated citations. Get
the verifier prompt:

```python
from tools.lens_evolution.verifier import build_verifier_prompt
verifier_prompt = build_verifier_prompt(candidate)
```

Read it **as if for the first time, without carrying over matcher
context**. The verifier prompt tells you to act as a reference
librarian fact-checking a bibliographic claim, NOT to evaluate
whether the match is tight. The prompt explicitly biases toward
`uncertain` — you should prefer uncertain 20x over confirmed.

Produce a JSON response:

```
{"status": "confirmed" | "uncertain" | "rejected", "reasoning": "..."}
```

Parse it:

```python
from tools.lens_evolution.verifier import parse_verification, is_accepted
verification = parse_verification(your_verifier_response)
if not is_accepted(verification):
    from tools.lens_evolution.evolver import record_verifier_drop
    record_verifier_drop(vault, candidate, verification, lens_override=active_lens_id)
    # Report FAILED_VERIFICATION with verification.reasoning. Stop.
```

### Step 5 — present to user and read decision

```python
from tools.lens_evolution.evolver import format_candidate_for_user
print(format_candidate_for_user(candidate))
```

Ask the user `Accept this theory as a candidate lens? (y/n):` and
read their reply. **Default-reject: only explicit `y`/`yes` accepts.**
Anything else — empty input, typos, explicit `n` — is rejection.

If rejected:

```python
from tools.lens_evolution.evolver import record_user_rejection
# Optionally prompt for a reason string.
record_user_rejection(vault, candidate, reason="<user's text or 'user-rejected'>",
                     lens_override=active_lens_id)
# Report USER_REJECTED with candidate.theory_name. Stop.
```

### Step 6 — author prompts.md and examples.md (you write the markdown)

Before calling the operationalizer, you author the two prose files
for the new lens directly. Get the authoring instructions:

```python
from tools.lens_evolution.operationalizer import (
    render_prompts_instructions,
    render_examples_instructions,
)
prompts_instructions = render_prompts_instructions(candidate)
examples_instructions = render_examples_instructions(candidate)
```

Read each instruction string. Write the actual markdown — prompts.md
(three sections: Tone, Rubrics, Traps) and examples.md (2-3 worked
examples). These are YOUR prose; no LLM API call happens. Store them
as Python strings `prompts_md` and `examples_md`.

Follow the rigor rules the instructions spell out (don't invent
concepts not in the primary source; keep examples domain-generic).

### Step 7 — operationalize (write the lens dir)

```python
from tools.lens_evolution.operationalizer import operationalize
op_result = operationalize(
    candidate, verification, vault,
    prompts_md=prompts_md,
    examples_md=examples_md,
)
```

This writes four files under `<vault>/.agent/lenses/<op_result.lens_id>/`:
lens.yaml, prompts.md, examples.md, candidate.json.

### Step 8 — record acceptance

```python
from tools.lens_evolution.evolver import record_user_acceptance
record_user_acceptance(vault, candidate, op_result, lens_override=active_lens_id)
```

Report `ACCEPTED_AND_INSTALLED` to the user with the lens_id and
lens_dir, and remind them the lens is `status: candidate` — not yet
active; they review the four files and switch explicitly via
/genesis or by editing .agent/lenses/active/.

## Terminal outcomes

| Outcome | When it happens | User sees |
|---|---|---|
| `empty_vault` | Observer has no events | "Use the vault more and try again" |
| `no_match` | You returned null at matcher stage | "No theory at Warburg-grade rigor matches; keep practicing" |
| `below_threshold` | Confidence < 0.60 | "Continuing to observe, try later" |
| `failed_verification` | Verifier returned uncertain/rejected | "Candidate dropped by independent citation check" |
| `user_rejected` | User typed anything other than y/yes | "Rejected: <theory>" |
| `accepted_and_installed` | All gates passed, lens dir written | "✓ new candidate lens installed at <path>" |

## Where state lives (vault-scoped)

- `<vault>/.agent/state/lens_observer.jsonl` — append-only event log
- `<vault>/.agent/state/lens_hypotheses.json` — running digest cache
- `<vault>/.agent/lenses/<new-id>/` — operationalized candidate lenses

## Known limitations (v2.2 MVP)

- Observer hooks currently wired into `tools.ask_runner.run_ask` and
  `tools.ask_runner.write_synthesis`. Hooks for `/ingest` and `/taste`
  are deferred to Sprint 5 — a vault used mainly for ingest may show
  empty_vault until the user runs /ask or archives a synthesis.
- Single candidate per invocation. If you reject one, the next call
  will propose a different one (the matcher prompt lists rejected
  theories as "do not re-propose").
- Confidence threshold (0.60) is a fixed default. Per-call override
  supported via `CONFIDENCE_THRESHOLD` argument to `below_threshold()`;
  adaptive-from-accept/reject-history is a Sprint 5 item.

## References

- PRD-v2.1-zh.md §0.5.4 — "对 Karpathy 的继承与扩展清单"
- PRD-v2.1-zh.md §0.5.3 — five operational principles (especially
  principle 1 late binding, principle 4 variety matching, principle 5
  practice over rules)
- `tools/lens_evolution/` — implementation (observer, matcher,
  verifier, evolver stage helpers, operationalizer)
- `docs/superpowers/plans/2026-04-20-sprint4-plan.md` — Track L
