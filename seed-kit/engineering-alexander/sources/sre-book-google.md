---
type: source
seed: true
authors: ["Google SRE team"]
year: 2016
publisher: O'Reilly
url: https://sre.google/books/
domain: operations
---

# Site Reliability Engineering (Google, 2016)

Google 团队把 SRE 实践体系化的权威文本。引入了现在通用的词汇：error budget / SLI / SLO / toil / 非幂等操作 / 蓝图驱动维护。

与这个 lens 的关系：SRE Book 提供 *力* 的词汇（reliability vs velocity, toil vs automation, error budget 作为交易货币），但本身不以 pattern-language 形式组织。这个 lens 的工作之一是把 SRE Book 里反复出现的设计选择抽出来作为 Alexander 风格的模式。

## 核心启发
- 可靠性是一个 *budget*，不是 *目标*
- "Too reliable" 也是一种失败（用户永远假设系统不会挂，那 99.99% 就是不够的）
