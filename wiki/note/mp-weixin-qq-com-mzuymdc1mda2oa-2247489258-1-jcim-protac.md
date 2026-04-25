---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzuymdc1mda2oa-2247489258-1-jcim-protac
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247489258-1-jcim-protac.md
bloom: analyze
concepts:
  - "[[dynamic-ensemble-beats-single-crystal]]"
  - "[[conformation-coverage-as-metric]]"
  - "[[short-md-validates-generated-poses]]"
  - "[[weak-interface-needs-linker-mediated-modeling]]"
layer_1_bolds:
  - "**现有晶体结构仅为动态体系的静态快照，可能受晶体堆积干扰，难以真实反映生理状态下的构象全貌。**"
  - "**研究发现，同一PROTAC可诱导多种复合物构象，而现有计算方法对这类多稳定相互作用模式的预测精度仍不足。**"
  - "**建立基于构象覆盖度的量化评估体系，以更全面、动态的视角系统探索三元复合物的构象空间。**"
  - "**对于柔性较大的三元复合物，仅基于单一晶体结构的短时模拟可能无法充分覆盖其构象空间。**"
  - "**该研究提出的构象生成与短时模拟验证策略，能够有效探索传统模拟难以采样的构象空间，并捕获潜在稳定构象。**"
layer_2_fragments:
  - "**三元复合物不是一个姿势而是一片构象带**"
  - "**评价标准应从贴近晶体改成覆盖动力学**"
  - "**弱界面体系更依赖 linker 介导的瞬时配合**"
  - "**短时 MD 不是终点模拟而是生成结果验真器**"
  - "**对接流程的价值在于产出可被动力学筛的候选系综**"
layer_3_thesis: "这篇真正推进 PROTAC 建模的地方，不是把对接流程再串长一点，而是把“是否接近晶体结构”改写成“是否覆盖动态高概率构象区”，从而承认三元复合物设计首先是系综问题。"
status: complete
---

# PROTAC 设计首先面对的不是一个结构，而是一片构象空间

## Layer 1 — bold key sentences

- **现有晶体结构仅为动态体系的静态快照，可能受晶体堆积干扰，难以真实反映生理状态下的构象全貌。**
- **研究发现，同一PROTAC可诱导多种复合物构象，而现有计算方法对这类多稳定相互作用模式的预测精度仍不足。**
- **建立基于构象覆盖度的量化评估体系，以更全面、动态的视角系统探索三元复合物的构象空间。**
- **对于柔性较大的三元复合物，仅基于单一晶体结构的短时模拟可能无法充分覆盖其构象空间。**
- **该研究提出的构象生成与短时模拟验证策略，能够有效探索传统模拟难以采样的构象空间，并捕获潜在稳定构象。**

## Layer 2 — bold fragments

- **三元复合物不是一个姿势而是一片构象带**
- **评价标准应从贴近晶体改成覆盖动力学**
- **弱界面体系更依赖 linker 介导的瞬时配合**
- **短时 MD 不是终点模拟而是生成结果验真器**
- **对接流程的价值在于产出可被动力学筛的候选系综**

## Layer 3 — one-sentence thesis

这篇真正推进 PROTAC 建模的地方，不是把对接流程再串长一点，而是把“是否接近晶体结构”改写成“是否覆盖动态高概率构象区”，从而承认三元复合物设计首先是系综问题。

## Concepts (tier_1_atoms)

- `[[dynamic-ensemble-beats-single-crystal]]`：对高柔性复合物而言，单个晶体姿势更像入口而不是答案。
- `[[conformation-coverage-as-metric]]`：构象生成质量应该用覆盖真实动力学密度区来衡量，而不是只看一个 RMSD。
- `[[short-md-validates-generated-poses]]`：短时 MD 在这里不是昂贵附属品，而是验证候选构象是否站得住的快速过滤器。
- `[[weak-interface-needs-linker-mediated-modeling]]`：POI 与 E3 弱接触时，linker 不只是连接件，而是界面形成的核心参与者。

## Back-references

- `[[mp-weixin-qq-com-mzkzmjc1njk0mq-2247485683-1-fep]]`：FEP Omega 追求用短轨迹提取可学习信号，这篇则把短轨迹用于验证构象系综；两者都说明短 MD 不必承担“还原全部真实世界”的任务，只要被放在对的位置上就足够有用。
- `[[mp-weixin-qq-com-mzk0mte3ntm2na-2247491383-1-ras-pi3k-ppi-glue-breaker-vividion]]`：那篇把 PPI 重编程看成作用模式连续体，这篇补上结构层面的难点：一旦作用模式靠弱界面和瞬时配合维持，静态结构就更不足以指导设计。
- `[[mp-weixin-qq-com-mzu5otu3nzyyoq-2247492421-1-nature-ml]]`：如果 PoseBench 一类工作强调静态 pose 预测的误差上限，这篇提醒我 PROTAC 更该比较的是生成系综能否落到真实动力学高密区，而不是能否精确复刻一张晶体照片。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247489258-1-jcim-protac.md`
- Type: markdown
- Kind: other
