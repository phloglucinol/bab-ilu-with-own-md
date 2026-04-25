---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkzMzkxNjQ4Nw%3D%3D&mid=2247494089&idx=1&sn=4d23ac930c93eee98f86121171605dbb
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkzMzkxNjQ4Nw%3D%3D&mid=2247494089&idx=1&sn=4d23ac930c93eee98f86121171605dbb
source_domain: mp.weixin.qq.com
title: Nat.Comput.Sci（IF=18.3）|伊利诺伊大学团队开发无需集体变量的反应坐标学习方法，精准预测蛋白质折叠路径
author: 
published_at: 
fetched_at: 2026-04-25T02:03:11Z
extractor: wechat_worker
content_hash: 8faf638a54b4b0c427be762a616577d62d92dad6a48151c8b9c87af7135b18cd
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/m3AVI6OFoUDibpOmjgYcDOVQCdicWCxkic07Hew6m5hDXf6WdCFOh8nxXRibDFnqGrMDrRSvibZ37PribibibRyaDQvzKkyYC5zLjwm3GxLdNCH6zibQ/0.jpg) 

# Nat.Comput.Sci（IF=18.3）|伊利诺伊大学团队开发无需集体变量的反应坐标学习方法，精准预测蛋白质折叠路径

粑粑柑 粑粑柑 [ AI蛋白质前沿站 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

  
**导 语**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m3AVI6OFoUAXxs1suHzUfWlBF9JG4KFHYN0PIg399hkcjaicrYfDAKJIXFb2kOSdmGP1iaoicUKQyYt2OhafVy8MKlUEtx8a6F1HY3UiaOialiasM/640.png)

来自**伊利诺伊大学厄巴纳-香槟分校**的研究团队，在期刊《Nature Computational Science》（影响因子 18.3）发表了题为 _“Learning the committor without collective variables”_ 研究论文。团队开发了基于几何向量感知器（GVP）的图神经网络架构，无需手工设计集体变量（CVs），直接从原子笛卡尔坐标预测承诺函数，同时实现了原子级的可解释性，能精准识别复杂分子跃迁中的关键原子，还可对底层过程的速率常数进行精确估计，为复杂分子动力学的理解和建模开辟了新路径。
  
  
**摘 要**

本研究介绍一种构建在几何向量感知器上的图神经网络架构，它能够直接从原子坐标预测提交者函数，从而绕过对手工制作的集体变量的需求。该方法提供了原子级别的可解释性，能够在没有先验假设的情况下，精准指出复杂转变中的关键原子参与者。该方法应用于不同的分子系统，能够准确推断提交者函数，并突出每个重原子在转变机制中的重要性。它还能为潜在过程提供速率常数的精确估计。团队所提出的方法通过实现无需集体变量的学习和自动识别复杂分子过程中具有物理意义的反应坐标，有助于理解和建模复杂动力学。
  
  
**介 绍**

