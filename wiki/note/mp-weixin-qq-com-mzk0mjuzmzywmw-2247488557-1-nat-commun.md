---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk0mjuzmzywmw-2247488557-1-nat-commun
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247488557-1-nat-commun.md
bloom: analyze
concepts:
  - uncertainty-aware-molecular-optimization
  - probabilistic-improvement-beats-greedy-search
  - ei-fails-in-open-chemical-space
layer_1_bolds:
  - 优化过程天然倾向于将搜索推向训练数据稀疏的未知区域——恰恰是模型预测最不可靠的地方。
  - 概率改进优化（Probabilistic Improvement Optimization, PIO）策略在大多数任务中显著优于不考虑不确定性的传统方法和另一种 UQ 集成策略（期望改进，EI）。
  - EI 在传统 BO 中的成功经验，不能直接迁移到大规模化学空间中的 GNN 优化场景。
layer_2_fragments:
  - 代理模型最怕被自己外推骗到
  - PIO比贪心和EI都稳
  - 开放化学空间里不确定性必须入适应度
  - 经典贝叶斯优化经验会失灵
layer_3_thesis: 这篇真正重要的不是“给GNN加不确定性”这么简单，而是指出在开放化学空间优化里，采集函数本身必须按模型失真方式重写，否则越聪明的搜索越会被高方差幻觉带偏。
status: complete
---

# mp-weixin-qq-com-mzk0mjuzmzywmw-2247488557-1-nat-commun

## Layer 1 — bold key sentences

- **优化过程天然倾向于将搜索推向训练数据稀疏的未知区域——恰恰是模型预测最不可靠的地方。**
- **概率改进优化（Probabilistic Improvement Optimization, PIO）策略在大多数任务中显著优于不考虑不确定性的传统方法和另一种 UQ 集成策略（期望改进，EI）。**
- **EI 在传统 BO 中的成功经验，不能直接迁移到大规模化学空间中的 GNN 优化场景。**

## Layer 2 — bold fragments

- **代理模型最怕被自己外推骗到**
- **PIO比贪心和EI都稳**
- **开放化学空间里不确定性必须入适应度**
- **经典贝叶斯优化经验会失灵**

## Layer 3 — one-sentence thesis

这篇真正重要的不是“给GNN加不确定性”这么简单，而是指出在开放化学空间优化里，采集函数本身必须按模型失真方式重写，否则越聪明的搜索越会被高方差幻觉带偏。

## Concepts (tier_1_atoms)

- [[uncertainty-aware-molecular-optimization]]：分子优化时必须把模型不确定性视为一等信号。
- [[probabilistic-improvement-beats-greedy-search]]：PIO比直接最大化预测值更适合开放化学空间搜索。
- [[ei-fails-in-open-chemical-space]]：期望改进在大化学空间和GNN场景下可能系统性失灵。

## Back-references

- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247488573-1-molve-ai-quot-quot.md]]：MolVE解决的是人类如何审查AI候选，这篇解决的是AI别先把候选生成到明显不可信的外推区域，两者构成前后两个质控层。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247487983-1-neurips-rgfn.md]]：RGFN用反应空间约束生成，这篇从优化侧说明为什么还要再管不确定性，因为即便状态空间合理，代理模型也会在外推时胡说。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247489047-1-nat-commun-clickgen.md]]：ClickGen靠强化学习追对接分数，这篇提醒我任何RL式优化都需要警惕oracle和代理模型在域外一起失真。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247488557-1-nat-commun.md`
- Type: markdown
- Kind: other
