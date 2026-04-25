---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkwMzY4NDA5MA%3D%3D&mid=2247491586&idx=1&sn=5fdfc71397831806df20a81249489dcc
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkwMzY4NDA5MA%3D%3D&mid=2247491586&idx=1&sn=5fdfc71397831806df20a81249489dcc
source_domain: mp.weixin.qq.com
title: AI解锁药物“续航力”：Schrödinger团队提出全新预测框架
author: 
published_at: 
fetched_at: 2026-04-25T02:03:34Z
extractor: wechat_worker
content_hash: 94806d49299a3af10c9c20d8e2d20c807b888380c79a13ffcb6d92f7aa04086c
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/m0Oo0Qo05yZeMJlxE6ayOnvy5l5exhAx1Wot55EYYPg25wHSSAKd94BiayicS5X62PnUYNJ44Y03PelsmhNJUARdZxBtBC3r4YGRicPiaUib2Iq8/0.jpg) 

# AI解锁药物“续航力”：Schrödinger团队提出全新预测框架

原创 Deep Biology Deep Biology [ Deep Biology ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m0Oo0Qo05yaGjs1mNh2zicTXtVsPUPFjlc2PkWicYgKSXSjjkib2oBZDL3bKLvufYCdlibdwF5XTv26wZ3XTNgXmsg97yGncV0cNiaJLVUlqCcic0/640.png)

  
**![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4KD6GHkP2NmgCRaKZsf6vJf6BUdLIsdbvlQ2eKCPweOuY0Z35zicRkh86hr3FgmWkicQy5BHVG4yQRnAnjaxGlqQ/640.png)**

  
**（1** **）“探索-利用”两阶段工作流：首次将 Random Acceleration Molecular Dynamics (RAMD) 与 Infrequent Metadynamics (iMetaD) 有机结合，先用RAMD快速探索配体可能的脱离路径，再用iMetaD沿主路径精确计算驻留时间。这种分工既保证了效率，又提升了精度；**

