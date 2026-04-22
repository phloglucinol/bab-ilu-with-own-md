---
type: force
seed: true
---

# 一致性 vs 可用性 (consistency-vs-availability)

CAP 定理的工程化身。网络分区发生时，要么拒绝写保持一致，要么接受写容忍分歧。这个 force 渗透每一个分布式存储 pattern：quorum、gossip、CRDT、主动-主动 vs 主动-被动。

系统通常不是在一端或另一端，而是在 *不同故障边界下有不同权衡*。

## 相关模式
- [[脑裂后的权威重建|post-split-brain-authority]]
- [[优雅降级到只读|graceful-readonly-fallback]]
