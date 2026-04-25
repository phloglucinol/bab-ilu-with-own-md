---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719075&idx=1&sn=941220588e7309aaecfa9f766de7c442
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719075&idx=1&sn=941220588e7309aaecfa9f766de7c442
source_domain: mp.weixin.qq.com
title: 嫌Muon太吃算力？Mamba作者团队巧用Gram矩阵，实测提速两倍
author: 
published_at: 
fetched_at: 2026-04-25T02:03:14Z
extractor: wechat_worker
content_hash: da04b9dc32c7631959fa46e5e16a82c2136254035ef85d00237fabe96483c676
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/nFNzd9xjFeD6T9QtaU16MSWibrXQNeicJLmVovicz13OMr6OhdrHQHxUsNsjUhPRXpSm2KlYYyZsAsYbpwa9GNFPBwibOsre1jYleDJviaPR0Kuc/0.jpg) 

# 嫌Muon太吃算力？Mamba作者团队巧用Gram矩阵，实测提速两倍

原创 让你更懂AI的 让你更懂AI的 [ PaperWeekly ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/Psho9dm7oDHKVtfYDubjKdZRUjAfBQQicXjoZWJ3qnK42ooD4eeJUfJBM4SSZVa2RE5lO0j6rWwzliby0j9u4bDg/640.gif)

  
## 

万亿模型训练的免费午餐，一个数学 trick 让 Muon 提速 50%。

  
在万亿参数大模型的竞逐中，训练效率的细微差距往往关乎巨大的算力成本。近期，Kimi K2 与 GLM-5 等前沿语言模型开始广泛采用 Muon 优化器。

  
对比 AdamW，Muon 达到特定损失值所需的优化器步数更少，但单步计算开销显著增加。

  
这种开销主要来自 Newton-Schulz 正交化过程，引入了早期优化器中不存在的三次方时间复杂度矩阵运算。

  
〓 Muon 与 AdamW 单步实际运行时间的对比

  
为突破该算力瓶颈，普林斯顿大学 Tri Dao 团队（Mamba 与 FlashAttention 核心作者）联合纽约大学研究人员提出了 Gram Newton-Schulz 算法。

  
在万亿参数 MoE 模型训练中，该算法将正交化步骤的端到端耗时有效降低了 40% 至 50%。

  
目前团队已将该算法开源，作为标准 Muon 优化器的即插即用替换模块，无需繁琐配置即可直接获得加速收益。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeAw4dsaIiaY54x5siaLh8qxkOM1MdQl1QZcwmVbplVlfNeVica0LcQUlb6nMbyOu498lYHVEuX7mebWsGnkZ8Kduias8UekgZrItFs/640.png)

  
文章标题：

GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization

文章链接：

https://dao-lab.ai/blog/2026/gram-newton-schulz/

项目链接：

https://github.com/Dao-AILab/gram-newton-schulz

核心算子链接：

https://github.com/Dao-AILab/quack/blob/main/quack/gemm\_symmetric.py

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wulOVRfC18yCkd6xXqGq22h6QUk8chptF0fnQ4uXeZtAktYMrWwG2SyQ/640.png)

为什么标准算法这么慢？

  
传统优化器（如AdamW）执行逐元素操作，时间复杂度为 。

  
Muon 等现代优化器需要进行正交化，单步计算需要耗费  的时间（假设 ）。

  
Muon 的更新规则基于对动量矩阵  的极分解：
  
  
由于极分解  精确计算成本高昂，Muon 采用 Newton-Schulz 多项式迭代进行近似：
  
  
现代 Transformer 架构（特别是包含大量细粒度专家的 MoE）的权重矩阵形状大多是不规则的矩形，满足 。

  
标准 Newton-Schulz 需要在庞大的矩形矩阵上执行多次乘法，矩形矩阵乘法完全主导了整体计算成本。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeBR14rvaGrRniaAOZ9LKXY3ADKhjHPiaImJCm4fvyV95zsnlHCnQgGUfZt0FdtpeZibRso2kpdMaz7ENajSkjicHjW7pCFX5ukEYcI/640.png)

