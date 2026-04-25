---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk3NTQ2NjI1Mg%3D%3D&mid=2247485379&idx=1&sn=0567818b5f068d12ed2bffe4b488c936
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk3NTQ2NjI1Mg%3D%3D&mid=2247485379&idx=1&sn=0567818b5f068d12ed2bffe4b488c936
source_domain: mp.weixin.qq.com
title: JMC 2025 深度评测：深挖7大主流 3D 分子生成模型到底行不行？
author: 
published_at: 
fetched_at: 2026-04-25T02:04:12Z
extractor: wechat_worker
content_hash: 9d24ae51f31ef5b57cbe7dda98f448b4175104aa0d8c078bbd885e9c58091241
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/rNo1wibelVwKHWeBfkoJIjVIetw0ibqyR0dnUTnYI7icicnJenacwFibXFaOrbor1NOICfw8ia2M25eEcW2Vd69FapKg/0.jpg) 

# JMC 2025 深度评测：深挖7大主流 3D 分子生成模型到底行不行？

原创 致富智网 致富智网 [ 生化环一圈 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

这篇文章**没有提出新模型**，而是做了一件更难、也更重要的事情： 

👉 **对当前主流 3D 结构驱动** **生成模型** **进行“化学合理性体检”。**

**![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwJawfaUibuGdkVG1F2BGhZFoXiclRYkCrxUEWxGCSBD60el5pz2dbsID4niaqAyn2QW72HxZG0lQx8qA/640.png)** 

文章直达：structure-based-generation-of-3d-small-molecule-drugs-are-we-there-yet.pdf

**一、研究背景**

在过去几年中，**结构基础药物设计（SBDD）** 正在经历一场由 AI 驱动的范式转移：

* 从 **虚拟筛选（Docking + Library）**
* 到 **基于蛋白口袋直接生成 3D 小分子**

理论上，这类 **structure-based generative models** 可以：

* 不再依赖超大化合物库
* 直接“按口袋形状与相互作用模式”生成候选分子
* 极大压缩 hit discovery 时间

但一个关键问题始终被回避：

> **这些模型生成的分子，真的“像药”吗？**

过去的评估方式大多停留在：

* docking score
* QED、SA 等简单指标
* SMILES 是否 valid

**但几乎没人系统评估：它们在化学层面是否合理、稳定、可合成。**

这正是本文要解决的核心问题。

这篇文章**没有提出新模型**，而是做了一件更难、也更重要的事情： 👉 **对当前主流 3D 结构驱动** **生成模型** **进行“化学合理性体检”。**

**二、研究方法**

### 1️⃣ 评测对象：7 种主流 3D 生成模型

包括但不限于：

* **3DSBDD**
* **Pocket2Mol**
* **TargetDiff**
* **MolSnapper**
* **PMDM / DecompDiff / DecompOpt**

统一使用：

* **CrossDock2020** 数据集
* 相同训练 / 测试划分
* 每个模型 \~10,000 个生成分子

### 2️⃣ 三个“对照组”（真实世界的药物化学）

作为“药物应有的样子”，作者引入：

* ✅ FDA 已批准小分子
* ✅ ChEMBL 临床阶段化合物
* ✅ CrossDock 数据集中的真实配体

### 3️⃣ 关键创新：两个全新的“化学合理性指标”

###   

#### 指标一：**环系统在 ChEMBL 中是否常见？**（Figure 3A）

* 提取每个分子的 ring system
* 查询其在 ChEMBL 中出现频率
* **最** **低频** **环 <100 次 → 高风险结构**

👉 直觉解释：**“几乎没人用过的环结构，往往要么不稳定，要么不可合成。”**

#### 指标二 & 三：**Bemis–Murcko Scaffold 是否存在于 ZINC20 / ZINC22？**（Figure 3B,C）

* BM scaffold 是药物化学中的“骨架核心”
* 若生成分子的 BM scaffold **在数十亿级 ZINC 库中完全不存在**
* → 极可能是 **非现实化学空间**

**三、研究结果**

## 1\. 化学合理性”第一次被量化，AI 集体不及格

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwKHWeBfkoJIjVIetw0ibqyR0C0TxovbZvBxsUmKNrdZKkh7JXx5CwibRUwxmia3F7yYicVcq5tHAwQzhg/640.png)

Figure 1 是整篇文章**最关键、也是最具方法学价值的一张图**。作者在这里首次系统性回答了一个长期被忽略的问题：**AI 生成的分子，在化学层面是否“站得住脚”？**

图 1A 使用 **ChEMBL 环系统频率（min\_freq > 100）** 作为评估指标。结果非常清晰：FDA、ChEMBL 临床分子和 CrossDock 对照组中，**超过 69% 的分子通过该标准**，而几乎所有结构生成模型的通过率都 **低于 50%**。这意味着，大量 AI 分子包含在真实药物数据库中极为罕见的环系统，暗示其**化学稳定性、可合成性或成药性存在系统性风险**。

