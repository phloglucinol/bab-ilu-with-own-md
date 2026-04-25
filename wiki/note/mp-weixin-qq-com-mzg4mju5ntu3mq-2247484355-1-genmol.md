---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mju5ntu3mq-2247484355-1-genmol
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mju5ntu3mq-2247484355-1-genmol.md
bloom: apply
concepts:
  - "[[input-canonicalization-before-generation]]"
  - "[[tokenization-induced-failure-modes]]"
  - "[[ring-closure-bias-in-scaffold-expansion]]"
  - "[[tool-behavior-is-often-not-a-bug]]"
layer_1_bolds:
  - "这些‘看似 bug’的地方，其实并不是程序错误，而是它在分子学习过程中采用了 SAFE molecular sequences 的机制。"
  - "如果使用 Kekulé（凯库勒式）SMILES，GenMol 可能无法正确解析。"
  - "当分子 scaffold 上的拓展位点太多时，GenMol 在生成过程中容易闭合成大环结构。"
  - "GenMol在分子生成时的核心逻辑并不是 bug，而是其分子学习策略导致的一些限制。"
layer_2_fragments:
  - "生成前先做输入规范化"
  - "token表示会塑造可生成空间"
  - "多扩展位点会诱发大环偏置"
  - "很多问题是模型假设泄漏到用户界面"
layer_3_thesis: "这篇短文最有用的地方在于它把‘工具不好用’重新翻译成‘表示与采样假设没有被显式暴露’，因此真正的修复通常不是调一个神秘参数，而是先把输入规范、拓展位点和成环倾向这些前置约束补齐。"
status: complete
---

## Layer 1 — bold key sentences

- **这些“看似 bug”的地方，其实并不是程序错误，而是它在分子学习过程中采用了 SAFE molecular sequences 的机制。**
- **如果使用 Kekulé（凯库勒式）SMILES，GenMol 可能无法正确解析。**
- **当分子 scaffold 上的拓展位点太多时，GenMol 在生成过程中容易闭合成大环结构。**
- **GenMol在分子生成时的核心逻辑并不是 bug，而是其分子学习策略导致的一些限制。**

## Layer 2 — bold fragments

- **生成前先做输入规范化**
- **token表示会塑造可生成空间**
- **多扩展位点会诱发大环偏置**
- **很多问题是模型假设泄漏到用户界面**

## Layer 3 — one-sentence thesis

这篇短文最有用的地方在于它把“工具不好用”重新翻译成“表示与采样假设没有被显式暴露”，因此真正的修复通常不是调一个神秘参数，而是先把输入规范、拓展位点和成环倾向这些前置约束补齐。

## Concepts (tier_1_atoms)

- `[[input-canonicalization-before-generation]]` — 芳香式标准化在这里不是清洁癖，而是生成能否开始的必要条件。
- `[[tokenization-induced-failure-modes]]` — SAFE 序列机制直接决定了哪些输入会被识别、哪些会静默失败。
- `[[ring-closure-bias-in-scaffold-expansion]]` — 多连接位点引发大环生成，是一种典型的采样偏置。
- `[[tool-behavior-is-often-not-a-bug]]` — 很多“bug”其实是模型假设没有向用户显式说明。

## Back-references

- `[[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness]]` — Harness那篇解释了为什么光有模型不够；这篇提供了一个非常具体的例子：没有输入校验和采样约束层，分子生成工具就会把内部假设直接扔给用户承担。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483994-1-biorxiv-2025-medsage-diffusion]]` — MedSAGE通过碎片库减少局部不合理结构，这篇则是在更低层次说明，连输入编码和 scaffold 扩展位点都需要被工具层约束。
- `[[mp-weixin-qq-com-mzg3ndc3nziynq-2247494762-1-jmc]]` — AutoOptimizer把优化规则显式化，这篇给我的启发是：真正可落地的生成平台，连输入表示和成环倾向也应该被规则化，而不能交给用户猜。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mju5ntu3mq-2247484355-1-genmol.md`
- Type: markdown
- Kind: other
