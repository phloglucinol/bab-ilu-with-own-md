---
type: raw_article
source_url: http://mp.weixin.qq.com/s?__biz=MzkwMjUyNTY1Mg%3D%3D&mid=2247483922&idx=1&sn=2fbd9876253669f4bc103bc63b3db068
canonical_url: http://mp.weixin.qq.com/s?__biz=MzkwMjUyNTY1Mg%3D%3D&mid=2247483922&idx=1&sn=2fbd9876253669f4bc103bc63b3db068
source_domain: mp.weixin.qq.com
title: 透过SVD理解：为什么“降维打击”不可逆
author: 
published_at: 
fetched_at: 2026-04-25T02:04:36Z
extractor: wechat_worker
content_hash: 27c0d150f6c58f26aa8b61c1835e9bbb7b74e3cacf4735d5be20da176a8ef558
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/ib6f7Y90VS4Bibv7qo0HQKCa3LgRuFSFezf6bBvBF7nibaPluHTLmdmUmvABFiaLKcEkdGbl2NwOiaa1HuluYIPibRibg/0.jpg) 

# 透过SVD理解：为什么“降维打击”不可逆

原创 乔利Joly 乔利Joly [ 计算机视觉研习社 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

 大家还记得《三体》中，歌者文明通过“二向箔”对太阳系实施的降维打击吗？我不知道随着科技的发展，降维打击会不会真的有一天发生在物理世界中；但是，在今天的数字世界中，“降维打击”无时无刻不在发生着，而且它有着非常广泛的应用场景和现实价值。今天我们就和大家一起透过矩阵奇异分解（SVD）来聊聊，降维打击究竟是怎么回事。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4Bibv7qo0HQKCa3LgRuFSFezopnrpcTRGQwotujTZdgiaOPVYOvU2Z64CpDXuicQevfvY9M529wpWX9Q/640.png)

1\. 什么是SVD?

 有工科背景的同学，一定都接触过线性代数。知道一个矩阵（方阵）是否可逆，与它的行列式是否为零（是否是奇异的）有关；并且矩阵的研究与线性方程组的求解有直接的关系。

 那么大家是否想过，如果线性方程组中未知数的个数少于方程的个数，或者系数行列式的值为零，又该如何求解呢？

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4CShtJ3StbqKs87K1dSEyxzjeCSQ3Ft3VtMfdOaQfLcj5ibWMrMvSFBgStzZMIFIG0b9ARDk53PB8Q/640.png)

 上面要求A的转置左乘A是可逆的，但如果它不可逆（对应着某些线性方程是其他线性方程线性组合的情况）呢？终于轮到我们的SVD登场了！

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4CShtJ3StbqKs87K1dSEyxzQeF5A0IU9jhW4Uc5InlpXdIOPdOUf6WXcQpDhFXJnUV38b5Ss1Goxw/640.png)

 以下代码示例，给出了求解前文给出的线性方程组的两种方法：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4CShtJ3StbqKs87K1dSEyxzMm4lJyrGSkBvCic92lWkdhKkS9XtE4HsuwP45N5h7AYjcjTWZ3fJV9w/640.png)

2\. 如何实现SVD?

2.1 基于特征值分解的方法

 当看到SVD的定义时， 大家一定会有种似曾相识的感觉：单位正交阵，对角矩阵……。没错！在矩阵特征值分解和相似对角化时，遇到过类似的问题。下图中红色圈出来的表达式是否有那么一点点SVD的神韵了呢？

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4CShtJ3StbqKs87K1dSEyxzicpYaQdSQ4GrCLnclMhtovw0GLBU8p4WxAIpwvHMHkcEibhEjnpJzgPA/640.png)

 再回忆下第1小节中构造最小二乘法求解求解线性方程组时，用到的A的转置左乘A （实对称矩阵），通过这些线索，基本上可以拼凑出一种对矩阵进行SVD分解的图景了。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4B9MgNcxaacy32CjrwxEa2zpboItG5UPEOKibxeQtPnWygsr3RTGQkQgcGib5T1GosyUF9ghO3h73ag/640.png)

 至此， 该方法的原理就不言而喻了，请看下面的实验：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4B9MgNcxaacy32CjrwxEa2zpicXL3X646YAGCyzNIY0orln2W2VnxbtiaG9tla34t6ChFMg3zB9zdtg/640.png)

 细心的朋友可能会发现我们的计算结果与numpy的计算结果并不完全一致：某些列相差一个正负号。这种情况是正常的，根据特征向量的定义，当特征向量乘以某个非零标量，依然是矩阵的特征向量。为了保证根据特征值分解得出的u, sigma和 vt满足SVD的定义，可以统一约定每一列第一个非零元素为正数。我们这里在得到左奇异矩阵和奇异值之后，直接通过矩阵运算求出vt, 没有进行两次特征值分解计算。

 这种对矩阵进行SVD的方法比较直观，容易理解。但也有不足：由于要计算A的自相关矩阵，涉及元素的平方，数值稳定性不好。 因此，在实际工程应用中，这种方法用的比较少。

