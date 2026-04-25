---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247484430&idx=1&sn=d75cee7e43cb099559219e1653ed99c7
canonical_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247484430&idx=1&sn=d75cee7e43cb099559219e1653ed99c7
source_domain: mp.weixin.qq.com
title: 【JCTC】化学宇宙的“无偏普查”！首次实现“真正随机”的分子采样
author: 
published_at: 
fetched_at: 2026-04-25T02:04:18Z
extractor: wechat_worker
content_hash: e010d2a480ce03649fc17dab56f02501f1b7cb3936d2f04b91daf52150ff6c8c
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajn9Wa0rKXvWvhiaQHybUXJt0VibuvQ3ddfGJ8duc2FQrarhbB0tn5nGag/0.jpg) 

# 【JCTC】化学宇宙的“无偏普查”！首次实现“真正随机”的分子采样

原创 一个小喵咪 一个小喵咪 [ 计算材料视界 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

在计算化学和AI驱动的材料发现领域，我们每天都在利用海量分子数据库（如QM9、ANI-1）训练模型、总结规律。但一个根本性问题始终悬而未决：**我们使用的数据库，真的能代表“化学空间”这个无限集合吗？** 还是说，它们只是人类偏好和软件限制下的“有偏采样”，让我们在认知上陷入“坐井观天”的困境？

传统的分子枚举方法受限于指数爆炸，通常只生成结构“合理”或“易算”的分子，系统性地排除了大量非常规但可能蕴含新奇的化学结构。这种**采样偏差**会悄悄渗透到所有基于这些数据得出的结论中，影响我们对构效关系的理解，甚至可能让我们错过颠覆性的“未知的未知”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajoYXv6kSnOtzhnEpibZOdA4yjaOdH4QJyoiag9WVlLKiatalw5ia7vKt6Og/640.png)

**2025年12月2日，德国卡塞尔大学的Guido Falk von Rudorff团队**在计算化学权威期刊 _**Journal of Chemical Theory and Computation**_ 上发表了题为 **“Representative Random Sampling of Chemical Space”** 的研究论文。该研究**提出了一种名为“代表性随机采样（RRS）”的革命性方法，首次实现了在不对化学空间进行完整枚举的前提下，生成近似均匀分布的随机分子样本，并能够估算任意自定义化学空间中的分子总数**。这相当于为化学宇宙进行了一次**无偏的“人口普查”**。

---

## **一、研究背景：为什么我们需要对化学空间进行无偏采样？**

“化学空间”是指所有稳定化合物构成的无限集合，是分子设计的终极搜索空间。然而在实践中，无论是实验研究还是计算模拟，我们只能接触到这个空间的一个极小的、有偏的子集。这种偏差来源多样：

* **软件限制**：计算软件倾向于处理“行为良好”的分子，排除了许多非常规但稳定的结构，如立方烷、六甲基苯双正离子等。
* **生成工具链偏好**：现有的分子枚举工具（如MOLGEN, surge）为了处理指数爆炸，会引入结构限制，导致生成分子多样性不足。
* **数据库历史沿革**：许多经典数据库（如QM9）源于特定的生成和筛选流程，缺失了许多常见分子（如苯、二氧化碳），更遑论罕见分子。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajR6ZbzJxlWhLoagZLwQsNee2HDKlFVjRfQeBkqQGDtPzNHMgpyN521A/640.jpg)

**这种偏差的后果是严重的**：基于有偏数据总结的规律（如电子效应、哈蒙德假设）可能只是对已观察化学角落的“过拟合”，一旦推广到其他区域就会失效。对于旨在高效、准确、可扩展、可迁移的机器学习模型，**数据的代表性与无偏性直接决定了模型的泛化能力上限**。

因此，开发一种能够对化学空间进行**真正无偏、均匀随机采样**的方法，是评估现有数据库、构建更优训练集、以及从根本上理解化学规律的前提。

---

## **二、研究目的与核心创新点：让“随机”变得“代表”**

本研究旨在**创建一套方法论和工具，使其能够：**

1. **无需枚举**：在不生成化学空间内所有分子列表的前提下，**估算该空间中分子的总数**。
2. **均匀随机采样**：从定义的化学空间中**以近似均匀的概率随机抽取分子**，确保每个分子被抽中的机会均等。
3. **评估数据库代表性**：为评估现有分子数据库（如QM9, ANI-1）相对于其目标化学空间的**代表性和偏差程度**提供量化工具。

**核心创新点：**

