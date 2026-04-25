---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkxNDIzMTcxNw%3D%3D&mid=2247522405&idx=1&sn=ea2a4e4001aa7e5207ce3418305a62ab
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkxNDIzMTcxNw%3D%3D&mid=2247522405&idx=1&sn=ea2a4e4001aa7e5207ce3418305a62ab
source_domain: mp.weixin.qq.com
title: Nature Machine Intelligence 2025｜消除数据偏差可提升结合亲和力预测的泛化能力
author: 
published_at: 
fetched_at: 2026-04-25T02:04:24Z
extractor: wechat_worker
content_hash: 33bed335fea04002b52348ff57746fcaee180db2d4efee62fc9b1615da9fc1b6
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr739WdUXuo38cRlFWtPPawKNicgEwhpQhyZQIR2VqyP0e1nyYtBYD91Ixg/0.jpg) 

# Nature Machine Intelligence 2025｜消除数据偏差可提升结合亲和力预测的泛化能力

AI in Graph AI in Graph [ AI in Graph ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

# 欢迎向本公众号投稿文献解读类原创文章，投稿邮箱：380198025@qq.com，请将稿件以附件形式发送。海内外招生、访学、招聘等稿件，请联系微信：xiongzhankun1997。

编辑 | 赵旭磊  

审核 | 黄锋

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr73BCnEZroxQFEic52Hq9BczQgAZpXDHa2qI8dfrIA6mrAGhYEblnVqK5g/640.png)

## 摘要

 今天给大家分享一篇发表在Nature Machine Intelligence上的论文：“Resolving data bias improves generalization in binding affinity prediction”。  
 计算药物设计领域需要准确的评分函数来预测蛋白-配体相互作用的结合亲和力。然而，PDBbind数据库与用于评估打分函数的Comparative Assessment of Scoring Function（CASF）基准数据集之间存在训练-测试数据泄漏，严重夸大了现有深度学习结合亲和力预测模型的性能指标，导致对其泛化能力的高估。在此，作者提出PDBbind CleanSplit，这是一个通过新的基于结构的过滤算法策划的训练数据集，可消除训练-测试数据泄漏以及训练集内部的冗余。在CleanSplit上重新训练当前表现最佳的模型后，它们的基准性能大幅下降，表明现有模型的性能主要由数据泄漏驱动。相比之下，作者的图神经网络模型在CleanSplit上训练时仍能保持较高的基准性能。通过利用蛋白-配体相互作用的稀疏图建模以及从语言模型进行迁移学习，模型能够泛化到严格独立的测试数据集。

## 研究背景

 近年来，基于结构的药物设计（SBDD）在计算药物发现中日益重要，其目标是设计能与特定蛋白靶点高亲和力结合的小分子。随着深度学习的发展，诸如AlphaFold3、RoseTTAFold All-Atom、Boltz-1等模型不仅能预测蛋白质结构，还能考虑配体结合；RFdiffusion和DiffSBDD等生成式模型更能直接设计新的蛋白质-配体相互作用。然而，这些生成结果并不一定具备真实的药物亲和力，因此仍需依赖评分函数来评估结合强度。  
 传统评分方法在精度与效率上存在局限。深度学习模型虽展现潜力，但常因训练集PDBbind与测试集CASF之间的相似性导致数据泄漏，使模型表现被高估。为解决这一问题，研究者开发了基于结构的聚类算法，重新划分数据集，构建了严格无重叠的PDBbind CleanSplit，并在此基础上重新评估现有模型，结果显示其性能显著下降，验证了以往结果的不可靠性。  
 为提升模型泛化能力，团队进一步提出结合图神经网络与大型语言模型迁移学习的新架构——GEMS。在经过清洗的数据集上训练后，GEMS在CASF基准上实现了领先性能，并展现出真正的泛化能力。  
 GEMS的出现填补了当前SBDD中缺乏高精度、强泛化评分函数的空白。它不仅能为生成模型提供可靠的亲和力评估，还为发现具有治疗潜力的新型蛋白质-配体相互作用提供了强大支持。研究团队已将GEMS完全开源，为AI驱动的药物设计带来了新的突破。

## 研究方法

