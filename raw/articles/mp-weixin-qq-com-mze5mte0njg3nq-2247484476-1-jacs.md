---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247484476&idx=1&sn=696830caa27297b36f57ba4367009bf0
canonical_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247484476&idx=1&sn=696830caa27297b36f57ba4367009bf0
source_domain: mp.weixin.qq.com
title: 【JACS复旦徐昕】张量预测不再难！复旦团队提出几何深度学习通用框架，实现分子与晶体张量性质端到端预测
author: 
published_at: 
fetched_at: 2026-04-25T02:04:18Z
extractor: wechat_worker
content_hash: 37399edabe8714d5c3da79174789f1429302beaec212acb3ac1a5933dbd05541
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDUP0umSj0eY4EL1WCouArOovCm2zxYRkq7KcWStAMGjv0b4I5TwJE0Q/0.jpg) 

# 【JACS复旦徐昕】张量预测不再难！复旦团队提出几何深度学习通用框架，实现分子与晶体张量性质端到端预测

原创 Re Re [ 计算材料视界 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在计算化学与材料科学领域，准确预测分子和晶体的响应性质（如极化率、弹性张量、化学屏蔽张量等）对于理解材料功能、设计新型分子与材料至关重要。这些性质通常以**张量**形式表达，具有明确的**对称性**和**协变性**约束，使得传统机器学习方法难以直接进行高精度预测。目前大多数模型只能处理标量性质或低阶张量，对于高阶张量或具有复杂对称性的张量预测仍面临巨大挑战。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDl1wAPTQFSEtxACNQUiarmLj2fI4FysuHehMNBvqYiapqkLFgQMyK1QIw/640.png)

**2025年11月24日，复旦大学徐昕团队在国际顶尖化学期刊《Journal of the American Chemical Society》上发表了题为《General Framework for Geometric Deep Learning on Tensorial Properties of Molecules and Crystals》的研究论文，提出了一种通用的几何深度学习输出模块，能够端到端预测任意阶数、具有指定对称性的张量性质。** 该框架结合团队自主研发的SE(3)-协变图神经网络XPaiNN，在多个分子与晶体数据集上实现了与第一性原理计算相媲美的预测精度，为AI辅助功能分子与材料发现提供了强大工具。

---

## 一、研究背景：为什么张量预测如此重要且困难？

分子和晶体的许多物理化学性质，如**偶极矩、极化率、化学屏蔽张量、弹性张量**等，都是响应外界电磁场或力学扰动而产生的张量响应。这些张量不仅具有明确的数学结构（阶数、对称性），还必须满足**旋转、反演等几何对称性**（即协变性）。传统的机器学习方法（如SchNet、DimeNet++等）通常只能预测标量性质，或在设计上难以保证张量的对称性与协变性。

近年来，**几何深度学习**（Geometric Deep Learning）的兴起为处理这类问题提供了新思路。尤其是**协变图神经网络**（Equivariant GNNs），能够在特征传递过程中保持对称性，显著提升了模型对几何结构的理解能力。然而，现有方法在预测高阶张量、处理晶体体系对称性、以及同时预测原子级性质时仍存在明显不足。

> **核心挑战：**
> 
> 1. 如何设计一个通用输出模块，能够构造任意阶数、任意对称性的张量？
> 2. 如何在不引入过高计算成本的前提下，保证张量的几何协变性？
> 3. 如何同时处理分子体系和晶体体系，并支持原子级性质的预测？

---

## 二、研究目的：构建一个通用、高效、对称性保持的张量预测框架

本研究旨在提出一种**通用的输出模块**，可与现有协变图神经网络结合，实现端到端的张量性质预测。该模块需满足：

* **通用性**：支持任意阶数张量，支持不同对称性（如对称、反对称、部分对称等）
* **协变性**：严格保持旋转、平移、反演对称性
* **高效性**：避免传统方法中计算量大的Clebsch-Gordan张量积操作
* **原子级预测能力**：支持如化学屏蔽张量、Born有效电荷等原子级张量的预测

---

## 三、研究方法：如何实现通用张量预测？

### 1\. 核心架构：XPaiNN + 自混合张量输出模块

研究团队在自主研发的SE(3)-协变图神经网络**XPaiNN**基础上，引入了一个创新的**自混合张量输出模块**（self-mix tensor output module）。该模块的核心思想是：

**将张量的球谐表示直接建模为图神经网络输出，再通过基变换得到笛卡尔张量。**

这样做的好处是：

* 张量的协变性和基本对称性自然满足
* 可避免在消息传递阶段进行耗时的CG张量积
* 支持从纯极张量表示构造出包含赝张量分量的输出

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDPMI2QjT96qWnaOtSvorQgHpbGRNqwQqCMTcYQx46ke2MO5CCibAugtg/640.jpg)

