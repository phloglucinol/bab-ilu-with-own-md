---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk3NTQ2NjI1Mg%3D%3D&mid=2247485505&idx=1&sn=5a58fb1fcb0906b9a4975d5e9d42a401
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk3NTQ2NjI1Mg%3D%3D&mid=2247485505&idx=1&sn=5a58fb1fcb0906b9a4975d5e9d42a401
source_domain: mp.weixin.qq.com
title: 北大来鲁华团队发布SynCraft，让“不可合成”的分子起死回生！
author: 
published_at: 
fetched_at: 2026-04-25T02:04:00Z
extractor: wechat_worker
content_hash: 9e11f51a8133a55efae6efc9712ff10972d02c318ac6ce6e8895f1001e96b253
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/rNo1wibelVwIfsqtF658B6I0wqRFQxU4QvU0CMJqET5HCJicEPuoiaqBpqhHicW3ATZGFyp5mldjIjDDfDXqBPxayA/0.jpg) 

# 北大来鲁华团队发布SynCraft，让“不可合成”的分子起死回生！

原创 致富智网 致富智网 [ 生化环一圈 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

“SynCraft 并不是又一个分子生成模型，而是第一次系统性地把“药物可合成性优化”重构为一个“可解释、可执行的分子编辑问题”，让大模型真正学会“怎么改分子”，而不是“瞎生成”。”

生成式 AI 已经可以设计出“看起来很强”的分子，但现实是：  
**大量高分子结构根本合成不了。**

以往方法要么：

* **事后过滤**（好分子被大量丢弃）
* **模板/积木约束生成**（新颖性被严重压缩）
* **投影到最近的可合成分子**（结构被“掰断”）

这篇论文提出 **SynCraft**：  
👉 **不重新生成分子，而是让大模型预测“原子级编辑步骤”，对分子做最小、最精准的修改，跨过“合成悬崖”。**

关键思想包括：

* 把问题从 **“生成 SMILES”** 改成 **“预测编辑指令序列”**
* 利用 LLM 的**化学推理能力**，但避开其**化学语法不可靠**的问题
* 编辑由**确定性化学工具执行**，保证结构永远合法
* 可引入 **蛋白–配体相互作用约束**，避免破坏关键药效基团

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwIfsqtF658B6I0wqRFQxU4QflKSibILdOjaYU8WqjKqqTX8f10NmHeZKpRr7kictuuEric0C4JBsYulg/640.png)

文章直达：SynCraft.pdf

本文的主要作者来自 **北京大学 (Peking University)**。

* **通讯作者**：**来鲁华 (Luhua Lai)** 教授。来教授是著名的物理化学家，北京大学化学与分子工程学院教授，主要研究领域包括基于结构的药物设计（SBDD）、AI制药、蛋白质工程及系统生物学。
* 以往研究包括开发了多种著名的药物从头设计工具（如LigBuilder）。
* 近年来，团队积极探索生成式AI在药物设计中的应用，例如文中提到的 **Pocket2Mol**和 **ResGen**等3D分子生成模型，以及逆合成分析工具 **SimpRetro**。
* SynCraft 可以看作是该团队在发现前代生成模型（如ResGen）生成的分子存在合成难题后，提出的针对性解决方案，体现了研究的连贯性和对实际应用问题的关注。

  
**一、研究背景 & 动机**

### 为什么这是一个“真问题”？

* 当前 de novo 分子生成模型（Pocket2Mol、ResGen 等）  
👉 **目标函数高度偏向 docking / 打分**
* 结果是：  
👉 **高分 ≠ 可合成**
* 在真实项目中，大量候选分子会因为“太难合成”被直接搁置

以往解决思路的根本问题：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwIfsqtF658B6I0wqRFQxU4QlEObTICgpsibWxDa0VC08y59rMMRaQGE0l0LfKKiafYr3e3y5HUNBQyg/640.png)

### 论文提出的新视角

> **很多不可合成分子，其实只差“一两刀精准修改”就能变得可合成。**

作者将其类比为药化中的 **Activity Cliff**，并提出新概念：

> **Synthesis Cliff（合成悬崖）**  
> —— 极小结构修改 → 合成可行性发生巨大跃迁

**二、方法**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwIfsqtF658B6I0wqRFQxU4Q0Aw4Mxavic0yCB6NSFFdYLxt8oKLuGhVLmTdtxhH0fTPvrercNyHfMw/640.png)

### 1️⃣ 核心思想：生成 ≠ 编辑

SynCraft 把任务重构为：

> **“预测一系列原子级编辑操作”**

而不是：

* 直接输出 SMILES
* 或在模板空间里搜索

### 2️⃣ 编辑动作空间（Action Space）

LLM 只能输出以下**严格受限的指令**：

* `DEL_ATOM`
* `ADD_ATOM`
* `MUTATE_ATOM`
* `ADD_BOND / DEL_BOND`
* `CHANGE_BOND`
* 手性 / 构型设置

👉 **完全避免非法分子**

### 3️⃣ 合成悬崖数据集（Synthesis Cliff Dataset）

作者构建了约 **3332 对**：

* ❌ 不可合成分子（来自 5 个生成模型）
* ✅ 与之高度相似、但**可商业购买**的分子

并自动提取：

* 最小编辑路径
* 再由 LLM 反向生成“药化学理由”

👉 得到一个：  
**“结构变化 + 专家级解释 + 可执行编辑”的参考库**

### 4️⃣ 推理方式：RAG + Chain-of-Thought

推理时流程是：

1. 相似分子检索（few-shot）
2. LLM **先写化学推理**
3. 再输出 JSON 编辑指令
4. 化学工具执行

