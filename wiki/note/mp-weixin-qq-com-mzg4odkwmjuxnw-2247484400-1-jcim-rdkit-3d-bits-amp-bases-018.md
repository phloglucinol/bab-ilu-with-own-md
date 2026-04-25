---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4odkwmjuxnw-2247484400-1-jcim-rdkit-3d-bits-amp-bases-018
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4odkwmjuxnw-2247484400-1-jcim-rdkit-3d-bits-amp-bases-018.md
bloom: analyze
concepts:
  - "[[probabilistic-bond-reconstruction]]"
  - "[[geometry-to-topology-inverse-problem]]"
  - "[[sanitization-as-bottleneck]]"
  - "[[distribution-aware-postprocessing]]"
layer_1_bolds:
  - "AIDD 生成模型的“最后一公里”往往受阻于 RDKit 的刚性规则。"
  - "本文提出 YuelBond，将化学键重建重构为噪声几何条件下的概率推断问题，从根本上解决了 3D 生成模型输出的 Sanitization 难题。"
  - "理论与应用 | 求解几何-拓扑映射的“病态逆问题”：YuelBond 的概率图视角。"
  - "将化学键重建重构为噪声几何条件下的概率推断问题。"
layer_2_fragments:
  - "从几何坐标反推键连接是病态逆问题"
  - "RDKit 规则化 sanitization 成为最后一公里瓶颈"
  - "以后验分布替代单一确定性键表"
  - "后处理必须认识噪声与不确定性"
  - "3D 生成与化学合法性不该靠硬阈值缝合"
layer_3_thesis: "YuelBond 的关键不是又一个键恢复工具，而是把“从 3D 坐标恢复化学拓扑”改写成概率推断问题，从而承认生成分子的输出天然带噪，不能再用 RDKit 式硬规则假装它是精确结构。"
---

# YuelBond 把 3D 生成分子的键重建从硬规则收口改成概率推断

## Layer 1 — bold key sentences

- **AIDD 生成模型的“最后一公里”往往受阻于 RDKit 的刚性规则。**
- **本文提出 YuelBond，将化学键重建重构为噪声几何条件下的概率推断问题，从根本上解决了 3D 生成模型输出的 Sanitization 难题。**
- **理论与应用 | 求解几何-拓扑映射的“病态逆问题”：YuelBond 的概率图视角。**
- **将化学键重建重构为噪声几何条件下的概率推断问题。**

## Layer 2 — bold fragments

- **从几何坐标反推键连接是病态逆问题**
- **RDKit 规则化 sanitization 成为最后一公里瓶颈**
- **以后验分布替代单一确定性键表**
- **后处理必须认识噪声与不确定性**
- **3D 生成与化学合法性不该靠硬阈值缝合**

## Layer 3 — one-sentence thesis

YuelBond 的关键不是又一个键恢复工具，而是把“从 3D 坐标恢复化学拓扑”改写成概率推断问题，从而承认生成分子的输出天然带噪，不能再用 RDKit 式硬规则假装它是精确结构。

## Concepts (tier_1_atoms)

- `[[probabilistic-bond-reconstruction]]` — 键重建不再是规则匹配，而是对多种可能键型进行后验判断。
- `[[geometry-to-topology-inverse-problem]]` — 这篇把 3D 生成里最常被忽略的一步单独拎出来，说明几何到拓扑并不是平凡映射。
- `[[sanitization-as-bottleneck]]` — 很多 3D 生成结果失败并非生成器本身无效，而是死在传统化学工具链的刚性收口。
- `[[distribution-aware-postprocessing]]` — 生成模型的后处理如果不显式建模噪声分布，就会把本来可修复的样本误杀掉。

## Back-references

- `[[mp-weixin-qq-com-mzg4odkwmjuxnw-2247487143-1-jcim-diff-shape-controlnet]]` — Diff-Shape 解决的是“如何在形状条件下生成候选几何”，这篇解决的是“如何把带噪几何恢复成可信键图”；它把前者从一个生成模型结果，改读成必须接上概率化收口器的半成品。
- `[[mp-weixin-qq-com-mzyzota3njkxmg-2247581783-1-jcim-yuelbond]]` — 另一篇 YuelBond 笔记若更偏方法细节，这篇则先固定住最值得迁移的抽象：真正的新意不是某组 benchmark，而是承认 sanitization 本身就是带不确定性的逆问题。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench]]` — MolGenBench 把命中发现失败更多归因于生成模型总体表现，这篇补出另一层解释：不少失败发生在后处理阶段，因为硬规则把本可修复的几何样本直接判成非法。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4odkwmjuxnw-2247484400-1-jcim-rdkit-3d-bits-amp-bases-018.md`
- Type: markdown
- Kind: other
