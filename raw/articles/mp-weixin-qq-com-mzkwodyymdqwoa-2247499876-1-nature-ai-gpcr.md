---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkwODYyMDQwOA%3D%3D&mid=2247499876&idx=1&sn=7a6a4041c1a8d9064e64a23920df9ce0
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkwODYyMDQwOA%3D%3D&mid=2247499876&idx=1&sn=7a6a4041c1a8d9064e64a23920df9ce0
source_domain: mp.weixin.qq.com
title: 新春首篇Nature！良渚实验室实现AI设计GPCR跨膜调控模块
author: 
published_at: 
fetched_at: 2026-04-25T02:03:39Z
extractor: wechat_worker
content_hash: 625bfb4811e361e7a7a855116a086f7749981f5f3dcc64e91899b750ae206297
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/SJOHZ9YuUNznQxIYmxcpcMyBFzfW9lPUPXMUI8KeDWTwIibWIGBKia4qrZXKQuvGXKpic4CzLa4VO7ndUNVUCVKibQxkpcibicYAwW8WG2z2mRUTM/0.jpg) 

# 新春首篇Nature！良渚实验室实现AI设计GPCR跨膜调控模块

原创 max max [ BioTender 观测日志 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNz5GxDclV3gic7nzurrNJ6tLNtUHEKhcNz5SOkEIhZ2Pbyp8myaic7yuIt7NPMN8MKx5mordW76qaibOEzlypx9CQmV0ga5oZzPEo/640.png)

  
---

  
新春首篇Nature
  
  
AI设计GPCR跨膜调控模块
  
  
**BioTender | AI4P**
  
  
GPCR，是现代药物研发的“头号靶点”。全球约三分之一上市药物作用于GPCR。但几十年来，我们的策略几乎都围绕一个地方打转——正构口袋。往里塞小分子。提高亲和力。优化选择性。直到今天，这个逻辑依然成立。但这篇发表在 _Nature_ 的工作，提出了一个完全不同的方向——不再改口袋，而是设计一个跨膜蛋白，从受体“外框”重写它的构象命运。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNw5NZ7WYHwjibGaed5XaeUBojltmWciaQzdSjTRUHabqerLQOVzo7dmAyO5iauowhA3kE5mELFCUAHENIXO0pP2fTofHliaxeOAZOM/640.png)

  
这项工作来自良渚实验室。他们用 AI，从零设计出一类调控 GPCR 的跨膜小蛋白模块。这不是优化。是创造。
  
  
不是设计GPCR，

而是设计“调控GPCR的蛋白”

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4PRWJO8VX6DwfPPwDiaeabofdCK3hQZpW6zibmkuGtDibd6vQPyibyF2Zsrgk3WXJTLIcu41QottLiaYQw3f9UlVlkw/640.png?&amp;wx_fmt=png#imgIndex=1)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BMNr1wLwd8P7M8FJdyJGvbFRfCGbmzxHAA1c7GpHO0wkChOdlJqs6KprjZzZlebcSIzYGQva46DSYQlP7kT0ZQ/640.png?&amp;wx_fmt=png#imgIndex=2)

首先必须讲清楚——这篇工作并不是从零设计一个GPCR本体。他们做的是保持GPCR序列完全不变、用AI设计一个双跨膜α螺旋小蛋白、让它贴附在GPCR跨膜区外侧、改变TM6外摆状态、从而改变信号输出。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/SJOHZ9YuUNzJjV5AFicJGIsMUrl0ibRJZZchSkLsFs336ibHDSpxj7MopV4gQ6gyAibiatg8qVJVWlgVPuSjqGlibqOoaPs7yRvL6PvrCO7vlKzE4/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/SJOHZ9YuUNw8pvwvK89Sga24NkLMAvsgtjTVYeAvvM9sP9w5x8mQVY2bXACSBdy7CicsKRuyibjhx4G7AxFFQ2Meyp3IZO4o9OHBMySibN0Aoc/640.png)

De novo Design of GEM

  
作者将其命名为GEM（GPCR Exoframe Modulators），可以理解为一个跨膜“外挂模块”。不是钥匙。而是支架。
  
  
为什么

要从“外框”入手？

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4PRWJO8VX6DwfPPwDiaeabofdCK3hQZpW6zibmkuGtDibd6vQPyibyF2Zsrgk3WXJTLIcu41QottLiaYQw3f9UlVlkw/640.png?&amp;wx_fmt=png#imgIndex=14)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BMNr1wLwd8P7M8FJdyJGvbFRfCGbmzxHAA1c7GpHO0wkChOdlJqs6KprjZzZlebcSIzYGQva46DSYQlP7kT0ZQ/640.png?&amp;wx_fmt=png#imgIndex=15)

