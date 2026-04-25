---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzYzODI1OTAzNA%3D%3D&mid=2247486534&idx=1&sn=3fc9a1cecb3b71c12dbac0faebf60872
canonical_url: https://mp.weixin.qq.com/s?__biz=MzYzODI1OTAzNA%3D%3D&mid=2247486534&idx=1&sn=3fc9a1cecb3b71c12dbac0faebf60872
source_domain: mp.weixin.qq.com
title: 【重磅】蛋白设计进入“全原子生成”时代，BoltzGen 正式登陆 SciMiner 平台！
author: 
published_at: 
fetched_at: 2026-04-25T02:04:07Z
extractor: wechat_worker
content_hash: c9dfbf9fb2278a5222183e63032ce45204ab3872c01cc7f4d6c2b843da5716e3
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/JRd5vo3IIOhCte6vEZDZpiaA7XxIs4ybia2AGibebaMse5RbGWZzK6ib5xdibABA3Jc1gLa2vMYgBCosWnBfzA1hTYw/0.jpg) 

# 【重磅】蛋白设计进入“全原子生成”时代，BoltzGen 正式登陆 SciMiner 平台！

原创 Sciminer小助 Sciminer小助 [ SciMiner科学矿工 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在生物医药研发中，寻找一个能够精准、稳定结合靶点的 Binder，几乎是一切干预策略的起点。无论是单克隆抗体、纳米抗体，还是功能性多肽与全新蛋白支架，研究者面对的始终是同一个问题：

如何在近乎无限的序列与构象空间中，同时满足“能折叠、能结合、还能发挥功能”？

过去几年，AlphaFold、RFdiffusion 等模型极大推动了结构预测与生成式设计的发展，但在真实研发中，研究者很快会意识到：

● 结构“看起来合理”，却难以稳定折叠

● 能折叠，却在界面力场上不够精细，结合不稳

● 流程割裂：设计、折叠、验证被拆成多步，试错成本极高。

真正缺失的，是一种能够在原子尺度上，把“设计”和“折叠”视为同一问题的方法。

这正是 BoltzGen 的核心突破，也是 SciMiner 将其作为“通用 Binder 工厂”引入平台的根本原因。
  
  
###   **BoltzGen 到底是什么？**

如果只用一句话概括：

BoltzGen 是一个在单一全原子扩散框架中联合生成结合体结构，并同时确定 Binder 残基类型的通用设计模型。

但更准确地说，它并不是一个“单点算法”，而是一整套围绕 全原子生成 构建的 Binder 设计体系。它关注的不是“某一类蛋白怎么设计”，而是更本质的问题：

在给定靶标与约束条件下，什么样的原子级结构才能稳定存在并产生有效结合？
  
  
## 核心思想：全原子生成扩散 + 设计与折叠一体化

BoltzGen 的技术核心，是一个 全原子生成扩散模型（All-atom Generative Diffusion）。

#### 1\. 统一设计与折叠，而不是“串联流程”

与传统“先生成结构 → 再补序列→ 再折叠验证”的串联方法不同，BoltzGen 在同一个模型中同时训练两件事：三维结构生成与氨基酸类型确定。

它采用纯几何表示，通过 14 原子残基表征 + 虚拟原子编码，其中残基类型不是离散分类输出，而是通过虚拟原子在 backbone 原子附近的叠放数量进行几何编码，并以 0.5 Å 阈值解码。在连续三维空间中生成原子坐标，让残基身份随着几何合理性自然“浮现”。这意味着：结构稳定性与化学合理性不再是事后筛选条件，而是生成过程的一部分。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhCte6vEZDZpiaA7XxIs4ybiau8CC2C76rt0zNYBQlrgvuXUr0S8NNlyWLT9wxuGI5nibp84tloSTJTw/640.png)

#### 2\. 扩散过程：从噪声到“可结合结构”

在推理阶段，BoltzGen 的工作方式可以理解为一个逆扩散过程：

● 起点：一个被完全噪声化（随机化）的“靶标 + 待设计 Binder”原子系统。

● 过程：模型通过学习去除噪声，在 3D 空间中逐步重建原子位置。

