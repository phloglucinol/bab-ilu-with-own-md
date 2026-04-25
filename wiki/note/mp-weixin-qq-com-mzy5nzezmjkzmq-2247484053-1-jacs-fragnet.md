---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzy5nzezmjkzmq-2247484053-1-jacs-fragnet
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzy5nzezmjkzmq-2247484053-1-jacs-fragnet.md
bloom: analyze
concepts:
  - fragment-level-interpretability
  - interpretability-needs-chemical-grounding
  - attention-is-not-contribution
  - fragment-connectivity-matters-for-property-prediction
layer_1_bolds:
  - "**该模型不仅在预测精度上与当前最优方法相当，还能够从原子、化学键、分子片段及片段间连接四个层次提供系统性的可解释性分析。**"
  - "**高注意力权重并不必然意味着大的贡献值——一个片段可能因其在分子中的关键位置而获得高关注，但其对最终预测的实际影响可能因与其他片段的相互作用而被调节。**"
  - "**结果显示，连接度为1的氧原子（如羟基和羰基氧）对溶解度有正贡献，而连接度为2的氧原子（如醚氧）则表现出负贡献。**"
  - "**结果显示，贡献值的方向与溶解度差异方向的一致率达到71.9%，贡献值大小与溶解度差异的相关系数为0.42，表明FragNet能够正确识别导致性质变化的结构差异。**"
  - "**实验表明，结合FragNet贡献数据的提示能够生成溶解度更高的分子结构，展示了可解释性信息在分子设计中的实际应用价值。**"
layer_2_fragments:
  - "**解释层级要覆盖原子 键 片段和片段连接**"
  - "**高注意力不等于正向贡献**"
  - "**同种元素在不同化学环境里作用方向不同**"
  - "**可解释性要经活性悬崖和物理化学规律双重校验**"
layer_3_thesis: "FragNet 的真正进步不是多给几张热图，而是把分子可解释性从“模型看了哪里”推进到“哪类片段和连接如何改变性质”，并且用化学规律与活性悬崖检验这种解释是否值得信。"
status: complete
---
# 分子可解释性如果不落到化学片段上，就还只是模型自我描述

## Layer 1 — bold key sentences
- **该模型不仅在预测精度上与当前最优方法相当，还能够从原子、化学键、分子片段及片段间连接四个层次提供系统性的可解释性分析。**
- **高注意力权重并不必然意味着大的贡献值——一个片段可能因其在分子中的关键位置而获得高关注，但其对最终预测的实际影响可能因与其他片段的相互作用而被调节。**
- **结果显示，连接度为1的氧原子（如羟基和羰基氧）对溶解度有正贡献，而连接度为2的氧原子（如醚氧）则表现出负贡献。**
- **结果显示，贡献值的方向与溶解度差异方向的一致率达到71.9%，贡献值大小与溶解度差异的相关系数为0.42，表明FragNet能够正确识别导致性质变化的结构差异。**
- **实验表明，结合FragNet贡献数据的提示能够生成溶解度更高的分子结构，展示了可解释性信息在分子设计中的实际应用价值。**

## Layer 2 — bold fragments
- **解释层级要覆盖原子 键 片段和片段连接**
- **高注意力不等于正向贡献**
- **同种元素在不同化学环境里作用方向不同**
- **可解释性要经活性悬崖和物理化学规律双重校验**

## Layer 3 — one-sentence thesis
FragNet 的真正进步不是多给几张热图，而是把分子可解释性从“模型看了哪里”推进到“哪类片段和连接如何改变性质”，并且用化学规律与活性悬崖检验这种解释是否值得信。

## Concepts (tier_1_atoms)
- `[[fragment-level-interpretability]]`：片段层解释比单原子热图更接近药化可操作单元。
- `[[interpretability-needs-chemical-grounding]]`：解释如果不能回到物理化学规律与化学环境，就只是可视化而不是理解。
- `[[attention-is-not-contribution]]`：这篇明确把“关注到哪里”和“改变了什么”拆开了。
- `[[fragment-connectivity-matters-for-property-prediction]]`：不仅片段本身重要，片段之间如何连接也在决定性质。

## Back-references
- `[[mp-weixin-qq-com-mzuymdc1mda2oa-2247489378-1-nat-commun-head-amp-ted]]`：HEAD&TED 给的是原子和可旋转键级错误定位，这篇会把那种局部反馈重新理解成“解释必须落到可操作子结构”，否则再精细也难转成设计动作。
- `[[mp-weixin-qq-com-mzy5nzezmjkzmq-2247484415-1-chem-sci-ml-mm]]`：EMLE 那篇强调环境极化对能量预测的决定作用，回看 FragNet 会让我更警惕任何脱离物理背景的解释，因为结构贡献必须最终能被环境和相互作用机制承接。
- `[[mp-weixin-qq-com-mzy5nzezmjkzmq-2247484559-2-jctc]]`：PROTEUS 展示的是如何在生成时把量子化学拉进闭环，这篇则说明一旦要把解释喂回生成器，最有价值的不是总体分数，而是带方向性的片段贡献。 

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzy5nzezmjkzmq-2247484053-1-jacs-fragnet.md`
- Type: markdown
- Kind: other
