---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIwNTE5MzA2Nw%3D%3D&mid=2247501577&idx=1&sn=42965c228d100adf13e4895625238cfb
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIwNTE5MzA2Nw%3D%3D&mid=2247501577&idx=1&sn=42965c228d100adf13e4895625238cfb
source_domain: mp.weixin.qq.com
title: 虚拟筛选 | 溶剂位点预测 | 提升片段对接精度
author: 
published_at: 
fetched_at: 2026-04-24T16:09:41Z
extractor: wechat_worker
content_hash: f37d5658041581de0a5706873975ca656be43ef19856973a163fbb1d014d1de9
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/Xdb0oXibAJhfFMd9OuiaU2HfkzlTVvs8IaDl6O1yHfO4oJat4mIl493pNyyZI2vtCIzfTRlILvQYNrIAYsiam8SmYIdvJ7O42NGDv7l5x4kicJU/0.jpg) 

# 虚拟筛选 | 溶剂位点预测 | 提升片段对接精度

原创 分迪科技 分迪科技 [ 分迪科技 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

近年来，虚拟按需合成库通常以“非枚举化学空间”的形式进行管理，以应对超大规模化合物库的处理需求。化学空间的本质是组合片段空间，由其构建单元（即合成子，分子砌块）与相应反应路径定义。[药物发现 | 超大型化学空间作为药物发现的起点](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwNTE5MzA2Nw==&mid=2247493642&idx=1&sn=a5bc6bb12de19c0eadbbaf5380dc5413&scene=21#wechat%5Fredirect)

  
尽管化学空间的扩大未必提升化学多样性，但不同市售化学空间之间的重叠程度极低。因此，基于化学空间进行分子对接或虚拟筛选，相较于仅筛选库存化合物，更有可能发现新颖且多样的苗头化合物。[药物发现 | what is Chemical Space Docking ?(1)](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwNTE5MzA2Nw==&mid=2247494807&idx=1&sn=734a35dfd06d33ec3689e3e425440e97&scene=21#wechat%5Fredirect)

  
然而，在此尺度下进行穷举式对接（“暴力对接”）在计算上不可行，需采用策略以降低时间与成本。例如，将机器学习整合至对接流程可在保持较高命中率的同时显著压缩计算开销。需注意的是，通过聚类选取库的多样性子集，可能无意中剔除簇内难以预测的活性分子；相较而言，基于已知结合骨架构建靶点聚焦的虚拟库更为有利，已展现出较高的命中率。此外，已知配体的晶体结合模式可用于模板引导的对接程序，已被验证为基于片段药物发现（FBDD）的有效起点。[药物设计 | Chemical Space Docking®](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwNTE5MzA2Nw==&mid=2247501154&idx=1&sn=3d613dcd6df8ce1a1d0c082a79fd84d8&scene=21#wechat%5Fredirect)

  
一种实用策略是直接对非枚举化学空间进行对接，即对相应的合成子（片段）进行对接，从而规避对完整枚举库的暴力对接。初步识别活性合成子后，可通过相应反应路径进行枚举延伸，生成类药物分子子库，并对其进一步对接。此类基于合成子的对接策略已在多项研究中取得成功。结合化学空间对接与晶体学苗头化合物发现的方法，筛选成功率可达约 40%，且整个过程最快可在 9 周内完成。[Genentech | ROCK-1激酶抑制剂 | ChemicaSpace Docking](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIwNTE5MzA2Nw==&mid=2247494925&idx=1&sn=2861175f24b92bb906f4762e02263a99&scene=21#wechat%5Fredirect)

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/icwRwl0DrJQZpYxY1ShiaoWib9ZY3GCEF2tZuoseaBbOopiae5icN9MKMNMop0jDaBsfXWG6BgCQ6rStkvzk4OBrhZg/640.png)

然而，上述方法要求初始片段级合成子对接具备足够准确性，而片段对接与打分精度目前仍是主要挑战。为此，德国美因茨约翰内斯·古腾堡大学的 Kersten 研究团队，围绕溶剂位点预测在片段对接中的作用及其对基于片段药物发现的影响，开展了一项系统的统计学评估研究。

“片段对接”所面临以下具体问题：

（1）对接精度不足：片段分子量小（<300 Da）、结合力弱，对接中易产生多个能量相近的错误结合模式，传统打分函数难以有效区分。

（2）溶剂效应争议：在对接中引入结构水或预测水分子能否提升精度尚无定论，且缺乏覆盖片段生长、合成子对接等真实场景的系统评估。

（3）交叉对接挑战：实际虚拟筛选常需将小片段对接到较大配体的结合口袋（片段入先导，FinL），或将生长所得的先导化合物对接到原始片段结合口袋（先导入片段，LinF），溶剂分子在此类场景中的作用尚不明确。

针对上述问题，研究人员设计了一系列统计学评估实验。研究采用两个数据集：

（1）LEADS-FRAG：93 个高分辨率蛋白–片段复合物，用于重对接评估；

（2）Frag2Lead：103 对蛋白–片段与对应蛋白–先导复合物，用于交叉对接评估。对接工具包括 FlexX、HYDE 重打分、DOCK 及 DOCK\_mod（仅保留经 HYDE 预筛选的水分子）。溶剂模型设置包括：dry（无水）、wet（晶体水）、rism（3D-RISM 预测水）、waterdock\_fxx（FlexX 自对接水）及 gw34（GalaxyWater-CNN 预测水）。

片段与先导重对接

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Xdb0oXibAJhcWgNnHciatejo8SUric4TCvoHOt2wpp5ScNibF8YwHRWSBlRshr4XeV1gxwkYCzhficAzwGjLEhtPjld1iaE8HjKLGyDnicmXsFYMps/640.png)

图1 LEADS-FRAG 数据集片段冲对接结果

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Xdb0oXibAJhdichNLjzTGoicAfiaSBBrAIce9bfdtCQGNFiaSPpibcz9IxHWp9DOt9ZNqGGFQbgQNiaW3PDoP0mfVQPFvLoJ0ez2F83wacUE7G95cY/640.png)

图2 Frag2Lead 数据集的片段与先导重对接结果

在 LEADS-FRAG 数据集的片段重对接（图1）中，FlexX 各溶剂模型间差异较小（成功率 53%–58%，dry 为 54%）；DOCK dry 成功率仅 35%，而 wet 升至 59%，gw34 达 60%；HYDE 与 DOCK\_mod 引入溶剂后存在性能波动，但整体仍优于 dry。在 Frag2Lead 数据集的片段与先导重对接中（图2），水模型同样稳定提升了对接精度，且先导化合物重对接成功率普遍高于片段，侧面反映片段对接的固有难度。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Xdb0oXibAJhcI0fHyIcovG5kkg2hV8EcOPI7nRhfrvib6NicN3MeRiaBwW8pObDHcuwHZErqDAVE5jzLRrcUoCtBGvib1wHbJVwYN86UiaBsvWAlM/640.png)

图3 A（DOCK\_dry：4.9 Å） B(DOCK\_wet：1.8 Å) C(DOCK\_mod wet：3.2 Å)

BRPF1 溴结构域（PDB: 5D7X）的对接实例显示：DOCK dry 的 RMSD 为 4.9 Å，DOCK wet 降至 1.8 Å，而 DOCK\_mod wet 为 3.2 Å（图3）。保留全部晶体水分子可显著改善 DOCK 的对接精度，但过多的水分子约束会限制配体的空间可及性，不利于后续片段生长模拟，在后续图4研究中有所体现。

先导入片段（LinF）模拟片段生长

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Xdb0oXibAJhcmDXfkzoticc1IQf3oM8hVgFG1ThD5Td8DzrgwaS5OQsQjZqpDC3ichicIfQIPVXfyKevic9BWmcicF0ESaiaWnOePfhVx9kYNmibgLc/640.png)

