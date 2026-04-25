---
type: raw_article
source_url: https://mp.weixin.qq.com/s/Jvq7kBzKrw-q2siQSa3f5Q
canonical_url: https://mp.weixin.qq.com/s/Jvq7kBzKrw-q2siQSa3f5Q
source_domain: mp.weixin.qq.com
title: 文献阅读 | NMI 2024 EquiScore: 基于物理先验知识整合和数据增强的通用蛋白质-配体相互作用评分
author: 
published_at: 
fetched_at: 2026-04-25T02:04:30Z
extractor: wechat_worker
content_hash: 5039570c99f8fc2258a238337410011e3b77aa5f1153155fa3a1ce0fa5b6bd5e
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VOPV9ut4U72YWJ96D7Pgbb9OfUZ6NtgZKPgCSONR1u1VJQErElZ1Ljw/0.jpg) 

# 文献阅读 | NMI 2024 EquiScore: 基于物理先验知识整合和数据增强的通用蛋白质-配体相互作用评分

原创 石头 石头 [ AI模型与算法 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

  
原文标题：Generic protein–ligand interaction scoring by integrating physical prior knowledge and data augmentation modelling

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VzwX8zffE3K2QFbOacdLAIEtSibswibeHf7rwJjo5gCz20Vm38wB5Vblg/640.png)

**摘要**

稳健的蛋白质-配体相互作用评估方法的设计与开发是一个长期存在的难题。基于数据驱动方法可能会使得模型过拟合于配体和蛋白质的训练数据，而非学习到蛋白质-配体之间相互作用的信息表达。**本文提出名为 EquiScore 的评分方法，该方法利用异质图神经网络整合物理先验知识，并在等变几何空间中表征蛋白质-配体相互作用。**除此之外，本文采用**多种数据增强策略**和**严格去冗余方法**构建大规模数据集训练模型的泛化性能。在两个大型外部测试集上，与其他 21 种方法相比，EquiScore 展现较好的评估性能。当 EquiScore 与不同的对接方法结合使用时，能有效提升这些对接方法的筛选能力。此外，EquiScore 在一系列结构类似物的活性排序任务中也表现出色，这表明其具有指导先导化合物优化的潜力。

**引言**

分子对接任务旨在为蛋白质大分子组找到特异性配体，一旦获得高质量的蛋白质结构，基于结构的虚拟筛选（SBVS）可以筛选出最适配的分子进行新药的合成和设计。尽管该领域已取得重大进展，但开发在实际应用场景中具有更高准确性的评分方法仍是一个未解决的挑战。目前，基于机器学习或深度学习的评分方法在算法和网络架构设计方面取得了重大进展。然而，最近的研究表明基于机器学习的评分方法在预测新靶标亲和力方面泛化能力较差。主要原因大概分为两方面：一方面，**机器学习模型容量的不断提高使其能够拟合整组训练数据。同时，训练数据和测试数据之间的数据泄漏（训练数据和测试数据存在重复和相似情况）问题导致对这些模型能力的评估过于乐观。**同时，从训练集中学习到并非任务核心本质的特征或模式的模型可能对数据集分布的微小变化高度敏感，从而阻碍了它们对分布外数据集的预测性能。另一方面，现有PDB数据库中可训练数据较少，并且不同数据集存在数据偏差，这也会导致模型泛化性能的下降，这些因素极大地限制了在现实场景中的应用潜力。

本研究主要从两个方面着手，以提高深度学习评分方法在未见过的靶点上的泛化能力。首先，为减少数据集偏差，**研究通过三种数据增强方式构建新数据集 PDBscreen。从数据库中收集了更多阳性（高质量）样本，通过重对接生成更多阳性样本以及利用交叉蛋白对接和结合形状筛选的分子生成模型来生成更具迷惑性且更多样化的阴性配体分子，以减少构建虚拟筛选（VS）训练数据集的偏差**。另外，本研究引入了一种等变的异质图神经网络学习蛋白质-配体的特征信息表达，包括通过新增化学相关节点和边的类型以及信息感知注意力机制，物理分子间相互作用的先验信息整合。其中，信息感知注意力模块能够处理来自不同方面的相互作用信息，**包括等变几何信息、化学结构信息和蛋白质 - 配体经验相互作用成分**。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6V1sCEaiaqXZN0ejMzmTiaxsp1OtJMLlkXKuAYLicw5NibRD8hcQIJS0zgfw/640.png)

