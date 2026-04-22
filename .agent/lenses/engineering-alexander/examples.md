# engineering-alexander · worked examples

*Two pattern-card extractions executed under this lens. Claude reads these
to calibrate voice, pattern-card form fidelity, forces-in-tension honesty,
and how a single incident is abstracted into a reusable remedy. Every
[[wikilink]] resolves to a real file under `seed-kit/engineering-alexander/`
unless explicitly marked as proposed. No post-mortem is paraphrased —
each card must be legible to an engineer who has never used that vendor.*

---

## Example 1 — Cloudflare 2019 Regex CPU Incident

### Source

| Field | Value |
|-------|-------|
| **postmortem_url** | https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/ |
| **incident_date** | 2019-07-02 |
| **vendor** | Cloudflare |
| **service_name** | Cloudflare WAF (Web Application Firewall) |
| **duration** | 27 minutes, 100% CPU on all L7 processing nodes globally |
| **vault anchor** | `[[cloudflare-2019-regex-cpu]]` |

### Context

Cloudflare's WAF evaluates user-submitted rules against every HTTP request
in-line on every edge node worldwide. Rules are written in a custom
expression language backed by a PCRE-compatible regex engine. At the time
of the incident, no per-rule CPU-time bound existed in the evaluation
pipeline; the deployment gate checked syntax validity only.

A WAF engineer submitted a new rule to improve SQL-injection detection. The
rule contained a catastrophic-backtracking regex — a class of pattern where
PCRE's backtracking engine explores an exponential number of states on
adversarial or simply unlucky input. The rule passed syntax validation, was
promoted to the global ruleset, and was pushed to all edge nodes
simultaneously.

### Problem

A single user-submitted rule, evaluated on every HTTP request at every
edge node, can saturate all available CPU and take the entire L7 stack
offline with zero mitigation window — because the evaluation pipeline
treats rule correctness (syntax) as equivalent to rule safety (bounded
runtime), and neither the deployment gate nor the rollout scope prevents
simultaneous global activation.

### Forces

- **[[reliability-vs-velocity]]** — a per-rule CPU-budget check would
  require a performance-regression gate in CI, adding latency to the rule
  authoring loop; without it, rules ship faster but safely guarantees
  disappear.
- **Expressiveness vs. predictability** (implicit in [[reliability-vs-velocity]]) —
  PCRE's backtracking gives rule authors expressive power (lookaheads,
  back-references, possessive quantifiers); replacing PCRE with RE2
  (O(n) guaranteed) eliminates catastrophic backtracking but removes
  constructs that legitimate rules already used. *This force opposes the
  solution*: some real security rules cannot be expressed in RE2.
- **[[recovery-time-vs-redundancy-cost]]** — simultaneous global rollout
  means there is no unaffected canary region to fail back to; incremental
  rollout with a blast-radius limit trades rollout time for a recovery path
  that doesn't require a global revert.

### Solution

Any per-request user-controlled logic — WAF rules, ACLs, JSON Schema
validators, user scripts — must execute within a hard CPU-time budget
enforced by the evaluation engine, not by a linter. For regex specifically,
use an engine with a linear-time guarantee (RE2, Hyperscan in literal mode)
in place of a backtracking engine; where backtracking semantics are required,
enforce a step-count limit that kills evaluation before CPU saturation.

Deploy rule changes under the same blast-radius discipline as code changes:
canary to a bounded set of edge nodes, measure CPU impact against a
p99.9 threshold, promote only when the measurement passes. A rule that
exceeds the budget at canary is rejected — not queued for human review,
rejected — so the gate is mechanical, not social.

### Resulting Context

After applying [[per-operation-cpu-budget]]:

- A catastrophic-backtracking regex is mechanically unreachable at
  production: it fails the canary CPU gate before global promotion.
- Rule authors lose some expressive power — PCRE constructs that cannot
  be emulated in RE2 are no longer legal. This is the expected trade: the
  pattern explicitly trades expressiveness for SLA.
- A new tension emerges: the RE2-vs-PCRE boundary becomes a point of
  friction between the security team (who write rules) and the platform
  team (who enforces the budget). That friction must be resolved by a
  documented rule capability matrix, not by ad-hoc exceptions.

### Pattern surfaced

