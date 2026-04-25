---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489186&idx=1&sn=e530a768fd79e35ce0c8f25e55a8d700
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489186&idx=1&sn=e530a768fd79e35ce0c8f25e55a8d700
source_domain: mp.weixin.qq.com
title: 【佳作推荐】哥伦比亚大学Ben-Johny团队Cell论文：计算设计“ELIXIR”多肽精准逆转钠通道功能异常，开辟全新治疗路径
author: 
published_at: 
fetched_at: 2026-04-25T02:04:06Z
extractor: wechat_worker
content_hash: 22acf0e1d029d877283115fcf8e616691075880c08789cc9d5d59e7f04f490bd
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EfcmZkehEMKj5icrOmJN2VcguzPjCmjeeNLnqDKa0txG6Fn7xB6a7BIR6yrQoEhZ31Jon3bBNamXcA/0.jpg) 

# 【佳作推荐】哥伦比亚大学Ben-Johny团队Cell论文：计算设计“ELIXIR”多肽精准逆转钠通道功能异常，开辟全新治疗路径

原创 ComputArt ComputArt [ ComputArt计算有乐趣 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfcmZkehEMKj5icrOmJN2Vcg5FuDqfw0hLfAUxraBhcfPyQSNbPAhYPYeT5qrVSP3KnHib2LQuN13sQ/640.png)

在生命体的电信号网络中，离子通道犹如自然界精密的晶体管，其中电压门控钠通道负责动作电位的起始与传播。其功能失调往往表现为晚钠电流的异常增强，这是连接长QT综合征、心力衰竭、癫痫、肌强直等多种疾病的共同病理纽带。传统小分子药物常因靶向性不足、影响正常通道功能或存在脱靶效应而受限。哥伦比亚大学Manu Ben-Johny团队针对这一问题，成功利用计算蛋白质从头设计技术，开发出一种名为ELIXIR的合成肽调节剂，能够高选择性、高效地逆转电压门控钠通道的功能异常，并在实验模型中显著改善与心脏钠通道和神经元钠通道病变相关的心律失常与癫痫表型。这一成果不仅为相关疾病的治疗提供了全新的分子工具，更展示了理性设计生命系统调控元件的强大能力，为离子通道疾病的精准干预开辟了全新的路径。近日，该项研究工作发表于著名的《Cell》期刊【1】。

研究团队首先从钠通道失活的分子机制出发，提出了一个基于结构生物学的理性设计策略：钠通道快速失活的关键在于其失活门从羧基末端结构域的酸性EF-hand样区域释放；在多种心脏与神经疾病中，这一释放过程受阻，导致通道持续开放、晚钠电流增强。基于这一机制，团队设想设计一个新肽段，以高亲合力竞争性结合于该EF-hand样区域，“置换”出滞留的失活门，促进其与孔道近端位点结合，从而恢复快速失活、抑制病理电流（图1）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfcmZkehEMKj5icrOmJN2VcgQl9FtmTBF7HiaXcEBECVnkUWKibxobDtRoKREjyOwtcJRQKvStEJeYhg/640.png)

**图1：ELIXIR的设计思路。**

为实现这一设想，团队采用了计算蛋白质从头设计方法。他们以人源心脏钠通道Naᵥ1.5羧基末端结构域的高分辨率晶体结构为模板，基于开源平台ColabDesign中的AfDesign算法。该设计流程不依赖任何已知结合片段，而是让神经网络在三维结构约束下从头生成可能结合目标口袋的氨基酸序列。经过多轮迭代优化——序列采样、结构预测、结合能评估与构象聚类——算法最终筛选出一个仅由21个氨基酸组成的候选肽。该肽与天然钠通道失活门序列相似度极低。研究团队将其命名为ELIXIR（Engineered Late-current Inhibitor X by Inactivation-gate Release），即“通过释放失活门来抑制晚钠电流”（图2）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfcmZkehEMKj5icrOmJN2Vcgf9XZUWib2XqhKjJ4Cwrce4x2ejwev6jCl8t61OicdrA3ujJGAM322ZNw/640.png)

**图2：从头设计、筛选得到ELIXIR。**

初步的结构建模显示，ELIXIR呈现为两亲性α螺旋，其疏水面与目标口袋的疏水裂缝高度互补，而带正电残基则与周围的酸性环境形成静电相互作用，整体结合模式与设计预期高度一致。随后，体外荧光各向异性结合实验证实，ELIXIR能以亚微摩尔级亲合性与Naᵥ1.5羧基末端结构域特异性结合，验证了计算设计的准确性（图3）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfcmZkehEMKj5icrOmJN2Vcgib5P77cZIjREEh63W7ZgznSXM2QVOpcVRw3OkVEsfUhZFyver5pr81Q/640.png)

