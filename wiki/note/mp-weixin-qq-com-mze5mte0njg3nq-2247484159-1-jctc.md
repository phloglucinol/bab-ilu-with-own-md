---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mze5mte0njg3nq-2247484159-1-jctc
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mze5mte0njg3nq-2247484159-1-jctc.md
bloom: analyze
concepts:
  - two-stage-cost-allocation
  - ai-force-field-for-flexible-crystals
  - shortlist-then-quantum-refine
layer_1_bolds:
  - 利用定制的高精度力场完成海量候选结构的快速初筛，仅对排名前100的最有希望的结构进行昂贵的最终优化。
  - 将总体计算成本降低了一个数量级。
  - 提供了一条将第一性原理精度与力场计算效率相结合的通用技术路径。
layer_2_fragments:
  - 先用AI力场做海量初筛
  - 只把贵算力投到前100名
  - 柔性分子晶体难点在分子内形变能
  - 成本分配比单点精度更关键
layer_3_thesis: 复杂材料预测的关键不只是做出更准的模型，而是把不同精度层级的计算预算按筛选阶段重新分配。
status: complete
---

# mp-weixin-qq-com-mze5mte0njg3nq-2247484159-1-jctc

## Layer 1 — bold key sentences

- **利用定制的高精度力场完成海量候选结构的快速初筛，仅对排名前100的最有希望的结构进行昂贵的最终优化。**
- **将总体计算成本降低了一个数量级。**
- **提供了一条将第一性原理精度与力场计算效率相结合的通用技术路径。**

## Layer 2 — bold fragments

- **先用 AI 力场做海量初筛**
- **只把贵算力投到前100名**
- **柔性分子晶体难点在分子内形变能**
- **成本分配比单点精度更关键**

## Layer 3 — one-sentence thesis

复杂材料预测的关键不只是做出更准的模型，而是把不同精度层级的计算预算按筛选阶段重新分配。

## Concepts (tier_1_atoms)

- [[two-stage-cost-allocation]]：把便宜模型和昂贵模型按阶段编排，而不是二选一。
- [[ai-force-field-for-flexible-crystals]]：用高精度机器学习力场处理柔性晶体的大规模候选。
- [[shortlist-then-quantum-refine]]：先形成可信 shortlist，再用量子精修完成排序。

## Back-references

- [[mp-weixin-qq-com-first-in-class]]：METL把模拟样本当成实验预算替代品，这篇把 AI 力场当成量子算力替代品；两者都是把昂贵信息后置。
- [[mp-weixin-qq-com-mza3mzi4mjgzmw-2651029279-2-transformer-mamba]]：两阶段蒸馏是为了结构迁移不崩，这里的两阶段筛选是为了成本不炸；分阶段不是折中，而是把不同工具放到最适合的位置。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mze5mte0njg3nq-2247484159-1-jctc.md`
- Type: markdown
- Kind: other
