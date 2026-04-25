---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkzMTY0NzMzNg%3D%3D&mid=2247485327&idx=1&sn=409fcb88465aa25b037b49de9fd8d378
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkzMTY0NzMzNg%3D%3D&mid=2247485327&idx=1&sn=409fcb88465aa25b037b49de9fd8d378
source_domain: mp.weixin.qq.com
title: PRE | 用阿诺德分岔理论重构蛋白质折叠动力学的物理图像 | Antti J. Niemi
author: 
published_at: 
fetched_at: 2026-04-25T02:03:15Z
extractor: wechat_worker
content_hash: 5fd296f657103a4ccec6d8125ba7ebba7a48868a2b3e40c12400f0a0b02d5bec
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/wBw7XXISyv5dxcK60OgVIeHSANYOW88k2JVfDjRM1JCIhicicBZ32OoQYbA3ZsAoiaxqmPgcBHmibrfE5tERtl1NBsVXWTGKN2rJRzH3HQMwian8/0.jpg) 

# PRE | 用阿诺德分岔理论重构蛋白质折叠动力学的物理图像 | Antti J. Niemi

原创 Yiquan Wang Yiquan Wang [ biomath ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

> Begun, A., Chernodub, M. N., Molochkov, A., & Niemi, A. J. (2025). Local topology and perestroikas in protein structure and folding dynamics. _Physical Review E_, _111_(2), 024406.

> https://journals.aps.org/pre/abstract/10.1103/PhysRevE.111.024406

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/wBw7XXISyv6tEgGgT055Kicy4geicDQsoPics2h85cOOVMtMkXDcEVaZUhMtiaLuSZauR39L2qkgYEsm5hwktmLSaLZJ4cdEwzKO0k8ot34XrIo/640.png)

## Abstracts

本文将局部拓扑学的方法引入蛋白质物理学领域。这是通过将球状蛋白质的折叠和去折叠过程解释为改变蛋白质C-alpha主链局部拓扑结构的构象分岔来实现的。该数学公式利用离散弗雷内（Frenet）标架形式体系，将阿诺德（Arnold）的“改革”（perestroikas）理论扩展到分段线性链。在低温折叠相中，主链几何结构推广了皮亚诺（Peano）曲线的概念，其模块化构件由离散非线性薛定谔方程的孤子解建模。当“改革”改变决定孤子中心的平坦点和分支点时，热去折叠随即开始。随着温度升高，“改革”发生级联，导致模块化结构逐渐解体。折叠和去折叠过程通过一个描述“改革”随温度演变的相关函数进行定量表征。该方法为理解蛋白质折叠和去折叠转变的物理机制提供了一个全面的框架，有助于更广泛的蛋白质结构和动力学领域的研究。

## 科学问题

在蛋白质科学领域，尽管像AlphaFold这样的人工智能算法在预测蛋白质最终折叠结构方面取得了巨大成功，但我们对蛋白质如何从一条随机链条“折叠”成具有生物活性的三维结构的动力学细节，依然知之甚少。

目前，描述线性异聚物（如蛋白质C-alpha主链）的相变通常依赖于几何指标，例如回转半径（Rg）。然而，这种几何描述存在一个核心瓶颈：它是一种“钝器”。回转半径可以告诉我们蛋白质在膨胀或坍缩，但它无法区分这种变化是仅仅源于热膨胀，还是源于内部拓扑结构的根本性改变。

为了解决这一难题，本文提出了一种基于**局部拓扑学**和**分岔理论**的全新视角。作者借用了数学家阿诺德（Arnold）提出的“Perestroika”（意为“改革”或“重组”）概念，试图捕捉蛋白质在热涨落下的拓扑突变。本质上，作者试图回答一个核心物理问题：当环境温度变化时，蛋白质主链的局部几何结构是如何通过一系列离散的拓扑跳变，最终导致整体结构的解体或形成的？

### **核心逻辑与深度解析**

#### **1\. 重构标架：从连续曲线到离散链的拓扑映射**

