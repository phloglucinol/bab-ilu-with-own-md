---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk0mjuzmzywmw-2247489047-1-nat-commun-clickgen
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247489047-1-nat-commun-clickgen.md
bloom: analyze
concepts:
  - click-chemistry-as-generation-grammar
  - inpainting-solves-synthesis-vs-novelty-tension
  - twenty-day-ai-to-bench-loop
layer_1_bolds:
  - 一个核心瓶颈始终制约着该领域的工程转化：生成分子的合成可行性（synthesizability）普遍偏低。
  - 核心设计哲学：通过inpainting技术解决合成可行性与新颖性之间的固有矛盾。
  - 从ClickGen生成分子库→完成三个先导化合物合成并获得体外生物活性数据，全程仅用20天。
layer_2_fragments:
  - 点击化学被当成生成语法
  - 反应组合器保底合成性
  - inpainting负责骨架跳跃
  - 湿实验闭环速度被真正压缩
layer_3_thesis: ClickGen的关键突破不是再把对接分数做高，而是证明“模块化真实反应 + 局部骨架修补 + 强化学习”可以同时拿到新颖性和可合成性，并且真的把闭环推进到实验台上。
status: complete
---

# mp-weixin-qq-com-mzk0mjuzmzywmw-2247489047-1-nat-commun-clickgen

## Layer 1 — bold key sentences

- **一个核心瓶颈始终制约着该领域的工程转化：生成分子的合成可行性（synthesizability）普遍偏低。**
- **核心设计哲学：通过inpainting技术解决合成可行性与新颖性之间的固有矛盾。**
- **从ClickGen生成分子库→完成三个先导化合物合成并获得体外生物活性数据，全程仅用20天。**

## Layer 2 — bold fragments

- **点击化学被当成生成语法**
- **反应组合器保底合成性**
- **inpainting负责骨架跳跃**
- **湿实验闭环速度被真正压缩**

## Layer 3 — one-sentence thesis

ClickGen的关键突破不是再把对接分数做高，而是证明“模块化真实反应 + 局部骨架修补 + 强化学习”可以同时拿到新颖性和可合成性，并且真的把闭环推进到实验台上。

## Concepts (tier_1_atoms)

- [[click-chemistry-as-generation-grammar]]：把点击化学和酰胺化规则直接当成生成语法。
- [[inpainting-solves-synthesis-vs-novelty-tension]]：用分子inpainting缓解可合成性与骨架新颖性的冲突。
- [[twenty-day-ai-to-bench-loop]]：AI分子生成到实验验证的闭环时间可以被压缩到工程可用尺度。

## Back-references

- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247487983-1-neurips-rgfn.md]]：RGFN用GFlowNet在反应树里生成，ClickGen则用点击化学语法和RL走得更工程化，二者都说明合成规则不能后补。
- [[mp-weixin-qq-com-mzkznjizmtu0nw-2247548964-1-ncs.md]]：SynGFN把反应轨迹和分子设计绑定，这篇是在固定模块化反应上做更强的新颖性生成，两者都是“设计-合成一体化”的不同形态。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247488573-1-molve-ai-quot-quot.md]]：ClickGen证明前端闭环能跑到实验，MolVE提醒后端仍需要标准化优先级和人工审查界面，闭环才算完整。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247489047-1-nat-commun-clickgen.md`
- Type: markdown
- Kind: other