图1 构建 PDBscreen 数据集的流程。左栏展示了从 PDB 数据库收集数据的流程图，右栏则说明了构建数据增强的示意图。

**PDBscreen数据集构造**

**PDB 数据库数据收集：**首先，下载 PDB 数据库中的所有蛋白质-配体复合物（截至 2021 年 7 月有 180,207 个条目）; 然后，保持分辨率优于2.5 Å的晶体结构;使用化学成分词典过滤掉内源性配体、结晶添加剂以及共价结合类型的配体。最后，仅保留配体分子量在 150–900 道尔顿（Da）之间的复合物，保证数据集与药物设计场景的相关性。

**重新对接收集：**首先，对前期从 PDB 筛选获得的蛋白 - 配体复合物，使用对接软件（如文中的 Glide 模块）重新执行对接计算，生成配体的多个预测构象。然后，保留与实验晶体构象的 均方根偏差（r.m.s.d.）< 2 Å的近天然构象以及重新对接后排名最高的构象，每个复合体最多保留五个构象，避免单一样本的构象过度冗余。同时，为了进一步保证PDBscreen的数据能量合理性，PDBscreen中只保留对接分数小于-5 kcal mol-1的构象。

**交叉蛋白质对接：**首先，分别借助UniProt数据库（存储蛋白序列与功能信息）和SMILES 格式实现对蛋白质和配体身份标识的唯一化。然后，与传统 “交叉对接（cross-docking，不同配体→同源蛋白）” 策略不同，本文实验设计为：每个配体 → 配对 10 个 UniProt ID 不同的蛋白（即同一配体，对接 10 种结构不同的蛋白），构建配体 - 蛋白对。对于每对配体-蛋白质，检索公共数据集排除已知复合物，实现假阴性规避；最终，交叉蛋白对接产生的 阴性样本数量是阳性样本的 10 倍。交叉蛋白对接构建了 “配体相同、蛋白异源且无已知结合” 的阴性样本集，既保证阴性样本的真实性（规避假阴性），又通过规模放大增强模型的泛化能力。

**生成诱饵分子：**使用生成模型 DeepCoy，为 每个 PDB ID 对应的蛋白 - 配体复合物 生成 500 个诱饵分子，来扩展阴性样本的化学多样性。对生成的 500 个诱饵，通过分子对接（molecular docking） 技术，预测它们与靶蛋白结合时的 3D 构象。借助 Schrödinger 的 Shape Screening 模块，计算诱饵构象与晶体配体（真实结合态）的 3D 形状重叠度，最终，按形状重叠度从高到低排序，仅保留排名前 5 的诱饵构象作为最终阴性样本。构造了“形状像真实配体、但实际不结合” 的高迷惑性阴性样本，逼迫模型学习更精准的结合模式。

**数据去冗余：**数据删除流程主要为避免数据泄漏以保证模型评估准确性，具体是在评估模型对未见过靶点的泛化能力时，基于蛋白质的 UniProt ID，移除训练集中与外部测试集（DUD-E、DEKOIS2.0）中蛋白质具有相同 UniProt ID 的数据，在先导化合物优化场景中则基于 LeadOpt 中蛋白质的 UniProt ID 对 PDBscreen 数据集进行去重，被移除的训练数据用作内部测试数据供后续注意力分析。

**模型架构设计**

EquiScore 的架构以蛋白质 - 配体结合构象为输入，先构建异质图，包含蛋白质和配体的原子节点及芳香环虚拟节点，边涵盖几何距离边、结构边（共价键）和基于相互作用指纹（IFP）的边以整合物理先验知识；再通过嵌入层将节点和边特征映射到潜在空间；随后经 EquiScore 层（含信息感知注意力、节点更新、边更新模块）进行特征提取与融合，确保等变性；最后将配体特征送入任务层，通过多层感知机输出评分以预测蛋白质 - 配体相互作用。

