---
type: raw_article
source_url: https://mp.weixin.qq.com/s/mZkB7W8oww6rbtWPs_OavA
canonical_url: https://mp.weixin.qq.com/s/mZkB7W8oww6rbtWPs_OavA
source_domain: mp.weixin.qq.com
title: JACS | SO3LR：一种结合预训练神经网络与通用力场的分子模拟方法
author: 
published_at: 
fetched_at: 2026-04-25T02:04:23Z
extractor: wechat_worker
content_hash: eec8dd9fdc573eba7b33dbf45a291815b9ddd204b8a3a78e67e018e08786355f
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/3a2JCUU90QU83t7eMYuYFKdmIYCwz2KHOGdN6iccWRibAAicT3Z8MFdia1aczO74HXoz9zomsKpWjZNT8fERIAOrQw/0.jpg) 

# JACS | SO3LR：一种结合预训练神经网络与通用力场的分子模拟方法

原创 Yiquan Wang Yiquan Wang [ biomath ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

> Kabylda, A., Frank, J. T., Suárez-Dou, S., Khabibrakhmanov, A., Medrano Sandonas, L., Unke, O. T., ... & Tkatchenko, A. (2025). Molecular simulations with a pretrained neural network and universal pairwise force fields. _Journal of the American Chemical Society_, _147_(37), 33723-33734.

> https://pubs.acs.org/doi/10.1021/jacs.5c09558

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3a2JCUU90QU83t7eMYuYFKdmIYCwz2KHwQ4fkLiaErETjfTZEDMC8zjl6e9cfOTmu4jxz3n5BdIDXcL4cCPIpZA/640.png)

## Abstracts

机器学习力（MLFFs）有望实现通用的分子模拟，能够同时为多样的分子、材料和混合界面实现效率、准确性、可移植性和可扩展性。朝着这个目标迈出的关键一步是GEMS方法在生物分子动力学中的应用\[Unke et al., Sci. Adv. 2024, 10, eadn4397\]。本工作介绍了SO3LR方法，该方法将快速且稳定的SO3krates神经网络用于半局域相互作用，并结合了为短程排斥、长程静电和色散相互作用设计的通用成对力场。SO3LR在包含400万个中性和带电分子复合物的多样化数据集上进行训练，这些数据在PBE0+MBD量子力学水平上计算，确保了对共价和非共价相互作用的广泛覆盖。我们的方法以计算和数据效率、在单个GPU上可扩展至20万个原子以及在有机（生物）分子化学空间中具有合理到高精度的特点为标志。SO3LR被应用于研究四种主要生物分子类型的单元、多肽折叠以及更大系统（如蛋白质、糖蛋白和脂质双分子层）在显式溶剂中的纳秒级动力学。最后，我们通过将MLFFs与传统原子模型相结合，讨论了实现真正通用分子模拟的未来挑战。

## 一.科学问题

长期以来，分子动力学（MD）模拟领域一直追求一个宏伟目标：仅根据原子核电荷和电子数，就能进行精确的定量模拟。然而，现有的方法往往需要在**效率（Efficiency）、准确性（Accuracy）、可扩展性（Scalability）和可移植性（Transferability）**（简称**EAST**）这四个关键维度上做出妥协。传统的力场要么依赖于快速但近似的力学表达式，牺牲了准确性；要么基于精确但计算成本高昂的从头算电子结构计算，牺牲了效率。这极大地限制了可研究问题的范围和规模。近年来，机器学习力场（MLFFs）展现了弥合这一差距的巨大潜力，但如何构建一个能够同时满足EAST四大要求，并能广泛应用于从有机小分子到大型生物分子体系的通用模型，仍然是一个巨大的挑战。本研究旨在通过**结合先进的机器学习架构与基础物理原理**，开发一个能够在庞大且多样的化学空间中保持高精度和高效率的通用力场，从而推动分子模拟进入一个全新的时代。

### 二.图片解释

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3a2JCUU90QU83t7eMYuYFKdmIYCwz2KHgk0NSibOialV9W2rvkt5szZmiasyMFkCGL59uCK7HpX1FOyFMds1o6ibwg/640.png)

#### **图1：SO3LR模型及其模拟结果概览**

这张图全面展示了SO3LR模型的架构和其强大的应用能力。

