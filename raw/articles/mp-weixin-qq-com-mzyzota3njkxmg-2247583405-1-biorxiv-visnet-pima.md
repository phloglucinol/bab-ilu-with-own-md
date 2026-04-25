---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzYzOTA3NjkxMg%3D%3D&mid=2247583405&idx=1&sn=c80b256f809468d593f7bb2c48e01dd0
canonical_url: https://mp.weixin.qq.com/s?__biz=MzYzOTA3NjkxMg%3D%3D&mid=2247583405&idx=1&sn=c80b256f809468d593f7bb2c48e01dd0
source_domain: mp.weixin.qq.com
title: bioRxiv｜ViSNet-PIMA：攻克长程作用建模难题，将量子精度推向全蛋白模拟
author: 
published_at: 
fetched_at: 2026-04-25T02:03:15Z
extractor: wechat_worker
content_hash: 86892a5c0040d4504e4c8a25321952cc52eaa3815c4bc66f848d74d7cf800b25
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/2r1FIaqNHdWS7Eba11LyiaST66L8RNGwY5TmoTFmeaIgLFNv9b21wZkjkqCtffdzF24J2jlcoib8AQibm3Of5XHHnR9TCE7uh4auOv5MpYJoVc/0.jpg) 

# bioRxiv｜ViSNet-PIMA：攻克长程作用建模难题，将量子精度推向全蛋白模拟

王童课题组 王童课题组 [ 智药邦 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

近日，清华大学生命科学学院王童课题组在bioRxiv上发布预印本文章：“Enhancing non-local interaction modeling for ab initio biomolecular calculations and simulations with ViSNet-PIMA”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt5uJ1vMcZKCpp6ZY9dH8XMA3jphogUBeoImeNR9GYtxF2ChPCOVCLTnibqX4MXrKD2nzPicmxcCnzhk4dibt8qam6ZqJ2Tt9r85M8/640.png)

该研究提出了名为ViSNet-PIMA的等变图神经网络用于分子结构建模和性质预测。该模型通过模拟物理学中的多极展开（Multipole Expansion）原理，专门捕捉生物分子至关重要的非局域（长程）相互作用，对分子性质预测性能提升55%以上。该工作进一步将ViSNet-PIMA模型引入AI2BMD模拟系统，新模拟程序AI2BMD-PIMA首次实现了对包括长程作用在内整个蛋白质全部原子间互作的量子精度计算和模拟，相比AI2BMD，其能量和受力计算误差降低超50%，对蛋白质折叠自由能等实验性质更为准确的计算，有效提升了AI驱动的动力学模拟在机理解释和结构设计研究中的应用价值。

**研究背景**

在当今生命科学研究的版图中，蛋白质与生物大分子的动力学模拟正处于从传统经验力场向人工智能力场（MLFF）转型的关键节点。尽管基于深度学习的力场模型在计算效率与局部精度上取得了显著进步，但一个长期被忽视的物理瓶颈始终制约着其向更高维度的演进：即生物分子系统内部复杂的非局域（Non-local）相互作用。

这种局限性源于大多数主流AI模型对“局部性”的过度依赖。为了维持计算效率，以及为不同构象的整体大分子生成充足DFT数据的代价高昂，现有模型通常采用截断（cutoff），只关注原子邻域有限半径内的几何环境，却难以有效捕捉跨越长距离的静电势能变化、电荷转移以及动态极化效应。在处理如蛋白质折叠、酶催化反应或离子通道输运等对电荷分布极其敏感的过程时，这种“物理视角的缺失”往往会导致模拟结果偏离真实物理规律，成为制约AI实现真正“从头算（ab initio）”精度的最后一道藩篱。

**研究方法**

面对长程建模缺失的困境，研究团队并没有盲目追求增加深度学习的参数量，而是回归物理本源，将经典物理中的多极展开理论融入模型架构。多极展开是描述分子电子密度分布的经典物理方法，它将电子密度分解为点电荷、偶极子、四极子等多阶项的组合与相互作用，对极化效应（Polarization）具有天然的描述能力。当分子的电子云受到周围环境电场的影响而发生形变时，多极展开的高阶项能够捕捉到这种动态的电荷重排。

  
团队通过精心设计的“场响应”与“相互作用整合”机制，模型第一次拥有了感知远距离电场变化和动态极化效应的能力。模块通过迭代方法更新全局多极信息，直至收敛，从而能准确刻画非局域静电效应。这意味着，AI不再仅仅是机械地记录原子坐标，而是像物理学家一样，学会了理解电荷与偶极子如何在分子内部产生共鸣。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt5O12qGhhJib0PfoTEic3YVdVib2ec0MkgS0g3QkuaicCSBY9v5XpHRMzbGib77zqria7bv4RLyu79RAt8X57FwXxbDPtt0icOryMhT0Q/640.png)

