---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzY5NzEzMjkzMQ%3D%3D&mid=2247484053&idx=1&sn=ee56c9e769b85eaae8d9d5984f0d36b1
canonical_url: https://mp.weixin.qq.com/s?__biz=MzY5NzEzMjkzMQ%3D%3D&mid=2247484053&idx=1&sn=ee56c9e769b85eaae8d9d5984f0d36b1
source_domain: mp.weixin.qq.com
title: JACS | FragNet：一种具有四层可解释性的分子性质预测图神经网络
author: 
published_at: 
fetched_at: 2026-04-25T02:03:33Z
extractor: wechat_worker
content_hash: fe6f17565ab19f7da9737c02231d1e6e4f49e230c2f7883b3f8a3910198ce31f
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/yiab2uNgggg3hj0H6WOxwLuql0IQhV1Wyby3Vy54mcdb7ros7xyB6PXgOkHIk4fK8axFVQLFzxhHpqF94bIpaHGnA9BdWABUNg9JMQW3DRicQ/0.jpg) 

# JACS | FragNet：一种具有四层可解释性的分子性质预测图神经网络

原创 AI4Mat前沿 AI4Mat前沿 [ AI4Mat前沿 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

分子性质预测是药物设计、能源材料开发、催化剂研究等现代科学领域的核心任务。尽管机器学习模型在该领域取得了显著进展，但如何在保持高预测精度的同时提供可解释的预测结果，仍是一个重要挑战。近期发表于《Journal of the American Chemical Society》的研究提出了FragNet模型，该模型不仅在预测精度上与当前最优方法相当，还能够从原子、化学键、分子片段及片段间连接四个层次提供系统性的可解释性分析。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3bOYygsSsnJBlaZQdAUQwWbmjeXdfKqGkypoh9uEXWKWM6PcGiaVianEqkh9yHDmIgeCvFUlPvC0SEOgv9zBpaiaRHbdcJS7MeLA/640.png)

## 研究背景与动机

可解释性在分子性质预测中具有重要意义。理解模型的决策过程有助于科学家发现新假设、设计具有目标性质的新材料，并加速分子设计流程。现有的可解释人工智能方法可分为内在可解释性和外在可解释性两类。SHAP和LIME等外在方法虽然适用于多种模型，但在处理图结构分子数据时面临挑战，难以捕捉分子特有的层级关系和相互作用。

图神经网络（GNN）因其与分子结构的天然契合性而成为分子表示的理想选择。然而，现有的可解释GNN模型存在明显局限：大多数模型仅关注原子或分子片段单一层次，且无法处理非共价键连接的分子亚结构（如盐类和配合物）。FragNet正是为解决这些问题而设计的。

## 模型架构与数据表示

FragNet基于消息传递图神经网络架构，同时对四种不同的图结构进行推理：原子图、化学键图、片段图和片段连接图。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3UjTmZ6E0ITlB5uO4RnlUnnVz3uicuLMky6aYctSTJBPq7bExAUgTGOrrTMHKTonWZqUMmZpv5GRvUXkvf4AexvOMxdCTia7akk/640.png)

▲ Fig.1 | FragNet的架构与数据表示。(a) 原子图和片段图的边特征分别从键图和片段连接图中学习获得。(b) 片段图的初始片段特征是组成该片段的更新后原子特征的加和。(c) FragNet在两个非共价键连接的子结构之间进行消息传递的示意图。片段-片段连接也存在于每个非共价键连接结构中的相邻片段之间。

如图1所示，原子图以原子为节点、共价键为边；化学键图以键为节点，当两个键共享一个原子时形成边；片段图通过分子分解算法（本研究采用BRICS分解）生成，片段之间的边由分解位点处的键形成。对于盐类或配合物等非共价键连接的分子，模型引入"虚拟边"来表示片段间的空间邻近关系。

BRICS是一种基于规则的分解算法，根据逆合成分析的16条化学环境规则在合成可行的键位置分解分子。这种分解方式产生的片段具有化学意义，便于后续的结构-性质关系分析。

## 预测性能评估

研究团队在MoleculeNet基准数据集上对FragNet进行了系统评估，涵盖回归和分类两类任务。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg2YkdnqQxp2SibZBsm989EILpn3n9wZoYf8Vb9HACkWmtt9rSOxKzI8mgc8lI0Z8NyQEW3ztVInLHoI1nWHAkaf6M2M4xou7xyI/640.png)