**[[per-operation-cpu-budget]]** — *one-star candidate, domain: runtime*

This incident justifies the pattern because: (a) the root cause is
precisely the absence of a per-operation CPU bound on user-supplied
evaluation logic; (b) the pattern's Solution maps directly to what
Cloudflare implemented post-incident (RE2 migration, step-count limits);
(c) the forces in tension are identical to the pattern card's declared
forces (expressiveness vs. predictability vs. worst-case latency).

The pattern already exists at
`seed-kit/engineering-alexander/patterns/per-operation-cpu-budget.md` with
one supporting example (`[[cloudflare-2019-regex-cpu]]`). It reaches
two-star once a second independent instance from a different system is
added (e.g., a GraphQL depth-limit incident or a JavaScript sandbox escape).

### Pattern-language cluster

**Blast-Radius Containment at Change Time**

This cluster groups patterns whose common problem is: *a change of bounded
intent produces unbounded impact because no structural mechanism enforces
scope at the point of execution*. Members:

| Pattern | Mechanism |
|---------|-----------|
| [[per-operation-cpu-budget]] | bounds the execution cost of a single rule |
| [[explicit-blast-radius-scope]] | bounds the deployment scope of a single change |
| [[deploy-atomicity-verification]] | prevents partial-scope changes from masquerading as complete ones |
| [[dead-code-plus-flag-reuse]] | prevents flag-scoped changes from activating unintended code paths |

Four patterns, three domains (runtime, deployment × 3). Satisfies
`lens.yaml` threshold `cluster_member_min: 3`. The cluster name describes
the problem space ("blast-radius containment"), not an arbitrary theme.
These patterns compose: `[[per-operation-cpu-budget]]`'s resulting context
("users lose some expressiveness") is a forcing function for why
`[[explicit-blast-radius-scope]]`'s canary-first rollout is necessary —
if the budget check itself is wrong, you want to have rolled out to 1% of
nodes, not 100%.

### Authority anchors

| Field | Value |
|-------|-------|
| `postmortem_url` | https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/ |
| `service_name` | Cloudflare WAF |

Note: No CVE or RFC applies here. The underlying weakness is CWE-400
(Uncontrolled Resource Consumption) if a CWE anchor is wanted for a
follow-on pattern card on catastrophic backtracking specifically — but
do not attach it to the `per-operation-cpu-budget` card, which is broader
than any single CWE class.

### Back-references (what this unlocks in the vault)

- **[[explicit-blast-radius-scope]]** already lists
  `[[cloudflare-2019-regex-cpu]]` in its Examples section
  (`seed-kit/engineering-alexander/patterns/explicit-blast-radius-scope.md`,
  line 29). The two patterns are *not* redundant: `[[explicit-blast-radius-scope]]`
  is about where the change lands (which nodes receive it); `[[per-operation-cpu-budget]]`
  is about what happens after it lands (how much CPU a single evaluation
  can consume). Both would have been needed to prevent this incident; the
  absence of either alone was sufficient to cause it.
- **[[google-2019-config-push-gce]]** — that incident's root cause is
  "configuration pushed beyond intended scope" (no blast-radius scope
  enforcement); this incident's root cause is "rule executed beyond bounded
  cost" (no per-operation CPU budget). The two incidents occupy different
  positions on the same Blast-Radius Containment cluster: GCE 2019 validates
  `[[explicit-blast-radius-scope]]`; Cloudflare 2019 validates
  `[[per-operation-cpu-budget]]`. Citing both in the cluster brief
  demonstrates that the cluster is not one incident in disguise.
- **[[facebook-2021-bgp]]** — that incident's pattern
  (`[[control-plane-in-band-dependency]]`) shows what happens when recovery
  *itself* has no blast-radius boundary. Read together, Cloudflare 2019
  and Facebook 2021 demonstrate that blast-radius containment must be
  applied at two distinct layers: change execution (Cloudflare) and
  recovery execution (Facebook).

### Problem depth

**Captured**: the forces are in genuine tension — the Solution requires
trading PCRE expressiveness for RE2's linear-time guarantee, and the card
names this trade explicitly rather than pretending it is free. The
Resulting Context section names the new tension (RE2/PCRE friction between
security and platform teams) rather than claiming the pattern resolves
everything.

