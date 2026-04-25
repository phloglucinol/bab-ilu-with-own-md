---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzYzOTA3NjkxMg%3D%3D&mid=2247582478&idx=1&sn=f53dcd8821b3b8c23f61d038146ff066
canonical_url: https://mp.weixin.qq.com/s?__biz=MzYzOTA3NjkxMg%3D%3D&mid=2247582478&idx=1&sn=f53dcd8821b3b8c23f61d038146ff066
source_domain: mp.weixin.qq.com
title: Nat Catal｜上海交通大学郑双佳等：用多模态大模型EnzymeCAGE精准预测酶催化
author: 
published_at: 
fetched_at: 2026-04-25T02:03:36Z
extractor: wechat_worker
content_hash: c1877f5f803daebed6e91855d24a46f17c389735488c464f836e7b625fc691e3
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/2r1FIaqNHdW5auLenQABicQtoExECpnK3v4Kq8icxYUMia20BiaFuDWAKiaatB9VibmOtmjIXsMeTSA87Mbhb3x6cib4BjVDAo1icR0r0IiaEB6sZWX0/0.jpg) 

# Nat Catal｜上海交通大学郑双佳等：用多模态大模型EnzymeCAGE精准预测酶催化

[ 智药邦 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

2026年2月12日，来自上海交通大学郑双佳团队联合香港科技大学、麻省理工学院、中山大学等国内外多家研究机构学者在Nature Catalysis上发表题为A geometric foundation model for enzymeretrieval with evolutionary insights的研究。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2r1FIaqNHdW7BnTRREGoic6M2frlAvLv3Nw9h5HCicjlhMNibY0SfswcTK7QAnkZ23iaL8rsSdHMO9riaatIWXwTb4kvqqLwbNhV0EH2IcXINom4/640.png)

该研究介绍了一种名为EnzymeCAGE的新型催化特异性几何基础模型，它通过整合酶的三维几何结构、进化信息与化学反应特征，实现了对酶功能的高精度预测和未知反应（孤儿反应）的酶催化剂检索，在多个基准测试和实际生物合成路径案例中展现了卓越性能。

**背景**

酶是生命体代谢和现代生物制造的核心催化剂。然而，准确预测酶的功能，即将特定的酶与其催化的化学反应精确关联，一直是生物信息学和合成生物学领域的重大挑战。现有的数据库存在巨大的知识缺口：在UniProt收录的约2.5亿条蛋白质序列中，仅有不到0.3%经过人工审编；而在KEGG、MetaCyc等主要代谢数据库中，高达40-50%的已知酶促反应缺乏对应的酶序列，这些反应被称为“孤儿反应”。传统预测方法主要依赖于序列同源性分析（如BLASTp）或将酶映射到酶学委员会（EC）编号系统。然而，序列相似性低并不总意味着功能不同，而一个EC编号下可能涵盖多个具体反应，且许多非典型反应难以被现有分类系统所容纳。这些局限性严重制约了我们对代谢网络的理解以及新型生物催化剂的发现与设计。

为了突破这些瓶颈，研究团队提出了一个全新的思路：绕过传统的序列比对或EC分类，直接建模酶的三维催化口袋与化学反应中心之间的几何兼容性与相互作用。他们认为，酶的功能本质上由其活性位点的三维结构及其与底物过渡态的互补性所决定。因此，EnzymeCAGE的核心创新在于构建了一个“几何感知”的基础模型，它能够直接评估一个给定的酶结构是否可能催化一个特定的化学反应，从而实现了更精准、更可解释且不依赖于序列相似性的酶功能预测与检索。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdVrA6sNk5ducebJ3h43ic8ZwiagqukbaiaDVyE2a0AKmXDlCBm51nHnCWwtgZ14p9o0kCN05cibwuyUJpHIZVvT2skPsB40aibQQJSw/640.png)

图1 EnzymeCAGE概览

**从结构出发：EnzymeCAGE的创新研究思路**

面对酶与反应关联预测的复杂性问题，作者没有选择在传统的序列或EC编号路径上继续优化，而是转向了更本质的物理化学原理——酶的结构与功能关系。他们的核心假设是：酶的催化特异性主要蕴含在其活性口袋的三维几何形状、化学微环境以及其与反应过渡态的相互作用中。基于此，他们设计了一个端到端的深度学习框架EnzymeCAGE，其输入是酶的结构（实验测定或AlphaFold预测）和化学反应的SMILES表示，输出是一个介于0到1之间的催化兼容性分数。

