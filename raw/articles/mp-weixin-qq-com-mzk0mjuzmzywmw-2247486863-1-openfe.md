---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247486863&idx=1&sn=93148e71a454dd8eb7a70ce669101fb9
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247486863&idx=1&sn=93148e71a454dd8eb7a70ce669101fb9
source_domain: mp.weixin.qq.com
title: 国际顶尖药企联合验证：开源工具 OpenFE 如何实现与商业软件比肩的结合自由能计算
author: 
published_at: 
fetched_at: 2026-04-25T02:04:12Z
extractor: wechat_worker
content_hash: 6bbd6057379e4d6f0057d1cf0f2718f89c2d522f9c87d9cd25aed5646b85e1fb
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7Se41N95IBLVcpBKibgfQticHt2YQGOCWTY61XgbT9T9nXC4YMdMNwv1Q/0.jpg) 

# 国际顶尖药企联合验证：开源工具 OpenFE 如何实现与商业软件比肩的结合自由能计算

原创 DrugIntel DrugIntel [ DrugIntel ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV777dmVrwfYGPaywADS9Jib3uzLJwoFxxwBGzQoiaibm8iaLwLmg7uFFIrYg/640.png)

在计算机辅助药物设计（CADD）领域，相对结合自由能（RBFE）计算是预测化合物-靶点结合亲和力、指导先导化合物优化的核心技术。长期以来，商业软件如Schrödinger的FEP+凭借成熟的算法与优化流程占据主导地位，但封闭授权、定制化成本高、灵活性不足等问题限制了其在学术界和中小企业的普及。

近日，由Open Free Energy（OpenFE）联盟主导、15家国际顶尖药企联合参与的一项大规模基准测试研究，在ChemRxiv预印本平台发布。该研究通过覆盖95个蛋白-配体系统、超1700个配体的严苛验证，证实了开源工具OpenFE的RBFE协议在准确性、 可重复性和吞吐量上已达到工业级应用标准，其 开箱即用 性能比肩商业解决方案，为药物研发领域提供了兼具专业性与开放性的全新选择。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV77LA3CKgPh6ib0CJUJH3AbKCKOKNdKO4VvOnYJ8Slp4HTURRtC1O5EFQ/640.png)

## 一、研究背景：破解RBFE计算的开源困境

RBFE计算通过炼金术转化模拟两个相似配体与靶点蛋白的结合亲和力差异，其核心优势在于能以原子级精度指导配体结构优化，减少实验合成成本。然而，该技术的规模化应用长期面临两大瓶颈：

### 1\. 商业工具的垄断与局限

主流商业RBFE工具虽性能稳定，但封闭源代码导致用户无法根据特定研究需求修改算法，高昂的授权费用让中小型研发团队望而却步，且默认参数难以适配所有药物靶点类型。

### 2\. 开源工具的验证缺口

现有开源RBFE方案多源于学术研究，缺乏工业级规模的多中心验证，存在数据兼容性差、结果重现性不足、高通量部署优化不足等问题，难以满足药物研发的严苛要求。

为填补这一空白，OpenFE联盟联合阿斯利康、拜耳、默克、罗氏、GSK等15家药企，开展了迄今为止规模最大的开源RBFE协议基准测试，旨在通过真实研发场景的验证，建立开源工具的工业应用标准。

---

## 二、核心研究设计：多维度、严标准的基准测试体系

该研究采用 公共数据集+私有数据集 的双重验证策略，从方法学严谨性、场景覆盖度和结果可靠性三个维度构建测试体系，确保结论的普适性与实用性。

### 1\. 数据集设计：覆盖从基础研究到工业应用的全场景

* **公共数据集**：选取Ross等人编译的Schrödinger 2023基准集v2.0中的58个体系（876个配体），涵盖R-基团替换、电荷变化、片段骨架等典型药物化学转化类型，排除膜蛋白、大环化合物开环等超出当前协议范围的系统。
* **私有数据集**：收集10家药企内部未公开的37个药物研发项目数据集（842个配体），所有数据经过匿名化处理，包含立体异构体歧义、结合模式不确定性、实验检测限边缘数据等真实研发场景中的复杂挑战（表3），更能反映工具的实际应用表现。

### 2\. 核心方法：模块化RBFE协议

OpenFE的RBFE协议基于混合拓扑策略，整合了多项前沿技术，形成兼具灵活性与高效性的计算框架：

* **核心算法**：采用哈密顿量副本交换增强采样，结合MBAR（multistate Bennett acceptance ratio）分析方法，平衡采样效率与结果准确性；
* **力场与引擎**：原生支持OpenFF Sage-2.2.0、GAFF等开源力场，适配OpenMM GPU加速分子动力学引擎；
* **流程自动化**：实现从原子映射（Kartograf 3D原子 mapper）、扰动网络规划（LOMAP算法）到结果分析的全流程自动化，支持CLI快速调用，降低专业门槛；

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7raN2H8qChjnNMc9kSz3N6PO7hnEZ3aS9Ig2wSF8m0GmfF82LibsQTCQ/640.png)

