---
type: raw_article
source_url: https://mp.weixin.qq.com/s/-Wd7HKpzi7gEqo9E5jGKVg
canonical_url: https://mp.weixin.qq.com/s/-Wd7HKpzi7gEqo9E5jGKVg
source_domain: mp.weixin.qq.com
title: 哈佛大学 Marinka Zitnik 团队：Atomica — 分子间相互作用的通用原子表征模型
author: 
published_at: 
fetched_at: 2026-04-25T02:04:03Z
extractor: wechat_worker
content_hash: 9dc064c475e5be11e537bb89bf0fb045967207f8763c76267fc8857a9aab9b27
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkynawMZ0OVaiauaCMquPfkQubnIpGKjic9KNTicQMxbo3qB9Qz63KSbkrRahupicPzABgsiazibdbA4ZaY8Q/0.jpg) 

# 哈佛大学 Marinka Zitnik 团队：Atomica — 分子间相互作用的通用原子表征模型

原创 Ada Fang Ada Fang [ 植物大模型 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

主讲人简介：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/jBwd4N7VkynawMZ0OVaiauaCMquPfkQubOM1GYOOCvIHZzzVic7hhIqXS9QPBzwfmdadJsmJvt9p2eSbpL5jgAcw/640.png)

Marinka Zitnik 是哈佛大学生物医学信息学系副教授，同时任职于坎普纳自然与人工智能研究所、Broad研究所及哈佛数据科学计划。她致力于人工智能基础研究，以推动科学发现和个体化医疗。博士毕业于卢布尔雅那大学，曾在斯坦福大学从事博士后研究。荣获多项国际奖项，包括NSF CAREER奖、Kavli Fellow等，并共同创立了Therapeutics Data Commons，担任AI4Science倡议的教员负责人。

  
本讲座主讲人，Ada Fang，是 Marinka Zitnik 课题组博士研究生。研究方向聚焦于**化学与机器学习的交叉领域**，致力于开发几何深度学习与等变图神经网络模型，以理解和探索超大规模药物样分子空间中的复杂化学生物学关系。

  
PPT（中文讲座记录见文末）：

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzwxhaKiaf7VibVnXgEad8YB5DiandiaX8Vda1w4bdGQ40UU9jtMicuyEepmg/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzXGCI4EUdlUsuoLQlRhZY4gL4dWVfdka4wuSHFAKQibiaoyib8VqiaSQgIQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzLrlJcBIvSDjMhbe6GHYq8Aic03j9mSSib3PrDXq2BmbPuLhicGRDIBNhQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzaGr7XRrkKpENF2BKdzu7BNwbz9lrcU7WhOVZDgab19hRM7hnTZYUTQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzib1YnicFd5spHqKOqhuDvehXmNO3R2E7N2eeAvLhqTibQ6K1txRGnjHjw/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzQfDACztq9FkIxd4kcCia2MN4bicQNXGbypAUMQnByargxYgVStDMM58Q/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzyQA26EQHsicFpwfLDRPtmPqCTNwmdFqZzFo0VH91ZbCF6BBaiczF0wMQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzgdAMsjO8xgNtmcksTX4WGdBFmDcsq4WYAUTX9WRdId2aUvlAzLKZuA/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzjoXtYomOaAuUroJjGrlC5zudDAiciaysNuXKvM28ibqWqXGQ1UicLqxsAg/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzTJKEKUmWty2kNvSwZxhjIsEmHtbnt2yViaWabJtHkPdaS8OicTeC9EcQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzp4kqBavFHl6doLkOvRPJZlvsOIbNWxGqo73vVB0T2bfycI4oV7Kia4g/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzxB5xkrlchYnzqKELrRyKLyp9VicIicHJov2tIc4Y4ndtLHKK98BqweBQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUz4S5SLhV7aNZT52PGq3UwI1ocXgITBnDkRAZibgEgpiaTQ9CbHOgL1LXQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzT5XwgvyGdPh5tdoY9yfDoC4bE4nuD4IaEicpFhzz6tj6o3MaUkiaXeZQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzO4TBhdeObNomb9s48rJj9hWLCYRiaDR5V6vWXnsmhTI9ccbFs9yjJUA/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzcHRawNvF1eoyhXfdbBOXJ0bbQ1iah98khYKcKziaIzKtAZeM5jqGqYkg/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzgCbVic4uCfgjgokqUDj6ZboyDEzoKlMYvkLrbsVJL6RxPPQroQrNstw/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzuQg1Bx19e9Jbk3kdZ6ib0icW8kv6GibOXeq20Nc6DQNMxusgVgqA9fzbA/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUz0OJsdZchk5q0qs8pqYtjd8zE2WeSb9ic64yDLAZia9PTwmzpPf0s3lwg/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzic4ZjdTNJ9LuDick7obTkPs4kPnvMsHc3pf38dCaH9bvxkZLdvicSRZFg/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzhejdUxpFPvjbvJoqRib0oCG7VPpKucLvaqsxrc0jlxuwuVponyQ86og/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzicibicDo9gtppAW6rLhauDKFEatCfHWw84qBGssrq8ztLD8GIGXcKre2Q/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUz6ibyp95Hp8CP2RO57icX8FgmO383FOiaj6zWoKicjplRqMZU29FPb1ayPw/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzaxxYn2UUY4KKsxBulibzZ8iazW1Povtv0EMgA95yUytQQXMWpYteG3Ng/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUziap4UjZicajAWcNQ2hH9uYYGe8vvEE6uAMLa3IH8RWj5Bjydib7xaiadew/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUznHhwkHdPhxIj1Fe7QicxDic19zAhcDPiawRduw1kxRZNgR5bII9Aqg6Ug/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzr2EJibgmLD58Nu3WpVcryAY5J8udEKMibtDDLmZ7oeRkm44PGwISqeYg/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzcakrCB0xkjRkJrrIIacYJRTGAJcp9OJbrnbWCOozhthL31S7mic0NDA/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzP0hiauVWQR5JQiaIpsyNUdSnJ4LYEM0qtxPB4aEUNSjBQ4aAlIvFVdibg/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzUBbMX8PK7spm3PHZhQ3XlKU30MSibKJ6pmoZIZUyENVIqFbAxRBFYLA/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzTyhKZQib9qQibibiaycBRgANLmgQgbSKibcDortufS8TnmPEhrVAVKZFL9A/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUz6V1hXCUJichTEHiaHOMXACGNtZVd39z0U5cuibanCgKaIgXzd8CySiaLnw/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzzlapficjqc7Y1iaXtAG5fMqvv6gbox12FIPU1M9evLkJ1Obcb6Fqf5zQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzzuwMibu5CjX7DHqsPDia1xbNjFvEzsSRESBZBuKDe0CmOTWCsRLvypVg/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzaCiaMnDJibYnf3LJrzy2SVVdkkRlA2YlNI0dhE3tEILhrXfqCpMnn8pQ/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUzTGY85WN0b7f4icE5tUBGhic1JoV9St0WXsb2xyfu68gJjZqic5EZsfSPw/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/jBwd4N7VkylGicTAuvbM5RCc36NIq2pUz1IK94tlwamhQiaI4YzdFGiaFhVY9ZWdLP9oqB4UhQyFsZHXsMrMLy4BQ/640.jpg)
  
  
中文讲座记录：

  
**研究背景**：当前AI化学/生物学领域的“基础模型”（如小分子模型、蛋白质模型）主要学习**孤立分子**的表征，而**分子通过相互作用实现功能**。现有方法（如简单拼接两个分子嵌入）无法捕捉驱动相互作用的关键**原子级化学环境**（氢键、π-π堆积、静电作用等）。

