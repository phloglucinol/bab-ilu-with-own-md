---
type: raw_article
source_url: http://mp.weixin.qq.com/s?__biz=MzkzNjIzMTU0Nw%3D%3D&mid=2247547772&idx=1&sn=186c0401ef02dc902b128478650fbf4b
canonical_url: http://mp.weixin.qq.com/s?__biz=MzkzNjIzMTU0Nw%3D%3D&mid=2247547772&idx=1&sn=186c0401ef02dc902b128478650fbf4b
source_domain: mp.weixin.qq.com
title: JCIM | 专家介入？有效评估药靶相互作用任务
author: 
published_at: 
fetched_at: 2026-04-25T02:04:36Z
extractor: wechat_worker
content_hash: 2587fdf1f0a2408f070b827629ed2e115d341b6063f016fe2df234c0e916116b
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/GSyZB2NwFcWJicfWXibIK90yPtZvl5wEt7bLXwM97dHB0LPpRlzItSHhyM6icC5TIvIILo7iaewEu9oxGBb541clWA/0.jpg) 

# JCIM | 专家介入？有效评估药靶相互作用任务

三寸不烂之舌 三寸不烂之舌 [ AIDD Pro ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcWJicfWXibIK90yPtZvl5wEt7wcC9764xAU358WD0Cs6LOKXHYB9Ud0zomiaAicbQgq5AV2eGibrcvJibEA/640.png)

今天给大家讲一篇2025年1月在JCIM上发表的一篇关于**药物靶点相互作用预测**的文章。在药物-靶点相互作用（DTI）预测任务中，传统深度学习方法虽有效，但往往仅从单一角度表征药物特征，缺乏全面性，且药物和蛋白质特征融合方法需要改进。因此，作者提出了**一种** **端到端的框架DO-GMA，它通过深度可分离卷积神经网络学习药物和蛋白质特征，并通过门控和多头注意力机制融合这些特征，最后使用多层感知机进行分类**。在四个DTI数据集上的实验表明，DO-GMA在多个评价指标上显著优于目前六种DTI预测方法，且经过验证分析后成功预测了潜在的药物-蛋白质相互作用对，为药物设计提供了有价值的信息，有望进一步加速药物发现和优化过程。

  
01

引言

**药物-靶点相互作用（DTI）预测**在药物发现中起着至关重要的作用，可以帮助药化专家们快速识别出可能与特定药物结合的蛋白质靶点，从而加速早期药物筛选过程。然而，尽管体外实验在筛选新的DTIs方面是可靠的，但由于其耗时耗力限制了其在大规模应用中的可行性。相比之下，基于计算机模拟的方法能够有效缩小候选药物的筛选范围，为发现新疗法提供了新的途径。随着人工智能技术的发展，**深度学习方法**在DTI预测中表现出显著优势，通过学习药物-靶点对之间的相关性，从而提升预测的准确性，如图注意力网络DTIGCCN、GADTI等能处理药物和蛋白质的图结构数据，并能高效地整合多种数据源以分析药物与靶点之间的相互作用，可以更好地理解药物的作用机制，这对于药物的后续优化和至关重要。

  
02

DO-GMA架构及设计流程

作者设计了一种方法（DO-GMA）用于预测药物-靶点相互作用，首先通过结合DO-Conv和GCN网络分别从药物的序列以及分子图中提取特征，然后使用DO-Conv从氨基酸序列中学习蛋白质特征。接着，通过门控多头注意力机制（GMA）将药物和蛋白质的特征进行融合。最后，利用多层感知机（MLP）对下游的药物-靶点对进行分类以判断是否发生相互作用。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcWJicfWXibIK90yPtZvl5wEt7DiaF898myqAiaK3KMBUwianicicCibGLyNAhRwSWwBqOk9zjarySRnNYSYlg/640.png)

图1 DO-GMA模型架构

  
03

实验结果

#### **3.1 DTI预测性能评估**

为了评估DO-GMA在预测DTI任务上的表现，作者采用四种不同的划分方式对训练数据进行划分，其一是药物与靶标对都在训练集中（E1），其二是药物不在训练集中，且相应的靶标在训练集中（E2），其三是靶标不在训练集中，且相应的药物在训练集中（E3）。其四是相应的药物靶标对均不在训练集中（E4）。对于每种策略，作者选择了多个基准方法在六个数据集上（如BindingDB）进行了10次独立的实验，且每次实验使用不同的随机种子来分割数据集。实验结果表明**在DrugBank数据集上，DO-GMA在所有四种实验设置E1、E2、E3和E4下，AUC、AUPR等五个分类指标都优于六个基准方法**（图2）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcWJicfWXibIK90yPtZvl5wEt7IsTMuxr4rYxuQJAR5KqUO0COibMCv2selFBcyibBbu2HTibyY4TJIjGUQ/640.png)

