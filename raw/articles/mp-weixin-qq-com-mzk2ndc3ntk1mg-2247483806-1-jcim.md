---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk2NDc3NTk1Mg%3D%3D&mid=2247483806&idx=1&sn=e10bbfd545ea35831cf3bae1066e20bb
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk2NDc3NTk1Mg%3D%3D&mid=2247483806&idx=1&sn=e10bbfd545ea35831cf3bae1066e20bb
source_domain: mp.weixin.qq.com
title: JCIM | 一种结合布朗动力学与分子动力学的多尺度模拟方法用于计算蛋白质-配体结合速率常数
author: 
published_at: 
fetched_at: 2026-04-25T02:03:27Z
extractor: wechat_worker
content_hash: e7806e06875ab34eb676c0a23f4667c4033a52b8c379e0551fef0aabc4dcb467
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/YFLnWDLn3VmewbbIS4QqRxymrTe5Y5f1OpumZsLBPyFricmtTnbf2rn9wlyIw94xhTicINkjxUjO67EjvbTSFMvDeVMq02BFuCPIjiad4ss9ag/0.jpg) 

# JCIM | 一种结合布朗动力学与分子动力学的多尺度模拟方法用于计算蛋白质-配体结合速率常数

凯算-生物 凯算-生物 [ 分子与生命 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9OicuUQbGCGQyUHDy9kDcnKb3WbOK9ZVCV4Vh2kIjNuGianwichUhDgbporUjZTe9OfOTb21VI0REaOutfmKwXooA/640.png)

文章标题：A Multiscale Simulation Approach to Compute Protein-Ligand Association Rate Constants by Combining Brownian Dynamics and Molecular Dynamics

期刊名称：Journal of Chemical Information and Modeling

DOI号：10.1021/acs.jcim.5c01488

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/YFLnWDLn3VnlhH1vAyt6wR4iamKOliaZc7kP2foRusef2cSv4aYxtRibD5tGnMGELGYPkKibiaVT8hD9BPD6jpYVWIa5w6DzcXabEUoUg7GsmNtE/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9OicuUQbGCGQyUHDy9kDcnKb3WbOK9ZVCVzx237hJKgmibQCBXmbmIXegic2dKrKyMSqic3uj9j6Mkj8Rz0zW6ibfog/640.png)

## **摘要**

药物与蛋白质结合的动力学参数（尤其是结合速率常数 kon）是衡量药效的关键指标，但其实验测定往往成本高昂且耗时。计算模拟方法需要在精度与计算可行性之间取得平衡。本文研究了一种结合布朗动力学（BD）与分子动力学（MD）的多尺度模拟方法。其中，BD用于模拟长程扩散以及形成扩散相遇复合物，而MD则用于模拟后续形成稳定结合复合物的过程，从而精细处理短程相互作用和分子柔性。尽管现有采用该策略的方法已成功估算了kon值，但它们通常需要大量计算资源。本研究开发了一个多尺度流程，通过优化BD模拟的采样来生成配体非常接近其蛋白质结合位点的扩散相遇复合物集合，并将这些结构作为MD模拟的起点，从而提高了计算效率。由于BD模拟的计算成本远低于MD，且所需的MD模拟时间缩短，该方法在保持精度的同时实现了计算高效。该流程已在一组不同大小、柔性和结合特性的蛋白质-配体复合物上得到验证，计算得到的kon值与实验测量结果吻合良好，并提供了对结合速率物理决定因素的深入见解。

## **Figure 1: 结合NAM算法的两区域结合模型示意图**

此图阐述了扩展的Northrup-Allison-McCammon（NAM）算法框架，用于结合BD和MD模拟计算kon。它将蛋白质周围空间划分为由界面分隔的“外部区域”（BD模拟）和“内部区域”（MD模拟）。关键的参数包括：β（配体从b-表面到达界面的概率）、α（从界面出发到达结合态的概率）以及Δ（从b-表面重新进入内部区域的概率）。该图是理解整个多尺度计算流程（从长程扩散到短程结合）的理论基础。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/YFLnWDLn3VnAlD1SvqsJTZ1ic1z2AaxjCWcV2XEBHrywaZxylYiaqUlmMWAbPJxKKibn5L8ESZYicFEIxWcPSiaobQKMLHsyPqa90VVWhcGDKZyM/640.png)

