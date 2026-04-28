---
title: "Chipot_PPT深度原理拆解"
source: "https://poe.com/chat/7ihfw5poqzf4cwog28"
author:
published:
created: 2026-04-28
description: "在 Poe 上与最优秀的 AI 进行私聊或群聊。一站式探索 GPT-5、Claude-Sonnet-4.5、DeepSeek-R1、Veo-3.1、Sora-2 以及数千个其他AI模型。"
tags:
  - "clippings"
---
Claude Opus 4.6 是 Anthropic 最先进的人工智能模型，专为深度推理、复杂编程和长期自主任务而设计。它在规划、调试和处理大型代码库方面表现出色，并支持100万词元的上下文窗口以理解海量信息。作为专业知识工作的理想选择，它将最先进的性能与强大的安全性和可靠性完美结合。 此机器人支持可选参数以进行额外定制。

---

由 Anthropic: claude-opus-4-6 提供技术支持。 [了解更多](https://poe.com/privacy_center)

1. 官方

邀请他人加入此聊天

分享此链接以邀请他人。

4月13日

解读一下这个ppt，为我详细讲述每一页，要求从第一性原理出发解释，不要漏掉公式推导理论细节

11:35

Claude-Opus-4.6

解读一下这个ppt，为我详细讲述每一页，要求从第一性原理出发解释，不要漏掉公式推导理论细节

11:41

Claude-Opus-4.6

## 详细解读：从原子到路径——分子转变的机器学习视角（第2节：学习反应坐标）

这组幻灯片来自2026年4月13日在重庆举行的第35届中国化学会大会上的报告，演讲主题为"From atoms to pathways: A machine-learning perspective on molecular transitions"，演讲者来自CNRS/ERC资助的研究组。以下我从第一性原理出发，逐页详解。

---

## 第一页：标题页——"Learning the reaction coordinate"

这是第2节的标题页，核心问题是： **如何从分子模拟数据中学习到最优的反应坐标（reaction coordinate）？**

从第一性原理出发，理解这一问题的背景至关重要。考虑一个分子体系（例如蛋白质折叠、化学反应、构象变化），其完整的相空间维度极高（ $3N$ 个坐标加上 $3N$ 个动量， $N$ 为原子数）。体系从亚稳态 A 到亚稳态 B 的转变（如反应物→产物）发生在一个极高维的自由能曲面上。"反应坐标"是一个低维投影，它能够最好地描述从 A 到 B 转变的进展。寻找这样一个坐标在计算化学和统计力学中是一个核心挑战，因为一个不好的反应坐标会导致对机理的误判和对速率常数的错误估计。

这一节的目标正是利用机器学习（特别是神经网络）从分子动力学轨迹数据中自动学习最优反应坐标，其理论基础是 **承诺概率（committor probability）** 。

---

## 第二页：承诺概率（Commitment probability / Committor function）

### 物理概念

承诺概率 $q(\mathbf{z})$ 是过渡路径理论（Transition Path Theory, TPT）的核心概念。它定义为：从构型 $\mathbf{z}$ 出发的一条动力学轨迹， **先到达态 B 而非态 A 的概率** 。其边界条件为：

$$
q(\mathbf{z}) = 0, \quad \mathbf{z} \in A; \qquad q(\mathbf{z}) = 1, \quad \mathbf{z} \in B
$$

committor 被认为是理论上"完美的"反应坐标，因为 $q = 0.5$ 的等值面恰好定义了过渡态分隔面——从该面出发，体系有50%的概率前往A，50%的概率前往B。

右侧的示意图展示了一个二维自由能曲面（紫色凹凸曲面），上面标注了两个态A和B，以及从某构型 $\mathbf{z}$ 出发的多条轨迹（绿色）。在A处 $q(\mathbf{z})=0$ ，在B处 $q(\mathbf{z})=1$ ，中间区域 $q$ 连续变化。

### 公式推导：从路径求和到自洽方程

幻灯片的推导思路是从最基本的路径概率出发，通过逐步求和，推导出 committor 满足的自洽积分方程。

设 $\mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})$ 为在时间间隔 $\tau$ 内从构型 $\mathbf{z}$ 转移到 $\mathbf{z}'$ 的转移概率（transition probability），且定义多步传播算符的复合为 $\mathscr{P}_{n\tau} = \mathscr{P}_\tau \cdots \mathscr{P}_\tau$ （ $n$ 次复合）。

**第一种到达B的方式：一步到位。** 体系从 $\mathbf{z}$ 出发，一步之内就落入B：

$$
q(\mathbf{z}) = \int_{\in B} \mathrm{d}\mathbf{z}' \; \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})
$$

**第二种方式：先到中间区域，再一步到B。** 体系先跳到一个既不在A也不在B的中间状态 $\mathbf{z}'$ ，然后从 $\mathbf{z}'$ 一步跳到B：

$$
+ \int_{\notin A,B} \mathrm{d}\mathbf{z}' \int_{\in B} \mathrm{d}\mathbf{z}'' \; \mathscr{P}_\tau(\mathbf{z}''|\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})
$$

**第三种方式：两步中间过渡后到B：**

