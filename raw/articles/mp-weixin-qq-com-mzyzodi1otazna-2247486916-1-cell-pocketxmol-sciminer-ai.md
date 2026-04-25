---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzYzODI1OTAzNA%3D%3D&mid=2247486916&idx=1&sn=8fa7b4c2b177cfe27f806e7b86eff6be
canonical_url: https://mp.weixin.qq.com/s?__biz=MzYzODI1OTAzNA%3D%3D&mid=2247486916&idx=1&sn=8fa7b4c2b177cfe27f806e7b86eff6be
source_domain: mp.weixin.qq.com
title: 登顶《Cell》！从“碎片化”到“大统一”：PocketXMol 全原子生成模型上线SciMiner，定义AI药物研发性能新高度
author: 
published_at: 
fetched_at: 2026-04-25T02:03:33Z
extractor: wechat_worker
content_hash: 0165c5d547244d5a4390ace0980ef74eefbda9e2e434b402b1320e9225e2cc4a
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/osubyajR6xica4bSYLYMMI7b4ic4PJ25Z8ABrnAGamVqrzib6yqk59iadhgQOWJNVOMor3ib56zq3VocHDRVlxGwGCgFTzEZlTNkIfibjECcdribTQ/0.jpg) 

# 登顶《Cell》！从“碎片化”到“大统一”：PocketXMol 全原子生成模型上线SciMiner，定义AI药物研发性能新高度

原创 SciMiner小助 SciMiner小助 [ SciMiner科学矿工 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在 AI 药物研发领域，我们正在经历一场从“专用模型割据”到“大模型跨尺度统一”的范式革命。近日，清华大学、北京大学及中国科学院的科研团队在顶刊 《Cell》 发表了名为 “Unified modeling of 3D molecular generation via atomic interactions with PocketXMol” 的重磅论文。该研究不仅刷新了 11 项计算任务的 SOTA 纪录，更打破了小分子与多肽设计之间的技术鸿沟。

作为 AI4Science 领域的深度赋能者，SciMiner 平台已第一时间完成了 PocketXMol 的全功能部署，并将其转化为工业级的生产力工具。

🚀 立即体验：https://sciminer.tech/utility?tool=PocketXMol
  
  
### **深度背景：AIDD 领域的“孤岛危机”与 PocketXMol 的降维打击**

1\. 传统模型的局限：分而治之的代价

在 PocketXMol 问世之前，AIDD 领域长期被“专用模型”统治，这种割据状态带来了三大核心挑战：

* 工具与数据的割据：分子对接（Docking）依赖打分函数和采样；小分子从头设计（De Novo Design）依赖化学信息学的排列组合；多肽设计（Peptide Design）则往往陷入氨基酸序列的黑盒预测。这导致研发工作流断裂，数据难以互通。
* 物理精度的缺失：为了计算效率，许多传统模型将氨基酸简化为“点”（如只看 Cα 原子），彻底忽略了侧链原子层面的精细相互作用。这种简化在面对氢键方向性、π-π 堆积等关键非共价相互作用时表现乏力，导致设计出的分子在湿实验中往往面临结合力不足的尴尬。
* 跨尺度挑战：小分子设计关注微观电荷分布，多肽设计关注宏观骨架特征。如何在一个模型中同时兼容两者的特征，曾被认为是难以逾越的技术鸿沟。

#### 2\. PocketXMol 的“底层逻辑”：以原子为共同语言

PocketXMol 的核心逻辑极其纯粹且硬核：它抛弃了所有关于“分子类型”的预设偏见，将蛋白质口袋与配体（无论小分子还是多肽）的交互，统一建模为 3D 空间中原子点云的相互作用（Unified modeling via atomic interactions）。

通过创新的几何神经网络（Geometric Neural Network），PocketXMol 能够像高精雷达一样扫描蛋白口袋的每一个几何凹槽。它理解的不再是“氨基酸”或“化学键”，而是底层的物理化学概率分布。这种原子级精度使其不仅能画出分子，更能“生长”出符合物理逻辑的分子，彻底告别了盲目拼凑的时代。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/osubyajR6x9EzVur1niaAAmbZLwLZJty4eTDqoobf5v25USowt24xuPc3QqyMTeyMv2oXnsib8icQNaasf8mKFulyUGDfU8dBTzHhF5eDXE7dU/640.png)
  
  
## 技术解密：PocketXMol 的“三大利剑”与核心竞争力

