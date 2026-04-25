---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUxOTY3OTk2MA%3D%3D&mid=2247487749&idx=1&sn=b714307570b5477e5eccbdb9bd559f25
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUxOTY3OTk2MA%3D%3D&mid=2247487749&idx=1&sn=b714307570b5477e5eccbdb9bd559f25
source_domain: mp.weixin.qq.com
title: 为什么有时酶与底物的亲和力高（低 Km），但催化速率（kcat）却很低？
author: 
published_at: 
fetched_at: 2026-04-25T02:03:59Z
extractor: wechat_worker
content_hash: 9c3854ca3c51c42453879a00204292d6e588b9007db8d0eaeda26ef12d725e66
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/I8vp5I6cicR9mc5oEaJaib5yaJ2H9XEfM8xG7cXiaktNBC6uvbibmicjzyCukajARUEfJjpcmoWpAOVuwic1Fv0I3HeA/0.jpg) 

# 为什么有时酶与底物的亲和力高（低 Km），但催化速率（kcat）却很低？

原创 duizhang duizhang [ 队长的生物实验室 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/I8vp5I6cicRibAzcubHqpW2wnZyN4m0fqFXtUcEicqYoFuLpzt2hq006tIonJbkZN0OtxBeMCQuYOhxM1RDj4Oy8A/640.jpg)

在酶催化底物过程中，我们经常追求高亲和力（低 Km ），但实验结果有时会表现为酶把底物结合得太紧，反而转化效率（kcat）极低。这种现象通常被称为“结合能的误用”**。理想的酶不应该仅仅完美互补底物，而应该完美互补**过渡态。

  
今天就从“基态过度稳定”、“产物抑制”以及“非生产性结合”三个主要方面来分析这个问题。

  
### 01\. 基态过度稳定

酶催化的核心在于降低反应的活化能。活化能是指酶-底物复合物（ES）转化为过渡态所需的能量差。如果酶与底物在**基态**（即尚未发生化学反应的状态）结合得过于紧密，ES 复合物的能量就会大幅降低，形成一个很深的“能量陷阱”。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/I8vp5I6cicR9mc5oEaJaib5yaJ2H9XEfM8XBd37mobLFvoQ7z4dFWYq1GwU8mXciagUTLd5p2srWaRCrIPbMdic8YA/640.png)

图. 酶催化反应（蓝色）和非催化反应（黑色）的反应

S，游离底物；ES，底物结合酶；TS‡，未结合的过渡态；ETS‡，酶结合的过渡态；EP，产物结合酶；P，游离产物；Δg‡uncat，非催化反应的活化能；Δg‡cat，催化反应的活化能。

（Reference：Engineering Enzyme Stability and Catalysis: A Case Study of Hen Egg White Lysozyme）

  
当 ES 复合物的能量处于极低的深谷时，虽然反应的过渡态能量可能没有变化，但从这个深谷到过渡态山顶所需的相对能量差反而变大了。因此，在这种情况下底物被“锁死”在活性中心里，导致化学键断裂或形成的难度增加，从而kcat显著下降。

  
这种现象违背了酶催化的“保罗原理”**。该原理指出，最高效的酶并不是与底物结构最匹配的，而是与反应的**过渡态结构最匹配的。如果酶的设计过于偏向于识别底物的初始结构，大部分的结合能都被用来稳定基态，而不是用来扭曲底物使其进入不稳定的过渡态，结果就是酶变成了单纯的“结合蛋白”，失去了催化活力。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/I8vp5I6cicR9mc5oEaJaib5yaJ2H9XEfM8iamTeeo2wQJITC1yQZh79wswmGRyJiaTIuAkCxPh1Cyk2ef9Dr01dibhA/640.png)

图. “铁丝酶”催化反应的过渡态稳定机制

（源于知乎id“生物汪汪”）

### 02\. 产物抑制与释放受阻

高亲和力往往意味着酶的活性中心与底物分子之间存在大量的弱相互作用（如氢键、疏水作用、范德华力等）。由于产物在结构上通常与底物高度相似，如果酶对底物结合极紧，它极有可能对产物也保持着极高的亲和力。

  
在这种情况下，催化反应的限速步骤可能不再是化学键的断裂，而是**产物的释放**。即便酶迅速地将底物转化为了产物，但由于结合得太紧，产物无法及时从活性中心扩散出去。此时，酶的活性中心被产物占据，无法结合新的底物分子，导致宏观上测得的kcat极低。

  
此外，这还会导致严重的**产物竞争性抑制**。随着反应进行，微量的产物积累就会迅速通过高亲和力抢占酶的活性位点。在动力学曲线上，会看到反应初速度可能尚可，但进程曲线迅速变平，表现为vmax很低。这种因结合太好导致的产物滞留，是许多高亲和力突变体酶活下降的主要原因。

