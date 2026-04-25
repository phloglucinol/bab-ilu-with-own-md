---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk3NTQ2NjI1Mg%3D%3D&mid=2247485458&idx=1&sn=48a2a84f1978193f5436ed62d0b61b5b
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk3NTQ2NjI1Mg%3D%3D&mid=2247485458&idx=1&sn=48a2a84f1978193f5436ed62d0b61b5b
source_domain: mp.weixin.qq.com
title: PNAS | SynFormer：让 AI 药物设计第一次真正“落地实验室”
author: 
published_at: 
fetched_at: 2026-04-25T02:04:03Z
extractor: wechat_worker
content_hash: 049950a996ee605b97cbae28c2bfe0bb3bbd697055d3cab53d6a131afe6906cc
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/rNo1wibelVwLrrzyA1wvykN8M7Js8WkKYic8JcibJiau7pW5uCOK6atP1ibiaySAOLUzFZJOF90ic14cg4ToMt6cSe26A/0.jpg) 

# PNAS | SynFormer：让 AI 药物设计第一次真正“落地实验室”

原创 致富智网 致富智网 [ 生化环一圈 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

“SynFormer 的核心贡献不是生成“更漂亮的分子”，而是第一次系统性地让生成式 AI 在“可合成化学空间”中进行导航。”

文章提出 **SynFormer**：一种**以合成路径为生成对象**的生成式 AI 框架。

* 核心思想：  
👉 **不直接生成分子结构，而是生成“从可购买砌块出发的合成路线”**
* 架构创新：
   * Transformer（路线建模）
   * Diffusion（building block 选择）
* 两大应用场景：
   1. **局部化学空间探索**（结构投影、hit 扩展）
   2. **全局化学空间优化**（RL / 遗传算法）
* 显著优势：  
**所有输出分子天然“可合成”**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLrrzyA1wvykN8M7Js8WkKYPBhSW7HpoicVQ0f7qaXt1ibbSduLzc6kehFynfib4Q4wmJSJQZWY4IaSg/640.png)

文章直达：SynFormer.pdf

**团队：** 麻省理工学院（MIT）化学工程系与电气工程计算机科学系（EECS）。

**主要作者：** Wenhao Gao (whgao), Shitong Luo, Connor W. Coley 。

**以往研究：** Connor Coley教授是AI合成领域的知名专家。该团队此前开发过 **ASKCOS**（自动合成规划平台）、**SynNet**（基于树的合成网络）和 **ChemProjector**（分子投影模型）等重要工具。SynFormer是在这些前期工作基础上的集大成之作。

**一、研究背景**

作者指出当前生成式分子设计的核心问题是：

> **生成模型经常输出实验上根本合不出来的分子**

SynFormer 的解决方案是：

* 生成**合成路径（synthetic pathways）**
* 使用 **Transformer + Diffusion**
* 在两个层面验证：
   * 局部空间（类似物、hit 扩展）
   * 全局空间（黑盒性质优化）

###   

这不是一个“再做一个分子生成模型”的工作，而是一次**建模对象的范式转移**：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLrrzyA1wvykN8M7Js8WkKYR0FC664ibQXgcJCicLETn6CpibFIKVrw4jlp9qjm5Q30oI7pH5Sic2Edcg/640.png)

**二、方法**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLrrzyA1wvykN8M7Js8WkKY49d8gFZE70vNuxZbPriax42FKByLg9sKMskVHBRJS395ars8icdvE9Rg/640.png)

### 1️⃣ 可合成化学空间如何定义？

* 223,244 个可购买 building blocks（Enamine US stock）
* 115 个反应模板（REAL + 常见有机反应）
* 最多 5 步反应
* 理论空间规模 > 10⁶⁰

📌 **关键点**：  
这是一个**规则驱动但规模极大的合成空间**

### 2️⃣ 合成路线如何被“语言化”？

作者采用 **postfix notation（后缀表达式）**：

* building block → building block → reaction
* 类似逆波兰表达式
* 能自然表达分支 / 汇合反应

👉 **这是 Transformer 能工作的前提**

### 3️⃣ 架构创新：Transformer + Diffusion

#### SynFormer 两个版本：

| 模型           | 用途                  |
| ------------ | ------------------- |
| SynFormer-ED | 给定分子 → 找可合成路径 / 类似物 |
| SynFormer-D  | 从零生成 → 性质优化         |

