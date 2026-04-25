---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4ODkwMjUxNw%3D%3D&mid=2247487143&idx=1&sn=bafca69d1b865d736f3e91020f26dafd
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4ODkwMjUxNw%3D%3D&mid=2247487143&idx=1&sn=bafca69d1b865d736f3e91020f26dafd
source_domain: mp.weixin.qq.com
title: JCIM | Diff-Shape：把 ControlNet 搬进分子生成，形状约束与骨架创新如何兼得
author: 
published_at: 
fetched_at: 2026-04-25T02:03:08Z
extractor: wechat_worker
content_hash: b00af426bb0ce39abe11ae016b56c00252ed99d27889cf61cd8bbe2b5316e59d
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/tm5Cx87BXvo4wsNOCT3vokmd1dL7aN3ibD043NmiaLlJROYMUg0eTKsvrBxiaicib2DSmbN3HG7K5Oy1GWcLwhvm8jsnUy81zSvphdqsVIVZtscE/0.jpg) 

# JCIM | Diff-Shape：把 ControlNet 搬进分子生成，形状约束与骨架创新如何兼得

原创 Bits & Bases Bits & Bases [ Bits & Bases ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

👆 点击上方 Bits & Bases 加入我们

🧬 Bits & Bases # 95  
Diff-Shape：把 ControlNet 搬进分子生成，形状约束与骨架创新如何兼得  
  
阅读时间：约 25 分钟 | 难度：⭐⭐⭐⭐

---

# 📄 推荐论文档案

* **论文标题：** De Novo Molecular Design via Shape-Constrained Diffusion Models
* **研究团队：** Bohao Li, Xinyu Wu, Yu Cao, Yuedong Yang, Mingyuan Xu, Jinsai Shang, Hongming Chen 等（广州国家实验室、中山大学）
* **发表期刊：** Journal of Chemical Information and Modeling (2026)
* **研究方向：** AI 辅助药物设计、3D 分子生成、形状约束生成模型

---

## 00\. 引言

形状相似性（shape fidelity）和结构新颖性（structural novelty）之间的矛盾，是分子生成领域一个持续存在的问题。基于配体的药物设计（LBDD）依赖三维形状相似性来寻找新苗头，但如果生成分子与参考物结构过于接近，骨架创新的空间就很有限；反之若骨架差异过大，形状约束本身也就没有意义了。

在读这篇论文时，我发现它的切入角度颇有意思——并没有从头设计一个新的条件扩散模型，而是借鉴了图像生成领域 ControlNet 的工程思路：冻结预训练的无条件生成主干，通过一个轻量级控制分支注入形状约束信息。将这一思路迁移到 3D 分子生成领域，并结合子结构 inpainting 机制，就是本文提出的 **Diff-Shape** 框架。

方法层面，Diff-Shape 将形状约束与子结构约束整合进一个统一框架，不需要为不同参考形状或设计任务重新训练主干模型。实验层面，论文声称这是第一个提供湿实验验证的形状约束生成模型，在 KRAS G12D 和 EGFR 三突变两个靶点上合成了设计化合物并测定了纳摩尔级活性。

本期一篇讲完，覆盖：方法背景 → Diff-Shape 架构 → 基准测试结果 → 子结构约束生成 → SBDD 应用 → 两个湿实验案例。

---

## 01\. 背景：形状约束分子生成的方法演进

### 1.1 为什么需要形状约束生成

配体相似性药物设计的经典流程是：找到已知活性化合物，通过三维形状或药效团相似性搜索已有化合物库来寻找新苗头。这条路线的天花板在于化合物库的覆盖范围——无论如何筛选，都不可能找到库中没有的分子。形状约束生成模型的价值正在于此：直接采样与参考分子三维形状一致、但化学结构新颖的分子，将 LBDD 的适用范围从"筛选"扩展到"设计"。

### 1.2 已有方法的局限

论文梳理了该方向的主要已有工作，指出各自的问题所在。

基于强化学习的方法（如 Papadopoulos et al.）仅在 SMILES 序列层面操作，不直接生成三维构象，且每换一个参考形状都需要从头重训练智能体。Imrie et al. 和 Skalic et al. 将三维药效团信息编码为体素或 CNN 表示，但模型最终仍输出二维图或线性序列，未能在生成过程中直接处理三维几何。Zheng et al. 将形状感知设计建模为监督翻译任务，三维性质在生成后才被评估，而非在建模过程中施加约束。Roney et al. 通过在上千个形状筛选命中物上微调来偏向特定形状，每换参考结构就需重新微调，计算代价较高。

较新的 SQUID 是第一个可迁移的三维方案，采用自回归片段生长配合启发式成键几何，但仅在小分子上做了验证。ShapeMol 引入了以学习到的形状嵌入为条件的等变扩散模型，在 SQUID 基础上有所提升，但它是端到端的条件生成器——形状描述符在训练时已编码进模型权重，主要针对整体分子的全局形状条件化，不支持子结构约束（如固定特定片段或 R 基团）与形状约束的同时施加。

### 1.3 Diff-Shape 的核心出发点

Diff-Shape 的出发点是借鉴图像条件生成领域 ControlNet 的设计：**冻结预训练主干，训练轻量级控制分支**。同一个主干模型可以在不重新训练的情况下适配不同的参考形状和设计意图；控制分支只涉及少量参数，成本远低于端到端重训。通过引入 inpainting 机制，Diff-Shape 在推理时无需任何额外训练，即可在形状约束的同时保留用户指定的固定子结构，统一支持骨架跃迁、骨架修饰（R 基团替换）和连接片段生成三类任务。

---

## 02\. Diff-Shape 方法框架

### 2.1 整体设计

Diff-Shape 以 **MIDI**（Mixed Graph and 3D Denoising Diffusion for Molecule Generation）为主干——一个同时生成分子图和三维坐标的 SE(3) 等变扩散模型，能够处理原子类型、化学键和三维坐标的联合分布。在此基础上，Diff-Shape 添加一个名为 **GrCN（Graph ControlNet）** 的约束模块，冻结 MIDI 的参数，仅训练 GrCN 的可训练部分。

分子用图  表示，其中  是原子类型和形式电荷的拼接独热编码， 是化学键类型， 是原子坐标。

### 2.2 GrCN 架构

GrCN 由两部分组成（论文 Fig. 1b, d）：

**3D 生成模块**：是预训练 MIDI 的一份副本，参数锁定（θ），负责维持无条件生成先验。

**约束模块**：包含两份预训练 MIDI 的副本——一份参数锁定，另一份参数可训练（θ\_c）。可训练副本接受条件图 （即经模糊化处理的参考形状）作为输入，通过零权重初始化的 MLP 层（zero-weighted MLP，所有可学习参数初始化为零）与锁定副本的解码器层相连，形成类似 ControlNet 的跳跃连接机制。

零权重初始化的设计意义在于：训练伊始，约束模块的输出为零，GrCN 的行为与预训练 MIDI 完全一致，不受条件图干扰。随着训练进行，约束模块逐渐学会将条件信息注入去噪轨迹，同时不破坏预训练先验中已有的化学知识。这与图像领域 ControlNet 的核心设计思路相同。

约束模块的输出  与 3D 生成模块的输出  通过线性组合或门控残差组合（MixGR）融合，得到 GrCN 的最终输出：

其中  是控制约束强度的缩放因子。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tm5Cx87BXvrEFNMEFibYYX3vicIBwxENy72Ca4D7kPxZ6aUxky8LVxq9EZGBD5opIOojzpjB1lQWM3uAc0fyWkWcZ2EI0WwVcopSSBZz9ib2nA/640.png)