###   

### 03\. 非生产性结合

高亲和力并不总是意味着酶与底物以正确姿态结合。有时，底物与酶结合得非常紧密，是因为底物被卡在一个能量极低的陷阱里，这种结合模式在空间构象上并不利于催化基团对底物的进攻。这就是所谓的**非生产性结合模式**。

  
例如，底物可能以一种错误的取向进入活性口袋，虽然与周边的氨基酸形成了很强的疏水作用或氢键网络（表现为高亲和力），但其反应基团距离酶的催化残基太远，或者角度不对，导致了最终催化效率极低。在这种情况下，大部分酶分子被底物以错误的姿态结合，只有极少部分以正确构象结合的底物能发生反应。这种无效的强结合会大量消耗游离酶，导致表观 kcat 极低。

  
\*本文涉及内容/图片如有版权问题请联系小编处理。

\*欢迎转发，转载请联系队长小助手(XBBen01)。

---

  
队长自建科研交流群，群内会互相答疑、文献互助、教程分享、软件分享，欢迎你的加入!  

群内氛围：

| ![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/I8vp5I6cicRicQ3NZ6HCXyacNkUibpqiaMrFRnzUgiaIOxMbhjWSlGNDJicr1npiahb4L7PCCeibDL310lPxV1iaeGgCGkw/640.jpg) | ![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/I8vp5I6cicRicQ3NZ6HCXyacNkUibpqiaMrFia2x89Weu1oricZIskM6TT834XwbbTlO4quLsqicGCL8AiaMZQuLyAicjZg/640.jpg) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/I8vp5I6cicRicQ3NZ6HCXyacNkUibpqiaMrFWicFvebcEvxiasP4lm6Rgov8cfNKmwibr0aKJJPqrZBjMIBS8f8aTSRtA/640.jpg)   | ![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/I8vp5I6cicRicQ3NZ6HCXyacNkUibpqiaMrFwsGA2ic3zviaPEMMGJojo7JXKZm5HKcbZBjsZGf2v5uicnsR0bhfLqpEg/640.jpg)   |

扫描下方二维码，添加队长的笔记本，

备注「科研交流」，即可加入群聊！ 

期待你的加入，让我们一起在科研的道路上携手同行，共创辉煌！ 

****![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/I8vp5I6cicRicyOBgd1ufTyZg5hKp8KtdpZTkPfag4mI9GYSN5lZ3gORy92iaiclvWnpvNOUkCnEqtJ1JUUhrLaIicw/640.jpg)**

****「碎片时间get 」专栏**