在复杂分子系统的研究中，稀有跃迁（即分子在两个亚稳态之间的转换）是理解分子功能和反应机制的关键，比如蛋白折叠、有机化学反应、分子构象变化等过程均涉及稀有跃迁。过渡路径理论（TPT）是描述这类过程的基础理论，该理论将分子系统的跃迁过程抽象为两个亚稳态 A 和 B 之间的转换，而承诺函数是这一理论中最核心的物理量之一，其定义为：从任意给定的分子构型出发，轨迹在到达亚稳态 A 之前先到达亚稳态 B 的概率。

  
承诺函数被公认为是最优的一维反应坐标（RC），能精准捕捉分子在 A 和 B 之间跃迁的进程，因此准确估计承诺函数是研究稀有跃迁的核心目标。传统的承诺函数估计方法主要分为两类：一类是基于射击策略的模拟方法，另一类是基于时间相关函数变分原理的方法。近年来，机器学习（ML）方法成为发现复杂反应坐标的重要方向，这类方法能将集体变量进行非线性组合，构建更灵活的反应坐标模型，但仍依赖于人工选择的输入特征（集体变量），并未从根本上解决集体变量带来的问题。

  
集体变量是原子位置的函数，作为低维嵌入保留了分子跃迁的动态特征，理想的集体变量应能区分不同的构象态并捕捉系统的慢模式。但集体变量的选择长期以来依赖研究人员的物理和化学直觉，常用的变量包括原子间距离、二面角或其复杂组合，这种直觉驱动的选择缺乏定量标准来评估其是否能准确封装分子的真实动力学，且低维集体变量模型在描述复杂分子系统的跃迁时，往往因信息损失而难以保证准确性。

  
为突破这一局限，研究人员尝试用先进的机器学习方法（如人工神经网络）对大量描述符进行非线性组合，构建灵活的集体变量，但这类方法仍需选择合适的输入特征；也有研究尝试直接从笛卡尔坐标学习有意义的集体变量，却导致分子模拟的计算成本大幅增加。

  
在这一背景下，图神经网络（GNN） 成为解决分子系统高维数据问题的理想工具，其能以数据驱动的方式从分子结构中提取几何和物理信息，将原子/残基作为节点，通过边特征编码原子间的相互作用（如距离、化学键）。但早期的 GNN 架构缺乏一致的几何信息整合和变换方式，无法准确描述分子的取向和空间对称性。而几何向量感知器图神经网络（GVP-GNN） 的出现解决了这一问题，该架构是欧氏空间等变的 GNN 模型，能同时处理标量和向量特征，在保持计算效率的同时，实现了对分子空间结构和对称性的精准捕捉，其在蛋白质模型质量评估、计算蛋白质设计等结构生物学任务中已展现出优异的性能。

  
GVP-GNN 对空间结构和对称性的敏感特性，使其非常适合计算分子系统中与原子空间排布高度相关的物理量（如承诺函数）。本研究基于 GVP-GNN 架构，开发了全新的承诺函数图神经网络（qGNN），首次实现了从原子笛卡尔坐标直接学习承诺函数，完全摒弃了对人工设计集体变量的依赖，同时通过灵敏度分析实现了原子级的可解释性，为复杂分子系统的稀有跃迁研究提供了全新的方法学。
  
  
**实验方法**

**qGNN 架构的理论基础**

qGNN 的学习框架基于承诺函数的变分原理，这是构建模型损失函数的核心。根据过渡路径理论，从反应物态 A 到产物态 B 的净正向标量通量JAB\[q;τ\]可表示为：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m3AVI6OFoUBm1mRdfIqjxLSfTVKibTzHZAlGyp9yrzS7nWlCBouf9Lbx79OGFt9BFbEDxl4N4HkAGTdHF4SZB5hjbVDKxjeP6GibRhiaqtKe3o/640.png)

其中，τ为时间滞后，q为承诺函数，且满足边界约束：若分子构型x∈A，则q(x)=0；若x∈B，则q(x)=1。承诺函数是使JAB\[q;τ\]取最小值的函数，满足变分条件δJAB\[q;τ\]/δq=0（τ的选择保证跃迁机制的马尔可夫性），因此时间相关函数C\[q;τ\]成为模型学习的核心损失函数基础。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m3AVI6OFoUDPvcbxxX23Xf28NKdHkYoW1h9UztvOLZRZh8Ct3bDLYqgxibH6M8OEcnzn3H2tV6jLIVv5GNTtLuSgJXSueoBcgjh8bqV1XUHs/640.png)

_图1\. qGNN 的学习过程示意图_
  
  
**分子图的构建**

要实现 AI 对分子系统的学习，首先需要将原子笛卡尔坐标转化为图神经网络可处理的分子图结构，这是连接分子物理特性和机器学习模型的关键桥梁。从分子动力学轨迹中提取每个分子构象的原子坐标，构建分子图G=(N,E,A)，其中：

  
**1.节点（N）：**代表分子中的重原子，每个节点赋予标量特征Sn∈Rn和向量特征Vn∈Rv×3，本研究中初始设置n=v=1，即每个节点仅包含 1 个标量和 1 个向量特征；

  
**2.边（E）：**代表原子间的相互作用，每条边同样赋予标量特征Se∈Rn和向量特征Ve∈Rv×3，编码原子间的距离、相对取向等几何信息；

  
**3.邻接矩阵（A）：**编码分子的连接性，即原子间的成键和空间邻近关系。

  
通过这一过程，将高维的原子笛卡尔坐标（R3N）转化为 GNN 可处理的、包含分子几何和结构信息的图结构，实现了分子物理信息向 AI 模型输入特征的转化。
  
  
**GVP-GNN 的核心计算**

