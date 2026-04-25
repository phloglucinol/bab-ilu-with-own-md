---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUxMjkzNTgyOQ%3D%3D&mid=2247490748&idx=1&sn=f8a148d731bb9ad71804d593a77bcd8a
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUxMjkzNTgyOQ%3D%3D&mid=2247490748&idx=1&sn=f8a148d731bb9ad71804d593a77bcd8a
source_domain: mp.weixin.qq.com
title: 比伞形采样更准？莫纳什大学团队开发的新方法：cPaCS-MD，刷新肽-蛋白结合自由能预测精度
author: 
published_at: 
fetched_at: 2026-04-25T02:04:06Z
extractor: wechat_worker
content_hash: 1ec8af71a614d4a1583677190fd3f6e5b4ed1dd228ad44ec200c89c4848fc963
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/tTsYdQUMxewQfI27IV6agkNIezHRM1QIkeIlpAKHgLjD23ggibKGfxDwITpwib3Th3nlPicOgeVBLKes7RamMAZew/0.jpg) 

# 比伞形采样更准？莫纳什大学团队开发的新方法：cPaCS-MD，刷新肽-蛋白结合自由能预测精度

原创 药研猿 药研猿 [ 药研猿 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

近年来，肽类药物因其高特异性、低毒性以及在蛋白–蛋白相互作用中的独特优势，正逐渐成为新药研发的重要方向。然而，与小分子药物相比，肽–蛋白结合自由能的计算预测始终是一个难题：构象高度灵活、溶剂效应显著、熵贡献复杂，使得传统分子动力学方法往往只能给出定性结果。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewQfI27IV6agkNIezHRM1QIHnkAyIibDtL3b0h5Ukx9DF3cDBurOEVbmwCJNDCLkIn7BJQW0S0IzKQ/640.png)

近期，一项发表于 Journal of Chemical Information and Modeling 的研究提出了一种新方法：接触并行级联选择分子动力学（cPaCS-MD），为肽类药物的理性设计提供了更可靠的计算工具。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewQfI27IV6agkNIezHRM1QIxl6W6FatH4EibDTHBbSZBGsS8T1cGAhk9Uz9TjGl6S085jBavNqYn4Q/640.png)

CPaCS-MD肽解离模拟工作流程

cPaCS-MD 基于并行级联选择分子动力学（PaCS-MD），但在关键反应坐标的定义上进行了创新。传统方法通常使用蛋白–配体质心距离作为解离路径指标，而 cPaCS-MD 则引入了蛋白–肽原子接触距离，更真实地反映了肽从结合位点逐步解离的物理过程。在模拟过程中，系统通过多条无偏短程轨迹并行探索构象空间，并在每一轮中选择“解离程度最大”的轨迹继续推进，从而高效获得低能量的解离通路。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewQfI27IV6agkNIezHRM1QIHJCy2zQUddAmz2caFwbkRPUP2v6m1Xz783R98xahTew172eLxb8keA/640.png)

更重要的是，研究将 cPaCS-MD 与 马尔可夫状态模型（MSM） 相结合，直接从解离轨迹中重构自由能景观，无需额外的伞形采样。这一策略在 12 个不同蛋白–肽复合物上的系统评估显示：计算得到的结合自由能与实验结果高度一致，相关系数达到 R² = 0.84，平均绝对误差仅 2.7 kJ/mol，明显优于传统伞形采样方法。

在计算效率方面，cPaCS-MD 同样表现出优势。相比伞形采样需要预先假设解离路径并进行大量受限模拟，cPaCS-MD 能在更短的模拟时间内获得平滑、连续且可逆的解离过程，显著降低了算力成本。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewQfI27IV6agkNIezHRM1QIxKwnRSyTPLWH6a2zsZSx0a3KoevS2sXk5EsjgoScPW1eaIu4Pr61yQ/640.png)

总体来看，cPaCS-MD 为肽–蛋白结合自由能的高精度、低成本预测提供了一种切实可行的解决方案。随着肽类药物研发需求的不断增长，这一方法有望在先导肽优化、亲和力排序以及机制研究中发挥重要作用，推动计算化学在肽药物设计中的进一步落地。

该方法开源地址：

https://github.com/chalmers-lab/cPaCS-MD\_peptide-affinity

  
参考文献：

Prypoten V, Norton RS, Chalmers DK. Contact Parallel Cascade Selection Molecular Dynamics (cPaCS-MD) for Accurate In Silico Prediction of Peptide Binding Free Energy. J Chem Inf Model. Published online December 22, 2025\. doi:10.1021/acs.jcim.5c02118

  
[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/tTsYdQUMxezXM1Z3QicsxZoMcmTTcBg3jaxGuO5GRdbYsfpSMnFQCUKSWVxGiagEcv6oXiaUerJNFTArMT9LeWPibA/640.jpg)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxMjkzNTgyOQ==&mid=2247490689&idx=2&sn=14ca8cdd3c9fd87fd9112224d66b95d2&scene=21#wechat%5Fredirect)

  
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
