---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkzmzkxnjq4nw-2247494089-1-nat-comput-sci-if-18-3
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkzmzkxnjq4nw-2247494089-1-nat-comput-sci-if-18-3.md
bloom: analyze
concepts:
  - reaction-coordinate-without-handcrafted-cv
  - committor-learning-from-cartesian-geometry
  - atom-level-interpretability-for-rare-events
layer_1_bolds:
  - 该方法能够直接从原子坐标预测提交者函数，从而绕过对手工制作的集体变量的需求。
  - 首次实现了从原子笛卡尔坐标直接学习承诺函数，完全摒弃了对人工设计集体变量的依赖。
  - qGNN计算的分子跃迁速率常数与已发表的实验/理论值高度吻合。
layer_2_fragments:
  - 不再先手工假设集体变量
  - 从几何直接学承诺函数
  - 原子级灵敏度解释驱动位点
  - 速率常数也能一起落地
layer_3_thesis: qGNN最重要的贡献不是又做出一个预测器，而是把“反应坐标应该先由人定义”这条老前提拆掉了，改成让几何和动力学自己决定什么才算进程变量。
status: complete
---

# mp-weixin-qq-com-mzkzmzkxnjq4nw-2247494089-1-nat-comput-sci-if-18-3

## Layer 1 — bold key sentences

- **该方法能够直接从原子坐标预测提交者函数，从而绕过对手工制作的集体变量的需求。**
- **首次实现了从原子笛卡尔坐标直接学习承诺函数，完全摒弃了对人工设计集体变量的依赖。**
- **qGNN计算的分子跃迁速率常数与已发表的实验/理论值高度吻合。**

## Layer 2 — bold fragments

- **不再先手工假设集体变量**
- **从几何直接学承诺函数**
- **原子级灵敏度解释驱动位点**
- **速率常数也能一起落地**

## Layer 3 — one-sentence thesis

qGNN最重要的贡献不是又做出一个预测器，而是把“反应坐标应该先由人定义”这条老前提拆掉了，改成让几何和动力学自己决定什么才算进程变量。

## Concepts (tier_1_atoms)

- [[reaction-coordinate-without-handcrafted-cv]]：反应坐标不必先由专家手工压缩成少数CV。
- [[committor-learning-from-cartesian-geometry]]：直接从笛卡尔坐标学习承诺函数，保留高维几何信息。
- [[atom-level-interpretability-for-rare-events]]：通过灵敏度分析标出真正驱动稀有跃迁的原子。

## Back-references

- [[mp-weixin-qq-com-mzkzmjc1njk0mq-2247486288-1-cpacs-md]]：cPaCS-MD已经提醒我一维距离坐标常常不够，这篇进一步把替代方案说清楚了：不要换另一组手工CV，而是直接学承诺函数。
- [[mp-weixin-qq-com-mzkzmty0nzmzng-2247485327-1-pre-antti-j-niemi]]：那篇用局部拓扑解释折叠转变，这篇提供了数据驱动的操作化路线，未来完全可以问qGNN学出的关键原子是否对应那些拓扑改革位置。
- [[mp-weixin-qq-com-mzk0mzyxntu0oa-2247486617-1-re-mmpbsa-pmf]]：RE-MMPBSA说明采样窗口会扭曲排序，这篇则把问题前移到表征层：如果反应进程本身压错了，后面怎么算自由能都可能是错的。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzkzmzkxnjq4nw-2247494089-1-nat-comput-sci-if-18-3.md`
- Type: markdown
- Kind: other
