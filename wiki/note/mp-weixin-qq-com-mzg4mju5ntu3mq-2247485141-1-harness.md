---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness.md
bloom: apply
concepts:
  - agent-equals-model-plus-harness
  - workflow-harness
  - decision-harness
  - control-systems-beat-bigger-models
layer_1_bolds:
  - "Agent = Model + Harness"
  - "模型负责生成，Harness负责约束、校验、串流程，让输出变成‘能用的东西’。"
  - "把每个计算单元钉死。Docking 吃什么、吐什么，MD 吃什么、吐什么，全都标准化。"
  - "真正拉开差距的，不是模型，而是外面这层控制系统。"
layer_2_fragments:
  - "工作流标准化比模型聪明更重要"
  - "决策边界必须被外部系统显式化"
  - "化学空间探索需要合法空间而不是搜索空间"
  - "没有Harness的agent只会做演示"
layer_3_thesis: "这篇文章最硬的一句话是‘Agent = Model + Harness’，因为它把很多AI化学系统的失败原因说穿了：问题通常不在模型不够强，而在输入输出、约束、校验和决策边界没有被工程化成一个可重复执行的控制系统。"
status: complete
---

# mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness

## Layer 1 — bold key sentences

- **Agent = Model + Harness**
- **模型负责生成，Harness负责约束、校验、串流程，让输出变成“能用的东西”。**
- **把每个计算单元钉死。Docking 吃什么、吐什么，MD 吃什么、吐什么，全都标准化。**
- **真正拉开差距的，不是模型，而是外面这层控制系统。**

## Layer 2 — bold fragments

- **工作流标准化比模型聪明更重要**
- **决策边界必须被外部系统显式化**
- **化学空间探索需要合法空间而不是搜索空间**
- **没有Harness的agent只会做演示**

## Layer 3 — one-sentence thesis

这篇文章最硬的一句话是“Agent = Model + Harness”，因为它把很多AI化学系统的失败原因说穿了：问题通常不在模型不够强，而在输入输出、约束、校验和决策边界没有被工程化成一个可重复执行的控制系统。

## Concepts (tier_1_atoms)

- [[agent-equals-model-plus-harness]]：这是整篇的主概念，足够通用，可以拿去解释很多 AI 系统为什么 demo 强、生产弱。
- [[workflow-harness]]：把计算单元标准化、串成稳定 I/O 的那一层。
- [[decision-harness]]：用边界、规则和搜索约束把模型决策锁进合法空间的那一层。
- [[control-systems-beat-bigger-models]]：真正拉开差距的是控制系统，而不是再堆一点模型参数。

## Back-references

- [[mp-weixin-qq-com-mzg4mju5ntu3mq-2247484355-1-genmol]]：GenMol那篇的“不是bug，是表示机制”其实就是缺少 harness 暴露与校验后的结果。
- [[mp-weixin-qq-com-mze5mte0njg3nq-2247486105-1-gpu]]：GPU电荷那篇说明高保真计算变便宜后，真正的问题转向如何把它接进默认工作流；这正是 workflow harness 的职责。
- [[mp-weixin-qq-com-mzg4mta4ntc4mw-2247484154-1-arxiv-2026-mmpt-rag-quot-quot-foundation-model]]：MMPT-RAG把药化动作结构化，是 decision harness 在生成模型里的一个具体体现：先定义合法动作，再允许模型扩展。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness.md`
- Type: markdown
- Kind: other