## **Figure 2: 诱导契合结合过程的两步模型**

此图将蛋白质\-配体结合过程概念化为两个连续步骤。第一步（扩散步骤）：配体在长程静电力和随机碰撞力的主导下扩散至蛋白质附近，不引起显著的构象变化。第二步（扩散后步骤）：当配体足够接近结合位点时，发生短程相互作用（如氢键、范德华力）、诱导构象变化以及去溶剂化过程，最终驱动系统形成稳定的结合复合物。这个模型为分别使用BD（第一步）和MD（第二步）进行模拟提供了理论依据。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/YFLnWDLn3VnS9dq1JYOjNwIFhdx3Sn0ZDAcFFyba49W9UhvUGf8GZ68RvCwHic2vyM6c09gxpa4wiaXm8YZGgPkic5OwIROqO8uHsdicDz5Biamc/640.png)

## **Figure 3: BD模拟轨迹分析及MD初始结构选择方案**

此图展示了如何分析BD模拟轨迹以获取用于MD模拟的初始结构。核心思想是记录配体在最短窗口距离（即最接近结合位点）时的构象。具体流程分为两轮BD模拟：第一轮用于确定配体能接近结合位点的最短窗口距离；第二轮则在该确定的最短窗口距离处，记录至少50个成功形成相遇复合物的轨迹中的配体构象。这些构象经过聚类后，选出代表性结构作为MD模拟的起点。该方案是提高整个流程效率的关键，因为它确保了MD模拟从最有利的位置开始，从而缩短了所需的MD模拟时间。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/YFLnWDLn3VkbFNxXsSibDOZGznhcictVfEhIoeQk5YGqibEk04wuibxKlKLV6GkKZUFOo8totULyhZDDJOjOQwvUol4BMMyMOaPjAoO2a21ZFFw/640.png)

## **Figure 5: 结合BD与MD结果的kon计算方案**

此图可视化了如何整合BD和MD的模拟结果来计算最终的kon值。它展示了从BD模拟的起始（b-表面）到最终结合态的完整路径，并标明了各阶段的概率：β（从b-表面到达MD区域界面的概率，由BD模拟计算）、α（从该界面出发最终形成结合态的概率，由MD模拟计算）。这些概率被代入扩展的NAM公式（见Figure 1所述）以计算kon。该图清晰地说明了两种模拟方法在计算流程中的衔接和数据整合方式。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/YFLnWDLn3VnLjGxoXNsv0UDmQmuKHdzfmqwpn9SnDLwPljkxbaORBpkI6adY5KpywTVhENZUURMoRaicyf8H5ns9mMmYHp6fRibib8kKyjEsZg/640.png)

## **Figure 9: 实验值、单纯BD预测值与BD+MD组合预测值的比较**

此图是评估方法性能的核心结果图。它在一张图上以散点图形式对比了10个蛋白质-配体体系的实验测量kon值、仅使用BD模拟计算的值以及BD+MD多尺度方法计算的值。结果显示，单纯BD模拟倾向于高估kon值（所有点位于对角线之上），因为它忽略了结合位点的去溶剂化和诱导契合等能垒。而BD+MD组合方法计算的值（菱形）与实验值（三角形）吻合得更好，大多数点更接近对角线。该图直观地证明了结合MD模拟以考虑扩散后步骤对于获得准确kon值的必要性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/YFLnWDLn3VmGVgD2dwP6sApAicFFPoUh8I4Il6A0IYQ506KARaJvUF7jKAHeasJSb2A9m7cGbLyyBhDicQGQF8v2JsND9eTnPcjqYT8x0MTSo/640.png)

  
## **文章重点核心内容讲解**

本文的核心是开发并验证一个高效、准确的计算蛋白质\-配体结合速率常数 kon的多尺度模拟流程，该流程创新性地通过优化布朗动力学模拟的采样策略来显著减少计算成本。

研究背景与目标：药物结合的动力学参数（如kon）对药效至关重要，但实验测定困难。传统长时间分子动力学模拟直接观测结合事件计算量巨大。现有结合BD（处理长程扩散）和MD（处理短程相互作用）的多尺度方法（如SEEKR）虽有成效，但仍需大量计算资源（例如数百万条BD轨迹和微秒级MD模拟）。本文旨在开发一个计算效率更高的BD-MD组合流程。

