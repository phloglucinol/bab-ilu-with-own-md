---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzI2MjU4MDYwOA%3D%3D&mid=2247491447&idx=1&sn=1dc043d0cb1673a40a707f8036a01890
canonical_url: https://mp.weixin.qq.com/s?__biz=MzI2MjU4MDYwOA%3D%3D&mid=2247491447&idx=1&sn=1dc043d0cb1673a40a707f8036a01890
source_domain: mp.weixin.qq.com
title: KV Cache 量化压缩的 TurboQuant 与 RaBitQ 之争，究竟在争什么
author: 
published_at: 
fetched_at: 2026-04-25T02:03:14Z
extractor: wechat_worker
content_hash: ce2fa39dd73252d6699465c4aabd13408fc5b0379ad1492dfd55f8fbd5175ce9
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/BdwSyGJqvPp787p6ut3xiamadAW9Jh2xwYicCVyRwECKnZkVetX5t0YsiaCooHKdWxanibJyyicMGYpRy0ezOBhiayHpicE1dvQvWHMibHx0wjajM8s/0.jpg) 

# KV Cache 量化压缩的 TurboQuant 与 RaBitQ 之争，究竟在争什么

原创 王庆法 王庆法 [ 清熙 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

本周谷歌推出KV Cache 量化压缩技术TurboQuant【文献1】，引发近千亿美元内存股震荡。

很快 RaBitQ【文献2】作者高健扬公开发声，指出TurboQuant存在多项学术不端，引发业界热议。

争议的第一点，是TurboQuant对RaBitQ技术源头的系统性回避。

高健扬指出，TurboQuant的核心技术，随机旋转加极低比特量化，与RaBitQ早已提出的技术框架高度重合。RaBitQ在SIGMOD 2024上正式发表，完整阐述了随机旋转在向量量化中的作用、理论误差界的证明，以及高效实现。

TurboQuant在论文中虽然引用了RaBitQ，却将其描述为“grid-based PQ”。高健扬认为这是一种带有误导性的简化，因为RaBitQ的核心在于随机旋转，不是基于网格的乘积量化。

而且TurboQuant的第二作者Majid Daliri在2025年1月曾主动联系高健扬，请求协助调试其用Python自行实现的RaBitQ代码。这意味着TurboQuant团队在论文写作之前，知晓RaBitQ的工作，还向原作者请教过技术细节。论文中对RaBitQ的定性偏差显得刻意。

争议的第二点，是TurboQuant对RaBitQ理论结果的错误定性。

TurboQuant论文中将RaBitQ的理论保证描述为次优的，并归咎于较粗糙的分析。

而RaBitQ在扩展版论文中严格证明了其误差界达到了Alon–Klartag【文献3】所给出的渐近最优界。被邀请到理论计算科学的顶级会议FOCS上做过报告。

高健扬也在2025年向TurboQuant团队详细澄清过这一事实，Majid Daliri明确回复称已同步给所有共同作者。但TurboQuant在ICLR审稿、修改、接收，到谷歌大规模宣发的全过程，始终未更正对RaBitQ的这一错误定性。

争议的第三点，是TurboQuant刻意制造不公平实验对比。

计算速度对比部分，TurboQuant用NVIDIA A100 GPU运行自身，而测试RaBitQ时却使用了单核CPU、未开启多线程的Python版本，未用RaBitQ官方提供的高效多线程C++实现。

Majid Daliri本人在2025年曾承认过单核限制，但论文最终呈现给读者的依然是“RaBitQ比TurboQuant慢多个数量级”，且未附任何说明。

面对这些争议，TurboQuant的一作Amir Zandieh承诺会在ICLR会议正式结束后修正定性错误和实验不公两个问题，但明确拒绝“技术相似性”的传承关系。

目前争议的核心是，当一篇拥有巨大影响力、能够左右市场预期的论文存在不规范的引用和误导性描述时，伤害的不仅是原作者的权益，更是整个学术信任基础。

TurboQuant

TurboQuant的核心目标，是解决向量量化领域中一个长期难题：如何将高维向量压缩至极低比特率，同时最小化几何结构的失真；而且压缩算法需独立于向量数据，不能依赖其先验分布。

大语言模型推理中的KV缓存，是最佳应用场景。  

自回归生成过程中，模型需要存储所有历史token的KV键值，内存开销随上下文长度线性膨胀，成为限制推理速度和并发能力的最大障碍。

如果能将KV缓存压缩到极致，同时保持注意力计算的精度，大模型的长上下文推理成本将大幅下降。

TurboQuant的技术路线是随机旋转+两阶段量化。

第一步对输入向量做随机正交变换。无论原始向量的坐标分布如何，经随机旋转后，各个坐标会趋向于独立同分布，而且每个坐标的值以极高概率集中在零附近。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BdwSyGJqvPrr4FQ9yegsic7ibdNCvlbVZRIxEdvDS5xFMBvt5x406dibPWF2iaWrO1nVg8MusQQ9kylYO5E36bMich8wVX0syTqOIaQ0yuvx57n0/640.png)

