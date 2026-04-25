---
type: raw_article
source_url: https://mp.weixin.qq.com/s/btaPY-duLXtR8wUphRF9sw
canonical_url: https://mp.weixin.qq.com/s/btaPY-duLXtR8wUphRF9sw
source_domain: mp.weixin.qq.com
title: 【First-in-class药设系列】物理-人工智能双驱动的蛋白质设计
author: 
published_at: 
fetched_at: 2026-04-25T02:04:26Z
extractor: wechat_worker
content_hash: 03f53ac40e52ec3dc9ae55934fa1acaed7de27d1cd478eb174225ed1915ab7e2
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeOO9YR2mHlFF8WAZ3D0OLrAKMYpeYAo2rtgSuGpyXnahozBIqVXT4Usw/0.jpg) 

# 【First-in-class药设系列】物理-人工智能双驱动的蛋白质设计

原创 宋煜承泽 & 张健 宋煜承泽 & 张健 [ 分子设计 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在蛋白质工程领域，蛋白质语言模型近年取得了快速进展。它们借鉴自然语言处理的理念，把氨基酸序列视作信息载体，通过在大规模进化序列上训练，能够学习序列、结构与功能之间的关系，并被广泛应用于预测蛋白质的活性、稳定性和功能特性。然而，这类模型主要依赖进化数据进行训练。虽然能够隐式地捕捉到结构和功能信息，但它们并未利用过去数十年积累下来的生物物理学知识。这些知识揭示了蛋白质如何通过能量学、结构折叠和分子相互作用来实现功能，是理解和设计蛋白质的核心原理。缺乏这类信息，使得现有模型在面对小规模实验数据或需要外推至未知突变时往往受到限制。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeOPXRBR4xIubB8gt9oO4cLq6BBKdFAfZDLs8Ribm7FNZcuCdnljKoh5ibw/640.png)

针对这些挑战，来自威斯康星大学的研究人员提出了一种全新的解决方案——METL（Mutational Effect Transfer Learning）框架。它的创新之处在于：在模型的预训练阶段引入了分子模拟产生的大规模生物物理数据，让模型在“学语言”的同时，也能“懂物理”。在此基础上，再结合有限的实验数据进行微调，最终构建出兼具统计规律与物理原理的蛋白质语言模型，为蛋白质工程带来了更强的泛化能力和设计能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeOxtZuIy8AKGccE2Dqk1yAPRKJTkVSNSHMiaasxKlv4xHKY9lGVGF8Tug/640.png)

METL框架采用子突变采样策略，即随机生成一个包含 5个氨基酸替换的突变体，使用这个突变体作为“种子”序列。从这个5突变体中，系统地生成所有可能的子突变体。去除重复序列后，重复上述过程，直到生成足够数量的突变体（约20万个）；最终构成一个覆盖 1\~5个突变 的突变空间。METL将稀疏的实验序列-功能数据与密集的生物物理模拟数据相结合，通过学习两者的映射关系，构建一个既懂生物物理规律又能预测实验功能的蛋白质语言模型。这种融合策略有效弥补了实验数据稀缺的问题。整个训练流程分为三部分：1\. 模拟数据生成：每个目标蛋白质生成20万种序列变体，一共选取了148种目标蛋白，即一共3000万左右的突变体序列空间。利用Rosetta进行结构建模，并计算每种结构的55种生物物理属性（如溶剂化能、氢键、范德华力等）；2\. 预训练：以这些模拟数据为输入，训练一个基于transformer的蛋白质语言模型，使其学会从序列预测生物物理属性，从而建立“生物物理感知”的序列表示。3\. 微调：将预训练模型在少量实验序列-功能数据上进行微调，使其能够预测具体的功能指标，如热稳定性、催化活性或荧光强度。在同样的训练流程下，研究团队使用局部与全局两种策略，搭建了METL-Local、METL-Global两类模型。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeOdSKlsarl9b06AfSMMGbW6PTdybiawNq7sl5nDraguibsWck5pHm61Dpw/640.png)

在较小的训练集上，蛋白质特异性模型 METL-Local、Linear-EVE 和 ProteinNPT 始终优于通用的蛋白质表示模型 METL-Global 和 ESM-2。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeO6pauRy8IFKOXNJOFTtLW9DWFCot1hjwvRzFiavUQvacOrmicFH8zfic9w/640.png)

对于通用蛋白质模型，METL-Global 和 ESM-2 在小到中等规模的训练集中保持竞争力，随着训练集规模的增加，ESM-2 通常更具优势。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeOrZe3L5vDKZBzhKdeqZrp5gTChIUkKcw8ic18z6ZwyYwX1fsgjTeP6Gg/640.png)

研究者实现了四个具有挑战性的外推任务——突变、位置、状态和评分以模拟真实的蛋白质工程场景。在突变外推中，METL-Local 与 ProteinNPT 并列第一。位点外推中ProteinNPT 第一（ρ≈0.65），METL-Local 第二（ρ≈0.59）。突变数目外推中，所有监督模型（含 METL-Local）ρ>0.75，线性模型也强（0.77）。分数外推中所有模型普遍掉到 ρ<0.3，唯一例外 GB1 数据集：METL-Local ρ=0.73（最高），METL-Global ρ=0.71，线性 ρ=0.55；其余模型 <0.3。这说明了METL模型对目标蛋白结构的理解与良好的外推性能。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeOPGqeeTz8JIKx3VeNPZnGumJiadjmR3elT2SPm9WAbx0fwLolkOzXu7w/640.png)