图1.模型使用的偶极-偶极、电荷-偶极相互作用矩阵

具体应用

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt4OUKJDxQZJPia7YExH1AAibBFLfRlcctl8NeAb24Ykib8dH7pA6Ciam9RlduG5ibbshQYPVh80wNhdnh4xCBETC573YoevIdWhawos/640.png)

图2.ViSNet-PIMA和AI2BMD-PIMA

  
**ViSNet-PIMA**

  
PIMA模块直接接入ViSNet交互层输出的原子级标量特征与等变向量特征。在初始化阶段，PIMA并不通过随机参数从零学习空间取向，而是直接继承ViSNet已经过几何正交变换精炼出的方向信息来构建初始的“虚拟偶极嵌入”。在随后的“场响应”迭代中，ViSNet提取的局域化学环境描述符扮演了关键的“调节因子”，动态地调制每个原子在全局电场下的极化敏感度。这种设计确保了非局域效应的建模是建立在精准的局域几何语境之上的。最后，ViSNet-PIMA以更小的参数量和训练成本，达到了超越同样层数的ViSNet精度的效果。

  
**AI2BMD-PIMA**

  
团队还创造性地提出了AI2BMD-PIMA新一代AI驱动的模拟系统，通过引入“迁移学习—预训练—微调”方案并用ViSNet-PIMA替代基于分子力学的蛋白片段间非局域计算，将ViSNet-PIMA融入AI2BMD模拟程序，从而使AI2BMD在不同蛋白构象及蛋白折叠/展开过程中的能量与力计算误差降低超过50%。这让全蛋白尺度的动力学模拟真正摆脱了传统经验参数的束缚，在保持计算效率的同时，实现了向“从头算（ab initio）”级别物理真实性的本质回归。

**结果与讨论**

为了验证ViSNet-PIMA的实战表现，研究团队在MD22与AIMD-Chig两大权威数据集上进行了全方位“大考”。实验结果不仅刷新了多项SOTA纪录，更揭示了模型在处理复杂生物物理现象时的独特优势。

在涵盖蛋白质、脂类、核酸及超分子（原子数最高达370个）的MD22数据集中，ViSNet-PIMA展现了压倒性的精度。相比于原版ViSNet，其能量预测精度平均提升了39%。尤为惊人的是，在buckyball catcher和双壁纳米管等大型超分子系统中，能量预测提升幅度高达44%-55%。这有力地证明了PIMA模块在捕捉大尺度非局域相互作用时的卓越性能，即使面对结构高度复杂的体系，也能游刃有余。

针对包含200万种构象的迷你蛋白数据集AIMD-Chig，ViSNet-PIMA再次证明了其对微小化学差异的敏锐感知：

1\. 过渡态的精准刻画。在蛋白质折叠与解折叠的自由能景观分析中，ViSNet-PIMA在关键的过渡态预测上展现出对原版模型的绝对优势。这表明，在非局域静电相互作用最为剧烈的构象转变期，ViSNet-PIMA能够捕捉到传统模型难以触及的物理细节。

2\. 物理量的全方位还原。在偶极矩（Dipole Moment）预测任务中，其精度相比原版 ViSNet实现了4.4倍的断崖式领先。这意味着模型不仅能算准能量，更在物理底层完美还原了分子的电荷分布特性。

3\. 普适性与统治力。即便与Equiformer v2、PaiNN等当前最强劲的AI力场相比，ViSNet-PIMA依然在各项指标上保持了9%至15%的领先优势。这种全方位的领先不仅确立了其作为新一代生物分子力场标杆的地位，更为解决生物大分子模拟中的“精度荒”提供了极具说服力的技术方案。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt6ROG7dhQLYOe3ibJeJqyhBeotGpH0NjnvZSVQ5z2R1RropwSk56UPDkwUeR41faXIB43RfvagyIS40HZABFZtVD06KNJr0CAGw/640.png)

图3.ViSNet-PIMA在AIMD-Chig数据集上的评估

