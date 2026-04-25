---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzYzOTA3NjkxMg%3D%3D&mid=2247583036&idx=1&sn=605e3d4f085a45fd28c2e3eea2376d88
canonical_url: https://mp.weixin.qq.com/s?__biz=MzYzOTA3NjkxMg%3D%3D&mid=2247583036&idx=1&sn=605e3d4f085a45fd28c2e3eea2376d88
source_domain: mp.weixin.qq.com
title: J Med Chem｜中国药科大学刘海春等：整合药物化学家专业知识与深度学习实现自动化分子优化
author: 
published_at: 
fetched_at: 2026-04-25T02:03:24Z
extractor: wechat_worker
content_hash: c7b2b4e161ba70da5a791aa8d7e77fdcee8f0d78eedd5ac952a596d1a2e2d229
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/2r1FIaqNHdUH5HiaNkqWMAIZP5ibNINujdVW5FslT2Dn5ib7oiajIic5Cc7hVmGDbI46Fz9b1tXLqsJGP4ViaxuyLiae4oZozHhpL6NTo9GXNeWGaM/0.jpg) 

# J Med Chem｜中国药科大学刘海春等：整合药物化学家专业知识与深度学习实现自动化分子优化

原创 智药邦 智药邦 [ 智药邦 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

成功的化合物优化在很大程度上依赖于药物化学家的专业知识。基于此，中国药科大学刘海春、陆涛、陈亚东及张艳敏团队于2026年1月30日在《Journal of Medicinal Chemistry》上发表文章，题为“Integrating Medicinal Chemist Expertise with Deep Learning for Automated Molecular Optimization”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2r1FIaqNHdWPmSWFwoajch2aj004icZDyicLX4qAzbiaLMNic2obD2ibqWfQVOibhgEYAp79qN3xHPgBJXf37Mz2sROdXE1XibaRsl6IGFjCelou1Q/640.png)

在该工作中，研究人员从药物化学文献中筛选了近9000个分子优化策略。在专家知识的驱动下，构建了基于图深度学习的MolOpt框架，用以扩展这些结构优化策略。结合专家衍生策略与MolOpt，作者开发了一个用于分子优化的自动化平台AutoOptimizer。为展示该平台的实际应用，针对成纤维细胞生长因子受体4(FGFR4)和造血祖细胞激酶1(HPK1)进行了案例研究。

AutoOptimizer代码仓库：

https://github.com/liang2508/AutoOptimizer

**背景**

近年来，人工智能技术的快速发展为药物研发开辟了新的途径。人工智能在靶点识别、分子生成、虚拟筛选和性质预测等方面的应用正加速药物发现进程。尽管取得了这些进展，缺乏高质量数据仍然是限制人工智能在药物开发中应用的主要障碍。此外，许多人工智能模型缺乏对化学规则和领域特定知识的基本理解，这可能导致生成不合理或不稳定的分子结构。因此，构建高质量数据集并将专家知识与化学直觉相结合至关重要。

与结构修饰相关的文献提供了大量针对众多靶点的化合物优化案例，为分子优化提供了宝贵的见解。通过整合文献中这些有效的分子优化策略，可以极大地加速先导化合物的结构优化与发现。然而，迄今为止尚无基于药物化学专家知识的结构修饰策略数据库可用。药物化学家通常利用他们的专业技能和专业知识来设计和优化针对特定靶点的小分子，这些设计理念常常源自先前应用于其他靶点的药物发现技术(图1)。成功的结构优化案例表明，替换特定的子结构可以显著改善先导化合物针对特定靶点的物理和生物性质，从而开发出结构新颖的抑制剂。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdXHRhWtVc2tjCMMYfNA7GduXfrgH8uU4coQ8xTDJ22xJYbqHwdkra3mQFaNI7eGzjZvkJ88LCDS05jLUQKxVQjmLP2Fdw5adjs/640.png)

图1 AutoOptimizer工作流程的构建及在FGFR4和HPK1靶点上的验证。

在本研究中，作者将从文献中提取的结构优化策略以及其开发的深度学习模型MolOpt生成的策略整合进了一个名为AutoOptimizer的自动化分子优化工作流程中(图1)，该流程完全由专家知识和深度学习模型支持。它可以快速高效地生成大量优化的分子，显著提高先导化合物发现的效率，加速药物发现进程。

**数据与方法**

为了促进基于专家知识的合理化合物设计，研究团队收集了过去24年(2000-2023年)发表在《药物化学杂志》(JMC)和《欧洲药物化学杂志》(EJMC)上的经典文献中近9000个结构修饰策略。源自专业知识的分子优化数据是有限的，不足以覆盖与药物发现相关的巨大化学空间。为解决这一局限，作者开发了一个深度学习模型MolOpt(图2)，旨在从可能尚未被药物化学家考虑过的广泛数据集中揭示新的分子优化策略，主要包含预训练深度学习框架和知识引导的迁移学习策略两部分。在预处理阶段，使用匹配分子对(MMP)分析方法从Enamine数据库的分子中提取分子优化策略对，骨架片段被表示为分子图，这些分子图使用门控图序列神经网络(GGNN)模型进行训练。在微调阶段，利用从药物化学文献中提取的分子优化策略来调整预训练模型的参数。这种知识引导的迁移学习策略引导模型与药物化学家采用的优化思路保持一致，增强了其生成相关且有效的分子修饰的能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2r1FIaqNHdXpID04ic0zGwHSfHaBb6TiamcjWp54e4ZE48nJIia0JWEJrnJr28hUzeQoco3n1LWIY4ibWleJ8F29cBIln4icZ1614RkUJrYHzPDU/640.png)

