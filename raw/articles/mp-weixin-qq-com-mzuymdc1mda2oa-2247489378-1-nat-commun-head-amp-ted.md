---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489378&idx=1&sn=94b53b472b3ddb7f8a15ddecf45500ad
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489378&idx=1&sn=94b53b472b3ddb7f8a15ddecf45500ad
source_domain: mp.weixin.qq.com
title: 【佳作推荐】望石智慧团队Nat. Commun.论文：基于能量的分子生成构象评估新框架HEAD&amp;TED
author: 
published_at: 
fetched_at: 2026-04-25T02:03:08Z
extractor: wechat_worker
content_hash: 952abfa0f0329ebf6625ca39239d74d3c26ef01bf5ea7f3e56e21a40d4dc33c5
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/upT6VMW9MvRbQTQv8RGtSgz68qH8be1Adj10kosJzhiaYGQMhJu7JnBLYZyFABRh3ib24fHFLfteuHjpNMV7pLAhPjTsYgLozjBUxhPg13dsY/0.jpg) 

# 【佳作推荐】望石智慧团队Nat. Commun.论文：基于能量的分子生成构象评估新框架HEAD&TED

原创 ComputArt ComputArt [ ComputArt计算有乐趣 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/upT6VMW9MvRXHA8upKJOD0HF7UhNbKJDQplanKeR3gcDbVicH9R2g044sX51JAdWjnTlF7ibDPyswNjHNseUdk8zexehcMnUicVk3z9OicSIg7U/640.png)

在药物设计研发中，理想的分子生成模型应能感知蛋白结合口袋的约束，从而为后续筛选优化提供新颖且多样的起始化学空间。近年来，自回归和扩散模型逐步具备了三维分子构象生成的能力，但普遍存在着生成异常构象的问题，如空间冲突、结构扭曲等，不论从指导模型改进还是生成分子的实际应用角度都需要对其进行有效评估。然而，现有的两类主流评估方法中，基于几何的构象评估因缺乏能量指标或参考数据集偏差影响，可能引起误判；而基于能量的评估方法则往往受困于精度与计算效率之间的矛盾，更缺乏细粒度的信息反馈。此外，对于是否应在评估前进行分子力场优化，领域内也尚无统一共识。

面对这一现状，望石智慧团队发展了一套基于能量的分阶段评估框架：在力场优化前，通过高能原子检测器（HEAD）模型评估分子构象的有效性（validity），再利用基于深度学习的扭转能描述符（TED）评估力场优化后的构象合理性。该方法旨在弥补现有评估策略的不足，来系统性评估模型生成的分子构象。相关研究近期发表在Nature Communications期刊上【1】。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/upT6VMW9MvTlO3MEdwib9T339Dnw34OneTibpWw6pNPU3RARp8PZP5x5RvHMLcficJN7G3jvgMvBfico8kkUibMFWbVLYZccOP4HWUB0cC89OTM0/640.png)

图1：三维构象评估体系HEAD&TED示意。

首先，作者构建了HEAD模型，用于直接评估AI生成的分子三维构象。该模型基于机器学习力场（如ANI-2x）计算原子能量，通过在QM9等若干经典数据集上计算出每种元素的原子能量分布以获得相应的能量阈值Ec，用于识别高能异常原子（图1左）。若构象中存在任意高能原子，则被判定为无效构象。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/upT6VMW9MvTlhmFpIic1wGc7jTwKlak2o2yK0T7ZVPIPmVMSU5FiaFetydrlQrC6q5nVncowQric2nKowpzUyO3nrLbyloF4PJdvzGicdnAJyM8/640.png)

图2：HEAD模型构象有效性验证结果与案例分析。

围绕HEAD模型，作者从构象有效性和配体-蛋白相互作用评价两个方面进行了验证。在构象有效性测试中，作者选取CSD和LigBoundConf数据集分别作为游离态与结合态配体的有效构象基准，并以基于几何的评估方法PoseBusters作为对照。结果表明，两种方法在两个数据集上都有较高的召回率（＞98%），且不同数据集没有显著差异，说明二者判定标准均不过于严格，有利于避免对后续测试任务的干扰（图2a）。同时，HEAD的计算速度约为PoseBusters的30倍，更适合于高通量的筛选任务。在此基础上，作者评估了HEAD区分有效和无效构象的能力。通过构建GM-5K数据集，将分子构象在MMFF94力场优化前后的能量差ΔE作为质量指标，并在量子力学精度下计算得到了该数据集的ΔE分布。随着选定的阈值在分布内的变化，作者比较了HEAD和PoseBusters判断构象是否有效的加权F1分数变化。结果显示，在ΔE阈值在200\~600 kcal/mol的区间范围内，HEAD对构象有效性的区分能力明显优于PoseBusters，其余区间表现相当（图2b、c）。基于作者的案例分析，这主要由于几何方法难以穷举所有异常类型，而基于能量的HEAD方法则能规避这一问题。在配体-蛋白相互作用评估方面，HEAD主要通过比较结合前后的原子级别能量变化来判断相互作用的有效性，若结合态的高能原子数增加，则此构象的配体-蛋白相互作用视为无效。结果同样表明，HEAD方法在识别结合自由能较高的无效构象方面优于PoseBusters。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/upT6VMW9MvRvL2enX3nR3Ey2SAfF2X10UKiba3QBqiavcOqM5LKQtrvEHXwEfAicGzaLRJNN8l0SvVCdAbOSa7I32HKhd7Wh4z7IkA2Ag7Tay8/640.png)

