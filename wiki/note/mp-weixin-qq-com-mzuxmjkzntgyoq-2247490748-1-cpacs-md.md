---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzuxmjkzntgyoq-2247490748-1-cpacs-md
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzuxmjkzntgyoq-2247490748-1-cpacs-md.md
bloom: apply
concepts:
  - "[[contact-coordinate-beats-centroid-distance-for-peptides]]"
  - "[[peptide-binding-free-energy-needs-dissociation-realism]]"
  - "[[msm-can-reconstruct-free-energy-without-umbrella-sampling]]"
  - "[[accurate-peptide-affinity-can-come-from-better-coordinate-choice]]"
layer_1_bolds:
  - "**肽–蛋白结合自由能的计算预测始终是一个难题。**"
  - "**cPaCS-MD 则引入了蛋白–肽原子接触距离，更真实地反映了肽从结合位点逐步解离的物理过程。**"
  - "**研究将 cPaCS-MD 与 马尔可夫状态模型（MSM） 相结合，直接从解离轨迹中重构自由能景观，无需额外的伞形采样。**"
  - "**计算得到的结合自由能与实验结果高度一致，相关系数达到 R² = 0.84。**"
  - "**相比伞形采样需要预先假设解离路径并进行大量受限模拟，cPaCS-MD 能在更短的模拟时间内获得平滑、连续且可逆的解离过程。**"
layer_2_fragments:
  - "**对肽体系 质心距离是坏反应坐标**"
  - "**接触距离更接近真实解离物理**"
  - "**MSM 可以接管自由能重构**"
  - "**更准不一定来自更贵 也可能来自坐标选对了**"
layer_3_thesis: "cPaCS-MD 最值得记住的是，它不是靠更暴力的采样赢过伞形采样，而是先把肽解离的反应坐标从质心距离换成接触距离，再让 MSM 把这些更物理的轨迹重组为自由能景观。"
status: complete
---
# 肽-蛋白自由能难算，常常不是采样不够，而是坐标先选错了

## Layer 1 — bold key sentences

<!-- Bold verbatim sentences from the source that carry the highest
     conceptual weight. Never paraphrase in Layer 1. -->

- **肽–蛋白结合自由能的计算预测始终是一个难题。**
- **cPaCS-MD 则引入了蛋白–肽原子接触距离，更真实地反映了肽从结合位点逐步解离的物理过程。**
- **研究将 cPaCS-MD 与 马尔可夫状态模型（MSM） 相结合，直接从解离轨迹中重构自由能景观，无需额外的伞形采样。**
- **计算得到的结合自由能与实验结果高度一致，相关系数达到 R² = 0.84。**
- **相比伞形采样需要预先假设解离路径并进行大量受限模拟，cPaCS-MD 能在更短的模拟时间内获得平滑、连续且可逆的解离过程。**

## Layer 2 — bold fragments

<!-- 3–5 conceptual fragments (not 'interesting phrases').
     Each fragment must anchor at least one downstream concept-atom. -->

- **对肽体系 质心距离是坏反应坐标**
- **接触距离更接近真实解离物理**
- **MSM 可以接管自由能重构**
- **更准不一定来自更贵 也可能来自坐标选对了**

## Layer 3 — one-sentence thesis

<!-- Your synthesis, not the author's thesis. One sentence, no hedges.
     If you need two sentences the note is not atomic yet. -->

cPaCS-MD 最值得记住的是，它不是靠更暴力的采样赢过伞形采样，而是先把肽解离的反应坐标从质心距离换成接触距离，再让 MSM 把这些更物理的轨迹重组为自由能景观。

## Concepts (tier_1_atoms)

<!-- Propose concept wikilinks that appear in ≥2 notes.
     Format: `[[concept-slug]]` — explanation of why it earns its place. -->

- `[[contact-coordinate-beats-centroid-distance-for-peptides]]`：肽体系里反应坐标定义会直接决定自由能质量。
- `[[peptide-binding-free-energy-needs-dissociation-realism]]`：自由能预测要先尊重肽真实离开口袋的方式。
- `[[msm-can-reconstruct-free-energy-without-umbrella-sampling]]`：MSM 在这里从分析工具变成了核心重构器。
- `[[accurate-peptide-affinity-can-come-from-better-coordinate-choice]]`：方法提升来自问题表述修正。

## Back-references

<!-- Each back-ref must include a specific claim about HOW the other
     note shifts interpretation of this one — not just 'related to X'. -->

- `[[mp-weixin-qq-com-mzu5otu3nzyyoq-2247490043-1-jctc]]`：SILCS-Kinetics 也是先枚举路径再让后端模型吃进去，这篇则证明即使不接 ML，只要把路径坐标定义得更物理，也能显著改善自由能预测。
- `[[mp-weixin-qq-com-mzkwmzy4nda5ma-2247491586-1-ai-schr-dinger]]`：RAMD+iMetaD 解决的是驻留时间预测中的“先找主通道”，这篇解决的是肽解离自由能中的“先找对反应坐标”，二者都说明动力学和热力学计算前半程的问题定义最关键。
- `[[mp-weixin-qq-com-mzuxmjkzntgyoq-2247490882-1-neuralmd]]`：NeuralMD 想用学习框架重建动力学，这篇给出一个务实提醒：哪怕完全在传统 MD 范式内，只要把坐标和状态重构设计好，也仍有巨大改进空间。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzuxmjkzntgyoq-2247490748-1-cpacs-md.md`
- Type: markdown
- Kind: other
