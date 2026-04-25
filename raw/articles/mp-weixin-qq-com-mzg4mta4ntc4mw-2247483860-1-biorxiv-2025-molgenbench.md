---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483860&idx=1&sn=0c34106c848e6a248f290fe5a0e53586
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247483860&idx=1&sn=0c34106c848e6a248f290fe5a0e53586
source_domain: mp.weixin.qq.com
title: bioRxiv 2025 | MolGenBench：当分子生成模型终于走上“实战考场”
author: 
published_at: 
fetched_at: 2026-04-25T02:04:11Z
extractor: wechat_worker
content_hash: 3cda7f2d77dfd5fe21b5d084e1573fe30fda722d8c4b78eb79785cb0092b8b5e
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGE0VFtZqrFibDnZqRCGlhWe0micNppD5bvMQxVNcFU5ibdGLvgBQFdX5O1w/0.jpg) 

# bioRxiv 2025 | MolGenBench：当分子生成模型终于走上“实战考场”

原创 陷入鞍点 陷入鞍点 [ 陷入鞍点 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

论文来源｜bioRxiv（2025.11）  
论文标题｜Benchmarking Real-World Applicability of Molecular Generative Models from De novo Design to Lead Optimization with MolGenBench  
单位｜同济大学 & 中科院上海药物所 曹端华/郑明月团队

---

0 引言：模型很多，但能在项目里用的有多少？

过去几年，基于结构的分子生成模型（Structure-based Molecular Generation, SBMG）几乎成了 AIDD 里最热闹的一条赛道：

* 早期的 liGAN、Pocket2Mol
* 后来的 TargetDiff、DecompDiff 等 3D 扩散模型
* 再到用贝叶斯流匹配（Bayesian Flow Network, BFN）的 MolCraft

一篇又一篇论文在 CrossDocked2020、PDBBind 等数据集上刷出漂亮的 Vina score、QED、SA 分数，看上去“又新又强”。但一线 CADD/AIDD 同事心里都有数：真正能在真实项目里持续产出 hits / leads 的生成模型，几乎没有。问题到底出在哪里？这篇来自同济大学和中科院上海药物所的 MolGenBench 工作，给出了一个相当扎心但很诚实的回答：

不是模型太少，而是我们一直在用错误的标尺评估它们。

现有 benchmark 存在至少三类硬伤：

1. 数据不真实：靶点数少（十几个到几十个），大量构象靠 Vina 对接“拼出来”，真实实验活性数据极少。
2. 指标不靠谱：过度依赖 Vina 打分、QED 之类与真实活性/成药性相关性有限的代理指标。
3. 场景不完整：几乎全部集中在“从零开始 de novo 设计”，而真实药物发现中最关键的一环——Hit-to-Lead（H2L）优化，基本缺席。

MolGenBench 的出现，就是要把 SBMG 从“模拟题刷榜”拉回药物发现的真实战场。

---

1 MolGenBench 做了什么？——从数据、任务到指标的“全栈重构”

1.1 数据集：从 PDBBind 玩具谷走向 ChEMBL 真实世界

MolGenBench 基于 ChEMBL v33，构建了目前为止最贴近真实项目的 SBMG 评测数据集之一：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGE46ibdV9yOPfLp2d86YJ1icDuoBLHFicEONpjADBeryW5Q2C1TXoGdSosw/640.png)

* 120 个蛋白靶点（显著多于 DurIAN 的 14 个、POKMOL-3D 的 32 个）
* 220,005 个实验验证的活性分子（IC₅₀/Kᵢ/Kd ≤ 10 µM）
* 5,433 个化学系列（series），支持对同一系列内部的 H2L 优化进行评估

筛选策略也很“药企范儿”：
* 每个靶点至少有 50 个活性分子 + 50 个独立骨架 + 20 个 series
* 活性阈值 10 µM 刻意设得相对宽松——宁可多留真实弱活性，也不想把参考空间收缩得过于理想化

此外，作者还构建了一个600 个 series 的 H2L 子集，每个 series：
* 提取最大公共子结构（Maximum Common Substructure, MCS）作为“起始片段”（fragment）
* 通过对接获得片段初始构象
* 用于模拟药化在实际项目中从 fragment/hit 出发做“往里长”的日常工作

这一步非常关键：

 👉 它使得 MolGenBench 不仅能评估“能不能生成像药的分子”，更能评估\*\*“能不能在已知骨架基础上做出真正有价值的优化”\*\*。

