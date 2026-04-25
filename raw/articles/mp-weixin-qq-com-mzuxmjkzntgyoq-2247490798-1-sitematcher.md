---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUxMjkzNTgyOQ%3D%3D&mid=2247490798&idx=1&sn=bd4f849297e54ab9da9fc6aac21276d3
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUxMjkzNTgyOQ%3D%3D&mid=2247490798&idx=1&sn=bd4f849297e54ab9da9fc6aac21276d3
source_domain: mp.weixin.qq.com
title: SiteMatcher：一个真正用“相互作用模式”做分子设计的在线服务器
author: 
published_at: 
fetched_at: 2026-04-25T02:03:49Z
extractor: wechat_worker
content_hash: 50149d28858dd2655242c330d2a886189424c7d499a04524b377938f0f45a224
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/tTsYdQUMxezhm8Kx3QPKu3BptNbNmEaAwKsBoyZnJqj8Mib6X4VibN6XjDCibXUG8ul3gnP1UuE9rmyu1kGfgI2nQ/0.jpg) 

# SiteMatcher：一个真正用“相互作用模式”做分子设计的在线服务器

药研猿 药研猿 [ 药研猿 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在基础靶点结构的药物设计中，结构数据从来不是稀缺资源，真正稀缺的是如何把这些结构中反复出现的相互作用规律，转化为可直接用于分子设计的“操作性知识”。面对动辄数万条 PDB 结构，药物化学家往往只能凭经验在口袋中“想象”片段替换与生长路径。近日，由华东师范大学与 NYU–ECNU 计算化学中心联合完成的一项工作，给出了一个高度工程化的解决方案:

SiteMatcher (https://sitematcher.xundrug.cn/)。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxezhm8Kx3QPKu3BptNbNmEaAdaJj5rV91SdYfVVl5qNPtWfOqNsCYDQCC7DhdUDlGib1wibE86MIPic7g/640.png)

该工作发表于 Journal of Chemical Information and Modeling，系统提出并实现了一个面向结构驱动分子设计的在线服务器。SiteMatcher 的核心思想并不是“从零生成分子”，而是基于真实晶体结构中已经被验证的蛋白–配体相互作用模式进行迁移与复用。研究团队从 PDB 中近 4 万个蛋白–配体复合物出发，系统挖掘并整理了氢键、π–π 堆叠和盐桥等关键相互作用，构建了一个可搜索的三维相互作用模式数据库，并与最小功能性配体片段精确对应。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxezhm8Kx3QPKu3BptNbNmEaAqriaJFsGVCVRkBdbPVvlDT98ShOL0ARROyJicoibxPYxGKLgrOax6L79w/640.png)

在实际设计流程中，用户只需输入蛋白结构与一个 seed ligand，即可选择片段生长（Grow）或替换（Replace）模式。SiteMatcher 会自动分析局部口袋的化学环境与几何约束，在数据库中寻找相似的相互作用位点，将匹配的配体片段精准嫁接到目标体系中；当几何条件不完全匹配时，系统还能引入三维 linker，在可实现的构象空间内完成连接。这一流程显著降低了片段设计中对人工空间判断的依赖。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxezhm8Kx3QPKu3BptNbNmEaAVeyl8z1ciadqCKCpqZfPOGDCvyZo5ibYncLbDLuXpicqu9cMumj82z0eA/640.png)

SiteMatcher工作流

在覆盖 GPCR、激酶、核受体等六类靶点的系统评测中，SiteMatcher 在 157 个蛋白体系中成功回收 176 个已知活性配体，整体 target success rate 达到 47.1%，其中激酶体系超过 70%。同时，单个任务平均运行时间控制在 1–2 分钟，使其具备真实药物研发中“交互式迭代设计”的可行性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxezhm8Kx3QPKu3BptNbNmEaAJkILr9xPJhvELSchDCjwvIhSISPjbhkzBF6jMfU8I9TEbQJMkQaPXg/640.png)

总体来看，该工作将分散在海量结构数据中的相互作用经验转化为可自动调用的设计模块，为结构驱动的 hit-to-lead 与 fragment-based 药物设计提供了一条清晰、可复用的新路径。

参考文献：

Ke, Dongliang, et al. "SiteMatcher: A Web Server for Structure-Based Drug Design Using Protein–Ligand Interaction Patterns." Journal of Chemical Information and Modeling (2025).

  
---

  
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
