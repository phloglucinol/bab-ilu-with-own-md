---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIwNDkxMDQ3Mg%3D%3D&mid=2247503402&idx=1&sn=2e144d55469f5dd26e9f8b56cdedc868
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIwNDkxMDQ3Mg%3D%3D&mid=2247503402&idx=1&sn=2e144d55469f5dd26e9f8b56cdedc868
source_domain: mp.weixin.qq.com
title: DeepPni：融合序列与结构，刷新结合能预测纪录
author: 
published_at: 
fetched_at: 2026-04-25T02:04:07Z
extractor: wechat_worker
content_hash: 260edd8b8ec5c5ed0f2d76989a164b5ed0e7b4dd89190df7f294c61073306013
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7ONJQHNUmmaMYkxbOBSjZjHXSENtibazjHxS5tA3lpBYqZ0SF57O6XYng/0.jpg) 

# DeepPni：融合序列与结构，刷新结合能预测纪录

原创 榴莲忘返2014 榴莲忘返2014 [ 榴莲忘返 AIDD ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OzEeOxGryWmypDeJADcTJLjZHM8lhAgB8Ix79nGKoIWDb44xccDIF2w/640.jpg)

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OnEMm6S1p9g4t8hYDbZyWNlqJNelr4JGiaUkxic8EFdPbB6jNQQJZhQTQ/640.jpg)

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OHp3nSaff0kuwCpAYCxojcNia6ShGYhaMaRvxxD7otEsNvdNkrdy9j1Q/640.jpg)

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7O7AXdLNRibpCykKOvP0muDZVWTvMibjPiazssbB0Te05EeAHibbdbXTUMAQ/640.jpg)

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OsRBkre2hWCNEdbvhoIIiaNEO1xOkDTjtKJ6dOQ4BW3icX7RoicIzSn2Tw/640.jpg)

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7Oplbt1hewV0jCyP5daTnCxTvDcewBblVAYxibclF7XiaTkEAlm4MrrgNg/640.jpg)

<<< 左右滑动见更多 >>>

---

  
**榴莲忘返AIDD** 

供稿 | 柠檬青年  
审稿 | 吉星 

### 目录

1. DeepPni 利用 ESM-2 语言模型与边缘感知图网络，精准捕捉突变对蛋白 - 核酸复合物结合能的影响，基准测试表现优于现有 SOTA 方法。
2. CryoBoltz 利用模糊的冷冻电镜数据引导 AI 模型，预测蛋白质的多种动态构象，揭示其活动状态。
3. GVT 将分子图转换为离散序列，生成精度媲美甚至超越扩散模型，而计算速度大幅提升。
4. 研究人员开发了一种灵活的 Transformer 模型，能利用分子任何已知的属性组合来预测未知属性，解决了现实世界中化学数据稀疏的难题。
5. XAMP 框架采用 ESM-2 与 Transformer 双引擎架构，解决数据偏差难题，从深海微生物组中精准锁定 2355 个高置信度抗菌肽。
6. BioMedGPT-Mol 通过多任务学习，能读懂多种分子语言并规划合成路线，向通用 AI 化学家迈出了一步。

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OCx7iabeU4eZPgicyCmaJuuQ2sibJyISThxXrVrtJibgpsulyQ9AbxBXs1A/640.png)

## 1\. DeepPni：融合序列与结构，刷新结合能预测纪录

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OzEeOxGryWmypDeJADcTJLjZHM8lhAgB8Ix79nGKoIWDb44xccDIF2w/640.jpg)

在转录因子或 RNA 结合蛋白相关靶点的药物设计中，核心痛点在于**预测突变对结合亲和力的影响**。传统自由能计算（FEP）耗时过长，普通机器学习模型往往局限于单一维度——仅关注序列或结构。DeepPni 结合两者，提供了一套高效的解决方案。

**进化语境与空间结构的融合**

DeepPni 的逻辑清晰：利用 Meta 开发的蛋白质语言模型 ESM-2 处理序列信息。如同理解文本，ESM-2 能判断氨基酸突变在进化语境下的合理性。

化学反应发生在三维空间，作者引入了边缘感知的关系图卷积网络（RGCN）。传统图模型常仅将原子视为节点，忽略连接它们的边。蛋白 - 核酸界面充斥着氢键、盐桥、范德华力及水分子桥接等复杂相互作用。DeepPni 特意强化对「边」的编码，通过算法捕捉原子间的具体物理化学关系，精准处理异质相互作用。

**实战数据表现**

在包含 1951 个突变的大型数据集上，DeepPni 的皮尔逊相关系数（PCC）达到 **0.76**。在充满噪音的结合能预测领域，这一数据代表了实质性进步，性能超越 DeePnaP 和 MutPni 等前沿模型。

