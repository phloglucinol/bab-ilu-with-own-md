---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkxmdc0ntuynq-2247483896-1-claude-code-agent-skill-harness-engineering
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkxmdc0ntuynq-2247483896-1-claude-code-agent-skill-harness-engineering.md
bloom: analyze
concepts:
  - filesystem-as-context
  - reviewer-executor-separation
  - taste-injection
  - handoff-as-api
layer_1_bolds:
  - 代码是高维的，但有价值的设计模式其实是低秩的，我蒸馏的本质就是找到这些主成分。
  - 先建协调机制，再开始干活。
  - Handoff 文档是 Agent 之间的 API。
  - 博客就是那组基向量。
layer_2_fragments:
  - 文件系统先于长提示词
  - review 与 execution 角色分离
  - 新 session 保持 token 预算干净
  - 人的品味用来压缩 action space
layer_3_thesis: 多智能体 harness 的核心不是把提示词写长，而是把角色、交接和共享状态外化到文件系统里，再用人的品味决定抽象方向。
status: complete
---

# 好的 agent harness 先设计协作介质，再讨论模型能力

## Layer 1 — bold key sentences

- **代码是高维的，但有价值的设计模式其实是低秩的，我蒸馏的本质就是找到这些主成分。**
- **先建协调机制，再开始干活。**
- **Handoff 文档是 Agent 之间的 API。**
- **博客就是那组基向量。**

## Layer 2 — bold fragments

- **文件系统先于长提示词**
- **review 与 execution 角色分离**
- **新 session 保持 token 预算干净**
- **人的品味用来压缩 action space**

## Layer 3 — one-sentence thesis

多智能体 harness 的核心不是把提示词写长，而是把角色、交接和共享状态外化到文件系统里，再用人的品味决定抽象方向。

## Concepts (tier_1_atoms)

- [[filesystem-as-context]]：把 repo 和协调文件当系统记录，而不是把上下文塞进单轮 prompt。
- [[reviewer-executor-separation]]：执行者不审自己，验证子代理持续提供新视角。
- [[taste-injection]]：人的偏好不是噪声，而是帮助 agent 收缩搜索空间的基向量。
- [[handoff-as-api]]：handoff 不是备忘录，而是下一轮 clean session 的调用接口。

## Back-references

- [[mp-weixin-qq-com-mzu1mzmxmzcymg-2247799439-1-140-skills]]：那篇谈科研技能编排的工业化平台，这篇则说明平台之前必须先把“技能如何协作”设计清楚。
- [[mp-weixin-qq-com-mzkzntkxodq3na-2247483878-1-ai-ai]]：高管那篇强调把 AI 当系统而非工具，这篇给出了系统化最底层的工程实现方式。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzkxmdc0ntuynq-2247483896-1-claude-code-agent-skill-harness-engineering.md`
- Type: markdown
- Kind: other