〓 包含大量昂贵矩形矩阵乘法的标准 Newton-Schulz 伪代码
  
  
更关键的是，算法执行期间产生的诸多中间矩阵具备对称结构，常规计算路线未能有效利用这一数学特性，导致半数计算工作冗余。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeDjetmlgs3muL23KAA7LicIib5c8QYqs7Zp4icxXmI1vDmyNvnmENkoQCGE9SmicUGGfRVyia7kJ5xJnPuscSxSmAlZm6raxFroTHxY/640.png)

〓 标准 Newton-Schulz 在 Hopper 架构下的纯算子优化收益

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuhfgUpIfdPSqH8YjjHbCUiaaKsMA36bIMsMtGNKoBcus5py06M0fvx3A/640.png)

Gram矩阵的数学重构

算法的核心在于转移迭代空间：不再对庞大的矩形输入矩阵  进行迭代，而是转移至尺寸更小且对称的方形 Gram 矩阵 。

  
极分解可表示为 。通过多项式的代数变换，Newton-Schulz 迭代隐含了计算逆平方根的过程。

  
核心迭代可转化为以下标量形式：
  
  
矩阵操作保留了奇异向量，该标量迭代逻辑可直接推广至矩阵空间。空间转换后，算法主体在  的对称矩阵内运行，极大削减了浮点运算次数。

  
在典型的  场景下，相较于未优化的标准实现，该方法理论上可节省 68% 的浮点运算次数。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wukOjHSmSsEuRCB0fJu69CtdNgLnvFPDUCgeicOppBKuDvniaD3q8XWQ0Q/640.png)

解决数值不稳定

上述理论在精确算术下完全等价，但在真实的半精度计算环境下会引发严重的数值不稳定。研究团队通过算法与硬件的协同设计，化解了这一工程隐患。  
  
  
重启策略

  
在 bfloat16 精度下计算 Gram 矩阵  会产生由于浮点误差导致的伪负特征值。由于更新规则包含平方项，初始微小的负特征值会随迭代呈指数级放大，最终导致数值崩溃。

  
研究团队引入了重启策略，在算法执行至中途时，利用当前的近似结果重新构造 Gram 矩阵，消除累积的负特征值并重置状态。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/nFNzd9xjFeA0bPL2FSlgSQBhqMHgwRkWeN7fITGeAZyU9jc3Er0u1gKkXHvEZvQLiaqibxsZibDic3Cq3ltlt4Dy3yo45ic6ejcsub0Gkj46cUFg/640.gif)

〓 引入重启策略后的特征值演变与稳定收敛
  
  
代数重排

  
在计算矩阵二次型时，常规方法会显式加上单位阵 。底层算子在执行该加法时，会先在 float32 下计算并由于输出限制向 float16 截断，导致后续乘法累积严重的精度损失。

  
团队重排了代数逻辑，将加法操作隐式融入后续计算，即先算 ，再在后续步骤中分配  的运算，全程在 float32 下保持高精度，消除了隐藏的数值隐患。  

  
精度回退决策

  
针对 bfloat16 的动态范围大但精度位数不足的问题，算法在初始化阶段默认将输入张量转换为 float16。

  
由于矩阵范数已被严格控制在 1 附近，float16 在这一小区间内能提供更高的尾数精度，进一步夯实了数值基础。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeBg3tH4Zm1qflS10xWicZyWcGqj395hmcJkoBxBP3mJg22T6D9CUNWHcNRWoOge05HqFHzLCcvzibuOr5Wov4asicWW035hbDUJEU/640.png)

〓 稳定的 Gram Newton-Schulz 算法伪代码
  
  
权重拆分策略

  
工程实现中，团队特别强调了将 SwiGLU 架构中的  和  拆分后独立进行正交化。

  
由于这两部分对激活函数的梯度贡献机制不同，拆分处理不仅使 Llama-430M 的验证集困惑度优化了约 0.2，更通过减半矩阵的小维度，使得依赖  复杂度的 Gram Newton-Schulz 获得了更显著的提速比例。  
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeDYoib3tOd4gjrr9QjzPCf9tfFTveaibsJxZQYRDwzhA04MNs5IVcGKCun4MvZzpKtHNc9BDptxAnI4aJ3k5ShG66jBEPFSqgbZE/640.png)

〓 不同形状权重矩阵的单步耗时拆解（极端矩形权重加速最显著）
  
  
定制三角形调度器

  
在底层算子层面，为最大化 Gram 矩阵对称性带来的计算红利，团队基于 CuTeDSL 针对 Hopper 和 Blackwell 架构开发了定制算子。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeCzpblAwmyUia8nwkc3OXsJDEiaDLevAtibJYWiao7RGibfMQDGgEr4jG73Pu53ypG09cyW4oLM3fNVXrjOOr6xZuOeedO1GWKU5KTQ/640.png)

