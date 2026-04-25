---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzYyMzI1NDI3MA%3D%3D&mid=2247486416&idx=1&sn=7a1c7d948270c5e1d092e644942424df
canonical_url: https://mp.weixin.qq.com/s?__biz=MzYyMzI1NDI3MA%3D%3D&mid=2247486416&idx=1&sn=7a1c7d948270c5e1d092e644942424df
source_domain: mp.weixin.qq.com
title: Science Advances 2026｜分子生成不再只会“硬塞口袋”，SeFMol 在生成过程中调整分子构象
author: 
published_at: 
fetched_at: 2026-04-25T02:03:08Z
extractor: wechat_worker
content_hash: a0fba20ee28a9550771e22d2ab997562c2f43c5338e86d9b3abe80ca713f0397
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/xawOdPt2Qv4lpicy9YGbZBqMLR97Q1n92a0iaWkfusU4x0iaa17IvewZlsJfap0yLEpjGeDe5ZpjAjnZ6owr2cRqEiaGx3c3WnZ2tKqKMSfu2rY/0.jpg) 

# Science Advances 2026｜分子生成不再只会“硬塞口袋”，SeFMol 在生成过程中调整分子构象

原创 徐东，Jonty 徐东，Jonty [ AI药物设计实验室 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

🔔关注我们，每日分享最新的人工智能与生命科学论文～

---

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/xawOdPt2Qv6z37XuU94oToFOJhs5y7NaDv2jxLuYUvCeHlicLplWfgrlW7zdU48X57Q1Y23nU8XLniaC3a4j9dOpx1F1DNvwneAdMa7pTlUI4/640.png)

> “
> 
> 配体进入蛋白口袋后通常会变化，它会转一下、弯一下，换一个构象，再去找更合适的结合姿势。
> 
> 现在很多模型已经能按口袋直接生成分子，但大多还是按“相对刚性的配体”来处理。这样做训练更顺，生成也更快，可一到新口袋，构象调整就不够准。
> 
> SeFMol 解决的就是这个问题：
> 
> 把扩散模型的去噪过程写成马尔可夫决策过程（Markov decision process），再用强化学习去引导“半柔性”构象优化。

## 一眼看懂

* 真实的蛋白-配体结合是动态的，现有很多生成模型还是静态思路。
* SeFMol 分三步走：先学分子和性质的关系，再学口袋和配体的关系，最后用强化学习在去噪过程中调整分子构象。
* 模型把 8 个理化性质作为条件输入，包括 QED（药物相似性定量估计）、SA（合成可及性）、LogP（脂水分配系数）、TPSA（拓扑极性表面积）、HBA/HBD（氢键受体/供体数）、Fsp3（sp3 碳分数）和 ROTB（可旋转键数）。
* 平均 Vina score 做到 -7.23 kcal/mol，SR 做到 11.53%，采样速度做到 0.81 秒/分子。

## 论文做了什么

### 方法

作者先做“刚性训练”，再做“半柔性优化”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/xawOdPt2Qv5gBaJcNq3ApicAchZdvo5OukDyN3ia8KeiadF2OPR1CNckibwiaLW69iaE0ALBHPCwRq7ia7qamicDFdXVKgiaCTjPKibesO5Ub6AZY38icg/640.png)

**图1\. SeFMol 框架总览。**A：整体训练目标；B：刚性训练阶段的两阶段策略；C：强化学习引导的半柔性优化与推理阶段。

第一步，作者在 100 万个没有靶点信息的 Molecule3D 分子上预训练，让模型先学会“分子三维结构—理化性质”这层关系。

第二步，再用 10 万个 CrossDocked2020 蛋白-配体复合物微调，把蛋白口袋条件加进去。底层去噪器用的是 SE(3)-equivariant GNN，专门处理三维几何。

第三步，把扩散模型的去噪过程当成一个逐步决策过程，让策略网络在每一步都微调分子位置。

为了避免策略跑偏，作者还加了 KL（Kullback-Leibler，库尔贝克-莱布勒散度）约束和价值网络。

还有两个细节很关键。

一个是性质引导，论文把理化性质直接作为条件输入，用来缓解终点奖励过稀的问题。另一个是快速采样，作者把采样步数从 1000 步压到 50 步，速度提升 20 倍。

