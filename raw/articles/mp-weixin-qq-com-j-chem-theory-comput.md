---
type: raw_article
source_url: https://mp.weixin.qq.com/s/pt5EuLkNQfUUWQcQ2yoceg
canonical_url: https://mp.weixin.qq.com/s/pt5EuLkNQfUUWQcQ2yoceg
source_domain: mp.weixin.qq.com
title: J. Chem. Theory Comput. | 面向高精度静电性质预测的有机分子图神经网络电荷模型
author: 
published_at: 
fetched_at: 2026-04-25T02:04:18Z
extractor: wechat_worker
content_hash: 20404c1f827272aa63613677c890babb9856ed71627123734e81fc01ef920335
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/jwaic6a7a9gN44TGWLPFcntWPccuDknRwWVHssanY6icbqmrsaUjh67tc9pn7qBUxoxmSe0GR5Sm9ziagDvaJrqog/0.jpg) 

# J. Chem. Theory Comput. | 面向高精度静电性质预测的有机分子图神经网络电荷模型

原创 DrugOne DrugOne [ DrugOne ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

DRUGONE

精确的电荷分布对于分子静电性质、反应性与分子间相互作用的预测至关重要。传统力场中的电荷模型通常依赖经验方法或低成本量子化学计算，难以在计算效率与准确度之间达到平衡。研究人员提出一种基于图神经网络（GNN）的电荷预测框架，能够高效推断有机分子的原子电荷，使其在静电性质计算中的表现接近高水平量子化学结果。

  
该模型结合局部与非局部特征，明确建模电荷守恒，并能在快速推理的同时保持高精度。研究人员证明，该模型可准确预测一系列静电性质，包括偶极矩、高阶多极矩、静电势与分子间相互作用能，为大规模分子模拟与药物设计提供了可实际落地的新工具。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRwS8tBs4kGE7RrytoQGE6rgMZFLR4ojmrk1bTzFgY4u0CZ0Gmn6gl6ag/640.png)

静电相互作用在有机分子体系中主导着反应性、结合能、构象稳定性与溶剂化行为。因此，分子模拟的精度在很大程度上取决于电荷模型的质量。

  
传统方法如 Mulliken、RESP 或基于 DFT 的方案虽然能提供可靠电荷，但计算成本高，难以满足大规模体系或实时模拟的需求。另一方面，经验力场中的固定电荷虽然计算快，但在多极性质以及环境响应方面表现有限。

  
近年来的机器学习电荷模型能以低成本模拟量子级别的电荷行为，但在以下方面仍不充分：

* 无法兼顾局域电子结构与长程静电效应；
* 难以通过可解释的方式确保电荷守恒；
* 在静电势与相互作用能预测上仍与高精度基准存在差距。

研究人员为此设计了一个面向静电性质的专用 GNN 电荷框架，使其能够从分子图结构中同时学习局部化学环境与分子整体极化行为。

  
**方法**

研究人员构建了一个以消息传递图神经网络为核心的电荷预测模型，并加入以下关键设计：

* 局部–非局部混合表示：GNN 捕获邻域化学信息，同时引入全局读出模块表征分子整体极化。
* 电荷守恒层：所有原子电荷经过投影确保总电荷满足分子净电荷要求。
* 多任务训练策略：模型同时拟合 DFT 计算得到的原子电荷、偶极矩、多极矩与静电势，使其具备更强泛化性。

该模型使用包含数万分子的量子化学数据库进行训练，推理速度远超 DFT，而精度接近高水平量子化学结果。

  
**结果**

**模型架构与训练表现**

研究人员展示模型的整体结构：

* 消息传递层负责原子表示更新；
* 全局上下文向量建模分子极化；
* 输出层通过守恒约束生成物理一致的电荷分布。

在训练集和验证集上，模型的电荷预测误差显著低于传统方法与已有 ML 模型。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRwibPRjSlRqHuA6ufvdkCLnEf3MR0Qn0zd3eN2FDrb8LJUxkiawjqQo3oA/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRwuPdDEWsnYKkqoQt8bbXJHTB2whLE2REUyWRBNz1kcPBPyYkfLKAeqQ/640.png)

  
**原子电荷预测的准确性**

研究人员比较了该模型与 Mulliken、RESP 以及其他 ML 模型的表现：

