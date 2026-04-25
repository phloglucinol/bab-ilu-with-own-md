---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mjm5mtcymtq5oq-2647507459-1-boltz2
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mjm5mtcymtq5oq-2647507459-1-boltz2.md
bloom: apply
concepts:
  - confidence-metrics-as-gates
  - sampling-budget-allocation
  - structure-affinity-dual-output
  - physics-steering
layer_1_bolds:
  - "相比前代 Boltz-1，Boltz-2 不仅能预测蛋白质复合物的三维结构，还新增了结合亲和力预测功能。"
  - "复合评分 = 0.8 × pLDDT + 0.2 × iPTM，用于预测结果排序。"
  - "使用 recycling_steps=10 和 diffusion_samples=25 可达到 AlphaFold3 的默认参数水平，但预测时间会显著延长。"
  - "高分只表示模型自信，可能存在假阳性。"
layer_2_fragments:
  - "用多指标而不是单一分数判断结果"
  - "把采样步数、样本数和seed当成预算分配问题"
  - "亲和力预测需要独立扩散预算"
  - "物理势能引导提高立体化学合理性"
  - "高分不等于真实结合"
layer_3_thesis: "Boltz2的真正价值不在于给出一个更神秘的总分，而在于把结构质量、亲和力估计和采样成本拆成可操作的控制面板，使用户第一次能系统地管理‘算多少、信什么、筛到哪一步为止’。"
status: complete
---

# mp-weixin-qq-com-mjm5mtcymtq5oq-2647507459-1-boltz2

## Layer 1 — bold key sentences

- **相比前代 Boltz-1，Boltz-2 不仅能预测蛋白质复合物的三维结构，还新增了结合亲和力预测功能。**
- **复合评分 = 0.8 × pLDDT + 0.2 × iPTM，用于预测结果排序。**
- **使用 recycling_steps=10 和 diffusion_samples=25 可达到 AlphaFold3 的默认参数水平，但预测时间会显著延长。**
- **高分只表示模型自信，可能存在假阳性。**

## Layer 2 — bold fragments

- **用多指标而不是单一分数判断结果**
- **把采样步数、样本数和seed当成预算分配问题**
- **亲和力预测需要独立扩散预算**
- **物理势能引导提高立体化学合理性**
- **高分不等于真实结合**

## Layer 3 — one-sentence thesis

Boltz2的真正价值不在于给出一个更神秘的总分，而在于把结构质量、亲和力估计和采样成本拆成可操作的控制面板，使用户第一次能系统地管理“算多少、信什么、筛到哪一步为止”。

## Concepts (tier_1_atoms)

- [[confidence-metrics-as-gates]]：这篇最适合抽出来的不是某个参数，而是“不同指标对应不同决策门槛”的工作流思想。
- [[sampling-budget-allocation]]：`recycling_steps`、`sampling_steps`、`diffusion_samples` 和多 seed 策略共同构成计算预算分配问题。
- [[structure-affinity-dual-output]]：Boltz2 相比 AF3 系最显著的差异是把结构预测和亲和力估计放进同一框架输出。
- [[physics-steering]]：Boltz-Steering 提醒我，生成模型的物理合理性可以在采样期显式纠偏，而不是完全依赖后处理。

## Back-references

- [[mp-weixin-qq-com-mze5odgwota0nq-2247485295-1-pnas-2025-siteaf3-alphafold3]]：SiteAF3说明“口袋条件化”能提高结构放置正确率；回看 Boltz2，就能把它理解成更像通用推理平台，而不是位点控制器。
- [[mp-weixin-qq-com-mzkyntmznzm3nq-2247483762-1-af3-dream-20-35-ai]]：DREAM强调把预测器反转成设计器，这会逼我意识到 Boltz2 当前仍主要解决筛选与评估，而不是把设计变量直接纳入梯度闭环。
- [[mp-weixin-qq-com-mzyzodi1otazna-2247486534-1-boltzgen-sciminer]]：如果 BoltzGen 代表“先生成候选再筛”，那 Boltz2 这套参数学的意义就在于为筛选阶段建立一套更透明的资源分级方法，而不是宣称任何单次预测就是答案。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mjm5mtcymtq5oq-2647507459-1-boltz2.md`
- Type: markdown
- Kind: other
