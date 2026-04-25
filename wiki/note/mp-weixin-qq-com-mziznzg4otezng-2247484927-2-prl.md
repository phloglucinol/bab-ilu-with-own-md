---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mziznzg4otezng-2247484927-2-prl
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mziznzg4otezng-2247484927-2-prl.md
bloom: analyze
concepts:
  - adaptive-long-range-modeling
  - short-range-long-range-decomposition
  - learned-decay-without-handcrafted-form
layer_1_bolds:
  - "本文针对传统机器学习原子势忽略长程相互作用的关键缺陷，提出高斯和神经网络（SOG-Net）框架。"
  - "SOG-Net 通过“短程 + 长程”分离建模与高效数值算法，实现对多种长程作用的自适应学习，同时保持量子级精度与近线性计算复杂度。"
  - "SOG-Net 对 6 类二聚体均实现最优性能，且无需预设 1/r 衰减假设。"
layer_2_fragments:
  - "先拆分短程与长程再分别建模"
  - "长程尾部可以被学习而不是手工指定"
  - "潜变量让物理量与表示空间重新对齐"
  - "近线性复杂度来自数值表示设计"
layer_3_thesis: "SOG-Net 真正让我记住的是一个方法论：当旧模型在长程作用上失灵时，不该继续在局部描述符上打补丁，而要单独为长程建立一套可学习表示。"
status: complete
---

# SOG-Net 说明长程相互作用的难点不是算不到 而是表示错了

## Layer 1

- **本文针对传统机器学习原子势忽略长程相互作用的关键缺陷，提出高斯和神经网络（SOG-Net）框架。**
- **SOG-Net 通过“短程 + 长程”分离建模与高效数值算法，实现对多种长程作用的自适应学习，同时保持量子级精度与近线性计算复杂度。**
- **SOG-Net 对 6 类二聚体均实现最优性能，且无需预设 1/r 衰减假设。**

## Layer 2

- **先拆分短程与长程再分别建模**
- **长程尾部可以被学习而不是手工指定**
- **潜变量让物理量与表示空间重新对齐**
- **近线性复杂度来自数值表示设计**

## Layer 3

SOG-Net 真正让我记住的是一个方法论：当旧模型在长程作用上失灵时，不该继续在局部描述符上打补丁，而要单独为长程建立一套可学习表示。

## Concepts

- `[[adaptive-long-range-modeling]]`：长程作用不必靠固定公式硬编码，也可以通过可学习结构拟合。
- `[[short-range-long-range-decomposition]]`：把不同尺度的相互作用拆开，是兼顾精度与效率的前提。
- `[[learned-decay-without-handcrafted-form]]`：不预设衰减形式，本身就是一种更强的归纳偏置。

## Back-references

- `[[mp-weixin-qq-com-mziwmtc4ode0mw-2247719075-1-muon-mamba-gram]]`：Gram 那篇会改变我对这里的理解，因为两者都不是简单加速，而是先找到更贴合结构的表示空间再谈算得快。
- `[[mp-weixin-qq-com-mzizmjqynzq5ma-2247726606-1-ai]]`：蛋白拓扑那篇提醒我长程联系不仅影响能量还影响动力学与功能，所以这里的长程建模意义就不止于数值精度，而是关系到能不能保住真实行为。
- `[[mp-weixin-qq-com-mziwmtc4ode0mw-2247717801-1-adam-muon-google-magma-sota]]`：Magma 说明选择性丢弃更新可以成为结构正则化，这会把本 note 从“更强原子势”改读成另一种结构偏置设计：都在把先验写进计算路径。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mziznzg4otezng-2247484927-2-prl.md`
- Type: markdown
- Kind: other
