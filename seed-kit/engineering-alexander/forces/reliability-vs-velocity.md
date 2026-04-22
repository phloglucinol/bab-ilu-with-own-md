---
type: force
seed: true
---

# 可靠性 vs 部署速度 (reliability-vs-velocity)

每一次部署引入故障的风险。限制部署频率可以减少风险，但延迟了价值交付。SRE Book 的 *error budget* 概念把这组张力变成了可交易：budget 没用完就可以快部署，用完了必须冻结。

这不是"解决"张力，是把它变成一个显式的、团队都同意的交易货币。任何部署安全的 pattern 最终都在这条轴上做选择。
