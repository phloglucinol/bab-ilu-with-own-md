---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkznjizmtu0nw-2247547772-1-jcim
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkznjizmtu0nw-2247547772-1-jcim.md
bloom: analyze
concepts:
  - multimodal-dti-fusion
  - gated-multihead-attention-for-drug-target-pairs
  - split-aware-generalization-in-dti
layer_1_bolds:
  - 作者提出了一种端到端的框架DO-GMA。
  - DO-GMA在所有四种实验设置E1、E2、E3和E4下，AUC、AUPR等五个分类指标都优于六个基准方法。
  - DO-GMA框架中的各个模块都有助于提高DTI预测性能，其中多头注意力机制对性能的提升最为显著。
layer_2_fragments:
  - SMILES序列加分子图双通道
  - 蛋白序列与药物特征门控融合
  - 多头注意力是主要增益来源
  - 四种划分都得过关
layer_3_thesis: DO-GMA的价值不在于又把DTI分类分数推高一点，而在于它证明了药物表示必须同时看序列和图，再用显式融合机制把这两路信息接到蛋白上。
status: complete
---

# mp-weixin-qq-com-mzkznjizmtu0nw-2247547772-1-jcim

## Layer 1 — bold key sentences

- **作者提出了一种端到端的框架DO-GMA。**
- **DO-GMA在所有四种实验设置E1、E2、E3和E4下，AUC、AUPR等五个分类指标都优于六个基准方法。**
- **DO-GMA框架中的各个模块都有助于提高DTI预测性能，其中多头注意力机制对性能的提升最为显著。**

## Layer 2 — bold fragments

- **SMILES序列加分子图双通道**
- **蛋白序列与药物特征门控融合**
- **多头注意力是主要增益来源**
- **四种划分都得过关**

## Layer 3 — one-sentence thesis

DO-GMA的价值不在于又把DTI分类分数推高一点，而在于它证明了药物表示必须同时看序列和图，再用显式融合机制把这两路信息接到蛋白上。

## Concepts (tier_1_atoms)

- [[multimodal-dti-fusion]]：药物不能只靠SMILES或只靠图结构，双模态联合更稳。
- [[gated-multihead-attention-for-drug-target-pairs]]：用门控与多头注意力把药物和蛋白表示压到同一交互界面上。
- [[split-aware-generalization-in-dti]]：评估DTI模型时必须看药物未见、靶点未见、双未见三类泛化。

## Back-references

- [[mp-weixin-qq-com-mzkyntqznzkzoq-2247485660-1-jcim-tabpfn.md]]：TabPFN强调小数据表格任务可以依赖预训练先验，这篇则说明在DTI里，结构化先验的一部分来自多模态表示本身，而不只是学习器。
- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim]]：BALM押注序列基础和严格划分，这篇提醒我另一条路线仍然成立：即便不用大语言模型，只要融合设计和评估拆分做对，也能得到扎实泛化。
- [[mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025.md]]：那篇把干净切分当成结合亲和力建模的第一约束，这篇在DTI分类任务里给出平行证据，说明任何只在随机同分布上好看的结果都不够。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzkznjizmtu0nw-2247547772-1-jcim.md`
- Type: markdown
- Kind: other
