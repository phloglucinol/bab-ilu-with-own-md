---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkwODE2OTMzMA%3D%3D&mid=2247483756&idx=1&sn=04584973f5eb6e871e26e2cfec7e6def
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkwODE2OTMzMA%3D%3D&mid=2247483756&idx=1&sn=04584973f5eb6e871e26e2cfec7e6def
source_domain: mp.weixin.qq.com
title: Science | 暴力训练BioEmu，生成近似热力学平衡系综
author: 
published_at: 
fetched_at: 2026-04-25T02:03:07Z
extractor: wechat_worker
content_hash: 9d43e6277880e4370a03e62f7abd30989e9a46178c5c11f6d0ab0273d1b432fa
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/2pCp7qzL7STYtZcLbyIQCOFxIVCZwiaMAJrNoTGb7dvdsyibTAgYUFltJTiaCYMbb6nHAgQAlE2icncibm9EMWOeH9icUQs2Y3wZ8Aqia0PkOvmFkA/0.jpg) 

# Science | 暴力训练BioEmu，生成近似热力学平衡系综

原创 数维幻方 数维幻方 [ 宏微星 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2pCp7qzL7SQ7q9Gc1WouHtGmv4HSkExEDFibI84LWak6EaHBovSranaAfCguk7KuPtOUQ78zzBREyyMfFexZLuv3rvNJyvhXMt3oZDEMRWics/640.png)

# 论文标题 | Scalable emulation of protein equilibrium ensembles with generative deep learning

# 背景

在药物研发和生物技术中，蛋白质及其复合物扮演着极为重要的角色。现有的预测工具尽管耦合序列和结构，但是蛋白质功能的实现通常依赖于动态转换。实验上，单分子实验可以观测分子间距离，冷冻电镜可以获得蛋白质多个稳态以及概率分布，然而，这些方法非常耗时且昂贵。传统分子动力学（MD）模拟可以模拟蛋白质的动力学，可却面临着能量障碍 -- 需要增强采样方法，或者在特定超级计算平台（例如Anton）才能完成。相比于MD模拟，机器学习方法能够以相对的精度，超过2-3个数量级的效率进行采样，但尚无一种通用方案直接生成蛋白质构象系综。

# 原理

BioEmu的功能是输入蛋白序列，直接生成相应的平衡构象系综。训练过程包含三个阶段，包含一个预训练和两次微调：首先，在Alphafold结构数据集上预训练，使得模型学习到结构多样的构象；随后用重加权的MD模拟轨迹数据进行微调，目的是令模型的生成符合序列独立的系综分布；第二阶段微调是用实验数据完成的，以此进一步提高模型生成平衡系综的性能，同时预测实验数据，例如蛋白质稳定性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2pCp7qzL7SSJmuxCD42pA98LdPibYjh3RmwRDl33DqvvDaUMdzsZaxdC6OMGjyvvu2Uricve5RNemXFGKHpsq1AhtBlkAGhmmrtG3ytf8spWY/640.png)

# 数据集

预训练阶段：建立“序列 -- 多样化结构”的关系，瓶颈在于“并不是每个序列都有MD轨迹数据”。为此，作者从AlphaFold database (AFDB)出发，通过序列比对，聚类和结构打分等一系列清洗手段，构造了将近50000个序列类，每一类包含多个不同的结构，并且保证类内序列相似度高达80%，类间序列相似度低于30%。

MD轨迹微调阶段：一方面，作者引用了多个不同的长MD轨迹数据（尽管已有MD轨迹数据库，然而大部分都是短轨迹，不适合平衡生成任务的训练）；另一方面，作者通过OpenMM和GROMACS在显式溶剂（tip3p水模型），周期性边界层与分子间隔1nm及0.1M NaCl, 和amber ff99sb--ildn力场条件下，额外拓展了大量MD轨迹数据，总计216 ms.

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2pCp7qzL7SRtlhtuGWqianjSP6DjFCgk6IjlWOGF3agKrzziadRzn1pqkpGtELF0I59ic6b0F1U133sStiaibu4Z1mLRgZ2jT4aYmAOk4RFcc734/640.png)