qGNN 的核心是 GVP-GNN 架构，其关键在于几何向量感知器（GVP）层对分子图标量和向量特征的等变变换，能在保留分子空间对称性（旋转、反射等变）的同时，将特征映射到高维潜空间，提取更具代表性的分子特征。

  
GVP 层的操作对象是标量-向量特征对(S,V)∈Rn×Rv×3，通过线性变换和激活函数，将其映射到更高维的特征空间：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m3AVI6OFoUB402YdfJkgGNc4enhzT5dV3ibEkoPmKOImmD8qHDMcRjH1jOPwia8QhhUHYZc7SnepvG7vMHbqbCAibmQVLQaraoCp5MxgRGIicrY/640.png)

设置m=16、μ=8（即m=2μ），实现了特征的维度提升。同时，GVP 层引入向量门控机制，让标量信息能调节向量通道，且不破坏等变性，既提升了模型的表达能力，又保证了对分子几何结构的精准捕捉。

  
特征变换后，模型通过消息传递机制实现图中节点的特征更新：每个节点根据其邻居节点的特征和连接边的特征，更新自身的标量和向量特征，从而整合分子的局部和全局几何信息，让模型能捕捉到驱动分子跃迁的关键结构特征。
  
  
**qGNN 的输出层**

经过 GVP 层的特征变换和消息传递后，模型需要从节点级的特征得到图级别的承诺函数预测值（即整个分子构象的承诺函数值）。采用置换不变池化操作（节点嵌入的求和），将所有节点的高维特征进行整合，得到一个标量输出qω（ω为 qGNN 模型的所有参数），该标量即为模型对当前分子构象承诺函数的预测值，实现了从分子图到承诺函数的端到端映射。
  
  
**损失函数的构建与优化**

基于承诺函数的变分原理，构建包含边界条件惩罚的损失函数，以优化 qGNN 的参数ω：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m3AVI6OFoUCUWkHr0UeTVtgW9sNyxay7PrhQhreYQpiaxY75kRicS04ATVF2uEEQPknEW3TeJhBmsZvYkSS6GSsRzuZrt2t7gRzFB1YicZaiccA/640.png)

其中，λ∈R+为预先选择的正标量惩罚系数，LAB为边界条件惩罚项，确保模型在亚稳态 A 处的预测值趋近于 0，在亚稳态 B 处的预测值趋近于 1。模型的优化目标为找到使损失函数最小的参数ω，得到真实的承诺函数：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m3AVI6OFoUAdkWWTDsic8j2qjGk2LrYmDr2ASletWbyhdnDs7YXIbSYsfAy2Oe5GK3ia8jHUys7brfHSPrVXN3fhLOaGQ9Yvr7UTIuUNicZvHc/640.png)

由于模型训练使用的分子动力学轨迹是偏置模拟（引入了偏置力以加速稀有跃迁的采样），会破坏分子的真实动力学，因此采用重加权方法将偏置系综的平均转化为无偏系综的平均，以保证承诺函数估计的准确性：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m3AVI6OFoUCqxkuh7ANEKsDruQ2AYkicXiaOYOCXz3bArmNiaYB0ya1Aciax6CjPyEeZR1JdBnibOgbEGyQwYcrlNXhoGWhlynsXbbuqFhIYN4pI/640.png)

其中，下标b代表偏置系综的平均，δW(z)为扰动的平均力势，kBT为热运动能，f和g为任意函数。

  
模型优化采用Adam 优化器，激活函数为 tanh，神经网络权重采用Xavier 初始化，除惩罚系数λ外，所有优化超参数在不同分子体系中保持一致，保证了方法的普适性。
  
  
**灵敏度分析**

为实现原子级的可解释性，团队开发了节点/边灵敏度分析方法，定量计算每个原子（节点）和原子间相互作用（边）对承诺函数预测的贡献，从而识别驱动分子跃迁的关键原子。

  
对于包含ℓ个时间步的分子动力学轨迹，构建图轨迹：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m3AVI6OFoUDWNwW5D1NJCL8mYKsxoGZncL7erbI95UH8GFMvwyvDjA3kbZBia25n77HKFFBQUemLSFcICcwJ5qic6zv13ibD15Nd5fkDVficy4E/640.png)

第i个节点的绝对灵敏度计算为：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m3AVI6OFoUD0j6yIZjZzLHdSV6icLlCV05CjaBIv5HGkRImNE21LLl8glSibo7ibhj5dBB9kpL6NMyjlow1o0TibOohTEDWJbMxAt52gT7UibUcg/640.png)

