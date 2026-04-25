---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzuymdc1mda2oa-2247489369-1-deepmind-nature-machine-intelligence
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247489369-1-deepmind-nature-machine-intelligence.md
bloom: analyze
concepts:
  - "[[global-encoding-fixes-gnn-locality]]"
  - "[[linear-time-global-attention]]"
  - "[[equivariant-global-message-passing]]"
  - "[[nonlocal-physics-needs-global-channel]]"
layer_1_bolds:
  - "**如何在计算效率与全局建模能力之间取得平衡，成为该领域的关键挑战。**"
  - "**提出了一种专为欧几里得数据设计的全新机制——欧几里得快速注意力（Euclidean Fast Attention, EFA）。**"
  - "**EFA允许中心节点直接访问所有节点，无论距离远近，从而在理论上具备捕捉长程物理效应的能力。**"
  - "**EFA采用线性缩放注意力公式，通过先求和键与值的外积再进行投影计算，实现了与原子数呈线性缩放的计算架构。**"
  - "**该研究提出的EFA机制的核心突破在于，在保持线性计算复杂度的前提下，实现了对分子体系中全局原子相互作用的直接建模。**"
layer_2_fragments:
  - "**长程物理需要显式全局通道**"
  - "**欧氏几何编码要和等变性一起设计**"
  - "**全局访问不能退回二次复杂度**"
  - "**局部 MPNN 与全局注意力应并联而非互斥**"
  - "**结构归纳偏置决定注意力能否用于三维分子**"
layer_3_thesis: "EFA 这篇最该留下的是一个架构判断：分子模型若想同时保留局部几何细节和远程相互作用，就必须把等变几何编码与线性复杂度的全局通信层一起设计，而不是继续靠截断半径和堆层数补救。"
status: complete
---

# 长程相互作用需要一条专门的全局通信层

## Layer 1 — bold key sentences

- **如何在计算效率与全局建模能力之间取得平衡，成为该领域的关键挑战。**
- **提出了一种专为欧几里得数据设计的全新机制——欧几里得快速注意力（Euclidean Fast Attention, EFA）。**
- **EFA允许中心节点直接访问所有节点，无论距离远近，从而在理论上具备捕捉长程物理效应的能力。**
- **EFA采用线性缩放注意力公式，通过先求和键与值的外积再进行投影计算，实现了与原子数呈线性缩放的计算架构。**
- **该研究提出的EFA机制的核心突破在于，在保持线性计算复杂度的前提下，实现了对分子体系中全局原子相互作用的直接建模。**

## Layer 2 — bold fragments

- **长程物理需要显式全局通道**
- **欧氏几何编码要和等变性一起设计**
- **全局访问不能退回二次复杂度**
- **局部 MPNN 与全局注意力应并联而非互斥**
- **结构归纳偏置决定注意力能否用于三维分子**

## Layer 3 — one-sentence thesis

EFA 这篇最该留下的是一个架构判断：分子模型若想同时保留局部几何细节和远程相互作用，就必须把等变几何编码与线性复杂度的全局通信层一起设计，而不是继续靠截断半径和堆层数补救。

## Concepts (tier_1_atoms)

- `[[global-encoding-fixes-gnn-locality]]`：局部消息传递的盲区必须靠显式全局层来补。
- `[[linear-time-global-attention]]`：全局访问若不能保持线性标度，就很难进入真实大体系模拟。
- `[[equivariant-global-message-passing]]`：三维分子里的全局通信不能只做 token mixing，必须保留欧氏几何约束。
- `[[nonlocal-physics-needs-global-channel]]`：长程静电、反应远程吸引、电子离域都属于必须跨截断半径传播的信息。

## Back-references

- `[[mp-weixin-qq-com-mzk0mjuzmzywmw-2247488825-1-nat-commun-range]]`：RANGE 用主节点做可学习平均场，这篇用欧氏快速注意力做全局访问；两篇合起来说明结论已经很稳定了，长程物理不能再寄希望于局部 GNN 自行涌现。
- `[[mp-weixin-qq-com-mzuymdc1mda2oa-2247488969-1-bingqing-cheng-nc]]`：LES 通过范围分离把长程项显式拉出来，这篇则在网络结构里给长程交互开通全局通道；一个在监督与物理分解层面补长程，一个在表示与通信层面补长程。
- `[[mp-weixin-qq-com-mzk0mjuzmzywmw-2247488931-1-hacettepe-do-an-nmi-transformer]]`：DrugGEN 把 Transformer 带入分子生成时主要押注全局结构表达，这篇让我更清楚看到，若场景是三维原子系统，Transformer 真正难点不在“有无注意力”，而在“注意力是否守住欧氏几何和线性复杂度”。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247489369-1-deepmind-nature-machine-intelligence.md`
- Type: markdown
- Kind: other
