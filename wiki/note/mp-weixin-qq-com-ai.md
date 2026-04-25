---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-ai
kind: other
ingested_at: 2026-04-25T14:07:20Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-ai.md
bloom: evaluate
concepts:
  - computationally-prioritized-medicinal-chemistry
  - relative-affinity-models-scale-lead-optimization
  - qualitative-prioritization-beats-fake-precision
  - evaluation-logs-are-training-data
  - hit-to-lead-over-library-size
layer_1_bolds:
  - "尽管人工智能（AI）技术被广泛引入，但如何有效衡量其对研发项目的真实贡献，尚缺乏共识性的方法。"
  - "因此，在评估时，应将关注点从单纯的“产出”（如完成了多少次计算预测）转向实际的“结果”（如先导化合物优化周期是否缩短）。"
  - "古德哈特定律的警示：当一个衡量指标本身成为追求的目标时，它便可能失去作为有效衡量工具的价值。"
  - "实验绕过率：计算有多少比例的化合物，是基于AI模型的高置信度预测结果而直接跳过某些常规实验步骤。"
  - "平均性质偏移：针对ADME（吸收、分布、代谢、排泄）性质预测模型，建议追踪所合成化合物的某项关键性质（如代谢稳定性）的平均值变化趋势。"
layer_2_fragments:
  - "模型指标必须让位于工作流结果"
  - "数字化评分给项目难度做基线校正"
  - "实验绕过率衡量组织是否真的信任模型"
  - "性质预测的价值要落到合成分子分布的偏移"
  - "筛选指标要问能否支撑后续 hit-to-lead"
layer_3_thesis: "AI 先导优化的核心评估对象不是模型本身，而是它是否改变了药化项目的决策速度、实验路径和候选分子性质分布。"
status: complete
---

# AI 先导优化要用工作流结果而不是模型分数来评估

## Layer 1 — bold key sentences

- **尽管人工智能（AI）技术被广泛引入，但如何有效衡量其对研发项目的真实贡献，尚缺乏共识性的方法。**
- **因此，在评估时，应将关注点从单纯的“产出”（如完成了多少次计算预测）转向实际的“结果”（如先导化合物优化周期是否缩短）。**
- **古德哈特定律的警示：当一个衡量指标本身成为追求的目标时，它便可能失去作为有效衡量工具的价值。**
- **实验绕过率：计算有多少比例的化合物，是基于AI模型的高置信度预测结果而直接跳过某些常规实验步骤。**
- **平均性质偏移：针对ADME（吸收、分布、代谢、排泄）性质预测模型，建议追踪所合成化合物的某项关键性质（如代谢稳定性）的平均值变化趋势。**

## Layer 2 — bold fragments

- **模型指标必须让位于工作流结果**
- **数字化评分给项目难度做基线校正**
- **实验绕过率衡量组织是否真的信任模型**
- **性质预测的价值要落到合成分子分布的偏移**
- **筛选指标要问能否支撑后续 hit-to-lead**

## Layer 3 — one-sentence thesis

AI 先导优化的核心评估对象不是模型本身，而是它是否改变了药化项目的决策速度、实验路径和候选分子性质分布。

## Concepts (tier_1_atoms)

- [[computationally-prioritized-medicinal-chemistry]]：这篇把 AI 价值从预测准确率拉回项目结果，正好补上“计算优先药化”该如何被衡量。
- [[relative-affinity-models-scale-lead-optimization]]：先导优化关心系列分子排序是否真的进入日常迭代，而不是某个单点预测分数。
- [[qualitative-prioritization-beats-fake-precision]]：内部推荐值、采纳率和推进决策比伪精确模型分数更接近真实组织行为。
- [[evaluation-logs-are-training-data]]：实验绕过、采纳和性质偏移都应该成为后续模型与流程改进的数据，而不是会后汇报材料。
- [[hit-to-lead-over-library-size]]：虚拟筛选指标最终要回答能不能支撑后续 hit-to-lead，而不是库规模或计算次数本身。

## Back-references

- [[mp-weixin-qq-com-mzkwmzy4nda5ma-2247491376-1-0-7-nm-ai-kai-11101]]：KAI-11101 是这篇 KPI 思路的强案例；它不是只展示模型分数，而是展示计算优先流程如何压缩周期并重排合成预算。
- [[mp-weixin-qq-com-mzyzodi1otazna-2247486769-1-18-7-pbcnet2-0-ai]]：PBCNet2.0 说明相对亲和力模型能进入日常优化循环；本 note 则给出判断这类模型是否真正影响项目的上层指标。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247488573-1-molve-ai-quot-quot]]：MolVE 把专家推进/不推进决策做成平台，本 note 解释为什么这种决策日志本身比单次模型分数更接近真实业务价值。
- [[mp-weixin-qq-com-mzg3otc3ndc0ma-2247487286-1-j-cheminf-poligenx-ai]]：PoLiGenX 代表生成式先导优化的技术路线，本 note 提醒我评价这类路线时不能只看新颖性或相似度，还要看最终采纳和性质分布是否改变。

## Source
- Input: `raw/articles/mp-weixin-qq-com-ai.md`
- Type: markdown
- Kind: other
