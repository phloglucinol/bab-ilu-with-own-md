---
type: incident
seed: true
service_name: Cloudflare
postmortem_url: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/
occurred: 2019-07-02
duration_minutes: 27
domain: network
---

# Cloudflare 全球 502 事件 (2019-07-02)

一条新部署的 WAF 规则包含一个灾难性回溯的正则表达式。该规则在全球每一个 CPU 上被评估，CPU 使用率瞬间飙到 100%，整个 L7 栈挂掉。

根因：WAF 规则没有 CPU-time budget；部署管道只做语法检查，不做性能回归。

## 出现的模式
- [[用户输入 × 用户规则 × 用户流量的三重乘积|user-input-user-rule-user-traffic-triple]]
- [[per-operation-cpu-budget|每操作 CPU 预算]]
- [[全球单点触发器|global-single-trigger-deploy]]

## 教训域
- 任何"随每请求运行"的代码必须有 worst-case time budget
- 正则引擎的选择（PCRE vs RE2）是一个架构决定，不是库选择
