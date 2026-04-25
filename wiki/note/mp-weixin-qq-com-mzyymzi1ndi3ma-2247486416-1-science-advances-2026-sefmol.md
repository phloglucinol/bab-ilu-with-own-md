---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzyymzi1ndi3ma-2247486416-1-science-advances-2026-sefmol
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzyymzi1ndi3ma-2247486416-1-science-advances-2026-sefmol.md
bloom: analyze
concepts:
  - semi-flexible-generation
  - rl-steers-diffusion-trajectories
  - property-conditioning-stabilizes-rl
  - generation-time-conformation-control
layer_1_bolds:
  - "SeFMol 解决的就是这个问题：把扩散模型的去噪过程写成马尔可夫决策过程，再用强化学习去引导“半柔性”构象优化。"
  - "作者先做“刚性训练”，再做“半柔性优化”。"
  - "为了避免策略跑偏，作者还加了 KL 约束和价值网络。"
  - "过去很多方法更像先生成，再看能不能 dock 上去。SeFMol 在生成时就把 binding mode 往目标方向推。"
layer_2_fragments:
  - "扩散去噪本身就是决策过程"
  - "先学静态，再学构象调整"
  - "性质条件不是装饰，而是稀疏奖励缓冲器"
  - "50 步采样让方法接近工作流可用"
  - "半柔性比纯刚性更接近真实结合"
layer_3_thesis: "SeFMol的关键不是又把RL接到分子生成上，而是把“配体进入口袋后还会继续调整”这件事写进了生成轨迹本身。"
status: complete
---

# mp-weixin-qq-com-mzyymzi1ndi3ma-2247486416-1-science-advances-2026-sefmol

## Layer 1

- **SeFMol 解决的就是这个问题：把扩散模型的去噪过程写成马尔可夫决策过程，再用强化学习去引导“半柔性”构象优化。**
- **作者先做“刚性训练”，再做“半柔性优化”。**
- **为了避免策略跑偏，作者还加了 KL 约束和价值网络。**
- **过去很多方法更像先生成，再看能不能 dock 上去。SeFMol 在生成时就把 binding mode 往目标方向推。**

## Layer 2

- **扩散去噪本身就是决策过程**
- **先学静态，再学构象调整**
- **性质条件不是装饰，而是稀疏奖励缓冲器**
- **50 步采样让方法接近工作流可用**
- **半柔性比纯刚性更接近真实结合**

## Layer 3

SeFMol的关键不是又把RL接到分子生成上，而是把“配体进入口袋后还会继续调整”这件事写进了生成轨迹本身。

## Concepts

- [[semi-flexible-generation]]：重要，因为很多口袋生成方法默认配体近似刚体，这里明确把这个近似放松了。
- [[rl-steers-diffusion-trajectories]]：重要，因为它把 RL 的作用点从结果筛选前移到了扩散路径控制。
- [[property-conditioning-stabilizes-rl]]：重要，因为化学性质条件在这里承担了训练稳定器，而不只是多目标标签。
- [[generation-time-conformation-control]]：重要，因为它说明构象优化不一定要留到 docking 或 MD 后处理。

## Back-references

- [[mp-weixin-qq-com-mzy5nzezmjkzmq-2247484559-2-jctc]]：PROTEUS 用 RL 引导化学空间搜索，这篇则把 RL 深埋进扩散采样内部；两者一起看，能把“强化学习用于设计”拆成不同控制层级。
- [[mp-weixin-qq-com-mze5odgwota0nq-2247485295-1-pnas-2025-siteaf3-alphafold3]]：SiteAF3 强调位点条件化，回看 SeFMol 就会发现它补的是另一半问题：位点确定之后，配体构象还要在生成期继续适配。
- [[mp-weixin-qq-com-mzyzodi1otazna-2247486916-1-cell-pocketxmol-sciminer-ai]]：PocketXMol 追求统一全原子生成框架，这会改变我对 SeFMol 的理解，它更像“口袋小分子场景里先把构象控制做深”的专用器。 

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzyymzi1ndi3ma-2247486416-1-science-advances-2026-sefmol.md`
- Type: markdown
- Kind: other
