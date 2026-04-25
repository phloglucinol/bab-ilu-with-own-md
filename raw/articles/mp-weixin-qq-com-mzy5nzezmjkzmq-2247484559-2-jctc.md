---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzY5NzEzMjkzMQ%3D%3D&mid=2247484559&idx=2&sn=f9c4401fee458f21449900c22fac2940
canonical_url: https://mp.weixin.qq.com/s?__biz=MzY5NzEzMjkzMQ%3D%3D&mid=2247484559&idx=2&sn=f9c4401fee458f21449900c22fac2940
source_domain: mp.weixin.qq.com
title: JCTC | 无需预训练数据：基于量子化学驱动的强化学习实现分子稳定异构体的逆向设计
author: 
published_at: 
fetched_at: 2026-04-25T02:03:20Z
extractor: wechat_worker
content_hash: 687c5ac5ae51e48b926af51aa74145448391111f3f888f62f48e622816c68d4f
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/yiab2uNgggg0Oz3v4CsHgtYicDYU1NkzNWw4Wg9uSoxzho70hgqTJtH1nXU2y3Cm0phrddGqROgUZ7ib4xZFtZ79Ppxc4Jn3fRgWhs5h7RxViak/0.jpg) 

# JCTC | 无需预训练数据：基于量子化学驱动的强化学习实现分子稳定异构体的逆向设计

原创 AI4Mat前沿 AI4Mat前沿 [ AI4Mat前沿 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3cJ6L4uxJMlHpZ1rJqzFQcmSv1CNGNLnFvfKnBIk1vNGRTkBYB1jrvej3Z6gnugpPiaCaFDrzw6QueIjpM45HWecGGxaqic9fgg/640.png)

**作者：** Francesco Calcagno¹_, Luca Serfilippi¹, Giorgio Franceschelli², Marco Garavelli¹, Mirco Musolesi², Ivan Rivalta¹_ 

**机构：** ¹博洛尼亚大学工业化学系；²博洛尼亚大学计算机科学与工程系 \*通讯作者

### 研究背景与科学问题

分子逆向设计（Inverse Design, ID）——即根据目标性质从头设计全新分子——被视为21世纪计算化学领域的核心挑战之一。其潜在应用涵盖催化剂工程、药物发现、分子储能材料等诸多前沿方向。然而，分子化学空间的规模极其庞大，结构与性质之间的映射关系又高度复杂，使得穷举式搜索在计算上不可行。

近年来，机器学习方法在分子生成领域取得了显著进展，尤其是基于强化学习（RL）的生成模型展现出巨大潜力。然而，现有方法大多依赖于大规模分子数据集进行预训练，这不可避免地引入了数据偏差，将化学空间的探索局限于训练集所覆盖的区域。遗传算法虽然无需训练数据，但其损失函数缺乏对候选分子生成的有效指导。此外，目前将量子力学（QM）第一性原理计算与无数据RL生成相结合的通用框架尚属空白。

### PROTEUS：无数据的量子化学驱动生成框架

针对上述瓶颈，本研究提出了一种名为PROTEUS的生成式人工智能工具，其核心创新在于完全摒弃预训练数据集，将强化学习与即时量子力学计算深度耦合，实现从第一性原理出发的分子从头设计。

PROTEUS的技术架构建立在两个关键设计之上。**第一**，研究团队引入了一种名为P-SMILES的定制化分子编码语法。P-SMILES基于经典SMILES表示法，但通过限制每个结构基元最多使用两个字符（单字符或双字符）来编码，大幅降低了语法复杂性，消除了SMILES语法中因编码不等价性而产生的生成偏差。这一简化对于无预训练条件下的化学语言学习至关重要。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg09dGniaiaickJTMMyQ8CgJAPNrd8ZOTR1LM0VK7bm1yepclNYVSNwqic7j1YZxniccowwHPP78HkzdfVxBFlHWL7QBibbpzBzplNaoU/640.png)

