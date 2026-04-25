---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mta4ntc4mw-2247484154-1-arxiv-2026-mmpt-rag-quot-quot-foundation-model
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247484154-1-arxiv-2026-mmpt-rag-quot-quot-foundation-model.md
bloom: analyze
concepts:
  - mmpt-as-atomic-medchem-action
  - rag-for-project-specific-medchem
  - variable-to-variable-generation
  - medchem-intuition-as-retrievable-memory
layer_1_bolds:
  - "把‘怎么改分子’本身变成训练目标，再用RAG把项目经验注进去。"
  - "这个动作是可以跨骨架迁移的。"
  - "这篇工作第一次直接学的是变量→变量的分布。"
  - "RAG不是fine-tuning，不需要为每个项目重新训练，只需要在推理时换一个参考库。"
layer_2_fragments:
  - "把改法而不是整分子当作生成原子"
  - "项目经验可以在推理期注入"
  - "药化直觉适合被做成可检索记忆"
  - "foundation model要学的是动作空间"
layer_3_thesis: "MMPT-RAG真正打开的一扇门，是把药化经验从‘模糊的人类直觉’压缩成可检索、可迁移、可组合的变量变换动作，因此它不像传统生成模型那样在化学空间里漫游，而是在药化动作空间里工作。"
status: complete
---

# mp-weixin-qq-com-mzg4mta4ntc4mw-2247484154-1-arxiv-2026-mmpt-rag-quot-quot-foundation-model

## Layer 1 — bold key sentences

- **把“怎么改分子”本身变成训练目标，再用RAG把项目经验注进去。**
- **这个动作是可以跨骨架迁移的。**
- **这篇工作第一次直接学的是变量→变量的分布。**
- **RAG不是fine-tuning，不需要为每个项目重新训练，只需要在推理时换一个参考库。**

## Layer 2 — bold fragments

- **把改法而不是整分子当作生成原子**
- **项目经验可以在推理期注入**
- **药化直觉适合被做成可检索记忆**
- **foundation model要学的是动作空间**

## Layer 3 — one-sentence thesis

MMPT-RAG真正打开的一扇门，是把药化经验从“模糊的人类直觉”压缩成可检索、可迁移、可组合的变量变换动作，因此它不像传统生成模型那样在化学空间里漫游，而是在药化动作空间里工作。

## Concepts (tier_1_atoms)

- [[mmpt-as-atomic-medchem-action]]：这篇最大的概念创新，是把 MMPT 视为药化动作的原子单位。
- [[rag-for-project-specific-medchem]]：RAG 让项目经验能在推理期注入，而不必重新训练大模型。
- [[variable-to-variable-generation]]：从常量→变量转向变量→变量，是问题定义层面的重写。
- [[medchem-intuition-as-retrievable-memory]]：它提供了一种编码药化经验的新方式：不是规则库，也不是黑箱参数，而是可检索动作记忆。

## Back-references

- [[mp-weixin-qq-com-mzg3ndc3nziynq-2247494762-1-jmc]]：JMC那篇用文献策略库增强优化，这篇把同样的想法更进一步，直接把“替换动作”提升为模型的训练与推理对象。
- [[mp-weixin-qq-com-mze5odgwota0nq-2247486046-1-acs-cent-sci-2026-prompt-drug]]：prompt-drug那篇说明自然语言要落到结构化控制层才可靠，而这篇恰好给出一种更扎实的控制层：MMPT动作。
- [[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness]]：从 harness 视角看，这篇本质上是在给药化生成模型补上一层 decision harness：先限定合法动作空间，再让模型扩展。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247484154-1-arxiv-2026-mmpt-rag-quot-quot-foundation-model.md`
- Type: markdown
- Kind: other