令![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/PZI7pLaVibDMXVEEgUqia8FOyUe4Siau4ZsE17gXbyLPEicOj4kqdicRlHReZ6JyliaH9lqVM4AUMZK4VnTticUxSKQN4aIsRAlEh0v/640.svg)表示蛋白质 - 配体相互作用图。其中，![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/PZI7pLaVibDMXVEEgUqia8FOyUe4Siau4ZsTR8BaxkXVlmS6Y743IZF500XrKL6UH7XUdY7P4QvicG7zHCqqD3r28ibropfp2qNOH/640.svg)为节点集，n 为节点数量；![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/PZI7pLaVibDMXVEEgUqia8FOyUe4Siau4ZsiaGy0KeibFHRUZ1gjoE4gCpcQ5SroBCOTIQ4ITh15GdYFCV0icktUuHdhgsepswzMmQ/640.svg)为基于几何距离的边集，m 为几何边的数量；![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/PZI7pLaVibDMXVEEgUqia8FOyUe4Siau4Zsy9KCqb5cwsGlyU4lU6L8Sd81yiaKdUpQaedIsIC0lFbu0gzHNkUs2jAjuGniaenSpC/640.svg)为基于共价键或相互作用指纹（IFP）信息的边集，k 为结构边的数量。每个节点（U）或边（e）分别有向量 h 或 m 表示其相关信息。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VC45NldxYe2TVcg6E02bkqw2ddjNQbzIPSgVUH6yKowdIwL8FQOib2Dg/640.png)

图2 EquiScore 的整体架构如下：a. 构建异构图作为输入；b. 利用嵌入层将特征初始化到潜在空间；c. 通过 EquiScore 层进行特征提取与融合；d. 将配体的特征输入任务层，以预测蛋白质 - 配体相互作用。

如图2，EquiScore 构建蛋白质和配体的异质图作为输入，主要通过EquiScore 层进行特征提取与融合，包括该层包含三个子模块：信息感知注意力模块、等变消息传递模块（节点更新模块）以及边更新模块。

**信息感知注意力模块：**该模块借助注意力机制感知节点间物理先验信息。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VxvZibT34Wc35qsWRPibelWgOfVibfic0vWzzicgIhbegAIMicYOr05W9waaA/640.png)

另外，为了利用异质图上的三维信息来帮助模型捕捉距离依赖性，该模块构造基于几何的边上的相对距离矩阵 Egeometric，其被用作基于相对距离的门控机制，以控制从每个节点到目标节点的信息流强度，得分公式计算如下：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VcobfmiaGbAZPH48VrjibFwGT1EHHO2ugYBmq7pN8sMiaQd0XctEqWnmicA/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6V0Le4Y0GV6FnQYDXGKuQDQHwtXyaeqWFlkhKAMH1licJYQDwXSlf1gSw/640.png)

为进一步利用图中基于几何的边的信息，同时保留复合物的化学先验信息，引入了边偏置模块。在该模块中，共价边上的预定义特征矩阵E\_structural通过以下公式作为偏置项

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VmHbPhaYqfGxbicVic7rHX8Mz7NTQgu1D7XSOx7a0S1LNRf9G001GHrAw/640.png)

**等变消息传递模块（节点更新模块）:** 遵循 E (n) 等变图神经网络（EGNN）更新节点的标量和向量表示，确保了 EquiScore 的等变性质，其中，![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/PZI7pLaVibDMXVEEgUqia8FOyUe4Siau4ZsicKtjxz9YJ687IbadkGKMlzhuhw8DN6694OsluS1gk7F3XA9K11rSiaT53EI9aAWU6/640.svg)是信息感知评分矩阵（scoreinfo-aware）中的一个元素，它代表边的特征：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VqT6VyHnL24V4Ts4fXLQhAUSeJibdnZXPibUkmQlX3wORetSEsIppDMNA/640.png)