其中，vi为第i个节点的向量特征，∥⋅∥2为欧几里得范数。在此基础上，计算相对灵敏度si/maxjsj，将贡献最大的原子相对灵敏度设为 1，其余原子在 \[0,1\] 范围内，直观反映各原子对分子跃迁的重要性。
  
  
**分子动力学模拟**

为获取 qGNN 训练所需的分子动力学轨迹，针对不同分子体系，采用NAMD 软件结合Colvars 库进行模拟，通过微正则系综元动力学扩展自适应偏置力（WTM-eABF） 算法实现增强采样，加速稀有跃迁的采样过程。所有模拟中，涉及氢原子的共价键均通过 RATTLE 算法约束，不同体系的模拟参数（如 CV 范围、偏置温度、势垒高度等）根据体系特性微调，具体如下：

  
**1.NANMA 异构化：**采用 CHARMM22 力场，以重原子相对于C7eq和C7ax的 RMSD 为偏置 CV，300K 下模拟 100ns；

  
**2.三丙氨酸构象平衡：**采用 AMBER ff14SB 力场，以重原子相对于两个亚稳态的 RMSD 为偏置 CV，300K 下模拟 100ns；

  
**3.狄尔斯-阿尔德反应：**采用 GFN2-xTB 半经验量子化学方法，以新形成的两个 C-C 键长为偏置 CV，32 个 walker 模拟，每个 walker2ns；

  
**4.Trp-cage 折叠：**使用 D.E. Shaw Research 提供的 208μs 原子分辨率轨迹，仅考虑Cα原子的笛卡尔坐标；

  
**5.villin 折叠：**使用上述相同模拟平台，基于所有重原子的笛卡尔坐标构建分子图。
  
  
**模型训练与验证流程**

1.从分子动力学轨迹中提取原子坐标，构建分子图并划分训练集/验证集；

  
2.将分子图输入 qGNN，通过 GVP 层和消息传递提取特征，得到承诺函数预测值qω；

  
3.基于变分原理和边界条件构建损失函数，结合重加权方法优化模型参数；

  
4.利用验证集评估模型性能，调整超参数（仅惩罚系数λ）；

  
5.对训练完成的模型进行灵敏度分析，识别关键原子；

  
6.计算分子跃迁的速率常数，并与已发表的参考值对比；

  
7.对过渡态区域的构象进行 K-means 聚类分析，研究过渡态集合的结构特征。
  
  
**研究结果**

**NANMA异构化**

NANMA（二丙氨酸）的C7eq和C7ax构象异构化是分子动力学研究中的经典模型体系，传统方法通常以主链二面角ϕ和ψ为集体变量估计承诺函数。本研究中，qGNN无需任何集体变量，直接从 NANMA 的重原子笛卡尔坐标学习承诺函数：

  
**1.承诺函数预测高度准确：**将 qGNN 学习到的承诺函数投影到(ϕ,ψ)子空间，得到的承诺函数图与基于射击策略的无偏数值结果、基于变分承诺函数网络（CV-based）的结果高度吻合，均展现出清晰的分离线（q=0.5 等承诺函数超平面），这是承诺函数捕捉跃迁进程的核心特征，证明了 qGNN 无需集体变量即可精准复现分子的跃迁动力学；

  
**2.关键原子识别与物理直觉一致：**节点灵敏度分析精准定位了驱动 NANMA 异构化的关键重原子（原子 14、0、16、12），这些原子正是定义主链二面角ϕ的核心原子，同时二面角ψ的构成原子（14、0、16、2）也被识别为相关原子，与已知的 NANMA 异构化机制完全一致，验证了灵敏度分析的可靠性；

  
**3.速率常数与参考值吻合：**qGNN 计算得到的 NANMA 异构化跃迁速率常数为3.92×10−5ps−1，与参考值1.34×10−5ps−1处于同一数量级，偏差在合理范围内，证明了 qGNN 定量计算速率常数的能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/m3AVI6OFoUCjDTggROGx3RkWZNzicgkibTUmFxsWLagdlJx0IuTAuMmqp3LnzEa4vlWqjCibYlic7ibHAnpka4nhMO9y9a7d7axWK2K6oWIQT7Pk/640.png)