1. **“两步走”采样策略**：将“从整个化学空间采样”分解为**先按化学式加权随机选择化学式，再在该化学式内均匀采样分子图**，巧妙地规避了枚举。
2. **基于“小世界网络”的规模估算**：创新性地将**给定化学式对应的所有分子图构成的集合**视为一个小世界网络，利用网络的平均路径长度与网络规模（分子数）的对数关系，通过采样少量分子对来估算总数。
3. **处理“非纯”度序列**：通过组合数学论证，将包含**多种相同价态元素**的复杂化学式的计数问题，简化为其对应的“纯”度序列（所有相同价态原子视为同种）的计数问题，极大降低了计算复杂度。
4. **实用软件包**：提供了开源的Python包 `nablachem.space` 和交互式网站 `random-molecule.org`，使方法论得以广泛应用。

---

## **三、研究过程：如何为化学宇宙“抽签”**

### **第一步：定义化学空间与获取所有化学式**

研究首先允许用户定义一个化学空间，例如：**原子数20-30，最多3个N，至少8个C，至少10个H**。通过高效的整数划分算法，系统可以**列出该空间内所有满足化合价规则的可能化学式**。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iaj8ofvj47VBLWCaUp7LLeDH7tP4raUj8qUYTUFj33QB3ElvHeyBn1zzQ/640.jpg)

**Figure 1：随机采样流程概览及应用**  
左图：（1）基于价态和化学计量限制定义化学空间；（2）通过整数划分获得所有化学式；（3）按度序列（原子价态序列）分组，区分为“纯”度序列（相同价态原子视为一种）和“非纯”度序列；（4）估算每个化学式对应的分子图总数；（5）基于权重进行随机采样。右图：展示了步骤（4）的细节——先尝试精确计数（如使用surge），超出时间预算则使用基于平均路径长度的启发式方法。

### **第二步：估算每个化学式对应的分子图数量（核心突破）**

这是本研究的精髓。对于小分子（约10个原子以内），可以使用surge等工具精确枚举。但对于更大的分子，枚举不可行。

研究团队的巧妙构思是：**将某个化学式对应的所有可能分子图（称为“原分子”）构成的集合想象成一个图（称为“宇宙图”）**，其中每个节点是一个原分子，两个节点相连当且仅当它们对应的分子图之间的**图编辑距离最小**。

他们发现，这个“宇宙图”具有**小世界网络**特性。在小世界网络中，节点间的**平均最短路径长度与网络节点总数的对数成正比。因此，只需** **通过随机采样少量原分子并计算它们之间的平均最小编辑距离，就能反向估算出该化学式对应的原分子总数**。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajqAscLsxSfsSz0I9F3UEsibh8bw5EicKLibTlG7evToh9kfiaGHun9aboAA/640.jpg)

**Figure 2：本工作所利用的相关性的准确性**  
  
### **第三步：执行随机采样**

在获得每个化学式对应的分子数量（作为权重）后，采样分两步：

1. **随机选择化学式**：根据各化学式的权重（分子数多少），随机选择一个化学式。
2. **在该化学式内随机采样分子图**：使用马尔可夫链蒙特卡洛方法，在选定化学式对应的所有连通、无环分子图中进行均匀随机游走采样。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajS3gsQAMZLxKUc2FTFibYaB1d1uYxbK8b3icHkpGpYPfvJU24AJntOicjw/640.jpg)

**Figure 3：联合多个化学式采样的均匀性测试**  
（A）对不同样本量，单个分子被采样频率的排序曲线。灰色区域为完美均匀采样的理论预期范围。（B）各化学式的采样频率按其包含的分子图数量归一化。结果表明，采样是均匀的。

### **第四步：评估现有数据库的代表性**

利用RRS方法，可以生成目标化学空间的**无偏参考分布**（按化学式的频率分布），然后与现有数据库（如QM9、ANI-1、GDB-13）的分布进行比较。使用**Kolmogorov-Smirnov (KS) 统计量**和**Kullback-Leibler (KL) 散度**作为量化指标。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajGAbqE6TfoML9FNVHg7SjfPlJ1DKzRibY8cDjEgBSrlOBtTUSeDDPicYA/640.jpg)

**Figure 4：Kolmogorov-Smirnov (KS) 统计量随采样比例的变化**  
实线：完整化学空间与其随机子集的比较。虚线：从数据库（ANI-1, QM9, GDB-13）采样的子集与完整化学空间的比较。KS值越低，代表数据库分布与化学空间整体分布越接近。

