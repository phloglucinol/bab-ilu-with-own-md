---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247716057&idx=1&sn=d2fb93dd5d9e2cc0fcf9cb11e5bc99ec
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247716057&idx=1&sn=d2fb93dd5d9e2cc0fcf9cb11e5bc99ec
source_domain: mp.weixin.qq.com
title: 优化即几何，几何即推理：用数学终结Transformer的黑盒时代
author: 
published_at: 
fetched_at: 2026-04-25T02:04:03Z
extractor: wechat_worker
content_hash: 047f02efe66c1d9c66c5d8feeb0c40d9d83d297883c9439674c2d511c4402af8
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/VBcD02jFhgmvQDasddbj0Phadjb1JPicOeteibA1RaQoCCVRJrcn8mvHorbibw4ztak5eA6tI3QCeWM4df9xs9Bkg/0.jpg) 

# 优化即几何，几何即推理：用数学终结Transformer的黑盒时代

原创 让你更懂AI的 让你更懂AI的 [ PaperWeekly ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/Psho9dm7oDHKVtfYDubjKdZRUjAfBQQicXjoZWJ3qnK42ooD4eeJUfJBM4SSZVa2RE5lO0j6rWwzliby0j9u4bDg/640.gif)

  
## 

不是设计，而是进化。当交叉熵遇见 SGD，贝叶斯推理成了唯一的数学必然。

长期以来，LLM 的推理能力被视为一种难以解释的“涌现”。我们目睹了 Loss 的下降，却难以透视参数空间内部发生了什么。

  
近日，来自**哥伦比亚大学和** **Dream Sports** 的研究团队发布了一组三部曲论文。

  
这项工作并未止步于实验观察，而是建立了一个连接**优化目标 (Loss)**、**内部几何 (Geometry)** 与**推理功能 (Inference)** 的完整物理图景。  

  
它讲述了一个关于 LLM 如何运作的完整故事。其核心野心正如标题所言——试图用数学终结 Transformer 的黑盒时代。

  
他们证明了：**Attention 机制并非某种近似的特征提取器，而是在梯度下降的驱动下，自发演化出的一套精确的贝叶斯推理机。**
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wulOVRfC18yCkd6xXqGq22h6QUk8chptF0fnQ4uXeZtAktYMrWwG2SyQ/640.png)

理论锚点：交叉熵的贝叶斯终局

Transformer 的训练通常基于最小化交叉熵损失。Paper I 首先澄清了这一优化过程的数学终局。
  
  
论文标题：

The Bayesian Geometry of Transformer Attention

论文链接：

https://arxiv.org/abs/2512.22471

  
在无限数据与容量的极限下，最小化交叉熵 ：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOJicSggfbpMLbPngMUuIYf54PFzg1vBjsIw3Xvfq1pCh8HBBbr2gajcQ/640.png)
  
  
其最优解  在数学上严格等价于解析贝叶斯后验预测分布 (Bayesian Posterior Predictive Distribution)：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOtuxia0y9ibLDEEupUbeqenWZ3qh85eX6eaLD9pIVykGr5I4QtfnBdOgw/640.png)

  
为了验证有限容量的 Transformer 是否真正逼近了这一极限，作者构建了贝叶斯风洞 (Bayesian Wind Tunnels) 。

  
这是一个完全受控的数学环境，其中每一步的解析后验都是精确已知的。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOjQPIIoQiacdxLdIJ4vqpHy0et6FYZp2sLv16bzwXFvk2GicmoWXRsLlw/640.png)

〓 图1\. “贝叶斯风洞”概念图。在缺乏 Ground Truth 的自然语言之外，作者构建了一个可精确测量的受控环境。

实验结果表明，在双射学习与 HMM 状态追踪任务中，Transformer 展现了极高的精度。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOtf2NPc68hDccm9Uyze4hicqyAAVMqEAeMutpIaIh8M6KmGaB6lzRB2A/640.png)