▲ 图 1（引自原论文 Fig. 1）：(a) Diff-Shape 的正向扩散与去噪过程；(b) GrCN 基本架构，含约束模块和 3D 生成模块；(c) 同时满足形状和子结构约束的去噪 inpainting 工作流（时间步 t）；(d) Diff-Shape 模型详细架构图。

### 2.3 形状条件的模糊化操作

给定参考分子的模板图 ，论文设计了七个层次的模糊操作，对模板信息进行不同程度的遮蔽，生成作为形状条件  的输入（论文 Fig. 2a）：

从信息量最完整到最模糊依次为：(1) 无模糊（保留原子类型、键类型、连接关系和坐标）；(2) 彩色混合点云；(3) 彩色点云；(4) 模糊元素；(5) 模糊元素和键；(6) 混合点云；(7) 点云（仅保留坐标，去除所有化学信息）。

论文用有效性×唯一性作为综合评分来比较七种方案。条件最宽松的点云模式综合得分约 0.57，而在混合点云基础上加入噪声水平 0.4 的方案得分为 0.583，略高于前者。总体规律是：条件越模糊，生成分子化学结构越新颖（二维相似性低），但三维形状约束相对宽松；条件越严格，三维形状保真度高但结构与参考过于相似。综合来看，后续实验均采用混合点云模式。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/tm5Cx87BXvoyCM0TgiakuSoa3mpelpL0ZZmrbVoKU2CXv4M94A1iaBCnuWhUykCDbNI4Wx6Pm7nNGhxia9ObVWfyxqa1E0k7cs1oYLl68erucE/640.png)

