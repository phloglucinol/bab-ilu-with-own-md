---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk5MDg4NzIxMw%3D%3D&mid=2247484477&idx=1&sn=c54e117ba16966cd9abd41b9638aa337
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk5MDg4NzIxMw%3D%3D&mid=2247484477&idx=1&sn=c54e117ba16966cd9abd41b9638aa337
source_domain: mp.weixin.qq.com
title: ProTDyn：颠覆传统！首个统一蛋白质热力学与动力学的AI大模型
author: 
published_at: 
fetched_at: 2026-04-25T02:04:29Z
extractor: wechat_worker
content_hash: 45cc887c3e76cb1e75c648a2b1ad5772408bb1a76289be6b69946be131708e87
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/ukAs1n8gyX3nxZK88Z2BPpfq6JeJAMDPsXCBfwAkiaiciaMYll0A0Q67gxU5nBQ1GGjE8VXLrXzJ0uI1UMxhwLlaA/0.jpg) 

# ProTDyn：颠覆传统！首个统一蛋白质热力学与动力学的AI大模型

原创 科研小猪莹 科研小猪莹 [ 科研小猪莹 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX3nxZK88Z2BPpfq6JeJAMDPicNOzKk3ZQXmd8DYKAujKcE310hHmkBa4B7Xxpx1gK69NjzOGNmCfKA/640.png)

  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/qn7xkhp67dqicwPBJmKpvsdxOdcxEGImojjsDOfM9cHibmGrs7BHNgAWbyF2jErOehd4u9twjt30nRBiatCn371vQ/640?from=appmsg)

01

研究概括

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/3E1egWXOmyzJyO1GDrIB7RJQiabNGAFa6P7dZHNsQLvh2b8yHp7DicJm4ZNnJx0GaqLDI6sZJrfEDpL60wyUwIqw/640.png)

传统的分子动力学（MD）模拟虽然能揭示蛋白质的构象变化和动态行为，但计算成本极高，限制了其广泛应用。来自普渡大学的研究团队提出了**ProTDyn**——首个能够**统一建模蛋白质热力学（平衡构象系综）和动力学（多时间尺度动态轨迹）** 的基础蛋白质语言模型。

这项研究突破了现有方法将热力学和动力学分开处理的局限，通过单一框架实现了：

• 平衡构象系综的独立同分布采样

• 多时间尺度的动态轨迹生成（1ns、10ns、100ns）

• 从粗粒度轨迹恢复细粒度动态路径的"动态修复"能力

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX3nxZK88Z2BPpfq6JeJAMDP4hL4HYUy67vFdl1ygFVmB88Vx391QwQiaPoMcsmDhxsh55EsKdwJSpg/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/uMVz3UCxHqcVqD7ibichasuqzZ9PTSRRJvnSDgI7B6UPbzBxs3lWGkvoPcP5fVNhz7dF2qunkyjk27sXMXSfLXjg/640.png)

02

核心模型：ProTDyn

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/p3cqqEeA04XGlXYFs13I9DiccUic6HBKoYY0ukic4k5v0EORzibvR3LPCma8CbmVuQB4c5vkPmDR0s5EJYxtFKdarw/640.png)

  
ProTDyn建立在ESM3蛋白质语言模型的基础上，采用**Transformer架构**并引入多项创新：

1\. **核心架构特点**：

• 24个Transformer块，14亿参数

 **• 采用Pre-LN而非Post-LN**

 **• 使用旋转位置编码（Rotary Embeddings）替代绝对位置编码**

 **• SwiGLU激活函数替代ReLU**

 **• 双层旋转嵌入机制：分别编码残基位置和时间位置**

**2\. 训练数据规模：**

 **• 54万+个序列-结构对（来自AlphaFold数据库）**

 **• 超过100万构象的大规模MD模拟数据**

 **• 涵盖从纳秒到微秒级的多时间尺度动态信息**

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/hyT894eibLdlcLibPLW65Cd698loyCDPQl1IicwicaBKjDWia8QLVkQ9SnEJl3RuhgqA4ybNsANe54YwC60d7A9lkow/640.png)

03

模型的用处：三大核心能力

![](https://mmecoa.qpic.cn/sz_mmecoa_png/ic4ILwfUyPQFT2jPB3BKuY3CibarXtebibhp1PW9ibRJMGBxcrk9HHMfLcB4fcfy8Q466iacDpMloNuKNCSxFUibavlg/640?from=appmsg)

1\. 热力学生成：平衡构象系综采样

ProTDyn能够生成符合玻尔兹曼分布的平衡构象系综，为蛋白质结构多样性研究提供了高效工具。

2\. 多尺度动力学生成：时空一致的动态轨迹

模型支持1ns、10ns、100ns三种时间分辨率的动态模拟，能够捕捉从局部快速波动到全局慢速转变的全尺度动态行为。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX3nxZK88Z2BPpfq6JeJAMDP0YnATS5yPk1cq5MbWMRv7QjUny9ENUKlb9kIYTupaIKWLfUQVjotwg/640.png)

3\. 动态修复：从粗到细的路径恢复

独特的动态修复能力允许模型将粗粒度时间分辨率（如100ns）的轨迹细化为精细时间分辨率（如10ns）的物理合理动态路径。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX3nxZK88Z2BPpfq6JeJAMDPW3KsQlicMUkBZcX6ZOkzj8XcjxKYiaj4gibMkYUOFZz0bRl2ibvMvNTyYw/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/hyT894eibLdlcLibPLW65Cd698loyCDPQl1IicwicaBKjDWia8QLVkQ9SnEJl3RuhgqA4ybNsANe54YwC60d7A9lkow/640.png)

04