旋转后做第一阶段量化，对旋转后的每个坐标独立应用均方误差最优的标量量化器。旋转后坐标的分布近似Beta分布，能被解析地知道，因而可精确计算出使均方误差最小的量化区间边界。

但单纯最小化均方误差的量化器会使内积估算产生偏差，严重影响注意力机制中最最重要Query与Key内积的准确性。

因而TurboQuant提出第二阶段量化，对一阶段结果应用QJL变换，每个维度最低仅需1bit表示向量，却能够通过纠偏机制近似原内积估算。这样不仅能大幅压缩KV向量的内存需求，也基本不影响注意力机制中Query与Key和Value之间内积的准确性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BdwSyGJqvPp9OpjkwhDia9dXbfYrTZvDyicS0danbY3lg82gVhkKaicAibkiccmp9iabF65SfBUdRib5Z9w8ngUtlZMq19dWWNhPWWOaiaSQBiaHwgAY/640.png)

TurboQuant给出了任意向量量化器所能达到的最优失真率的信息论下界，并证明其方法与该下界的差距仅为一个常数因子。这意味着TurboQuant在渐进意义下已经非常接近理论上可能达到的极限，进一步压缩比特率可能适得其反。

TurboQuant做了两个核心场景实验验证：

KV缓存量化，3.5比特每通道的压缩率下实现了绝对无损，2.5比特每通道时仅有可忽略的质量损失；最近邻搜索，召回率超越了经典的乘积量化方法，而且将索引时间几乎降为零，无额外计算开销的向量检索。

精妙的随机旋转与纠偏机制，可将高维向量压缩到极限，且几乎不损失其几何结构信息。对大模型推理、向量数据库等影响深远。

RaBitQ  

TurboQuant的前一年，苏黎世联邦理工学院的高健扬团队就发布了RaBitQ论文，随后被SIGMOD 2024接收。

RaBitQ研究动机来自于对现有向量量化方法的反思：尽管乘积量化及变体在近似最近邻搜索中取得成功，但缺乏严格的理论误差保证。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/BdwSyGJqvPrVym396YlT65mkWtZuX5s3VIAsL1YJic9icazS88HUZcy1Aib2R96urPKF98cOxcOsvmIzP18cb9mFtqWKcY5iaL0udcpJOfyzmcU/640.png)

高健扬团队发现，在量化之前对向量施加某种变换，使得量化误差的统计特性变得可控，就有可能同时获得理论保证和实际性能。他们选了随机旋转变换，是，与后来的TurboQuant用的一样。尽管论文定位略有侧重，一个强调理论的完整可证明，一个追求极致压缩。

RaBitQ的技术核心可分为三个层面：

理论上证明了经过随机旋转后，用1bit（即仅保留符号）量化每个坐标，得到的内积估算的均方误差能够达到Alon-Klartag渐近最优下界【文献3】。证明不是简单的引理应用，还包含了完整的误差下界推导，也考虑了常数因子的精细控制；

RaBitQ将1bit量化进一步扩展到2比特、3比特等多比特场景，给出了不同比特率误差下界的闭合表达式，并做了理论到实践的闭环验证；

