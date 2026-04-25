---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzU2ODU3Mzc4Nw%3D%3D&mid=2247513112&idx=1&sn=93ef71b554af5df4fef01ad2ae48bd68
canonical_url: https://mp.weixin.qq.com/s?__biz=MzU2ODU3Mzc4Nw%3D%3D&mid=2247513112&idx=1&sn=93ef71b554af5df4fef01ad2ae48bd68
source_domain: mp.weixin.qq.com
title: 字节跳动AI制药团队发布AnewSampling | 打破AlphaFold3静态结构局限，精准捕捉复合物动态结合过程
author: 
published_at: 
fetched_at: 2026-04-25T02:03:22Z
extractor: wechat_worker
content_hash: 497bed564fc83e2cdf56f706debe962a7a1e487eab326e971683fc3acdb2bae0
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/yvQQqODtVt4Qx4X5PaUQ2hlzHSpMiav3nexCv3ysrIKtn8rPTju8qzAX5sbRMdcfeySxckN4GyK7RqkVg6ozBHgWia8eEiayt6gFvvqiaqF1Ir0/0.jpg) 

# 字节跳动AI制药团队发布AnewSampling | 打破AlphaFold3静态结构局限，精准捕捉复合物动态结合过程

DrugAI DrugAI [ DrugAI ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

**导言**

在过去几年中，AI彻底改变了蛋白质结构预测的能力，从序列到结构的预测精度达到前所未有的高度。然而，对于真实的药物发现和对应分子体系而言，单一的静态结构远远不够。

  
蛋白与配体的结合本质是一个动态过程：构象不断变化，能量状态持续交换，关键相互作用在不同时间尺度上形成与消失。理解动态热力学景观，一直是药物发现中的核心挑战。

  
近日，字节跳动AI制药团队发表的一篇技术报告显示，其发布的 AnewSampling 模型已经可以实现蛋白-配体复合物的系统性动态平衡采样。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt6OA9O5Piacd1pA4YLYfoNxpRokib67QhAew0msP80gEr67qvLRBgmg9ZibKnuW6icicXcOVslwOFY7j09WREXiahmL95iadQEmntJ8RI/640.png)

  
这一研究成果意味着，AI驱动药物发现已不再只停留在预测单一静态结构。通过将生成式 AI 引入全原子热力学采样，能够高效地生成接近分子动力学参考结果的构象集合。AI驱动药物发现有望打破静态结构局限，精准捕捉复合物动态结合过程。

  
**真实分子世界，从来不是静态结构**

如果说静态结构预测像是为蛋白-配体拍摄了一张高分辨率照片，那么真实的分子体系更像是一段持续演化的电影。

  
如今，越来越多研究者在面对挑战性靶点时开始意识到：仅仅依靠预测静态结构，已经不足以理解分子体系。因为在真实的药物发现过程中，决定药物效果的往往不是单一的结合姿势，而是一整片构象分布及其背后的热力学平衡状态。AnewSampling 让 AI 从“预测一个结构”，进化为生成一整片动态构象景观。

  
AlphaFold 让 AI 看见了结构，AnewSampling 让 AI 学会复合物的运动规律。

  
**将昂贵的模拟，推向可规模化应用**

对于基于结构的药物设计，尤其是 lead optimization 阶段，真正有价值的信息包括但不限于：

* 配体在结合口袋中的结合方式
* 关键侧链和药效结构的耦合运动
* 稀有但产生功能影响的低频状态
* 影响稳定性、选择性和活性的动态相互作用网络

这些恰恰是传统静态模型最难给出的信息，也是经典分子动力学（MD）虽然能提供、却难以大规模供给的部分。AnewSampling 让这些过去 “高成本才能看到” 的动态信号，有机会进入每个项目的日常研发决策流程。对药物研发团队来说，这意味着：

* 更快：以远低于传统 MD 的时间成本完成平衡采样。
* 更广：不依赖针对单一靶点反复重训练，可跨蛋白家族和配体化学空间进行泛化。
* 更深：不只给一个答案，而是给出一个构象集合，帮助发现关键且隐蔽的功能状态。

  
AnewSampling 不只是把动态建模做快了一点，而是尝试使用可规模化的AI模型取代长期依赖高成本物理模拟的核心环节。这意味着新的变革正在出现：AI 不再局限于预测复合物结构长什么样，而是能够学习分子为什么这样运动、会稳定在哪些状态、又会如何在多个状态之间切换。

  
这种从静态结构到动态分布、从单一构象到热力学集合的跨越，可能成为AI制药走向下一阶段的关键拐点。

  
**严谨验证之下，多维展现革新能力**

从结果来看，AnewSampling 在内部自建测试集、公开的 JACS and Merck 基准测试集，以及大规模蛋白动态数据集 ATLAS上，均展现出强劲表现。它生成的蛋白单体与蛋白 - 配体构象集合，与参考 MD 模拟保持了高度一致性，显示出对未知靶点、不同配体化学类型和不同评估设置的稳定泛化能力。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt4ZWdD8ibwbWaOFcXGLRJmjGKAgdNnU2pkNQarW5EDgyANkPGn2SWgax8icmiaxibyyIp1LfibO8onBwUDOBKyibicd5tSOQWDDjov3FY/640.png)

