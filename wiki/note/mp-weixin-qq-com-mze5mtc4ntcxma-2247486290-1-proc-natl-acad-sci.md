---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mze5mtc4ntcxma-2247486290-1-proc-natl-acad-sci
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mze5mtc4ntcxma-2247486290-1-proc-natl-acad-sci.md
bloom: analyze
concepts:
  - manifold-constrained-generation
  - nucleus-level-diffusion
  - physical-validity-during-sampling
layer_1_bolds:
  - 现有扩散模型在三维分子生成中往往偏离物理可行的化学流形。
  - 研究人员提出 NucleusDiff——一种在化学流形上进行约束采样的去噪扩散模型。
  - 加入流形约束后，扩散轨迹保持在低势能区域，生成分子在几何与能量上更接近真实复合物。
layer_2_fragments:
  - 在采样过程中持续投影回化学流形
  - 原子核级表示连接几何与电子环境
  - 结构引导把口袋信息嵌入生成
  - 物理合法性在过程中维护
layer_3_thesis: 生成模型若把物理合法性留到采样结束后再检查，已经太晚了；真正有效的是让每一步去噪都在可行流形上发生。
status: complete
---

# mp-weixin-qq-com-mze5mtc4ntcxma-2247486290-1-proc-natl-acad-sci

## Layer 1 — bold key sentences

- **现有扩散模型在三维分子生成中往往偏离物理可行的化学流形。**
- **研究人员提出 NucleusDiff——一种在化学流形上进行约束采样的去噪扩散模型。**
- **加入流形约束后，扩散轨迹保持在低势能区域，生成分子在几何与能量上更接近真实复合物。**

## Layer 2 — bold fragments

- **在采样过程中持续投影回化学流形**
- **原子核级表示连接几何与电子环境**
- **结构引导把口袋信息嵌入生成**
- **物理合法性在过程中维护**

## Layer 3 — one-sentence thesis

生成模型若把物理合法性留到采样结束后再检查，已经太晚了；真正有效的是让每一步去噪都在可行流形上发生。

## Concepts (tier_1_atoms)

- [[manifold-constrained-generation]]：生成轨迹被显式限制在物理可行流形上。
- [[nucleus-level-diffusion]]：以原子核而非更粗糙单位作为扩散生成基元。
- [[physical-validity-during-sampling]]：物理一致性在采样过程中维护，而不是后验过滤。

## Back-references

- [[mp-weixin-qq-com-af2rave-alphafold2]]：AF2RAVE把受体候选构象限制在自由能景观上，这篇把配体生成限制在化学流形上；两边都在缩小“看似合法但任务无效”的空间。
- [[mp-weixin-qq-com-mze5mte0njg3nq-2247484143-1-jctc]]：无数据粗粒化那篇也强调从能量函数直接学习而不是依赖样本复现，这篇是在生成任务里把同样的物理优先原则落到扩散轨迹上。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mze5mtc4ntcxma-2247486290-1-proc-natl-acad-sci.md`
- Type: markdown
- Kind: other
