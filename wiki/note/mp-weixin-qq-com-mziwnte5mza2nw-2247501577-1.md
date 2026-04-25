---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mziwnte5mza2nw-2247501577-1
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mziwnte5mza2nw-2247501577-1.md
bloom: analyze
concepts:
  - redocking-does-not-equal-screening
  - solvent-model-is-task-dependent
  - template-guidance-beats-water-tuning
layer_1_bolds:
  - "片段对接与打分精度目前仍是主要挑战。"
  - "重对接性能不能直接等价于交叉对接场景下的排序优势，仅凭重对接结论指导真实片段筛选存在风险。"
  - "在片段生长场景中，依赖水模型优化收益甚微，过度水分子约束甚至有害，而模板对接策略远优于水模型调优。"
layer_2_fragments:
  - "重对接成功不等于交叉对接成功"
  - "保留全部水分子会改善一种任务却破坏另一种任务"
  - "模板约束比继续调溶剂模型更有效"
  - "共识策略比单一软件结论更稳健"
layer_3_thesis: "这篇最有价值的地方是把“对接精度”拆成具体任务情境，从而逼你承认同一套评分与溶剂处理策略不可能同时服务重对接、片段生长和片段筛选。"
status: complete
---

# 片段对接里最危险的误判是把重对接成绩当成真实筛选能力

## Layer 1

- **片段对接与打分精度目前仍是主要挑战。**
- **重对接性能不能直接等价于交叉对接场景下的排序优势，仅凭重对接结论指导真实片段筛选存在风险。**
- **在片段生长场景中，依赖水模型优化收益甚微，过度水分子约束甚至有害，而模板对接策略远优于水模型调优。**

## Layer 2

- **重对接成功不等于交叉对接成功**
- **保留全部水分子会改善一种任务却破坏另一种任务**
- **模板约束比继续调溶剂模型更有效**
- **共识策略比单一软件结论更稳健**

## Layer 3

这篇最有价值的地方是把“对接精度”拆成具体任务情境，从而逼你承认同一套评分与溶剂处理策略不可能同时服务重对接、片段生长和片段筛选。

## Concepts

- `[[redocking-does-not-equal-screening]]`：离线 benchmark 分数高，不代表前瞻性筛选真的可用。
- `[[solvent-model-is-task-dependent]]`：水分子处理不是通用增强项，而是强依赖任务目标。
- `[[template-guidance-beats-water-tuning]]`：在 LinF 这类问题里，给结构先验比继续抠溶剂细节更重要。

## Back-references

- `[[mp-weixin-qq-com-mzixmjywota4oq-2247485714-1-drugclip-posebench-immunostruct]]`：PoseBench 那部分系统比较了深度学习对接的泛化缺口，所以它会把这篇的“软件差异”改读成“评测任务定义差异”，问题不只是工具弱，而是 benchmark 常常测错了能力。
- `[[mp-weixin-qq-com-mzixmjywota4oq-2247485483-1-acc-chem-res]]`：自由能那篇强调不同方法适合不同研发阶段，这会改变我对本 note 的理解：片段对接也应按研发问题选方法，而不是追求单一全能流程。
- `[[mp-weixin-qq-com-mzuxoty3otk2ma-2247487749-1-km-kcat]]`：酶动力学那篇指出强结合可能是非生产性结合，这条反过来帮助我理解片段对接里的错误高分，本质上也是“结合得紧但姿态不对”。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mziwnte5mza2nw-2247501577-1.md`
- Type: markdown
- Kind: other
