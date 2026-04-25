---
type: raw_article
source_url: http://mp.weixin.qq.com/s?__biz=MzUxMjkzNTgyOQ%3D%3D&mid=2247488798&idx=1&sn=8e649e59a9667d5e8d08c0606ee91924
canonical_url: http://mp.weixin.qq.com/s?__biz=MzUxMjkzNTgyOQ%3D%3D&mid=2247488798&idx=1&sn=8e649e59a9667d5e8d08c0606ee91924
source_domain: mp.weixin.qq.com
title: LigPath: 模拟配体从蛋白活性空腔中的解离路径
author: 
published_at: 
fetched_at: 2026-04-25T08:07:56Z
extractor: wechat_worker
content_hash: 745a869b424c38794669546ad7f0dfcf6c9e04e827948075e61ef52d917b3f4c
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1lffQibpgpCLibExjCcibOIaSdDIu6B2ibxOia60kuETLoylwgtOaasjMgww/0.jpg) 

# LigPath: 模拟配体从蛋白活性空腔中的解离路径

原创 药研猿 药研猿 [ 药研猿 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![Image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/JK3OqyrWaAUGLY50ZsxwX2ibogGxC41icaiaWDb7l2Iv0wZSBNlpM5Avia2d1RBOj5IRwD68DDUFxxDibTX8fiak01KQ/640.png)

点击上方蓝字加入我们

  
**MoMA-LigPath** 是首个模拟蛋白质-配体解离的网络服务器，基于分子机械表示和机器人运动规划算法（ML-RRT），通过解耦主动变量（配体位姿、键扭转角）与被动变量（蛋白质侧链扭转角）探索构象空间，仅需秒级至分钟级计算时间。用户上传 PDB 文件后，可设置分子柔性参数，输出包含解离路径的PDB 文件、接触信息及执行报告，免费开放给用户使用。

网址：**http://moma.laas.fr/applications/LigPath/**

在开始操作演示前，大家先看一下最终效果：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb12jibzLOIcFMJKH3Kvp28CX7IE5aOhzqoyee2wAzMricHia5nvmJNGgjUg/640.gif "null")

本文用到的示例文件以及用到的脚本文件都可以通过后台回复 **“250516”** 自取。

## 1\. 准备蛋白-配体复合物结构

复合物结构可以来自实验解析的，也可以是通过分子对接得到的。总之上传之前需要确保结构中的氢原子去除干净。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1icMEbMLflLyBPib7sIibCe6LhustFSkicdymTFUtiaO8V4EYs8BicoZJUKAQ/640.png "null")

## 2\. 上传复合物

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1OhF5Sx5eMroPaLRnDbibpvb97tgbJKhL1UVSX5zsruxbCCVea5IpFvA/640.png "null")

  
在上图中，我们可通过调整 softness 参数控制配体解离路径的搜索策略：较小的值（如 0.6）允许更激进的构象探索，适合寻找隐蔽的结合口袋；而较大的值（如 0.9）更接近物理真实，适合验证已知结合模式的解离路径。这种灵活性使算法能在不同场景下平衡速度与准确性。在本例中，我采用了他的默认参数：0.7

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1IgkvGiaTLTEHkVfPVUkN8XZlLcjkuFEtibs0Ip1P3hwzHyzqLfCbX37A/640.png "null")

另外一个重要的参数是解离路径个数的设定。最大可以设置20（即结果返回给你20种可能的解离路径）。测试中我设置了一条，运行时间接近三小时，如果设置多条可能等待时间还会更长，根据需求自行把握！！！

  
## 3\. 结果查看

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1WwQLT0X4yk2nDp2ekQOpINW1gvlUebED4meT0gPjXrYb0z7RuJFaEQ/640.png "null")

  
下载结果文件到本地后解压，你会看到如下结果：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1jqdbSzd5KfRRvA8JXxIclLAe2iaZdhT6g2ziaF91V8XOt95vibkZN0tVg/640.png "null")

  
上图`Path_1`中包含的就是解离路径中的所有pdb文件。如果你在上一步设置了多条解离路径，最终结果会出现多个文件夹，每个文件夹中表示一种解离路径。