### PDBbind CleanSplit构建

 为了解决数据泄漏这一核心问题，该研究提出了一种新颖的、基于结构的过滤算法，其工作流程如下图所示：![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr738tK9jQPibdLzsydv6vkHl4REOsXjVUd7VYRlXZdjODnC0kasx7kBDgg/640.png) 首先（图a），该算法从三个维度综合评估两个蛋白质-配体复合物的结构相似性。它不仅使用“Tanimoto分数”来比较小分子配体的化学结构相似度，还引入了“TM分数”（通过TM-align工具计算）来比较蛋白质的三维结构。这种方法的强大之处在于，它能识别出那些即便氨基酸序列差异很大、但3D结构依然高度相似的蛋白质。最后，算法还通过“口袋对齐的配体rmsd”来精确定量配体在蛋白质结合口袋中的位置和姿态是否一致。  
 随后（图b），算法会通过一个四层决策树来判断是否排除训练集中的某个复合物。第一层，它会比较二者的亲和力标签。一个非常关键的设计是：如果两个复合物结构高度相似，但结合活性差异巨大，算法会保留这个数据点，因为它能为模型提供极其宝贵的构效关系信息。第二层则严格排除那些与测试集配体相同（Tanimoto>0.9）且亲和力相近的训练数据，以防止模型通过“记忆配体”来作弊。最后两层则基于蛋白质相似性和配体/结合构象的综合相似性进行排除。这种分层策略使得该算法能够精准识别出具有相似相互作用模式的复合物，其效果远超传统的基于序列的比对方法。

### GEMS模型设计

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr73FtMMtLnEUH4ZVTGHzib27MAPcdzS0U8Tjypz1Z9Th8CqG0bPr4BP82A/640.png) GEMS模型的工作流（如上图所示）首先是将复杂的三维蛋白质-配体结构，转换成一个信息密集的“交互图” 。在这个图表示中，配体小分子被构建为原子水平的图（节点是原子，边是化学键），而蛋白质的结合口袋则被构建为氨基酸水平的图（节点是氨基酸残基）。随后，模型会根据原子间的空间邻近性，在配体节点和蛋白质节点之间建立“交互边”，从而捕捉它们之间的非共价相互作用。  
 GEMS的关键创新在于它如何利用大型语言模型来丰富这个交互图。它不仅使用原子的基本化学属性作为特征，还引入了多个LLM的嵌入 。具体来说，它使用蛋白质语言模型来为蛋白质的氨基酸节点生成特征，并使用化学语言模型来为整个配体分子生成一个全局特征嵌入。这相当于让模型在开始计算前，就已经获得了关于分子结构和生物功能的丰富先验知识。  
 在模型架构上，GEMS采用了一种先进的图神经网络设计，通过交替运行的节点卷积和边卷积层来处理这个富含信息的交互。在这个计算过程中，信息会在原子、氨基酸以及代表整体的全局特征之间动态传递和更新。最后，模型汇总所有学到的信息，通过一个全连接的回归器，输出对绝对结合亲和力（pK值）的精准预测。

## 实验结果

### PDBbind数据泄漏分析

 研究者针对PDBbind与CASF基准数据集之间的潜在数据泄漏问题进行了系统分析。通过设计基于结构相似度的过滤算法，计算了每对训练–测试复合物之间的蛋白结构相似度（TM-score）、配体化学相似度（Tanimoto系数）以及结合位点配体位置相似度（口袋对齐RMSD）。这三个指标被综合为一个整体相似度评分S=TM+Tanimoto+(1−RMSD)−ΔpK，用于定量评估两个复合物的整体相似程度。高S值表示两者在结构与亲和力标签上高度相似，从而容易导致模型通过记忆而非学习获得高预测精度。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr735SnuSAaicnTqHqEwp0hPAw7hBPxQ6o9FAZoLLWbsyNFk24r4urTtDOw/640.png) 如上图所示，图a展示了在过滤算法应用前，训练集与测试集之间存在大量几乎完全重叠的复合物结构。灰色为测试集蛋白，蓝色为训练集蛋白，品红与绿色分别代表测试和训练配体。可见如1O3F–1O3G、3DD0–3DCW等复合物在结构与亲和力上几乎相同（Tanimoto=1.00、TM=1.00、RMSD≈0Å、ΔpK≈0），表明模型可能通过“记忆”已见过的复合物获得高分，即存在严重数据泄漏。  
 图b显示在应用过滤算法后，同样的测试复合物与CleanSplit训练集中最相似的复合物相比，相似度显著下降（如1O3F–1O2Q，Tanimoto=0.58，RMSD≈1Å），重叠明显减少，说明算法有效去除了高相似度样本。  
 图c展示了过滤后仍存在的最相似样本。它们的结构重叠较小、取向差异明显，综合相似度S值约1.6–1.7，远低于过滤前的约3.0，说明PDBbind CleanSplit数据集已在很大程度上消除了结构与标签层面的数据泄漏。

