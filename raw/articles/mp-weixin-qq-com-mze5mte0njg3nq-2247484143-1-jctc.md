---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247484143&idx=1&sn=de4e9290e21db1750e4ce0adb47e1807
canonical_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247484143&idx=1&sn=de4e9290e21db1750e4ce0adb47e1807
source_domain: mp.weixin.qq.com
title: 【JCTC】慕尼黑工业大学团队开发基于能量的生成式框架，无需漫长模拟轨迹即可直接从原子势能构建粗粒化模型并精准重构全原子结构
author: 
published_at: 
fetched_at: 2026-04-25T02:04:23Z
extractor: wechat_worker
content_hash: d2ae2c8aa9727ce20c4a2572e766867340d00fae0e62fb2847acadb28baaebcb
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgou90V59g3iabP3iaoicgw6XWZPPz0dBQ5eHibbYo64DjYtqkTXOYfRgWl3cBU3wqZwjdiamMkjiaa4YHBA/0.jpg) 

# 【JCTC】慕尼黑工业大学团队开发基于能量的生成式框架，无需漫长模拟轨迹即可直接从原子势能构建粗粒化模型并精准重构全原子结构

原创 Re Re [ 计算材料视界 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

### 

在分子模拟领域，“粗粒化”是一种通过减少自由度来简化系统、从而模拟更大时空尺度现象的关键技术。然而，传统的粗粒化方法严重依赖于漫长且昂贵的全原子分子动力学模拟所产生的海量数据。这导致了一个“鸡生蛋”的困境：我们需要粗粒化模型来高效探索新的构型，却又需要先有覆盖所有构型的全原子数据来训练这些模型。

**2025年，慕尼黑工业大学数据驱动材料建模首席教授P. S. Koutsourelakis及其团队成员Maximilian Stupp在《Journal of Chemical Theory and Computation》上发表了一项突破性研究。** 他们提出了一种**完全无需模拟数据、仅基于能量（势函数）的生成式粗粒化框架**，成功绕过了传统方法的根本性限制，为分子模拟提供了全新的解决方案。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgou90V59g3iabP3iaoicgw6XWZ7EVibicqDnxvp6tYPX6a3nvfxZE8MLILLEdt8UCRYyAcOySjhUHHTYhg/640.png)

---

#### **一、引言：粗粒化的“鸡生蛋”困境**

分子动力学模拟是揭示生物大分子、材料等微观世界奥秘的重要工具。但随着体系变复杂，模拟所需的时间尺度远超计算能力，此时粗粒化技术应运而生。它通过将多个原子“捆绑”成一个“珠子”来降低复杂度。

传统“自下而上”的粗粒化方法，其目标是让粗粒化模型的平衡分布与全原子模型保持一致（即热力学一致性）。但这个过程通常需要预先运行漫长的全原子模拟以获取训练数据。这就陷入了循环依赖：**粗粒化模型的能力被其训练数据所局限，无法发现数据中未出现过的新构型**。同样的问题也困扰着增强采样技术中的集体变量发现。

#### **二、研究目的与创新点：一场“无数据”的革命**

本研究旨在回答一个核心问题：**能否不依赖任何预先的模拟数据，仅利用分子的能量（势函数）信息，直接构建出热力学一致的粗粒化模型，并能精准地重构出全原子结构？**

其核心创新在于：

1. **完全数据无关：** 训练过程**仅需要分子力场（势能函数）及其梯度（原子受力）的信息**，完全不需要预先采集分子动力学轨迹。
2. **结构化潜空间：** 模型通过一个可逆的双射变换，将全原子坐标分解为一个**低维的“慢变量”空间（捕捉系统的亚稳态）** 和一个**互补的“快变量”空间（描述局部热涨落）**。
3. **统一生成式框架：** 该框架**同时解决了粗粒化映射和反向重构（Back-mapping）两大难题**。一旦模型训练完成，可以一次性生成独立、平衡的全原子样本。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgou90V59g3iabP3iaoicgw6XWZkx9F1GWrlTrHawMgcjMemdnojz5yXtHjpxwibs5eoP1P3samEgRgSVg/640.jpg)

> **图1（Figure 1）: 生成式框架示意图**  
> 该图展示了本方法的整体思路：通过一个可学习的双射变换，将全原子坐标分解为具有多峰分布的慢变量和具有单峰分布的快变量，并能够无损地重构回全原子坐标。

#### **三、研究过程：如何从能量中“学习”结构？**

**1\. 核心方法论：**  
研究者设计了一个生成式概率模型。它通过一个可学习的线性变换，将原子坐标映射到由慢变量和快变量构成的潜空间。其中：

* **慢变量的分布** 用一个**表达能力极强的归一化流模型**来刻画，以捕捉复杂的多峰特性（即不同的亚稳态）。
* **快变量的分布** 则在给定慢变量的条件下，被设计为**简单的单峰分布（如高斯分布）**，代表局部的快速振动。

