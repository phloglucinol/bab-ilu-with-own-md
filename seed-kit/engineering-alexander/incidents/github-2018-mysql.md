---
type: incident
seed: true
service_name: GitHub
postmortem_url: https://github.blog/2018-10-30-oct21-post-incident-analysis/
occurred: 2018-10-21
duration_minutes: 1440
domain: storage
---

# GitHub 24 小时降级 (2018-10-21)

一次 43 秒的跨海岸网络中断让 East/West MySQL 集群各自选主。Orchestrator 没设计双集群合并协议，用户开始在两边写数据。后续 24 小时用于手工仲裁冲突写。

根因：主动-主动冲突解决被设计为"理论上不会发生"，所以没有机制。

## 出现的模式
- [[脑裂后的权威重建|post-split-brain-authority]]
- [[冲突不会发生的假设|conflict-never-happens-assumption]]
- [[优雅降级到只读|graceful-readonly-fallback]]

## 教训域
- 网络分区在分布式系统里不是"事件"，是"状态"
