---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247487192&idx=1&sn=6c3045ea3dea8f8d7f509e8f88f2243e
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247487192&idx=1&sn=6c3045ea3dea8f8d7f509e8f88f2243e
source_domain: mp.weixin.qq.com
title: NeurIPS 2025 | AI驱动分子动力学模拟：基于能量的扩散模型实现一致采样与模拟
author: 
published_at: 
fetched_at: 2026-04-25T02:03:52Z
extractor: wechat_worker
content_hash: 093fab3f120bd5796ba624ecc3e00681a39b871205168cde3323489768273937
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/KoRXqKjLA9icWn3SfJiaHvyePxowobpaXejxdVkOfkhWUtyoLxIKWkic6pU7WuibfJB6QEswZqWEt3Vu0qqwwib1oBA/0.jpg) 

# NeurIPS 2025 | AI驱动分子动力学模拟：基于能量的扩散模型实现一致采样与模拟

原创 DrugIntel DrugIntel [ DrugIntel ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icWn3SfJiaHvyePxowobpaXePgd0yy9ibpOzHW12Szykic2vLfDYxBZmOLgydGrAU6zF7TyFpoUgyQlQ/640.png)

在计算生物学与分子模拟领域，分子动力学（MD）模拟是解析生物分子构象变化、揭示分子间相互作用机制的核心手段。然而，传统全原子MD模拟面临计算成本高昂的困境，而粗粒化（CG）方法虽能提升模拟效率，却难以精准刻画分子力场与动力学行为。扩散模型作为强大的生成式建模工具，在生物分子采样中展现出巨大潜力，但长期存在采样分布与动力学仿真不一致的关键问题。

NeurIPS 2025收录的这项研究《Consistent Sampling and Simulation: Molecular Dynamics with Energy-Based Diffusion Models》，通过融合福克-普朗克方程正则化与专家混合架构，系统性解决了这一核心矛盾，为生物分子模拟提供了兼具效率、精度与一致性的方法。

## 一、领域痛点：扩散模型在分子模拟中的核心矛盾

### 1\. 现有方法的双重困境

* **计算效率与精度的权衡**：全原子MD模拟能提供高精度的热力学与动力学信息，但面对大分子系统或慢构象转变时，往往需要耗费海量计算资源，难以达到生物学相关时间尺度；粗粒化方法通过合并原子降低系统维度，虽提升了模拟速度，却因力场描述的简化的，无法准确复现分子动力学行为。
* **采样与仿真的一致性缺失**：扩散模型通过学习分子平衡态分布，能高效生成符合物理规律的分子构象（采样任务），但现有模型学习到的分数函数（可推导分子受力）与训练分布存在内在不一致性。这一问题在极小扩散时间步长下尤为突出，导致模型虽能完成高质量采样，却无法基于分数函数开展可靠的动力学仿真，形成 采样准、仿真差 的割裂局面。

### 2\. 矛盾根源：福克-普朗克方程的违背

研究团队通过深入分析发现，**扩散模型的一致性缺失本质上源于对福克-普朗克方程的违背**。该方程是描述扩散过程中概率密度演化的核心物理规律，而现有扩散模型在极小扩散时间步长下，分数函数无法满足这一方程的约束，导致密度演化与分数函数演化不同步，最终积累为采样与仿真的显著偏差。即使在低维玩具系统中，这种不一致性也会导致仿真结果出现非物理模态。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ibiciaMUWa5T8gL5dJvNUMMyuBhr3KH4MRcbCuXcniasoHt6AteiaIQeNyr0TicHvDuBaVic9K7AwkuicPFQ/640.png)

## 二、核心创新：构建物理一致的能量基扩散模型

研究团队提出了一套 正则化约束+架构优化 的完整解决方案，从三个维度实现了采样与仿真的一致性突破：

### 1\. 福克-普朗克正则化：强制物理规律约束

为解决分数函数与密度演化的不一致问题，研究引入了基于福克-普朗克方程的正则化项。该正则化项通过惩罚模型对福克-普朗克方程的偏离，将大时间步长下的稳定精度传递到极小时间步长区域，确保分数函数在整个扩散时间轴上都能遵循物理规律。