图2 MolOpt工作流

从现有的分子优化过程中提取结构片段优化反应，并进一步利用深度学习技术生成这些反应。通过结合手动提取和机器生成的结构片段优化策略，作者开发了AutoOptimizer，这是一个使用Pipeline Pilot组件构建的自动化分子优化平台。其分子优化工作流程如图3所示，优化过程包括数据预处理与转换、结构优化反应的生成及分子优化三个阶段。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdUlo6IK7V2vPAgxGFdEDe4T0DIJFFZzofnqQiassvXgOUGkaF5tWabqlDeEg8sRKEicrqH1vvh28d8DiaKSb5u3xQSHIANVsD8BU0/640.png)

图3 AutoOptimizer工作流

为了评估AutoOptimizer在先导化合物优化中的效果，研究团队选择了一个已知的FGFR4抑制剂和一个课题组内部的HPK1抑制剂作为起始化合物进行结构优化。经CPIScore模型预测具有潜在FGFR4和HPK1活性的化合物，随后进行基于结构的虚拟筛选以进一步评估。采用分子力学/广义Born表面积(MM/GBSA)方法作为对接后预测工具。这种综合方法展示了AutoOptimizer在识别对特定抗肿瘤靶点具有高结合亲和力的新骨架方面的潜力。

**结果**

  
**结构修饰数据库分析**

  
基于知识的分子优化数据库分析。分析重点考察了靶点的分布以及结构修饰前(化合物1)和修饰后(化合物2)化合物理化性质的分布。如图4a所示，收集到的优化策略涵盖了多样化的靶点，其中酶仍然是小分子的主要靶点，受体、激酶和其他酶合计占所有结构优化靶点的70%以上。图4b展示了几种优化策略，片段替换是最常见的优化类型，其次是环修饰和生物电子等排替换。此外，这些优化策略的发表年份分布如图4c所示。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdXBFKBqA4j78LxZSUdd4OSJ0wO5k8OTWAXCZgJd4nLNkqS48ImFrtyEI7jXf0oOu18YH6rtTTXHroiahTO2x0XItvPfJD6O0nWQ/640.png)

图4 对8992个结构优化实例的分析，显示靶点分布、结构优化实例及比例、发布年份分布。

此外，检查了结构修饰前后化合物物理性质的分布(图5)。观察到的生物活性改善以及理化性质趋势强调了这些优化策略在提高化合物疗效和类药性方面的有效性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2r1FIaqNHdVGkPLppyicUaLW50DTecsFPGkIslicibu9VZ3flh4siad5D9EahxsHGFLmicvhrMQCXcL8pz0KImnxmyYxkaTnkY6cot3NpjBpqrtw/640.png)

图5 对8992个结构优化实例的分析，显示修饰前(紫色标记的化合物1)和修饰后(黄色标记的化合物2)化合物物理性质的分布。

预训练分子优化数据库分析。修饰前(蓝色标记的化合物1)和修饰后(黄色标记的化合物2)化合物物理性质的分布如图6所示。与起始化合物1的分布相比，化合物2表现出更优的性质，这确保了预训练模型倾向于生成化学上可行且具有类药性的结构。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdVdia0E8IxL2iayu7MibzibEic180GfQiaic0vcQhxDJQibm8UCyJ5mWtQmBF5ERd2Wj790TfTmH6bRwh1426UGTgibvbicn4HZrMrO4Ak30/640.png)

图6 通过匹配分子对分析方法获得的结构修饰实例分析，显示修饰前(蓝色标记的化合物1)和修饰后(黄色标记的化合物2)化合物物理性质的分布。

MolOpt生成的分子优化策略分析。预训练模型和微调模型生成的化合物理化性质分布如图7所示。与仅由预训练模型生成的分子相比，由微调模型生成的分子与起始分子的相似性值更低，显示出更高的结构多样性。图7b显示微调策略产生了更高比例的位于“最优区域”(其特征同时具有高预测活性和有利的对接/类药性质)的化合物。此外，使用迁移学习采样策略生成的化合物具有更高的QED评分和更低的SA评分。这些发现表明将专家知识整合到迁移学习模型中成功提升了优化后化合物的类药性和合成可行性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdX57KhDmfqwTy7og71DJyb9Q8SMXsVOGEW5bU2IWk7gqEsH8l3PesL1ibE7IeU5hn3XVgBGwwtHYKQ9MrXk2Xvbx42GxMjLMnOI/640.png)

