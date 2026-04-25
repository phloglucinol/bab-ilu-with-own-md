---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483994&idx=1&sn=12dcf7e3887707614fdd72d9309f3c8c
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483994&idx=1&sn=12dcf7e3887707614fdd72d9309f3c8c
source_domain: mp.weixin.qq.com
title: BioRxiv 2025 | MedSAGE：Diffusion 终于学会像药化专家那样“拼积木”了
author: 
published_at: 
fetched_at: 2026-04-25T02:04:05Z
extractor: wechat_worker
content_hash: ad062ebf388999f8de07d611dccac7fc21c1d8dfb0194d3cf77635545d4befd4
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/pUZwvicbdez4Be1yRkC74mDkElT7LU8qvKictxTUibuJzAJ2ZJJ6hr8eqKGLqVW8xGS915575ufsUWvF70n0iaRn6w/0.jpg) 

# BioRxiv 2025 | MedSAGE：Diffusion 终于学会像药化专家那样“拼积木”了

原创 陷入鞍点 陷入鞍点 [ 陷入鞍点 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在 AIDD 的生成赛道上，我们正经历着一场痛苦的 “恐怖谷效应” 。 过去两年，基于全原子（All-atom）的 Diffusion 模型（如 DiffSBDD, EDM）虽然在数学上很性感，但生成的分子却让药化专家直摇头： 键角诡异、环系扭曲、充满不存在的化学键 ——即使 Glide 打分再高，造不出来就是废纸。

问题出在哪？ AI 把分子当成了 物理坐标点云 ，而人类专家把分子看作 功能模块的拼装 。语言不通，自然鸡同鸭讲。

今天解读的 MedSAGE （Molecule Generation via Retrieval and Diffusion），来自斯坦福 Ron Dror 组（分子动力学与 AI 的顶级豪门）。这项工作不仅是一个新模型，更是一个 范式转移（Paradigm Shift） ：它放弃了“从零捏原子”，转而拥抱 “基于检索的生成（Retrieval-Augmented Generation）” 。

简单说： 它不再试图画出每一个像素，而是学会了去仓库里找现成的“乐高积木”来搭房子。 这可能是目前最接近“图灵测试”的分子生成模型。

01

核心动机：拒绝“为了生成而生成”（The Why）

痛点：连续空间的“诅咒”

现有的 SOTA 模型大多在连续的坐标空间里“硬算”。

   * 高维灾难 ：生成一个药物分子涉及几十个原子的坐标预测，自由度极高，误差稍微累积一点，苯环就变成了“塌陷的大饼”。
   * 化学失语症 ：模型不懂“生物电子等排体”，不懂“优势骨架”，它只知道最小化几何损失。

洞察：药化专家的脑回路是 FBDD

作者的核心洞察极其犀利： 药物发现本质上是一个 FBDD（基于碎片的药物设计）过程。 如果我们把问题从“预测 50 个原子的坐标”简化为“预测 5 个碎片的类型和位置”， 复杂度将呈指数级下降 。而且，如果我们强制模型从一个合法的“碎片库”里 检索（Retrieve）组件，那么生成的局部结构天然就是 100% 合理且可合成的 。

02

方法拆解：架构师眼里的 MedSAGE（The How）

MedSAGE 的工作流像极了一位资深建筑师的设计过程： 选材 -> 布局 -> 施工 。

第一步：建立“数字乐高库”（Representation Learning）

作者没有用简单的 One-hot 编码，而是构建了一个 语义丰富的碎片空间 。

   * 输入：从 PubChem 等数据库中提取数千个高频药化碎片。
   * 编码：使用 GVP-GNN （几何向量感知图神经网络）提取碎片的 3D 结构特征和物理化学性质。
   * 结果：将离散的碎片映射到一个连续的 潜在空间（Latent Space） 。在这个空间里，苯环和吡啶靠得很近（性质相似），而和长链烷烃离得很远。

第二步：扩散模型做“布局”（Diffusion for Layout）

这是核心引擎。给定一个蛋白口袋，模型不生成原子，而是生成 “幽灵碎片” （Ghost Fragments）。

   * 扩散过程：模型在口袋里通过去噪过程，逐渐显现出若干个“重心点”和“方向向量”。
   * 双重预测：不仅预测位置（Where），还要预测潜在向量（What）。比如，模型在疏水口袋位置生成一个向量，这个向量在库里解码后对应的是“异丙基”。

第三步：检索与连接（Retrieval & Assembly）

这是最精彩的“落地”环节，也是其他模型所缺失的。

   * 检索（Retrieval）：拿着模型预测的潜在向量，去碎片库里搜索（KNN Search）最近似的真实碎片。这一步保证了局部结构的绝对正确。
   * 连接（Connector）：怎么把撒在口袋里的碎片连成一个分子？作者设计了一种 并行束搜索（Parallel Beam Search） 算法。它尝试在邻近碎片间建立化学键，并利用物理能量函数（如 Glide）作为打分器，剪枝掉不合理的连接，保留能量最优的拓扑结构。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Hk1BhEwZmyiao3zeQc2UcBxOWgvLgF4LIjN2I390vbJRh8tcuclIvCOR1ac1ticH3ewBdfn3LiaQZzSiaj7PFJArXQ/640.png)

