---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247486032&idx=1&sn=9f35690ebdc0d64a1b74248c8d03744e
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247486032&idx=1&sn=9f35690ebdc0d64a1b74248c8d03744e
source_domain: mp.weixin.qq.com
title: J. Med. Chem. | 基于大规模分子库对接与生物物理分析的小分子 TMPRSS2 抑制剂研究
author: 
published_at: 
fetched_at: 2026-04-25T02:04:30Z
extractor: wechat_worker
content_hash: fd9c8021cc6724f2e56a834abc845bb7f9bd5831e61f4efd222b77324d8138f5
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/KoRXqKjLA99Frpib4r6Bh0uCb99GP13Y2JhibErjg9b8oiaFZDrTICWrUOqOkAWpHZrr9Ogic7aEZtic9oetaYMPQlQ/0.jpg) 

# J. Med. Chem. | 基于大规模分子库对接与生物物理分析的小分子 TMPRSS2 抑制剂研究

[ DrugIntel ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

# 《Journal of Medicinal Chemistry》发表的《Large Library Docking and Biophysical Analysis of Small-Molecule TMPRSS2 Inhibitors》一文，以跨学科视角整合虚拟筛选、生物物理分析与结构生物学技术，为呼吸道病毒通用靶点TMPRSS2的抑制剂研发提供了从理论到实践的完整解决方案。

# 作者以 **TMPRSS2 的结构** 为靶点，进行了小分子的 **大规模虚拟筛选对接**，以期寻找新的先导化合物起点。作者探索了两种不同的、基于结构指导的策略，通过 **共价** 和 **非共价** 小分子抑制剂来抑制 TMPRSS2 蛋白酶的活性（见图 1c）。具体而言，作者对一个包含 **2 亿个按需可得的类先导分子** 的化合物库，分别基于 **TMPRSS2 的同源建模结构** 和 **晶体结构** 进行了分子对接，从中筛选出一个 **基于酯类的共价骨架** 和一个 **非共价的胺类骨架**，并进一步开展生化表征。作者成功获得了 TMPRSS2 的一种易于结晶的构型，并解析了两个新的复合物晶体结构。同时，结合一系列生化和生物物理实验，作者验证了这些抑制剂分子的有效性，并从 **灭活效力**、**三元复合物结合** 以及 **酰基-酶复合物的稳定性** 等方面深入理解了其作用机制。

# 本文将从研究背景、核心方法、关键发现及科学价值四个维度，对文献进行专业拆解。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/KoRXqKjLA99Frpib4r6Bh0uCb99GP13Y241R7yO4rtUmRs5UPPiaHjGGFjBiaY0nfe4yXyo4sJmlOY3urYPGyJOIw/640.jpg)

### 一、研究背景：TMPRSS2作为抗病毒靶点的必要性与挑战

TMPRSS2（II型跨膜丝氨酸蛋白酶）是呼吸道病毒入侵宿主的“不可替代环节”，其生物学特性决定了其作为靶点的核心价值，但现有研究存在显著瓶颈：

#### 1\. 靶点的不可替代性

* **病毒入侵的“必经步骤”**：TMPRSS2通过切割SARS-CoV-2的Spike蛋白（S1/S2位点），诱导其构象变化，从而介导病毒与宿主细胞膜融合；该机制同样适用于流感A/B型、MERS-CoV等多种呼吸道病毒，使其成为“广谱抗病毒靶点”。
* **生理功能的安全性冗余**：TMPRSS2敲除小鼠无明显生理缺陷，且对病毒感染的敏感性显著降低，证明抑制该蛋白酶不会严重干扰人体稳态，为药物研发提供了安全窗口。

#### 2\. 现有抑制剂的局限性

临床候选药物卡莫司他（camostat）、那法莫司他（nafamostat）虽能抑制TMPRSS2，但存在两大问题：

* **选择性差**：二者均为泛丝氨酸蛋白酶抑制剂，可作用于凝血因子、胰蛋白酶等，易引发出血、胃肠道副作用；
* **临床效果不佳**：在COVID-19临床试验中，未显示出优于标准治疗的获益，且口服生物利用度低（卡莫司他需静脉给药）；
* **结构信息缺失**：缺乏高分辨率的TMPRSS2-抑制剂共晶结构，难以精准优化分子设计。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99Frpib4r6Bh0uCb99GP13Y2NskcFhkOibkHZicX3xy1kV00026cfwC6fpwicFLNJd9VIPD7Tka73Mo0g/640.png)

### 二、研究核心方法：多维度技术整合的“靶点-药物”开发体系

本文的核心创新在于建立了一套“结构引导-高通量筛选-生物物理验证”的闭环研究体系，覆盖从虚拟筛选到临床前验证的全流程：

#### 1\. 结构模型构建：从“同源建模”到“晶体解析”的递进

