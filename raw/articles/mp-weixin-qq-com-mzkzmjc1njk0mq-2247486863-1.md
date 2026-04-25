---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247486863&idx=1&sn=878e6439b417c8069a53bb886c802c2a
canonical_url: https://mp.weixin.qq.com/s?__biz=MzkzMjc1Njk0MQ%3D%3D&mid=2247486863&idx=1&sn=878e6439b417c8069a53bb886c802c2a
source_domain: mp.weixin.qq.com
title: 不用“炼金术”也能算结合自由能？一种更高效的结合亲和力预测新方法来了
author: 
published_at: 
fetched_at: 2026-04-25T02:03:23Z
extractor: wechat_worker
content_hash: 1935c7b85561b3afdb840e0f0e4b81b9b98ad5ab183929558abb5218145d59da
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/d1ibKq69vtySUNmYicibic3JpwzqibDf73Lulh3wwbyzoia9G8dGL67oxiah29orvVDicphx2WGAzXFhjVFqjicCZ1iaD3LPqO0mHDDPHeicZpsC50QpVA/0.jpg) 

# 不用“炼金术”也能算结合自由能？一种更高效的结合亲和力预测新方法来了

原创 drugdesign drugdesign [ 药研魔镜 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/d1ibKq69vtyS4xKWVKbGRCUAfDazOpXybRQgAl2145dYEvic1jXLMTwmOTmNd2Hzk5xwcC32KJZsp3J1ElSAib3WbaYnMjShuGL37RP88baYIA/640.gif)

  
---

> **传统 ABFE 很准，但太贵；这篇新工作提出 DBFE，不再依赖繁琐的“炼金中间态”，试图用更低成本把结合自由能计算真正推向虚拟筛选场景。**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/d1ibKq69vtySGz2c6RicfqcwyJCDn2m4LnPadSGb73eIaah68gNibepcicFcXA2eZqkIqcs9HEatLIiaIseNATHiagLVolEYeMZ5ODE5mb9fKo7k0/640.jpg)

## 不用“炼金术”也能算结合自由能？一种更高效的结合亲和力预测新方法

> 做过自由能计算的人都知道：**ABFE 很强，但也很“烧”资源。**

它准，是因为它足够“物理”； 它难用，也是因为它太“物理”了。

传统绝对结合自由能方法，往往需要在“结合态”和“解耦态”之间构建大量 **alchemical intermediates（炼金中间态）**，一步一步完成自由能变换。这样做当然严谨，但问题也很直接：

**算一次可以，算一批配体就太贵了。**

而最近，一篇题为 **Binding Free Energies without Alchemy** 的工作，提出了一个很有意思的新思路：**能不能不走那条“炼金路径”，只靠末态采样，直接估算结合自由能？**

作者给出的答案是：**可以试，而且还真做出来了。**

---

## 研究背景

在结构基础药物发现里，**蛋白-配体结合亲和力预测**一直是最核心、也最棘手的问题之一。对接打分虽然快，但通常把受体看得太“硬”；机器学习方法虽然近年来很火，但面对新靶点时，泛化能力仍然是现实挑战。相比之下，**绝对结合自由能（ABFE）** 依然是最接近物理本质、也最被认可的高精度路线之一。问题在于，传统 ABFE 通常依赖大量 alchemical intermediates，因此计算成本极高，很难直接进入大规模虚拟筛选流程。正是在这个背景下，作者提出了 **Direct Binding Free Energy（DBFE）**：一种**基于隐式溶剂、只使用末态模拟、无需炼金中间态**的结合自由能方法。论文指出，DBFE 只需要三类模拟：**受体单独模拟、配体单独模拟、以及复合物模拟**；并且在虚拟筛选场景中，受体和配体轨迹都可以预先计算和复用，从而把每个新配体的边际成本显著压低。论文摘要和方法部分明确强调，这正是 DBFE 的核心优势之一。

---

## 研究结果

### 1）这篇文章，想解决的到底是什么问题？

先说白一点： 传统 ABFE 最大的麻烦，不是“公式不会写”，而是**末态之间几乎没法直接比较**。

为什么？

因为在未结合态里，蛋白和配体彼此“看不见”； 而在结合态里，它们彼此作用、彼此限制。 如果你直接拿这两个末态去做自由能估计，通常会发现——**相空间重叠太低**。