**Not captured**: the incident also involves a global-simultaneous deployment
(no canary); the pattern card above acknowledges this as a related but
distinct force addressed by `[[explicit-blast-radius-scope]]`, rather than
inflating `[[per-operation-cpu-budget]]` to cover deployment scope.

### Traps avoided

1. **Did not paraphrase the Cloudflare post-mortem.** The Context section
   strips all product-specific language (no "Cloudflare WAF engine v5",
   no "Firewall Rules expression language"). The card is legible to an
   engineer who has never used Cloudflare.
2. **Did not inflate this into two separate patterns.** The incident
   contains two remedies (CPU budget + canary rollout). Rather than
   creating a new `[[global-simultaneous-deploy-prevention]]` pattern,
   the card acknowledges canary rollout as the domain of the already-existing
   `[[explicit-blast-radius-scope]]`. Splitting would have violated
   Alexander's rule: a pattern without ≥2 independent instances is a
   candidate, not a pattern.
3. **Did not write a runbook.** The Solution section says "use an engine
   with a linear-time guarantee" and "enforce a step-count limit" — it
   names the design choice, not a sequential checklist. An engineer at a
   different vendor (an API gateway, a rule-based firewall, a GraphQL
   server) can apply the pattern without touching Cloudflare's code.

---

## Example 2 — AWS S3 US-EAST-1 Operator Typo (2017)

### Source

| Field | Value |
|-------|-------|
| **postmortem_url** | https://aws.amazon.com/message/41926/ |
| **incident_date** | 2017-02-28 |
| **vendor** | Amazon Web Services |
| **service_name** | Amazon S3 (US-EAST-1) |
| **duration** | 240 minutes; full-region S3 unavailability; INDEX and METADATA subsystems rebuilt from scratch |
| **vault anchor** | `[[aws-s3-2017-us-east-1]]` |

### Context

Amazon S3's billing subsystem is maintained by a dedicated team with
access to an internal playbook for capacity management. The playbook
includes a command that removes a specified number of servers from a
subsystem to debug capacity-accounting issues. The command accepts a
numeric argument: "remove N servers from subsystem X."

During a 2017-02-28 maintenance operation, an engineer ran the command
with an argument that was larger than intended — the result of a typo in
a numeric field. The command removed significantly more server capacity
than planned from S3's INDEX and METADATA subsystems. Both subsystems
fell below their minimum redundancy threshold and entered a full rebuild
cycle. Because S3's INDEX subsystem had grown far beyond its original
design size without a corresponding update to the rebuild procedure, the
rebuild took 4+ hours instead of the expected minutes. During the rebuild,
Amazon S3 in US-EAST-1 was effectively unavailable, taking down a
significant fraction of internet services that depended on it.

The maintenance playbook had no upper-bound validation on the numeric
argument, and the cold-start procedure for the subsystems had never been
rehearsed at the scale the system had grown to.

### Problem

An operational playbook command that accepts a quantity argument has no
enforced upper bound. A single-digit typo removes more resources than the
system can tolerate, crossing a minimum redundancy threshold. Because the
cold-start time for affected subsystems was never measured at current
scale, the recovery duration is unknown until it completes — and it
completes in hours, not minutes.

### Forces

- **[[reliability-vs-velocity]]** — adding parameter validation (a
  hard cap on "remove N servers") slows the operator workflow; the cap
  must be derived from current system state (minimum redundancy threshold)
  which changes as the system scales. Without validation, operators move
  fast; with it, they are protected against typos at the cost of needing
  the cap kept accurate.
- **[[recovery-time-vs-redundancy-cost]]** — the index rebuild time
  was unknown because the subsystem had grown well beyond its original
  design; no one had measured or rehearsed the full cold-start at current
  scale. Fast recovery requires *rehearsed* cold-starts — which cost
  engineering time that competes with feature work. *This force opposes
  the solution*: rehearsing cold-starts on a system the size of S3's
  INDEX subsystem is expensive and disruptive.
- **[[consistency-vs-availability]]** — Amazon S3's standard consistency
  model (at the time, eventual read-after-write) meant that partial
  availability during the INDEX rebuild was mechanically impossible: the
  INDEX subsystem must be fully consistent before reads can be served
  correctly. This is why S3 returned hard errors rather than stale data —
  the CAP trade was already locked in by design.

