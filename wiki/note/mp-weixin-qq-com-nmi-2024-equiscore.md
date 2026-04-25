---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-nmi-2024-equiscore
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-nmi-2024-equiscore.md
bloom: analyze
concepts:
  - data-augmentation-for-scoring-generalization
  - physical-priors-in-rescoring
  - deduplication-is-part-of-model-design
  - rescoring-can-be-a-generic-boost-layer
layer_1_bolds:
  - "本文提出名为 EquiScore 的评分方法，该方法利用异质图神经网络整合物理先验知识，并在等变几何空间中表征蛋白质-配体相互作用。"
  - "研究通过三种数据增强方式构建新数据集 PDBscreen。"
  - "训练前按 UniProt ID 去重。"
  - "所有对接方法经 EquiScore 重打分后，EF、BEDROC、AUROC 均显著提升。"
layer_2_fragments:
  - "泛化差往往先是数据集问题"
  - "去冗余不是评测礼仪，而是模型设计的一部分"
  - "物理先验要进图结构，不只进损失函数"
  - "重打分层可以复用已有 docking 管线"
  - "高迷惑性阴性样本比普通 decoy 更值钱"
layer_3_thesis: "EquiScore 说明高质量评分模型的核心不只是网络结构，而是把物理先验、困难负样本和严格去重一起做成训练分布。"
status: complete
---

# mp-weixin-qq-com-nmi-2024-equiscore

## Layer 1

- **本文提出名为 EquiScore 的评分方法，该方法利用异质图神经网络整合物理先验知识，并在等变几何空间中表征蛋白质-配体相互作用。**
- **研究通过三种数据增强方式构建新数据集 PDBscreen。**
- **训练前按 UniProt ID 去重。**
- **所有对接方法经 EquiScore 重打分后，EF、BEDROC、AUROC 均显著提升。**

## Layer 2

- **泛化差往往先是数据集问题**
- **去冗余不是评测礼仪，而是模型设计的一部分**
- **物理先验要进图结构，不只进损失函数**
- **重打分层可以复用已有 docking 管线**
- **高迷惑性阴性样本比普通 decoy 更值钱**

## Layer 3

EquiScore 说明高质量评分模型的核心不只是网络结构，而是把物理先验、困难负样本和严格去重一起做成训练分布。

## Concepts

- [[data-augmentation-for-scoring-generalization]]：重要，因为它把泛化提升的重点从“更大模型”移到了“更像真实部署的数据”。
- [[physical-priors-in-rescoring]]：重要，因为重打分若不引入相互作用先验，容易退化成配体或蛋白身份记忆器。
- [[deduplication-is-part-of-model-design]]：重要，因为药物发现里数据泄漏会直接制造虚假进展。
- [[rescoring-can-be-a-generic-boost-layer]]：重要，因为它意味着不用重建全流程，也能提升现有 docking 体系。

## Back-references

- [[mp-weixin-qq-com-mzyzodi1otazna-2247486769-1-18-7-pbcnet2-0-ai]]：PBCNet2.0 关注系列分子相对亲和力，这篇更偏 hit finding 与 pose rescoring；两者一起能区分不同阶段该用什么模型。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe]]：OpenFE 追求的是协议级可重复物理计算，这篇追求的是更泛化的学习型打分，会让我更清楚两类工具的边界。
- [[mp-weixin-qq-com-mzyzota3njkxmg-2247583405-1-biorxiv-visnet-pima]]：ViSNet-PIMA 提醒物理先验应进到底层能量建模，这篇则展示了即使在评分层，物理先验同样能显著改变泛化。 

## Source
- Input: `raw/articles/mp-weixin-qq-com-nmi-2024-equiscore.md`
- Type: markdown
- Kind: other