**核心目标**：开发一个**通用的、原子级的**模型，能够学习**任意两种分子间相互作用**的统一表征，涵盖蛋白质、核酸、小分子、离子、脂质等多种模态。

---

### **一、 Atomica 模型设计**

1. **输入与图构建**：
   * 仅关注**相互作用界面**的原子，以降低计算复杂度。
   * 构建一个**异质图**，节点是原子，边分为**分子内边**（同一分子内原子连接）和**分子间边**（不同分子间原子连接，基于空间距离阈值定义）。
   * 引入**“模块”层级**：将原子分组为更高级的化学单元（如氨基酸、核苷酸、常见化学基团）。这形成了一种分层图结构，被证明比纯原子图更具表达力，且能捕捉高阶结构信息。
2. **架构与训练**：
   * **去噪**：对其中一个分子的扭转角和平动/旋转添加噪声，让模型学习去噪，从而理解维持相互作用的关键几何约束（键长、键角）。
   * **掩码预测**：随机掩码“模块”的身份，让模型预测被掩码的类型，学习上下文信息。
   * 使用**等变图神经网络**（基于Tensor Field Networks），确保模型能感知并保持三维几何结构。
   * **自监督预训练任务**：
3. **预训练数据**：
   * **蛋白质数据库**：不仅提取蛋白质，还提取与其共结晶的**配体、肽、核酸、离子**等，构建蛋白质-“X”的相互作用对。
   * **剑桥结构数据库**：包含大量小分子-小分子相互作用的晶体结构，数据量更大。
   * 处理时，对大分子（蛋白、核酸）进行裁剪，只保留界面附近残基。