* **(A) SO3LR框架**: 该模型的核心是一个混合框架。它将高效的**SO3krates神经网络**用于描述复杂的半局域多体相互作用，同时显式地加入了三个基于物理原理的成对相互作用项：用于短程的**ZBL核排斥**、用于长程的**静电相互作用**以及一个新颖的**通用范德华色散势**。这四大模块在一个包含**400万**个分子的庞大数据集上进行联合训练，该数据集覆盖了蛋白质、碳水化合物、脂质和核酸等关键生物分子片段，确保了模型的广泛适用性。
* **(B) 模拟应用**: 该图展示了SO3LR在多个尺度上的成功应用。它不仅能精确模拟小的生物分子单元，还能对包含数万个原子的大型复杂体系进行**纳秒级的动力学模拟**，例如液态水、Crambin蛋白、N-连接糖蛋白以及POPC脂质双分子层，并能准确预测径向分布函数（RDF）、红外光谱（IR Spectra）和均方根偏差（RMSD）等重要物理化学性质。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3a2JCUU90QU83t7eMYuYFKdmIYCwz2KHKZKfvIO2Tcl8OQ8Wu3TucBqsckL2u0Y1P3sfWx2JaibKCmUjv5yur6Q/640.png)

#### **图2：SO3LR长程相互作用模块性能评估**

此图验证了模型对长程静电和非共价相互作用的预测精度。

* **(A) 偶极矩预测**: 在包含7211个分子的**QM7b**测试集和包含52个多样化物种的**AlphaML**测试集上，SO3LR预测的偶极矩与高精度量子化学计算结果高度一致。平均绝对误差（MAE）分别仅为**0.13 D**和**0.14 D**，这一精度可与昂贵的杂化密度泛函理论（如B3LYP）相媲美，证明了其静电模型的高度可靠性。
* **(B) 结合能预测**: 在包含近万个中性和带电分子复合物的**SAPT10k**基准测试集上，SO3LR表现出色。对于中性体系，MAE为**0.82 kcal/mol**；对于更具挑战性的带电体系，MAE为**1.46 kcal/mol**。整体MAE达到了**0.90 kcal/mol**的亚化学精度水平，这表明模型能准确捕捉由色散和静电主导的复杂非共价相互作用。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3a2JCUU90QU83t7eMYuYFKdmIYCwz2KHsFssIMNHbq0iaMkrFDMu0WbMxicj3ThXAJ5m04iam6w1R9APcpLxRN6Sg/640.png)

#### **图3：小型生物分子片段的模拟**

该图通过Ramachandran图展示了SO3LR在模拟小分子构象动力学方面的准确性。

* **(A) AcAla₃NMe四肽** 和 **(B) 水苏糖四糖**: 在**500 K**的高温下，SO3LR对这两个分子的动力学模拟所探索的二面角（φ/ψ）构象空间，与从头算分子动力学（PBE+MBD）的参考结果在视觉上高度吻合。这表明SO3LR能够准确地再现分子的柔性和构象偏好，即使这些分子代表了不同的生物分子类别（蛋白质和碳水化合物）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3a2JCUU90QU83t7eMYuYFKdmIYCwz2KHPmW9XMIQ0T3RhunjVia6Xxcup3Qa0yMlaagrSKNZQfxtDEYVBEwNDHg/640.png)

#### **图4：聚丙氨酸体系的模拟**

此图展示了SO3LR在模拟多肽折叠和稳定性方面的能力，这是一个评估力场平衡各种相互作用的经典难题。

* **(A) AcAla₁₅NMe的折叠**: 从一个完全伸展的线圈结构出发，在**300 K**下，SO3LR能够在**500 ps**内成功模拟其折叠过程。轨迹分析显示，多肽经历了从**转角（turn）\*_到\*_波浪状中间体**，最终形成了稳定的**α-螺旋**和**3₁₀-螺旋**动态共存的结构。这与实验观察和其他高精度模拟结果一致，证明了模型能准确描述氢键、色散和极化之间的精细平衡。
* **(B) AcAla₁₅LysH⁺的稳定性**: 对于带正电荷的α-螺旋多肽，模型显示其在**500 K**高温下仍能保持稳定的螺旋结构，这与实验中观察到的其高达**\~725 K**的热稳定性相符，进一步验证了模型的可靠性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3a2JCUU90QU83t7eMYuYFKdmIYCwz2KHicoUVp2zJKG5AiagiaBR8tDiaXic0icdXq5b1bdPRLLEVPmAWDW5JEG0cEcA/640.png)

