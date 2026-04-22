---
type: pattern
seed: true
star_rating: 2
domain: deployment
forces: [velocity, safety, rollback-speed]
---

# 显式作用域边界 (explicit-blast-radius-scope)

## Context
任何"把改动推向生产"的工具：配置推送、特性开关翻转、部署滚动、审计命令。

## Problem
当工具的默认作用域没有显式边界，小错误产生全网影响；"只打算改一个集群"最后改了所有集群。

## Forces
- 速度：全网推送是一条命令，分批推送是 N 条
- 安全：边界越窄，爆炸半径越小
- 回滚速度：更细粒度作用域 = 更细粒度回滚

## Solution
每一个"推送"命令都要求显式 `--scope` 参数，无默认值。CLI 拒绝解释 wildcards（除非再加 `--i-really-mean-everything`）。日志记录实际作用域 vs 预期作用域的差异。

## Resulting context
偶然全网推送变为不可能；故意全网推送变为两步确认。代价是每个 operator 要学 scope 语法。

## Examples
- [[google-2019-config-push-gce|Google Cloud 网络事件 (2019-06-02)]]
- [[cloudflare-2019-regex-cpu|Cloudflare 全球 502 事件 (2019-07-02)]]
