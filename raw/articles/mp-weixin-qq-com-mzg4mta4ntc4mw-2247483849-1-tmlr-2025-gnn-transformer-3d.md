---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483849&idx=1&sn=1253f8bd66218a93615610e789e82c2b
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483849&idx=1&sn=1253f8bd66218a93615610e789e82c2b
source_domain: mp.weixin.qq.com
title: TMLR 2025 | 告别 GNN？标准 Transformer 其实天生就会“懂” 3D 结构
author: 
published_at: 
fetched_at: 2026-04-25T02:04:12Z
extractor: wechat_worker
content_hash: e2663be217e086e5b59f69fad7959416d0c90d8507434c1906055f5f47322f18
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/pUZwvicbdez5iazqcJibofIoMPXpWAc0lyj92leOypAdhgsLvMibgyj335xefvwUjR7xcwz3p3zjT9NViaicCnu4yx8w/0.jpg) 

# TMLR 2025 | 告别 GNN？标准 Transformer 其实天生就会“懂” 3D 结构

原创 陷入鞍点 陷入鞍点 [ 陷入鞍点 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

本文解读的是发表在 Transactions on Machine Learning Research（TMLR 2025）的论文：Transformers trained on proteins can learn to attend to Euclidean distance，作者来自Oxford Protein Informatics Group。作者用一套非常“极简”的设计，证明了一个对 AIDD 很有冲击力的结论：不改架构、不加GNN，只要给标准 Transformer 喂坐标，它就能自己学会按欧氏距离“看世界”，并在多个蛋白任务上打平甚至超过专门的结构 GNN。

---

0 引言：当我们说“用结构”，到底要不要 GNN？

在过去几年，蛋白相关的 AIDD/CADD 模型几乎默认遵循一条“分工路线”：

* 序列 → 用 Transformer / PLM（ESM 家族、SaProt-Seq 等）；
* 结构 → 用 GNN / SE(3)-等变模型（EGNN、GVP、SE(3)-Transformer 等）。

这套范式在工程实践中有几个很现实的痛点：

1. 算效率瓶颈：GNN 依赖于边（Edge）的构建，随着节点数 NN 增加，全连接图的内存消耗是 O(N2)，且难以利用 FlashAttention 等针对 Transformer 优化的底层算子。
2. 模型复杂性：为了保证旋转平移不变性（SE(3)-invariance），我们设计了极其复杂的几何张量操作，导致模型难以训练且难以扩展。
3. 模态割裂
   * 序列和结构各有各的编码器，最后再“拼一起”，多模态融合往往靠工程技巧，而不是统一的表示空间。

同时，AlphaFold3 / Proteina / SimpleFold 等新一代结构模型给出了另一个信号： 它们越来越少依赖专门的等变 GNN，而是直接用 “坐标 + Transformer” 完成三维推理。

这篇 TMLR 的工作，本质上是在回答一个被工程实践反复暗示、但一直缺少理论解释的问题：

标准 Transformer（pre-norm, dot-product attention），到底能不能原生地学会欧氏距离和三维结构？ 如果能，它内部是在做怎样的几何计算？

作者的答案是：可以，而且还“挺聪明”。

---

1 方法概览：从 Q·K 到高斯距离门

这篇工作可以拆成三层理解：

1. 理论层：Attention = 高斯距离核？
   * 作者从 1D/3D 位置嵌入出发，推导出：  
    在合适的坐标 embedding + LayerNorm 下，Q·K 点积可以近似为“负的平方距离”， softmax 之后就变成了形如 exp(-α‖xᵢ - xⱼ‖²) 的高斯距离核。
   * 每个 head 的 “α” 可学习，于是自然形成了“不同空间尺度的高斯滤波器”。
2. simulated experiment model 层（点云）  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez5iazqcJibofIoMPXpWAc0lyjI8XYibLfCCZq9iaJdZicC4Fehz7b2Ua0OueDiag9hqdOUibJKftUuyaCFUA/640.png)
   * 搭一个极简的 Transformer，只输出单个 head 的未归一化 attention；
   * 让它去拟合exp(-‖xᵢ - xⱼ‖^p)这类函数，看最容易学的是哪一种；
   * 顺带评估：在 Rⁿ 里学距离，需要多少个 head 维度（d\_head）才够用。
