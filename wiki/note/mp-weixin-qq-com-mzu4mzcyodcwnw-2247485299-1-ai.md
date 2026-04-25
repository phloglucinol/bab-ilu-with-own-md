---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzu4mzcyodcwnw-2247485299-1-ai
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzu4mzcyodcwnw-2247485299-1-ai.md
bloom: analyze
concepts:
  - white-box-statistical-potentials-can-still-win
  - docking-and-screening-need-different-potentials
  - affinity-weighting-improves-statistical-potentials
layer_1_bolds:
  - 通过精心设计的统计势能模型，不仅能实现媲美甚至超越顶尖DL模型的效果，还具备极佳的物理可解释性。
  - 对接更依赖于具有明确物理意义的距离相关原子-原子势能。
  - 筛选更依赖于能够捕捉局部化学环境的方向相关原子-残基势能。
layer_2_fragments:
  - 老派统计势能并未过时
  - 对接和筛选不是同一种任务
  - 亲和力加权减少低质量噪声
  - 白盒模型在小数据下很能打
layer_3_thesis: HybridSP最有启发的一点是它把“传统方法 vs 深度学习”这种空泛对立拆开了，说明真正该问的是任务需要哪种归纳偏置，而不是谁更新潮。
status: complete
---

# mp-weixin-qq-com-mzu4mzcyodcwnw-2247485299-1-ai

## Layer 1 — bold key sentences

- **通过精心设计的统计势能模型，不仅能实现媲美甚至超越顶尖DL模型的效果，还具备极佳的物理可解释性。**
- **对接更依赖于具有明确物理意义的距离相关原子-原子势能。**
- **筛选更依赖于能够捕捉局部化学环境的方向相关原子-残基势能。**

## Layer 2 — bold fragments

- **老派统计势能并未过时**
- **对接和筛选不是同一种任务**
- **亲和力加权减少低质量噪声**
- **白盒模型在小数据下很能打**

## Layer 3 — one-sentence thesis

HybridSP最有启发的一点是它把“传统方法 vs 深度学习”这种空泛对立拆开了，说明真正该问的是任务需要哪种归纳偏置，而不是谁更新潮。

## Concepts (tier_1_atoms)

- [[white-box-statistical-potentials-can-still-win]]：统计势能在数据有限或任务定义清晰时仍可能优于DL。
- [[docking-and-screening-need-different-potentials]]：对接与筛选需要不同的势能结构，不能混成一个分数。
- [[affinity-weighting-improves-statistical-potentials]]：用亲和力质量给样本加权，可显著改善统计势能。

## Back-references

- [[mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025.md]]：那篇质疑很多AI药物模型的评估可信度，这篇给出一个实际对照物，提醒我别把“深度学习更强”当默认前提。
- [[mp-weixin-qq-com-mzu3mtczmjmymq-2247484806-1]]：π-π那篇批评模糊相互作用标签，这篇的优势就在于它把相互作用拆成可量化的方向和环境势能，而不是凭直觉命名。
- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim]]：BALM说明大模型在严格切分下仍有价值，这篇则补上另一边界条件：如果数据不够、物理结构强，白盒统计势能仍可能是更可靠的起点。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzu4mzcyodcwnw-2247485299-1-ai.md`
- Type: markdown
- Kind: other