▲ 图 2a（引自原论文 Fig. 2a）：七种模糊操作的示意图。红色、蓝色、绿色、白色节点分别代表氧、氮、氟、碳原子。从左到右信息量依次减少，生成分子的二维化学相似性随之降低，结构新颖性提升。

### 2.4 形状约束 Inpainting：子结构约束的推理时实现

Diff-Shape 通过在推理阶段加入 inpainting 机制，无需重新训练即可同时施加子结构约束。

用户通过一个二值掩码（binary mask）标记参考分子中需要固定保留的子结构 ，其余部分由模型在形状约束下自由生成。在每个反向扩散步骤 t，操作分两步并行进行：对固定子结构加噪得到 ；对待生成部分在形状条件  下去噪得到临时生成结果 。随后，将两者按掩码合并：

其中  是标记固定原子的二值掩码。覆写操作保证了在最终生成步骤  时，固定原子与参考分子完全一致，其余原子则在形状条件和扩散先验的联合约束下自由生成。inpainting 完全在推理时执行，不涉及模型重建或重训练，可灵活应用于骨架修饰、骨架跃迁和连接片段生成等不同场景。

---

## 03\. 基准测试：形状约束生成性能

### 3.1 评估设置

以 GEOM-Drugs 数据集为主要基准，随机选取 100 个参考分子，每个参考生成 100 个分子，与 SQUID、ShapeMol（无引导和 0.5 权重引导两个变体）和无条件基线 MIDI 进行对比。评估指标包括：化学有效性（validity）、唯一性（uniqueness）、3D 形状相似性（Sim₃D，ROCS Shape Tanimoto 系数）和 2D 图相似性（Sim\_g，Morgan ECFP4 Tanimoto）。论文还引入 MIDI-i 作为消融基线，即直接用含噪点云初始化 MIDI，以单独衡量形状控制模块的贡献。

### 3.2 主要结果

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/tm5Cx87BXvoa4BM2uPNW2gBV5rvtn2ZDaKu5sywR6APVnPvNXWABUCYfX5DaAcGA8StCpRhLWRFia8DuaZQnf0aXX6G7gW8Ns7SkBJg8VQMU/640.png)

▲ Table 2（引自原论文 Table 2）：Diff-Shape 与基线方法在 100 个参考分子上的性能对比（GEOM-Drugs、ZINC、MOSES 三个数据集）。★ 表示 Diff-Shape 相对所有基线在该指标上显著更优（Holm 校正后 p < 0.001）。

在 GEOM-Drugs 数据集上，Diff-Shape-0.3（噪声水平 0.3）生成分子中 Sim₃D > 0.8 的比例达到 **0.913**，Diff-Shape-0.4 为 0.657；SQUID 为 0.126，ShapeMol 两个变体均低于 0.003。Diff-Shape 在所有基线中三维形状保真度最高，且在统计上显著优于全部对比方法（Holm 校正后 p < 0.001）。

在结构新颖性方面，对于二维相似性 Sim\_g < 0.3 的低相似性分子，Diff-Shape-0.3 和 Diff-Shape-0.4 中 Sim₃D > 0.8 的比例分别为 0.213 和 0.353，均显著高于 SQUID（0.055）和 ShapeMol（< 0.003）。即便在低二维相似性的约束下，Diff-Shape 的三维形状相似性仍仅略有下降——Diff-Shape-0.3 在全部生成分子中的中位 Sim₃D 为 0.91，在 Sim\_g < 0.3 子集中仍达到 0.84，说明形状约束与骨架创新之间的权衡在 Diff-Shape 中得到了较好的平衡。

消融实验中，MIDI-i 相比 MIDI 有所提升，说明坐标信息本身有助于形状相似性；但 Diff-Shape 在高形状保真度率和低相似性多样性方面均进一步优于 MIDI-i，说明性能提升不只来源于坐标注入，结构化的形状控制模块有其独立贡献。