于是，传统方法只能在两者之间硬塞很多中间窗口，让体系慢慢走过去。

而 DBFE 的想法很新：

**既然难点主要来自蛋白和配体拼在一起时的大量空间冲突，那我能不能先分别模拟蛋白、配体和复合物，再通过组合采样与筛选，只保留那些“不会撞车”的构型，最后直接做自由能估计？**

这就是 DBFE 的核心逻辑。

作者将体系拆成三部分理解：**蛋白内部构象、配体内部构象、以及二者之间的刚体相对位姿。**

随后通过：

* 对蛋白、配体和复合物进行末态模拟
* 对蛋白构象、配体构象和相对位姿进行组合采样
* 用 **KD-tree** 快速筛掉有严重空间冲突的构型
* 再对筛选后的样本做统计重加权与自由能估计

最终得到结合自由能。

换句话说，DBFE 不是去“走一条炼金路径”，而是试图**在末态之间直接搭桥**。

---

### 2）它为什么值得关注？因为真的更“省”

这篇工作的一个现实意义非常清楚：

**DBFE 的目标不是只做一个“新公式”，而是想把高精度自由能计算真正往虚拟筛选场景里推。**

论文写得很明确： DBFE 只需要三类模拟，而在实际应用中，**受体模拟和配体模拟可以预计算并缓存**。这意味着，对每个新候选分子来说，新增成本主要只剩下一次复合物模拟。

而对比之下，文中基准测试里的 OBC2 double decoupling，往往需要大量 lambda windows。 在 host-guest 基准中，作者使用了 **26 个 complex lambda windows + 8 个 solvent windows**；在 protein-ligand 基准中，则使用了 **26 个 complex lambda windows + 4 个 solvent windows**。论文讨论部分进一步指出，在虚拟筛选语境下，DBFE 对单个配体的成本可近似理解为只需一次短复合物模拟，相比 OBC2 DD 的 26 个 complex windows，具有大约 **26 倍的单配体模拟成本压缩潜力**。

这也是这篇文章最容易打动做药设、做筛选、做重打分研究者的地方：

**它不是在说“我比所有方法都更准”，而是在说“我可能让高精度方法变得更能用”。**

---

### 3）在 host-guest 体系里，DBFE 还不错

作者先在经典的 **host-guest benchmark** 上测试 DBFE。 这类体系结构相对简单、结合口袋也更明确，所以经常被用来验证自由能方法。

结果挺有意思：

* **DBFE：Pearson r = 0.58**
* **OBC2 DD：Pearson r = 0.48**
* **OBC2 MM/GBSA：Pearson r = 0.31**
* **TIP3P DD：Pearson r = 0.89**

也就是说，在这个 benchmark 上，**DBFE 的相关性优于 OBC2 double decoupling。**

这说明什么？

作者的解释是： 在 host-guest 体系中，DBFE 所包含的**构象熵修正**可能确实起到了作用，而单纯的 MM/GBSA 因为没有这部分修正，所以表现更差。与此同时，显式溶剂的 TIP3P DD 依然最好，说明**水效应仍然很重要**，哪怕在相对简单的主客体体系里也是如此。

> 先别急着说“新方法一定不靠谱”， 至少在 host-guest 这种标准测试里，DBFE 已经跑出了比 OBC2 DD 更好的相关性。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/d1ibKq69vtyTR6pEwVOsyG3fQNTv7g3M8Erbg0w57XKm7u4mKdSpb33cVAjZqpNakgsu13r0tqUyiaEwdianqFoxYiaKibDF7Vl9TnHClicZ1zaUI/640.png)

---

### 4）但到了真正复杂的蛋白-小分子体系，问题就来了

如果说 host-guest 只是“热身”， 那真正决定这篇论文价值的，还是后面的 **protein-ligand benchmark**。

作者测试了 4 类蛋白靶点、54 个复合物。结果如下：

* **DBFE：Pearson r = 0.65**
* **OBC2 DD：Pearson r = 0.73**
* **OBC2 MM/GBSA：Pearson r = 0.71**
* **TIP3P DD：Pearson r = 0.88**

这组结果非常值得玩味。

因为它意味着：

**DBFE 在更真实、更复杂的蛋白-配体体系里，并没有超过传统 OBC2 DD；甚至比 OBC2 MM/GBSA 还略差一点。**

作者对此没有回避，反而讲得很坦率： 这提示 DBFE 中的**构象熵估计**，在复杂蛋白-配体体系里，可能反而引入了额外噪声。