▲ Table 1

表1展示了FragNet在六个数据集上的预测性能。在回归任务中，FragNet在ESOL（水溶性）和Lipophilicity（脂溶性）数据集上的表现与AttentiveFP和D-MPNN等先进模型相当。在分类任务中，FragNet在BBBP（血脑屏障渗透性）和HIV数据集上同样展现出竞争力。值得注意的是，FragNet在保持高预测精度的同时，还提供了其他模型所不具备的多层次可解释性。

## 四层可解释性机制

FragNet的核心创新在于其四层可解释性框架，包括注意力权重和贡献值两种互补的解释机制。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg2oO6VV0WyHfJSsRAJUmQTeG5yuR6y3rvOzAhOkAGFic0E5VSuNnwiadqAktFkhjR0uOTpkb5bWStxd75mMIrJzUXqL6WQAAotcE/640.png)

▲ Table 2

### 注意力权重与贡献值的区别

注意力权重反映模型在预测过程中对特定子结构的关注程度，而贡献值则量化该子结构对预测结果的方向性影响。高注意力权重并不必然意味着大的贡献值——一个片段可能因其在分子中的关键位置而获得高关注，但其对最终预测的实际影响可能因与其他片段的相互作用而被调节。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg2C06o24g6FYSulvNxxiaqfRia5IurLDCUWIuppblgpoEwp0p38NkWwSuLGc1moMhYQvozGysjTmq0SvoiaOVRTQnAialHbYVgs9LU/640.png)

▲ Fig.2 | 贡献值计算的示意图。

贡献值的计算采用"遮蔽"策略：通过比较完整分子的预测值与移除特定片段后的预测值之差来量化该片段的贡献。正贡献值表示该片段增加预测值，负贡献值表示降低预测值。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg1Q0gQXMjLqqGvUQE5u6Wr5BTSwm3vcKWKLHuGTicByJasRDrX6zWNCaVCIhtnmEb78yTTF5AHggvibgiceca9H8D0V2WfTSQZO7Q/640.png)

▲ Fig.3 | FragNet中不同类型的注意力权重和贡献值可视化，以CC\[NH+\](CCCl)CCOc1cccc2ccccc12.\[Cl-\]为例，(a)、(b)和(c)分别展示原子、键和片段的注意力权重，(d)展示片段贡献值。(b)中的色标适用于原子、键和片段的注意力权重。(e)中的表格提供了片段连接的注意力权重。(c)中蓝色方框内的数字对应片段索引，该索引同样用于(e)。

图3以一个具体分子为例，展示了FragNet提供的多层次可解释性信息，包括原子注意力权重、化学键注意力权重、片段注意力权重、片段贡献值以及片段连接注意力权重。

## 原子层面的可解释性分析

### 原子注意力权重

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg2h1efWTx26gTvWmrhiaicgD2I1hWqABw1tRaVia86XQiaqiabV3LtquvdPZBqrWTArCdIDoHPsn50Prhjb4ibbnibdarINX0diajmdRsE/640.png)

▲ Fig.4 | 常见原子类型的平均注意力权重，由溶解度、亲脂性和癌症药物响应预测中绝对误差小于0.1的预测结果计算得出。高权重表明模型在进行预测时对这些原子赋予了更高的重要性。误差棒表示所分析分子间的标准偏差。

图4展示了常见原子类型在水溶性、脂溶性和癌症药物响应预测中的平均注意力权重。碳原子在所有性质预测中均获得最高关注，这与其作为有机分子骨架核心的角色一致。氧和氮原子的注意力权重相对较低但稳定，反映了它们作为官能团组成部分的重要性。卤素原子（氟、氯、溴）的注意力权重因性质而异，体现了模型对不同预测任务的适应性。

### 原子贡献值

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3ENpzyt9N4MUseZrfHfIB8lWueW4ibNBcN0heLe9tljLy1AX773I1wxQEZVmszhue8eQTJicYB2VKOQiaUIsibaRjFBZNZskkH8BI/640.png)

▲ Fig.5 | 按元素和分子性质分类的平均原子贡献值及统计标注。每个单元格显示平均贡献值±标准偏差，括号内为样本数n。