_图2\. N - 乙酰 - N'- 甲基丙氨酰胺的异构化_
  
  
**三丙氨酸构象平衡**

三丙氨酸的构象平衡涉及三个主链二面角ϕ1、ϕ2、ϕ3的协同变化，是典型的多自由度分子跃迁体系，传统方法需以这三个二面角为集体变量。qGNN 直接从重原子笛卡尔坐标学习承诺函数：

  
**1.承诺函数清晰区分亚稳态：**将承诺函数投影到(ϕ1,ϕ2)、(ϕ2,ϕ3)、(ϕ1,ϕ3)子空间，均能清晰识别出两个亚稳态 A 和 B 的盆域，分离线明确，证明 qGNN 能捕捉多自由度分子跃迁的核心动力学特征；

  
**2.关键二面角的精准识别：**节点灵敏度分析识别出的关键原子，恰好是定义ϕ1（6、8、10、16）、ϕ2（16、18、20、26）、ϕ3（26、29、30、36）的核心原子，与已发表的研究结果完全一致，证明 qGNN 能从高维原子坐标中提取出驱动跃迁的核心结构特征；

  
**3.速率常数计算可靠：**qGNN 计算的跃迁速率常数为5.60×10−5ps−1，与参考值3.62×10−5ps−1高度吻合，进一步验证了方法的定量性能。
  
  
**狄尔斯-阿尔德反应**

狄尔斯-阿尔德反应是有机化学中的经典 \[4+2\] 环加成反应，涉及新 C-C 键的形成，需量子化学处理，是化学反应体系的典型代表。qGNN 基于反应体系的原子笛卡尔坐标学习承诺函数：

  
**1.承诺函数捕捉反应进程：**将承诺函数投影到新形成的两个 C-C 键长(d1,d2)子空间，得到的承诺函数图与传统 CV-based ANN 方法的结果高度一致，分离线与理论预期的反应路径匹配，证明 qGNN 能适配化学反应的动力学特征；

  
**2.关键反应原子的精准定位：**节点灵敏度分析识别出参与新 C-C 键形成的四个核心原子（0、2、5、8），同时还识别出参与反应构型变化的原子 1 和 4（这些原子在反应物态形成 180° 角，产物态变为 120° 角），为理解狄尔斯 - 阿尔德反应的微观机制提供了新的定量依据；

  
**3.速率常数与量子化学计算一致：**由于该反应无实验速率常数，通过 Eyring 方程从耦合簇计算结果得到理论速率常数1.03×10−3ps−1，qGNN 计算值为1.33×10−3ps−1，二者高度吻合，证明 qGNN 可应用于有机化学反应的动力学研究。
  
  
**Trp-cage 可逆折叠**

Trp-cage 是由 20 个残基组成的迷你蛋白，其可逆折叠是蛋白折叠研究的经典模型，折叠时间约 14μs，是复杂生物分子体系的代表。本研究中，qGNN 分别基于Cα原子和全重原子的笛卡尔坐标学习承诺函数：

  
**1.无 CV 实现蛋白折叠承诺函数预测：**将承诺函数投影到 RMSD 和端到端距离子空间，能清晰区分折叠态（q=1）和去折叠态（q=0），并展现出明确的分离线，且基于Cα原子的结果与全重原子的结果高度一致，证明 qGNN 在蛋白体系中可通过粗粒化的原子坐标实现精准的承诺函数预测，大幅降低计算成本；

  
**2.蛋白折叠关键原子与结构的识别：**节点灵敏度分析识别出四个对 Trp-cage 折叠最关键的原子，基于这些原子的边灵敏度分析，进一步识别出三个物理上有意义的距离：端到端距离代理d1、螺旋延伸距离d2、蛋白双臂分离距离d3，其中d1和d2是描述折叠过程的最核心特征，为理解 Trp-cage 的折叠机制提供了全新的定量视角；

  
**3.过渡态集合的结构特征揭示：**对承诺函数在 0.45\~0.55 范围内的过渡态构象进行 K-means 聚类，识别出四个代表性的过渡态簇，所有过渡态均表现为7\~16 位残基的二级结构丢失，而蛋白两端的结构特征保持完整，这是对 Trp-cage 折叠过渡态结构的精准刻画，且该分析在全笛卡尔坐标空间完成，避免了集体变量降维带来的信息损失；

  
**4.速率常数与实验/模拟值吻合：**qGNN 计算的 Trp-cage 折叠速率常数为4.67×10−7ps−1，与已发表的参考值3.2×10−7ps−1和2.5×10−7ps−1高度吻合，证明 qGNN 可应用于蛋白折叠的定量研究。
  
  
**villin 折叠**

