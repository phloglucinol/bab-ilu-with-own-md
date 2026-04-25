---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzU4MDk1ODI4Mg%3D%3D&mid=2247484575&idx=1&sn=90593652b59c0ddd517aced952b0e979
canonical_url: https://mp.weixin.qq.com/s?__biz=MzU4MDk1ODI4Mg%3D%3D&mid=2247484575&idx=1&sn=90593652b59c0ddd517aced952b0e979
source_domain: mp.weixin.qq.com
title: Kirkwood–Dirac (KD) 准概率分布
author: 
published_at: 
fetched_at: 2026-04-25T02:04:00Z
extractor: wechat_worker
content_hash: 8d996af02f3a788073885b7d347dba5e3c92b016432b7fe1429e74182afe6c1f
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/ZYRagjpeCsibkj4mF06L3tGcFMWNEJ6D9CcXI0H2PGFibZShiaet1mgKjP50GiaHshROlPSoNrAYWsTG5OlcL1I0lw/0.jpg) 

# Kirkwood–Dirac (KD) 准概率分布

原创 林舞鹤 林舞鹤 [ 也疏寒 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

#   

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/ZYRagjpeCsibkj4mF06L3tGcFMWNEJ6D9zZJP5BDjctx8Yrpoh2e8whV15NIahhsibhvEOwUHZbuQaicULZtP4XYg/640.jpg)

#   

John Gamble Kirkwood（约翰·甘布尔·柯克伍德），1907年5月30日生于美国俄克拉何马州戈特博，1959年8月9日卒于康涅狄格州纽黑文，是一位著名的化学家与物理学家，曾先后在康奈尔大学、芝加哥大学、加州理工学院和耶鲁大学担任教职。他在1933年提出了KD分布，随后1945，狄拉克重新发现了KD分布。

  
最近在研究与 **Kirkwood–Dirac (KD) 准概率分布**（通常简称 **KD 分布**）相关的课题，发现网上关于KD分布的介绍不多，所以简单写点。

与其他广义概率模型中的准概率分布一样，KD 分布是一个极具魅力的概念工具，它处在经典概率理论与量子力学奇异、反直觉结构的边界。它提供了一种表示量子态的方法，超越了经典统计的范畴，允许出现_负值_甚至_复数值_。这些特性在经典理论中没有对应，却真实地编码了量子测量、量子相干和量子情境性等本质的量子特征。

从这个意义上讲，KD 分布为量子理论的非经典本质提供了一个尤为清晰的窗口，使其成为基础研究和现代量子信息应用中的一个重要工具。

## 什么是量子力学中的准概率分布？

在讨论 KD 分布之前，有必要回顾一下基本的历史背景。

在经典物理学中，系统的状态可以直接在_相空间_中描述。一个点  指定了粒子的位置和动量，而我们对系统的不确定性则通过真实的概率密度  来编码。这类分布总是非负实函数，并满足归一化条件，符合经典概率论的熟悉规则。所有经典可观测量都是相空间上的函数 ，其期望值由在相空间的概率平均给出：

然而，**量子力学**采用了截然不同的语言。基本对象是_波函数_（或更一般的密度算符），它并不表示相空间中的概率分布。虽然  给出了位置的概率密度， 给出了动量的概率密度，但没有单一函数能够同时为位置和动量分配概率。这种障碍不仅是技术性的，而是根本性的，源于量子可观测量的不可对易性，并由海森堡不确定性原理描述。

尽管如此，我们仍然自然地想知道，是否可以用_类似相空间的方式_表示量子态，即便必须牺牲某些经典特性。这种动机促成了**准概率分布**的发展。这类对象在形式上类似经典概率分布，但放宽了一个关键要求：它们不必非负，甚至不必为实数。允许出现负值或复数值，使得量子干涉、相干性以及其他真正非经典效应能够在相空间框架内被编码。这种观念在现代量子理论的研究中非常重要。

常见的例子包括：

* **Wigner 准概率分布**，由 Eugene Wigner 于 1932 年提出，实数值但可能为负。
* **Husimi \-函数** 和 **Glauber–Sudarshan \-函数**，广泛应用于量子光学。

**Kirkwood–Dirac (KD) 准概率分布**属于这一类，但具有一个重要区别：它可以针对_任意一对可观测量_定义（实际上Wigner 准概率分布也可以做相应的拓展），而不仅仅是位置和动量，并且通常是_复数值_。这些特性使得 KD 分布在研究量子测量、时间相关性以及量子信息处理应用中尤其强大。

## 历史背景：从 Kirkwood 到 Dirac

KD 分布起源于量子力学早期，当时物理学家正在努力调和量子现象与经典直觉。