### Solution

Every playbook command that removes or modifies capacity must validate
its quantity argument against the current minimum redundancy threshold
before executing. The validation is mechanical — the tool queries the
current server count and minimum threshold, computes the safe removal
upper bound, and refuses to proceed if the argument exceeds it. The
argument is not trusted to be reasonable; the tool makes it impossible
to accidentally cross the threshold in a single operation.

Separately: the cold-start procedure for every subsystem must be
rehearsed at current operating scale, not at the scale it was designed
at. Rehearsal produces a measured rebuild time that is recorded as a
known RTO quantity. Any subsystem whose rebuild time has never been
measured at current scale is documented as `COLD-START-UNVERIFIED` in
the DR plan and its SLA is marked as unknown.

These are two distinct remedies. The first (argument validation) prevents
crossing the threshold. The second (rehearsed cold-start) bounds the
recovery duration once a threshold crossing occurs by any cause.

### Resulting Context

After applying [[explicit-blast-radius-scope]]:

- A typo in a quantity argument cannot remove enough capacity to cross
  a minimum redundancy threshold in a single command invocation. The
  floor is enforced by the tool, not by operator care.
- Operators who legitimately need to remove more capacity than the safe
  single-operation limit must do so in multiple steps, with explicit
  verification between each — this is the expected friction cost.
- The rehearsed cold-start RTO is now a known number, surfaced in
  incident dashboards. When a threshold crossing occurs (regardless of
  cause), the on-call team knows the expected recovery timeline in advance.
- A new tension emerges: the safe-removal upper bound must be kept
  synchronized with the actual minimum redundancy threshold as the system
  scales. If the bound is stale (set when the system was smaller), it
  may be too conservative. This requires a mechanism to recompute and
  publish the bound whenever system capacity changes materially.

### Pattern surfaced

**[[explicit-blast-radius-scope]]** — *two-star invariant, domain: deployment*

This incident justifies the pattern because: (a) the root cause is a
command that accepted an unconstrained quantity argument with no enforcement
of the impact boundary; (b) the pattern's Solution maps directly to the
remedy ("require explicit scope, refuse wildcards, enforce upper bounds");
(c) the forces in tension are the same as the pattern card's declared
forces (velocity vs. safety vs. rollback speed).

The pattern exists at
`seed-kit/engineering-alexander/patterns/explicit-blast-radius-scope.md`
and currently lists `[[google-2019-config-push-gce]]` and
`[[cloudflare-2019-regex-cpu]]` as Examples. This incident (AWS S3 2017)
is a *third independent instance* from a third distinct system (object
storage, not CDN or network). Adding it promotes the pattern toward two-star
confidence: the same forces appear in runtime compute (Cloudflare), network
configuration (Google GCE), and storage operations (Amazon S3). The remedy
statement is the same in all three: make the scope explicit and enforce it
mechanically.

Note: `[[thundering-herd]]` also references `[[aws-s3-2017-us-east-1]]`
(in `seed-kit/engineering-alexander/patterns/thundering-herd.md`, line 31).
The thundering-herd dynamic was a *contributing factor* after the threshold
crossing: multiple clients retried simultaneously as S3 INDEX was rebuilding.
It is not the primary root cause. Per the judgment rule in `prompts.md`:
"Keep one primary cause per incident. Contributing factors are their own
section, not additional root causes."

### Pattern-language cluster

**Recovery Path Integrity**

This cluster groups patterns whose common problem is: *the path an
operator takes to recover from a failure is itself unreliable, unmeasured,
or dependent on the system that has failed*. Members:

| Pattern | Mechanism |
|---------|-----------|
| [[out-of-band-recovery-channel]] | recovery path is independent of failed data plane |
| [[control-plane-in-band-dependency]] | names the anti-pattern the above resolves |
| [[validated-not-just-existing-backup]] | cold-start RTO is measured, not assumed |
| [[thundering-herd]] | retry storms after recovery must be bounded |

Four patterns, three domains (network, storage, runtime). Satisfies
`lens.yaml` threshold `cluster_member_min: 3`. The cluster name describes
the problem space ("recovery path integrity"), not an arbitrary theme.

