---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkwmji4odg2na-2247484368-1-jcim-admet
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkwmji4odg2na-2247484368-1-jcim-admet.md
bloom: analyze
concepts:
  - "[[noisy-label-denoising]]"
  - "[[pretrain-finetune-denoise]]"
  - "[[task-local-noise]]"
  - "[[test-set-cleanliness]]"
layer_1_bolds:
  - "**巧用预训练-微调框架挽救含噪ADMET数据。**"
  - "**真实噪声的复杂性未被充分模拟。**"
  - "**多任务模型主要是为了提升整体精度，而非获得额外的抗噪能力。**"
  - "**可以放心地在多任务模型中针对特定脏任务进行清洗，而不用担心破坏其他任务的特征学习。**"
  - "**干净测试集的构建方式是否可靠。**"
layer_2_fragments:
  - "**回归标签噪声首先是测量问题不是建模问题**"
  - "**预训练提供先验 微调承担去噪适配**"
  - "**多任务共享不等于噪声互相传染**"
  - "**评估去噪方法先要问测试集干不干净**"
  - "**高斯噪声基准往往低估真实实验偏差的复杂性**"
layer_3_thesis: "这篇最重要的启发不是某个去噪技巧更优，而是 ADMET 建模的真正上游问题是标签可信度分层管理，否则所有模型比较都可能在脏基准上循环自证。"
status: complete
---

# 含噪 ADMET 建模的上游问题是先区分哪些标签值得相信

## Layer 1 — bold key sentences

- **巧用预训练-微调框架挽救含噪ADMET数据。**
- **真实噪声的复杂性未被充分模拟。**
- **多任务模型主要是为了提升整体精度，而非获得额外的抗噪能力。**
- **可以放心地在多任务模型中针对特定脏任务进行清洗，而不用担心破坏其他任务的特征学习。**
- **干净测试集的构建方式是否可靠。**

## Layer 2 — bold fragments

- **回归标签噪声首先是测量问题不是建模问题**
- **预训练提供先验 微调承担去噪适配**
- **多任务共享不等于噪声互相传染**
- **评估去噪方法先要问测试集干不干净**
- **高斯噪声基准往往低估真实实验偏差的复杂性**

## Layer 3 — one-sentence thesis

这篇最重要的启发不是某个去噪技巧更优，而是 ADMET 建模的真正上游问题是标签可信度分层管理，否则所有模型比较都可能在脏基准上循环自证。

## Concepts (tier_1_atoms)

- `[[noisy-label-denoising]]`：这是全文主轴，但重点在“噪声来自哪里”。
- `[[pretrain-finetune-denoise]]`：预训练-微调在这里扮演的是去噪工作流，而不是一般迁移学习。
- `[[task-local-noise]]`：多任务场景下，噪声更多是局部污染而不是全局扩散。
- `[[test-set-cleanliness]]`：若测试集本身不干净，去噪改进就很难解释。

## Back-references

- `[[mp-weixin-qq-com-mzk0mzyxntu0oa-2247487738-1-qhts-qsar-herg-gpcr]]`：hERG 那篇把实验 qHTS 与 QSAR 绑在一起，这篇解释了为什么这种混合策略必要，因为纯模型若不先处理标签质量，外推会很脆弱。
- `[[mp-weixin-qq-com-mzk5mdg4nzixmw-2247490028-3-ai-llm-10]]`：那篇说老代码需要工程清洁，这篇是数据版的同一句话：基础设施不干净，后面的模型和代理都只是在脏地板上起舞。
- `[[mp-weixin-qq-com-mzk3ntq2nji1mg-2247485379-1-jmc-2025-7-3d.md]]`：3D 生成评测那篇关心 benchmark 指标是否真反映药化质量；这篇把同一怀疑指向训练与测试数据本身，说明“基准可信度”比模型排名更先验。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzkwmji4odg2na-2247484368-1-jcim-admet.md`
- Type: markdown
- Kind: other
