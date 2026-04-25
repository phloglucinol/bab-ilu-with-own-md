---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247484032&idx=2&sn=ccdee5bdda15be01c0fccc6ceb19a6ad
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247484032&idx=2&sn=ccdee5bdda15be01c0fccc6ceb19a6ad
source_domain: mp.weixin.qq.com
title: JCIM 2025 &amp; OpenADMET | 当 ADME 预测走出“盲盒”：从盲测教训到开源军火库
author: 
published_at: 
fetched_at: 2026-04-25T02:04:00Z
extractor: wechat_worker
content_hash: e7d70cec108c3f55d04df7221ba749b88dae02c6f19b4f563cf46a95d835e8d1
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/pUZwvicbdez6tp85UhKr7AMEkLbglHUekTFb5jBj9LSsG4UZPe1U6rboiaSCgfL4puKUH7zaf6NbC7ibPXv6n8Yrw/0.jpg) 

# JCIM 2025 & OpenADMET | 当 ADME 预测走出“盲盒”：从盲测教训到开源军火库

原创 陷入鞍点 陷入鞍点 [ 陷入鞍点 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

编者按： 如果说 2024 年是 AlphaFold 3 称霸结构预测的一年，那么 2025 年初的这两个信号（Novalix 盲测报告 & OpenADMET 首发模型）则狠狠地把我们拽回了药物研发的泥潭——ADMET 预测。

现在的局面很有趣：一方面，Novalix 的盲测告诉我们“别迷信大模型，随机森林依然能打”；另一方面，OpenADMET 刚刚发布的基准测试却在说“深度学习在 ADME 上大有可为，但泛化性是个深坑”。

作为一个在工业界摸爬滚打多年的算法老兵，今天我不讲虚的。我们将结合这两份重磅材料，聊聊同一个话题：在一个数据由于“少、脏、偏”而充满迷雾的领域，我们到底该怎么构建靠谱的 ADME 预测引擎？

---

Part 1\. 战场传来的消息：Novalix 盲测的“当头棒喝”

首先，让我们回顾一下 JCIM 2025 封面文章（Novalix 盲测报告）带来的残酷真相。这不仅仅是一场比赛，更像是对当前 AIDD 技术栈的一次“体检”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Hk1BhEwZmyiaqgshd73AsvRLf5v6CMyiczxoXJficbej2Qp2t8C2goXMuIJ5BETo3VAlINV9iaTsiawkEHEHpWibn9MQ/640.png)

这篇文章干了什么？

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Hk1BhEwZmyiaqgshd73AsvRLf5v6CMyiczPqVnfpZWRVRMUiaZb1Q9qAnXbiaFyJUrcDEproicVvHJUzmtZSOfN9QrA/640.png)

得到了什么结论?

1.活性预测：姜还是老的辣

在 SARS-CoV-2 Mpro 的活性预测任务中，随机森林（Random Forest）配合经典的 ECFP4 指纹，依然稳稳压制了 MolFormer、ChemBERTa 等预训练大模型。

* Why? 因为活性往往依赖特定的子结构匹配（Substructure Matching）。在微调数据稀缺（Few-shot）的情况下，大模型那些高维的 Embedding 反而不如简单的“数指纹”来得直接。

2.ADME 预测：深度学习的“甜蜜点”

但在 ADME（如代谢稳定性、透膜性）任务上，风向变了。

* TabPFN（一种针对表格数据预训练的 Transformer）和 ChemProp-MT（多任务 GNN）开始屠榜。
* Insight：ADME 数据往往是非线性的（涉及复杂的酶-底物相互作用），且不同 ADME 任务之间存在内在关联（比如 LogD 和透膜性）。这正是深度学习擅长的领域——捕捉非线性映射和利用多任务学习（Multi-Task Learning）进行知识迁移。

3.致命盲区：立体化学

最让人背脊发凉的是那个 Failure Case：两个互为对映异构体的分子，活性差 1000 倍，但所有基于 2D Graph 的模型都预测它们活性相同。

* 教训：2D 模型永远看不见手性悬崖。 只要你还在用 SMILES 建模，就必须接受这个天花板。

---

Part 2\. 援军抵达：OpenADMET 的“开源军火库”

就在大家对着 Novalix 的结果陷入沉思时，OpenADMET 团队发布了他们的 Inaugural Model Release。这不仅仅是一组模型权重，更是一套工业级的基准测试（Benchmarking）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Hk1BhEwZmyiaqgshd73AsvRLf5v6CMyicz0BZ4TKStEXvRXFeVqzQUKnuichPOoWuTqjb1ZdUa4kTP7R32IZsTPicA/640.png)

OpenADMET 专注于两个最让药化头疼的性质：CYP3A4 抑制（药干掉酶）和 PXR 诱导（药激活核受体，导致酶过量表达）。让我们看看他们发现了什么，以及这些发现如何验证了 Novalix 的结论。

1.承认现实：数据不仅少，而且“脏”

OpenADMET 团队非常坦诚。他们基于 ChEMBL 清洗出了 4800 个 CYP3A4 数据点和 600 个 PXR 数据点。

