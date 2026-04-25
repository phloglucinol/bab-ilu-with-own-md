---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzizmtkzmjq5oq-2247484028-1-claude-code-100
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzizmtkzmjq5oq-2247484028-1-claude-code-100.md
bloom: apply
concepts:
  - context-window-is-working-memory
  - explicit-verification-loops
  - plan-before-edit
layer_1_bolds:
  - "你发的每一条消息、Claude 读取的每一个文件、它执行的每一条命令，全部都会被写到这块白板上面。"
  - "这篇文章里后面提到的几乎所有方法，归根到底都是在管理这块白板。"
  - "前面多花十分钟做计划，后面能省好几个小时的返工时间。"
layer_2_fragments:
  - "上下文窗口就是工作记忆"
  - "验证标准要前置给模型"
  - "plan mode 的价值是先缩小问题"
  - "subagent 的本质是隔离脏上下文"
layer_3_thesis: "Claude Code 的上限主要取决于你是否把它当作需要工作记忆管理和验证回路的协作者，而不是一次性出答案的聊天机器人。"
status: complete
---

# 用 Claude Code 的分水岭在于你会不会主动管理上下文

## Layer 1

- **你发的每一条消息、Claude 读取的每一个文件、它执行的每一条命令，全部都会被写到这块白板上面。**
- **这篇文章里后面提到的几乎所有方法，归根到底都是在管理这块白板。**
- **前面多花十分钟做计划，后面能省好几个小时的返工时间。**

## Layer 2

- **上下文窗口就是工作记忆**
- **验证标准要前置给模型**
- **plan mode 的价值是先缩小问题**
- **subagent 的本质是隔离脏上下文**

## Layer 3

Claude Code 的上限主要取决于你是否把它当作需要工作记忆管理和验证回路的协作者，而不是一次性出答案的聊天机器人。

## Concepts

- `[[context-window-is-working-memory]]`：上下文不是免费资源，必须像内存一样被管理。
- `[[explicit-verification-loops]]`：把验证条件写进 prompt，能把你从唯一检查者变成监督者。
- `[[plan-before-edit]]`：真正省时间的不是更快开写，而是更晚开写。

## Back-references

- `[[mp-weixin-qq-com-mziynzq3mdm3mw-2247484009-1-2026-skills-90]]`：Skills 那篇把流程固化成 SOP，因此会把这里的技巧从个人习惯改读成可组织化复用的方法。
- `[[mp-weixin-qq-com-mziwmtc4ode0mw-2247719075-1-muon-mamba-gram]]`：Gram 那篇让我把 plan mode 理解得更激进一些，因为它提示真正的性能提升来自先换计算表述，而不是直接去抠实现。
- `[[mp-weixin-qq-com-mziwmtc4ode0mw-2247717801-1-adam-muon-google-magma-sota]]`：Magma 把更新选择交给动量对齐，这会改变我对本 note 的理解：好的 agent workflow 也需要过滤机制，让噪声不要直接进入执行链。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzizmtkzmjq5oq-2247484028-1-claude-code-100.md`
- Type: markdown
- Kind: other