图 1B 和 1C 进一步引入 **Bemis–Murcko scaffold 是否存在于 ZINC20 / ZINC22** 的指标。这是一个极其严格、但非常现实的判断逻辑：**如果一个骨架在数十亿规模的“drug-like”化学空间中从未出现过，那么它很可能并非现实药物化学的一部分**。结果显示，AI 模型在这两个指标上依旧显著落后于真实分子对照组，且不同模型之间差异不大，说明这是**普遍性问题，而非个别模型缺陷**。

值得特别注意的是图 1D：**PAINS filter 几乎对所有数据集都“放行”**。这直接说明，传统依赖子结构规则的过滤方法，**无法识别 AI 时代出现的“新型化学不合理结构”**。这也是作者提出新指标的现实背景——**不是规则失效，而是问题升级了**。

👉 **核心启示**： 当前 3D 结构生成模型已经严重“脱离真实药物化学分布”，而这种偏差在传统评估指标下是被系统性忽略的。

## 2\. 雷达图揭示真相：AI 学的是“结合模式”，不是“药物经验”

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwKHWeBfkoJIjVIetw0ibqyR0zQgWtwqQezuURLuGg8jrJXcRhiaflYrKQ00N5su76fnx5AWUWXnltNw/640.png)

Figure 2 通过雷达图，将多个关键分子性质（分子量、环数量、手性中心、SA、NH/OH 数量等）进行归一化对比，是理解 **“AI 为什么会生成不合理分子”** 的关键证据。

首先观察三组对照数据（FDA、ChEMBL、CrossDock），可以看到它们在所有维度上呈现出**高度一致的形状轮廓**。这说明，无论是上市药物、临床候选物，还是被用于训练的真实配体，它们都遵循相似的化学约束和设计经验。

反观 AI 生成分子，其雷达图形状与对照组出现**系统性偏移**，尤其体现在：

* **手性** **中心数量明显偏高**
* **脂环比例升高、** **芳香环** **比例下降**
* **合成可及性（** **SA** **）整体恶化**
* **NH/OH 等极性基团显著增加**

这些偏移并非随机波动，而是高度一致地出现在不同生成模型中。这说明问题**并不源于某一个具体算法，而是源于当前结构生成** **范式** **本身**：模型更倾向于通过增加立体复杂度、极性相互作用来“讨好”蛋白口袋，却缺乏对“什么样的分子才是药”的整体理解。

👉 **核心启示**： AI 在结构生成任务中学到的是 **protein–ligand interaction 的几何与能量模式**，而不是长期由药物化学实践总结出的 **化学先验知识**。

## 3\. 环系统失衡：AI 偏爱脂环，牺牲了“药物友好性”

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwKHWeBfkoJIjVIetw0ibqyR0diaON0ficNpQfpQRIddqjCYZ79T66Ic6rLZSkxoQM9fNNqX12AXvrQyA/640.png)

Figure 3 聚焦于一个非常具体、但极其重要的结构问题：**芳香环** **与脂环的比例失衡**。

从图 3A 可以看到，部分模型（如 3DSBDD、Pocket2Mol）生成的分子分子量明显偏低，乍看之下似乎更“轻量化”，但图 3C 揭示了真正的问题所在——**芳香环** **数量显著减少，而脂环数量明显增多**。

在真实药物中，芳香环不仅提供 π–π 堆积、疏水相互作用，还在代谢稳定性、构象可控性方面发挥重要作用。而 AI 模型生成的分子往往包含多个脂环，却几乎不含芳香体系，这在图 3D 给出的实例中表现得尤为直观。这类结构虽然在三维空间中更“立体”，但往往：

* 合成路线复杂
* 构象自由度过高
* 稳定性和可预测性下降

作者指出，这种偏好可能源于模型训练目标的单一性：**脂环更容易填满口袋体积、提高 docking 分数**，但这并不等价于药物化学上的合理设计。

👉 **核心启示**： 当前结构生成模型在“空间填充”与“药物可行性”之间，系统性地选择了前者。

## 4\. 手性中心泛滥：复杂度正在失控

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwKHWeBfkoJIjVIetw0ibqyR0N0llTibgCND4s9Bb0UPEficAA8sNcjdBr6AXObQoQibzGoVSicyNbFzx2g/640.png)

Figure 4 揭示了 AI 生成分子在**结构复杂度**上的另一个严重问题——**手性** **中心数量显著过多**。

数据显示，绝大多数生成模型产生的分子平均包含 **2.7–3.6 个** **手性** **中心**，明显高于 ChEMBL（\~1.6）和 FDA 药物（\~2.5）。更关键的是，这种增加并非来自明确的药效需求，而往往源于多个脂环和桥环的叠加。

与之直接相关的是合成可及性（SA）分布的整体右移。图 4A 显示，AI 分子的 SA 分数普遍高于真实药物，意味着**实验合成难度显著增加**。图 4B 中给出的示例分子则直观展示了这种“过度设计”的结果：多个手性中心嵌套在复杂环系统中，即便结构上满足指标，也极不现实。

