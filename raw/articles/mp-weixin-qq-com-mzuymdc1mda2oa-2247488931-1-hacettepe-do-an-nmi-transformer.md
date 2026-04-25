---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247488931&idx=1&sn=37b838a121a95c08c2cceb4eb36821c2
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247488931&idx=1&sn=37b838a121a95c08c2cceb4eb36821c2
source_domain: mp.weixin.qq.com
title: 【佳作推荐】 土耳其Hacettepe大学Doğan团队NMI论文：基于图Transformer的分子生成模型实现靶向分子设计
author: 
published_at: 
fetched_at: 2026-04-25T02:04:27Z
extractor: wechat_worker
content_hash: 797695f81dcef00436e9d69c610bb353e86a8b42d8bd38339f98e2aed20fac32
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EfNDx73XHqXvo0guhiat1lQXWoxAF7iciaLrfdiaLmSLIj5B53GpCvTeHtyiclxxZR9YUjsEPI4Eu2bM8w/0.jpg) 

# 【佳作推荐】 土耳其Hacettepe大学Doğan团队NMI论文：基于图Transformer的分子生成模型实现靶向分子设计

原创 ComputArt ComputArt [ ComputArt计算有乐趣 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfNDx73XHqXvo0guhiat1lQXV6gks72icfp6SqUCMlibd7juul0gW7anvqrtHk3ia5I30OQiaJeXPejZSQ/640.png)

药物研发是一项长周期、高投入的系统工程，旨在围绕特定靶点筛选具备生物活性的化合物。尽管高通量筛选技术可同时测试数万个分子，但庞大的化学与靶点空间仍远未被充分探索，最优候选分子的发现依然困难。针对未被覆盖的蛋白家族，需要更具多样性的小分子结构，但现有化合物库难以满足这一需求。此外，许多候选分子在临床阶段因毒性或疗效不足被淘汰，导致药物研发成功率偏低。近年来，人工智能分子生成方法虽能优化分子性质，却缺乏靶点导向的设计能力。因此，发展以靶点为中心的人工智能从头药物设计，被视为突破传统研发瓶颈、实现精准靶向治疗的重要途径。

近日，土耳其Hacettepe大学Tunca Doğan教授团队针对上述问题，开发了一种基于图Transformer的生成对抗网络（GAN）模型DrugGEN，用于从零开始生成特定靶点的候选药物分子。该模型以分子图为输入，结合靶点特异性活性数据进行训练，能够高效学习药物分子的结构分布并生成具有靶向特征的新分子。此外，研究团队以AKT1（与多种癌症密切相关的激酶）为主要研究对象，联合DrugGEN、分子对接、分子动力学模拟等技术，设计并合成了5个候选化合物，其中两种在体外实验中表现出显著的AKT1抑制活性。该项研究近期发表在计算科学领域著名期刊Nature Machine Intelligence上【1】。

1\. 模型架构与训练方法

DrugGEN是一种基于图Transformer的靶点特异性分子生成模型（图1），致力于从头设计可与特定蛋白靶点高效结合的小分子化合物。该模型以二维分子图作为输入，其中节点特征编码原子类型，邻接矩阵则表征化学键的连接关系与类型。在模型架构层面，DrugGEN的核心创新点在于其生成器与判别器模块均采用了图Transformer编码器作为基础构建单元。相较于传统图神经网络局限于局部邻域的信息传递机制，图Transformer凭借其全局注意力机制，实现了在整个分子图范围内对原子间相互作用权重的动态建模，从而精确识别并表征那些跨越多个化学键、对分子构象与性质具有关键影响的远程相互作用。

在训练方法上，作者分别使用了两个数据集分别训练的生成器和判别器。生成器的训练数据来自于ChEMBL29，作者过滤出重原子数小于45的分子共1588865个用作训练数据。判别器的训练数据更为特殊，需要指定靶点的活性化合物数据集，在本研究中，作者选取了AKT1蛋白和CDK2蛋白作为靶标，分别从ChEMBL数据库过滤出了靶向这两种蛋白IC50 < 1 μM且重原子数小于45的化合物（AKT1配体分子共计2607个，CDK2配体分子共计1817个）。生成器在学习完大量化合物结构知识生成一个新的分子之后，判别器会根据活性化合物数据集中的信息判别这个分子是否能够成为活性分子，生成器与判别器在对抗中进行迭代，让模型在生成过程中倾向于产生与目标蛋白作用模式相似的分子。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfNDx73XHqXvo0guhiat1lQXcLgDibvBfLeJEic9Wu7Yx1yicG849py0quRcDoJw64UZTArtBwCLdjicxA/640.png)

**图1：DrugGEN模型架构。**

2\. 模型性能评估

