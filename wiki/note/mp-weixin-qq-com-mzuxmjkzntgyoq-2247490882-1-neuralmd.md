---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzuxmjkzntgyoq-2247490882-1-neuralmd
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzuxmjkzntgyoq-2247490882-1-neuralmd.md
bloom: understand
concepts:
  - "[[learning-binding-dynamics-needs-physical-inductive-bias]]"
  - "[[multi-grained-equivariant-dynamics]]"
  - "[[second-order-neural-ode-stabilizes-trajectories]]"
  - "[[ml-md-acceleration-only-matters-if-trajectories-stay-physical]]"
layer_1_bolds:
  - "**传统 MD 方法计算成本高、时间尺度受限，而现有机器学习加速方法在长时间模拟中往往面临误差累积和物理一致性不足等问题。**"
  - "**该方法以物理约束为核心，将机器学习与牛顿力学和几何对称性系统性结合。**"
  - "**作者提出了多粒度、SE(3) 等变的 BindingNet。**"
  - "**NeuralMD 采用二阶神经微分方程，同时对速度和位置进行积分。**"
  - "**在保持精度的前提下实现了数量级上的计算加速。**"
layer_2_fragments:
  - "**学动力学时 物理先验不是可选项**"
  - "**多粒度表示让结合界面不再被压平**"
  - "**二阶动力学比一步步回归更稳定**"
  - "**加速只有在轨迹仍然物理时才有意义**"
layer_3_thesis: "NeuralMD 的真正目标不是把 MD 变成更快的轨迹生成器，而是把物理约束直接写进学习框架里，让长时间蛋白-配体动力学在加速后仍然像动力学而不是像插值动画。"
status: complete
---
# 机器学习想替 MD 干活，先得学会尊重牛顿而不是绕过牛顿

## Layer 1 — bold key sentences

<!-- Bold verbatim sentences from the source that carry the highest
     conceptual weight. Never paraphrase in Layer 1. -->

- **传统 MD 方法计算成本高、时间尺度受限，而现有机器学习加速方法在长时间模拟中往往面临误差累积和物理一致性不足等问题。**
- **该方法以物理约束为核心，将机器学习与牛顿力学和几何对称性系统性结合。**
- **作者提出了多粒度、SE(3) 等变的 BindingNet。**
- **NeuralMD 采用二阶神经微分方程，同时对速度和位置进行积分。**
- **在保持精度的前提下实现了数量级上的计算加速。**

## Layer 2 — bold fragments

<!-- 3–5 conceptual fragments (not 'interesting phrases').
     Each fragment must anchor at least one downstream concept-atom. -->

- **学动力学时 物理先验不是可选项**
- **多粒度表示让结合界面不再被压平**
- **二阶动力学比一步步回归更稳定**
- **加速只有在轨迹仍然物理时才有意义**

## Layer 3 — one-sentence thesis

<!-- Your synthesis, not the author's thesis. One sentence, no hedges.
     If you need two sentences the note is not atomic yet. -->

NeuralMD 的真正目标不是把 MD 变成更快的轨迹生成器，而是把物理约束直接写进学习框架里，让长时间蛋白-配体动力学在加速后仍然像动力学而不是像插值动画。

## Concepts (tier_1_atoms)

<!-- Propose concept wikilinks that appear in ≥2 notes.
     Format: `[[concept-slug]]` — explanation of why it earns its place. -->

- `[[learning-binding-dynamics-needs-physical-inductive-bias]]`：动态学习如果没有物理偏置，长时段会快速漂。
- `[[multi-grained-equivariant-dynamics]]`：多粒度和等变性一起决定了表示是否能承载结合动力学。
- `[[second-order-neural-ode-stabilizes-trajectories]]`：二阶积分把速度显式带回模型里。
- `[[ml-md-acceleration-only-matters-if-trajectories-stay-physical]]`：速度提升必须服从轨迹可信度。

## Back-references

<!-- Each back-ref must include a specific claim about HOW the other
     note shifts interpretation of this one — not just 'related to X'. -->

- `[[mp-weixin-qq-com-mzuxmjkzntgyoq-2247490748-1-cpacs-md]]`：cPaCS-MD 仍然在经典 MD 范式内优化采样效率，这篇则尝试直接学习动力学；两者共同说明加速路径有两种，一种优化采样策略，一种重写动力学求解器。
- `[[mp-weixin-qq-com-mzuymdc1mda2oa-2247488969-1-bingqing-cheng-nc]]`：LES 解决的是长程相互作用如何学进去，这篇解决的是学进去之后怎么稳定积分成轨迹，前者偏势能面，后者偏动力学演化。
- `[[mp-weixin-qq-com-mzuymdc1mda2oa-2247489369-1-deepmind-nature-machine-intelligence-v2]]`：EFA 用全局注意力修正局部模型的视野瓶颈，这篇则用多粒度等变表示修正动力学学习的稳定性瓶颈，都是“先补物理盲区再谈 AI 加速”的路线。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzuxmjkzntgyoq-2247490882-1-neuralmd.md`
- Type: markdown
- Kind: other