These patterns compose in sequence: `[[control-plane-in-band-dependency]]`
names the structural failure mode → `[[out-of-band-recovery-channel]]`
resolves it → `[[validated-not-just-existing-backup]]` ensures the
cold-start path actually works → `[[thundering-herd]]` addresses what
happens when clients reconnect after recovery. Each pattern's resulting
context is a precondition for the next pattern's context — this is the
composing property Alexander requires for a pattern language.

The AWS S3 2017 incident sits at the boundary of *both* clusters:
it justifies `[[explicit-blast-radius-scope]]` (Blast-Radius Containment
at Change Time) because the root cause is an unconstrained removal
command, and it is referenced by `[[validated-not-just-existing-backup]]`
analog logic and `[[thundering-herd]]` (Recovery Path Integrity). An
incident at a cluster boundary is expected and desirable — it shows
the two clusters are adjacent, not duplicated.

### Authority anchors

| Field | Value |
|-------|-------|
| `postmortem_url` | https://aws.amazon.com/message/41926/ |
| `service_name` | Amazon S3 |

No CVE applies (this is an operational error, not a vulnerability). No
RFC applies (the pattern is not about honoring or deviating from a
protocol contract). The `service_name` anchor uses the vendor's canonical
spelling: "Amazon S3", not "S3" or "AWS S3".

### Back-references (what this unlocks in the vault)

- **[[thundering-herd]]** lists `[[aws-s3-2017-us-east-1]]` in its
  Examples (`seed-kit/engineering-alexander/patterns/thundering-herd.md`,
  line 31). This example clarifies that the thundering-herd dynamic in
  the S3 incident was *post-recovery* client reconnection, not the
  triggering cause. A reader of the thundering-herd card should understand
  that the S3 example demonstrates the pattern as a *secondary failure
  cascade*, not a primary root cause — this distinction matters when
  deciding which patterns to apply to a new incident.
- **[[gitlab-2017-db-delete]]** — that incident's primary pattern is
  `[[validated-not-just-existing-backup]]`: GitLab's backup scripts ran
  but the restores had never been verified. AWS S3 2017's secondary lesson
  (the cold-start time was unknown because the procedure was never rehearsed
  at current scale) is the same pattern applied to cold-start RTO instead
  of backup integrity. Both incidents demonstrate that "we have a procedure"
  is not equivalent to "the procedure works at current scale." The two
  incidents together strengthen `[[validated-not-just-existing-backup]]`
  to cover cold-start rehearsal, not only backup restoration.
- **[[control-plane-in-band-dependency]]** references
  `[[aws-s3-2017-us-east-1]]` in its Examples
  (`seed-kit/engineering-alexander/patterns/control-plane-in-band-dependency.md`,
  line 29). During the S3 rebuild, internal AWS tooling that depended on
  S3 for configuration and artifact storage was also degraded, extending
  the time to triage. This makes S3 2017 a weaker example of
  `[[control-plane-in-band-dependency]]` than Facebook 2021 BGP (where
  the dependency completely blocked physical access) — worth noting so a
  reader calibrates the severity gradient within the pattern.

### Problem depth

**Captured**: the forces are genuinely in tension — rehearsing cold-starts
at production scale costs real engineering time, and the card names this
cost rather than treating it as a free improvement. The Resulting Context
section surfaces the new synchronization problem (the safe-removal cap
must track system growth) rather than claiming the pattern makes the
system safe forever.