RaBitQ开源了两种高效的工程实现。一种是基于位运算的极简实现，适用于对速度要求极高、对存储极度敏感的场景；另一种是基于SIMD指令集的向量化实现，能够在现代CPU上以极高的吞吐量完成内积估计。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BdwSyGJqvPpRdicQAGz55jAiamRczRnbUBVUPtZTiatnf4r0eHMIFFa9bogbqvhEuWW3Iph1Z3VvoNM8lDU37CwuqJDzqVyWib7ibGng6ju1TSm8/640.png)

RaBitQ主要面向两个应用场景，近似最近邻搜索，在相同的召回率下，查询速度更快，或在相同的速度下召回率更高；KV缓存压缩，展示了用2比特量化KV缓存时对模型质量的影响甚微。

RaBitQ论文开篇就明确引用Alon-Klartag的理论，坦诚说明自己的工作是“将这一理论首次系统性地应用于向量量化问题”。文中技术选择都有理论依据，实验对比也力求公平。

Alon–Klartag理论

这是RaBitQ和TurboQuant共同的理论根基。源头在Noga Alon和Bo'az Klartag 2017年在顶会FOCS的论文【文献3】。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BdwSyGJqvPpgWCbXebM12y3KkJXT1PBwZxzkskPh97s3JPfsEvRaLAwJ0GYMajRed78Fib9633D70vEteWZoA9BnSVGbe1ibb7XnZZMp6f7EU/640.png)

论文研究的问题是：如果允许用极少的比特来存储高维向量，那么从中恢复内积时，最小可能的误差究竟是多少？

Alon和Klartag的答案分为两个部分：

首先是下界。他们证明了无论采用何种量化方案，只要每个向量使用的比特数被限制在某个范围内，内积估算的均方误差就不可能小于一个与维度相关的量 ，其中d是向量的维度，任何算法都无法突破。

然后是这个下界是否可达。他们证明了存在一种与数据无关的随机线性变换（随机旋转），使得变换后，仅用1bit量化每个坐标，内积估算的误差就能够达到 ，与下界相匹配。

这个答案给出直观判断，在渐近意义下，随机旋转加极低比特量化已经是最优策略，不可能再有本质性的改进。  

Alon和Klartag的理论还揭示了一个深刻的高维几何现象：

在高维空间中，随机旋转具有某种均匀化的效果，能够将任意分布的向量转化为坐标近似独立同分布的形式，从而使得简单的标量量化器能够达到信息论极限。

他们在论文中还探讨了当允许的误差非常小的时候情况如何变化，发现在非常小的误差范围内，Johnson-Lindenstrauss引理可能可以进一步改进，应该是间接影响了TurboQuant对小常数因子的探索。

Alon和Klartag的论文给出存在性理论证明的同时，还提供了构造算法，使得理论结果可以实际计算。RaBitQ和TurboQuant加以应用与拓展。

随机旋转与Beta分布

上文提到的随机旋转与Beta分布是TurboQuant和RaBitQ的技术内核。要理解它们如何帮助实现极低比特量化，需要深入观察一个向量在随机旋转之后，坐标究竟会变成什么样。