### 重新训练前沿模型

 研究者进一步探讨了PDBbind数据集内部的训练–测试数据泄漏问题是否也导致了许多前沿模型的性能被高估。为此，他们尝试复现主流深度学习评分函数的原始结果，并在经过严格划分的PDBbind-CleanSplit数据集上重新评估其真实性能。然而，复现实验面临巨大挑战：多数模型的代码未公开、仅提供推理版本或依赖私有数据集，导致难以完整重训。最终，研究者仅成功复现了两种代表性模型——经典的Pafnucy和较新的GenScore。  
 结果显示，经过重新训练的Pafnucy在传统基准CASF2016上表现出色（RMSE达到1.046），几乎刷新了公开模型的最佳纪录。然而，当训练集切换为经过数据泄漏清除的PDBbind-CleanSplit后，Pafnucy的性能骤降，几乎跌至简单搜索算法的水平；相比之下，GenScore的表现相对稳定，仅出现轻微下降。这一显著对比验证了研究者的核心假设——许多深度学习评分函数在以往基准中取得的“高分”，实际上源于训练与测试数据之间的泄漏，而非模型真正具备的泛化能力。  
 在经过数据泄漏清理的PDBbind-CleanSplit数据集上训练后，GEMS依然在CASF2016基准上取得了优异成绩（RMSE=1.308，Pearson R=0.803），不仅明显优于同条件下重新训练的PafnucyRMSE=1.484）和GenScore（RMSE=1.362），还达到了当前深度学习评分函数的领先水平。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr73M7foboQqf29hjnaI0iaVlo4ZDjyjoCmHVRjofpJhtibt9Vp0nO9UPAww/640.png)

### 消融实验

 研究者设计了一个关键的消融实验，以验证GEMS模型的预测结果是否真正依赖于蛋白–配体相互作用信息，而非仅凭配体结构进行记忆式的预测，该实验的结果展示于下图a。  
 在这一实验中，研究者将原有的蛋白–配体相互作用图进行修改，去掉了所有蛋白节点，仅保留配体分子图结构，从而得到仅输入配体版本的数据集。随后，他们在两种不同的数据条件下训练GEMS：原始PDBbind数据集与经过数据泄漏清理的PDBbind-CleanSplit数据集。通过比较模型在CASF2016基准测试集上的性能变化，研究者能够判断模型是否真正学会了蛋白–配体间的结合机制。  
 实验结果如图所示：当GEMS在原始PDBbind上训练时，即使完全移除蛋白信息，模型的性能几乎不受影响（RMSE≈1.42），仍可接近甚至超过部分已发表的深度学习打分函数。这说明在存在数据泄漏的情况下，模型主要依赖于配体特征和结构相似性即可获得高精度预测，并未真正理解蛋白–配体结合的物理规律。  
 然而，当训练数据换为去除结构重叠和冗余的PDBbind-CleanSplit后，去掉蛋白信息会导致性能显著下降（RMSE≈1.57），模型预测能力明显减弱。这一差异表明，在无泄漏的干净数据环境下，模型必须利用蛋白–配体交互信息才能获得准确结果。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr73aFgrm3aULAD3icghicicyKb1xMuye7svV5hNKJvmkuBkXWdIUsglnE1PQ/640.png)

