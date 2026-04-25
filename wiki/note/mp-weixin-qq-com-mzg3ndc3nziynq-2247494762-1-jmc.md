---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg3ndc3nziynq-2247494762-1-jmc
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg3ndc3nziynq-2247494762-1-jmc.md
bloom: analyze
concepts:
  - expert-strategy-augmented-generation
  - molecular-optimization-as-rule-expansion
  - autooptimizer-loop
  - literature-derived-medchem-priors
layer_1_bolds:
  - "整理了近9000种分子优化策略。"
  - "构建了一个名为MolOpt的深度学习框架，以拓展这些结构优化策略。"
  - "作者开发了一个用于分子优化的自动化平台AutoOptimizer。"
  - "这代表了首个以药物化学专家知识为基础、通过深度学习生成的分子优化策略数据库。"
layer_2_fragments:
  - "先把专家策略库化再让模型外推"
  - "优化不是从零生成而是规则扩展"
  - "多轮迭代把少量命中放大成海量候选"
  - "文献药化经验可以变成训练先验"
layer_3_thesis: "这篇工作真正把深度学习放对了位置：不是让模型替代药化家凭空发明修改，而是先把文献中的优化动作整理成策略语料，再让模型在这个动作空间里外推，因此它更像‘可扩展的药化记忆库’而不是一个会做梦的生成器。"
status: complete
---

# mp-weixin-qq-com-mzg3ndc3nziynq-2247494762-1-jmc

## Layer 1 — bold key sentences

- **整理了近9000种分子优化策略。**
- **构建了一个名为MolOpt的深度学习框架，以拓展这些结构优化策略。**
- **作者开发了一个用于分子优化的自动化平台AutoOptimizer。**
- **这代表了首个以药物化学专家知识为基础、通过深度学习生成的分子优化策略数据库。**

## Layer 2 — bold fragments

- **先把专家策略库化再让模型外推**
- **优化不是从零生成而是规则扩展**
- **多轮迭代把少量命中放大成海量候选**
- **文献药化经验可以变成训练先验**

## Layer 3 — one-sentence thesis

这篇工作真正把深度学习放对了位置：不是让模型替代药化家凭空发明修改，而是先把文献中的优化动作整理成策略语料，再让模型在这个动作空间里外推，因此它更像“可扩展的药化记忆库”而不是一个会做梦的生成器。

## Concepts (tier_1_atoms)

- [[expert-strategy-augmented-generation]]：这里的亮点不是模型架构，而是把专家知识作为生成前提而非后处理过滤。
- [[molecular-optimization-as-rule-expansion]]：该工作把分子优化理解为“已有规则的扩展”，而不是重新发明化学空间。
- [[autooptimizer-loop]]：AutoOptimizer体现的是一个标准循环：策略库、候选爆炸、筛选收缩、再迭代。
- [[literature-derived-medchem-priors]]：文献中的成功改造案例可以直接变成机器学习的药化先验。

## Back-references

- [[mp-weixin-qq-com-mzg4mta4ntc4mw-2247484154-1-arxiv-2026-mmpt-rag-quot-quot-foundation-model]]：MMPT-RAG把“改法”抽成变量到变量的动作；这篇是更早的路线，先把文献策略整理成规则库，再让模型围着它做扩展。
- [[mp-weixin-qq-com-mzg3otc3ndc0ma-2247487286-1-j-cheminf-poligenx-ai]]：PoLiGenX更关注保持参考配体的空间意图，这篇更关注扩展药化动作空间；前者像受控生成，后者像受控改造。
- [[mp-weixin-qq-com-mze5odeymta0nq-2247484040-1-nuak1-pk]]：NUAK1那篇提醒我，真正难的是性质分流；因此这里的策略库如果想更实用，迟早要把PK/脑穿透这种性质后果也写进动作标签里。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg3ndc3nziynq-2247494762-1-jmc.md`
- Type: markdown
- Kind: other