这一思路的关键突破在于其“几何增强”与“进化信息整合”的双轨策略。首先，模型并非处理整个酶分子，而是利用AlphaFill工具智能提取出潜在的催化口袋，将注意力集中在功能相关的局部区域，这大大减少了无关结构的噪声干扰。其次，模型不仅编码口袋的几何特征（如原子坐标、二面角），还通过强大的蛋白质语言模型ESM-C（Evolutionary Scale Model Cambrian）嵌入全局的进化信息，从而在保留精细空间细节的同时，融入了从亿万序列中学习到的进化约束与功能暗示。对于化学反应，模型则着重识别并加权处理发生键合、电荷或手性变化的“反应中心”原子，强调其对催化过程的关键性。最终，通过一个几何增强的交互模块，显式地计算催化口袋残基与反应分子之间的三维相互作用特征。这种将局部几何结构、全局进化语境和反应中心化学变化紧密结合的建模方式，使EnzymeCAGE能够从原理上学习酶与反应之间的适配规则，而非仅仅依赖历史数据的模式匹配。

**整合几何与进化的模型架构及其卓越性能**

EnzymeCAGE的成功得益于其精心设计的模型架构、大规模高质量数据集的构建以及系统严格的评估。整体而言，作者采用了一种多模态的几何深度学习框架，分别对酶口袋和化学反应进行编码，并通过一个几何引导的交互模块评估其兼容性。训练数据来源于Rhea数据库，涵盖了超过150万个经过筛选的酶-反应对，涉及3000多个物种，构建了一个广泛而坚实的知识基础。模型的评估则分为内部测试（针对训练中未见的酶或反应）和外部测试（针对特定酶家族），并采用了Top-k成功率（SR）、富集因子（EF）和折损累计增益（DCG）等多个指标进行全面衡量。

  
**1\. 精准预测未知酶的功能**

  
为了评估模型对全新酶的功能注释能力，团队构建了Enzyme-405测试集，包含405个在训练数据中未出现过的酶及其对应的295个反应。EnzymeCAGE需要从大量候选酶中识别出正确的催化者。结果显示，EnzymeCAGE在Top-10成功率上达到了58%，显著优于MMseqs2、ESP、CLIPZyme、CLEAN和GraphEC等现有先进方法。这意味着对于超过一半的测试反应，模型都能在前10个推荐酶中找到真正的催化剂。更值得注意的是，即使对于与训练集序列相似性极低（例如低于0.3）的酶，EnzymeCAGE也能成功将其排名第一。这证明了模型摆脱了对序列同源性的依赖，能够基于结构和几何原理进行功能推断，具备了强大的外推能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2r1FIaqNHdVIjAskF5S9WQyuhkduU7rkUvdbRdu9VvwS8Krw8wPOmro3Mn6uCictqkGAY1V4ia2v9Gn78OvoWkraKtPzOPpkvRlFpYoV253DM/640.png)

图2 EnzymeCAGE在测试集Enzyme-405上的表现

  
**2\. 高效检索孤儿反应的催化酶**

  
“反应去孤儿化”是另一个关键挑战，即为一个已知化学反应找到其对应的酶催化剂。研究团队构建了Orphan-335测试集，包含335个在训练时尚未被注释酶的反应（即当时的孤儿反应）。EnzymeCAGE的任务是从一个大型酶数据库中检索出可能催化这些反应的酶。评估表明，EnzymeCAGE在此任务上也大幅领先于Selenzyme、ESP和CLIPZyme等检索工具。例如，在Top-3成功率上，EnzymeCAGE比最佳基线模型提高了超过40%。模型甚至能对与训练集反应相似度很低（<0.7）的孤儿反应做出正确预测，展示了其对新颖生物化学的强大泛化能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdUc5qszxkEd9iaGpexicKA8he6S5I8zA4Q8iaz6OxibTAvZ3h6cQYJq3S7z2IgxiaHQGFITIUweUSicg54WExPbyMBlSJrJp9zMg1o0A/640.png)

图3 EnzymeCAGE在Orphan-335测试集上的表现

  
**3\. 领域微调提升家族特异性预测**

  
酶家族内部具有高度的多样性。为了提升对特定酶家族的预测精度，EnzymeCAGE支持快速的领域特异性微调。研究团队在细胞色素P450、萜烯合酶和磷酸酶这三个重要家族上进行了测试。经过在家族数据上的微调后，EnzymeCAGE的预测准确性得到了进一步提升。例如，在P450家族上，微调后的模型Top-5成功率从约75%提升至超过85%。这表明EnzymeCAGE的通用基础架构能够有效吸收特定领域的知识，从而提供更专业、更可靠的预测。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2r1FIaqNHdWbzGHE0wEYm6ic0423ekMepoVWeCakiaehdtsWBNAjkpTV5Frm9S9W1eiabOgJs6ynTqkCxfMUBy1GPLicGedrCIgMTV1IR2dVJlo/640.png)