---

### **二、 表征空间分析：Atomica 学到了什么？**

1. **跨模态组织**：将不同分子相互作用对的嵌入投射到二维空间，发现**相互作用模式相似的模态在嵌入空间中彼此靠近**（如蛋白-肽相互作用靠近蛋白-蛋白相互作用）。
2. **化学感知**：
   * **原子嵌入**：按元素类型平均原子嵌入，发现其在隐空间中按**周期表位置**聚类（如卤素聚集在一起）。
   * **氨基酸/核苷酸嵌入**：按其化学性质（芳香族、带负电、带正电）自然聚类。
3. **语义组合性**：受NLP中“国王-男人+女人≈女王”的启发，研究团队在相互作用空间中也发现了类似的规律。例如，通过嵌入运算，可以将“蛋白A-辅因子NAD”的相互作用关系，转移到“蛋白B”上，从而近似得到“蛋白B-NAD”的嵌入。这表明模型学习了可转移的、与结合口袋功能相关的**高阶语义**。
4. **识别关键界面残基**：通过“掩码扰动”分析（掩码一个残基看整个相互作用嵌入的变化程度），Atomica能够**优先识别出那些实际参与分子间键合**的氨基酸，其表现优于仅依赖序列的模型。
5. **通用性价值**：通过“消融实验”证明，**跨所有分子模态的联合训练**显著提升了在**数据稀缺的相互作用类型**上的表征质量。这证明了通用训练的“知识迁移”优势，即从数据丰富的模态（如小分子-小分子）中学到的化学原理，帮助了数据匮乏的模态（如蛋白-DNA、蛋白-RNA）的表征学习。

---

### **三、 应用案例**

1. **疾病蛋白与分子相互作用网络**：
   * 在Atomica Nets中，**共享同一疾病的蛋白也更倾向于拥有相似的相互作用界面嵌入**。
   * 不同疾病在不同模态的网络中呈现出独特的、互补的“通路”模式。例如，自身免疫性离子通道病在“脂质”和“离子”网络中高度连接；淋巴瘤的不同靶点被不同模态的网络优先提名。
   * 这为疾病机制研究和**靶点提名**提供了超越传统PPI网络的、多模态互补的新视角。
   * **背景**：网络生物学中，已知疾病相关蛋白在蛋白质-蛋白质相互作用网络中倾向于彼此连接（“连带责任”原则）。
   * **新视角**：研究团队利用Atomica，从**五种不同分子模态**视角构建了新的网络：“Atomica Nets”。网络中的节点是蛋白质，如果两个蛋白质在特定模态下的**相互作用界面嵌入相似**，则它们之间形成连接。
   * **发现**：
