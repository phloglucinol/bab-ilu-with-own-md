---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247488969&idx=1&sn=aa1b3f5855744a540049f18459898afc
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247488969&idx=1&sn=aa1b3f5855744a540049f18459898afc
source_domain: mp.weixin.qq.com
title: 【佳作推荐】 加州大学伯克利分校Bingqing Cheng小组NC论文：从能量和力中学习电荷与长程相互作用的机器学习方法
author: 
published_at: 
fetched_at: 2026-04-25T02:04:27Z
extractor: wechat_worker
content_hash: 3b1a4cd231cae5faa7fc9a9d7f744f645ff7e74f529ab594da16ca2ecb3a5902
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EdJbpQuVdV9V4ttHic8xS79EWrRrkNrKphf4JdWOjFcpByq1bflvFrCuN7qWY0iaiclftACvf48L93xw/0.jpg) 

# 【佳作推荐】 加州大学伯克利分校Bingqing Cheng小组NC论文：从能量和力中学习电荷与长程相互作用的机器学习方法

原创 ComputArt ComputArt [ ComputArt计算有乐趣 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EdJbpQuVdV9V4ttHic8xS79EicrBseKKxictOj3t7q7AhO5Fbhiar0OMdEatQIvU8SIe2upYyuTJBwgsg/640.png)

在原子尺度模拟中，长程相互作用的精确描述是理解材料与化学体系性质的核心。传统机器学习势能大多基于短程近似，难以准确刻画电解质、带电分子等依赖静电与色散作用的体系，这成为其应用的主要瓶颈。为突破此限制，现有方案通常引入由密度泛函理论导出的原子电荷，或采用电荷平衡策略。然而，原子电荷本身并非物理可观测量，其数值强烈依赖于人为选择的电荷划分方法。这种定义上的模糊性，成为提升机器学习势能的关键挑战。

加州大学伯克利分校和奥地利科学技术研究院的Bingqing Cheng小组针对这一问题，引入了一种名为“Latent Ewald Summation(LES)”的方法。该框架直接从能量和力中学习长程相互作用，无需显式的电荷标签或额外输入。该方法具备高度的通用性，可与多种主流的机器学习势能架构相结合。近日，该项研究工作发表在Nature Communications期刊上。

Latent Ewald Summation（LES）框架的构建基于一个核心的物理思想，即通过对体系总势能进行范围分离，将其明确分解为短程与长程两部分。短程部分由标准的机器学习势能处理，它依赖于原子的局部化学环境描述符；而长程部分的创新之处在于引入了一个称为“隐式电荷”的变量。这些隐式电荷并非来自先验的电荷定义，而是通过一个神经网络从局部原子特征中直接映射得到。随后，这些学习到的隐式电荷被代入经典的Ewald求和中，用于计算系统的全局长程静电相互作用。该框架的训练范式严格遵循端到端的学习原则，其显著特点是仅使用量子力学计算提供的总能量和原子力作为监督信号，而完全不需要任何显式的原子电荷标签。

LES框架具备高度的通用性与可解释性。它是一个模块化设计，其短程部分可以与多种主流的机器学习势能架构结合，如原子簇扩展或消息传递神经网络，从而广泛适用于各类体系。尽管不依赖电荷标签，但学习到的隐式电荷展现出明确的物理意义。在已知精确电荷的经典点电荷体系中，LES能精确复原其值。在量子力学体系中，这些电荷能成功预测出偶极矩、四极矩乃至玻恩有效电荷等严格的物理可观测量。计算上，通过代码优化，LES在保持物理严谨性的同时，仅引入了微小的计算开销，能够高效地应用于大规模分子动力学模拟，为解决电化学界面、离子液体和生物分子等复杂体系中的长程相互作用提供了一个强大而精准的工具。

测试首先使用经典带电系统。如图-1所示，在由64个带+1e和64个带-1e电荷的点电荷构成的气体系统中，LES能够准确地学习并恢复正确的原子电荷。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EdJbpQuVdV9V4ttHic8xS79EYrniawfrX7swdfJywgKNia6zvw5rAQUYMqqAoqtnJpFyUAqG4icc88l7g/640.png)

**图1：经典带电体系的电荷与力的预测结果。**

在电解质溶液体系中，研究人员对KF水溶液进行测试。模型在数百个训练样本后同样能够恢复真实的离子电荷，并表现出比短程模型更高的学习效率。这表明该长程模型能够学习涉及不同物种和介电屏蔽效应的系统。