图4 EnzymeCAGE在外部测试集上的表现

  
**4\. 在真实生物合成路径中的应用验证**

  
为了证明其实际应用价值，研究团队将EnzymeCAGE应用于两个真实的复杂生物合成路径：醉茄内酯（withanolide）生物合成和戊二酸生物合成路径。在醉茄内酯路径中，涉及三个由细胞色素P450催化的羟基化反应。EnzymeCAGE在107个候选P450酶中，成功地将三个正解酶CYP87G1、CYP88C7和CYP749B2分别排名第13、第10和第6位，而所有基线模型均将它们排在20名开外。这些正解酶与训练集的最高序列相似性仅为\~0.4，再次凸显了模型的结构泛化能力。

在包含六个步骤的戊二酸生物合成路径重建案例中，EnzymeCAGE成功地为每一步反应检索到了正确的酶，且排名均在前20之内，对于中间步骤（第2-4步）的酶更是排名前三。这一案例生动展示了EnzymeCAGE在从头设计或重构复杂代谢路径方面的强大潜力，能够高效地从海量酶资源中筛选出合适的催化元件。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdW3sGsxfmgHfrHuic1cH0cmA8xkkpjKphEuGgzVX3kYToAibM8ibgq8niaEoW3HSgvv8s8kF26j4xiaicIs0iaic3LBX3Pibwx5fib1iax5xM/640.png)

图5 醉茄内酯生物合成关键反应的酶功能预测

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdV7txxxYgGJBbmUtMPyRuOtWefaJbpibYkfzIDgDbhnAfEpxWJrTLJjPWIsibfZZ2ChQQG3kWOfdIjzCCFYWud4cgwEYh28pppFs/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2r1FIaqNHdV87QmeGzXaSdlVUxxpZ1GDMP2dumvKlWQqsNMEngiabLXor4eXJgf26GJHwBSATRQgm2jdbrd0SIXt3Mwv6u8zpKTnWU401faA/640.png)

图6 b–g，酶检索结果，展示了步骤1-6的阳性酶排名（左）及其三维结构（右）

**总结与展望**

本研究提出的EnzymeCAGE模型，标志着酶功能预测领域向基于结构与物理原理的“几何基础模型”迈出了关键一步。它通过整合催化口袋的几何特征、进化尺度模型提供的序列语义以及化学反应的动态中心信息，建立了一个强大且可解释的酶-反应关联预测平台。其最突出的优势在于能够突破序列相似性的限制，直接评估结构-功能的兼容性，从而在预测未知酶功能、解锁孤儿反应以及辅助设计生物合成路径等方面展现出超越现有方法的性能。

当然，该模型仍有提升空间。作者指出，其性能在某些酶类别（如硫转移酶、酰胺水解酶）上仍有不足，这可能与这些家族的数据稀缺或结构功能多样性更高有关。此外，反应数据的质量（如原子-原子映射的准确性）和负样本的构建策略也是未来可以优化的方向。

展望未来，EnzymeCAGE为代表的结构感知AI模型，将不仅加速新酶的发现与功能注释，更将深化我们对酶催化这一生命核心过程的理解。它有望与自动化实验平台结合，形成“AI设计-实验验证”的闭环，极大地推动合成生物学、代谢工程和绿色生物制造的发展。下一步的研究可能会聚焦于扩展模型对更复杂酶促反应（如多底物、辅因子依赖）的处理能力，以及将其应用于酶工程的理性设计，直接预测或生成具有特定催化性能的酶变体。

参考资料：

Liu, Y., Hua, C., Xu, M. et al. A geometric foundation model for enzyme retrieval with evolutionary insights. Nat Catal (2026).

https://doi.org/10.1038/s41929-026-01478-y

\--------- End ---------

感兴趣的读者，可以添加小邦微信加入**读者实名讨论微信群**。添加时请主动注明**姓名-企业-职位/岗位**或**姓名-学校-职务/研究方向**。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/2r1FIaqNHdWMb1tkRfNxLniaVcmMJXiaG3X2GLVWIGB2bTicLFLDKqSia9qMmw1qhLNZ3rPdZxgrKWsnuSyvNsPPxlZ6ueuftbrE2emvhibAu2Aw/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdVMwEetx49J87Rqn1GnFrIXPkY5s7YicLdnKUYsMRXsgfBiacwkUUicAPuZYrqh2iaias3CyxghoKzyMz82nXCO3R2S7180x4wvm7Rw/640.png)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ialRowSiaYaicLpRDGcNCxDe2JW42DIHlYGhp0NmIhickwQUicNf81fmgO3icOeSxoeYoCAibbXzq1AxTrfEnU7yCz7Rw/0.png) 

 智药邦 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ialRowSiaYaicLpRDGcNCxDe2JW42DIHlYGhp0NmIhickwQUicNf81fmgO3icOeSxoeYoCAibbXzq1AxTrfEnU7yCz7Rw/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