* **John G. Kirkwood 的贡献（1933）**：美国物理学家 John Gamble Kirkwood 首次在论文 _"Quantum Statistics of Almost Classical Assemblies"_（发表于 _Physical Review_）中提出了该分布。Kirkwood 旨在描述接近经典的量子系统，使用相空间表示。他的版本本质上是一个关于位置和动量的复值联合分布。
* **Paul Dirac 的独立发现（1945）**：传奇物理学家 Paul A. M. Dirac 在论文 _"On the Analogy Between Classical and Quantum Mechanics"_ (_Reviews of Modern Physics_) 中独立重新发现了这一分布。Dirac 强调它在说明经典与量子理论之间类比中的作用，尤其是对于非对易算符。

KD 分布的实部称为 Margenau-Hill 准概率分布，由 H. Margenau 和 R. N. Hill 于 1961 年在论文 _"Correlation between Measurements in Quantum Theory"_ 中提出。

几十年来，KD 分布相对而言其实并不为研究者们所广泛关注， Wigner 分布是大家所聚焦的地方。然而，自 2010 年代以来，它因在量子信息理论中的应用而重新受到关注，成为量化非经典资源（如相干性与情境性）的有力工具。更多细节可参考Arvidsson-Shukur 等人撰写的综述论文 _"Properties and applications of the Kirkwood–Dirac distribution"_.

## 数学表述：KD 分布的定义

让我们深入数学部分。假设读者对量子力学符号（如密度算符 、bra 、ket ）有基本了解，我会边解释边讲。

### 两个可观测量的基本定义

考虑一个量子系统，其状态由密度算符  描述（可为纯态或混态）。设  和  为两个厄米可观测量，分别具有本征基  和 ，为了简便假设 Hilbert 空间为有限维度 。

**Kirkwood–Dirac (KD) 准概率分布**定义为：

其中：

* 是本征向量的重叠。
* 从定义可以看出，该表达式一般为复数。

对于投影算符  和 ，可写为：

在连续变量（如位置  和动量 ）下：

如果我们对KD分布取实部，我们就得到了 **Margenau-Hill 准概率分布**，由于KD分布归一化特性，在求和过程中，虚部自动消失，所以 Margenau-Hill 准概率分布也是归一化的，并且取值为实数的一种准概率分布。

### 推广

KD 分布可以自然地扩展到更一般的情形：

* **多个可观测量**（ 个）：
* **正算符值测度 (POVMs)**：

### 核心数学性质

* **归一化**：  
对于多个可观测量亦成立。
* **边际分布**：对一个指标求和可重现标准量子概率（Born 规则）：  
对于多个可观测量的情形，这会变成Kolmogorov相容性条件。
* **态重构**：假设所有重叠  非零，可由 KD 分布重建密度算符：  
从这个意义上看，KD分布完整地刻画了量子态。

有趣的是KD分布是实验上可测的，有多种实验方案来实现这一点，较为常见的是基于弱测量的方案（KD分布与弱测量有密切的关联）、相干测量方案、块编码方案等。

## 特性：KD 分布如何体现非经典性？

KD 分布之所以强大，是因为它捕捉了量子态中无经典对应的特征：

* **复值与负值**：KD 分布的元素可能为负（实部）或包含虚部。负值直接体现量子干涉，而虚部反映测量引入的扰动。
* **量化非经典性**：一种常用的度量是_总非正性_：  
对于相对于所选可观测量表现经典的态，。
* **与量子基础的联系**：
   * KD 分布的负值可见证_情境性_，说明测量结果无法由非情境隐藏变量解释。
   * 它体现_可观测量的不兼容性_，凸显量子理论中力学量的非对易结构。
   * 也与违反_宏观实在性_有关，例如通过 Leggett–Garg 不等式量化。
   * 在量子混沌方向，与OTOC有密切联系，可以对OTOC做一定拓展。

## 现代量子研究中的应用

* **量子计量学**：虚部可实现超灵敏参数估计。
* **弱测量**：负值产生异常弱值，可放大信号。
* **量子热力学**：定义相干功分布及涨落定理。
* **量子信息**：通过时间无序算符关联（OTOCs）量化相干性、纠缠与信息扰动。 用于直接测量量子态，所需资源少于完整态层析。
* **量子计算**：KD分布的量子性与量子计算的magic态注入方案的计算能力有密切关联。（这在Wigner分布体系内有许多研究，因为大家发现量子计算的优势起源与量子情境性有密切关联，而KD分布和Wigner分布均与量子情境性密切相关）。

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ZYRagjpeCs8FUJF2FAsroBAG5EwmjVOJR4m1adib8zVeXr5Ke5ibu5HMF1rRZkpIjNXricDhQOmBG27wPfH7dFeQA/0.png) 

 也疏寒 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ZYRagjpeCs8FUJF2FAsroBAG5EwmjVOJR4m1adib8zVeXr5Ke5ibu5HMF1rRZkpIjNXricDhQOmBG27wPfH7dFeQA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
