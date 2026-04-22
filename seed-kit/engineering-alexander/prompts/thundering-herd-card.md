---
type: pattern-card-template
pattern: "[[thundering-herd]]"
lens: engineering-alexander
seed: true
---

# 雷鸣之群 (Thundering Herd) — Pattern Card Template

## Context

This pattern applies to any system where multiple waiters — threads, connections,
clients, autoscaling nodes — block on a shared external event and are released
simultaneously. The trigger is typically a recovery event: a cache miss fills,
a leader is re-elected, a DNS record resolves, or autoscaling launches a cohort
of new nodes. The system shape is one emitter, many synchronized receivers.

## Problem

Synchronized release converts a single recovery event into a second failure.
The downstream target — a service, a database, a DNS resolver — receives a
request spike at exactly the moment it is most fragile, immediately after its
own recovery. The spike overwhelms remaining capacity, triggering further
failures and another round of retries.

### Forces in tension

- [[thundering-herd]] itself: every waiter has a legitimate reason to retry
  immediately; individually rational behavior produces collectively catastrophic
  load.
- [[consistency-vs-availability]] — delaying retries with jitter introduces
  uncertainty about *when* the system will actually reach a consistent state;
  operators lose the ability to predict recovery timing precisely.
- Fairness: bounded random jitter breaks strict FIFO ordering; the first waiter
  to acquire a resource is no longer the one who waited longest.

## Forces

- [[thundering-herd]] — synchronized retry amplifies load at the exact moment
  of recovery, converting a resolvable fault into a second outage.
- [[consistency-vs-availability]] — jitter trades predictable recovery timing
  for reduced peak load; the system becomes available sooner on average but
  later in the worst case.
- Latency vs capacity utilization — random delay extends p99 recovery latency
  by one jitter window while eliminating brief over-capacity spikes.

## Solution

At every point where a waiter blocks on an external event and will retry upon
notification, introduce bounded random jitter before the retry fires. Size the
jitter window to be inversely proportional to downstream capacity: if the
downstream can serve N concurrent requests sustainably, the jitter window
should spread the cohort so that the arrival rate stays below N/2 per second.
Use exponential backoff with jitter (not pure exponential backoff) for
persistent retries. Apply the same principle to autoscaling launch: stagger
health-check registration so new nodes do not all query service discovery
simultaneously.

## Resulting Context

Recovery proceeds smoothly across the cohort rather than in one synchronized
wave. The trade-off is a wider p99 recovery time — the last waiter in the
jitter window finishes later than it would have without jitter. Monitoring must
confirm that jitter is actually distributing load: a poorly seeded RNG or a
clock-synchronized cluster can produce apparent jitter that collapses back into
synchronization at the distribution's tail.

## Examples (from vault)

- [[slack-2021-dns]] — autoscaling cohort overwhelmed DNS simultaneously on
  node registration; jitter on health-check registration would have flattened
  the spike.
- [[aws-s3-2017-us-east-1]] — retry storms from S3 clients amplified the
  initial metadata service degradation; client-side jitter was part of the
  eventual recovery guidance.

## Traps / Counter-forces

- **Pure exponential backoff without jitter**: each client picks a
  deterministic delay based on attempt count; if clients share the same
  start time (e.g. a deployment cohort), they remain synchronized across
  every retry tier. The backoff *looks* like it should help but does not.
- **Jitter applied only at the application layer, not the infrastructure
  layer**: staggering application retries while autoscaling launches nodes
  in synchronized bursts relocates the herd to the infrastructure tier rather
  than eliminating it.
