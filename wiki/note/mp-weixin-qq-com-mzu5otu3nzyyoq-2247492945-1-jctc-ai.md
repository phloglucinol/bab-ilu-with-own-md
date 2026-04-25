---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzu5otu3nzyyoq-2247492945-1-jctc-ai
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzu5otu3nzyyoq-2247492945-1-jctc-ai.md
bloom: analyze
concepts:
  - "[[cryptic-pocket-probability-is-harder-than-direction-of-change]]"
  - "[[ai-and-md-share-low-probability-blind-spot]]"
  - "[[mutation-effect-prediction-can-precede-absolute-calibration]]"
  - "[[conformational-ensembles-still-need-physics]]"
layer_1_bolds:
  - "**用于结构预测的人工智能方法已带来了革命性的变革，但它们尚未充分掌握物理学原理，因而无法全面表征蛋白质的整个构象集合。**"
  - "**本文对这些AI模型以及基于物理学的分子动力学模拟进行了基准测试。**"
  - "**多种方法在预测特定突变究竟会增加还是降低隐匿性口袋的开启概率方面，均取得了显著的成功。**"
  - "**尚无任何方法能够可靠地预测口袋开启的绝对概率。**"
  - "**面对那些实验测得开启概率极低的口袋时，所有方法均显得力不从心。**"
layer_2_fragments:
  - "**会不会变大比到底开多少更容易预测**"
  - "**低概率口袋是 AI 和 MD 的共同盲区**"
  - "**构象集合问题不能只靠静态结构模型**"
  - "**突变效应预测与绝对热力学校准不是同一难度**"
layer_3_thesis: "这篇把隐匿口袋问题拆得很清楚：当前方法已经能判断突变会把口袋推向更开还是更关，但离“可靠给出口袋开放绝对概率”还差着一整层对低概率构象集合的物理刻画能力。"
status: complete
---
# 预测隐匿口袋时，方向判断已经会了，定量校准还远没会

## Layer 1 — bold key sentences

<!-- Bold verbatim sentences from the source that carry the highest
     conceptual weight. Never paraphrase in Layer 1. -->

- **用于结构预测的人工智能方法已带来了革命性的变革，但它们尚未充分掌握物理学原理，因而无法全面表征蛋白质的整个构象集合。**
- **本文对这些AI模型以及基于物理学的分子动力学模拟进行了基准测试。**
- **多种方法在预测特定突变究竟会增加还是降低隐匿性口袋的开启概率方面，均取得了显著的成功。**
- **尚无任何方法能够可靠地预测口袋开启的绝对概率。**
- **面对那些实验测得开启概率极低的口袋时，所有方法均显得力不从心。**

## Layer 2 — bold fragments

<!-- 3–5 conceptual fragments (not 'interesting phrases').
     Each fragment must anchor at least one downstream concept-atom. -->

- **会不会变大比到底开多少更容易预测**
- **低概率口袋是 AI 和 MD 的共同盲区**
- **构象集合问题不能只靠静态结构模型**
- **突变效应预测与绝对热力学校准不是同一难度**

## Layer 3 — one-sentence thesis

<!-- Your synthesis, not the author's thesis. One sentence, no hedges.
     If you need two sentences the note is not atomic yet. -->

这篇把隐匿口袋问题拆得很清楚：当前方法已经能判断突变会把口袋推向更开还是更关，但离“可靠给出口袋开放绝对概率”还差着一整层对低概率构象集合的物理刻画能力。

## Concepts (tier_1_atoms)

<!-- Propose concept wikilinks that appear in ≥2 notes.
     Format: `[[concept-slug]]` — explanation of why it earns its place. -->

- `[[cryptic-pocket-probability-is-harder-than-direction-of-change]]`：相对变化比绝对概率更容易建模。
- `[[ai-and-md-share-low-probability-blind-spot]]`：问题不只在 AI，低概率态本身就是难采样对象。
- `[[mutation-effect-prediction-can-precede-absolute-calibration]]`：可以先用来做筛突变，再谈定量热力学。
- `[[conformational-ensembles-still-need-physics]]`：构象集合问题最终仍要回到物理采样和校准。

## Back-references

<!-- Each back-ref must include a specific claim about HOW the other
     note shifts interpretation of this one — not just 'related to X'. -->

- `[[mp-weixin-qq-com-mzu5otu3nzyyoq-2247489426-1-jctc]]`：ApoDock 处理的是口袋已给定时的局部几何修复，这篇提醒在那一步之前还有更难的一层问题，即口袋本身是否会开、开到什么频率。
- `[[mp-weixin-qq-com-mzu5otu3nzyyoq-2247492421-1-nature-ml]]`：PoseBench 证明结构预测在未知结合态上仍然不稳，这篇把这种“不稳”进一步量化为构象概率分布失真，尤其是低占比开放态的失真。
- `[[mp-weixin-qq-com-mzkwmzy4nda5ma-2247491586-1-ai-schr-dinger]]`：RAMD+iMetaD 那篇展示了动力学精算要靠路径与概率显式建模；这里的隐匿口袋问题也是同类困难，只不过对象从配体解离换成了口袋开放。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzu5otu3nzyyoq-2247492945-1-jctc-ai.md`
- Type: markdown
- Kind: other
