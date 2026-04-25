---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mza3mzi4mjgzmw-2651029279-2-transformer-mamba
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mza3mzi4mjgzmw-2651029279-2-transformer-mamba.md
bloom: analyze
concepts:
  - architecture-translation
  - intermediate-representation-distillation
  - structural-alignment-before-compression
layer_1_bolds:
  - 能不能不重训，把 Transformer 的能力，直接搬到 Mamba 上？
  - 先造一个“中间形态”，让 Transformer 先变成一个更简单、更接近 Mamba 的版本。再从这个中间版本，转成 Mamba。
  - 两阶段蒸馏在这里不是优化，而是绕不过去的结构性条件。
layer_2_fragments:
  - 先对齐表达方式再做结构转换
  - Hedgehog作为线性注意力过渡层
  - 轻S1重S2的数据分配
  - 从平方成本迁移到线性成本
layer_3_thesis: 架构替换最难的不是把参数搬过去，而是先找到一个两边都能说得通的中间表示，否则压缩就会退化成失真。
status: complete
---

# mp-weixin-qq-com-mza3mzi4mjgzmw-2651029279-2-transformer-mamba

## Layer 1 — bold key sentences

- **能不能不重训，把 Transformer 的能力，直接搬到 Mamba 上？**
- **先造一个“中间形态”，让 Transformer 先变成一个更简单、更接近 Mamba 的版本。再从这个中间版本，转成 Mamba。**
- **两阶段蒸馏在这里不是优化，而是绕不过去的结构性条件。**

## Layer 2 — bold fragments

- **先对齐表达方式再做结构转换**
- **Hedgehog 作为线性注意力过渡层**
- **轻 S1 重 S2 的数据分配**
- **从平方成本迁移到线性成本**

## Layer 3 — one-sentence thesis

架构替换最难的不是把参数搬过去，而是先找到一个两边都能说得通的中间表示，否则压缩就会退化成失真。

## Concepts (tier_1_atoms)

- [[architecture-translation]]：把一种架构的能力转译到另一种架构，而不是从头重训。
- [[intermediate-representation-distillation]]：蒸馏不是一步到位，而是先蒸出可过渡的中间表示。
- [[structural-alignment-before-compression]]：表达结构不对齐时，任何压缩都会先损坏能力。

## Back-references

- [[mp-weixin-qq-com-mzawmjy0odk3nw-2247486028-1-9-ai-ai]]：Boris 那套工作流强调先计划再实现，这篇在模型迁移里给了一个同构版本：先中间表示再结构替换，都是先解决“理解和对齐”，再开始执行。
- [[mp-weixin-qq-com-mze5mte0njg3nq-2247484159-1-jctc]]：柔性晶体预测里也是先用便宜近似做大规模筛选，再把贵算力留到末端精修；这里则是先用中间模块做结构对齐，再进入真正迁移，阶段化不是保守，而是控制风险。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mza3mzi4mjgzmw-2651029279-2-transformer-mamba.md`
- Type: markdown
- Kind: other