〓 图2\. Transformer 的预测熵精确贴合理论贝叶斯后验，平均绝对误差（MAE）低至 10^{-3} 比特；相比之下，MLP 无法有效利用上下文进行假设消除。

更微观的证据来自单序列分析，这是证明模型真理解而非平均记忆的铁证：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOw781sibA5pQP8sHAwxhpKB2nkLibUxXe3qzdkibffEsLeWXibVJIYXMgAA/640.png)

〓 图3. 针对每一个具体序列，Transformer 的熵值（实线）能够精确追踪理论后验（虚线）的锯齿状变化，证明模型在进行逐 Token 的实时推理。

而在 HMM 任务中，模型甚至展现出了完美的长度外推 (Length Generalization) 能力，证明其学会了通用的递归算法：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOkw9rnpU3yS1VlMOicESOpjKpYpwXicVCkbzGunibicZmgQPIMlCSo15ykw/640.png)

〓 图4. 模型在训练长度 K=20 内完美拟合。在测试长度 K=30 和 K=50 时，误差平滑增长，未出现断崖式下跌，证明模型并未死记硬背。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuhfgUpIfdPSqH8YjjHbCUiaaKsMA36bIMsMtGNKoBcus5py06M0fvx3A/640.png)

几何表征：推理的三阶段演化

探针实验进一步揭示了 Transformer 内部如何实现这一推理过程。作者将其描述为一个三阶段的几何演化机制。

1\. 假设框架构建 (Layer 0)

推理始于坐标系的建立。第 0 层的 Key 向量形成了一个 近似正交的基底 (Orthogonal Basis)，将所有可能的假设映射到独立的几何子空间中。

〓 图5. Layer 0 的 Key 向量余弦相似度矩阵。非对角元素接近 0，表明模型构建了正交的假设空间框架。

2\. 渐进式假设消除 (Middle Layers)

随着层数加深，Attention 的路由 (Routing) 功能逐渐显现。Query 和 Key 的对齐程度呈现显著的锐化 (Sharpening) 趋势。

  
这一过程在数学上等价于贝叶斯更新中似然函数的乘法操作，逐层抑制与当前证据不符的假设。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOgiaxEJUSbgFMiczJ8m5JyameIN9uuAHqm6EPI3XWKDJnX0NW6hic7kySA/640.png)

〓 图6. 从 Layer 0（左）的发散关注到 Layer 5（右）的高度聚焦，展示了模型对错误假设的逐步剔除。

3\. 熵有序流形 (Late Layers)

当路由结构稳定后，Value 向量 () 在表示空间中并未坍缩为离散点，而是展开成一条光滑的一维流形 (1D Manifold)。

该流形的参数化坐标精确对应于后验熵 (Posterior Entropy)。

〓 图7. 训练后期，Value 向量的 PCA 投影形成了一条平滑曲线，低熵（高置信度）状态与高熵状态在几何上有序排列。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wukOjHSmSsEuRCB0fJu69CtdNgLnvFPDUCgeicOppBKuDvniaD3q8XWQ0Q/640.png)

动力学溯源：梯度下降的诱导机制

为何标准的梯度下降能够自发产生上述几何结构？

  
Paper II 通过全套一阶梯度动力学推导，发现交叉熵损失诱导了一套精妙的正反馈机制。

  
论文标题：

Gradient Dynamics of Attention: How Cross-Entropy Sculpts Bayesian Manifolds

论文链接：

https://arxiv.org/abs/2512.22473

1\. 优势路由法则 (E-step)

Attention Score () 的梯度遵循以下公式：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicO206oAetzPFMG7INGib6ut9uYdSKJWMZ8krMiaWzC8DsDOO3Nj9NuKgNA/640.png)

其中 。定义 Advantage 。

  
物理含义：这里  代表误差梯度方向。当  与误差方向相反（即  越负，有助于减少 Loss）时，Advantage 为正。

  
结论：梯度下降会增加那些能有效减少 Loss 的位置的注意力权重。

2\. 责任加权更新法则 (M-step)