$$
+ \int_{\notin A,B} \mathrm{d}\mathbf{z}' \int_{\notin A,B} \mathrm{d}\mathbf{z}'' \int_{\in B} \mathrm{d}\mathbf{z}''' \; \mathscr{P}_\tau(\mathbf{z}'''|\mathbf{z}'') \, \mathscr{P}_\tau(\mathbf{z}''|\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})
$$

以此类推，无穷求和覆盖了所有可能的先到达B的路径。

关键的数学步骤是识别出递归结构。将上式整理，提取出关于第一步跳到 $\mathbf{z}'$ 的积分：

$$
q(\mathbf{z}) = \int_{\in B} \mathrm{d}\mathbf{z}' \; \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z}) + \int_{\notin A,B} \mathrm{d}\mathbf{z}' \left\{ \int_{\in B} \mathrm{d}\mathbf{z}'' \; \mathscr{P}_\tau(\mathbf{z}''|\mathbf{z}') + \int_{\notin A,B} \mathrm{d}\mathbf{z}'' \int_{\in B} \mathrm{d}\mathbf{z}''' \; \mathscr{P}_\tau(\mathbf{z}'''|\mathbf{z}'') \mathscr{P}_\tau(\mathbf{z}''|\mathbf{z}') + \cdots \right\} \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})
$$

大括号中的无穷级数正是 $q(\mathbf{z}')$ 的定义本身！因此：

$$
q(\mathbf{z}) = \int_{\in B} \mathrm{d}\mathbf{z}' \; \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z}) + \int_{\notin A,B} \mathrm{d}\mathbf{z}' \; q(\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})
$$

接下来，利用边界条件 $q(\mathbf{z}')=1$ 当 $\mathbf{z}' \in B$ 以及 $q(\mathbf{z}')=0$ 当 $\mathbf{z}' \in A$ ，第一项可以写成 $\int_{\in B} \mathrm{d}\mathbf{z}' \, q(\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})$ ，而A区域的贡献为零，因此可以将三个区域的积分合并：

$$
q(\mathbf{z}) = \int_{\in A} \mathrm{d}\mathbf{z}' \, q(\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z}) + \int_{\in B} \mathrm{d}\mathbf{z}' \, q(\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z}) + \int_{\notin A,B} \mathrm{d}\mathbf{z}' \, q(\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})
$$

最终得到优美的自洽方程：

$$
\boxed{q(\mathbf{z}) = \int \mathrm{d}\mathbf{z}' \; q(\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})}
$$

### 物理意义

这个方程表明： **committor 是转移算符的不动点** 。从任意构型 $\mathbf{z}$ 出发，经过一个时间步 $\tau$ 的传播后，committor 的期望值不变。用概率论的语言来说， $q$ 关于在A和B处吸收的动力学过程是一个 **调和函数（harmonic function）** ，也可以理解为关于吸收Markov链的一个鞅（martingale）。

这个性质在数学上等价于说 $q$ 满足带有吸收边界条件的 Fokker-Planck / Smoluchowski 方程的稳态解（在连续极限下即为 backward Kolmogorov 方程）。

参考文献包括Chandler (1978)、Berezhkovskii, Hummer, Szabo (2009)、Roux (2021, 2022) 等关于committor理论的经典和近期工作。

---

## 第三页：用偏置轨迹迭代学习——变分承诺概率网络（VCN）

### 核心思想

上一页推导出了committor满足的理论方程，但在高维体系中直接求解该方程是不可行的。这一页介绍的是如何用 **神经网络** 以 **变分方法** 从分子动力学轨迹数据中学习committor，核心方法称为 **VCN（Variational Committor Network）** 。

### 网络架构

左侧示意图展示了一个Siamese（孪生）网络结构。两个完全相同的神经网络 $F$ （共享权重）分别接收时间 $t$ 和 $t+\tau$ 的构型 $\mathbf{z}(t)$ 和 $\mathbf{z}(t+\tau)$ 作为输入，输出 $F(\mathbf{z}(t))$ 和 $F(\mathbf{z}(t+\tau))$ 。

committor 的估计量定义为：

$$
q(t) = \begin{cases} 0, & \mathbf{z}(t) \in A \\ 1, & \mathbf{z}(t) \in B \\ F(\mathbf{z}(t)), & \mathbf{z}(t) \notin (A \cup B) \end{cases}
$$

这样，边界条件被硬编码到了定义中，只需要在中间区域训练网络。

### 变分原理与损失函数

损失函数为：

$$
\mathscr{L}_q = 2\tau \, J_{AB} = \left\langle \left( q(\tau) - q(0) \right)^2 \right\rangle
$$

这个损失函数的物理含义可以从第一性原理理解如下。

由于真实的committor满足 $q(\mathbf{z}) = \int \mathrm{d}\mathbf{z}' \, q(\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})$ ，也就是 $\langle q(\tau) | \mathbf{z}(0) = \mathbf{z} \rangle = q(\mathbf{z})$ ，这意味着 $q(\tau) - q(0)$ 在给定 $\mathbf{z}(0)$ 时的条件期望为零。因此， $\langle (q(\tau) - q(0))^2 \rangle$ 就等于 $q(\tau) - q(0)$ 的方差，即随机波动的幅度。对于真实committor，这个量取到最小值（因为任何偏离真实committor的函数都会引入系统性的漂移，增大该方差）。

更准确地说，该损失函数与反应速率常数直接相关。最小值等于 $2\tau J_{AB}$ ，其中 $J_{AB}$ 是从A到B的稳态反应流（reactive flux）。这建立了学习committor与计算反应速率之间的直接联系。

这一变分原理的严格推导来自以下论证：定义时间相关函数 $C_{qq}(\tau) = \langle (q(\tau) - q(0))^2 \rangle$ ，其中平均是在平衡态分布上取的。可以展开：

$$
C_{qq}(\tau) = \langle q(\tau)^2 \rangle + \langle q(0)^2 \rangle - 2\langle q(\tau) q(0) \rangle = 2\langle q^2 \rangle - 2\langle q(\tau)q(0) \rangle
$$

利用转移算符的谱分解，可以证明当 $q$ 恰好是真实committor时， $C_{qq}(\tau)$ 在所有满足边界条件的函数中取最小值。

### 从偏置采样中学习

右侧还给出了从偏置轨迹中提取"进度指标" $s(\mathbf{z})$ 的公式：

$$
s(\mathbf{z}) = \lim_{\lambda \to \infty} \frac{\int_0^1 \mathrm{d}t \; t \; e^{-\lambda |\mathbf{z} - \mathbf{z}(t)|^2}}{\int_0^1 \mathrm{d}t \; e^{-\lambda |\mathbf{z} - \mathbf{z}(t)|^2}}
$$

这个表达式的含义是：给定一条（归一化到 $[0,1]$ 时间区间的）轨迹 $\mathbf{z}(t)$ ，对于任意构型 $\mathbf{z}$ ， $s(\mathbf{z})$ 计算的是轨迹上距离 $\mathbf{z}$ 最近的那个点所对应的时间。在 $\lambda \to \infty$ 的极限下，高斯权重 $e^{-\lambda|\mathbf{z}-\mathbf{z}(t)|^2}$ 变成一个δ函数，只选择轨迹上与 $\mathbf{z}$ 最近的时刻。因此， $s(\mathbf{z})$ 是沿偏置轨迹的"进度"，可作为学习committor的辅助特征。

### 关键优势

幻灯片列出的三个要点：（1）不需要aimless shooting，即不需要从每个构型发射大量短轨迹来统计估计committor；（2）可以从偏置采样（如metadynamics或eABF等增强采样方法）产生的轨迹中学习；（3）使用有限时间间隔 $\tau$ ，而非无穷长轨迹。

参考文献包括Strahan et al. JCTC 2021, Jung et al. Nature Comput. Sci. 2023, Chen, Roux, Chipot JCTC 2023 等。

---

## 第四页：评注1——从偏置轨迹中学习的理论基础

### 离散状态Markov模型的转移概率

这一页从第一性原理出发，严格推导了如何从偏置（biased）模拟中恢复无偏（unbiased）的时间相关函数。

首先考虑一个跳跃过程（jump-like process）的离散态Markov模型，其转移概率形式为：

$$
\mathscr{P}_\tau(\mathbf{z}'|\mathbf{z}) = \left( \tau \frac{D(\mathbf{z}) + D(\mathbf{z}')}{2(\Delta z)^2} \right) e^{-\beta[w(\mathbf{z}') - w(\mathbf{z})]/2}
$$

这个表达式来源于对过阻尼Langevin动力学（Smoluchowski方程）的空间离散化。这里 $D(\mathbf{z})$ 是位置依赖的扩散系数， $w(\mathbf{z})$ 是平均力势（PMF, potential of mean force）， $\beta = 1/(k_BT)$ 是逆温度， $\Delta z$ 是空间网格间距。

指数因子 $e^{-\beta[w(\mathbf{z}')-w(\mathbf{z})]/2}$ 体现了\*\*细致平衡（detailed balance）\*\*条件的对称形式。这个"半-半"的划分（一半给起点，一半给终点）使得转移概率可以分解为：

$$
\mathscr{P}_\tau(\mathbf{z}'|\mathbf{z}) = e^{-\beta w(\mathbf{z}')/2} \left( \tau \frac{D(\mathbf{z}) + D(\mathbf{z}')}{2(\Delta z)^2} \right) e^{+\beta w(\mathbf{z})/2}
$$

这种分解的意义在于将转移概率写成了一个对称矩阵 $K(\mathbf{z},\mathbf{z}') = \tau[D(\mathbf{z})+D(\mathbf{z}')]/(2\Delta z^2)$ 夹在两个 Boltzmann 因子之间的形式，这正是满足细致平衡的标准结构。

### 偏置势对转移概率的影响

当我们在系统中施加一个额外的偏置势 $\delta w(\mathbf{z})$ （例如来自metadynamics或eABF），系统感受到的有效势变为 $w(\mathbf{z}) + \delta w(\mathbf{z})$ 。将上面的表达式中的 $w$ 替换为 $w + \delta w$ ，得到偏置系统的转移概率：

$$
\mathscr{P}_\tau^{(\text{pert})}(\mathbf{z}'|\mathbf{z}) = e^{-\beta \delta w(\mathbf{z}')/2} \; \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z}) \; e^{+\beta \delta w(\mathbf{z})/2}
$$

这个关系非常重要： **偏置系统的转移概率可以表示为原始转移概率乘以起点和终点上与偏置势相关的指数修正因子** 。

### 重加权恢复无偏时间相关函数

幻灯片的最后部分给出了核心的重加权公式。无偏系统中的时间相关函数 $\langle f(\tau) \, g(0) \rangle$ 可以从偏置系统的模拟中通过重加权来计算：

$$
\langle f(\tau) \, g(0) \rangle = \langle e^{+\beta \delta w} \rangle_{(\text{pert})}^{-1} \left\langle f(\tau) \, e^{+\beta \delta w(\tau)/2} \, g(0) \, e^{+\beta \delta w(0)/2} \right\rangle_{(\text{pert})}
$$

推导思路是这样的：无偏系统中两个时间点的联合概率密度为 $\rho(\mathbf{z}_0) \mathscr{P}_\tau(\mathbf{z}_\tau|\mathbf{z}_0)$ ，而偏置系统中为 $\rho^{(\text{pert})}(\mathbf{z}_0) \mathscr{P}_\tau^{(\text{pert})}(\mathbf{z}_\tau|\mathbf{z}_0)$ 。利用上面导出的 $\mathscr{P}_\tau^{(\text{pert})}$ 与 $\mathscr{P}_\tau$ 的关系，以及平衡态分布的变化 $\rho^{(\text{pert})}(\mathbf{z}) \propto \rho(\mathbf{z}) e^{-\beta \delta w(\mathbf{z})}$ ，可以将无偏平均改写为偏置平均加上适当的重加权因子。

右侧的图是一个一维双势阱的验证。图中展示了三条committor曲线：黑色线是无偏模拟的结果，红色线是偏置模拟加重加权（RW）的结果，绿色线是偏置模拟不加重加权的结果。黑色和红色曲线完美重合，证明了重加权公式的正确性；而绿色曲线明显偏离，说明如果不做重加权，偏置轨迹给出的committor是错误的。

参考文献包括Bicout & Szabo (1998)、Schumaker, Pomès, Roux (2001)、Rydzewski & Valsson (2021)、Wang & Tiwary (2020)、Keller & Bolhuis (2024)。

---

## 第五页：评注2——从无目标发射（aimless shooting）中学习

### 背景

Aimless shooting是过渡路径采样（Transition Path Sampling, TPS）中的一种技术。其基本思想是：从一条已知的反应性轨迹上随机选一个构型，赋予随机的初始速度，向前和向后各发射一条轨迹。如果新轨迹仍然连接A和B（一端到A，一端到B），则被接受为一条新的过渡路径。通过统计每个构型的轨迹有多少比例到达B，可以直接估计该构型的committor值。

### 幻灯片内容

这一页比较了对NANMA（一种小的丙氨酸二肽衍生物）分子的committor map，在Ramachandran图的 $(\phi, \psi)$ 二面角空间中展示：

左图是通过传统的aimless shooting方法获得的committor map。具体做法是：从1,000个构型中的每一个，以随机初始速度发射10条独立轨迹，统计到达B的比例，然后用样条插值平滑。

右图是VCN方法从偏置轨迹中学习到的committor map。

颜色编码从蓝色（ $q=0$ ，态A）到红色（ $q=1$ ，态B），等高线叠加了自由能的等值线。

**核心结论是两种方法给出了等价的committor map** 。这验证了VCN方法的可靠性，同时VCN的计算效率远高于aimless shooting（后者需要从大量构型各发射多条轨迹，计算量巨大）。

从等高线的形态可以看出，committor的变化主要沿φ方向，而ψ方向的贡献相对较小（等高线近似平行于ψ轴），这暗示对于NANMA的这个构象转变，φ是主导的反应坐标。

参考文献包括Bolhuis, Chandler, Dellago, Geissler (Ann. Rev. Phys. Chem. 2002) 和 Swenson, Prinz, Noé, Chodera, Bolhuis (JCTC 2019) 等TPS领域的经典文献。

---

## 第六页：评注3——数据驱动的速率常数确定

### 核心问题

一旦学习到了committor，能否从中提取体系的 **反应速率常数** $k_{AB}$ ？这是这一页要回答的问题。速率常数是实验上可测量的最核心的动力学量之一。

### 方法比较

表格比较了以下方法在不同模型势上得到的 $k_{AB}$ （单位 $\text{ps}^{-1}$ ）：

**MFPT（Mean First Passage Time，平均首达时间）** ：这是最直接的参考方法。对于一维问题，Kramers理论给出 $k_{AB} = 1/\langle t_{\text{FP}} \rangle$ 。对于更复杂的情况，可以从长时间无偏模拟中直接计算。

**SRVs（Slow Reversible Variables / state-free reversible VAMPnets）** ：这是另一种机器学习方法，通过学习最慢的可逆动力学模式来确定速率。分别在无偏和偏置轨迹上训练。

**VCNs（Variational Committor Networks）** ：本讲座介绍的方法，同样分别在无偏和偏置轨迹上训练。

测试的模型体系包括一维双势阱（Double-well 1D）、二维Müller-Brown势（2D MB）、二维Berezhkovskii-Szabo势（2D BS，分别在摩擦比 $\gamma_x/\gamma_y = 0.1, 1.0, 10.0$ 下测试），以及NANMA分子。

高亮行（2D BS, $\gamma_x/\gamma_y = 1.0$ ）显示所有方法的结果高度一致，MFPT给出 $1.07 \times 10^{-2}$ ，SRV无偏给出 $1.18 \times 10^{-2}$ ，VCN无偏给出 $1.02 \times 10^{-2}$ 。

### 速率常数的提取方法

底部的四幅图展示了速率常数的具体提取方式。左侧两幅是无偏轨迹的结果，右侧两幅是偏置轨迹（WTM-eABF）的结果。

对于左边的无偏轨迹：

- 第一幅图画的是 $-\ln \hat{\lambda}(\tau)$ 对时间间隔 $\tau$ 的函数图，其中 $\hat{\lambda}(\tau)$ 来自SRV方法的自相关函数。在 $\tau$ 足够大时，这个函数呈线性增长，其斜率就是最慢弛豫速率 $k_1$ ，对于双态体系即等于 $k_{AB} + k_{BA} \approx k_{AB}$ （若两态不对称）或 $2k_{AB}$ （若对称）。图中提取的速率为 $k_{AB} = 1.18 \times 10^{-2} \, \text{ps}^{-1}$ 。
- 第二幅图画的是 $C_{qq}(\tau) = \langle (q(\tau) - q(0))^2 \rangle$ ，即VCN损失函数中的核心量。这个量在小 $\tau$ 时线性增长，斜率等于 $2 J_{AB}$ ，而 $J_{AB}$ 与速率常数的关系为 $k_{AB} = J_{AB} / \rho_A$ （其中 $\rho_A$ 是在A态的平衡占据概率）。图中提取的速率为 $k_{AB} = 1.02 \times 10^{-2} \, \text{ps}^{-1}$ 。

对于右边的偏置轨迹：

- 同样的分析，但使用了重加权（上一页推导的公式）来修正偏置效应。偏置轨迹的时间尺度被压缩（因为增强采样加速了罕见事件），但通过正确的重加权，仍然可以提取出正确的无偏速率常数。结果分别为 $k_{AB} = 1.95 \times 10^{-2}$ 和 $1.76 \times 10^{-2} \, \text{ps}^{-1}$ ，与无偏结果在数量级上一致（有一定偏差，这在偏置采样的重加权中是预期的统计波动）。

参考文献为Chen, Roux, Chipot, J. Chem. Theory Comput. 2023, 19, 14, 4414-4426。

---

## 总结

整个第2节的逻辑链条非常清晰：

**理论基础（第2页）** ：从路径概率的逐项求和出发，严格推导出committor满足的自洽积分方程 $q(\mathbf{z}) = \int \mathrm{d}\mathbf{z}' \, q(\mathbf{z}') \, \mathscr{P}_\tau(\mathbf{z}'|\mathbf{z})$ ，这是转移算符的不动点条件。

**计算方法（第3页）** ：将committor参数化为神经网络，利用变分原理（最小化 $\langle (q(\tau)-q(0))^2 \rangle$ ）从轨迹数据中学习，无需传统的aimless shooting。

**偏置校正（第4页）** ：从Smoluchowski方程的离散化出发，推导出偏置势如何影响转移概率，给出了从偏置模拟中恢复无偏时间相关函数的严格重加权公式。

**方法验证（第5页）** ：在NANMA分子上，VCN得到的committor map与传统aimless shooting完全一致。

**应用（第6页）** ：从学习到的committor中提取反应速率常数，在多种模型体系上与参考值吻合，证明了方法的定量可靠性。

这是一个从基础理论到实际应用的完整框架，将统计力学的严格理论（committor、转移算符、细致平衡）与现代机器学习工具（神经网络、变分优化）有机结合。

11:41

解读一下这个ppt，为我详细讲述每一页，要求从第一性原理出发解释，不要漏掉公式推导理论细节[Chipot\_5.pdf](https://pfst.cf2.poecdn.net/base/application/853a5c770428a913de88e79f168393ae59ab6313d20ff174b803facc5b7103c9?pmaid=603420158)

[

PDF · 5 MB

](https://pfst.cf2.poecdn.net/base/application/853a5c770428a913de88e79f168393ae59ab6313d20ff174b803facc5b7103c9?pmaid=603420158)

11:53

Claude-Opus-4.6

## 详细解读：第5节——超越增强采样（Beyond Enhanced Sampling）

这是同一报告的第5节，标志着方法论的重大飞跃：从传统的增强采样技术（如metadynamics、eABF等）转向利用 **生成式AI模型** （特别是扩散模型）来探索分子转变。以下逐页从第一性原理详解。

---

## 第一页：标题页——"Beyond enhanced sampling"

### 背景与动机

传统的增强采样方法（如第2节讨论的WTM-eABF、metadynamics等）已经在学习反应坐标和采样罕见事件方面取得了巨大成功，但它们有根本性的局限：需要预先选择集体变量（collective variables, CVs），采样效率随体系维度的增加急剧下降，对于蛋白质折叠这样涉及数千个原子的问题，传统增强采样可能需要极长的模拟时间。

"Beyond enhanced sampling"的意思是：能否利用机器学习生成模型， **绕过传统增强采样中对长时间分子动力学轨迹的依赖** ，直接从已知的端态结构（如蛋白质的折叠态和去折叠态）生成中间过渡态结构？这将彻底改变研究分子转变的范式。

---

## 第二页：扩散模型——前向扩散过程

### 扩散模型的第一性原理

扩散模型（Diffusion Models）是一类基于随机微分方程（SDE）的生成模型，其理论根基在非平衡统计力学中。核心思想极其优雅：先将数据逐步"毁坏"为噪声（前向过程），然后学习如何将噪声逐步"还原"为数据（反向过程）。

### 前向扩散（Forward diffusion）

幻灯片展示了前向扩散的链式结构：

$$
\mathbf{x}_0 \to \cdots \to \mathbf{x}_{t-1} \xrightarrow{q(\mathbf{x}_t|\mathbf{x}_{t-1})} \mathbf{x}_t \to \cdots \to \mathbf{x}_T
$$

其中 $\mathbf{x}_0$ 是原始数据（图中以人脸照片为例）， $\mathbf{x}_T$ 是纯噪声。每一步通过条件分布 $q(\mathbf{x}_t|\mathbf{x}_{t-1})$ 向数据中添加少量噪声。

这个过程可以用连续时间的随机微分方程（SDE）描述：

$$
\mathrm{d}\mathbf{x} = \mathbf{f}(\mathbf{x}, t)\,\mathrm{d}t + g(t)\,\mathrm{d}\mathbf{W}
$$

从第一性原理解释这个方程的每个组成部分：

**$\mathbf{f}(\mathbf{x}, t)$ 是漂移项（drift term）。** 在前向扩散过程中，它控制数据如何系统性地向某个参考分布（通常是零均值的高斯分布）移动。在最简单的情况（如VP-SDE，即Variance Preserving SDE）， $\mathbf{f}(\mathbf{x},t) = -\frac{1}{2}\beta(t)\mathbf{x}$ ，其中 $\beta(t)$ 是时间依赖的噪声调度（noise schedule），它的作用是使信号逐渐衰减。

**$g(t)$ 是扩散系数（diffusion coefficient）。** 它控制随机噪声的强度。在VP-SDE中， $g(t) = \sqrt{\beta(t)}$ 。

**$\mathrm{d}\mathbf{W}$ 是维纳过程（Wiener process）的增量。** 这是标准布朗运动的数学表达，满足 $\mathrm{d}\mathbf{W} \sim \mathcal{N}(\mathbf{0}, \mathrm{d}t \cdot \mathbf{I})$ 。在物理上，这对应于热涨落。

这个SDE与分子动力学中的过阻尼Langevin方程形式完全一致——这正是扩散模型与统计力学之间的深刻联系。在Langevin动力学中， $\mathbf{f}$ 对应于外力和摩擦力， $g$ 对应于热噪声的振幅，而涨落-耗散定理（fluctuation-dissipation theorem）将它们联系起来。

### 与统计力学的对应

在统计力学的语言中，前向扩散过程等价于一个粒子在逐渐变浅的势阱中做Langevin运动——势阱越来越浅，热噪声的影响越来越大，最终粒子的位置分布趋向于高斯白噪声。对应到数据空间：数据的结构性信息逐渐被噪声淹没。

在 $t=0$ 时， $\mathbf{x}_0$ 从数据分布 $p_{\text{data}}(\mathbf{x})$ 中采样；在 $t=T$ 时， $\mathbf{x}_T$ 近似服从一个简单的先验分布 $\pi(\mathbf{x}) \approx \mathcal{N}(\mathbf{0}, \mathbf{I})$ 。

参考文献包括Ho, Jain, Abbeel (NeurIPS 2020，DDPM的开创性论文)、Song, Meng, Ermon (ICLR 2021，Score-based SDE框架)、Anderson (1982，时间反转SDE的数学基础)。

---

## 第三页：扩散模型——反向扩散与去噪

这一页是扩散模型的数学核心，展示了前向和反向过程的完整对称性，以及去噪扩散概率模型（DDPM）的具体参数化。

### 前向过程（复述）

$$
\mathrm{d}\mathbf{x} = \mathbf{f}(\mathbf{x}, t)\,\mathrm{d}t + g(t)\,\mathrm{d}\mathbf{W}
$$

从 $\mathbf{x}_0$ （清晰数据）到 $\mathbf{x}_T$ （纯噪声）。

### 反向扩散（Reverse diffusion）——Anderson定理

这是最关键的数学结果。Anderson (1982) 证明了一个深刻的定理： **任何前向SDE的时间反转过程也是一个SDE** ，其形式为：

$$
\mathrm{d}\mathbf{x} = \left[\mathbf{f}(\mathbf{x}, t) - g^2(t) \, \nabla_{\mathbf{x}} \log p_t(\mathbf{x})\right] \mathrm{d}t + g(t)\,\mathrm{d}\bar{\mathbf{W}}
$$

其中 $\mathrm{d}\bar{\mathbf{W}}$ 是反向时间的维纳过程增量， $p_t(\mathbf{x})$ 是前向过程在时刻 $t$ 的边际概率密度。

**幻灯片中用红色方框特别标注了 $\nabla_{\mathbf{x}} \log p_t(\mathbf{x})$ ，这就是所谓的"分数函数"（score function）。**

从第一性原理理解反向SDE的推导。考虑前向SDE对应的Fokker-Planck方程（描述概率密度 $p_t(\mathbf{x})$ 的演化）：

$$
\frac{\partial p_t}{\partial t} = -\nabla \cdot [\mathbf{f} \, p_t] + \frac{g^2}{2} \nabla^2 p_t
$$

这是一个连续性方程，右边第一项是概率流的对流项，第二项是扩散项。

要构造从 $t=T$ 到 $t=0$ 的反向过程，我们需要找到一个新的SDE，使得其Fokker-Planck方程的解 $\tilde{p}_{T-t}$ 恰好等于原过程的 $p_t$ 。通过要求反向过程的概率流与前向过程的概率流在时间反转下一致，可以严格推导出上面的反向SDE。关键在于扩散项产生了一个额外的"分数力" $-g^2 \nabla \log p_t$ ，它驱动系统从高噪声区域向高概率密度区域移动——这正是"去噪"的物理机制。

### 分数函数的物理意义

$\nabla_{\mathbf{x}} \log p_t(\mathbf{x})$ 的物理意义非常直观：它是概率密度对数的梯度，指向概率增加最快的方向。在统计力学中，如果 $p_t(\mathbf{x}) \propto e^{-\beta U(\mathbf{x})}$ ，则 $\nabla \log p_t = -\beta \nabla U$ ，即负的力场梯度。因此，分数函数扮演的角色等价于一个"有效力"，将系统从噪声状态拉回到数据分布。

### 去噪扩散概率模型（DDPM）的具体参数化

幻灯片给出了离散时间版本的具体分布形式：

**前向过程（加噪声）：**

$$
q(\mathbf{x}_t|\mathbf{x}_{t-1}) = \mathcal{N}\left(\mathbf{x}_t; \underbrace{(1-\beta_t)^{1/2}\,\mathbf{x}_{t-1}}_{\mu_t}, \beta_t \mathbf{1}\right)
$$

这是一个高斯条件分布。均值为 $(1-\beta_t)^{1/2}\,\mathbf{x}_{t-1}$ ——信号被缩放了 $(1-\beta_t)^{1/2}$ 倍（略小于1，信号衰减）；方差为 $\beta_t$ （添加的噪声量）。当 $\beta_t$ 很小时，每步添加的噪声很少，但经过 $T$ 步后，累积效应使得 $\mathbf{x}_T \approx \mathcal{N}(\mathbf{0}, \mathbf{I})$ 。

可以验证，这个参数化保持了总方差的稳定性：如果 $\mathbf{x}_{t-1}$ 的方差已经是1，则 $\mathbf{x}_t$ 的方差也是 $(1-\beta_t) \cdot 1 + \beta_t = 1$ ，这就是"Variance Preserving"的含义。

**反向过程（去噪声）：**

$$
p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t) = \mathcal{N}\left(\mathbf{x}_{t-1}; \boldsymbol{\mu}_\theta(\mathbf{x}_t, t); \boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t)\right)
$$

这也是一个高斯分布，但其均值 $\boldsymbol{\mu}_\theta$ 和协方差 $\boldsymbol{\Sigma}_\theta$ 由参数为 $\theta$ 的 **神经网络** 来预测。训练的目标是使反向过程生成的分布尽可能接近前向过程的真实后验 $q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0)$ 。

实践中，Ho et al. (2020) 证明，最优的 $\boldsymbol{\mu}_\theta$ 可以参数化为对噪声的预测：训练一个神经网络 $\boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)$ 来预测在第 $t$ 步添加的噪声 $\boldsymbol{\epsilon}$ ，损失函数为简单的均方误差：

$$
L = \mathbb{E}_{t, \mathbf{x}_0, \boldsymbol{\epsilon}} \left[ \|\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\|^2 \right]
$$

这与分数匹配（score matching）在数学上是等价的，因为 $\nabla_{\mathbf{x}_t} \log q(\mathbf{x}_t|\mathbf{x}_0) = -\boldsymbol{\epsilon}/\sqrt{1-\bar{\alpha}_t}$ （其中 $\bar{\alpha}_t = \prod_{s=1}^t (1-\beta_s)$ ）。

### 右侧示意图

右下角的示意图展示了去噪过程：从纯噪声图像出发，每一步应用学习到的去噪函数（score function），逐渐恢复出清晰的人脸图像。底部的小图展示了概率密度函数和score function的关系——score function在概率峰值处为零（无净力），在两侧指向峰值（恢复力）。

左侧展示了生成的人脸图像矩阵，展示了模型的多样性——每张脸都是从噪声中生成的不同样本。

---

## 第四页：扩散模型用于分子过渡——Gen-COMPAS流程

这是本节的核心页面，展示了如何将扩散模型从图像生成领域 **迁移到分子科学** ，具体实现为 **Gen-COMPAS** （Generative COMmittor-guided PAssage Sampling）框架。

### 完整流程（7步）

**步骤1：从A和B端态进行短时间模拟。**

起点是两个已知的亚稳态结构A和B（例如蛋白质的折叠态和去折叠态）。对每个态进行短时间的常规分子动力学模拟（短到不需要跨过能垒），收集A和B附近的构型样本。这些样本代表了"数据"——我们已知的状态。

**步骤2：训练扩散模型。**

利用步骤1中收集的A和B态的结构样本，训练一个扩散模型。这里的关键创新是：在传统的图像扩散模型中，前向过程将数据扩散到高斯噪声；而在Gen-COMPAS中，扩散过程被设计为 **在A和B之间进行插值** ，即前向过程不是"数据→噪声"而是"A态→B态"（或反之）。

更具体地说，可以将前向过程理解为一个条件化的扩散桥（diffusion bridge），它从态A出发，经过中间步骤，到达态B。训练数据只需要A和B的样本，模型自动学习A和B之间的"最可能的插值路径"。

**步骤3：聚类，识别质心和离群点。**

对步骤2中生成的中间结构进行聚类分析（例如用k-means或DBSCAN），找到代表性的质心结构（centroids）和离群点（outliers）。质心代表最可能的中间态，离群点代表非典型但可能重要的构型。

**步骤4：从质心和离群点出发进行短时间模拟。**

对步骤3中识别出的代表性结构，再次进行短时间MD模拟。这些模拟产生中间区域的局部采样数据，用于后续的committor学习。

**步骤5：训练VCN，识别分隔面。**

利用步骤4生成的轨迹数据，训练第2节介绍的变分承诺概率网络（VCN）。VCN学习到committor函数 $q(\mathbf{z})$ ， $q=0.5$ 的等值面即为过渡态分隔面（separatrix）。

同时，可以进一步训练扩散模型来生成committor值接近0.5的结构——这些就是过渡态结构。

**步骤6：筛选罕见事件过渡态。**

利用学习到的committor对生成的结构进行筛选，选择 $q \approx 0.5$ 的结构作为候选过渡态。图中用红-蓝颜色编码的committor图展示了这一筛选过程。

**步骤7：从过渡态出发进行短时间模拟。**

从筛选出的过渡态结构出发，发射短时间MD轨迹。由于起点已经在能垒顶部（ $q \approx 0.5$ ），这些轨迹会自然地"滑落"到A或B态，从而获得完整的反应路径——无需任何增强采样！

### 底部附注

**Generative process / Generation of intermediates：** 左下角的示意图展示了扩散模型如何在内部表示空间中生成从A到B的中间结构，底部的曲线暗示生成的结构覆盖了自由能面上A和B之间的整个区域。

**Transition states / TMD：** 中下角展示了过渡态的物理意义——TMD（Targeted Molecular Dynamics）是一种传统方法，强制系统沿某个集体变量从一个态拉向另一个态。但TMD生成的路径往往不物理（因为外力太大）。Gen-COMPAS的优势在于它从扩散模型生成的候选结构出发，通过短时间无偏MD验证物理可行性，确保过渡态结构是"physically meaningful structures"。

**Sampling strategy：** 右下角展示了采样策略——在 $q \approx 0.5$ 的分隔面附近集中采样，这是最高效的策略，因为这是A和B之间的瓶颈区域。

参考文献包括Lewis et al. (Science 2025, 389, eadv0617)——这是2025年发表在Science上的突破性工作，以及Tang, Pandey, Chen, Mégias, Dehez, Chipot (2025, arXiv:2510.24979)——Gen-COMPAS的原始论文。Vaswani et al. 2017 (arXiv:1706.03762) 引用的是Transformer架构的原始论文（"Attention is all you need"），暗示Gen-COMPAS的扩散模型可能使用了基于Transformer的架构。

---

## 第五页：Gen-COMPAS应用于蛋白质折叠——与D.E. Shaw的208微秒模拟对比

这是整个报告中最具说服力的应用展示页。

### 研究体系

研究对象是一个小型快速折叠蛋白。左上角展示了四种关键构象：折叠态（folded, f，蓝色，含α-螺旋结构），两个过渡态（transition state 1, ts1，橙色；transition state 2, ts2，红色），以及去折叠态（unfolded, u，浅蓝色，柔性链）。其中 $d$ 标注的是某个关键距离（可能是端到端距离或某对接触的距离）。

这是Lindorff-Larsen, Piana, Dror, Shaw (Science 2011, 334, 517-520) 经典研究的体系——Shaw研究组在专用超级计算机Anton上用了 **208微秒** 的连续MD模拟来观察蛋白质的多次折叠-去折叠事件。

### 路径分析

**左下角的两幅图：** 展示了沿两条不同反应路径（path 1和path 2）的归一化集体变量值。横轴是路径坐标（0到1），纵轴是归一化的CV值。图中包括committor $q$ （青色）、RMSD $_{C\alpha}$ （红色）、RMSD $_{helix}$ （橙色）等。

Path 1的特征是： $q$ 的变化（即真正的反应进展）与RMSD $_{C\alpha}$ 的变化几乎同步，且过渡态ts1的结构特征是螺旋性部分保留但整体结构开始崩溃。

Path 2的特征不同：过渡态ts2的结构特征是螺旋性先丧失，然后整体结构才发生变化。这意味着蛋白质折叠存在 **多条不同的路径** ，对应不同的过渡态。

### 中间面板：Committor映射

中间的几幅密度图展示了在不同集体变量组合下的committor分布。用RMSD $_{C\alpha}$ 和 RMSD $_{helix}$ 作为横纵坐标，颜色编码为committor值（深蓝=0，接近A态；亮色=1，接近B态）。

上面的图（标注path 1）显示了一条路径主要沿RMSD $_{C\alpha}$ 方向穿越。

中间的图（标注path 2）显示了另一条路径，其committor变化与 $d$ （端到端距离）和RMSD $_{C\alpha}$ 的关系。

下面的图展示了在RMSD $_{helix}$ vs $d$ 空间中两条路径的不同轨迹。

这些图揭示了折叠机理的 **多途径性（multi-pathway nature）** ——不同的路径经过不同的过渡态鞍点。

### 右侧面板：与DESRES（Shaw）数据的对比

这是最核心的验证。右侧展示了两列对比：

**Gen-COMPAS（0.6 μs）** vs **DESRES（208 μs）**

Gen-COMPAS只使用了 **0.6微秒** 的总模拟时间（包括端态短模拟和过渡态短模拟），而DESRES使用了 **208微秒** ——两者相差约350倍！

对比的是在多个集体变量组合（如RMSD $_{C\alpha}$ vs RMSD $_{helix}$ 、 $d$ vs RMSD $_{C\alpha}$ 、 $d$ vs RMSD $_{helix}$ 等）下的自由能面（用等高线或颜色编码的自由能图表示）。Gen-COMPAS的结果中能清晰地看到折叠态（f）、去折叠态（u）和过渡态（ts1、ts2）的标注。

结论是： **Gen-COMPAS在仅用0.6微秒的情况下，重现了Shaw研究组208微秒暴力模拟得到的自由能面的所有关键特征** ，包括：两个稳定态的位置和相对深度、过渡态的位置、两条反应路径的存在。

### 方法论的第一性原理解释

为什么Gen-COMPAS能如此高效？原因在于它巧妙地结合了多个层次的信息：

首先，扩散模型作为生成模型， **利用了端态结构的全局信息** 来推断中间态的结构特征。这类似于在高维空间中做"智能插值"，而非在构型空间中盲目搜索。

其次，VCN学习到的committor提供了 **最优的反应坐标** ，使得过渡态的识别（ $q \approx 0.5$ ）不依赖于直觉选择的集体变量。

最后，从正确识别的过渡态出发发射短时间MD轨迹， **利用了自然动力学来"下坡"** ——过渡态位于自由能鞍点上，轨迹自然会快速到达A或B态，无需额外的偏置力或增强采样。

整个策略的本质是： **用生成模型解决"在哪里采样"的问题，用物理模拟解决"如何验证物理可行性"的问题** 。

参考文献再次确认了Tang, Pandey, Chen, Mégias, Dehez, Chipot (2025, arXiv:2510.24979)。

---

## 总结

第5节的逻辑链条：

**动机（第1页）** ：传统增强采样有维度诅咒和CV选择的困难，需要新的范式。

**工具（第2-3页）** ：扩散模型提供了一个从第一性原理（随机微分方程、Fokker-Planck方程、Anderson时间反转定理）出发的生成框架。前向过程通过SDE将数据扩散为噪声，反向过程通过学习分数函数 $\nabla \log p_t$ 将噪声恢复为数据。这与统计力学中的Langevin动力学在数学结构上完全同构。

**应用框架（第4页）** ：Gen-COMPAS将扩散模型与VCN结合，形成7步流程：端态采样→训练扩散模型→生成中间结构→聚类→短时间MD→训练VCN识别过渡态→从过渡态发射轨迹。

**验证（第5页）** ：在蛋白质折叠问题上，Gen-COMPAS用0.6微秒的计算量重现了Shaw研究组208微秒暴力模拟的结果，不仅找到了正确的自由能面，还识别出了多条折叠路径和对应的不同过渡态结构。

这标志着分子模拟领域从"力的驱动"向"数据+物理联合驱动"的范式转变。扩散模型不替代物理模拟，而是极大地提高了模拟的效率——它告诉我们应该在构型空间的什么位置进行模拟，从而避免了在已知区域的无效采样。

11:53

还是有点不懂 从第一性原理推导所有涉及的公式，并给出这个模型的计算流程。

15:01

Claude-Opus-4.6

## 从第一性原理推导扩散模型与Gen-COMPAS的全部数学框架

---

## 第一部分：随机过程的数学基础

### 1.1 布朗运动（Wiener过程）

一切的起点是布朗运动。设 $\mathbf{W}(t) \in \mathbb{R}^d$ 是一个 $d$ 维标准维纳过程，它满足以下性质：

$\mathbf{W}(0) = \mathbf{0}$ ；增量 $\mathbf{W}(t) - \mathbf{W}(s)$ 对于 $t > s$ 服从 $\mathcal{N}(\mathbf{0}, (t-s)\mathbf{I})$ ；不同时间区间的增量相互独立。

在无穷小时间间隔 $\mathrm{d}t$ 内，增量 $\mathrm{d}\mathbf{W} = \mathbf{W}(t+\mathrm{d}t) - \mathbf{W}(t)$ 满足：

$$
\mathrm{d}\mathbf{W} \sim \mathcal{N}(\mathbf{0}, \mathrm{d}t \cdot \mathbf{I})
$$

即 $\mathrm{d}\mathbf{W} = \boldsymbol{\xi}(t)\sqrt{\mathrm{d}t}$ ，其中 $\boldsymbol{\xi}(t) \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 。

### 1.2 Itô随机微分方程

一般的Itô SDE定义为：

$$
\mathrm{d}\mathbf{x} = \mathbf{f}(\mathbf{x}, t)\,\mathrm{d}t + \mathbf{G}(\mathbf{x}, t)\,\mathrm{d}\mathbf{W}
$$

其中 $\mathbf{f}(\mathbf{x},t)$ 称为漂移系数（drift）， $\mathbf{G}(\mathbf{x},t)$ 称为扩散矩阵（diffusion matrix）。在本报告讨论的扩散模型中，扩散矩阵简化为标量函数乘以单位矩阵，即 $\mathbf{G} = g(t)\mathbf{I}$ ，此时SDE简化为：

$$
\mathrm{d}\mathbf{x} = \mathbf{f}(\mathbf{x}, t)\,\mathrm{d}t + g(t)\,\mathrm{d}\mathbf{W}
$$

这个方程的含义是：在每个无穷小时间步内，粒子位置的变化由两部分组成——确定性的漂移 $\mathbf{f}\,\mathrm{d}t$ 和随机的扩散 $g\,\mathrm{d}\mathbf{W}$ 。

### 1.3 Itô引理

要推导Fokker-Planck方程，需要Itô引理（Itô's lemma）。对于任意光滑函数 $\phi(\mathbf{x})$ ，如果 $\mathbf{x}$ 满足上述SDE，则：

$$
\mathrm{d}\phi = \left[\sum_i f_i \frac{\partial \phi}{\partial x_i} + \frac{g^2}{2}\sum_i \frac{\partial^2 \phi}{\partial x_i^2}\right]\mathrm{d}t + g\sum_i \frac{\partial \phi}{\partial x_i}\mathrm{d}W_i
$$

注意第二项（二阶导数项）是Itô微积分特有的——它来自于 $(\mathrm{d}W_i)^2 = \mathrm{d}t$ 这一关键性质。在常规微积分中， $(\mathrm{d}x)^2$ 是高阶无穷小可以忽略，但在随机微积分中 $(\mathrm{d}W)^2 \sim \mathrm{d}t$ 是一阶量，不能忽略。

---

## 第二部分：Fokker-Planck方程的推导

### 2.1 推导过程

设 $p_t(\mathbf{x})$ 是时刻 $t$ 时 $\mathbf{x}$ 的概率密度函数。我们要推导 $p_t$ 的演化方程。

对任意测试函数 $\phi(\mathbf{x})$ ，计算期望值的时间变化：

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[\phi(\mathbf{x}(t))] = \frac{\mathrm{d}}{\mathrm{d}t}\int \phi(\mathbf{x})\,p_t(\mathbf{x})\,\mathrm{d}\mathbf{x}
$$

由Itô引理， $\mathrm{d}\phi$ 的期望为（随机项的期望为零）：

$$
\mathbb{E}[\mathrm{d}\phi] = \mathbb{E}\left[\sum_i f_i \frac{\partial \phi}{\partial x_i} + \frac{g^2}{2}\sum_i \frac{\partial^2 \phi}{\partial x_i^2}\right]\mathrm{d}t
$$

因此：

$$
\int \phi \frac{\partial p_t}{\partial t}\,\mathrm{d}\mathbf{x} = \int \left[\sum_i f_i \frac{\partial \phi}{\partial x_i} + \frac{g^2}{2}\sum_i \frac{\partial^2 \phi}{\partial x_i^2}\right] p_t\,\mathrm{d}\mathbf{x}
$$

对右边进行分部积分（假设 $p_t$ 和 $\phi$ 在无穷远处衰减为零）：

第一项： $\int f_i \frac{\partial \phi}{\partial x_i} p_t\,\mathrm{d}\mathbf{x} = -\int \phi \frac{\partial (f_i p_t)}{\partial x_i}\,\mathrm{d}\mathbf{x}$

第二项： $\int \frac{g^2}{2} \frac{\partial^2 \phi}{\partial x_i^2} p_t\,\mathrm{d}\mathbf{x} = \int \phi \frac{g^2}{2}\frac{\partial^2 p_t}{\partial x_i^2}\,\mathrm{d}\mathbf{x}$ （两次分部积分）

由于 $\phi$ 是任意的，比较被积函数得到 **Fokker-Planck方程** ：

$$
\boxed{\frac{\partial p_t(\mathbf{x})}{\partial t} = -\sum_i \frac{\partial}{\partial x_i}[f_i(\mathbf{x},t)\,p_t(\mathbf{x})] + \frac{g(t)^2}{2}\sum_i \frac{\partial^2 p_t(\mathbf{x})}{\partial x_i^2}}
$$

用向量符号简写：

$$
\frac{\partial p_t}{\partial t} = -\nabla \cdot (\mathbf{f}\,p_t) + \frac{g^2}{2}\nabla^2 p_t
$$

这个方程完全等价于原始SDE——SDE描述单个粒子的随机轨迹，Fokker-Planck方程描述粒子集合体的概率密度演化。

---

## 第三部分：前向扩散过程

### 3.1 VP-SDE（Variance Preserving SDE）

扩散模型中最常用的前向过程是VP-SDE，其漂移和扩散系数为：

$$
\mathbf{f}(\mathbf{x},t) = -\frac{1}{2}\beta(t)\mathbf{x}, \quad g(t) = \sqrt{\beta(t)}
$$

其中 $\beta(t) > 0$ 是噪声调度函数（noise schedule），通常从接近0单调递增到某个最大值。SDE为：

$$
\mathrm{d}\mathbf{x} = -\frac{1}{2}\beta(t)\mathbf{x}\,\mathrm{d}t + \sqrt{\beta(t)}\,\mathrm{d}\mathbf{W}
$$

### 3.2 求解前向SDE的转移核

这是一个线性SDE（Ornstein-Uhlenbeck过程的推广），可以精确求解。定义 $\alpha(t) = e^{-\frac{1}{2}\int_0^t \beta(s)\,\mathrm{d}s}$ ，则该SDE的解为：

$$
\mathbf{x}(t) = \alpha(t)\,\mathbf{x}(0) + \int_0^t \alpha(t)\,\alpha(s)^{-1}\,\sqrt{\beta(s)}\,\mathrm{d}\mathbf{W}(s)
$$

令我们验证这一点。对 $\mathbf{y}(t) = \alpha(t)^{-1}\mathbf{x}(t)$ 应用Itô引理：

$$
\mathrm{d}\mathbf{y} = \alpha^{-1}\mathrm{d}\mathbf{x} + \mathbf{x}\,\mathrm{d}(\alpha^{-1})
$$

由于 $\frac{\mathrm{d}\alpha^{-1}}{\mathrm{d}t} = \frac{\beta(t)}{2}\alpha^{-1}$ ，代入SDE得：

$$
\mathrm{d}\mathbf{y} = \alpha^{-1}\left[-\frac{\beta}{2}\mathbf{x}\,\mathrm{d}t + \sqrt{\beta}\,\mathrm{d}\mathbf{W}\right] + \frac{\beta}{2}\alpha^{-1}\mathbf{x}\,\mathrm{d}t = \alpha^{-1}\sqrt{\beta}\,\mathrm{d}\mathbf{W}
$$

漂移项恰好抵消，因此 $\mathbf{y}(t) = \mathbf{y}(0) + \int_0^t \alpha(s)^{-1}\sqrt{\beta(s)}\,\mathrm{d}\mathbf{W}(s)$ ，即 $\mathbf{x}(t) = \alpha(t)\mathbf{x}(0) + \alpha(t)\int_0^t \alpha(s)^{-1}\sqrt{\beta(s)}\,\mathrm{d}\mathbf{W}(s)$ 。

由于Itô积分的方差为 $\int_0^t \alpha(s)^{-2}\beta(s)\,\mathrm{d}s$ ，而 $\alpha(s)^{-2} = e^{\int_0^s \beta(u)\,\mathrm{d}u}$ ，令 $\Phi(t) = \int_0^t \beta(s)\,\mathrm{d}s$ ，则 $\alpha(t)^2 = e^{-\Phi(t)}$ ，积分为：

$$
\int_0^t e^{\Phi(s)}\beta(s)\,\mathrm{d}s = \int_0^t \frac{\mathrm{d}}{\mathrm{d}s}e^{\Phi(s)}\,\mathrm{d}s = e^{\Phi(t)} - 1
$$

因此 $\mathbf{x}(t)$ 的条件方差为 $\alpha(t)^2(e^{\Phi(t)}-1) = 1 - \alpha(t)^2 \equiv 1 - \bar{\alpha}(t)$ 。

最终得到 **转移核** ：

$$
\boxed{q(\mathbf{x}_t|\mathbf{x}_0) = \mathcal{N}\left(\mathbf{x}_t;\, \sqrt{\bar{\alpha}(t)}\,\mathbf{x}_0,\, (1-\bar{\alpha}(t))\mathbf{I}\right)}
$$

其中 $\bar{\alpha}(t) = \alpha(t)^2 = e^{-\int_0^t \beta(s)\,\mathrm{d}s}$ 。

物理解释：在时刻 $t$ ，原始信号 $\mathbf{x}_0$ 被缩放了 $\sqrt{\bar{\alpha}(t)}$ 倍（信号衰减），同时叠加了方差为 $1-\bar{\alpha}(t)$ 的高斯噪声。当 $t \to T$ 且 $\bar{\alpha}(T) \to 0$ 时， $q(\mathbf{x}_T|\mathbf{x}_0) \to \mathcal{N}(\mathbf{0}, \mathbf{I})$ ——所有关于 $\mathbf{x}_0$ 的信息完全丧失。

### 3.3 离散化：DDPM的前向过程

将连续时间离散化为 $T$ 步，设 $\beta_t$ 为第 $t$ 步的噪声量。单步转移核为：

$$
q(\mathbf{x}_t|\mathbf{x}_{t-1}) = \mathcal{N}\left(\mathbf{x}_t;\, \sqrt{1-\beta_t}\,\mathbf{x}_{t-1},\, \beta_t\mathbf{I}\right)
$$

这正是幻灯片第三页的公式。可以验证多步的累积效果：

定义 $\alpha_t = 1 - \beta_t$ ， $\bar{\alpha}_t = \prod_{s=1}^t \alpha_s$ ，则通过递归可以证明：

$$
q(\mathbf{x}_t|\mathbf{x}_0) = \mathcal{N}\left(\mathbf{x}_t;\, \sqrt{\bar{\alpha}_t}\,\mathbf{x}_0,\, (1-\bar{\alpha}_t)\mathbf{I}\right)
$$

证明： $\mathbf{x}_t = \sqrt{1-\beta_t}\,\mathbf{x}_{t-1} + \sqrt{\beta_t}\,\boldsymbol{\epsilon}_{t-1}$ 。递归代入得 $\mathbf{x}_t = \sqrt{\bar{\alpha}_t}\,\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\,\boldsymbol{\epsilon}$ ，其中 $\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 。这利用了独立高斯随机变量的方差可加性： $a\boldsymbol{\epsilon}_1 + b\boldsymbol{\epsilon}_2$ 的方差为 $a^2 + b^2$ ，而 $(1-\beta_t)(1-\bar{\alpha}_{t-1}) + \beta_t = 1 - \bar{\alpha}_t$ 。

---

## 第四部分：Anderson时间反转定理——反向SDE的严格推导

这是扩散模型最核心的数学定理。

### 4.1 定理陈述

**Anderson (1982)定理：** 若前向SDE为 $\mathrm{d}\mathbf{x} = \mathbf{f}(\mathbf{x},t)\,\mathrm{d}t + g(t)\,\mathrm{d}\mathbf{W}$ ，且 $p_t(\mathbf{x})$ 为其边际密度，则时间反转过程 $\mathbf{x}(\tau)$ （其中 $\tau = T - t$ ，即时间从 $T$ 回退到 $0$ ）满足：

$$
\boxed{\mathrm{d}\mathbf{x} = \left[\mathbf{f}(\mathbf{x},t) - g(t)^2\,\nabla_{\mathbf{x}}\log p_t(\mathbf{x})\right]\mathrm{d}t + g(t)\,\mathrm{d}\bar{\mathbf{W}}}
$$

其中 $\mathrm{d}t$ 在此处取负值（时间倒流）， $\mathrm{d}\bar{\mathbf{W}}$ 是反向维纳过程。

### 4.2 严格推导

我们需要找到一个反向时间的SDE，使其产生的边际分布 $\tilde{p}_\tau(\mathbf{x})$ 满足 $\tilde{p}_\tau(\mathbf{x}) = p_{T-\tau}(\mathbf{x})$ 。

**步骤A：前向过程的Fokker-Planck方程**

$$
\frac{\partial p_t}{\partial t} = -\nabla \cdot (\mathbf{f}\,p_t) + \frac{g^2}{2}\nabla^2 p_t \tag{FP-forward}
$$

将右边改写为散度形式。注意 $\nabla^2 p_t = \nabla \cdot (\nabla p_t)$ ，因此：

$$
\frac{\partial p_t}{\partial t} = -\nabla \cdot \left[\mathbf{f}\,p_t - \frac{g^2}{2}\nabla p_t\right]
$$

利用 $\nabla p_t = p_t \nabla \log p_t$ ，得：

$$
\frac{\partial p_t}{\partial t} = -\nabla \cdot \left[\left(\mathbf{f} - \frac{g^2}{2}\nabla \log p_t\right) p_t\right] \tag{1}
$$

**步骤B：构造反向过程的Fokker-Planck方程**

设反向SDE的漂移为 $\tilde{\mathbf{f}}(\mathbf{x},t)$ ，扩散系数为 $\tilde{g}(t)$ 。反向过程在 $\tau = T - t$ 时间坐标下的Fokker-Planck方程为：

$$
\frac{\partial \tilde{p}_\tau}{\partial \tau} = -\nabla \cdot (\tilde{\mathbf{f}}\,\tilde{p}_\tau) + \frac{\tilde{g}^2}{2}\nabla^2 \tilde{p}_\tau \tag{FP-reverse}
$$

**步骤C：匹配条件**

要求 $\tilde{p}_\tau = p_{T-\tau}$ 。由于 $\frac{\partial \tilde{p}_\tau}{\partial \tau} = -\frac{\partial p_t}{\partial t}\Big|_{t=T-\tau}$ ，将(1)代入：

$$
-\frac{\partial p_t}{\partial t} = \nabla \cdot \left[\left(\mathbf{f} - \frac{g^2}{2}\nabla \log p_t\right) p_t\right]
$$

另一方面，(FP-reverse)的右边为：

$$
-\nabla \cdot (\tilde{\mathbf{f}}\,p_t) + \frac{\tilde{g}^2}{2}\nabla^2 p_t = -\nabla \cdot \left[\tilde{\mathbf{f}} - \frac{\tilde{g}^2}{2}\nabla \log p_t\right] p_t
$$

令两者相等：

$$
\nabla \cdot \left[\left(\mathbf{f} - \frac{g^2}{2}\nabla \log p_t\right) p_t\right] = -\nabla \cdot \left[\left(\tilde{\mathbf{f}} - \frac{\tilde{g}^2}{2}\nabla \log p_t\right) p_t\right]
$$

最简单的满足方式（且物理上自然的选择）是取 $\tilde{g} = g$ （反向过程保持相同的噪声强度），则：

$$
\mathbf{f} - \frac{g^2}{2}\nabla \log p_t = -\tilde{\mathbf{f}} + \frac{g^2}{2}\nabla \log p_t
$$

解出反向漂移：

$$
\boxed{\tilde{\mathbf{f}}(\mathbf{x},t) = \mathbf{f}(\mathbf{x},t) - g(t)^2\,\nabla_{\mathbf{x}}\log p_t(\mathbf{x})}
$$

因此反向SDE为（时间从 $T$ 到 $0$ ）：

$$
\mathrm{d}\mathbf{x} = \left[\mathbf{f}(\mathbf{x},t) - g(t)^2\,\nabla_{\mathbf{x}}\log p_t(\mathbf{x})\right]\mathrm{d}t + g(t)\,\mathrm{d}\bar{\mathbf{W}}
$$

### 4.3 物理解释

反向漂移比前向漂移多了一项 $-g^2 \nabla \log p_t$ 。这个额外项的方向指向 **概率密度增大** 的方向（因为 $\nabla \log p_t$ 指向高概率区域，乘以 $-1$ 后再乘以时间反转的负号，净效果是指向高概率区域）。

在统计力学中，如果 $p_t \propto e^{-\beta U}$ ，则 $\nabla \log p_t = -\beta \nabla U$ ，额外的力为 $g^2 \beta \nabla U$ ，即一个将系统从高能区域推向低能区域的力——这就是"去噪"的物理机制。

---

## 第五部分：分数函数的学习与训练目标

### 5.1 核心问题

反向SDE中需要知道 $\nabla_{\mathbf{x}}\log p_t(\mathbf{x})$ ，但 $p_t(\mathbf{x})$ 是未知的（它是数据分布经过前向扩散后的边际分布）。解决方案是训练一个神经网络 $\mathbf{s}_\theta(\mathbf{x}, t)$ 来近似它：

$$
\mathbf{s}_\theta(\mathbf{x}, t) \approx \nabla_{\mathbf{x}} \log p_t(\mathbf{x})
$$

### 5.2 分数匹配（Score Matching）

直接的训练目标是最小化：

$$
\mathcal{L}_{SM} = \mathbb{E}_{t \sim \mathcal{U}[0,T]}\,\mathbb{E}_{\mathbf{x} \sim p_t} \left[\left\|\mathbf{s}_\theta(\mathbf{x},t) - \nabla_{\mathbf{x}}\log p_t(\mathbf{x})\right\|^2\right]
$$

问题是 $\nabla_{\mathbf{x}}\log p_t(\mathbf{x})$ 本身未知。但我们可以利用 **去噪分数匹配** （Denoising Score Matching, Vincent 2011）的恒等式。

关键观察：虽然边际分布 $p_t(\mathbf{x})$ 未知，但 **条件分布** $q(\mathbf{x}_t|\mathbf{x}_0)$ 是已知的高斯分布（我们在第三部分已经推导出）。利用贝叶斯公式：

$$
p_t(\mathbf{x}_t) = \int q(\mathbf{x}_t|\mathbf{x}_0)\,p_{\text{data}}(\mathbf{x}_0)\,\mathrm{d}\mathbf{x}_0
$$

可以证明（通过分部积分和对称性论证）：

$$
\mathbb{E}_{\mathbf{x}_t \sim p_t}\left[\|\mathbf{s}_\theta - \nabla \log p_t\|^2\right] = \mathbb{E}_{\mathbf{x}_0 \sim p_{\text{data}}}\,\mathbb{E}_{\mathbf{x}_t \sim q(\cdot|\mathbf{x}_0)}\left[\|\mathbf{s}_\theta(\mathbf{x}_t, t) - \nabla_{\mathbf{x}_t}\log q(\mathbf{x}_t|\mathbf{x}_0)\|^2\right] + C
$$

其中 $C$ 是不依赖于 $\theta$ 的常数。

### 5.3 条件分数的解析表达式

由前面推导的转移核 $q(\mathbf{x}_t|\mathbf{x}_0) = \mathcal{N}(\sqrt{\bar{\alpha}_t}\mathbf{x}_0, (1-\bar{\alpha}_t)\mathbf{I})$ ，其对数为：

$$
\log q(\mathbf{x}_t|\mathbf{x}_0) = -\frac{\|\mathbf{x}_t - \sqrt{\bar{\alpha}_t}\mathbf{x}_0\|^2}{2(1-\bar{\alpha}_t)} + \text{const}
$$

对 $\mathbf{x}_t$ 求梯度：

$$
\nabla_{\mathbf{x}_t}\log q(\mathbf{x}_t|\mathbf{x}_0) = -\frac{\mathbf{x}_t - \sqrt{\bar{\alpha}_t}\mathbf{x}_0}{1-\bar{\alpha}_t}
$$

由于 $\mathbf{x}_t = \sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\,\boldsymbol{\epsilon}$ ，代入得：

$$
\nabla_{\mathbf{x}_t}\log q(\mathbf{x}_t|\mathbf{x}_0) = -\frac{\sqrt{1-\bar{\alpha}_t}\,\boldsymbol{\epsilon}}{1-\bar{\alpha}_t} = -\frac{\boldsymbol{\epsilon}}{\sqrt{1-\bar{\alpha}_t}}
$$

### 5.4 等价的噪声预测目标

将分数网络参数化为 $\mathbf{s}_\theta(\mathbf{x}_t, t) = -\frac{\boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)}{\sqrt{1-\bar{\alpha}_t}}$ ，则训练目标变为：

$$
\mathcal{L} = \mathbb{E}_{t, \mathbf{x}_0, \boldsymbol{\epsilon}}\left[\frac{1}{1-\bar{\alpha}_t}\left\|\boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t) - \boldsymbol{\epsilon}\right\|^2\right]
$$

Ho et al. (2020) 发现去掉权重 $\frac{1}{1-\bar{\alpha}_t}$ 后效果更好，因此实际训练目标简化为：

$$
\boxed{\mathcal{L}_{\text{simple}} = \mathbb{E}_{t \sim \mathcal{U}\{1,...,T\},\, \mathbf{x}_0 \sim p_{\text{data}},\, \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0},\mathbf{I})}\left[\left\|\boldsymbol{\epsilon}_\theta\!\left(\sqrt{\bar{\alpha}_t}\,\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\,\boldsymbol{\epsilon},\, t\right) - \boldsymbol{\epsilon}\right\|^2\right]}
$$

含义极其直观：给定一个加噪后的样本 $\mathbf{x}_t$ ，神经网络学习预测添加的噪声 $\boldsymbol{\epsilon}$ 。

### 5.5 DDPM反向过程的推导

训练完成后，反向采样使用离散化的反向过程。需要求前向过程的后验分布 $q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0)$ 。

由贝叶斯公式：

$$
q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0) = \frac{q(\mathbf{x}_t|\mathbf{x}_{t-1})q(\mathbf{x}_{t-1}|\mathbf{x}_0)}{q(\mathbf{x}_t|\mathbf{x}_0)}
$$

三个分布都是已知的高斯分布：

$$
q(\mathbf{x}_t|\mathbf{x}_{t-1}) \propto \exp\left(-\frac{\|\mathbf{x}_t - \sqrt{\alpha_t}\mathbf{x}_{t-1}\|^2}{2\beta_t}\right)
$$
 
$$
q(\mathbf{x}_{t-1}|\mathbf{x}_0) \propto \exp\left(-\frac{\|\mathbf{x}_{t-1} - \sqrt{\bar{\alpha}_{t-1}}\mathbf{x}_0\|^2}{2(1-\bar{\alpha}_{t-1})}\right)
$$
 
$$
q(\mathbf{x}_t|\mathbf{x}_0) \propto \exp\left(-\frac{\|\mathbf{x}_t - \sqrt{\bar{\alpha}_t}\mathbf{x}_0\|^2}{2(1-\bar{\alpha}_t)}\right)
$$

将前两个合并（作为 $\mathbf{x}_{t-1}$ 的函数），完成配方：

指数部分中 $\mathbf{x}_{t-1}$ 的二次项系数为 $-\frac{\alpha_t}{2\beta_t} - \frac{1}{2(1-\bar{\alpha}_{t-1})}$ ，一次项系数为 $\frac{\sqrt{\alpha_t}\mathbf{x}_t}{\beta_t} + \frac{\sqrt{\bar{\alpha}_{t-1}}\mathbf{x}_0}{1-\bar{\alpha}_{t-1}}$ 。

经过配方，后验为高斯分布 $q(\mathbf{x}_{t-1}|\mathbf{x}_t,\mathbf{x}_0) = \mathcal{N}(\mathbf{x}_{t-1}; \tilde{\boldsymbol{\mu}}_t, \tilde{\beta}_t\mathbf{I})$ ，其中：

$$
\tilde{\beta}_t = \frac{(1-\bar{\alpha}_{t-1})\beta_t}{1-\bar{\alpha}_t}
$$
 
$$
\tilde{\boldsymbol{\mu}}_t = \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}\mathbf{x}_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t}\mathbf{x}_0
$$

由于在采样时 $\mathbf{x}_0$ 未知，利用 $\mathbf{x}_0 = \frac{1}{\sqrt{\bar{\alpha}_t}}(\mathbf{x}_t - \sqrt{1-\bar{\alpha}_t}\,\boldsymbol{\epsilon})$ 代入，用网络预测的 $\boldsymbol{\epsilon}_\theta$ 替换 $\boldsymbol{\epsilon}$ ，最终得到DDPM的采样公式：

$$
\boxed{\mathbf{x}_{t-1} = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\,\boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\right) + \sqrt{\tilde{\beta}_t}\,\mathbf{z}, \quad \mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})}
$$

这就是幻灯片第三页中 $p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t) = \mathcal{N}(\mathbf{x}_{t-1}; \boldsymbol{\mu}_\theta(\mathbf{x}_t, t), \boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t))$ 的具体形式。

---

## 第六部分：Committor函数的理论基础

### 6.1 从第一性原理定义

考虑一个分子系统在势能面上运动，满足过阻尼Langevin方程：

$$
\mathrm{d}\mathbf{x} = -\nabla U(\mathbf{x})\,\mathrm{d}t + \sqrt{2\beta^{-1}}\,\mathrm{d}\mathbf{W}
$$

其中 $U(\mathbf{x})$ 是势能， $\beta = 1/(k_BT)$ 是逆温度。

给定两个亚稳态区域 $A$ 和 $B$ ，committor函数 $q(\mathbf{x})$ 定义为从位置 $\mathbf{x}$ 出发的轨迹 **先到达** $B$ （而非 $A$ ）的概率。

### 6.2 Committor满足的偏微分方程

committor函数满足后向Kolmogorov方程（backward Kolmogorov equation）。这可以从第一性原理推导。

设 $\mathcal{L}$ 为与过阻尼Langevin方程对应的生成算子（generator）：

$$
\mathcal{L} = -\nabla U \cdot \nabla + \beta^{-1}\nabla^2
$$

对于任何函数 $h(\mathbf{x})$ ，如果 $h(\mathbf{x}) = \mathbb{E}[\phi(\mathbf{x}(\tau_{\text{exit}}))|\mathbf{x}(0)=\mathbf{x}]$ （其中 $\tau_{\text{exit}}$ 是首次到达 $A \cup B$ 的时间），则由最优停止理论/Dynkin公式， $h$ 满足：

$$
\mathcal{L}\,h(\mathbf{x}) = 0, \quad \mathbf{x} \in \Omega \setminus (A \cup B)
$$

对于committor， $\phi = \mathbf{1}_B$ （到达B取1，到达A取0），因此 $q$ 满足：

$$
\boxed{-\nabla U(\mathbf{x}) \cdot \nabla q(\mathbf{x}) + \beta^{-1}\nabla^2 q(\mathbf{x}) = 0, \quad \mathbf{x} \notin A \cup B}
$$

边界条件为 $q(\mathbf{x}) = 0$ 在 $\partial A$ 上， $q(\mathbf{x}) = 1$ 在 $\partial B$ 上。

等价地，乘以玻尔兹曼权重 $e^{-\beta U}$ ，可以写成自伴形式：

$$
\nabla \cdot \left(e^{-\beta U}\nabla q\right) = 0
$$

这说明committor是玻尔兹曼加权的调和函数。

### 6.3 过渡态的定义

$q(\mathbf{x}) = 0.5$ 的等值面（即isocommittor surface）定义了 **过渡态集合（transition state ensemble, TSE）** 。在这个面上，分子从任何构型出发，到达A和B的概率恰好相等——这是过渡态的严格数学定义，无需依赖鞍点或势垒的概念。

### 6.4 变分方法学习Committor（VCN）

在高维空间中直接求解上述PDE不可行。变分committor网络（VCN）将committor参数化为神经网络 $q_\phi(\mathbf{z})$ （其中 $\mathbf{z}$ 是某种特征表示），并通过变分原理求解。

committor的变分原理为：真正的committor函数最小化以下泛函：

$$
\mathcal{F}[q] = \int e^{-\beta U(\mathbf{x})}\|\nabla q(\mathbf{x})\|^2\,\mathrm{d}\mathbf{x}
$$

在边界条件 $q|_A = 0$ ， $q|_B = 1$ 下。

这个变分原理的推导：对Euler-Lagrange方程 $\delta \mathcal{F}/\delta q = 0$ 取变分，得到 $-2\nabla \cdot (e^{-\beta U}\nabla q) = 0$ ，恰好是committor的PDE。

实际训练中，可以使用短MD轨迹数据，将变分问题转化为：

$$
\mathcal{L}_{\text{VCN}} = \mathbb{E}_{\mathbf{x} \sim \rho}\left[\|\nabla q_\phi(\mathbf{x})\|^2\right] + \lambda_A\,\mathbb{E}_{\mathbf{x} \in A}\left[q_\phi(\mathbf{x})^2\right] + \lambda_B\,\mathbb{E}_{\mathbf{x} \in B}\left[(1-q_\phi(\mathbf{x}))^2\right]
$$

其中 $\rho$ 是某种采样分布（如从短MD轨迹中获得），后两项是边界条件的软约束。

或者等价地，可以使用committor的概率解释——对从 $\mathbf{x}$ 出发的短轨迹，统计其到达B的比例作为标签，用交叉熵损失训练。

---

## 第七部分：Gen-COMPAS的完整计算流程

现在将所有理论组件整合为Gen-COMPAS的完整算法。

### 输入

两个已知的端态结构：A（例如蛋白质折叠态）和B（例如去折叠态），以及一个能够进行分子动力学模拟的力场。

### 步骤1：端态采样

对A和B分别进行短时间（纳秒级）的常规MD模拟。设从A获得的构型集合为 $\{\mathbf{x}_A^{(i)}\}_{i=1}^{N_A}$ ，从B获得的为 $\{\mathbf{x}_B^{(j)}\}_{j=1}^{N_B}$ 。

这些模拟只需要在各自的势阱内采样，不需要跨越能垒，因此计算成本很低。

### 步骤2：训练扩散模型

**数据表示：** 蛋白质构型通常用所有原子的三维坐标表示， $\mathbf{x} \in \mathbb{R}^{3N}$ （ $N$ 为原子数）。为了尊重物理对称性（旋转、平移不变性），可以使用内部坐标（键角、二面角）或对齐后的笛卡尔坐标。

**扩散桥模型：** 与标准扩散模型（数据→噪声）不同，Gen-COMPAS使用的是 **扩散桥** （diffusion bridge）：训练一个条件生成模型，使其能够在A和B之间进行插值。前向过程不是将A态扩散到高斯噪声，而是将A态扩散到B态。

具体地，扩散桥可以通过条件化的SDE实现。对于标准的扩散桥，设我们要求轨迹在 $t=0$ 处为 $\mathbf{x}_A$ ，在 $t=T$ 处为 $\mathbf{x}_B$ ，则条件化后的SDE漂移多了一个"引导项"，将系统拉向 $\mathbf{x}_B$ ：

$$
\mathrm{d}\mathbf{x} = \left[\mathbf{f}(\mathbf{x},t) + g(t)^2\frac{\mathbf{x}_B - \mathbf{x}}{T-t}\right]\mathrm{d}t + g(t)\,\mathrm{d}\mathbf{W}
$$

（这是Doob's h-transform的一个特例。）

训练目标类似于标准扩散模型，但条件化在端点上。神经网络学习预测A到B路径中间时刻的结构分布。

### 步骤3：生成中间结构

使用训练好的扩散模型，从A态（或噪声）出发，通过反向采样生成大量（例如数千个）中间结构 $\{\mathbf{x}_{\text{gen}}^{(k)}\}_{k=1}^{M}$ 。这些结构应覆盖A和B之间的构型空间。

### 步骤4（对应原始步骤3-4）：聚类与二次采样

对生成的中间结构进行聚类分析（例如基于RMSD距离的k-medoids聚类），识别质心和离群点。然后从这些代表性结构出发，进行短时间（纳秒级）的无偏MD模拟，收集中间区域的局部采样数据。

### 步骤5：训练VCN

利用步骤1和步骤4收集的所有轨迹数据，训练变分committor网络。训练数据的构成为：从A附近出发的轨迹（大部分回到A，committor接近0）、从B附近出发的轨迹（大部分回到B，committor接近1）、从中间区域出发的轨迹（部分到A，部分到B，committor为中间值）。

VCN输出每个构型的committor值 $q_\phi(\mathbf{x})$ 。 $q \approx 0.5$ 的等值面定义了过渡态。

### 步骤6：筛选过渡态

在步骤3生成的中间结构中，利用VCN筛选出满足 $|q_\phi(\mathbf{x}) - 0.5| < \delta$ （ $\delta$ 为小阈值）的结构作为候选过渡态集合（TSE）。

### 步骤7：从过渡态发射轨迹

从TSE中的每个结构出发，发射多条短时间无偏MD轨迹。由于起点在自由能鞍点上，轨迹自然"滑落"到A或B态。统计学上，约50%到达A，约50%到达B（这是committor = 0.5的定义）。

收集这些轨迹，可以构建：完整的反应路径集合；committor函数的验证（检查是否真的约50/50分裂）；通过重加权（reweighting）得到自由能面的估计。

### 迭代改进（可选）

步骤5-7可以迭代：新的轨迹数据用于重新训练VCN和扩散模型，逐步提高精度。

### 输出

最终产出包括：反应路径（可能有多条），过渡态结构（物理上可靠的TSE），committor函数（最优反应坐标），自由能面（在关键区域的自由能图景）。

---

## 第八部分：为什么Gen-COMPAS能实现350倍加速

回到幻灯片第五页的核心结果（0.6 μs vs 208 μs），从信息论角度理解这一加速。

传统的暴力MD模拟大部分时间花在了亚稳态（A或B）内部的热涨落上。系统在势阱底部做无数次无意义的振荡，等待极罕见的热涨落将其推过能垒。如果A到B的平均过渡时间为 $\tau_{AB}$ ，而单次过渡事件本身只持续 $\tau_{\text{cross}}$ ，则暴力模拟的"信息效率"约为 $\tau_{\text{cross}}/\tau_{AB}$ ，对于蛋白质折叠这类问题，这个比值可能是 $10^{-6}$ 到 $10^{-3}$ 。

Gen-COMPAS通过以下方式避免了这种浪费：扩散模型直接生成中间区域的候选结构（跳过了在势阱底部的等待时间）；VCN精确定位过渡态（避免了在错误区域采样）；短时间MD仅在过渡态附近运行（每条轨迹都携带关于反应机理的最大信息量）。

从数学上，这等价于将采样问题从"在整个构型空间均匀采样"转变为"在committor等值面 $q = 0.5$ 附近集中采样"——后者的信息密度最高，因为过渡态区域是反应路径的"瓶颈"，包含了决定反应速率和机理的全部关键信息。

15:01

星期日

将文件放在这里