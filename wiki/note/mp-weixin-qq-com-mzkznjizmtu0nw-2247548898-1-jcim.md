---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim.md
bloom: analyze
concepts:
  - metric-learning-for-binding-affinity
  - peft-for-protein-ligand-language-models
  - strict-splits-beat-random-splits
layer_1_bolds:
  - 该研究提出 BALM（Binding Affinity via Language Model）。
  - BALM基于蛋白−配体嵌入距离直接建模pKd。
  - 提出以靶点、骨架、药物等维度进行划分的方法，更客观反映真实应用场景中的模型表现。
layer_2_fragments:
  - 亲和力映射为嵌入距离
  - ESM-2加ChemBERTa-2
  - PEFT降低微调成本
  - 先修评估再谈性能
layer_3_thesis: BALM真正值得记住的是它把亲和力预测从“黑盒回归一个数”改成了“在共享空间里拉近真实配对”，同时用严格切分把许多看似进步的结果重新打回了原形。
status: complete
---

# mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim

## Layer 1 — bold key sentences

- **该研究提出 BALM（Binding Affinity via Language Model）。**
- **BALM基于蛋白−配体嵌入距离直接建模pKd。**
- **提出以靶点、骨架、药物等维度进行划分的方法，更客观反映真实应用场景中的模型表现。**

## Layer 2 — bold fragments

- **亲和力映射为嵌入距离**
- **ESM-2加ChemBERTa-2**
- **PEFT降低微调成本**
- **先修评估再谈性能**

## Layer 3 — one-sentence thesis

BALM真正值得记住的是它把亲和力预测从“黑盒回归一个数”改成了“在共享空间里拉近真实配对”，同时用严格切分把许多看似进步的结果重新打回了原形。

## Concepts (tier_1_atoms)

- [[metric-learning-for-binding-affinity]]：用嵌入距离而不是直接回归来表示蛋白-配体亲和力。
- [[peft-for-protein-ligand-language-models]]：大语言模型进入药物任务后，PEFT是可扩展落地的关键。
- [[strict-splits-beat-random-splits]]：新靶点、新骨架、新药物切分比随机切分更接近真实筛选场景。

## Back-references

- [[mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025.md]]：这篇几乎是那篇“数据泄漏会夸大一切方法创新”的直接实例化，把论证从综述判断落到了具体模型设计上。
- [[mp-weixin-qq-com-mzkzmjc1njk0mq-2247485911-1-proaffinity-esm-foldx-g.md]]：ProAffinity++把语言表示和物理能项放到同一个界面图里，这篇则走另一侧，说明即便只靠序列表示，只要度量空间和评估协议设计得当，也能有强泛化。
- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247547772-1-jcim]]：DO-GMA靠多模态融合提升DTI识别，这篇提醒我在亲和力回归里更关键的未必是模态数，而是训练目标和数据划分是否贴近部署场景。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzkznjizmtu0nw-2247548898-1-jcim.md`
- Type: markdown
- Kind: other
