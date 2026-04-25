---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk0mjuzmzywmw-2247487637-1-nature
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247487637-1-nature.md
bloom: analyze
concepts:
  - full-library-docking-beats-preclustering
  - ultra-large-docking-finds-new-chemotypes
  - score-to-hit-rate-can-be-modeled
layer_1_bolds:
  - 本文的核心创新在于：将“按需合成”理念与超大规模结构对接相结合，突破了“只能筛选现货化合物”的传统瓶颈。
  - 对全库每个分子独立对接是发现最优配体的必要条件，无法用预聚类代替。
  - 从数亿打分结果中选出测试候选物需要多层过滤。
layer_2_fragments:
  - 按需合成和超大对接真正接上了
  - 预聚类会错过最好分子
  - 新骨架来自全库逐个算
  - 命中率能和打分曲线挂钩
layer_3_thesis: Nature这篇真正重塑的不是“库更大”这件事本身，而是发现了一条反直觉操作原则：在超大化学空间里，省算力的预聚类会系统性错过最优命中，所以必须先把全库独立算完，再谈多样性和人工判断。
status: complete
---

# mp-weixin-qq-com-mzk0mjuzmzywmw-2247487637-1-nature

## Layer 1 — bold key sentences

- **本文的核心创新在于：将“按需合成”理念与超大规模结构对接相结合，突破了“只能筛选现货化合物”的传统瓶颈。**
- **对全库每个分子独立对接是发现最优配体的必要条件，无法用预聚类代替。**
- **从数亿打分结果中选出测试候选物需要多层过滤。**

## Layer 2 — bold fragments

- **按需合成和超大对接真正接上了**
- **预聚类会错过最好分子**
- **新骨架来自全库逐个算**
- **命中率能和打分曲线挂钩**

## Layer 3 — one-sentence thesis

Nature这篇真正重塑的不是“库更大”这件事本身，而是发现了一条反直觉操作原则：在超大化学空间里，省算力的预聚类会系统性错过最优命中，所以必须先把全库独立算完，再谈多样性和人工判断。

## Concepts (tier_1_atoms)

- [[full-library-docking-beats-preclustering]]：超大规模筛选里，预聚类替代全库对接会系统性丢失强命中。
- [[ultra-large-docking-finds-new-chemotypes]]：超大按需合成库能提供小库中根本不存在的新骨架。
- [[score-to-hit-rate-can-be-modeled]]：对接分数分布与命中率之间可以建立经验定量关系。

## Back-references

- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247486956-1-nat-chem-biol.md]]：Nat Chem Biol那篇像是这里的后验反思，说明大库确实能给好分子，但也会同步放大打分假象。
- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247548963-1.md]]：small can be beautiful并不是否定这篇，而是提醒这篇解决的是“怎样从超大库里找到东西”，没解决“什么时候值得用超大库”。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247486032-1-j-med-chem-tmprss2.md]]：TMPRSS2案例说明超大对接之后必须马上接结构与生物物理闭环，否则新骨架发现只是方法学半成品。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247487637-1-nature.md`
- Type: markdown
- Kind: other
