---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzY5NzEzMjkzMQ%3D%3D&mid=2247484415&idx=1&sn=7553058b05d7574398aa78c21b332e72
canonical_url: https://mp.weixin.qq.com/s?__biz=MzY5NzEzMjkzMQ%3D%3D&mid=2247484415&idx=1&sn=7553058b05d7574398aa78c21b332e72
source_domain: mp.weixin.qq.com
title: Chem. Sci. | 静电嵌入机器学习势在酶催化模拟中的应用：兼顾精度与效率的ML/MM新策略
author: 
published_at: 
fetched_at: 2026-04-25T02:03:08Z
extractor: wechat_worker
content_hash: 0b74fc20d6eb342c7dfca12ce08f277bc301625c9293772b3979407895a1e24c
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/yiab2uNgggg1ncfagEMSfrWX1yO8npic2kuVWAbXKAcBicJ68OMjfibcAER4ichibYSqf7sCQXFjKwkptdfh2ibyyv7gZFS5uksxuh5FtOk5HKQHf0/0.jpg) 

# Chem. Sci. | 静电嵌入机器学习势在酶催化模拟中的应用：兼顾精度与效率的ML/MM新策略

原创 AI4Mat前沿 AI4Mat前沿 [ AI4Mat前沿 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg03sdQjGqa1ErLX5I16zo2ib3tbo0iauJvYlmoEpp4xicrFUpSlSfTUjmsLYmFcOMxyuvS6FYicb17WR8VkNlsbnNj6mLpUvHYG1rk/640.png)

## 研究背景与科学问题

酶催化反应的精确模拟对于催化剂设计、共价药物优化和从头酶设计等领域具有重要意义。近年来，人工智能驱动的蛋白质设计取得了革命性进展，已能通过纯计算手段获得具有一定活性的从头设计酶，但通常仅有约5%–10%的设计方案表现出活性，后续仍需大量实验筛选与定向进化。因此，发展能够从结构出发准确预测酶催化活性的高效计算方法，是降低生物催化剂开发成本的关键。

量子力学/分子力学（QM/MM）方法是模拟酶催化的成熟范式，能够提供活化自由能并结合过渡态理论预测反应速率常数。然而，QM/MM面临精度与采样的双重瓶颈：高精度QM方法计算代价极为昂贵，而充分的构象采样同样不可或缺，二者的同时满足使模拟成本居高不下。

机器学习势（MLPs）的出现为这一矛盾提供了新的解决思路——以接近训练所用量子化学方法的精度，实现数量级的计算加速。然而，将MLPs应用于酶催化的ML/MM模拟时，如何正确描述ML区域（反应核心）对MM环境（酶和溶剂）的电子响应，是一个核心挑战。本文提出并验证了一种基于静电机器学习嵌入（EMLE）的ML/MM策略，仅用气相数据训练MLP，同时通过EMLE模型捕捉环境的静电效应，在两个代表性酶体系中实现了对酶催化效应的准确预测。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg3fOqCjzuqnv36TxYhCSpuia2gnXn3Nnoaz4IbLibvgPnJlHDSxSGBU7s0OwrZF4TvAAs7VoW6MwnGeib2uRjUsic8hF0IicNzybBw0/640.png)

▲ Fig.1 | 本研究中考察的反应及酶–底物结合构象。(A) 由AbyU催化的Diels–Alder反应（O-甲基化类似物的

## 方法框架：EMLE嵌入方案

本研究采用的EMLE方案将ML/MM体系的总能量分解为四个分项：气相能量、静态相互作用能、诱导能和MM能量。气相能量由仅在气相数据上训练的MLP提供，不依赖于特定的MM环境；静态相互作用能描述未扰动ML区域与MM点电荷之间的库仑作用；诱导能则捕捉ML区域电子密度在MM电场作用下的极化响应及其能量代价；MM能量涵盖了ML与MM子系统之间的范德华和短程排斥相互作用。

这一分解策略的核心优势在于：第一，允许使用仅在气相参考数据上训练的MLP，大幅降低训练数据生成成本；第二，MM环境仅以点电荷和坐标表示，使EMLE可作为现有QM/MM程序中QM后端的即插即用替代；第三，气相、静态和诱导三个分量的分离便于独立监控各组分的训练精度。更重要的是，由于MLP与EMLE模型解耦，同一MLP可在不同环境（溶液、酶突变体）下复用，仅需调整EMLE模型即可适配新场景。

## 体系一：AbyU Diels-Alderase

AbyU是一种天然的螺四环烯酸环化酶，催化Diels-Alder \[4+2\]环加成反应。本文选取该体系的两种不同酶-底物构象（Pose 1和Pose 2）进行研究，以检验EMLE方案能否区分不同结合模式下的催化差异。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg1icgvibpcoEEugRxnK6zU5qlSl6nM2hMZj7JySoqU8ZrVVLJhM9LHwhKXdsQclrgKZ5NhNmCHjc72bicV9boB2QaVNlnd1TL5om8/640.png)

▲ Fig.2

