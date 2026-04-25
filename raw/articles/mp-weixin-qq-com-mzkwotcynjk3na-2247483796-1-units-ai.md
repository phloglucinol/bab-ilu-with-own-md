---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkwOTcyNjk3NA%3D%3D&mid=2247483796&idx=1&sn=ba72094da2527c5c15fae5cc9ceaa4f4
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkwOTcyNjk3NA%3D%3D&mid=2247483796&idx=1&sn=ba72094da2527c5c15fae5cc9ceaa4f4
source_domain: mp.weixin.qq.com
title: 文献精读｜UniTS框架：AI如何解决过渡态搜索的“第一公里”难题？
author: 
published_at: 
fetched_at: 2026-04-25T02:03:40Z
extractor: wechat_worker
content_hash: 7c92cc9341208f0a74bfc1fcfc3d4c1c68979073e9d03268d46154eb411698ba
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/DHoTyt7PSzbeVvUhkfNnoYHzVRibRebTN4Yu0yCxlEzSw0icODsicMMGAfhIg8TQU2QO5nVyG2T0e8V9B28FHKxSg/0.jpg) 

# 文献精读｜UniTS框架：AI如何解决过渡态搜索的“第一公里”难题？

原创 捞鱼 捞鱼 [ 洞庭湖捞鱼 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/pdt0cLstDG6IbX1ibkVcPWnJibV3OL9NQhxUpcCr2nCkl6fEictdcPoC8h80ZsE6m8by3dNLL2Cicp0FreVjuuTaAQ/640.gif)点击上方

蓝字

 关注我们

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/hGpW8f7xcCboFdchPdLI6ANpcpcrKlnAcHHUKzDIrlOIMzTnK0MeDhZKFT11S2cEMwshn3bE1TqkFjUpJbvklA/640.jpg)

A unified framework for automated transition state generation to accelerate mechanistic exploration in organic synthesis 

  
简述：本文介绍了一个名为UniTS的统一框架，它包含一个由文献挖掘构建的高质量过渡态数据集（UniTS-Lib）和一个基于高阶等变图神经网络的扩散生成模型（UniTS-Gen）。该框架能够仅根据反应物的二维图结构和反应位点，生成高度可信的复杂有机反应（含过渡金属催化）的三维过渡态结构，为机理研究提供了强大的“初始猜测”生成器。

01 研究问题  
  
  
传统的量子化学方法（如QST2/3或伯恩哈德-李普曼线性组合方法）极其依赖“初始猜测”（Initial Guess）。如果初始结构离真实的过渡态太远，计算往往会发散或收敛到错误的结构。

对于涉及过渡金属催化、大环化或手性诱导的复杂体系，构建合理的初始猜测通常需要化学家耗费数天甚至数周的时间进行手动试错。

本文的任务非常明确：利用生成式AI，自动化地“猜”出高质量的过渡态结构。 具体的挑战在于，模型不能只处理简单的SN2取代反应，必须能泛化到真实的、复杂的、包含各种过渡金属（如Pd, Rh, Ru）的有机合成反应中，并且要支持从二维分子图直接生成三维结构，而不需要预先知道产物的精确立体构型。

02 背景与难点拆解   
  
  
为什么通用的过渡态生成模型迟迟没有出现？核心矛盾在于“数据稀缺”与“结构复杂性”之间的不对称。

首先是数据的匮乏。与数以亿计的稳定分子数据库（如ZINC, PubChem）不同，过渡态是瞬态结构，不存在于常规数据库中。现有的过渡态数据集（如Transition1x）大多局限于小分子（<30原子）和简单的气相反应，缺乏过渡金属催化等复杂反应的数据。没有高质量的“教材”，AI就学不会复杂的“化学直觉”。

其次，过渡态处于势能面的最高点，是一个不稳定的平衡点。化学键处于“半断半连”的微妙状态，键长、键角的微小偏差都会导致能量剧烈升高。这对生成模型的精度要求远高于普通的稳定分子生成。

此外，建模逻辑上存在一个深层难点：如何在不依赖产物3D结构的前提下生成TS？ 许多现有的方法（如NEB插值）需要同时知道反应物和产物的3D结构。但在探索未知反应机理时，产物的立体构型往往是未知的（这正是我们要研究的）。

因此，一个真正实用的工具必须具备“生成”能力，即仅凭反应物和反应位点信息，就能在构象空间中“无中生有”地构建出过渡态。