**图1 使用XPaiNN模型学习与预测笛卡尔张量的示意图**

> （a）使用协变图神经网络预测笛卡尔张量的一般流程；（b）XPaiNN模型架构；（c）本文设计的笛卡尔张量输出模块，接收来自消息传递块的不变和协变节点隐藏表示，传入节点自混合层并施加适当变换；（d）节点自混合张量积示意图，输入特征通过合法张量积路径形成输出，用于表示任意对称性的二阶张量。

### 2\. 关键创新：节点自混合层

输出模块的核心是**节点自混合层**，通过对节点隐藏特征进行定制化的通道级张量积，构造目标张量所需的球谐表示。这一设计充分挖掘了XPaiNN架构的能力，并基于“GNN隐藏层输出反映局部化学环境”的假设，适用于原子级性质的建模。

### 3\. 支持的性质范围

该方法支持预测的张量性质包括但不限于：

| 性质       | 符号  | 阶数 | 对称性  | 典型体系    |
| -------- | --- | -- | ---- | ------- |
| 偶极矩      | μ   | 1  | 向量   | 分子      |
| 极化率      | α   | 2  | 对称   | 分子、晶体   |
| 超极化率     | β   | 3  | 全对称  | 分子      |
| 化学屏蔽张量   | σ   | 2  | 任意   | 分子（原子级） |
| 介电张量     | ε   | 2  | 对称   | 晶体      |
| 压电张量     | e   | 3  | 部分对称 | 晶体      |
| Born有效电荷 | Z\* | 2  | 不对称  | 晶体（原子级） |
| 弹性张量     | C   | 4  | 四重对称 | 晶体      |

---

## 四、研究结果：性能如何？

### 1\. 分子张量性质预测（QM9S数据集）

在QM9S数据集上，XPaiNN结合自混合输出模块（XPaiNN-mix）在多个张量性质预测任务上取得最佳性能：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDY6F8pmXiaouzxwMEDyVOOqVxbhgPCRQ0sfRwYXDbRVLTpRj9rhpiaNIA/640.png)

**表1 在QM9S分子张量性质上的模型测试性能（平均绝对误差，MAE）**

> 包括偶极矩μ、极化率α、超极化率β、四极矩D和八极矩O。XPaiNN-mix在所有任务上均表现最优。

特别地，对于三阶超极化率β，XPaiNN-mix无需在隐藏特征中包含高阶球谐分量，仅通过自混合张量积操作即可高效捕获相关贡献，在保持较低模型复杂度的同时实现更高精度。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDeWAUQrqkJcwvxwDarH4WRnzlz79tjR0Kk6r5QZzRhF5CZj972gPSRQ/640.jpg)

**图2 XPaiNN-mix在QM9S上的测试性能**

> （a）（b）预测的极化率张量α及其导出的各向同性与各向异性极化率；（c）（d）预测的超极化率张量β及其导出的大小、平行与垂直于z轴的分量。

### 2\. 化学屏蔽常数与化学位移预测（QM9NMR数据集）

对于原子级的化学屏蔽张量预测，XPaiNN使用单一模型（共享参数）对所有原子类型进行联合训练，测试集上所有核的平均MAE为0.36 ppm，优于DetaNet（0.49 ppm，使用4个独立模型）。对¹³C、¹⁵N、¹⁷O等重原子的预测精度与专门为NMR设计的NMRNet模型相当。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDHbsSyW9RH8Q4e959pr5z1TMialFF58lnave7vDbSXWzQd0F61WGC4jg/640.jpg)

**图3 XPaiNN在QM9NMR上的测试性能**

> （a）预测屏蔽常数与DFT计算值的元素分别绘图；（b）三种模型在各核类型上的误差统计比较；（c）（d）对测试集中所有¹³C位点以及¹⁵N和¹⁷O位点的节点隐藏特征进行UMAP分析，显示特征与屏蔽常数之间的清晰相关性。

### 3\. 晶体电学响应性质预测（JARVIS-DFT DFPT数据集）

在晶体介电张量ε和压电张量e的预测任务中，XPaiNN-mix表现出色，与当前最先进的GMTNet模型性能相当甚至更优。特别是在高质量预测率（EwT）指标上，XPaiNN-mix显著优于基线模型。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDEtzACpR6nuyYZ9jOUg9icTZS6oc0n7elB3C1nDXzGjMP97mFxs2ZWAw/640.png)

**表3 在精选JARVIS-DFT DFPT数据集上预测电学响应性质的模型性能**

