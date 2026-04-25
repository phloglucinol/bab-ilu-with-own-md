---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkzNjIzMTU0Nw%3D%3D&mid=2247548898&idx=1&sn=7ff4d3a4ca740ba749c29142131004f3
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkzNjIzMTU0Nw%3D%3D&mid=2247548898&idx=1&sn=7ff4d3a4ca740ba749c29142131004f3
source_domain: mp.weixin.qq.com
title: JCIM｜通过蛋白与配体语言模型微调实现结合亲和力预测
author: 
published_at: 
fetched_at: 2026-04-25T02:04:14Z
extractor: wechat_worker
content_hash: 232ff60e3df78bb7915d601fdc12d769825fd829244372c40709d93211d7bade
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/GSyZB2NwFcWhY647GxMzmzjl1zQBlKD1LxiaZqz3eAD7C8ML6IN46CGYEkYnZjAj3B9a7ghTXOGjWoCfZibXlcBw/0.jpg) 

# JCIM｜通过蛋白与配体语言模型微调实现结合亲和力预测

玉渡南山 玉渡南山 [ AIDD Pro ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

# ****![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcWhY647GxMzmzjl1zQBlKD1rxghibe2VNicibTdObicoX7JKm5NUhLC7LpQgoAU57uWL1ibRy4EweT3x7Q/640.png)**

01 引言

蛋白−配体结合亲和力（binding affinity, BA）预测在早期药物发现中具有关键作用，是从超大规模化合物库中识别潜在先导化合物的重要步骤。传统基于结构的计算方法，如大规模对接（giga-docking），能够生成合理构象，但在化合物排序上的表现有限。此外，自由能方法虽然预测精度较高，但对计算资源要求极大，难以用于早期筛选阶段。随着按需合成化合物库的迅速扩张，虚拟筛选规模从百万量级扩展至万亿量级，使得依赖计算效率与泛化能力的预测模型变得更加重要。

深度学习方法加速了虚拟筛选、先导发现和分子优化等流程，但在结合亲和力预测中仍面临多重限制。包括：  
（1）传统模型常依赖结构信息；  
（2）数据集常混合不同测量体系（如 IC50 与 Ki），导致噪声累积；  
（3）随机划分训练集与测试集易造成数据泄漏，使模型泛化能力被高估。

该研究提出 BALM（Binding Affinity via Language Model），利用预训练蛋白语言模型（ESM-2）与分子语言模型（ChemBERTa-2），结合参数高效微调（PEFT）方法，构建一种可扩展、计算效率高、且具备更强泛化能力的结合亲和力预测框架。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcWhY647GxMzmzjl1zQBlKD15x3NT5KpCfqQO8xJLGHO5SV4ZvNRy9w7teB4Pcib1ib758ibvgEx2l7aQ/640.png)

图1: BALM架构概述

02 研究方法

### ****2.1 模型设计总体结构**

BALM 为序列基础（sequence-based）的深度学习体系，输入为蛋白序列与配体的 SMILES 字符串。其核心思想是在统一嵌入空间中，通过蛋白—配体距离（以余弦相似度度量）直接表示结合亲和力。  
模型通过以下步骤实现训练：

使用 ESM-2 编码蛋白序列；使用 ChemBERTa-2 编码配体 SMILES；分别将两者映射到共享潜在空间；优化蛋白与配体嵌入之间的余弦相似度，使得高 pKd 的配体靠近蛋白，低 pKd 的配体远离蛋白。

这一方式突破了传统的“拼接特征 → 回归预测”的方法，而是以度量学习（metric learning）的方式直接建模配体与蛋白间的相互作用强度。

### ****2.2 数据与评价方式的改进**

作者指出，当前许多亲和力预测模型在数据与评估层面存在三大问题：

1. 混合 IC50 与 Ki 数据导致测量噪声；
2. 不同来源实验条件不一致；
3. 随机划分数据集会导致“相似化合物同时出现在训练与测试中”的数据泄漏问题。

为解决这些问题，研究采用：  
（1）基于 BindingDB 的严格筛选数据集；  
（2）基于靶点、配体骨架（scaffold）、药物结构三种划分方式，以模拟“预测新靶点/新骨架/新化学空间”的真实应用场景；  
（3）采用多种指标度量模型表现，例如皮尔逊相关系数、RMSE 等。

### ****2.3 参数高效微调（PEFT）**

由于 ESM-2 与 ChemBERTa-2 参数量极大，直接微调会带来巨大的计算成本。因此 BALM 引入 PEFT，使得仅需微调少量参数即可使模型适应亲和力预测任务。

研究使用以下 PEFT 方法：

