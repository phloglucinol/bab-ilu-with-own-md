---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-openai-chronicle-48-00
kind: other
ingested_at: 2026-04-25T14:07:20Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-openai-chronicle-48-00.md
bloom: analyze
concepts:
  - ai-as-operating-system
  - context-window-is-working-memory
  - filesystem-as-context
  - multi-surface-agent-workflow
  - agent-equals-model-plus-harness
layer_1_bolds:
  - "不只是聊天更顺了，而是交互方式变了。"
  - "他们不是在做一个单纯的功能替代品，而是将「AI 的眼睛和记忆」从单一产品中直接拆解出来。"
  - "它记住的不是聊天，而是「你在干什么」。"
  - "不同工具之间，也第一次有机会共享同一份「用户上下文」。"
  - "模型可以换，工具可以换，但你的「上下文」始终是连续的。"
layer_2_fragments:
  - "记忆层从产品能力拆成基础设施"
  - "屏幕上下文把指代解析从聊天转向环境读取"
  - "跨会话连续性依赖可迁移的用户上下文"
  - "本地 Markdown SQLite 让记忆变成可审计数据层"
  - "Agent 开始待在工作过程里而不是回答单次问题"
layer_3_thesis: "OpenChronicle 的意义不是复刻一个付费功能，而是把 AI 的工作记忆从平台黑箱改造成本地可迁移、可共享、可审计的上下文层。"
status: complete
---

# OpenChronicle 把 AI 记忆从产品功能拆成用户上下文层

## Layer 1 — bold key sentences

- **不只是聊天更顺了，而是交互方式变了。**
- **他们不是在做一个单纯的功能替代品，而是将「AI 的眼睛和记忆」从单一产品中直接拆解出来。**
- **它记住的不是聊天，而是「你在干什么」。**
- **不同工具之间，也第一次有机会共享同一份「用户上下文」。**
- **模型可以换，工具可以换，但你的「上下文」始终是连续的。**

## Layer 2 — bold fragments

- **记忆层从产品能力拆成基础设施**
- **屏幕上下文把指代解析从聊天转向环境读取**
- **跨会话连续性依赖可迁移的用户上下文**
- **本地 Markdown SQLite 让记忆变成可审计数据层**
- **Agent 开始待在工作过程里而不是回答单次问题**

## Layer 3 — one-sentence thesis

OpenChronicle 的意义不是复刻一个付费功能，而是把 AI 的工作记忆从平台黑箱改造成本地可迁移、可共享、可审计的上下文层。

## Concepts (tier_1_atoms)

- [[ai-as-operating-system]]：这篇给出更底层的版本：操作系统化不只是多开几个 agent，而是让上下文成为跨工具连续层。
- [[context-window-is-working-memory]]：Chronicle/OpenChronicle 把工作记忆从单个对话窗口扩展到屏幕、应用和历史过程。
- [[filesystem-as-context]]：Markdown、SQLite 和本地存储说明上下文可以外化成文件与数据库，而不是被锁在模型会话里。
- [[multi-surface-agent-workflow]]：同一个用户上下文可以被 Claude Code、Codex、OpenCode、桌面端等不同界面消费。
- [[agent-equals-model-plus-harness]]：可共享记忆层本质上是 harness 的状态组件；模型只是读取和使用这层状态。

## Back-references

- [[mp-weixin-qq-com-mzkzntkxodq3na-2247483878-1-ai-ai]]：那篇说 AI 要嵌入长期工作流，这篇补上关键机制：长期工作流需要独立于单个产品的上下文层。
- [[mp-weixin-qq-com-mzizmtkzmjq5oq-2247484028-1-claude-code-100]]：Claude Code 那篇把上下文窗口当工作记忆管理；OpenChronicle 则把工作记忆外置，让它不再随会话边界清空。
- [[mp-weixin-qq-com-mzkxmdc0ntuynq-2247483896-1-claude-code-agent-skill-harness-engineering]]：harness note 强调文件系统和 handoff 是 agent 协作介质，本 note 把同一原则扩展到屏幕级行为记忆。
- [[mp-weixin-qq-com-mzawmjy0odk3nw-2247486049-1-opencode-ai-web-ui]]：OpenCode note 关心多界面共享同一会话状态；OpenChronicle 更进一步，让不同 agent 工具共享同一份用户上下文。
- [[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness]]：如果 agent 真是 model + harness，那么 OpenChronicle 代表的就是 harness 里最稀缺的一块：可迁移、可审计、用户控制的长期状态。

## Source
- Input: `raw/articles/mp-weixin-qq-com-openai-chronicle-48-00.md`
- Type: markdown
- Kind: other