> 包括介电张量ε和压电张量e。XPaiNN-mix在多个指标上表现最佳。

### 4\. Born有效电荷预测（钙钛矿氧化物等体系）

对于原子级且不对称的Born有效电荷张量Z\*，研究团队进一步优化了输出模块（称为“mix2”），通过引入非等效特征输入和更高阶的极张量特征，成功解决了原始“mix”模块在预测非对称张量时的局限性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDibmWXnCQBicHFmgm1drqlQDFica8E2HMD3ZpU4ZIeP2OzqJ472RtRAr9w/640.jpg)

**图4 预测Born有效电荷的模型性能**

> （a）不同模型在三个BEC数据集上的整体预测误差；（b）XPaiNN-mix2在钙钛矿氧化物（ABO₃）数据集上的元素级误差统计（小提琴图）；（c）比较XPaiNN使用“mix”和“mix2”输出模块预测钙钛矿氧化物中B位元素（Ti、Zr、Hf）的BEC张量非对角分量与真实值。

### 5\. 弹性张量预测与材料筛选（MatTen数据集）

弹性张量C是四阶张量，具有复杂的对称性。XPaiNN-mix在MatTen数据集上实现了最优的预测性能，其导出的体模量K、剪切模量G和杨氏模量E的预测误差均低于现有模型（如MatTen、MatSca）。

**表4 在MatTen数据集上预测弹性张量及相关弹性性质的模型性能**

> XPaiNN-mix在所有指标上均表现最佳。

基于训练好的模型，研究团队对Materials Project数据库中的25,021种晶体结构进行了筛选，以寻找潜在的超硬材料（高体模量和高剪切模量）。筛选出的20种候选材料主要为碳化物、硼化物和氮化物，其中一些如Fe(BW)₂、B₃Os₂、Mo₂CN等是此前未被报道的化合物。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpxBsicUsVZZgKy1BSJaAyvDEiciaJC8WiaIRtRPVesNsLdlcFbMcYIia2IcqjryK2CavFdLkPOlvkiaMcw/640.jpg)

**图5 预测弹性性质的结果**

> （a）在MatTen数据集上按不同晶系列出的弹性性质测试误差；（b）在Materials Project中25,021种材料上的筛选结果，以剪切模量G vs 体模量K作图，潜在超硬材料位于右上角区域；（c）元素组合的相关性图，基于二元和三元化合物中记录的最大K值估算。

---

## 五、创新点总结

1. **通用张量输出模块**：首次提出能够处理任意阶数、任意对称性张量的通用输出模块，严格保持几何协变性。
2. **高效架构设计**：结合XPaiNN模型，避免传统方法中计算量大的CG张量积，在保持精度的同时提升效率。
3. **原子级性质预测**：支持化学屏蔽张量、Born有效电荷等原子级张量的“一体化”预测，无需为不同原子类型训练独立模型。
4. **晶体对称性兼容**：能够自然满足不同晶体体系的固有对称性要求，成功预测介电、压电、弹性等晶体张量性质。
5. **材料发现应用**：展示了在Materials Project数据库中进行高通量筛选、发现潜在超硬材料的能力，为AI辅助材料设计提供了实用工具。

---

## 六、研究意义与展望

本研究提出的通用张量预测框架，不仅在理论上统一了分子与晶体张量性质的机器学习预测方法，在实践中也展现出与第一性原理计算相媲美的精度，为计算化学和材料科学领域提供了强大的新工具。

**未来方向：**

* 进一步扩展框架，支持外场下的响应性质预测
* 结合更大规模、更多样化的数据集，构建面向分子与材料的“基础模型”
* 探索在药物设计、催化筛选、功能材料开发等领域的实际应用

该工作标志着几何深度学习在预测复杂张量性质方面迈出了重要一步，为AI驱动的新材料发现与分子设计开辟了更广阔的道路。

---

**📚 论文信息：**  
Wenjie Yan, Xinming Lai, Yicheng Chen, Wenhao Zhang, Jianming Wu, Xin Xu. _General Framework for Geometric Deep Learning on Tensorial Properties of Molecules and Crystals_.  
_Journal of the American Chemical Society_, 2025.  
DOI: 10.1021/jacs.5c12428  
代码与模型已开源：https://github.com/wiyan39/XequiNet\_tensor

  
预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajicM8NiadIPfeSzL1nFugbgrN0GO1hvZKLJOaBZvsoj55yGAmCZVw4Iiag/0.png) 

 计算材料视界 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajicM8NiadIPfeSzL1nFugbgrN0GO1hvZKLJOaBZvsoj55yGAmCZVw4Iiag/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
