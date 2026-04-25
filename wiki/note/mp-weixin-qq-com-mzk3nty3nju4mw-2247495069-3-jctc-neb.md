---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk3nty3nju4mw-2247495069-3-jctc-neb
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk3nty3nju4mw-2247495069-3-jctc-neb.md
bloom: understand
concepts:
  - "[[active-learning-neb]]"
  - "[[barrier-search-efficiency]]"
  - "[[transition-path-budgeting]]"
  - "[[surrogate-guided-quantum-workflow]]"
layer_1_bolds:
  - "**主动学习算法结合NEB高效计算过渡态。**"
  - "**高效。**"
  - "**过渡态。**"
  - "**主动学习。**"
  - "**NEB。**"
layer_2_fragments:
  - "**用主动学习缩短昂贵路径搜索**"
  - "**NEB 仍是路径优化骨架**"
  - "**代理模型负责把算力投到最有信息的位置**"
  - "**过渡态工作流的瓶颈在采样预算分配**"
  - "**路径搜索越来越像数据驱动实验设计**"
layer_3_thesis: "即使这篇原文在当前抓取里信息不完整，我仍能确定它指向一个越来越清晰的趋势：过渡态搜索的核心竞争力不再只是更强的量化方法，而是谁能更聪明地分配每一步昂贵计算。"
status: complete
---

# 主动学习版 NEB 把过渡态搜索问题改写成预算分配问题

## Layer 1 — bold key sentences

- **主动学习算法结合NEB高效计算过渡态。**
- **高效。**
- **过渡态。**
- **主动学习。**
- **NEB。**

## Layer 2 — bold fragments

- **用主动学习缩短昂贵路径搜索**
- **NEB 仍是路径优化骨架**
- **代理模型负责把算力投到最有信息的位置**
- **过渡态工作流的瓶颈在采样预算分配**
- **路径搜索越来越像数据驱动实验设计**

## Layer 3 — one-sentence thesis

即使这篇原文在当前抓取里信息不完整，我仍能确定它指向一个越来越清晰的趋势：过渡态搜索的核心竞争力不再只是更强的量化方法，而是谁能更聪明地分配每一步昂贵计算。

## Concepts (tier_1_atoms)

- `[[active-learning-neb]]`：主动学习与 NEB 的结合值得单独记住，因为它改变的是工作流而不是单一势能面近似。
- `[[barrier-search-efficiency]]`：过渡态方法的比较应逐渐从“算得准不准”转向“单位算力能找出多少有效路径”。
- `[[transition-path-budgeting]]`：路径搜索中的每个采样点都像预算决策。
- `[[surrogate-guided-quantum-workflow]]`：量化流程正在被代理模型重新组织。

## Back-references

- `[[mp-weixin-qq-com-mzkwotcynjk3na-2247483796-1-units-ai]]`：UniTS 处理的是“第一公里”的初猜生成；这篇很可能处理的是“后半程”的路径优化，二者拼起来才是更完整的 TS 自动化工作流。
- `[[mp-weixin-qq-com-mzkwmji4odg2na-2247484368-1-jcim-admet]]`：ADMET 去噪那篇说明机器学习可以先做数据质量控制；这里则是另一种分工，让模型先做算力路由而不是直接替代量化计算。
- `[[mp-weixin-qq-com-mzk2ndc3ntk1mg-2247483806-1-jcim]]`：BD+MD 那篇把 kon 计算拆成两个区域；这里提供了另一个同构思路，即复杂物理流程应先找最昂贵的环节，再用学习器压缩它。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzk3nty3nju4mw-2247495069-3-jctc-neb.md`
- Type: markdown
- Kind: other
