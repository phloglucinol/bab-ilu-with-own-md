---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzE5MTc4NTcxMA%3D%3D&mid=2247487086&idx=1&sn=a99a6b1e27cb880bcb702c7d9080a69c
canonical_url: https://mp.weixin.qq.com/s?__biz=MzE5MTc4NTcxMA%3D%3D&mid=2247487086&idx=1&sn=a99a6b1e27cb880bcb702c7d9080a69c
source_domain: mp.weixin.qq.com
title: Nat. Commun. | 一种可扩展的强化学习方法用于筛选超大肽库以发现生物活性肽
author: 
published_at: 
fetched_at: 2026-04-25T02:04:15Z
extractor: wechat_worker
content_hash: c989a09c72f134a3740c6a242a15819d135a904ea8a3ee5b22e58d6168d1e8a6
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9mx4RKVeNJIfJQu6x0YkcYbMTkxnoFSU6vXp1DNHjmeOZeBenykOGCw/0.jpg) 

# Nat. Commun. | 一种可扩展的强化学习方法用于筛选超大肽库以发现生物活性肽

原创 DrugOne DrugOne [ DrugOne ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

DRUGONE

发现具有高生物活性的短肽对药物开发、免疫调节和细胞通信研究具有关键价值，但从超大规模肽库中寻找候选肽往往面临高昂成本和低效率。研究人员提出一种基于强化学习的可扩展筛选框架，通过模拟肽结构与细胞受体的相互作用并结合自适应探索策略，有效在海量序列空间中识别具备显著结合活性的肽段。该方法在多种不同评估体系中显著优于传统穷举或基于规则的搜索策略，并在真实实验验证中发现多条具备功能性的新型活性肽，为高效肽类药物筛选提供可扩展解决方案。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9GyW15DvibFibZaqLtcy9nHcre6pDaYHB0TMKJ4ySDBxoNw1YUoOtcJVQ/640.png)

肽分子因其结构灵活、易于设计且可快速合成，逐渐成为药物与功能分子的重要来源。然而，自然肽序列空间极为巨大，即便长度仅为 12–20 个氨基酸，其可能组合数量依然超过天文规模，使得通过传统方法全面扫描成为不可能。现有策略如实验高通量筛选、结构预测、基于规则的算法或遗传算法仍受到搜索效率、成本或对结构依赖度高等限制。研究人员提出的强化学习框架能够在未知序列空间中持续学习、探索与优化，利用奖励信号驱动模型向高活性肽序列聚集，从而在大规模肽库中快速定位潜在生物活性肽。

  
**方法**

研究人员构建了一个多步骤强化学习流程，将每条肽序列视为由多个动作（添加不同氨基酸）构成的决策过程，并通过预测模型评估每个序列与目标受体之间的结合能力。强化学习代理在大量模拟探索中更新策略，以最大化最终序列的活性得分。研究人员将序列生成、结合能评估、策略更新、候选筛选构建为统一框架，使模型能在无需完整遍历肽库的情况下高效识别潜在活性肽，并最终结合实验验证筛选结果。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9O9AjUrVWWaavsupSPFXl2Yib6ThxpQ8eWfd9t19IT8sd5icmAbKLSQRQ/640.png)

图 1：框架结构与整体流程示意图

  
**结果**

**强化学习框架实现对大规模肽库的高效搜索**

研究人员首先构建包含数十亿条候选肽序列的虚拟肽库，使用强化学习代理逐步探索并生成具备高结合能力的序列。与随机搜索、基于规则筛选或简单遗传算法相比，强化学习框架能更快收敛于高评分区域，并在探索–利用之间保持有效平衡。在不同受体模型中，该方法均展现出良好的鲁棒性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9aJBHunoiaI1tQDABxmM4ggqV68wYoiajEbRKoKInmAiaQO9770BsCAFTQ/640.png)

图 2 ：不同搜索策略性能对比

  
**序列空间逐渐集中到高活性区域**

在强化学习的迭代过程中，研究人员观察到模型生成的肽序列逐步从全局随机分布收缩至特定模式的高活性区域。模型不仅优化氨基酸组成，还能自动识别关键结构模式，例如疏水–带电残基的交替排列、对折结构的形成倾向等。相比传统搜索，强化学习能够捕捉到更复杂的序列–结构–功能关系。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9yRLt2jxFw9jvc6TVuQ5KZ7bOI9gs6xHMQbKKCQkd0S0TCZKicBgF4Kw/640.png)

图 3 ：序列分布收敛趋势图

  
**在模拟评估中的显著性能提升**

研究人员使用多种预测模型评估强化学习生成的序列，在不同受体靶点、不同打分体系，以及多种执⾏条件下测试框架性能。结果显示：

* 强化学习生成的肽平均得分显著高于随机与基于规则方法；
* 模型能够持续提升序列的稳定性、可折叠性与结合能力；
* 在早期迭代阶段即可获得大量候选肽。

强化学习框架在所有模拟实验中均表现稳定且可扩展。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya955ibeAR2To08lZC8fFp9B4QT3ExQibXZYW3dgvYpXYX193ichxacH5lCA/640.png)

