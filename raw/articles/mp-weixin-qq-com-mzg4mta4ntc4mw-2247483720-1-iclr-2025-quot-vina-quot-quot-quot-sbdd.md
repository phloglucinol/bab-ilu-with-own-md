---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483720&idx=1&sn=56289fc0bd899de41d8d0d85d373f45e
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483720&idx=1&sn=56289fc0bd899de41d8d0d85d373f45e
source_domain: mp.weixin.qq.com
title: ICLR 2025｜从&quot;刷 Vina 分&quot;到&quot;找得到好分子&quot;：SBDD 模型评估的新范式
author: 
published_at: 
fetched_at: 2026-04-25T02:04:12Z
extractor: wechat_worker
content_hash: 70bc442808cb1c8eb6ea593d9865a8a890e8fe3b164ccf5bfabc7111884a6be2
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibqyf5YlsADXT1pHjNa7CrFyBGCogWugjq5AMVh1CEjfJO3Goib7NibYlzg/0.jpg) 

# ICLR 2025｜从"刷 Vina 分"到"找得到好分子"：SBDD 模型评估的新范式

原创 陷入鞍点 陷入鞍点 [ 陷入鞍点 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

今天给大家分享的是ICLR 2025上的一篇文章”Reframing Structure-Based Drug Design Model Evaluation via Metrics Correlated to Practical Needs“。作者是来自清华大学的Bowen Gao，指导教师是Prof. Ya-Qin Zhang and Prof. Yanyan Lan。非常适合作为SBDD模型工作对比和复现实验的标准起点。

01

引言 - SBDD 模型很“强”，但为什么总落不了地？

近几年，结构基药物设计（Structure-Based Drug Design, SBDD）迎来了一波深度生成模型大爆发：Pocket2Mol、TargetDiff、MolCRAFT 等模型，动辄在论文里展示——

“生成分子的 Vina docking score 比真实配体还好！”

同时，生成分子的 QED、SA 分数也往往看起来很“漂亮”。

但真正到了 合成 & 体外实验 这一步，很多团队会有类似的体验：

* 生成分子又大又奇怪、难合成；
* 实际活性并不如预期；
* 即使“分数很好”，却很难转化为可用的候选化合物。

这篇来自清华 AIR 等机构的 ICLR 2025 工作，正面怼的就是这件事：

当前 SBDD 社区流行的评估指标（尤其是 Vina docking score），在很大程度上是“可被模型轻易 hack 的理论指标”，与真实药物发现中的“有没有用”之间存在巨大鸿沟。

作者提出了一个以“贴近实际需求”为目标的 模型级评估框架，并在一套重新构建的 benchmark 上，对主流 SBDD 模型进行了系统“回炉重测”。

02

现状之痛：Vina 分数真的不能信了吗？

2.1 Vina 分数可以“刷”，而且很好刷

论文的图 1 展示了一件很直观的事：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibqtnia1R8dZqKltNKVeh3cznTicuf2Pp1ibicZYzjibFllia0qibeIAHNh8xh3A/640.png)

把分子 原子数 与 Vina score / QED 的关系画在一起，结果非常扎心：

* 原子数越多，Vina score 越“好”（更低）；
* 但与此同时，QED 反而在持续下降——也就是越来越不像“好药”。

在附录 E 里，作者更进一步量化了 Vina 的“可被操纵性”：

* 增加羟基数量（–OH），Vina score 可系统性变好；
* 降低 N+O 原子比例 / 增加卤素（F, Cl, Br, I）数量，也能持续改善 Vina 分数；
* 换句话说，只要模型学会往这些“方向”堆结构，就能 在不提升真实结合能力的前提下刷出很好的 Vina。

同时，以往被广泛使用的 SA score 也被多篇工作证明与真实可合成性存在偏差——生成模型可以生成“理论上易合成、实际上没人愿意做”的奇怪结构。

2.2 Benchmark 本身也有问题：CrossDocked 的偏倚与泄漏

当前很多 SBDD 模型是基于 CrossDocked 数据集进行训练和评测的，但这套数据本身存在明显问题：