* LoRA（Low-Rank Adaptation）
* LoHa（LoRA + Hadamard）
* LoKr（LoRA + Kronecker）
* IA³（Additive adapter method）

这些微调方法通过在注意力矩阵或中间表示中引入少量额外参数，使训练更为轻量，同时避免“灾难性遗忘”。

### ****2.4 基线模型与 BALM 的比较**

基线模型采用传统深度学习流程：

1. 使用相同的蛋白与配体编码器；
2. 拼接两者的特征；
3. 使用全连接层预测 pKd；
4. 使用 MSE 损失训练。

BALM 则为度量学习框架，通过优化蛋白−配体嵌入之间的余弦相似度，而不是直接进行回归。这样的优化目标更接近实际物理意义，即“更强的结合对应更近的距离”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/GSyZB2NwFcWhY647GxMzmzjl1zQBlKD1hs7XxWcW2bzkia6xFRJhaP9JPTFg1UDEEx9rw3icuI1NMic78mqF4icWQw/640.png)

图2: BALM 在具有挑战性的数据划分上表现优于基线模型，并且参数高效的微调进一步提高了其性能

03 结果分析

论文包含了多个数据集上的实验，重点包括：

* 基于 BindingDB 的大规模数据集；
* 针对特定靶点（如 USP7、Mpro）的 few-shot 学习；
* 与 AutoDock Vina 等对接方法比较；
* 与传统机器学习方法比较（如随机森林、神经网络等）。

实验显示，BALM 在预测未见过的靶点、化学骨架以及药物结构时都具有更好的泛化性能。特别是在仅有少量样本的 few-shot 场景中，BALM 仍然优于基线方法以及对接方法。

这说明度量学习式的建模方式能够更有效地利用序列信息与语言模型的特征学习能力。

04 ****研究主要贡献**

研究贡献主要体现于以下几个方面：

### ****1\. 提出 BALM：绑定于度量空间的预测框架**

相较传统“端到端回归预测”，BALM 基于蛋白−配体嵌入距离直接建模 pKd。这一方式更贴近相互作用本质，同时提升了模型在新靶点上的泛化能力。

### ****2\. 融入大规模语言模型的序列基础方法**

使用 ESM-2 与 ChemBERTa-2，可在没有三维结构的情况下完成亲和力预测，避免了对蛋白结构质量的依赖。

### ****3\. 参数高效微调（PEFT）降低计算成本**

PEFT 对于构建可扩展的药物开发模型具有显著意义，使得模型能在有限资源的情况下高效适配任务。

### ****4\. 全新的严格评价体系**

研究强调“随机划分”造成的数据泄漏问题，提出以靶点、骨架、药物等维度进行划分的方法，更客观反映真实应用场景中的模型表现。

这为未来结合亲和力预测模型提供了一套更可靠的评估标准。

05 ****结论**

该研究提出了 BALM，一种基于蛋白与配体语言模型微调的结合亲和力预测方法。模型通过度量学习式训练，将亲和力映射为蛋白−配体嵌入空间中的距离。通过大规模语言模型、PEFT 技术和严格的数据划分方法，BALM 在多个典型场景中展现出优于传统深度学习模型与对接方法的泛化能力，特别是在新靶点与少样本场景中表现突出。

模型的计算效率、适应性与可扩展性，使其适合用于早期大规模虚拟筛选，具有较高的药物发现应用潜力。

## ****参考文献**

Gorantla, R., Gema, A. P., Yang, I. X., Serrano-Morrás, Á., Suutari, B., Juárez-Jiménez, J., & Mey, A. S. J. S. (2025). Learning Binding Affinities via Fine-Tuning of Protein and Ligand Language Models. **Journal of Chemical Information and Modeling.** https://doi.org/10.1021/acs.jcim.5c02063

**版权信息**

本文系AIDD Pro接受的外部投稿，文中所述观点仅代表作者本人观点，不代表AIDD Pro平台，如您发现发布内容有任何版权侵扰或者其他信息错误解读，请及时联系AIDD Pro (请添加微信号Cynthia\_qin1114)进行删改处理。

本文为原创内容，**未经授权禁止转载，授权后转载亦需注明出处**。有问题可发邮件至qinxin@stonewise.cn

****关注我，更多资讯早知道↓↓↓**

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/GSyZB2NwFcVEduxRt4IviciaicmLciaV7xcHYG2MrpsblicPZib20yh4vNNOmdNftgu0icAl8AlnonUepCX6MOc7vYcMQ/0.png) 

 AIDD Pro 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/GSyZB2NwFcVEduxRt4IviciaicmLciaV7xcHYG2MrpsblicPZib20yh4vNNOmdNftgu0icAl8AlnonUepCX6MOc7vYcMQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
