---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247486956&idx=1&sn=860db97aacb05c81f9e73fa142c9a2d3
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247486956&idx=1&sn=860db97aacb05c81f9e73fa142c9a2d3
source_domain: mp.weixin.qq.com
title: Nat. Chem. Biol. | 化学宇宙的“大爆炸”
author: 
published_at: 
fetched_at: 2026-04-25T02:04:03Z
extractor: wechat_worker
content_hash: d9773de03bacaf42db1f30cc9ad74a652685577852f183b95ec1f511aede09c5
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/KoRXqKjLA9ib8PDp5LYalZiaQ9EnKIn0E0hLVtzicAKY7ZjU0N9QDKlGl8DHqAq5okxUK9uTORnTNIkZOUG23IVpA/0.jpg) 

# Nat. Chem. Biol. | 化学宇宙的“大爆炸”

[ DrugIntel ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9ib8PDp5LYalZiaQ9EnKIn0E0Nh1icz2yia9yIFuSvpp9ObCDHiaHhc2CjQEoQPXILK6v2M4I1sQ5pEpLw/640.png)

作者：Artem Cherkasov（原载 《Nature Chemical Biology》 2023年）

现代药物发现依赖于对“库存”与“按需”虚拟化合物库的智能探索。一项比较分析突显了可访问化学空间的爆炸式扩张，同时揭示了计算药物发现领域随之而来的挑战与机遇。

在开发新治疗药物的过程中，近90%的候选化合物在临床试验中失败，这使得开发单一药物的平均成本攀升至惊人的28亿美元。有观点认为，通过使用能够进行虚拟筛选以发现新颖且有利化学型的超大型化学库，可以改善这种成功率和成本问题。近年来，机器人技术的进步以及人工智能（AI）引导的合成建模方法的出现，共同推动了此类虚拟库的空前增长。例如，常用于虚拟筛选以识别计算命中化合物的ZINC数据库，在2004年时包含的分子数量不足100万，而最新更新的ZINC22版本则包含了超过370亿个独特的化学条目——在大约18年间增长了超过5万倍，其中最为剧烈的“大爆炸”式扩张发生在过去两年（图1）。

与此同时，计算机辅助药物发现（CADD）领域中“越大越好”这一范式的有效性正受到越来越多的审视。人们关注的是，近期可挖掘“化学宇宙”的爆炸式增长，带来的挑战是否多于机遇？在《Nature Chemical Biology》本期中，Lyu等人发表了一项综合分析《Modeling the expansion of virtual screening libraries》，通过数个成功的药物发现案例表明，**对超大型化学库进行虚拟筛选确实能够带来更优配体的发现**。作者特别聚焦于**三个基本问题**：**①**随着化合物库规模的扩大，我们是否能看到评分更优（与受体契合度更好）的分子数量增加？**②**与类生物分子（‘bio-like’ molecules）的相似性随着库的扩张发生了怎样的变化？以及，**③**罕见但排名靠前的假阳性结果的识别会如何随库的扩张而变化？

这三个问题反映了CADD中一些非常重要但尚未在实际背景下被全面审视的主题。Lyu等人采用的方法是，同时评估百万级别规模的“库存”化合物库和十亿级别规模的“按需定制”化合物集合，因为这两者共同体现了化学空间的最新扩张。他们**从化合物的类药性、极性表面积分布、形式电荷、可旋转键数量、疏水性等CADD常规关注的分子性质方面对这两个数据集进行了比较**。重要的是，作者利用他们之前成功的对接活动所获得的实验结果，研究了不同规模数据库中对接评分的分布情况，并查验了经实验确认的命中化合物与类药分子和天然物质的相似性。最后，他们分析了在超大规模对接实践中出现的排名靠前的假阳性结果及其来源。

这项全面的回顾性分析使Lyu等人得出结论：**随着对接数据集规模的增大，确实发现了更多评分更高的分子**，且评分随着虚拟筛选库规模的扩大呈对数线性提高。此外，他们指出，**更大的按需定制库不仅能产生更多活性化合物，还能产生效力更强的配体**。这些是非常重要的发现，为在CADD中使用超大型化学库提供了充分理由，并丰富了当前的最佳实践。

其次，分析表明，在所分析的虚拟筛选中，**那些经过实验验证的高排名命中化合物通常并不“类生物”**。这一观察结果一方面挑战了在许多药物发现流程中常规使用的各种类天然产物或类代谢物过滤器的价值；另一方面，它也进一步凸显了超大型按需定制库作为能够有效结合生物靶标的小分子丰富来源的价值。

最后，作者证明，**使用更大的对接库会增加假阳性预测的可能性**。尽管CADD从业者普遍知晓会出现人为导致高评分的非活性化合物，但Lyu等人提出，在大规模对接活动中，此类对接假象甚至可能压倒真正的阳性结果。因此，需要通过改进当前评分函数的不足以及采用各种共识策略来调整命中化合物的选择策略，以最大限度地降低对接假象带来的风险。

总体而言，这项研究为利用正以爆炸速度持续扩张的超大型化学库进行药物发现提供了若干实用且重要的见解（图1）。尽管本研究结论尚需未来使用不同对接程序和多样化生物靶标进行进一步的实验评估，但其结果无疑为未来进一步拓展和利用这个巨大的化学宇宙奠定了坚实基础，这个宇宙很可能不仅包含易于合成的分子，更重要的是，将包含具有药学价值的分子。

参考文献：Cherkasov, A. The ‘Big Bang’ of the chemical universe. _Nat Chem Biol_ **19**, 667–668 (2023).

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icaZmJVvQe5nCiabibOyaceianZY23nlsXAkxR5uiajvHibdBJvESicc58tOeibVXmVTp4HVVADZh79C1iczA/0.png) 

 DrugIntel 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icaZmJVvQe5nCiabibOyaceianZY23nlsXAkxR5uiajvHibdBJvESicc58tOeibVXmVTp4HVVADZh79C1iczA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
