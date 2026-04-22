---
type: pattern
seed: true
star_rating: 2
domain: runtime
forces: [latency, capacity-utilization, fairness]
rfc_id: ""
---

# 雷鸣之群 (thundering-herd)

## Context
多个等待者（线程/连接/客户端）在同一个外部事件发生时被同时唤醒或重试。

## Problem
同步化的唤醒击穿下游容量：刚恢复的服务被风暴打垮，进入二次故障。

## Forces
- 延迟：随机抖动延长了最坏情况恢复时间
- 容量利用：但消除了短暂超容
- 公平性：抖动打破了"先到先服务"

## Solution
在任何 "等到某个事件再做某事"的点上加 *有界随机抖动*。抖动范围与下游容量成反比。重试使用指数退避 + 抖动。

## Resulting context
恢复更平滑，代价是最坏情况延迟增加一个抖动窗口；需要监控抖动是否真的起效（可能被抖动分布的尾部揭穿）。

## Examples
- [[slack-2021-dns|Slack 网络级联失败 (2021-01-04)]]
- [[aws-s3-2017-us-east-1|AWS S3 US-EAST-1 服务中断 (2017-02-28)]]
