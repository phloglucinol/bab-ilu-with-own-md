---
type: raw_article
source_url: https://mp.weixin.qq.com/s/R-pOfU6dUV1UTPHMTxD3NQ
canonical_url: https://mp.weixin.qq.com/s/R-pOfU6dUV1UTPHMTxD3NQ
source_domain: mp.weixin.qq.com
title: AF2RAVE :  将动态构象注入AlphaFold2，助力虚拟筛选
author: 
published_at: 
fetched_at: 2026-04-25T02:04:30Z
extractor: wechat_worker
content_hash: d3b0ca654f72a4ff83314be5bbd2e340b3d774715b2613ab1770e15c1c7a9fa2
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/KoRXqKjLA99AiaP7BqKcmLwGYf7dVXUY0SIQxMYRHQiaMOQHT0kcLLMaiaZr0KXu0eZE6dq5e3DSA4akPediagUZIw/0.jpg) 

# AF2RAVE : 将动态构象注入AlphaFold2，助力虚拟筛选

[ DrugIntel ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

# 在药物研发的漫长征程中，对蛋白质结构与功能的精准理解是迈向成功的基石。蛋白质，作为生命活动的主要执行者，其功能并非由单一静态结构所决定，而是依赖于在亚稳构象之间的动态转换。这些构象变化丰富多样，且许多在同源蛋白间并不保守，为选择性药物设计带来了契机，但同时也对精准建模和药物筛选提出了严峻挑战。近期发表于《Journal of Chemical Theory and Computation》的一项研究，开发出了一款创新工具——hierarchical AF2RAVE，为蛋白质动态研究及药物筛选领域注入了新的活力，有望打破传统方法的局限，实现药物研发效率的飞跃。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/KoRXqKjLA99AiaP7BqKcmLwGYf7dVXUY0BBjYrII24omGcmoar7SG93icLRSyRtzib16Yibsd24AtTDOg4wAQWSIKg/640.jpg)

## 一、传统方法的局限性剖析

### （一）AlphaFold2的不足

自问世以来，AlphaFold2在蛋白质结构预测领域取得了突破性进展，能够从氨基酸序列高效预测蛋白质的天然无配体（apo）结构，准确性超越了众多传统模型。然而，其在药物研发应用中存在显著短板。一方面，AlphaFold2通常输出单一结构，难以全面反映蛋白质在生理状态下的动态构象变化，而这些动态构象往往与药物结合及功能发挥密切相关。另一方面，该模型主要聚焦于无配体状态，在预测配体结合的全酶（holo）结构时存在局限性，无法精准呈现药物分子与靶点结合时蛋白质的真实构象状态，导致在虚拟筛选中可能遗漏潜在的活性化合物。

### （二）X射线晶体学的缺陷

X射线晶体学作为获取蛋白质结构的经典实验手段，为药物研发提供了大量关键的结构信息。然而，该方法存在固有缺陷。在结晶过程中，蛋白质所处的环境与生理状态差异较大，可能导致蛋白质形成特定的结晶构象，这种构象未必能准确代表其在溶液中与药物分子相互作用时的真实状态，存在“假象”风险。此外，对于一些难以结晶的蛋白质，尤其是具有高度动态特性或柔性区域的蛋白质，X射线晶体学技术面临巨大挑战，限制了其在广泛蛋白质靶点研究中的应用。

### （三）药物筛选中的困境

在药物筛选环节，精准捕捉蛋白质的“待结合”活性构象至关重要。传统方法由于无法精确刻画蛋白质的动态构象，常常导致筛选出的化合物与靶点结合能力不佳或出现“脱靶”现象，极大地降低了药物研发的成功率，延长了研发周期，增加了研发成本。以S100钙结合蛋白家族为例，该家族蛋白在细胞内信号传导等过程中发挥关键作用，与癌症、阿尔茨海默病等多种重大疾病密切相关。其构象变化迅速且复杂，不同成员间结构高度同源，传统方法难以有效区分并针对其特定活性构象设计抑制剂，使得针对该家族蛋白的药物研发进展缓慢。

## 二、AF2RAVE的技术解析

### （一）创新的两步采样策略

AF2RAVE采用了独特的分层式工作流程，将AlphaFold2与基于机器学习的增强采样技术有机结合，系统地探索蛋白质体系的自由能景观和亚稳特性，尤其在蛋白质骨架和侧链层面实现了深度构象分析。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99AiaP7BqKcmLwGYf7dVXUY0GibAWQdrv3ArsNl76Yhcibz4ov3sFzsfeYXn70c4C1BtiaJzHXO0zuecg/640.png)

