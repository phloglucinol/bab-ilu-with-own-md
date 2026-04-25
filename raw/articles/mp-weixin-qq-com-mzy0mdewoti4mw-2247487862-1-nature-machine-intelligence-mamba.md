---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzY0MDEwOTI4Mw%3D%3D&mid=2247487862&idx=1&sn=6357fe0fdac29a80690f2233a6723ae6
canonical_url: https://mp.weixin.qq.com/s?__biz=MzY0MDEwOTI4Mw%3D%3D&mid=2247487862&idx=1&sn=6357fe0fdac29a80690f2233a6723ae6
source_domain: mp.weixin.qq.com
title: Nature Machine Intelligence | Mamba+强化学习实现药物候选分子高效发现
author: 
published_at: 
fetched_at: 2026-04-25T02:03:20Z
extractor: wechat_worker
content_hash: 333224bc2f9a5dbded3aed5653319df134988b9b252904b47df291abf71cd8ed
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/EwJFyCpdmEIX0OHPcwExjYOL8giaJNJtRvpF9PqlIWMpYaoOfXrGJZLnA7WcMPF1So8VPOjZZs3LXu8xpbToIR8I3epJJL9IhKZsawslT3R4/0.jpg) 

# Nature Machine Intelligence | Mamba+强化学习实现药物候选分子高效发现

原创 LifeNexAI LifeNexAI [ LifeNexAI ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

  
编辑：LifeNexAI

  
在药物研发领域，高效、低成本地设计和筛选潜在药物候选分子是永恒的核心挑战。近日，发表于《自然·机器智能》的一项研究提出了一个名为Saturn的新型生成式分子设计框架。该研究团队巧妙地将新兴的Mamba架构与增强记忆强化学习算法相结合，在样本效率方面取得了革命性突破。简单来说，Saturn框架能用更少的计算资源，找到更多、更优的候选药物分子。它不仅在一系列多参数优化任务中显著超越了包括GEAM在内的15个先进基准模型，更令人瞩目的是，它首次证明了在有限的“计算预算”下，直接利用高保真度的密度泛函理论（DFT）模拟来优化分子电子性质是可行的。这项研究为加速早期药物发现和功能材料设计提供了强大的新范式。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/EwJFyCpdmEKME1HCYia7WYXFGr1JUAhWE1A0QLobldZ3xU1HWRTicxSY7Nloea8GJTL9ZGKCqJwlFMeicHw0FQREKZ5V6p1H1iaOEVTjudj8QZU/640.png)

**_LifeNexAI_**

**用AI助力生命科学**

  
**药物分子设计的“效率瓶颈”**

**PART ONE**

  
药物研发是一条漫长而昂贵的道路，其起点在于从浩瀚的化学空间中设计出具有特定理化性质和生物活性的分子。近年来，基于人工智能的生成式分子设计已成为革命性的工具，它能够像“编剧”一样，按照预设的“剧情大纲”（如高结合亲和力、类药性、易合成性等目标），自动“创作”出全新的分子结构。

  
然而，一个关键的瓶颈制约了此类方法的实际应用：样本效率。要判断一个AI“创作”的分子是否优秀，需要调用计算“神谕”——一种预测分子性质的模型，如分子对接（预测结合能力）或DFT计算（预测电子性质）。这些“神谕”调用成本高昂，特别是高保真度的模拟。现有方法往往需要调用成千上万次这样的模拟，才能找到少量有潜力的分子，这在实际应用中意味着巨大的时间和算力成本。

  
因此，开发一种能在极其有限的“神谕”调用次数内，最大化发现优质候选分子的AI算法，是领域内亟待解决的难题。本研究提出的Saturn框架，正是为了突破这一效率瓶颈。

  
**Saturn框架——“Mamba引擎”驱动的高效学习系统**

**PART TWO**

  
Saturn框架的核心创新在于其架构设计和训练机制的协同优化，旨在从每一次“神谕”评估中榨取最大价值。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/EwJFyCpdmELNhKhicy0bWYaiaCuv5dptqnCUV6T9cOKuGgupF5OKVFDadicEy8qkwZxvVse6ib9ag7Z7LkJMY3A09fE0712YaIhavBrkGF5Rcss/640.png)

  
1\. 核心引擎：Mamba架构

* 与目前主流大型语言模型普遍采用的Transformer架构不同，Saturn选择了Mamba作为其生成分子的语言模型骨干。Mamba是一种状态空间模型，以其在长序列建模中的线性计算复杂度和卓越的序列建模能力而受到关注。
* 在本研究中，研究者发现Mamba相较于传统的循环神经网络或Transformer，具有更强的分布匹配能力，这意味着它能更精准地学习并复现那些被评估为“高奖励”（即性质优异）的分子序列模式，这是实现高样本效率的关键基础。

2\. 高效学习机制：增强记忆算法

* Saturn集成了此前研究者提出的增强记忆强化学习算法，但首次深入揭示了其工作原理。
* 该算法的核心是SMILES数据增强与经验回放。当一个分子被“神谕”认定为优秀后，算法会生成该分子的多种不同字符串表示（SMILES），并将其存入一个“记忆回放池”。
* 在后续的训练中，模型会反复、重点地学习这个记忆池中的高质量分子及其变体，从而“铭记”何种结构特征能带来高奖励，并倾向于生成更多类似或相关的分子。这个过程被研究者形象地比作“跳跃-局部探索” 行为：模型先“跳跃”到一个成功的分子结构附近，然后在该结构的局部化学空间中进行精细的“探索”和优化。

3\. 灵活的工作流

