---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench.md
bloom: analyze
concepts:
  - benchmarking-for-practical-hit-discovery
  - de-novo-hit-rate-collapse
  - hit-to-lead-over-de-novo
  - crossdock-is-good-for-papers-not-products
layer_1_bolds:
  - "当分子生成模型终于走上‘实战考场’。"
  - "完全从头的 de novo 生成 → 活性 hit 极少、验证成本极高。"
  - "挂在 fragment/series 上的 H2L 优化 → 模型性能明显改善，结果更可用。"
  - "CrossDock2020 很适合做论文创新，但未必能训练出真正能落地的 SBMG 模型。"
layer_2_fragments:
  - "真正实战评测会让命中率塌缩"
  - "系列内优化比完全从头生成更现实"
  - "高质量晶体和真实活性库比对接宇宙更重要"
  - "benchmark要奖励可用性而不是刷分"
layer_3_thesis: "MolGenBench最有杀伤力的地方不是给出一组更难数字，而是把行业里默认回避的事实量化了：当前许多3D生成模型在完全从头的真实命中任务上几乎不可用，而它们真正有希望发挥价值的场景，其实是挂在fragment和series上的受限优化。"
status: complete
---

# mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench

## Layer 1 — bold key sentences

- **当分子生成模型终于走上“实战考场”。**
- **完全从头的 de novo 生成 → 活性 hit 极少、验证成本极高。**
- **挂在 fragment/series 上的 H2L 优化 → 模型性能明显改善，结果更可用。**
- **CrossDock2020 很适合做论文创新，但未必能训练出真正能落地的 SBMG 模型。**

## Layer 2 — bold fragments

- **真正实战评测会让命中率塌缩**
- **系列内优化比完全从头生成更现实**
- **高质量晶体和真实活性库比对接宇宙更重要**
- **benchmark要奖励可用性而不是刷分**

## Layer 3 — one-sentence thesis

MolGenBench最有杀伤力的地方不是给出一组更难数字，而是把行业里默认回避的事实量化了：当前许多3D生成模型在完全从头的真实命中任务上几乎不可用，而它们真正有希望发挥价值的场景，其实是挂在fragment和series上的受限优化。

## Concepts (tier_1_atoms)

- [[benchmarking-for-practical-hit-discovery]]：这套基准最重要的是它把评测对象改成真实命中发现能力。
- [[de-novo-hit-rate-collapse]]：从头生成的 hit rate 崩塌是全文最值得记住的现实结论。
- [[hit-to-lead-over-de-novo]]：H2L 场景明显更适合当前模型，是一个策略性判断。
- [[crossdock-is-good-for-papers-not-products]]：对 CrossDock 的批评足够尖锐，值得作为单独概念记住。

## Back-references

- [[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483720-1-iclr-2025-quot-vina-quot-quot-quot-sbdd]]：ICLR那篇重写了评估目标，这篇则把这种重写落成了一个更系统、更“企业现场感”的 benchmark。
- [[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483994-1-biorxiv-2025-medsage-diffusion]]：MedSAGE试图通过碎片化设计贴近H2L现实，而这篇正好说明这种路线为什么比完全自由的de novo更有机会落地。
- [[mp-weixin-qq-com-mzg3ndc3nziynq-2247494762-1-jmc]]：AutoOptimizer做的正是以已有hit或先导为起点的多轮优化，这和MolGenBench得出的“H2L优于de novo”结论高度同向。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench.md`
- Type: markdown
- Kind: other