**边特征更新模块：**本文设计了边特征与节点的交替迭代更新来提升模型的表达能力与泛化能力。先计算信息感知注意力矩阵![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/PZI7pLaVibDMXVEEgUqia8FOyUe4Siau4Zs4tp8iamC5EiajbCbb8DqEn7fBgAIjWPdnBpf7Y9ibIZE81Eu1PGukwqYsa2aicz10Hkia/640.svg)，该矩阵整合了几何距离门控信息与结构边偏差，包含边的重要性权重；二是节点更新模块输出的最新节点特征（标量![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/PZI7pLaVibDMXVEEgUqia8FOyUe4Siau4Zs2MJagZN1a13rd9uCODIppHktvLnrDs8e4tutibYOPhcj0pLCVX1d59WpFk50etsgib/640.svg)和向量![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_svg/PZI7pLaVibDMXVEEgUqia8FOyUe4Siau4Zsib5jfNYhMqMQfRI9M0yUlaiaiahCicqjEJTQ1r8gpgIRYSVGKGQRy4fqX1r6hAKX2SGP/640.svg)，确保边特征与节点状态同步。解决了单一节点更新可能忽略边特征动态变化的问题。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VFbJ3xVmdsXDujdOMibWfpA6DrKIqZk1ScUu9UdhRtLicN7iaXNv5a3J0A/640.png)

最后，本文通过公式添加这部分信息，以更新基于结构的边上的特征矩阵

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VbLeuyic7wn6RERn8U5j9lTcyugBf3BMmPBnnJ4gjSR5XuY62Cr8ibPGA/640.png)

**模型的训练与推理**

**分子对接设置**：在对接设置中，对蛋白质的优化通过 Schrödinger 的Maestro 模块中 Protein Preparation Wizard 完成，包括添加氢原子、分配键序、填补缺失的侧链和环、移除配体 5Å 以外的水分子、优化氢键网络，并使用 OPLS-2005 力场最小化系统至重原子的均方根偏差（r.m.s.d.）收敛到 0.30Å。

配体处理方面，在 LigPrep 中利用 Epik 模块获取目标 pH 7.0±2.0 下可能的电离状态，再用 OPLS-2005 力场生成能量最低的配体构象作为对接起点；为减轻因过度代表的骨架导致的类似物偏差，仅保留对接得分最佳的同分异构体，确保每个独特分子仅一个对接构象。

受体网格由 Receptor Grid Generation 模块生成，内盒为 10Å×10Å×10Å（以共晶配体直径中点为中心），外盒从内盒各方向延伸 10Å。最终，所有配体 - 蛋白质对接通过 Schrödinger 的 Glide 模块（v.8.9）在标准精度模式下进行。

本文从训练数据中移除了与相关数据集中蛋白质具有相同 UniProt ID 的数据，然后随机选择 10% 的 UniProt ID，并选取其对应数据作为训练的验证集。将蛋白质 - 配体相互作用图中属于配体的节点提取出来，并输入到任务层。使用加权和操作作为读出池化函数，通过以下公式得到图级别表示：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VJN5tKhdkajWyGKwDHGmYTIpyTKLrnffKqUoU5m9nzU2EF4m4BYSALg/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VibZKhL5OeGU4uL06x2naqaPibibicz7PlO9VoYYYW7ZEHA5WptubXxrv9Q/640.png)

最后，EquiScore 使用交叉熵作为损失函数。其表达式如下式：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6V3NsZULQ9buS0m4wGmlticeLAr5KqR1wg7EoliaPXXco2u9E0xpH1Z8OA/640.png)

**实验设计与结果**

对比模型选择：选取了 Kdeep、3D-GNN、PIGNet，以及 TANKBind、RTMScore、DeepDock 作为基线模型。

核心指标：聚焦于蛋白质 - 配体结合活性预测的关键指标如AUROC（分类能力）、BEDROC（早期识别能力）、5.0% EF（富集因子）等，重点评估模型在 “未见过靶点” 场景下的泛化能力，以及先导化合物优化场景中的表现。

实验数据集基于 PDBscreen 数据集构建，通过 “交叉蛋白质对接” 生成阴性样本（同一配体对接不同蛋白，排除已知相互作用对），并结合 DeepCoy 生成的高迷惑性诱饵分子作为补充阴性样本；训练前按 UniProt ID 去重（移除与测试集蛋白 ID 重叠的数据），随机选取 10% UniProt ID 对应数据作为验证集。外部测试集：采用 DUD-E 和 DEKOIS2.0 数据集，用于评估模型对 “未训练过的新靶点” 的泛化能力，这两个数据集均为行业公认的蛋白质 - 配体结合预测基准集。特定场景测试集：使用 LeadOpt 数据集，针对先导化合物优化场景（评估模型对同系列化合物结合活性的预测能力），进一步验证模型在药物发现实际环节中的适用性。