* **正则化损失设计**：通过最小化福克-普朗克方程的残差误差，构建了包含分数函数梯度、散度等关键物理量的损失项，使模型在训练过程中始终受到物理规律约束。
* **高效计算实现**：针对高维分子系统中高阶导数计算昂贵的问题，提出弱残差公式与有限差分近似方法，仅通过一阶导数计算即可实现正则化损失的高效估计，大幅降低了计算开销。

### 2\. 物理一致的模型架构设计

* **保守参数化方案**：将分数函数定义为能量函数的梯度，确保分子力源自明确的势能面，避免了直接参数化分数函数导致的动力学不稳定性。这种设计不仅符合经典力学中“力是势能梯度的负值”的基本原理，也为数值仿真的稳定性提供了保障。
* **等变图 transformer**：采用等变图Transformer架构，通过成对距离而非绝对坐标实现平移不变性，并通过训练中的随机旋转数据增强，使模型学习到旋转等变性，完美适配分子系统的几何对称性。最终通过将节点嵌入映射为标量能量，进一步确保了模型的保守性与物理一致性。

### 3\. 时间轴专家混合（MoE）策略

针对扩散模型在不同时间步长下的任务差异，研究提出将扩散时间轴划分为多个不相交的子区间，为每个区间训练专门的“专家模型”：

* **小时间步长专家**：专注于动力学仿真任务，采用保守参数化与福克-普朗克正则化，确保分数函数的物理准确性。
* **大时间步长专家**：专注于构象采样任务，采用更简洁的无约束架构，避免过度正则化导致的采样质量下降。

这种设计的核心优势在于：一方面，通过任务分工提升了模型在各时间区间的性能；另一方面，仅需加载对应区间的专家模型即可完成采样或仿真任务，显著降低了训练与推理的计算成本，使模型在保持高精度的同时，采样速度提升超过50%。

## 三、实验验证：多系统下的性能突破

研究团队在三类典型生物分子系统上开展了全面验证，从定量与定性两个维度证明了方法的优越性：

### 1\. 实验设置与评估指标

* **测试系统**：涵盖丙氨酸二肽（小分子模型）、Chignolin（10个氨基酸的快速折叠蛋白）、BBA（28个氨基酸的蛋白）以及175种二肽（迁移性验证），全面覆盖不同尺度的分子系统。
* **核心指标**：采用势能面误差（PMF误差）、詹森-香农散度（JS散度）等指标，量化采样与仿真结果与参考分布的差异；同时通过接触图、键长分布、状态转移概率等分析，评估模型的物理一致性。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icWn3SfJiaHvyePxowobpaXeIcwAIWxdtvhVS2F1UMLebq3l4sxJuAoINLRwic7lH548AVjGqicolAVw/640.png)

### 2\. 关键实验结果

* **一致性显著提升**：在丙氨酸二肽系统中，该方法的仿真PMF误差仅为0.091，优于传统扩散模型和Two For One方法（0.206）；在Chignolin和BBA蛋白系统中，传统方法的仿真结果出现明显的非物理模态，而该方法的采样与仿真结果几乎完全对齐，PMF误差分别低至0.038和0.254。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icWn3SfJiaHvyePxowobpaXeb3kGUlWMnpffI2ibOKXYPnHMgfyTWPhDibODkctyH8xF3JMJiaTYFcpPA/640.png)![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icWn3SfJiaHvyePxowobpaXemXfcw0ciaWJUWlYCu3HrFqbia2mIUwLCRYaDHzlD18ep2ZK25gYWomiaA/640.png)
* **迁移性与泛化能力**：针对175种二肽训练的迁移模型，在92种测试二肽上均实现了高质量的采样与仿真，仿真PMF误差低至0.203，优于现有迁移性玻尔兹曼生成器，证明了模型在不同分子系统上的强大泛化能力。
* **动力学行为复现**：通过状态转移概率分析，该方法能准确复现蛋白折叠-解折叠的动态过程，其状态转移矩阵与参考MD模拟的JS散度仅为2.1×10⁻⁴（Chignolin系统），优于其他方法，证明了模型对动力学行为的精准捕捉能力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icWn3SfJiaHvyePxowobpaXe9NAl8icov20Ncr4KLicXhqU805Fvqv5eHa1BticfCyM9vLdM20N9XNmnA/640.png)

