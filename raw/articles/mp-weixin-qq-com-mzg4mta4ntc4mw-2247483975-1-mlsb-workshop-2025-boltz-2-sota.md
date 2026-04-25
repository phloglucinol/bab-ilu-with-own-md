---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483975&idx=1&sn=c9682b4fb805b41f564f36a941dcd01f
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483975&idx=1&sn=c9682b4fb805b41f564f36a941dcd01f
source_domain: mp.weixin.qq.com
title: MLSB Workshop 2025 | Boltz-2 的滑铁卢：当 SOTA 结构模型在亲和力预测上输给“纯序列”
author: 
published_at: 
fetched_at: 2026-04-25T02:04:12Z
extractor: wechat_worker
content_hash: 3c1df875060717ecbc8b15c4c3bad38dac022941d96c8ada5ce611ffda46b58b
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/pUZwvicbdez4vjdI51jiczvS0VaZjWElZaLCxUfSHqzfemzCxQu0RDwziah8ORvt9WU2wksZ7OglXGaAcPIzcR1kw/0.jpg) 

# MLSB Workshop 2025 | Boltz-2 的滑铁卢：当 SOTA 结构模型在亲和力预测上输给“纯序列”

原创 陷入鞍点 陷入鞍点 [ 陷入鞍点 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

作者：James King, et al. (Synteny, London) 一句话省流：不要迷信“结构就是一切”。在预测 PPI 结合能这件事上，昂贵的几何深度学习（Boltz-2）竟然被“不懂几何”的语言模型（ProtT5/ESM2）按在地上摩擦。

编者按：泡沫破裂的声音

自从 AlphaFold 和 Boltz 系列模型横空出世，AIDD 圈子里弥漫着一种“结构傲慢”：我们理所当然地认为，既然 AI 已经能精准预测原子坐标，那预测结合能岂不是探囊取物？毕竟物理化学告诉我们，结构决定能量，对吧？

今天介绍的这项工作，来自伦敦 Synteny 团队，它是一份极为珍贵的“清醒剂”。作者试图将 Boltz-2 强行转行，从“建筑师”（预测结构）变成“鉴定师”（预测亲和力）。

结果令人大跌眼镜：在这个任务上，算力消耗巨大的结构大模型，输给了仅仅基于序列的 BERT 类模型。 这不仅是一个负面结果（Negative Result），更揭示了当前 AI for Science 的一个深层隐忧：我们的模型学会了“画出”分子，但可能根本不懂分子之间为什么会“相爱”。

---

01 核心动机：试图捅破最后这层窗户纸 (The Why)

在 PPI（蛋白-蛋白相互作用）药物开发中，我们有两个终极问题：

1. Pose Prediction：它们怎么结合？（AlphaFold/Boltz 已经基本解决了）
2. Affinity Prediction：它们结合得有多紧？（目前的痛点）

传统的 FEP（自由能微扰）太慢，传统的打分函数（Scoring Functions）太糙。大家的直觉是：Boltz-2 的 latent space 里应该藏着物理规律。 如果我们把这些表征提取出来，加个回归头（Regression Head），是不是就能得到一个完美的  预测器？

作者的核心假设（Hypothesis）非常直接：结构模型的信息量 > 序列模型，所以 Boltz-2 微调后理应秒杀 ESM2。

但事实真的如此吗？

---

02 方法拆解：如何把“结构脑”改装成“能量脑”？(The How)

作者并没有重新训练 Boltz-2（那太贵了），而是采用了“冻结主干 + 适配器微调”的策略。这在工业界非常常见，既省钱又快。

1.架构改造：从几何到能量的映射

* 输入流：Boltz-2 处理后的 MSA（多序列比对）和 Pair Representations（成对表征）。这是模型的精华，它编码了残基对之间的距离、角度信息。
* Affinity Head（亲和力探头）：
   * 原生 Boltz-2 有一个针对 Protein-Ligand 的模块，但不能处理 Protein-Protein 的对称性。
   * 魔改点：作者设计了一个 Cross-pair Pooling 层。简单来说，就是把所有残基对的特征“揉”在一起，压缩成一个标量（Scalar）。
   * 大白话：模型看着两个蛋白接触面上一堆复杂的化学键，最后必须给出一个打分：“这俩关系很铁”或者“这俩只是路人”。

2.Loss 设计：排位赛机制

作者敏锐地发现，直接预测绝对数值（MSE Loss）很难，因为实验数据的噪音很大。

* 双管齐下：
* Ranking Loss：这就好比教模型，你不需要告诉我 A 和 B 的准确战斗力，你只要告诉我 A 比 B 强 就行。这在同一个靶点筛选不同突变体时非常有效。

---

03 实验结果：残酷的真相 (The Evidence)

这是全篇最精彩、也最让人深思的部分。作者在 TCR3d（T细胞受体）和 PPB-affinity（通用PPI）两个数据集上进行了测试。

1.降维打击的反转

看看这张数据对比表，序列模型简直是“乱拳打死老师傅”：

* 解读：你没看错。在 TCR 数据集上，复杂的 Boltz-2 相关系数只有 0.15（几乎是随机猜测）。而在通用数据集上，ProtT5 以 0.48 的成绩碾压了 Boltz-2 的 0.33。
* 潜台词：你辛辛苦苦折叠了半天，还不如我不看结构直接猜准。

2.是结构算不准，还是模型不懂能量？

有人会辩解：“肯定是 Boltz-2 预测的结构有误差（Docking Error），垃圾进垃圾出嘛。” 为了堵住这个借口，作者做了一个绝杀实验（Ablation Study）：

* 实验设置：不再让 Boltz-2 预测结构，而是直接把 PDB 里的真实晶体结构（Ground Truth）喂给模型。
* 结果：Pearson r 仅仅从 0.153 提升到了 0.159。
* 结论：这是致命一击。 这说明问题根本不在于结构准不准，而在于 Boltz-2 的 Embeddings 本身就没有包含足够的“热力学信息”。它学会了“几何互补（Geometric Fit）”，但没学会“结合强弱”。

---

04 深度解析：为什么会输？(The Post-Mortem)

作为一个 AIDD 从业者，我们不仅要看热闹，更要看门道。为什么会出现这种反直觉的现象？

1. 进化信息的降维打击： ESM2 和 ProtT5 是在数亿条序列上训练的。进化是最高级的能量筛选器。 两个残基之所以共进化（Co-evolution），就是因为它们在空间上相互作用并维持了结构稳定。序列大模型隐式地“背诵”了这些能量规律，而 Boltz-2 虽然显式地重建了结构，却可能在复杂的几何变换中丢失了这些统计学上的能量信号。
2. 几何  能量：
   * Boltz-2 的训练目标是 RMSD（位置偏差）。只要原子位置对了，Loss 就很低。
   * 但结合能  对位置极其敏感。氢键角度偏几度，范德华力距离差 0.5 埃，能量可能差出 10 倍。
   * 目前的结构 Embedding 太“粗”了，它能分辨“形状匹配”，但分辨不出“电子云的爱恨情仇”。
3. 冻结主干的代价： 由于显存限制，作者冻结了 Boltz-2 的主干。这意味着模型无法通过反向传播去调整其底层的几何表征来适应“能量预测”这个新任务。这就像让一个只会造房子的建筑师（结构预测）去鉴赏古董（能量预测），还不让他学习新知识，只能靠最后一眼的感觉。

---

05 优缺点与落地建议 (The Verdict)

优点 (Pros)

* 学术诚实：发表 Negative Results 是对社区最大的贡献，避免了大家重复造轮子。
* 控制变量严谨：通过使用“真实结构”作为输入，彻底排除了结构预测误差的干扰，逻辑闭环非常漂亮。

局限 (Cons)

* 数据饥渴：TCR3d 只有几百个数据点，微调几亿参数的模型确实容易过拟合。
* 缺乏物理约束：模型完全是数据驱动的，没有引入物理势能项（Physics-informed），导致它在没见过的数据上泛化能力很差。

给药化/算法专家的建议：

1. 如果你在做 First-in-class 筛选：
   * 请继续使用 ProtT5 或 ESM2 结合简单的 MLP/XGBoost。这是目前的性价比之王。
   * 不要盲目相信结构大模型的打分。
2. 结构有什么用？
   * 用 Boltz-2/AlphaFold3 来做 Filter（过滤器）。比如，如果模型预测两个蛋白根本碰不到一起，那就直接扔掉。
   * 但如果它们结合了，不要问模型结合得紧不紧，它真的不知道。
3. 未来的机会：
   * 真正的突破点在于 Physics-AI 融合。未来的模型不能只是 Transformer，它必须在 Embedding 层融合物理力场（Force Field）的信息。

06 结语

这篇论文告诉我们，AI for Science 还没有到达“奇点”。 我们造出了能“看见”微观世界的显微镜（AlphaFold/Boltz），但我们还没有造出能“感知”微观力量的天平。

序列依然是王道，直到结构模型学会物理的那一天。

---

互动 Q&A 

一些小编的问题 + GPT的答案，仅供参考\~

Q1：如果对 Boltz-2 解冻主干进行全参数微调（Full Fine-tuning），结论会反转吗？

理论上会有提升，但实际上是一场赌博。目前的亲和力数据集（如 SKEMPI）太小了（\~1k 数据量），去微调一个数亿参数的模型，极大概率会发生灾难性过拟合（Catastrophic Overfitting）。除非我们能搞到药企内部百万级的 DEL 库数据，否则“冻结主干”是目前算力和数据约束下的最优解。

Q2：那我现在拿到一个 PPI 项目，到底该怎么算结合能？

实话实说，目前最稳妥的流程是：

* 用 AlphaFold/Boltz 预测复合物结构。
* 用 Rosetta/Schrodinger 等传统物理工具基于这个结构做 Relax 和打分。
* 用 ESM2 提取序列特征做辅助排序。 这种“AI 结构 + 物理打分 + 序列统计”的混合流（Hybrid Workflow），目前比单用任何一个端到端模型都要靠谱。

Q3：有没有一种可能，不是“结构模型”不行，而是 Boltz-2 这种“为了折叠而生”的模型本身就存在原罪？微调一条只会搭积木的狗去抓老鼠，方向是不是一开始就错了？如果不微调，而是重新设计一个结构模型，有机会超越序列模型吗？

问题很可能不在于“微调（Fine-tuning）”这个动作，而在于 Boltz-2（以及 AlphaFold）的“预训练目标（Pre-training Objective）”与亲和力预测任务之间存在本质的 Misalignment（错位）。

* “静态几何” vs “动态热力学”的鸿沟

Boltz-2 的训练目标是最小化 FAPE 或 RMSD。换句话说，它学习的是“如何把原子堆得像 PDB 里的晶体一样”。
* 晶体的陷阱：PDB 里的结构是静态的、低能态的快照。Boltz-2 只要记住这个“最终形态”就算赢了。
* 亲和力的本质：结合能 ΔG=Gcomplex−(Gprotein+Gligand)ΔG\=Gcomplex−(Gprotein+Gligand)。它不仅关乎复合物（Complex）长什么样，更关乎未结合态（Unbound State）长什么样，以及结合过程中熵（Entropy）的损失。
* 结论：Boltz-2 这种模型，先天缺失了对“未结合态”和“构象动态变化”的感知。它只看到了结果，没看到过程。而序列模型（ESM）通过学习进化历史，隐式地捕捉到了蛋白质在自然界中为了保持功能（结合）而必须维持的动态稳定性。

* 微调救不了“特征流形（Feature Manifold）”的缺陷

当我们冻结 Boltz-2 主干时，我们假设其 Latent Space 已经包含了亲和力信息，只是需要提取出来。但现在的证据表明，这个假设可能不成立。
* Boltz-2 的 Latent Space 可能是按照“形状互补性”组织的，而不是按照“相互作用强度”组织的。
* 在一个形状完美的界面上，可能因为几个隐蔽的静电排斥或去溶剂化惩罚（Desolvation Penalty），导致亲和力极差。这些物理细节在以 RMSD 为导向的特征空间里，可能被视为“噪音”被滤掉了。

* 重新建模是唯一的出路吗？

是，但仅仅换架构（Architecture）没用，必须换数据和 Loss。

如果重新训练一个结构模型，想让它超越序列模型，必须引入以下变革：
* Physics-Informed Pre-training：不能只喂 PDB 坐标，要喂 MD（分子动力学）轨迹。让模型看懂蛋白质的“呼吸”，看懂水分子是如何在界面上起桥梁作用的。
* Energy-Aware Loss：训练时必须引入物理势能项（Force Field terms）或直接对大规模的亲和力数据（如 Mega-scale Mutational Scanning）进行端到端训练。

总结：不要指望从一个只会“搭积木”的模型里，通过简单的微调就能榨出“量子化学”的智慧。下一代的 SOTA，一定不是 Boltz-2 的补丁，而是一个懂物理、懂动态的全新物种。

  
* 参考文献：King, J. et al. On fine-tuning Boltz-2 for protein-protein affinity prediction. Preprint at https://doi.org/10.48550/arXiv.2512.06592 (2025).

  
---

本文为个人解读，如有疏漏或理解不当之处，欢迎指正交流。觉得有价值的话，欢迎转发分享\~

本公众号主要介绍AIDD中小分子、多肽、PROTAC的前沿算法、综述、评估。欢迎关注本公众号获取领域最新文献解读。

预览时标签不可点

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