方法创新：优化采样策略：本文方法的关键改进在于对BD模拟生成的“相遇复合物”的定义和记录方式。不同于之前方法在距离结合位点较远处（如32Å）定义界面，本文的流程通过分析BD轨迹，记录配体在满足所有反应接触准则的前提下所能达到的、最靠近结合位点的位置（“最短窗口距离”）的构象。这确保了MD模拟从一个非常有利的、接近最终结合态的初始构象开始，从而大幅减少了为观测结合事件所需的MD模拟时间（通常仅需纳秒级别，而非微秒级别）。

流程验证与结果：该流程在包含10个体系（如胰蛋白酶-苯甲脒、Haspin-卤代结核菌素衍生物、因子Xa-抑制剂、神经氨酸酶-奥司他韦/扎那米韦）的多样化数据集上进行了测试。

计算效率：如表2所示，对于不同体系，所需的MD模拟时间从0.5纳秒到500纳秒不等，相比于需要长时间模拟来捕获自发结合事件的传统MD或某些需要大量短轨迹的里程碑方法，计算资源需求显著降低。

计算精度：结果显示，单纯BD模拟普遍高估kon值（Spearman相关系数仅0.24），因为它假设扩散相遇即等同于结合，忽略了后续的能垒。而BD+MD组合方法计算的值与实验值吻合良好（Spearman相关系数达0.72），统计检验（p=0.536）表明两者无显著差异。该方法甚至成功预测了结合速率极慢的Haspin-结核菌素体系在10纳秒MD模拟内无法到达结合态，与其实验值最低的现象一致。

物理机制洞察：通过分析模拟轨迹，研究揭示了不同体系的结合机制差异。例如，胰蛋白酶\-苯甲脒的结合主要由扩散控制（MD时间极短），而Haspin-抑制剂和扎那米韦-神经氨酸酶的结合则受扩散后步骤（构象调整）控制（需要较长MD时间）。研究还复现了奥司他韦与扎那米韦因与Glu276残基相互作用方式不同（疏水排斥 vs. 氢键吸引）而导致的结合速率差异。

结论与意义：本文开发的多尺度流程成功实现了在保持与实验数据良好一致性的前提下，高效计算蛋白质\-配体结合的kon值。其核心优势在于通过智能选择MD起始构象来缩短昂贵的MD模拟时间。该流程不仅能提供定量的动力学参数，还能揭示结合路径和机制（扩散控制 vs. 构象变化控制），为基于结构的药物设计提供了有力的计算工具。

## 

## **分子模拟计算内容与参数**

本文中的“分子模拟”包含两个层次：布朗动力学模拟和分子动力学模拟，两者分工明确。

## **1\. 布朗动力学模拟的计算内容与参数：**

计算内容：模拟配体在隐含溶剂中，在蛋白质长程静电力和随机力作用下的扩散运动，直至其与蛋白质形成“扩散相遇复合物”（即满足预设的一组原子间接触准则）。核心目标是计算配体从远处（b-表面，100 Å）扩散到蛋白质附近“界面”（即记录构象的最短窗口距离）的概率 β，并生成用于后续MD模拟的初始构象集合。

### **关键参数与目的：**

软件：SDA (Software for Diffusional Association) 7.3.4。目的：专门用于执行BD模拟的软件。

### **力场/相互作用网格：**

静电势网格：使用APBS软件求解线性化Poisson-Boltzmann方程生成。参数：网格间距1 Å，溶剂介电常数78，溶质介电常数2。目的：提供蛋白质和配体在空间各点的静电势，用于计算BD模拟中的静电力。

有效电荷模型：将蛋白质和配体的原子电荷拟合为数量更少的“有效电荷”。目的：在保持静电势精度的前提下，大幅加速BD模拟中力的计算。

非极性去溶剂化网格：基于溶剂可及表面积计算生成，但采用了精修模型——忽略带有非零形式电荷的原子（如配体中的氨基）的贡献。目的：更准确地描述疏水效应，避免过度估计带电基团周围的非极性吸引力（如图7所示）。