1. **全局SPIB（骨架层面）**：在第一步全局采样中，利用状态预测信息瓶颈（SPIB）方法，重点关注蛋白质骨架的大规模运动。通过分析蛋白质结构的关键自由度，识别出决定蛋白质整体构象变化的主要因素，捕捉如蛋白质口袋开合等缓慢但关键的构象转变过程。这种全局视角的分析为后续深入研究侧链细节提供了宏观框架，确保在整体构象变化的背景下理解蛋白质功能。
2. **局部SPIB（侧链层面）**：第二步的局部采样则聚焦于结合口袋区域的侧链原子运动。侧链的细微变化对蛋白质与配体的特异性结合起着决定性作用。通过局部SPIB方法，精确探测结合口袋内关键残基的侧链旋转、摆动等微观运动，定位可能影响药物结合亲和力和特异性的关键位点，为精准药物设计提供原子层面的详细信息。

### （二）从序列到动态构象的高效生成

AF2RAVE的一大显著优势在于，只需输入蛋白质的氨基酸序列，即可启动从结构预测到动态构象生成的全流程。首先，利用AlphaFold2基于序列预测蛋白质的初始结构，然后通过增强采样技术对初始结构进行多样化拓展，生成一系列更接近蛋白质在生理条件下与配体结合时的 holo 构象。这些构象不仅涵盖了蛋白质骨架的多种可能排列方式，还细致呈现了侧链原子在不同构象状态下的分布情况，全面模拟了药物分子结合前蛋白质的动态预备状态，为虚拟筛选提供了丰富且精准的构象模型库。

### （三）卓越的实战性能表现

研究团队针对S100B蛋白对AF2RAVE进行了全面的性能测试，结果令人瞩目。

1. **回顾性对接**：在回顾性对接实验中，AF2RAVE生成的蛋白质构象与已知的真实配体结合构象之间的匹配度大幅超越了AlphaFold2预测的结构。这表明AF2RAVE能够更准确地模拟蛋白质在与药物分子相互作用时的实际构象变化，为评估化合物与靶点的结合模式提供了更可靠的结构模型。
2. **富集测试**：在富集测试环节，AF2RAVE的表现更为出色。它不仅优于AlphaFold2，甚至在区分“真抑制剂”和“假阳性分子”方面超越了实验测定的X射线晶体结构。富集因子（enrichment factor）作为衡量虚拟筛选方法性能的关键指标，AF2RAVE使其得到了显著提升，意味着在大规模化合物库筛选中，能够更高效地富集具有潜在活性的化合物，极大地提高了药物筛选的命中率和效率。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99AiaP7BqKcmLwGYf7dVXUY0wqOJBLowAHI8u45tP7xxzZia70SSSw1Jibp6HHxlobpQliaJ0yEa4kYWg/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99AiaP7BqKcmLwGYf7dVXUY0YzAqzoic6hhmH1OVBw9tgnrjFOOqnagbFRibc2dQ5eDWjvYVJ4xplbOw/640.png)

## 三、AF2RAVE优势的深度剖析

### （一）全面覆盖动态构象

