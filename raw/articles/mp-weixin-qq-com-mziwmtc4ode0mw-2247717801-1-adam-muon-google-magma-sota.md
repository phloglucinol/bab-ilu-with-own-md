---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247717801&idx=1&sn=9dc2dec0af4d407c55b25d67cb15097f
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247717801&idx=1&sn=9dc2dec0af4d407c55b25d67cb15097f
source_domain: mp.weixin.qq.com
title: 零开销超越Adam/Muon！Google新型优化器Magma：丢弃一半梯度反夺SOTA
author: 
published_at: 
fetched_at: 2026-04-25T02:03:36Z
extractor: wechat_worker
content_hash: 7b08e8cdfc3c17d786d6c6c5e7f0825f193200ee94c203465fa8e51a785db902
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/nFNzd9xjFeCysMwofmX4lpWxrFic2uia3u1WJq402lszrSyffBeVQlb7X23swGvgSMwPGQt60ywjFzGeFqZzwqc0TknChUspPalCAvemOGgRc/0.jpg) 

# 零开销超越Adam/Muon！Google新型优化器Magma：丢弃一半梯度反夺SOTA

原创 让你更懂AI的 让你更懂AI的 [ PaperWeekly ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/Psho9dm7oDHKVtfYDubjKdZRUjAfBQQicXjoZWJ3qnK42ooD4eeJUfJBM4SSZVa2RE5lO0j6rWwzliby0j9u4bDg/640.gif)

  
## 

随机丢弃一半梯度，大模型训练困惑度反降 19%。

  
在当前的训练主流中，Adam 等密集型优化器占据着绝对统治地位。业界习惯了尽可能利用所有可用的梯度信息来更新参数。

  
然而，西北大学与 Google 的一项最新研究挑战了这一固有认知。在优化过程中随机掩码（即直接丢弃）一半的参数更新，不仅没有让训练崩溃，反而大幅提升了收敛性能。

  
该团队提出了一种基于动量对齐的梯度掩码优化器 Magma。

  
在 1B 参数规模的实测中，Magma 相比现有的 SOTA 优化器 Adam 和 Muon，分别将困惑度降低了 19% 和 9%，且实现了完全的零额外计算开销。
  
  
论文标题：

On Surprising Effectiveness of Masking Updates in Adaptive Optimizers

论文链接：

https://arxiv.org/pdf/2602.15322
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wulOVRfC18yCkd6xXqGq22h6QUk8chptF0fnQ4uXeZtAktYMrWwG2SyQ/640.png)

SkipUpdate 与隐式几何正则化

现有的密集梯度依赖与坐标下降等稀疏更新策略之间存在结构性不匹配。

  
研究人员首先分析了 RMSProp 的一种变体 SkipUpdate。在 SkipUpdate 中，整个参数块在每次迭代时会遵循伯努利分布被随机掩码。

  
当某个参数块被掩码时，该步的更新将直接跳过；但是，动量估计依然保持密集更新，并且保留下来的更新会被适当重新缩放以保持无偏性。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeAdl0F5gFGZlvq0IXoNcSwK7JkCIBNRo81UdesNapHo3mcH04pOLrxEy783HW9MF6mz0PKzEsguMCCIZaNVe18J6B92W4C2BbE/640.png)

〓 图1. SkipUpdate 与 Magma 的算法伪代码
  
  
从经典收敛分析的角度来看，由于更新中随机噪声的增加，这种随机掩码在理论上会削弱最差情况下的收敛保证。

  
此外，在反向传播的计算成本保持不变的情况下，每个参数实际上接收到的更新更少。

  
然而，尽管丢弃了一半的更新，SkipUpdate 依然在不同模型规模上持续优于包含了复杂曲率信息的 Muon 等密集优化器。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeBH2bhsTZCPxHM2siafNbaQPSH69otibdibJiayXTB1HMeYvZVFfWWRjtmbm8PJEgjXjZpCts3TicSzYiaoYbYnQked4IPVsxMeKl2rI/640.png)

〓 图2\. C4 数据集上跨模型规模的预训练表现
  
  
这种现象的本质在于，块级别的随机掩码天然引入了一种依赖于曲率的几何正则化。根据理论推导，给定过滤 ，SkipUpdate 的预期损失为：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeCvrqPWJHbf6nPPiaOVlA20vXsHlwvpVtMjxJChrs6FEItnNdicB50yk1xMcyqrlw5qsibvbsFOXkZL8tANzs2yajrmDBBY9YdTQY/640.png)
  
  
其中， 作为一个自然的几何正则化项，衡量了沿更新方向  的局部损失曲率。

