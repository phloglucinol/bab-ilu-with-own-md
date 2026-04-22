---
type: pattern-language
seed: true
members: 3
domain: observability
---

# 审计即代码 (audit-as-code)

每一个 "在生产上做事情" 的工具本身都是一段代码，它的契约与代码一致：dry-run 可测、输入有 schema、输出可验证、变更可 diff。不遵守这个契约的运维工具就是 footgun。

## 成员模式
- [[per-operation-cpu-budget|每操作 CPU 预算]] — worst-case 可预测
- [[validated-not-just-existing-backup|验证过的备份]] — 未演练 = 不算
- [[审计命令的 dry-run 契约|audit-command-dry-run-contract]]（待认证）

## 核心张力
operator 便利性 ↔ 工程严谨性；短期节省 ↔ 长期可恢复性。

## 适用性
- 所有 SRE/ops 自研工具
- 任何 CI/CD pipeline 的 release 阶段
- 灾难恢复 playbook 里的每一步命令