图3：TED-Model扭转能预测验证结果。

在分阶段评估方案中，TED预测模型用于评估力场优化后的构象合理性。其核心思想是基于每个可旋转键的扭转能预测结果判断：输入构象先被拆分出所有的重原子间可旋转键片段，然后通过基于注意力机制的深度学习模型TED-Model来预测其中可旋转键的扭转能曲线；若构象中任一可旋转键的扭转能超过预定义的阈值2 kcal/mol，则该构象被视为不合理（图1右）。为了验证TED-Model的预测性能，作者在自己构建的DFT-5K数据集上与半经验方法GFN2-xTB进行比较。该数据集包含了5000个独立的可旋转键片段，其每个片段的多个构象扭转能标签经过MD模拟与DFT计算而得。对每一个可旋转键片段，作者分别使用TED-Model与GFN2-xTB计算了其中各个构象的扭转能，得到各自的Pearson相关系数，汇总形成了DFT-5K数据集上的分布。结果表明，TED-Model的预测结果与DFT结果表现出更强的一致性，其平均PCC = 0.84，明显高于GFN2-xTB的0.63（图3）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/upT6VMW9MvSEKbB5WQP3y7tZMge31SjJu4UtCImoYWWicD9UNywfibvQNZ0ofHBxroC6hwblqLecMy1ktJeWtVOTKtUe2Ony3HTAIZlVLnfyQ/640.png)

图4：5个待测分子生成模型在HEAD&TED评估体系中的主要测试结果。

最后，作者将经过充分验证的HEAD&TED评估体系应用于5个代表性AI分子生成模型（自回归模型：Lingo3DMolv2、Pocket2Mol、PocketFlow；扩散模型：PMDM、TargetDiff），在DUD-E数据集的102个靶点上进行测试。对某个靶点，每个模型均尝试生成1000个分子，并在实际评估前先过滤掉类药性（QED）与可合成性（SAS）较差的分子。结果表明，在基于HEAD开展的配体-蛋白相互作用评估和配体构象评估通过率上，仅Lingo3DMolv2都保持了相对较高的通过率（＞70%），而余下模型至多只在单一测试中有着良好的通过率，反映出模型生成的原始构象与力场优化后的构象之间仍存在明显差距（图4左a、b）。在TED测试中，只有PocketFlow较其他模型有着相对优势，通过率超过了50%（图4左c）。总体上看，没有任何单一模型在各项评估维度上能全面胜出。如果汇总整个生成分子构象的筛选流程，在依次经过了类药性与可合成性、口袋冲突、构象有效性和构象合理性过滤的处理后，即使表现最好的Lingo3DMolv2和PocketFlow也只有约20%的分子构象得以保留（图4右）。

  
**小编总结**  

该工作开发了一套基于能量的多阶段AI生成分子三维构象的系统评估体系HEAD&TED，并测试了基于自回归或扩散模型的代表性生成模型。这一评估体系因其在评价策略上的改进规避了现有评估方法的局限，可以更可靠地筛除生成的异常分子构象，同时保持较高的计算效率，可被整合在完整的筛选工作流中。由于HEAD&TED体系能够给出原子及片段水平的评估结果，对分子生成模型开发与下游分子挑选等工作都能带来更多的引导信息。该研究的结果也表明，尽管一些现有的生成模型在此前的基准上表现良好，但生成构象的质量仍有较大提升空间。

  
**参考文献**

\[1\] Fan Fan, Bin Xi, Xianghu Meng, Han Wang, Bowen Zhang, Qingbo Xu, Wei Feng, Wenfeng Gao, Xiaoman Wang, Yuji Wang, Hongbo Zhang\*, Feng Zhou\*, Zhenming Liu\*, Wenbiao Zhou\*, and Bo Huang\*, Assessing conformation validity and rationality of deep learning-generated 3D molecules. Nature Communications, 2026, 17(1): 2481\. https://doi.org/10.1038/s41467-026-69303-5.
  
  
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