* **初始阶段（无晶体结构时）**：基于5种同源蛋白酶（血浆激肽释放酶、凝血因子XI等，序列一致性38%-44%），用RosettaCM构建1500个TMPRSS2同源模型，通过“活性化合物对接验证”（卡莫司他、那法莫司他等）筛选出200个高质量模型，确保活性口袋构象的准确性；
* **进阶阶段（有晶体结构后）**：解析出TMPRSS2的截短体（mnTMPRSS2，缺失N端LDLR结构域）与3种配体的共晶结构：
   * 那法莫司他代谢物（4-胍基苯甲酸）：1.59 Å（PDB 8V04）；
   * 抑制剂157（4-乙氨基苯甲酸）：2.07 Å（PDB 9E83）；
   * 非共价抑制剂6-脒基-2-萘酚：2.19 Å（PDB 8V1F）； 这些结构首次揭示了TMPRSS2 S1口袋（关键结合位点）的氨基酸相互作用模式（如D435与胍基的盐桥结合），为分子设计提供了精准坐标。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99Frpib4r6Bh0uCb99GP13Y2aIkKyOyXoApIdFFAW5FuyP9Hia5ibHIwJia8p4EJiaDOGNtH37OHTVnWQw/640.png)

#### 2\. 高通量筛选：两种策略靶向“共价”与“非共价”抑制

研究针对TMPRSS2的催化机制，设计了两种筛选路径，分别对应不同作用机制的抑制剂：

| 筛选策略     | 靶点结构           | 化合物库                      | 筛选规模         | 核心筛选标准                                                   | 命中分子           |
| -------- | -------------- | ------------------------- | ------------ | -------------------------------------------------------- | -------------- |
| 共价抑制剂筛选  | 同源模型           | ZINC20库（以Enamine REAL库为主） | \~2亿个单阳离子化合物 | 1\. 对接分数Top 0.1%；2\. 活性口袋覆盖度≥80%；3\. 含可与S441反应的亲电基团（如酯基） | 2805（酯类）       |
| 非共价抑制剂筛选 | 晶体结构（PDB 7MEQ） | ZINC22库                   | \~2亿个单阳离子化合物 | 1\. 与S1口袋D435形成氢键；2\. 无亲电基团；3\. 分子柔性≤5（避免非特异性结合）         | 2222、2602（酰胺类） |

####   

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99Frpib4r6Bh0uCb99GP13Y2hNibwiadfIOujeTxDUgv7ulqMNPUUicCAGIwWzY0mwD7MxMc27LTlAbOA/640.png)

#### 3\. 生物物理验证：多维度评估抑制剂性能

为确保筛选出的分子具备临床转化潜力，研究采用了4类关键实验进行验证：

* **酶活抑制实验**：用荧光底物（Boc-QAR-AMC）检测IC₅₀，同时通过“预孵育时间梯度”（3/11/20分钟）评估时间依赖性（判断是否为共价抑制）；
* **动力学分析**：用DynaFit软件拟合反应进程曲线，计算k\_inact/K\_I（ inactivation rate constant/dissociation constant，衡量抑制效率的金标准），如那法莫司他的k\_inact/K\_I为2.8 μM⁻¹s⁻¹，156为0.93 μM⁻¹s⁻¹；
* **病毒底物切割实验**：用SARS-CoV-2 Spike蛋白（HexaFurin变体）作为底物，通过SDS-PAGE检测切割产物，验证抑制剂能否阻断病毒入侵关键步骤；
* **热稳定性分析**：用差示扫描荧光法（DSF）检测ΔTₘ（熔点变化），如那法莫司他可使TMPRSS2 ΔTₘ提升24.4℃，证明结合稳定性。

### 三、关键研究发现：破解TMPRSS2抑制剂研发的核心难题

本文通过系统性研究，取得了3项具有里程碑意义的发现，直接推动TMPRSS2抑制剂从“基础研究”走向“应用开发”：

#### 1\. 共价抑制剂：优化“P1/P1'双位点结合”，提升选择性与稳定性

* **结构-活性关系（SAR）新认知**：通过对6类衍生物（Scaffold 1-6）的分析，发现抑制剂需同时满足“P1位点阳离子结合”与“P1'位点疏水作用”：
   * P1位点：胍基（那法莫司他）> 乙氨基（157）> 甲氨基（156）> 3-氧杂氮杂环丁烷（139），其中胍基可与D435形成三联盐桥（结合能-12 kcal/mol），是高活性的关键；
   * P1'位点：萘环（156、157）> 苯环（2805）> 联苯（128），萘环可与S1'口袋的G464形成π-π堆积，提升结合特异性；
* **解决“时间依赖型IC₅₀”难题**：发现共价抑制剂的IC₅₀会随预孵育时间延长先降低后升高，原因是“酰基酶复合物水解”与“抑制剂降解”的竞争平衡，提出用“k\_inact/K\_I + t₁/₂（水解半衰期）”替代单一IC₅₀，更精准评估活性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99Frpib4r6Bh0uCb99GP13Y2CNMEibjkdOQ47gDbTuibaTTjlAuLYjZwGymLC9fIg0BKMUok0IYq3iaYw/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99Frpib4r6Bh0uCb99GP13Y2UZDI6C7Qm6iaEA76dM4pkIo5xve1riagt3aHTGX0FjQcPGQA1K8tge2A/640.png)

