---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk3ntq2nji1mg-2247485379-1-jmc-2025-7-3d
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk3ntq2nji1mg-2247485379-1-jmc-2025-7-3d.md
bloom: analyze
concepts:
  - "[[chemical-plausibility-benchmark]]"
  - "[[distribution-shift-from-real-medicinal-chemistry]]"
  - "[[docking-optimized-is-not-drug-like]]"
  - "[[new-metrics-for-generative-evaluation]]"
layer_1_bolds:
  - "**这篇文章没有提出新模型，而是对当前主流3D结构驱动生成模型进行化学合理性体检。**"
  - "**这些模型生成的分子，真的像药吗？**"
  - "**化学合理性第一次被量化，AI集体不及格。**"
  - "**AI学的是结合模式，不是药物经验。**"
  - "**当前结构生成模型在空间填充与药物可行性之间，系统性地选择了前者。**"
layer_2_fragments:
  - "**新 benchmark 把真实药化分布拉回评测核心**"
  - "**稀有环系和不存在 scaffold 是现实化学的红旗**"
  - "**模型偏爱脂环 手性中心和过量极性基团**"
  - "**高 docking 分不等于化学上站得住**"
  - "**AI 生成评价必须从 valid 转向 plausible**"
layer_3_thesis: "这篇评测真正击中的问题是：当前 3D 生成模型优化的是“如何更像口袋喜欢的分子”，而不是“如何更像现实世界里能做、能测、能成药的分子”。"
status: complete
---

# 3D 生成模型最大的问题不是不会生成，而是不懂真实药化分布

## Layer 1 — bold key sentences

- **这篇文章没有提出新模型，而是对当前主流3D结构驱动生成模型进行化学合理性体检。**
- **这些模型生成的分子，真的像药吗？**
- **化学合理性第一次被量化，AI集体不及格。**
- **AI学的是结合模式，不是药物经验。**
- **当前结构生成模型在空间填充与药物可行性之间，系统性地选择了前者。**

## Layer 2 — bold fragments

- **新 benchmark 把真实药化分布拉回评测核心**
- **稀有环系和不存在 scaffold 是现实化学的红旗**
- **模型偏爱脂环 手性中心和过量极性基团**
- **高 docking 分不等于化学上站得住**
- **AI 生成评价必须从 valid 转向 plausible**

## Layer 3 — one-sentence thesis

这篇评测真正击中的问题是：当前 3D 生成模型优化的是“如何更像口袋喜欢的分子”，而不是“如何更像现实世界里能做、能测、能成药的分子”。

## Concepts (tier_1_atoms)

- `[[chemical-plausibility-benchmark]]`：这篇贡献首先是 benchmark，而不是结论。
- `[[distribution-shift-from-real-medicinal-chemistry]]`：AI 生成分子与真实药化分布之间存在系统漂移。
- `[[docking-optimized-is-not-drug-like]]`：这是全文最值得带走的判断。
- `[[new-metrics-for-generative-evaluation]]`：环系频率和 scaffold 存在性是对旧指标体系的重要补丁。

## Back-references

- `[[mp-weixin-qq-com-mzk3ntq2nji1mg-2247485458-1-pnas-synformer-ai]]`：SynFormer 之所以重要，正因为这篇说明“会生成”不够，必须把可合成空间直接写进生成对象。
- `[[mp-weixin-qq-com-mzk3ntq2nji1mg-2247485505-1-syncraft]]`：SynCraft 针对的“合成悬崖”正是这篇评测暴露出来的系统症状之一，因此它更像是对 benchmark 结果的后续处方。
- `[[mp-weixin-qq-com-mzkwmji4odg2na-2247484368-1-jcim-admet]]`：ADMET 去噪那篇怀疑标签质量，这篇怀疑评测指标本身，二者都指向同一个更大的问题：如果基准定义错了，模型进步只是幻觉。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzk3ntq2nji1mg-2247485379-1-jmc-2025-7-3d.md`
- Type: markdown
- Kind: other
