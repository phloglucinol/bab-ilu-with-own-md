---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489258&idx=1&sn=7300d80ee1a3ddc693da3b084a968c2d
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489258&idx=1&sn=7300d80ee1a3ddc693da3b084a968c2d
source_domain: mp.weixin.qq.com
title: 【佳作推荐】北京大学化学与分子工程学院高毅勤研究团队JCIM论文：PROTAC三元复合物的多构象建模与动态验证
author: 
published_at: 
fetched_at: 2026-04-25T02:03:55Z
extractor: wechat_worker
content_hash: 298a2e224f5b4cf1129146743b7ac22b0175ad48b9a8dd57f5bf675555b5325f
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EchtIx6BFzSyW7nicXMMbibLIos3mTGkvDdEcYc6RFZdaKzibPaw7vvtQV0iaxUWhoH6xenOibXZvicsXDw/0.jpg) 

# 【佳作推荐】北京大学化学与分子工程学院高毅勤研究团队JCIM论文：PROTAC三元复合物的多构象建模与动态验证

原创 ComputArt ComputArt [ ComputArt计算有乐趣 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EchtIx6BFzSyW7nicXMMbibLIxWTHMXKGMDYJHgZsTQF9gwEa0LAOk8D0olOxH52Om08beD80CJV7Ow/640.png)

蛋白质降解靶向嵌合体（PROTAC）是近年药物研发领域的前沿技术，它通过双功能分子将靶蛋白（Protein of Interest, POI）与E3泛素连接酶拉近，形成三元复合物，进而诱导靶蛋白发生泛素化并被降解。相较于传统小分子药物，PROTAC在降低剂量、克服耐药性及靶向“不可成药”靶点等方面具有显著优势。然而，PROTAC分子中连接链的设计仍是关键瓶颈：其长度、刚柔性等直接影响三元复合物的空间构象、稳定性及降解效率。尽管基于结构的设计方法受到关注，但由于三元复合物构象灵活多样，目前依靠晶体结构指导连接链设计的成功案例仍然有限。

这一困境源于双重制约：一方面，获取高质量POI-PROTAC-E3三元复合物晶体结构技术门槛较高；另一方面，现有晶体结构仅为动态体系的静态快照，可能受晶体堆积干扰，难以真实反映生理状态下的构象全貌。此外，研究发现，同一PROTAC可诱导多种复合物构象，而现有计算方法对这类多稳定相互作用模式的预测精度仍不足。

为应对上述挑战，北京大学化学与分子工程学院高毅勤研究团队发展了一套POI-PROTAC-E3三元复合物建模流程，并引入分子动力学模拟轨迹作为构象评价标准，建立基于构象覆盖度的量化评估体系，以更全面、动态的视角系统探索三元复合物的构象空间。相关成果已发表于美国化学会出版的著名计算化学期刊Journal of Chemical Information and Modeling上\[1\]。

研究者首先对PDB数据库中所有PROTAC三元复合物晶体结构进行了系统梳理。分析发现，绝大多数结构中靶蛋白与E3连接酶之间的直接相互作用非常微弱：通常近距离残基对数少于10对，界面面积小于500 Å²。这提示PROTAC分子在填补界面间隙、介导瞬时相互作用中起关键作用，也凸显了对此类弱相互作用、高柔性体系进行精确构象建模的特殊挑战。

该项工作中POI-PROTAC-E3三元复合物建模流程如图-1所示：首先采用改进快速傅里叶变换对接方法FFT生成初步的POI-E3复合物构象集合；接着利用基于AlphaFold2的蛋白-蛋白对接工具ColabDock进行重采样以拓展构象的多样性；然后将POI与E3配体对齐至各二元复合物结合口袋，并利用RDKit生成连接链的初始三维构象；最后使用分子对接程序DSDP将完整PROTAC分子对接到复合物中，进行构象优化与评分。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EchtIx6BFzSyW7nicXMMbibLII1aRHaJroiabHEwuCyxwOozCpELFy3n1NN6aBQyH7X3o02191ztR3ibQ/640.png)

**图1：POI-PROTAC-E3三元复合物建模工作流程示意图。**

为验证该建模框架的有效性，研究者选取了五个 POI 与 VHL 间相互作用微弱甚至为零的测试体系（PDB ID：8QW7、7JTO、7JTP、8FY1、8QJR），其连接链长度覆盖3至18个原子。研究者首先对这五个体系进行了100ns分子动力学模拟，结果显示所有体系的构象均从晶体结构起点发生明显漂移。尤其是在 POI 与 VHL 几乎无直接接触的 8QJR 体系中，模拟中观察到降解剂从 VHL 口袋解离后再次结合的动态过程，表明该体系可能存在多个亚稳态构象。