### 3\. 计算效率优势

得益于粗粒化策略与专家混合架构，该方法在计算效率上实现了突破：在单NVIDIA A100 GPU上，二肽系统的并行仿真速度可达125k步/秒，远超传统力场模拟在单NVIDIA V40的10k步/秒；BBA蛋白的100组并行仿真（每组100万步）仅需约1小时即可完成，为大规模分子动力学研究提供了高效工具。

## 四、方法对比与科学价值

### 1\. 与现有方法的核心差异

| 方法类型    | 核心特点            | 采样质量 | 仿真一致性 | 计算效率 |
| ------- | --------------- | ---- | ----- | ---- |
| 传统全原子MD | 基于物理力场，精度高      | \-   | 高     | 极低   |
| 传统扩散模型  | 无物理正则化，采样高效     | 高    | 低     | 中    |
| 力匹配方法   | 依赖显式力标签，需物理先验   | \-   | 中     | 中    |
| 本文方法    | 福克-普朗克正则化+MoE架构 | 高    | 高     | 高    |

### 2\. 领域贡献与科学价值

* **理论价值**：从福克-普朗克方程的角度揭示了扩散模型采样与仿真不一致的本质，建立了物理规律与生成式建模的桥梁，为能量基扩散模型的物理一致性设计提供了理论指导。
* **方法创新**：提出的福克-普朗克正则化、保守参数化架构与专家混合策略，不仅解决了分子模拟中的核心问题，也为其他需要物理一致性的生成式建模任务（如材料设计、流体模拟等）提供了可复用的技术框架。
* **应用价值**：该方法无需显式力场标签，仅通过平衡态样本即可同时实现高质量采样与动力学仿真，尤其适用于粗粒化等缺乏直接力信息的场景。其开源的代码、模型权重及JAX/PyTorch示例（https://github.com/noegroup/ScoreMD），为领域研究提供了强大的工具支持。

## 五、局限与未来方向

尽管取得了突破，该研究仍存在一些值得进一步探索的方向：

* **计算开销**：福克-普朗克正则化的计算仍需多次前向传播，导致训练开销高于传统扩散模型；
* **泛化边界**：模型在高能量或未见过的构象区域的表现仍有待提升，增强采样任务中仍存在探索不足的问题；
* **系统规模**：目前的验证主要集中在中小规模分子系统，对更大规模的生物大分子（如抗体、酶复合物）的适用性仍需进一步验证。

未来研究可围绕三个方向展开：一是优化正则化计算效率，降低训练成本；二是探索迁移学习策略，实现跨分子家族的泛化；三是扩展模型至更复杂的分子系统，结合增强采样技术进一步提升模型的适用范围。

## 小结

该研究通过将物理规律（福克-普朗克方程）与生成式建模深度融合，缓解了扩散模型在分子模拟中 采样与仿真不一致 的核心痛点，构建了兼具效率、精度与物理一致性的模拟方法。其创新的正则化方法与架构设计，不仅推动了分子动力学模拟领域的技术进步，也为AI for Science领域提供了 物理约束+数据驱动 的成功范例。对于从事计算生物学、药物设计、材料科学等领域的研究者而言，这篇文献不仅提供了强大的技术工具，更展现了跨学科融合的深刻价值，值得深入研读与实践。

参考文献：Plainer M, Wu H, Klein L, et al. Consistent sampling and simulation: Molecular dynamics with energy-based diffusion models\[J\]. NeurIPS 2025.17139, 2025.

代码链接：https://github.com/noegroup/ScoreMD

预览时标签不可点

[阅读原文](javascript:;) 

修改于 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icaZmJVvQe5nCiabibOyaceianZY23nlsXAkxR5uiajvHibdBJvESicc58tOeibVXmVTp4HVVADZh79C1iczA/0.png) 

 DrugIntel 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icaZmJVvQe5nCiabibOyaceianZY23nlsXAkxR5uiajvHibdBJvESicc58tOeibVXmVTp4HVVADZh79C1iczA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