扩散系数：使用HYDROPRO软件计算。参数：蛋白质原子元素半径2.9 Å，配体原子元素半径1.2 Å。目的：为BD模拟提供配体和蛋白质的平动和转动扩散系数。

### **模拟设置：**

轨迹数：每个体系运行250,000条独立BD轨迹。目的：获得统计可靠的相遇概率 β。

反应准则：基于蛋白质\-配体复合物的晶体结构，定义一组独立的极性或π相互作用原子对接触（如氢键、卤键、π-π堆积）。当配体在模拟中同时形成所有这些接触，且距离在阈值内（如3.5-4.5 Å），即认为形成了相遇复合物。目的：精确判断配体是否以正确的几何取向接近了结合位点。

记录策略：分析轨迹，找到满足所有反应准则的最短窗口距离，并在该距离处记录至少50个成功轨迹的配体构象。目的：为MD模拟提供最接近结合态的初始结构，以最大化MD效率。

## **2\. 分子动力学模拟的计算内容与参数：**

计算内容：以BD提供的50个代表性相遇复合物构象为起点，在显式溶剂模型下进行MD模拟。模拟监测配体是否能在有限时间内（最长10 ns）形成结合态（定义为所有反应接触原子对距离≤4.0 Å），从而计算从“界面”到结合态的概率 α。同时，模拟捕获了去溶剂化、诱导契合等原子细节过程。

### **关键参数与目的：**

软件：AMBER 22。目的：执行全原子、显式溶剂的分子动力学模拟。

力场：

蛋白质：AMBER ff14SB力场。目的：描述蛋白质的键合和非键合相互作用。

配体：GAFF力场，配体电荷通过量子化学计算（GAMESS软件）的静电势进行RESP拟合得到。目的：为小分子配体提供准确的参数。

水模型与溶剂化：TIP3P水模型，周期性边界条件，溶质与盒子边界距离10 Å。添加Na⁺和Cl⁻离子以中和体系电荷并匹配实验离子强度。目的：提供真实的溶剂环境。

### **模拟细节：**

静电与范德华处理：使用粒子网格Ewald方法处理长程静电，非键相互作用截断半径为10 Å。

平衡过程：采用分步平衡策略，包括能量最小化、在NVT系综下加热至目标温度、在NPT系综下进行压力平衡。关键的是，在向蛋白质中添加配体后，进行局部平衡——仅对配体及周边8 Å内的残原子以弛豫，而约束蛋白质其他部分。目的：在保持蛋白质整体构象大致不变的前提下，允许结合口袋局部调整以适应配体，这模拟了从相遇复合物到过渡态的初始步骤。

生产模拟：对50个初始构象各进行1条MD轨迹，使用CUDA加速的pmemd模块在GPU上运行。模拟在以下任一条件满足时停止：配体到达结合态（窗口距离4 Å）、配体逃逸至远处（b-表面，100 Å）、或达到最大模拟时间10 ns。目的：统计从起始构象成功结合的比例，用于计算概率 α。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/YFLnWDLn3Vn91ibzn74quYf4QibxOQ8vIC36Sbalev7I7fQ8Drso8iaxUxm1Y6FHvQf25UbQNntia1G9GLiaMDPaRwgib6qnxibTpsTKGSkicLicvZ2M/640.png)

https://passport.compshare.cn/register?referral\_code=AKi762zEPo4DJ8DlHwzKAJ&ytag=GPU\_YY\_YX\_bl\_qiuxinlong

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9OicuUQbGCGRRQOYOeHlIaFEMz4ciaZmZGyAVvOteNSm3D4CLzhWvwKkWJ0eFCXWXenaYhDTJgrLvtggfkamzArw/640.png)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/YFLnWDLn3VmFrZepuiadnCicJorbhh2dj82lBgnbypsSAT9vP6pMNnqFw4pcZINRyKI6kPbZTxeo6H5Fwq9N8AFibzEcqLicUUXuEXTicAO9UFMk/0.png) 

 分子与生命 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/YFLnWDLn3VmFrZepuiadnCicJorbhh2dj82lBgnbypsSAT9vP6pMNnqFw4pcZINRyKI6kPbZTxeo6H5Fwq9N8AFibzEcqLicUUXuEXTicAO9UFMk/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
