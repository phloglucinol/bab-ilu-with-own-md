---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzAxMzY2NDc4OQ%3D%3D&mid=2247520856&idx=1&sn=55bd3c1c988e4542d8b07e8c8c7c5095
canonical_url: https://mp.weixin.qq.com/s?__biz=MzAxMzY2NDc4OQ%3D%3D&mid=2247520856&idx=1&sn=55bd3c1c988e4542d8b07e8c8c7c5095
source_domain: mp.weixin.qq.com
title: Scientific reports/盐桥不破，疗效翻倍！BGM0504：分子动力学设计的新一代代谢疾病 “克星”，超越替尔泊肽
author: 
published_at: 
fetched_at: 2026-04-25T02:04:06Z
extractor: wechat_worker
content_hash: ac8b0476a2e216049586b932ef708026c155509d217dd6c4ec52d2179a2ce0eb
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeybH61ia6IaO05FosY5RicucaVGia9f1Qt8NALdGAdpX1r8icpTicQWbiaGwNQ/0.jpg) 

# Scientific reports/盐桥不破，疗效翻倍！BGM0504：分子动力学设计的新一代代谢疾病 “克星”，超越替尔泊肽

[ 生物密码情报局 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyfbQq792L4iaB3J0KK3wjDOITje5SIVegzCTgicwUuRXpo2JKSka7CbJA/640.png)

摘要：胰高血糖素样肽 - 1 受体（GLP-1R）和葡萄糖依赖性促胰岛素多肽受体（GIPR）的双重激活，已成为治疗 2 型糖尿病和肥胖症的潜在有效策略。双激动剂肽替尔泊肽（Tirzepatide）在血糖控制和体重管理方面，展现出优于选择性 GLP-1R 激动剂的临床疗效。然而，替尔泊肽通过母肽上的酰化侧链实现半衰期延长，其结构基础引发了关于其部分激动活性的疑问。

本研究利用分子动力学模拟，探究了肽与受体相互作用的动态过程，发现母肽上的 K20 残基与 GLP-1R/GIPR 之间存在关键盐桥作用，这一特征在冷冻电镜结构中未被识别。基于该发现，我们开发了一种基于母肽的优化策略，核心是重新定位酰化侧链。体外和体内实验结果表明，优化后的肽段激动活性较替尔泊肽提升 2-3 倍，同时保留了血浆中延长的半衰期。据此设计出 BGM0504，在实验室和动物研究中均表现出优于前代药物替尔泊肽的疗效。
  
  
01.替尔泊肽结构分析

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyAtkJWrdzjf67zeAficO6t2fZ60hHSEHia9DicLaJkpX5GW2KN4DIrTrTA/640.webp)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyNsyiaia7wmgiaibRXpA5icvkvqFKypFAQ8JibOtAd3YYyghMic7nRl1ib4IgNw/640.webp)

  
作为研究生物分子构象分布的工具，分子动力学模拟方法在研究生物分子的多种构象状态和构象变化机制方面表现出可靠性能 \[19-21\]。本研究中，我们通过 Amber 18 \[22\]、MOE2022 \[23\]、Antechamber \[24,25\] 进行分子动力学模拟，利用 CHARMM-GUI 构建膜结构 \[26\]，通过 Amber18 中集成的 charmmlipid2amber.py 脚本将 CHARMM-GUI 生成的 PDB 文件转换为 Amber 格式。蛋白质、POPC 膜和配体分子分别采用 AMBERff15ipq-m \[27\]、lipid14 \[28\] 和通用 Amber 力场 2（GAFF2）\[29\]，并使用 AM1-BCC \[25\]、SHAKE \[30\]、PME \[31,32\]、CPPTRAJ \[33\] 算法或方法。

为阐明 K20 酰化修饰后，未酰化替尔泊肽刺激 cAMP 积累活性降低的原因，我们分析了 GLP-1R / 未酰化替尔泊肽（PDB: 7VBI）和 GIPR / 未酰化替尔泊肽（PDB: 7FIY）复合物的结构 \[20\]。结果显示，未酰化替尔泊肽的 K20 可与 GLP-1R 的 E128ECD 形成盐桥，但与 GIPR 之间未观察到显著的有利相互作用（图 1）。从构效关系来看，K20 位的酰化修饰导致 E128ECD-K20 未酰化替尔泊肽的盐桥消失，这可能是未酰化替尔泊肽对 GIPR 刺激 cAMP 积累活性更高的原因。然而，在 GIPR / 未酰化替尔泊肽复合物中，K20 与 GIPR 无直接显著相互作用，因此无法解释未酰化替尔泊肽对 GIPR 的高激动活性。