---

1.2 任务设计：从 de novo 到 H2L 的三层考核

MolGenBench 设计了多个层次的任务，大致可以归为三类场景：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGETtjYCawTRc5adiaxfQG7OFj8QSDia5NSMibz0pKqcF6bJGj0sLCYweMLQ/640.png)

1. De novo 生成（Unconstrained / Pocket-based）
   * 仅给出蛋白口袋结构，让模型自由生成配体
   * 考察：是否能在无限化学空间中“摸到”真实活性区域
2. Scaffold / series-aware 生成
   * 给定已有活性分子的骨架或 series 信息
   * 看模型是否能做出“同系列但有改进”的新分子
3. Fragment-based H2L 优化
   * 给定 MCS 片段 + 蛋白口袋
   * 要求在保留片段锚点的前提下，优化亲和力、相互作用质量等
   * 这是最接近真实项目 H2L 场景的任务

这套设计基本覆盖了药企项目中从 hit 发现到 lead 优化的关键环节。

---

1.3 评估指标：从“模型喜欢的”换成“药化在乎的”

MolGenBench 的一大亮点，是明显抛弃了很多容易被 hack 的指标（单纯 Vina score、分布对齐等），转而引入一批更接近真实价值判断的指标。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGE8yhRV9Y85HZvIuXibpyzk8h3eiaYyU3MvibJw6USJxicIwxDUtObsz22Pw/640.png)

核心指标分为几类：

① 活性回收能力（Hit/Series Rediscovery）

* Hit Rate：生成分子中，真实活性分子所占比例
* Hit Fraction：参考活性空间中被模型“重新覆盖”的比例
* Series / Scaffold 级别重发现：能否找回已有活性骨架或系列

这类指标直接回答：

你的模型到底能不能“踩中”我们已经知道的活性区域？

② 靶点感知能力（Target-Aware Score, TAScore）

TAScore 用来衡量：模型是否真的利用了蛋白口袋信息，而不是在所有靶点上生成差不多的分子。

简单理解：

* 若不同靶点上生成的分子分布差异不大 → TAScore 接近 1 以下
* 若不同靶点分子有明显特征差异 → TAScore > 1，说明模型有一定 target-aware 能力

③ H2L 优化能力（MNA Score 等）

* MNA（Mean Normalized Affinity）Score：在给定 series 背景下，新生成分子相对于已知分子的“归一化亲和力水平”
* Interaction Score：结合模式是否更合理、相互作用是否更加丰富

这类指标更接近药化关心的问题：

在这个系列里，你能不能给我“更好”的分子？是瞎改 R 基团，还是构象/相互作用真的更优？

④ 构象与物理合理性（PoseBusters）

引入 PoseBusters 用于检查：

* 是否存在严重 clash
* 键长、键角是否物理合理
* strain energy 是否过高

这对构象生成类模型（如 MolCraft）是一次真实的“物理学期中考”。

---

2 关键发现：繁荣背后的五个“冷水”

MolGenBench 把主流 17 个 SBDD 模型拉到同一条起跑线上，包括：

* 扩散模型：TargetDiff、DecompDiff、DiffSBDD（CrossDock / BindingMOAD 两版）
* 自回归 / Transformer：PocketFlow等
* BFN：MolCraft
* 以及若干基于药效团 / 片段约束的模型（ShEPhERD、PGMG 等）

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGE9qJOgPxoSKxPXSyRjL4oK75339TmS9UKo93xyxDoJDbicg4rf9eKX8w/640.png)

系统评测后的结论，可以用一句话概括：

“看起来都很强，真上战场都不行。”

下面挑出最有信息量的五点。

---

2.1 发现一：活性分子重发现几乎是“零点几时代”

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGE3RMd4LQqLUjoibEB7s80Kg28LkGcK0jjiamhowu7bnicPjCs4MZkcibATQ/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGEAFTR4iaibo3NH6dsbemZgNHF4aV5t2TAAXrGibw2zZN5Nj0gtUhvCrPsQ/640.png)

在 de novo 任务中：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGEZrMZbMHoVTIicBYSLWFbJ1JOicmFhBuQw5Z8QObmXibw4o5XbyO3YKkmA/640.png)

* 分子级 Hit Rate 在 CrossDock 靶点上通常 < 0.124%
* 在 Novel 新靶点上，甚至跌到 0.02% 量级

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGE298dApJV9kXYtmibn63qujiabDnYZF35UEHbmhqZQAz1SrlQyycicZ1Hg/640.png)

