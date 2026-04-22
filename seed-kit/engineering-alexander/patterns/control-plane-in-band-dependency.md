---
type: pattern
seed: true
star_rating: 2
domain: network
forces: [operational-simplicity, recoverability, cost]
---

# 控制面带内依赖 (control-plane-in-band-dependency)

## Context
一个分布式系统的控制面（配置推送、运维 RPC、鉴权）与数据面共享网络/DNS/鉴权基础设施。

## Problem
当数据面故障时，恢复所需的控制面也失效。运维团队无法 ssh 进机器、无法推配置、甚至无法进物理机房（门禁系统同样依赖）。

## Forces
- 操作简单性：带外通道额外维护成本
- 可恢复性：所有恢复都依赖于某些基础设施必须不故障
- 成本：冗余带外路径在 99% 时间闲置

## Solution
把恢复路径显式地 *带外*：独立的 VPN + 独立的鉴权源 + 物理层备用 console + 门禁系统硬件钥匙备用。恢复团队每季度演练走带外路径。

## Resulting context
故障时控制面可用，代价是一小组工程师必须定期维护一个"90% 不用"的通道。

## Examples
- [[aws-s3-2017-us-east-1|AWS S3 US-EAST-1 服务中断 (2017-02-28)]]
- [[facebook-2021-bgp|Facebook BGP 撤回事件 (2021-10-04)]]
- [[slack-2021-dns|Slack 网络级联失败 (2021-01-04)]]
