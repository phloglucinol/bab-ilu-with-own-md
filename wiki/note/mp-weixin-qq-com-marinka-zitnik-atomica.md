---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-marinka-zitnik-atomica
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-marinka-zitnik-atomica.md
bloom: analyze
concepts:
  - interaction-first-foundation-model
  - cross-modal-interface-embedding
  - joint-training-across-molecular-modalities
layer_1_bolds:
  - 当前AI化学/生物学领域的“基础模型”主要学习孤立分子的表征，而分子通过相互作用实现功能。
  - 开发一个通用的、原子级的模型，能够学习任意两种分子间相互作用的统一表征。
  - 跨所有分子模态的联合训练显著提升了在数据稀缺的相互作用类型上的表征质量。
layer_2_fragments:
  - 从孤立分子转向相互作用界面
  - 原子层和模块层的分层图
  - 自监督去噪加掩码预测
  - 跨模态联合训练带来知识迁移
layer_3_thesis: 如果功能发生在界面上，那么基础模型的基本样本就不该是“一个分子”，而该是“一次相互作用”。
status: complete
---

# mp-weixin-qq-com-marinka-zitnik-atomica

## Layer 1 — bold key sentences

- **当前AI化学/生物学领域的“基础模型”主要学习孤立分子的表征，而分子通过相互作用实现功能。**
- **开发一个通用的、原子级的模型，能够学习任意两种分子间相互作用的统一表征。**
- **跨所有分子模态的联合训练显著提升了在数据稀缺的相互作用类型上的表征质量。**

## Layer 2 — bold fragments

- **从孤立分子转向相互作用界面**
- **原子层和模块层的分层图**
- **自监督去噪加掩码预测**
- **跨模态联合训练带来知识迁移**

## Layer 3 — one-sentence thesis

如果功能发生在界面上，那么基础模型的基本样本就不该是“一个分子”，而该是“一次相互作用”。

## Concepts (tier_1_atoms)

- [[interaction-first-foundation-model]]：把相互作用而非孤立对象设为预训练单位。
- [[cross-modal-interface-embedding]]：蛋白、小分子、核酸、离子等不同模态共享同一套界面表征空间。
- [[joint-training-across-molecular-modalities]]：数据丰富模态向稀缺模态迁移化学知识。

## Back-references

- [[mp-weixin-qq-com-jcim-rinpy-python]]：RinPy把蛋白内部拓扑当成分析对象，Atomica把跨分子界面当成学习对象；两者都说明“关系”比“实体清单”更值得做一级建模。
- [[mp-weixin-qq-com-mze5mtc4ntcxma-2247487086-1-nat-commun]]：活性肽筛选最终也是在巨大序列空间里寻找能形成有效界面的候选，Atomica提供的是另一种界面先验，只不过这里是表征学习，不是策略搜索。

## Source
- Input: `raw/articles/mp-weixin-qq-com-marinka-zitnik-atomica.md`
- Type: markdown
- Kind: other