#### 最大亮点：building block 选择

* building block 数量巨大（20 万+）
* 不能直接分类
* 解决方案：
   * Diffusion 生成 **fingerprint**
   * 最近邻搜索匹配真实分子

📌 **这一步是论文中最关键的工程与方法创新之一。**

**三、结果讨论**

## 结论一：SynFormer 显著提升“可合成化学空间覆盖率”

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLrrzyA1wvykN8M7Js8WkKY8nE0Ig3iauj80icQdiaHoX1Wo70Va9BzQn9hHA337AvywXoG7tyuEfUdA/640.png)

* REAL Space 分子重构率：**66%**
* ChEMBL：**20%**
* 明显高于：
   * SynNet
   * ChemProjector

> **SynFormer 是目前少数能够“真正覆盖大规模可合成空间”的生成模型。**

* 生成模型最大的隐性失败：  
**“你以为你在搜索，其实模型根本到不了那片空间”**
* reconstruction rate 是：
   * 模型表达能力
   * 解码稳定性
   * 化学空间连通性  
   的综合指标
* SynFormer 证明：
   * synthesis-centric 模型并不必然牺牲覆盖率
   * Transformer 架构在路线层面具备可扩展性

  
## 结论二：SynFormer 能将“不可合成设计”投影为可合成类似物

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLrrzyA1wvykN8M7Js8WkKY6bLXCkge1YgUuVJ8sczHscPufbIiaRXvflkjsnicJtydT3NnO4Z609Sg/640.png)

* SA score 分布明显左移
* 原始分子 vs 类似物：
   * 结构相似
   * 性质保持
   * 合成可行

> **SynFormer 是一种“合成投影算子”，而不仅是生成器。**

* 现实研发中大量分子：
   * docking 好
   * score 高
   * 但“化学家摇头”
* SynFormer 的价值：
   * 保留 pharmacophore
   * 替换不可行片段
   * 输出**直接可下单的路线**
* 特别适合：
   * SBDD
   * 口袋条件生成模型的后处理

  
## 结论三：SynFormer 在 hit 扩展中优于 REAL NN 搜索

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLrrzyA1wvykN8M7Js8WkKYzbbTof6mxuiclJ2wc2mkbwIoBOibicUvQviaNSgqlBRMYVHmPoaxBIUNnw/640.png)

* JNK3 预测活性：
   * SynFormer > 最近邻搜索
* 合成路线多样性更高

> **SynFormer 不只是“找相似分子”，而是在“可合成空间中做创造性扩展”。**

* 最近邻的局限：
   * 结构连续
   * 合成路径固定
* SynFormer：
   * 相同骨架
   * 不同合成逻辑
* 对 hit-to-lead 极其关键

  
## 结论四：SynFormer 可作为“通用合成约束模块”嵌入优化算法

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLrrzyA1wvykN8M7Js8WkKYxV7Kjp09H0a3gvFuicgUTobX9V9sj3otMpSUoRtIuquFYehRaaXiahGQ/640.png)

* GraphGA-SF：
   * 性质略降
   * SA score 大幅改善
* 优于：
   * 纯 synthesis-centric 模型
   * 不受限优化模型

> **SynFormer 的真正潜力在于“模块化整合”，而不是单独使用。**

* 单一 RL 不够高效
* 单一 synthesis-centric 搜索信号稀疏
* SynFormer 作为 mutation / projection：
   * 保证合成
   * 保留搜索效率
* 非常适合：
   * 闭环实验
   * 自动化药物发现

  
**四、安装**

Github直达：https://github.com/wenhao-gao/synformer

环境创建

`# Install conda environment` `conda env create -f env.yml -n synformer` `conda activate synformer` `  
` `# Install SynFormer package` `pip install --no-deps -e .`

用法

`python sample.py \` `    --model-path data/trained_weights/original_default.ckpt \` `    --input data/example.csv \` `    --output results/example.csv`

---

如果你也在研究药物发现、药靶互作预测等，欢迎扫码添加小编，共建交流群👇一起追踪最新进展！！

**合作/投稿/推广，请添加小编WX**

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/rNo1wibelVwLzwVbZVbpOH9JictdQS8EbsUib8uW6IHBFH9x6JtPlHjicjuHiaA0SudJqicJEIcDmTSFMKtcw7G6vcZw/640.png)

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