Value () 的更新遵循以下公式：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicO1mdKa6hC8sF32zmQKM9X3GI0x5jMqx3Of4elDnvOpdK0TYprv7CfkQ/640.png)

  
物理含义：Value 向量会被拉向所有关注它的 Query 的上游误差信号 () 的加权平均方向，逐步演化为该簇 Query 的“原型” (Prototype)。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOD0aIwa4BqJX5tmQLatctG4oibno86UYmsYiaF8OEicLWDGdPo0fTwbicYg/640.png)

〓 图8. 动力学几何解释

Value  向误差信号  移动，优化 Context ，进而增加兼容性 （使其更负），形成路由与内容的协同演化闭环。

  
这一动力学过程在结构上等价于隐式的 EM 算法 (Expectation-Maximization)。Attention 权重充当 E 步的“软责任”，而 Value 向量充当 M 步的“原型”。

  
这也解释了框架-精度解离 (Frame-Precision Dissociation) 现象。Attention 结构通常在训练早期快速稳定，而 Value 内容则在剩余训练中持续在流形上精修。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuiaLfO9V4lkD8cXK7ImEicqib5bPGH6syOrWzicR2KaqPyAicMccs8icC03Gw/640.png)

现实映射：从叠加态到思维链

虽然上述结论基于受控环境，但作者在博客 \[3\] 中指出，在 Pythia, Llama, Mistral 等生产级模型中，同样观察到了类似的几何特征。  

  
关键在于叠加态 (Superposition)：在混合任务中，流形结构往往被高维噪声掩盖；但通过领域限制 (Domain Restriction)（如仅关注数学任务），高维表征会坍缩为清晰的熵有序流形 。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmvQDasddbj0Phadjb1JPicOiayyyUoH7TQIb42x2qBWJtmWwic5WpjqiaK5EgTPtiaeNVqFxTA8j1rFNQ/640.png)

〓 图8. 概念图展示了 Pythia、Llama 和 Mistral 内部在特定领域任务下涌现出的相似流形结构。

这一发现为 Chain-of-Thought (CoT) 提供了清晰的几何解释。

  
对于复杂推理任务，Transformer 面临层数耗尽 (Run out of layers) 的风险，无法在有限的计算步数内完成所有必要的假设消除。  

  
CoT 本质上起到了几何延展器 (Geometric Extender) 的作用。

  
通过生成中间推理步骤，模型实际上获得了更多的计算轮次，使其能够沿着高置信度的“熵有序流形”进行一系列短距离、稳健的状态转移，从而避免了在低置信度区域进行长距离跳跃所引发的幻觉。
  
  
![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wukGHdevfTibLOpic6945Lrhqmt43pKicyIhGs4m7ANzKOfY9RJgmTicZGdg/640.png)

**结语**

  
这项研究提供了一个统一的视角来理解 Transformer 的智能本质。优化产生几何，几何产生推理 (Optimization gives rise to geometry. Geometry gives rise to inference.) 。

  
参数矩阵并非随机的统计近似，而是梯度流在交叉熵势能面上“雕刻”出的贝叶斯推理机。

  
Attention 机制从几何动力学的角度来看，正是这一推理过程的物理载体。

  
![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/lpHDr05YrIRDN0iaJZR6j0k3hdCoOJyQBOzmoSYv4hnzD3Da34ibPg7uafy0CadjWfaIqaC7RiblTducI8fAvBnUf8O4WvMXAml/640.svg)

**参考文献**

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/lpHDr05YrIRDN0iaJZR6j0k3hdCoOJyQBOzmoSYv4hnzD3Da34ibPg7uafy0CadjWfaIqaC7RiblTducI8fAvBnUf8O4WvMXAml/640.svg)

\[1\] Naman Aggarwal, Siddhartha R. Dalal, Vishal Misra. The Bayesian Geometry of Transformer Attention. arXiv preprint arXiv:2512.22471 (2025). 

\[2\] Naman Aggarwal, Siddhartha R. Dalal, Vishal Misra. Gradient Dynamics of Attention: How Cross-Entropy Sculpts Bayesian Manifolds. arXiv preprint arXiv:2512.22473 (2025). 

