---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkzmjc1njk0mq-2247486288-1-cpacs-md
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkzmjc1njk0mq-2247486288-1-cpacs-md.md
bloom: analyze
concepts:
  - adaptive-dissociation-path
  - contact-metric-over-distance
  - peptide-binding-free-energy
  - msm-aware-sampling
layer_1_bolds:
  - cPaCS-MD 对实验 ΔG° 的预测与实验值相关性强。
  - US 在本数据集上未显示出与实验值的关联，且误差远大于 cPaCS-MD。
  - cPaCS-MD 通过 contact-metric 与 tICA/MSM 能更好地捕获构象异质性与弱结合中间态。
  - 肽-蛋白自由能难点不只是采样量，而是采样路径是否尊重真实解离过程。
layer_2_fragments:
  - 反应坐标不能只看 COM 距离
  - 中间态需要被显式看见
  - adaptive sampling 比固定窗更自然
  - MSM 让路径统计可解释
layer_3_thesis: cPaCS-MD 提醒我，肽-蛋白自由能问题里最危险的假设是把复杂解离过程压成一维距离坐标，因为真正重要的往往是接触模式和中间态拓扑。
status: complete
---

# 肽结合自由能常输在反应坐标选错，而不是算力不够

## Layer 1 — bold key sentences

- **cPaCS-MD 对实验 ΔG° 的预测与实验值相关性强。**
- **US 在本数据集上未显示出与实验值的关联，且误差远大于 cPaCS-MD。**
- **cPaCS-MD 通过 contact-metric 与 tICA/MSM 能更好地捕获构象异质性与弱结合中间态。**
- **肽-蛋白自由能难点不只是采样量，而是采样路径是否尊重真实解离过程。**

## Layer 2 — bold fragments

- **反应坐标不能只看 COM 距离**
- **中间态需要被显式看见**
- **adaptive sampling 比固定窗更自然**
- **MSM 让路径统计可解释**

## Layer 3 — one-sentence thesis

cPaCS-MD 提醒我，肽-蛋白自由能问题里最危险的假设是把复杂解离过程压成一维距离坐标，因为真正重要的往往是接触模式和中间态拓扑。

## Concepts (tier_1_atoms)

- [[adaptive-dissociation-path]]：让轨迹自己展开解离通道，而不是人为钉死路径。
- [[contact-metric-over-distance]]：接触模式往往比质心距离更能描述真实反应坐标。
- [[peptide-binding-free-energy]]：肽体系的自由能难点来自更高构象异质性。
- [[msm-aware-sampling]]：采样和后验状态建模应一起设计。

## Back-references

- [[mp-weixin-qq-com-mzkzmjc1njk0mq-2247486863-1]]：DBFE 也想绕开传统炼金路径，这篇从采样路径角度给出另一种高效路线。
- [[mp-weixin-qq-com-mzkzmzkxnjq4nw-2247494089-1-nat-comput-sci-if-18-3]]：那篇强调反应坐标要从数据里学，这篇在自由能计算里展示了反应坐标选错的直接代价。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzkzmjc1njk0mq-2247486288-1-cpacs-md.md`
- Type: markdown
- Kind: other