#### **图5：显式溶剂中大型生物分子的模拟与性能**

这组图集中展示了SO3LR在模拟真实生物大分子体系方面的可扩展性、准确性和计算效率。

* **(A-C) Crambin蛋白（\~2.5万原子）**: 模拟得到的功率谱**（A）**与实验测量的水分子振动峰（\*_1640 cm⁻¹\*_和**3200-3600 cm⁻¹**）吻合良好，优于多种经典力场。RMSD分析**（B）**和UMAP降维投影**（C）**表明，SO3LR能比传统力场更广泛地探索蛋白质的构象空间，与NMR实验揭示的高度构象变异性一致，同时保持了蛋白质的折叠状态。
* **(D) 糖蛋白（\~4.8万原子）**: 即使训练集中没有碳水化合物，SO3LR也能正确推断出糖链部分比蛋白质部分具有更高的柔性（更大的RMSD），展示了模型的优异泛化能力。
* **(E) POPC脂质双分子层（\~3.3万原子）**: 模拟得到的脂质尾链NMR序参数与实验数据高度吻合，证明模型能准确再现膜的结构和动力学特性。
* **(F) 单GPU性能**: 性能测试显示，SO3LR的计算耗时与体系原子数呈线性关系，在单个NVIDIA H100 GPU上，其延迟仅为**3.25 μs/原子/步**。这意味着对于一个**1万个原子**的体系，每天可以模拟**2.6纳秒**，使其能够进行有意义的生物过程模拟。

## 三.总结分析

本研究成功开发了**SO3LR模型**，一个**兼具量子力学精度和经典力场效率**的通用机器学习力场。该模型的核心创新在于将**数据驱动的SO3krates神经网络**（用于学习复杂的半局域多体效应）与**基于物理原理的通用成对势**（用于描述短程排斥和长程静电/色散作用）无缝结合。

**关键亮点包括**：

1. **全面的数据基础**：SO3LR在一个包含**400万个分子构象**的庞大、多样化的量子力学数据集（PBE0+MBD水平）上进行了训练，覆盖了H, C, N, O, F, P, S, Cl等生物系统中常见的8种元素，为其卓越的**可移植性**奠定了坚实基础。
2. **卓越的精度与泛化性**：在偶极矩、非共价相互作用能等多个基准测试中，SO3LR均达到了与高水平量子化学方法相媲美的精度（例如，SAPT10k结合能MAE仅为**0.90 kcal/mol**）。更重要的是，它能成功模拟训练集中未包含的体系，如糖蛋白和脂质双分子层，并得到与实验一致的结果。
3. **强大的模拟能力**：从模拟小型多肽的自发折叠，到在显式溶剂中对包含**数万个原子**的蛋白质、糖蛋白和脂质膜进行**纳秒级**的稳定动力学模拟，SO3LR展示了其处理真实复杂生物体系的强大能力。
4. **优异的计算性能**：该模型实现了前所未有的**可扩展性**，可在单个GPU上高效模拟多达**20万个原子**的系统，其计算速度（**\~3.25 μs/原子/步**）使得曾经遥不可及的长时间、大规模量子精度模拟成为可能。

**总之，SO3LR模型及其开源框架为分子模拟领域提供了一个强大而通用的工具，极大地推动了我们向“无需为特定体系定制参数即可进行普适性量子精度模拟”这一终极目标迈进。** 这项工作不仅展示了机器学习与物理学知识结合的巨大威力，也为未来开发更强大、更通用的“基础模型”力场开辟了新的道路。

  
预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3a2JCUU90QUuTeYXCbOb7djufW3uD583EdiaKnptPJdVPhrrdrual3icaAra6FDM3ogSjeFA76MvDTehoM3c7x7A/0.png) 

 biomath 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3a2JCUU90QUuTeYXCbOb7djufW3uD583EdiaKnptPJdVPhrrdrual3icaAra6FDM3ogSjeFA76MvDTehoM3c7x7A/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
