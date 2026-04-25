---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mta4ntc4mw-2247483994-1-biorxiv-2025-medsage-diffusion
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483994-1-biorxiv-2025-medsage-diffusion.md
bloom: analyze
concepts:
  - fragment-retrieval-over-atom-generation
  - ghost-fragment-generation
  - local-validity-by-construction
  - fbdd-as-generative-inductive-bias
layer_1_bolds:
  - "药物发现本质上是一个 FBDD（基于碎片的药物设计）过程。"
  - "如果我们把问题从‘预测 50 个原子的坐标’简化为‘预测 5 个碎片的类型和位置’，复杂度将呈指数级下降。"
  - "如果我们强制模型从一个合法的‘碎片库’里检索组件，那么生成的局部结构天然就是 100% 合理且可合成的。"
  - "Diffusion 终于学会像药化专家那样‘拼积木’了。"
layer_2_fragments:
  - "从原子生成降到碎片检索"
  - "局部合理性应当内建而不是事后修补"
  - "药化专家的工作更像拼积木而不是画自由曲线"
  - "FBDD可以作为生成模型的归纳偏置"
layer_3_thesis: "MedSAGE最重要的不是把扩散模型又做大了一点，而是把生成单位从原子级连续雕刻换成了碎片级检索与放置，因此它把‘可合成、局部合理、可解释’这些药化需求从后验过滤器前移成了模型先验。"
status: complete
---

# mp-weixin-qq-com-mzg4mta4ntc4mw-2247483994-1-biorxiv-2025-medsage-diffusion

## Layer 1 — bold key sentences

- **药物发现本质上是一个 FBDD（基于碎片的药物设计）过程。**
- **如果我们把问题从“预测 50 个原子的坐标”简化为“预测 5 个碎片的类型和位置”，复杂度将呈指数级下降。**
- **如果我们强制模型从一个合法的“碎片库”里检索组件，那么生成的局部结构天然就是 100% 合理且可合成的。**
- **Diffusion 终于学会像药化专家那样“拼积木”了。**

## Layer 2 — bold fragments

- **从原子生成降到碎片检索**
- **局部合理性应当内建而不是事后修补**
- **药化专家的工作更像拼积木而不是画自由曲线**
- **FBDD可以作为生成模型的归纳偏置**

## Layer 3 — one-sentence thesis

MedSAGE最重要的不是把扩散模型又做大了一点，而是把生成单位从原子级连续雕刻换成了碎片级检索与放置，因此它把“可合成、局部合理、可解释”这些药化需求从后验过滤器前移成了模型先验。

## Concepts (tier_1_atoms)

- [[fragment-retrieval-over-atom-generation]]：这篇最核心的范式切换，是让模型检索并摆放碎片，而不是从头生成原子细节。
- [[ghost-fragment-generation]]：“幽灵碎片”是它特有的生成中间表示，值得单独记住。
- [[local-validity-by-construction]]：通过合法碎片库保证局部化学合理性，是一种按构造确保有效性的思路。
- [[fbdd-as-generative-inductive-bias]]：把 FBDD 当作生成模型的归纳偏置，是这篇真正的方法学贡献。

## Back-references

- [[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench]]：MolGenBench说明H2L和fragment条件下的任务更贴近现实，这篇可以被看成对那个结论的直接架构回应。
- [[mp-weixin-qq-com-mzg3otc3ndc0ma-2247487286-1-j-cheminf-poligenx-ai]]：PoLiGenX通过参考分子潜变量来保留设计意图，MedSAGE则通过碎片库显式保留局部合理性，两者都是把“自由生成”改造成“受控扩展”。
- [[mp-weixin-qq-com-mze5odgwota0nq-2247484064-1-nat-comput-sci-phoregen]]：PhoreGen把药效团作为约束，MedSAGE把碎片合法性作为约束；它们都在证明约束不是生成质量的敌人，而是前提。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483994-1-biorxiv-2025-medsage-diffusion.md`
- Type: markdown
- Kind: other
