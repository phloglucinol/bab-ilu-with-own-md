---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4odkwmjuxnw-2247487143-1-jcim-diff-shape-controlnet
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4odkwmjuxnw-2247487143-1-jcim-diff-shape-controlnet.md
bloom: analyze
concepts:
  - "[[shape-conditioned-diffusion]]"
  - "[[controlnet-for-molecular-generation]]"
  - "[[soft-geometric-control]]"
  - "[[shape-scaffold-decoupling]]"
layer_1_bolds:
  - "Diff-Shape：把 ControlNet 搬进分子生成，形状约束与骨架创新如何兼得。"
  - "De Novo Molecular Design via Shape-Constrained Diffusion Models"
  - "研究方向：AI 辅助药物设计、3D 分子生成、形状约束生成模型。"
  - "把 ControlNet 搬进分子生成，形状约束与骨架创新如何兼得。"
layer_2_fragments:
  - "把形状条件作为扩散侧通道输入"
  - "几何控制不等于模板复制"
  - "保留药效形状同时放开骨架多样性"
  - "借用 ControlNet 思路做软约束生成"
  - "生成任务从自由采样转向受控探索"
layer_3_thesis: "Diff-Shape 真正证明的是形状约束不必等于 scaffold 锁死，只要控制信号被设计成扩散过程里的软条件，模型就能在保持药效几何的同时继续做结构创新。"
---

# Diff-Shape 证明形状约束可以作为软控制而不是骨架枷锁

## Layer 1 — bold key sentences

- **Diff-Shape：把 ControlNet 搬进分子生成，形状约束与骨架创新如何兼得。**
- **De Novo Molecular Design via Shape-Constrained Diffusion Models**
- **研究方向：AI 辅助药物设计、3D 分子生成、形状约束生成模型。**
- **把 ControlNet 搬进分子生成，形状约束与骨架创新如何兼得。**

## Layer 2 — bold fragments

- **把形状条件作为扩散侧通道输入**
- **几何控制不等于模板复制**
- **保留药效形状同时放开骨架多样性**
- **借用 ControlNet 思路做软约束生成**
- **生成任务从自由采样转向受控探索**

## Layer 3 — one-sentence thesis

Diff-Shape 真正证明的是形状约束不必等于 scaffold 锁死，只要控制信号被设计成扩散过程里的软条件，模型就能在保持药效几何的同时继续做结构创新。

## Concepts (tier_1_atoms)

- `[[shape-conditioned-diffusion]]` — 这里的条件不是标签或属性，而是 3D 形状本身进入采样过程。
- `[[controlnet-for-molecular-generation]]` — 借 ControlNet 的价值不在“跨模态套壳”，而在于给扩散模型增加一条不完全支配主干的控制旁路。
- `[[soft-geometric-control]]` — 文章最有用的抽象是“软约束”，它避免了模板法常见的化学空间坍缩。
- `[[shape-scaffold-decoupling]]` — 形状与骨架可以部分解耦，这一点对 hit-to-lead 的可控多样化非常关键。

## Back-references

- `[[mp-weixin-qq-com-mzg3otc3ndc0ma-2247487286-1-j-cheminf-poligenx-ai]]` — PoLiGenX 用参考配体维持设计意图，这篇则用全局形状条件维持空间意图；两篇并读后，“保留设计意图”会被拆成参考实例控制和几何场控制两条不同路线。
- `[[mp-weixin-qq-com-mze5odgwota0nq-2247484064-1-nat-comput-sci-phoregen]]` — PhoreGen 从药效团模式施加局部功能约束，这篇从整体 3D 形状施加全局几何约束；它帮助我把“受控生成”进一步区分成局部功能对齐和整体空间对齐两种粒度。
- `[[mp-weixin-qq-com-mzg4odkwmjuxnw-2247484400-1-jcim-rdkit-3d-bits-amp-bases-018]]` — Diff-Shape 负责把形状生成对，YuelBond 负责把带噪几何合法化；这篇因此不再像一个完整闭环，而更像 3D 分子生成流水线中的控制层，后者则是必要的收口层。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4odkwmjuxnw-2247487143-1-jcim-diff-shape-controlnet.md`
- Type: markdown
- Kind: other
