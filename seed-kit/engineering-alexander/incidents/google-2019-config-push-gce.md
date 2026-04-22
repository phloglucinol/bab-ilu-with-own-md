---
type: incident
seed: true
service_name: Google Compute Engine
postmortem_url: https://status.cloud.google.com/incident/cloud-networking/19009
occurred: 2019-06-02
duration_minutes: 240
domain: network
---

# Google Cloud 网络事件 (2019-06-02)

一次意图推送给单个集群的网络配置更改，因为配置系统缺乏区域边界验证，被广播给了多个区域。控制面先失联，然后流量重路由到剩余容量过载的区域。

根因：配置推送工具允许超出原设计意图的广播范围；区域隔离是假设而非机制。

## 出现的模式
- [[explicit-blast-radius-scope|显式作用域边界]]
- [[配置即流量|config-push-is-traffic-event]]
- [[control-plane-in-band-dependency|控制面带内依赖]]

## 教训域
- 隔离必须被工具强制，不能靠"约定"
- 降级路径不能依赖正在降级的资源