该模型的泛化能力值得关注。无论蛋白结合对象是 DNA 还是 RNA，实验温度是 25 度还是 37 度，模型表现均稳定。在涵盖 ITC（等温滴定量热法）和荧光偏振数据的 ProNab 外部验证集中，DeepPni 依然维持高相关性。面对新突变体或新结合位点设计，该工具能提供高置信度的结果，提升湿实验复现的成功率。

📜Title: DeepPni: Language and graph-based model for mutation-driven protein nucleic acid energetics  
🌐Paper: https://arxiv.org/abs/2511.22239

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OTfFNfgJFShN221yB7m8ic1ZfTyM7tIs5pDdHpTsS8JZ3Fe0x8AibhrYA/640.png)

## 2\. CryoBoltz: 用 AI 透视蛋白质动态，解锁药物新靶点

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OnEMm6S1p9g4t8hYDbZyWNlqJNelr4JGiaUkxic8EFdPbB6jNQQJZhQTQ/640.jpg)

蛋白质并非静态结构，它们通过移动、变形等构象变化来执行功能。AlphaFold 这类工具能生成蛋白质的静态「证件照」，但药物研发更需要了解它们工作时的「录像」。

冷冻电镜（cryo-EM）可以捕捉这些分子机器的快照。然而，当研究对象是离子通道或抗体这类柔性蛋白质时，得到的数据通常是「模糊」的。这好比对跳舞的人进行长曝光，最终只拍到一团运动虚影，而非任何清晰的舞姿。这种包含多种构象的模糊数据被称为「异质性」（heterogeneity），是结构解析长期面临的障碍。

CryoBoltz 方法将这种模糊性视为包含多种构象的宝贵信息。它与一个基于扩散的结构预测 AI 模型协同工作。这个 AI 模型好比一个结构组装工，从随机的原子云开始，逐步搭建出合理的蛋白质结构。

在此过程中，CryoBoltz 充当「向导」，利用模糊的冷冻电镜密度图，指导「组装工」将搭建的结构置于密度图的相应区域内。其核心是「多尺度引导」机制，同时关注整体与局部。

1. **全局引导**：确保整个蛋白质模型的大致形状和朝向，符合冷冻电镜密度图的整体轮廓。
2. **局部引导**：确保模型中每一小段肽链和氨基酸侧链，都位于各自对应的局部密度区域内。

这种双重约束，如同经验丰富的工匠，既保证整体比例，又打磨局部细节。因此，AI 模型在生成结构时，会探索那些符合物理化学原理且能嵌入实验数据的构象。由于实验数据本身包含多种构象的「虚影」，CryoBoltz 能引导模型生成一系列不同的合理结构，分别对应这些构象。

在药物发现中，该方法的价值尤为突出。以膜转运蛋白为例，它通过「开放」和「关闭」两种构象转运物质，而靶向药物可能只对其中一种构象起作用。如果模型只能预测出单一的平均构象，药物设计便无从下手。CryoBoltz 能从同一份模糊的实验数据中，解析出「开放」和「关闭」两种状态，为药物设计提供与功能相关的清晰靶点结构。

CryoBoltz 是一个「推理时」的方法，无需重新训练庞大的 AI 模型，可直接应用。拥有冷冻电镜数据和结构预测模型的实验室，都能将其整合进工作流程。这降低了应用门槛，使解析动态结构成为更多研究者可以使用的工具。

📜Title: Multiscale guidance of protein structure prediction with heterogeneous cryo-EM data  
🌐Paper: https://arxiv.org/abs/2506.04490v2

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OC50XqFZ4V1An9iaEicJAYYS0UDEoAicgKjUdqYAusPAWgTNcTbHnWFOEw/640.png)

## 3\. GVT: 分子生成新范式，比扩散模型更快更准

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OHp3nSaff0kuwCpAYCxojcNia6ShGYhaMaRvxxD7otEsNvdNkrdy9j1Q/640.jpg)

分子生成领域追求的目标是：生成化学结构新颖、性质优良的分子，同时兼顾速度与计算成本。近年来，扩散模型（Diffusion Models）因其高质量的生成结果备受关注，但其计算开销大，生成一个分子库耗时数日，成为药物研发的瓶颈。

Graph VQ-Transformer (GVT) 模型提供了一个新思路。它采用离散化方法，取得了优异成果。

**把分子当作一门语言来学**

GVT 的核心思路分为两步，就像学习语言一样。

第一步是「学单词」。模型使用一个图向量量化变分自编码器（Graph VQ-VAE）来构建一本「分子词典」。VQ-VAE 读取一个分子的图结构，将其压缩成一系列离散编码，即「单词」。每个「单词」代表一种特定的化学子结构或基团。