**图3：ELIXIR的结构建模和亲合性测试。**

在活细胞内，荧光能量共振转移实验同样证明了二者的直接相互作用。更为关键的是，功能研究表明ELIXIR展现出高效的选择性和广谱性：它能够强力抑制由不同机制，如多种致病突变、心力衰竭相关的磷酸化修饰等，引起的心脏钠通道晚钠电流升高，却对野生型通道的正常激活、失活动力学几乎没有影响（图4）。其选择性在针对其他钠通道亚型（与癫痫相关的Naᵥ1.6、与肌强直相关的Naᵥ1.4等）的实验中进一步印证——ELIXIR能有效、专一地纠正突变通道的功能缺陷。这表明其作用机制并非简单阻断，而是精准地修复失活过程的病理环节。

**图4：ELIXIR对病理性迟发钠电流的选择性抑制。野生型通道的电流几乎不受ELIXIR影响；携带致病突变的通道表现出巨大的迟发电流，被ELIXIR显著抑制。**

研究的多层次模型验证将发现从分子、细胞水平推向了整体生理与病理意义。在模拟癫痫的转基因小鼠脑中表达ELIXIR，能够显著改善突变神经元的异常电活动，缓解其过早出现的去极化阻滞，从而在细胞层面逆转致病的兴奋性失衡。在心力衰竭模型小鼠的心肌细胞中，通过细胞穿透肽形式递送的ELIXIR，不仅能降低病理性晚钠电流，还能纠正动作电位时程延长及其不稳定性，这两者正是心力衰竭时心律失常风险增加的关键电生理基础。尤为重要的是，在长QT综合征患者来源的诱导多能干细胞分化的心肌细胞中，以及在整体转基因小鼠模型上，通过病毒载体实现ELIXIR的长期表达，均能有效降低晚钠电流，并在后者身上直接观察到延长的QT间期被显著缩短，实现了对疾病核心表型的在体逆转（图5）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/IBYsyRibb4EfcmZkehEMKj5icrOmJN2VcgTK5ynHYkOic6c8ejCZUI1OAa3LZsFFwQDAz64XVOGZjC7Rf8fPxicagQ/640.png)

**图5：通过AAV9病毒递送的ELIXIR基因在病变的心肌细胞和小鼠体内持续表达，可以特异性抑制病理性晚钠电流。**

**小编总结**  

该项工作成功地将前沿的计算蛋白质设计技术应用于跨膜离子通道这一复杂靶点，完成了从计算机模拟、体外验证到细胞和活体功能确认的全链条研究。ELIXIR的作用机制独辟蹊径，它并非直接堵塞通道孔道或干扰电压感知，而是通过增强内源性的失活调控通路来发挥作用，具备了高度的病理状态选择性。同时，鉴于钠通道家族结构的保守性，ELIXIR所展现的跨亚型治疗潜力，为由钠通道功能获得性突变引起的疾病带来广谱的治疗希望。当然，将这一突破推向临床仍面临挑战，特别是如何实现治疗性肽分子的高效、安全体内递送。未来仍需要开发更优化的递送系统，或以其作用界面为靶标筛选非肽类小分子化合物。

**参考文献**

\[1\] Ryan Mahling, Bence Hegyi, Erin R Cullen, Timothy M Cho, Aaron R Rodriques, Lucile Fossier, Marc Yehya, Lin Yang, Bi-Xing Chen, Alexander N Katchman, Nourdine Chakouri, Ruiping Ji, Elaine Y Wan, Jared Kushner, Steven O Marx, Sergey Ovchinnikov, Christopher D Makinson, Donald M Bers, Manu Ben-Johny\*. De novo design of a peptide modulator to reverse sodium channel dysfunction linked to cardiac arrhythmias and epilepsy. Cell. 2025;188(22):6170-6185.e19\. doi:10.1016/j.cell.2025.07.038.

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IBYsyRibb4EcibThuywhbNciciaiauxu6DUhtp75nQZnrPxniaYia0RMN9XgXMVCiaqEOxkU4EjMoIsmD98kDTcLz5NC3w/0.png) 

 ComputArt计算有乐趣 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IBYsyRibb4EcibThuywhbNciciaiauxu6DUhtp75nQZnrPxniaYia0RMN9XgXMVCiaqEOxkU4EjMoIsmD98kDTcLz5NC3w/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
