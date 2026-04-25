---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA%3D%3D&mid=2651286930&idx=1&sn=f7bf1e3af475e13f3837a325cf154e88
canonical_url: https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA%3D%3D&mid=2651286930&idx=1&sn=f7bf1e3af475e13f3837a325cf154e88
source_domain: mp.weixin.qq.com
title: DUET + SAAFEC：预测点突变引起的蛋白稳定性改变（计算ΔΔG）
author: 
published_at: 
fetched_at: 2026-04-25T02:04:18Z
extractor: wechat_worker
content_hash: d302e196128a5a30f571345d34c5f569afdbbf777f7face1f0bc6ccd5ab286c4
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/dREape4YBzzusia6MiaP0IPeKQZhib92PmuoeQFv4YxsN0D6OIEv8TJ3bnYjeo1z2tQBaUKryyXuYD0epj9vAHr1A/0.jpg) 

# DUET + SAAFEC：预测点突变引起的蛋白稳定性改变（计算ΔΔG）

原创 晏宝 晏宝 [ 生物信息云 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

  
---

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/dREape4YBzyF5jVxNCORGgSJRgWqy8hD1vw3aTCTiauBVLErhPNxeAq1Z3p1iaawPViah3KsJ6q4ibys098ibmnjzcQ/640.jpg)  

---

DUET 是一款专门用于预测点突变对蛋白质稳定性影响的生物信息学工具，通过计算突变前后的折叠自由能变化（ΔΔG）来量化稳定性差异。其核心优势在于整合了 mCSM 和 SDM 两种算法，显著提升预测准确性，尤其适用于解析突变对蛋白结构的动态影响。以下是具体应用方法与操作要点：

1\. 核心功能与原理

ΔΔG 计算：ΔΔG = ΔG（突变型）− ΔG（野生型），负值表示稳定性下降（如 ΔΔG = -2.063 Kcal/mol 表示突变后蛋白更易变性）。

算法整合：

mCSM：基于分子图论预测突变对蛋白 - 配体相互作用的影响。

SDM：结合序列保守性与结构特征评估突变效应。

输入要求：需提供蛋白的三维结构文件（如 PDB 格式）及突变信息（位置、残基变化）。

2.分析演示  

继续以前面介绍的PTEN基因为例：

在Uniport数据库中找到该蛋白在PDB数据库中的3级结构ID。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzzusia6MiaP0IPeKQZhib92PmueXtwJwBhVMAqLMAMIkLILKOF4ZZibpdWCnq2MzoPVFeGKV40zW2Adow/640.png)

网站：https://biosig.lab.uq.edu.au/duet/stability

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzzusia6MiaP0IPeKQZhib92PmuttVxlWgEQITOz6cl8I4ngfgIz19KJ17qJzEgsgnmlVRU0rN0ULxlTQ/640.png)

分析的结果如下：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzzusia6MiaP0IPeKQZhib92Pmu9QRUcAyz9y4ya4ia7hVpeIVaLXibUcHxmicEJDiaGjbuhM07VtI3rBTTwg/640.png)

可以看到：该突变会导致蛋白稳定性下降。

可以下载突变后的3级结构文件，进一步的和野生型的结构，美化突变位点的部分。[分子对接教程 | (8) PyMOL可视化对接结果](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzA4NDAzODkzMA==&mid=2651274201&idx=1&sn=96d1aeada24d8d4a5ddb1b68ab858227&scene=21#wechat%5Fredirect)。

2\. SAAFEC-SEQ

http://compbio.clemson.edu/SAAFEC-SEQ/

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzzusia6MiaP0IPeKQZhib92Pmuib0DfqgybsNQMchyowO1gozibFgMCBLr1yOXjjdTIrT2T9wEu51n1icng/640.png)

分析结果如下：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzzusia6MiaP0IPeKQZhib92PmuKjicy5aUjN2Avianj76I8CthQzaHkbia9GF27LXcI8cUQlXk3icOibFaic6w/640.png)

结论也是和前面一致。

类似的工具还有：MaestroWeb

相关文章：