关键在于如何将非线性的图结构转化为线性序列，而不丢失连接信息。模型采用了反向 Cuthill-McKee (RCM) 节点排序算法。该算法系统性地为原子编号，确保空间上邻近的原子在序列中也相邻，从而将复杂的图转化为信息密集的序列。

这一设计使 GVT 的 VQ-VAE 实现了近乎完美的分子重建率。如果模型无法准确复现已见过的分子，就难以生成可靠的新分子。GVT 在此基础上表现扎实。

第二步是「学语法」。有了「词典」后，自回归 Transformer 开始学习如何将这些「单词」组合成化学上合理的「句子」（即分子）。Transformer 学习分子「单词」间的排列规律，例如哪个基团后面通常连接哪类基团。生成新分子时，它会像写作一样，逐个输出「单词」，最终构成一个完整的新分子。

**性能和速度，这次可以兼得**

GVT 在 ZINC250k、MOSES 和 GuacaMol 等标准测试集上表现出色。在衡量生成分子与真实药物分子相似性的 FCD（Fréchet ChemNet Distance）和 KL 散度等关键指标上，GVT 的分数优于顶尖的扩散模型。

这表明 GVT 生成的分子不仅化学结构合理，其化学空间分布也更接近类药分子。

GVT 的速度优势源于其离散的自回归生成过程，避免了扩散模型耗时的迭代去噪计算。对于计算辅助药物设计（CADD）团队，这能缩短探索化学空间的时间，加快研发迭代。

GVT 证明了离散隐空间模型通过精巧设计，其性能可以媲美连续模型（如扩散模型），并在效率和实用性上更具优势。这也启示我们，在追逐新技术时，审视经典方法或许能带来更优的解决方案。

📜Title: Graph VQ-Transformer (GVT): Fast and Accurate Molecular Generation via High-Fidelity Discrete Latents  
🌐Paper: https://arxiv.org/abs/2512.02667v1

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OCx7iabeU4eZPgicyCmaJuuQ2sibJyISThxXrVrtJibgpsulyQ9AbxBXs1A/640.png)

## 4\. Transformer 新架构：用分子已知属性预测未知属性

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7O7AXdLNRibpCykKOvP0muDZVWTvMibjPiazssbB0Te05EeAHibbdbXTUMAQ/640.jpg)

在药物研发中，我们总要和不完整的数据打交道。

一个项目里有成百上千个化合物，我们可能测定了一部分分子的溶解度，另一部分的细胞活性，还有一小部分的代谢稳定性。最终的数据集就像一块满是窟窿的瑞士奶酪。传统的定量构效关系 (QSAR) 模型需要分子结构才能预测性质，无法利用这些已经测得的宝贵数据。

新的 Transformer 架构能直接用已知性质预测未知性质。例如，它能仅凭溶解度 (logS) 和脂水分配系数 (logP) 来预测细胞渗透性 (Caco-2)，无需分子的化学结构。它将一个分子的一系列理化性质看作一个「句子」，并通过 Transformer 的序列处理能力发现性质间的关联。

首先，模型有一个特殊的嵌入层 (embedding layer)，能明确区分「缺失」的数据点和「零」值。在化学数据中，一个零值和一个「未测量」是两回事。

其次，它的自注意力机制 (self-attention mechanism) 能学习不同性质间的「化学直觉」。例如，它会发现脂水分配系数高的分子，溶解度通常不高。这种性质间的内在关联是预测的基石。

最后，模型的输出端是可变的，需要预测什么就输出什么。这让一个模型就能应对各种数据缺失情况，无需为每种情况单独训练模型。

在一个包含 1600 万个分子和 23 种性质的数据集上，模型得到了验证。在只提供性质、不提供结构的情况下，模型预测的 R² 值达到 0.75 到 0.85，表明仅靠性质间的关联就能做出可靠预测。这甚至优于许多单纯依赖结构的 QSAR 模型。其原因在于，很多理化性质本身就是分子结构特征的浓缩体现。

在药物早期发现阶段，化合物的各种性质通常分批次、分阶段测定。这个工具可以随时利用已有数据，去「填补」那些未测或因成本高而放弃测量的性质，从而加速化合物的筛选和优化，节省时间和经费。

例如，当一个苗头化合物合成路线长、只测了几个基本参数时，可以用这个模型预测其更复杂的 ADME 属性，提前判断它是否值得投入更多资源深入研究。

📜Title: Generalized Molecular Property Imputation Using a Flexible Transformer Architecture  
🌐Paper: https://doi.org/10.26434/chemrxiv-2025-ztp34

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OCx7iabeU4eZPgicyCmaJuuQ2sibJyISThxXrVrtJibgpsulyQ9AbxBXs1A/640.png)

