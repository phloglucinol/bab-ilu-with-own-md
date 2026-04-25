---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mta4ntc4mw-2247484032-2-jcim-2025-amp-openadmet-adme
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247484032-2-jcim-2025-amp-openadmet-adme.md
bloom: analyze
concepts:
  - cluster-split-over-random-split
  - small-data-adme-pragmatism
  - uncertainty-is-a-feature
  - multitask-learning-for-adme
layer_1_bolds:
  - "Cluster Split（按骨架聚类切分）：模型 R² 直接掉到了 0.1。"
  - "在 ADME 这种数据稀缺领域，‘借力打力’（Transfer Learning）是必选项。"
  - "最好的模型不是 R² 最高的那个，而是最诚实地告诉你‘我不知道’的那个。"
  - "TabPFN 和预训练 GNN 是表现最稳健的选手。"
layer_2_fragments:
  - "随机切分会夸大ADME可用性"
  - "小样本下先要稳健基线而不是大模型幻觉"
  - "不确定性输出应该进入决策看板"
  - "多任务学习是在数据稀缺下借邻近任务续命"
layer_3_thesis: "这篇文章真正把ADME建模从‘选一个更强模型’拉回到工程现实：当数据少、分布偏、骨架外推困难时，最有价值的不是炫耀随机切分上的高R²，而是建立一个会在陌生化学空间里主动暴露不确定性的稳健系统。"
status: complete
---

# mp-weixin-qq-com-mzg4mta4ntc4mw-2247484032-2-jcim-2025-amp-openadmet-adme

## Layer 1 — bold key sentences

- **Cluster Split（按骨架聚类切分）：模型 R² 直接掉到了 0.1。**
- **在 ADME 这种数据稀缺领域，‘借力打力’（Transfer Learning）是必选项。**
- **最好的模型不是 R² 最高的那个，而是最诚实地告诉你‘我不知道’的那个。**
- **TabPFN 和预训练 GNN 是表现最稳健的选手。**

## Layer 2 — bold fragments

- **随机切分会夸大ADME可用性**
- **小样本下先要稳健基线而不是大模型幻觉**
- **不确定性输出应该进入决策看板**
- **多任务学习是在数据稀缺下借邻近任务续命**

## Layer 3 — one-sentence thesis

这篇文章真正把ADME建模从“选一个更强模型”拉回到工程现实：当数据少、分布偏、骨架外推困难时，最有价值的不是炫耀随机切分上的高R²，而是建立一个会在陌生化学空间里主动暴露不确定性的稳健系统。

## Concepts (tier_1_atoms)

- `[[cluster-split-over-random-split]]` — 这是全文最具杀伤力的经验：切分协议本身会决定你是在测记忆还是泛化。
- `[[small-data-adme-pragmatism]]` — 小样本 ADME 场景更需要稳健、可复现的工程策略而不是参数更大的模型。
- `[[uncertainty-is-a-feature]]` — 不确定性输出在这里不是附属品，而是系统可信度核心。
- `[[multitask-learning-for-adme]]` — 多任务学习被证明是数据稀缺下最现实的增益路径之一。

## Back-references

- `[[mp-weixin-qq-com-mzg3otc1nduxoq-2247484629-1-cell-reports-method.md]]` — DTI综述已经说明数据划分和冷启动定义任务，这篇把同样的逻辑在ADME里用真实盲测和开源基准再验证了一遍。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench]]` — MolGenBench要求生成模型在更接近实战的设置里被评估；这篇告诉我性质模型也一样，不能再靠宽松 split 自嗨。
- `[[mp-weixin-qq-com-mze5odeymta0nq-2247484040-1-nuak1-pk]]` — NUAK1那篇的中枢/外周分流说明ADME与PK会改变项目方向，因此这里关于不确定性和小样本微调的建议并不是方法学洁癖，而是实战需要。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247484032-2-jcim-2025-amp-openadmet-adme.md`
- Type: markdown
- Kind: other
