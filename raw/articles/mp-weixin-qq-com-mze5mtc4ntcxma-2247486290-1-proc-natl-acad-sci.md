---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzE5MTc4NTcxMA%3D%3D&mid=2247486290&idx=1&sn=2b0ce99c4a2af5db6148d599c302feda
canonical_url: https://mp.weixin.qq.com/s?__biz=MzE5MTc4NTcxMA%3D%3D&mid=2247486290&idx=1&sn=2b0ce99c4a2af5db6148d599c302feda
source_domain: mp.weixin.qq.com
title: Proc. Natl. Acad. Sci. | 用于基于结构的药物设计的流形约束核级去噪扩散模型
author: 
published_at: 
fetched_at: 2026-04-25T02:04:27Z
extractor: wechat_worker
content_hash: fc7cf57691fe98d24a52dbb6c4325300f8c142c24748aa7f47a8cb0a31f74e91
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/jwaic6a7a9gNpibia4icEuZcIdzuubh484O9icAoarCY2pknRS1r60kCP6ZV2odBRjib8UNC7WibS8N99Izm2ZAQfvg1w/0.jpg) 

# Proc. Natl. Acad. Sci. | 用于基于结构的药物设计的流形约束核级去噪扩散模型

原创 DrugOne DrugOne [ DrugOne ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

DRUGONE

基于结构的药物设计（SBDD）旨在利用蛋白三维结构生成能够与靶点高效结合的小分子。然而，现有扩散模型在三维分子生成中往往偏离物理可行的化学流形，导致生成分子稳定性不足或结合构象不合理。为解决这一问题，研究人员提出 NucleusDiff—— 一种在化学流形上进行约束采样的去噪扩散模型。该方法以“原子核”为最小生成单元，在扩散过程中引入流形投影与几何约束，确保生成轨迹始终位于物理合理的能量面。NucleusDiff 能捕捉分子构象的低维内在结构，实现了在 SBDD 任务中的更高稳定性、有效性与结合能预测性能。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNpibia4icEuZcIdzuubh484O9SzLgA2r7O7K4pdvtdhuRZpwgWtkfGkzgRFZsWvKojiaA4xY0HDBehgQ/640.png)

近年来，扩散模型已被广泛应用于分子生成和蛋白–配体复合物设计。通过在三维空间中逐步去噪，它们能从随机坐标生成结构合理的分子。然而，传统的三维扩散模型存在以下两个瓶颈：

* **化学不合理性** —— 直接在笛卡尔坐标上加噪会导致生成结构超出真实分子流形（如键长异常、角度畸变）；
* **缺乏几何一致性** —— 模型未显式考虑分子势能面的流形约束，生成结果可能偏离低能量区。

在化学空间中，真实分子的构象分布受键长、键角、非键相互作用与电子密度共同决定，形成高维势能面的低维“可行流形”。研究人员因此提出在扩散模型中嵌入流形约束机制，使生成过程符合化学物理规律。通过“核级（nucleus-level）”表示，模型能以原子核为中心捕捉结构几何与电子特征之间的耦合关系。

  
**方法**

NucleusDiff 的核心思想是在分子生成的扩散过程中引入几何流形约束，以保证生成分子的物理一致性。

整个模型包含三个关键组件：

* **核级表示（Nucleus-level representation）：**  
将分子表示为原子核位置及其局部电子环境特征，以几何方式表达分子内的键长、键角与电子势能分布。
* **流形约束扩散（Manifold-constrained diffusion）：**  
在去噪采样过程中，NucleusDiff 通过投影操作确保每一步采样保持在化学势能面对应的流形上，避免偏离可行的物理区域。
* **结构引导（Structure-guided constraint）：**  
结合蛋白结合口袋的空间几何、电势和疏水性信息，引导生成分子在扩散过程中逐步贴合靶标结构。

在训练阶段，模型以蛋白–配体复合物为输入，学习去噪分布到真实结构的映射；在生成阶段，从高噪声分布逐步采样分子核位置，直至得到物理合理且能量稳定的三维构象。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNpibia4icEuZcIdzuubh484O9k1OPQeT2EutspdsSs8oh0xaPkdgHUDiacyVQ9M4Dq0miaiaL1uY57BIdA/640.png)

**结果**

**模型整体性能与生成质量**

