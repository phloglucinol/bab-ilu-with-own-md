---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247716247&idx=1&sn=584edb6041579a68d396bb9a3f0c278f
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247716247&idx=1&sn=584edb6041579a68d396bb9a3f0c278f
source_domain: mp.weixin.qq.com
title: 别再把KL散度加进loss了！Bengio团队实证：回归Reward才是无偏正解
author: 
published_at: 
fetched_at: 2026-04-25T02:04:03Z
extractor: wechat_worker
content_hash: 1d03e2834b50394b4f00d864901e49f826dff761b063c95bb2e76358e10a8559
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQ3TeNvWuXL3ia5p0npcqDETvLI479phoSHRicvcUlBQh3Pwzcq0cmJaFQ/0.jpg) 

# 别再把KL散度加进loss了！Bengio团队实证：回归Reward才是无偏正解

原创 让你更懂AI的 让你更懂AI的 [ PaperWeekly ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/Psho9dm7oDHKVtfYDubjKdZRUjAfBQQicXjoZWJ3qnK42ooD4eeJUfJBM4SSZVa2RE5lO0j6rWwzliby0j9u4bDg/640.gif)

  
## 

全网都在卷 RLVR，但 Bengio 团队刚泼了盆冷水。

  
DeepSeek-R1 的爆火让 RLVR 成为当下大模型后训练的绝对主流。

  
无论是 PPO 还是近期大热的 GRPO，核心逻辑都是一致的：在最大化 Reward 的同时，利用 KL 散度约束策略模型  不偏离参考模型 。

这个逻辑听起来天经地义，但在工程落地时，我们往往面临一个极其隐蔽的选择。这个 KL 惩罚项，到底是应该减在 reward 里，还是直接加在 loss 里？

  
绝大多数开源库（如 VeRL, OpenRLHF, SkyRL）为了实现方便，默认将特定的估算器（如 K3）直接置于 Loss 中。

  
然而，Mila 实验室（Bengio 团队）的最新研究《A Comedy of Estimators》给这种约定俗成的做法泼了一盆冷水。

  
这项研究指出目前主流的 KL 实现方式，在数学上其梯度估计是有偏的（Biased）。这种偏差不仅会导致训练不稳定，更严重的是会损害模型的泛化能力。

  
而修复方案出奇简单，返璞归真地将 KL 移回 Reward 并使用朴素 K1 估算器，就能在域外任务（OOD）上带来近 20% 的性能提升。

  
本文将剥开繁复的代码实现，从数学本质出发，带你避开这个 LLM RL 训练中的梯度陷阱。
  
  
论文标题：

A Comedy of Estimators: On KL Regularization in RL Training of LLMs

论文链接：

https://arxiv.org/pdf/2512.21852
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wulOVRfC18yCkd6xXqGq22h6QUk8chptF0fnQ4uXeZtAktYMrWwG2SyQ/640.png)

KL散度的计算困境

在 RLVR 的标准设定下，我们的优化目标非常明确。既要最大化奖励 ，又要约束策略模型  不偏离参考模型 。

  
这通常通过在目标函数中加入反向 KL 散度 (Reverse KL Divergence) 来实现：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQiadolQzSxYoFTLJA3lHibRa5pq0oKDAzNVVBLvFJfJEvv0q6oIibiaONsg/640.png)

其中  是正则化系数。但在实际操作中，面对高维序列空间，我们无法直接计算 ，只能通过采样估算。这里涉及到两个核心变量：  

1\. 估算器 (Estimator)：是用朴素的 Log-ratio（称为 K1），还是用 PPO/GRPO 中常用的低方差近似项（称为 K3，由 Schulman 提出）？

2\. 位置 (Placement)：是作为惩罚项从 Reward 中扣除 (In-Reward)，还是作为正则项直接加入 Loss 函数 (In-Loss) ？

目前的行业现状是：为了工程实现方便或沿袭惯例，绝大多数开源库（如 VeRL, SkyRL 等）默认选择 K3 in Loss。但 Bengio 团队告诉我们：这可能是个错误的决定。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuhfgUpIfdPSqH8YjjHbCUiaaKsMA36bIMsMtGNKoBcus5py06M0fvx3A/640.png)