\[3\] Vishal Misra. Attention Is Bayesian Inference. Medium (Dec 2025). https://medium.com/@vishalmisra/attention-is-bayesian-inference-578c25db4501

  
**更多阅读**

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDETRUPLvibIrbN7887TkTc4ovcxcVb6SkW8kc5rdV5yIn1RbYtMQdIyNBicjepybX8Sezhva6kibgEyQ/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247715048&idx=1&sn=4d77441dd965f7a80b4f2492d315f4be&scene=21#wechat%5Fredirect)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDETRUPLvibIrbN7887TkTc4o8iaM2MYeu2KLtia5McwTfNHYHxfjTq8FsCibmQLu8XPuT8NKHz2pwFOfA/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247714831&idx=2&sn=d5973381d8e4db08286dbc3f41314751&scene=21#wechat%5Fredirect)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDETRUPLvibIrbN7887TkTc4oncBBtTBtU8ial2JQ3XrsGQgiab0FzvEHibaU9PiaSuPrbBqxGNUkUL4fYg/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247714906&idx=1&sn=88f461e412fee53526da9f10e611d8ba&scene=21#wechat%5Fredirect)
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/Psho9dm7oDHHMXQ2IicFvJwssWxgWhKuK7ulQVyw7gPTxZia00vCxia2vzhRH6pGq8t1FN1zY48ibULAEZpic41k6eg/640.gif)

**#投 稿 通 道#**

 **让你的文字被更多人看到** 
  
  
如何才能让更多的优质内容以更短路径到达读者群体，缩短读者寻找优质内容的成本呢？**答案就是：你不认识的人。**

  
总有一些你不认识的人，知道你想知道的东西。PaperWeekly 或许可以成为一座桥梁，促使不同背景、不同方向的学者和学术灵感相互碰撞，迸发出更多的可能性。 

  
PaperWeekly 鼓励高校实验室或个人，在我们的平台上分享各类优质内容，可以是**最新论文解读**，也可以是**学术热点剖析**、**科研心得**或**竞赛经验讲解**等。我们的目的只有一个，让知识真正流动起来。

  
📝 **稿件基本要求：**

• 文章确系个人**原创作品**，未曾在公开渠道发表，如为其他平台已发表或待发表的文章，请明确标注 

• 稿件建议以 **markdown** 格式撰写，文中配图以附件形式发送，要求图片清晰，无版权问题

• PaperWeekly 尊重原作者署名权，并将为每篇被采纳的原创首发稿件，提供**业内具有竞争力稿酬**，具体依据文章阅读量和文章质量阶梯制结算

  
📬 **投稿通道：**

• 投稿邮箱：hr@paperweekly.site 

• 来稿请备注即时联系方式（微信），以便我们在稿件选用的第一时间联系作者

• 您也可以直接添加小编微信（**pwbot02**）快速投稿，备注：姓名-投稿

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgmic1CRCSOKfDibC3dZ4BaJuYyYTWJyw8gFxqon34STk3icf9aJbY4rqMpmhNjTGJXIGGFsCdTBHy3Tw/640.png)

**△长按添加PaperWeekly小编**
  
  
🔍

  
现在，在**「知乎」**也能找到我们了

进入知乎首页搜索**「PaperWeekly」**

点击**「关注」**订阅我们的专栏吧
  
  
·

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgnZ3nlEAOI3MyTd7jqeD6cq8uTbkM2xZNpribyNr9liaPJ722zaHxd0YpQvib2nxOYmWibydCVY7W94ew/640.jpg)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgklOsJKfNKCYFCiaBOjViaarib352vjdQc2vvcV7BEicdEsZJEonTkeZMsqh3nx2s1NzAUmsRNHM7Og3Q/0.png) 

 PaperWeekly 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhgklOsJKfNKCYFCiaBOjViaarib352vjdQc2vvcV7BEicdEsZJEonTkeZMsqh3nx2s1NzAUmsRNHM7Og3Q/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