图5呈现了不同元素对三种分子性质的平均贡献值。对于水溶性预测，碳原子表现出负贡献（降低溶解度），而氧和氮原子的贡献接近零或略为负值。这一看似反直觉的结果实际上反映了分子系统的复杂性：虽然氧和氮通常与亲水性相关，但它们的实际贡献取决于具体的化学环境和连接方式。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg2JPeCiacu6iabPSDVcpssynVrAyIhvb2yzSibpy0QicIEYNg6bPUFOK7730WraZTJX7HZDibnzXjsGhcrian2GbKibyHnryDkbZUYNGk/640.png)

▲ Fig.6 | 在水溶性预测中，按成键原子数（度）分组的氧原子和氮原子的原子级贡献值分布。

图6进一步分析了氧和氮原子的贡献值与其连接度（键合原子数）的关系。结果显示，连接度为1的氧原子（如羟基和羰基氧）对溶解度有正贡献，而连接度为2的氧原子（如醚氧）则表现出负贡献。这种细粒度的分析揭示了原子化学环境对性质影响的重要性。

## 化学键层面的可解释性分析

### 化学键注意力权重

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg01oE9NfxMCJZGGacpGvicEbPujfRDMvDmicEkv1jInu1dicicAmZbQRNSKTLKO4Aq3qdx3LrHUMzb1lScI9GwHp5tCV7QZ72G0kyw/640.png)

▲ Fig.7 | 溶解度预测中常见键类型的平均注意力权重，由绝对误差小于0.1的预测结果计算得出。每种键类型所分析的键数量以n表示。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg2QkMTtL9nHUSP4bkPRVGI7icHXibvnricwY7dRHLJfGLhp335VIMUtwNnYylhZE6bCnWicEeE1G5zibicv7xlRiaOUzSsZY0cN6lHjQg/640.png)

▲ Fig.8 | 常见键类型的平均注意力权重，由绝对误差小于0.1的预测结果计算得出。C−C键和C−N键在所有三种性质中均获得较高的注意力权重，反映了它们作为主要结构骨架的重要性。误差棒表示标准偏差。

图7和图8展示了常见化学键类型的注意力权重分布。C-C键和C-N键在所有性质预测中均获得高关注，反映了它们作为分子主要结构骨架的重要性。芳香键（如芳香C-C键和芳香C-N键）同样受到显著关注，表明模型能够识别芳香体系在分子性质中的作用。

### 化学键贡献值

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg0JCdu4Iibkhh9CSc1EBOHicXalhttwvAS5S1yTLABlIJ3TicJ7Dh5fSv5NqhYRZMFhGclAUPNlricNRvugqQlNpToNLGAAx9qnOgE/640.png)

▲ Fig.9 | 三种性质下各键类别的平均贡献值。（左）对于水溶性，极性键增加预测值，而卤素键降低预测值。（中）对于亲脂性，趋势相反。（右）对于癌症药物响应，影响较为温和。这些结果定量地验证了基本的物理化学原理。误差棒表示标准偏差。

图9量化了不同类别化学键对三种性质的贡献。对于水溶性，极性键（如C-O、C-N键）表现出正贡献，而卤素键（如C-Cl、C-Br键）则降低溶解度。对于脂溶性，这一趋势完全相反。这些结果定量验证了基本的物理化学原理，增强了对模型可靠性的信任。

## 片段层面的可解释性分析

### 水溶性预测中的关键片段

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg2oeu8rCL6fATTwEXXhTX1g4E7WibgNlpKiatGYBS6ibkzDNvKOialVS3BN8eRI5ezMhsLQiaPsu4hkWT5c33vicubDeMsT8BSl5lmBk/640.png)

▲ Fig.10 | 水溶性预测中具有影响力的片段分析。（左）小提琴图展示了最受关注片段的注意力权重分布及相应贡献值。高注意力权重表示模型的关注点，而贡献值量化了片段对预测溶解度的贡献。（右）具有最正（上）和最负（下）平均贡献值的片段，对应模型预测会增加或降低溶解度的结构基元。

图10分析了水溶性预测中的关键片段。左侧小提琴图展示了高注意力片段的注意力权重和贡献值分布。右侧列出了具有最正和最负平均贡献值的片段结构。羧酸基团、磺酸基团等亲水性片段表现出正贡献，而长链烷基、卤代芳环等疏水性片段则降低溶解度。

### 脂溶性预测中的关键片段

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg3cFvVwx5P22CRiaLC8uuyPEAj6ns3HlYzL4RfrbVCoZ7RvEiaPn4PGD2icdny7aP449hOUVklgy3iahxoaCN9hxcRzPfQJPlkUkwA/640.png)