---

## **四、重磅结果：化学数据库的“偏差体检报告”**

1. **成功实现大规模无偏随机采样**：RRS方法能够在原子数高达30+的化学空间中高效生成均匀随机分子样本。计算成本极低，在单核CPU上采样一个分子通常只需**约1秒**，且可轻松并行化。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iaj3CywULgurHyVj4cSYeKscdBynvicTG7tdXBic9s5zibDbI5ZkqVn388eQ/640.jpg)  
**Figure 5：单核CPU上分子生成速度对比**  
比较了RRS（圆圈）与完全枚举工具surge（方块）的速度。对于小分子（如C4系列），枚举更快；但对于稍大的分子（如C14H16），RRS速度超过枚举100倍以上，且随原子数增加优势急剧扩大。
2. **精准估算化学空间规模**：方法能可靠地估算化学空间的分子总数，为宏观认识化学多样性提供了量化工具。
3. **量化现有数据库的偏差**：对三大著名数据库的分析揭示了显著偏差：  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajyh6Ksdua1UlC4Js338tRdN8JhbmAbdevHialLrbYrLjsW2q7f8IT5oQ/640.png)

**Table 3：数据库规模、对应化学空间规模及偏差分数**  
数据清晰地展示了数据库规模与化学空间规模的巨大差距，以及QM9和GDB-13较高的KS和KL值。

   * **QM9**：尽管旨在包含C、H、N、O、F且≤9重原子的分子，但却缺失了**苯、二氧化碳、乙烯**等基础分子。其分布与完整化学空间的KS值高达**0.485**，表明偏差较大。
   * **ANI-1**：偏差相对较小（KS=0.260），但仍不具代表性。
   * **GDB-13**：规模巨大（近10亿分子），但其基于枚举规则引入了强烈的化学偏好，KL散度高达**16.389**，表明分布尾部（稀有化学式）与真实化学空间差异巨大。
1. **确定数据库最小代表性规模**：通过分析KS值随采样比例的变化，研究为每个数据库**估算了一个“最小代表性采样比例”**。例如，要获得与完整QM9数据库相似的分布代表性，可能只需要采样其中一小部分分子。这为设计**更小、更精、计算成本更低的代表性训练集**提供了指导。

---

## **五、深远意义：迈向真正“科学”的化学数据科学**

这项研究的意义远超一种新的采样技术：

* **对机器学习**：为构建**满足独立同分布假设**的训练数据提供了可能。RRS可以持续生成“从未见过”的测试分子，作为**移动靶标基准**，真正测试模型的泛化能力，避免在老旧基准上过拟合。
* **对化学发现**：为探索“未知的未知”打开了大门。通过无偏采样，可以系统性地发现被传统工具忽略的、可能具有独特性质的新型分子骨架。
* **对理论化学**：为验证化学经验规律（如哈蒙德假设、休克尔规则）的普适性提供了 rigorous 的检验平台。可以在无偏采样的分子集合上测试这些规律是否成立，抑或只是局部观察的巧合。
* **对数据库建设**：提供了一把“尺子”，可以度量并改进现有数据库的偏差。未来可以基于RRS构建真正具有代表性的基准数据集。

**当然，RRS也有其局限**：它生成的是**所有可能的分子拓扑**，而非**所有稳定的分子**。将稳定性过滤整合进RRS流程，是未来构建实用、无偏、稳定分子数据库的关键方向。

**论文信息**：  
Monterrubio-Chanca, D. J.; von Rudorff, G. F. Representative Random Sampling of Chemical Space. _J. Chem. Theory Comput._ **2025**, ASAP.  
**DOI:** 10.1021/acs.jctc.5c01523  
**代码与工具**：  
Python包: `nablachem.space`  
交互式网站: `random-molecule.org`

---

**💬 互动话题：**  
如果给你一个按钮，按下去就能随机生成一个自然界可能从未存在过的全新分子结构，你敢按吗？你认为这种无偏探索，是会带来颠覆性的材料/药物发现，还是会在海量“荒谬”结构中迷失方向？欢迎在评论区分享你的看法！

  
预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajicM8NiadIPfeSzL1nFugbgrN0GO1hvZKLJOaBZvsoj55yGAmCZVw4Iiag/0.png) 

 计算材料视界 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajicM8NiadIPfeSzL1nFugbgrN0GO1hvZKLJOaBZvsoj55yGAmCZVw4Iiag/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