▲ Fig.1 | 化学空间分析与P-SMILES语法。(a)"参考E/Z空间"、(b) trans/cis子空间（即R2 = H）和(c) cis/trans子空间（即R1 = H）的主成分分析（PCA）。PCA使用Z构型分子的Morgan指纹，并根据基于DFT优化几何构型计算的能隙进行颜色编码。图中展示了具有最大能隙的分子的结构式及其P-SMILES字符串，即Ca1C(CCCCa1)CECC(EC)F（a和b）和Ca1C(CCCCa1)CECCONECF（c）。PCA分析已完成。

图1展示了化学空间的主成分分析（PCA）结果。研究者以苯乙烯骨架的几何异构体（E/Z异构体）为模型体系，通过Morgan分子指纹对参考E/Z空间及其子空间进行聚类分析。结果表明，分子可被分为三至四个主要簇，但各簇内的异构化能隙分布高度不均匀——同一簇中同时包含正值和负值，充分说明了该逆向设计问题中结构-性质关系的非平凡性。

**第二**，PROTEUS采用层次化的五模型RL智能体架构以适配P-SMILES语法特性。如图2所示，该架构包含：(i) 一个主决策模型，决定添加单字符、双字符还是终止生成；(ii-iii) 两个位置预测模型，分别确定单字符和双字符的插入位置；(iv-v) 两个生成模型，实际执行字符添加。这种层次化设计有效避免了逐字符生成方式对双字符编码特征（如环和分支结构）的惩罚效应。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg2ibmjlg9uTK4ic4bp2CeTZRVmt42p9U8Bpj3szK9VDl9uBlfrI22dQvohDpibXEs6w9ZVHaNicRwsFeJ8ngXDeMQVvlbHuU8TquibA/640.png)

▲ Fig.2 | 利用PROTEUS进行无数据分子生成。(a) 苯乙烯骨架（见插图）的两个取代基（即R1和R2基团）被嵌入P-SMILES字符串中。该字符串通过一个由五个模型组成的强化学习（RL）智能体算法迭代生成，包含一个主决策器以及单字符和双字符预测器。随后将所选的P-SMILES字符串附加到苯乙烯骨架上，如图中所示的一个简单示例：E异构体中R1 = COCH3且R2 = H（Z异构体则反之）。

图2详细展示了PROTEUS的完整工作流程。P-SMILES字符串生成后，经过一套严格的多步骤验证与计算管线：首先转换为SMILES并进行语法有效性检查；通过后先进行分子力学预优化，再经密度泛函紧束缚（DFT-TB）方法进行几何优化，并进行连接性验证；随后通过元动力学进行构象采样，最后以DFT方法优化最稳定构象。E和Z两种异构体分别经历上述流程后，计算其能量差作为化学奖励。

模型的总奖励函数将化学奖励与多样性奖励相结合。化学奖励量化了异构化能隙的大小，多样性奖励则基于Tanimoto相似性的互补值，鼓励智能体探索化学空间中的不同区域。两者之间的平衡由超参数调控，在充分利用已知高回报区域的同时避免陷入局部最优。

### 逆向设计实验验证

研究者首先在6个P-SMILES字符的化学空间中验证了PROTEUS的性能。该空间包含1628个化学有意义的E/Z异构体对，是从近195万种语法组合中筛选而出的。关键在于，研究者预先计算了该空间内所有分子的异构化能隙，从而能够精确评估PROTEUS的搜索效率。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg3n04NTGOgE9218kvE7M8O5XOhnPuX2TabkQg6HnMmlVUOPanYyuTyWJK6ZmTBQK3iah5ZgSIIOiaicFedqBtLggHmyVbsWCyH2d4/640.png)

▲ Fig.3 | 利用PROTEUS进行E/Z异构体的逆向设计。(a) 在6-token化学空间内，针对E/Z异构体的一次代表性PROTEUS模拟中，化学奖励和多样性奖励的时间演化过程。图中报告了每个训练轮次的均值（蓝色散点）和滑动平均值（红色实线）。首次生成最优解（其分子式和P-SMILES字符串见插图）所对应的训练轮次在"E/Z空间"中排序后以虚线标出。模拟共运行3000个训练轮次。

