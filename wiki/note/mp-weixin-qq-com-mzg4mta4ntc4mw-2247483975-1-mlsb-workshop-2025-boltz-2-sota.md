---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mta4ntc4mw-2247483975-1-mlsb-workshop-2025-boltz-2-sota
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483975-1-mlsb-workshop-2025-boltz-2-sota.md
bloom: evaluate
concepts:
  - structure-affinity-misalignment
  - sequence-as-energy-prior
  - geometry-without-thermodynamics
  - hybrid-scoring-workflow
layer_1_bolds:
  - "不要迷信“结构就是一切”。"
  - "在这个任务上，算力消耗巨大的结构大模型，输给了仅仅基于序列的 BERT 类模型。"
  - "这说明问题根本不在于结构准不准，而在于 Boltz-2 的 Embeddings 本身就没有包含足够的“热力学信息”。"
  - "序列依然是王道，直到结构模型学会物理的那一天。"
layer_2_fragments:
  - "结构预测目标与亲和力目标错位"
  - "序列模型携带进化压缩的能量先验"
  - "真实结构输入也救不了错误表征流形"
  - "AI 结构 + 物理打分 + 序列统计的混合流"
layer_3_thesis: "这篇负结果真正打碎的不是 Boltz-2，而是“只要几何更准，能量就会自动显现”的偷懒信念：亲和力需要的是热力学表征，不是更漂亮的坐标。"
---

# Boltz-2 在亲和力预测上的失利暴露了结构表征与热力学表征的错位

## Layer 1 — bold key sentences

> 不要迷信“结构就是一切”。

> 在这个任务上，算力消耗巨大的结构大模型，输给了仅仅基于序列的 BERT 类模型。

> 这说明问题根本不在于结构准不准，而在于 Boltz-2 的 Embeddings 本身就没有包含足够的“热力学信息”。

> 序列依然是王道，直到结构模型学会物理的那一天。

## Layer 2 — bold fragments

- **结构预测目标与亲和力目标错位**
- **序列模型携带进化压缩的能量先验**
- **真实结构输入也救不了错误表征流形**
- **AI 结构 + 物理打分 + 序列统计的混合流**

## Layer 3 — one-sentence thesis

这篇负结果真正打碎的不是 Boltz-2，而是“只要几何更准，能量就会自动显现”的偷懒信念：亲和力需要的是热力学表征，不是更漂亮的坐标。

## Concepts (tier_1_atoms)

- [[structure-affinity-misalignment]] — 训练目标若是 RMSD/FAPE，模型学到的是“像不像晶体结构”，不是“自由能差从哪里来”；这篇文章把任务错位讲清楚了。
- [[sequence-as-energy-prior]] — 序列模型之所以能赢，不是因为它更神秘，而是因为进化本身已经做过长期能量筛选，语言模型吃到了这种压缩过的统计先验。
- [[geometry-without-thermodynamics]] — 即便喂入真实结构，模型仍然不懂结合强弱，说明几何表征和热力学表征不是自然等价物。
- [[hybrid-scoring-workflow]] — 当前更稳妥的策略不是迷信单一端到端模型，而是把结构预测、物理打分和序列统计拼成混合流程。

## Back-references

- [[mp-weixin-qq-com-mjm5mtcymtq5oq-2647507459-1-boltz2]] — 那篇教我如何读取 Boltz-2 的 confidence 和 interface 输出，但这篇说明这些输出主要服务于“结构是否像真”，不是“能量是否可比”；它把参数解读从能力说明书改成了适用范围说明书。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe]] — OpenFE 这类 RBFE 流程直接优化的是自由能差和收敛诊断，因此会把这里的负结果读成对物理打分路线的再正当化：几何生成可以做前置过滤，但能量判别仍要靠专门的热力学工具链。
- [[mp-weixin-qq-com-mzu2odu3mzc4nw-2247513112-1-ai-anewsampling-alphafold3]] — AnewSampling 强调的是构象分布与动态采样，这篇则指出单一静态 embedding 缺失热力学信息；两篇合起来，结构模型若想进入亲和力任务，必须从单帧几何转向分布式动力学表征。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483975-1-mlsb-workshop-2025-boltz-2-sota.md`
- Type: markdown
- Kind: other