实验数据微调阶段：仅准备序列以及对应的热稳定性数据（折叠自由能，ΔG）。

# 模型架构

蛋白质序列编码器。作者使用预训练的AlphaFold2编码序列的单一和成对表示（single and pair representation），使用Colabfold的mmseqs工具进行快速多序列比对。此外，由于蛋白质序列编码与其他变量无关，而仅取决于序列，所以训练以及推理阶段的所有序列的单一和成对表示都被提前计算和储存，从而便于训练时快速调用。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2pCp7qzL7SS2QcdtUxKNxONZ0c3bQO0908h57A0bqlXARMoBnRGfHM0Nws4ROoSd2jP9II6VVJXcE3U4IUN8iaTC0YkRwAQTjosHh9Yeoicnc/640.png)

蛋白质的粗粒化结构表示。训练一个结构生成模型时，需要选择一个合适的输入以及输出坐标，既要包含大部分结构特征，又能够比较物理合理的复现蛋白质的全原子构象。BioEmu仅提取骨架重原子，不显式建模侧链或氢原子。将任意帧的全原子结构按照给定残基转化为骨架表示。作者对CA原子坐标r∈R3在位移矢量CA --> N和CA --> C上应用Gram-Schmidt正交化，这产生了可以被表示为旋转矩阵Q ∈ SO(3)的正交基。对每个残基重复这个过程，从而对蛋白质的全部N个残基获得位置-方向元组（position-orientation tuples）。作者为每个残基类型定义了一个参考骨架重原子模板，有着理想化的原子位置，用于恢复给定帧骨架表示的笛卡尔骨架原子坐标。

条件扩散生成模型。

BioEmu是一个输入蛋白质序列S，采样蛋白质3D构象x的条件扩散模型，

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2pCp7qzL7STpdgj1BBlcKIGnElicRicJ8xpAiaJ8wDt8qbv1On1A8WJ3JYKOFSTPoLOgrD9kOvKGnsviaZ4HZgOicaRPC3E9wwqCdRic8LyHtWcQs/640.png)

其中，θ是可学习的权重，用于参数化一个打分模型神经网络sθ(x|S)。pθ(x|S)的采样过程是通过模拟正向扩散模型的反向过程进行的，由骨架模板表示x空间上的随机微分方程定义，

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2pCp7qzL7STAnbhl5erj2OO4dk4AUTvmHxGOnbdxs5FYe60ibUFU9q2WiaSibY0r6ssmkUNFWTPpXO2iax6XTMaVTAP2ylM2rhzrCJwxVPLcJxg/640.png)

w是标准的Wiener过程，f和G是相应的drift和扩散系数。所有残基和相应的位置r，方向Q被独立扰动（corrupted）。具体而言，这些位置通过一个保持型随机微分方程（SDE）的方差和余弦噪声进行扰动。当x以上述方式被扰动后，使用p(x,t)表示扩散时间t时x的概率分布，边缘条件是p(x,0) = p(x)，即目标分布。如果初始位置r0是边界，那么p(x,1)接近于采样先验分布，此时的位置具有标准各向同性高斯分布（isotropic），且方向符合均匀分布（uniformly）。

通过使用来自p(x)的样本x(0)以及给定x(0)时x(t)的条件分布的对应样本进行训练，模型能够近似计算得分∇xP(x,t)。若已知得分，可构建随机微分方程（SDEs），使概率密度函数的演化方向反转。

从先验分布中采样位置r和取向Q，然后通过从t=1到t=0逐步模拟其中一个SDEs来实现‘去噪’，从而近似采样目标分布。

打分模型（score model）。

打分模型的结构类似于AlphaFold2 和Distributional Graphormer模型的结构模块，并采用不变点注意力（IPA）transformer架构。Algorithm 1中打分模型生成的平移与旋转评分（Sr&SQ）均定义于各残基的局部坐标系，且在整体结构旋转或平移时保持不变。因此在去噪过程中，主链原子位置的更新对整个结构的旋转和平移具有等变性。