● 终点：一个满足几何、化学与界面约束的全原子结合体结构。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhCte6vEZDZpiaA7XxIs4ybiaibxbse7nfBGpt3aLZK56kgLdUSalw5p56icMSuCswdyiaJ1iaITbsUicBXA/640.png)
  
  
## 系统架构：三位一体的“通用 Binder 工厂”

从工程视角看，BoltzGen 并不是孤立运行的模型，而是一条高度自动化的设计流水线，由三部分协同完成：

BoltzGen（扩散内核）

在 3D 原子空间中对“靶标 + Binder”整体做扩散去噪，直接生成全原子结合体结构，是整个系统的“创造引擎”。

BoltzIF（Inverse Folding）

给定生成的 3D 结构，反推出什么样的氨基酸序列能稳定该结构。这一步用于序列精炼，解决了“结构好看但序列难实现”的问题。

Boltz-2（Refolding & Scoring）

将设计序列重新折叠，检查是否能折回原始构象，同时输出 pTM / pAE 等置信度指标，并用 refold RMSD 等一致性指标做过滤；再结合界面氢键/盐桥、埋藏面积（buried surface area / delta SASA）、序列溶解性与最大疏水斑块等指标进行排序。在小分子靶点场景下，还可额外给出 affinity 估计，作为排序参考。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhCte6vEZDZpiaA7XxIs4ybiaZO4kqoXA7Tav4KJLibrMere11Ax1Zj9ibtS7nc7z0wheaJ1MfbEB67nQ/640.png)
  
  
## 为什么说它是真正“通用”的？

在论文中，同一套 BoltzGen 体系被用于多种差异极大的挑战性任务：

● 纳米抗体 & 全新蛋白 Binder：9 个全新靶点，每个靶点验证 ≤15 个候选，在 66% 的靶点上获得 nM binder（蛋白 binder 同样为 66%）。

● 无序蛋白区域（IDRs）：针对 NPM1 区域设计出具活细胞定位功能的肽段。

● 多模态靶点：涵盖线性肽、二硫键环肽、甚至覆盖小分子靶点的结合蛋白设计（论文中对两类小分子给出了几十–数百 µM 的弱结合验证，证明通用模型在该模态可用）。

真正重要的并不是“覆盖面广”，而是这些任务共用同一个全原子生成内核，实现了真正的通用化设计。换句话说，BoltzGen 并不是为不同任务定制不同模型，而是为“结合”这一物理过程本身建模：不预设蛋白还是肽；不假设是否有序；不限定结合模态。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhCte6vEZDZpiaA7XxIs4ybiaU1pZtdM8c7icCE9R3cwoI81LLLriaLDsLvM8Ib4Ugkdn7EgibQZ6Pl6YQ/640.png)
  
  
## 当 BoltzGen 遇见 SciMiner：从论文能力到科研生产力

BoltzGen 的原生使用门槛极高：显存消耗大、参数复杂、部署环境苛刻。对绝大多数研究团队而言，真正的难点并不在于理解论文思想，而在于如何把这套全原子级别的设计方法稳定、可控地运行起来。SciMiner 的价值，在于把这套“全原子工厂”真正变成可落地的科研生产力。

在 SciMiner 平台上，BoltzGen 的能力被组织为五类清晰的设计入口，对应论文中已经验证过的核心应用场景：

● Protein Anything：针对蛋白 / 肽靶点，从头设计全新蛋白 Binder

● Peptide Anything：设计线性肽或环肽，与指定蛋白界面结合

● Protein–Small Molecule：以小分子结构为起点，生成特异性结合蛋白

● Antibody Anything：在给定或 de novo 框架下，精确控制 CDR 区域进行抗体设计

● Nanobody Anything：针对单域抗体场景，进行高自由度 Binder 生成

这些入口并不是简单的参数封装，而是将 BoltzGen 的设计规范语言工程化落地。用户只需明确三件事：靶标是什么、结合界面在哪里、需要哪些结构约束，其余全原子扩散、逆折叠与重折叠验证流程，均由平台自动完成。

在保持易用性的同时，SciMiner 仍完整保留了论文级约束能力，例如结合位点指定、长度与环化控制、二级结构偏好等，使 BoltzGen 真正从“论文方法”进入科研决策流程。
  
  
、
  
  
### 实测案例：针对溶酶体氨基酸传感器 Rag GTPase 的 环肽 Binder 设计

