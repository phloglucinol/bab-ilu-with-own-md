---
type: incident
seed: true
service_name: Amazon S3
postmortem_url: https://aws.amazon.com/message/41926/
occurred: 2017-02-28
duration_minutes: 240
domain: storage
---

# AWS S3 US-EAST-1 服务中断 (2017-02-28)

一个维护团队执行 playbook 时的一个拼错命令，移除了 S3 计费子系统中比预期多得多的服务容量。移除量跨过了两个内部索引子系统的最小冗余阈值，它们都需要从零重建。

根因：子系统规模已经增长到远超最初设计时的假设，但从未演练过完整重启，所以没人知道这需要 4 小时。

## 出现的模式
- [[蓝图驱动的容量移除|playbook-driven-capacity-removal]]
- [[从未演练的完全重启|unrehearsed-cold-start]]
- [[隐式最小冗余阈值|implicit-min-redundancy-threshold]]

## 教训域
- 运维工具需要参数上限验证
- "重启某服务"的耗时必须作为已知量而非未知量