较大的正曲率方向意味着损失的急剧增加。因此，最小化预期损失，实际上就是隐式抑制了那些与块内高曲率（陡峭）方向一致的更新。

这种正则化效应平滑了优化轨迹，并使算法偏向损失景观中更平缓的区域。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuhfgUpIfdPSqH8YjjHbCUiaaKsMA36bIMsMtGNKoBcus5py06M0fvx3A/640.png)

动量对齐梯度掩码 (Magma)

SkipUpdate 应用的是同质掩码操作。Transformer 中的参数具有极大的异质性，例如明显不同的 Hessian 谱和梯度方差。

由于跨迭代一致的梯度分量倾向于携带有效的优化信号，而快速波动的分量通常由随机噪声主导，研究人员进一步提出利用动量-梯度对齐来控制掩码过程的 Magma 优化器。  

对于迭代  时的每个块 ，Magma 计算对齐得分 ：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeAQIX1Aq7bQbzDXYm3wq2g5baia3eaeldTKcicjVpDLqlOxPKVF0Podc9EfUUDy8n4t4WGbqjZO9dIdp8k1Xg52nfm3JOFTQhTmA/640.png)

  
这里  是一阶动量估计， 是温度参数，采用余弦相似度是因为其尺度不变性在梯度范数变化剧烈的大型语言模型训练中尤为有效。

Magma 通过指数移动平均得分  调制掩码更新，应用更新规则 。

Magma 是一个即插即用的封装器，直接将  乘入现有自适应优化器产生的更新方向  中，不引入任何额外的内存或计算开销。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wukOjHSmSsEuRCB0fJu69CtdNgLnvFPDUCgeicOppBKuDvniaD3q8XWQ0Q/640.png)

全局收敛性证明与理论闭环

Magma 的有效性不仅仅依赖于实证，研究提供了严谨的全局非凸平稳性收敛保证。在平滑目标假设下，Magma 每步迭代满足如下下降引理：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeASiaEuus4J5Z89hic2IJWJyVUvcJRvAnKGMVibDEBZiaJMNia1BjSpEUCAwWrLXzZBDKWIRMe61NDONq1kskpQlH8jczjsWN1yMfJo/640.png)

  
通过定义二阶矩缩放因子 ，Magma 实际上重塑了各个参数块的有效平滑度常数：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeA8gSvBLcwhCXbCxrSdB2JaWFznbrtqaAl1HRWmZQBPoNm3V1YmRIKq4mQrHSgfUvibmWaibbeNqWWtkl46axicOsEFrEos6UoF9o/640.png)

  
结合缩放随机掩码下的有效下降效率下界：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeCBOukNnNib2YDrQtNYN3fF6H4CLClwvDia3ncBHVqJlLnVibQSBibGxzZkicd6IShnbyfFX9xoc2sD5ta3Fia2jtNYibWgfggyhSECRM/640.png)

  
论文给出了在恒定学习率下最终的全局非凸平稳性收敛界限：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeA0aShM3miaU0iaibWMricOVz8NHhfRsia4mVSa6HpibM2955icHpTlf3gXYIqvpRNgoGG6OcWmsqdO9lx5HCDUwkZrwZg9xle962QOa0/640.png)

  
上述数学推导从底层证明了，Magma 利用动量-梯度对齐机制，精准衰减了那些引发高曲率噪声和平滑度瓶颈的参数块，降低了有效平滑度  和噪声水平 ，从而扩大了稳定区域，加速了收敛。  
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuiaLfO9V4lkD8cXK7ImEicqib5bPGH6syOrWzicR2KaqPyAicMccs8icC03Gw/640.png)

异质损失景观下的有效性验证

为验证 Magma 在异质景观中的表现，研究采用了受控的二次基准测试。该测试包含两个具有相同特征谱但块级曲率结构不同的二次目标。

  
同质 Hessian 将尺度相近的特征值归入同一个块内（例如 {1, 2, 3}），而异质 Hessian 在每个块内混合了幅度差异巨大的特征值（例如 {1, 99, 4998}），诱发了强烈的曲率不对齐，这定性模拟了自回归 Transformer 观察到的损失几何结构。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeCFNAuCAZUawY9ogTZYho7tAaKJxGxCAoA56UYd4zPTiaJVvnYeMibbQ262kRReautrGEibsGhzoDNJSU3GJickibOS5pNUsM6EgsHY/640.png)

