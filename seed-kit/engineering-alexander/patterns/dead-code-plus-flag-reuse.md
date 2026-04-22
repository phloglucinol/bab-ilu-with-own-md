---
type: pattern
seed: true
star_rating: 1
domain: deployment
forces: [code-cleanliness, feature-flag-expressiveness, safety]
cwe_id: CWE-1164
---

# 死代码 + Flag 复用反模式 (dead-code-plus-flag-reuse)

## Context
一个曾经的功能被下线，但代码路径和对应的 feature flag 都还在 repo 里。后来一个新功能复用了这个 flag 名，期望它"意思一样"。

## Problem
死代码路径被 flag 意外唤醒，以今天完全不合时宜的方式运行（几年前的协议、退役的路由、错误的数据源）。症状看起来像 "flag 工作不正常"，实际是另一段代码被唤醒。

## Forces
- 代码清洁：删代码看起来在"做好事"，但也可能删掉需要回滚的路径
- Flag 表达力：复用名字是一种沟通
- 安全：新旧语义碰撞是 footgun

## Solution
每一个 flag 有明确的 *lifecycle*：`alpha | beta | GA | deprecated | removed`。`removed` 的 flag 从代码中彻底删除（不是"注释掉"），配置中的引用会编译失败。从不复用 flag 名 — 退役的名字永久保留为 sentinel。

## Resulting context
代码比有 flag 保险时更少；偶然唤醒退役路径变为编译错误而非运行时 bug。

## Examples
- [[knight-capital-2012|Knight Capital 部署事故 (2012-08-01)]]