图3呈现了一次代表性模拟的训练动态。化学奖励在约250个世代后出现显著跃升，多样性奖励则在整个训练过程中保持较高水平，表明模型持续探索了化学空间的不同区域。在10次独立模拟中，PROTEUS在9次中均成功找到了全局最优解，平均仅需评估约1000个分子——这意味着模型仅需遍历化学空间的约60%即可锁定最优分子，充分展示了其高效的探索-利用平衡能力。

为进一步检验模型在更大空间中的可扩展性，研究者将搜索范围扩展至7个P-SMILES字符的化学空间，该空间包含2,430,845种语法有效组合，相比6字符空间扩大了一个数量级以上。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg1jxibGibvib0tF7UCrxf371ibMdk0oe6kBUaLxh4I6Gcu4ECibe7CmaH0gRw7iaFSG3qOQLslRiawaLxwNgaG1KfYuSdFZiaGsEaFmmtg/640.png)

▲ Fig.4 | 利用PROTEUS探索大规模trans/cis化学空间。在7个P-SMILES token的化学空间内，针对trans/cis异构体的一次PROTEUS模拟中，化学奖励和多样性奖励的时间演化过程。图中报告了每个训练轮次的均值（蓝色散点）和滑动平均值（红色实线）。图中标注了两个关键训练轮次：首次生成trans/cis能隙超过6-token化学空间中最优解能隙的解（灰色虚线），以及最优解的生成轮次。

图4展示了在这一大规模化学空间中的搜索过程。PROTEUS在约450个世代时即发现了优于6字符空间最优解的分子，并在后续训练中持续发现能隙更大的候选分子。值得注意的是，模型在探索过程中展现出对化学空间不同区域的系统性覆盖，表明多样性奖励机制有效引导了全局搜索。

### 方法学意义与创新贡献

PROTEUS框架的核心学术贡献体现在三个层面。**首先**，它实现了真正意义上的"无数据"分子逆向设计——不依赖任何预训练数据集，完全由量子化学计算驱动分子生成策略的学习，从根本上消除了数据偏差问题。**其次**，P-SMILES语法与层次化智能体架构的协同设计，为化学语言的无监督学习提供了一种新范式，其思路对其他分子表示学习任务同样具有启发意义。**第三**，研究通过在已知精确解的化学空间中进行严格基准测试，为分子生成模型的性能评估建立了可靠的方法论标准。

### 展望与启示

该框架的设计理念具有天然的可扩展性。P-SMILES语法可以方便地扩展至更复杂的分子体系，而量子化学计算模块也可灵活替换为适用于不同化学性质的计算方法。研究者指出，PROTEUS的应用场景可推广至催化剂设计（最小化反应决速步能垒）、分子光电材料设计等需要优化能隙相关性质的广泛问题。然而，当前方法的主要计算瓶颈仍在于每次分子评估所需的DFT计算成本，未来引入机器学习势函数或多保真度代理模型可能是提升效率的重要方向。总体而言，PROTEUS为无偏、基于第一性原理的分子逆向设计开辟了新的技术路径，对计算化学与人工智能的交叉研究具有重要参考价值。

---

****参考文献：Francesco Calcagno\*, Ivan Rivalta\* _et al._ Quantum Chemistry-Driven Molecular Inverse Design of Stable Isomers with Data-Free Reinforcement Learning. J. Chem. Theory Comput. (2026).https://doi.org/10.1021/acs.jctc.5c02055**

****本文由AI4Mat前沿编译分享，旨在学术交流。文中所有图文版权归原作者及出版社所有。**

****关注我们,获取更多AI+材料前沿进展**

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3dePnhYnbJVMpcphQbicTIgcMjbKb36Q3LE6C5V3e39ZjDgMYD0wZTgTCu3xHZuUKnZt8icHsWtpqrkWRI5SdIYXH3icaAtV8IyY/0.png) 

 AI4Mat前沿 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3dePnhYnbJVMpcphQbicTIgcMjbKb36Q3LE6C5V3e39ZjDgMYD0wZTgTCu3xHZuUKnZt8icHsWtpqrkWRI5SdIYXH3icaAtV8IyY/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