### 5️⃣ 进阶：Interaction-aware 编辑

* 通过 docking + PLIP 提取关键相互作用
* 转写成自然语言约束：  
> “Atom 14 与 LYS43 形成关键氢键，不可破坏”
* 注入 prompt  
👉 **保证合成优化 ≠ 药效破坏**

  
**三、结果讨论**

### 结论一：跨越“合成悬崖”——精准的生物等排体编辑

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwIfsqtF658B6I0wqRFQxU4QiaQEEWib49Fp4lTMLhTyJIFhiaDQyp283sqCNsErveDZOxPvRv5Vq8tcw/640.png)

在 Figure 2a 中，ResGen生成的一个分子含有一个复杂的并环碳骨架（难以合成）。

* ChemProjector、SynFormer 等投影类方法，试图在预定义的合成空间里找“替身”，结果生成了带有苯并环丁烯的张力环结构，这不仅难合成，还可能是算法强行匹配的产物。
* SynCraft 并没有盲目搜索，而是通过推理，将饱和环上的一个亚甲基（-CH2-）替换为氧原子（-O-）。这一步“神来之笔”将难合成的碳环变成了易于构建的色满（chroman-like）衍生物，且保留了分子的整体形状 。
* SynCraft 在处理“合成悬崖”问题上表现出了超越传统投影方法的优越性。它不是在有限的数据库中寻找最近邻，而是通过“理解”化学结构，进行原子级别的精准编辑（如引入杂原子以利用更可靠的成键反应），从而在极小的改动下实现可合成性的质变。

结论二：复现专家直觉——自动识别并移除手性隐患

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwIfsqtF658B6I0wqRFQxU4QV0qxD2sm6nsFwVMaoE3KawJDUG7uajflyGjYQyxUiaic93gSpJ1NvvGA/640.png)

* **问题分子**：生成的 PLK1 抑制剂 lig-886 含有一个 2,5-二甲基哌嗪环。这在合成上是一个巨大的隐患，因为它引入了两个手性中心，可能产生多达4种立体异构体混合物，分离纯化极其昂贵 。
* **SynCraft的推理**：模型在推理链中明确指出：“...引入两个手性中心...会导致复杂的混合物...”。
* 解决方案：SynCraft 给出的编辑指令是直接切除这两个甲基（DEL\_ATOM），将分子简化为非手性的哌嗪环。这一操作与真实世界中人类专家将 lig-886 优化为最终先导化合物 IIP0944 的策略完全一致 。
* SynCraft 具备了类似人类药物化学家的“直觉”推理能力。它不仅能修复化学键连接错误，还能识别出立体化学、异构体纯化难度等更深层次的开发风险，并自主做出与人类专家高度一致的优化决策。

结论三：拯救“沉睡”的高分分子——相互作用感知的骨架跃迁

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwIfsqtF658B6I0wqRFQxU4QG5vu007c6Sjk5xNAx31RcMhEuFgsfNib74NMkzdccicXKqz9VrkOVzVA/640.png)

* **背景**：在 RIPK1 抑制剂的研发中，大量高分分子因结构太怪异而被“束之高阁”。
* 挑战：由于存在复杂的非平面稠环系统（diazepino\[1,2-f\]purine-like），且含有一个季碳中心，合成难度极大 。
* **SynCraft的操作**：在相互作用感知（Interaction-Aware）模式下，SynCraft 识别出原有骨架的关键氢键受体位置（N12）。然后，它大胆地进行了一次“骨架跃迁”（Scaffold Hopping），将复杂的稠环系统替换为平面的、模块化易合成的 2,4-二取代嘧啶骨架。
* 结果：新分子不仅合成路线清晰（通过亲核芳香取代反应），而且完美保留了与关键残基的氢键网络，Vina打分几乎没有下降 。
* 通过引入基于PLIP的相互作用感知机制，SynCraft 能够在大幅度简化分子结构（Scaffold Hopping）的同时，精准保留关键的药效团和结合模式。这使得它能够“复活”那些因合成难度而被遗弃的高活性分子，将其转化为具有实际开发价值的先导化合物 。

  
### 四、讨论：优势与不足 

✅ **优势：**

1. 高精度与高保真：通过预测编辑操作而非直接生成SMILES，SynCraft在保持母核结构特征方面远超现有模型，避免了结构幻觉 。
2. 可解释性强：基于CoT机制，SynCraft能输出完整的推理过程（Reasoning Trace），让化学家明白“为什么要这么改”，建立了人机信任 。
3. **灵活的生物约束**：通过自然语言注入药效团约束，无需重新训练模型即可适应不同的靶点需求。

  
❌ **不足与局限：**

1. 成本与速度：由于依赖大语言模型（如Gemini-2.5-Pro）的推理，SynCraft的运行成本（API费用）和时间远高于简单的模板匹配或投影方法。文中估算每优化100个分子需3-5美元 。
2. 不适合大规模库扩增：鉴于成本，它更适合用于优化少量高价值的先导化合物（Hit Optimization），而不是用于数百万级虚拟库的构建 。
3. **上下文限制**：依赖于检索到的Few-shot案例质量，如果数据库中缺乏相关的转化案例，模型效果可能会下降。

---

如果你也在研究药物发现、药靶互作预测等，欢迎扫码添加小编，共建交流群👇一起追踪最新进展！！

**合作/投稿/推广，请添加小编WX**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwIfsqtF658B6I0wqRFQxU4QCLPuvj0YB9uYrgT7gsJiaqWfW3iba3pLVTXjOiaia6NibIJ6Ec0QZZsjsCg/640.png)

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
