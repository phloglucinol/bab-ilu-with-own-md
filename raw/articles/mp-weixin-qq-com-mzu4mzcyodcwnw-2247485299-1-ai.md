---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzU4MzcyODcwNw%3D%3D&mid=2247485299&idx=1&sn=d874f5b7d77af9301d24c7d0f4e37523
canonical_url: https://mp.weixin.qq.com/s?__biz=MzU4MzcyODcwNw%3D%3D&mid=2247485299&idx=1&sn=d874f5b7d77af9301d24c7d0f4e37523
source_domain: mp.weixin.qq.com
title: 别被AI“神话”忽悠了，传统统计势能模型也能在药物筛选中“逆袭”！
author: 
published_at: 
fetched_at: 2026-04-25T02:03:26Z
extractor: wechat_worker
content_hash: 2eccb37cfd877ced56c8d80da35a27e5b2f0310d5df30c4dc664b274e6e30149
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/9UxHHXgwDxfHjibTSGA38JrtdoLLcibEbeBgQGbTWFlcP1zGicLrjJ7giaYFjYWuKPDEq0qzc0wA4iaCbJ276NZxLBymojlglRWOHZcLGZ3ylpe0/0.jpg) 

# 别被AI“神话”忽悠了，传统统计势能模型也能在药物筛选中“逆袭”！

