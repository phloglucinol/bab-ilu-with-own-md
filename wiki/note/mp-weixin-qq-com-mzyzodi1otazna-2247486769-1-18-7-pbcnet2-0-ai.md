---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzyzodi1otazna-2247486769-1-18-7-pbcnet2-0-ai
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzyzodi1otazna-2247486769-1-18-7-pbcnet2-0-ai.md
bloom: analyze
concepts:
  - relative-affinity-models-scale-lead-optimization
  - siamese-ddg-prediction
  - scaling-laws-for-structure-scoring
  - zero-shot-mutation-sensitivity
layer_1_bolds:
  - "PBCNet2.0 采用孪生神经网络架构，专门针对“相对结合亲和力”设计。"
  - "PBCNet2.0 遵循“缩放法则”，将其训练数据集扩展到了惊人的 860 万个蛋白质-配体对。"
  - "在标准的 FEP 测试集上，其预测精度较一代提升了 18%，相关性系数ρ 达到 0.67。"
  - "即便在训练阶段并未专门针对蛋白质突变数据进行强化，PBCNet2.0 依然能够准确预测因口袋残基突变导致的药物活性丧失。"
layer_2_fragments:
  - "先导优化更关心 ΔΔG，不是绝对值"
  - "数据规模扩张带来零样本泛化"
  - "等变几何约束让模型不再只背 ligand 偏见"
  - "突变敏感性是意外涌现能力"
  - "它在 FEP 与早期 AI 之间占了一个实用中间层"
layer_3_thesis: "PBCNet2.0 的位置很明确：它不是替代物理模拟的真值机，而是用大规模几何学习把相对亲和力排序推到足够接近 FEP、足够便宜到能进入日常优化循环。"
status: complete
---

# mp-weixin-qq-com-mzyzodi1otazna-2247486769-1-18-7-pbcnet2-0-ai

## Layer 1

- **PBCNet2.0 采用孪生神经网络架构，专门针对“相对结合亲和力”设计。**
- **PBCNet2.0 遵循“缩放法则”，将其训练数据集扩展到了惊人的 860 万个蛋白质-配体对。**
- **在标准的 FEP 测试集上，其预测精度较一代提升了 18%，相关性系数ρ 达到 0.67。**
- **即便在训练阶段并未专门针对蛋白质突变数据进行强化，PBCNet2.0 依然能够准确预测因口袋残基突变导致的药物活性丧失。**

## Layer 2

- **先导优化更关心 ΔΔG，不是绝对值**
- **数据规模扩张带来零样本泛化**
- **等变几何约束让模型不再只背 ligand 偏见**
- **突变敏感性是意外涌现能力**
- **它在 FEP 与早期 AI 之间占了一个实用中间层**

## Layer 3

PBCNet2.0 的位置很明确：它不是替代物理模拟的真值机，而是用大规模几何学习把相对亲和力排序推到足够接近 FEP、足够便宜到能进入日常优化循环。

## Concepts

- [[relative-affinity-models-scale-lead-optimization]]：重要，因为 lead optimization 本质上是系列分子排序，不是单分子打分。
- [[siamese-ddg-prediction]]：重要，因为孪生结构正对应药化里“差之毫厘”的比较任务。
- [[scaling-laws-for-structure-scoring]]：重要，因为这篇证明打分模型也吃数据规模红利，不只是生成模型。
- [[zero-shot-mutation-sensitivity]]：重要，因为它提示模型学到的可能不止配体模式，还包含口袋几何对扰动的响应。

## Back-references

- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe]]：OpenFE 代表另一条路线，即靠默认协议和统计收敛做工业化；回看这篇，会更清楚 PBCNet2.0 走的是近似器路线。
- [[mp-weixin-qq-com-nmi-2024-equiscore]]：EquiScore 主要做筛选和重打分，而这篇更贴近系列优化；两篇合起来刚好对应 hit finding 和 lead optimization 的不同节奏。
- [[mp-weixin-qq-com-mzyymjazmzc3ng-2247484062-1]]：那篇提醒“好设计”不止活性，所以这篇再强，也只是多目标优化中的一个高频子模块。 

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzyzodi1otazna-2247486769-1-18-7-pbcnet2-0-ai.md`
- Type: markdown
- Kind: other
