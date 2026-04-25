---
type: question
lens: general-zettelkasten
bridge_hash: 272e0d6a2cf6
atom_a: adaptive-dissociation-path
atom_b: computationally-prioritized-medicinal-chemistry
cluster_a: 5
cluster_b: 15
status: bridge-proposed
---

# Unbridged gap: [[adaptive-dissociation-path]] × [[computationally-prioritized-medicinal-chemistry]]

These two atoms live in different communities (5 vs
15) and share zero tier-0 exemplifiers. Either
a bridge exists and we haven't written it down, or the gap is
real and worth naming.

## Open sub-questions

- [ ] Is there a tier-0 entry that cites both?
- [x] Can a new tier-0 be authored that would bridge them?
- [ ] Or should one of the atoms be renamed / merged?

## Proposed bridge

This bridge is valid, but only if it is framed as mechanism evidence for
computer-aided design rather than as a direct medicinal-chemistry
priority score.

`[[adaptive-dissociation-path]]` exposes dissociation intermediates,
contact-breaking order, and transient ligand-protein interactions. Its
main contribution to `[[computationally-prioritized-medicinal-chemistry]]`
is to help CADD judge binding mode plausibility, key residue
interactions, and pose-level mechanism before a candidate is escalated
into heavier ranking, FEP, synthesis, or SAR interpretation.

In other words, dissociation paths do not replace affinity ranking or
workflow-level prioritization. They provide the structural-mechanistic
evidence that makes those prioritization steps less dependent on a
single static docking pose.

## Candidate tier-0 note

Working title: 解离中间态让计算优先药化不只看静态结合姿态

Core claim:

> 计算优先药化如果只依赖静态 docking pose 或单点亲和力排序，容易把错误结合模式也推进到后续流程；`[[adaptive-dissociation-path]]` 通过暴露解离中间态和关键相互作用断裂顺序，为 CADD 判断结合模式、关键残基和 pose 合理性提供机制证据，从而补强 `[[computationally-prioritized-medicinal-chemistry]]` 的候选优先级判断。

Recommended concepts:

- `[[adaptive-dissociation-path]]`
- `[[computationally-prioritized-medicinal-chemistry]]`
- `[[contact-metric-over-distance]]`
- `[[conformational-ensemble-as-screening-object]]`