在量子力学系统中，原子电荷没有明确的物理定义。研究发现，仅通过能量和力训练的LES模型，其预测的潜电荷能够用于推断偶极和四极矩等物理可观测量。如图-2所示，在对SPICE数据集的极性二肽数据测试中，由LES电荷计算出的分子偶极矩与DFT的参考值高度吻合（R2=0.991），同时在预测四极矩（R2=0.911）和玻恩有效电荷（BEC）张量方面也表现出良好的一致性。这表明，无需对任何电荷或偶极矩信息进行显式训练，LES框架也能以较高精度模拟分子电荷密度的可观测量。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EdJbpQuVdV9V4ttHic8xS79EPwY3xHTC5tAJ6BFDiaCE6bUaltsUetibe8mMalibTuWEtykdmM7iav3LDg/640.png)

**图2：模型在二肽测试集上的物理可观测量结果。**

研究团队在四个专门针对不同电荷态或具有显著长程电荷转移的系统上对LES方法的性能进行了评估。如表1所示，仅使用能量和原子力作为训练目标的LES长程模型（CACE‑LR），在能量与力的预测精度上优于多种需要显式学习原子电荷的先进方法。例如，在Au2-MgO系统上，CACE‑LR模型的预测误差比其它对比方法降低了约一个数量级。研究指出，这一优势源于LES所捕捉的“响应电荷”在物理意义上的根本不同。传统方法所学习的DFT原子电荷强烈依赖于人为选择的电子密度划分方案，其数值本身存在模糊性，而LES中的隐式电荷则是以端到端的方式，从能量和力的数据中反演得到。

表1：LES方法（CACE-LR）在四个具有不同电荷状态和电荷转移的数据集上表现最优。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EdJbpQuVdV9V4ttHic8xS79EiagV0U4qWroRDsFF1MaxjxLhUTQGWn0k0iaUiaZicQV0ZcSOmf0SXHaRUw/640.png)

研究人员还将LES应用于电解质/固体界面和固-固界面。在Pt(Ⅲ)/KF(aq)和TiO2/NaCl(aq)界面系统中，CACE-LR模型相比于其他长程模型取得了更高的精度。最后，在LiCl/GaF₃固-固异质界面的案例中，LES框架卓越的外推预测能力与不确定性量化优势得到了充分体现。面对一个远超训练集尺寸的分布外测试结构，仅基于短程近似的模型其原子力误差高达116.3 meV/Å，而引入长程相互作用的LES模型则将误差显著降低至40.5 meV/Å。同时，如图-3所示，短程模型对其自身在界面区域产生的巨大预测误差未能提供有效预警，LES模型则成功地在此区域标识出更高的不确定性。这一结果不仅证实了短程模型在刻画涉及长程静电作用的周期性界面结构时存在本质局限，也凸显了LES框架在应对此类复杂体系时，兼具更高的预测精度和更强的泛化能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EdJbpQuVdV9V4ttHic8xS79ERQuibTK5iaeRFia3JCfdvXMlQhNvibhwg4lgxdcDFnEEw0tkuU3Ukjic5RA/640.png)

图3：SR(上)和LR(下)模型的预测力误差(左图)和不确定性估计(右图)。

**小编总结**

该研究系统阐述了Latent Ewald Summation (LES) 框架的理论基础、扩展潜力与应用前景。其核心在于将体系的总势能明确分解为短程与长程两部分：短程部分由各原子的局部环境能量叠加而成；而长程部分则创新性地引入一个由局部特征映射得到的“潜电荷”变量，该变量通过一个多层感知机自动学习获得，无需任何先验的电荷定义。研究表明，与明确学习DFT部分电荷的方法相比，LES在能量和力的预测中能达到更高精度。对于具有固定电荷的经典系统，LES能够重现这些精确电荷；对于量子力学系统，LES能够推断出偶极矩、四极矩等物理可观测量。该框架为一系列复杂体系的长程相互作用建模提供了强大而精准的工具，适用于电解质界面、带电分子复合物及离子溶液等传统方法难以精准描述的场景。

**参考文献**

\[1\] King, D. S., Kim, D., Zhong, P. & Cheng, B. Machine learning of charges and long-range interactions from energies and forces. Nature Communications 16, 8763 (2025). https://doi.org/10.1038/s41467-025-63852-x

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IBYsyRibb4EcibThuywhbNciciaiauxu6DUhtp75nQZnrPxniaYia0RMN9XgXMVCiaqEOxkU4EjMoIsmD98kDTcLz5NC3w/0.png) 

 ComputArt计算有乐趣 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IBYsyRibb4EcibThuywhbNciciaiauxu6DUhtp75nQZnrPxniaYia0RMN9XgXMVCiaqEOxkU4EjMoIsmD98kDTcLz5NC3w/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