villin 是由 35 个残基组成的蛋白，包含 470 个重原子，其折叠过程的复杂度远高于 Trp-cage，是中大型蛋白体系的代表，用于验证 qGNN 的可扩展性：

  
**1.高维体系下的精准学习：**qGNN 基于 villin 的全重原子笛卡尔坐标，无需任何集体变量，成功学习到承诺函数，证明了架构在高维复杂分子体系中的可扩展性；

  
**2.速率常数计算准确：**qGNN 计算的 villin 折叠速率常数为5.88×10−7ps−1，与参考值3.57×10−7ps−1高度吻合，进一步验证了方法在复杂蛋白体系中的定量性能；

  
**3.原子级可解释性保持：**通过灵敏度分析，qGNN 成功识别出驱动 villin 折叠的关键原子和结构特征，为理解中大型蛋白的折叠机制提供了工具。
  
  
**各体系速率常数的综合对比**

将 qGNN 计算的所有体系的跃迁速率常数与已发表的参考值进行综合对比，结果如表1所示，所有体系的速率常数均与参考值处于同一数量级，且偏差在合理范围内，充分证明了 qGNN 定量计算分子跃迁速率常数的可靠性。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/m3AVI6OFoUD68OLhxEHrhb3M7DBxuwaHkXE49HD1jlOBtpeaAkV2yN4uMAfxg1Q0mQ21OICdDUD1ZFE6dGsb4zaqERLum2eYPQQHxMSXwuc/640.png)

_表1\. N - 乙酰 - N'- 甲基丙氨酰胺、三丙氨酸构象平衡、狄尔斯 - 阿尔德反应及 Trp-cage 蛋白可逆折叠的跃迁速率常数汇总_

  
1.qGNN 架构无需任何人工设计的集体变量，直接从原子笛卡尔坐标即可精准学习承诺函数，在从简单小分子到中大型蛋白的不同复杂度分子体系中均表现出优异的性能，证明了方法的普适性；

  
2.基于 GVP-GNN 的等变性设计，qGNN 能精准捕捉分子的空间结构和对称性特征，其预测的承诺函数与传统方法的结果高度吻合，证明了方法的准确性；

  
3.节点/边灵敏度分析能精准定位驱动分子跃迁的关键原子、二面角和键长，结果与已知的分子机制和物理直觉一致，实现了原子级的可解释性；

  
4.qGNN 计算的分子跃迁速率常数与已发表的实验/理论值高度吻合，证明了方法的定量性能；

  
5.qGNN 能在全笛卡尔坐标空间研究过渡态集合，结合聚类分析可揭示过渡态的结构特征，避免了集体变量降维带来的信息损失，为分子跃迁机制的研究提供了更全面的视角；

  
6.qGNN 架构具有高度的可扩展性，同一套架构仅需微调一个超参数，即可适配小分子、有机化学反应、蛋白折叠等不同类型的分子体系，且在包含 470 个重原子的 villin 蛋白中仍能高效学习。
  
  
**讨论与结论**

本文提出基于 GVP-GNN 架构的 qGNN 模型，可直接从原子坐标学习承诺函数，摆脱对人工预定义集体变量的依赖，精准捕捉分子系统动力学的空间与关系信息。团队在 NANMA 和三丙氨酸构象平衡、环己-1,2-二烯形成、Trp-笼微型蛋白可逆折叠这四个复杂度递增的原型分子过程的分子动力学模拟中验证模型性能，结果显示其推导的速率常数与已知实验/理论结论一致；且借助聚类分析，qGNN 能在笛卡尔全坐标空间研究转变系综结构，避免了基于集体变量降维带来的信息损失。此外，节点敏感性分析可精准识别分子转变的关键原子，为定义物理可解释的集体变量、解析分子机制提供重要依据。综上，该模型能从分子模拟中学习复杂动态特征，兼具通用性与可扩展性，是高维系统中反应坐标发现的实用工具。

  
该基于承诺函数的框架还可推广至多亚稳态系统，通过学习状态分辨的承诺函数，为构建马尔可夫状态模型奠定基础，实现慢动态过程、关键亚稳态等的系统表征。需说明的是，qGNN 虽解决了承诺函数学习对预定义集体变量的依赖，仍需依靠基于集体变量的增强采样完成罕见转变的详尽采样，未直接解决罕见事件采样的集体变量设计难题，但可通过其重现的承诺函数推断物理可解释的集体变量，或直接将承诺函数作为集体变量用于增强罕见事件采样。后续研究将延续人工神经网络相关方法的思路，实现从笛卡尔坐标直接学习承诺函数与转变路径，并整合至自适应采样、集体变量优化策略中。

  
**开源工具链接：**

