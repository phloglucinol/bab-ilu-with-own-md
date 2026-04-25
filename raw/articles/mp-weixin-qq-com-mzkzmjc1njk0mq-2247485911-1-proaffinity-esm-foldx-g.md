---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247485911&idx=1&sn=abf39f59ecdef4ad63885b2e51a26640
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247485911&idx=1&sn=abf39f59ecdef4ad63885b2e51a26640
source_domain: mp.weixin.qq.com
title: ProAffinity++：将 ESM 表征与 FoldX 能量项融合，提高蛋白质 ∆G 预测的捷径
author: 
published_at: 
fetched_at: 2026-04-25T02:04:24Z
extractor: wechat_worker
content_hash: bc7cf67288a17e82521dbd0e87dafc96d835a7dceb2dc971757d49a37555e160
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/9jvm9wboRXC3boeqzZibgdT5m3TBatBDBPUibf6HLXahCMxTWpfIsibCHpf4IyfDnAicm0r2GSRBYM7JiaibcQt0QG6A/0.jpg) 

# ProAffinity++：将 ESM 表征与 FoldX 能量项融合，提高蛋白质 ∆G 预测的捷径

原创 drugdesign drugdesign [ 药研魔镜 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/9jvm9wboRXC3boeqzZibgdT5m3TBatBDBX71zXnTgJAkEsZxsNyM3dfktgKx1rfbZBzBfKYpUGzeMgfKWTLT3Vg/640.gif)

---

## 研究背景

蛋白-蛋白相互作用的结合自由能（binding affinity, ∆G）是理解生物过程与药物设计的关键热力学量。传统生物物理实验（如 SPR、ITC）准确但耗时，现有计算方法（分子动力学、经验能函数、机器学习）要么计算昂贵，要么在泛化性与界面细粒度建模上存在不足。**为了解决这些问题，作者提出了 ProAffinity++：一个结合序列与结构预训练表征、以结合区（binding region）为单位构建二部图并用图神经网络捕捉残基局域微环境的端到端结合亲和力预测方法。**

## 研究结果

* 总体性能：在多个基准（PDBBind、Affinity Benchmark）上，ProAffinity++ 超过了 FoldX、Prodigy、PPI-Affinity、PIPR 等方法。论文给出的分表显示，使用二元复合体训练集合 S653 与多组分复合体 S1902 联合训练时，ProAffinity++ 的 Pearson ≈ **0.594**、Spearman ≈ **0.567**、MAE ≈ **1.650 kcal/mol**。在另一组 PDBBind 的评测里作者报告的最佳 Pearson 可达 **0.676**，Spearman **0.812**，MAE **1.455 kcal/mol**。
* 突出场景：在抗原-抗体（AT-Bind）与点突变变化（SKEMPI）任务上也表现稳健。对于突变导致的 ∆∆G 预测，作者展示了预测值与实验值的散点对比图（图 1），并在 AT-Bind / SKEMPI 上给出 Pearson（分别约 0.551 / 0.697）与 MAE 指标，表明模型能提取到部分变动信息但 ∆∆G 的线性假设仍有限。  
![ProAffinity++ 在 ∆∆G（突变）预测上的散点对比](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC3boeqzZibgdT5m3TBatBDBEkkZkcRmUHfmRicexuTqXLfAC4098of7uhkBe80lrahyf5F7StcibPDQ/640.png)  
ProAffinity++ 在 ∆∆G（突变）预测上的散点对比
* 模型与设计要点：ProAffinity++ 将结合区建模为**二部图（bipartite graph）**，节点特征融合了 ESM-1v（序列表征）、ESM-IF（结构逆折叠表征）、AAindex、FoldX 物理能项、DSSP/侧链信息等，随后用 MPNN 更新节点表示并通过 MLP 回归 ∆G。  
![ProAffinity++ 模型概览](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC3boeqzZibgdT5m3TBatBDBCXna9Mic22IWzqqxTic2BN49tujJm9URKRqmJ6h0BeahBoXMXhIUo2gA/640.png)  
ProAffinity++ 模型概览
* 消融/解析性实验：  
![不同图类型与距离截断对性能的影响](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXC3boeqzZibgdT5m3TBatBDBlctobEbdbr4iaj96icatpfMCe4FBJORyqURcOib5RXSqX6qd3a3iakcgyg/640.png)  
不同图类型与距离截断对性能的影响
   * 特征重要性：去掉 ESM-1v 后性能显著下降（完整模型 Pearson ≈ **0.654** → 去 ESM-1v 后 **0.496**），说明序列预训练表征对预测贡献很大。去掉 FoldX 的物理能项也会明显降低性能，表明物理先验仍有补偿作用。
   * 图构建与数据增强：以二部图建模优于无图或无向图；通过对节点注入高斯噪声与不同距离截断（4.0–5.0 Å）构建多种训练样本可提升鲁棒性。

## 研究结论

**ProAffinity++ 通过将序列与结构的预训练表征、物理能量项与基于结合区的二部图 GNN 有机结合，显著提升了蛋白-蛋白结合亲和力预测的准确性与泛化能力，尤其在多组分复合体与抗原-抗体/突变预测任务上表现突出。** 作者同时指出可进一步通过加深网络、引入更多构象数据（如非结合态构象）与扩充训练集来继续提升性能。总体上，ProAffinity++ 为高通量、相对快速的结合能预测提供了一条可行路径，对药物发现与蛋白工程具有现实应用价值。

---

_参考文献： ProAffinity++ Keyu Xu, Zeyuan Di, Jianquan Zhao, Haicang Zhang, Dongbo Bu bioRxiv 2025.10.31.685718; doi: https://doi.org/10.1101/2025.10.31.685718_

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