模型的优点与创新

![](https://mmecoa.qpic.cn/sz_mmecoa_png/ic4ILwfUyPQFT2jPB3BKuY3CibarXtebibhp1PW9ibRJMGBxcrk9HHMfLcB4fcfy8Q466iacDpMloNuKNCSxFUibavlg/640?from=appmsg)

1\. 五大技术优势：

• **统一框架**：首次将热力学和动力学建模整合到单一模型中

• **多尺度建模**：支持从纳秒到微秒的多时间尺度动态模拟

• **精确似然计算**：基于离散标记的自回归建模提供精确的似然评估

**• 强大泛化能力**：在训练集外的蛋白质上仍保持优异性能

 **• 计算高效**：相比传统MD模拟，速度提升数个数量级

2\. 性能表现：

 • 在CATH1测试集上，热力学采样模块的Jensen-Shannon散度最低，表现最佳

 • 动态采样模块能够恢复参考MD模拟的自相关函数和马尔可夫状态模型特性

 • 即使对于训练集外的十肽，仍能生成与参考MD高度一致的构象系综

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX3nxZK88Z2BPpfq6JeJAMDPjgn0UJCclbKIibZkRZuTphmSp474vWNNTe6lbIrLUKZABhlFsQTHqrQ/640.png)

  
小 编 观 点

ProTDyn的提出标志着计算生物学领域的一个重要里程碑。这项工作的价值不仅在于技术上的创新，更在于其**开创性的研究范式**：

1\. **革命性意义**：

• 打破传统界限：将热力学与动力学从分离建模走向统一整合，符合物理本质

• 解决核心痛点：针对MD模拟计算成本高的根本问题，提供了AI驱动的解决方案

• **推动范式转变**：从"模拟驱动"转向"学习驱动"，开启蛋白质动态研究新篇章

2\. **应用前景**：

• 药物设计：更准确地预测药物-靶标结合动力学

• 蛋白质工程：指导理性设计具有特定动态特性的蛋白质

• 疾病机制：揭示与构象动态异常相关的疾病分子机制

3\. **挑战与展望**：

虽然ProTDyn表现出色，但仍受训练数据规模和质量的限制。未来随着更多高质量动态数据的积累，以及物理约束（如细致平衡原理）的引入，这类模型有望发展成为真正物理一致的蛋白质动态模拟器。

ProTDyn不仅是一个技术工具，更是通向**数字化蛋白质宇宙**的重要钥匙。它让我们看到，AI正在重新定义我们理解和探索生命分子机制的方式。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4lAAmTGicmg0WqvUAo1R60SvV1wrJ6LSaibmHYufQHntqQU1nZVTWzWvSyPQZbXvy9bUVoHCicKTwVCbgGoib39A1g/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/xrUbVt0eL75B6SbmKeCuTp08jYbYreGlRjurRKroibjc1HvSxnrUcGWmL1XMaCTa8LCiaxHUKHa1cZem1Ih9iaUUg/640.png)

点击下载原文

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/dTxkmqQ6SznicxdpxUKbBLoJzSlpvNfyfeGn8PIB1Wx5kSbhECECnibDwEYfQrkyyjQibSo1zMUX5sJo4KzcibF9GQ/640.gif)

Liu和Zheng-ProTDynafoundationProteinlanguagemodelforThermodynamicsandDynamicsgeneration.pdf

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/Hfh61fSZadiaJKKamCziceVUjOFVGMmmk2qPTykvEQNMHiaibdV5W3jQwhg4icG3yYYuKibcNQia1XLP8Xy9YM83fCkicA/640.gif) 找到我们 

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/4ZCae4yl53klulj6O0b7N5ze7sPltptcv23a1eYD0799Y8awib665MZbVGTgeeAHQH3hFnibibXNL2OzSRmaoic5ww/640.gif)

  
对相关内容感兴趣的读者，可以添加小编微信 keyanzhu333加入学习交流讨论群

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0S6xN1Jic5oIUia1aeicv2cDt74hGltEvZN6ic91wQHDmeI32ZEicuPtxNMT1vLvxekEiaq0Bx1SgOar5A/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/4ZCae4yl53klulj6O0b7N5ze7sPltptcv23a1eYD0799Y8awib665MZbVGTgeeAHQH3hFnibibXNL2OzSRmaoic5ww/640.gif)
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/keqpjicn6JgIItCkxTwmPIA270gM5NPRE8ReZUdXnndR2aJuOpY2VBqjdMoDVTXDbKSxVJ7e2Q42mnlmqTWTo5Q/640.png)

本团队推出下列科研服务，如有需求可添加客服微信：keyanzhu333

① AI生成式互作蛋白靶点筛选与挖掘

  
② AI从头设计高亲和力binder、多肽、抗体、小分子等

  
③ 虚拟筛选与反向钓靶（AI与物理模型）

  
④ 多种组分蛋白、核酸、小分子对接与动力学模拟

  
⑤ 高效能工业酶AI从头设计与定制

  
⑥ 多种基因蛋白组学分析

  
更多服务项目完善中

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0S6xN1Jic5oIUia1aeicv2cDtDYoR4WQicFKdsOEy0yg41QknqUnicTnnPDCoAU2Hhb0yM0s5tn8ia8LPg/640.png)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0K5tG3KpVl4QZEn5BE5WWicAYLShBmlhVLWhHBAuOQFX0YkGHF1s9M4A2I2iapd7wJOB3OQm3rMNyg/0.png) 

 科研小猪莹 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0K5tG3KpVl4QZEn5BE5WWicAYLShBmlhVLWhHBAuOQFX0YkGHF1s9M4A2I2iapd7wJOB3OQm3rMNyg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
