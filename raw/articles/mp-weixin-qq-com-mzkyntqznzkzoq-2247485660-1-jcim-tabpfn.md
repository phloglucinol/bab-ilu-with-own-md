---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkyNTQzNzkzOQ%3D%3D&mid=2247485660&idx=1&sn=99c5c733ce117003966b7196c29ed3db
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkyNTQzNzkzOQ%3D%3D&mid=2247485660&idx=1&sn=99c5c733ce117003966b7196c29ed3db
source_domain: mp.weixin.qq.com
title: JCIM封面论文｜TabPFN：破解小数据困境，开启药物发现新范式
author: 
published_at: 
fetched_at: 2026-04-24T16:09:47Z
extractor: wechat_worker
content_hash: ca570333c5389f805a8acbb784e79e300e73d55cd64de5148099c8c84baecc68
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/wHzFZQibtWCeaHIIkE3sibErNgEfNcvQA82wtX9TW74zr61wM97L0nMnsIvB1icyl47fxKK4qpGlODywWicMdLfwKPYf3mJTGAib1RibaRsIPYx98/0.jpg) 

# JCIM封面论文｜TabPFN：破解小数据困境，开启药物发现新范式

原创 XYDrugs XYDrugs [ XYDrugs ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/wHzFZQibtWCfYkz6yib1NBFIr4ibOKrNvicpqzbAu8STmEojcWticvwpq60zSicbLlPteQ56qJ2xqcQu5iagO434qYqMrhbicMox6NgPCphXdTmlTic4/640.jpg)

![研究摘要图](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/wHzFZQibtWCcL3CzeEM5L8VxG8NmdaUXnv8hKGVkJ0JAFtsdn3wDSM1FDtRS0pw1I6znBEq6ib1d5GJV9YIibBg1a81JGibGJPNqG9FhQMSOAmc/640.png)

研究摘要图

在药物发现领域，真正棘手的问题往往不是“模型不够复杂”，而是“数据太少、分布太难”。近期，中南大学湘雅药学院曹东升教授、蒋德军副教授团队的研究成果发表于 Journal of Chemical Information and Modeling（JCIM），并入选期刊封面论文。该工作系统展示了 TabPFN 在小样本药物表格数据建模中的潜力，为药物发现中的 AI 建模提供了一种有别于传统机器学习和常规深度学习的新范式。

## unsetunset一、 研究背景unsetunset

在药物研发的早期阶段，研究者往往面临一个长期存在却难以彻底解决的问题：**数据太少，但问题却很复杂**。

不同于互联网或推荐系统中动辄百万级的数据规模，药物发现中的实验数据往往只有几百甚至更少。与此同时，这些数据还存在明显的分布差异，例如新设计的分子结构往往与历史数据存在较大偏离。在这种“小数据 + 分布偏移”的双重挑战下，现有机器学习模型的可靠性和泛化能力受到严重限制。

传统方法如支持向量机、随机森林和梯度提升树（XGBoost）在过去十余年中一直是QSAR/QSPR建模的主流工具。然而，这类方法高度依赖特征工程，在样本有限或类别分布不均衡时性能显著下降。而近年来兴起的深度学习模型，尽管在表示学习方面具有优势，却通常依赖大规模数据，难以在真实药物研发场景中稳定发挥作用。

## unsetunset二、新范式：TabPFN 的核心思想unsetunset

在这一背景下，中南大学湘雅药学院曹东升教授、蒋德军副教授团队开展了一项系统性研究，探索一种全新的建模范式——**TabPFN（Tabular Prior-Fitted Network）** 在药物发现中的应用潜力。相关成果已发表于国际权威期刊 \_Journal of Chemical Information and Modeling\_。

TabPFN的核心思想与传统模型截然不同。它并不是针对具体任务进行训练，而是通过在海量合成任务上进行预训练，学习到一个通用的“先验分布”。在实际应用中，模型无需重新训练，也不需要复杂的超参数调优，而是通过类似“上下文学习”的方式，直接对新数据进行预测。这种“training-free”的特性，使其在数据稀缺场景中展现出独特优势。

## unsetunset三、整体性能：在小数据任务中的显著优势unsetunset

在本研究中，团队系统评估了TabPFN在多种药物相关任务中的表现，包括25个ADMET分类数据集、10个回归任务，以及MoleculeNet和量子化学数据集。结果表明，在回归任务中，TabPFN表现出显著优势。相较于XGBoost，其R²平均提升约3.30%，同时RMSE显著降低，表现出更高的稳定性和预测精度。尤其是在样本量较小的数据集上，这种优势更加明显。

在分类任务中，TabPFN同样展现出良好的性能。在样本量小于4000的数据集上，其性能普遍优于传统方法；而在更大规模数据集上，则与XGBoost表现相当。这一结果揭示出TabPFN的一个重要特点：**其优势主要集中在小样本和中等规模数据场景**，这恰恰与实际药物研发的需求高度契合。

![图1: TabPFN在回归任务中整体优于传统方法，在小规模分类任务中表现更优](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/wHzFZQibtWCfWkoHuf7kAqjmEkTK6fPibKtB5IKxVyxt3jniaWr22a6bF9Ne7wV3z3icmU8y6dfJhN9kyqIa0XzxKHkuYbdVw9qVWgI53ib6sVZo/640.png)

图1: TabPFN在回归任务中整体优于传统方法，在小规模分类任务中表现更优

## unsetunset四、表示鲁棒性：对特征工程不敏感unsetunset

除了整体性能评估，研究还进一步分析了模型对不同分子表征方式的敏感性。传统模型通常对特征设计高度依赖，而实验结果显示，TabPFN在使用不同特征组合（如仅RDKit描述符或加入MACCS指纹）时，性能变化极小。这说明其具备较强的表示鲁棒性，可以在较少特征工程的情况下稳定工作，从而降低实际应用门槛。

