---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUxMjkzNTgyOQ%3D%3D&mid=2247490882&idx=1&sn=028e702a6838d930b8550b69d5668b4e
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUxMjkzNTgyOQ%3D%3D&mid=2247490882&idx=1&sn=028e702a6838d930b8550b69d5668b4e
source_domain: mp.weixin.qq.com
title: NeuralMD：一种面向药物发现的物理约束分子动力学新框架
author: 
published_at: 
fetched_at: 2026-04-25T02:03:52Z
extractor: wechat_worker
content_hash: 2e2d6a33665bf7344aab36a3110a060660e54a1f052c3cb68153e9a4d0330741
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/tTsYdQUMxewibibpxCtf70uJPwAeX9QTdBPqN8514HZYbhE8ElPmLQUUdzuJ4bu8V2r5ApGCGEZxlxsSyWvniaJag/0.jpg) 

# NeuralMD：一种面向药物发现的物理约束分子动力学新框架

药研猿 药研猿 [ 药研猿 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

分子动力学（MD）模拟是研究蛋白–配体相互作用的重要工具，在阐明结合机制、评估构象稳定性以及指导药物优化中发挥着不可替代的作用。然而，传统 MD 方法计算成本高、时间尺度受限，而现有机器学习加速方法在长时间模拟中往往面临误差累积和物理一致性不足等问题，限制了其实际应用价值。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibibpxCtf70uJPwAeX9QTdByK1libLTDw4J62ib1zMxHXS33j3aTPezolziafou39QO9V0ibbvxTKM3pQ/640.png)

近日，来自加州大学伯克利分校、加州理工、牛津大学等团队联合在国际顶级期刊 Nature Communications 发表工作，提出了一种新的蛋白–配体分子动力学学习框架——NeuralMD。该方法以物理约束为核心，将机器学习与牛顿力学和几何对称性系统性结合，旨在实现对结合动力学过程的稳定、长时间尺度建模。

代码开源地址：

https://github.com/chao1224/NeuralMD

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibibpxCtf70uJPwAeX9QTdBJlIQ5oCm0BlDEDu8YY7pERL9rQcxfq1RETwpzNghCjCUc5VspHeARw/640.png)

NeuralMD的核心创新体现在两个方面。首先，在结构表示层面，作者提出了多粒度、SE(3) 等变的 BindingNet，同时刻画配体原子、蛋白骨架以及结合界面的残基级相互作用，从而在旋转和平移变换下保持物理一致性。其次，在动力学建模层面，NeuralMD 采用二阶神经微分方程，同时对速度和位置进行积分，有效缓解了长时间轨迹预测中常见的数值不稳定问题。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibibpxCtf70uJPwAeX9QTdBwEAGBg0aYcaCCpRlcWIhspwOMW49XdP2Cy9LgMzb2hVruiaLLCGO19A/640.png)

在大规模蛋白–配体动力学数据集上的系统评测表明，NeuralMD 在单轨迹预测和跨体系泛化任务中均显著优于现有主流方法：轨迹重建误差明显降低，结构稳定性和物理有效性显著提升。同时，相较传统全原子 MD 模拟，NeuralMD 在保持精度的前提下实现了数量级上的计算加速。

总体而言，这项工作展示了在严格物理约束下使用机器学习重建分子运动过程的可行性，为蛋白–配体动力学模拟提供了一种兼具效率与可靠性的全新范式，也为面向药物发现的动态机制研究奠定了重要基础。

  
参考文献：

Liu S, Du W, Xu H, et al. A multi-grained symmetric differential equation model for learning protein-ligand binding dynamics\[J\]. Nature Communications, 2025.

  
---

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibibpxCtf70uJPwAeX9QTdBa9wHRlibaeyLdkp9QvWC2basXKh5T6u1E0gCAc7dLU17BTlYegpNxwQ/640.png)

找到我们  

FIND US  

扫码进粉丝群

群里禁广告！

二维码失效加小编微信

拉你进群

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxexISa8UZWibSfgR0KsHzZUC82Yibvouic0F4lB4icVe0gzWYgx2auiciaIjFibuNscmVA6lA5hu1eJibVs5Jg/0.png) 

 药研猿 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxexISa8UZWibSfgR0KsHzZUC82Yibvouic0F4lB4icVe0gzWYgx2auiciaIjFibuNscmVA6lA5hu1eJibVs5Jg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