3. 蛋白建模层（真实任务）
   * 搭一个 6 层、768 hidden、12 头的“迷你版 ESM”， 分别训练“只看序列”和“序列 + Cα 坐标”两个模型；
   * 任务包括：masked LM、GO 功能预测、ProteinGym zero-shot 变体效应、接触图预测；
   * 分析 attention 随 3D 距离的变化，并把结果和 GNN/结构 token 模型（DeepFRI、SaProt、ESM2 等）对比。

与主流方法的关键区别在于：

* 不引入任何 GNN、pair representation 或 SE(3) 特殊模块；
* 坐标只通过一层 线性 embedding 加到 token embedding 上；
* 其余一切都保持“教科书版 Transformer”的形态。

这让所有收益都可以更干净地归因于：“原生 Transformer + 坐标”的能力，而不是堆参数或设计复杂结构模块。

---

2 方法细节：几个真正“非平庸”的设计

2.1 LayerNorm 的“隐藏几何”：从内积到 -‖xᵢ - xⱼ‖²

我们习惯把 attention 看成“相似度”：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez5iazqcJibofIoMPXpWAc0lyjq5iaarxUExVhlGH4Vlvo6WIibSyIlDFRaQfg6UmWpvWOGqkyYJgmnc8A/640.png)

但对于坐标来说，更自然的是距离：

关键在于：LayerNorm 会把向量的模长拉成近似常数。 这样一来， 在一定近似下就可以写成：

softmax 之后自然变成了“距离越近，权重越大”的高斯核。

更有意思的是，作者给出了几种 1D 位置嵌入：

* trig 型（sin/cos）
* linear 型：
* quadratic 型：显式包含 (x²) 项

即使只是 linear 型，在 LayerNorm 的非线性作用下，也能在本地表现出二次结构，足以近似距离²。

这解释了一个一直存在于工程实践中的“黑箱直觉”：

为啥 AlphaFold3 那种“线性嵌入坐标 + Transformer”的方案能 work？  
 ——因为 LayerNorm + dot-product attention 本身就有能力“变出二次项”， 并自动逼近高斯距离核。

顺带一提，作者在博客里还指出：像 ReGLU / SwiGLU 这类门控激活函数，

 其实可以很自然地表达 (x²)（ReGLU(x) + ReGLU(-x) ≈ x²），

 这可能是它们在结构任务里表现好的另一个原因。

---

2.2 学 Rⁿ 距离只要 n+2 维：极其紧凑的需求

在点云实验里，作者让模型去拟合不同指数 p 的核  ，

 并在 R¹\~R⁴ 的空间中扫了 head 维度 d\_head = 1\~8。结果：

* p=2（高斯）时训练 loss 最小、收敛最快；
* 只要 d\_head ≥ n + 2，模型就能很好地拟合距离核，再加维度收益极小。

对于 3D 场景，这意味着：

只需要给每个 head 预留 5 维左右来专门处理坐标，就足以学会 3D 距离。

这对 AIDD 工程团队非常实用：不用盲目堆宽度，就能给“几何通道”一个合理的 budget。

---

2.3 用随机旋转“学” SE(3) 不变：架构不变，数据做功

标准 Transformer 对旋转、平移都不不变。

 作者没有在架构上硬塞等变性，而是采用了一种工程上极简单但有效的做法：

* 每次读入结构时，先 recenter 到原点，再做随机旋转和缩放；
* 观察训练/验证 loss 曲线，以及对随机旋转前后的预测差异（SE(3) divergence）。

结果表明：