**Zenodo 开源仓库：**

https://doi.org/10.5281/zenodo.18259668

**GitHub 仓库：**

https://github.com/Sergio-co/CommittorLearningGNN

  
往

期

文

章

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/m3AVI6OFoUBY9j2JDb63IfM4zy5PzeyggBqZogZs9Vw7ictqfanMficrdhlvKgFtBnqBV9tYtLohLicrVLHtg3ju02p03XcOaNINgE7sbPJGAo/640.gif)

  
[Nat.Commun.（IF=15.7）|加州理工AI设计新型TrpB酶，活性超实验室进化体，底物广谱性创天然酶未及水平](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzkzMzkxNjQ4Nw==&mid=2247493961&idx=1&sn=525c1835956392815d38bef386604e56&scene=21#wechat%5Fredirect)

[Nat.Commun.（IF=15.7）|香港科技大学联合浙江大学揭秘DNA双向调控凝缩蛋白 “安全带” 动力学，量化环挤压分子机制](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzkzMzkxNjQ4Nw==&mid=2247493960&idx=1&sn=6a93086fad16efab2bdb64d81a4c99b6&scene=21#wechat%5Fredirect)

[Adv.Sci.（IF=14.1）|清华大学团队AI定义蛋白词实现多功能预测，全数据集完胜经典工具PROSITE](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzkzMzkxNjQ4Nw==&mid=2247493926&idx=1&sn=35f2a5b4963b4177fed2bc7cf39091fe&scene=21#wechat%5Fredirect)

[JACS（IF=15.7）|台湾大学AI设计出“水装甲”蛋白，120°C不熔化、8M尿素不崩塌，70+残基替换仍超稳](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzkzMzkxNjQ4Nw==&mid=2247493925&idx=1&sn=4a411776f99ad629cfcf7b91f71b4290&scene=21#wechat%5Fredirect)

[Adv.Sci.（IF=14.1）|新加坡国立大学：AlphaFold+定向进化打造高性能紧凑碱基编辑器，编辑效率提升31倍、毒性降低10倍](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzkzMzkxNjQ4Nw==&mid=2247493924&idx=1&sn=f684295fc8305ee110df553dd954cdb4&scene=21#wechat%5Fredirect)

[Nat.Commun.（IF=15.7）|内华达大学算法突破：HIT-EC精准预测酶功能，F1分数高达0.93，远超现有方法](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzkzMzkxNjQ4Nw==&mid=2247493909&idx=1&sn=40984edb089e13524abf41d978c4506c&scene=21#wechat%5Fredirect)

[Nat.Biotechnol.（IF=41.7）|Profluent Bio 开发Protein2PAM模型，实现CRISPR-Cas PAM精准定制，切割率最高提升50倍](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzkzMzkxNjQ4Nw==&mid=2247493908&idx=1&sn=db1526e1e589167d910cad504a8ab68e&scene=21#wechat%5Fredirect)

  
\- end -

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/m3AVI6OFoUCib6CWk7h420QgR3l3ePeWxDGZZ3VDGlNdRCAic8ITdqDDyU5KVPYOgIiakAPd24IiaCAkEuANZWvx3VRjKLxq8ytqohibvPqS9BCw/640.gif)

点赞

收藏

分享

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/eICe20sr8SQOTh2upZibyunuxGuFxkfuH42hj0yOadQVAiaVfPuDHxcI9IVdcnOxbpKiatmORibMCKIKqyu672uJ1Q/0.png) 

 AI蛋白质前沿站 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/eICe20sr8SQOTh2upZibyunuxGuFxkfuH42hj0yOadQVAiaVfPuDHxcI9IVdcnOxbpKiatmORibMCKIKqyu672uJ1Q/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