* 骨架级表现稍好，大约在 10–30% 左右，但从骨架到精细 R 基团调优仍是巨大鸿沟

TamGen 这类预训练了大量活性分子的模型在既有靶点上表现相对好一些，但一到新靶点上性能明显崩塌，暴露出严重的数据记忆/泄漏问题。

药化视角翻译：

* 现在的生成模型大概知道“这类骨架对这个靶点差不多是对的”，
* 但对“R 基团怎么长、构象怎么摆、相互作用如何补”的细节几乎没有真正掌握。
* 也就是说，它们更像是会说“房子”这个词，但不会画出能住人的房子。

---

2.2 发现二：大部分模型并没有真正“看见”蛋白

TAScore 的结果非常刺眼：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGEqibjBxofnwrSn1KGNnyosibZwRCGO9LwquR9lefCxvet9EtBIQQQKI1w/640.png)

* 超过一半以上的靶点上，多数模型的 TAScore 并没有超过 “target-aware” 的判定阈值
* 换句话说，它们在不同靶点上生成的分子分布非常相似
* 唯一较明显展现出靶点特异性的，是类似 PocketFlow 这种同时结合了大规模分子预训练 + 结构输入的模型

这意味着：很多号称“结构驱动”的生成模型，其实做的是“结构不敏感”的分子生成。口袋信息被喂了进去，但训练过程里并没有真的逼迫模型学会“口袋差异”。

---

2.3 发现三：构象质量比我们想象的更糟，PoseBusters 一过就“原形毕露”

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGEuLjKCwibz7HyUxJJNaLnJPU5rREOcQZOXIhr0vBVQ2uafYJIKmlhPrg/640.png)

对于构象生成，论文中一个直观结果是：

* MolCraft 在 PoseBusters 上表现相对最好，PB-Valid 可达 \~78% 左右
* 多数模型生成的构象，不管 RMSD 看上去多漂亮，一经过物理合理性过滤，合格率都非常有限
* 很多所谓“低 RMSD”的 pose，本质上是在局部做了不合理的强行拉扯——既不物理，也未必更有活性

好消息是：

* 在减少严重 clash、改善几何合理性方面，优秀模型已经开始超过传统 Vina 对接结果，说明结构深度学习的确有潜力突破经典对接方法天花板。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7h7dxOqYH73Y2mdu47MibGEdn61x9pYlEKzHD19NuMhkNPzaeficT8S1qcdrl25aPZTG8gjfvVqnyA/640.png)

坏消息则是：

目前构象生成仍不足以“直接拿去做 FEP / MD / 结构基础上的精细 SAR 分析”，依然需要后处理和再优化。

---

2.4 发现四：H2L 优化任务里，生成模型终于开始“像点样子”了

真正让人看到希望的，是 fragment-based H2L 这一块。

在以 MCS 片段为锚点、约束生成的任务上：

* Delete 和 DiffDec 是表现最突出的两类模型
   * Delete 在 221 个 series 中重发现了活性骨架
   * DiffDec 在 167 个 series 中表现突出，并且在未见靶点上泛化能力最好
* H2L 场景下，Hit Rate 可以达到 5–8%，比 de novo 任务提升了近两个数量级

这传达一个很重要的信息：

问题从“无限化学空间自由探索”缩小到“给定正确骨架下的定向微调”，生成模型的实用价值开始显现。

对企业而言，这可能意味着：与其指望生成模型从 0 到 1 产出全新 chemotype，不如先老老实实在已有 hit/series 上做“聪明的 0.2 到 0.8”。

---

2.5 发现五：训练数据的来源，几乎“决定模型性格”

DiffSBDD 的两个版本给出了非常有趣的对照实验：

* DiffSBDD-M（基于 BindingMOAD 晶体结构训练）
   * 优点：构象质量更好、strain energy 更低
   * 适合追求 “pose 可信度” 的场景
* DiffSBDD-C（基于 CrossDock 模拟复合物训练）
   * 优点：生成分子的多样性更好，覆盖的 series 更多
   * 更适合做化学空间拓展

这直接说明：

* 高质量晶体结构 → 更物理合理的构象
* 大规模对接数据 → 更宽广的化学空间覆盖

未来更值得尝试的是： 👉 如何在训练阶段实现两类数据的有机融合，而不是二选一。

---

3 方法学启示：下一代生成模型应该长什么样？