03 方法路线总览：从“变废为宝”到“高阶等变”   
  
  
作者提出了一套完整的“数据+模型”解决方案，技术链路清晰且环环相扣：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DHoTyt7PSzbeVvUhkfNnoYHzVRibRebTN78Kkib3GWnK1fouMsQNknQF8KLaDFRyBreJQOVMg0Areny3jJumy1Hg/640.png)

第一步：构建UniTS-Lib数据集（图1a）。这是本工作的数据基石。作者没有重新计算数万个反应，而是采取了“文献挖掘”的策略。他们编写了自动化脚本，从346篇有机合成文献的“补充材料”（Supplementary Information, SI）中提取了原始的过渡态坐标。

这些数据被提取后，作者使用统一的高精度DFT方法（B3LYP-D3/Def2SVP）对这些结构进行重新优化和频率验证，最终清洗出4391个高保真的过渡态结构。

这不仅解决了数据来源问题，还保证了数据分布符合真实的科研场景（涵盖42种元素，包括多种过渡金属）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DHoTyt7PSzbeVvUhkfNnoYHzVRibRebTNa2b1pMBvwJF4xCzF9ibcq3t3XVZ1MjKpY5Qdd2Y4Mdcoy7QXcOTckGw/640.png)

第二步：设计UniTS-Gen生成模型。有了数据，如何建模？作者设计了一个基于条件扩散模型（Conditional Diffusion Model）的生成器。 输入端：仅使用反应物的2D分子图和反应中心（Reactive Site）的原子索引。

这极大地降低了使用门槛。

核心去噪网络：引入了高阶等变图神经网络（HiEGNN）。 在此处进行深入解释：为什么要用“高阶”等变网络？普通的等变网络（如EGNN）通常只处理标量（L=0）和矢量（L=1）特征。

但在过渡金属催化剂中，d轨道的参与使得电子云环境具有高度的各向异性，反应中心的几何形状往往偏离简单的球对称。HiEGNN引入了高阶球谐函数（Higher-degree Spherical Harmonics, L>1）作为特征表示，就像是用更高分辨率的镜头去观察原子周围的空间环境。

这种对方向性信息的敏锐捕捉，使得模型能够精确重构出金属中心复杂的配位几何（如平面正方形、八面体），有效防止了结构坍塌。

第三步：生成与验证。模型从随机高斯噪声出发，在反应物2D图和反应位点信息的引导下，逐步去噪，最终“凝固”成合理的三维过渡态结构。

为了证明模型的有效性，作者对数据复杂度和生成质量进行了多维度的量化分析。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DHoTyt7PSzbeVvUhkfNnoYHzVRibRebTNKeqPWchm5ianIMoweCmK0utqK3a9tMBZQFJscxooSwaHZw8YBAxQaUg/640.png)

这张图有力地反驳了“现有数据已足够”的观点。

图2a的弦图（Chord Diagram）展示了UniTS-Lib中元素共现的丰富性。外圈不仅有常见的C/H/O/N，还密布着Pd, Ir, Rh, Ru等贵金属催化剂，内部错综复杂的连线表明这些元素参与了多样的化学键合。

图2c的雷达图更是直观地对比了UniTS-Lib与经典数据集（Transition1x）的差异：UniTS-Lib在元素多样性、分子尺寸（最大原子数>200）和配方复杂度上都呈碾压之势。

这说明模型是在“困难模式”下训练的，具备处理真实合成问题的潜力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DHoTyt7PSzbeVvUhkfNnoYHzVRibRebTN2AujPaltlSjwIIg3sfzEVaBIelNIoLUz0IqzOHJcZUxviaiaBAz0ib6gw/640.png)

这是验证模型核心假设的关键图表。作者对比了使用HiEGNN（高阶）和普通EGNN（标量/矢量）作为去噪内核的效果。

图4a展示了一个Pd催化的C-H活化过渡态。使用EGNN生成的结构（红色框）发生了严重的“结构坍塌”（Structural Collapse），配体与金属中心的距离错乱，化学上完全不合理。而HiEGNN生成的结构（绿色框）不仅构型正确，RMSD仅为0.12 Å。

更重要的是，作者提出了\*\*“冲突率”（Clash Ratio）\*\*这一指标（图4b），即结构中出现原子重叠或非物理键长的比例。在复杂的UniTS-Lib测试集上，EGNN的冲突率高达66.4%，而HiEGNN降至3.9%。