▲ Fig.11 | 亲脂性预测中具有影响力的片段分析。图中突出显示了模型识别的关键片段和片段-片段连接。结构标注了其平均注意力权重和相应贡献值，说明模型关注哪些片段以及它们被预测为增加（正贡献）还是降低（负贡献）亲脂性。

图11展示了脂溶性预测的片段分析结果。与水溶性相反，疏水性片段（如烷基链、卤代基团）对脂溶性有正贡献，而亲水性片段则降低脂溶性。这种互补的模式进一步验证了模型学习到的结构-性质关系的化学合理性。

### 癌症药物响应预测中的关键片段

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg1Lra4njgNficZVJ1j4VCOWJ0eftx3iauxEJCBHL6FMgKqMZVInflQXHKtal13JLPWD5G27IicEgGXKohHJ7BWlOOicGYeLkfrIVuk/640.png)

▲ Fig.12 | 对癌症药物响应预测贡献最大和最小的五个片段，这些片段至少出现在十个不同的独特分子中。

图12识别了对癌症药物响应预测贡献最大和最小的片段。含氮杂环（如吡啶、哌嗪）和特定官能团表现出显著的正贡献，这与已知的药效团知识一致。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg3m3meKFhfq6yjibXndOQHF3SeYTxzLYVXKMGhLCIQxomOVsq5cX9TQN0WYOaaDyy1FonFyyCQeyHo0Uiatbn2mOib977liaqxmR6o/640.png)

▲ Fig.13 | 具有高药物响应值和低药物响应值药物的片段贡献值。Average (+)和Average (−)分别表示每个分子内正片段贡献值和负片段贡献值的平均值。

图13比较了高响应和低响应药物分子中片段贡献值的分布，直观展示了片段组成与药物活性之间的关系。

## 活性悬崖分析验证

活性悬崖是指结构高度相似但活性差异显著的分子对，是评估可解释性方法的严格测试。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg36ATtIlcRVIxq6oINibQPVqJiaSG8rvGvUb27kgJwC36GswDHo4cxicLU93YAHU9qXbO1Q8wNyG6SSy8nhQPPjRbHpdic7m4T9pq0/640.png)

▲ Fig.14 | 使用活性悬崖分析对解释正确性的定量验证。(a) 相似分子对中贡献值与溶解度差异的方向一致性。(b) 贡献值大小与溶解度差异的相关性。

图14展示了FragNet在活性悬崖分析中的表现。研究团队筛选了结构相似度高（Tanimoto相似度>0.7）但溶解度差异大（>1 log单位）的分子对，分析独特片段的贡献值与性质差异的关系。结果显示，贡献值的方向与溶解度差异方向的一致率达到71.9%，贡献值大小与溶解度差异的相关系数为0.42，表明FragNet能够正确识别导致性质变化的结构差异。

## 片段连接层面的可解释性分析

FragNet的独特优势之一是能够分析片段间连接的重要性，这对于理解分子整体性质至关重要。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg1qSoPNgaYGz2PP2xjbNgVGRH2lPfV6yg7CeicScEcu535icyWbnJHtECpA4e7MriaYdpCeweicZI1gRLzk5ynoibttS6LQnHsknNibA/640.png)

▲ Fig.15 | 在溶解度、亲脂性和癌症药物响应预测中识别出的高权重连接。误差棒表示平均值的标准误差（SEM）。注意三个柱状图共用水平轴。每种连接的代表性示例见图S14。

图15展示了在三种性质预测中获得高注意力的片段连接类型。不同性质关注的连接类型存在差异：水溶性预测更关注涉及极性基团的连接，而脂溶性预测则更关注疏水性片段之间的连接。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3xNcWOCaETFNBVNx9YZORbRn66zG3Cnriaa6o2V9PzJo184y6bJicGtxBEWMnH4chIGOhlXSz3015pmiaS6Y2jLPibPVRLbYkdOx0/640.png)

▲ Fig.16 | 溶解度数据集的片段连接贡献值。仅包含出现在≥4个分子中的连接以确保统计可靠性。误差棒表示平均值的标准误差（SEM）。

图16量化了片段连接对水溶性的贡献值。涉及亲水性基团（如羧酸、胺基）的连接表现出正贡献，而疏水性片段之间的连接则降低溶解度。

## 物理化学验证