把 MolGenBench 的结果和我们在一线的经验放在一起，可以勾勒出一个“下一代实用型生成模型”的轮廓。

3.1 架构：扩散 + 自回归 + 物理先验，而不是单一路线

* 自回归模型（如 PocketFlow）
   * 化学有效性高、生成分子更“像药”
   * 但模式易收缩，多样性相对不足
* 扩散模型（如 DiffSBDD、DecompDiff）
   * 多样性和泛化能力更强
   * 但很容易在有效性、构象物理合理性上“翻车”
* BFN（如 MolCraft）
   * 在 pose 合理性上优势明显
   * 更像是“结构修正器 + 优化器”

一个越来越清晰的趋势是：没有一个架构能单独解决所有问题，混合式 pipeline 才是更现实的选择：

自回归 → 负责“做对化学”  
 扩散 / Flow → 负责“做广化学” BFN / 物理模块 → 负责“做对构象 & 相互作用”

---

3.2 训练信号：从“只看对接分数”升级到“多源监督”

当前大部分模型的监督信号仍高度依赖 Vina 等传统打分，导致：

* 上限被打分函数本身锁死
* 极易学会“打分黑科技”（刷分），而非真实物理规律

从 MolGenBench 的结果看，下一步值得引入的信号包括：

* 真实实验活性数据（ChEMBL、BindingMOAD 等）
* 多任务属性（ADMET、合成可行性）
* 物理先验（简单能量项、clash penalty、药效团约束）

真正有潜力的是多源监督下的统一模型，而不是再做一个“更 fancy、但仍然只盯着 Vina 的扩散模型”。

---

3.3 场景聚焦：与其 All-in De novo，不如从 H2L 做起

MolGenBench 的结果非常明确：

* 完全从头的 de novo 生成 → 活性 hit 极少、验证成本极高
* 挂在 fragment/series 上的 H2L 优化 → 模型性能明显改善，结果更可用

对企业项目来说，一个更现实的应用形态是：

内部已有：

* 片段 / hit / series
* 少量初期 SAR

引入生成模型在局部化学空间内进行：

* 侧链替换 / R 基团优化
* 多目标（活性 + ADMET + 合成难度）平衡
* 帮助药化更高效地“刷思路”，而不是替代药化

---

4 对 CADD/AIDD 实战的几条硬核建议

结合 MolGenBench 的结论，可以给一线团队几条相对直接的建议：

4.1 评估任何生成模型之前，先做“小型 MolGenBench”

* 在你关心的靶点上，构建一份自己的“小型真实活性库”
* 测一测模型的：
   * Hit/Series rediscovery 能力
   * TAScore（靶点差异性）
   * 构象物理合理性（可用 PoseBusters 或内部规则）

如果某个模型连这些基本指标都站不住，就不要指望它在项目中“爆冷”。

---

4.2 在管线中优先落地 H2L，而不是全流程替代

建议的 pipeline 更像这样：

```
已有 fragment / hit / series
        ↓
基于结构的生成模型（DiffDec/Delete/DiffSBDD-inpainting 等）
        ↓
化学规则过滤（PAINS, Brenk, Lilly, 企业自定义黑名单）
        ↓
快速打分筛选（多打分函数 + ML 活性预测）
        ↓
药化 review + 合成可行性评估
        ↓
少量关键化合物进湿实验
```

而不是：

de novo 模型 → 一次性生成几十万 SMILES → 简单按 Vina score 排序 → 直接送实验。

---

4.3 把化学过滤和物理检查前移，而不是最后救火

MolGenBench 显示：

* 约 70% 的参考活性分子可以通过工业级化学过滤
* 但多数生成模型的“通过率”远低于这个数

这意味着：

* 模型生成端本身不带“药化常识”
* 若不在前期就引入过滤器，很容易浪费大量算力去处理 一眼药化就会否决的垃圾分子

实操建议：

* 在模型训练/采样阶段就引入：
   * PAINS/毒性片段过滤
   * 合成可行性粗筛
   * 企业自定义的“禁用片段”库

---

4.4 对生成构象保持理性怀疑

哪怕是 MolCraft 这类在构象上最强的模型：

* 其“高质量 pose”比例在严格判据下仍有限
* 对于精细结构基础任务（FEP、相对自由能计算）来说仍然不够

所以：

生成构象可以作为一个好起点，但不能当“终极真相”。  
 关键 project 上，仍需对生成 pose 做：

