---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIxMjYwOTA4OQ%3D%3D&mid=2247485483&idx=1&sn=555d4a0a6b80336bdbf2b0329ec35b61
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIxMjYwOTA4OQ%3D%3D&mid=2247485483&idx=1&sn=555d4a0a6b80336bdbf2b0329ec35b61
source_domain: mp.weixin.qq.com
title: Acc. Chem. Res.｜药物研发中的自由能计算
author: 
published_at: 
fetched_at: 2026-04-25T02:04:27Z
extractor: wechat_worker
content_hash: be03632c3eb4b7d509135b435a44c2080a006865c511b7cf8c74171b04a74d93
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/T9mbEn97C38BCJJZwvPdfzs59xexMKKjiacUiamWq0KbhKJ3nKNxwSU4JTOrlaWkBOxbVOGOjLZ9kKLtjwqaoHtQ/0.jpg) 

# Acc. Chem. Res.｜药物研发中的自由能计算

原创 gzhAI gzhAI [ AIBioPred ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

[Nat. Mach. Intell. ｜用于分子性质预测的Kolmogorov–Arnold图神经网络](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247484975&idx=1&sn=32d30d0bc3261f0219da0feff4e3d60c&scene=21#wechat%5Fredirect)

[bioRxiv｜RFdiffusion3：利用RFdiffusion3的从头设计全原子生物分子相互作用](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247485347&idx=1&sn=04b97b25ea3794b9974f28fb0106e80f&scene=21#wechat%5Fredirect)

[Nat. Commun.｜DTIAM：预测药物-靶标相互作用、结合亲和力和药物机制的统一框架](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247484569&idx=1&sn=e91018c617cf12b9bdbdf302ace1ebbe&scene=21#wechat%5Fredirect)

[Nat. Mach. Intell.｜利用立体电子学注入的分子图推进分子机器学习表征](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247484530&idx=1&sn=81b349e3b588a14347fceedde63529cf&scene=21#wechat%5Fredirect)

[Nat. Methods｜InterPLM：通过稀疏自动编码器发现蛋白质语言模型中的可解释特征](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247485425&idx=1&sn=7ffd70037c567bedf91de142be855d54&scene=21#wechat%5Fredirect)
  
  
---
  
  
> 字数 1293，阅读大约需 7 分钟

标题: On Free Energy Calculations in Drug DiscoveryClick to copy article link  
作者: Alessia Ghidini, Eleonora Serra, Andrea Cavalli  
单位/机构: 洛桑联邦理工学院、意大利技术研究院  
期刊：Accounts of Chemical Research  
研究内容: #结合自由能 #分子动力学 #MetaDynamics #牵引分子动力学 #非平衡模拟  
原文链接：  
https://pubs.acs.org/doi/10.1021/acs.accounts.5c00465

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C38BCJJZwvPdfzs59xexMKKjZdUeib2hFbOhU4ZrFNxq9NDGjDqClj64xLpZicSsI2OW7AECmdrhshUQ/640.png "null")

### 导读

**近年来，随着计算能力的提升，分子动力学（MD）模拟在药物发现中的应用日益广泛。尤其是结合自由能（binding free energy）计算，已成为评估药物候选分子与靶点亲和力的重要手段。然而，由于蛋白-配体结合是一个稀有事件，传统MD模拟难以充分采样，亟需发展增强采样方法以提高预测精度与效率。**

### 摘要

本文系统回顾了药物发现中用于计算结合自由能的两类主要方法：炼金术变换（alchemical transformations）与路径法（path-based methods）。炼金术方法如自由能微扰（FEP）和热力学积分（TI）已被广泛应用于药物工业中的相对自由能计算，但其在绝对自由能预测、机制解释和动力学分析方面存在局限。相比之下，路径法如MetaDynamics、伞形采样（Umbrella Sampling）和牵引分子动力学（SMD）能够提供结合路径、自由能剖面和机制洞察。作者重点介绍了其团队开发的路径变量（Path Collective Variables, PCVs）与非平衡模拟结合的方法，并展示了其在药物-靶标系统中的应用前景。

### 框架图

![图1：炼金术双解耦热力学循环图（alchemical double decoupling）](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C38BCJJZwvPdfzs59xexMKKjhc7UsrNqbYnbmMMru2PrLOsibEk05W8xDEk9QFOQ4EvhbkUiaOa1eCZg/640.png "null")

图1：炼金术双解耦热力学循环图（alchemical double decoupling）

![图2：基于路径变量计算绝对结合自由能的流程图（从CV选择到自由能估算）](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C38BCJJZwvPdfzs59xexMKKjREIzwZKLiceSevs2vrflXHMEBCzMXtEbibTibiaCWTM3Ryiala9LP111bug/640.png "null")

图2：基于路径变量计算绝对结合自由能的流程图（从CV选择到自由能估算）

### 方法

**炼金术方法：**

* • 利用耦合参数λ插值初始与终态哈密顿量
* • 使用FEP或TI计算自由能差
* • Bennett Acceptance Ratio（BAR）用于双向平衡估算

**路径法方法：**

* • 使用路径变量 S(x) 和 Z(x) 描述系统沿预定义路径的演化和偏离
* • 结合增强采样方法（如MetaD、US、SMD）进行自由能剖面（PMF）计算
* • 非平衡模拟结合 Crooks 涨落定理（CFT）进行双向自由能估算

**机器学习辅助：**

* • 利用ML优化路径变量选择与自由能估算流程
* • 自动化流程减少人为干预，提高效率与可重复性

### 结果（部分）

**炼金术方法：工业主流但机制缺失**

* • **背景：** 炼金术变换（如FEP、TI）因其高效性，已成为制药公司评估结构类似物亲和力的首选工具。
* • **方法特色：** 通过λ耦合参数实现非物理路径的自由能差计算，结合BAR方法提升精度。
* • **结果亮点：** 成功应用于抗HIV药物优化（Jorgensen, 2005），实现高通量相对自由能排序。

**路径法 + MetaDynamics：机制与能量并重**

* • **背景：** 传统炼金术方法无法揭示配体如何结合/解离，路径法弥补了这一空白。
* • **方法特色：** 引入路径变量（PCVs）描述结合过程，结合MetaDynamics增强采样。
* • **结果亮点：** 作者团队开发出自驱动流程，成功预测GSK3β激酶抑制剂的结合自由能，与实验高度一致。

**非平衡模拟 + CFT：新策略提升效率与精度**

* • **背景：** 非平衡模拟（如SMD）在计算自由能时常因耗散问题导致误差较大。
* • **方法特色：** 将SMD与PCV结合，采用双向非平衡模拟与Crooks涨落定理（CFT）估算自由能。
* • **结果亮点：** 新方法支持高度并行化，显著缩短计算时间，成功应用于Abl-Gleevec等复杂体系。

**机器学习辅助：自动化与智能化趋势**

* • **背景：** CV选择一直是路径法的瓶颈，人工设定易引入偏差。
* • **方法特色：** 引入机器学习算法自动识别最优路径变量，并整合进MetaD或SMD流程。
* • **结果亮点：** 构建出半自动化计算流程，减少人为干预，提高可重复性与效率。

### 关键点

* • 炼金术方法适合高通量筛选，但无法揭示结合机制
* • 路径法提供机制洞察，适合先导化合物优化阶段
* • PCV是描述复杂结合过程的有效集体变量
* • 非平衡模拟结合CFT可提高自由能估算精度
* • 机器学习在路径选择与自由能估算中展现出强大潜力

### 结论

本文全面总结了当前药物发现中结合自由能计算的主要方法，强调了炼金术与路径法各自的优劣，并指出未来发展方向在于：**发展更高效的增强采样算法、构建更精确的多体势能面（如神经网络势）、推动自由能计算的标准化与自动化。** 这将有助于将分子动力学模拟更广泛地应用于药物筛选与优化流程中，提升新药研发效率与成功率。

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C39iaMr4p8gOeTaBuDSaDAClfveGOv8QS6WE1ddlHdHpBxUeQ2icYmdk50tsoAfrKLRxibhibuiajbXfNow/0.png) 

 AIBioPred 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C39iaMr4p8gOeTaBuDSaDAClfveGOv8QS6WE1ddlHdHpBxUeQ2icYmdk50tsoAfrKLRxibhibuiajbXfNow/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
