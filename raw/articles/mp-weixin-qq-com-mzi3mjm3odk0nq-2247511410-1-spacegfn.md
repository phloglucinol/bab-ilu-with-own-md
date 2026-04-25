---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzI3MjM3ODk0NQ%3D%3D&mid=2247511410&idx=1&sn=09a726ba64ece28af9de0ae79a3e2b1a
canonical_url: https://mp.weixin.qq.com/s?__biz=MzI3MjM3ODk0NQ%3D%3D&mid=2247511410&idx=1&sn=09a726ba64ece28af9de0ae79a3e2b1a
source_domain: mp.weixin.qq.com
title: 将化学空间转变成可编程计算对象，浙大侯廷军、谢昌谕团队等提出SpaceGFN
author: 
published_at: 
fetched_at: 2026-04-25T02:03:19Z
extractor: wechat_worker
content_hash: 3e466edc388bd8bcf69ebf307d57da4d6d6f6b6dce52ee3b41608aee58174ec2
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/5hq6GFHibJv73jPjf8pTFGtGRSqRoibOIia8RF5mUxoDklDg4iaGH6xr4sTSUjfkLTqJwcgYsC4W58tp4R85ib1vH3EAotav19VwjYliad0oIMkuA/0.jpg) 

# 将化学空间转变成可编程计算对象，浙大侯廷军、谢昌谕团队等提出SpaceGFN

[ ScienceAI ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

---

将 **ScienceAI** 设为**星标**

第一时间掌握

新鲜的 AI for Science 资讯

****![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/cbQsE5QH8RqlDSgibPlwuRlZ2tBFFcVcOGBEtNYpKmkbSLK9YYKWZMpxriaX1OnEzPghic8FIffyxbJgMbxQRHTwA/640.gif "动态黑色音符")**

---

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/5hq6GFHibJv5V2PYcQGB3jDgHVomC2XsEMibhdBhP0sfyeVEEwwolJug5nz8k0HUnfXKOHFD0agDPRkcS55KXAXJfUphM6sQ1QQMGIVf72vjs/640.jpg)

编辑丨coisini

治疗分子的探索，已从天然产物的经验性发现，演进至理性、从头分子设计的时代。生成式人工智能已成为一股变革性力量，将范式从枚举库的被动筛选，转向化学空间的主动探索。

然而，一个根本性局限依然存在：当前大多数模型将化学空间视为一个固定的、从精选数据库中隐式学习得到的分布。它们在一个由数据定义的流形内运作，未能显式控制化学空间自身的结构组织。

基于此，来自浙江大学药学院的侯廷军和谢昌谕团队等提出一个将空间定义与空间探索解耦的框架 ——SpaceGFN，从而将分子宇宙从静态约束转变为可控变量。研究团队认为：分子设计的下一前沿在于将化学空间提升至一个可编程的计算对象。

通过将可编程的、由反应定义的化学空间与生成流网络（GFlowNets）相结合，SpaceGFN 能够构建并自适应地遍历为特定治疗假说量身定制的结构化宇宙。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/5hq6GFHibJv4bXWr6Hjt9McicltNgAlQzqib2XjibkKILqI2UbuPUA8yEJXqZItbInDY2ogysCLxykmYbic9eHp30U9NvnfCiapElDmVDRb2arJgk/640.jpg)

论文地址：https://arxiv.org/abs/2603.00614

SpaceGFN

为应对药物开发中苗头化合物发现与先导化合物优化的差异化需求，该研究设计了 SpaceGFN 的两种模式 —— 发现模式与编辑模式。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/5hq6GFHibJv4whefvaNbjuxuejTN73XFtqPvEJMF3A5bmzqyjLzXeciaHqxOYf12pia8oldEDlw7mnwgJSCoMAaEMibozEyOn5Jeer5bZzMekZ0/640.jpg)

发现模式（Discovery mode）通过两种不同策略展示了空间级编程的深远影响。