为什么 PocketXMol 能在竞争激烈的 AI4Science 领域脱颖而出？这源于其在算法架构上的三大突破。

#### 1\. 原子级精度的全能视野

不同于以前的模型可能只看氨基酸的 Cα 原子，PocketXMol 是 All-atom（全原子） 建模。这意味着它能精确捕捉到多肽侧链的旋转异构体（Rotamers）如何与蛋白口袋的氨基酸侧链进行空间适配。这种精度对于预测复杂的蛋白-蛋白相互作用（PPI）抑制剂至关重要。

#### 2\. 强大的非标准氨基酸（NAA）泛化能力

在现代药企的多肽药物开发中，引入非天然氨基酸以增强稳定性、降低酶解速度已成为常态。PocketXMol 在处理非标准氨基酸（Non-standard Amino Acids）时表现极其出色。论文数据显示，它能够支持多达 454 种 NAA 的建模。由于它理解的是原子间的物理规律，而非死记硬背氨基酸序列，因此它不需要针对每一种新结构重新训练，展现了极强的 Zero-shot（零样本）迁移能力。

#### 3\. 从计算到湿实验的闭环验证

不同于许多仅停留在理论阶段的 AI 模型，PocketXMol 在 Cell 论文中展示了极其震撼的实战成果：

● Caspase-9 抑制剂：精准度媲美商业药物

研究团队利用 PocketXMol 设计出的候选分子 D12，在细胞实验中表现出与目前临床在研或商业抑制剂（如 Q-VD-OPh）相当的抑制效力。更重要的是，该分子表现出了极高的选择性，显著降低了脱靶毒性，这标志着 AI 生成的分子已具备直接进入临床前研究的潜力。

● PD-L1 靶向多肽：突破命中率极限

针对免疫检查点 PD-L1，研究团队合成了 382 种由 PocketXMol 设计的多肽。实验结果显示，其中有 15 种候选肽的结合亲和力（KD）达到了惊人的 10^-8 M 级别。这一命中率远远超过了传统随机文库筛选的效率。在体内（In Vivo）实验中，这些多肽展现了显著的肿瘤靶向和富集效果。
  
  
## SciMiner 平台接口详解：将顶刊成果转化为你的生产力

为了让科研人员从繁琐的算法环境配置中解脱出来，SciMiner 团队对 PocketXMol 进行了工业级的优化与封装，推出了三个核心 API 接口，覆盖了药物研发的核心场景。

#### 接口一：精准分子/多肽对接 (Dock a small molecule or peptide)

* 功能： 将已知的小分子、线性肽或环肽精准“放置”入蛋白质结合口袋。

* 技术亮点：相比于 AutoDock Vina 等传统工具，PocketXMol 在处理具有几十个可旋转键的高柔性多肽时，展现了压倒性的构象搜索能力。其在 PoseBusters 验证集上的表现（82.5% 成功率）足以比肩 AlphaFold 3，但在特定靶向口袋的灵活性上更胜一筹。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/osubyajR6x8iczfvtFORpUzvkXolz9ekKjfiaB3OcAshiaia0SBX6b7uODrcQIMeeFAsEZrlWNjK9BHIZGn8DP1McgVQbUDselLPdniaW8thseWw/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/osubyajR6x8lrXrJc4451jJPNWor106wEyrZeFcV8w7K7icxB2zC8gwoTicddTNXfpOZ0eExyFuqskCXEfs2JsV8hdH4B3AF8HtjwibibxvmLg0/640.png)

点击查看 SciMiner 运行结果展示： 

小分子对接：https://sciminer.tech/share?id=24bba229-877f-4292-a027-dec2fed6149d&type=API\_TOOL

多肽对接：https://sciminer.tech/share?id=5c1d8c92-f401-4420-8f2a-3ecfc3705d1c&type=API\_TOOL

#### 接口二：小分子从头设计 (Design novel drug-like molecules de novo)