* 没有旋转增强时，模型会严重过拟合某个固定朝向，验证集 loss 脱轨；
* 加了随机旋转后，train/val loss 基本重合，且验证 loss 明显下降， 模型对同一结构不同旋转的预测差几乎与验证 loss 持平。

换句话说：

数据层面的 SE(3) 增强，足以诱导模型学出“近似”旋转平移不变的距离度量。

这对工业实践的启示是相当直接的：在大多数3D任务里，先把数据增强做到位，再考虑上昂贵的等变模块。

---

2.4 蛋白模型：刻意“保守”的小架构

蛋白侧实验用了一个刻意压缩的“小 ESM”：

* 6 层 encoder，768 hidden，12 头，FFN=2048，GeLU，无 dropout；
* token embedding = AA embedding + sinusoidal 线性位置 encoding；
* coords 版本再加一层 Cα 坐标的线性 embedding；
* 预训练任务：15% masked token prediction，数据集是 DeepFRI 的 GO PDB (\~36K 链)。

也就是说，作者没有指望靠大参数“碾压”基线，而是想看：在完全可比的体量上，“加结构 + 理解结构”的收益究竟有多大。

---

3 实验与结果：从点云到蛋白功能

3.1 点云：高斯核 + n+2 维结论被直接验证

* 在拟合  的实验中，p=2 时真的最容易学；
* head 维度达到 n+2 之后，验证误差基本饱和；
* 随机旋转增强可以显著降低过拟合和“朝向记忆”。

这部分更多是对理论的 sanity check，但给出了很清晰的工程 guideline。

---

3.2 Masked LM：结构信息极大降低不确定性

在 GO PDB 上：

* 训练 perplexity
   * 无坐标：≈ 11.9
   * 有坐标：≈ 6.5
* mask 恢复率
   * 无坐标：\~23%
   * 有坐标：\~38%，其中 Gly/Pro 等对局部构象高度敏感的氨基酸提升尤为明显。

更有意思的是 attention 行为：

* 无坐标模型：attention 只和线性距离强相关，对 3D 距离不敏感；
* 有坐标模型：前几层对 3D 距离非常敏感，且曲线拟合高斯非常好；
* 随着层数增加，高斯的方差变大，模型从“看局部邻域”逐渐过渡到“全局整合”。

这非常符合我们对蛋白的直觉：浅层学 local geometry & secondary structure，深层做 global fold & function 相关的长程推理。

---

3.3 GO 功能预测：小模型 + 小数据，超越深度 GNN

在 DeepFRI 的 GO molecular function benchmark 上，

 作者比较了：DeepFRI（GCN+LSTM）、DeepCNN，以及本文的 MLP / finetune 模型。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez5iazqcJibofIoMPXpWAc0lyjibpefrCBtX72iaDwA3A0ROTQyxia8hOUhtcjKm7bUOm8DMRzdJAl6vjBw/640.png)

粗略总结一下关键信号：

* DeepFRI 加不加结构，AUPRC 从 0.427 → 0.446，结构带来的增益 ≈ 0.02；
* 本文仅用 预训练 embedding + 2 层 MLP，就能做到 AUPRC ≈ 0.46， 与 DeepFRI 持平甚至略好，且训练只需几分钟；
* 对预训练 Transformer 做结构感知的 finetune 后，AUPRC 进一步提升到 \~0.56，明显领先 DeepFRI。

注意：DeepFRI 预训练了 \~10M 序列，而本文结构预训练只用 \~36K PDB 链。

这说明：

在“有结构”的场景下，结构信息 + 标准 Transformer 的表达力，比“更多序列 + GNN”这种传统路线可能更划算。

---

3.4 ProteinGym zero-shot DMS：结构带来的额外溢价

在 ProteinGym 上，作者基于 ESM2-8M 表示训练了有/无坐标版本，并与 MIF、ProteinMPNN 等结构模型对比：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez5iazqcJibofIoMPXpWAc0lyjduhq6CFhoNWHlfuLH1QSThWvIdIXibIvrk91dNPPbM3yHYO57u1WBeg/640.png)

