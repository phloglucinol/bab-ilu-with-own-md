---
type: pattern-language
seed: true
members: 4
domain: network
---

# 部分失败下的韧性 (resilience-under-partial-failure)

系统不是"工作"或"不工作"的二元态 — 真正的分布式系统总是处于某种 *部分* 故障。这个 pattern-language 回答：当一部分子系统挂了，剩余部分如何继续提供价值，而不把自己也拖垮。

## 成员模式
- [[control-plane-in-band-dependency|控制面带内依赖]] — 承认依赖环
- [[out-of-band-recovery-channel|带外恢复通道]] — 切断依赖环
- [[thundering-herd|雷鸣之群]] — 重试不要同步
- [[脑裂后的权威重建|post-split-brain-authority]] — 网络分区是状态

## 核心张力
可用性 ↔ 一致性（CAP 的现实化身）；性能 ↔ 隔离性；简单 ↔ 完备。这些张力不能"解决"，只能按场景加权。

## 适用性
- 所有跨 AZ / 跨区域的生产系统
- 从不单机运行的控制面
- 任何宣称 "99.9%" 以上 SLA 的 API