这张图展示了 MedSAGE 的灵魂—— RAG（检索增强生成） 在分子层面的应用。c) ：碎片库被压缩进 Latent Space，这是模型的“词典”。e) ：扩散模型在口袋（灰色）中生成了几个彩色的球（Anchor points），这些球不仅有位置，还隐含了“我是谁”的信息。通过检索真实碎片并连接，最终“拼”出了完整的分子。注意，这一步是 离散 的，彻底消除了原子坐标微小偏差带来的几何扭曲。

03

实验结果：全方位碾压（The Evidence）

作者在 CrossDocked2020 数据集上，选取了 25 个具有代表性的靶点，与 DiffSBDD、Pocket2Mol 等 SOTA 模型进行了“生死局”较量。

1\. 亲和力（Vina/Glide Score）：断层式领先

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Hk1BhEwZmyiao3zeQc2UcBxOWgvLgF4LISH39gzvhtFdLINrKMkh8JZOlGFCLdIAAG0lt41YD0NHctGMzu6sJnA/640.png)

请看图 (a) 的箱线图。MedSAGE（深蓝色）生成的分子亲和力分布，几乎与 Reference 分子（红色，已知的高活性药物）持平，甚至在某些靶点上更优。相比之下，基于原子的 DiffSBDD（浅蓝色）虽然也能生成，但分数分布明显偏低。这说明 “拼凑好碎片”比“堆砌好原子”更容易获得高活性。

2\. 药化性质（QED & SA）：这才是“人”设计的

   * SA Score (合成可及性)：这是工业界最看重的指标。MedSAGE 生成分子的 SA Score 均值约为 3.4 （越低越好），非常接近真实药物（\~3.2）。而全原子模型往往飙升到 4.5-5.0，意味着那是“PPT 分子”，根本合成不出来。
   * 多样性：基于检索并没有限制想象力。数据显示，MedSAGE 生成了大量训练集中未见的全新骨架（Scaffold），证明它不是在死记硬背，而是学会了 迁移学习 。

3\. 捕捉“活性悬崖”（Activity Cliffs）

这是一个非常有意思的测试。作者测试了模型是否对微小的结构变化敏感。结果表明，由于 MedSAGE 是基于碎片替换的，它能极其敏锐地捕捉到 Bioisosteric Replacement（生物电子等排替代） 带来的能量变化。这意味着它可以作为先导化合物优化（Lead Optimization）的利器。

04

案例分析：不仅是对，而且“美”（Visual Proof）

我们来看几个真实的生成案例，感受一下算法的“审美”。

Case 1: Aurora Kinase

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Hk1BhEwZmyiao3zeQc2UcBxOWgvLgF4LI0xB9F495R2yfpP7ycuypnjZYAe8DcHibW7lObonJPrS2Jn7hJV7YGTg/640.png)  