![图2: TabPFN在不同分子特征表示下性能稳定，明显优于对特征敏感的传统模型](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/wHzFZQibtWCeH3lhhNaE8W1sSpibrvbIojXsBIWoPKGmjgrHDp6VXnZbSKjfYJ1iaEe9QqU8XSB50UsoqHOJPWx6n71prwnFjoxJ6VunrIEZxU/640.png)

图2: TabPFN在不同分子特征表示下性能稳定，明显优于对特征敏感的传统模型

## unsetunset五、OOD泛化能力：更接近真实应用场景unsetunset

更为关键的是，研究采用了更接近真实应用场景的评估方式，即基于分子结构聚类的分布外（OOD）划分。与常规的随机划分不同，这种方法能够更真实地模拟模型在面对“全新化学空间”时的表现。结果表明，尽管所有模型在OOD场景下都会出现性能下降，但TabPFN的下降幅度明显更小，并在多个任务上仍保持领先。这一结果表明，其具备更强的跨分布泛化能力。

![图3: 在OOD划分下，TabPFN性能下降更小，展现更强泛化能力](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/wHzFZQibtWCdcvWibGpcTOHiaJwez81uicRwBX9kt5oa13GmF5y10CdGMPK4sUgoAJN9nVhA8NjKmRDTicyiaHZqcHqiaMibdEhaHDUm7GfXficWqWW8/640.png)

图3: 在OOD划分下，TabPFN性能下降更小，展现更强泛化能力

## unsetunset六、极端测试：特征与数据消融实验unsetunset

为了进一步检验模型的稳定性，研究还设计了极端条件下的消融实验，包括特征删除和数据删除两种设置。在特征最多删除90%、训练数据减少90%的情况下，TabPFN依然能够保持相对稳定的性能，而传统模型则普遍出现明显退化。这一结果从另一个角度印证了TabPFN在数据稀缺环境中的优势。

![图 4: 在特征大量缺失情况下，TabPFN依然保持稳定性能](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/wHzFZQibtWCe6ia1tp3GzhLFiaBPciartIvhHIj1lEQTwicibUUduTR5KET8DHCyBNZjUB9yDYRPS7QPicxKZFe4RdibGX6mr0C1AS65UkvswGDT5EQ/640.jpg)

图 4: 在特征大量缺失情况下，TabPFN依然保持稳定性能

![图 5: 在训练数据大幅减少时，TabPFN依然优于传统方法](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/wHzFZQibtWCcScgVFpPe6BibOhvVU4ffp1ZIvibxFibw1EPK6icLEHLOCicBeZBu20YT1Mroj9lapMXy6s7clGQqbSnaVPqaXSxn7fjsnjJN8FnK0/640.jpg)

图 5: 在训练数据大幅减少时，TabPFN依然优于传统方法

## unsetunset七、模型理解：学习到更合理的结构表示unsetunset

除了预测性能，研究还对模型的内部表示进行了分析。通过对嵌入空间的可视化，研究发现TabPFN能够学习到更加平滑且具有连续结构的表示。在回归任务中，分子在嵌入空间中呈现出清晰的性质梯度；在分类任务中，不同类别之间的边界更加清晰。这表明模型不仅是在拟合数据，更是在捕捉潜在的结构–性质关系。

![图 6: TabPFN嵌入空间呈现更平滑的性质分布与更清晰的结构关系](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/wHzFZQibtWCficjLRGGtqiapy98Pbjocwf1jAPK0bSk5AbfdwsxFnfRG6Qoj5cKESzRlDSwxhDSefKqtKyMYAoggN6rzT9Cq19IyPk4MSgkhdA/640.jpg)

图 6: TabPFN嵌入空间呈现更平滑的性质分布与更清晰的结构关系

## unsetunset八、适用边界：不是所有场景都最优unsetunset

当然，研究也指出了TabPFN的适用边界。在数据规模较大（超过8000样本）或类别极度不平衡的情况下，XGBoost等传统方法仍具有一定优势。因此，在实际应用中，模型选择应根据具体数据特征进行权衡，而非简单追求单一方法。

## unsetunset九、总结：从方法到范式的转变unsetunset

总体而言，本研究表明，TabPFN为药物发现中的表格数据建模提供了一种全新的解决思路。其无需训练、对特征不敏感、在小数据和分布偏移场景下表现优异等特点，使其成为传统方法的重要补充。

从更宏观的角度来看，这项工作也反映出一个重要趋势：**基础模型（foundation model）正在从自然语言和图像领域，逐步扩展到表格数据这一长期被忽视但极其重要的方向**。对于药物研发而言，这意味着未来的建模方式可能不再依赖大量数据和复杂调参，而是更多依赖预训练知识和泛化能力。

在数据始终有限、问题却不断复杂的药物发现领域，这种范式转变，或许正是突破瓶颈的关键所在。

文章链接：https://pubs.acs.org/doi/abs/10.1021/acs.jcim.5c02823
  
  
投稿人 | 陈沃若、田 垚

责 编 | 许燕红 

 审 核 | 蒋德军 

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/CVXhibsq4e1njW71iavg4XIQibawF0iazVtC9ZSGeibXibTxY3gVNrkzrkc0raRhLRzLgOBlfRw1dzYlUTkOYaA2kLoQ/0.png) 

 XYDrugs 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/CVXhibsq4e1njW71iavg4XIQibawF0iazVtC9ZSGeibXibTxY3gVNrkzrkc0raRhLRzLgOBlfRw1dzYlUTkOYaA2kLoQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
