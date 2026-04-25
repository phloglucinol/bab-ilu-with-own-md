---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247486288&idx=1&sn=fe6de71cca3e7da3308144afbfd5bd06
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247486288&idx=1&sn=fe6de71cca3e7da3308144afbfd5bd06
source_domain: mp.weixin.qq.com
title: 更准、更快、更稳：cPaCS-MD 实现肽—蛋白结合自由能的高精度预测
author: 
published_at: 
fetched_at: 2026-04-25T02:03:48Z
extractor: wechat_worker
content_hash: 5b5e621cc08747bffa399fee523fb7a95748c655a48c819ef07a20b92fc9c4e0
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1O2xTB2zGx14pY0UaCbzHPzjdvwoqJlQQMfkHrVNsL3kJ7DibXyR2qZw/0.jpg) 

# 更准、更快、更稳：cPaCS-MD 实现肽—蛋白结合自由能的高精度预测

原创 drugdesign drugdesign [ 药研魔镜 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA179FibDPVexBQMXibpCAdJwxibhIfdjuys9cJVXj9ZMm6ibCDOB3fZ4v82A/640.gif)

## 研究背景

肽类药物在近年药物开发中地位上升，但由于肽分子柔性高、溶剂化效应强，常规计算方法难以准确预测肽—蛋白结合自由能，限制了计算指导肽类优化的应用。为此，**作者提出并优化了一种基于并行级联筛选的分子动力学方法 —— contact PaCS-MD（cPaCS-MD），并将其与经典的 umbrella sampling（US）方法直接比较，旨在提供一个既高精度又相对高效的肽结合自由能预测方案。**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1GwpL3MKI3NWqcELed9lSia6c3JVqVj7TB2AYyJKoEIfWRf68sv69xDg/640.png)

## 研究结果

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1tfJFViaBicbRsiaeEx1h2F6MRBdRZo8dic3vfP5RYpsoqFDAEvCBUficTZw/640.png)

### 方法要点

cPaCS-MD 使用“短平行无偏模拟 → 以接触对（contact-distance）作为选取进展的指标 → 迭代筛选最“前进”的轨迹”来构建物理退结合路径，结合 tICA 降维 + Markov State Model（MSM）对轨迹重加权并计算 PMF，从而得到标准态结合自由能（ΔG°）。参数优化后推荐的配套方案为：每 cycle 9 条 100 ps 并行模拟，选取 top-3 进入下一轮。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1hlSDaRfvn3ugx7iayrPdFo8f6FL7t6cQ3AkEWI1d2qNib6vuMf8uvJ2A/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1ooWDL6DYb0N1a7fBflMHSgUH29GcNUG3ClhxW9xmBUmhicr0GpgG39Q/640.jpg)

### 基准测试结果（核心数据）

* 在一套 12 个肽—蛋白复合物（残基 ≤ 9）的基准集中，cPaCS-MD 对实验 ΔG° 的预测与实验值相关性强，四折交叉验证得到 **R² = 0.84**，均方根误差（RMSE）约 **3.4 kJ·mol⁻¹**，平均绝对误差（MAE）约 **2.7 kJ·mol⁻¹**。即精度通常优于多数物理路径法并接近小分子严格自由能方法的水平。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1yh2bqLYnzcoFHsshS1orRFWLZiayTOjHfE9gJT5ibbrMxfKCiaaAktUOw/640.png)

### 与 umbrella sampling的对比

* 在 6 个系统上直接比较时，US 在本数据集上未显示出与实验值的关联（R² ≈ 0），且误差远大于 cPaCS-MD；cPaCS-MD 在计算量上也更节省（示例统计：cPaCS-MD 总模拟量 \~29.3 μs vs US \~37.2 μs，在 GPU-day 层面也更优）。
* 原因分析：SMD→US 的路径常包含不连续的大跳（导致所取 umbrella 窗口在一维 COM 距离上看似“重叠”但结构空间实际上不重叠），而 cPaCS-MD 通过 contact-metric 与 tICA/MSM 能更好地捕获构象异质性与弱结合中间态，从而获得更合理的 PMF。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1nGuC0Dz1Vk3kKfI4vAsYKIDZ2oAT5oNC1KK6CD0DPcE9j9f1HQA95g/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1obyO9rhXtkyn6LInZfibicsVnFPic5lRNKs8JH54ghRzYJTBMt1RnZ6NA/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC4KcphaQBMXn6XTvFLTGA1ibTYZZ0K0CkfIbKVB2WDZeLc3EJJXpD3VUwibywAGLr6cR2DkTnibs4Kw/640.png)

### 方法适用范围与限制

* 方法对小/短肽（≤9 残基）、且蛋白不发生巨大构象重排的系统表现优异；若体系涉及大尺度缓慢的蛋白构象变化（例如远端全osteric 重排），则需要进一步验证和扩展。

## 研究结论

cPaCS-MD 将“并行短模拟 + 基于接触的筛选 + tICA/MSM 重加权”这一思路成功组合，**能够以较低的计算成本给出高精度的肽—蛋白结合自由能预测（R² ≈ 0.84，RMSE ≈ 3.4 kJ·mol⁻¹）**，并在多系统基准测试中明显优于常用的 umbrella sampling 方法；因此它为肽类先导分子的计算筛选与机制研究提供了一个有力且可扩展的工具。

---

_参考文献： Contact Parallel Cascade Selection Molecular Dynamics (cPaCS-MD) for Accurate In Silico Prediction of Peptide Binding Free Energy Viktor Prypoten, Raymond S. Norton, and David K. Chalmers Journal of Chemical Information and Modeling 2026 66 (1), 413-424 DOI: 10.1021/acs.jcim.5c02118_

**Github：https://github.com/chalmers-lab/cPaCS-MD\_peptide-affinity**

# 分子模拟计算和AI科研需求可联系我们

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