在化学有效性方面，Diff-Shape 在 GEOM-Drugs 上略低于 SQUID 和 ShapeMol。作者对此有坦承的解释：在更大的 ZINC 和 MOSES 数据集上重训后，有效性分别提升至 0.842 和 0.912，接近 ShapeMol 水平，提示有效性偏低主要源于 MIDI 主干在 GEOM-Drugs 规模下的局限，而非控制模块本身。此外，三维几何合理性方面，Diff-Shape 在 GEOM-Drugs 和 MOSES 上的 PoseBusters 有效性均高于 SQUID 和 ShapeMol，说明其生成构象具有更好的物理合理性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tm5Cx87BXvqayn1vxFMZODfNl94OA4OIzice7MF3e7vOlMpyqd77yWWuENTxiciatFMGzpUibCaibiasUZzhicKwDeOWWqQwFHVicwKK9JsfDOrXync/640.png)

▲ 图 2c–e（引自原论文 Fig. 2c–e）：Diff-Shape 与基线方法在不同 2D 相似性截断（Sim\_g < 1.0、< 0.7、< 0.3）下的 Sim₃D 分布对比。即便在最严格的低相似性约束下，Diff-Shape 的形状相似性分布仍显著优于其他方法。

---

## 04\. 子结构约束生成：骨架修饰、跃迁与连接片段

论文在骨架修饰（scaffold decoration）、骨架跃迁（scaffold hopping）和连接片段生成（linker generation）三个任务上评估了 inpainting 机制的效果（Table 3）。每个任务选取 2 个参考分子，每个生成 250 个有效且唯一的分子，以无条件 MIDI + inpainting 为基线对比。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/tm5Cx87BXvqRjN85x3rTSPGavNOF9oPib3WVrzGHA3e3OLp3OUhmWE2ymLov0lo2qqIMskXibzHfOhektmH5yVAMiaP2hatuMibj8eE9gvEpOpY/640.png)

▲ Table 3（引自原论文 Table 3）：Diff-Shape 在子结构约束分子生成三类任务上的性能。指标为修改区域（magenta region）的 Sim₃D 和 Sim\_g，而非整体分子。

三类任务中，Diff-Shape 在修改区域的形状相似性方面均显著优于无条件 MIDI 基线。在骨架修饰和连接片段生成任务中，MIDI 的有效性分别低于 0.1，远低于 Diff-Shape，原因在于无条件 MIDI 在子结构约束下难以形成合理的成键关系；骨架跃迁中 MIDI 有效性为 0.54，Diff-Shape-0.3 仍有明显优势。

论文 Fig. 3b 展示了三类任务的代表性生成样例：固定区域（黑色部分）保持不变，修改区域（品红色部分）在保持参考分子整体形状的同时实现了明显的化学结构替换，三维形状相似性和二维图相似性均有标注。即使在 Sim\_g < 0.3 的低相似性约束下，仍有相当比例的生成分子达到 Sim₃D > 0.7（骨架跃迁任务中 Diff-Shape-0.3 为 0.351），而 MIDI 基线在这一条件下几乎为零。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/tm5Cx87BXvrS4iciccwaib9JHvTGMZbsn6v5h4uLwfj4R1xlPtNAyavbhU6o5GrOOyebsfMeLSFkj1SdIs0qRgKPiblQCcPNFvQ939aiarJAZh0M/640.png)

▲ 图 3b（引自原论文 Fig. 3b）：Diff-Shape-0.3 在骨架修饰、骨架跃迁、连接片段生成三类 inpainting 任务的代表性样例。左列为参考分子（黑色为固定区域，品红色为待修改区域），右三列为生成结果，括号内数字依次为修改区域 Sim₃D（黑）、修改区域 Sim\_g（蓝）、整体 Sim₃D（橙）。

---

## 05\. 结构辅助药物设计应用

论文进一步探索了 Diff-Shape 在结构辅助药物设计（SBDD）中的应用：以参考配体的 X 射线结合构象作为形状条件，生成分子后用 GLIDE 对接打分，评估结合亲和力。选取 PDBBind CASF-2016 核心集中的三个蛋白靶点（PDB IDs: 1z95、4cra、4w9c），每个靶点生成 1000 个分子。

比较对象包括口袋条件生成模型 DiffSBDD 和 Pocket2Mol（论文明确指出这并非方法层面的直接对比，而是为了展示当配体晶体结构可用时 Diff-Shape 的实际适用性）。结果显示，Diff-Shape-0.3 和 Diff-Shape-0.4 的对接分数分布总体优于所有对比方法（Fig. 4a–c）。作者认为这与形状引导的生成机制有关：参考形状约束使生成分子倾向于模仿参考配体的结合模式，因此对接姿态与参考一致，得分更优。Fig. 5 展示了三个靶点各三个代表性结合姿态，所有 Diff-Shape 生成结构的对接得分均优于参考配体。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tm5Cx87BXvq45NtT0tNZh9U7QXc7kiaToISprFyRaFFvg1cyGA3Qqg5EzPviaskMMFeonoxqfD8HC2ia973Uj4FQdfcicdsCwl04nLcv8CRJqzI/640.png)