〓 对称矩阵乘法的三角形调度器示意
  
  
其核心是一个三角形调度器，仅将矩阵下三角区域的工作块分配给计算集群，并在底层内存回写时转置复制至上三角位置，确保负载均衡并消除冗余的内存访存。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeAVdTjB0RaWwUd9MXkVyQHJw2bu2eYSNzMXqZcZBiaoCZWInQSysOnDLqEMEBqNkT3O95cPHKOZia2gR9cCKXfjmPIFV0RsCCfOQ/640.png)

〓 定制对称算子与 cuBLAS 在不同架构下的 TFLOPS 吞吐量对比

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuiaLfO9V4lkD8cXK7ImEicqib5bPGH6syOrWzicR2KaqPyAicMccs8icC03Gw/640.png)

实验验证与工程收益

在 Llama-430M、Qwen-600M、Gemma-1B 以及 10 亿参数规模的 MoE-1B 模型上进行的对比实验表明，使用 Gram Newton-Schulz 与原版 Muon 的验证集困惑度差异严格控制在 0.01 以内。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeDicQpq9361n3DlyibicApUGFk1yJPgBuZejxBG8duGkMENTB8zNEv9ChSS7AFxImkNhj4xsQhxWuROHeaLNZq7pX9cstwBYg5XV4/640.png)

〓 不同模型上的验证集困惑度对比（Hopper 架构）
  
  
在实际训练耗时方面，新算法配合定制算子切实缩短了正交化的端到端耗时。

  
在模拟 Kimi K2 模型特定流水线阶段的真实并行负载测试中，Gram Newton-Schulz 实现了 2 倍的端到端正交化加速。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeA06tHeohtc1rRXUzpoxgMaoIJ1mqkjcmZfLDp6NcY8zvicyMEE4SVX8vOD9ibngnzfQtNW9dMoYY23aXgIzXibtV7Arj1pxCEgmw/640.png)

〓 Kimi K2 流水线切片下的端到端耗时对比

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wukGHdevfTibLOpic6945Lrhqmt43pKicyIhGs4m7ANzKOfY9RJgmTicZGdg/640.png)

结语

Gram Newton-Schulz 通过底层的数学逻辑重构与针对性的数值稳定性修复，以及 GPU 架构级别的定制算子优化，打通了现代优化器在大规模并行训练中的效率瓶颈。

  
这为极度消耗算力的矩阵正交化问题提供了一条可行路径，也再次印证了算法与硬件协同设计的实用价值。

  
目前，研究团队已将 Gram Newton-Schulz 完整开源。在实际工程应用中，唯一需要微调的超参数仅为重启迭代的节点。

  
为此，开源库中提供了一个自动化调参脚本，只需输入一组多项式系数，即可自动分析并建议最优的重启节点。

  
这套兼具理论深度与工程可用性的工具，为受限于算力瓶颈的大模型训练提供了一份切实可用的优化方案。

  
**更多阅读**

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/RBRgSeVXhYOMbu1Q6xTmJb7niczMUhicyMILIulq5JUqJibnQMMVjh336icllT8F201TJo6xQqC1OpMuibjFjic52gZC7bLob902Labc2MRtGKJwQ/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247701843&idx=1&sn=817c0b9a4589052831da2170c0157ec0&scene=21#wechat%5Fredirect)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/RBRgSeVXhYN8zYiczzgueonRic6rPnsRtjba0NfpF8F57dKfngutdgvrudVJS3ET1GfMNC7Uibv3rLUwjk72mpYokZzhRJpAXW9iamjsqtKHuLo/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247718294&idx=1&sn=98574ef7e60acb19a3894a5663f78549&scene=21#wechat%5Fredirect)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/RBRgSeVXhYOibBcsaDPDyibEZ7xibGFQUbP2icYbkVGeqLS36SicGcekibckiaqFoA2lHVdrH1ZlSuwvyraZkHUQvic5FEic76DPib9OQVGbzghgWSQcU/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247713461&idx=1&sn=9cd02b0ef3871afe7817c03553b16930&scene=21#wechat%5Fredirect)
  
  
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
