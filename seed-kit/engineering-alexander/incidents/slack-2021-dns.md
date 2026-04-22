---
type: incident
seed: true
service_name: Slack
postmortem_url: https://slack.engineering/slacks-outage-on-january-4th-2021/
occurred: 2021-01-04
duration_minutes: 180
domain: network
---

# Slack 网络级联失败 (2021-01-04)

节后流量激增触发一个之前隐藏的雷鸣之群：自动扩容拉起新节点，新节点向服务发现注册时大量并发查询压垮了 DNS 层，进而阻塞节点健康检查，更多节点被标记不健康，更多扩容请求。

根因：扩容反馈回路依赖 DNS；DNS 没有按服务分片的容量预留。

## 出现的模式
- [[thundering-herd|雷鸣之群]]
- [[control-plane-in-band-dependency|控制面带内依赖]]
- [[扩容反馈回路断路|autoscale-feedback-loop-breaker]]

## 教训域
- 自动扩容不是救星，是一个会咬人的反馈回路