原创 酶矿工人的二重身 酶矿工人的二重身 [ EnzymeDesign ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在AI制药领域，AlphaFold等深度学习（DL）模型几乎占据了所有头条。但你是否想过：**在数据有限的场景下，那些看似“过时”的统计势能模型，真的就比AI差吗？**

最近发表在《Briefings in Bioinformatics》上的一项研究给出了肯定的回答：通过精心设计的统计势能模型，不仅能实现媲美甚至超越顶尖DL模型的效果，还具备极佳的物理可解释性。

---

### 核心发现：为什么“老派”方法依然能打？

研究团队通过系统性评估发现，蛋白质-配体相互作用的预测存在“分工”：

• **对接（Docking）**：更依赖于具有明确物理意义的**距离相关原子-原子势能**。

• **筛选（Screening）**：更依赖于能够捕捉局部化学环境的**方向相关原子-残基势能**。

基于这一洞察，研究团队开发了名为 **HybridSP** 的混合统计势能模型。它巧妙地将三种互补的势能项结合在一起，通过一种“亲和力加权”方案，修正了统计分布中的偏差。

### 关键技术亮点

为了让模型更“聪明”，研究团队在方法论上做了几项关键优化：

1\. **亲和力加权（Affinity-weighted）**：传统的统计势能往往平等对待所有样本，但低亲和力复合物会引入噪声。研究引入了基于结合亲和力的加权方案，让模型更关注高质量的相互作用数据。

2\. **残基感知（Residue-aware）**：不同残基环境下的相同原子类型，其物理性质截然不同。通过将蛋白质原子细分为100种残基相关类型，模型能更精准地捕捉局部化学环境。

3\. **多模型集成**：如 **表1** 所示，HybridSP 整合了原子-原子接触和原子-残基接触，通过加权求和，弥补了单一模型在处理复杂溶剂效应时的不足。

![表1：各类评分函数的特性对比，HybridSP通过整合多种接触类型，在物理意义与预测目标上实现了平衡。](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9UxHHXgwDxeJeN0NUv1rcrJs8pg6kygFVrmcRtFypVSA6Tzibic10y64gFtHJ7nma0NwbgQmBOYf2Rj5yywfNPibrhOJIeLV4lLtf7TWlk7Qb0/640.png)

表1：各类评分函数的特性对比，HybridSP通过整合多种接触类型，在物理意义与预测目标上实现了平衡。

### 性能表现：不仅是媲美，更是超越

在经典的 CASF-2016 基准测试中，HybridSP 的表现令人惊艳：

• **对接能力**：在包含晶体构象的测试中，HybridSP 达到了 **91.6%** 的对接成功率（RMSD < 2 Å），直接对标甚至超过了部分深度学习模型。

• **筛选能力**：在虚拟筛选任务中，HybridSP 在 Top 1% 的富集因子（EF）达到了 **29.35**。如 **图2** 所示，相比于传统方法，HybridSP 在保持高对接成功率的同时，显著降低了筛选中的假阳性率。

![图2：CASF-2016基准测试结果，HybridSP（加粗项）在对接成功率和筛选富集因子上均展现出强劲的竞争力。](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9UxHHXgwDxdqOOppiaj3sIH9xBw0OOmMINjG5szgcJ5lRwYkS49vuAsrcXicIzw7PDQibJmjicAztUj9xoSalTX0V4TQXhQQX4sVdUqg8A1VpH4/640.png)

图2：CASF-2016基准测试结果，HybridSP（加粗项）在对接成功率和筛选富集因子上均展现出强劲的竞争力。

此外，研究团队还通过 **图1** 展示了 HybridSP 的工作流。通过对比加权与未加权势能曲线，可以发现加权后的曲线在处理高能区域时更加平滑，有效缓解了采样偏差。

![图1：HybridSP的工作流及统计结果，展示了原子对接触频率及加权前后的势能曲线差异。](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/9UxHHXgwDxcdmQX1DZib1utQicvxDXibyt7QHj2D4H08MqclLlYBWpZjQOAjDkW1xAGkUL4jbibeO3ttx2EP6AfAWhoy8ib8CP63JcdnWicsBGNVY/640.png)

图1：HybridSP的工作流及统计结果，展示了原子对接触频率及加权前后的势能曲线差异。

### 为什么它更可靠？

为了探究 HybridSP 为何在筛选中表现优异，研究团队分析了模型识别出的分子相互作用模式。**图4** 显示，HybridSP 能够识别出在不同配体中高度一致的氢键相互作用，这证明了模型不是在“死记硬背”，而是真正捕捉到了关键的化学相互作用模式。

![图4：分子相互作用分析，HybridSP在筛选中识别出的关键氢键模式具有高度的一致性。](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/9UxHHXgwDxfckzSmDnPt69RGjboJEf29j2clzxjAiaW9TOYwE2FhGHFLJqTzEgdBoFRKEPn0UtewM5HvKOjYcInpmYhIXc9BAmTDrADOgTQ0/640.png)

图4：分子相互作用分析，HybridSP在筛选中识别出的关键氢键模式具有高度的一致性。

在更广泛的基准测试（如 DUD-E 和 DUD-AD）中，HybridSP 同样表现稳健（见 **图3**），证明了其在面对多样化蛋白-配体系统时的泛化能力。

![图3：多基准测试下的性能表现，HybridSP在PoseBusters及DUD系列数据集上均保持了领先的筛选性能。](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/9UxHHXgwDxdWiabURxOd75DwDcNYUicTecKKg1xuInEXM8Qnlv2yLlhUerjqDloEOaOmJASPp99CUmollV6judESwbia1ZQBo8rn3sW6r5BgGA/640.png)

图3：多基准测试下的性能表现，HybridSP在PoseBusters及DUD系列数据集上均保持了领先的筛选性能。

### 结论与展望

这项研究告诉我们，**深度学习并非解决所有问题的唯一钥匙**。在药物发现中，将物理化学先验知识与统计学方法相结合，往往能带来意想不到的惊喜。

HybridSP 的成功不仅在于其高精度，更在于其**透明的物理机制**。对于那些需要深入理解药物分子结合机理的科研人员来说，这种“白盒”模型无疑比复杂的深度学习“黑盒”更具参考价值。

如果你对这个模型感兴趣，或者想在自己的项目中尝试这种高效的评分函数，可以访问他们的开源项目：https://github.com/zelixirSH/HybridSP.git

---

_参考文献：Wang, Z., et al. (2026). Could statistical potential models achieve comparable or better performance than deep learning models? Briefings in Bioinformatics._

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/MftTT3icN14LQQdpA4HIHc4oZKpmEKZZbOaicy2WozCA0gZcKsQ9C3gE40XtJ5FdWlZc5RVTcmibTMF0IsF5Wic5eQ/0.png) 

 EnzymeDesign 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/MftTT3icN14LQQdpA4HIHc4oZKpmEKZZbOaicy2WozCA0gZcKsQ9C3gE40XtJ5FdWlZc5RVTcmibTMF0IsF5Wic5eQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