被忽视的梯度偏差

判断一种实现方式是否正确，唯一的标准是看它的梯度是否与真实梯度 (True Gradient) 一致。

  
对于序列级反向 KL 散度，其真实梯度的数学形式如下 ：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQtqE87W9SOficsQEaTCr8bxGAmryfIDuqpASZnRya8vy1iaR4aWxyg3oQ/640.png)
  
  
论文对四种常见的“估算器+位置”组合进行了详尽的梯度推导，结果与直觉截然相反。
  
  
〓 表1\. 不同估算器配置的梯度偏差与训练行为总结。

  
注意 K3 in Loss 虽然稳定但有偏，只有 K1 in Reward 兼顾了无偏与稳定。

  
最反直觉的点在于 K3 in Loss（主流方案）虽然工程上表现稳定，但其梯度在数学上是有偏的 (Biased) 。而 K1 in Reward，虽然看起来最原始，却是唯一既无偏又稳定的最优解。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wukOjHSmSsEuRCB0fJu69CtdNgLnvFPDUCgeicOppBKuDvniaD3q8XWQ0Q/640.png)

为什么K3 in Loss是错的？

当我们把 K3 放入 Loss 直接进行反向传播时，推导出的梯度期望包含了一个错误的系数项：
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQnUlHy03A8YQPUlsibdu8wCyE7VGgJQMcfKRju3jXQb6IRAPB4JZPO6A/640.png)

  
论文明确指出（Eq 41），这个梯度形式实际上是在优化前向 KL 散度：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQSrwS8ysQrzBnLYpgZtgowZE35MB47MibZN6ZqdvjF22RNFuME8GHhGw/640.png)

  
这导致模型倾向于去覆盖参考模型的分布（Mode-covering），而非我们期望的寻找高奖励模式（Mode-seeking）。  

为了直观展示这种偏差，作者构建了一个极简参数化模型（Toy Model）进行验证。

〓 图2\. 极简自回归模型下各估算器的梯度偏差（左）与方差（右）。K1 in Reward（点线）的偏差接近于 0，而 K3 in Loss（虚线）存在显著的偏差。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuiaLfO9V4lkD8cXK7ImEicqib5bPGH6syOrWzicR2KaqPyAicMccs8icC03Gw/640.png)

实验结果

理论上的偏差真的会影响 LLM 的推理能力吗？作者在 Qwen2.5-7B 和 Llama-3.1-8B 上进行了大规模的 MATH 数据集微调实验。

  
1\. 训练稳定性：避坑K3 in Reward

首先，千万不要尝试 K3 in Reward。实验表明，这种配置会引入巨大的梯度方差，导致模型训练瞬间崩溃。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQXujqKs3n0AMUZbudLzhCbMicsP4f7CynyUnrOYBpBLHkUx4qBZRH0fw/640.png)

〓 图3\. 如图所示，K3 in Reward 会导致 Pass@1 准确率直接跌零。

  
2\. 泛化能力：K1 in Reward的降维打击

这是本研究最核心的发现。作者对比了 K3 in Loss（有偏，主流方案）和 K1 in Reward（无偏，推荐方案）在域内（MATH）和域外（Physics, Chemistry, Biology）任务上的表现。
  
  
〓 图4\. Qwen2.5-7B 在不同 KL 配置下的性能对比。浅绿色 (K1 in Reward) 代表无偏方案，灰色 (K3 in Loss) 代表主流有偏方案。  

  
数据极其惊人，K1 in Reward 在所有任务上均优于或持平于 K3 in Loss。特别是在 OOD 任务上，优势呈现碾压之势。

  
例如在 Physics 任务上（），K1 in Reward 达到了 0.508 的准确率，而 K3 in Loss 仅为 0.429。平均而言，无偏估计在 OOD 任务上带来了约 19% 的相对提升。  

  
这意味着无偏的梯度估计能让模型学到更本质的推理逻辑，而不是仅仅死记硬背训练集的分布。  

  
3\. 异步训练下的鲁棒性

