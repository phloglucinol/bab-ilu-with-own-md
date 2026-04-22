---
type: incident
seed: true
service_name: Knight Capital
postmortem_url: https://www.sec.gov/litigation/admin/2013/34-70694.pdf
occurred: 2012-08-01
duration_minutes: 45
domain: deployment
---

# Knight Capital 部署事故 (2012-08-01)

新交易功能部署到 8 台生产服务器中的 7 台；第 8 台保留了旧二进制，但同时接收新路由配置。旧代码里一个名字重用的 flag 激活了 8 年前的退役路径，开始以每秒数千次的速度下单。45 分钟损失 \$460M，公司被迫出售。

根因：部署流程没有"所有节点版本一致"的显式验证；代码里的死代码被 flag 复用悄悄唤醒。

## 出现的模式
- [[deploy-atomicity-verification|部署原子性验证]]
- [[dead-code-plus-flag-reuse|死代码 + flag 复用]]
- [[金丝雀指标与业务指标分离|canary-metric-vs-business-metric]]

## 教训域
- 删除代码比保留"以后可能用"的代码安全
- 部署完成不等于部署成功
