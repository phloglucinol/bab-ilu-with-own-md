---
type: source
seed: true
authors: ["Michael T. Nygard"]
year: 2018
publisher: Pragmatic Bookshelf
edition: 2
domain: resilience-engineering
---

# Release It! 2nd ed. (Nygard, 2018)

在 Alexander 形式上最现代的软件模式集合。明确地区分了 *稳定性模式* (circuit-breaker, bulkhead, timeouts, steady-state) 与 *容量模式* (scaling, pool, cache, governor)。每个模式都有 Context-Problem-Forces-Solution 结构。

与这个 lens 的关系：Nygard 的模式直接可以作为 `wiki/pattern/` 的一星或二星模式的来源。他对 forces 的清晰定义（"操作员不需要知道这个选择的内部原理，但模式要求他监控 X"）是 pattern quality 的 gold standard。

## 核心启发
- Stable 的对立面不是 "fast"，而是 "brittle"
- 每一个稳定性模式的代价是某种 *显式的复杂度*（超时时间、断路器阈值、bulkhead 边界）