2. **暗蛋白质组的功能注释**：
   * **挑战**：大量蛋白质（“暗蛋白质组”）缺乏功能注释，且结构未知。
   * **方法**：结合Pesto模型预测的暗蛋白结合位点，使用Atomica来**预测哪些配体/离子最可能结合到该口袋**。
   * **湿实验验证**：以“血红素”结合为例，Atomica从暗蛋白质中预测了9个潜在的血红素结合蛋白。实验合成和验证表明，其中**5个成功结合血红素**，成功率可观。这证明了Atomica在从**计算预测到实验验证**的闭环中，具有强大的功能发现潜力。

---

### **四、 总结与展望**

* Atomica是一个**面向相互作用的、原子级的、通用的分子表示学习模型**。
* 它成功捕捉了跨模态的化学和生物学相互作用规律，并在**疾病网络分析**和**暗蛋白质功能注释**两个重要生物学问题上展示了应用价值。
* **局限性**：模型依赖于**结构信息**，对于固有无序区域等难以获得准确结构的相互作用，其应用受限。
* **未来方向**：探索如何结合非结构化的相互作用信息，并针对特定下游任务进行高效微调。

  
欢迎关注“植物大模型”公众号

添加小编微信获取资料！进群交流！

  
**_往期课程：_**

[MIT公开课 | 计算生物学中的机器学习 - MLCB24 - 全部课程链接](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4OTg5MjE5Nw==&mid=2247486227&idx=1&sn=7256f37de9fdf05e0ed19c7c66ef97a8&scene=21#wechat%5Fredirect)  

[MIT公开课 | 基础模型与生成式AI - 6.S087 - 全部课程链接](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4OTg5MjE5Nw==&mid=2247486328&idx=2&sn=480c786c068c90968c368378b965d3c6&scene=21#wechat%5Fredirect)  

[MIT公开课 | How To AI (Almost) Anything - MAS.S60 - 全部课程链接](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4OTg5MjE5Nw==&mid=2247488493&idx=1&sn=31b5b4e0927cc4ca4de149ff9a658470&scene=21#wechat%5Fredirect)  

  
_**往期内容：**_

[德国马普所 Detlef Weigel 院士：上位性，生命进化中的调味剂——以植物免疫系统为例](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4OTg5MjE5Nw==&mid=2247488462&idx=1&sn=4e18619dee73b73cb30ca9e4bd5edaec&scene=21#wechat%5Fredirect)

[康奈尔大学 Edward Buckler 院士：植物育种目标亟待根本性转变——健康饮食、循环农业、碳封存](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4OTg5MjE5Nw==&mid=2247488327&idx=1&sn=3cab793d9dd577ffa6265febbf5fd38a&scene=21#wechat%5Fredirect)  

[苏黎世大学 Cyril Zipfel：植物受体激酶介导的免疫信号转导](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4OTg5MjE5Nw==&mid=2247488727&idx=1&sn=53ca2d7957595580b1765416d1f108fe&scene=21#wechat%5Fredirect)

[斯坦福大学 ( Evo2 通讯作者) Brain Hie：利用 Evo2 对全域生物进行建](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4OTg5MjE5Nw==&mid=2247488549&idx=1&sn=31038bd1948915efa7feceef3341a67a&scene=21#wechat%5Fredirect)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/jBwd4N7VkymhYr0WbuBmiaBFzibhcCxIZJysSveibM7yvhknTBaNtvYAHCneicVhyPUcjwm7ErvGvUYzXf6F3P9Ipg/0.png) 

 植物大模型 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/jBwd4N7VkymhYr0WbuBmiaBFzibhcCxIZJysSveibM7yvhknTBaNtvYAHCneicVhyPUcjwm7ErvGvUYzXf6F3P9Ipg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