### 结果

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/xawOdPt2Qv54FqlTKQzPEl5tw3TvlJxzYARwIW7kz744ctvgq6r9kvic9xByZYQSdCd5UUQareYUsOOHajD1dV8ZNYM9rLqiaJmiav9X37ga0w/640.png)

**表1\. 不同方法在多项指标上的性能对比。**↓ 表示越小越好，↑ 表示越大越好。

第一，SeFMol 的平均 Vina score 是 -7.23 kcal/mol，优于参考分子的 -6.36，也优于所有基线。

第二，High affinity 达到 68.7%，也就是很多口袋里都能生成比参考分子结合更强的结果。

第三，QED 做到 0.63，是表里最高。

第四，Lipinski 规则满足度也很强。SA 和多样性处在中上水平，论文整体表现最强。论文后面还专门分析了分子量，SeFMol 在分子量接近参考分子的前提下拿到了更高亲和力。

除了主表，文章还有几组结果。

* **采样效率更实用。** SeFMol 平均 0.81 秒生成一个分子，完成率 98.3%。对比之下，MolCRAFT 需要 1.41 秒，TargetDiff 和 DecompDiff 分别要 34.28 秒和 61.89 秒。
* **化学合理性更强。** 论文定义的 SR 达到 11.53%，比 IPDiff 高 8.09 个百分点。
* **构象和相互作用更靠谱。** SeFMol 的 Vina score 和 Vina dock 相关系数做到 0.95，说明模型直接生成出来的构象就比较像可行结合模式。在相互作用类型分布上的 JSD 做到 0.1401，和 TargetDiff 并列最好。
* **对真实靶点也能工作。** 在 CDK2 和 ROCK1 两个真实治疗靶点上，作者展示的代表性 SeFMol 分子拿到了更低的 Vina dock，并复现了部分已知相互作用。

## 我们的看法

过去很多方法更像先生成，再看能不能 dock 上去。SeFMol 在生成时就把 binding mode（结合模式）往目标方向推。

另外，作者同时追亲和力和性质控制。论文里 PT（预训练）和 PG（性质引导）的消融说明得很清楚：少了性质先验，强化学习很容易被稀疏奖励带偏。把化学先验和 RL 放在一起，模型更稳，也更像真实的药物设计流程。

还有 50 步采样和 0.81 秒/分子的速度，让这套方法更像一个能接进实际筛选流程的工具，而不只是“指标好看”的模型。

## 边界

* 它做的是 **semi-flexible（半柔性）** 生成，主要调整的是配体构象。蛋白口袋本身还是固定条件。更完整的蛋白-配体协同适配，这篇文章还没有展开。
* 论文自己也承认，PG、PT 和 SFRL 会把模型推向高分结构附近。这样能换来更好的亲和力和性质，同时会牺牲一部分多样性。这是一个很典型的 exploitation（利用）和 exploration（探索）平衡问题。

## 论文信息

* **标题**：Steering semi-flexible molecular diffusion model for structure-based drug design with reinforcement learning
* **作者**：Xudong Zhang, Sanqing Qu, Fan Lu, Jianmin Wang, Zhixin Tian, Shangding Gu, Yanping Zhang, Alois Knoll, Shaorong Gao, Guang Chen, Changjun Jiang
* **机构**：同济大学、上海市第一妇婴保健院临床与转化研究中心、上海创新研究院、延世大学、加州大学伯克利分校、慕尼黑工业大学等
* **期刊**：_Science Advances_（2026）
* **DOI**：10.1126/sciadv.ady9955
* **GitHub**：https://github.com/ispc-lab/SeFMol

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zulfczIufvIwLEibl0DgDqCZOk0tQUYszF9Zpg9y9qKrVebN6ICJMUDcTHI3xMCzjFWXVyqEmtdlckTp8llHibiaQ/0.png) 

 AI药物设计实验室 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zulfczIufvIwLEibl0DgDqCZOk0tQUYszF9Zpg9y9qKrVebN6ICJMUDcTHI3xMCzjFWXVyqEmtdlckTp8llHibiaQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