### 非极性/极性比率分析

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3P4IdFH8GgoTt2EwE4GUcb4cNc0H601ia8UnDmWvTYtlRLVyMk5RcGD3hDGJ5aAdD0nET1GNZcjE86J6njZPdPrE1iaCUItUJCM/640.png)

▲ Fig.17 | 片段的非极性/极性比（NPR）与贡献值（C）。可以观察到，对于高度疏水的片段，其非极性分数相比亲水片段具有更大的值。

图17将片段的非极性/极性比率（NPR）与其贡献值进行关联。结果显示，高疏水性片段（高NPR值）对脂溶性有正贡献、对水溶性有负贡献，而亲水性片段（低NPR值）则表现相反。这种定量关系验证了模型学习到的结构-性质关系符合基本物理化学原理。

### 密度泛函理论验证

研究团队还通过密度泛函理论（DFT）计算分子的静电表面电势，与FragNet的贡献值进行比较。结果表明，模型识别的亲水性和疏水性区域与DFT计算的静电表面电势分布高度一致，从量子化学层面验证了模型的可解释性。

## 交互式应用与大语言模型集成

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg1d9Biay6Qe6vGBpnJJAM8NkeCV8HJm0yVNE1ib86CLTYWLaDrYAT46fUny4Xec3xhMZq6x2sicSn9W0ySz2Lo8g9VR4bgyTiaibIs4/640.png)

▲ Fig.18 | 交互式应用程序界面。

研究团队开发了交互式浏览器应用（图18），使研究人员能够可视化任意分子的注意力权重和贡献值，便于进行结构-性质关系分析。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg2Ad75jSQuaNXEYDzDk1ByB0LYnhNVYCbY0lPkShBpOugAeTTYgKiaQnG1bwiaFficdFDmhm1HoGUjkKpo30gyMpW6lI1wBfQ9M2g/640.png)

▲ Fig.19 | 使用和不使用FragNet贡献数据提示Claude 3.5 Sonnet创建具有改进溶解度的分子。大语言模型修改后分子中的新片段以绿色高亮显示。

图19展示了FragNet与大语言模型（Claude 3.5 Sonnet）集成的应用案例。通过向大语言模型提供FragNet的贡献值信息，可以指导分子优化设计。实验表明，结合FragNet贡献数据的提示能够生成溶解度更高的分子结构，展示了可解释性信息在分子设计中的实际应用价值。

## 总结与展望

FragNet代表了可解释分子性质预测领域的重要进展。该模型在保持与最先进方法相当预测精度的同时，提供了前所未有的四层可解释性分析能力。通过系统的化学验证和活性悬崖分析，研究证明了模型学习到的结构-性质关系具有化学合理性和实际应用价值。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg0l2OP71riaO02gwzL9IXzreLcKCWVhOeIBoenEpAvEOWcrDO3YNOMtPD0OAribJ4sZZZa4vgmDrgcybYJgGszNUZtvc2kdqhXHE/640.png)

▲ Table 3

FragNet的局限性包括：BRICS分解算法可能对高度官能化的分子产生过度分解；对于复杂天然产物或高度约束的环系统，可能无法捕捉所有相关的亚结构特征。未来研究可探索替代分解策略（如RECAP、Murcko骨架）以适应不同应用场景。

对于从事分子性质预测和药物设计的研究者，FragNet提供了一个兼具预测能力和可解释性的有力工具。其多层次分析框架有助于深入理解结构-性质关系，加速新材料和新药物的发现进程。

---

****参考文献：Gihan Panapitiya\*, Peiyuan Gao, C. Mark Maupin and Emily G. Saldanha\*. FragNet: A Graph Neural Network for Molecular Property Prediction with Four Levels of Interpretability. J. Am. Chem. Soc. (2026). https://doi.org/10.1021/jacs.5c22620**

****本文由AI4Mat前沿编译分享，旨在学术交流。文中所有图文版权归原作者及出版社所有。**

****关注我们,获取更多AI+材料前沿进展**

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3dePnhYnbJVMpcphQbicTIgcMjbKb36Q3LE6C5V3e39ZjDgMYD0wZTgTCu3xHZuUKnZt8icHsWtpqrkWRI5SdIYXH3icaAtV8IyY/0.png) 

 AI4Mat前沿 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3dePnhYnbJVMpcphQbicTIgcMjbKb36Q3LE6C5V3e39ZjDgMYD0wZTgTCu3xHZuUKnZt8icHsWtpqrkWRI5SdIYXH3icaAtV8IyY/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