| ![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2pCp7qzL7SRv3IibnTlpSPb5icXictzLrMRHucen0JFZtfma7ybVia3YGyYtZxViaNOAOvvdRBH8icZvEGhZ6AlF88pzsj0uic9ib6KfTMSWy2TWyIQ/640.png) | ![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2pCp7qzL7STPFJpAiaM1XqLFsaulLhmtApnqzauE1VEFya8vKxkKFINmah1uhDMVF3Yia3B1JY1cbKLhK9q448kSbop4XFRR4DsbGrwJyAiaJ4/640.png) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#   

# 训练过程

训练始于从 AlphaFold2 预训练的序列编码器，其权重被冻结，同时从头训练一个自定义的结构模块。首先在源自AFDB 的合成数据集上进行训练，该数据集具有高序列多样性，且每个序列对应多种不同的构象。预训练模型能够预测相同蛋白质序列的多种不同构象，但它不能准确地建模不同构象状态的概率。随后，在混合了MD 模拟数据（占 95%）和AFDB 结构（占5%）的数据集上进行微调。在MD 数据微调之后，使用开发的“属性预测微调 (PPFT)” 方法结合百万规模级别的实验性折叠自由能测量数据，同时仍然保留一小部分AFDB 和MD 数据，再进行一个阶段的微调。在所有阶段，都使用标准的去噪分数匹配损失函数。此训练流程最终生成了本文报道的模型BioEmu。

注意，在第1阶段微调过程中，MD轨迹数据被折叠自由能或者MSM进行了重加权。

训练设备

挺贵的，感兴趣了解一下就好。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2pCp7qzL7SQluuLsic8SlvAicDFQSHcATsInaZAhMkPsWopsmESzKF6Yv0a943pyJnGDuFWEica0zkeiarAJOPuOKnU3ZpOHw2tiaiaIsFdLbFcBs/640.png)

  
# 应用

构象变化 <--> 折叠，构象转换机制，局部解折叠

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2pCp7qzL7STQ92P1KRCLl0dVTmNibkdd9qr2Xrqh3Nxg6x9ubNULBzPIDiapWppqEpYrVzwbnMyIF3NOWpDxRT7X15B2GibyRyv3UsfdbjdGWE/640.png)

近似平衡构象系综

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2pCp7qzL7SQpUl7IPiaZxGGKV9RQx65xgpkn3oUEdUrcXSPIY62Wc6PygWicE3143vCia84SWdesAKaEOMbMiaFsmtm52475Rj3D8ufJaBxEN7A/640.png)

折叠自由能 & 突变 & 结构稳定性

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2pCp7qzL7SSFqInGxicQt7DXtHXNEXicv9paaAFEbdmZjnoCu95ynWH8AT2hEEsQsy8j3VLNibicSNNrzFBdOaor4dbwzLLzq1BanxtMRtJ2C1A/640.png)

# 总结

限制：生成的构象比较粗糙，不具备生成膜系统，多链系统和小分子配体平衡系综的能力，且温度受限于300 K。

作者认为BioEmu不可能替代掉MD模拟，在未来，MD模拟仍然是研究动力学过程的主流方法。除了在非MD精度水平研究近似平衡系综以及相应的热力学性质外，BioEmu的另一个优势在于为MD模拟提供大量可选的优势起点，从而加速分子机制的研究和新药研发，蛋白相关的产业应用。

---

文章链接

URL:https://www.science.org/doi/10.1126/science.adv9817

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Qic3VVU7ZibibicWFwyDPulKHnqeAnTicKicFKSic89A7NYjXpEXVEBuMo43vwb2153bMGBSGcyjiaUtIMj7hlhPu6QvkQ/0.png) 

 宏微星 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Qic3VVU7ZibibicWFwyDPulKHnqeAnTicKicFKSic89A7NYjXpEXVEBuMo43vwb2153bMGBSGcyjiaUtIMj7hlhPu6QvkQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