图 4 ：模拟打分分布与性能曲线

  
**框架可自然扩展至不同长度与不同受体**

研究人员进一步验证框架对不同长度、多类型受体、多模型评分体系的兼容性。通过调整奖励权重与搜索深度，该框架能够成功适配短肽、中长肽乃至环肽设计场景。其多样性显著优于传统生成模型，表明强化学习方法具备跨场景迁移能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9mHU6zugzVeAvruLftpibVFCkyVciaNib9vmxYVZCIiaX6dQk4rNZeZJUMQ/640.png)

图 5 ：多受体、多长度序列迁移性能图

  
**与现有序列生成方法的对比**

研究人员将强化学习框架与变分自编码器、扩散模型、遗传算法等常见生成式模型进行对比。结果显示：

* 强化学习方法更擅长在高维搜索空间中持续提升序列质量；
* 生成肽的活性预测分数最佳；
* 在等量计算资源下能发现更多的高活性候选序列；
* 生成序列的结构多样性与潜在功能性更强。

强化学习方法在多维指标上的综合效果更优。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9xY62UpibpKzRj6ZNFhTQoCiadpLsd7ibWs9Lqib0JmCSewTnWs9hiaFabdg/640.png)

图 6 ：与其他生成模型的整体性能比较

  
**实验验证证明生成肽具有实际活性**

为了进一步验证模型的有效性，研究人员挑选部分评分最高的序列进行合成与湿实验检测。实验结果表明：

* 多条由强化学习生成的肽具有显著结合活性；
* 部分肽表现出比现有参考肽更强的功能；
* 活性结果与预测模型的趋势一致；
* 实验结构分析显示强化学习生成的序列确实形成特定关键结构。

这些结果充分证明该方法不仅能在模拟中表现优异，也能在真实实验体系中识别新型活性肽。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9Pyg3kibpN3FHwc4TzJIhL7nHastbwxufvJa7Z13ibpTmrLsVkCYD9ibyw/640.png)

图 7 ：实验测定活性与模型预测的对比

  
**活性肽结构分析揭示优选模式**

研究人员进一步分析了实验验证的高活性肽结构，发现强化学习生成的肽往往具有以下特征：

* 关键残基在三维空间中的排布呈现特定模式；
* 肽链倾向于形成局域束缚结构；
* 多数活性肽呈现疏水/带电残基交替排列；
* 关键结合残基出现高频共现模式。

这些结构规律为未来的肽类药物设计提供重要启发。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9nmmUHkkibZc8xwWpLOV96rL0hcsQk9kEHsE6LzV8FkCVmtSzm2QaSXg/640.png)

图 8 ：高活性肽结构与残基分布示意

  
**全流程可扩展、可自动化且适合工业级探索**

研究人员展示该强化学习框架可以并行执行、多 GPU 扩展、对极大肽库进行自动化探索，使其具备工业应用潜力。框架可集成到药物发现流程中，实现：

* 海量候选筛选；
* 持续优化序列；
* 自动生成高潜力活性肽；
* 大幅减少人工干预与实验成本。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gPfmtzaGKdJ3UHyyLVBPya9SZYrkkZ6gX5iaicibibA7ibPVgz9Cx3cuXib0rGItQHkEQ3qWDllD55ldLZg/640.png)

图 9 ：可扩展并行运行与工业级流程示意图

  
**讨论**

本研究提出一种可扩展、自动化的强化学习框架，能够在巨大且复杂的肽序列空间中高效识别潜在生物活性肽。与传统搜索方法相比，该方法具有显著优势：搜索效率高、可迁移性强、可扩展到不同受体与肽长度，同时能够处理高维非线性序列–结构–活性关系。真实实验验证进一步证明强化学习生成的肽不仅具备高预测分数，也具有实际功能。

  
该方法为肽类药物筛选、免疫肽设计、信号肽研究等领域提供强大工具，未来可通过结合结构预测模型、实验高通量平台和更强的策略学习机制，实现从序列生成到实验验证的端到端自动化活性肽发现流程。

整理 | DrugOne团队

  
**参考资料**

  
Pandey, M., Foo, J., Massah, S. et al. A scalable reinforcement learning approach for screening large peptide libraries for bioactive peptide discovery. Nat Commun (2025). 

https://doi.org/10.1038/s41467-025-66748-y

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/mS8qdZ3O8bgdeoYb8GbWMEQtibvyWMWd4ibMHwnXR3p2ib7OFjXc5270g3H1H58WIiclWBQibtJZHIUtWBGcl2czITw/640.gif)

**内容为【DrugOne】公众号原创**｜转载请注明来源

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNehllibjzmuk4oLoB5rbwiaptSMEyFTTvTGzKpWggLwMXaOg5D9z1CFfdjdkorM4IHicxibkXEAe2IPA/0.png) 

 DrugOne 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/jwaic6a7a9gNehllibjzmuk4oLoB5rbwiaptSMEyFTTvTGzKpWggLwMXaOg5D9z1CFfdjdkorM4IHicxibkXEAe2IPA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