* 在包含多种官能团的测试集上，GNN 电荷模型展现出最低的平均绝对误差
* 对于极化强烈的体系（如酯、氨基、硝基等），模型仍能保持高度稳定性
* 电荷预测在不同构象与不同取代基下均表现一致，显示其良好泛化能力

  
**静电特性（ESP、偶极矩、多极矩）的重现能力**

GNN 电荷模型不仅预测原子电荷，更能准确重建分子静电势：

* 静电势的均方误差显著低于其他电荷模型；
* 三阶及更高多极矩重现能力突出，说明其捕获了更完整的电子密度分布；
* 对大分子、多芳环系统和强极性结构具有稳定表现。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRwqFv2gsEKbKKUuByq0QFrON70o6WbvRVWJRhB1MIBbXj9eWA3lqPy9g/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRw0grX5OiazwrrWc64Y5ibjz5NsjoJ3I1MZTHEf6zYapO0icJY7LBKnDPIg/640.png)

  
**分子间相互作用能预测**

GNN 电荷模型在 intermolecular electrostatics（如氢键、π–π、离子–偶极）中的表现接近 DFT 基准：

* 能量误差低于传统力场固定电荷模型；
* 对不同距离下的静电吸引与排斥均能精确重建；
* 在弱相互作用体系中（如水簇、醇类、酰胺）表现尤为优异。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRwicll8XGNvVmRIicNb3UicNLUlia8lsOXks2T2Hupcb5ofCVDSZgKeC4IKA/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRw3OcXtjkLlowYP17qtP7D9lriboDxXZWe0lhYwW5AWEKJGdRBfMgibsNQ/640.png)

  
**在分子动力学模拟中的应用测试**

研究人员将模型输出的电荷用于短程 MD 模拟：

* 体系能量收敛稳定，无数值震荡；
* 构象分布及自由能曲线与 DFT 基准一致；
* 揭示其可作为下一代 ML 力场中电荷模块的重要组成部分。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRwk2ICIkIz9KlWbVAkwicW0nnoT22FBvCqfzibR6DGiaZhMu1kzGrLCAx9Q/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRw6kicu27cgdH9mwaGRfnxtTT6ZXJyqX1mMaYD3KFOWaCkZkcuAGOJpHQ/640.png)

  
**案例研究：功能基团电荷再现**

该模型能准确处理高极化与共振结构，如：

* 羧酸与酯基的负电荷离域；
* 硝基官能团中的强电子吸引；
* 含卤素与季铵盐体系中高度非均匀的电荷分布。

其电荷分布与 DFT 结果高度一致。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gN44TGWLPFcntWPccuDknRwRH5mXLalkSjhEhn3dQuYkzuDumViaJPYcz4CgdEtBphib48UqM1PCiaxA/640.png)

  
**讨论**

研究人员提出的 GNN 电荷模型填补了传统力场电荷模型与高精度量子化学之间的性能缺口：

* **高精度**：多项指标接近 DFT，远优于现有 ML 电荷方法。
* **高速度**：推理成本与传统力场相当，可用于千到百万级规模分子模拟。
* **物理一致性**：电荷守恒、极化行为与多极矩均能自然出现。
* **可扩展性**：适用于从小分子建模到药物设计、材料筛选等任务。

未来，研究人员计划将该电荷模块进一步整合至端到端 ML 力场中，以提升分子模拟的物理真实性和效率。

整理 | DrugOne团队

  
**参考资料**

  
Adams, Charlie, Joshua T. Horton, Lily Wang, Simon Boothroyd, David L. Mobley, David W. Wright, and Daniel J. Cole. "A graph neural network charge model targeting accurate electrostatic properties of organic molecules." Journal of Chemical Theory and Computation (2025).

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/mS8qdZ3O8bgdeoYb8GbWMEQtibvyWMWd4ibMHwnXR3p2ib7OFjXc5270g3H1H58WIiclWBQibtJZHIUtWBGcl2czITw/640.gif)

**内容为【DrugOne】公众号原创**｜转载请注明来源

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNehllibjzmuk4oLoB5rbwiaptSMEyFTTvTGzKpWggLwMXaOg5D9z1CFfdjdkorM4IHicxibkXEAe2IPA/0.png) 

 DrugOne 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNehllibjzmuk4oLoB5rbwiaptSMEyFTTvTGzKpWggLwMXaOg5D9z1CFfdjdkorM4IHicxibkXEAe2IPA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