MedSAGE 及其精准地在铰链区（Hinge Region）放置了一个 氨基嘧啶 母核，与关键残基形成了经典的双齿氢键。这是激酶抑制剂设计的教科书式操作！而它生成的侧链延伸到了溶剂区，增加了溶解度。

Case 2: Dopamine Transporter

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Hk1BhEwZmyiao3zeQc2UcBxOWgvLgF4LIrBMfXaowpLT1PwHDwKepiaIm9ChHKSw7VfLBqicwmsIugIdNVUxPicwOw/640.png)

模型识别出了口袋深处的两个疏水空腔，分别填入了两个苯环，并通过一个刚性连接子（Linker）将它们固定在特定的二面角上。这种对构象限制（Conformational Constraint）的理解，通常只有经验丰富的药化专家才具备。

Case 3: The target is the gp120 subunit of the HIV-1 envelope trimer (PDB 6MTN)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/Hk1BhEwZmyiao3zeQc2UcBxOWgvLgF4LIXhiaFcaGmcMYrW5D1boIcpAzoHtCtSrzhdbjUAMICCxxtFoaWVsycBg/640.png)

The reference ligand, cmpd 484, is an analog of BMS-626529 (temsavir), an approved antiretroviral medication.

05

优缺点与避坑指南（The Verdict）

优点 (Pros)

   * 落地性极强：生成的分子 100% 由常见药化碎片组成，天然保证了子结构的合成可及性。这是对全原子生成的最大降维打击。
   * 物理与数据双驱动：扩散负责“想象力”（探索构象空间），检索负责“守规矩”（化学有效性），连接算法负责“物理自洽”（能量打分）。三者结合得非常巧妙。
   * 效率恐怖：相比于几亿分子的虚拟筛选，MedSAGE 直接在口袋里“生长”分子，效率提升了两个数量级。

局限与挑战 (Cons)

   * 连接算法的算力瓶颈：虽然扩散很快，但最后的 Beam Search 连接步骤涉及大量的物理打分，这在计算上是昂贵的。如果分子碎片过多，推理速度会显著下降。
   * 受限于“词汇量”：模型的上限取决于碎片库的质量。如果库里没有某种特殊的、新颖的弹头（Warhead）或大环结构，模型永远无法生成出来。 它无法发明全新的化学反应。
   * 对口袋构象敏感：这是一个 Rigid-Receptor 模型。如果 AlphaFold 预测的口袋是闭合的（Apo），模型可能根本塞不进碎片。

工业界落地建议

   * Scaffold Hopping（骨架跃迁） ：这是 MedSAGE 的杀手锏应用。当你被专利困住时，用它固定关键药效团，重组骨架，快速绕过专利壁垒。
   * FBDD 项目加速：在 Fragment Hit 拿到后，利用 MedSAGE 做 Growing，比人工脑补要快得多。

06

深度思考：AIDD 的下一个篇章（Takeaway）

MedSAGE 的出现，标志着生物计算正在经历 NLP 领域的演进路线：从 End-to-End Generation 转向 RAG (Retrieval-Augmented Generation) 。

它告诉我们一个深刻的道理： 与其让神经网络在几十亿个参数里死记硬背化学规则，不如给它一本字典（碎片库），教它查字典。 这种“符号主义”与“连接主义”的融合，才是通往 可解释、可信赖、可落地 AI 制药的必经之路。

07

Q&A

Q1: MedSAGE 是如何把 LBDD 的“碎片拼接”强行移植到 SBDD 的？它如何解决坐标、词表和能量的深层矛盾？

核心逻辑：从“砌砖”到“摆家具”的范式降维。

传统 SBDD 模型试图预测每个原子的绝对坐标（x,y,z），如同装修时一块块砌砖，稍有误差墙就歪了。MedSAGE 的做法则是 “摆家具”：它不生成点云，而是直接在蛋白口袋里预测刚体框架（SE(3) Frames）——即预测“这里该放个苯环（质心位置 ，并且“它应该正对着深处的空腔（旋转角度）”。

关于词表爆炸与碎片切割的巧妙平衡：