但更关键的是，作者进一步提出了一个非常重要的判断：

**限制隐式溶剂方法精度的核心瓶颈，也许不是自由能估计器本身，而是溶剂模型本身。**

这句话其实很有分量。

因为从结果上看：

* DBFE vs OBC2 DD 的差距，没有那么夸张
* 但 OBC2 系列 vs TIP3P DD 的差距，却非常明显

这说明，如果未来想真正把这条路线做强， 可能最该优先解决的，不是“末态方法还能不能再调一调”， 而是：

**隐式溶剂，究竟还能不能做得更像真实的水。**

> 真正的考验，从来不是 host-guest。 一上蛋白-小分子复杂体系，方法的短板就开始暴露了。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/d1ibKq69vtyTn5n5BdbibCpb6CV4Tzn2DCIGdJwibkpUDfwwWbmwdx2DuhGGRUkJWvrictyFMLribU4LPibT2dFiad6fWby29lsyrVR9zQzbdo7HK8/640.png)

---

### 5）它虽然不走“alchemy”，但结果并没有完全跑偏

这篇文章还有一个很有说服力的结果： 作者专门比较了 **DBFE 和 OBC2 double decoupling** 的预测值一致性。

结果显示，在 host-guest 和 protein-ligand 两个 benchmark 上， 两者整体上都表现出较强相关性。

这意味着：

**DBFE 虽然不再显式构造 alchemical intermediates，但它并不是“另起炉灶胡乱算”，而是在一定程度上逼近了传统 DD 的结果。**

这点很重要。

因为一个新方法最怕两件事：

第一，不准； 第二，连“为什么会这样”都解释不清。

而 DBFE 至少证明了：**它和传统严谨 ABFE 路线，在结果上是有连续性的。**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/d1ibKq69vtyTicROmENgbSCAumzWs3dFofBKHk8PBuibDF1GjTJkWwOuWn28ygeuojzUNzybkCM39xdVuLI8VckHosezrhJKpNgBPaAm9HpYZQ/640.png)

---

### 6）这篇文章真正的价值，不只是“一个新方法”

很多论文看完以后，你会觉得它只是“又多了一个方法名”。

但这篇不太一样。

它真正有价值的地方在于：

**它提出了一种新的思考方向——结合自由能计算，未必一定要靠 alchemical path 才能成立。**

过去大家默认的逻辑是：

> 想算 ABFE，就得走 λ 路径； 想走 λ 路径，就得跑很多中间态； 想跑很多中间态，就注定又贵又慢。

而 DBFE 提供了一种新的可能：

> 我不走那条路， 我只做末态， 但我通过组合采样、空间筛选和统计重加权， 也许一样能逼近结合自由能。

哪怕这条路线今天还不完美， 它也已经把一个问题重新问了一遍：

**ABFE 的未来，真的只能是“更快地做 alchemy”吗？ 还是也可能是“绕开 alchemy”？**

---

## 研究结论

总体来看，这篇工作提出的 **DBFE** 是一种很有启发性的结合自由能计算新框架。它不依赖传统 ABFE 中昂贵的 alchemical intermediates，而是通过**末态模拟、组合采样、空间冲突筛选和统计重加权**来直接估算结合自由能。在 host-guest 体系中，DBFE 的表现优于 OBC2 DD，说明这一路线在简单体系上具有真实潜力；在更复杂的 protein-ligand 体系中，DBFE 虽然尚未超过传统显式溶剂自由能方法，但论文的结果也清楚表明：真正限制隐式溶剂方法上限的，很可能不是是否使用 alchemy，而是**溶剂模型本身**。因此，这篇文章最值得关注的，不只是 DBFE 这个具体方法，更是它背后的方法学信号：**未来高效自由能计算的突破口，可能来自末态统计与采样策略创新，而不一定只来自对 alchemical 路线的不断修补。**

---

> **DBFE 还不是终点， 但它很可能提醒了我们： 结合自由能计算，未必要永远困在“炼金术”里。**

你觉得未来的高精度结合自由能计算， 会继续沿着 **alchemy** 路线优化， 还是会像 DBFE 这样，转向 **end-state** 新范式？

欢迎留言聊聊。

---

_参考文献： arXiv:2603.12253v2 \[q-bio.QM\] 17 Mar 2026_

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