* 局部重对接 / Energy minimization
* MD 采样或更细致的构象搜索

---

5 不足与未来方向：MolGenBench 也不是“终点站”

作者在文中也坦率地讨论了 MolGenBench 自身的局限，我们可以再顺势往前推一步：

5.1 参考活性空间并不完整

* ChEMBL 中的“无活性记录”，并不意味着真的无活性
* 当前的 Hit Rediscovery 指标更像是“下限评估”，不能完全代表模型探索“未知活性区域”的能力

这要求我们在解读结果时保持一个基本意识：模型没找到的，并不一定是假阴性；找到的，也不一定是最优。

---

5.2 10 µM 的阈值有其任意性

* 对某些靶点来说，10 µM 是可接受的 hit
* 对另一些则可能过于宽松或过于严格

未来可以探索靶点特异的分层评估： 例如按 MoA 或靶点家族定义不同的活性 cut-off。

---

5.3 H2L 评估依赖 MCS，有可能低估 scaffold hopping

* 强制要求 series 内存在大 MCS
* 对“彻底换骨架”的 H2L 模式（scaffold hop）友好度不足

这部分的评估，在未来也许需要与骨架层面的分簇 + 活性变化分析结合。

---

5.4 ADMET 维度几乎还没被纳入

当前 MolGenBench 的主战场仍在“活性 + 构象”，而工业界越来越在意：

* 溶解度
* 代谢稳定性
* hERG/心毒
* DDI 风险

这些多目标优化（multi-objective）未来很有可能成为“下一代 MolGenBench 2.0”的核心内容。

---

6 深度 Q&A：从“考核模型”走向“反思整个评估体系”

最后，用几个问题来凝练这篇工作的本质启发。

---

Q1：Rediscovery（重发现已知活性分子）到底是不是一个“好指标”？

短答：既必要，又不充分。

* 必要：如果模型连“已知活性骨架”都覆盖不好，很难相信它学到了合理的 SAR，更多只是生成“看起来像药”的分子。
* 不充分：生成模型的使命之一是探索未知化学空间，单纯追求高 Rediscovery 会鼓励模型过度记忆训练数据，抑制创新骨架的出现。

---

Q2：既然 Vina 不准，那基于 CrossDock 训练出来的模型还有价值吗？

有，但有明显天花板。

* CrossDock 提供了大规模、多构象的“粗糙监督”，对模型学习“口袋形状–配体占位”的关系仍然有价值。
* 但它把模型的上限锁定在 “Vina 打分能达到的水平”，难以学到超出打分函数之外的物理规律。

可能的破局方向：

* 更多依赖 BindingMOAD/高质量晶体结构 + 少量高精度物理模拟数据（FEP、MD）
* 引入“teacher model”（例如更精准的物理打分或实验活性预测模型）作为软标签

---

Q3：为什么模型在新靶点上的崩盘如此普遍？

本质上，这是“几何深度学习”的半吊子问题。

* 目前很多 3D GNN / Equivariant 模型，学到的更多是“几何填充模式”（哪里有空腔就塞原子），
* 而非真正意义上的“相互作用物理”（静电配合、疏水分布、去溶剂化代价等）。

再叠加训练数据分布高度偏向少数常见靶点（kinase 类等），泛化到新靶点自然极其困难。

---

Q4：那我们该如何设计“下一代更靠谱的 SBMG”？（思路清单）

结合 MolGenBench 的结果，可以列出一个极简思路清单：

1. 先做好 H2L，再谈大规模 de novo
2. 把大模型学到的分子语言（SMILES/SELFIES 预训练）与 3D 结构生成结合
3. 用多源监督替代“唯 Vina 论”：实验活性 + 预测模型 + 简化物理能量
4. 在训练阶段嵌入药化过滤器和物理合理性检查，而不是当成后处理
5. 以 Pareto 多目标优化为设计原则，而不是简单线性加权打分

---

🔥 来自一线从业者的尖锐意见：

“CrossDock2020 很适合做论文创新，但未必能训练出真正能落地的 SBMG 模型”

MolGenBench 的结果其实狠狠戳穿了一个行业内大家心照不宣但很少在论文里说破的事实：

CrossDock2020 是一个“非常适合研究创新”、但“极其不适合训练能在企业落地的模型”的数据集。

为什么这么说？

 我们从实战角度给出几个不那么政治正确、但非常真实的理由：

---

1.CrossDock 本身是“对接数据生成的数据”，错误和偏差会层层放大