针对药化碎片数量成千上万导致的“词表爆炸”，MedSAGE 放弃了传统的 Softmax 分类，改用连续潜在空间（Continuous Latent Space）。模型预测的是一个抽象的特征向量，再通过 KNN 去检索库里最接近的真实碎片。这不仅避开了计算瓶颈，还赋予了模型“插值”能力——即便没见过某个具体碎片，也能找到功能相似的“平替”（Bioisosterism）。而在切割方式上，不同于 BRICS 这种为了合成反应服务的“二维剪刀”，MedSAGE 选择保留具有稳定 3D 构象的刚性子结构。它存储的是带有特定空间形态的“积木块”，而非简单的化学图谱。

能量悖论的解决方案：

至于“局部低能不等于整体低能”的难题，MedSAGE 采取了 “先猜后修”的策略。扩散模型利用等变网络（Equivariant GNN）先给出一个没有严重碰撞的“粗糙布局”，随后利用物理打分（如 Glide）和 Beam Search 进行连接与松弛。它不奢求一步生成全局最优，而是提供一个极佳的初始构象（Initial Guess） ，让物理引擎去完成最后的一公里。

Q2: 这不就是高级版的“拼图游戏”吗？如果有两个碎片距离很远，模型怎么处理 Linker？

MedSAGE 的机制允许在检索到的碎片之间自动插入简单的 Linker（如亚甲基、醚键等）来满足价键要求。更重要的是，扩散模型在训练时就学会了碎片间的 隐式密度分布 ，它不会把两个需要连接的碎片放得太远。如果真的很远，它会在中间生成第三个“桥接碎片”。

Q3: 既然用了检索，那会不会存在严重的 Data Leakage（数据泄露）？生成的分子是不是都在训练集里见过？

虽然“积木”是旧的，但“房子”是新的。实验表明，生成的分子中只有极少部分（<5%）与训练集重合。绝大多数分子是利用旧碎片组合出的 全新拓扑结构 。这正是 FBDD 的魅力——有限的词汇，写出无限的诗篇。

Q4: 论文中对比的虚拟筛选（VS）效率提升令人震惊（MedSAGE top 1% 相当于 VS top 0.001%）。但这是否只是因为它生成的分子“更像”训练集里的类药分子，从而在同样有偏的评分函数（Glide）上占便宜？这是一种“过拟合”吗？

这是一个非常尖锐且正确的问题。这确实可能是一种针对“Glide打分函数”的过拟合。但需要拆解来看：

1）目标过拟合：是的，如果评分函数有系统偏差，任何优化该分数的模型都会继承这个偏差。这是整个领域依赖打分函数的通病，非MedSAGE独有。

2）化学空间过拟合：MedSAGE通过片段库隐式学习了类药化学空间，其生成分子分布自然与训练集（经类药性过滤的PDB配体）相似。但这恰恰是它的设计目标——生成类药分子，而不是随机化学分子。因此，这更应被视为“利用先验知识”，而非有害的过拟合。

真正的检验在于湿实验：这些“像药”的分子，是否真的比随机库分子有更高的实验验证命中率？这是下一步关键研究。

Q5：片段级表示的局限在哪里？如果我想生成的分子恰好不在你的片段组合空间里怎么办？

这确实是一个权衡。MedSAGE的片段库覆盖了\~3500个药物化学相关的官能团，能够组合出的化学空间已经非常大（理论上是片段数的排列组合）。但你说得对，某些exotic结构——比如含硼药物、宏环、共价warhead——目前确实不在MedSAGE的表示范围内。不过这恰恰是MedSAGE的设计初衷：通过限制搜索空间来提升生成质量。未来可以针对特定场景（如PROTACs、分子胶）构建专门的片段库。

Q6：MedSAGE用Glide作为打分函数，但众所周知docking score和真实亲和力相关性有限。有没有考虑用更现代的AI打分函数？