* 口袋–配体构象来自 对接软件生成的“伪复合物”，而非真实晶体结构；
* 训练样本的选择本身依赖 docking 结果，带来 对 Vina 等打分函数的系统性偏倚；
* 更严重的是：不少工作直接使用官方测试集作 checkpoint 选择的验证集，造成 数据泄漏。

结果就是：模型在“自己造的虚拟世界”里表现很好，但与真实药物发现场景渐行渐远。

03

作者的核心观点：先问一句——“这些分子到底有啥用？”

作者的视角非常务实：

真正有用的生成分子，不一定要自己就是“好药”，但至少要能 帮助我们在真实化合物库里找到更多活性分子。

这与近两年多篇工作中出现的实践经验高度一致：业界/学术界经常把生成分子当成 虚拟筛选的“模板”，据此在商业库或公司自有库中做相似性搜索，再交由药化进行修饰与验证——而不是直接合成“原始生成分子”。

因此，作者提出了一个 三层级评价框架（见论文第 4 页图 2）：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibquc1K4BQstxBG97MVI0oL5Osfx3V7mcBlLQ36eanibEMTtTAmWdpMsBg/640.png)

3.1 Level 1：与已知活性分子 / 已上市药物的相似度

目标：评估一个模型 是否能生成“像样的药物化学结构”。

做法：

* 把分子映射到多种特征空间：
   * 2D 指纹：ECFP / Morgan
   * 3D 指纹：E3FP
   * 深度表征：Uni-Mol 分子 encoder、DrugCLIP 分子 encoder
* 对于某个靶点，给定所有已知活性分子 aia\_iai，对生成分子 lll 定义：  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibqnvRWMYytEhTp3Soo6aCABzKsXAiaZiaYbZ7TrviaWDuAJqnarRWVSMTdQ/640.png)

 即：与 **最相似活性分子的最大相似度**。

* 附录 A 还额外构建了一个 FDA-Approved Drug Similarity：
   * 统计生成分子与 2582 个已上市小分子药物的最大相似度；
   * 用来衡量“离已知药物化学空间有多远”。

直观理解：

如果一个模型生成的分子，普遍与已知活性/药物“化学上长得不像”，那它想要通过少量修饰变成真药，难度就会很大。

3.2 Level 2：把生成分子当“模板”做虚拟筛选，好不好用？

只看相似度还不够，因为模型可能生成一堆“长得像但实际上是 decoy 的分子”。

于是作者引入了 虚拟筛选能力（Virtual Screening Ability） 这一层：

   * 对每个靶点，构建一个含 已知 actives + decoys 的大库；
   * 把 生成分子作为查询模板，用上面提到的各种指纹/encoder 做相似性检索；
   * 看在排序前 1%、2% 里，能富集多少真实 actives。

评价指标：

   * BEDROC：强调前排富集（常用 BEDROC85变体，上排 2% 候选贡献 80% 权重）；
   * Enrichment Factor (EF@1)：前 1% 里真实活性分子占比，相比随机的提升倍数。

一个非常重要的对照实验（论文表 1）：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibqoiaRTGgp3B2wBU0lfXjE4blhZ47eKFSCd8Y6bEoFhowmJtCTAoaXQmg/640.png)

   * 使用 真实晶体配体 作为模板做虚拟筛选 vs. 用 Vina docking score 排序 做虚拟筛选

结果是：

“真实配体做相似性筛选” 在 BEDROC & EF 上显著优于 “Vina 打分排序”。

这直接验证了作者的逻辑：能作为虚拟筛选模板找到更多活性分子，是一个更贴近实验 hit rate 的指标。

3.3 Level 3：更“严谨”的结合能力估计：Delta score & DrugCLIP

虽然作者认为“理论打分容易被 hack”，但也没有完全抛弃结合亲和力估计，而是做了两件事：

1. 保留传统 Vina docking score 作为“参考维度”；

2\. 引入更关注“特异性”的 Delta score 以及 DrugCLIP score：

