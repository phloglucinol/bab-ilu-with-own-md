---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247485683&idx=1&sn=564443b02f64f5777a2bca967e0b10e5
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247485683&idx=1&sn=564443b02f64f5777a2bca967e0b10e5
source_domain: mp.weixin.qq.com
title: FEP Ω：把高精度自由能计算变成“即插即用”的引擎
author: 
published_at: 
fetched_at: 2026-04-25T02:05:40Z
extractor: wechat_worker
content_hash: 746be97bbf00d88704c17fe496c32722e4fb7a7978e3f82ed56c40703a251153
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/9jvm9wboRXBcX52wDRlabplGFntWicib4F2LwWoQtKCCGqBzxt7Z5Ippoiapf2J64U2PbacRPUqtJrO0OqEibuiavng/0.jpg) 

# FEP Ω：把高精度自由能计算变成“即插即用”的引擎

原创 drugdesign drugdesign [ 药研魔镜 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/9jvm9wboRXBcX52wDRlabplGFntWicib4Fd1v61DwAXQxDphsicpK3TwRxYWpzXMKetlTadAiceTyTenqxqmib4iaNyw/640.gif)

---

## 研究背景

自由能扰动（FEP）一直是结构基础药物设计中预测配体结合能的金标准，但通常需要大量的参数调优与复杂的 alchemical 网络修正，导致耗时高、难规模化应用。为了解决“高精度但难以实用”的矛盾，作者提出了一套全新的 **ML-native 平台——FEP Ω：在标准化、自动化的短时模拟（无 alchemistry、无回环修正）基础上，使用机器学习对模拟产物进行后处理修正，从而在大幅降低计算量与人工调参的同时，保持或超越现有商用实现的预测精度。**

---

## 研究结果

### 1) 平台设计与关键组件

* 作者将整个流程标准化为三步：自动化预处理 → 标准化短时 MD 模拟 → 基于仿真时序特征的机器学习后处理修正（active learning）。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/9jvm9wboRXBcX52wDRlabplGFntWicib4FfIjOG2A3qOOFtuVibbUMeE3picl4O2UhdAsWmmaUIcibm4ZEficTReMbmA/640.jpg)
* 在力场参数化方面，提出了**Q-Unity**框架：通过 xtb 等量子力学计算直接为蛋白与小分子生成参数（不依赖查表）。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBcX52wDRlabplGFntWicib4FBh0w2XabgAjssj82sF0T820OpUobSofWmjCvytkhria8CQM3TibCxKNQ/640.png)

### 2) 启动结构质量对 FEP 表现的影响

* 作者提出了“原子重叠（overlap）”度量用于评估起始构象与变换体的对齐质量，回顾性分析显示重叠度低的起始构象通常伴随较低 RMSE（p38 系列示例）。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/9jvm9wboRXBcX52wDRlabplGFntWicib4FFkmHEpI372QhDE3ib8rbC3s04e89s1uKGibCLBDptcgZbw5SHQYHLYZg/640.jpg)

### 3) 模拟时长对 ML 校正性能的影响

* 在 HIF2α 数据集上，作者对比了不同生产模拟时长（分段到 5 ns）对 ML 校正后预测精度的影响。结果显示：**即使在非常短的模拟时间（如 1 ns）下，模型在 RMSE 与 Spearman 排序上已接近或低于 1 kcal/mol，且在多数时间点能达到亚 kcal/mol 误差。**这表明短时、标准化的物理模拟+后处理 ML 能快速给出可用预测。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBcX52wDRlabplGFntWicib4FnT2nLLIfOfQc6GtZ9O8ljrqnVawt63sA80nDK4PhPgatJia1VMjPsmA/640.png)

### 4) 外推能力——scaffold hopping

* 在 HIF2α 的 scaffold-hopping 试验中（用两套化学系列训练，第三套独立测试），RB FEP 与 AB FEP 均表现稳健：独立测试集 RMSE 从 0.590 降至 0.558 kcal/mol，说明 ML 校正学习到的是系统性偏差而非对 scaffold 的记忆性拟合。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBcX52wDRlabplGFntWicib4Fr2XltRWic9Q7mZK3MEIv5b42Ll10YetmqEDttHaoRpHT3aulDpDgq0Q/640.png)

### 5) 与行业基准及盲测结果

* 与 Schrödinger FEP+（包含人工或 Protocol Builder 调参）比对：在 BACE1、P38、MCL1 三个常用 benchmark 上，FEP Ω 在 1 ns 简短模拟下，RMSE 常比 FEP+ 低 30–40%，并保持良好 Spearman 排序。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBcX52wDRlabplGFntWicib4FSRNn7oxicUPAibmrDibZ5GHrRuJ7b84xYib4S1GvoC4VSxia8lEzqria8rvQ/640.png)
* 在盲测的 DPP-4（无 FEP 先例）回顾性评估中，作者用 24 个训练样本构建 ML 校正，结果在独立测试上实现 Spearman Rho > 0.7、RMSE ≈ 0.6 kcal/mol。这说明该方法在真实、未知目标上亦有良好推广能力。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBcX52wDRlabplGFntWicib4FS3doreRrbnT5W7LEO7MwpPHM1xthbtujIyRpiaQKcB7gRG7tQ6pkKXw/640.png)

---

## 研究结论

FEP Ω 通过**标准化短时 MD + 基于仿真特征的机器学习后处理**，在**无需复杂**预调参数与 alchemical 网络修正的前提下，**实现了与甚至优于现有商用 FEP 实现的预测精度**（多数情况下达到亚 kcal/mol 误差），同时将计算成本和人工维护显著降低，从而把高精度自由能计算变为可在药物发现流程中“及时”、常规化应用的工具。该框架通过 Q-Unity 的第一性原理参数化与闭环的 ML 校正机制，为把 FEP 从研究级工具转化为工业级、可量产的设计引擎提供了可行路径。

---

_参考文献：Giannakoulias S, Ferrie J, Apicello A. FEP Ω: The End of Parameter Tuning. ChemRxiv. 2025; doi:10.26434/chemrxiv-2025-bg1t9 This content is a preprint and has not been peer-reviewed._

# 计算和科研需求可联系我们

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/9jvm9wboRXAzkPaUEbSvyorwhuOrMnE5D5TYZXQOMJM3qOBCWy5fVicYic6n0qs2onIAMyarHwkSKE3YcobChwFA/640.gif)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXDtOEbnagWTNKQsZ1U1Rdv8OibE6MtsSLWTicIqSkBqYTosgBUrGBTMRgiaHtddKcbsaI5JdYyicc4GCA/640.png)

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC2Z2N1KlQX5nYngmYeQaBNPIa3WvarWwkcNgKF4ia5cYuVmhP0WLoYic73YgA1x2zzx1PYtHzL0WVw/0.png) 

 药研魔镜 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC2Z2N1KlQX5nYngmYeQaBNPIa3WvarWwkcNgKF4ia5cYuVmhP0WLoYic73YgA1x2zzx1PYtHzL0WVw/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