基于这一假设，我们以上述两组复合物为初始构象，分别进行了 500ns 的分子动力学模拟（排除 G 蛋白和 Nb35，肽 - 受体复合物用 MOE2022 制备），并设置三组平行实验。均方根偏差（RMSD）反映了叠加的蛋白质 / 肽结构 CA 原子之间的平均距离，指示两种结构的相似程度。结果显示，未酰化替尔泊肽在 GLP-1R/GIPR 结合位点保持稳定结合，但 GIPR 复合物的稳定性不如 GLP-1R 复合物，这源于 GIPR 的 ECL1 结构柔性导致的 ECD 区域和肽段构象波动。下文所有结合自由能值和盐桥占有率均为三组平行 MD 模拟的平均值。

此外，如图 1b所示，我们发现 GLP-1R 中 E128ECD-K20 未酰化替尔泊肽和 E127ECD-K20 未酰化替尔泊肽均可形成盐桥，其占有率（即出现该作用的帧比例）分别为 88.3% 和 80.7%。有趣的是，在 GIPR 复合物的分子动力学模拟轨迹分析中，E119ECD-K20 未酰化替尔泊肽形成盐桥的占有率为 66.5%。GLP-1R 复合物中的 K20 未酰化替尔泊肽可与 E128ECD 和 E127ECD 均形成盐桥，而 GIPR 复合物中的 K20 未酰化替尔泊肽可与 E119ECD 形成盐桥（图 1b 右上）。通过 MMGBSA 计算的结合自由能显示，未酰化替尔泊肽对 GLP-1R（-179.06 vs. -161.38 kcal/mol）和 GIPR（-160.59 vs. -152.82 kcal/mol）的结合亲和力均优于替尔泊肽。这一结果从分子动力学角度解释了为何替尔泊肽的 K20 酰化修饰会导致其对 GLP-1R/GIPR 刺激 cAMP 积累的活性降低。
  
  
02.内容归纳

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyAtkJWrdzjf67zeAficO6t2fZ60hHSEHia9DicLaJkpX5GW2KN4DIrTrTA/640.webp)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyNsyiaia7wmgiaibRXpA5icvkvqFKypFAQ8JibOtAd3YYyghMic7nRl1ib4IgNw/640.webp)

  
（一）研究背景与核心问题

疾病现状：肥胖症和 2 型糖尿病（T2DM）发病率高，且互为关联，还会增加微血管并发症、非酒精性脂肪肝（NASH）等疾病风险，对全球健康和社会经济发展构成严峻挑战。

现有治疗局限：GLP-1R 单激动剂需高剂量使用，易引发胃肠道副作用；替尔泊肽作为 GLP-1R/GIPR 双激动剂，虽半衰期延长（依赖 K20 酰化修饰），但酰化会降低其激动活性，分子层面的机制尚未明确。

研究目标：通过分子动力学模拟解析替尔泊肽活性降低的原因，优化设计新型双靶点激动剂，在保留长半衰期的同时提升激动活性。

（二）BGM0504 的设计原理与优化策略

| 优化核心  | 替尔泊肽的问题           | BGM0504 的解决方案           | 关键机制                                                                    |
| ----- | ----------------- | ----------------------- | ----------------------------------------------------------------------- |
| 酰化位点  | K20 酰化破坏盐桥，降低激动活性 | 将酰化位点转移至 C 端（新增 K40 残基） | 保留 K20 与 GLP-1R 的 E128ECD/E127ECD、GIPR 的 E119ECD 形成的盐桥（占有率 66.5%-93.1%） |
| 连接链长度 | γGlu-2×OEG 连接链较短  | 替换为 γGlu-2×3PEG 连接链     | 延长连接链以适配 C 端与受体的距离，增强酰化侧链与受体 ECL1/ECD 的相互作用                             |
| 构象稳定性 | \-                | 利用 C 端 Trp 笼基序维持折叠结构    | 保证肽段与受体结合后的构象稳定，提升结合亲和力                                                 |

（三）实验验证结果

1\. 体外实验

激动活性：BGM0504 对 GLP-1R/GIPR 的 EC50 值分别为 0.031nM 和 0.182nM，激动活性是替尔泊肽（EC50：0.086nM/0.441nM）的 2-3 倍。

结合亲和力：通过生物层干涉法（BLI）检测，BGM0504 与人体血清白蛋白（HSA）的结合解离常数（KD）为 73.04nM，与替尔泊肽（KD：86.30nM）相当，保证半衰期延长的基础。

结合自由能：MMGBSA 计算显示，BGM0504 对 GLP-1R（-182.39 kcal/mol）和 GIPR（-166.96 kcal/mol）的结合亲和力均优于替尔泊肽（-161.38/-152.82 kcal/mol）。

2\. 体内实验