〓 图3\. AdamW 和 Magma 在同质与异质二次目标上的优化轨迹及平均梯度-动量对齐对比
  
  
在同质问题上，Magma 和 AdamW 表现相当。但在异质问题中，Magma 实现了比 AdamW 更快的收敛和更低的最终损失。

  
值得注意的是，Magma 的这种几何正则化收益是与 Transformer 特有的损失景观高度绑定的。

  
当把 Magma 应用于曲率结构类似同质情况的 CNN 架构（如 CIFAR-10 上的 ResNet-50 图像分类任务）时，其测试准确率（93.82%）并未超越 AdamW（94.46%）。

  
这进一步证实了其在处理恶劣曲率条件和跨参数子空间不对齐问题时的针对性优势。
  
  
![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wukGHdevfTibLOpic6945Lrhqmt43pKicyIhGs4m7ANzKOfY9RJgmTicZGdg/640.png)

**大规模预训练表现与核心实验**

  
在 C4 数据集的 Llama 2 预训练中（涵盖 60M 到 1B 模型规模），Magma 在各个模型规模上，均稳定提升了所有基线优化器的性能。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeBZDkicyZFXQMo15ZE9DIM9hQ8nIwNTJTPCyyO9KIicRnvUEpOehKHjYjeFY1hr4TjgtODecphlke8icpyPoT0ezQqyyY7ia6OrH8k/640.png)

〓 表1\. Llama 2 在 C4 数据集上的预训练结果及各模型规模的验证困惑度

  
在 1B 参数规模下，Adam+Magma 显著超越了 Adam+SGG 和 C-Adam 等竞争性增强方法。

  
更为惊人的是，基础版 RMSProp 在该规模下直接发散崩溃，而加入 Magma 封装后的 RMSProp+Magma 不仅稳住了训练，更一举拿下了全场最低的验证困惑度 13.19，超越了计算密集的矩阵优化器（如 Muon 和 SOAP）以及复杂的增强器（如 APOLLO+SGG）。

  
稀疏混合专家（MoE）架构由于动态负载均衡和稀疏 Token 路由，导致优化过程显著复杂且不平滑。

  
在 OpenWebText 数据集上的 Nano MoE 预训练中，Magma 同样在 MoE 设置下持续改善了 Adam 和 Muon 的性能。

  
例如当应用于 Adam 时，Magma 虽然在训练中期的收敛速度略有放缓，但最终却达到了更优的收敛性能。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeCwE1jwX25r5OiavicZnm1vNNOrqYoCmSbiceBvib4iaib0JG33yUlRyIXSvRepjJR9ZpDXYpUR2SSiaLkSbTcicasGlaQmLRyECMOFenM/640.png)

〓 图4\. Nano MoE 模型在 OpenWebText 上的预训练优化轨迹

  
此外，自回归语言模型训练存在厚尾随机梯度噪声。在受控线性 Transformer 基准中，Magma 在厚尾设置下显著优于 Adam。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeBw2QNRf98nhtk23qmtGuEcqT17LOTIACjVaBP5IWIeru9D9dM4YA8smMMNU5Uwjtv5LGMSQexy9ZyEgOicg0Ex7dGM7Gvttz4c/640.png)

〓 图5\. Magma 在轻尾和厚尾数据分布下的优化轨迹与鲁棒条件数
  
  
在厚尾噪声下，Magma 持续获得了明显更小的鲁棒条件数，表明其更新保持在损失景观中条件良好的区域。
  
  
![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuJXXicvv3JrPNYrFlYadg4ibA8SxC6OvibZyBHGuub04X1AXxeRTC0WUJA/640.png)

**机制消融与超参数敏感性分析**

  
Magma 究竟赢在哪些细节？后续的消融实验给出了答案。

  
在掩码组件方面，仅对注意力块应用掩码改善了性能（21.92），但当掩码同时应用于注意力和 MLP 时产生了协同效应，达到了最低的困惑度（21.65）。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeDliaqgXltfGSheibtZjBTZnzX0WVkJUn6qWrHybxEg8XVn1V0TJdZrp27JicmiaUdbf3hv8LnWxoPicDwQ2dx6eQxelshamxGp4oCI/640.png)