**（2）高度自动化，减少人工干预：整个流程从系统准备、路径聚类到CV定义、iMetaD运行，几乎无需手动调参，具备“即用型”工具的潜力，适合工业级药物筛选场景。**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4KD6GHkP2NmgCRaKZsf6vJf6BUdLIsdbUpsEfGRPWkR1diafClwMiaEfaAOd5FGHAcdPia6VeBIAEYhsSC0ZF5EGw/640.png)

  
该研究的背景源于药物研发中对“驻留时间”（即药物与靶点结合持续时间）重要性的日益重视——它比传统亲和力指标更能预测体内药效、毒性及给药频率。然而，现有计算方法面临两难困境：基于经验拟合的快速方法精度有限且依赖大量实验校准；而基于严格动力学的物理模拟虽准确，但计算成本极高，难以在药物设计周期中大规模应用。为此，作者提出了一套结合随机加速分子动力学（RAMD）与罕遇元动力学（iMetaD）的自动化两阶段工作流，旨在在精度与效率之间取得平衡，实现无需人工干预的绝对驻留时间预测。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4KD6GHkP2NmgCRaKZsf6vJf6BUdLIsdbY7dJ9r3y80ENkUUNVfsiawg84VAmdsB6UdbIp3Jo4m0hWkcnWdgbGDw/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m0Oo0Qo05yZzPfB2richm6yaLUydCKxsRWicxo3ibpAmnbZlAb3wQnib4LKeDhQ720eiaPu04qD4fwdOEuh0C8lEBHrSmvt0lwhT2PQEf6nvAVWo/640.png)

  
首先文章展示了本文提出的两阶段“探索-利用”工作流：首先通过随机加速分子动力学（RAMD）生成一系列配体脱离轨迹；随后将这些轨迹处理为摘要路径并进行聚类，识别出主要的脱离路径；最后基于该主路径定义集体变量，并利用罕遇元动力学（iMetaD）沿此路径采样，从而估计出绝对的药物驻留时间。该流程图清晰概括了整个方法的核心步骤，强调了RAMD的探索能力与iMetaD的精确计算相结合的策略。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m0Oo0Qo05yZDMcfWNJQswlN0fuX2cFHDvMyqZTAKuxdusmEdfZlxknko66sibYwetyLCGQ2WQKDm3gOyjHWibKIQAUJA12hUQU3EBMBx2MXTw/640.png)

  
其次文章详细说明了如何从RAMD轨迹中提取和精简出代表配体脱离过程的摘要路径。首先从RAMD模拟的初始帧开始，通过反向追踪识别出配体从结合位点运动至溶剂暴露区域的“反应性”轨迹片段，并排除未产生位移的“预反应”部分；然后提取初始结合构象和首个溶剂暴露构象作为关键帧，再通过蒙特卡洛方法筛选出约20个等距的中间构象，形成粗略路径；最后通过插值平滑处理，使相邻构象间的RMSD间距约为1.5 Å，得到最终的摘要路径。这一系列处理将冗长的原始轨迹压缩为具有代表性的关键帧序列，为后续的路径聚类和集体变量定义奠定了基础。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m0Oo0Qo05yYiaKDwj6hHwygicc67GMcsHRcPRQ2CticgssbZvcPicp5xbc0AIQUiaUSUcRE9SX0ppicqZeX7oe2Gt3qfwn2uxMrkzwEL5vfxCTgZ4/640.png)

  
随后以示意图形式展示了路径聚类的基本概念。左侧表示从RAMD模拟中获取的多条脱离路径，每条路径由一系列摘要点构成；右侧将这些路径投影到二维空间，用不同颜色表示不同的聚类簇，其中粗箭头代表各簇的质心路径，虚线箭头代表簇内其他成员。通过聚类分析，可以识别出出现频率最高的主脱离路径（图中橙色簇的质心），该路径将被用于后续iMetaD模拟中的集体变量定义。该图直观地说明了如何从多条随机轨迹中自动归纳出主导的脱离通道。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m0Oo0Qo05yZcaczz4go6Koncu7kUwAibqG8TsiaMpOibV5bsl9pw9F7XPd7JHoPeIVianvkT2J39xyqqtTUB8Tq0xI8ib1RqtUwAjDHByMMFJW4o/640.png)

  
之后阐释了在进行路径聚类前，如何对不同长度的脱离路径进行标准化对齐和距离计算。由于每条路径的摘要点数量可能不同（图A），需将较短的路径通过外推延伸至与最长路径相同的长度（图B），确保所有路径具有相同数量的位置点。随后，在计算两条路径之间的距离时，仅考虑配体仍与蛋白接触（MinDist < 3 Å）的片段，对已完全溶剂化的部分赋予权重为零，并采用基于蛋白叠合后配体重原子的RMSD作为距离度量（图C）。这种方法确保了距离计算聚焦于配体在蛋白内部的关键脱离阶段，避免了溶剂区域随机游走带来的干扰。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m0Oo0Qo05ybvicDMBWroAKjBLwnVr2Q7P4DImN0oPdgrbBl4WyXm11O7MPEn92PhfWNqaxpzEOw8KoNRTt0Dwpf5v9fKSv3KSibRrrHK9u6MQ/640.png)

  
然后以p38体系中的BIRB796配体为例，展示了RAMD路径聚类的结果以及后续iMetaD模拟的典型轨迹。图A中，不同颜色的球体代表不同脱离路径簇中配体质心的位置，较大的球体为各簇的质心路径，其中红色簇包含最多的路径（30条中的9条），被选为主路径用于定义集体变量。图B则显示了一次iMetaD模拟中配体沿该主路径脱离的轨迹，彩色渐变表示模拟时间进程，橙色半透明配体表示路径上的关键构象，清晰地展示了配体如何逐步从结合口袋运动至溶剂环境。该图验证了RAMD能够有效采样多种脱离途径，且主路径能够引导iMetaD进行有针对性的增强采样。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m0Oo0Qo05yZE2cbhpsbdNSvYkib5HLibrpwjafVsqJLQtdz3tCONXrUrW66uu3P4icsBt5fZicxiaiaKBUiaXvmhrxYngMCv7F7wfmWPFKC1MkDUO4/640.png)

  
接着对比了p38激酶抑制剂系列在RAMD模拟时间和iMetaD预测驻留时间与实验值之间的相关性。图A显示RAMD模拟时间与实验驻留时间的对数呈弱相关（R²=0.19），表明仅靠RAMD时间难以准确量化绝对驻留时间。图B则展示了使用主路径CV进行iMetaD计算后，预测值与实验值呈现出极佳的一致性（R²=0.98，RMSE=0.66），且大部分点落在1个数量级误差范围内，显著提升了预测精度。这一对比突显了iMetaD在恢复真实动力学方面的关键作用，同时也说明RAMD路径质量为后续精确计算提供了可靠基础。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m0Oo0Qo05ybk6GJZ1xvicq6iaYKmuTNhGo4eotswGWUTU6jwxMLeKsw6iavLrfdMfkKyM2PsyKibcA4wePssna5IYGiaicicgiaXc6hu7k6qb6uk9rU/640.png)

  
该图为CDK8体系九个化合物的iMetaD预测驻留时间与实验值的相关性图。图中水平误差棒表示部分化合物因低于实验检测限而存在不确定性。整体上，预测值与实验值吻合较好，R²达到0.40，Spearman秩相关系数为0.86，表明方法能够正确排序不同配体的驻留时间。值得注意的是，化合物4F6W（分子量较大且柔性高）的iMetaD模拟成功率较低，其预测偏差也较大，这提示该方法对高度柔性的配体可能存在局限性，而模拟成功率本身可作为预测可信度的内在指标。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m0Oo0Qo05ybI9PdsqHvEibpcJAFvfKzDviaW6tJ8icF0DdGSD2kRicHiccxaCRWA1lUp14dicgNAezegPIia4ISJKBiaHpSGCR4Cz6V6icxEBb9YCz14/640.png)

  
该图展示了A2A腺苷受体系列配体的iMetaD预测结果与实验值的对比。图中显示大多数配体的预测值落在理想对角线附近，R²高达1.0（拟合线斜率1.0，截距-0.20），表明绝对驻留时间被准确恢复。仅有一个配体（4k-up）显著低估，作者指出其预测值对模拟条件敏感。整体而言，该图证明了工作流在膜蛋白体系中的适用性，且相较于单独RAMD（R²=0.26）有明显改进，进一步验证了探索-利用策略的普适性。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m0Oo0Qo05yafs0jibQ6icPBnoGibFSIFXSVyCgmyDXOoGWeicjvSezMDu8Xiaq4LjU6G7Hynp0LiaK2aWRVeX2pmYCf37wRia1twORDh5POkrouXbU/640.png)

  
该图为T4溶菌酶突变体体系的iMetaD预测驻留时间与实验值的对比。尽管整体趋势正确（Spearman ρ=0.90），但预测值系统性地偏高（拟合线斜率3.4），且L99A突变体的偏差最大。分析认为，该突变体结合腔完全封闭，配体脱离需要F114侧链的显著重排，而这种蛋白构象变化未被配体为中心的路径CV充分描述，导致iMetaD未能加速相关自由度，从而高估驻留时间。这一结果揭示了方法对蛋白柔性依赖的边界，同时也说明即使在这种挑战性体系中，排名能力依然保持良好。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m0Oo0Qo05yb9nlFHe1giaXAXB43ibRGZW86M3SAYQhLtib7OFtHcqoicRHGZfyZYdxJj7iaXCNv6tYQ7PVS5ZHT7ib5RibJogEPialX9vJBFzbfBJ7Q/640.png)

  
该图汇总了默认参数下全部五个体系29个化合物的预测结果，仅包含实验可测范围内的数据点。图中不同颜色代表不同靶点，绝大多数点落在1-2个数量级误差带内，整体R²为0.80，RMSE为1.22，Spearman ρ为0.90，展现出方法跨体系、跨时间尺度（覆盖10个数量级）的稳健预测能力。最大的偏差出现在快速解离的片段体系（如T4L和Trypsin），提示默认RAMD参数可能不适用于低驻留时间 regime。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m0Oo0Qo05yY4haWu0Jafl2ywS2q8KoYpEK5ibzoMt1qB9HYW0ftOvs9nnKJluaticq7ES6Vgc4ZaAnaG5OSnpGmBIx4XG5K5uXibKdiaWyme8jA/640.png)

  
最后展示了针对快速解离体系（T4L和Trypsin）调整RAMD参数后的改进结果。通过将RAMD力常数从15 kcal/mol/Å降低至5 kcal/mol/Å并增加副本数，这些体系的预测精度显著提升，整体RMSE从1.22降至1.08，R²从0.80升至0.87。透明点为原默认参数结果，半透明显示改进效果。该图强调RAMD参数对路径质量的关键影响，并提供了参数调优的实用指导：对于实验驻留时间短（<10 s）或RAMD模拟时间<100 ps的体系，应采用更温和的偏置力，以避免路径失真。

  
综上所述，该研究为药物发现提供了一种高精度、自动化的驻留时间预测工具，在五个靶点、29个化合物上验证了其跨越多达10个数量级的预测能力（RMSE低至1.08）。其核心影响在于将预测从“经验拟合”推向“物理自动化”，不仅为药物筛选提供了可即时部署的工具，更通过内置可靠性指标解决了预测可信度问题。此外，其“探索-利用”框架为未来整合机器学习、描述蛋白柔性变化奠定了基础。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4KD6GHkP2NmgCRaKZsf6vJf6BUdLIsdbtMMn6xw5dxjedaR0ePrZzZ5LX2YSIBJoI3Sdy1XukXGIkFDtuZsqeg/640.png)

  
文章标题是Toward Automated Physics-Based Absolute Drug Residence Time Predictions，作者是来自Schrödinger和University of Maryland的Zachary Smith，Davide Branduardi，Dmitry Lupyan等人。文章于2025年发表在Journal of Chemical Information and Modeling期刊上。

  
DOI：10.1021/acs.jcim.5c01832 

  
by yym

  
————————————————

  
关于薛定谔软件

  
美国薛定谔公司（Schrödinger, Inc.）成立于1990年，是全球领先的计算化学与分子模拟软件公司，总部位于美国纽约，并于2020年在纳斯达克上市。公司以量子力学奠基人薛定谔命名，核心理念是通过第一性原理物理、化学模型结合高性能计算与人工智能，加速药物与材料创新。其强大的软件平台集成量子化学、分子动力学、粗粒化模拟、自由能计算和机器学习等多尺度方法，广泛应用于药物发现、材料科学、半导体、能源及OLED等领域。薛定谔软件以高精度、亲用户、工业级验证和良好可视化著称，既能支持基础科研，也能直接指导实验与工程决策，是连接理论计算与实际应用的重要工具。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/mYM4jHjSdQdOfcZBk9rqTVPvIseW4UxBe1hJgcLg5GyqibCIL8whibGxuUb8iaRReK0WdJCUWiaCg4ZWg6btKM6Y8g/640.png)

  
薛定谔软件提供免费试用、技术培训、设备推荐、硬件支持以及体贴、及时、周到的售后服务，欢迎扫码联系：  

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/mYM4jHjSdQcGh5LtpHRPXt5ajiaJAKLfcszaqpocsym1D4j9unricewhesr8Ua48dlxmTVes9O3DNrKPlRmpLH6Q/640.png)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/mYM4jHjSdQficNdbpibtKMMynXe0ByrFSrRyrs4Q3dmk6SQxSeaYVEwv49WQ2YVYGGicH6dN6ibf5fkSgnPWBZkB5Q/0.png) 

 Deep Biology 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/mYM4jHjSdQficNdbpibtKMMynXe0ByrFSrRyrs4Q3dmk6SQxSeaYVEwv49WQ2YVYGGicH6dN6ibf5fkSgnPWBZkB5Q/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