研究人员在 PDBbind 和 CrossDock2020 数据集上评估了 NucleusDiff 的性能。在分子生成任务中，NucleusDiff 显著优于基线模型（如 TargetDiff、Pocket2Mol、DiffDock）：

* 分子有效率（validity） 提升至 98.2%；
* 平均 QED 提高约 0.07；
* 对接能（Docking score） 平均提升 1.3 kcal/mol；
* 生成构象的 RMSD 仅为 1.9 Å。

这些结果表明，NucleusDiff 能在保持高生成质量的同时生成更具化学可行性的配体结构。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNpibia4icEuZcIdzuubh484O9DH4GlJr7sH33ClSQ1XprZQ73ptvb0MMicNCSGA0McFIkmKNBYicJIXkA/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNpibia4icEuZcIdzuubh484O9GOIFHjqpPxdaNiaUP7iafXFWO5xU0hEQ6qE4L3Zd9aV687UwoicicQb6PQ/640.png)

  
**流形约束在生成过程中的作用**

为验证流形约束的重要性，研究人员分别训练了带约束与无约束的模型。

  
结果显示：

* 无约束扩散模型在采样早期阶段易偏离真实结构分布，生成的分子出现化学键拉伸、空间重叠等现象；
* 加入流形约束后，扩散轨迹保持在低势能区域，生成分子在几何与能量上更接近真实复合物。

研究人员通过势能分布分析发现，NucleusDiff 生成的样本主要集中于实验分子的能量分布范围内，说明模型成功学习了分子构象的物理规律。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNpibia4icEuZcIdzuubh484O9po05FspnTk1jhXicRTMFWxztNnPatVflYUFgyfYjc2Via8PREBsa48Mw/640.png)

  
**模型的可解释性与泛化能力**

NucleusDiff 的核级建模使得每个生成步骤均具物理可解释性。研究人员通过可视化生成轨迹发现，模型逐步形成稳定的键长与角度，并在靠近靶点结合口袋时自发生成氢键和疏水配位。在未见过的蛋白靶点（如 HIV-1 蛋白酶、EGFR、MDM2）上，NucleusDiff 仍能生成具药效团特征的配体，展示出良好的跨靶点泛化性能。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNpibia4icEuZcIdzuubh484O9zWPlywa3sic0Mu5SxYHBUwxqxS0sLVfTuhadOECDib4FIHibAA778ppRg/640.png)

  
**讨论**

NucleusDiff 在扩散建模中引入化学流形约束，为结构基础药物设计提供了新的物理一致性生成范式。

与传统三维扩散模型相比，其主要优势包括：

* 流形一致性 —— 保证生成分子始终位于化学势能面上；
* 核级建模 —— 在原子核层面显式引入电子环境特征；
* 结构引导 —— 有效利用靶蛋白几何与能量信息指导生成方向。

研究人员指出，未来的改进方向包括：

* 结合量子力学能量函数进一步增强物理精度；
* 扩展至反应路径建模与多靶点生成；
* 将流形约束思想推广至蛋白–蛋白相互作用界面建模。

总体而言，NucleusDiff 实现了从物理一致性到药物设计可解释性的融合，为高精度的结构导向分子生成奠定了新基础。

整理 | DrugOne团队

  
**参考资料**

  
S. Liu,L. Yan,W. Du,W. Liu,Z. Li,H. Guo,C. Borgs,J. Chayes, & A. Anandkumar, Manifold-constrained nucleus-level denoising diffusion model for structure-based drug design, Proc. Natl. Acad. Sci. U.S.A. 122 (41) e2415666122, 

https://doi.org/10.1073/pnas.2415666122 (2025).

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/mS8qdZ3O8bgdeoYb8GbWMEQtibvyWMWd4ibMHwnXR3p2ib7OFjXc5270g3H1H58WIiclWBQibtJZHIUtWBGcl2czITw/640.gif)

**内容为【DrugOne】公众号原创**｜转载请注明来源

预览时标签不可点

[阅读原文](javascript:;) 

修改于 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNehllibjzmuk4oLoB5rbwiaptSMEyFTTvTGzKpWggLwMXaOg5D9z1CFfdjdkorM4IHicxibkXEAe2IPA/0.png) 

 DrugOne 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNehllibjzmuk4oLoB5rbwiaptSMEyFTTvTGzKpWggLwMXaOg5D9z1CFfdjdkorM4IHicxibkXEAe2IPA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