2.2 基于幂运算的方法

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4B9MgNcxaacy32CjrwxEa2zfAmKFNzAHtTqKcgUIQAuhdZ9gww6OWznmknnhh2cib7DdeHlEH4f0og/640.png)

 通过上面的推导，可以看出，对于任意的非零向量，经过多次左乘矩阵A得到的向量x\_k 会趋近于主特征向量的方向，当迭代次数足够多时，也可以估计主特征值。

 接下来我们简单分析一下基于幂的方法进行SVD时用到的一些小技巧：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4B9MgNcxaacy32CjrwxEa2zsExH6tbKZWB3OD5wAvJNqT25vSEeWpe19gy2eZWtdvX3bQCZXc19dA/640.png)

 基于幂方法的SVD实现如下：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4B9MgNcxaacy32CjrwxEa2zicNs2h4XqgrMS81ApNiabYniapPy8WkTOYibMbjp61jBSPk08UPiaK0ia0MQ/640.png)

 需要注意的是，该方法也有一定的限制，若特征值的之间差别不大时，算法可能面临无法收敛的情况。

2.3 基于QR分解的方法

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4AgdyZdrxXBpxVpyuKTNch947eoiaOg4L0p3Cm19nTGJbiayOhHn19GKuOhoJlZNxRz2KMYLROiahk4w/640.png)

 下面的代码示例，给出了基于施密特变换进行QR分解，并用它来计算矩阵的特征值的过程。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4AgdyZdrxXBpxVpyuKTNch96SrHQODIgibgVhzR45P5mQ2iaibFI07qYOEBOr9HFVwjdtGQqHI4JFFsA/640.png)

 在2.1中，我们介绍了基于特征值分解进行SVD的思路，而基于基本QR分解做奇异值分解也是通过进行特征值分解进行的。自然而然绕不开自相关矩阵，可能导致数值不稳定的情况。 对此，可以参考householder变换方法，它避免了数值不稳定的情况，也是应用最广泛的一种SVD方法，感兴趣的小伙伴可进一步研究。

3\. SVD的应用

3.1 SVD用作数据压缩

 在基于幂运算的SVD方法中，每迭代计算一个主特征值和特征向量之后的矩阵收缩过程，其实已经用到了SVD做矩阵近似的思想。 对于一幅图像而言，将其进行奇异分解后，取前top\_k的奇异值重新构建，就可以达到对图像压缩的效果， 如下图所示：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4CxgHjCuDME84DC1UGYe1xUNVv0bYmmGiaib0c0oK92tbdcalQy31zibPqj5aKEHSlQice2micibqJCnr5g/640.png)

 通过调整top\_k的值,可以达到不同的压缩程度。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4CxgHjCuDME84DC1UGYe1xUebv9134icsdlVxiaZIAEyyonTEibRtsOKF5LNAUyJO1JSmKYq0Mp3Atdw/640.png)

3.2 SVD用作降维

 终于到降维了。降维操作对于高维数据的分析、降低模型复杂度、提高泛化能力有着重要的作用。例如，下面的例子中，我们对随机生成的5维数据采用k-means进行聚类，并将结果通过降维技术进行可视化：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4AgdyZdrxXBpxVpyuKTNch9VQDUVbOh1fKOuFe4M8FBykfZQSopmApfHiaXrDldZZ2zPe6mI5aZKNQ/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4AgdyZdrxXBpxVpyuKTNch9q0qZ9mAGhThMeSM3ibt0iaqwywz1GCWW44QfU2ia7iawa7nCfViaqKucSnQ/640.png)

 众所周知，PCA也是一种主要的降维技术。在此我们将SVD与PCA就降维方面的差异做一个简单的对比：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4AgdyZdrxXBpxVpyuKTNch9sE8cdxL0DAF2WFgFTbKj8udqib0ry1uJV9sGKNnfvpEUgvsABbq9uUQ/640.png)

3.3 SVD用作旋转分解

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4AgdyZdrxXBpxVpyuKTNch9COfia2JR0Uf9aXgGzToSXricHhM3YoCswxWV2paSQejpaR1ntFnG5LTw/640.png)

 将旋转矩阵进行SVD分解，可以得到两个独立的旋转矩阵。在处理机器人的复杂运动规划、运动学习与优化，视觉任务重的姿态估计与追踪，图像配置等方面，有着重要作用。

4\. 结束语

 回到文章最开头问题，为什么“降维”打击不可逆？根据我们对对SVD原理及其应用的分析，可以看到在降维过程中，丢失部分维度的信息，而丢失的部分信息是凭借现有的技术是无法找回的（除非在将来某一天，人们发现零点场假说是成立的，并有办法从虚空中恢复出那些缺失的信息，“降维”打击或有可逆的一天）。

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4Ba0eM9KF4XFc7EFLINLibTs8CfdzS3TX8FTqmocLest4dEe9icrhPpMF5WFicIUdhJ1dX8xN4lKFWcw/0.png) 

 计算机视觉研习社 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ib6f7Y90VS4Ba0eM9KF4XFc7EFLINLibTs8CfdzS3TX8FTqmocLest4dEe9icrhPpMF5WFicIUdhJ1dX8xN4lKFWcw/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