**2\. 训练策略：**  
模型的训练目标是**最小化生成分布与目标玻尔兹曼分布之间的反向KL散度**。这个过程只依赖于对势能函数的计算，无需任何数据。

* **挑战：** 反向KL散度具有“模式寻求”特性，容易忽略概率较低的亚稳态，导致模式坍塌。
* **解决方案：** 团队引入了**自适应退火方案**。训练从高温（分布平缓）开始，逐渐降温至目标温度。在每一步，算法都会自动确定最佳的降温步长，确保模型能稳定地捕捉到所有新出现的亚稳态，从而成功找到所有相关构型。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgou90V59g3iabP3iaoicgw6XWZBehXgIuz2ksPZJyM9ibFdQCkWaf9zWmr6v4icbxU6jAUjQbL5AfK1mAg/640.jpg)

> **图3（Figure 3）: 双阱势能系统中的训练过程**  
> 左列展示了在不同逆温度下，模型预测的有效势能与真实势能的对比；右列展示了慢变量边际分布的演化。可以看到，随着训练进行，模型成功地捕捉到了两个能量阱。

#### **四、研究结果与性能展示**

**1\. 合成系统验证：**

* **双阱势能（Double-Well）：** 模型成功发现了两个能量阱，并学到了正确的粗粒化变量（即区分两个阱的反应坐标）。
* **高斯混合模型（GMM）：** 在一个20维的复杂多峰分布中，**没有退火策略的模型会坍塌到其中一个模式，而采用自适应退火的模型则完整地捕捉了所有三个模式**，证明了该策略的有效性。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgou90V59g3iabP3iaoicgw6XWZxHDSwWlicI4A0TMLTQafEyibZtNPMIVDhHGM7BnicIINPiarQtn1VeBntg/640.jpg)

> **图8（Figure 8）: 高斯混合模型采样结果对比**  
> 左图（使用退火）显示模型生成了覆盖所有三个模式的样本；右图（未使用退火）显示样本仅集中于一个模式，证明了自适应退火对于避免模式坍塌至关重要。

**2\. 标准生物分子测试：丙氨酸二肽**  
研究者将方法应用于经典的丙氨酸二肽分子。这是一个小型蛋白质片段，其构象由两个二面角所主导。

* **自动发现物理意义变量：** 尽管模型**没有被告知任何关于二面角的信息**，但它自动学习到的粗粒化变量与这两个关键的二面角高度相关。
* **精准预测构象分布：** 模型生成的构象在拉氏图上精准地复现了所有主要的能垒和亚稳态区域，与参考数据高度一致。
* **高精度结构重构：** 模型重构出的全原子结构，在键长、键角、回转半径等物理观测量上，都与传统模拟结果吻合极好。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgou90V59g3iabP3iaoicgw6XWZZE9VK7WfPl9pQj0oxrXn0sfpLibLp28jFOn95Y652oZX227Zw2RWl7A/640.jpg)

> **图12（Figure 12）: 丙氨酸二肽的拉氏图对比**  
> 在不同温度下，模型预测的二面角分布（右列）与参考模拟结果（左列）几乎无法区分，证明了其精准的预测能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgou90V59g3iabP3iaoicgw6XWZkbwJicPMv4XGBpZd1kukvmQ1zy7LqrfjlfO6TAYTRmPDzJqAsfgibheQ/640.jpg)

**图14（Figure 14）: 粗粒化变量与二面角的关联**  
该图通过颜色映射显示，模型学习到的某些粗粒化变量与特定的二面角区域有强烈的对应关系，表明模型自动发现了有物理意义的慢变量。

#### **五、创新点总结**

1. **范式转移：** 首次实现了**完全“无数据”** 的粗粒化模型训练，仅凭能量函数即可学习，破解了长期存在的“鸡生蛋”难题。
2. **统一框架：** 将**粗粒化映射**与**全原子重构**两个分离的步骤统一在一个端到端的生成式模型中，解决了反向映射的模糊性问题。
3. **智能训练：** 提出的**自适应退火方案**，有效克服了能量训练中固有的模式坍塌问题，确保能发现所有相关亚稳态。
4. **自动发现：** 模型能够**自动从能量景观中学习出具有物理意义的粗粒化变量（慢变量）**，无需人工干预或先验知识。

---

#### **六、结论与展望**

这项工作为分子模拟领域提供了一条全新的道路。它证明了**即使没有预先的模拟数据，我们也能直接从物理定律（势能函数）出发，构建出强大、精准且可解释的粗粒化模型**。这不仅大幅降低了构建模型的前期成本，更重要的是，它使模型具备了探索未知构型空间的潜力。

未来，该方法可与等变网络、图神经网络等更先进的架构结合，以处理更大、更复杂的生物分子系统。这项研究标志着分子建模向更智能、更自主、更基于第一性原理的方向迈出了关键一步。

https://pubs.acs.org/doi/10.1021/acs.jctc.5c01504

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