| 实验模型                                 | 检测指标                                       | BGM0504 的表现                  | 与替尔泊肽的对比                  |
| ------------------------------------ | ------------------------------------------ | ---------------------------- | ------------------------- |
| db/db 小鼠（2 型糖尿病模型）                   | 非空腹血糖                                      | 给药 72h 内显著抑制血糖，高剂量组维持低水平时间更长 | 同等剂量（0.15mg/kg）下，血糖控制效果更优 |
| | 血清胰岛素                              | 剂量依赖性降低胰岛素浓度，差异具有统计学意义（p≤0.05）             | 0.15mg/kg 剂量组降低效果显著优于替尔泊肽    |                           |
| | 体重 / 进食量                           | 给药初期快速下降，后期保持稳定                            | 对代谢指标的调控更温和持久                |                           |
| STZ+HFD 诱导 C57BL/6 小鼠（糖尿病 + NASH 模型） | 肝功能指标（ALT/AST）                             | 剂量依赖性降低，ALT 水平改善更显著          | 优于替尔泊肽，且接近正常对照组水平         |
| | 肝脏脂质（TC/TG）                        | 显著降低肝脏总胆固醇和甘油三酯含量                          | 0.15mg/kg 剂量组可恢复至正常对照组水平     |                           |
| | 肝纤维化 / NAS 评分                      | 降低肝纤维化率（0.15mg/kg 组达正常水平的 55%），显著降低 NAS 评分 | 对 NASH 的进展有明显抑制作用            |                           |

3\. 药代动力学特征（SD 大鼠 + 食蟹猴模型）

半衰期（T1/2）：食蟹猴静脉注射（0.1mg/kg）后 T1/2 为 37.9h，皮下注射（0.2-5mg/kg）后 T1/2 为 38.7-43.4h，长于 SD 大鼠（13.6-14.7h）。

生物利用度：食蟹猴皮下注射生物利用度为 60.5%-69.7%，SD 大鼠为 34.3%-44.5%，暴露量（AUC0-last）与剂量呈正比。

安全性：未观察到性别差异或明显不良反应，药代动力学特征稳定，适合临床应用。

（四）核心优势总结

活性更强：体外 / 体内实验均证明，BGM0504 对 GLP-1R/GIPR 的激动活性是替尔泊肽的 2-3 倍，血糖控制、胰岛素调节效果更优。

功能全面：除治疗糖尿病和肥胖外，对 NASH 具有显著改善作用，可降低肝功能损伤、肝脏脂质沉积和纤维化。

药代优异：保留长半衰期（食蟹猴 T1/2 超 38h），生物利用度高，暴露量与剂量呈正比，具备临床转化潜力。
  
  
03.主题总结

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyAtkJWrdzjf67zeAficO6t2fZ60hHSEHia9DicLaJkpX5GW2KN4DIrTrTA/640.webp)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyNsyiaia7wmgiaibRXpA5icvkvqFKypFAQ8JibOtAd3YYyghMic7nRl1ib4IgNw/640.webp)

  
本文围绕 “优化 GLP-1R/GIPR 双靶点激动剂的活性与药代动力学平衡” 这一核心，通过分子动力学模拟揭示了替尔泊肽 K20 酰化修饰导致激动活性降低的关键机制 —— 破坏了 K20 与受体之间的盐桥作用。基于该发现，研究团队设计了新型激动剂 BGM0504，通过 “转移酰化位点至 C 端、延长连接链” 的优化策略，在保留长半衰期的同时，将激动活性提升 2-3 倍。

实验验证表明，BGM0504 在糖尿病模型中展现出更优的血糖和胰岛素调控效果，在 NASH 模型中能有效改善肝功能、降低肝脏脂质沉积和纤维化，且药代动力学特征稳定，生物利用度高。核心主题可概括为：以分子动力学模拟为指导，通过精准结构优化，开发出兼具高激动活性、长半衰期和多适应症潜力的 GLP-1R/GIPR 双靶点激动剂，为糖尿病、肥胖症及 NASH 的治疗提供了更高效的新型候选药物。
  
  
04.核心图片

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyAtkJWrdzjf67zeAficO6t2fZ60hHSEHia9DicLaJkpX5GW2KN4DIrTrTA/640.webp)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyNsyiaia7wmgiaibRXpA5icvkvqFKypFAQ8JibOtAd3YYyghMic7nRl1ib4IgNw/640.webp)

  
图 1：替尔泊肽与 BGM0504 的结构分析及优化策略

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyicgYFQMqA044S7iaicKlYgFywjzUnlQHoPTAZmAA9sCoALicanN2oXnYqA/640.png)

核心元素：左 / 右侧分别展示替尔泊肽母肽与 GLP-1R/GIPR 的结合结构，放大 K20 位点的盐桥作用；中间呈现优化策略 —— 将替尔泊肽 K20 位的酰化侧链转移至 C 端新增的 K40 位；下方展示 BGM0504 的序列及 γGlu-2×3PEG 连接链与 C18 脂肪酸酰化修饰。