* Delta score 思路：
   * 对于一个生成分子 𝑥𝑖𝑗 和其目标靶点 𝑦𝑖计算 −S(xij, yi) + S(xij, yk)
   * 平均后得到该靶点的 Delta score；
   * 直观上，它衡量的是“对正确靶点比对随机靶点更有优势多少”。
* Docking 部分使用了 Glide SP / Glide XP，更精细但更耗时；
* 同时引入 DrugCLIP 打分——利用在虚拟筛选中表现很好的 DrugCLIP，来衡量生成分子与口袋之间的对齐程度。

论文第 10 页图 5 进一步表明：Delta score、相似度指标、虚拟筛选指标与原子数几乎无相关性，相比 Vina 分数更不容易被简单的“堆原子”策略所欺骗。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibq4LHbhFlpPAJaEK9Ab1juwl5G0If1JV9fBodia8frZ92ENFkTFR224TA/640.png)

04

数据集与实验设计：用真实晶体结构 & 严格划分来测试模型

4.1 训练集：基于 PDBbind、按口袋相似度“去同源”

作者放弃了 CrossDocked，而是回到 真实晶体结构数据库 PDBbind：

* 对配体解析异常、含核酸、口袋原子数过少等样本进行严格过滤；
* 以配体为中心 10 Å 范围内定义 binding pocket；
* 然后使用 FLAPP 对训练集与测试集之间的 pocket 结构进行对齐，相似度大于 0.6 / 0.9 的 training pockets 会被移除；
* 得到两个版本的数据集：
   * FLAPP 阈值 0.6：约 12,344 个复合物；
   * 阈值 0.9：约 17,519 个。

这一步的意义是：确保模型在测试靶点上确实是“泛化到新 pocket 类型”，而不是记住了相似结构。

4.2 测试集：DUD-E + LIT-PCBA

* 主测试集来自 DUD-E：
   * 101 个靶点，涵盖 GPCR、kinase、核受体等多种类型；
   * 每个靶点平均有 \~224 个 actives，每个 active 配有约 50 个精心构造的 decoys。
* 附加测试来自 LIT-PCBA（15 个更难的靶点）：
   * decoys 是通过真实实验确认“基本无活性”的化合物，
   * 因此虚拟筛选任务更接近真实 HTS 场景。

与训练集一样，测试时同样用 10 Å 半径 pocket。

4.3 对比的模型

作者系统评测了 5 类主流 SBDD 模型：

* LiGAN（体素网格）；
* AR（3D 自回归）；
* Pocket2Mol（自回归，经典工作）；
* TargetDiff（3D 等变 diffusion）；
* MolCRAFT（Bayesian Flow Network + SBDD）。

另外还纳入了一个 优化型方法 RGA（Reinforced Genetic Algorithm） 作为参考：它代表一类“在 docking score 上反复优化”的传统算法。

每个靶点上，各模型采样 20 个分子（AR/TargetDiff 先采 100 个再筛选，以保证分子大小一致性）。

  
05

结果：SBDD 模型“刷分能力”很强，但离真实配体还有多远？

5.1 结合能力估计：Vina 很强，但 Delta & DrugCLIP 很“打脸”

从论文表 2 可以看到一个典型场景：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibqLZdFXG4iaOnMLkMAOYXNxM1f6KTuW3Wr3SARibrVDiaAibyicwibqq0lT3MQ/640.png)

* 真实配体的平均 Vina score ≈ –9.36，Delta score ≈ 2.69，DrugCLIP score ≈ 0.51；
* MolCRAFT 的 Vina score 甚至能达到 –9.78，看起来“比配体还强”；
* 但其 Delta score ≈ 0.97、DrugCLIP score ≈ 0.17——远远低于真实配体。

TargetDiff 情况类似：

* 在 Vina 上表现不错，但 Delta score 甚至不如简单的自回归模型；
* 说明它很可能通过“变大 + 结构模式化”来讨好 Vina，而不是提升真正的特异性结合。

结论非常明确：

只看 Vina，现有 SBDD 模型似乎已经“超越”了真实配体；但一旦用更合理的结合能力指标衡量，它们整体还大幅落后。

5.2 与已知活性/药物的相似度：化学空间仍然“离谱”