图1\. 计算两个相关配体间相对结合自由能的热力学循环。 通过炼金转化两个配体间差异原子，将一个配体转化为另一个配体。该转化同时在溶剂中（）和结合位点中（）进行，整体结合自由能差异。

### 3\. 评估指标：兼顾准确性与实用性的多维体系

研究采用加权均方根误差（RMSE）、平均无偏误差（MUE）、配体排序准确率（Kendall's τ）和最佳配体识别率等指标，全面评估协议性能：

* 准确性指标：重点关注 pairwise（全配体两两对比）和 edgewise（模拟边直接对比）的误差分布；
* 实用性指标：分析结果重现性（三次独立重复的偏差）、收敛速度（80%采样时间的性能平台期）；
* 挑战性指标：针对电荷变化转化、部分稠环转化等难点场景，单独评估协议的鲁棒性。

---

## 三、关键研究结果：开源协议的工业级性能验证

### 1\. 准确性：接近商业工具，满足药物研发需求

* **公共数据集表现**：加权 pairwise RMSE 为1.72（95%置信区间1.52-1.94）kcal/mol，10个系统达到亚千卡级精度（<1 kcal/mol），其中edgewise RMSE为1.37 kcal/mol，56.4%的模拟边误差小于1 kcal/mol，88.2%小于2 kcal/mol，但与FEP+相比存在差距。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7pcAE0kG3l8hqRmqYvr6gBPibISFJ8Qc4icpW1ZD0nI28TnqbX0lgNxXA/640.png)  
图2\. OpenFE和FEP+ RBFE协议在Ross et al.公共数据集上的准确性指标比较。 A) 成对（所有对所有）∆∆G根均方误差，按系统和整体加权，附带通过自举获得的95%置信区间。 B) 绝对成对误差的经验累积分布函数。 C) 协议的成对∆∆G符号估算准确性，作为实验∆∆G幅度的函数，使用0.5 kcal/mol分箱，每个分箱基部显示比较数量。
* **私有数据集表现**：受真实研发数据的异质性和复杂性影响，加权 pairwise RMSE 升至2.44（1.94-3.06）kcal/mol，仅2个系统达到亚千卡级精度，但43.1%的 pairwise 误差小于1 kcal/mol，71.9%小于2 kcal/mol，且无系统性失败模式，表明协议对真实场景的适配性。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV72ceiaaPkPXPYHu4jgQIxtOxmwXuun8fPNwprzXlkIut4ypubiaI7slTg/640.png)  
图6\. 私有数据集相对于精选公共对应物对默认OpenFE协议呈现增加挑战。 A) OpenFE的私有数据集按体系和整体加权所有对所有成对∆∆G RMSE显示，附带通过自举获得的95%置信区间。每个系统配体总数叠加在相应条形基部。 B) 绝对成对误差的经验累积分布函数。 C) 协议的符号估算准确性，作为实验∆∆G幅度的函数，使用0.5 kcal/mol分箱，考虑的对总数叠加在相应分箱基部。
* **与商业工具对比**：在435个重叠模拟边的对比中，OpenFE的 edgewise RMSE为1.32 kcal/mol，虽略高于手动调参后的FEP+（1.02 kcal/mol），但在配体排序准确率（Kendall's τ）和最佳配体识别率上与FEP+无统计学差异（p=0.25），且无需手动优化参数，更适合高通量部署。  
    
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7h1AYxx4LkUlzHmKHSR7PeLMicI3mxjhKycyhCsRbqJ21LPVLGvUibs8g/640.png)  
图3\. 公共数据集上OpenFE与FEP+（Ross et al.）结果的偏差和相关统计比较。 仅纳入22个数据集，遵循Hahn et al.标准（至少16个配体，动态范围3 kcal/mol）。显示相对绝对误差（RAE）、根均方误差（RMSE）、平均无符号误差（MUE）、决定系数（R²）、Kendall’s τ以及最佳配体分数的箱线图。星号表示统计显著性（\* p < 0.05；\*\* p < 0.01；\*\*\*\* p < 0.0001；ns 无显著差异）。P值使用Wilcoxon检验获得。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7CdlxtUWYmiaAJ8xTjxv2VkNfvZC30stWyQRVrCqIfg4rw5t18vAcpAg/640.png)  
图4\. 模拟边绝对边向∆∆G误差的经验累积分布显示OpenFE和FEP+协议，在1和2 kcal/mol处标线。 FEP+在435个重叠转化集上给出略更准确的∆∆G估算。虽然OpenFE亚kcal/mol估算少于FEP+，但在2 kcal/mol阈值下性能差异减小。

### 2\. 重现性与收敛性：工业级应用的核心保障

