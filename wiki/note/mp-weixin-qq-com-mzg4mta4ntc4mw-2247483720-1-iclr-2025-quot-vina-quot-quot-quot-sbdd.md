---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mta4ntc4mw-2247483720-1-iclr-2025-quot-vina-quot-quot-quot-sbdd
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483720-1-iclr-2025-quot-vina-quot-quot-quot-sbdd.md
bloom: analyze
concepts:
  - "[[docking-score-hacking]]"
  - "[[practical-need-aligned-evaluation]]"
  - "[[virtual-screening-template-utility]]"
  - "[[benchmark-bias-in-sbdd]]"
layer_1_bolds:
  - "当前 SBDD 社区流行的评估指标（尤其是 Vina docking score），在很大程度上是‘可被模型轻易 hack 的理论指标’。"
  - "把生成分子当成 虚拟筛选的‘模板’。"
  - "真正有用的生成分子，不一定要自己就是‘好药’，但至少要能 帮助我们在真实化合物库里找到更多活性分子。"
  - "CrossDocked 数据集本身存在明显问题。"
layer_2_fragments:
  - "Vina低分不等于实用分子"
  - "评估要围绕下游用途而不是理论分数"
  - "生成分子更像筛库模板而非终产物"
  - "训练基准的偏差会被模型放大"
layer_3_thesis: "这篇工作的价值在于把SBDD评测从‘模型能不能刷出更低的对接分’转成‘这些分子是否能在真实筛选链条里帮你更快找到活性化合物’，因此它不是改良指标，而是在重写成功定义。"
status: complete
---

## Layer 1 — bold key sentences

- **当前 SBDD 社区流行的评估指标（尤其是 Vina docking score），在很大程度上是“可被模型轻易 hack 的理论指标”。**
- **把生成分子当成 虚拟筛选的“模板”。**
- **真正有用的生成分子，不一定要自己就是“好药”，但至少要能 帮助我们在真实化合物库里找到更多活性分子。**
- **CrossDocked 数据集本身存在明显问题。**

## Layer 2 — bold fragments

- **Vina低分不等于实用分子**
- **评估要围绕下游用途而不是理论分数**
- **生成分子更像筛库模板而非终产物**
- **训练基准的偏差会被模型放大**

## Layer 3 — one-sentence thesis

这篇工作的价值在于把SBDD评测从“模型能不能刷出更低的对接分”转成“这些分子是否能在真实筛选链条里帮你更快找到活性化合物”，因此它不是改良指标，而是在重写成功定义。

## Concepts (tier_1_atoms)

- `[[docking-score-hacking]]` — 文章明确指出 Vina 可以通过堆原子、改元素比例等方式被策略性利用。
- `[[practical-need-aligned-evaluation]]` — 真正的新意在于让评测指标回到药物发现的实际用途。
- `[[virtual-screening-template-utility]]` — 把生成分子视为筛库模板，是它最重要的评估视角。
- `[[benchmark-bias-in-sbdd]]` — CrossDocked 的偏差和泄漏问题会直接污染结论。

## Back-references

- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench]]` — MolGenBench是这篇逻辑的进一步展开：如果评估真按实战需求来重建，很多现有SBDD模型的表现会急剧缩水。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483994-1-biorxiv-2025-medsage-diffusion]]` — MedSAGE试图通过碎片级生成减小物理与评测错位，这正是对“刷分不落地”问题的一种方法回应。
- `[[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness]]` — Harness那篇提供了一个上位解释：评测指标本身就是系统控制层的一部分，如果它可被 hack，整个 agent 就会朝错误目标优化。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483720-1-iclr-2025-quot-vina-quot-quot-quot-sbdd.md`
- Type: markdown
- Kind: other