CrossDock 的大量构象是由 Vina 等对接程序模拟出来的：

* 对接 pose 的平均误差远高于真实晶体
* 结合能估计误差非常大（经典打分函数先天不足）
* 错误 label 会成为模型训练的“监督信号”
* 模型上限直接被打分函数“天花板”限制

模型越强，就越容易学到对接方法的偏差。  
 甚至会比对接方法本身更“迷信”它的错误模式。

---

2.数据分布极不均衡，严重偏向常见口袋（kinase 等）

CrossDock 里靶点的构象分布、生化环境、本身的底层分布非常“集中”：

* Kinase/GPCR 类口袋过度代表性
* 小而浅的口袋或非典型蛋白几乎没有
* 真实药企管线里那些“难搞靶点”（PPIs、蛋白–RNA 等）完全缺席

导致模型训练后出现典型的\*\*“同质化盲目自信”\*\*：

* 在训练集内的靶点上一切看上去都很美
* 一旦换到真正新靶点，性能迅速坍塌（MolGenBench 清清楚楚验证了这一点）

企业真正痛点是什么？

永远不是“再做一个 EGFR / CDK6 的模型”，而是那些训练集中根本没有出现过的新靶点。

CrossDock 对此几乎毫无帮助。

---

3.CrossDock 是“对接范式”的数据，而不是“真实药物化学”的数据

在 CrossDock 的世界里：

* 分子的立体结构可以随意扭曲
* 功能团可以插入奇怪 pose
* 蛋白 pocket 也常常被重采样、对接到奇怪的位置

模型学到的往往是：

“如何塞进 Vina 认为高分的位置”  
 而不是“如何产生药化学家眼中可信、物理合理、可成药的结构”

MolGenBench 的 PoseBusters 评估已经证实：

* 很多模型在 CrossDock 世界里成绩很好
* 但生成出来的 3D 结构在真实物理规则下一塌糊涂（高 internal strain、clash、能量爆炸）

企业里这类结构根本无法进入后续计算（FEP/MD）或化学评审。

---

4.CrossDock 鼓励“刷分模型”，而非“可落地模型”

因为 CrossDock 的指标（Vina 打分、对接能）容易被 hack：

* 模型可以通过生成“形状刚性、极性集中”的分子刷低 Vina score
* 可以生成不合理的构象来获得“看似更紧密的结合”
* 可以靠记忆训练集生成“伪活性分子”
* 可以通过大量采样把 tail event 刷出来，假装“高分子很多”

这在学术界容易“SOTA”，但在企业里 100% 无法落地。

MolGenBench 清晰地告诉我们：

* 这些“高分子”几乎全都不通过工业过滤器（PAINS、Brenk、Lilly）
* 构象物理合理性极差（高 clash、扭曲键角）
* 真正 hits 的比例接近于零

换句话说：

CrossDock 给你了一个“能刷榜但不能成药”的训练环境。

---

5.在 CrossDock 上过拟合，很可能让模型在真实靶点上“集体溃败”

MolGenBench 的最刺眼发现是：

* 模型在训练集内靶点上“看似懂了结构”
* 到新靶点时完全不会“泛化”

这是因为 CrossDock 的蛋白–配体关系是“伪物理”的。

真实世界里：

* 静电相互作用、疏水模式、指向性氢键、去溶剂化等因素高度复杂
* CrossDock 根本没办法提供这种细粒度信息
* 也就无法支持模型学习“跨靶点的物理规律”

这才是企业最关心的能力。

---

结束语：从“能生成”到“能用上”

MolGenBench 做的一件事，说大不大，说小不小：

* 它没有提出一个新的 SOTA 模型；
* 也没有用花哨的 architecture 把评估指标再往上“抬一位小数”；

它做的，是更基础却更重要的一步：

把 SBMG 从“好玩”拉向“好用”，  
 让所有后来的工作，不得不先回答一句：  
 ‘你在 MolGenBench 上表现如何？’

对我们这些在 pipeline 里摸爬滚打的 CADD/AIDD 从业者来说，这可能才是最值得欢迎的进展。

  
文章链接：https://www.biorxiv.org/content/10.1101/2025.11.03.686215v2

代码链接：https://github.com/CAODH/MolGenBench

本文为个人解读，如有疏漏或理解不当之处，欢迎指正交流。对于SBDD/SBMG模型的现状与未来，也期待听到各位的见解。觉得有价值的话，欢迎转发分享\~

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
