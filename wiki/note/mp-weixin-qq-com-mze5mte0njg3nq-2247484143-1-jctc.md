---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mze5mte0njg3nq-2247484143-1-jctc
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mze5mte0njg3nq-2247484143-1-jctc.md
bloom: analyze
concepts:
  - data-free-coarse-graining
  - adaptive-annealing-against-mode-collapse
  - learned-slow-variables
layer_1_bolds:
  - 首次实现了完全“无数据”的粗粒化模型训练，仅凭能量函数即可学习。
  - 提出的自适应退火方案，有效克服了能量训练中固有的模式坍塌问题。
  - 模型能够自动从能量景观中学习出具有物理意义的粗粒化变量（慢变量）。
layer_2_fragments:
  - 不靠轨迹样本直接学玻尔兹曼分布
  - 慢变量与快变量分层建模
  - 自适应退火保障多峰覆盖
  - 自动发现有物理意义的反应坐标
layer_3_thesis: 粗粒化真正稀缺的不是数据量，而是能否在没有示范轨迹时仍抓住决定分布形状的慢变量。
status: complete
---

# mp-weixin-qq-com-mze5mte0njg3nq-2247484143-1-jctc

## Layer 1 — bold key sentences

- **首次实现了完全“无数据”的粗粒化模型训练，仅凭能量函数即可学习。**
- **提出的自适应退火方案，有效克服了能量训练中固有的模式坍塌问题。**
- **模型能够自动从能量景观中学习出具有物理意义的粗粒化变量（慢变量）。**

## Layer 2 — bold fragments

- **不靠轨迹样本直接学玻尔兹曼分布**
- **慢变量与快变量分层建模**
- **自适应退火保障多峰覆盖**
- **自动发现有物理意义的反应坐标**

## Layer 3 — one-sentence thesis

粗粒化真正稀缺的不是数据量，而是能否在没有示范轨迹时仍抓住决定分布形状的慢变量。

## Concepts (tier_1_atoms)

- [[data-free-coarse-graining]]：只凭能量函数训练粗粒化生成模型。
- [[adaptive-annealing-against-mode-collapse]]：通过自动退火步长维持多模态覆盖。
- [[learned-slow-variables]]：让模型自己发现慢变量，而不是手工指定反应坐标。

## Back-references

- [[mp-weixin-qq-com-mze5mtc4ntcxma-2247486290-1-proc-natl-acad-sci]]：NucleusDiff在采样时维持物理流形，这篇在训练时用能量函数塑形分布，都是把物理规律前移到生成核心。
- [[mp-weixin-qq-com-af2rave-alphafold2]]：AF2RAVE也在找慢构象变化，但它依赖结构预测加增强采样；这篇更进一步，试图直接从能量景观里学出慢变量。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mze5mte0njg3nq-2247484143-1-jctc.md`
- Type: markdown
- Kind: other
