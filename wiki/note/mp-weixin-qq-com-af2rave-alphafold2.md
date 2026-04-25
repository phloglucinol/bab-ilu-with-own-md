---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-af2rave-alphafold2
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-af2rave-alphafold2.md
bloom: analyze
concepts:
  - conformational-ensemble-as-screening-object
  - sequence-to-ensemble
  - hierarchical-sampling
layer_1_bolds:
  - AlphaFold2通常输出单一结构，难以全面反映蛋白质在生理状态下的动态构象变化，而这些动态构象往往与药物结合及功能发挥密切相关。
  - AF2RAVE采用了独特的分层式工作流程，将AlphaFold2与基于机器学习的增强采样技术有机结合，系统地探索蛋白质体系的自由能景观和亚稳特性。
  - AF2RAVE从序列出发直接生成可用的蛋白质构象，无需耗时费力的实验操作，大大缩短了从靶点确定到虚拟筛选的时间周期。
layer_2_fragments:
  - 单一静态结构不足以代表成药构象
  - 全局骨架采样加局部侧链采样
  - 从序列直接生成holo候选构象库
  - 富集因子优于实验晶体结构
layer_3_thesis: 虚拟筛选里真正需要预测的不是“蛋白长什么样”，而是“蛋白会以哪些可结合姿态出现”，所以序列到构象集合比序列到单结构更接近药设任务本身。
status: complete
---

# mp-weixin-qq-com-af2rave-alphafold2

## Layer 1 — bold key sentences

- **AlphaFold2通常输出单一结构，难以全面反映蛋白质在生理状态下的动态构象变化，而这些动态构象往往与药物结合及功能发挥密切相关。**
- **AF2RAVE采用了独特的分层式工作流程，将AlphaFold2与基于机器学习的增强采样技术有机结合，系统地探索蛋白质体系的自由能景观和亚稳特性。**
- **AF2RAVE从序列出发直接生成可用的蛋白质构象，无需耗时费力的实验操作，大大缩短了从靶点确定到虚拟筛选的时间周期。**

## Layer 2 — bold fragments

- **单一静态结构不足以代表成药构象**
- **全局骨架采样加局部侧链采样**
- **从序列直接生成 holo 候选构象库**
- **富集因子优于实验晶体结构**

## Layer 3 — one-sentence thesis

虚拟筛选里真正需要预测的不是“蛋白长什么样”，而是“蛋白会以哪些可结合姿态出现”，所以 [[sequence-to-ensemble]] 比序列到单结构更接近药设任务本身。

## Concepts (tier_1_atoms)

- [[conformational-ensemble-as-screening-object]]：筛选对象不该是单个口袋，而是一个带权重的构象集合。
- [[sequence-to-ensemble]]：从序列直接生成可筛选的构象分布，而不是停在静态折叠预测。
- [[hierarchical-sampling]]：先抓骨架慢变量，再抓口袋侧链细节，这种分层比一次性乱采样更像问题分解。

## Back-references

- [[mp-weixin-qq-com-first-in-class]]：METL把物理先验塞进语言模型，AF2RAVE把动力学先验塞进结构预测，两者都说明“先验”真正值钱的地方不是更像训练集，而是更接近下游任务的约束面。
- [[mp-weixin-qq-com-mze5mtc4ntcxma-2247486290-1-proc-natl-acad-sci]]：NucleusDiff强调生成轨迹不能离开化学流形，这篇则强调筛选构象不能离开自由能景观；一个在配体侧约束生成，一个在受体侧约束候选空间。

## Source
- Input: `raw/articles/mp-weixin-qq-com-af2rave-alphafold2.md`
- Type: markdown
- Kind: other
