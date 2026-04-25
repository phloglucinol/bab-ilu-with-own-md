---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkyntqznzkzoq-2247485660-1-jcim-tabpfn
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkyntqznzkzoq-2247485660-1-jcim-tabpfn.md
bloom: analyze
concepts:
  - small-data-foundation-model
  - tabular-prior-over-feature-engineering
  - ood-first-evaluation
  - training-free-predictor
layer_1_bolds:
  - TabPFN 为药物发现中的表格数据建模提供了一种全新的解决思路。
  - 其无需训练、对特征不敏感、在小数据和分布偏移场景下表现优异。
  - 基础模型正在从自然语言和图像领域，逐步扩展到表格数据这一长期被忽视但极其重要的方向。
  - 在数据始终有限、问题却不断复杂的药物发现领域，这种范式转变或许正是突破瓶颈的关键所在。
layer_2_fragments:
  - 表格基础模型进入药物发现
  - 小数据优先于大模型崇拜
  - 特征工程依赖被削弱
  - OOD 场景更接近真实研发
layer_3_thesis: TabPFN 的意义不是又赢了一张 leaderboard，而是它把“先验来自大规模预训练而不是当前任务训练”这件事带进了药物发现里最常见的表格小数据场景。
status: complete
---

# 小数据药研任务开始吃到 foundation model 的红利

## Layer 1 — bold key sentences

- **TabPFN 为药物发现中的表格数据建模提供了一种全新的解决思路。**
- **其无需训练、对特征不敏感、在小数据和分布偏移场景下表现优异。**
- **基础模型正在从自然语言和图像领域，逐步扩展到表格数据这一长期被忽视但极其重要的方向。**
- **在数据始终有限、问题却不断复杂的药物发现领域，这种范式转变或许正是突破瓶颈的关键所在。**

## Layer 2 — bold fragments

- **表格基础模型进入药物发现**
- **小数据优先于大模型崇拜**
- **特征工程依赖被削弱**
- **OOD 场景更接近真实研发**

## Layer 3 — one-sentence thesis

TabPFN 的意义不是又赢了一张 leaderboard，而是它把“先验来自大规模预训练而不是当前任务训练”这件事带进了药物发现里最常见的表格小数据场景。

## Concepts (tier_1_atoms)

- [[small-data-foundation-model]]：预训练先验开始覆盖小样本监督任务。
- [[tabular-prior-over-feature-engineering]]：模型先验替代一部分手工特征工程。
- [[ood-first-evaluation]]：真正值得看的不是 IID 准确率，而是分布偏移下的稳健性。
- [[training-free-predictor]]：预测器的价值来自少训练甚至免训练带来的低摩擦部署。

## Back-references

- [[mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025]]：那篇说明 benchmark 要先去泄漏，这篇说明在干净任务上小数据基础模型才有真实意义。
- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim]]：BALM 把 foundation model 用到配体-蛋白序列，这篇把同一趋势推进到表格任务。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzkyntqznzkzoq-2247485660-1-jcim-tabpfn.md`
- Type: markdown
- Kind: other