### 训练集冗余消除效应

 作者进一步评估了训练集内部冗余样本对模型性能与泛化能力的影响。他们注意到，原始PDBbind数据集中存在大量高度相似的复合物结构，这些样本往往仅在微小的配体修饰或蛋白口袋取向上有所不同。如果这些近乎重复的复合物同时出现在训练集与验证集中，模型就可能通过“记忆”相似结构来获得虚高的预测精度，从而掩盖其泛化性能的不足。  
 为此，研究者在构建PDBbind-CleanSplit的过程中，专门增加了训练集冗余清除步骤。他们通过多重相似性标准（蛋白结构相似度TM-score>0.8、配体化学相似度与构象相似度综合分数>1.3、亲和力差异ΔpK<0.5）识别出高度重复的样本对，并从这些相似聚类中仅保留一个代表复合物。最终，大约有1,400余个冗余样本被移除，使得训练数据更加多样化且不再存在过度重叠。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr73IQ2z03fH20s6GKETFWvhhfZ2zl8l4trJ6QwTKond2xne05icqs1dcsA/640.png) 如图c所示，模型在三种不同版本的数据集上表现出明显的趋势差异：在原始PDBbind上，交叉验证得分较高，但在独立测试集上泛化能力较弱；而在去除冗余后的CleanSplit数据集上，虽然验证集性能略有下降，但测试集RMSE明显改善，预测结果更加稳定。这说明冗余样本的存在会导致模型“过拟合”于特定结构模式，而去除冗余则迫使模型学习更普适的结合规律。  
 总体而言，图c的结果揭示了一个关键结论：适度减少数据量、提高数据独立性，反而有助于提升模型的真实泛化能力。

### 语言模型嵌入的影响

 研究者还系统探讨了语言模型嵌入对GEMS泛化能力的影响。GEMS模型中引入了三种不同来源的语言模型嵌入：用于配体SMILES表征的ChemBERTa，以及用于蛋白质序列的ESM2与Ankh。这些预训练模型能够为节点提供高层次的化学与生物语义特征，使得GEMS在蛋白–配体图表示中不仅包含结构几何信息，还融入了序列与分子语言的上下文关联。  
 如图d所示，当模型在未经清理的PDBbind数据集上训练时，加入语言模型嵌入并未提升性能，甚至在测试集上略有下降。模型在这种情况下依然可以通过数据泄漏带来的结构相似性“取巧”，无需依赖语言语义信息即可获得较高分数。相比之下，图e展示了在经过数据去冗余与泄漏过滤的PDBbind-CleanSplit上的结果：随着ChemBERTa、ESM2、Ankh等嵌入特征的逐步引入，模型的交叉验证表现与在CASF2016测试集上的RMSE均明显改善，说明这些语义特征在干净数据环境下能真正提升模型的泛化能力。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/DJLt0aztibk7eazyqjb8FY3vI3nq2Mr73TAJohIMjzsTvgID6MF3uAbNWGycmxYo4dDFWsfBtEIZiajicyTB6koEQ/640.png)

## 总结

 在本研究中，作者首先提出了一种新的基于结构的过滤算法，用以解决PDBbind训练集与CASF基准之间严重的数据泄漏问题。基于该算法，作者构建了新的训练数据集PDBbind CleanSplit，并证实了现有顶尖模型在CleanSplit上训练后性能会显著下降，表明其原有效能很大程度上依赖于数据泄漏。随后，作者提出了一个名为GEMS的新型图神经网络模型，该模型结合了GNN架构与大型语言模型的迁移学习。GEMS在PDBbind CleanSplit上训练后，依然在CASF基准上实现了最先进的预测。

## 论文和代码

原文：https://www.nature.com/articles/s42256-025-01124-5  
代码：https://github.com/camlab-ethz/GEMS

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6dUWHl3lx0MAnJTiaMxjqblqkRp9IueKaicef4oDic5dNk9DzjJDkHaO5TKKibadTDEpYr1yku5wqMKCx1bEc35sg/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/DJLt0aztibk53icvxoXNOYj0qLymWr70qvbiaTcricQxdNr0wia04SiaMnc5xicsQ4ZsLMVC6Oiap1NRR9RPWEU7Gwffhg/640.jpg)

扫描二维码获取

更多精彩

AI in Graph

本公众号主要介绍应用于图、知识图谱的人工智能算法和研究进展，及其在生物信息、医学健康领域的应用。欢迎关注本公众号获取领域最新文献解读。
  
  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DJLt0aztibk7pSXD3DuyVSpMbm6p5lTbic9xQMChc2VFTOBSXWicVAJRGCcD0puhDicv2zUsVT3l9k254ZyOCJW3rg/0.png) 

 AI in Graph 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DJLt0aztibk7pSXD3DuyVSpMbm6p5lTbic9xQMChc2VFTOBSXWicVAJRGCcD0puhDicv2zUsVT3l9k254ZyOCJW3rg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