为了描述蛋白质主链的局部拓扑，传统的微分几何工具（如Frenet-Serret方程）面临失效，因为蛋白质主链是分段线性的折线，且存在曲率为零的拐点。为了解决这一偏差，作者引入了**离散Frenet标架**，并定义了处处可导的“有符号曲率”和广义扭转。这使得研究人员能够精确定义三种关键的拓扑奇点：拐点（inflection point）、平坦点（flattening point）和双平坦点（biflattening point）。

为了可视化这些复杂的拓扑特征，作者利用立体投影技术，将蛋白质主链的几何信息映射到一个二维平面上。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/wBw7XXISyv61bibbbpHY7DWlqEAsUEZaoWjSTT8DDKA8ymfos1HD3GVrut57qfaic0dg3dEIkLHDSmgdd5ic8aibxX8q0HCGBibwArA7MDS1tbWs/640.png)

**\[图3：(a) 弗雷内球面的立体投影示意图；(b) 蛋白质数据库(PDB)中C-alpha主链的立体投影图谱\]**

从图3(b)可以看出，绝大多数蛋白质的键角（kappa）和扭转角（tau）数据高度集中在一个环形区域（Annulus A）内。图中清晰地展示了蛋白质二级结构的拓扑分布：右手法尔法螺旋集中在环形的上方区域，而贝塔折叠则分布在扭转角分支切割线（branch cut）附近，即tau约为 **正负pi** 的位置。这种映射揭示了一个关键事实：蛋白质的折叠结构并非杂乱无章，而是严格受限于特定的拓扑区域内。图中的“平坦线”（tau=0）和“分支切割线”成为了判断拓扑结构是否发生突变（即发生“改革”）的关键边界。

#### **2\. 模块化本质：蛋白质作为拓扑孤子系统**

在确立了拓扑描述语言后，作者进一步探索了折叠态蛋白质的深层结构。研究发现，球状蛋白质的主链表现出惊人的模块化特征，类似于空间填充曲线（Peano曲线）。为了量化这种模块化，作者对肌红蛋白（1ABS）进行了分析，并发现通过引入Z2变换（允许键角取负值），蛋白质的结构可以被建模为离散非线性薛定谔方程的暗孤子解。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/wBw7XXISyv6wG0snsQVZ1bLemX2POiaBb39JxWO4hfHfnYAetPgo2tphjVDDMS9nklOpEIDQwRlRQxS6FV5LTkSLLN7H4EcM0nr5OxUedGM4/640.png)

**\[图6：(a) 1ABS主链的离散键角和扭转角；(b) 折叠指数；(c) Z2变换后的键角；(d) Z2变换后的扭转角\]**

图6(c)展示了极具说服力的证据：在经过Z2变换最小化扭转距离后，肌红蛋白的主链呈现出明显的“畴壁”结构。图中识别出了 **13** 个键角畴壁，这些畴壁精确对应了蛋白质中的螺旋结构（A至H）以及连接它们的回路。这意味着，蛋白质不仅仅是一串氨基酸，从物理角度看，它是一个多孤子系统。其折叠指数（图6b）最终达到 **+4**，意味着主链轨迹在拓扑空间中顺时针绕环形中心旋转了两圈。这种基于孤子的描述，不仅捕捉了蛋白质的几何形状，更揭示了其拓扑稳定性。

#### **3\. 热动力学演化：几何相变与拓扑相变的脱节**

确立了静态模型后，作者利用Glauber动力学模拟了升温过程，以观察蛋白质如何解折叠。首先，作者使用了传统的回转半径（Rg）作为序参量来观察相变。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/wBw7XXISyv7miankibZVRSbW3TKYmsm1gChvGXOoKFwnbPU43SicBSU6UQuFJEd8gjcpxryrxoUgY5mbdBgbUHlhVxUEtvP7dcVFqAXA26U5KU/640.png)

**\[图8：(a) 不同排斥体积参数下回转半径Rg随温度因子T的变化；(b) Rg的宾德累积量；(c) Rg的磁化率；(d) 螺旋度及其磁化率\]**

