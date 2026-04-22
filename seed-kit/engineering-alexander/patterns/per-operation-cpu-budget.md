---
type: pattern
seed: true
star_rating: 1
domain: runtime
forces: [expressiveness, predictability, worst-case-latency]
---

# 每操作 CPU 预算 (per-operation-cpu-budget)

## Context
任何随用户请求流量评估的用户可控逻辑：WAF 规则、ACL、正则、用户脚本、JSON Schema。

## Problem
某一次调用的最坏情况开销 × 全网 QPS = 整个系统下线。单个病态输入可以击穿 CPU。

## Forces
- 表达力：某些需求（灾难性回溯正则、递归 schema）是真的有用
- 可预测性：有界的最坏情况值得牺牲一些表达力
- 最坏延迟：用户不会记得平均延迟，只记得尾部

## Solution
每一个用户可控的 per-request 逻辑都必须在 CPU-time budget 内。正则用 RE2（O(n) 保证），不用 PCRE；循环用迭代 budget；递归限深度。部署 CI 检查每个 rule 的 worst-case CPU，不只是语法。

## Resulting context
用户失去某些表达能力（灾难性回溯的正则不能写了），换来 SLA。

## Examples
- [[cloudflare-2019-regex-cpu|Cloudflare 全球 502 事件 (2019-07-02)]]