* 功能： 针对特定靶点，从无到有生成全新的类药小分子。
* 技术亮点： 生成过程实时兼顾了类药性（Lipinski's Rule of Five）与合成可及性（SA Score）。它不是简单的结构堆砌，而是在口袋空间内依据物理分布“自生长”。
* 价值：帮助药企有效避开现有专利保护区，在全新的化学空间（Chemical Space）中寻找高活性的骨架。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/osubyajR6xicrOI0RRkkE8F3j1Jibc7AhV9GiaoXia9sN2XFaBkOI5yUGEqQL5rtYy2Fb44TQcicFZjpLccbGgI69hprrZZpazsQEA8gYphB4sicQ/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/osubyajR6x8vBjOEqXbt95AO2rbpzOamzNNkAtHQtAqcCL2Lu9ljjoqJqVUnIrGI5scDb7ZJibGMRFBk7qtyF2OwJ47EENWoSjZGD0DNicaXA/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/osubyajR6xibytzMI0Z3erF6mbnEIgb6os7HzRcsCltCnjohuY4YQbA8oPlOdGfKrQTN0x4M75KlaoKEjoMWk6aPiaOXGaKJ0b848zdHkHm3Y/640.png)

#### 点击查看 SciMiner 实时运行结果展示： 

小分子生成：https://sciminer.tech/share?id=669d6782-3793-4ec6-96c8-b6343d202113&type=API\_TOOL

#### 接口三：多肽全能设计中心 (Design peptides for a protein binding pocket)

这或许是目前市场上最强大的多肽设计工具，支持：

* De Novo Design：基于口袋生成全新多肽序列与结构。
* 反向折叠 (Inverse Folding)：给定特定的主链骨架，反推最优的氨基酸序列。
* 侧链优化 (Side-chain Packing)：在序列和骨架结构确定的情况下，微调侧链 3D 构象以极大化增强结合能。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/osubyajR6xib6GQcHA5sjpsNVMibiap1HPQniaIlpAhdUasLblh3M7PF2cCEBoAz8B88eQ99UGYiaSSENlPsSyXlVqic5er3HSNBsueWjtx7FjicmE/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/osubyajR6x9AOcDhYQSKt6wrcl3wlNVeHgbSejNeqT7UVtsDa53qAlsscVOd7UWPjxCXCX2bPsnvlSukEtKDmbJicwEt2J2SRuB6gMWJRaN0/640.png)

点击查看 SciMiner 实时运行结果展示： 

多肽生成：https://sciminer.tech/share?id=5cbf022c-7640-44f6-97a6-60079b3967ae&type=API\_TOOL

多肽逆折叠：https://sciminer.tech/share?id=ac77d1e7-4145-48e1-a80e-5ab0ce5525d5&type=API\_TOOL

多肽侧链优化：https://sciminer.tech/share?id=bea2ecdf-44ae-40ad-8182-be1e51db1540&type=API\_TOOL
  
  
、
  
  
## 让 AI 成为科学家的“第二大脑”

PocketXMol 的出现，标志着药物设计正从“大海捞针”般的盲目筛选，转向“按图索骥”般的精准生成。SciMiner 的使命，就是将这些处于金字塔尖、改变行业游戏规则的技术，转化为每一位科研人员都能轻松驾驭的利器。

无论您正处于先导化合物发现陷入僵局的时刻，还是在寻找更具稳定性的多肽改造方案，PocketXMol 都能为您提供前所未有的灵感与证据支持。

未来已来，原子级设计的终极奥义已在 SciMiner 开启。 诚邀各位同仁点击下方链接，开启您的 AI 设计之旅。

https://sciminer.tech/

---

#### 关于 SciMiner

我们致力于通过人工智能驱动药物研发的数字化与智能化转型。作为 AI4Science 领域的领航者，SciMiner 始终走在行业前沿，通过将尖端 AI 算法转化为简单易用的工业级生产力工具，为全球生物医药企业构建起高效、精准的数字化研发闭环，助力科研团队在复杂药物开发中实现突破。

联系我们： 

邮箱：sciminer@protonunfold.com

视频会议预约：https://uqjwb92lf61.feishu.cn/scheduler/3c775aa5445613ae

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