打开`Path_1`后，你可以看到包含很多用数字命名的pdb文件，他们是配体解离过程中每一个阶段的“快照”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1zgtr9OK2Lux0tNtOZMhd1G7AicicRgYD1QD1fb6dI7Ryfd4vD2Yd8I6g/640.png "null")

我们可以尝试用pymol同时打开所有的pdb，结果如下图所示：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1bBvxMGl2VPkVVP7vVdrOQ96EPK2YZKyPibKWpicv2ggrh4gibwppEdrzA/640.png "null")

这么查看是不是不直观？  
不急！使用我为大家准备的bat脚本文件可以轻松应对：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1ibta25c8t9e1Entibz19aZugS4kaa8mjL8W0OicWf5OY9bZpmeqcYzmFg/640.png "null")

  
将上图中的脚本文件拷贝到`Path_1`文件夹下，双击即可运行。运行过程中会弹出命令窗口，不要主动关闭。待到运行结束它会自行关闭。

运行结束后，当前路径下出现一个新文件，名为`merged.pdb`。用pymol打开：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1Vw7YyH7XNhCMlHBhtPM8NnnTjysuGiaXqQya1ia91ErkjfbqthaO2l4g/640.png "null")

我们设置一下显示样式：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb1lM2DwDzyaiat0jeXkAE3vtGWR5DbxrMtr6CibaFwibEXC4bjBZaicy8TWA/640.gif "null")

最后一步，让小分子动起来吧！！！

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/tTsYdQUMxewibQY6FTkFAQ8HtibT97Ovb12jibzLOIcFMJKH3Kvp28CX7IE5aOhzqoyee2wAzMricHia5nvmJNGgjUg/640.gif "null")

  
若想在自己的文章中使用此工具，你应该引用如下文献：  

D. Devaurs, L. Bouard, M. Vaisset, C. Zanon, I. Al-Bluwi, R. Iehl, T. Siméon, J. Cortés. “MoMA-LigPath: a web server to simulate protein-ligand unbinding". _Nucleic Acids Research_, 41(W1):W297-W302, 2013\. https://doi.org/10.1093/nar/gkt380 , https://hal.laas.fr/hal-00843321v1
  
  
---
  
  
「往期推荐」

[预测蛋白质溶解度,科研神器：Protein-sol](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxMjkzNTgyOQ==&mid=2247488750&idx=1&sn=099aca985781fae334007eea49216d4a&scene=21#wechat%5Fredirect)

[InDeepNet——革新PPI药物设计的蛋白质结合位点预测平台](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxMjkzNTgyOQ==&mid=2247488703&idx=1&sn=cf275e0a6a0de21d8074d07b3102d5f2&scene=21#wechat%5Fredirect)

[推荐一种使用ChimeraX渲染蛋白-配体复合物的方法](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxMjkzNTgyOQ==&mid=2247488748&idx=1&sn=f2a9c2b004e3d19a07c4d728ec2c5a15&scene=21#wechat%5Fredirect)

  
感兴趣的读者，可以扫码加入**读者讨论微信群**。

![Image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxezT1C6p0puU9ibZbXBN2ITZdK3wibNkwRbiacf1dN8SqAmXibeFhpxbo2h0e5RpMrFC66uvwgl2sBdvbQ/640.png)

---
  
  
![Image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/PekErwtg4WKmwH3eibyzzq6s8Y3mAfMqgg4oMDqNdgewSt6icvABmJGpFQ45Bic3oZZx5iaVXrYiasFZttZOx1ticcRg/640.png)

点个在看你最好看

![Image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/lNwjBmeZOpwtYL4m6wWia6fPCyrOZiaygfADsajMnp7pkAQE6vg8w3bG9iae1AribdH3EQkrcO6ziaDhcBpl7ksCEkA/640.png)

  
预览时标签不可点

修改于 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxexISa8UZWibSfgR0KsHzZUC82Yibvouic0F4lB4icVe0gzWYgx2auiciaIjFibuNscmVA6lA5hu1eJibVs5Jg/0.png) 

 药研猿 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/tTsYdQUMxexISa8UZWibSfgR0KsHzZUC82Yibvouic0F4lB4icVe0gzWYgx2auiciaIjFibuNscmVA6lA5hu1eJibVs5Jg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
