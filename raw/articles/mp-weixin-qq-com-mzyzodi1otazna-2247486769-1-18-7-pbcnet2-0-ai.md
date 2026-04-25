---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzYzODI1OTAzNA%3D%3D&mid=2247486769&idx=1&sn=2a2c9c56a25c5c74703e89201b182812
canonical_url: https://mp.weixin.qq.com/s?__biz=MzYzODI1OTAzNA%3D%3D&mid=2247486769&idx=1&sn=2a2c9c56a25c5c74703e89201b182812
source_domain: mp.weixin.qq.com
title: 18%精度跃迁，7倍效率加速！PBCNet2.0 开启 AI 驱动结合亲和力预测的新纪元
author: 
published_at: 
fetched_at: 2026-04-25T02:03:49Z
extractor: wechat_worker
content_hash: 5aacaec1e54df56d79249d6a2d058816b516133d1a2065f483b9480be2f743fb
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/JRd5vo3IIOj2vbYqZGyoSWuKkibOVNJSictutNuwswR3ezIdzmWCziaMXh4UEtqKQqK9kLcfibofKqOYkh4fhsUzLw/0.jpg) 

# 18%精度跃迁，7倍效率加速！PBCNet2.0 开启 AI 驱动结合亲和力预测的新纪元

原创 游刃有余的 游刃有余的 [ SciMiner科学矿工 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在药物研发的漫长征途中，准确预测蛋白质与配体之间的“化学牵手”——结合亲和力，一直是决定分子优化的核心难题。传统的自由能扰动（FEP）计算虽然精准，却因极高的算力消耗和时间成本让许多团队望而却步。

今天，SciMiner 平台正式迎来重磅工具更新：PBCNet2.0 算法正式部署上线！ 这款基于笛卡尔张量等变神经网络的“性能猛兽”，不仅在零样本预测上媲美工业级物理模拟，更实现了 718% 的研发提效。 

  
**核心痛点：为什么我们需要更好的亲和力预测？** 
  
  
在创新药研发的 Lead Optimization（先导化合物优化）阶段，化学家往往需要对数百甚至数千个分子进行微调。此时，判断哪个原子改动能增强活性，就像在暗房里摸索。 

* 传统实验法：耗时长、成本高，无法覆盖巨大的化学空间。
* 传统计算法（如 FEP）：虽然精准，但单个样本耗时数小时，难以应对大规模筛选。
* 早期 AI 模型：往往缺乏物理意义的约束，泛化能力差，遇到新靶点就“哑火”。

PBCNet2.0 的出现，正是为了打破这个“三角难题”。 

技术内核：PBCNet2.0 凭什么更强？ 
  
  
PBCNet2.0 并非简单的版本迭代，而是一次从底层逻辑到数据规模的全面进化。 

#### 1\. 笛卡尔张量等变神经网络（Cartesian Tensor-based E(3)-equivariant GNN） 

这是 PBCNet2.0 的“灵魂”。不同于前代产品依赖预定义的物理势函数，2.0 版本直接从 3D 空间几何出发。它将原子间的相互作用分解为标量（Scalar）、向量（Vector）和张量（Tensor）。 

这种处理方式能够完美捕捉蛋白质口袋内复杂的对称性和空间方向性，让模型“读懂”分子在三维空间中的真实受力与相互作用模式。 

#### 2\. 从 60 万到 860 万：暴力美学下的“缩放法则” 

深度学习的威力源于数据。PBCNet2.0 遵循“缩放法则（Scaling Laws）”，将其训练数据集扩展到了惊人的 860 万个蛋白质-配体对。 

* 覆盖 28 万个 独特小分子。
* 涉及 1122 个 不同类别的蛋白质靶点。

这种海量数据的灌溉，赋予了模型极强的零样本（Zero-shot）预测能力，即使是面对从未见过的靶点，也能给出极具参考价值的预测。 

#### 3\. 孪生网络架构：更懂“差之毫厘” 

PBCNet2.0 采用孪生神经网络架构，专门针对“相对结合亲和力”设计。它通过同时输入两个相似分子的结合姿态，精准捕捉它们在能量上的微小差异（ΔΔG）。这正是药物化学家在优化分子活性时最关心的核心指标。 

**实战表现：数据不会撒谎** 
  
  
在多项基准测试和实际靶点验证中，PBCNet2.0 展示了令人惊叹的性能： 

* 性能跨越： 在标准的 FEP 测试集上，其预测精度较一代提升了 18%，相关性系数ρ 达到 0.67，已经跨入了与高昂的 FEP+ 商业软件同台竞技的门槛。
* 效率奇迹： 在模拟真实研发场景时，PBCNet2.0 的介入使结合亲和力的优化效率提升了 718%。原本需要数月才能完成的分子进化过程，现在被压缩到了数周甚至数天。
* 资源节省： 相比传统的高精度物理计算，PBCNet2.0 减少了约 41% 的计算资源消耗，真正实现了“既快又准且省”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOj2vbYqZGyoSWuKkibOVNJSicoOHaX4yd43ibQrE9lEv7z4RWCwMEBCozMQn0QE1aSKr15zFGCqg1Flg/640.png)

