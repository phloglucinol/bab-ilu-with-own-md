---
type: pattern-language
seed: true
members: 3
domain: deployment
---

# 安全部署 (safe-deploys)

"部署上线"的默认路径应该让小错误 *不可能* 变为大事故，让故意的大动作需要两步确认。这个 pattern-language 回答：如何把错误的爆炸半径缩到 operator 能接受的范围。

## 成员模式
- [[explicit-blast-radius-scope|显式作用域边界]] — 默认不全网
- [[deploy-atomicity-verification|部署原子性验证]] — 完成 = 一致
- [[dead-code-plus-flag-reuse|死代码 + Flag 复用反模式]] — 退役即删除

## 核心张力
部署速度 ↔ 验证成本；敏捷 ↔ 可预测性；operator 自主 ↔ 防呆设计。

## 适用性
- 超过 3 个节点的任何 rollout
- 任何带 feature flag 的系统
- 任何有资产与信任之分的生产路径
