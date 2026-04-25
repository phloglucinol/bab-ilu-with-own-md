---
type: raw_article
source_url: http://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247484171&idx=1&sn=c72f16241f87f36eba571996164872a8
canonical_url: http://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247484171&idx=1&sn=c72f16241f87f36eba571996164872a8
source_domain: mp.weixin.qq.com
title: 字节跳动研究突破：ByteFF力场，化学空间全覆盖的AI解决方案
author: 
published_at: 
fetched_at: 2026-04-25T02:04:38Z
extractor: wechat_worker
content_hash: 6897e31b63090a5a253fb6f5e16891e4256f23053c3b94f9265ca7ec223256f3
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/9jvm9wboRXBLmDCLwH3ju0IdL5LictRKJMPCwLEU3KQV3VaadLvcn6xJicrGkWyB9xddRpKS0oVkumuNTnpw8c9w/0.jpg) 

# 字节跳动研究突破：ByteFF力场，化学空间全覆盖的AI解决方案

原创 drugdesign drugdesign [ 药研魔镜 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

**01**

**—**

**研究背景**

文章的背景部分强调了分子动力学（MD）模拟在计算药物发现中的重要性。MD模拟能够揭示分子系统的动态行为和物理性质，以及分子间的相互作用。**力场是MD模拟的核心组成部分，它是一个数学模型，用于描述分子系统的势能面（PES）作为原子位置的函数。**随着合成化学和高通量筛选技术的进步，药物候选的化学空间显著扩展，这要求力场能够为广泛的分子提供准确的PES预测。

**传统的分子力学力场（MMFFs）通过固定解析形式来近似能量景观，具有高计算效率，但在非成对加和性非键合相互作用重要的情况下可能不够准确。**而机器学习力场（MLFFs）使用神经网络映射原子和分子特征到PES，不受固定函数形式的限制，但计算效率相对较低，且需要大量数据进行训练，限制了它们在化学空间的全面覆盖。因此，开发新的力场**ByteFF**以覆盖广泛的化学空间并保持高准确性是一个重要挑战（图1）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBLmDCLwH3ju0IdL5LictRKJDbtYrIP2afWtOZ0xmFPSEske9WKFlkA637osZgev3rtU0QE5eIa0LQ/640.png)

图1 ByteFF 的模型结构

  
**02**

**—** 

**研究结果**

文章的结果部分详细讨论了ByteFF的性能和准确性。ByteFF在多个基准数据集上的表现如下：

1. 化学空间覆盖： 使用Morgan指纹和t-SNE分析，作者展示了ByteFF训练数据集在化学空间覆盖上的优越性。这为ByteFF的泛化能力和在不同化学环境中的适用性提供了基础。
2. 扭转能量剖面（Torsional Potential Energy Surfaces）： **ByteFF在预测扭转能量剖面方面表现出色。通过与TorsionNet500和BDTorsion数据集的比较，ByteFF在预测扭转能量剖面方面的准确性显著优于其他力场**（图2）。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBLmDCLwH3ju0IdL5LictRKJsRHDVH5vTPbk6RbwEqGejHlcHzQ9ONWU1pxqe8v1a2QypKDFTSQBEA/640.png)  
    
图2 扭转 PES 在QM和力场预测之间的差异柱状图
3. 平衡和非平衡构象： **ByteFF在预测分子的平衡构象和相关能量方面也表现出了优越性。使用OpenFFBenchmark数据集，ByteFF在预测分子几何结构的准确性方面优于其他力场，这确保了在MD模拟中正确采样局部** **最小值**（图3，图4）。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBLmDCLwH3ju0IdL5LictRKJliajppBWV08UibWibVGsxy9dNwhdGoGYnic0VvSPnicOfEedbuLqZRVibsIA/640.png)  
图3 OpenFFBenchmark 不同指标的柱状图  
    
图4 分子平衡构象预测实例
4. 能量和力的预测： 在非平衡构象的能量和力预测方面，**ByteFF-gopt在没有使用力标签训练的情况下，仍然取得了比GAFF-2.2和OpenFF-2.0更高的准确性。**通过在较小的非平衡数据集上进行微调，ByteFF-joint的性能超过了其竞争对手（表1）。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9jvm9wboRXBLmDCLwH3ju0IdL5LictRKJxUNq9gzCtXGGibZhPpHhOblTdZasZNQicvjrc3l7rD7KQgEjIyEIoS3Q/640.png)  
表1 不同力场在不同数据上的能量和力的比较

  
**03**

**—** 

**研究结论**

在这篇文章中，我们成功开发了**ByteFF，这是一个与Amber兼容的分子力学力场，它不仅在多个基准测试中展现了卓越的性能，而且在广泛的化学空间内提供了前所未有的覆盖范围和准确性**。ByteFF通过利用先进的数据驱动方法和精心设计的图神经网络模型，能够精确预测扭转能量剖面、平衡构象以及非平衡能量和力，这对于生物分子模拟和药物发现领域来说是一个重大突破。

---

**_参考文献：_** _**arXiv:2408.12817 \[cs.LG\] (or arXiv:2408.12817v2 \[cs.LG\] for this version) https://doi.org/10.48550/arXiv.2408.12817**_

****计算和科研需求可联系我们！**

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
