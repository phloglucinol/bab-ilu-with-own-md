---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzawmjy0odk3nw-2247486028-1-9-ai-ai
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzawmjy0odk3nw-2247486028-1-9-ai-ai.md
bloom: apply
concepts:
  - plan-before-code
  - annotated-spec-loop
  - persistent-research-surface
layer_1_bolds:
  - 永远不要让 AI 写代码，直到你审核并批准了一份书面计划。
  - 把规划和执行分开，是他做的最重要的一件事。
  - Annotate 这个循环通常重复 1 到 6 次。
layer_2_fragments:
  - Research先落成持久化文档
  - 计划文件作为共享可变状态
  - 批注循环注入人的判断
  - 先Todo再实现
layer_3_thesis: AI 编程最该被人类把关的不是补全代码那一刻，而是方案还没凝固成实现之前的那段可修改文本。
status: complete
---

# mp-weixin-qq-com-mzawmjy0odk3nw-2247486028-1-9-ai-ai

## Layer 1 — bold key sentences

- **永远不要让 AI 写代码，直到你审核并批准了一份书面计划。**
- **把规划和执行分开，是他做的最重要的一件事。**
- **Annotate 这个循环通常重复 1 到 6 次。**

## Layer 2 — bold fragments

- **Research 先落成持久化文档**
- **计划文件作为共享可变状态**
- **批注循环注入人的判断**
- **先 Todo 再实现**

## Layer 3 — one-sentence thesis

AI 编程最该被人类把关的不是补全代码那一刻，而是方案还没凝固成实现之前的那段可修改文本。

## Concepts (tier_1_atoms)

- [[plan-before-code]]：没有经过人工批准的书面计划，不进入实现。
- [[annotated-spec-loop]]：通过批注循环把人的约束持续注入同一份规格。
- [[persistent-research-surface]]：研究结果必须落在可审阅文件里，而不是漂在聊天历史中。

## Back-references

- [[mp-weixin-qq-com-mzawmjy0odk3nw-2247486049-1-opencode-ai-web-ui]]：OpenCode 那篇是这套方法论的工具承载层，这篇是流程骨架；前者解释“怎么跑”，后者解释“为什么这样跑”。
- [[mp-weixin-qq-com-mza3mzi4mjgzmw-2651029279-2-transformer-mamba]]：两阶段蒸馏之所以有效，本质上和这里的 plan-annotate 循环一致，都是先建立中间可审查状态，再进入不可逆的执行阶段。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzawmjy0odk3nw-2247486028-1-9-ai-ai.md`
- Type: markdown
- Kind: other