这深刻揭示了在处理复杂三维几何时，高阶几何特征不仅是锦上添花，而是决定生成的分子是否符合物理规律的必要条件。

05 结果解读与边界条件   
  
  
模型不仅能“复现”已知结构，还能在未知的化学空间中“泛化”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DHoTyt7PSzbeVvUhkfNnoYHzVRibRebTNUmAkaom5HdWSWIQvYkIZYYCnichicH7SwYVic40hfxiaMV69I25lddaYOA/640.png)

模型被应用于两个极具挑战的真实案例（Out-of-Sample测试）。 第一个案例（图5a）是路易斯碱-硼基自由基促进的C-H与C-F键选择性活化。

对于同一个反应物，仅通过改变输入的“反应位点索引”，UniTS-Gen就成功生成了通往C-F活化（TS4）和C-H活化（TS5）的两种截然不同的过渡态。后续DFT计算表明，C-H活化的能垒更低，这与实验观测的选择性一致。这证明模型学到了“条件生成”的精髓，能作为探索反应路径分支的导航仪。

第二个案例（图5b）是复杂的\[3+2\]偶极环加成。该反应存在多个手性中心，涉及复杂的立体选择性。UniTS-Gen不仅生成了所有可能的四种非对映异构体过渡态（TS6-TS9），而且令人惊喜的是，它找到的TS6构象比原始文献中报道的最低能垒结构还要低3.1 kcal/mol。

这意味着AI不仅仅是在模仿人类专家，甚至在构象搜索的广度上超越了人类。传统的过渡态搜索往往受限于化学家的直觉或有限的构象采样，容易陷入局部极小值。而基于扩散模型的生成过程具有随机性，能够在高维构象空间中进行更广泛的探索，从而发现那些被人类忽略的、动力学上更有利的“幽灵”构象。

边界条件与局限性：作者坦诚地指出，尽管生成的结构可以直接作为DFT优化的初猜，但成功率并非100%。在最具挑战性的“公式外推”（Formula-OOS）测试中，优化收敛到正确的一阶鞍点的成功率约为41.9%。这意味着用户仍需具备一定的DFT知识来筛选结果。

此外，模型目前主要针对均相有机反应，对于非均相催化或酶催化等涉及更复杂环境的体系，其适用性尚待验证。

06 给研究者的抓手  
  
  
作为初猜生成器： 当你在寻找复杂催化循环的过渡态而屡战屡败时，使用UniTS-Gen生成一批结构（建议生成10-20个），然后批量提交DFT优化（Opt=TS）。

利用反应位点控制： 如果你的反应物有多个竞争位点（如区域选择性问题），可以通过指定不同的反应原子索引，强制模型生成对应路径的过渡态，从而快速比较能垒。

构象采样的补充： 不要只生成一个结构。利用扩散模型的随机性，生成多个构象，这有助于发现比你直觉中更优的低能过渡态，避免漏掉真正的优势路径。

关注Clash Ratio： 如果生成的结构看起来原子挤在一起（Clash），不要浪费算力去优化它，直接丢弃。虽然HiEGNN降低了冲突率，但仍需人工检查。

数据清洗的启示： 你的课题组过去积累的失败或成功的计算文件（log/out文件），不要删。参考本文的思路，建立组内的TS数据库，这可能是未来训练私有模型的宝贵资产。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/ibibcV5C2Fxt8KF2nvUB4ibibbBvwBdymVkQKw5xG6xAoAFellPY0mz4BREtkJ1M3Mib3uSxwXrpSDicAia7jCEKemWsw/640.gif)

END  

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/HCvJibB1GOk9I5gVaia7OYPPgE0DUhlhOgrZoiaaKeuCTuXmQCy47oxxo9Tt1uBibtnS1hx8I8EelibTXuqhjNtliaVg/640.gif)

点赞在看哦～  

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DHoTyt7PSzaWahcZMgIqfMjMrcicc85Ehhhj1k3mQEFx6DlbWk3kWria2btqvTxcVTsXZ76Srretbs3qr8DFb8rQ/0.png) 

 洞庭湖捞鱼 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/DHoTyt7PSzaWahcZMgIqfMjMrcicc85Ehhhj1k3mQEFx6DlbWk3kWria2btqvTxcVTsXZ76Srretbs3qr8DFb8rQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