▲ 图 4（引自原论文 Fig. 4）：三个蛋白靶点（1z95、4cra、4w9c）生成分子的 GLIDE 对接分数分布（a–c）及对应 3D 形状相似性和 2D 图相似性分布（d–f）。Diff-Shape 生成分子的对接分数总体优于所有方法。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/tm5Cx87BXvodUNhaVhJe0T7VbBH4778JsNqFUSxe4LjU4QyVnDpWIY61EKKIfNI09uVdBU72XvhBNf5vsEkN7Up10rgCt7au2VLew8aCLDg/640.png)

---

## 06\. 湿实验案例：KRAS G12D 与 EGFR 三突变

论文在此前所有形状约束生成模型中首次提供了湿实验活性数据，设计化合物经化学合成并通过酶活性检测确认了纳摩尔级活性。

### 6.1 KRAS G12D：R 基团替换

KRAS G12D 是 KRAS 基因第 12 位甘氨酸被天冬氨酸取代的常见致癌突变，广泛存在于胰腺癌、结直肠癌、肺癌等。MRTX1133 是目前最具代表性的 KRAS G12D 高选择性抑制剂，但因药代动力学性质不佳而终止临床开发。保留其吡啶并嘧啶骨架（pyridopyrimidine scaffold），替换侧链以改善性质，是合理的先导物优化策略。

Diff-Shape 以 MRTX1133 的晶体结合构象（PDB: 7RPZ）为输入，通过 inpainting 对醚侧链进行 R 基团替换，生成 1,291 个化学有效的三维分子。经化学合理性和形状相似性（Sim₃D > 0.7）筛选后，382 个候选物被对接至 KRAS G12D 活性位点；其中 223 个对接姿态与 MRTX1133 晶体构象的形状相似性 Sim₃D > 0.85。综合合成可行性和结构新颖性（SciFinder 检索确认未被报道），最终选定一个化合物 **KRASi** 进行合成（多阶段筛选流程见 Supporting Information Fig. S9）。

HTRF 酶活性检测结果（Fig. 6c）：KRASi 对 KRAS G12D 的 IC₅₀ = **10.21 nM**，与 MRTX1133（IC₅₀ = 7.09 nM）相当。KRASi 与 MRTX1133 的整体三维形状相似性 Sim₃D = 0.897（Fig. 6b）。对接结合模式分析（Fig. 6d, e）显示两者结合模式相似：KRASi 生成的侧链含酰胺连接基和带正电荷的末端甲胺基，与 E62 的负电荷侧链形成盐桥和氢键；环丙胺基团以类似 MRTX1133 醚基团的取向稳定侧链构象。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tm5Cx87BXvqovBe6xtCKodMm15iculuUiaWibWs90W78j9rFXCyHAsHp0XhzLicSTO3ukeuuxgZZjj0l3Z7Fp0NqxSxttAxqVwrUWuZ2aYyBcIA/640.png)

▲ 图 6（引自原论文 Fig. 6）：KRAS G12D 抑制剂设计案例。(a) inpainting 设计方案示意（固定吡啶并嘧啶骨架，替换醚侧链）；(b) MRTX1133 与 KRASi 的形状对比（Sim₃D = 0.897）；(c) KRASi 对 KRAS G12D 的剂量依赖抑制曲线（IC₅₀ = 10.21 nM）；(d, e) MRTX1133 和 KRASi 在 KRAS G12D 结合口袋中的结合模式对比。

### 6.2 EGFR L858R/T790M/C797S：骨架跃迁

EGFR L858R/T790M/C797S 三突变是非小细胞肺癌中常见的耐药形式，对一代和三代 EGFR 酪氨酸激酶抑制剂均产生耐药。BLU-945 作为第四代 EGFR 抑制剂，对该三突变体具有高效活性。

Diff-Shape 以 BLU-945 为参考，固定部分子结构（黑色区域，包含非异喹啉部分），对异喹啉核和相邻氮杂环丁烷（azetidine）进行骨架跃迁（红色区域，Fig. 7a）。生成 1,429 个化学有效的三维分子，筛选 143 个进行对接；其中 102 个对接姿态的 Sim₃D > 0.85（以 BLU-945 晶体构象为参考）。最终选定 **EGFRi** 进行合成，BLU-945 与 EGFRi 的 Sim₃D = 0.888。