首先，该研究构建了一个拟天然产物空间，系统性地组装出重现天然产物结构复杂性的分子架构 —— 这是许多计算库中仍探索稀少的化学空间区域。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/5hq6GFHibJv74uRyzyPwWfDMMcKYUVDpuNJ8EeIU4Fbib4MjrvwWrxtUUxLkF7pewZdqU2IaH5o7KJPON3YQzlicJl8PmnJicbTfdl8nKmzYohU/640.jpg)

更重要的是，该研究引入了一个受进化启发的进化空间，该空间由内源性代谢物和酶催化转化构建而成。进化空间并非仅依赖 post hoc ADMET 筛选，而是将进化生化原理作为结构先验，嵌入到生成过程中。通过利用生命系统历史上处理过的分子基序，这一先验在保持药理多样性的同时，引导了预测代谢与毒理学分布向统计上更有利的方向偏移。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/5hq6GFHibJv4PPNmWYQBGv6FIqzFomCzDXKia3KtVZngUEJbzMdYOylqjxxD1mKom87SZWk13n3fQgSuKibP3GqQzXxPicjqAwOqu3pj0N2ZNGg/640.jpg)

在编辑模式（Editing mode）下，SpaceGFN 通过应用由可执行合成转化组成的精选分子编辑工具包，实现了与反应一致的先导化合物优化。这使得对现有化合物进行局部的、考虑合成可行性的修饰成为可能，而非进行不受限制的图结构突变。针对 96 个药物靶点，SpaceGFN 在合成约束下实现了稳健的优化性能，同时保持了结构多样性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/5hq6GFHibJv7vtlL3RAwhjq5NXe2mmJLx36V7HYKBetg48qicocSJPx5RMibJCuXxngWRLh6dsvicp73LuwFlj6RsGNWf3YLk9DP9Zc1wT2utBg/640.jpg)

通过将可编程的化学宇宙构建、基于流的探索以及反应级编辑统一于一体，SpaceGFN 建立了一个用于审慎设计与导航治疗性化学空间的计算框架，架起了连接生成式人工智能、合成方法学与生物学设计原理的桥梁。

局限性与未来方向

该研究在 96 个不同的药物靶点上对 SpaceGFN 进行了验证。结果表明，在明确的合成约束条件下，SpaceGFN 在实现稳健优化性能的同时，大幅拓展了分子拓扑结构的多样性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/5hq6GFHibJv4u64Skx1vhUzQAvVjInmbXHGBFWuOupkG9cOO7FW8icMkhEn9gJm0njx9ic9aNDQbRgE5VLd7b7R7PuZgQD8BmCtIuw5Wwg0zz8/640.jpg)

需要注意的是，该研究中所有验证均为计算性的，这些结果反映的是计算机内的性能指标，而非经验性的药代动力学结果。

此外，可编程空间的表现力受限于用于构建它的反应规则和构建块。然而，研究团队认为这也是一种优势：SpaceGFN 并非试图取代人类专业知识，而是为药物化学家提供一种媒介，将他们的领域特定直觉形式化为可执行的结构先验。

展望未来，可编程化学空间设计可能受益于适应性优化循环，其中实验反馈会重塑底层空间定义。从这个意义上说，SpaceGFN 为闭环范式提供了计算支架，其中化学宇宙设计与实验验证共同演化。  

**人工智能** **×** **\[ 生物 神经科学 数学 物理 化学 材料 \]**

**「ScienceAI」关注人工智能与其他前沿技术及基础科学的交叉研究与融合发展** **。**

**欢迎** **关** **注标星** **，并点击右下角** **点赞** **和** **在看** **。**

**点击** **阅** **读原文** **，加入专业从业者社区，以获得更多交流合作机会及服务。**

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/XLCp9HBkwLls7SBSrPNH0iafx9YKFxoSewNSqfpuK04lO3ibfdQfaQk6QgSQnPvY9rvuy4bLwYu8frx4b9CRU3cQ/0.png) 

 ScienceAI 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/XLCp9HBkwLls7SBSrPNH0iafx9YKFxoSewNSqfpuK04lO3ibfdQfaQk6QgSQnPvY9rvuy4bLwYu8frx4b9CRU3cQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
