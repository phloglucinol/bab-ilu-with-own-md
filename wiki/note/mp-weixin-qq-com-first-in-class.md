---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-first-in-class
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-first-in-class.md
bloom: analyze
concepts:
  - simulation-to-experiment-exchange-rate
  - physics-pretrained-protein-model
  - low-n-protein-engineering
layer_1_bolds:
  - 在模型的预训练阶段引入了分子模拟产生的大规模生物物理数据，让模型在“学语言”的同时，也能“懂物理”。
  - 约29个模拟数据点带来的性能提升与单个实验数据点相同。
  - 生成荧光蛋白的综合命中率：16/20 = 80 %；随机基线 1/20 = 5 %。
layer_2_fragments:
  - Rosetta能量预训练进入Transformer
  - 模拟数据部分兑换实验数据
  - low-N条件下仍能外推设计
  - 三维相对位置编码只进入注意力打分
layer_3_thesis: 当实验样本极少时，最有效的不是更激进地正则化，而是先让模型学会一个可迁移的物理语法，再把实验数据留给任务校准。
status: complete
---

# mp-weixin-qq-com-first-in-class

## Layer 1 — bold key sentences

- **在模型的预训练阶段引入了分子模拟产生的大规模生物物理数据，让模型在“学语言”的同时，也能“懂物理”。**
- **约29个模拟数据点带来的性能提升与单个实验数据点相同。**
- **生成荧光蛋白的综合命中率：16/20 = 80 %；随机基线 1/20 = 5 %。**

## Layer 2 — bold fragments

- **Rosetta 能量预训练进入 Transformer**
- **模拟数据部分兑换实验数据**
- **low-N 条件下仍能外推设计**
- **三维相对位置编码只进入注意力打分**

## Layer 3 — one-sentence thesis

当实验样本极少时，最有效的不是更激进地正则化，而是先让模型学会一个可迁移的物理语法，再把实验数据留给任务校准。

## Concepts (tier_1_atoms)

- [[simulation-to-experiment-exchange-rate]]：把模拟样本视为可折算的监督预算，而不是廉价替代品。
- [[physics-pretrained-protein-model]]：预训练目标不只复现序列统计，还要显式学习能量与结构约束。
- [[low-n-protein-engineering]]：真正困难的不是拟合已有突变，而是在很少标签下做可信外推。

## Back-references

- [[mp-weixin-qq-com-af2rave-alphafold2]]：AF2RAVE说明动态先验能改进筛选，这篇说明生物物理先验能改进突变外推；两者都在反驳“只要规模够大，黑箱自己会学会物理”。
- [[mp-weixin-qq-com-mze5mte0njg3nq-2247484159-1-jctc]]：柔性晶体预测那里把昂贵量子计算留给最终前100名，这里把珍贵实验数据留给微调阶段，本质都是把高成本信息放到最后一层决策。

## Source
- Input: `raw/articles/mp-weixin-qq-com-first-in-class.md`
- Type: markdown
- Kind: other
