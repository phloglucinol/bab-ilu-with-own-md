---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489369&idx=1&sn=86a88c6c07112a020faf292b8bc3f3ee
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489369&idx=1&sn=86a88c6c07112a020faf292b8bc3f3ee
source_domain: mp.weixin.qq.com
title: 【佳作推荐】DeepMind联合团队发表Nature Machine Intelligence期刊论文：欧几里得快速注意力机制突破分子全局相互作用模拟瓶颈
author: 
published_at: 
fetched_at: 2026-04-24T16:02:01Z
extractor: wechat_worker
content_hash: bf1ef4e27ec77f0be413b0d868c708238ff34037a0a4deb6d57c84e763bc175a
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/upT6VMW9MvRD5LGPtDxlDEyu5jRevIQoZsz1dicoLP22HoNRmZCTEtZCgBxlXzsBSksdkT8C5LHAoaiamgvG1OweAkCpTRRT2wkauKO4tQCyA/0.jpg) 

# 【佳作推荐】DeepMind联合团队发表Nature Machine Intelligence期刊论文：欧几里得快速注意力机制突破分子全局相互作用模拟瓶颈

原创 ComputArt ComputArt [ ComputArt计算有乐趣 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/upT6VMW9MvTrtWtkF7pTYqQwuIdMXTxwct2UvaBWS3PKvnnBYmGMhvibHhDTcrpxOPe8EhxibvHdicopT369t0fpav5pibvKmxbZTIpQFSWRhQ8/640.jpg)

在原子尺度的机器学习研究中，分子动力学模拟的精度高度依赖于力场模型。然而，为提升计算效率，主流方法通常采用局部截断策略，仅关注一定范围内的邻近原子。这一设计虽然降低了计算成本，却难以准确描述分子体系中的长程相互作用与全局结构关联。与此同时，基于自注意力机制的模型虽然具备全局建模能力，但其计算复杂度随原子数呈二次增长，难以应用于大规模分子体系。如何在计算效率与全局建模能力之间取得平衡，成为该领域的关键挑战。

针对上述问题，Google DeepMind团队联合柏林工业大学、柏林学习与数据基础研究所、马克斯·普朗克研究所及高丽大学的研究人员，提出了一种专为欧几里得数据设计的全新机制——欧几里得快速注意力（Euclidean Fast Attention, EFA）。该机制可作为模块集成到现有局部模型中，在保持线性计算成本的前提下，有效提取原子间的长程关联特征。相关研究成果近期发表于著名期刊Nature Machine Intelligence【1】。

传统的局部消息传递神经网络（MPNNs）在处理分子结构时存在固有局限：每个原子节点只能与截断半径内的邻接原子交换信息。为突破这一限制，研究团队提出了欧几里得旋转位置编码（ERoPE），将原子的三维空间相对位移向量编码为复指数特征。为了赋予模型空间旋转不变性以及等变性，研究人员在三维单位球面上对注意力进行积分操作（图1b），消除了位置编码对特定空间方向的依赖。与传统方法不同，EFA允许中心节点直接访问所有节点，无论距离远近，从而在理论上具备捕捉长程物理效应的能力（图1a）。此外，EFA采用线性缩放注意力公式，通过先求和键（Keys）与值（Values）的外积再进行投影计算，实现了与原子数呈线性缩放的计算架构，显著区别于标准二次复杂度自注意力机制（图1c）。值得注意的是，该编码机制并非用于优化传统的经验力场参数，而是为深度学习网络提供具有严密物理意义的空间输入。在这一机制的驱动下，机器学习力场能够直接输出高精度的系统总能量及作用于各原子上的力，从而推动分子动力学模拟的发展。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/upT6VMW9MvSHtOtTgZ02Lh4QpEPxPeKlUwxOsqmphHshdQXcI0MCUdpS74DsbxVQwVndxQPhiag82ZOEeCYfqIX1ddJfSZqlOSgIiaOt9ExDs/640.jpg)

图1：本研究的核心概念与算法机制概览。（a）传统局部消息传递网络受限于局部截断半径的视野盲区，以及EFA能够直接获取全局节点信息的范围差异。（b）欧几里得旋转位置编码将空间位移向量投影编码为复指数特征，并通过在三维单位球面上进行数学积分消除方向依赖的操作过程。（c）对比展示了具有二次复杂度的标准自注意力机制与具有线性缩放时间复杂度的快速注意力机制在矩阵运算架构上的区别。

在模型设计上，研究人员将EFA模块引入MPNN中，使其在保留局部结构建模能力的同时，具备全局信息交互能力，从根本上突破了传统消息传递网络依赖逐层传播信息的限制。为了全面验证模型性能，研究人员针对不同的物理和化学场景，分别采用两类基准数据集进行独立训练和测试：一类是用于验证基础几何与物理特性的理想化系统（Idealized systems）合成数据集（如双粒子系统以及类氯化钠多粒子体系等）；另一类是用于评估真实化学场景的分子与材料基准数据集，涵盖非局部电荷转移、SN2反应轨迹、DES370K二聚体基准测试以及累积烯烃分子等。