![https://images.openai.com/static-rsc-4/ScxsqFnSBfbmkAsD6z0c3XnRfVxUy0c74IqknVn5TSEADTkHdw9jb6QtXaZzQuuY3tJ0SKY7ynO095YCVtpVKQH4aMlS7M55pX_zSd550THPoTsxh1tbHL-lT5ZSTiWrNRJr_qN9qOF97yT5yT6KxaudvhLOzJrvTEPx9Xqxl_S3qmHyF0wekD1t7aDKC9bS?purpose=fullsize](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/BdwSyGJqvPooM0tu0UibjGib6cjjpr2uAlcFf8ZZl1urBrN8LoSpibal9VW7OCfH5MlwsLGQEcZhcKLvcEfsWKsvianmuaEiaHssAvjl08MDNgXQ/640.jpg)

想象一个固定的向量 ，长度为 ，方向在空间中任意。现在，从所有可能的方向中均匀随机地选择一个正交矩阵 ，然后计算旋转后的向量 。 的第一个坐标  服从什么样的分布？

这个问题的答案在高维几何学中早有定论。由于旋转的均匀性，向量 在旋转后的所有方向上是等可能出现的。也就是说， 的分布等同于一个长度为  的向量在单位球面上均匀随机取值。

![https://images.openai.com/static-rsc-4/-iwNJ-TTlywpEAUl9FvLYx779DgmPaYDysXTQaK1dUjlLfTOiceEfKghnEMqLuUSIiXYOKXgH4f6t_TWtJEkQiyeA22SRP3-nEChD5K-PDPQiaV9DSDifBmWCMEmfvKj5nHs8Ow-5CDKhL_FLWCguoEbuOpYvE_A1xDgHiw9P15LISAkNl-hgz5YnS0fT5CD?purpose=fullsize](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/BdwSyGJqvPqDMuWd6EzmnUfqHCD4pxKrndyygXhM05AIkT0Voqvmdu1LyQwibKIy3JENmVHabzC1RNwFy8r4X2Hv9mG9etmY8ypWPZSwibKTo/640.jpg)

因此， 的分布就等同于从单位球面上随机取一个点，其第一个坐标的分布。这个分布可以通过球面积分精确计算出来，结果就是： 服从参数为  和  的Beta分布。

Beta分布  的概率密度函数为 ，定义在区间  上。当  且  时，这个分布会呈现出一种奇特的性质，随着维度  的增加，分布的质量会急剧向0附近集中。

具体来说，当  很大时， 以极高的概率落在  的区间内。这意味着，在高维空间中，旋转后的向量几乎所有坐标都极其接近于0。

这一现象源自高维几何的一个反直觉事实，即高维单位球面上的点，其大部分质量都集中在赤道附近。如果从球心向外看，球面的腰部是如此之宽，以至于随机选一个点，它落在任何给定坐标方向附近的概率都微乎其微。随机旋转正是利用了这种维度诅咒，将原始向量的能量均匀地摊薄到所有坐标上，使得每个坐标都只分得微不足道的一小部分。

这一性质对于极低比特量化来说至关重要。如果原始向量未经旋转，其坐标可能呈现出巨大的动态范围，有的坐标很大，有的坐标很小，有的坐标分布高度偏斜。直接量化时，无法为所有坐标设计统一的量化器，因为不同坐标的统计特性相差悬殊。

但经过随机旋转后，所有坐标变得几乎同分布，且都集中在0附近，这意味着可以为所有坐标使用同一套标量量化器，而且量化误差的统计特性可以精确计算。

在RaBitQ和TurboQuant中，Beta分布不仅用于解释现象，更用于指导量化器的设计。知道旋转后坐标的分布形式，就可以计算出使均方误差最小的量化区间边界。进一步还可以计算出量化误差的期望和方差，从而在最终的内积估算中引入纠偏项，使估算量变得无偏。

随机旋转与Beta分布的结合，蕴含一个深刻的工程原理，RaBitQ和TurboQuant都是这个原理的实践：

在足够高的维度下，通过一个与数据无关的线性变换，可以将任意复杂的原始分布标准化成一个简单的、可控的分布，然后在这个标准化的空间中进行压缩和量化。

此量化非彼量化

TurboQuant和RaBitQ的极低比特量化方法，虽然与常见的模型量化技术同属压缩范畴，但它们在压缩对象、数学原理、应用场景和工程约束上，存在着本质性的差异。

最根本的区别在于压缩对象不同：

传统模型量化压缩的是神经网络的**权重参数，**这些参数在模型训练完成后就固定下来，可以被反复使用。所以权重参数量化是一次性的，通常离线进行，并且可以使用校准数据集来寻找最优的量化参数，例如缩放因子和零点。

而本文TurboQuant和RaBitQ压缩的是**KV缓存**，是推理过程中动态生成的，每一轮对话、每一个新token都会产生新的KV向量，且这些向量在生成之前未知的。这要求压缩算法必须具备数据无关和在线处理的能力。

其次是误差度量的根本差异：

权重参数量化的目标是使量化后的权重矩阵尽可能接近原始权重，通常使用均方误差或输出分布的KL散度作为优化目标。目前的大模型参数量化压缩技术往往以牺牲精度与泛化能力为代价，笔者做过研讨：[爱因斯坦校友提出的Transformer简化方案是条歧路](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI2MjU4MDYwOA==&mid=2247486690&idx=1&sn=e9bf7f77adce26770803b52a6d927601&scene=21#wechat%5Fredirect)，[大模型量化压缩是条歧路](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzI2MjU4MDYwOA==&mid=2247487580&idx=1&sn=a458bd99c1f8b6289752e2ea25a4fd2e&scene=21#wechat%5Fredirect)。

而KV缓存的压缩，可实现内存占用大幅降低的同时，保证注意力计算中Query与Key之间的内积尽可能准确，估算精度可以做到几乎0损失。内积误差与权重误差并不等价，TurboQuant和RaBitQ之所以引入纠偏机制，是为了在内积上做到无偏估计。

硬件适配性方面两者也不一样，INT8量化广泛部署，在于几乎所有现代AI加速器，从CPU到GPU到NPU都原生支持8位整数运算。而随机旋转，需要高效的正交变换实现，常通过Hadamard变换来近似，硬件支持程度远不如INT8成熟。

权重参数量化解决的是模型存储的问题，而KV缓存压缩解决的则是推理时的内存带宽和延迟问题。随着上下文长度从数千扩展到数百万，KV缓存压缩的重要性将越来越凸显。

理解这些区别，有助于避免两个常见误区：一是将TurboQuant与权重量化混为一谈；二是将所有压缩技术视为等价，忽视了场景下的适用差异。

业界质疑  

此外，TurboQuant的激进宣传与实际效果之间存在差距，业界对此也提出了多点质疑。

夸大宣传，摩根士丹利指出，“内存减少6倍”仅针对KV Cache，而非整个模型，不含参数权重，对短文本任务效果有限；

计算换存储，随机旋转变换会引入额外计算开销，可能抵消内存带宽收益，尤其在非主流硬件上；

普适性存疑，基于Beta分布的理论假设在长尾分布的真实数据中能否保持稳定，尚需更多模型架构验证；

极端量化风险，在金融、医疗等严谨场景下，偶发性错误会导致幻觉风险增加，即使是1%的也难以接受。

TurboQuant的技术进步值得肯定，但“6倍节省”的宣传应被理性看待，目前主要作用于长文本推理，而不是全面替代现有内存硬件需求。

  
综上可见，TurboQuant和RaBitQ的核心思想、技术源头、探索路线、应用场景与效果都趋同。特别是双方实际上共享相同的Alon–Klartag理论根基，与随机旋转+极低比特量化的核心技术路线。

不过，笔者整理本文目的不是评判TurboQuant和RaBitQ的学术争议，而是系统学习他们共同的优秀思想：

通过随机旋转将高维向量转化为坐标接近独立同分布且集中于零的Beta分布，从而将任意复杂的原始分布标准化，使得简单的标量量化器能够在逼近信息论极限的条件下实现极低比特压缩。

在随机旋转后的标准化空间中进行两阶段量化，先采用均方误差最优的标量量化，再通过纠偏机制保证极低比特下内积估算的无偏性，从而优先维持注意力机制所需的内积准确性，而不是单纯保留向量本身的几何形状。

  
文献1，TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate，https://arxiv.org/abs/2504.19874

文献2，RaBitQ: Quantizing High-Dimensional Vectors with a Theoretical Error Bound for Approximate Nearest Neighbor Search，https://arxiv.org/abs/2405.12497

文献3，Optimal compression of approximate inner products and

dimension reduction，https://arxiv.org/pdf/1610.00239
  
  
预览时标签不可点

修改于 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zNPOIJqb1FZfYgfH502NvjEkXlGZqTNVctbkHicAA9vqTulPGhYImBYEyp98eCtawogI3Y2WMEEckVSibj0vKtsg/0.png) 

 清熙 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zNPOIJqb1FZfYgfH502NvjEkXlGZqTNVctbkHicAA9vqTulPGhYImBYEyp98eCtawogI3Y2WMEEckVSibj0vKtsg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
