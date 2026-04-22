---
type: incident
seed: true
service_name: Meta (Facebook)
postmortem_url: https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/
occurred: 2021-10-04
duration_minutes: 380
domain: network
---

# Facebook BGP 撤回事件 (2021-10-04)

一个常规的骨干网容量审计命令在审计逻辑中有 bug，撤回了所有 BGP announcement — Facebook 网络从互联网消失。恢复依赖物理到场，而进入数据中心的门禁系统和追溯权限本身依赖于那个已撤回的网络。

根因：控制平面带内依赖 + 审计工具缺少 dry-run 机制 + 物理安保与网络耦合。

## 出现的模式
- [[out-of-band-recovery-channel|带外恢复路径]]
- [[审计命令的 dry-run 契约|audit-command-dry-run-contract]]
- [[control-plane-in-band-dependency|控制面带内依赖]]

## 教训域
- "BGP 故障"不是网络问题，是治理问题