传统GPCR药物有三个核心问题——正构位点高度保守，选择性差、小分子变构位点空间有限、功能缺失突变（LOF）几乎无法救治。而GPCR激活的核心物理机制，是TM6向外摆动。如果我们能稳定外摆 → 激活、锁死内摆 → 抑制，那就相当于直接控制信号开关。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/SJOHZ9YuUNytGRPZHXQ2Aiav46ib8KUKXKwa4qRwEaaHibibiayBeONs4vSicACw2YmFyDvNWAxlydKmIIMFM4zibksR9W1qNWXXGBqgFxwaGs1MzQ/640.png)

传统GPCR药物的三个核心问题

  
问题是跨膜区外侧的调控位点几乎从未被系统开发。良渚实验室做的第一步，是用AF2-multimer + 跨膜探针扫描整个TMD表面，寻找“可设计结合凹槽”。他们找到了三个潜在位点TM1/2/4、TM3/4/5、TM5/6/7，然后，AI正式登场。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNzicW5KE8V3ib2HEHian17keG2Gwz1b3ysrv1QGqFhLvC0Z9DavDiabstQaZbHPXghFo8yHD1hUUoey9le7UQKmDnCvzPYAcYNiaTmU/640.png)

AF2-multimer + 跨膜探针扫描

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/SJOHZ9YuUNwrk0V2ScCa5TJ7AoRSoiasdPRtmbcJjpYmYV2rWibVNZIAnVic1UzspOq24WxPDxVxZX64LXzgAe3Oy0UyCBqMxTZx97O3r0xj0A/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNx9putkLKnjpPwiaWZia3rcOjJ0s5ocOGIqk6iaBlQpU8FmOYBem6T7Iamubepw74icAqiaGnniaagaZUJVatlzjcHcAv5t6ZeyffCsI/640.png)

针对不同靶位点，对单个跨膜螺旋的结合姿势和探针结合姿势分布进行俯视图分析

  
AI设计流水线：

RFDiffusion × 

ProteinMPNN × AF2

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4PRWJO8VX6DwfPPwDiaeabofdCK3hQZpW6zibmkuGtDibd6vQPyibyF2Zsrgk3WXJTLIcu41QottLiaYQw3f9UlVlkw/640.png?&amp;wx_fmt=png#imgIndex=52)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BMNr1wLwd8P7M8FJdyJGvbFRfCGbmzxHAA1c7GpHO0wkChOdlJqs6KprjZzZlebcSIzYGQva46DSYQlP7kT0ZQ/640.png?&amp;wx_fmt=png#imgIndex=53)

整个设计过程可以概括为——RFDiffusion 生成跨膜骨架、ProteinMPNN 设计序列、AF2预测复合物结构、用自洽性和pLDDT过滤。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNxJIiafIicIC5Vta5Qeu0oHD3jfonU1c4lhjMpf5E1J8AxN2r2AfruffBjM3sxknLK5ANviaib2MEWRrNfT09xrBqlvhmsC9LPYcA0/640.png)

设计流程四步：RFDiffusion → ProteinMPNN → AF2 → 置信度过滤

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/SJOHZ9YuUNyCWqXc3S8rUeFia6iafvoHfgmrs9TYSq8raGpSY6UU1vfKGCj3sTIMQdE5eJZ4CHMyGIFoUSxuTZLTWKsFCSQk8bUicibWzC3KWsQ/640.png)

  
值得注意的是他们并未依赖传统能量函数，而是用global scRMSD、结构自洽性、预测置信度、来判断“是否可设计”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/SJOHZ9YuUNwdhFnapeDWh5QzyT7OXIIDTjUnxL7Reia5raZWmZTQ0MkpxiaURmKlGWaxLh6XO7XCIGeHnqI71a8upPsRzo25KEhiaOG0FPEsyk/640.png)

global scRMSD：判断“是否可设计”的关键指标

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/SJOHZ9YuUNwg3F0zvUOG7nZN5v7z9w4V4LoHvOa2k4ibB0wibvTcRtibQAkAqCj3MvdqEVOmP76dzUOans58LHBBJRHmu9oVict0R0CboGVQfAc/640.png)

pLDDT 作为预测置信度指标

  
这是一种典型的现代AI蛋白设计范式。更关键的是，他们加入了“结构提示”（structural prompting）：插入策略限制结合面、占位策略避免错位结合、引入G蛋白诱导active构象、这相当于给生，模型加入“构象约束”。设计，不再盲目。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNzamsawKPHWWC9JQ3S2DBF9r0LMdcLM5X5AtN4zVmTheibMNb8ZoUvibe9elQs04ZibNlaBDibFYWumBOGZwc9uSEF76Hice7IHA8Zo/640.png)

不是盲目搜索，而是受约束的构象优化

  
四种不同功能

的跨膜调控模块

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4PRWJO8VX6DwfPPwDiaeabofdCK3hQZpW6zibmkuGtDibd6vQPyibyF2Zsrgk3WXJTLIcu41QottLiaYQw3f9UlVlkw/640.png?&amp;wx_fmt=png#imgIndex=52)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BMNr1wLwd8P7M8FJdyJGvbFRfCGbmzxHAA1c7GpHO0wkChOdlJqs6KprjZzZlebcSIzYGQva46DSYQlP7kT0ZQ/640.png?&amp;wx_fmt=png#imgIndex=53)

