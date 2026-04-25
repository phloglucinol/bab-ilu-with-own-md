---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkzmjc1njk0mq-2247485911-1-proaffinity-esm-foldx-g
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkzmjc1njk0mq-2247485911-1-proaffinity-esm-foldx-g.md
bloom: analyze
concepts:
  - representation-plus-physics
  - interface-bipartite-graph
  - delta-g-shortcut
  - hybrid-affinity-predictor
layer_1_bolds:
  - ProAffinity++ 将结合区建模为二部图。
  - 节点特征融合了 ESM 表征、AAindex、FoldX 物理能项、DSSP 与侧链信息。
  - 在多个基准上，ProAffinity++ 超过了 FoldX、Prodigy、PPI-Affinity、PIPR 等方法。
  - 纯表示学习和纯能量函数都不够，关键是把二者拼成同一个局部相互作用模型。
layer_2_fragments:
  - 界面二部图承载互作结构
  - 语言模型补语义
  - FoldX 提供物理归纳偏置
  - 混合特征比单路更稳
layer_3_thesis: ProAffinity++ 的启发不是“再加一个 embedding”，而是结合亲和力这种任务需要把统计表示和物理能项压到同一个界面图里共同解释。
status: complete
---

# 亲和力预测里最稳的路线通常是表示学习加物理归纳

## Layer 1 — bold key sentences

- **ProAffinity++ 将结合区建模为二部图。**
- **节点特征融合了 ESM 表征、AAindex、FoldX 物理能项、DSSP 与侧链信息。**
- **在多个基准上，ProAffinity++ 超过了 FoldX、Prodigy、PPI-Affinity、PIPR 等方法。**
- **纯表示学习和纯能量函数都不够，关键是把二者拼成同一个局部相互作用模型。**

## Layer 2 — bold fragments

- **界面二部图承载互作结构**
- **语言模型补语义**
- **FoldX 提供物理归纳偏置**
- **混合特征比单路更稳**

## Layer 3 — one-sentence thesis

ProAffinity++ 的启发不是“再加一个 embedding”，而是结合亲和力这种任务需要把统计表示和物理能项压到同一个界面图里共同解释。

## Concepts (tier_1_atoms)

- [[representation-plus-physics]]：表征学习与物理项混合往往比任一路线单打独斗更稳。
- [[interface-bipartite-graph]]：把界面两侧残基视为二部图而非整蛋白黑箱。
- [[delta-g-shortcut]]：很多 ∆G 任务的捷径是给模型显式界面与能量结构。
- [[hybrid-affinity-predictor]]：混合式预测器在工程上更容易迁移。

## Back-references

- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim]]：BALM 更像纯序列表示路线，这篇说明在结构可得时混入物理项仍然很值。
- [[mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025]]：GEMS 强调干净数据和稀疏相互作用图，这篇则进一步说明图上该放哪些物理与统计特征。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzkzmjc1njk0mq-2247485911-1-proaffinity-esm-foldx-g.md`
- Type: markdown
- Kind: other
