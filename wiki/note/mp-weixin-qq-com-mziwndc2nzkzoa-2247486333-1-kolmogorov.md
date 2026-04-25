---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mziwndc2nzkzoa-2247486333-1-kolmogorov
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mziwndc2nzkzoa-2247486333-1-kolmogorov.md
bloom: understand
concepts:
  - "[[density-as-random-variable-vs-function]]"
  - "[[backward-equation-from-moving-start-point]]"
  - "[[derivation-needs-interpretation-not-symbol-pushing]]"
layer_1_bolds:
  - "因为终点是随机的，于是引出了终点的概率密度函数，概率密度函数是确定的。"
  - "现在我们把终点固定，移动起点，观察概率密度函数的变化。"
  - "在原文推导中，认为概率密度函数单位时间改变量的条件期望是0，于是就得到了3.42式，这一步我非常不理解。"
layer_2_fragments:
  - "固定终点 改变起点得到倒向视角"
  - "概率密度既是映射又被当作随机变量"
  - "关键卡点不是公式而是零期望假设"
  - "推导链条必须说明物理含义"
layer_3_thesis: 这篇真正有价值的地方不在把倒向方程再推一遍，而在逼我区分“符号上能写通”和“物理上为何成立”其实是两件事。
status: complete
---

# 倒向方程最难的地方不是微分算子 而是你到底在对什么取期望

## Layer 1 — bold key sentences

<!-- Bold verbatim sentences from the source that carry the highest
     conceptual weight. Never paraphrase in Layer 1. -->

- **因为终点是随机的，于是引出了终点的概率密度函数，概率密度函数是确定的。**
- **现在我们把终点固定，移动起点，观察概率密度函数的变化。**
- **在原文推导中，认为概率密度函数单位时间改变量的条件期望是0，于是就得到了3.42式，这一步我非常不理解。**

## Layer 2 — bold fragments

<!-- 3–5 conceptual fragments (not 'interesting phrases').
     Each fragment must anchor at least one downstream concept-atom. -->

- **固定终点 改变起点得到倒向视角**
- **概率密度既是映射又被当作随机变量**
- **关键卡点不是公式而是零期望假设**
- **推导链条必须说明物理含义**

## Layer 3 — one-sentence thesis

<!-- Your synthesis, not the author's thesis. One sentence, no hedges.
     If you need two sentences the note is not atomic yet. -->

这篇真正有价值的地方不在把倒向方程再推一遍，而在逼我区分“符号上能写通”和“物理上为何成立”其实是两件事。

## Concepts (tier_1_atoms)

<!-- Propose concept wikilinks that appear in ≥2 notes.
     Format: `[[concept-slug]]` — explanation of why it earns its place. -->

- `[[density-as-random-variable-vs-function]]`：作者反复纠结的核心其实是同一个对象在不同语境中的身份切换。
- `[[backward-equation-from-moving-start-point]]`：从“移动起点而非终点”看扩散，是这篇最值得带走的视角变换。
- `[[derivation-needs-interpretation-not-symbol-pushing]]`：只会套伊藤公式还不够，关键是假设到底对应什么现实含义。

## Back-references

<!-- Each back-ref must include a specific claim about HOW the other
     note shifts interpretation of this one — not just 'related to X'. -->

- `[[mp-weixin-qq-com-mzg5otkynjqxna-2247485656-1-fokker-planck]]`：如果 Fokker-Planck 那篇更偏正向分布演化，这篇正好补了反向视角，提醒我“同一个扩散过程”可以被两种问题定义重写。
- `[[mp-weixin-qq-com-mzkwmjuynty1mg-2247483922-1-svd]]`：SVD 那篇让我记住“公式压缩的是结构不是意义”，这里则是“偏微分方程压缩的是动力学不是解释”；都在提醒我别把符号变换误认成理解。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mziwndc2nzkzoa-2247486333-1-kolmogorov.md`
- Type: markdown
- Kind: other