**惊喜发现：涌现的“耐药性预测”能力** 
  
  
在研究过程中，团队发现 PBCNet2.0 展现出了一种非凡的“涌现能力”——蛋白质突变后的亲和力预测。 

即便在训练阶段并未专门针对蛋白质突变数据进行强化，PBCNet2.0 依然能够准确预测因口袋残基突变（如耐药性突变）导致的药物活性丧失。这一特性对于开发抗肿瘤药物、抗病毒药物等极易产生耐药性的药物具有不可估量的临床前价值。  

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOj2vbYqZGyoSWuKkibOVNJSic0fskjOIV0pTibSlBibaw0wH9cnasgnhw6lPLl1NNunqiagAfWeJUCfh2g/640.png)

参考来源

https://www.biorxiv.org/content/10.1101/2025.06.04.657800v3 

**SciMiner 平台集成：您的云端 AI 实验室** 
  
  
现在，您无需配置复杂的本地环境，也不必购买昂贵的算力集群。通过 SciMiner 平台，您可以直接调用 PBCNet2.0 的强大算力：

* 一键上传： 支持 PDB 蛋白受体与 SDF 配体文件的快速导入。
* 多参考分子策略：支持设定一个或多个具有已知活性数据的分子作为参考。通过“多点锚定”消除单点实验数据偏差，显著提升一系列新分子在预测时的稳健性与一致性。
* 可视化交互： 在 SciMiner 优秀的 UI 界面下，直观查看分子结合姿态与评分结果。
* 批量计算： 依托 SciMiner 底层的分布式架构，支持成百上千个分子的并行评估。
* 结果导出： 自动生成预测报告，助力您的实验方案决策。

输入界面

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOgkMzBhia10gcmrZ5ZhDYnNzP9V5jWpLIoXRJD4HJ7UJ2iax7oEWOhicyzjdPZAzdNfNtLlSKkA9cqDw/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/JRd5vo3IIOgkMzBhia10gcmrZ5ZhDYnNzxzLZemYsoMGKZNf0un8fMD2X7ocpISxn75mU4onBw6x23xeop8XkKQ/640.gif)

输出界面

PBCNet2.0 在 SciMiner 的部署，旨在为科研人员提供更具性价比的高精度筛选工具。通过将深度学习的泛化能力与物理空间的几何约束相结合，我们希望帮助药化专家和计算科学家在分子优化的盲盒中，找到更清晰的路径。

点击下方链接，立即在 SciMiner 平台开启您的 PBCNet2.0 亲和力预测之旅！

立即体验：https://sciminer.tech/utility?tool=PBCNet%202.0

结果示例链接（免登录查看）：https://sciminer.tech/share?id=19839644-c0f0-491f-bae8-818e216f2988&type=API\_TOOL

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOj2vbYqZGyoSWuKkibOVNJSicsAdgpe0MVb5U8ShUbEMqhoQ1Vq4ejrpHlP4URT4dvmXEXkYHE2nZCA/640.png)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhjk0xxKKibZ7B721J3CPIp4dHy1ic63862A0PIIXjt5ibVbIBcXN2VErxhVq7NIicb7Bo6m0A0zVyzkg/0.png) 

 SciMiner科学矿工 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhjk0xxKKibZ7B721J3CPIp4dHy1ic63862A0PIIXjt5ibVbIBcXN2VErxhVq7NIicb7Bo6m0A0zVyzkg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