图4 先导入片段（LinF）交叉对接结果

将较大先导分子对接到片段结合口袋（模拟片段生长）时，各溶剂模型下成功率仅为 18%–24%，与 dry 相比无显著提升；DOCK 部分水模型成功率甚至为 0%，表明过多水分子导致对接失败。DOCK\_mod 相对稳健，但总体成功率仍低（图4）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Xdb0oXibAJhfDdk4QpWLuicj1NquhMvXyDXCg0ZHVticnLU2vgEP4pah8n7srcaDbAoNylGTpDpG1MNyoPCesJeianvLxEBdSdu8Y8wfl5tichicM/640.png)

图5 LinF 交叉对接中引入药效团约束与模板对接

为改善 LinF 交叉对接，研究者进一步引入药效团约束与模板对接策略。以 FlexX dry 为例，无约束成功率 22%，药效团约束提升至 24%，模板对接大幅提升至 52%。因此，在片段生长场景中，依赖水模型优化收益甚微，过度水分子约束甚至有害，而模板对接策略远优于水模型调优（图5）。

片段入先导（FinL）模拟片段虚拟筛选

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/Xdb0oXibAJhfcB4VLLiafQ5yd4ZJRiaz8VmdGnwu78ls03ibnNicRvVVZ3vKGdKzb1J4IWyQwR1HMhvDsShvCYaMjhogxu1bxibLKKiaJQ5ibkauPMY/640.png)

图6 片段入先导（FinL）交叉对接结果