在基础能力验证方面，研究人员首先考察了模型的几何特征表达能力。针对微观局部原子环境，实验证实EFA引入高阶等变特征后，展现出等同于SO(3)连续卷积的几何解析力（图2a）。在宏观全局层面，研究人员在具有不同链长且拓扑结构完全非同构的几何图形数据集（k链数据集）上开展实验。结果表明，引入EFA后，模型能够在更少的网络层数下捕捉整体拓扑结构（图2b），以单层网络实现非同构图的精准区分，展现出更强的全局几何感知能力。进一步地，研究团队在类氯化钠离子体系数据集上评估模型的可扩展性。图2c展示了不同模型在能量预测上的误差随体系尺寸变化的趋势。可以看到，传统基于局部截断的模型随系统尺寸增大误差明显累积，而引入EFA后，模型能够在更大范围内维持稳定精度。推理时间随原子数变化的关系图进一步表明（图2d），该方法整体呈线性增长趋势，说明其在引入全局信息建模能力的同时，仍然保持了良好的计算效率，为大规模分子体系的应用奠定了基础。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/upT6VMW9MvQxR2V7X4ZlriaeK3OmcyoKwS9MnCfg7UGJHhCxOfsyHs5arrML6CzI4tibtPg7S0usYM6ic3yR8nL2MtM56GlyYxSgNtiaGPvR4PE/640.jpg)

图2：EFA的基础性能测试。（a）EFA操作与SO(3)卷积的相似性验证。（b）在分辨不同链长且拓扑非同构的几何分子图时，传统消息传递网络与引入新机制的网络所需的最少网络层数对比。（c）在具有不同原子数的NaCl-like多粒子系统上，MP+EFA模型预测的能量均方根误差远低于标准MP模型。（d）MP+EFA模型的评估时间随系统原子数（N）线性增长，证明了其线性标度特性。

在真实化学场景的测试中（图3），研究团队评估了模型对典型卤素取代化学反应的模拟能力。传统模型在反应物距离较远时，由于缺乏对长程相互作用的建模能力，预测的能量曲线逐渐偏离真实趋势，无法正确描述反应路径。而引入EFA后，模型能够在整个反应坐标范围内准确拟合势能变化，成功还原反应势垒与稳定构型（图3a）。进一步的分子动力学模拟显示（图3b），传统模型因忽略远距离作用，反应物在接近过程中缺乏有效相互作用，最终未能发生反应；而在引入EFA的模型则能够正确捕捉离子与分子之间的吸引效应，引导体系完成空间重排并成功发生反应。这表明，EFA不仅提升了数值预测精度，也在动力学层面恢复了正确的物理行为。此外，在双分子复合物测试中（图3c和3d），新模型精准捕获了长程能量分布规律，其提取出的相互作用函数展开系数分布模式与基准真实数据实现了高度吻合。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/upT6VMW9MvThFEOMhtgPWXSAAZibSDFrmP1w1XPqzLOynqib0mV140mnx6aHdIR6GQrEfHuyVCr9VDzk95FXnGd3P5xNkGAAmCUoXYeEia5jco/640.jpg)

图3：EFA在多种真实化学系统中的应用表现。(a) 在SN2反应中，传统的基础局部消息传递神经网络（MP）预测的势能面在长程区域存在非物理伪影并给出错误的渐进行为，而MP+EFA模型能准确描述整个反应坐标。(b) 相应的分子动力学轨迹显示，只有MP+EFA模型驱动的模拟能发生正确的反应，生成产物。(c) 在DES370K二聚体基准测试中，标准MP模型在分子间距超过截断距离后失效，而MP+EFA模型能准确预测整个结合能曲线。(d) 将长程相互作用拟合为距离的幂级数并比较系数，MP+EFA模型的预测与真实基态参考值高度相关（s=0.95），远优于标准MP模型（s=0.56）。

面对含有复杂的电子离域现象的体系，单纯依赖距离的局部模型常常会遭遇彻底失效。在累积烯烃分子数据集测试中，该体系表现出典型的非局部量子效应。传统模型在预测该分子能量随二面角旋转变化时几乎呈现一条直线，完全错过了真实的物理能垒。而引入具有三维方向信息处理能力的等变性EFA模块后，模型立即学习到电子离域带来的全局影响，精准重构了能量波动曲线（图4a）。这种微观层面的预测差异进一步体现在分子动力学行为及可观测物理量上。MP+EFA模型对微观能垒的精准描述（图4b和图4c），不仅正确引导了动力学模拟中的构象空间物理采样，使其在势能极小值附近合理波动，更在宏观系统功率谱上成功消除了由非物理采样引发的虚假吸收峰信号。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/upT6VMW9MvR0ZjVNaInwIwSj7a83R8TfWKK7pKMPPhzfwibhGMzNMSHLkk92G8viada818koGW1rvlVAAxmQAZriaM4hfBhujBn6evWoun3jRo/640.jpg)

图4：处理电子离域效应时的能量与构象动力学分析。（a）以累积烯烃分子为例，其能量强烈依赖于末端CH₂转子间的二面角θ，使用等变特征（ℓ>0）的EFA模型能准确描述能量分布，而仅用不变特征（ℓ=0）的EFA或层数不同的标准MPNN则预测出平坦的曲线或低估能垒。（b）分子动力学模拟显示，基于错误平坦势能面的标准MP模型会均匀采样所有二面角，而基于准确势能面的MP+EFA模型则使二面角在最小值附近正确波动。（c）错误的动态行为导致标准MP模型预测的功率谱中出现虚假峰，突显了准确描述此类非局部效应对预测实验观测量的重要性。

  
**小编总结**  

该研究提出的EFA机制的核心突破在于，在保持线性计算复杂度的前提下，实现了对分子体系中全局原子相互作用的直接建模。其价值不只体现在单一任务性能提升，更在于提供了一种更具普适性的建模思路，即通过引入高效的全局信息交互机制，在不显著增加计算成本的情况下突破传统局部模型的信息瓶颈。这对于涉及远程效应的分子模拟任务具有重要意义。

  
**参考文献**

\[1\] Frank, J.T., Chmiela, S., Müller, KR. et al. Machine learning global atomic representations with Euclidean fast attention. Nat Mach Intell 8, 388–402 (2026). https://doi.org/10.1038/s42256-026-01195-y.
  
  
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