图1：对 ATLAS 蛋白单体测试集的评估，AnewSampling 在生成单体蛋白质构象集合方面与当前最先进的基线模型性能比较。AnewSampling 在所有评价指标均达到当前最佳性能。

  
更值得关注的是，在真实药物研发的问题上，AnewSampling 展现出的优势并不只是 “生成得像”，而是能够恢复那些真正决定研发判断的动态信号。

  
在药物发现关键性指标，如：配体扭转角分布、蛋白 - 配体相互作用网络和蛋白柔性变化的评估中，AnewSampling 相比现有生成模型表现出显著优势，同时与 MD 参考保持高度一致性。这说明它学到的并非表面几何相似性，而是更接近热力学意义上的有效分布。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt5LreBxxwhagv3rXXRpWic0EmN3IE9Q7SJsq6SYMLoSLibXFF8gp0MRLtMwfibBCRbm8ibyVNNo14jWSbUxdlCg1BT9Rgq2InZx8h4/640.png)

图2：在蛋白-配体测试集的评估中，评估多个模型的Jensen-Shannon (JS) 距离指标，Wasserstein (WS)距离指标，和均方误差 (RMSE) 指标。AnewSampling 展现出稳定优势表现，并在成功率指标（JS distance ≤ 0.3、WS distance ≤ 0.3、Spearman correlation ≥ 0.85）上显示出与MD相近的结果。

  
在进一步使用 JACS and Merck 数据集分析蛋白 - 配体构象全景生成能力时，AnewSampling 的蛋白 - 配体构象生成成功率显著优于现有静态结构预测与动态结构预测模型，并且与 MD 结果保持高度相关。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yvQQqODtVt5MkiaHRVWnTz40VRWOiaXicQMheR0D33KNynH5QOOPgjj6862kVB3tUDUR9Pu2YczYnS1narD1rRh3BkyDsOLQCPbsMHTRWpiaYwI/640.png)

图3：使用 JACS and Merck 数据集进一步分析蛋白-配体构象全景生成能力。图a结果显示AnewSampling在蛋白-配体构象生成的成功率显著优于现有静态结构预测和动态结构预测模型，且能够保持和MD结果的高度相关性。图b使用CDK2 配体示例展示了苯环取代而形成的蛋白质-配体氢键增益，比较了 MD（蓝色）和 AnewSampling（红色）组在 WS 距离上的差异。

  
真正能拉开差距的，往往不是简单体系，而是那些传统方法也难以充分解决的难题。在富有挑战性的 CDK2 研究中，AnewSampling 捕捉到了多样性的结合模式以及配体与侧链协同运动的复杂现象，而这些状态，在标准模拟预算下的常规 MD 中，往往难以被充分覆盖。

  
AnewSampling 在该案例上的表现部分接近增强采样方法 Replica-Exchange MD（REMD）所能达到的效果。这意味着，过去需要更高计算成本才能触及的功能关键状态，现在可以使用AnewSampling实现高效探索。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt5L4DkMcmZsSXgzS6yeeXzfiamHvpHz0FPJQ9SP95rpvE42LplfRSicvnVdibJH1MrA6L1rRTu7Eog0JiaGDjlvzwujCq1mG6Qr3uQ/640.png)

图4：通过分析CDK2复合物的增强采样构象，AnewSampling 展示出能够捕捉到 REMD 轨迹中观察到的多种分布的潜力（蓝色）。在 PDB ID: 1H1S 的案例分析中，AnewSampling（粉色）能够捕捉到 REMD 轨迹中观察到的关键瞬时氢键（蓝色）。

  
**面向未来，动态感知的 AI 药物设计新机遇**

尽管成果令人瞩目，论文也分析了当前框架的几项局限。目前，高质量动态训练数据的稀缺仍是制约模型扩展的主要瓶颈。同时，模型在处理复杂复合物时仍较依赖初始模板，仅依赖一级序列的高精度分布预测仍有提升空间。此外，由于当前框架主要在单一固定的热力学环境下学习分布，尚不能完全替代传统分子动力学在不同宏观条件下的灵活模拟。

  
这些局限也为未来的优化指明了方向。通过扩充数据与扩大规模，模型有望实现真正的热力学完备性与无模板预测。更重要的是，AnewSampling 展现出了与传统物理模拟的高度互补，能够为后者提供多样化的初始构象，从而高效跨越极高的能量势垒。

  
AnewSampling 的出现，标志着 AI 正迈出关键一步，从“结构预测”走向“动态分子理解”。如果说过去的 AI 帮助我们看到分子的形状，那么下一代 AI 将开始理解分子如何运动、如何演化，以及这些动态过程如何决定功能与成药性。通过在速度、规模与物理可信度之间建立新的平衡，AnewSampling 为探索蛋白-配体相互作用景观提供了一种全新的技术基础，并为未来更广泛的药物研发应用打开了空间。

参考资料

Learning the All-Atom Equilibrium Distribution of Biomolecular Interactions at Scale, Yusong Wang, Youjun Xu, Wentao Li, Haoyu Yu, Wenjuan Tan, Shaoning Li, Qiaojing Huang, Nanjun Chen, Xuan Wu, Qilong Wu, Kai Liu, bioRxiv 2026.03.10.710952

 doi: https://doi.org/10.64898/2026.03.10.710952

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/P4UadRgibwicbuY1KHAu0TsZh33ofJ5NbQGOgUj2JxH8cib6UvRl5wwucN58lfh65N29mHNraHyOia43ChPcraLRqQ/0.png) 

 DrugAI 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/P4UadRgibwicbuY1KHAu0TsZh33ofJ5NbQGOgUj2JxH8cib6UvRl5wwucN58lfh65N29mHNraHyOia43ChPcraLRqQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
