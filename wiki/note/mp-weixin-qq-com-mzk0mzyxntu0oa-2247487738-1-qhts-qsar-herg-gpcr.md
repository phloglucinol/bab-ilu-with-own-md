---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk0mzyxntu0oa-2247487738-1-qhts-qsar-herg-gpcr
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk0mzyxntu0oa-2247487738-1-qhts-qsar-herg-gpcr.md
bloom: analyze
concepts:
  - "[[early-safety-gating]]"
  - "[[qhts-plus-qsar]]"
  - "[[target-activity-safety-coupling]]"
  - "[[consensus-tox-filter]]"
layer_1_bolds:
  - "**整合qHTS和QSAR模型以识别安全的GPCR靶向化合物：关注hERG依赖性心脏毒性。**"
  - "**hERG毒性在GPCR药物中的普遍性。**"
  - "**双模型建模策略。**"
  - "**共识策略。**"
  - "**实验验证结果。**"
layer_2_fragments:
  - "**把安全性筛查前移到命中发现阶段**"
  - "**qHTS 给出现实活性分布而 QSAR 负责外推**"
  - "**双模型共识比单模型更像真实决策**"
  - "**GPCR 活性与 hERG 风险必须同时看**"
  - "**外部验证决定模型能否离开训练集**"
layer_3_thesis: "这篇的关键不是又做了一个 hERG 分类器，而是把 GPCR 活性筛选和心脏毒性规避放进同一早期决策面板里，让“先命中再补安全”这种串行流程变得站不住脚。"
status: complete
---

# qHTS 与 QSAR 联用把 hERG 风险前移成先导筛选条件

## Layer 1 — bold key sentences

- **整合qHTS和QSAR模型以识别安全的GPCR靶向化合物：关注hERG依赖性心脏毒性。**
- **hERG毒性在GPCR药物中的普遍性。**
- **双模型建模策略。**
- **共识策略。**
- **实验验证结果。**

## Layer 2 — bold fragments

- **把安全性筛查前移到命中发现阶段**
- **qHTS 给出现实活性分布而 QSAR 负责外推**
- **双模型共识比单模型更像真实决策**
- **GPCR 活性与 hERG 风险必须同时看**
- **外部验证决定模型能否离开训练集**

## Layer 3 — one-sentence thesis

这篇的关键不是又做了一个 hERG 分类器，而是把 GPCR 活性筛选和心脏毒性规避放进同一早期决策面板里，让“先命中再补安全”这种串行流程变得站不住脚。

## Concepts (tier_1_atoms)

- `[[early-safety-gating]]`：安全性不是项目后段的过滤器，而是命中阶段的入口条件。
- `[[qhts-plus-qsar]]`：高通量实验和结构模型各管一半现实，合在一起才形成可用筛选面。
- `[[target-activity-safety-coupling]]`：对 GPCR 项目来说，靶点活性和 hERG 风险天然耦合，不能分开优化。
- `[[consensus-tox-filter]]`：共识判定比单模型概率更接近研发现场的“保守通过”逻辑。

## Back-references

- `[[mp-weixin-qq-com-mzkwmji4odg2na-2247484368-1-jcim-admet]]`：ADMET 去噪那篇关心标签质量，这篇则说明即便标签质量足够，真正难的是把毒性判断接到特定靶点任务上，而不是做一个通用 ADMET 分数。
- `[[mp-weixin-qq-com-mzk4oda4mjqynw-2247485518-1-cyp3a4-p-gp-pk-pk]]`：非线性 PK 那篇说明“安全/暴露问题”常在药代阶段暴露；这篇把另一类风险前移，提醒我早期筛选真正该做的是多维度淘汰，而不是只盯 potency。
- `[[mp-weixin-qq-com-mzkwodyymdqwoa-2247499876-1-nature-ai-gpcr]]`：GEM 那篇展示了 GPCR 调控可以跳出口袋设计；这篇则从反面说明，哪怕机制创新，GPCR 项目仍绕不开通道毒性这类老问题，所以安全性过滤必须跟着创新一起前移。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzk0mzyxntu0oa-2247487738-1-qhts-qsar-herg-gpcr.md`
- Type: markdown
- Kind: other
