---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzu5otu3nzyyoq-2247490043-1-jctc
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzu5otu3nzyyoq-2247490043-1-jctc.md
bloom: analyze
concepts:
  - "[[path-enumeration-before-kinetics]]"
  - "[[free-energy-trajectory-as-ml-feature]]"
  - "[[high-throughput-koff-needs-physics-compression]]"
  - "[[residence-time-explanations-should-be-atomistic]]"
layer_1_bolds:
  - "**药物分子的解离速率 (koff) 已被证明与疗效的相关性高于其对特定体系的亲和力。**"
  - "**这些方法主要基于增强采样分子动力学模拟，但计算成本高昂。**"
  - "**本文提出了一种基于物理和机器学习相结合的方法。**"
  - "**使用基于物理的配体竞争饱和位点识别 (SILCS) 方法来枚举潜在的配体解离途径，并计算沿这些途径的配体解离自由能曲线。**"
  - "**SILCS-Kinetics工作流程提供了一种研究配体解离动力学的高效方法，包括能够对原子和功能团对配体解离的贡献进行定量估计。**"
layer_2_fragments:
  - "**先枚举离开路径 再预测 koff**"
  - "**自由能曲线不是终点而是特征工程输入**"
  - "**高通量动力学需要把昂贵物理压缩成可学习表示**"
  - "**驻留时间模型必须能回到原子贡献解释**"
layer_3_thesis: "这篇真正有价值的地方在于把高成本的解离动力学问题改写成“先用物理方法枚举路径并压成自由能曲线，再让机器学习做批量外推”的两阶段问题。"
status: complete
---
# 高频筛选 koff，不是把增强采样硬跑一千遍

## Layer 1 — bold key sentences
- **药物分子的解离速率 (koff) 已被证明与疗效的相关性高于其对特定体系的亲和力。**
- **这些方法主要基于增强采样分子动力学模拟，但计算成本高昂。**
- **本文提出了一种基于物理和机器学习相结合的方法。**
- **使用基于物理的配体竞争饱和位点识别 (SILCS) 方法来枚举潜在的配体解离途径，并计算沿这些途径的配体解离自由能曲线。**
- **SILCS-Kinetics工作流程提供了一种研究配体解离动力学的高效方法，包括能够对原子和功能团对配体解离的贡献进行定量估计。**

## Layer 2 — bold fragments
- **先枚举离开路径 再预测 koff**
- **自由能曲线不是终点而是特征工程输入**
- **高通量动力学需要把昂贵物理压缩成可学习表示**
- **驻留时间模型必须能回到原子贡献解释**

## Layer 3 — one-sentence thesis
这篇真正有价值的地方在于把高成本的解离动力学问题改写成“先用物理方法枚举路径并压成自由能曲线，再让机器学习做批量外推”的两阶段问题。

## Concepts (tier_1_atoms)
- `[[path-enumeration-before-kinetics]]`：先找出可能怎么走，再讨论多久走完。
- `[[free-energy-trajectory-as-ml-feature]]`：物理曲线在这里不是结果展示，而是送给模型的中间表示。
- `[[high-throughput-koff-needs-physics-compression]]`：想做大规模动力学预测，必须先把模拟压缩。
- `[[residence-time-explanations-should-be-atomistic]]`：原子与官能团贡献可解释性让模型更适合药化迭代。

## Back-references
- `[[mp-weixin-qq-com-mzkwmzy4nda5ma-2247491586-1-ai-schr-dinger]]`：RAMD+iMetaD 那篇强调“先找主通道再精算”，这篇把同一逻辑进一步工程化成可批量训练的特征抽取流程，说明 kinetic screening 的核心不是哪种增强采样更贵，而是谁能更稳定地产出可学习的路径摘要。
- `[[mp-weixin-qq-com-mzu5otu3nzyyoq-2247489426-1-jctc]]`：ApoDock 处理的是结合态姿势生成，这篇处理的是离开路径枚举；两个工作共同说明 docking 与 kinetics 的差别不只是时间尺度，而是是否需要把“路径”显式纳入表示。
- `[[mp-weixin-qq-com-mzuxmjkzntgyoq-2247490748-1-cpacs-md]]`：cPaCS-MD 那篇追求更准的自由能估计，这篇追求更可扩展的 koff 预测，正好形成“精算单体系”和“压缩多体系”两条不同策略。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzu5otu3nzyyoq-2247490043-1-jctc.md`
- Type: markdown
- Kind: other
