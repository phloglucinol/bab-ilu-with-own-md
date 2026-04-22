---
type: pattern
seed: true
star_rating: 2
domain: deployment
forces: [deploy-speed, consistency, rollback-cost]
---

# 部署原子性验证 (deploy-atomicity-verification)

## Context
任何多节点部署：滚动更新、蓝绿、金丝雀。节点版本在部署过程中必然短暂不一致。

## Problem
"部署完成"被定义为"最后一个节点的命令返回成功"，而不是"所有节点在同一个版本上"。版本漂移的节点（stale deployment）可以激活死代码路径或破坏新协议。

## Forces
- 部署速度：严格一致性检查延长 deploy pipeline
- 一致性：但不一致是 bug 的温床
- 回滚成本：漂移节点让回滚也不完全

## Solution
部署步骤的最后一步是 *显式版本一致性验证*：查询每个注册节点的实际运行版本，拒绝声明"deployed"直到所有节点报告同一 SHA。未更新的节点被踢出 LB 而不是静默带着旧版本服务。

## Resulting context
部署时间略长，但没有"7/8 成功"这种半失败状态。

## Examples
- [[knight-capital-2012|Knight Capital 部署事故 (2012-08-01)]]