表 3（以及附录表 5）给出了一组很直观的数字：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibqeawtf8UBCyV0SFOAmOOFqWgdpDiakibajibcmL0HmZlIIHdbNUIjxvPicw/640.png)

* 对已知活性分子，真实配体的 2D 指纹相似度约为 0.59，DrugCLIP 空间相似度 0.87；
* MolCRAFT 虽然在各模型中最好，但 2D 相似度只有 0.21 左右，DrugCLIP 相似度 0.52 左右；
* Pocket2Mol 在 FDA 药物相似度（2D 指纹） 上表现最好，说明它在生成“药物化学友好骨架”方面有一定优势。

这说明：

现有 SBDD 模型距离“像真实药一样”的化学空间，还有非常大的 gap。

很多生成分子在结构空间里，更像是“模型为了刷分构造出的奇怪区域”，而不是药化眼中熟悉、可操作的 scaffold / chemotype。

5.3 虚拟筛选能力：最佳模型才刚刚接近 Vina

再看表 4（虚拟筛选 BEDROC / EF）：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibqgt8OzibRlGlOVNnOu2ialxF4dt2AocVvDAtkHQ8fmibHGE7tsIYzianjFw/640.png)

* 真实配体作为模板：
   * DrugCLIP encoder 下 EF@1 ≈ 29.2，BEDROC ≈ 45.4；
* Vina docking 排序本身（表 1）EF ≈ 7.3；
* 在所有生成模型中，表现最好的是 MolCRAFT + DrugCLIP：
   * EF ≈ 5.55，已经接近 Vina；
* 其余模型大多在 EF ≈ 1–3 左右，基本只是略好于随机水平。

这组结果有两层含义：

1. 目前最好的 SBDD 模型，最多也只是“接近 Vina 做虚拟筛选”的效果，离真实配体模板（EF≈29）还有 5 倍以上差距；
2. 但从另一个角度看：  
MolCRAFT + DrugCLIP 的 VS 性能已经接近 Vina，而计算成本却远低于对所有化合物做 docking，说明“生成分子 + 相似性虚拟筛选”开始具备实用潜力。

LIT-PCBA 上的结果（附录表 7）也延续了这一趋势：

在更严格的实验型 decoy 数据集上，所有方法表现整体下降，但 MolCRAFT 仍然是生成模型中的最佳者，而真实配体仍然遥遥领先。

5.4 模型层面的观察：谁在刷分，谁在“干正事”？

论文第 9 页的雷达图和附录可视化给出了一些有趣的模型画像：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibq9rUl6RGK2Z6WUibZkw5rm3fIcSbchLNcE86xdsxX2DuyeBcqE3Rny8Q/640.png)

  
* TargetDiff：
   * Vina 特别好，但 Delta、相似度、虚拟筛选都很差；
   * 很可能是 “过度拟合 Vina” 的典型案例——生成又大又“讨好打分函数”的分子，而非真正有意义的配体候选。
* Pocket2Mol：
   * 分子普遍偏小，导致 Vina 分数不占优势；
   * 但在指纹相似度、VS 能力上表现不错，尤其能生成有价值的子结构/功能团；
   * 对药化来说，它更像一个 “片段/骨架生成器”。
* MolCRAFT：
   * 在绝大多数指标上是现有方法中的综合最优者；
   * 虚拟筛选效果可以接近 Vina，但仍明显落后真实配体。
* RGA（优化型方法）：
   * 通过多轮优化，Vina 从 –9.0 提到 –9.67，但 Delta score 和 EF 几乎 原地踏步甚至略降；
   * 说明“只盯着 docking 优化”并不会自然带来更好的实用价值。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez6RNR8R6Qzvp9pa6gGIibBibqhicGjyV1iag6W0ibPhg4GeuY5dmtqVbkwm0F1QoCInWs1kwOzzs0PDXZg/640.png)

06

对 AIDD / CADD 实践的启示？

6.1 对模型开发者：不要再只报 Vina / QED / SA 了

这篇工作释放的信号非常明确：

如果一篇 SBDD 论文只在 Vina/QED/SA 上做文章，那它对真实药物发现的参考价值很可能是有限的。

