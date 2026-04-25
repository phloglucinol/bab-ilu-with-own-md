---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIxMjYwOTA4OQ%3D%3D&mid=2247485714&idx=1&sn=95847faf4a5254d9cd226f88c247411a
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIxMjYwOTA4OQ%3D%3D&mid=2247485714&idx=1&sn=95847faf4a5254d9cd226f88c247411a
source_domain: mp.weixin.qq.com
title: 论文导读 ｜ 对比学习框架-DrugCLIP｜蛋白-配体评估-PoseBench｜免疫原性预测-ImmunoStruct
author: 
published_at: 
fetched_at: 2026-04-25T02:03:52Z
extractor: wechat_worker
content_hash: 975a8de836a4703ee53083c1380a0b91913e59112d6bb5c84b103d5e9182239c
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/T9mbEn97C3ib3dZaSOyJ2sFGZLgXZj40dg4wALXbrYViaeUfXaqZCsn28Ewh8bXByFcVvTrGBPGVW35POFljmyIw/0.jpg) 

# 论文导读 ｜ 对比学习框架-DrugCLIP｜蛋白-配体评估-PoseBench｜免疫原性预测-ImmunoStruct

原创 gzhAI gzhAI [ AIBioPred ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

[Nat. Mach. Intell. ｜用于分子性质预测的Kolmogorov–Arnold图神经网络](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247484975&idx=1&sn=32d30d0bc3261f0219da0feff4e3d60c&scene=21#wechat%5Fredirect)

[bioRxiv｜RFdiffusion3：利用RFdiffusion3的从头设计全原子生物分子相互作用](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247485347&idx=1&sn=04b97b25ea3794b9974f28fb0106e80f&scene=21#wechat%5Fredirect)

[Nat. Commun.｜DTIAM：预测药物-靶标相互作用、结合亲和力和药物机制的统一框架](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247484569&idx=1&sn=e91018c617cf12b9bdbdf302ace1ebbe&scene=21#wechat%5Fredirect)

[Nat. Mach. Intell.｜利用立体电子学注入的分子图推进分子机器学习表征](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247484530&idx=1&sn=81b349e3b588a14347fceedde63529cf&scene=21#wechat%5Fredirect)

[Nat. Methods｜InterPLM：通过稀疏自动编码器发现蛋白质语言模型中的可解释特征](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247485425&idx=1&sn=7ffd70037c567bedf91de142be855d54&scene=21#wechat%5Fredirect)

[论文导读 ｜ 蛋白质-肽/互作/打分/位点预测](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIxMjYwOTA4OQ==&mid=2247485519&idx=1&sn=1fc9bd6be8b457d34039c7cdaa4fbc99&scene=21#wechat%5Fredirect)
  
  
---

  
> 字数 2197，阅读大约需 11 分钟

# DrugCLIP：深度对比学习实现全基因组尺度的虚拟筛选

标题: Deep contrastive learning enables genome-wide virtual screening  
期刊: Science  
单位/机构: 清华大学

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/T9mbEn97C3ib3dZaSOyJ2sFGZLgXZj40d7wCaMV1Yhp2uKSP7oFDPDyG5w44iciblnd0ccAOPybxbvPo0rhOfURxg/640.jpg)

**在人类可成药基因组中,仍有相当一部分尚未被小分子治疗药物有效靶向。随着AlphaFold等蛋白质结构预测技术的发展,在全基因组尺度上开展药物发现逐渐成为现实目标。然而,当前广泛使用的虚拟筛选工具仍难以满足这一需求。无论是传统的分子对接方法,还是基于深度学习的模型,在计算成本上都过于昂贵,难以覆盖全基因组范围内的潜在靶点。基于这一背景,相关研究旨在开发一种高效的方法,用于全基因组尺度的虚拟筛选,从而能够快速为人类基因组中每一个可成药靶点识别潜在的小分子配体。为实现快速且准确的虚拟筛选,研究提出了DrugCLIP这一对比学习框架。该方法将蛋白口袋与小分子编码到共享的潜在空间中,并结合大规模合成数据以及实验解析的蛋白—配体复合物结构进行训练。在此基础上,可以借鉴现代搜索引擎中的稠密检索技术,实现利用蛋白靶点对大型化合物库的高速查询。为增强方法在AlphaFold预测结构上的适用性,研究进一步开发了GenPack这一生成式口袋精修模块,用于提升口袋识别的精度。DrugCLIP的有效性通过基准数据集评测和湿实验验证加以检验,并在此基础上开展了全基因组尺度的虚拟筛选工作,相关结果均以公开形式发布。在DUD-E和LIT-PCBA这两个广泛使用的虚拟筛选基准数据集上,DrugCLIP在速度和准确性方面均优于传统分子对接方法和当前先进的深度学习基线模型。同时,该方法在不同化学骨架和蛋白家族之间展现出良好的泛化能力,并对结构扰动具有较强的鲁棒性。在实验验证中,DrugCLIP成功识别了血清素2A受体和去甲肾上腺素转运体这两个精神疾病相关关键靶点的高效配体。其中,两种血清素2A受体激动剂的半数有效浓度低于100 nM,而两种去甲肾上腺素转运体抑制剂则通过冷冻电镜结构获得了验证。当与GenPack模块结合使用时,DrugCLIP在处理无配体结构以及AlphaFold预测结构等具有挑战性的情形下,显著优于传统对接方法和诱导契合对接策略。该组合还成功用于一个研究较少的靶点甲状腺激素受体相互作用蛋白12的筛选,该靶点此前既无已报道的全复合物结构,也无已知配体。在表面等离子体共振实验中,模型获得了17.5%的命中率,其中两种化合物进一步被证实具有酶抑制活性。此外,DrugCLIP被应用于一次全基因组尺度的虚拟筛选任务,针对约10,000个人类蛋白与5亿种化合物进行组合评估,在仅使用8块GPU的情况下,于24小时内完成了超过10万亿个蛋白—配体对的打分。该筛选共获得200多万种候选分子,覆盖约20,000个结合口袋,对应人类基因组中约一半的蛋白靶点。所有筛选数据均已公开,以支持更广泛的药物发现研究。DrugCLIP是一种经过严格计算评测与湿实验验证的超高速虚拟筛选方法。其计算效率使得在万亿规模上覆盖人类可成药蛋白组成为可能,并通过公开可获取的数据资源为下一代药物发现奠定了基础,尤其有助于推动对机制尚不清楚或研究不足靶点的系统性探索。**

原文链接：  
https://www.science.org/doi/10.1126/science.ads9530  
Github：

# PoseBench：评估深度学习在蛋白-配体对接中的潜力

标题: Assessing the potential of deep learning for protein–ligand docking  
期刊: Nature Machine Intelligence  
单位/机构: 密苏里大学哥伦比亚分校，劳伦斯伯克利国家实验室

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C3ib3dZaSOyJ2sFGZLgXZj40dl1hVcS7znbEAMMKJOCeuZ8M0p9oibqxscBibG3axOrtWgvaGhlWjkGDQ/640.png)

**配体结合对蛋白质结构及其体内功能的影响,在现代生物医学研究和生物技术发展中具有广泛而深远的意义,尤其体现在药物发现等应用场景中。尽管近年来已提出多种用于蛋白—配体对接的深度学习方法和相应基准,但此前尚缺乏系统性研究,全面考察最新对接与结构预测方法在更具普适性的实际应用背景下的表现,具体包括以下情形：其一,在仅使用预测得到的无配体状态蛋白结构进行对接时的适用性,例如针对全新蛋白靶点的应用；其二,在同一靶蛋白上同时结合多个配体或辅因子的能力,例如在酶设计中的应用；其三,在事先未知结合口袋信息的情况下对方法泛化能力的考察,例如面对未知结合位点的场景。为更深入地理解对接方法在真实应用中的实用价值,相关工作提出了PoseBench这一全面的蛋白—配体对接基准。PoseBench使研究人员能够对深度学习方法在从无配体到有配体状态的蛋白—配体对接以及蛋白—配体结构预测任务中进行严格而系统的评估。该基准同时包含以主配体为核心的数据集,以及引入给深度学习领域的多配体基准数据集,从而覆盖更具挑战性的应用场景。基于PoseBench的实证分析表明,深度学习共折叠方法整体上优于可比的传统对接算法和深度学习对接基线模型,但包括AlphaFold 3在内的一些主流方法在面对全新的蛋白—配体结合构象时仍然存在明显挑战。同时,部分深度学习共折叠方法对输入的多序列比对高度敏感,而另一些方法则表现出较强的鲁棒性。此外,在预测新的或多配体蛋白靶点时,深度学习方法往往难以在结构准确性与化学特异性之间取得理想平衡,这一问题仍有待进一步研究与改进。**

原文链接：  
https://www.nature.com/articles/s42256-025-01160-1  
Github：

# ImmunoStruct:实现用于免疫原性预测的多模态深度学习

标题: ImmunoStruct enables multimodal deep learning for immunogenicity prediction  
期刊: Nature Machine Intelligence  
单位/机构: 密苏里大学哥伦比亚分校，劳伦斯伯克利国家实验室

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C3ib3dZaSOyJ2sFGZLgXZj40dDGEyp753muyhL1icYGN8uWJibe2BXaOh0uEmlPicysmdACXB1UFicp4olw/640.png)

**基于表位的疫苗被认为是在传染病和肿瘤治疗中极具潜力的一类治疗策略,但免疫原性表位的准确识别始终具有较大挑战性。现有的大多数预测方法主要依赖氨基酸序列信息,尚未系统性地整合肽—主要组织相容性复合体(MHC)层面的结构信息与生化性质。为此,相关工作提出了ImmunoStruct这一深度学习模型,通过融合序列、结构和生化特征,实现对多等位基因Ⅰ类肽—MHC免疫原性的预测。该模型基于包含26,049个肽—MHC复合物的多模态数据集进行训练与评估,结果表明,在传染病表位和肿瘤新抗原表位等多种任务中,ImmunoStruct在预测性能和结果可解释性方面均优于现有方法。进一步分析显示,模型预测结果与一组SARS-CoV-2表位的体外实验测定具有良好一致性,并且在基于肽—MHC特征的肿瘤患者生存预测任务中同样表现出较强性能。总体而言,该研究不仅提供了一种性能优越的免疫原性预测方法,也展示了一种将等变图处理与多模态数据融合相结合的模型架构,为免疫治疗领域长期存在的关键问题提供了新的技术路径。**

原文链接：  
https://www.nature.com/articles/s42256-025-01163-y  
Github：
  
  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C39iaMr4p8gOeTaBuDSaDAClfveGOv8QS6WE1ddlHdHpBxUeQ2icYmdk50tsoAfrKLRxibhibuiajbXfNow/0.png) 

 AIBioPred 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/T9mbEn97C39iaMr4p8gOeTaBuDSaDAClfveGOv8QS6WE1ddlHdHpBxUeQ2icYmdk50tsoAfrKLRxibhibuiajbXfNow/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
