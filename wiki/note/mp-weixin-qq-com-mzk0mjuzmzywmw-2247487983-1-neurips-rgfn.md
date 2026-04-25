---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk0mjuzmzywmw-2247487983-1-neurips-rgfn
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247487983-1-neurips-rgfn.md
bloom: analyze
concepts:
  - molecule-generation-should-follow-reaction-space
  - gflownet-in-reaction-trajectories
  - synthesizability-by-construction
layer_1_bolds:
  - 将分子生成过程与分子合成过程统一起来——分子不是被“设计出来”的，而是被“合成出来”的。
  - 优化目标（高活性/高评分）与合成可行性之间缺乏内在约束。
  - RGFN 属于第三类策略中最新的代表性工作。
layer_2_fragments:
  - 在反应空间而不是字符串空间生成
  - GFlowNet天生适合多模态高奖赏
  - 合成可行性要靠构造保证
  - 反应树就是生成轨迹
layer_3_thesis: RGFN最关键的判断是，药物生成模型不该把“合成性”当作事后评分，而该把它写进状态空间本身，这样高分分子才不是对oracle的投机取巧。
status: complete
---

# mp-weixin-qq-com-mzk0mjuzmzywmw-2247487983-1-neurips-rgfn

## Layer 1 — bold key sentences

- **将分子生成过程与分子合成过程统一起来——分子不是被“设计出来”的，而是被“合成出来”的。**
- **优化目标（高活性/高评分）与合成可行性之间缺乏内在约束。**
- **RGFN 属于第三类策略中最新的代表性工作。**

## Layer 2 — bold fragments

- **在反应空间而不是字符串空间生成**
- **GFlowNet天生适合多模态高奖赏**
- **合成可行性要靠构造保证**
- **反应树就是生成轨迹**

## Layer 3 — one-sentence thesis

RGFN最关键的判断是，药物生成模型不该把“合成性”当作事后评分，而该把它写进状态空间本身，这样高分分子才不是对oracle的投机取巧。

## Concepts (tier_1_atoms)

- [[molecule-generation-should-follow-reaction-space]]：真正可落地的生成模型应直接在反应空间中工作。
- [[gflownet-in-reaction-trajectories]]：GFlowNet适合在多步合成轨迹中发现多样高奖赏解。
- [[synthesizability-by-construction]]：合成可行性应由生成过程天然保证，而不是后验过滤。

## Back-references

- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247548964-1-ncs.md]]：SynGFN和这篇的共同点很明显，都是把设计和合成路线并在一起；区别是SynGFN更偏反应策略网络，RGFN更偏GFlowNet采样分布。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247489047-1-nat-commun-clickgen.md]]：ClickGen用模块化点击反应加RL解决同一问题，RGFN则提供更一般的GFlowNet反应树视角，两者是同一路线的不同实现。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247488573-1-molve-ai-quot-quot.md]]：MolVE说明真正的瓶颈常在优先级评估端，而RGFN提醒我前端生成端也得先解决“别吐出根本做不出来的分子”。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247487983-1-neurips-rgfn.md`
- Type: markdown
- Kind: other