工业界（如 DeepSeek）通常使用异步架构（Asynchronous RL）来提升训练效率，这会引入 Off-policy 滞后。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQzrttoATuZneryVmqIUrUOhpPo1p6RC7TS9qthCKpiaQTicMET1eLakLQ/640.png)

〓 图5\. 高并发异步设置 (Async Level=10) 下的训练曲线。

  
在 Dr. GRPO 架构下，K1 in Reward（灰色线）依然稳健，而其他配置（如 No KL 或 K1 in Loss）迅速崩盘。

  
实验证明，在 Dr. GRPO 等异步架构下，K1 in Reward 依然是防止模型崩坏的鲁棒性保障。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wukGHdevfTibLOpic6945Lrhqmt43pKicyIhGs4m7ANzKOfY9RJgmTicZGdg/640.png)

为什么无偏这么重要？

为了彻底证实梯度无偏性是性能提升的根本原因，作者做了一个精妙的控制变量实验。

  
如果你费劲地把 K3 同时加入 Reward 和 Loss 以凑出无偏梯度，效果会怎样？

〓 图6\. 一旦梯度被修正为无偏（右侧柱状图），K3 的表现立刻追平了 K1。

  
**这说明估算器叫什么不重要，重要的是数学上的 Unbiased。**

**进一步的熵分析显示，K3 in Loss 的行为更像是一种 Forward KL 正则化，它倾向于让模型“覆盖”参考模型的分布（Mode-covering）。**

**而 K1 in Reward 则表现出 Reverse KL 应有的 Mode-seeking 特性，允许模型在保持低熵（更自信）的同时探索高奖励区域。**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQB2VU97fCiazWIeEsXRg4rIOBVrwJnD8EGD1VCgzWFSBMqNfQ4ibBbJwQ/640.png)

〓 图7\. 熵 (Entropy) 与前向 KL 分析。K1 in Reward (深色线) 保持了更低的熵，体现了 Mode-seeking 特性。  

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuJXXicvv3JrPNYrFlYadg4ibA8SxC6OvibZyBHGuub04X1AXxeRTC0WUJA/640.png)

**结语**

这篇论文给火热的 RLVR 泼了一盆必要的冷水，提醒我们在追求算力堆砌的同时，不要忽视数学本源的严谨性。  

  
对于正在使用 VeRL 或 OpenRLHF 等框架的一线从业者，建议参考以下配置表进行修改，以获得“免费”的性能提升。  

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/VBcD02jFhglCfnY2AWCQiaSXiabFbfl6bQae2Zar0O5NIvLyGojrRqMBvWpS6KDI87XBNiaPEmKXiaMY4WNWvZgCbg/640.png)

〓 表2\. 针对 VeRL 和 OpenRLHF 的代码配置修正指南。核心是将 KL 估算器类型设为 "k1" 并开启 "use\_kl\_in\_reward"。

  
一句话总结：别再盲目信任默认配置了。把 KL 惩罚项从 loss 移回 reward，用最简单的 K1 估算器，你可能会发现你的模型比你想象的更聪明。

  
**更多阅读**

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDEIjnsdmcibpmUEicctXJn2BO0AX9JO5sZtCf1IKh4muZWVicnR8KckNrMmKBkBuBNntZibvZTrGiao2XQ/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247709834&idx=1&sn=2986fb95731ad97b3c473dad0bec0ad1&scene=21#wechat%5Fredirect)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDEIjnsdmcibpmUEicctXJn2BOVsB1OYIuQmdU7keLGuNgux2icx0ArbgggzyeTkYtMibUovJEbvUlLDsg/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247709503&idx=3&sn=eede2987d8a2ac7125285ebfb7aa9d1f&scene=21#wechat%5Fredirect)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDEIjnsdmcibpmUEicctXJn2BOsVNDKsAwGqXKE7pFZiahRYZnNpfysfibauP3xnnxJMcxcniaSS4cWEO2g/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247709412&idx=2&sn=b9fd526b87e266001c746686cb9c2078&scene=21#wechat%5Fredirect)
  
  
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
