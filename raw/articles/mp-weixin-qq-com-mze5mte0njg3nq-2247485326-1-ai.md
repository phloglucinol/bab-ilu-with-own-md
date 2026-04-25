---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247485326&idx=1&sn=fc9af05fe3ac979059821fa8148a4535
canonical_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247485326&idx=1&sn=fc9af05fe3ac979059821fa8148a4535
source_domain: mp.weixin.qq.com
title: 让AI看清“远方的原子”：新模型精准捕捉分子间长程作用力
author: 
published_at: 
fetched_at: 2026-04-25T02:03:46Z
extractor: wechat_worker
content_hash: 6a375f49df1f8f908742a3dbd68acce32ea7c4c35f7f390e28e216f9c5823f00
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgrF9j3p2nBsNKA4Wlq9lvbObTlm5Iulic68H4ictJRrC1S9ls4yrx7POcdO19JEic3ibXA4zacnfCfryA/0.jpg) 

# 让AI看清“远方的原子”：新模型精准捕捉分子间长程作用力

原创 Re Re [ 计算材料视界 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在原子和分子的微观世界里，各种力相互作用，共同决定了物质的性质。其中，**长程相互作用力**——例如静电力和范德华力——虽然强度随距离衰减缓慢，却对电解液、蛋白质折叠、极性材料等复杂体系的结构和性质至关重要。然而，传统基于机器学习的原子间势能模型通常只擅长处理原子“邻居”间的短程作用，对于这些“看得远”的长程力，常常束手无策或依赖固定的经验公式，导致预测精度有限、模型通用性差。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgrF9j3p2nBsNKA4Wlq9lvbOqAFSicgAPCx7HayTiamt1CLYgpX1QI4EMAQfRicuB6YwgA5LZp7nj1EUg/640.png)

**2026年1月31日，上海交通大学的研究人员纪亚杰、梁久阳、徐振礼在《Journal of Chemical Physics》上发表了题为“CACE-SOG: 一种用于学习具有可变衰减尾部的长程原子间相互作用的模型”的研究论文。** 他们成功开发了一种名为 **CACE-SOG** 的新型机器学习原子间势能模型，它像给AI装上了“远视眼”，能够从数据中自适应地学习并精确预测各种衰减速率的长程相互作用，在多项测试中超越了现有主流方法。

---

### **研究核心：如何让AI“学会”长程力？**

传统的解决方案，例如基于**埃瓦尔德求和方法**的模型，通常预设相互作用遵循特定的衰减规律（如经典的1/r库仑衰减）。但现实体系（如界面水、含离子溶液）中的长程力往往更为复杂，衰减模式会因环境（如屏蔽效应）而改变。固定内核的模型对此难以精确描述。

> **作者观点与创新**：研究团队提出，与其预设物理规律，不如让模型从数据中**直接学习**长程相互作用的“尾部”衰减行为。他们将新开发的 **SOG-Net（高斯求和网络）** 模块，与优秀的短程描述符 **CACE** 结合。SOG-Net的核心创新在于，它用一组可训练的高斯函数来拟合相互作用在傅里叶空间中的核，从而可以灵活地模拟不同衰减速率（如1/r, 1/r³, 1/r⁶）的长程力。此外，团队还提出了基于物理知识的**智能初始化策略**，大幅提升了模型训练的收敛速度和稳定性。

---

### **关键验证：模型表现如何？**

研究团队在多个具有挑战性的体系上测试了CACE-SOG模型，并将其与仅包含短程作用的CACE模型、以及基于固定埃瓦尔德求和的CACE-LES模型进行对比。

**1\. 分子二聚体测试：精准区分不同作用类型**  
他们首先在包含电荷-电荷（CC）、极性-极性（PP）、非极性-非极性（AA）相互作用的分子二聚体数据集上进行测试。  

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgrF9j3p2nBsNKA4Wlq9lvbOPdUuqeicEJFoIAyteC3eQTQnna5afW4KWBnupviaf8sTaNKdQrSibTGFw/640.png)

**Figure 2\. 三种二聚体（CC, PP, AA）的结合能预测误差**  
图示清晰地展示了CACE-SOG（红色）在PP和AA类型上的显著优势。对于偏离经典1/r衰减的高阶相互作用（如1/r³, 1/r⁶），CACE-SOG能够更准确地捕捉其长程尾部，而基于固定1/r内核的CACE-LES模型则表现稍逊。

**2\. 氟化钾水溶液测试：攻克界面屏蔽效应难题**  
该体系包含体相和界面构型，界面处的屏蔽效应使得长程衰减严重偏离理想的1/r形式。  

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgrF9j3p2nBsNKA4Wlq9lvbOd7icBKnCGka173UOTmAhicmjgZznRjicvPVBhyvTQLRChWSJB1NuUY8pQ/640.png)

**Figure 3\. 氟化钾水溶液数据集上的结果**  
子图(d)和(e)显示，在预测原子电荷和原子受力方面，CACE-SOG的误差显著低于CACE-LES，尤其在训练数据量增大时，优势可达到一个数量级。这证明了SOG-Net自适应学习非库仑衰减尾部的强大能力，能更精确地描述界面等复杂环境中的长程相互作用。

**3\. 水/铂界面测试：再现复杂界面结构**  
在水与铂金属的复杂界面体系中，同时存在静电和色散作用。CACE-SOG成功预测了与第一性原理计算高度一致的氧-氧径向分布函数，并精准再现了水分子在铂表面形成的特征性双峰密度分布（**Figure 6d**），而CACE-LES的预测则出现明显偏差。

---

### **结论与意义**

这项研究通过将**可灵活学习的长程模块（SOG-Net）** 与**强大的短程描述符（CACE）** 相结合，为解决机器学习势能模型中的长程相互作用难题提供了一个高效、通用的方案。CACE-SOG模型不仅**精度更高**，而且在参数数量上比同类模型**减少了一个数量级以上**，兼具了效率与准确性。

这项工作打破了依赖固定物理公式处理长程作用的局限，使AI能够更“智能”、更“物理”地从数据中挖掘出复杂的原子间相互作用规律，为在量子精度下模拟电池、催化、生物大分子等复杂体系铺平了道路，是计算化学与材料科学领域的一项重要进展。

[【npj cm】给离子固体“装上长程雷达”：巧妙分离电荷构建高精度机器学习势函数](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzE5MTE0Njg3NQ==&mid=2247485205&idx=1&sn=8096c4c1d0e4e42c7d44a535c7f7b2a6&scene=21#wechat%5Fredirect)

[【JCTC长程作用新方案】打破“短视”局限！AI学懂静电，通用框架赋能分子模拟新时代](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzE5MTE0Njg3NQ==&mid=2247484491&idx=1&sn=bcc553c49e46b9e16b87378f4ff7926e&scene=21#wechat%5Fredirect)

[【纯计算NC】模拟革命：融合“物理直觉”与“AI大脑”的新一代材料势函数，解锁长程相互作用之谜](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzE5MTE0Njg3NQ==&mid=2247484289&idx=1&sn=fdd63767ecd4cc77cf1ba9baef56379b&scene=21#wechat%5Fredirect)

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajicM8NiadIPfeSzL1nFugbgrN0GO1hvZKLJOaBZvsoj55yGAmCZVw4Iiag/0.png) 

 计算材料视界 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajicM8NiadIPfeSzL1nFugbgrN0GO1hvZKLJOaBZvsoj55yGAmCZVw4Iiag/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
