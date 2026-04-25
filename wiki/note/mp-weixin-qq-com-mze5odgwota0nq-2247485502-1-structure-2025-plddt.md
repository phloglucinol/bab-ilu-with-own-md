---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mze5odgwota0nq-2247485502-1-structure-2025-plddt
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mze5odgwota0nq-2247485502-1-structure-2025-plddt.md
bloom: analyze
concepts:
  - confidence-is-not-dynamics
  - single-structure-certainty-vs-ensemble-flexibility
  - plddt-misuse-in-flexibility-studies
  - structure-prediction-metrics-have-ontology
layer_1_bolds:
  - "pLDDT本质上衡量的是模型对单一结构假设的确定性，而非蛋白质在不同时间尺度上的构象采样能力。"
  - "高pLDDT并不等同于结构刚性。"
  - "pLDDT值反映的是模型对某一单一结构假设的内部确定性，而非蛋白质真实存在的构象能景。"
  - "它并未包含任何关于动力学时间尺度的信息。"
layer_2_fragments:
  - "把置信度指标误读成柔性指标"
  - "单构象自信与多构象可达性是两回事"
  - "代理量混淆会直接污染机制解释"
  - "动力学需要时间尺度而不是高分"
layer_3_thesis: "pLDDT最容易误导人的地方在于它看起来像一个关于蛋白本体的分数，但它真正描述的是模型对某一静态答案的把握，因此任何把它直接翻译成‘柔性大小’的做法都是把认识论指标误当本体论性质。"
status: complete
---

# mp-weixin-qq-com-mze5odgwota0nq-2247485502-1-structure-2025-plddt

## Layer 1 — bold key sentences

- **pLDDT本质上衡量的是模型对单一结构假设的确定性，而非蛋白质在不同时间尺度上的构象采样能力。**
- **高pLDDT并不等同于结构刚性。**
- **pLDDT值反映的是模型对某一单一结构假设的内部确定性，而非蛋白质真实存在的构象能景。**
- **它并未包含任何关于动力学时间尺度的信息。**

## Layer 2 — bold fragments

- **把置信度指标误读成柔性指标**
- **单构象自信与多构象可达性是两回事**
- **代理量混淆会直接污染机制解释**
- **动力学需要时间尺度而不是高分**

## Layer 3 — one-sentence thesis

pLDDT最容易误导人的地方在于它看起来像一个关于蛋白本体的分数，但它真正描述的是模型对某一静态答案的把握，因此任何把它直接翻译成“柔性大小”的做法都是把认识论指标误当本体论性质。

## Concepts (tier_1_atoms)

- `[[confidence-is-not-dynamics]]` — 这是全文最可迁移的判断，适用于所有把模型信心直接转译成物理性质的场景。
- `[[single-structure-certainty-vs-ensemble-flexibility]]` — 文章实际讨论的是“确定一个构象”与“遍历构象集合”这两个任务的范畴差异。
- `[[plddt-misuse-in-flexibility-studies]]` — pLDDT被拿来代替柔性指标已经形成一种常见误用，值得单独立项记住。
- `[[structure-prediction-metrics-have-ontology]]` — 指标不是中性容器，每个指标都携带自己测量对象的本体论边界。

## Back-references

- `[[mp-weixin-qq-com-mjm5mtcymtq5oq-2647507459-1-boltz2]]` — Boltz2那篇也提醒“高分不等于真实结合”；这篇把同样的认识推进一步，说明即便在结构预测里，高分也只是在某个任务定义下的自信。
- `[[mp-weixin-qq-com-mze5mte0njg3nq-2247486105-1-gpu]]` — GPU电荷那篇提供了一个反面对照：有些物理问题必须上更贵的显式计算，而不能拿方便分数替代。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483849-1-tmlr-2025-gnn-transformer-3d]]` — Transformer学会欧氏距离不等于它学会动力学，这篇能防止我把“结构表征能力”继续误推成“运动表征能力”。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mze5odgwota0nq-2247485502-1-structure-2025-plddt.md`
- Type: markdown
- Kind: other