**[刚性、柔性和半柔性对接方式中哪种更符合真实情况？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487575&idx=1&sn=630b44b1cda62e5808f5e9693e73ee4f&scene=21#wechat%5Fredirect)**

**[MD中哪些分析能作为催化活性、稳定性等方面的理论支撑？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487484&idx=1&sn=bc56465b036a2e77274cd543d75f71e4&scene=21#wechat%5Fredirect)**

**[酶热稳定性的提升为何会以活性为代价？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487479&idx=1&sn=cf9b10e566327c7e48fea28c77dc7bac&scene=21#wechat%5Fredirect)**

**[为什么突变位点距离活性中心很远，却能显著改善酶活？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487461&idx=1&sn=350292be8b9194a2d3ff899efa260726&scene=21#wechat%5Fredirect)**

**[酶与底物结合涉及的非共价作用力有什么？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487431&idx=1&sn=802ca36c3483ee5ef48b148b2b20340f&scene=21#wechat%5Fredirect)**

**[在分子对接结果中，打分和催化距离哪个更重要？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487407&idx=1&sn=ccf0d14a77a210218a84058befee0549&scene=21#wechat%5Fredirect)**

**[为什么蛋白在储存过程中（即使在4°C或-80°C）活性也会逐渐丧失？应如何解决？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487395&idx=1&sn=38e00d3adf67f8c1e7717533adf95565&scene=21#wechat%5Fredirect)**

**[高压匀浆、超声破碎和酶法裂解对目标蛋白有何不同影响？如何针对蛋白特性选择最佳的裂解方案？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487377&idx=1&sn=e85e5fcbdad7d09826c6357395a58147&scene=21#wechat%5Fredirect)**

**[如何选择蛋白标签？选择不同标签对蛋白的性质有何影响？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487332&idx=1&sn=2173b58b1b6609c78d7e84c5f5c93c3a&scene=21#wechat%5Fredirect)**

**[在大肠杆菌中表达异源蛋白时，为何表达量极低或出现翻译提前终止？如何解决？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487292&idx=1&sn=046f6395a4883d2f742bcba53dbcf0a6&scene=21#wechat%5Fredirect)**

**[如何精确测定反应速度极快或极慢的酶的动力学参数？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487249&idx=1&sn=583386d9bf13ad1a20d05e0f14f8acdd&scene=21#wechat%5Fredirect)**

**[在原核系统中表达含有二硫键的真核蛋白，为何容易形成错配的二硫键或聚集？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487244&idx=1&sn=643d0b107ba64345abab09c368d88f41&scene=21#wechat%5Fredirect)**

**[在细胞裂解或纯化过程中，目标蛋白为何总是容易被降解？如何最大限度地减少降解？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487232&idx=1&sn=1abfc3b0728a6cb9a4fba35bf10e82f3&scene=21#wechat%5Fredirect)**

**[离子交换或分子筛层析效果不佳：如何解决峰形差、分离度低的问题？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487227&idx=1&sn=4a3b434379c5781aacca03b1626d0054&scene=21#wechat%5Fredirect)**

**[Bradford法和BCA法测定蛋白浓度为何会产生巨大差异？应如何选择合适的定量方法？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487211&idx=1&sn=4a0430269f44d46b7b52a47d398e1a05&scene=21#wechat%5Fredirect)**

**[纯化后的蛋白为何会发生沉淀或聚集？如何提高其长期稳定性？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487204&idx=1&sn=ea21f9130051710c011cf58a7d8b8ec9&scene=21#wechat%5Fredirect)**

**[从包涵体中复性蛋白时，如何筛选最佳复性条件以恢复其生物学活性？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487169&idx=1&sn=86c27c03ce69d331c158351bbdf89fc0&scene=21#wechat%5Fredirect)**

**[信号肽在蛋白表达中是天然引导还是障碍？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247487091&idx=1&sn=6feec1202d525d650d514754dcc249e9&scene=21#wechat%5Fredirect)**

**[酶抑制剂如何“刹住”酶的反应？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247486698&idx=1&sn=47b8de89969b00f4b83eec0f73c39ce7&scene=21#wechat%5Fredirect)**

**[酶固定化：工业生物催化的效率革命](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247486678&idx=1&sn=826362a00b164dafb7d9c50841b4df69&scene=21#wechat%5Fredirect)**

****[Western Blot为何能特异性检测目标蛋白？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247486507&idx=1&sn=58cd32892e499603c20dd36a58526cd2&scene=21#wechat%5Fredirect)**

****[异源表达中，蛋白质折叠错误的后果是什么？如何改善错误折叠？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247486469&idx=1&sn=9658899c621fc4695abcf14d46c73bd4&scene=21#wechat%5Fredirect)**

****[一个细菌只能容纳一个质粒吗？深度剖析质粒不相容性](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247486395&idx=1&sn=9a5b9a91b355b16069b330041d3690c5&scene=21#wechat%5Fredirect)**

****[考马斯亮蓝是如何给蛋白质染色的？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247486227&idx=1&sn=68048e6f57474cf6c75516bb3cf3aca9&scene=21#wechat%5Fredirect)**

****[细菌培养中为什么通常选择测量OD600？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247485958&idx=2&sn=bc5d85a3d9795d6840c043f6cdef5515&scene=21#wechat%5Fredirect)**

****[蛋白质与小分子的相互作用力有哪些？](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247485945&idx=2&sn=7115d8ed3f7e34b40caa7e758bc8d8f3&scene=21#wechat%5Fredirect)**

****[甘油保菌那些事](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247485922&idx=2&sn=d14456f2e98c288bc8b2e8fb2c997041&scene=21#wechat%5Fredirect)**

****[DNA甲基化](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzUxOTY3OTk2MA==&mid=2247485896&idx=2&sn=63efea5cc8e2f82e8e30049e00b04350&scene=21#wechat%5Fredirect)**

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/I8vp5I6cicRibmbMNFZhKmSPfdrmyHF6xicKvdSWm9HfnChsRuhg52NEbbmhVRYkWvNicTQ4yETjcAiaibE6zcZ71puA/0.png) 

 队长的生物实验室 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/I8vp5I6cicRibmbMNFZhKmSPfdrmyHF6xicKvdSWm9HfnChsRuhg52NEbbmhVRYkWvNicTQ4yETjcAiaibE6zcZ71puA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
