---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg3OTc3NDc0MA%3D%3D&mid=2247487627&idx=1&sn=2ea597ba8bddf4a62f4c6cdaef0d73db
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg3OTc3NDc0MA%3D%3D&mid=2247487627&idx=1&sn=2ea597ba8bddf4a62f4c6cdaef0d73db
source_domain: mp.weixin.qq.com
title: Nat. Comput. Sci. | PropMolFlow: 基于几何完备流匹配的性质引导分子生成框架
author: 
published_at: 
fetched_at: 2026-04-25T02:03:48Z
extractor: wechat_worker
content_hash: f632603ed093b29150a040891870476231ffe61fda7d30e3dfba4a35047c7dfb
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/jwaic6a7a9gMjd4u5LhO9u7pZ0Wy3ia8bRrRTXjapkgS5H4XKicFywwnLoKTZVzZ3UkibNdQfIMPAmXktGTyu8fZqQ/0.jpg) 

# Nat. Comput. Sci. | PropMolFlow: 基于几何完备流匹配的性质引导分子生成框架

[ MindDance ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

以下文章来源于DrugOne ，作者DrugOne 

[ ![](http://wx.qlogo.cn/mmhead/7j1UQofaR9cqU7ONamCnROjFO8vQorSibm6t1GJ98PG0CBpljj64PBw5xR0so3BxaajBkoH8Yka8/0) **DrugOne** . 聚焦医药动态和前沿。关注医药行业新闻事件，IPO动态和人工智能在药学、化学、生物、生命科学与医学中的融合应用。致力于连接科研、产业与临床，助力新一代科研人员与转化推动者。 ](#) 

DRUGONE

分子生成模型正在快速推动化学发现与药物设计的发展。近年来，流匹配模型(flow matching)在无条件分子生成任务中已达到领先水平，但在性质引导生成(property-guided generation)方面仍主要由扩散模型占优。

  
研究人员提出 PropMolFlow，一种基于几何完备 SE(3) 等变流匹配的性质引导分子生成框架。该方法通过整合多种性质嵌入策略，并引入高斯展开机制对标量物性进行结构化编码，实现对分子结构、原子类型、电荷、键级和三维几何的联合生成。在QM9数据集上的系统评估表明，PropMolFlow在性质对齐精度、结构稳定性与化学有效性方面达到与现有最优扩散模型相当甚至更优的性能，同时显著提升采样效率，在更少时间步数下实现更快生成速度。研究人员进一步通过密度泛函理论(DFT)计算对生成分子的性质进行物理验证，并提出分布外(OOD)生成任务，评估模型在稀有性质区域的泛化能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gMjd4u5LhO9u7pZ0Wy3ia8bRGkQSz2s1vdxIAcFTf7nNqswjr5DIzZk4uh78DwuOAXMFC5gEnbeqBQ/640.png)

深度生成模型为化学发现提供了一种通过统计采样分子结构、降低高昂物理模拟成本的路径。当前主流三维分子生成方法主要依赖等变图神经网络驱动的扩散模型，在几何建模上表现优异。

  
相比之下，流匹配方法作为新兴范式，在材料、蛋白质和小分子生成任务中展现出更高的采样效率和路径灵活性。然而，在性质引导生成场景下仍存在多重挑战，包括：

* 离散化学特征（原子类型、电荷、键级）的表达失真；
* 手性与几何完整性难以统一建模；
* 性质嵌入方式缺乏系统性设计；
* 生成结果缺乏物理层面的独立验证；
* 模型泛化能力主要局限于训练分布内任务。

研究人员认识到，要实现高可信度的性质可控分子设计，需要在几何完备建模、离散变量建模、性质嵌入机制和物理验证体系之间建立统一框架。

  
**方法**

PropMolFlow 基于 FlowMol 架构构建，以几何完备 SE(3) 等变流匹配过程为核心，将分子表示为包含原子类型、电荷、键级和三维坐标的全连接图结构。模型通过联合流匹配过程，同时生成所有分子模态信息。

在性质引导方面，研究人员将标量分子性质映射为高维性质嵌入向量，并设计多种嵌入交互方式（拼接、求和、乘法及其组合），实现性质信息与分子节点特征的深度耦合。同时引入非可训练高斯展开层，将连续性质值转化为局部响应分布，从而增强模型对性质变化的表达能力。最终模型在统一框架下实现几何一致、结构稳定、性质可控的分子生成。

  
**结果**

**模型框架与生成机制概览**

PropMolFlow 在统一流匹配框架中联合建模原子类型、电荷、键级与三维几何结构，通过性质嵌入调控分子生成方向，实现结构与物性的协同生成。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gMjd4u5LhO9u7pZ0Wy3ia8bR4ZRqyO9puWO0xibYqvUUpm6kXuXib5ofckTRWjyax6a00hpP0G1axe0g/640.png)

图 1｜PropMolFlow 方法总体框架。

  
**性质引导生成性能评估（ID任务）**

在训练分布内任务中，PropMolFlow 在多个物性指标（极化率、HOMO–LUMO 间隙、偶极矩、热容等）上实现与最优扩散模型相当或更优的平均绝对误差（MAE）表现。

系统分析表明，性质嵌入策略与高斯展开机制对模型性能影响显著，不同嵌入方式可导致超过 40% 的性能差异，验证了系统化设计的重要性。

  
**结构稳定性与生成效率**

PropMolFlow 在多项结构有效性指标上持续优于对比模型，包括：

* 原子价稳定性；
* 分子整体稳定性；
* RDKit 化学有效性；
* 闭壳层比例；
* 结构合理性约束指标。

在采样效率方面，由于流匹配路径更短且为确定性过程，PropMolFlow 仅需约 100 个时间步，相比扩散模型的 1,000 步实现 ≥8 倍加速，同时保持高结构保真度。

  
**物理一致性验证（DFT 校验）**

研究人员对生成分子进行大规模 DFT 计算验证，比较目标性质、模型预测值与物理计算结果的一致性。结果表明：

* 生成分子在物理层面保持合理性；
* 性质预测存在可量化系统偏差，但统计一致性良好；
* 结构松弛后性质更贴近真实物理分布。

该过程证明模型不仅在数据分布层面有效，同时在物理化学层面具有可信度。

  
**分布外（OOD）性质生成能力**

研究人员构建了 OOD 任务，以训练集中罕见的高分位性质值作为目标进行生成。结果显示：

* 生成分子性质分布整体向目标区域偏移；
* 模型可探索训练分布外结构空间；
* 生成分子在 PubChem 等大规模数据库中具有显著新颖性；
* 相似度分析表明多数分子不属于训练集重复样本。

证明 PropMolFlow 具备一定程度的外推泛化能力。

  
**讨论**

PropMolFlow 展示了一种将几何完备建模、流匹配生成与性质引导控制统一于单一框架的分子生成范式。该模型不仅实现了高效采样与结构稳定性，还在物性对齐与物理一致性验证方面建立了系统流程。

  
研究人员指出，未来改进方向包括：

* 引入主动学习 / 强化学习机制提升 OOD 泛化能力；
* 扩展至更大规模分子体系与更复杂性质空间；
* 融合能量函数与构象稳定性约束；
* 构建多性质联合调控机制；
* 探索一步式流映射以进一步提升生成效率。

总体而言，PropMolFlow 为AI 驱动分子设计提供了一个在几何一致性、性质可控性与计算效率之间高度平衡的基础框架，为后续智能分子发现系统奠定了方法学基础。

整理 | DrugOne团队

  
**参考资料**

  
Zeng, C., Jin, J., Ambrose, C. et al. PropMolFlow: property-guided molecule generation with geometry-complete flow matching. Nat Comput Sci (2026). 

https://doi.org/10.1038/s43588-025-00946-y

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/mS8qdZ3O8bgdeoYb8GbWMEQtibvyWMWd4ibMHwnXR3p2ib7OFjXc5270g3H1H58WIiclWBQibtJZHIUtWBGcl2czITw/640.gif)

**内容为【DrugOne】公众号原创**｜转载请注明来源

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/iaFJFs8iaTrACosrVo3d1bPiaPqYACC7s1g9ZfZr6QmAKQXNtSlKFBUriaHypMWJ72tWS7HdYgicGYMxD3ibJnNiaVcOQ/0.png) 

 MindDance 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/iaFJFs8iaTrACosrVo3d1bPiaPqYACC7s1g9ZfZr6QmAKQXNtSlKFBUriaHypMWJ72tWS7HdYgicGYMxD3ibJnNiaVcOQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