该研究首先在标准评估平台MOSES【2】上对DrugGEN的生成性能进行了综合评估。结果表明，该模型在有效性、新颖性、独特性与内部多样性等关键指标上均取得优异表现。值得注意的是，其非靶向版本DrugGEN-NoTarget在包括REINVENT、MolGPT等在内的12种主流生成模型中脱颖而出，荣获非靶向模型组综合排名第一；而其靶向版本同样在6种靶向设计模型中位居榜首。这一结果表明，DrugGEN不仅能够生成高度多样且符合化学规则的新型分子结构，同时在保持分子质量与创新性方面超越了当前主流方法，为后续靶向药物设计奠定了坚实基础。

在靶向分子设计方面，DrugGEN展现出与真实抑制剂相媲美的优异结合性能（图2）。针对关键抗癌靶点AKT1，模型生成分子的对接结合能中位数达到-8.386 kcal/mol，这一数值达到了真实AKT1抑制剂对接打分的99.98%，显著优于RELATION、TargetDiff等主流靶向生成模型，进一步分析发现，模型成功生成了40个在对接分数上超越已进入临床实验的AKT1抑制剂Capivasertib的候选分子，充分证明了其在发现高亲合性靶向化合物方面的强大能力。在CDK2靶点的测试中，模型同样表现出色，对接得分达-8.747 kcal/mol，相当于真实抑制剂对接打分的86.99%。此外，作者使用QED、SA、Lipinski五规则等测试方法对生成分子进行了评估，发现DrugGEN生成的分子在多项药物属性指标上表现良好，提高了药物设计的成功率。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfNDx73XHqXvo0guhiat1lQX4WAEvwQ6usSs9HwwKibEc2z3rtvRuuds61UV1BfxJIGIRIBYdBGXfgQ/640.png)

**图2：DrugGEN针对AKT1和CDK2蛋白生成分子的对接打分结果及横向对比。**

最后，本研究通过湿实验验证了DrugGEN在真实药物设计场景下的性能。作者从生成的分子中选取五个结构各异的候选化合物进行化学合成（图3a），所有化合物纯度均达到95%以上。体外酶活性实验结果显示，其中两个化合物对靶点AKT1表现出显著抑制活性：分子MOL\_02\_045762的IC50值达到1.89 μM，展现强效抑制能力；分子MOL\_02\_045795也表现出48.6 μM的明确活性。为深入理解结合机制，研究团队进一步进行了分子动力学模拟，发现活性分子与AKT1活性位点形成了稳定的相互作用网络，其结合模式与已知抑制剂相当（图3b）。这一系列实验不仅证实了DrugGEN模型在真实药物设计场景下的性能，更首次实现了基于图Transformer的生成模型从虚拟设计到实验验证的全流程贯通，为AI驱动的药物发现提供了坚实的实例支撑。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfNDx73XHqXvo0guhiat1lQXDiaoTd7PTyZic9RKpvKljd6sNuLjK2QGnaRcGod7pGltc4JibQ8QXv2uw/640.png)

图3：（a）湿实验环节中DrugGEN生成的候选分子，（b）分子动力学模拟预测出的各候选分子与靶蛋白的结合模式。

**小编总结**

本研究提出了基于图Transformer的分子生成模型DrugGEN，通过在对抗生成网络架构中引入多头注意力层，使模型可以识别分子图中距离较远原子之间的相互作用，实现了对特定蛋白靶点的高亲合性、高类药性分子的定向设计，并且通过湿实验验证了模型的性能。然而需要指出的是，虽然图Transformer在分子生成模型中较为新颖，但该架构在性质预测领域早已得到广泛应用，因此模型在架构层面的创新性相对有限。此外，由于该模型依赖对抗训练框架，其判别器需要特定靶点的已知活性化合物数据进行训练，导致模型在面对不同靶点时需要重新训练，在实际应用中灵活性和便利性受到一定限制。

**参考文献**

\[1\] Ünlü, A., Çevrim, E., Yiğit, M.G. et al. Target-specific de novo design of drug candidate molecules with graph-transformer-based generative adversarial networks. Nat Mach Intell 7, 1524–1540 (2025). https://doi.org/10.1038/s42256-025-01082-y.

\[2\] Polykovskiy, D. et al. Molecular Sets (MOSES): a benchmarking platform for molecular generation models. Front. Pharmacol. 11, 565644 (2020).

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IBYsyRibb4EcibThuywhbNciciaiauxu6DUhtp75nQZnrPxniaYia0RMN9XgXMVCiaqEOxkU4EjMoIsmD98kDTcLz5NC3w/0.png) 

 ComputArt计算有乐趣 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IBYsyRibb4EcibThuywhbNciciaiauxu6DUhtp75nQZnrPxniaYia0RMN9XgXMVCiaqEOxkU4EjMoIsmD98kDTcLz5NC3w/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