〓 表2\. 不同掩码组件（仅 Attention、Attention+MLP）的验证困惑度
  
  
在掩码粒度方面，Element、Row、Column 和 Block 级别的掩码对稳定性的影响极小，由于块级掩码具备高效的操作剪枝特性且节省内存，因此被默认采用。
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeCUJ3aQvLCIkFIZg0dVJB6PXWUmNOTkVBQdxAXzr73cUE8O5hZy566eYMa7fJ8pZ3WdzRSDyv5p8bYoEYbJLhtEibg38KG9RIfA/640.png)

〓 表3\. 不同掩码粒度（Element、Row、Column、Block）与采样方案的验证困惑度对比

  
关于采样率  和阻尼温度 ，实验表明  在所有温度下均表现最佳，且结果对温度  相对不敏感。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/nFNzd9xjFeBBiaOPJCSLMQA0o9TOTVYicVGJ7l2ub9gWPX1M6iasVc8Jl0gaXT7iaYke9NG5nSicNqNteU8ZdrllNzxPwEFTnic2Scm0Csh8DibdVU/640.png)

〓 图6\. 不同采样率 p 和阻尼温度 τ 对评估困惑度的比较

  
在动量更新机制上，密集与稀疏动量更新存在关键差异。密集基线始终保持稳健收敛并获得最低困惑度；而无阻尼的稀疏动量更新表现出严重的训练不稳定性。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeBhbXLrzU9ffLNMcbicIMvrAaZD90NVl2RfTKrvNQlHm1tTNnic6RxsDg1jyqfLibhhhg7FVkd3R0I0gsjZct2Zh1REegFeaHbNNk/640.png)

〓 图7\. 密集 (Dense) 与稀疏 (Sparse) 动量更新的训练困惑度对比
  
  
学习率敏感性分析表明，与 Adam 和 C-Adam 具有狭窄的最优窗口不同，Adam+Magma 在高达 0.05 的学习率下仍保持有效，展现出跨极宽超参数范围的卓越稳定性。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/nFNzd9xjFeCH6gkwDqxxia7iak5FHmSnKz36CsOsMRIZtFn2htgmYguib1E3p5N7TB0Ka4j2VxMVMcyZDaXx06bPKBybTyp8AZdW6TVTciaVBj0/640.png)

〓 图8\. 不同优化器评估困惑度对学习率的敏感性分析

  
![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDGhKg9nnSz5qQrwKvXibt3wuCkR96mP8kh7KicSzPQiaIQa3ft5MLn54FNK0UD2MI99iaHjT9m9NjLl7A/640.png)

**结语**

  
长期以来，密集梯度更新几乎是大语言模型训练的默认前提。

  
但 Magma 的出现证明了，面对 Transformer 极度复杂和异质的优化空间，与其一味追求计算昂贵的二阶矩阵预处理，不如巧妙引入结构化的随机性。

  
这种基于动量对齐的参数掩码策略，不仅从底层逻辑上实现了有效的几何正则化，更为当下亟需降低训练成本、提升稳定性的基础模型开发，提供了一条极具潜力的工程新路径。
  
  
**更多阅读**

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDHiaMulJaPwRzymicjxy4FibicVPcSmtjcm0rY7jAPzy0M2Xc2hx2csgic2sQL4gGQdC8ajdK7Aibe609Eg/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247716706&idx=1&sn=861ccba253718964b98e2d76503eb879&scene=21#wechat%5Fredirect)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDHiaMulJaPwRzymicjxy4FibicVWibf3mnLLvYLH8ic8AI55x3gSp4YAcyRqiaVXGnGPUxtfiaCq8seIQtMIw/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247716764&idx=2&sn=a4dda29a9b9dcc5d7d5468893af82a44&scene=21#wechat%5Fredirect)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Psho9dm7oDHiaMulJaPwRzymicjxy4FibicVBOvfUqZhaBL6dU03qaWptzfqZ5nESraQvJA94INmXGHFWrXqC0fCsg/640.png)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwMTc4ODE0Mw==&mid=2247716247&idx=1&sn=584edb6041579a68d396bb9a3f0c278f&scene=21#wechat%5Fredirect)
  
  
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