**虚拟筛选性能评估实验（DEKOIS2.0 和 DUD-E 数据集）**验证 EquiScore 在未见过的蛋白质靶标上的泛化能力，与 21 种现有方法对比。DEKOIS2.0上EquiScore 在 AUROC（0.821）和 5.0% EF 上排名第一，BEDROC（0.460）排名第二；去重后（11 个靶标）仍保持优势。在DUD-E数据集：整体 AUROC 仅次于 TANKBind（0.776 vs 0.778），但去重后（12 个靶标）排名第二，性能远超其他机器学习方法，仅略低于传统方法 Glide SP。特别地，其他基于 PDBbind 训练的方法在数据去重后性能显著下降， EquiScore 泛化能力稳定。实验结果表明EquiScore较强的泛化性能。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VNiaD1HrU5SviaxG8EibIcH3VyRLOMUNa7E2UQSDCMXezuGbic4rYLF4RLw/640.png)

图 3 22 种评分方法在DEKOIS2.0 数据集上的评估（以 AUROC、BEDROC 和 EF 为指标）。a-e，从 AUROC（a、d）、BEDROC（α=80.5）（b、e）和 5.0% EF（c、f）三个方面对评分方法进行评估。箱线图中的蓝色三角形代表每个分组的平均值。所有方法按其平均值排序。a-c 中的结果基于完整数据集（数据点数量 n=102）；d-f 中的结果基于与 PDBbind2020 去重后的数据集（数据点数量 n=12）。所有箱线图均包含中位数线：箱体表示四分位距（IQR），须线表示在 ±1.5×IQR 范围内的其余数据分布。

**重打分能力实验（与多种对接方法结合）**验证 EquiScore 作为重打分工具对不同对接方法的提升效果。将 EquiScore 与 AutoDock Vina、GOLD 等 5 种对接方法结合，在 DEKOIS2.0 上评估筛选性能。所有对接方法经 EquiScore 重打分后，EF（1.0%）、BEDROC、AUROC 均显著提升。例如，AutoDock Vina 的 1.0% EF 从约 10 提升至 30，Glide SP 的 AUROC 从 0.7 提升至 0.8 以上，证明其增强对接方法筛选能力的通用性。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQYvxbFiaKkP5TzdlrRgxGE6VjHNWqUBlxcUicSSpia6taI7E7TnlJvngicia2J3FsiazwJX9zibAw83KRJHA/640.png)

图 4 EquiScore 在 DEKOIS2.0 数据集上对不同对接方法生成的对接构象进行重打分的性能比较。a-c，在 EF（前 1.0%）（a）BEDROC（α=80.5）（b）和 AUROC（c）方面的性能。

**总结与展望**

本研究开发了通用蛋白质 - 配体相互作用评分方法 EquiScore。首先构建了含多种数据增强策略 PDBscreen 数据集，通过近天然配体结合构象扩大阳性样本，以生成的高欺骗性诱饵增加阴性样本；其次基于该数据集，采用整合蛋白质 - 配体相互作用物理及先验知识的等变异质图架构训练模型；随后评估显示，在虚拟筛选场景中，EquiScore 在 DEKOIS2.0 和 DUD-E 的未见过蛋白质上，性能优于 21 种现有方法；在先导化合物优化中，仅弱于 FEP+，且计算成本更低，速度与准确性更均衡；同时，其对不同对接方法生成的构象有稳健重打分能力，可提升虚拟筛选性能；此外，模型具有可解释性，能捕捉关键分子间相互作用，为合理药物设计提供线索，有望助力对人类健康疾病的理解及新药研发。

  
参考文献

Cao D, Chen G, Jiang J, et al. Generic protein–ligand interaction scoring by integrating physical prior knowledge and data augmentation modelling. Nature Machine Intelligence, 2024, 6(6): 688-700.
  
  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQb8OicgkP7oleLXsqQia00MWOIswgycMSQRMEmMyRTbqsHehISSOCIHYkNKp7ibKWlCiahfyma29XzErw/0.png) 

 AI模型与算法 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/h7gllneBWQb8OicgkP7oleLXsqQia00MWOIswgycMSQRMEmMyRTbqsHehISSOCIHYkNKp7ibKWlCiahfyma29XzErw/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