图8(a)中的紫色数据点（Delta = 3.7 Å，对应真实蛋白质）展示了三个明显的阶段：

1. 低温折叠相：Rg稳定在 **15 Å** 左右。
2. 中间过渡相（熔球态）：温度因子在 **10^-15** 到 **10^-13** 之间，Rg增加到约 **24 Å**。
3. 高温相（自回避随机游走 SARW）：Rg进一步增加并稳定在 **34 Å** 左右。

然而，仅仅依赖Rg的数据（图8a和8c）虽然能区分这些相，但其变化是渐进的，磁化率（图8c）甚至没有出现明显的峰值，这暗示几何参数无法敏锐地捕捉相变的临界点。几何上的膨胀（Swelling）掩盖了内部拓扑结构的剧烈重组。

#### **4\. 核心突破：拓扑序参量捕捉“改革”级联**

为了捕捉几何参数遗漏的动力学细节，作者引入了一个新的拓扑序参量——相关函数 C(0)。这个参数专门用于计数主链中越过平坦线或分支切割线的链接数量，即直接量化“改革”（Perestroikas）发生的频率。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/wBw7XXISyv77neu5XoR5wH8oplR7nDOOzTbHmwIsMibJnFR4U6KaVwfMcyV0yZrwCPiaGYButibxftW6o0Q3zr7MwDvjA1MSp6Z3ldzbX9yQH0/640.png)

**\[图11：(a) 回转半径Rg（紫色）与拓扑计数C(0)（绿色）随温度变化的对比；(b) C(0)的宾德累积量（紫色）和磁化率（绿色）\]**

图11(a)展示了本文最核心的发现：相比于回转半径（紫色曲线）的平缓变化，拓扑序参量 C(0)（绿色曲线）对相变极其敏感。

* 在低温折叠相（I区），C(0)保持在 **0.13** 左右的低位，表明拓扑结构极度稳定，“改革”几乎不发生。
* 当系统进入熔球态（III区）时，虽然Rg已经显著增大，但C(0)仅微幅上升至 **0.17**。这揭示了熔球态的一个关键物理图像：蛋白质虽然在几何上发生了膨胀和部分螺旋解体，但其核心的局部拓扑约束依然存在，并未发生大规模的拓扑崩溃。
* 真正的剧变发生在向高温相（V区）的转变中。C(0)突然急剧上升至 **0.44** 左右（接近理想随机游走的0.5）。这标志着“改革”的级联（cascading）发生，拓扑约束彻底瓦解。

图11(b)进一步证实了这一点，C(0)的宾德累积量在 **10^-13** 和 **10^-8** 附近出现了两个清晰的峰值，精确界定了折叠态、熔球态和无规卷曲态之间的相变边界。这证明了拓扑序参量比几何序参量能更清晰、更准确地定义蛋白质的动力学相变。

## 总结与展望

本文通过引入阿诺德的“改革”理论和局部拓扑学方法，成功构建了一个描述蛋白质折叠动力学的全新物理框架。其核心创新在于证明了蛋白质的去折叠不仅仅是几何上的膨胀，更是一场拓扑上的“级联革命”。

**关键结论**：

1. **拓扑优于几何**：传统的几何参数（如回转半径）对蛋白质相变的反应是迟钝的，而基于分岔理论的拓扑序参量能精确捕捉相变的临界点。
2. **熔球态的本质**：熔球态不仅是几何上的中间态，在拓扑上它是一个独特的相——具有高度的几何膨胀性，但在局部拓扑上仍保持相对稳定，只有少量的“改革”发生。
3. **孤子模型**：折叠蛋白质可以被精确地描述为离散非线性薛定谔方程的拓扑孤子系统。

这项工作为蛋白质物理学提供了一套强大的数学语言，它不仅补充了全原子分子动力学模拟的不足，也为理解蛋白质错误折叠疾病（如阿尔茨海默病）背后的拓扑机制提供了新的理论视角。未来，这种基于拓扑的分析方法有望从单链蛋白质扩展到更复杂的蛋白质复合物研究中。

  
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