* 总体上，带坐标版本的 Spearman ρ 明显高于纯 ESM2，接近 MIF 这类专门设计的结构模型；
* 但在 稳定性（stability）子集 上，仍显著落后于 MIF/ProteinMPNN。

这和我们对模型粒度的判断是吻合的：只用 Cα 坐标，足以帮助很多功能/活性相关任务，但对精细稳定性预测仍不够。

---

3.5 接触图预测：几乎“完美”的全局几何保留

作者在预训练模型上加了一个 contact head，直接预测接触图。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez5iazqcJibofIoMPXpWAc0lyjR2zxvdBiczlRrW07Gq0jMgTM1jKdCiatvEM6sY1KKAYn5LvlGx9pib4oA/640.png)

 对比 ESM2-650M、SaProt-650M 等：

* ESM2 / SaProt：长程接触 P@L 在 30–50% 区间；
* 本文模型：短/中/长程 P@L 均在 96–99% 之间。

含义非常直接：

离散结构 token（如 SaProt）不可避免地丢失了一部分全局几何信息；而直接把连续坐标喂给 Transformer，则几乎可以无损地保留全局结构。

这对任何需要“看清”折叠拓扑、长程互作的工作流都非常关键。

---

4 专业评价：它的真正价值与坑在哪里？

4.1 Take home message

1. 给“Attention 懂结构”这件事补了理论课
   * 不再只是“看 attention heatmap 很像 contact map”这种现象描述， 而是有了明确的数学框架：LayerNorm + 合适 embedding → 高斯距离核。
2. 架构极简，工程友好
   * 不改 Transformer block，不加特殊层；
   * 只需在输入端加线性坐标 embedding + 合理数据增强；
   * 非常适合在现有 PLM 代码库中“外挂一个结构版本”，对工程团队成本极低。
3. 小模型小数据，收益已经很可观
   * 6 层小模型、3.5 万条结构，就能在 GO/ProteinGym 上打平甚至超越经典 GNN 结构模型；
   * 对很多企业团队来说，这是“现实可行”的规模，而不是论文级超大模型。
4. 为“GNN vs Transformer”之争提供了分工视角
   * GNN 更适合做精细局部几何（键角、侧链、力学量等）；
   * Transformer 更适合做全局结构 + 语义整合；
   * 这篇工作给“谁该干什么”画了一条相对清晰的界线。

4.2 需要警惕的局限与风险

1. 粒度问题：只用 Cα，能做的事有限
   * 对很多功能预测任务足够，但在稳定性、力学性质、对接精度等任务上， 缺乏侧链 / 全原子信息会成为硬伤。
2. SE(3) 不变性是“学”出来的，不是硬编码
   * 依赖随机旋转增强，理论上不保证严格等变；
   * 在数据很少或分布偏斜的场景下，模型仍可能偷偷“记朝向”。
3. 评估任务相对集中
   * GO、DMS、接触图都属于“结构相关但不要求极致几何精度”的任务；
   * 真正考验细节几何的场景（抗体–抗原、复合物精准对接、全原子逆折叠）还没系统验证。

---

5 我们的看法

5.1 什么时候可以“先试试 Transformer + 坐标”？

* 任务主要看 全局结构 + 功能/语义：
   * 如蛋白功能预测、家族分类、接口/epitope/热点位点识别等；
* 有相对可靠的结构（实验或 AF-DB），但算力/显存预算有限；
* 你已经有一套 PLM（ESM/SaProt-Seq 等），想以最小改动把结构信号引进来。

在这些场景下，“PLM + 线性坐标通道 + 旋转增强” 是一个非常性价比高的 baseline， 足以替代不少自定义 GNN 模块。

5.2 什么时候仍然需要 GNN / 等变网络？

