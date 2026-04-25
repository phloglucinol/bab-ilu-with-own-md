---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247486105&idx=1&sn=e0fed97b5cea69f20dcb90f09f1376e2
canonical_url: https://mp.weixin.qq.com/s?__biz=MzE5MTE0Njg3NQ%3D%3D&mid=2247486105&idx=1&sn=e0fed97b5cea69f20dcb90f09f1376e2
source_domain: mp.weixin.qq.com
title: 给分子电荷“称重”的GPU快进：一转就是一辈子，现在只需一眨眼
author: 
published_at: 
fetched_at: 2026-04-25T02:03:33Z
extractor: wechat_worker
content_hash: 4fc39e33a6bcaa9dc3228a543bfcdeb13ae38158e881e066e4bdebdaf02d54c8
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/9azMKawwL0eEQEGIFCps6GJibfYcz4auOrCwBA3056LwV9zAia6vQYD9ZpnZjASAsPck45ibSXxSotDzR8yWwOgCXPEj2yJ1ibRPZkVpChYku24/0.jpg) 

# 给分子电荷“称重”的GPU快进：一转就是一辈子，现在只需一眨眼

原创 Re Re [ 计算材料视界 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

2026年3月7日，美国加州大学圣地亚哥分校超级计算机中心的Andreas W. Götz团队联合Kenneth M. Merz, Jr.、Francesco Paesani等，在国际顶尖化学期刊《Journal of Chemical Information and Modeling》上发表研究论文，在开源量子化学软件QUICK中实现了GPU加速的静电势计算，并提出了全新的“重加权RESP”电荷模型。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9azMKawwL0cVfc0dF1zPSCQVdCGv4KJPpbjU9L9XMiaAqL9icCL13kf3VWukM8blh89iaCnicicRPqibqfjGWM3gxGBLAibQutlDkzicV53szYziaJ4M/640.png)

**研究问题与背景**

分子模拟的准确性，很大程度上取决于原子电荷的质量。静电势拟合电荷（ESP）和它的“ restrained”版本RESP，是力场开发的黄金标准。但这里有个尴尬的问题：**电荷值会随着分子在空间中的朝向而改变**——同一个分子，转个角度，算出来的电荷就不一样了。

过去几十年，人们用各种办法减轻这种“朝向依赖”，比如设计更聪明的网格、或者对多个朝向取平均。但根本原因其实很简单：网格不够密。问题是，网格加密意味着计算量爆炸——传统CPU根本扛不住。于是，大多数人只能凑合用粗糙的网格，忍受电荷的不确定性。

**方法与创新点**

团队的解决方案简单直接：**用GPU硬算**。他们在QUICK中实现了一套高效的GPU算法来计算静电势，把计算分布的逻辑从“按壳层对分配”改成“按网格点分配”，让相邻线程处理同一个壳层对、不同网格点，大幅减少了内存写冲突。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9azMKawwL0cXyfhwnwicUUEMmQjvUOaLcXAh66YaPpVibqibTF1BXaHFMYxA4sUM8WOIsz6cLw9CCibQWuLnSgVBMpKibIjffbjfoXd2ibtNc3eEI/640.png)

**图2\. 静电势计算的网格生成过程**  
_(a) 获取原子的范德华半径并缩放；(b) 在缩放后的范德华表面上生成均匀分布的球面网格（默认间距0.25 Å）；(c) 按不同缩放因子生成四层这样的表面；(d) 用于ESP电荷评估的代表性网格；(e) 部分分层单独显示以便观察。_

结果相当惊人：**单张NVIDIA A100 GPU，比128个AMD EPYC CPU核心还要快7-9倍**。当网格细到0.05 Å（每原子约2万个网格点）时，ESP计算甚至比12圈SCF迭代还耗时——但GPU依然能扛住。

**关键结果与意义**

有了GPU撑腰，团队终于可以回答那个老问题了：网格到底要多密，电荷才能不看分子脸色？

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9azMKawwL0eTc3ZYde8rydrhEGH5LVIZvyDI09Cw9v2Mt6uEicDwl5cNPY9jW9uwYhOZxPgADyxzTdNwYViaMno2ANXlU2QFXFicunoicCCmjtI/640.png)

**图6\. 不同朝向下的电荷变化范围**  
\*绿色部分（QUICK实现）随着网格变密（Sgrid从1.00降到0.05 Å），电荷变化范围从\~0.07 e一路降到<0.01 e，与朝向几乎无关。相比之下，GAMESS中几种常用网格（Connolly、geodesic、CHELPG）的电荷变化范围在0.1-0.2 e之间。\*

但RESP电荷遇到了新问题：网格越密，原来的约束权重被稀释，电荷值开始漂移。团队提出了**重加权RESP（rwRESP）**，让约束强度随网格点数等比例放大——默认网格0.25 Å对应的权重因子是17.0。这样，rwRESP电荷既保持了RESP的优点（避免埋藏原子电荷过大），又在细网格下实现了朝向无关。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/9azMKawwL0dyCfF2A6BehXFRcV0c4m3troDd5UE4ZlKI1cBmWw30K5bqVMKz0jPDiblw7yYpItgB8YvDk7sCL0B9AqicfLiaP7otjkq95iaRSJo/640.png)

**图7\. 不同网格间距下磷原子的电荷变化**  
_绿色（ESP）和棕色（rwRESP）随网格加密趋于稳定，蓝色（传统RESP）则明显漂移。灰色阴影是GAMESS Connolly网格的结果。_

这套方案已经无缝集成到AmberTools中，用户跑一遍QUICK单点计算，就能拿到高质量的rwRESP电荷，直接用于GAFF力场参数化。未来，这项GPU加速技术还有望用于极化率QM/MM模拟中的电场计算。

**意义**：给分子电荷“称重”这件事，过去是“转一次一个样”，现在终于可以做到“不管怎么转，称出来都一样”。对于高通量力场参数化、药物分子虚拟筛选这些需要可靠静电描述的领域，这无疑是地基级别的加固。

[告别“垃圾进垃圾出”：CO₂吸附材料发现，先给AI喂口“好饭”](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzE5MTE0Njg3NQ==&mid=2247485448&idx=1&sn=aaf28c36c244043e92455b96f1b89095&scene=21#wechat%5Fredirect)

[【npj cm】给离子固体“装上长程雷达”：巧妙分离电荷构建高精度机器学习势函数](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzE5MTE0Njg3NQ==&mid=2247485205&idx=1&sn=8096c4c1d0e4e42c7d44a535c7f7b2a6&scene=21#wechat%5Fredirect)

  
预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajicM8NiadIPfeSzL1nFugbgrN0GO1hvZKLJOaBZvsoj55yGAmCZVw4Iiag/0.png) 

 计算材料视界 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/zt6icQPibHZgpZtwC0iaMVXASUkQ7ibzJ2iajicM8NiadIPfeSzL1nFugbgrN0GO1hvZKLJOaBZvsoj55yGAmCZVw4Iiag/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
