---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkzNjIzMTU0Nw%3D%3D&mid=2247548964&idx=1&sn=593ccad4ae7a0c008a49bf608d04a4a7
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkzNjIzMTU0Nw%3D%3D&mid=2247548964&idx=1&sn=593ccad4ae7a0c008a49bf608d04a4a7
source_domain: mp.weixin.qq.com
title: NCS | 高效化学空间探索模型加速药物发现
author: 
published_at: 
fetched_at: 2026-04-25T02:04:15Z
extractor: wechat_worker
content_hash: a9e5b0d58ecb761744c742c042f98b9b6167c44c2478c32f439c4b1cc11e4b29
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/GSyZB2NwFcW942j89oZwNWkPib4N62geG7hTIPxeicibgLSpEbUNFicrQicOzVdw3AY22M1YEPg2hBpuuxqibdTF5lXA/0.jpg) 

# NCS | 高效化学空间探索模型加速药物发现

三寸不烂之舌 三寸不烂之舌 [ AIDD Pro ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcW942j89oZwNWkPib4N62geGPtKrKx3COs9418xwmcz9Eiap10dCaUrqtUwKVtC5DwxX9x0Q3me9M2w/640.png)

今天给大家讲一篇2025年11月在nature computer science上发表的一篇基于结构的分子生成文章。为了解决现有分子生成方法设计的分子可合成性不佳、多样性不足的问题，本研究设计了SynGFN模型。该模型创新性地将分子构建过程模拟为可执行的化学反应步骤，通过融合分层预训练与多保真度优化策略，直接从可合成的化学空间中进行高效探索。在针对特定神经疾病靶点的实验中，该模型成功设计出具有体外抑制活性的新颖结构的分子，并同步生成了经实验室验证可行的合成路线，为未来实现智能化药物设计奠定了基础。  

01 引言

### 设计-合成-测试-分析（DMTA）循环是一种系统化的研究方法，广泛应用于药物发现与材料科学等领域。其目的在于通过假设、实验、学习的快速闭环，从海量候选化合物中高效筛选出性能最优的分子或材料。传统DMTA循环中，计算化学家在设计阶段提出的理想分子，可能在合成阶段步骤冗长或成本高昂导致其在实际应用中被排除，并且整个过程依赖人工经验与试错，迭代周期长，难以广泛探索新颖且多样的化学空间。

为提升生成分子的多样性，基于流的生成模型通过可逆变换架构实现了对化学空间广泛探索。通过在训练过程中引入特定的目标属性约束从而引导生成高质量的分子。例如，GFlowNets通过为分子生成轨迹分配奖励，引导模型生成满足特定属性约束的分子，显著提升生成分子的多样性。此外，还结合反应模板或合成路径规划直接生成具有可行合成路线的分子，实现了药物分子设计与合成规划的结合。基于流的方法生成的分子不仅能覆盖已知化学空间，更能扩展到未知的候选药物空间，从而高效构建结构多样且易于合成的候选分子库。

02 SynGFN模型架构设计

为了解决现有分子生成方法设计出的分子多样性不足、且往往设计出大部分的分子可合成性不佳的问题，作者提出了基于流的生成模型SynGFN模型。它将分子设计过程建模为马尔可夫决策过程，通过一系列模拟化学反应来构建目标分子。该架构由一个分层策略网络引导，其中包含两个独立的神经网络（反应选择网络与试剂选择网络），前者负责根据当前分子状态输出反应模板的概率分布，而后者则在选定反应后，从庞大的反应物库中识别并输出兼容试剂的概率分布。这种设计确保了每一步分子组合过程的化学合理性。在训练流程中，SynGFN采用在线学习方式，通过不断采样生成轨迹，并利用轨迹平衡损失函数进行优化，目标是使生成分子的概率与其奖励值（如生物活性）成正比。为了进一步提高生成分子的质量，作者还引入了预训练技术，通过一个多标签分类任务提前让试剂选择网络学会识别与反应模板兼容的试剂，从而有效加速了模型的收敛。最终，经过训练的SynGFN不仅能高效探索广阔的化学空间，还能在生成分子的同时，直接输出一条可行的合成路线，实现了分子设计与合成规划的集成，为人工智能助力药物分子设计提供了更有效的方案（图1）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcW942j89oZwNWkPib4N62geGUticZxzWZ7BIiaqf7U00pyadjIWpaWey9iaksManK9dDQ60rzPXgy59WQ/640.png)

图1 SynGFN分子生成流程

03 实验结果分析

#### 3.1 与现有基准方法在类药属性方面的评估

**为了有效评估SynGFN**模型生成分子的质量，作者将其与三种代表性的生成模型（SyntheMol、SynFlowNet 和 REINVENT4.0）进行了比较实验。具体而言，首先选取了 Aurora 激酶 A、D2 多巴胺受体和 sEH 作为特定靶点，并对每个模型分别采样10,000 个分子进行评估。其中各个方法在生成结果上有所不同，如SynFlowNet 生成分子图，而 SynGFN 则生成**合成轨迹序列**，以实现更直观的**合成**过程。通过进一步分析 QED 和 logP 的分布，可以发现SynGFN、SyntheMol 和 SynFlowNet 生成的分子均表现出较高的类药性，这可能得益于它们基于反应的组装方式。此外，基于排名前 1,000 个分子的 t-SNE 可视化结果表明**SynGFN 在新颖性和化学空间覆盖方面优于其他模型（图2）**。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcW942j89oZwNWkPib4N62geGGaeE6icshY5smVT0cj2Y90eRAgMt1P7c7KjD0PHUG1ibshIVlGic2qMibA/640.png)

