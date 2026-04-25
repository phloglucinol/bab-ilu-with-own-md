---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzuxmjkzntgyoq-2247488798-1-ligpath
kind: other
ingested_at: 2026-04-25T08:10:57Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzuxmjkzntgyoq-2247488798-1-ligpath.md
bloom: apply
concepts:
  - adaptive-dissociation-path
  - conformational-ensemble-as-screening-object
  - contact-metric-over-distance
  - ligand-unbinding-as-trajectory-object
layer_1_bolds:
  - "MoMA-LigPath 是首个模拟蛋白质-配体解离的网络服务器，基于分子机械表示和机器人运动规划算法（ML-RRT），通过解耦主动变量（配体位姿、键扭转角）与被动变量（蛋白质侧链扭转角）探索构象空间，仅需秒级至分钟级计算时间。"
  - "在上图中，我们可通过调整 softness 参数控制配体解离路径的搜索策略：较小的值（如 0.6）允许更激进的构象探索，适合寻找隐蔽的结合口袋；而较大的值（如 0.9）更接近物理真实，适合验证已知结合模式的解离路径。"
  - "打开 Path_1 后，你可以看到包含很多用数字命名的pdb文件，他们是配体解离过程中每一个阶段的“快照”。"
layer_2_fragments:
  - "配体解离路径是一个可操作对象"
  - "softness 在探索性和物理真实性之间调参"
  - "主动变量与被动变量解耦"
  - "多帧 PDB 快照把路径转成可视化轨迹"
layer_3_thesis: "LigPath 的价值不是又提供了一个网页工具，而是把蛋白-配体结合从静态 pose 推进成可检查、可调参、可复现实操的解离路径对象。"
status: complete
---

# LigPath 把配体结合从静态姿态变成可检查的解离路径

## Layer 1 — bold key sentences

- **MoMA-LigPath 是首个模拟蛋白质-配体解离的网络服务器，基于分子机械表示和机器人运动规划算法（ML-RRT），通过解耦主动变量（配体位姿、键扭转角）与被动变量（蛋白质侧链扭转角）探索构象空间，仅需秒级至分钟级计算时间。**
- **在上图中，我们可通过调整 softness 参数控制配体解离路径的搜索策略：较小的值（如 0.6）允许更激进的构象探索，适合寻找隐蔽的结合口袋；而较大的值（如 0.9）更接近物理真实，适合验证已知结合模式的解离路径。**
- **打开 Path_1 后，你可以看到包含很多用数字命名的pdb文件，他们是配体解离过程中每一个阶段的“快照”。**

## Layer 2 — bold fragments

- **配体解离路径是一个可操作对象**
- **softness 在探索性和物理真实性之间调参**
- **主动变量与被动变量解耦**
- **多帧 PDB 快照把路径转成可视化轨迹**

## Layer 3 — one-sentence thesis

LigPath 的价值不是又提供了一个网页工具，而是把蛋白-配体结合从静态 pose 推进成可检查、可调参、可复现实操的 [[ligand-unbinding-as-trajectory-object]]。

## Concepts (tier_1_atoms)

- [[adaptive-dissociation-path]]：路径不是预先钉死的一维距离，而是在柔性约束和碰撞约束下被搜索出来。
- [[conformational-ensemble-as-screening-object]]：这里的筛选对象不只是一个 docked pose，而是一串能展示离开口袋过程的构象快照。
- [[contact-metric-over-distance]]：LigPath 输出接触信息，说明判断路径是否合理不能只看配体质心移动了多远，还要看相互作用如何断开。
- [[ligand-unbinding-as-trajectory-object]] *(proposed)*：把“配体怎么离开口袋”作为可导出、可合并、可在 PyMOL 里检查的一级对象。

## Back-references

- [[mp-weixin-qq-com-mzkzmjc1njk0mq-2247486288-1-cpacs-md]]：cPaCS-MD 讨论的是自由能计算里反应坐标选错的代价，LigPath 则提供一个更轻量的工程入口，先让用户看到解离路径本身，而不是直接跳到自由能估计。
- [[mp-weixin-qq-com-af2rave-alphafold2]]：AF2RAVE 把受体从单结构改写成构象集合，LigPath 把配体从单姿态改写成离口袋轨迹；两者共同推翻“一个结构足以代表药设对象”的默认设定。
- [[mp-weixin-qq-com-mzk0mzyxntu0oa-2247486617-1-re-mmpbsa-pmf]]：RE-MMPBSA/PMF 那篇提醒采样窗口会决定排序质量，这篇提醒在进入自由能排序前，路径生成参数本身已经在塑造你会看到哪些离口袋过程。
- [[mp-weixin-qq-com-mzu5otu3nzyyoq-2247492421-1-nature-ml]]：PoseBench 暴露静态对接在新结合构象上的脆弱性，LigPath 的实用意义正是在静态 pose 之后补一层“这个配体能不能合理离开”的路径检查。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzuxmjkzntgyoq-2247488798-1-ligpath.md`
- Type: markdown
- Kind: other
