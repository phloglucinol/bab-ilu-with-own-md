---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mze5mte0njg3nq-2247484476-1-jacs
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mze5mte0njg3nq-2247484476-1-jacs.md
bloom: analyze
concepts:
  - tensor-output-as-design-problem
  - symmetry-preserving-head
  - universal-tensor-prediction
layer_1_bolds:
  - 提出了一种通用的几何深度学习输出模块，能够端到端预测任意阶数、具有指定对称性的张量性质。
  - 将张量的球谐表示直接建模为图神经网络输出，再通过基变换得到笛卡尔张量。
  - 可避免在消息传递阶段进行耗时的CG张量积。
layer_2_fragments:
  - 张量预测难点在输出头而不只在主干
  - 对称性和协变性应在构造时满足
  - 自混合层替代昂贵CG张量积
  - 分子和晶体共用同一输出思想
layer_3_thesis: 很多“模型不会预测张量”的问题其实不是主干不够强，而是输出头没有把张量的语法写进去。
status: complete
---

# mp-weixin-qq-com-mze5mte0njg3nq-2247484476-1-jacs

## Layer 1 — bold key sentences

- **提出了一种通用的几何深度学习输出模块，能够端到端预测任意阶数、具有指定对称性的张量性质。**
- **将张量的球谐表示直接建模为图神经网络输出，再通过基变换得到笛卡尔张量。**
- **可避免在消息传递阶段进行耗时的CG张量积。**

## Layer 2 — bold fragments

- **张量预测难点在输出头而不只在主干**
- **对称性和协变性应在构造时满足**
- **自混合层替代昂贵 CG 张量积**
- **分子和晶体共用同一输出思想**

## Layer 3 — one-sentence thesis

很多“模型不会预测张量”的问题其实不是主干不够强，而是输出头没有把张量的语法写进去。

## Concepts (tier_1_atoms)

- [[tensor-output-as-design-problem]]：张量预测的核心设计空间在输出模块。
- [[symmetry-preserving-head]]：让输出头天然遵守协变性与对称性。
- [[universal-tensor-prediction]]：同一框架同时支持分子、晶体和原子级张量性质。

## Back-references

- [[mp-weixin-qq-com-j-chem-theory-comput]]：电荷模型靠守恒层保证物理合法，这篇靠张量头保证对称合法；二者都是“把约束写进输出”。
- [[mp-weixin-qq-com-mze5mte0njg3nq-2247485326-1-ai]]：CACE-SOG说明长程作用的核函数需要可学习，这篇说明张量输出语法也需要显式设计；两者都在反对“主干万能论”。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mze5mte0njg3nq-2247484476-1-jacs.md`
- Type: markdown
- Kind: other