为了验证 BoltzGen 在复杂靶点上的实操能力，我们在 SciMiner 平台上针对 RagA-RagC 复合体（PDB: 6WJ3） 进行了 Binder 设计。

设计背景：RagC是 mTORC1 信号通路中的关键开关。我们选取 6WJ3 的 G 链（Ras-related GTP-binding protein C） 作为靶标，利用 BoltzGen 的 Peptide Anything 模块进行针对性设计。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhCte6vEZDZpiaA7XxIs4ybiaJ0j4AZ4wibFA9wzfSdeqN3iavwRfwrTrn5yPQP1ZuE5N6HbIpg1Gz1Hg/640.png)

参数配置

系统自动完成了 50 个初始设计并进行了全流程验证，实测结果显示：

● 高置信度与高一致性：多组设计（如 6wj3\_design\_35）展现出极佳的 pTM（最高达 0.72）与 pAE 指标。特别是 Rank 1 的 pAE 仅为 6.359，配合低至 1.37A 的 filter\_rmsd，说明生成结构与重折叠构象高度一致，设计极度可靠。

● 原子级结合精准：生成的 Binder 与 RagC 界面建立了稳固的物理化学作用，多项设计观察到多达 6-7 个界面氢键（如 6wj3\_design\_20/06/11），且 delta\_sasa（埋藏表面积变化）表现优异，预示着强劲的结合亲和力。

● 物理性质均衡：模型给出的 Rank 1-10 候选序列不仅结合力预测出色，在疏水性指标（design\_chain\_hydrophobicity）上也表现出良好的溶解性潜力，规避了常见的人工设计蛋白易聚集问题。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhCte6vEZDZpiaA7XxIs4ybiaD3WvdrR8unvDX2FZBHRjicIgcBseZCDibGP0ZBCIGbGGoDdklFnwr0aQ/640.png)

输出结构

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhCte6vEZDZpiaA7XxIs4ybiaKdSFicozpBiaQGvsHyGNvgQTQztnRgUcqukoxPmtvvwDWQGDD98B2PvA/640.png)

输出结果
  
  
、
  
  
### 从“能生成结构”到“能生成候选”

BoltzGen 的出现，标志着蛋白设计正在从结构预测时代，跨入原子级功能生成时代。

而 SciMiner 的目标，是让这种能力不再停留在代码仓库和图表中，而是进入真实科研实践：设计，即折叠；生成，即候选。

🚀 立即在 SciMiner 上体验 BoltzGen，开启您的全原子 Binder 设计之旅。

https://sciminer.tech/
  
  
、
  
  
## 推荐阅读：

* [AI赋能下的蛋白设计：RFdiffusion vs. BindCraft，谁是下一代研发利器？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzYzODI1OTAzNA==&mid=2247486337&idx=1&sn=c604acd838e87551e62dffe82dab9cd8&scene=21#wechat%5Fredirect)
* [重磅！RFdiffusion3.0 正式上线，这波性能飞升你绝对不能错过！](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzYzODI1OTAzNA==&mid=2247486373&idx=1&sn=cbc38bc97f4d910c3a0e41dc558480d9&scene=21#wechat%5Fredirect)
* [让蛋白结合体设计更简单](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzYzODI1OTAzNA==&mid=2247486276&idx=1&sn=037913187119440c3e17c9f896e9741f&scene=21#wechat%5Fredirect)[：](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzYzODI1OTAzNA==&mid=2247486276&idx=1&sn=037913187119440c3e17c9f896e9741f&scene=21#wechat%5Fredirect)[BindCraft 正式上线 SciMiner](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzYzODI1OTAzNA==&mid=2247486276&idx=1&sn=037913187119440c3e17c9f896e9741f&scene=21#wechat%5Fredirect)

预览时标签不可点

修改于 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhjk0xxKKibZ7B721J3CPIp4dHy1ic63862A0PIIXjt5ibVbIBcXN2VErxhVq7NIicb7Bo6m0A0zVyzkg/0.png) 

 SciMiner科学矿工 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/JRd5vo3IIOhjk0xxKKibZ7B721J3CPIp4dHy1ic63862A0PIIXjt5ibVbIBcXN2VErxhVq7NIicb7Bo6m0A0zVyzkg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