* **重现性**：三次独立重复模拟中，公共数据集83.5%的模拟边误差范围小于1 kcal/mol，私有数据集71.7%的模拟边满足该标准；若筛选MBAR重叠度>0.03的收敛模拟边，这一比例分别提升至88.6%和79.5%，高于行业可接受阈值。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7iawMK5W3icmK6juI5bu7r6WeyaBp8zRe8OvQbJg5edR2SBcAiaMUjPExg/640.png)  
图9\. OpenFE协议在公共和私有数据集上显示良好可重现性。 经验累积分布函数显示所有边（实线）和最小对角外MBAR重叠>0.03的边（虚线）的绝对重复间∆∆G估算。通过MBAR重叠过滤减少具有大重复间变异的异常边数量。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7It9DGjd2VQvm94mCiat5gyibIBGVia0ZmWN0x9ZvuQ3WdpibKIrSuVl67w/640.png)  
图10\. 箱线图显示公共数据集代表性按系统边向∆∆G RMSE值分布，跨1000次自举复制，使用每个边一个或三个随机选择重复的平均。如预期，三重复模拟在大多案例中导致更窄误差分布，尽管中位RMSE值平均差异<0.1 kcal/mol。
* **收敛速度**：中性配体转化在5 ns/λ-窗口、带电配体在20 ns/λ-窗口的默认设置下，80%的模拟边已达到收敛平台期，延长模拟时间对准确性提升有限（公共数据集RMSE仅降低0.01 kcal/mol），兼顾了计算效率与结果可靠性。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7BEqtUtUaQRaeZib3lvBLGcpeg3icPgM1iaQYqcK4ibzFk5zOvlNlZHNqSg/640.png)  
图11\. 边向∆∆G准确性作为总采样时间的函数分析。 A) 绝对∆∆G误差的经验分布函数显示为公共（实线）和私有数据集（虚线），作为采样百分比的函数。增加采样仅略微减少高误差边（>2 kcal/mol）的分数（公共和私有数据集分别减少2.2%和2.7%）。 B) RMSE作为采样时间的函数显示为公共和私有数据集，附带通过自举获得的95%置信区间。两种数据集均显示小准确性改进（公共0.07\[0.04, 0.1\] kcal/mol，私有0.18\[0.12,0.27\] kcal/mol），随着模拟时间增加。

### 3\. 难点场景的性能表现

* **电荷变化转化**：31个重叠电荷变化模拟边的RMSE为1.65 kcal/mol（OpenFE）vs 1.39 kcal/mol（FEP+），虽略高于中性转化，但无统计学差异（p=0.84），表明可以校正电荷转化带来的 artifacts。  
表1\. OpenFE和FEP+协议在重叠转化集及其子集上的性能概述。 RMSE和MUE以kcal/mol为单位报告。
* ![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV78PVs8uBKgG21PycZ36XMzndlhvm9sJRdIdOg5NCq87IzUBpiaG3S4IA/640.png)
* **配体对齐问题**：针对P38片段数据集的配体对齐优化实验显示，通过RDKit的open3Dalign方法进行形状对齐后，pairwise RMSE从2.06 kcal/mol降至1.52 kcal/mol，证实配体输入姿态质量是影响结果的关键因素，而OpenFE的模块化设计支持集成第三方对齐工具。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ic4J4edNYBfy0WjicR45TSV7uYFREwRdT5z8vL7a2PXdhE0HdpVVfmhokxfMTCaibz0E8CjT5zmzicbw/640.png)  
图5\. P38片段数据集由于配体对齐差导致的问题原子映射示例。 (A) 配体5 1WBW与配体3间原子映射的2D描绘。黑色原子包括在映射区域，红色原子未映射，但属于虚拟区域。 (B) 配体5 1WBW与配体3的3D叠加。差3D配体对齐导致问题映射，其中吡啶环未映射，配体3的苯环映射到配体5 1WBW萘环的“错误”部分，引入键断裂。
* **部分稠环转化**：54个部分稠环转化模拟边的RMSE达2.20 kcal/mol，显著高于整体水平，表明该类型转化仍是开源协议的优化方向，需通过键断裂支持或双拓扑策略进一步改进。

---

## 四、小结

该研究通过15家药企的多中心协作验证，证实了开源RBFE协议在药物研发场景中的工业级应用潜力。OpenFE的RBFE协议在准确性上接近商业工具FEP+，在重现性、吞吐量和灵活性上具有优势，其开源特性打破了商业工具的垄断，为药物研发提供了兼具专业性、可及性和可扩展性的解决方案。

参考文献：Baumann HM, Horton JT, Henry MM, Travitz A, Ries B, Gowers RJ, et al. Large-scale collaborative assessment of binding free energy calculations for drug discovery using OpenFE. ChemRxiv. 2025.

代码链接：https://github.com/OpenFreeEnergy/openfe

预览时标签不可点

[阅读原文](javascript:;) 

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
