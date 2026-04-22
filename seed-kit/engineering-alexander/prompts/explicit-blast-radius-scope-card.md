---
type: pattern-card-template
pattern: "[[explicit-blast-radius-scope]]"
lens: engineering-alexander
seed: true
---

# 显式作用域边界 (Explicit Blast Radius Scope) — Pattern Card Template

## Context

This pattern applies to any tool or command that writes to, reconfigures, or
deploys across a set of production targets. The targets may be servers, network
devices, CDN edge nodes, feature-flag populations, or database replicas. The
pattern is triggered when the tool's default scope — the set of targets it
affects when no explicit boundary is specified — is broader than the scope an
operator typically intends.

## Problem

When push tools carry implicit global defaults, a single mistyped or omitted
argument transforms a local change into a global one. The intent-to-effect gap
is invisible in the command line: the invocation that targets one cluster looks
identical to the invocation that targets all clusters, except for the absence
of a flag. The blast radius of the mistake is proportional to the default scope,
which is typically the largest possible scope.

### Forces in tension

- [[reliability-vs-velocity]] — requiring an explicit scope flag on every push
  adds friction to the fast path; operators working under incident pressure are
  most likely to omit the flag at exactly the moment when a mis-scoped push
  would be most damaging.
- [[explicit-blast-radius-scope]] — tools that infer broad scope from silence
  violate the principle of least surprise; every invocation should do
  exactly as much as the operator can see it is doing.
- Rollback granularity — a narrower push scope produces a narrower rollback
  unit; a global push can only be rolled back globally, while a per-region push
  can be rolled back per-region.

## Forces

- [[explicit-blast-radius-scope]] — the tool must refuse to act without an
  explicit scope declaration; absence of a scope argument must be a hard error,
  not an implicit "apply everywhere."
- [[reliability-vs-velocity]] — the fastest deployment path (no scope flag,
  broad default) is also the most dangerous; the pattern imposes a small
  per-invocation cost to bound the worst-case outcome.
- Audit legibility — logged commands that include an explicit scope are
  self-documenting; commands that rely on defaults require the reader to
  consult tool documentation to reconstruct the actual target set at the
  time of execution.

## Solution

Require every push command to carry an explicit `--scope` argument. The tool
must reject invocations that omit the scope with a clear error message naming
the missing parameter; it must not infer a default scope. If a genuinely global
push is needed, require a second flag — such as `--scope=global
--i-really-mean-everything` — that makes the intent unambiguous and forces a
deliberate second keystroke. Log both the declared scope and the resolved target
set so that post-incident analysis can verify that what was intended to be
targeted was actually targeted. Reject glob patterns in scope values unless a
separate confirmation flag is present.

## Resulting Context

Accidental global pushes become structurally impossible: the tool will not
execute without an explicit scope, and a global scope requires deliberate
double-confirmation. Intentional global pushes become two-step operations
rather than one-step operations — a small cost that is acceptable for a rare
operation. Operators must learn the scope syntax, which introduces onboarding
friction. Post-incident log review is significantly cleaner because every
historical invocation carries a documented target set. The pattern does not
prevent *intentionally* mis-scoped pushes; it only prevents accidental ones
caused by default behavior.

## Examples (from vault)

- [[google-2019-config-push-gce]] — a network configuration push intended for
  one cluster propagated to multiple regions because the push tool had no
  mandatory scope boundary; the resulting routing change overwhelmed remaining
  capacity in adjacent regions.
- [[cloudflare-2019-regex-cpu]] — a WAF rule deployed globally without a staged
  rollout scope reached every CPU simultaneously; a mandatory `--scope=region`
  first-tier deployment would have surfaced the CPU regression before global
  propagation.

## Traps / Counter-forces

- **Scope validation without scope enforcement**: a tool that warns about a
  missing scope but proceeds anyway provides logging value with none of the
  blast-radius protection; the warning will be ignored under incident pressure.
- **Scope that names logical groups rather than physical boundaries**: a scope
  named `production` that resolves to all production infrastructure is a
  global push wearing a local label; scopes must map to bounded, enumerable
  target sets.
