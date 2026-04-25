---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk0mzyxntu0oa-2247486617-1-re-mmpbsa-pmf
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk0mzyxntu0oa-2247486617-1-re-mmpbsa-pmf.md
bloom: analyze
concepts:
  - sampling-window-beats-longer-md
  - hydrophobic-pocket-narrows-energy-landscape
  - replica-exchange-mmpbsa-for-antibody-ranking
layer_1_bolds:
  - 采样时间越长并不必然提升预测力，20-50 ns窗口反而比20-100 ns更能复现实验趋势。
  - 经验性截断配合密集抽帧才是让RE-MMPBSA保持预测力的关键。
  - 10×5 ns多副本MMPBSA仍是兼顾速度与准确性的方案。
layer_2_fragments:
  - 更长采样不一定更接近实验
  - 疏水口袋把熵差压窄
  - 温度交换平衡段必须剔除
  - 多副本短轨迹比单条长轨迹更划算
layer_3_thesis: 这篇真正改写的是采样直觉：在疏水主导且能量景观狭窄的体系里，决定排序质量的不是总时长，而是是否截住了仍保留实验判别力的那段轨迹。
status: complete
---

# mp-weixin-qq-com-mzk0mzyxntu0oa-2247486617-1-re-mmpbsa-pmf

## Layer 1 — bold key sentences

- **采样时间越长并不必然提升预测力，20-50 ns窗口反而比20-100 ns更能复现实验趋势。**
- **经验性截断配合密集抽帧才是让RE-MMPBSA保持预测力的关键。**
- **10×5 ns多副本MMPBSA仍是兼顾速度与准确性的方案。**

## Layer 2 — bold fragments

- **更长采样不一定更接近实验**
- **疏水口袋把熵差压窄**
- **温度交换平衡段必须剔除**
- **多副本短轨迹比单条长轨迹更划算**

## Layer 3 — one-sentence thesis

这篇真正改写的是采样直觉：在疏水主导且能量景观狭窄的体系里，决定排序质量的不是总时长，而是是否截住了仍保留实验判别力的那段轨迹。

## Concepts (tier_1_atoms)

- [[sampling-window-beats-longer-md]]：采样窗口的选择可以比总模拟时长更决定预测有效性。
- [[hydrophobic-pocket-narrows-energy-landscape]]：界面若被疏水口袋强约束，温度与长程采样带来的构象增益会迅速边际递减。
- [[replica-exchange-mmpbsa-for-antibody-ranking]]：RE-MMPBSA适合做抗体变体相对排序，但前提是把平衡段和漂移段分开看。

## Back-references

- [[mp-weixin-qq-com-mzkzmjc1njk0mq-2247486288-1-cpacs-md]]：cPaCS-MD强调“别把复杂解离压成一维距离”，这篇则补上另一层判断：即便采样维度对了，时间窗口照样会把排序做坏。
- [[mp-weixin-qq-com-mzkzmjc1njk0mq-2247486863-1]]：DBFE通过复用末态信息降低自由能成本；这篇说明在抗体筛选里，另一条降本路线是承认短程多副本已经足够，不必盲目追求长轨迹。
- [[mp-weixin-qq-com-mzkzmzkxnjq4nw-2247494089-1-nat-comput-sci-if-18-3]]：qGNN试图从数据里学反应坐标，这篇则提醒即便不用手工坐标，采样是否落在“有效判别区间”仍是独立问题。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzk0mzyxntu0oa-2247486617-1-re-mmpbsa-pmf.md`
- Type: markdown
- Kind: other
