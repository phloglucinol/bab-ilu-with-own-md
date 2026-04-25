---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MjM5MTcyMTQ5OQ%3D%3D&mid=2647507459&idx=1&sn=9d9e6570215a79592fc4d29befd26560
canonical_url: https://mp.weixin.qq.com/s?__biz=MjM5MTcyMTQ5OQ%3D%3D&mid=2647507459&idx=1&sn=9d9e6570215a79592fc4d29befd26560
source_domain: mp.weixin.qq.com
title: Boltz2 参数详解：从入门到精通的完整指南
author: 
published_at: 
fetched_at: 2026-04-25T02:03:40Z
extractor: wechat_worker
content_hash: e8729b75f528cb09ea202628fd4c64a81197ac443e24b863c8725de451b1f84e
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/SoB2vic5Yaoa88T2YfxuGud5Dy8iaNxPhgcLvAoYKGcyy4uSdjyfUuH9ibAZRccMno5tfdWPtSbHiazcZreDicPMAHA/0.jpg) 

# Boltz2 参数详解：从入门到精通的完整指南

原创 张江药哥 张江药哥 [ 张江药哥 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

## 

前言

Boltz-2 是由 MIT 和 Recursion 联合开发的开源生物分子结构预测模型，是目前最受欢迎的 AlphaFold3 开源替代方案。相比前代 Boltz-1，Boltz-2 不仅能预测蛋白质复合物的三维结构，还新增了结合亲和力预测功能。

本文将全面介绍 Boltz2 的输出指标含义、推荐阈值以及不同应用场景下的最佳参数设置，所有内容均基于官方文档和最新研究文献，确保准确可靠。

---

## 

第一部分：输出置信度指标详解

运行 Boltz2 后，会生成 confidence\_\*.json 文件，包含多个评估指标。

### 

1.1 核心置信度指标

| 指标                | 全称                    | 范围  | 含义                                       |
| ----------------- | --------------------- | --- | ---------------------------------------- |
| confidence\_score | 综合置信度分数               | 0-1 | 复合评分 = 0.8 × pLDDT + 0.2 × iPTM，用于预测结果排序 |
| ptm               | Predicted TM-score    | 0-1 | 评估整体折叠准确性，判断蛋白质全局拓扑结构是否正确                |
| iptm              | Interface PTM         | 0-1 | 评估链间相互作用界面的准确性，复合物预测的关键指标                |
| ligand\_iptm      | Ligand Interface PTM  | 0-1 | 专门评估蛋白质-配体界面的准确性                         |
| protein\_iptm     | Protein Interface PTM | 0-1 | 专门评估蛋白质-蛋白质界面的准确性，PPI研究的核心指标             |

### 

1.2 局部置信度指标

| 指标              | 全称                      | 范围  | 含义               |
| --------------- | ----------------------- | --- | ---------------- |
| complex\_plddt  | Complex pLDDT           | 0-1 | 整个复合物的残基水平置信度平均值 |
| complex\_iplddt | Complex Interface pLDDT | 0-1 | 仅界面区域残基的置信度平均值   |

### 

1.3 距离误差指标

| 指标            | 全称                               | 单位    | 含义                  |
| ------------- | -------------------------------- | ----- | ------------------- |
| complex\_pde  | Complex Predicted Distance Error | 埃 (Å) | 复合物整体的预测对齐误差，数值越低越好 |
| complex\_ipde | Complex Interface PDE            | 埃 (Å) | 界面区域的距离误差，数值越低越好    |

> 重要提示：与其他指标"越高越好"不同，PDE 指标的单位是埃，数值越低表示预测越准确。 

---

## 

第二部分：推荐阈值标准

### 

2.1 蛋白质-蛋白质相互作用 (PPI)

基于 AlphaFold-Multimer 官方文档和最新研究文献：

| 质量等级           | ipTM  | protein\_iptm | complex\_ipde | confidence\_score |
| -------------- | ----- | ------------- | ------------- | ----------------- |
| 优秀 (Excellent) | ≥ 0.9 | ≥ 0.9         | ≤ 0.5 Å       | ≥ 0.95            |
| 良好 (Good)      | ≥ 0.8 | ≥ 0.8         | ≤ 1.0 Å       | ≥ 0.90            |
| 一般 (Fair)      | ≥ 0.6 | ≥ 0.6         | \-            | \-                |
| 不合格 (Poor)     | < 0.6 | < 0.6         | \-            | \-                |

关键参考值（来自官方文档）：

* ipTM > 0.8：高置信度预测，结果可信
* ipTM 0.6-0.8：灰色地带，预测可能正确也可能错误
* ipTM < 0.6：预测很可能失败，不建议采信

### 

2.2 抗体-抗原对接

根据最新基准测试研究（mAbs, 2025）：

| 应用场景    | ipTM 阈值 |
| ------- | ------- |
| 抗体-抗原   | ≥ 0.5   |
| 纳米抗体-抗原 | ≥ 0.4   |

> 注意：Boltz-1/2 在抗体对接上的高精度成功率约为 4-5%，AlphaFold3 约为 10-13%。这些工具适合用于初步筛选，而非最终判断。 

---

## 

第三部分：推理参数详解

### 

3.1 核心参数

| 参数                 | 默认值   | 范围      | 含义                           |
| ------------------ | ----- | ------- | ---------------------------- |
| recycling\_steps   | 3     | 1-10    | 神经网络迭代优化次数。数值越高，准确性越好，但耗时增加  |
| sampling\_steps    | 50    | 10-1000 | 扩散模型去噪步数。步数越多，结构质量通常越好       |
| diffusion\_samples | 1     | 1-25    | 生成的独立预测数量。多个样本可提供构象多样性       |
| step\_scale        | 1.638 | 0.5-5.0 | 采样温度。数值越低，样本多样性越高；数值越高，收敛性越好 |
| seed               | 随机    | 整数      | 随机种子。不同种子会产生不同结果，用于可重复性控制    |

### 

3.2 亲和力预测专用参数

| 参数                           | 默认值   | 范围      | 含义                     |
| ---------------------------- | ----- | ------- | ---------------------- |
| sampling\_steps\_affinity    | 200   | 10-1000 | 亲和力预测专用的扩散步数，通常高于结构预测  |
| diffusion\_samples\_affinity | 5     | 1-10    | 亲和力预测的独立样本数，用于平均以提高可靠性 |
| affinity\_mw\_correction     | False | 布尔值     | 分子量校正，对含金属配体有帮助        |

### 

3.3 物理势能校正 (Boltz-Steering)

| 参数                           | 默认值             | 含义                            |
| ---------------------------- | --------------- | ----------------------------- |
| potentials / use\_potentials | True (Boltz-2x) | 启用物理势能引导。在扩散过程中应用物理约束，提高结构合理性 |

Boltz-Steering 的作用：

* 消除空间冲突（原子重叠）
* 纠正手性中心错误
* 修正立体化学构型
* 确保芳香环保持平面
* 整体提升物理合理性，同时不损失准确性

性能开销：

* NVIDIA GPU：运行时间增加约 1.25 倍
* Mac (M系列)：运行时间增加约 2.5 倍

---

## 

第四部分：不同场景的推荐参数设置

### 

4.1 快速筛选模式（速度优先）

recycling_steps: 3 sampling_steps: 20 diffusion_samples: 1 potentials: false

适用场景：大规模化合物库的初步虚拟筛选

预计耗时：最短

### 

4.2 标准预测模式（平衡模式）

recycling_steps: 3 sampling_steps: 50 diffusion_samples: 1 potentials: true step_scale: 1.638

适用场景：常规结构预测任务

预计耗时：中等

### 

4.3 高质量预测模式（精度优先）

recycling_steps: 6 sampling_steps: 100 diffusion_samples: 5 potentials: true

适用场景：重要靶点，需要高置信度结果

预计耗时：较长

### 

4.4 AlphaFold3 级别设置（最高质量）

recycling_steps: 10 diffusion_samples: 25 potentials: true

适用场景：关键预测，不计较运行时间

预计耗时：显著增加

> 官方说明：使用 recycling\_steps=10 和 diffusion\_samples=25 可达到 AlphaFold3 的默认参数水平，但预测时间会显著延长。 

### 

4.5 多 Seed 筛选策略

用于虚拟筛选应用：

seeds: [1, 2, 3, 4, 5]  # 5个不同的随机种子 diffusion_samples: 5 recycling_steps: 3 potentials: true

工作流程：

1. 对每个靶点-配体对使用多个 seed 运行（5-20个）
2. 每对选择最佳预测（最高 ipTM 或结构一致性）
3. 跨所有候选按置信度指标排序
4. 优先验证排名靠前的候选

---

## 

第五部分：高级功能

### 

5.1 实验方法条件化 (Method Conditioning)

Boltz-2 支持根据实验方法类型调整预测偏好：

| 方法     | 参数值                 | 适用场景              |
| ------ | ------------------- | ----------------- |
| X射线晶体学 | x-ray diffraction   | 预测类似晶体结构的构象       |
| 溶液NMR  | solution nmr        | 预测溶液态构象           |
| 冷冻电镜   | electron microscopy | 预测与 Cryo-EM 兼容的模型 |
| 分子动力学  | md                  | 预测类似 MD 模拟的构象集合   |
| 固态NMR  | solid-state nmr     | 膜蛋白等固态样品          |
| 中子衍射   | neutron diffraction | 需要显示氢原子的结构        |

### 

5.2 模板条件化 (Template Conditioning)

提供已知结构作为模板指导预测：

* 支持多链模板（Boltz-2 新功能）
* 可选择软约束或严格遵循模式
* 适用于建模突变体或新结合伙伴

### 

5.3 接触和口袋约束 (Contact & Pocket Constraints)

整合先验知识：

* 定义残基对距离约束
* 指定结合口袋残基
* 模型会应用软势能以满足约束条件

---

## 

第六部分：结果解读指南

### 

6.1 高分数的含义

| 指标          | 高分含义        |
| ----------- | ----------- |
| ipTM > 0.8  | 模型对链间排列高度自信 |
| pLDDT > 80  | 局部结构预测置信度高  |
| PDE < 1.0 Å | 距离预测精确      |

### 

6.2 低分数的含义

| 指标          | 低分含义          |
| ----------- | ------------- |
| ipTM < 0.6  | 预测很可能失败，界面不可信 |
| pLDDT < 50  | 无序区域或预测较差的区域  |
| PDE > 2.0 Å | 相对位置不确定       |

### 

6.3 常见误区

| 误区             | 正确理解                       |
| -------------- | -------------------------- |
| 高 ipTM 意味着一定结合 | 错误。高分只表示模型自信，可能存在假阳性       |
| 低 ipTM 意味着不结合  | 错误。真正结合的配对也可能得分低（假阴性率约65%） |
| 单一指标足以判断       | 错误。应综合多个指标判断               |
| 计算结果可替代实验      | 错误。计算筛选只能缩小范围，最终需实验验证      |

---

## 

第七部分：实用工作流程示例

### 

虚拟筛选流程

第一步：输入准备    ├── 靶标蛋白序列    └── 候选分子库（抗体/配体）  第二步：初步筛选    ├── recycling_steps: 3    ├── diffusion_samples: 1    └── 每对运行多个 seed (5x)  第三步：置信度过滤    ├── 抗体筛选：ipTM >= 0.5    ├── 蛋白互作：ipTM >= 0.6    └── complex_ipde <= 1.0  第四步：精细化预测（Top 候选）    ├── recycling_steps: 6    ├── diffusion_samples: 10    └── potentials: true  第五步：综合排序    ├── 组合 ipTM + pLDDT    ├── 可选：Rosetta 能量重打分    └── 选择 Top N 进行验证  第六步：实验验证    └── SPR、ELISA 或其他结合实验

### 

质量分组脚本

可使用以下 Python 脚本对结果进行自动分组：

def classify_quality(row):     protein_iptm = row['protein_iptm']     iptm = row['iptm']     complex_ipde = row['complex_ipde']     confidence = row['confidence_score']          # Excellent     if (protein_iptm >= 0.9 and iptm >= 0.9 and          complex_ipde <= 0.5 and confidence >= 0.95):         return 'Excellent'     # Good     elif (protein_iptm >= 0.8 and iptm >= 0.8 and            complex_ipde <= 1.0 and confidence >= 0.90):         return 'Good'     # Fair     elif protein_iptm >= 0.6 and iptm >= 0.6:         return 'Fair'     # Poor     else:         return 'Poor'

---

## 

第八部分：常见问题解答

### 

Q1: protein\_iptm 和 iptm 有什么区别？

A: iptm 是所有链间相互作用的综合评分，而 protein\_iptm 仅计算蛋白质-蛋白质之间的界面。如果你的体系包含配体，iptm 会包含蛋白-配体界面的贡献，而 protein\_iptm 只关注蛋白间相互作用。

### 

Q2: 为什么我的预测 ipTM 很高，但实验验证失败？

A: 这是正常现象。高 ipTM 只表示模型对预测结果有信心，但模型可能"过度自信"。建议：

* 使用多个 seed 进行预测
* 结合多个指标综合判断
* 将计算结果视为筛选工具，而非最终判断

### 

Q3: 应该用 Boltz-2 还是 Boltz-2x？

A: Boltz-2x 是启用了 Boltz-steering 物理势能的版本。建议：

* 如果关注物理合理性：使用 Boltz-2x（potentials: true）
* 如果追求速度：使用 Boltz-2（potentials: false）
* 大多数情况下推荐使用 Boltz-2x

### 

Q4: diffusion\_samples 设多少合适？

A:

* 快速筛选：1
* 标准预测：1-5
* 高质量预测：5-10
* 最高质量：25（与 AlphaFold3 默认设置相同）

每增加一个 sample，计算时间近似线性增加，但第一个 sample 之后的额外 sample 耗时相对较少。

### 

Q5: 抗体-抗原预测准确率低怎么办？

A: 这是当前所有 AI 模型的共同挑战。建议：

* 使用多 seed 策略（20个以上）
* 采用结构一致性选择方法
* 结合 Rosetta 能量重打分
* 将 ipTM >= 0.5 作为初筛阈值
* 最终依赖实验验证

---

## 

总结

Boltz-2 是一个强大的生物分子结构预测和虚拟筛选工具。正确理解其输出指标和参数设置对于获得可靠结果至关重要。

核心要点：

1. ipTM 和 protein\_iptm 是蛋白质-蛋白质相互作用预测最重要的指标
2. PDE 指标（越低越好）是 TM 评分的重要补充
3. Boltz-steering (potentials) 能显著提升结构的物理合理性
4. 多 seed 策略 可提高虚拟筛选的可靠性
5. 计算结果必须经过实验验证 才能作为最终结论

---

## 

参考文献

1. Boltz-2 论文: "Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction"
2. AlphaFold-Multimer 置信度评分: EBI Training Documentation
3. 抗体对接基准测试: "What does AlphaFold3 learn about antibody and nanobody docking" (mAbs, 2025)
4. NVIDIA NIM Boltz2 官方文档
5. Neurosnap Boltz-1/2 指标指南

---

官方资源：

* GitHub: https://github.com/jwohlwend/boltz
* 论文: https://jeremywohlwend.com/assets/boltz2.pdf

本文内容基于官方文档和经同行评审的文献，力求准确可靠。如有更新，请以官方文档为准。

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SoB2vic5YaoagO8RmSu2icRia5uereOO9gticA2uezpZlZ48Euops2QKKtXrl6NAPBmr4fNFS0vkl5AFQFwHnoeWcQ/0.png) 

 张江药哥 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SoB2vic5YaoagO8RmSu2icRia5uereOO9gticA2uezpZlZ48Euops2QKKtXrl6NAPBmr4fNFS0vkl5AFQFwHnoeWcQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