酶活性检测结果（Fig. 7c）：EGFRi 对 EGFR L858R/T790M/C797S 的 IC₅₀ = **74.92 nM**，弱于 BLU-945（IC₅₀ = 7.073 nM），但已代表一个新型骨架的活性出发点。SciFinder 检索确认其 2-oxo dihydropyridoimidazole 骨架在 EGFR 专利中属于新型结构。对接模式分析（Fig. 7d, e）显示 EGFRi 保留了 BLU-945 大部分关键氢键相互作用，模型生成的环丁基成功模仿了 BLU-945 中氮杂环丁烷的连接作用，使末端砜基与 K716 形成氢键。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tm5Cx87BXvrHWkBQibaJX62rmroTTV8dNia9wtps4JFHexlnljmmO1XJ4YY6mbewDia3FiajBbYOiaCEwwN2ib7rxW5vVy14bhefKwlcKAF6XmIRc/640.png)

▲ 图 7（引自原论文 Fig. 7）：EGFR 抑制剂设计案例。(a) inpainting 骨架跃迁方案示意（红色为跃迁区域，黑色为固定区域）；(b) BLU-945 与 EGFRi 的形状对比（Sim₃D = 0.888）；(c) EGFRi 对 EGFR L858R/T790M/C797S 的剂量依赖抑制曲线（IC₅₀ = 74.92 nM）；(d, e) BLU-945 和 EGFRi 在 EGFR 结合口袋中的结合模式对比。

---

## 07\. 总结与延伸探讨

_(📍 个人观点与延伸探讨)_

读完这篇论文，有几点值得单独说说。

首先是 ControlNet 迁移这件事本身。把图像条件生成领域的一个工程范式搬到三维分子生成，在技术上并不复杂，但它解决的问题很实际：如何在不重训生成主干的前提下注入新的条件信息。对 AIDD 来说，训练高质量的 3D 分子生成主干成本相当高，如果每换一个条件类型就要重训，实际部署价值会大打折扣。Diff-Shape 提供的"主干复用、控制可插拔"思路值得关注。

然后是湿实验验证这部分。KRASi 和 EGFRi 的合成验证在该类工作中确实不多见，对方法的转化可信度有实质帮助。但需要注意的是，两个案例都是在已有高质量参考配体（MRTX1133 和 BLU-945）的基础上进行有限的局部修改：KRAS 案例固定了骨架替换侧链，EGFR 案例固定了大部分结构只替换较小区域。这验证的是"形状引导的局部替换能否在已知活性骨架上保留活性"，而非"从形状出发从头设计全新化合物"——这两类任务的难度差距相当大。论文本身对此没有过度宣称，这一定位是合理的，只是在理解工作边界时需要有所区分。

最后是化学有效性偏低的问题。论文在 GEOM-Drugs 上的有效性（0.831）低于 SQUID（0.994）和 ShapeMol（0.982），作者将其归因于 MIDI 主干本身的局限。在更大数据集上重训后有效性确实有所提升，这一解释有数据支撑。如果后续将 MIDI 主干替换为性能更强的 3D 生成模型，形状控制效果和化学有效性是否能同时改善，是个值得跟进的问题。

---

**Disclaimer**  
 本文为 Bits & Bases 学术笔记与深度解读，仅供参考。限于作者水平，文中难免存在理解偏差或疏漏，恳请各位同行专家批评指正。

---

Bits & Bases

专注 AI for Science · 深度笔记 · 庚续初心

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/tm5Cx87BXvoibI9EeJmt8qe2cky2eMqdFJUFLc05iapnqg3riam4QA36xUviax1piapIRI0GNKkvIksGaQJCtwjns2npSarSCzfUagGz0oMAVVzU/640.jpg)

👆 长按扫码，不错过每一篇硬核干货

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/0LlI74ApO0lPHPibiaVWrfFqQpPP2L7gNIoI4AEgZI9icElp0Ro35FMsic4ibQQpicEmD7nrKx5lox4frbNSrIjAfjHg/0.png) 

 Bits & Bases 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/0LlI74ApO0lPHPibiaVWrfFqQpPP2L7gNIoI4AEgZI9icElp0Ro35FMsic4ibQQpicEmD7nrKx5lox4frbNSrIjAfjHg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
