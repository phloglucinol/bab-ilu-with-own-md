---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4ODkwMjUxNw%3D%3D&mid=2247484400&idx=1&sn=f204aee2ea42521b86550c0ebf7ebe89
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4ODkwMjUxNw%3D%3D&mid=2247484400&idx=1&sn=f204aee2ea42521b86550c0ebf7ebe89
source_domain: mp.weixin.qq.com
title: JCIM | RDKit 又报错？深度解析为何 3D 生成模型需要“概率化”的后处理 | Bits &amp; Bases #018
author: 
published_at: 
fetched_at: 2026-04-25T02:03:35Z
extractor: wechat_worker
content_hash: 12b533cd23c1c0205b28eec1a7241e1ea445687c1384799d6687c9e4eb5ccf89
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/0LlI74ApO0nxkvHy3ibrnu5dIrVgPP5Sq2tKW0cHbbENe899iaPse8nqcIYrlKzSYJzNAM9SNuK2RRFF5HxTFmJw/0.jpg) 

# JCIM | RDKit 又报错？深度解析为何 3D 生成模型需要“概率化”的后处理 | Bits & Bases #018

Rhona Rhona [ Bits & Bases ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

👆 点击上方 Bits & Bases 加入我们

🧬 Bits & Bases #018 (Part 1)  
理论与应用 | 求解几何-拓扑映射的“病态逆问题”：YuelBond 的概率图视角  
  
阅读时间：约 12 分钟 | 难度：⭐⭐⭐

## 00\. 文献档案 (Paper Profile)

> ❝
> 
> **题目**：Multimodal Bond Reconstruction toward Generative Molecular Design   
> **期刊**：_J. Chem. Inf. Model._ (JCIM)   
> **发表时间**：2026年   
> **通讯作者**：Nikolay V. Dokholyan (UVA)  
> **导读**：AIDD 生成模型的“最后一公里”往往受阻于 RDKit 的刚性规则。本文提出 YuelBond，将化学键重建重构为噪声几何条件下的概率推断问题，从根本上解决了 3D 生成模型输出的 Sanitization 难题。

---

## 01\. 核心困境：当 CSP 遇上 Manifold

在 AIDD 的生成范式中，我们实际上是在强行拼接两个数学性质截然不同的世界：

* **生成端（流形假设）**：Diffusion Model 假设分子是高维流形上的点。它生成的  是连续的，本质上带有  级别的热涨落（Noise）。
* **校验端（离散约束）**：RDKit 的 `DetermineBonds` (`xyz2mol`) 本质上是一个 **约束满足问题 (Constraint Satisfaction Problem, CSP)** 。它要求存在一个图 ，使得所有原子间距离  和化合价 **同时严丝合缝地满足**预设规则。

**The Incompatibility (不可通约性)。**这就是为什么 `Sanitization Failed` 如此频发。生成模型输出的坐标，往往落在化学流形的 **切空间 (Tangent Space)** 附近，稍微偏离了理想几何一点点。

* **对于物理世界**：这只是构象的柔性（Flexibility），是合理的。
* **对于 CSP 求解器**：这是**无解 (Infeasible Solution)** 。方程组出现了矛盾（超定），算法无法收敛，只能抛出异常。

我们需要停止用 CSP 的刚性逻辑去处理流形上的柔性噪音。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/0LlI74ApO0nxkvHy3ibrnu5dIrVgPP5SqqibgzAM2BNM2PH6aD9Uu4DOw0zkS9qh1dRVc0Db24terlPZVic2eNs6A/640.png)

▲ Figure 3\. 确定性算法的崩溃。在引入 Å 的高斯噪声后，RDKit 的 CSP 求解器在 78.3% 的样本上失效，而 YuelBond 保持了 100% 的鲁棒性。

---

## 02\. YuelBond 的本质：贝叶斯视角的重构

YuelBond 的出现，标志着我们将后处理从 **“规则求解”** 转向了 **“概率推断 (Probabilistic Inference)”**。

它不再试图硬性判断“这个距离是不是单键”，而是回答一个贝叶斯问题：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/0LlI74ApO0nxkvHy3ibrnu5dIrVgPP5SqIEibGMtlTP6wMhXB55XokpIrcib8cSWzeF4dp9m2NWQuMlB1iaibWzQloQ/640.png)

  
▲ Figure 1\. 概率推断框架。不同于传统算法的硬规则匹配，YuelBond 采用 Edge-Centric GNN 聚合局部环境特征，将含噪几何映射为化学键的概率分布。

**为了实现这一推断，它引入了两个关键的归纳偏置 (Inductive Biases)：**

1. **非局部性 (Non-locality) —— 从“近视”到“广角”**：
   * **RDKit 的局限**：它是“近视”的，只看两体距离 。如果 Å，它就认为是单键，它看不见这两个原子是不是在一个苯环里。
   * **YuelBond 的突破**：通过堆叠多层 Edge-Centric GNN，模型获得了广阔的 **感受野 (Receptive Field)** 。边  的更新不仅依赖于端点，还聚合了 \-hop 子图的拓扑信息。
   * _这意味着_：即便苯环上的某个  键被噪音拉伸到了 1.5Å（在 RDKit 眼里是单键），但 YuelBond 能“看到”它处于一个共面的六元环结构中，从而利用**上下文置信度 (Contextual Confidence)** 修正局部几何的偏差，正确判定为芳香键。
