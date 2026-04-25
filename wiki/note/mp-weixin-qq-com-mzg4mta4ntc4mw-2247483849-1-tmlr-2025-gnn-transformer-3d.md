---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg4mta4ntc4mw-2247483849-1-tmlr-2025-gnn-transformer-3d
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483849-1-tmlr-2025-gnn-transformer-3d.md
bloom: analyze
concepts:
  - "[[transformers-can-learn-distance]]"
  - "[[layernorm-as-geometry-engine]]"
  - "[[data-augmentation-over-equivariant-complexity]]"
  - "[[coordinate-plus-transformer-minimalism]]"
layer_1_bolds:
  - "只要给标准 Transformer 喂坐标，它就能自己学会按欧氏距离‘看世界’。"
  - "Q·K 点积可以近似为‘负的平方距离’。"
  - "只需要给每个 head 预留 5 维左右来专门处理坐标，就足以学会 3D 距离。"
  - "标准 Transformer（pre-norm, dot-product attention），到底能不能原生地学会欧氏距离和三维结构？作者的答案是：可以。"
layer_2_fragments:
  - "注意力本身能逼近高斯距离核"
  - "LayerNorm在偷偷制造几何"
  - "随机旋转增强可以代替部分等变设计"
  - "坐标加Transformer是一条极简路线"
layer_3_thesis: "这篇工作真正重要的不是宣布‘GNN过时了’，而是证明很多被认为必须通过专门几何架构显式注入的能力，其实可以在标准Transformer里由表示、归一化和数据增强共同涌现出来，因此复杂架构需要重新举证其必要性。"
status: complete
---

## Layer 1 — bold key sentences

- **只要给标准 Transformer 喂坐标，它就能自己学会按欧氏距离“看世界”。**
- **Q·K 点积可以近似为“负的平方距离”。**
- **只需要给每个 head 预留 5 维左右来专门处理坐标，就足以学会 3D 距离。**
- **标准 Transformer（pre-norm, dot-product attention），到底能不能原生地学会欧氏距离和三维结构？作者的答案是：可以。**

## Layer 2 — bold fragments

- **注意力本身能逼近高斯距离核**
- **LayerNorm在偷偷制造几何**
- **随机旋转增强可以代替部分等变设计**
- **坐标加Transformer是一条极简路线**

## Layer 3 — one-sentence thesis

这篇工作真正重要的不是宣布“GNN过时了”，而是证明很多被认为必须通过专门几何架构显式注入的能力，其实可以在标准Transformer里由表示、归一化和数据增强共同涌现出来，因此复杂架构需要重新举证其必要性。

## Concepts (tier_1_atoms)

- `[[transformers-can-learn-distance]]` — 这是全文核心结论，直接挑战了“结构任务必须上专用几何网络”的默认前提。
- `[[layernorm-as-geometry-engine]]` — 文章最反直觉的洞见之一是 LayerNorm 在几何学习中的作用。
- `[[data-augmentation-over-equivariant-complexity]]` — 随机旋转增强提供了比堆复杂等变模块更简单的路径。
- `[[coordinate-plus-transformer-minimalism]]` — 这条路线强调最少额外结构、最大底层优化兼容性。

## Back-references

- `[[mp-weixin-qq-com-mze5odgwota0nq-2247485502-1-structure-2025-plddt]]` — 这篇说明 Transformer 可以学到结构距离，但 pLDDT 那篇提醒我，学到几何结构并不等于学到动力学柔性，两者不能继续混读。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench]]` — 如果结构表示真的更强，最终应该在更接近实战的 benchmark 上体现；MolGenBench正好提供了这种检验场。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247484032-2-jcim-2025-amp-openadmet-adme]]` — ADME那篇提醒表征进步必须在更严格切分下才有意义；同样地，这里的架构极简优势也要放到真实泛化任务里看，而不是只看模型内分析。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg4mta4ntc4mw-2247483849-1-tmlr-2025-gnn-transformer-3d.md`
- Type: markdown
- Kind: other
