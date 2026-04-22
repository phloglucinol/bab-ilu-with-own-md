---
type: pattern
seed: true
star_rating: 2
domain: network
forces: [recovery-reliability, operational-complexity, cost]
---

# 带外恢复通道 (out-of-band-recovery-channel)

## Context
任何其运维（BGP 广播、控制面 RPC、鉴权）与主业务共用基础设施的系统。

## Problem
主业务挂了 → 运维路径也挂了 → 恢复需要物理到场 → 物理设施鉴权也挂了。递归依赖最终在屋顶门被一条物理钥匙打断。

## Forces
- 可靠性：带外通道在灾难时救命
- 复杂性：维护一个几乎从不使用的通道
- 成本：冗余鉴权源、独立 VPN、物理备件

## Solution
为控制面定义 *带外恢复路径*：独立的网络（LTE/卫星）、独立的鉴权（硬件 token / offline YubiKey）、独立的 bootstrap 通道（console server），并定期演练走这条路径恢复。把这条路径列入 DR plan，在 on-call 培训中走一遍。

## Resulting context
灾难恢复时间从"希望能到数据中心"变为"30 分钟内上线"。

## Examples
- [[facebook-2021-bgp|Facebook BGP 撤回事件 (2021-10-04)]]
- [[aws-s3-2017-us-east-1|AWS S3 US-EAST-1 服务中断 (2017-02-28)]]
