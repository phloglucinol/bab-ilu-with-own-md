---
type: pattern
seed: true
star_rating: 2
domain: storage
forces: [operational-cost, recovery-guarantee, discovery-latency]
---

# 验证过的备份 (validated-not-just-existing-backup)

## Context
任何声称有"备份"的存储系统。备份策略可能有很多条（LVM 快照、S3 同步、复制到 DR site、磁带归档）。

## Problem
"我们有备份" ≠ "我们可以恢复"。Backup 静默失败的常见模式：快照脚本报告成功但实际没运行；拷贝到了不可读格式；恢复流程从未被演练所以没人知道它不工作。

## Forces
- 运维成本：定期演练恢复需要人力
- 恢复保证：只有演练过的备份是真备份
- 发现延迟：未演练的备份会在最需要时暴露失败

## Solution
每一条备份路径必须有 *恢复演练*，至少每季度一次。演练输出一个 SHA/字节数报告，必须匹配源。未演练的路径在文档中标记 `UNTESTED`，不算入 RTO 计算。

## Resulting context
备份数量减少（一些路径会被发现是假的），但数字是真的。

## Examples
- [[gitlab-2017-db-delete|GitLab.com 数据库删除事件 (2017-01-31)]]