#### 2\. 非共价抑制剂：开辟“酰胺类新 scaffold”，降低脱靶风险

过去非共价抑制剂因活性低未受重视，本文筛选出的2222、2602打破了这一局面：

* **选择性突破**：在8种呼吸道TTSP家族蛋白酶（TMPRSS3/11A/11B等）及牛胰蛋白酶的筛选中，2222对TMPRSS2的抑制率（77%）显著高于其他蛋白酶（53%-117%，多数接近100%，即无抑制），而那法莫司他对TMPRSS2/3/13的抑制率均<40%，证明非共价抑制剂的选择性更优；
* **作用机制明确**：通过分子对接与DSF验证，2222的氨基端与D435形成氢键（结合能-5.2 kcal/mol），氟代苯基与S1'口袋的V280形成疏水作用，这种“双锚定”模式是高选择性的核心；
* **口服潜力初显**：2222、2602的ClogP（脂水分配系数）分别为2.3、2.1，符合口服药物的理化性质（ClogP 1-3），且无亲电基团（避免胃肠道降解），为后续口服制剂开发奠定基础。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99Frpib4r6Bh0uCb99GP13Y2g3jwWBmzAAgJsPt2n1vOgfX740esDycx4UDnGZ1rUHzF3b55zBCfCA/640.png)

#### 3\. 工具与资源：公开可复用的“研究工具箱”

为推动领域发展，研究团队公开了3类关键资源，降低后续研究的门槛：

* **蛋白质工具**：dasTMPRSS2（活性全长）、mnTMPRSS2（高结晶性截短体），可直接用于抑制剂筛选；
* **结构资源**：3个高分辨率共晶结构（PDB 8V04、8V1F、9E83），涵盖共价/非共价结合模式，可作为分子对接的模板；
* **筛选方法**：公开了虚拟筛选的打分函数参数（如氢键权重1.2、疏水作用权重0.8）、酶活检测的“反应体系配方”（50 mM Tris-HCl pH 8.0、150 mM NaCl、0.02% Tween-20），可直接复现。

### 四、科学价值与应用前景：为呼吸道病毒防治提供新策略

#### 1\. 学术价值：填补TMPRSS2抑制剂研究的3项空白

* 首次建立“同源建模-晶体解析-虚拟筛选-生物验证”的全流程体系，为其他丝氨酸蛋白酶抑制剂研发提供范式；
* 首次揭示TMPRSS2 S1/S1'口袋的“双位点结合模式”，纠正了过去“单一P1位点决定活性”的认知；
* 首次证明非共价抑制剂可有效阻断Spike蛋白切割，开辟了TMPRSS2抑制剂的新方向。

#### 2\. 应用前景：推动两类药物研发落地

* **短期（1-3年）**：基于156、157的结构，优化P1位点的胍基类似物（如吗啉胍），提升口服生物利用度，开发静脉注射用广谱抗病毒药物，用于新冠、流感的重症治疗；
* **长期（3-5年）**：以2222为母核，通过“结构优化”（如在苯环引入甲基提升疏水性）提升活性（目标IC₅₀降至100 nM以下），开发口服预防性药物，用于高危人群（老年人、免疫缺陷者）的病毒暴露后预防；
* **跨界潜力**：TMPRSS2在前列腺癌、胰腺癌中高表达，本文的抑制剂或可用于“病毒感染与癌症共病”患者的联合治疗（如新冠合并前列腺癌）。

#### 3\. 未来方向：需解决的2个关键问题

* **选择性进一步提升**：虽然2222对TMPRSS2的选择性优于那法莫司他，但仍对TMPRSS3（同源性最高）有抑制（70%），需通过“结构-Based设计”靶向TMPRSS2特有的K342（S2口袋），提升亚型选择性；
* **体内活性验证**：当前研究均基于体外实验，下一步需在动物模型（如hACE2转基因小鼠）中验证抑制剂的药代动力学（PK）、药效动力学（PD），评估体内抗病毒效果。
  
  
参考文献：Bryan J. Fraser, Nicholas J. Young, Brian J. Bender, Stefan Gahbauer, Olzhas Ilyassov, Ryan P. Wilson, Yanjun Li, Almagul Seitova, André Luiz Lourenço, Dong Hee Chung, Conner Bardine, François Bénard, Brian K. Shoichet, Charles S. Craik, and Cheryl H. Arrowsmith, Large Library Docking and Biophysical Analysis of Small-Molecule TMPRSS2 Inhibitors, Journal of Medicinal Chemistry, 2025.

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icaZmJVvQe5nCiabibOyaceianZY23nlsXAkxR5uiajvHibdBJvESicc58tOeibVXmVTp4HVVADZh79C1iczA/0.png) 

 DrugIntel 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icaZmJVvQe5nCiabibOyaceianZY23nlsXAkxR5uiajvHibdBJvESicc58tOeibVXmVTp4HVVADZh79C1iczA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