研究者首先系统比较了多种蛋白-蛋白对接方法（ClusPro、Hdock、Rosetta、FFTDock及其与ColabDock的重采样组合）在五个测试体系中生成POI-E3复合物的构象集合。结果显示（图-2），FFTDock 与ColabDock重采样组合策略所产生的POI-E3构象能更全面地覆盖从晶体结构出发进行100ns分子动力学模拟所采样的构象空间，为后续 PROTAC 分子对接提供了更丰富的受体构象基础。进一步分析显示，FFTDock、ColabDock 与 DSDP 相结合策略生成的三元复合物在对接分数与配体 RMSD 分布上更为集中，且主要位于低RMSD与低对接分数的优质区域，表明该组合策略具有更高的构象生成质量。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EchtIx6BFzSyW7nicXMMbibLIkbIRNIhicrj5cAAbQQhdF2hSG4NUnianqDibAYARfOJKZK5JzSmIz7MBA/640.png)

**图2：不同方法对5个测试体系生成POI-E3复合物构象的POI与E3口袋距离分布图。虚线表示分子动力学模拟所得口袋距离的上下限范围。**

为进一步评估该框架构建PROTAC三元复合物构象的准确性，研究者发展了一套基于集体变量的动态构象评价方法：通过定义描述POI与E3连接酶间相对取向（欧拉角Θ、Φ、Ψ）、方位（球面角θ、φ）及口袋间距（距离r）的六维参数体系，将分子动力学模拟轨迹降维投影至二维空间，形成反映构象分布概率的密度图；进而通过计算生成构象在二维图中覆盖区域的密度积分，量化其与真实动态构象集的接近程度，一定程度上克服了传统依赖单一静态晶体结构的局限性。基于此方法开展具体评估的结果表明（图-3），在测试案例8QW7、7JTO与7JTP中，该建模框架所生成的三元复合物构象能够成功覆盖或紧密靠近分子动力学模拟轨迹中呈现的高密度区域，这一结果从动态构象采样角度验证了该建模框架的构象生成可靠性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EchtIx6BFzSyW7nicXMMbibLIjoic0Z8nQIo8cOzgq88TUDibOrgdzvNTTTV8qyfCeD6pa0VRFFOdeSVg/640.png)

图3：左列：所有测试体系分子动力学模拟轨迹与不同方法生成复合物构象在二维空间上的分布密度图；右列：反映不同方法预测构象在分子动力学模拟中出现总概率的密度分数分布。

针对8FY1与8QJR两个建模效果欠佳的体系，研究者开展了进一步分析。其中，8FY1体系与8FY0共享相同的降解剂和E3连接酶部分，仅靶蛋白不同。为此，研究人员构建了以BCL-2替代BCL-xl的杂合模型，并开展了三轮100 ns分子动力学模拟。结果显示，该杂合系统的构象空间较原单一晶体结构出发的模拟明显拓宽，且新产生的复合物构象在该拓展构象空间中仍具有良好的覆盖度（图-4）。这说明对于柔性较大的三元复合物，仅基于单一晶体结构的短时模拟可能无法充分覆盖其构象空间。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EchtIx6BFzSyW7nicXMMbibLIIic3kd5yyLUROsaXf2nO2JNWd28Gmx98YbLicFnaQK460rjvqbYicib7XQ/640.png)

图4：对8FY0/8FY1杂合系统进行3次平行100ns分子动力学模拟分析结果。（a）分子动力学模拟轨迹RMSD波动；（b）不同方法生成POI-E3复合物口袋距离分布；（c）分子动力学模拟轨迹与不同方法生成复合物构象在二维空间上的分布密度图；（d）不同方法的密度分数分布。

对于高度动态的8QJR体系，研究者将生成构象聚类后，从每类中选取一例进行10 ns短时分子动力学模拟。结果显示，所得构象分布在多个高密度区域，其中不少是原始基于晶体结构的长期模拟未能覆盖的（图-5）。延长模拟至50 ns后这些构象仍保持稳定，提示其可能对应自由能景观中的局部极小点。这表明，该研究提出的构象生成与短时模拟验证策略，能够有效探索传统模拟难以采样的构象空间，并捕获潜在稳定构象，从而为降解剂作用机制研究和理性设计提供更全面的动态结构基础。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EchtIx6BFzSyW7nicXMMbibLI0yd3rgbJjAYx5bEYibkmcpI6J3wzz3rp1js6hFt8MF1jVPzocQGib40Q/640.png)

图5：从分子动力学模拟结果中提取三元复合物构象的降维分布图。

**小编总结**  

该项工作基于已有计算方法构建了一套高效的POI-PROTAC-E3三元复合物建模流程，具有较强的实用性。另外，作者提出以分子动力学模拟轨迹作为构象评价标准，建立基于构象覆盖度的量化评估体系，将PROTAC三元复合物建模的评估基准，从单一的静态晶体结构升级为动态的分子动力学构象系综，为PROTAC连接链的理性设计提供了可靠、全面的构象起点与评估工具。

**参考文献**

\[1\] Zhao, T.; Gao, Y. Q. Shotgun Approach for PROTAC Ternary Complex Modeling and Evaluation. Journal of Chemical Information and Modeling 2025, 65 (23), 12929–12944\. DOI: 10.1021/acs.jcim.5c02037.

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