👉 **核心启示**： AI 当前缺乏对“结构复杂度是成本”的认知，生成的不是“优化后的药物结构”，而是“工程感极强的理论分子”。

## 5\. NH / OH 过量：亲和力换来的，是糟糕的 PK 风险

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwKHWeBfkoJIjVIetw0ibqyR0bGk7NAHzsHcCM2R4YBVdSY9braYeOrwia2dia325rOeI0x0MzxF6O9nw/640.png)

Figure 5 讨论的是一个在 docking 任务中极易被忽视、但在真实药物开发中至关重要的问题：**氢键** **供体（NH/OH）数量失控**。

从图 5A 可以看到，AI 生成分子平均含有 **2.8–5.5 个 NH/OH 基团**，显著高于对照组。这一现象本身并不难理解：氢键是 protein–ligand 相互作用中“性价比极高”的手段，模型自然倾向于大量使用。

但问题在于，**药物不是只在口袋里存在**。过多的 NH/OH 会直接导致：

* 细胞膜通透性下降
* 口服生物利用度降低
* 代谢位点增加

图 5C 给出的分子尤其具有讽刺意味：**它们在所有新提出的指标上“全部通过”，却依然不是一个合格的药物分子**。这恰恰说明，单一维度的指标再先进，也无法替代对整体药物性质的综合判断。

👉 **核心启示**： AI 生成模型正在“用结合能换取可成药性”，而这种交换在现实中是不可接受的。

## 6\. 与 HTVS 的正面对决：生成并未击败筛选

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwKHWeBfkoJIjVIetw0ibqyR0X1kquMzXOXXMgnv6ibqGn01NLFlzFGVheibDrT3pr0eVParksBERDWfg/640.png)

Figure 6 是整篇文章最具现实意义的一组结果。作者将 AI 生成分子与传统 **HTVS（基于 Enamine** **HTS** **库）** 在三个真实靶点上进行了直接比较。

结果非常明确：

* HTVS hit 的 docking score **整体优于** AI 生成分子
* 在化学合理性指标上，HTVS hit **通过率更高**
* 即便是表现最好的 MolSnapper，也依赖 pharmacophore 约束才能接近 HTVS 水平

换言之，在“结合能力 + 化学可行性”这一综合目标下，**成熟的虚拟筛选流程依然更稳健**。AI 生成的优势主要体现在某些极端阈值下的 enrichment factor，但高度依赖靶点类型。

👉 **核心启示**：在当前阶段，**结构** **生成模型** **并不是 HTVS 的替代品，而是一个尚未成熟的补充工具**。

## 五、结论

##   

**这不是一篇“唱衰 AI 药物设计”的论文，而是一篇告诉我们“下一步该怎么走”的路标型研究。**

在 AI 药物研发越来越“炫技”的今天，这篇 JMC 2025 提醒我们：

* **结构对了 ≠ 化学对了**
* **分数高了 ≠ 药就来了**
* **真正的瓶颈，已经从模型能力，转向“化学认知”**

如果你从事：

* AI 药物设计
* 分子生成模型
* 虚拟筛选 / hit discovery

👉 **这是一篇必须精读、也值得反复引用的文章。**

文章给出了明确的结论和展望：

1\. **答案是“No”**：目前的基于结构的3D分子生成模型尚未达到即插即用的实用阶段（Are We There Yet? No.）。它们生成的分子虽然能完美契合蛋白口袋的几何形状，但在“化学合理性”上存在严重缺陷，充斥着不稳定结构和难以合成的特征。

2\. **评估体系需革新**：传统的QED和SA指标已不足以约束AI。必须引入基于大规模化学空间（如ZINC和ChEMBL）的统计学指标作为新的“图灵测试”，以剔除那些不切实际的设计。

3\. **未来方向**：AI的“想当然”部分源于训练数据（CrossDock）本身的偏差（如靶点类型分布不均、对接构象非最优）。未来的改进需要引入更高质量的数据集（如BindingNetV2），并在生成过程中加入明确的化学规则约束或后处理步骤，让AI不仅学会“拼积木”，更要学会“懂化学”。

---

如果你也在研究药物发现、药靶互作预测等，欢迎扫码添加小编，共建交流群👇一起追踪最新进展！！

**合作/投稿/推广，请添加小编WX**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwKvaDDSuZic2KUskmfr7ibOSRaHa8IKbHn47d1ctabtKYcokUFYz5JMbib1sBPS5LskPOjwQC3FXib7iaA/640.png)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLoZBMeRAOQfHFSPAUqY1HKdiawXTaBEKicV1ydV8rcMxkCr88HeOrM31xHyuPXibFR07KAWIjwna9UA/0.png) 

 生化环一圈 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLoZBMeRAOQfHFSPAUqY1HKdiawXTaBEKicV1ydV8rcMxkCr88HeOrM31xHyuPXibFR07KAWIjwna9UA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
