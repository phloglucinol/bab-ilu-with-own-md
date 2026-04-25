---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzuymdc1mda2oa-2247489378-1-nat-commun-head-amp-ted
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247489378-1-nat-commun-head-amp-ted.md
bloom: analyze
concepts:
  - energy-based-conformation-screening
  - multi-stage-molecule-filtering
  - atom-level-feedback-for-generative-models
  - molecular-generation-needs-post-generation-evaluation
layer_1_bolds:
  - "**近年来，自回归和扩散模型逐步具备了三维分子构象生成的能力，但普遍存在着生成异常构象的问题，如空间冲突、结构扭曲等，不论从指导模型改进还是生成分子的实际应用角度都需要对其进行有效评估。**"
  - "**面对这一现状，望石智慧团队发展了一套基于能量的分阶段评估框架：在力场优化前，通过高能原子检测器（HEAD）模型评估分子构象的有效性（validity），再利用基于深度学习的扭转能描述符（TED）评估力场优化后的构象合理性。**"
  - "**同时，HEAD的计算速度约为PoseBusters的30倍，更适合于高通量的筛选任务。**"
  - "**结果表明，TED-Model的预测结果与DFT结果表现出更强的一致性，其平均PCC = 0.84，明显高于GFN2-xTB的0.63。**"
  - "**如果汇总整个生成分子构象的筛选流程，在依次经过了类药性与可合成性、口袋冲突、构象有效性和构象合理性过滤的处理后，即使表现最好的Lingo3DMolv2和PocketFlow也只有约20%的分子构象得以保留。**"
layer_2_fragments:
  - "**先判原子级高能异常 再判扭转合理性**"
  - "**评估不该只看几何，也要看能量**"
  - "**高通量筛选需要便宜但有物理含义的过滤器**"
  - "**生成模型真正的瓶颈常出在后处理存活率**"
layer_3_thesis: "HEAD&TED 把“分子生成之后怎么筛”从粗糙几何检查改写成分阶段的能量审计流程，结果也因此暴露出当前生成模型的问题不只是会不会生成，而是大多数样本根本活不过物理过滤。"
status: complete
---
# 生成模型的分数再高，也得先活过物理过滤线

## Layer 1 — bold key sentences
- **近年来，自回归和扩散模型逐步具备了三维分子构象生成的能力，但普遍存在着生成异常构象的问题，如空间冲突、结构扭曲等，不论从指导模型改进还是生成分子的实际应用角度都需要对其进行有效评估。**
- **面对这一现状，望石智慧团队发展了一套基于能量的分阶段评估框架：在力场优化前，通过高能原子检测器（HEAD）模型评估分子构象的有效性（validity），再利用基于深度学习的扭转能描述符（TED）评估力场优化后的构象合理性。**
- **同时，HEAD的计算速度约为PoseBusters的30倍，更适合于高通量的筛选任务。**
- **结果表明，TED-Model的预测结果与DFT结果表现出更强的一致性，其平均PCC = 0.84，明显高于GFN2-xTB的0.63。**
- **如果汇总整个生成分子构象的筛选流程，在依次经过了类药性与可合成性、口袋冲突、构象有效性和构象合理性过滤的处理后，即使表现最好的Lingo3DMolv2和PocketFlow也只有约20%的分子构象得以保留。**

## Layer 2 — bold fragments
- **先判原子级高能异常 再判扭转合理性**
- **评估不该只看几何，也要看能量**
- **高通量筛选需要便宜但有物理含义的过滤器**
- **生成模型真正的瓶颈常出在后处理存活率**

## Layer 3 — one-sentence thesis
HEAD&TED 把“分子生成之后怎么筛”从粗糙几何检查改写成分阶段的能量审计流程，结果也因此暴露出当前生成模型的问题不只是会不会生成，而是大多数样本根本活不过物理过滤。

## Concepts (tier_1_atoms)
- `[[energy-based-conformation-screening]]`：这篇把构象质量判断从几何规则推进到能量分解层面，和只看形状是否合法不是一回事。
- `[[multi-stage-molecule-filtering]]`：类药性、口袋冲突、原子高能和扭转能应分层过滤，而不是混成单一总分。
- `[[atom-level-feedback-for-generative-models]]`：HEAD/TED 的价值不止于筛掉坏样本，还在于能把错误定位到原子和可旋转键。
- `[[molecular-generation-needs-post-generation-evaluation]]`：生成阶段的 benchmark 分数无法替代后生成的系统性审计。

## Back-references
- `[[mp-weixin-qq-com-mzu5otu3nzyyoq-2247492172-1-jcim-chemprop-v2]]`：Chemprop v2 那篇会让我把这篇读成“评估基础设施也要像基础设施”而不只是单篇方法，因为 HEAD&TED 真正可复用的地方在于它是一条可插入工作流的评价流水线。
- `[[mp-weixin-qq-com-mzy5nzezmjkzmq-2247484559-2-jctc]]`：PROTEUS 把量子化学直接拉进生成闭环，这篇则提醒我即使生成器已经闭环，后端仍需要独立的物理审计器，否则优化目标会和实际可存活构象脱节。
- `[[mp-weixin-qq-com-mzuymdc1mda2oa-2247488931-1-hacettepe-do-an-nmi-transformer]]`：DrugGEN 更强调“生成能命中靶点的分子”，回看这篇会意识到命中不是终点，因为如果构象本身大面积失真，任何下游对接或活性判断都可能建立在不可信几何上。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247489378-1-nat-commun-head-amp-ted.md`
- Type: markdown
- Kind: other