* 对比工业界：这比大药企内部的数据库（通常几万到几十万）少了一个数量级。
* 策略：他们使用了 "CheMeleon"（一种预训练版的 ChemProp）和 TabPFN。结果再次印证了 Novalix 的发现——在小样本下，TabPFN 和预训练 GNN 是表现最稳健的选手。

2.泛化性的“恐怖谷”

这是 OpenADMET 报告中最具价值的一张图表（虽然它让人很难受）：

* Random Split（随机切分）：模型 R² 能达到 0.6。看起来还不错？
* Cluster Split（按骨架聚类切分）：模型 R² 直接掉到了 0.1。
* 这意味着什么？ 这意味着如果你只用公共数据训练，遇到同骨架的分子（Me-too），模型还能蒙对；但一旦你想做 First-in-class，去探索全新的化学空间，这个模型的预测结果基本上等于扔硬币。

3.多任务学习（Multitask）是唯一的救命稻草

为了拯救那个可怜的 R²，OpenADMET 最终发布的 Champion Model 是 Multitask CheMeleon。

* 逻辑：既然 CYP3A4 的数据不够，那就把 CYP1A2、2D6、2C9 的数据全拉进来一起练。
* 效果：多任务模型显著优于单任务模型。这再次验证了 Novalix 的结论：在 ADME 这种数据稀缺领域，"借力打力"（Transfer Learning）是必选项。

---

Part 3\. 架构师视角：我们该如何构建实战级 ADME 引擎？

好了，论文读了，模型也下载了。作为一家 Biotech 的算法负责人，周一早上你该怎么干？

以下是基于这两份资料的 Actionable Guide：

步骤一：不要从零训练，学会“站在巨人的肩膀上”

OpenADMET 已经发布了基于 Anvil 框架的预训练模型。

* Do this: 直接下载他们的 CheMeleon 预训练权重作为起点。
* But: 绝对不要直接拿来用。正如 R²=0.1 警告的那样，它在你的专有骨架上大概率会失效。
* Strategy: 使用你的内部数据（即使只有 50 个点）对模型进行 Fine-tuning（微调）。对于小样本，推荐使用 TabPFN 作为 strong baseline 进行对比，它不需要调参，往往能给出令人惊讶的下限保证。

步骤二：建立“置信度”护城河（Uncertainty Quantification）

既然模型在 Out-of-Distribution (OOD) 数据上表现极差，我们必须知道模型什么时候在瞎猜。

* 技术选型：不要只输出一个预测值。利用 Ensemble（集成学习） 或 Dropout MC 方法，输出预测的方差（Variance）。
* 落地策略：在看板上，如果某个分子的预测方差过大，直接标记为“需实验验证”，而不是给药化一个虚假的数值。OpenADMET 的文档里也明确提到了这一点。

步骤三：解决“手性”与“构象”的 Research Gap

这是目前开源社区最大的痛点。Novalix 和 OpenADMET 目前的主流模型都是 2D 的。

* Gap: 遇到手性中心多的分子，或者分子内氢键导致透膜性突变的分子，2D 模型统统失效。
* Emerging Tech:
   * 3D Conformer Ensemble: 尝试引入生成的 3D 构象集合作为特征（如 3D-GNN, SchNet）。但要注意，构象生成的噪声可能比信号还大。
   * Physics-Informed ML: 将物理计算（如简单的 LogD 计算、极性表面积 PSA、甚至快速 Docking 的打分）作为 额外特征（Explicit Features） 拼接到深度学习模型中。这叫“归纳偏置（Inductive Bias）”，能强行纠正模型违反物理常识的预测。

步骤四：拥抱主动学习（Active Learning）

OpenADMET 提到他们将在 2026 年与 Octant Bio 合作引入主动学习。这是解决“数据脏”的终极方案。

* Shift: 不要被动等待药化给数据。算法团队应该根据模型的不确定性（Uncertainty），主动挑选那些模型“最看不准”的分子去送测。
* Benefit: 这样产生的 100 个数据点，对模型迭代的价值可能超过随机测量的 1000 个点。

---

结语：从“炼丹”到“工业化”

JCIM 的这篇论文和 OpenADMET 的发布，标志着 AIDD 进入了一个\*\*祛魅（Disenchantment）\*\*的阶段。

我们不再幻想有一个“万能大模型”能解决所有问题。相反，我们开始承认：

* 数据比算法重要（SALI 清洗、主动学习）。
* 场景比指标重要（Random vs. Cluster Split）。
* 流程比单点重要（TabPFN + Fine-tuning + Uncertainty）。

如果你正在搭建 ADME 平台，请记住：最好的模型不是 R² 最高的那个，而是最诚实地告诉你“我不知道”的那个。

  
参考链接：

* JCIM 2025 | Novalix Blind Challenge Paper
* OpenADMET Inaugural Model Release

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7zibiaVPt4xq6YOATjn0icWC4ddwoYnGvBTcJRErwMnMUOEcyS3QnGFMDwQr9DZlWibmFGdvDKY0ao0A/0.png) 

 陷入鞍点 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7zibiaVPt4xq6YOATjn0icWC4ddwoYnGvBTcJRErwMnMUOEcyS3QnGFMDwQr9DZlWibmFGdvDKY0ao0A/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
