---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mju5ntu3mq-2247485034-1
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mju5ntu3mq-2247485034-1.md
bloom: apply
concepts:
  - "[[security-tiering-for-computational-chemistry]]"
  - "[[convenience-security-tradeoff]]"
  - "[[public-network-is-not-neutral]]"
  - "[[infrastructure-choice-shapes-research-risk]]"
layer_1_bolds:
  - "第一等：物理隔离。"
  - "第二等：知名云厂商。"
  - "第三等：公网局域网混用环境。"
  - "第四等：私接跳板机。"
layer_2_fragments:
  - "安全性与便捷性必须一起评估"
  - "网络架构本身就是科研风险模型"
  - "不是所有‘能连上’的方案都该用"
  - "计算化学也需要分级安全观"
layer_3_thesis: "这篇清单的真正价值不在于告诉你哪种环境最安全，而在于迫使你承认基础设施选择本身就是研究方法的一部分，因为你把数据、模型和算力放在哪种网络边界里，直接决定了项目暴露面。"
status: complete
---

## Layer 1 — bold key sentences

- **第一等：物理隔离。**
- **第二等：知名云厂商。**
- **第三等：公网局域网混用环境。**
- **第四等：私接跳板机。**

## Layer 2 — bold fragments

- **安全性与便捷性必须一起评估**
- **网络架构本身就是科研风险模型**
- **不是所有“能连上”的方案都该用**
- **计算化学也需要分级安全观**

## Layer 3 — one-sentence thesis

这篇清单的真正价值不在于告诉你哪种环境最安全，而在于迫使你承认基础设施选择本身就是研究方法的一部分，因为你把数据、模型和算力放在哪种网络边界里，直接决定了项目暴露面。

## Concepts (tier_1_atoms)

- `[[security-tiering-for-computational-chemistry]]` — 它提供了一个很实用的四级分层视角，方便快速判断环境风险。
- `[[convenience-security-tradeoff]]` — 文章的结构本身就在说明安全与便捷是同一张表上的两列。
- `[[public-network-is-not-neutral]]` — 混用公网和局域网不是中性选择，而是默认扩大攻击面。
- `[[infrastructure-choice-shapes-research-risk]]` — 基础设施不是后勤问题，它会决定项目的风险轮廓。

## Back-references

- `[[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness]]` — Harness那篇谈的是让模型不失控，这篇谈的是让基础设施不失控；两者都在说明“外部系统”决定工具是否可用。
- `[[mp-weixin-qq-com-mzg4mju5ntu3mq-2247484355-1-genmol]]` — GenMol那篇从工具层暴露了输入与采样假设，这篇把同样的思路推到部署层：真正的稳定性不只在模型里，也在运行环境里。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247484032-2-jcim-2025-amp-openadmet-adme]]` — 如果ADME模型要用内部数据微调，这篇就是前提：你得先想清楚这些数据应该待在哪种安全边界里。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mju5ntu3mq-2247485034-1.md`
- Type: markdown
- Kind: other