2. **软约束 (Soft Constraints) —— 从“硬过滤”到“软先验”**：
   * **RDKit 的局限**：它将化合价规则视为 **Hard Filter**。一旦出现价态冲突（例如生成模型让氮原子连了 4 根键），整个分子直接判废 (Sanitization Failed)。
   * **YuelBond 的突破**：它将化学规则内化为 **Soft Priors**（习得的分布模式）。模型输出的是键级的 **Categorical Distribution**（分类分布）。
   * _这意味着_：面对生成模型中常见的“过渡态”或“亚稳态”几何，YuelBond 不会直接报错，而是寻找一个**“违规程度最低”**的最大似然解，或者保留这种不确定性（通过 Entropy 体现），为后续优化留出空间。

---

## 03\. 实验洞察：从“修复”到“势能优化”

为了量化 YuelBond 在生成管线中的价值，作者在 DiGress (2D) 和 DecompDiff (3D) 两个 SOTA 模型上进行了测试。

#### 3.1 拯救“非法”分子

| 生成模型           | RDKit Sanitize Rate | YuelBond Refined Rate |
| -------------- | ------------------- | --------------------- |
| **DiGress**    | 81%                 | **95%**               |
| **DecompDiff** | 76%                 | **94%**               |

#### 3.2 Log Probability 的深层含义

作者不仅比较了通过率，还强调了 **Log Probability Scores** 的提升。 这不是一个简单的分类分数，它代表了 **拓扑势能 (Topological Potential)** 的优化。

* **优化前**：生成模型的几何结构  与其默认推断的键级  存在“逻辑张力”（例如：几何上是平面的，但拓扑上被标为 ）。
* **优化后**：YuelBond 找到了一个最大似然的键级分配 。

**关键结论**：YuelBond 并没有移动原子（Geometry 没变），但它通过修正拓扑定义，消除了分子内部的物理矛盾。对于下游任务（如 MD 模拟或 FEP）来说，这意味着力场参数分配将更加合理，从而避免模拟发散。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/0LlI74ApO0nxkvHy3ibrnu5dIrVgPP5Sq8WaxrI0yhOfeAYictaNL3FembTpbqt8icicFO0CHRlNjlHR9aUDv9DMqA/640.png)

  
▲ Figure 6\. 相容性的提升。YuelBond 处理后的分子（绿色）不仅合法率更高，其 Log Probability 的提升表明键级分配与几何结构的物理一致性显著增强。

---

## 04\. 总结与展望：迈向概率化的后处理

YuelBond 的成功揭示了 AIDD 流程中被忽视的一环：**Interfaces (接口)** 。

在“连续生成的模型”与“离散模拟的世界”之间，我们需要一个**概率化的转换层**。

* 这个层必须是 **Differentiable (可微的)** ，以便未来可以回传梯度指导生成。
* 这个层必须是 **Noise-tolerant (抗噪的)** ，以适应生成模型的随机性。

YuelBond 是目前填补这一生态位**极具竞争力的解法**，也是从规则走向学习的**典型代表**。

但硬核的问题来了： 面对 **共振结构 (Resonance)** 和 **互变异构 (Tautomerism)** 这种连量子力学都很难定义的模糊地带，YuelBond 是如何通过 **Edge-Centric 架构** 和 **自回归采样** 来捕捉这些长程依赖的？

我们将在下期技术详解中，深入其 GNN 内核。

  
📢 下期预告  
  
技术拆解 | 概率图模型的实现：Edge-Centric GNN 与链式采样  
我们将深入代码与公式层面，解读 YuelBond 如何实现对化学键  
联合概率分布 (Joint Probability Distribution) 的建模。

  
---

**References**  
\[1\] Wang, J., & Dokholyan, N. V. (2026). _Multimodal Bond Reconstruction toward Generative Molecular Design._ JCIM.  
\[2\] Guan, J., et al. (2024). _DecompDiff: Diffusion Models with Decomposed Priors for Structure-Based Drug Design._  arXiv.  
**Disclaimer**  
 本文为学术笔记，旨在交流分享。准确定义请以原论文为准。文中部分配图引自原论文。

Bits & Bases

专注 AI for Science · 论文拆解 · 博士生笔记

![Image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/0LlI74ApO0l1lYTGRiaNhz5skwLKhfKXAIpPVb3ibnHp9sOBzRQ2wHiaR3icMSTmpWUZ6S0naS8d3ESWnHQY6GoCRg/640.jpg)

  
👆 长按扫码，不错过每一篇硬核干货

  
© Bits & Bases | 专注 AI for Science 解读

  
预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/0LlI74ApO0lPHPibiaVWrfFqQpPP2L7gNIoI4AEgZI9icElp0Ro35FMsic4ibQQpicEmD7nrKx5lox4frbNSrIjAfjHg/0.png) 

 Bits & Bases 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/0LlI74ApO0lPHPibiaVWrfFqQpPP2L7gNIoI4AEgZI9icElp0Ro35FMsic4ibQQpicEmD7nrKx5lox4frbNSrIjAfjHg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