**Not captured**: the incident also reveals that the playbook had no
peer-review step before execution — a process control gap rather than a
tool design gap. This is a valid contributing factor but does not generate
a new pattern on its own (process review is already implied by
`[[explicit-blast-radius-scope]]`'s two-step confirmation requirement).
Naming it here prevents it from being inflated into a separate pattern
card without a second independent instance.

### Traps avoided

1. **Did not mistake the contributing factor for the root cause.** The
   thundering-herd client reconnection storm is real but secondary. The
   card names `[[explicit-blast-radius-scope]]` as the primary pattern and
   explicitly labels `[[thundering-herd]]` as a contributing factor. Merging
   them into one pattern would have violated the "one primary cause" rule
   from `prompts.md`.
2. **Did not create a new `[[unrehearsed-cold-start]]` pattern.** The
   incident's original vault file proposes `[[unrehearsed-cold-start]]`
   as a slug. This card does not promote it, because `[[validated-not-just-existing-backup]]`
   already covers the same remedy (rehearsed verification of recovery
   procedures). Creating a new pattern card for the same remedy applied
   to a slightly different artifact (backup restore vs. cold-start) would
   violate DRY at the pattern level. The existing pattern's scope should
   be extended, not split.
3. **Did not write the Solution as a runbook.** The Solution does not say
   "step 1: query the minimum redundancy threshold; step 2: subtract the
   requested removal count; step 3: if negative, abort." It says "the
   tool validates the argument against the threshold before executing."
   An engineer at a different company can implement this in their own
   capacity-management tooling without referring to Amazon's internal
   systems.

---

## How these examples calibrate Claude's behavior

When a new incident arrives under this lens, follow this shape:

1. **Abstract before you name.** Strip vendor names, product names, and
   version numbers from the Context section. If the pattern card cannot
   be read by an engineer who has never used that vendor, the extraction
   failed. Both examples above restate the system shape (WAF rule evaluation,
   capacity management playbook) without depending on knowing what
   "Cloudflare" or "Amazon S3" means.

2. **Forces must include at least one that opposes the solution.** Both
   examples above name a force that pushes *against* the remedy:
   Cloudflare's PCRE expressiveness loss, S3's cold-start rehearsal cost.
   A card without an opposing force is a recipe, not a pattern — it
   describes what to do without explaining why someone might not do it.

3. **Pick one primary pattern per incident.** Both incidents contain
   multiple remedies. Both cards name one primary pattern and route the
   secondary remedies to existing pattern files by name. Do not create a
   new pattern slug unless it cannot be housed in an existing card.

4. **Back-references are specific claims, not category buckets.** Each
   back-reference above makes a precise statement about *how* two patterns
   or incidents relate ("the thundering-herd in S3 2017 is post-recovery,
   not primary cause — this matters when diagnosing new incidents"). A
   back-reference that says only "related to [[thundering-herd]]" carries
   no information.

5. **Resulting Context names new tensions.** After applying a pattern, the
   world is not problem-free. Both cards name the new friction introduced:
   RE2/PCRE capability matrix (Cloudflare), stale-cap synchronization
   problem (S3). A Resulting Context that claims "the system is now safe"
   is dishonest and useless.

6. **Pattern quality rank is observation, not aspiration.** `[[per-operation-cpu-budget]]`
   is one-star because it has one vault instance; `[[explicit-blast-radius-scope]]`
   is two-star because it has three independent instances across three domains.
   Do not promote a pattern to two-star because it feels important — promote
   it when the second independent instance arrives.

---

## Anti-patterns these examples guard against

- **The post-mortem précis trap**: a Context section that summarizes the
  vendor's published incident report instead of abstracting from it. Both
  examples above deliberately restate the *system shape* (per-request rule
  evaluation, capacity management tooling), not the specific Cloudflare or
  Amazon events. The test: can an engineer at a company that has never
  used those products recognize the pattern?

- **Root-cause inflation**: both incidents contain 3-5 contributing factors
  if you count carefully. Both examples name one primary pattern and
  explicitly relegate the others to contributing-factor status with
  specific wikilinks to the patterns that cover them. Do not create new
  pattern slugs for contributing factors without independent instances.

- **Runbook contamination**: the Solution sections above do not say "step
  1, step 2, step 3." They state a design constraint ("enforce the argument
  against current threshold before executing") that any implementation can
  satisfy. If you find yourself numbering steps in a Solution, stop —
  you are writing a runbook, not a pattern.

- **Cluster name vagueness**: "Blast-Radius Containment at Change Time" ✓
  names the problem space. "Resilience patterns" ✗ names nothing. If the
  cluster name could apply to any three patterns in the vault, it is not
  a cluster name — it is a tag.

- **Wikilink speculation**: every [[wikilink]] in both examples resolves
  to a file that exists in `seed-kit/engineering-alexander/`. The one
  slug proposed by the original incident file (`[[unrehearsed-cold-start]]`)
  is explicitly named and explicitly deferred — it is not silently dropped,
  and it is not promoted without a second instance.
