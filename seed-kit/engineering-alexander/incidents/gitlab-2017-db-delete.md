---
type: incident
seed: true
service_name: GitLab.com
postmortem_url: https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/
occurred: 2017-01-31
duration_minutes: 360
domain: storage
---

# GitLab.com 数据库删除事件 (2017-01-31)

一名工程师在响应复制延迟的疲劳末尾误以为在 secondary 上操作，实际在 primary 上执行了 `rm -rf`。5 个备份方案中 4 个要么没运行要么不可用；恢复依赖某个 LVM 快照的幸存副本。

根因：备份存在 ≠ 备份可恢复；生产/副本的 shell prompt 视觉无差异。

## 出现的模式
- [[validated-not-just-existing-backup|验证过的备份]]
- [[危险环境的视觉标记|danger-visual-signaling]]
- [[疲劳时段的只读降级|fatigue-hours-readonly-mode]]

## 教训域
- "我们有备份"是一个技术债务指标，不是一个安全承诺