[PolyPhen-2：预测氨基酸点突变对蛋白功能影响的分析工具](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzA4NDAzODkzMA==&mid=2651286901&idx=1&sn=05cf57bdac9068b09d1aa79731e9b8c6&scene=21#wechat%5Fredirect)

---

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzwlcDib0ZJoicuLyG92DicwGVnDorFCjt6v1RVJKusT6ib2vicAibS7CvADLziaUWZHqictxy4YkgyhsggMbg/640.png)

B站视频合集

---

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzw321c7L6nrpqs6Sa0FGFzaFwzp7pdXrJZ5QRhib950DOAUMrj2NDyfuonw7jbnBljp2rxeQJlAyng/640.png)

**[加入生信学习交流群](http://mp.weixin.qq.com/s?%5F%5Fbiz=MzA4NDAzODkzMA==&mid=2651278937&idx=1&sn=70b476a444883a9282efc13ee9c19a72&chksm=841eaa24b3692332de6263a5ed15e2b3da3017845d6e533a0b7944624afd2fc3275710f61439&scene=21#wechat%5Fredirect)**

---

  
经 典 栏 目
  
  
| [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RNDhkvd0VYruWibnf6I99uicOsqFSIPicvmUP7w8m3ictoTgeAmsmF6v40nqw/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1338047035672526848#wechat%5Fredirect) | [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RND8LOmqZpGNerHE2ib3hrYBm7czV8ibjkg6bgUynABicHtDblDwibcK0iafdg/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1385753371944239106#wechat%5Fredirect) |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RNDnwmiaAUS36yqYw6aeJ9iaNkNUGmcU7ux65wvficPlQXDHQibW3JYrFJFvQ/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1410264757734817793#wechat%5Fredirect) | [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RNDANc1t4lIm5wTqesgaITcicUlfiaXHrSxrKVeWZYCzlH9MSy7IibTYQLNg/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1369789283514761218#wechat%5Fredirect)   |
| [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RNDQmkz6ffBVfRj1Ab8ibMyygNmmvL7yia3eoZzJNoWjNW6vwjG4y3PWsNg/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1519504738202025984#wechat%5Fredirect)   | [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RNDCpphsguALa0tR6pfEy8yLBahRX9iaeYdKCwicKFbBd2X1yTSiaZyZwFqA/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1519504738034253825#wechat%5Fredirect)   |
| [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RND73kOWY2pcLs5dmFMQWCG1Noz1oRR2oBCDHgNjiaAXqEZkLllKtoeO0g/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1687484069455986690#wechat%5Fredirect)    | [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RND6nm4ADziajqL0hpSudJTiacRyqVOg9NpnKoyfmVOgzwp97HicIFjb0gDw/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1521974159344533507#wechat%5Fredirect)   |
| [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RNDRBOVZUPB816xXqA1SlbNzDRkmNRSjtCa3pqjuyAoQJxa1drcW0yeZQ/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1715194110111776770#wechat%5Fredirect)     | [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RNDxgtG3pdSyaKcfgvqjDrC2mpKa0MCu1rsbGkQLcOys8c9BVLs2VnjEg/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1715194110212440067#wechat%5Fredirect)      |
| [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RNDXqLDtKHqQMBReWKnTibVusnVlY43shlib0iaoluz4tmJPej8ej4vWiaehA/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1712569781846933508#wechat%5Fredirect) | [![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxVERm1kp30MnGymicMs1RND3CbMQTDNRO3A5SELiaQ3DDeqQkt5rfZqpwQRsQYyTicQUD9zQlfolIvQ/640.png)](https://mp.weixin.qq.com/mp/appmsgalbum?%5F%5Fbiz=MzA4NDAzODkzMA==&action=getalbum&album%5Fid=1338481272770953216#wechat%5Fredirect)    |
  
  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxWN6ialKv18AuE9NAspKUjBTu1vDKIiaVNfPJmP2iaZGCB4RuvytSBVEqoqMI9mIa91jfCmp1jWwA8g/0.png) 

 生物信息云 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/dREape4YBzxWN6ialKv18AuE9NAspKUjBTu1vDKIiaVNfPJmP2iaZGCB4RuvytSBVEqoqMI9mIa91jfCmp1jWwA8g/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