图2 不同分子生成模型生成分子属性评估

#### 3.2 配体结合效率评估

为了进一步评估SynGFN生成分子的潜在生物活性，作者使用AutoDock Vina计算了四种不同SynGFN架构（SynGFN-S、SynGFN-M、SynGFN-L、SynGFN-XL）及基准方法所生成分子的对接分数。实验结果表明，SynGFN-XL模型在多个靶点上能高效生成大量具有高结合潜力的候选分子，并且其生成高质量分子的数量显著超过传统基准模型。

考虑到对接分数可能对大分子结构存在固有偏好，研究进一步引入配体结合效率指标进行校正分析。数据表明，SynGFN架构生成分子的配体结合效率也具有一定优势，即在维持良好结合亲和力的同时，同样也能更高效地探索化学空间。然后，研究将生成分子与已知实验验证的活性化合物进行深入比较。发现两者在关键靶点上的配体结合效率分布存在显著重叠，且生成分子的结合构象与已知活性物结构高度相似，这些分子能够准确匹配蛋白结合口袋的几何形状，并形成稳定的相互作用网络，将为研发人员提供更有效的疾病治疗方案（图3）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcW942j89oZwNWkPib4N62geGvh7GAEGtVg3nd5lyfVSibWyTkEnGnozbcgKnLT0qLPuZsZjTuH7icT0Q/640.png)

图3 不同分子生成模型生成分子配体结合效率评估

#### 3.3 GluN1/GluN3A 靶标上的案例分析

为了验证SynGFN模型在攻克缺乏三维结构信息的困难靶点方面的实际应用能力，作者进行了一项针对兴奋性甘氨酸受体（eGlyR） 的药物发现实验。首先以两个已知的变构调节剂（EU1180-438和WZB117）的三维形状为模板，利用SynGFN在化学空间中高效探索并生成结构匹配的分子。实验结果表明SynGFN不仅生成出十个候选分子，更为每个分子提供相应的合成路线。此外，在短短30天内，所有十个分子均被成功合成并完成测试，效率比传统化学合成提升了一倍，而且其中六个分子展现出明显抑制活性，命中率较高。因此，即使对于缺乏三维结构信息的靶点而言，通过结合已知活性分子的形状信息依旧可以高效地发现潜在的候选化合物（图4）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcW942j89oZwNWkPib4N62geGicFM5lUzeFh05Z8I7aP2CboTcfjQk22rPAzxBmyyw0g4aIuAwC1Oz6A/640.png)

图4 候选分子可视化展示

04 总结

为了解决现有分子生成方法设计的分子难以合成、且化学空间探索效率不高的问题，作者设计了**SynGFN模型**，它基于化学反应的分子组装策略，能够实时生成分子并同时提供可行的合成路线。为了从多个维度对其进行评价，还设计了相应的计算与实验。首先，在针对GluN1/GluN3A受体亚型的抑制剂设计中，SynGFN在30天内成功合成了10个候选分子，其中6个在体外展现出抑制活性，效率较高。其次，作为虚拟筛选工具，其较小的搜索范围却能覆盖较广阔的高活性化学空间。不过该方法仍存在局限性。当前的验证仅集中于针对单一受体亚型（GluN1/GluN3A）的体外抑制剂设计。开发同时具有靶点特异性且在**全细胞环境中具有活性**的分子，仍然是一个重大挑战。即便如此，SynGFN已展现出在药物分子设计中的潜在价值，并可能成为一种加速**设计-合成-测试-分析循环**、推动分子设计研究的有用方法。

### 参考文献

Zhu Y, Li S, Chen J, et al. SynGFN: learning across chemical space with generative flow-based molecular discovery\[J\]. Nature Computational Science, 2025: 1-10.

**版权信息**

本文系AIDD Pro接受的外部投稿，文中所述观点仅代表作者本人观点，不代表AIDD Pro平台，如您发现发布内容有任何版权侵扰或者其他信息错误解读，请及时联系AIDD Pro (请添加微信号Cynthia\_qin1114)进行删改处理。

本文为原创内容，**未经授权禁止转载，授权后转载亦需注明出处**。有问题可发邮件至qinxin@stonewise.cn

****关注我，更多资讯早知道↓↓↓**

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/GSyZB2NwFcVEduxRt4IviciaicmLciaV7xcHYG2MrpsblicPZib20yh4vNNOmdNftgu0icAl8AlnonUepCX6MOc7vYcMQ/0.png) 

 AIDD Pro 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/GSyZB2NwFcVEduxRt4IviciaicmLciaV7xcHYG2MrpsblicPZib20yh4vNNOmdNftgu0icAl8AlnonUepCX6MOc7vYcMQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