他们最终成功设计出四种代表性GEM——无显著调控型、β-arrestin偏向型、负变构调控型（NAM）、激动型PAM（ago-PAM）。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/SJOHZ9YuUNz8yInqm1ux0EFxOM0iav5v495hUlRl8HLUa0bpE2sKqSdLRKZaN15ibpkeZ6ibpHhZyU3lDeAoCQicpeiaOicmWGKhjFLKxiaRPic9bRs/640.png)

  
结构解析（cryo-EM）显示——设计模型与实验结构高度一致。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNxQ4MLvQPqB1ic9x7zdriaibSAKUUZ97dq1R4t6GxnWO9V5PqI7xJ1Avapzia3XyxAQGzQ6oHdxXTj11EtSg9YLsUicesPc2dTX8LNk/640.png)

cryo-EM 结构显示：设计与实验高度一致

  
尤其关键的是：NAM模块像“夹子”锁死TM6、ago-PAM模块稳定TM6外摆，这是对GPCR激活物理机制的直接操控。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNwh3LZeJhZx4eMkGRUnabBicrMQ6ZOKqfegnV6bXDjTRp2BHdEicxh7hemPnjibdf5JmhWibKZjXSy7R7byGRicC0Z4iarfRLxiaLUrOI/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNzypaQxmKFGdTwO0ThBgZ7pNiaebeTBRMUYD4ib2iaGiatSiblw9FYicrzWKkVN5NzNt05znLuzRbuFoYteBYiaSykB5Jv92hhLgXngXo/640.png)

NAM 模块“锁死”TM6
  
  
最震撼的部分

功能缺失突变被救活

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4PRWJO8VX6DwfPPwDiaeabofdCK3hQZpW6zibmkuGtDibd6vQPyibyF2Zsrgk3WXJTLIcu41QottLiaYQw3f9UlVlkw/640.png?&amp;wx_fmt=png#imgIndex=52)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BMNr1wLwd8P7M8FJdyJGvbFRfCGbmzxHAA1c7GpHO0wkChOdlJqs6KprjZzZlebcSIzYGQva46DSYQlP7kT0ZQ/640.png?&amp;wx_fmt=png#imgIndex=53)

更重要的是——ago-PAM型模块能够恢复多种D1R功能缺失突变的信号输出。包括正构口袋关键残基突变、激活微开关突变、临床相关突变。恢复幅度可达接近WT水平。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNyfvHJYFKvcOplIryD9WPPWzNxiau9fUb957knW5lLSePAjyUXgYWQlcAbiatTGPEeVbDOWOlqfeia0RgEt8ibK4X7GGPH8xJuGicGw/640.png)

ago-PAM 可以恢复多种 D1R 功能缺失突变

  
这意味不是修口袋，而是修“构象平衡”。这是一种完全不同的治疗思路。

  
这件事的真正意义

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4PRWJO8VX6DwfPPwDiaeabofdCK3hQZpW6zibmkuGtDibd6vQPyibyF2Zsrgk3WXJTLIcu41QottLiaYQw3f9UlVlkw/640.png?&amp;wx_fmt=png#imgIndex=52)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/BMNr1wLwd8P7M8FJdyJGvbFRfCGbmzxHAA1c7GpHO0wkChOdlJqs6KprjZzZlebcSIzYGQva46DSYQlP7kT0ZQ/640.png?&amp;wx_fmt=png#imgIndex=53)

这篇Nature的价值，并不仅仅在于做出几个新分子。它意味着跨膜蛋白可以被AI从零设计、膜蛋白复合体设计进入可控时代、GPCR变构空间远未被开发完、构象工程成为新范式。更深一层的意义在于——药物设计，正在从“分子识别”走向“构象工程”。GPCR，不再只是一个被动的受体。它开始成为一个可以被外挂模块编程的构象机器。当然，这仍然只是第一步，体内递送方式如何实现？免疫原性如何评估？是否可扩展到更多GPCR亚型？能否形成药物级产品？但有一点已经非常明确——AI设计已经走进了膜蛋白领域。

如果你想跟进这类“AI × 生物资讯”的最新进展，欢迎关注

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNxmyg43mTjllEicP2Y0ncJk4TrwOlNUUahhRiafk0JHurCeDEUBicnaxRx8DzoyTxsmhq9PXg9dzwKTPcC35kItBLuJAa5hn8ZjWE/640.png)

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNxJsxIkKLzrrWgURSJnE8X4htYbNZibmKFX0MRTdR803olwLgSFzD9PB6tWDMEPJp9VicRpPFonscB4eibQh4CHwMELRUkcO6NhU8/0.png) 

 BioTender 观测日志 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/SJOHZ9YuUNxJsxIkKLzrrWgURSJnE8X4htYbNZibmKFX0MRTdR803olwLgSFzD9PB6tWDMEPJp9VicRpPFonscB4eibQh4CHwMELRUkcO6NhU8/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
