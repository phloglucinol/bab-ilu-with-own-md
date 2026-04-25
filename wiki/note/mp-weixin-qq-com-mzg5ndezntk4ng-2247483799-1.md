---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg5ndezntk4ng-2247483799-1
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg5ndezntk4ng-2247483799-1.md
bloom: understand
concepts:
  - "[[manifold-navigation-for-llms]]"
  - "[[prompt-as-entry-selector]]"
  - "[[cot-as-geometric-stabilizer]]"
  - "[[tool-use-as-state-jump]]"
layer_1_bolds:
  - "大模型是在一个极高维的参数空间内，学习并贴合一个低维的流形（Manifold）结构。"
  - "Prompt 的作用是将模型的初始状态推入某个特定的子流形（Sub-manifold）的“吸引盆”中。"
  - "Chain-of-Thought (CoT) 的本质，是将隐式轨迹显式化，以换取几何稳定性。"
  - "设计一个好的 AI 系统，本质上就是在设计一套高效的“流形导航与约束系统”。"
layer_2_fragments:
  - "高维是画布，低维是画作"
  - "Prompt 负责入口定位而非教学"
  - "CoT 通过小步再投影降低偏航"
  - "RAG 改变势能场，Graph RAG 铺设路径"
  - "Tool-use 是跳出封闭流形的状态跃迁"
layer_3_thesis: "把 LLM 看成流形导航系统之后，Prompt、CoT、RAG 和 Tool-use 就不再是零散技巧，而是同一套“如何让轨迹留在可达真值区域”的几何控制手段。"
---

# 用流形导航视角统一理解 Prompt、CoT、RAG 与 Tool-use

## Layer 1 — bold key sentences

- **大模型是在一个极高维的参数空间内，学习并贴合一个低维的流形（Manifold）结构。**
- **Prompt 的作用是将模型的初始状态推入某个特定的子流形（Sub-manifold）的“吸引盆”中。**
- **Chain-of-Thought (CoT) 的本质，是将隐式轨迹显式化，以换取几何稳定性。**
- **设计一个好的 AI 系统，本质上就是在设计一套高效的“流形导航与约束系统”。**

## Layer 2 — bold fragments

- **高维是画布，低维是画作**
- **Prompt 负责入口定位而非教学**
- **CoT 通过小步再投影降低偏航**
- **RAG 改变势能场，Graph RAG 铺设路径**
- **Tool-use 是跳出封闭流形的状态跃迁**

## Layer 3 — one-sentence thesis

把 LLM 看成流形导航系统之后，Prompt、CoT、RAG 和 Tool-use 就不再是零散技巧，而是同一套“如何让轨迹留在可达真值区域”的几何控制手段。

## Concepts (tier_1_atoms)

- `[[manifold-navigation-for-llms]]` — 这篇把许多经验技巧压成一个统一视角，方便和后续系统设计笔记互相校准。
- `[[prompt-as-entry-selector]]` — Prompt 不教知识，只负责把模型推到正确局部，这个表述很适合拿来约束我写 prompt 时的预期。
- `[[cot-as-geometric-stabilizer]]` — CoT 的价值不再是“让模型更会想”，而是“把大跳跃拆成带纠偏的小步”。
- `[[tool-use-as-state-jump]]` — 工具调用的本质是非连续外部跳转，这个说法能把 agent 系统和纯语言推理明确区分开。

## Back-references

- `[[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness]]` — harness 那篇从工程组织面谈控制层和协作介质，这篇从几何面谈轨迹约束；并在一起看，系统设计的重要性就不只是经验偏好，而是为了让推理轨迹持续落在可控流形上。
- `[[mp-weixin-qq-com-mzawmjy0odk3nw-2247486028-1-9-ai-ai]]` — Boris 那篇要求把计划、批注、执行分层保存，从这篇视角看，那其实是在模型外部铺设一条更稳定的导航轨道，减少一次大跳直达答案时的偏航概率。
- `[[mp-weixin-qq-com-mziwmtc4ode0mw-2247716057-1-transformer]]` — Transformer 那篇更像内部机理解释，把注意力看成概率更新；这篇则提供外部系统比喻，说明 Prompt、RAG、Tool-use 为什么能在不改模型参数的前提下改变推理路径。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg5ndezntk4ng-2247483799-1.md`
- Type: markdown
- Kind: other