图7 对从预训练模型(紫色标记)和微调模型(黄色标记)采样的优化策略生成的化合物进行分析。

  
**验证案例1：发现高效的FGFR4抑制剂**

  
FGFR4信号通路的激活不仅与恶性肿瘤的发展密切相关，还与肿瘤细胞对靶向治疗的耐药性有关。目前，已有几种FGFR4抑制剂进入临床试验。以一个已知的FGFR4抑制剂为起点，使用AutoOptimizer进行了三轮优化(图8a)。图8b展示了FGFR4抑制剂(以"ref"表示)及来自第一轮(s1)、第二轮(s2)和第三轮(s3)优化所得化合物的化学分布。每增加一轮优化，分子数量就会增加几个数量级，从而显著增加了所探索化学空间的多样性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdUX7tpC8Lfs51avhPyicVZDiaK7abfmsudQibPKnJ14x3sxlfDLb6nfnQMeVoTwJUuRMMlj7PnxiaFOticPfmibaQ1iaumAMWAmabuXUQ/640.png)

图8 FGFR4抑制剂发现案例研究

根据结合亲和力预测模型和基于结构的虚拟筛选方法的预测，选择并合成了八个化合物。这八个化合物的化学结构和IC50值如图8e所示。M8对FGFR4激酶表现出最强的抑制活性，IC50值相较于起始分子活性提升了77.6倍。这些结果表明AutoOptimizer可以通过对初始化合物的结构修饰生成具有期望活性的分子。

图9展示了起始化合物Hit-1和合成的化合物在FGFR4结合口袋内的结合模式，突出了关键的相互作用残基。这些化合物在FGFR4的结合口袋内表现出相似的相互作用模式。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdUib8yI6LCMdHQzmwcYLnjs7qDJicvJZZRpm6tbxT8X3IGS6Nr7fpSV3mJNPicypKc3kD2ibJYPKXVlCiaKUV6Uate5Eiak7DoupQfIs/640.png)

图9 FGFR4与配体结合相互作用的示意图

  
**验证案例2：发现高效的HPK1抑制剂**

  
HPK1是丝氨酸/苏氨酸相关蛋白激酶MAP4K家族的成员，作为T细胞受体信号的负反馈调节因子发挥作用。抑制HPK1能有效促进T细胞活化。大量研究表明，HPK1参与多种信号级联反应，并在肿瘤生长中扮演重要角色。以课题组内部发现的HPK1抑制剂LT-1103−214为起点，使用AutoOptimizer进行了三轮优化(图10a)。已知HPK1抑制剂以及来自三轮优化化合物的化学空间分布如图10b所示。通过结合亲和力预测和基于结构的虚拟筛选选出的六个化合物进行合成，鉴定出的化合物的优化过程如图10e所示。这六个化合物是通过AutoOptimizer进行的三轮优化获得的，优化过程中使用了深度学习模型MolOpt生成的分子优化策略。可以看出，这六个化合物与起始化合物的相似性得分均大于0.65，并且所有化合物的实验活性值均低于1 μM。在这些化合物中，M9对HPK1激酶具有最佳的抑制活性。上述结果进一步表明AutoOptimizer可以通过对给定的起始分子进行微小修饰生成更多具有理想活性的分子。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdWFicq17mA9MDwujicB7t8sOfvic8tFds0oHQygzARTvE5oPw0jl5oddh2jFguz3m7DYmfAp1VDI0DicOibowFePOPUmujpPzUKMmwk/640.png)

图10 HPK1抑制剂发现案例研究

此外，进行了对接研究以分析这六个分子在HPK1活性口袋内的相互作用，与关键相互作用残基的结合模式如图11所示。合成的化合物在HPK1的结合口袋内表现出相似的相互作用模式。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/2r1FIaqNHdVjSoAqWiahoYpXTWpnHiavrXtuHLUwiaF8qZqCbNAgDriaXDXZOJrwklEK0Y5Jvz9SuZm6XAqFicHu2jF4goY3VH07bLg5zUrUY2GU/640.png)

图11 HPK1与配体结合相互作用的示意图

**总结**

研究人员首次基于化学家的知识构建一个分子优化策略库，并在此基础上开发了一个高度用户友好的自动化优化平台AutoOptimizer。用户仅需输入想要优化的起始分子结构，该平台即可实现快速的多轮优化，生成数以千万计的潜在分子。将AutoOptimizer应用于两个激酶靶点FGFR4和HPK1以验证其有效性。结合药物-靶点结合亲和力预测模型和基于结构的虚拟筛选，并对筛选出的化合物进行实验验证，这一组合策略取得了理想的结果，发现了对FGFR4具有高生物活性的M8和对HPK1具有高亲和力的M9。这项研究不仅弥合了专家知识与人工智能之间的差距，而且为探索广阔的化学空间提供了一个可扩展的框架，为更高效、更具创新性的药物发现铺平了道路。

参考链接：

https://doi.org/10.1021/acs.jmedchem.5c03746

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
