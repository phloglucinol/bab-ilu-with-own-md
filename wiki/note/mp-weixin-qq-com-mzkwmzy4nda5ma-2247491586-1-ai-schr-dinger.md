---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkwmzy4nda5ma-2247491586-1-ai-schr-dinger
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkwmzy4nda5ma-2247491586-1-ai-schr-dinger.md
bloom: analyze
concepts:
  - "[[explore-then-exploit-kinetics]]"
  - "[[automated-residence-time-prediction]]"
  - "[[ramd-imetad-workflow]]"
  - "[[path-quality-controls-accuracy]]"
layer_1_bolds:
  - "**首次将Random Acceleration Molecular Dynamics与Infrequent Metadynamics有机结合。**"
  - "**整个流程几乎无需手动调参。**"
  - "**先用RAMD快速探索配体可能的脱离路径，再用iMetaD沿主路径精确计算驻留时间。**"
  - "**预测从经验拟合推向物理自动化。**"
  - "**RAMD参数对路径质量具有关键影响。**"
layer_2_fragments:
  - "**先探索主路径 再沿主路径精算**"
  - "**驻留时间预测需要工作流自动化而非单次漂亮模拟**"
  - "**路径聚类是把随机轨迹变成可用 CV 的关键**"
  - "**默认参数并非跨体系普适**"
  - "**可信度可以从模拟成功率内部读出**"
layer_3_thesis: "这篇的真正突破不只是把驻留时间算得更准，而是把原本高度手工化的解离路径选择过程自动化成一个“先找主通道、再做物理精算”的稳定工作流。"
status: complete
---

# 驻留时间预测的难点在于先找到值得精算的解离通道

## Layer 1 — bold key sentences

- **首次将Random Acceleration Molecular Dynamics与Infrequent Metadynamics有机结合。**
- **整个流程几乎无需手动调参。**
- **先用RAMD快速探索配体可能的脱离路径，再用iMetaD沿主路径精确计算驻留时间。**
- **预测从经验拟合推向物理自动化。**
- **RAMD参数对路径质量具有关键影响。**

## Layer 2 — bold fragments

- **先探索主路径 再沿主路径精算**
- **驻留时间预测需要工作流自动化而非单次漂亮模拟**
- **路径聚类是把随机轨迹变成可用 CV 的关键**
- **默认参数并非跨体系普适**
- **可信度可以从模拟成功率内部读出**

## Layer 3 — one-sentence thesis

这篇的真正突破不只是把驻留时间算得更准，而是把原本高度手工化的解离路径选择过程自动化成一个“先找主通道、再做物理精算”的稳定工作流。

## Concepts (tier_1_atoms)

- `[[explore-then-exploit-kinetics]]`：这是整套方法最值得记的抽象。
- `[[automated-residence-time-prediction]]`：自动化在这里不是附加便利，而是方法能否扩展的前提。
- `[[ramd-imetad-workflow]]`：两阶段组合是方法的实体。
- `[[path-quality-controls-accuracy]]`：最终精度高度受前段路径质量制约。

## Back-references

- `[[mp-weixin-qq-com-mzk2ndc3ntk1mg-2247483806-1-jcim]]`：BD+MD 那篇处理进入路径，这篇处理离开路径，二者共同说明动力学计算的核心都是先把事件拆阶段，再决定哪一段用哪种物理。
- `[[mp-weixin-qq-com-mzkwmzy4nda5ma-2247491376-1-0-7-nm-ai-kai-11101]]`：KAI-11101 侧重 potency/选择性/暴露闭环，这篇补上了“续航力”这一维，说明真正完整的药效预测会逐渐把 residence time 也拉进设计循环。
- `[[mp-weixin-qq-com-mzk5mdg4nzixmw-2247484477-1-protdyn-ai]]`：如果 ProTDyn 想学统一动力学，未来这类 RAMD+iMetaD 工作流很可能成为它最需要先验建模的对象之一，因为它们明确揭示了关键路径和时间尺度结构。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzkwmzy4nda5ma-2247491586-1-ai-schr-dinger.md`
- Type: markdown
- Kind: other