* 框架还允许集成遗传算法，以在需要时引入更多样化的突变，在“效率”与“生成分子的多样性”之间取得平衡。

  
**全面超越基准，实现高效优化**

**PART THREE**

  
研究通过三部分实验，系统验证了Saturn框架的强大性能。

  
第一部分：理解“高效”从何而来

* 通过一个包含多个理化性质目标的玩具优化任务，研究者量化了不同架构（RNN, Transformer, Mamba）在相同增强记忆算法下的表现。
* 结果清晰地表明，在模型参数量相近的情况下，Mamba架构的样本效率显著更高。它能以更少的“神谕”调用次数，生成更多满足高奖励阈值（Reward > 0.7）的分子。
* 分析揭示了Mamba的“跳跃-局部探索”行为：其在化学空间中的探索轨迹更具方向性，且在一个小区域内生成的分子彼此更相似（高内部相似性），表明其高效的局部优化能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/EwJFyCpdmEJVjmibXaic8ibB9ibq8mfWKdCPoTRoM3gef3xp2xRzXMqXMLkeQJia5049sAy1luj8AI8ShoPZSNmQ42Gh5iaZXuRVTnsx0E7hNFspQ/640.png)

第二部分：在真实药物设计任务中碾压性胜出

* 在针对PARP1、FA7、JAK2等5个重要药物靶点的分子对接优化任务中，Saturn与当前最先进的模型GEAM进行了正面比较。优化目标综合了对接打分、类药性（QED）和合成可行性（SA）三个关键参数。
* 在严格的3000次对接计算预算下，Saturn的“命中率”在多个靶点上达到GEAM的1.3至1.8倍，优势巨大。更严格的“严格命中率”指标（要求QED>0.7且SA<3）对比中，Saturn的优势更为明显，最高可达GEAM的8.5倍。
* 这意味着Saturn生成的分子不仅在结合能力上更优，而且在整体成药性平衡上也做得更好。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/EwJFyCpdmEKiaa58z0DkkDib2YxicSzic4u8du5O1dNXjcEnFkyrwlDfel67Ljnuy1QkjRA5WB9WwWw1WzFcs02WibzRNrAuKUp7IWhXfCd4C0C8/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/EwJFyCpdmEI5sGTgoGPuXeg8bGglluejfWH0hDohZmn2ZIzkEyGeek6tibEjRsGZrwWBa0GeX37QPGibCOtvAGCw9z1bNhMCNwtvhCictbkqo4/640.png)

  
第三部分：攻克高保真“神谕”优化壁垒

* 这是本研究最具前瞻性的成果。研究者尝试用Saturn直接优化密度泛函理论（DFT）计算出的分子最高占据-最低未占轨道能隙——一个对材料科学至关重要的电子性质，计算成本极高。
* 在极为有限的DFT计算次数内，Saturn成功地将生成分子的HOMO-LUMO能隙分布向更小的值（目标方向）系统性地移动，证明了直接、高效优化此类高保真性质的可能性，为AI驱动功能材料设计打开了新的大门。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/EwJFyCpdmEIbLEb5FHicBMxPz9gNov8Ibtxhskztm9RvcAEXCwHzib6TXADIFCiaxh6FCvEK6mgyib5S4ibDwQFvgkrnsDrPSj8hyKM48rXRZMWA/640.png)

**开启精准、经济的分子设计新纪元**

**PART FOUR**

  
Saturn框架的成功，为AI辅助的分子发现领域带来了新的启示和方向：

  
1. 推动药物发现流程变革：极高的样本效率意味着可以用更低的计算成本探索更广阔的化学空间，有望大幅缩短早期药物发现的周期，降低研发成本。
2. 赋能高保真模拟驱动设计：Saturn证明了直接优化DFT等昂贵模拟的可行性。未来，研究人员可以更直接地将更精确的结合自由能微扰计算、分子动力学模拟等纳入优化循环，设计出性质预测更可靠、更接近实验真实的分子。
3. 平衡“探索”与“利用”的艺术：研究也坦诚了当前框架的倾向性——它通过“局部探索”来实现高效率，但在面对性质“悬崖”（微小结构变化导致性质剧变）时可能需要更“激进”的探索策略。未来的框架可能会发展出能自适应动态调整探索-利用策略的智能系统。
4. 向可合成性设计深化：虽然研究中已考虑了合成可行性评分，但整合更强大的逆合成分析模型，实现“设计即可合成”的分子生成，是下一个重要的演进方向。

  
Saturn框架通过将先进的Mamba序列模型与精心设计的增强学习机制融合，在生成式分子设计的样本效率上树立了新的标杆。它不仅仅是一个性能更强的工具，更展示了一条通向更精准、更经济、更高保真的AI驱动创新分子设计的可行路径。随着此类技术的成熟，我们有望见证从药物、农药到新型功能材料等多个领域研发范式的加速革新。

  
DOI: https://doi.org/10.1038/s42256-026-01200-4

\- END -

  
如果您对AI4Protein&Peptide&TCR&Other感兴趣，欢迎关注交流合作  
  
**// 人工智能 × 生命科学 //**

  
**欢迎关注标星，并点击右下角点赞和在看。**
  
  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/bBiaLIBgZwsab0FW0GO2RNvj388TyZCZrd4Xj2ZA8FFvJicYxuB9AUVXm3sNt5Xsv9Cs8aMgWY4n8ia17o5HJCo0w/0.png) 

 LifeNexAI 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/bBiaLIBgZwsab0FW0GO2RNvj388TyZCZrd4Xj2ZA8FFvJicYxuB9AUVXm3sNt5Xsv9Cs8aMgWY4n8ia17o5HJCo0w/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
