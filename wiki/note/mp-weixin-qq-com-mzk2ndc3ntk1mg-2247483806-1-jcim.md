---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk2ndc3ntk1mg-2247483806-1-jcim
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk2ndc3ntk1mg-2247483806-1-jcim.md
bloom: analyze
concepts:
  - "[[two-region-binding-kinetics]]"
  - "[[bd-md-handoff]]"
  - "[[encounter-complex-selection]]"
  - "[[kon-needs-post-diffusion-physics]]"
layer_1_bolds:
  - "**BD用于模拟长程扩散以及形成扩散相遇复合物，而MD则用于模拟后续形成稳定结合复合物的过程。**"
  - "**本文方法的关键改进在于对BD模拟生成的相遇复合物的定义和记录方式。**"
  - "**这确保了MD模拟从一个非常有利的、接近最终结合态的初始构象开始。**"
  - "**单纯BD模拟倾向于高估kon值，因为它忽略了结合位点的去溶剂化和诱导契合等能垒。**"
  - "**BD+MD组合方法计算的值与实验值吻合良好。**"
layer_2_fragments:
  - "**结合速率是扩散和扩散后步骤的乘积**"
  - "**相遇复合物定义决定后续 MD 成本**"
  - "**最短窗口距离是效率杠杆**"
  - "**去溶剂化与诱导契合不能被纯 BD 省略**"
  - "**kon 预测需要物理分层而不是单一模拟尺度**"
layer_3_thesis: "这篇让我重新理解 kon 预测的难点：问题不是怎样把一条长模拟做完，而是怎样把“扩散到了口袋附近”和“真正过了结合能垒”这两个物理阶段干净地拆开。"
status: complete
---

# kon 预测的关键是把扩散与成键后过程拆开

## Layer 1 — bold key sentences

- **BD用于模拟长程扩散以及形成扩散相遇复合物，而MD则用于模拟后续形成稳定结合复合物的过程。**
- **本文方法的关键改进在于对BD模拟生成的相遇复合物的定义和记录方式。**
- **这确保了MD模拟从一个非常有利的、接近最终结合态的初始构象开始。**
- **单纯BD模拟倾向于高估kon值，因为它忽略了结合位点的去溶剂化和诱导契合等能垒。**
- **BD+MD组合方法计算的值与实验值吻合良好。**

## Layer 2 — bold fragments

- **结合速率是扩散和扩散后步骤的乘积**
- **相遇复合物定义决定后续 MD 成本**
- **最短窗口距离是效率杠杆**
- **去溶剂化与诱导契合不能被纯 BD 省略**
- **kon 预测需要物理分层而不是单一模拟尺度**

## Layer 3 — one-sentence thesis

这篇让我重新理解 kon 预测的难点：问题不是怎样把一条长模拟做完，而是怎样把“扩散到了口袋附近”和“真正过了结合能垒”这两个物理阶段干净地拆开。

## Concepts (tier_1_atoms)

- `[[two-region-binding-kinetics]]`：两区域模型是本文真正的抽象单位，不是 BD+MD 的软件堆叠。
- `[[bd-md-handoff]]`：交接点怎么定义，直接决定精度和成本。
- `[[encounter-complex-selection]]`：不是所有 encounter complex 都值得送进 MD，挑起点是方法核心。
- `[[kon-needs-post-diffusion-physics]]`：kon 失真常出在把“扩散到达”误当成“完成结合”。

## Back-references

- `[[mp-weixin-qq-com-mzk2ndc3ntk1mg-2247483780-1-chemical-reviews]]`：综述那篇给了更大的物理背景，这篇则把“溶剂和局部重排不可省略”落成了具体的两阶段工作流。
- `[[mp-weixin-qq-com-mzkwmzy4nda5ma-2247491586-1-ai-schr-dinger]]`：驻留时间预测那篇用 RAMD+iMetaD 处理解离过程；这篇处理结合过程，二者共同说明动力学参数都需要先探索通路，再在关键通路上精算。
- `[[mp-weixin-qq-com-mzk4odkxmzc3ng-2247488269-1]]`：如果焓熵那篇提醒我们亲和力不能代替动力学，这篇就是一个实践版例子，说明相同亲和力背后可以藏着完全不同的进入能垒。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzk2ndc3ntk1mg-2247483806-1-jcim.md`
- Type: markdown
- Kind: other