## 5\. AI 双引擎驱动抗菌肽发现

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OsRBkre2hWCNEdbvhoIIiaNEO1xOkDTjtKJ6dOQ4BW3icX7RoicIzSn2Tw/640.jpg)

耐药菌威胁紧迫，陆地资源日渐枯竭，寻找新型抗生素的目光转向深海。高压、低温、黑暗的极端环境，迫使微生物进化出独特的防御机制——抗菌肽（AMPs）。

既往预测模型常因训练数据偏差失效。数据库中序列长度分布不均，且充斥着测序或表达技术引入的 N 端甲硫氨酸伪影。模型若习得这些噪音，预测结果便毫无价值。

XAMP 框架首要任务是清洗数据。团队构建平衡数据集，剔除干扰，确保模型学习到真实的生物学特征。

**XAMP 的核心在于「双引擎」设计**。

如同矿山寻宝，单纯依赖高精度扫描效率低下，仅凭肉眼又易遗漏。XAMP 结合两者优势：

1. **XAMP-T（Transformer 引擎**）：充当高效探矿员，利用 Transformer 架构快速从海量宏基因组数据中圈定潜在区域。
2. **XAMP-E（ESM-2 引擎**）：引入大语言模型（LLM）技术，利用 ESM-2 模型深度表征蛋白质序列，对初步筛选样本进行高精度确认。

组合拳成效显著：XAMP 中位 AUC 达 0.972，较现有顶尖工具提升约 10%。在药物研发中，这 10% 往往决定成药率。

为验证实战能力，研究人员分析了 238 个深海宏基因组样本，成功识别出 2355 个高置信度抗菌肽候选物。

通过宏蛋白质组数据交叉验证，确认这些预测肽段在深海环境中真实表达，而非算法生成的幻觉。

该工作展示了一条极具潜力的药物发现管线：利用 ESM-2 等蛋白质语言模型结合多组学数据，能有效从极端环境挖掘生物活性分子。

📜Title: A Global Discovery of Antimicrobial Peptides in Deep-Sea Microbiomes Driven by an ESM-2 and Transformer-based Dual-Engine Framework  
🌐Paper: https://www.biorxiv.org/content/10.1101/2025.11.20.689422v1

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7OnG5nOJwZib1y0A2ia2r9TdToib5sTh17qYhnGbAkH8X7qOHwzHtI0W2KA/640.png)

## 6\. BioMedGPT-Mol：能读懂分子语言的 AI 化学家

![alt](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/WaicZuM2mxM3wKM6H8wTvZgPWwXviasz7Oplbt1hewV0jCyP5daTnCxTvDcewBblVAYxibclF7XiaTkEAlm4MrrgNg/640.jpg)

大语言模型（Large Language Model, LLM）在化学领域常犯低级错误。例如，它们无法正确解析 SMILES 字符串中的括号和数字，导致输出化学上无效的结构。

BioMedGPT-Mol 采用不同思路，将一个通用大模型培养成化学专家，而非从零开始构建新模型。

其核心方法是多任务学习。BioMedGPT-Mol 将分子命名转换、分子描述、性质预测、反应预测等多个任务打包，用一个数据集统一训练。

这种训练方式促使模型寻找任务间的底层规律，理解分子的 IUPAC 命名、SMILES 线性表示及其生物活性之间的内在联系，从而建立对化学世界的认知。

模型引入了特殊标记（special tokens），为 SMILES 字符串、IUPAC 名称等不同类型的化学信息打上标签。助模型准确区分和解析不同化学语言，减少混淆，提高生成结果的准确性。

模型还需要解决实际问题。逆合成路线规划是一项复杂的化学任务。研究者采用三阶段微调策略训练模型：首先学习从反应物到产物的正向反应，然后学习从产物反推反应物，最后进行端到端的规划训练。

结果显示，BioMedGPT-Mol 在逆合成规划基准测试集 RetroBench 上表现出色。这表明模型具备了解决实际合成问题的能力，而不只是一个知识库。

BioMedGPT-Mol 的成功表明，将通用大模型的推理能力通过专业数据和训练方法「嫁接」到特定科学领域，是一条可行路径，或许优于为每个领域都开发全新的 AI 模型。

📜Title: BioMedGPT-Mol: Multi-task Learning for Molecular Understanding and Generation  
🌐Paper: https://arxiv.org/abs/2512.04629v1

— 完 —

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/WaicZuM2mxM3fmx2gJiaXuvVg8vxSTG8qI2712ANOJ39BicP34aicWnZuRuFrqxro2IhtiaD7qTJBpGT2GB7MP5zdrA/0.png) 

 榴莲忘返 AIDD 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/WaicZuM2mxM3fmx2gJiaXuvVg8vxSTG8qI2712ANOJ39BicP34aicWnZuRuFrqxro2IhtiaD7qTJBpGT2GB7MP5zdrA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