为了验证AI2BMD-PIMA在真实蛋白质模拟中的鲁棒性，研究团队在Chignolin（175原子）、Trp-cage（281原子）、WW结构域（571原子）和ABD（746原子）四种不同规模的蛋白质体系上进行了严苛的横向测试。实验涵盖了折叠态、解折叠态及中间态等多种复杂构象，其结果深刻揭示了AI2BMD-PIMA对模拟范式的改变。

1.误差显著降低。数据显示，AI2BMD-PIMA在四种蛋白质上的平均每原子能量MAE降至0.0309 kcal/mol，力MAE降至0.7138 kcal/(mol·Å)。相比于原版AI2BMD，新方案在能量与力的预测上均实现了超过50%的误差降低。这意味着，在全原子尺度上，模型已经能够提供极高可靠性的动力学反馈。

2.突破“折叠态预测”的技术盲区。测试中最关键的发现源自对不同构象状态的对比分析。实验揭示了原版AI2BMD的一个深层瓶颈：在蛋白质处于紧密的折叠构象时，由于原子间距离缩短，非局域（长程）相互作用变得极其显著，而传统模型依赖的经典分子力学（MM）函数在此时显得捉襟见肘，导致力预测误差显著飙升。

3.实现“全状态”一致的从头算精度。相比之下，AI2BMD-PIMA展现出了令人惊叹的稳定性。得益于ViSNet-PIMA对非局域相互作用的原生建模能力，模型在折叠态、解折叠态及中间态之间表现出了高度一致的预测精度。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/yvQQqODtVt50Ue3YgzTQluk58R5xYy6bNEvGH358r189iaV1s1VuINhSguMTaDksKTYnYzOkicx75ibfRpy0SHsv9J6bX8atBpQMmdwRASkalc/640.png)

图4.AI2BMD-PIMA在不同蛋白质上的能量和力计算评估

**总结与展望**

除了显著的极低误差之外，PIMA还展现了卓越的“即插即用”通用性与适配力。作为一种物理启发的增强插件，它能无缝接入ViSNet、PaiNN等多种主流深度学习力场模型。实验证明，引入PIMA模块后，各模型在处理复杂生物分子时的性能平均提升达55.1%。这种设计无需推倒重构，仅需模块化集成即可显著强化模型对非局域相互作用的捕捉能力，为提升AI力场精度提供了极具普适性的高效方案。

这标志着AI力场从“数据拟合”向“物理驱动”的深度跨越。通过捕获关键的长程相互作用，它不仅在精度上刷新了SOTA纪录，更为复杂生命过程的数字化重现提供了可靠工具。展望未来，该模型有望在药物高通量筛选、酶催化机理研究及蛋白质大尺度构象转化等领域发挥核心作用。随着物理启发架构的持续演进，我们正加速步入一个计算效率与物理真实性完美融合的“真从头算”模拟新时代。

---

**团队介绍和开放职位**

清华大学王童课题组（https://wanggroup.ai/）围绕“人工智能+生物结构”展开研究，具体研究方向：

（1）系统：AI驱动的生物分子动力学模拟系统

（2）模型：几何深度学习算法和基础模型用于结构表征学习和性质预测

（3）应用：模型和动态模拟技术应用于高精度分子筛选、优化和设计

王童课题组现开放以下职位招聘：

（1）高性能计算/系统软件开发加速方向博士后/科研助理（优先考虑）

（2）深度学习/结构模型方向博士后/科研助理

\--------- End ---------

感兴趣的读者，可以添加小邦微信加入**读者实名讨论微信群**。添加时请主动注明**姓名-企业-职位/岗位**或**姓名-学校-职务/研究方向**。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/2r1FIaqNHdWMb1tkRfNxLniaVcmMJXiaG3X2GLVWIGB2bTicLFLDKqSia9qMmw1qhLNZ3rPdZxgrKWsnuSyvNsPPxlZ6ueuftbrE2emvhibAu2Aw/640.jpg)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/2r1FIaqNHdVMwEetx49J87Rqn1GnFrIXPkY5s7YicLdnKUYsMRXsgfBiacwkUUicAPuZYrqh2iaias3CyxghoKzyMz82nXCO3R2S7180x4wvm7Rw/640.png)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ialRowSiaYaicLpRDGcNCxDe2JW42DIHlYGhp0NmIhickwQUicNf81fmgO3icOeSxoeYoCAibbXzq1AxTrfEnU7yCz7Rw/0.png) 

 智药邦 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ialRowSiaYaicLpRDGcNCxDe2JW42DIHlYGhp0NmIhickwQUicNf81fmgO3icOeSxoeYoCAibbXzq1AxTrfEnU7yCz7Rw/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
