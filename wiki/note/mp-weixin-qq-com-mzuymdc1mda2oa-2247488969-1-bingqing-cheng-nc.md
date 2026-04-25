---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzuymdc1mda2oa-2247488969-1-bingqing-cheng-nc
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247488969-1-bingqing-cheng-nc.md
bloom: analyze
concepts:
  - "[[observable-first-supervision]]"
  - "[[implicit-charge-learning]]"
  - "[[range-separated-ml-potential]]"
  - "[[long-range-interaction-without-charge-labels]]"
layer_1_bolds:
  - "**原子电荷本身并非物理可观测量，其数值强烈依赖于人为选择的电荷划分方法。**"
  - "**该框架直接从能量和力中学习长程相互作用，无需显式的电荷标签或额外输入。**"
  - "**这些隐式电荷并非来自先验的电荷定义，而是通过一个神经网络从局部原子特征中直接映射得到。**"
  - "**该框架的训练范式严格遵循端到端的学习原则，其显著特点是仅使用量子力学计算提供的总能量和原子力作为监督信号，而完全不需要任何显式的原子电荷标签。**"
  - "**在量子力学体系中，这些电荷能成功预测出偶极矩、四极矩乃至玻恩有效电荷等严格的物理可观测量。**"
layer_2_fragments:
  - "**先放弃电荷标签 再把可观测量学回来**"
  - "**长程项要从局部表征里长出来**"
  - "**隐式电荷是模型中介 不是先验真值**"
  - "**能量和力监督比部分电荷监督更稳**"
  - "**范围分离让物理归因与神经表示各守一段**"
layer_3_thesis: "LES 最重要的转向不是又给势能模型补了一个长程模块，而是把监督对象从含糊的“原子电荷真值”换成能量、力和可观测多极矩，从而把长程学习建立在可验证物理量上。"
status: complete
---

# 不要监督一个本来就说不清的量

## Layer 1 — bold key sentences

- **原子电荷本身并非物理可观测量，其数值强烈依赖于人为选择的电荷划分方法。**
- **该框架直接从能量和力中学习长程相互作用，无需显式的电荷标签或额外输入。**
- **这些隐式电荷并非来自先验的电荷定义，而是通过一个神经网络从局部原子特征中直接映射得到。**
- **该框架的训练范式严格遵循端到端的学习原则，其显著特点是仅使用量子力学计算提供的总能量和原子力作为监督信号，而完全不需要任何显式的原子电荷标签。**
- **在量子力学体系中，这些电荷能成功预测出偶极矩、四极矩乃至玻恩有效电荷等严格的物理可观测量。**

## Layer 2 — bold fragments

- **先放弃电荷标签 再把可观测量学回来**
- **长程项要从局部表征里长出来**
- **隐式电荷是模型中介 不是先验真值**
- **能量和力监督比部分电荷监督更稳**
- **范围分离让物理归因与神经表示各守一段**

## Layer 3 — one-sentence thesis

LES 最重要的转向不是又给势能模型补了一个长程模块，而是把监督对象从含糊的“原子电荷真值”换成能量、力和可观测多极矩，从而把长程学习建立在可验证物理量上。

## Concepts (tier_1_atoms)

- `[[observable-first-supervision]]`：当中间变量没有唯一物理定义时，监督最终可观测量比监督人为分解量更可靠。
- `[[implicit-charge-learning]]`：这里的电荷是为了让 Ewald 长程项可计算的潜变量，不是要复刻某一种分区电荷。
- `[[range-separated-ml-potential]]`：短程交给局部势，长程交给显式可积模块，是一种比单一黑箱更可控的分工。
- `[[long-range-interaction-without-charge-labels]]`：长程建模不必先拿到“正确电荷标签”，可以直接从能量与力反推。

## Back-references

- `[[mp-weixin-qq-com-mzk0mjuzmzywmw-2247488825-1-nat-commun-range]]`：RANGE 那篇说明长程信息需要独立通信通道；这篇进一步把这个判断落到物理监督层，提醒我通道不够，监督目标也必须避开含糊标签。
- `[[mp-weixin-qq-com-mzkzmjc1njk0mq-2247485683-1-fep]]`：FEP Omega 把短轨迹后处理成可学习误差信号，这篇则把电荷从真值改成潜变量；两篇都在做同一件事，把不可直接信赖的中间表征降级，把最终物理读数抬成训练锚点。
- `[[mp-weixin-qq-com-mzk2ndc3ntk1mg-2247483780-1-chemical-reviews]]`：那篇综述把溶剂和相互作用网络看成系统组成部分，这篇提供一个更尖锐的实现例子，说明长程静电若处理错了，后面的结构与动力学解释都会跟着偏。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247488969-1-bingqing-cheng-nc.md`
- Type: markdown
- Kind: other