更合理的做法是：

* 至少同时报告：
   * 与已知 actives / FDA 药物的多模态相似度（2D/3D/深度 encoder）；
   * 把生成分子作为模板时的虚拟筛选 EF / BEDROC；
   * Delta score 与类似 DrugCLIP 这类更鲁棒的评分函数。
* 在训练目标中，考虑显式地：
   * 惩罚“堆原子、堆 OH、堆卤素”式的 Vina hacking 行为；
   * 或者直接 用虚拟筛选指标 / 对比学习目标 作为优化方向（例如与 actives 对齐、与 decoys 拉开）。

这与用户之前在 DrugCLIP、对比学习方向上的思考其实非常契合——把“能帮助找到更多真活性”的能力作为一等公民目标，而不是事后附带的分析。

6.2 对工业应用：把生成模型当“虚拟筛选模板工厂”

对于企业内的 CADD/AIDD workflow，这篇文章给出的一个很现实的落地模式是：

1. 使用 SBDD 模型（例如类似 MolCRAFT 的方法）在口袋上生成一批分子；
2. 不急着直接合成，而是：  
\- 先用 DrugCLIP / Uni-Mol 等 encoder 把这些分子作为查询，  
\- 在内部化合物库 / 商业库上做高效相似性检索；
3. 对检索到的候选：  
\- 结合虚拟筛选指标（EF/BEDROC）、Delta score、药物化学规则进行筛选；  
\- 再交给药化进行结构优化与合成决策。

这条路径有几个优点：

* 避免了直接依赖“怪异的生成分子”本身；
* 将生成模型的优势转化为 “在化学空间中提供好模板”；
* 与现有的 LBVS、药化经验高度兼容。

6.3 对 Benchmark 设计：回到真实结构与可转化指标

作者的 benchmark 设计有两点值得借鉴：

* 使用 真实晶体结构（PDBbind）+ 严格去同源划分（FLAPP） 作为训练/验证基线；
* 测试上引入 带真实 actives/decoys 的 DUD-E & LIT-PCBA，并直接用虚拟筛选指标作为主角。

对后续 SBDD 相关工作的建议是：

尽量在类似“真实结构 + VS 指标”的框架下比较模型，而不是继续在同一个 CrossDocked + Vina score 的闭环里内卷。

  
07

小结：从“分数好看”走向“真正有用”

这篇文章的工作做的事情其实很朴素，却非常关键：

* 没有再堆一个更 fancy 的生成模型；
* 而是回到一个根本问题——“这些生成分子，究竟能不能帮助我们在真实世界里找到好药？”

通过提出 三层级、面向实际需求的评估框架，以及一套基于 PDBbind + DUD-E + LIT-PCBA 的新 benchmark，作者系统地“降温”了当前 SBDD 模型在 Vina 指标下的那种虚假繁荣。

对我们做 AIDD/CADD 的同行来说，它至少带来三点共识：

1. Vina 不是不要，而是不能再“唯 Vina 论”。

2\. 生成模型的价值，很大程度上在于“做模板、做导航”，而不是直接给出终极药物。

3\. 评估指标和 benchmark 的设计，会深刻影响整个社区模型的发展方向。

如果你正在做 SBDD 生成模型，这篇文章非常值得细读，并且可以考虑在自己的工作中：

* 引入相似度 & 虚拟筛选指标；
* 把 DrugCLIP、Uni-Mol 这类 encoder 当作“新一代评分函数”；
* 更系统地把“可用于实际项目的能力”放进模型目标和评估里。

  
文章地址：https://openreview.net/pdf?id=RyWypcIMiE

代码地址：https://github.com/bowen-gao/sbdd_practical_evaluation

本公众号主要介绍AIDD中小分子、多肽、Protac的前沿算法、综述、评估。欢迎关注本公众号获取领域最新文献解读。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/699z0IL45wP2MLVqoB96IS7icJfBlTCjPfA4rUuf8OQ0Eia2h1IE4Mgib7xyx73Hzb2B9Imak1huT1hjRyPUwnnlw/640.png)

。

  
点个在看+赞支持一下呗

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