研究采用MACE架构训练气相MLP，参考数据由ωB97X-D/6-31G\*水平的气相计算生成。自由能计算通过伞型采样结合加权直方图分析方法（WHAM）完成。结果表明，当采用简单的机械嵌入（即对ML原子赋予固定的气相点电荷）时，两种构象的催化差异无法被正确捕捉。而采用EMLE静电嵌入后，ML/MM模拟能够准确再现DFT/MM参考计算给出的两种构象之间的活化自由能差异和反应能差异。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg0FYpbsEAT1RvaDTe4uGTCDeMLD8P1PlhLZhTiakI6TTZDcL8UNeCib7TpTvZkAhxTpxhfKicgxR7HZ1dVIjgicKSAfVapWD53ElYE/640.png)

▲ Fig.3 | AbyU Diels–Alder反应在两种不同AbyU–底物结合构象下自由能垒及反应能的差异。

图3清晰展示了这一关键结论：EMLE嵌入下两种构象的自由能垒差异和反应能差异与DFT/MM参考值高度一致，而机械嵌入则严重偏离。这说明酶环境对底物电子分布的影响——即电子极化效应——是正确预测不同构象催化活性的必要条件，而EMLE方案成功地捕捉了这一效应。

## 体系二：分支酸变位酶催化的Claisen重排

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg0y785IasjaDS5u5YicRAefv7w4FY4emQTiaPXhZGiaoMMiaa6dEzSW59TjP009Dt6FxPrTxibZM4BCYVHZToRYVVgicv8IkNGvLR0z8/640.png)

▲ Fig.4

分支酸变位酶（ChoM）催化分支酸（chorismate）经Claisen重排转化为预苯酸（prephenate），是酶催化研究中的经典体系。该反应的过渡态具有高度极化和带电特征，对嵌入模型的电子响应描述能力提出了更高要求。

本文为该体系训练了专用的反应特异性EMLE模型，参考数据来自M06-2X/6-31+G\*\*水平的QM/MM计算。气相MLP采用PhysNet架构训练。自由能曲线通过伞型采样获得。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg1Zu5A0PDzUzc6Frzrj9px4YyKfTS3PmneZQouot758VSYaJNp2R0mLNOrS4ibwkngARmY9ZIkO0Jo46XyicWFbvN4k7KMEyK3wA/640.png)

▲ Table 1 | 水溶液中分支酸转化为预苯酸的活化自由能（D‡G）、反应能（DG）及催化效应（DD‡G）

表1汇总了ChoM催化反应在水溶液和酶环境中的活化自由能、反应能和催化效应。结果显示，采用通用EMLE模型时，酶催化效应（即酶中与水中活化自由能之差）已接近DFT/MM参考值，而采用反应特异性训练的EMLE模型后，催化效应的预测精度进一步提升，与DFT/MM参考值的偏差降至约1 kcal/mol以内。相比之下，机械嵌入方案在该体系中的表现明显不足，无法正确捕捉高度极化过渡态的环境稳定化效应。

更令人瞩目的是，本文将为ChoM训练的ML/MM模型直接应用于结构家族完全不同的天然异构酶（BsCM）的野生型和突变体，成功再现了突变导致的活化自由能变化，展现了EMLE方案的跨体系迁移能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/yiab2uNgggg1LkznibjfUgAmCiaOQyX2ibeXVd8jcwYM9DAIxV46UQvf80vtXHquiakucjoxnibnrsbBUaI7ibuf4b015Y3miahibrhticeFD3QITyn8I/640.png)

▲ Fig.5

## 总结与展望

本研究系统验证了EMLE静电嵌入方案在酶催化模拟中的有效性。核心创新在于：仅需在气相参考数据上训练MLP，通过物理驱动的EMLE模型处理环境静电效应，即可在ML/MM框架下实现与高精度DFT/MM可比的酶催化效应预测。在AbyU和ChoM两个具有不同挑战特征的酶体系中，EMLE方案均显著优于机械嵌入策略，准确区分了不同构象和不同环境下的催化活性差异。

该方法的主要优势包括：训练数据仅需气相计算，数据生成成本低；MLP与环境解耦，同一MLP可复用于不同酶突变体和溶剂环境；计算效率远高于传统QM/MM方法，适合大规模酶活性筛选。当然，对于电子极化效应特别显著的体系，训练反应特异性EMLE模型可进一步提升精度。

展望未来，该策略有望与蛋白质设计流程深度集成，为从头酶设计中的活性预测和突变筛选提供高效可靠的计算工具，从而减少对实验高通量筛选的依赖，加速功能性生物催化剂的开发进程。

---

****参考文献：Valentin Gradisteanu, Kirill Zinovjev _et al._ Simulating enzyme catalysis with electrostatically embedded machine learning potentials. _Chem. Sci._, 2026, Advance Article https://doi.org/10.1039/D6SC01156J**

****本文由AI4Mat前沿编译分享，旨在学术交流。文中所有图文版权归原作者及出版社所有。**

****关注我们,获取更多AI+材料前沿进展**

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3dePnhYnbJVMpcphQbicTIgcMjbKb36Q3LE6C5V3e39ZjDgMYD0wZTgTCu3xHZuUKnZt8icHsWtpqrkWRI5SdIYXH3icaAtV8IyY/0.png) 

 AI4Mat前沿 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yiab2uNgggg3dePnhYnbJVMpcphQbicTIgcMjbKb36Q3LE6C5V3e39ZjDgMYD0wZTgTCu3xHZuUKnZt8icHsWtpqrkWRI5SdIYXH3icaAtV8IyY/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