Glide确实有其局限性，特别是对某些靶点存在系统性偏差。但作者选择Glide有几个原因：(1) 它是工业界的标准工具，便于大家复现和对比；(2) AI打分函数虽然在很多benchmark上表现更好，但普遍性和鲁棒性还有待验证；(3) 使用同样的打分函数评估所有方法，至少保证了比较的公平性。未来结合AI打分函数（比如GNINA或新一代的结合自由能预测器）是一个很自然的扩展方向。关键是要避免"training-evaluation bias"——用同一个AI模型既做生成又做评估。

Q7: 作为一个“刚性”模型，MedSAGE 的真实边界在哪里？是否存在“刷分”嫌疑？未来 AIDD 将如何演进？

局限性：刚性的代价与 Linker 的软肋。

MedSAGE 最大的命门在于 “刚性假设”。它默认蛋白口袋和碎片都是刚体，这导致它在处理诱导契合（Induced Fit） 或隐蔽口袋时无能为力——蛋白不是石头，它是会呼吸的。此外，基于局部邻近性的连接算法对 Linker（连接子） 的处理较为生硬。对于像 PROTAC 或分子胶这样需要长柔性链跨越两个药效团的场景，MedSAGE 极易失效，甚至强行生成不合理的碳链，这是“局部最优”策略的天然缺陷。

关于“过拟合”的辩证思考：

其在虚拟筛选中恐怖的效率提升（Top 1% 命中率），确实引发了 “针对打分函数过拟合”的质疑。但这更像是一种“良性的先验植入” 。MedSAGE 通过碎片库隐式地学会了“类药空间”的分布，它生成的分子天然就比随机生成的原子堆更符合药化直觉。只要这种“过拟合”是指向真实的类药性（Drug-likeness）而非单纯的数据集记忆，它就是有价值的。当然，最终的裁判权必须交给湿实验。

未来的演进方向：从“拼图”到“生长”。

下一代模型必须打破刚性枷锁。我们期待MedSAGE V2.0 版本引入柔性碎片生成（Flexible Fragment Generation），允许在生成过程中优化碎片的内部扭转角。更长远的目标是实现蛋白-配体的协同折叠（Co-folding），让口袋侧链配合分子的生成而重排。最后，必须引入反应感知（Reaction-aware），如果两个碎片在几何上能连但在烧瓶里连不上，模型应当给予惩罚。那时的 AIDD，将不再只是画图纸，而是在设计合成路线。

08

头脑风暴

这篇工作让小编想起一个更大的问题： 生成式AI在小分子领域为什么一直落后于蛋白质设计？

蛋白质有天然的语法：20种氨基酸、线性序列、有限的二级结构motif。AlphaFold学会的是"氨基酸序列→3D结构"的映射，RFdiffusion学会的是"在二级结构约束下设计序列"。这些都是well-defined的、有物理意义的任务。

但小分子呢？没有统一的"词汇表"，连接规则复杂得多，化学空间是离散的组合爆炸。原子级表示把这个问题搞成了一个"在10^60空间里找针"的游戏。

MedSAGE的insight是： 不要硬来，降维 。用药化社区几十年积累的片段知识来约束搜索空间。这其实是一种很聪明的"归纳偏置注入"——你不是让模型从头学习什么是苯环，而是告诉它"苯环是一个单元，你只需要决定放不放"。

这预示着一个趋势： 未来成功的小分子生成模型，可能都需要在表示层面做深度的领域适配 。不是"大力出奇迹"地扔更多数据和参数，而是巧妙地编码先验知识。

另一个值得关注的点是 与虚拟筛选的融合 。MedSAGE不是要替代VS，而是提供了一种"生成→匹配"的新范式：先用生成模型高效探索化学空间的高亲和力区域，再回到商业库里找可买的类似物。这可能是当前最务实的落地路径。

* 参考文献：Powers, Alexander S., et al. "MedSAGE: Bridging Generative AI and Medicinal Chemistry for Structure-Based Design of Small Molecule Drugs." bioRxiv (2025): 2025-05.

  
本文为个人解读，如有疏漏或理解不当之处，欢迎指正交流。觉得有价值的话，欢迎转发分享\~

本公众号主要介绍AIDD中小分子、多肽、PROTAC的前沿算法、综述、评估。欢迎关注本公众号获取领域最新文献解读。

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