与传统方法依赖单一静态结构不同，AF2RAVE致力于生成多样化的活性构象库。通过对蛋白质自由能景观的系统探索，涵盖了从低频的骨架重排到高频的侧链热运动等多种构象变化，确保在虚拟筛选中能够为药物分子提供更多可能的结合模式。这种全面性极大地增加了发现新型抑制剂的概率，尤其对于那些依赖蛋白质动态构象发挥功能的靶点，具有不可替代的优势。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99AiaP7BqKcmLwGYf7dVXUY0okLXDl2clOxjuDwuyLGiaEYFobb9icxs5d8xwkYPCXobMydgVZAkJqZw/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99AiaP7BqKcmLwGYf7dVXUY0FSBa77jex67VDP3hawygicrQFcXxuI8Cy7FmUqdPzT5oTD7jZicpEp8Q/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA99AiaP7BqKcmLwGYf7dVXUY0Lm0trsXeaBsdicvRULvYBuN5cM6ZArLRG5SciaqB0derduw2AqIUJpMQ/640.png)

### （二）规避结晶相关问题

X射线晶体学由于结晶条件的限制可能导致蛋白质构象失真，而AF2RAVE基于物理模拟和机器学习的方法，无需结晶过程即可生成构象。其通过对蛋白质内在物理性质和动态行为的建模，更真实地反映了蛋白质在生理溶液环境中的构象状态，有效避免了因结晶假象导致的药物筛选偏差，为药物研发提供了更贴近实际情况的结构基础。

### （三）显著提升筛选效率

在药物研发的早期阶段，高通量虚拟筛选需要处理海量的化合物数据，计算效率至关重要。AF2RAVE从序列出发直接生成可用的蛋白质构象，无需耗时费力的实验操作，大大缩短了从靶点确定到虚拟筛选的时间周期。同时，其高效的计算算法能够在相对较短的时间内完成大规模的构象搜索和分析，显著提升了虚拟筛选的通量和速度，使研发人员能够在更短的时间内对大量化合物进行评估，加速药物研发进程。

## 四、AF2RAVE的应用前景展望

### （一）为疑难疾病靶点开辟新路径

癌症、神经退行性疾病等复杂疾病往往涉及多个异常的蛋白质靶点，且这些靶点的结构和功能机制复杂，传统药物研发手段难以突破。AF2RAVE能够精准解析蛋白质的动态构象，发现潜在的药物结合位点，为针对这些疑难靶点的药物设计提供新的思路和结构基础。例如，在阿尔茨海默病中，一些关键蛋白质的错误折叠和异常聚集与疾病发生发展密切相关，AF2RAVE有望揭示这些蛋白质在不同阶段的动态构象变化，为开发干预其病理过程的药物提供关键线索。

### （二）助力高选择性抑制剂设计

药物的副作用往往源于其对非靶标蛋白的“脱靶”作用。AF2RAVE通过精准捕捉蛋白质的特异性活性构象，能够帮助研发人员设计出更具选择性的抑制剂。针对特定靶点的独特构象特征，优化药物分子的结构，使其仅与目标靶点发生特异性结合，而对其他相似蛋白的影响降至最低，从而显著提高药物的治疗指数，为患者带来更安全有效的治疗方案。

### （三）推动多学科深度融合发展

AF2RAVE的成功开发是人工智能、计算化学、结构生物学等多学科交叉融合的成果。其应用将进一步促进这些学科之间的深度合作与交流。在未来的研究中，随着各学科技术的不断进步，AF2RAVE有望与更先进的分子动力学模拟方法、深度学习算法以及实验技术相结合，形成更完善的药物研发技术体系。例如，结合冷冻电镜技术获得的高分辨率结构信息，进一步优化AF2RAVE的构象预测模型，实现理论计算与实验数据的相互验证和补充，推动药物研发从经验驱动向精准理性设计转变。

目前，研究团队已将AF2RAVE的代码开源（https://github.com/tiwarylab/Hierarchical\_AF2RAVE\_S100），这一举措将极大地促进该技术在全球科研和工业界的广泛应用与进一步优化。

参考文献：Xinyu Gu, Venkata Sai Sreyas Adury, Akashnathan Aranganathan, Xinhao Zhuang, Kristen M. Varney, David J. Weber, and Pratyush Tiwary, Hierarchical AF2RAVE for Multiconformation Virtual Screening Targeting S100 Ca2+-Binding Proteins, Journal of Chemical Theory and Computation, 2025.

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
