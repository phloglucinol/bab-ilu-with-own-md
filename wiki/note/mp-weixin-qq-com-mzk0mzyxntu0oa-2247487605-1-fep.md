---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk0mzyxntu0oa-2247487605-1-fep
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk0mzyxntu0oa-2247487605-1-fep.md
bloom: apply
concepts:
  - atom-typing-semantics
  - mapping-policy-must-follow-force-field
  - sequential-vs-chemical-typing
  - alignment-before-mapping
layer_1_bolds:
  - "不同力场对原子类型的编码方式存在本质差异，这直接影响了映射算法中是否应该使用原子类型作为匹配条件。"
  - "这类力场的原子类型本质上是分子内部的顺序标识符，不编码化学环境信息。"
  - "FEP映射策略：必须跳过原子类型检查（或者真去检查该atom type的参数），仅使用距离、元素和电荷进行匹配。"
  - "这类力场的原子类型编码了化学环境和连接模式，相同类型的原子在不同分子中具有相似的化学性质。"
  - "FEP映射策略：应该使用原子类型检查作为额外的匹配条件。类型相同意味着化学环境相似，可以提高映射的准确性和化学合理性。"
layer_2_fragments:
  - "原子类型是否携带化学语义"
  - "顺序编号型不能直接拿来做等价约束"
  - "化学环境型适合加入类型一致性检查"
  - "映射规则必须随力场而变"
  - "错误映射会把后续 FEP 全部带偏"
layer_3_thesis: "FEP 映射里最容易被忽略的前提是：原子类型从来不是通用语义，它是否能当匹配约束，取决于这个力场究竟在编码顺序还是编码化学环境。"
status: complete
---

# mp-weixin-qq-com-mzk0mzyxntu0oa-2247487605-1-fep

## Layer 1 — bold key sentences

- **不同力场对原子类型的编码方式存在本质差异，这直接影响了映射算法中是否应该使用原子类型作为匹配条件。**
- **这类力场的原子类型本质上是分子内部的顺序标识符，不编码化学环境信息。**
- **FEP映射策略：必须跳过原子类型检查（或者真去检查该atom type的参数），仅使用距离、元素和电荷进行匹配。**
- **这类力场的原子类型编码了化学环境和连接模式，相同类型的原子在不同分子中具有相似的化学性质。**
- **FEP映射策略：应该使用原子类型检查作为额外的匹配条件。类型相同意味着化学环境相似，可以提高映射的准确性和化学合理性。**

## Layer 2 — bold fragments

- **原子类型是否携带化学语义**
- **顺序编号型不能直接拿来做等价约束**
- **化学环境型适合加入类型一致性检查**
- **映射规则必须随力场而变**
- **错误映射会把后续 FEP 全部带偏**

## Layer 3 — one-sentence thesis

FEP 映射里最容易被忽略的前提是：原子类型从来不是通用语义，它是否能当匹配约束，取决于这个力场究竟在编码顺序还是编码化学环境。

## Concepts (tier_1_atoms)

- `[[atom-typing-semantics]]`：这篇抓住的不是某个具体力场，而是“atom type 到底表达什么”的语义问题；只有先回答这个，映射策略才站得住。
- `[[mapping-policy-must-follow-force-field]]`：映射不是独立算法，它必须服从底层力场的表示法，否则“更严格”的检查反而制造错配。
- `[[sequential-vs-chemical-typing]]`：把 OpenFF / OPLS-AA 与 GAFF / CGenFF 分成两类后，很多映射分歧都能用“编码顺序还是编码环境”解释。
- `[[alignment-before-mapping]]`：文中虽主谈 atom type，但它隐含提醒我：映射判断永远是多信号组合，类型、距离、电荷、构象对齐缺一不可。

## Back-references

- `[[mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe]]`：OpenFE 那篇把 P38 误差追到姿态对齐问题；这篇再往前追一步，说明即便姿态合理，若力场语义被误读，映射本身就会把错误灌进整个热力学循环。
- `[[mp-weixin-qq-com-mzkzmjc1njk0mq-2247485683-1-fep]]`：FEP Ω 试图把复杂性后移到 ML 校正层；这篇提醒我有些复杂性不能后移，因为前端映射若破坏了化学等价关系，后处理只是在学习错误输入上的偏差。
- `[[mp-weixin-qq-com-j-chem-theory-comput]]`：如果这篇 JCTC/JCTC 类方法笔记后续补完，它很可能提供更正式的映射或自由能理论框架，让这里的经验性分类上升为可比较的方法学判断。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzk0mzyxntu0oa-2247487605-1-fep.md`
- Type: markdown
- Kind: other