* 需要对 局部细节 高度敏感：
   * 精确对接得分、全原子稳定性预测、力场相关任务；
* 想要显式建模 方向、角度、二面角，而不是只靠距离；
* 任务本身要求 严格的 SE(3)-equivariance（如基于力学的可逆变换建模）。

在这些场景下，一个合理的路线是：

GNN / 等变模块负责局部几何 → Transformer 负责跨尺度全局整合。

而不是简单“谁替代谁”。

5.3 对分子生成/口袋建模的启发

* 这套思路非常自然地可以扩展到：
   * 小分子原子/fragment 的 3D 坐标；
   * 蛋白口袋、复合物界面的 3D 几何；
* 可以想象一种 workflow：
   * 用 GNN/等变模型生成或精修局部 pocket / ligand 构象；
   * 用 Transformer + 坐标实现 条件生成、属性预测、多任务共享表征。
* 虽然本文未直接涉及 Pocket Generation，但其证明了 Transformer 可以理解“空腔”和“距离”。这是否意味着我们可以用类似 BERT 的掩码方式，让模型去“填补”口袋中的原子，这可能是比 Diffusion 更快的生成路径？

或许这篇工作提供了一个潜在的思路：后端统一用“坐标感知 Transformer”做 global reasoning 和多任务头，前端根据任务需求决定是否叠 GNN 做局部几何。

---

附：几个值得思考的 Q&A

Q1：Transformer 既然能学到距离，那能学到“方向”吗？

* 距离是标量，而方向是向量（或角度/二面角等）。
* 标准 dot-product attention 天生是标量机制，很适合表达“靠近/远离”， 但对“朝哪儿”不敏感，这也是作者承认 Transformer 不适合做 inverse folding 等任务的原因之一。
* 若任务对方向极敏感，可能需要向量值 attention 或显式的等变结构模块来补足。

---

Q2：随机旋转增强真的足以解决 SE(3) 问题吗？

* 短答案：在很多实际任务上“够用”，但不是严格意义上的解决。
* 它能显著降低对绝对朝向的过拟合，让模型更关注相对距离；
* 但不保证在所有旋转下都完全一致——效果取决于训练分布和缩放策略。

---

Q3：和 SaProt 这类结构 token 方法相比，该怎么选？

* 如果你有高质量结构、关心全局几何拓扑（例如接触图、复合物界面）， 直接嵌入坐标往往表现更好；
* 如果你更在意推理速度、对 AlphaFold 结构噪声的鲁棒性， 预计算好的结构 token + 纯序列模型也有优势。
* 实际项目中，非常值得把“结构 token 方案”和“坐标 + Transformer 方案”都做成模块化组件，针对不同任务切换。

---

Q4：对已经有大型 PLM（ESM2/SaProt）的团队，这篇工作意味着什么？

* 不一定要推倒重来，但有两个非常自然的升级路径：
   1. 在现有 PLM 顶层再加一层“坐标感知的小 Transformer”，专门做结构整合；
   2. 对原模型做结构感知的继续预训练，让它变成 unified sequence+structure encoder。

这两条路，都可以在不彻底重构现有系统的前提下，把论文中的思想转化为可落地的改进。

---

一句话收尾：

这篇工作没有再造一个新 SOTA，而是帮我们看清了一件事——原生 Transformer 其实并不“只会看序列”，在合适的坐标输入和正则下，它完全有能力在三维空间里按距离做推理。

对于任何正在尝试统一“语言 + 几何”的 AIDD/CADD 平台来说，这是一个值得认真消化，并立刻在自己代码库里尝试的结论。

---

本文链接：https://openreview.net/forum?id=AUq3nsJ2ga

作者课题组（Oxford Protein Informatics Group）链接：https://www.blopig.com/blog/

代码链接：https://github.com/Ellmen/attending-to-distance

---

本公众号主要介绍AIDD中小分子、多肽、Protac的前沿算法、综述、评估。欢迎关注本公众号获取领域最新文献解读。

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
