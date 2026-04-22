---
type: pattern-card-template
pattern: "[[out-of-band-recovery-channel]]"
lens: engineering-alexander
seed: true
---

# 带外恢复通道 (Out-of-Band Recovery Channel) — Pattern Card Template

## Context

This pattern applies to any system whose operational plane — the tooling used
to diagnose, reconfigure, or restart the system — shares critical dependencies
with the data plane that serves production traffic. The shared dependencies
typically include the same network fabric, the same DNS infrastructure, the
same authentication service, and sometimes the same physical access control
system. The pattern is triggered when a fault in the data plane is severe
enough to also sever the operational plane.

## Problem

When the data plane fails, the operational plane must be available to execute
recovery. If both planes share the same infrastructure, the failure that most
urgently demands intervention is precisely the failure that prevents
intervention. The recursive dependency bottoms out at the physical layer —
an engineer who cannot SSH in must drive to the data center, and the data
center whose door lock runs on the same network that just failed presents
a second locked door.

### Forces in tension

- [[out-of-band-recovery-channel]] — maintaining a separate operational path
  requires dedicated resources (an LTE uplink, a hardware token, a console
  server) that are idle 99% of the time; the cost is real and the benefit is
  invisible until the one moment it matters.
- [[recovery-time-vs-redundancy-cost]] — faster recovery requires idle spare
  capacity; every organization must decide where on this axis to sit.
- Operational complexity — a rarely-used recovery path is a path that has not
  been rehearsed; an un-rehearsed path fails at the worst possible time.

## Forces

- [[out-of-band-recovery-channel]] — the recovery path must be structurally
  independent of the failing system; shared dependencies at any layer
  (network, auth, physical) propagate the fault into the recovery path.
- [[recovery-time-vs-redundancy-cost]] — a fully independent control plane
  (dedicated fiber, satellite uplink, offline auth tokens) eliminates shared
  failure modes but carries ongoing maintenance cost proportional to the
  degree of independence.
- Rehearsal decay — a control path that is never exercised accumulates
  configuration drift; by the time it is needed, certificates have expired,
  VPN configs have rotated, and nobody on the current on-call rotation has
  ever used it.

## Solution

Define an explicit out-of-band recovery path for every system tier that is
critical enough to require emergency intervention. The path must be independent
at each layer: a separate network (LTE modem, dedicated management VLAN, or
satellite link), a separate authentication source (hardware security key with
offline capability, break-glass credentials stored in a physically secured
vault), and a separate bootstrap channel (serial console server accessible
without the primary network). Document this path in the DR runbook. Include a
quarterly drill in which the on-call rotation actually exercises the path
end-to-end and records the outcome. Flag the path as `UNTESTED` in the runbook
if the drill has not been completed in the past six months; do not count it
toward RTO commitments.

## Resulting Context

When the data plane fails completely, the operational team reaches the system
within a predictable time window — typically the length of one authentication
step and one network hop — rather than waiting for physical access. The
out-of-band path introduces its own maintenance burden: the dedicated channel
must be kept current with certificate rotations, key issuance, and firmware
updates. Organizations that invest in the path but not in rehearsal will
discover, at the worst moment, that their "independent" path has silently
re-acquired a shared dependency.

## Examples (from vault)

- [[facebook-2021-bgp]] — BGP withdrawal made the network unreachable; physical
  access required door-lock systems that also depended on the withdrawn network;
  recovery required hours of physical escalation that a functioning out-of-band
  channel would have compressed to minutes.
- [[aws-s3-2017-us-east-1]] — metadata service degradation limited operational
  visibility; pre-positioned out-of-band tooling was cited as a contributing
  factor in reducing total incident duration.

## Traps / Counter-forces

- **The "we have a VPN" fallacy**: a VPN that terminates in the same data center
  it is meant to recover does not constitute an out-of-band path; it is an
  in-band path with extra steps.
- **Credentials stored in the system being recovered**: if the break-glass
  password is in the secrets manager that runs in the same VPC as the
  production system, it is not a break-glass credential.