图2 DrugBank数据集上性能评估实验

#### **3.2 消融实验分析**

为了探究DO-GMA不同模块对药物-靶点相互作用（DTI）预测的影响，作者对该框架进行了**消融实验**（图3）。首先为了验证DO-Conv在药物和蛋白质表示学习中的效果，实验中将DO-Conv替换为卷积神经网络（CNN）来提取药物特征和蛋白质特征。进一步，为了评估药物单模态特征学习（仅SMILES序列或2D分子图）和多模态特征学习（结合SMILES序列和2D分子图）对预测效果的影响，还额外设计了两个DO-GMA变体，Uni-S（输入信息为药物SMILES序列 + 蛋白质序列）和Uni-M（输入信息为药物2D分子图 + 蛋白质序列）。此外，还对注意力机制进行了消融分析，分别为门控注意力机制和多头注意力机制。实验结果表明**DO-GMA框架中的各个模块都有助于提高DTI预测性能**，其中多头注意力机制对性能的提升最为显著，且当整合这些模块时实现了最佳的预测性能。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcWJicfWXibIK90yPtZvl5wEt78qtT2XZS4XewqWgTu3G8dbP5U3grpxPYgZ8QCh7YyHibIibhSKPqicz4A/640.png)

图3 四个数据集上的消融实验

#### **3.3 蛋白与药物特征可视化**

为了表征融合的蛋白与药物的特征的分布，作者**使用了** **UMAP进行降维**，并可视化了三种不同的数据类型（图4）。其一是通过DO-Conv提取的药物SMILES字符串特征、通过GCN提取的药物2D分子图特征，以及通过DO-Conv提取的蛋白质序列特征，称之为V1。其二是带有真实标签的药物-靶点对（DTPs）的融合特征，称之为V2。其三是带有预测标签的药物-靶点对的融合特征，称之为V3。结果发现，**DO-GMA能够有效地将药物和蛋白质特征映射到不同的区域，从而生成更密集的药物和蛋白质子群体**。此外，预测标签的融合特征可视化结果与真实标签的结果基本一致，这表明**DO-GMA在在区分相互作用和非相互作用的药物-靶点对方面的有效性**。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcWJicfWXibIK90yPtZvl5wEt7W16HsBnIIA8Y88UCGJWS4ibfAfn8C5rqOduuQKEP3I318qC32GRO8Mw/640.png)

图4 四个数据集上融合特征的可视化

  
04

结论

在药物发现领域，药物-靶点相互作用（DTI）预测的重要性日益凸显，但现有的计算方法在预测性能、计算资源和表征学习方面存在局限性。针对这些问题，作者**提出了一种名为DO-GMA的新方法，该方法结合了DO-Conv、图卷积网络、门控注意力机制和多头注意力机制，通过共享学习查询策略来融合药物和蛋白质特征，并使用多层感知器进行分类**。该方法不仅提高了DTI预测准确性，节省了时间和资源，还有助于药化专家对药物作用机制进一步分析，从而促进了新药的开发和优化。未来，DO-GMA将有助于辅助药化专家快速识别潜在的DTIs，指导他们更有效地开发新药，从而加速药物发现和开发的过程。

**参考文献**

\[1\] Peng L, Mao J, Huang G, et al. DO-GMA: An End-to-End Drug–Target Interaction Identification Framework with a Depthwise Overparameterized Convolutional Network and the Gated Multihead Attention Mechanism\[J\]. Journal of Chemical Information and Modeling, 2025.

**版权信息**

本文系AIDD Pro接受的外部投稿，文中所述观点仅代表作者本人观点，不代表AIDD Pro平台，如您发现发布内容有任何版权侵扰或者其他信息错误解读，请及时联系AIDD Pro (请添加微信号sixiali\_fox59)进行删改处理。

本文为原创内容，**未经授权禁止转载，授权后转载亦需注明出处**。有问题可发邮件至sixiali@stonewise.cn

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
