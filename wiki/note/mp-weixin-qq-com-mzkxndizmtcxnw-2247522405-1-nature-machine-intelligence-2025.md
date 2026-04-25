---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025.md
bloom: analyze
concepts:
  - leakage-dominated-benchmark
  - clean-split-over-big-benchmark
  - sparse-interaction-graph
  - lm-benefit-after-cleaning
layer_1_bolds:
  - 现有模型的性能主要由数据泄漏驱动。
  - 适度减少数据量、提高数据独立性，反而有助于提升模型的真实泛化能力。
  - 在经过数据去冗余与泄漏过滤的 PDBbind-CleanSplit 上，语言模型嵌入才能真正提升模型的泛化能力。
  - 通过利用蛋白-配体相互作用的稀疏图建模以及从语言模型进行迁移学习，模型能够泛化到严格独立的测试数据集。
layer_2_fragments:
  - benchmark 高分可能只是记忆
  - 结构过滤优先于模型堆料
  - 去冗余迫使模型学习普适规律
  - 预训练特征只在干净数据上显效
layer_3_thesis: 结合亲和力预测真正稀缺的不是更大的模型，而是更干净的数据划分，因为数据泄漏会让一切建模创新看起来都比它们实际更有效。
status: complete
---

# 亲和力预测的第一创新往往应该是清洗 benchmark

## Layer 1 — bold key sentences

- **现有模型的性能主要由数据泄漏驱动。**
- **适度减少数据量、提高数据独立性，反而有助于提升模型的真实泛化能力。**
- **在经过数据去冗余与泄漏过滤的 PDBbind-CleanSplit 上，语言模型嵌入才能真正提升模型的泛化能力。**
- **通过利用蛋白-配体相互作用的稀疏图建模以及从语言模型进行迁移学习，模型能够泛化到严格独立的测试数据集。**

## Layer 2 — bold fragments

- **benchmark 高分可能只是记忆**
- **结构过滤优先于模型堆料**
- **去冗余迫使模型学习普适规律**
- **预训练特征只在干净数据上显效**

## Layer 3 — one-sentence thesis

结合亲和力预测真正稀缺的不是更大的模型，而是更干净的数据划分，因为数据泄漏会让一切建模创新看起来都比它们实际更有效。

## Concepts (tier_1_atoms)

- [[leakage-dominated-benchmark]]：高分 benchmark 可能主要测的是训练测试重叠。
- [[clean-split-over-big-benchmark]]：与其追求大数据集，不如先保证结构独立性。
- [[sparse-interaction-graph]]：只建模真正参与作用的局部相互作用图以提升泛化。
- [[lm-benefit-after-cleaning]]：语言模型特征的价值只有在泄漏被去掉后才可见。

## Back-references

- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim]]：那篇也用语言模型做亲和力预测，这篇提醒先确认提升是否来自表征而不是数据切分漏洞。
- [[mp-weixin-qq-com-mzkyntqznzkzoq-2247485660-1-jcim-tabpfn]]：TabPFN 说明小数据里先看泛化机制，这篇把同样的警告放到蛋白配体 benchmark 上。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025.md`
- Type: markdown
- Kind: other