关键标注：明确盐桥形成位点（E127/E128/E119 与 K20）、酰化位点转移方向，直观体现优化核心逻辑。

  
图 2：BGM0504 的结构分析与性能测试

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyFRj5fJNKMfT0yqvH7Yh4J3Ca8UGqMzeJ3fqg68ajdwLTC3HOnaY5BQ/640.png)

核心元素：（a）BGM0504 在替尔泊肽基础上新增 K40 氨基酸，酰化侧链从 K20 转移至 K40；（b-e）GLP-1R/GIPR 分别与替尔泊肽、BGM0504 结合的 RMSD 曲线及 500ns 主结构放大图，展示 BGM0504 构象更稳定；（f）cAMP 积累实验的 EC50 结果对比，直观呈现 BGM0504 活性优势；（g）BGM0504 与替尔泊肽结合 HSA 的 BLI 测试曲线。

  
图 3：db/db 小鼠体内实验结果

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyAicCPsh7iatzCzCtfsMAYibcUgaq3PiaOlDnFjgwBASLKC2WDMrPibnQibww/640.png)

核心元素：（a）非空腹血糖监测曲线，展示给药 72h 内各剂量组（0.05/0.15/0.5mg/kg BGM0504）与替尔泊肽（0.15mg/kg）的血糖抑制效果，体现 BGM0504 的剂量依赖性优势；（b）血清胰岛素检测柱状图，标注统计显著性差异（p≤0.05），显示 BGM0504 降低胰岛素的效果更显著。

  
图 4：STZ+HFD 诱导 C57BL/6 小鼠体内实验结果

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeypagfcHowZsOichjwXjCDIOuQFniblib5HW7jDukTsSaXz0mW1aiaDncTeQ/640.png)

核心元素：（a）肝组织 H&E 染色图，对比模型组、替尔泊肽组与 BGM0504 组的肝细胞脂肪变性程度；（b）天狼星红（SR）染色图，展示肝脏纤维化改善情况；（c-j）柱状图分别呈现 ALT/AST、NAS 评分、肝脏 TC/TG、纤维化率、LDL/HDL 水平，清晰对比各组治疗效果，突出 BGM0504 在改善肝功能和血脂方面的优势。
  
  
05.未来展望

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyAtkJWrdzjf67zeAficO6t2fZ60hHSEHia9DicLaJkpX5GW2KN4DIrTrTA/640.webp)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/zXkvMydN2lqSCSzgCyzIPYot3QT9xKeyNsyiaia7wmgiaibRXpA5icvkvqFKypFAQ8JibOtAd3YYyghMic7nRl1ib4IgNw/640.webp)

  
未来，BGM0504 的研发与应用可向以下方向推进：

临床转化深化

1. 开展Ⅰ-Ⅲ期临床试验，验证 BGM0504 在人体中的安全性、有效性和剂量方案，重点关注其对糖尿病合并 NASH 患者的综合疗效，明确与替尔泊肽的临床优势差异。

适应症拓展

1. 基于其对代谢指标和肝脏功能的改善作用，探索用于非酒精性脂肪性肝病（NAFLD）、代谢综合征等相关疾病的治疗潜力，扩大临床应用场景。

结构进一步优化

1. 结合人工智能与分子动力学模拟，优化连接链长度、酰化基团结构或肽段序列，进一步提升受体选择性、降低潜在副作用，或开发口服制剂以提高患者依从性。

作用机制深挖

1. 深入研究 BGM0504 对 GLP-1R/GIPR 下游信号通路的调控差异，明确其改善 NASH 的具体分子机制（如线粒体功能调节、脂质合成抑制等），为联合用药提供理论依据。

产业化与临床应用

1. 推进生产工艺优化，降低生产成本，同时建立精准的患者筛选体系，实现个体化治疗，让这一新型双靶点激动剂更好地惠及糖尿病、肥胖症及相关并发症患者。

原文链接DIO: https://www.nature.com/articles/s41598-024-66998-8

声明：以上只代表个人的观点，不包含任何投资建议；文中信息不当或不准确的地方，欢迎留言或私信指正。文中图片来自于公开渠道可获取的资料，若涉及隐私及保密信息或若有侵权请联系删除。

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zXkvMydN2lq5pe9segmMKKjibpg2H2Oic5Xo0mqQ9b9VtdLV89oXkpFx7EMajDDmhXzsk35ssibq9gzA8FF0qiaWtQ/0.png) 

 生物密码情报局 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/zXkvMydN2lq5pe9segmMKKjibpg2H2Oic5Xo0mqQ9b9VtdLV89oXkpFx7EMajDDmhXzsk35ssibq9gzA8FF0qiaWtQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
