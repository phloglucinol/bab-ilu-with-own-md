---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzi3mjm3odk0nq-2247511410-1-spacegfn
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzi3mjm3odk0nq-2247511410-1-spacegfn.md
bloom: analyze
concepts:
  - programmable-chemical-space
  - reaction-defined-space
  - space-exploration-decoupling
  - synthesis-consistent-editing
  - evolutionary-biochemical-prior
layer_1_bolds:
  - "**当前大多数模型将化学空间视为一个固定的、从精选数据库中隐式学习得到的分布。**"
  - "**基于此，来自浙江大学药学院的侯廷军和谢昌谕团队等提出一个将空间定义与空间探索解耦的框架 ——SpaceGFN，从而将分子宇宙从静态约束转变为可控变量。**"
  - "**研究团队认为：分子设计的下一前沿在于将化学空间提升至一个可编程的计算对象。**"
  - "**在编辑模式（Editing mode）下，SpaceGFN 通过应用由可执行合成转化组成的精选分子编辑工具包，实现了与反应一致的先导化合物优化。**"
layer_2_fragments:
  - "**空间定义与空间探索解耦**"
  - "**可编程的、由反应定义的化学空间**"
  - "**进化生化原理作为结构先验**"
  - "**与反应一致的先导化合物优化**"
  - "**实验反馈会重塑底层空间定义**"
layer_3_thesis: "SpaceGFN 真正推进的不是又一个分子生成器，而是把“在哪个化学宇宙里搜索”前移成一等设计变量，使生成模型从拟合库分布转向执行可审计的空间程序。"
status: complete
---

# mp-weixin-qq-com-mzi3mjm3odk0nq-2247511410-1-spacegfn

## Layer 1 — bold key sentences

- **当前大多数模型将化学空间视为一个固定的、从精选数据库中隐式学习得到的分布。**
- **基于此，来自浙江大学药学院的侯廷军和谢昌谕团队等提出一个将空间定义与空间探索解耦的框架 ——SpaceGFN，从而将分子宇宙从静态约束转变为可控变量。**
- **研究团队认为：分子设计的下一前沿在于将化学空间提升至一个可编程的计算对象。**
- **在编辑模式（Editing mode）下，SpaceGFN 通过应用由可执行合成转化组成的精选分子编辑工具包，实现了与反应一致的先导化合物优化。**

## Layer 2 — bold fragments

- **空间定义与空间探索解耦**
- **可编程的、由反应定义的化学空间**
- **进化生化原理作为结构先验**
- **与反应一致的先导化合物优化**
- **实验反馈会重塑底层空间定义**

## Layer 3 — one-sentence thesis

SpaceGFN 真正推进的不是又一个分子生成器，而是把“在哪个化学宇宙里搜索”前移成一等设计变量，使生成模型从拟合库分布转向执行可审计的空间程序。

## Concepts (tier_1_atoms)

- `[[programmable-chemical-space]]` — 把化学空间本身视为可被定义、裁剪、重写的对象，而不是训练集留下来的背景分布。
- `[[reaction-defined-space]]` — 用反应规则和构建块来显式给出可到达宇宙，核心不是分子表示，而是可达性的生成边界。
- `[[space-exploration-decoupling]]` — 先定义空间，再在空间内搜索；这个拆分改变了“模型能力”与“设计意图”的责任边界。
- `[[synthesis-consistent-editing]]` — 编辑不是任意图突变，而是受可执行转化约束的局部修改，直接把合成可行性带入生成步骤。
- `[[evolutionary-biochemical-prior]]` — 把代谢物与酶催化转化编码成先验，不靠事后 ADMET 过滤，而是在搜索时就偏向生命历史处理过的区域。

## Back-references

- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247484082-2-iclr-2025-drugflow-flow-matching-markov-bridge-sbdd-quot-quot]]` — DrugFlow 让我把这里的创新重新看成“搜索域设计”而不是“采样器升级”：前者决定允许进入哪些结构区域，后者决定如何在既定分布之间运输样本。
- `[[mp-weixin-qq-com-mzkwode2otmzma-2247483756-1-science-bioemu]]` — BioEmu 把平衡系综当近似可学习分布，这反过来提醒我：SpaceGFN 所谓“可编程”更像对搜索空间施加外部结构，而不是去忠实再现某个自然热力学系综。
- `[[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485036-1-chemical-reviews-2025]]` — 这篇综述位点如果补完，会把 SpaceGFN 从单篇方法推回药物设计全流程里看：它的价值不在普遍替代库筛，而在把 hit finding 和 lead optimization 的化学可达域改成可写的工程接口。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzi3mjm3odk0nq-2247511410-1-spacegfn.md`
- Type: markdown
- Kind: other
