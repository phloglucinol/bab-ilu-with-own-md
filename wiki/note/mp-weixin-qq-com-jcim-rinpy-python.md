---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-jcim-rinpy-python
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-jcim-rinpy-python.md
bloom: apply
concepts:
  - structure-to-network-lens
  - centrality-as-functional-hypothesis
  - perturbation-graph-comparison
layer_1_bolds:
  - 残基相互作用网络（RIN）模型是一种行之有效的方法，它基于蛋白质结构的接触拓扑特征，用于识别不同蛋白质结构中的功能残基和配体结合位点。
  - 介数中心性得分最高的节点可用于预测潜在的变构位点。
  - 该工具还提供网络比较分析功能，能够定量评估配体结合或基因突变等扰动因素如何改变蛋白质复合物的接触拓扑结构。
layer_2_fragments:
  - 结构先转成残基网络
  - 中心性指标变成功能假设
  - 扰动前后网络差分可解释
  - 小分子水和离子也能进图
layer_3_thesis: RIN方法最有用的地方不是“把蛋白画成图”，而是把本来零散的结构直觉统一成一套可比较、可排名、可做差分的拓扑操作。
status: complete
---

# mp-weixin-qq-com-jcim-rinpy-python

## Layer 1 — bold key sentences

- **残基相互作用网络（RIN）模型是一种行之有效的方法，它基于蛋白质结构的接触拓扑特征，用于识别不同蛋白质结构中的功能残基和配体结合位点。**
- **介数中心性得分最高的节点可用于预测潜在的变构位点。**
- **该工具还提供网络比较分析功能，能够定量评估配体结合或基因突变等扰动因素如何改变蛋白质复合物的接触拓扑结构。**

## Layer 2 — bold fragments

- **结构先转成残基网络**
- **中心性指标变成功能假设**
- **扰动前后网络差分可解释**
- **小分子、水和离子也能进图**

## Layer 3 — one-sentence thesis

RIN 方法最有用的地方不是“把蛋白画成图”，而是把本来零散的结构直觉统一成一套可比较、可排名、可做差分的拓扑操作。

## Concepts (tier_1_atoms)

- [[structure-to-network-lens]]：先把三维结构投影到接触网络，再谈功能热点。
- [[centrality-as-functional-hypothesis]]：中心性不是结论，而是可实验检验的功能优先级。
- [[perturbation-graph-comparison]]：比较复合物或突变前后的网络差异，比只看局部坐标变化更适合解释机制。

## Back-references

- [[mp-weixin-qq-com-marinka-zitnik-atomica]]：Atomica学的是跨分子相互作用界面的原子级表征，RinPy学的是蛋白内部残基拓扑；前者偏表征学习，后者偏分析透镜，但都在把“相互作用”当成一级对象。
- [[mp-weixin-qq-com-jctc]]：PINN求解PBE关注连续静电场，这篇把连续结构压成离散拓扑；两者提醒我，分子问题既可以在场上解，也可以在图上解，关键看你想保留哪类可解释性。

## Source
- Input: `raw/articles/mp-weixin-qq-com-jcim-rinpy-python.md`
- Type: markdown
- Kind: other