因为生成模拟数据比实验数据快几个数量级且成本更低。研究团队想要了解这两种数据来源如何相互作用，以及模拟数据是否可以部分弥补实验数据的不足。例如，一个在 1000 个模拟数据点上预训练、在 320 个实验数据点上微调的 METL-Local 模型，其性能与一个在 8000 个模拟数据点上预训练、仅在 80 个实验数据点上微调的模型相似。 在这个例子中，添加 7,000 个模拟数据点相当于添加 240 个实验数据点；因此，约 29 个模拟数据点带来的性能提升与单个实验数据点相同。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeOtdOOTaicD0m61cPBeNj1s5hiayOuTJK5DwOFG1YdUulO4rTP5XDlS96Q/640.png)

METL采用transformer编码器架构，创新性地引入了基于三维结构的相对位置编码（3D relative positional embedding），使模型能够感知残基之间的空间距离，而非仅依赖序列顺序。即构建一个无向图，0,1,2,3四类最短路径码，以8埃为分界。3D 距离只在“自注意力”里出现——确切地说，只在 Q·K 打分阶段插入作为偏置。这种结构感知的注意力机制有助于捕捉蛋白质折叠和功能的关键空间相互作用。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/F7uydMlgmicLTsnnBIJLCOw5VwO65LqeOdKjaVJaRqtJ94gJPQfCSC6JJz7zoialoHkmc1HdPJnxyFGMMLuXKlHw/640.png)

研究团队构建了“功能特化”概念验证实验，用 GB1–IgG 结合 affinity 数据集做对照，系统地比较了METL-L：只用 GB1 单体 Rosetta 能量项METL-Bind：额外加入 GB1–IgG 复合体结合能量项。他们的模型层架构完全相同，唯一区别是输出头从 55维调整到72 维（METL-Bind 多 17 项结合分数）。研究团队还计算了 GB1 序列中每个残基位置的预测误差，以了解这两个模型是否专注于不同的结构区域。METL-Bind 在大多数残基位置表现更好，并且在预测 GB1-IgG 界面突变效应方面尤为出色。METL-Bind 表现最大改善的残基是谷氨酸 27，这是一个对形成稳定 GB1-IgG 复合物至关重要的界面残基。

 研究者在仅从完整数据集中随机采样的 64 个 GFP 变体上微调了一个 METL-Local PLM。这 64 个采样变体平均有 3.9 个氨基酸替换，其适应度分布与完整数据集相似。然后从零设计 20 条全新序列，送到湿实验室实测亮度。为了探究在小样本（low-N）和极端外推条件下，AI 设计的蛋白是否真的有实际应用潜力。生成荧光蛋白的综合命中率：16/20 = 80 %；随机基线 1/20 = 5 %，与完全随机的对照组相比， METL 设计效率提升 16 倍。并且对唯一亮的随机序列，METL 给出高预测分；其余 19 条随机序列预测分均低。说明设计成功并非运气，而是模型确实识别到突变绿色荧光蛋白结构与功能之间的对应关系。

综上，METL 把“Rosetta 能量”预训练塞进 Transformer，让模型先学会序列-结构-能量的物理语法，再凭极少实验数据微调，便在 low-N、位点外推、正向增强等应用场景对传统进化模型的性能实现追平与超越。在这个实验中，无论是29:1 的“模拟-实验兑换率”与 64→16/20 的 GFP 设计命中率都证明，生物物理先验对小样本的蛋白质工程具有重要的先导意义。

  
参考文献

Gelman S, Johnson B, Freschlin CR, et al. Biophysics-based protein language models for protein engineering. Nat Methods. 2025;22(9):1868-1879\. doi:10.1038/s41592-025-02776-2

  
相关阅读

[1\. 靶向G1-S检查点受损肿瘤的Cyclin A/B RxL抑制剂设计](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI4NDg5MzIwMQ==&mid=2247488812&idx=1&sn=e200d744b0ca62b6fe9001f80e970a82&scene=21#wechat%5Fredirect)

[2\. 可逆转钠通道功能障碍的肽调节剂从头设计](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI4NDg5MzIwMQ==&mid=2247488753&idx=1&sn=a8779e624978f7b7fd8dbb5b49f6ce9c&scene=21#wechat%5Fredirect)

[3\. ](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI4NDg5MzIwMQ==&mid=2247488847&idx=1&sn=8d2dbb5ca7c4074b66a2eee2973d0993&scene=21#wechat%5Fredirect)[基于千万级定制库的双靶标分子设计](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI4NDg5MzIwMQ==&mid=2247488847&idx=1&sn=8d2dbb5ca7c4074b66a2eee2973d0993&scene=21#wechat%5Fredirect)

[4\. 靶向难成药蛋白家族HECT型E3连接酶的变构抑制剂发现](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI4NDg5MzIwMQ==&mid=2247488661&idx=1&sn=ff311d3dd787c5b02397defb7a196b39&scene=21#wechat%5Fredirect)

[5\. Fundemental Res | AI加速药物发现的范式变革](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI4NDg5MzIwMQ==&mid=2247488772&idx=2&sn=6e45071401a4d50a4556514707ba1357&scene=21#wechat%5Fredirect)

[6\. Nat Mach Intell | 张健课题组开发人工智能药物设计技术实现先导分子从头生成](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI4NDg5MzIwMQ==&mid=2247488720&idx=1&sn=9da55a95db9bd76e028a6c85c506f40b&scene=21#wechat%5Fredirect)

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/F7uydMlgmicIjiaLITHPeZo2SfeWJIHJJd6G46gibUQOd0tiaC9Bia2GlMjGSicNO0EZBicLQchvo00BsHsLic6cO3qGicw/0.png) 

 分子设计 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/F7uydMlgmicIjiaLITHPeZo2SfeWJIHJJd6G46gibUQOd0tiaC9Bia2GlMjGSicNO0EZBicLQchvo00BsHsLic6cO3qGicw/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