将小片段对接到先导物结合口袋（模拟片段虚拟筛选）时，预测水模型对 FinL 具有中等提升作用：最优组合 FlexX + gw34 成功率 40%（dry 为 35%）。若限定在先导重对接成功的案例中，各溶剂模型成功率普遍提升，FlexX + gw34 可达 50%（图6）。然而，即便如此，FinL 交叉对接成功率仍显著低于先导重对接{后者多在 60%–70% 以上（图2）}，提示仅解决水合位点问题不足以完全攻克片段对接的核心挑战。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Xdb0oXibAJhcuHI9ho9DrbViaqNZ03sro0IOgJIVZChZyZuPs4q5niatUsokvuWWnFakK1E9XQ0daR8plOTLPRVic3gW8E4rWNo9enpllSnJ2wI/640.png)

图7 共识对接策略分析

为此，研究人员又统计了每个条目在各组合中的最佳 RMSD 发现：片段/先导重对接共识成功率高达 92%–97%，远超任一单一模型；FinL 交叉对接共识成功率为 80%；LinF 交叉对接无模板时为 51%，引入模板约束后升至 72%（图7）。说明结合多溶剂模型与多对接软件的共识策略，是提高对接预测鲁棒性的有效途径。

评估不同组合在虚拟筛选中的排序能力

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Xdb0oXibAJhfOT85T30pFCtqO8PadmZfXdbxFNYAaL8KfJMiawTRqKic1jib66DjqSpW0IUobZBiau10HXv7TKA04NvSY3icuYBnhdoiaRoRnbVhHg/640.png)

图8 LEADS-FRAG片段重对接

研究者还进一步评估了不同组合在虚拟筛选中的排序能力。在 LEADS-FRAG 片段重对接中，FlexX 区分结合与非结合片段的能力最佳，且受水模型影响较小；DOCK 引入溶剂后排序能力有所提升，但仍不及 FlexX。对接构象正确时排序显著改善(图8)。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Xdb0oXibAJhdx1kAm6RWSDSTr04f79meuRCWK4iaH1PtWfFcIQGUZx6wlY8f5hLDdcPiaWHicEywXTUmeML1c3iciafQUeVbxibyLcqJk1E7XiahES0/640.png)

图9 Frag2Lead进行片段重对接 + FinL 交叉对接（FlexX）

FlexX在 Frag2Lead 的 FinL 交叉对接中（模拟更加真实的“将小片段对接到大口袋中筛选”的应用场景），当构象正确时，75% 的结合片段可排入前 26–35 位；若仅统计先导重对接成功的条目，dry 与 wet 模型排名略有改善，而预测水模型提升有限。这表明重对接性能不能直接等价于交叉对接场景下的排序优势，仅凭重对接结论指导真实片段筛选存在风险（图9）。

实际应用建议

重对接场景：保留全部水分子或可提高重对接成功率，但对前瞻性筛选缺乏合理性。仅纳入靶点特异性的关键水分子是更合理的替代方案，已在多个案例中展现潜力，但需更详尽的保守水合位点信息。

片段生长（LinF）：不应单纯依赖重对接成功率选择工具；即使片段重对接成功，也不能可靠预测片段生长的成败。保留全部晶体水易造成空间位阻，会导致大分子无法置入。建议删除全部水分子或仅保留极关键的桥接水，推荐优先使用模板对接，可将成功率从约 20% 提升至 52%。

片段虚拟筛选（FinL）：重对接表现对工具选择有参考价值但非绝对；即使将评估限定在先导重对接成功中，FinL交叉对接的成功率也仅提升约5–10%（图6）。从图9中correct pose与val.的对比可见，在实际片段虚拟筛选中，确保片段对接构象本身的准确性，往往比依赖重对接结果预选工具更为有效。溶剂处理方面，建议保留部分关键水分子（完全删除或全保留均不推荐），并采用多溶剂模型的共识对接策略；预测水分子有助于适度收缩结合空腔、引导片段识别极性热点，共识策略可将FinL对接成功率从40%大幅提升至80%。

参考资料：

https://doi.org/10.1021/acs.jcim.5c02352

https://doi.org/10.1021/acs.jcim.1c01378 

https://doi.org/10.1021/acsmedchemlett.9b00331 

https://doi.org/10.1038/s41467-022-33981-8 

“分子设计，启迪未来”\-（分迪科技）专注于新药设计与药物发现18年，分迪一直在路上为工业制药企业、科研机构提供最前沿的药物设计解决方案与工具应用、以及药物设计项目合作等。 “分迪科技”是“分迪药业”的前身，现为分迪药业的全资子公司。

"分迪药业"是一家致力于开发靶向蛋白降解创新药研发企业，目前“分子胶”新药已经进入临床实验，欢迎各大药企与投资机构洽谈合作。 

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/icwRwl0DrJQZFxibLEZ6O16XLv8qWiaQiaWCN15qbX3TnaaxQkHZRQ9IZ1kZDhuHrgibLeu0qdNeVgsCzibRKbwultWg/0.png) 

 分迪科技 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/icwRwl0DrJQZFxibLEZ6O16XLv8qWiaQiaWCN15qbX3TnaaxQkHZRQ9IZ1kZDhuHrgibLeu0qdNeVgsCzibRKbwultWg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
