---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk4ODA4MjQyNw%3D%3D&mid=2247485518&idx=1&sn=d651781811698374201c2f47d811de05
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk4ODA4MjQyNw%3D%3D&mid=2247485518&idx=1&sn=d651781811698374201c2f47d811de05
source_domain: mp.weixin.qq.com
title: CYP3A4/P-gp的底物更容易出现非线性PK！讨论药物的非线性PK问题！
author: 
published_at: 
fetched_at: 2026-04-25T02:04:06Z
extractor: wechat_worker
content_hash: 571c5e64d0b495583ab665f7909ce9b51fdfc3a827a3a79c2798c29ed3181424
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/qPA7ibWx6uicY5MymjGSQLMuTrTiaXLS3ict9JYctLU10UtCgs7eeMmxUicSN7WJuXFUHQSmxNFMz8HAJODVniao5USw/0.jpg) 

# CYP3A4/P-gp的底物更容易出现非线性PK！讨论药物的非线性PK问题！

原创 大龙phd 大龙phd [ 药界物语 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

欢迎大家关注公众号和视频号！

**前言**

上个星期，有一个朋友和我说了一下他遇到的非线性PK的问题，聊了一下。其实我自己碰到的在临床前动物上存在非线性PK的化合物不在少数，可谓是家常便饭了。所以大家遇到的时候也不用觉得太惊讶！甚至很多临床上的药物也都存在这种情况。

巧合的是，假如大家看过三周前我写的关于英矽智能的PKMYT1 PROTAC研发逻辑的文章，或者看过我那期直播的话，可能会有印象。文章中的PROTAC的口服PK几乎都是非线性的，剂量归一化的暴露量不是随着剂量非线性的增加，就是非线性的下降。不知道大家遇到的非线性PK都是啥样的。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/qPA7ibWx6uicY5MymjGSQLMuTrTiaXLS3ictKCweI6lIFEXnCLyJHOmMjFqY9kbxBh7xPra1C3enwjTFib0yH0rr59w/640.png)

今天来聊一下药物出现的非线性PK的问题吧。

1\. **药物出现口服非线性** **PK** **的机制**

非线性PK可能由单一或者多种机制引起，这也是我们研究药物ADME的其中一个价值所在。什么样的ADME特点，多大剂量下或者多大的cmax会出现可能会出现非线性PK。当然，很多都是发现了非线性PK的现象，再回过头来去做ADME，寻找可能的原因。包括药物的溶解度限制、渗透限制、外排转运体的饱和、摄取转运体饱和、PBB饱和、代谢酶饱和等原因，当然还有代谢酶和转运体的抑制（概率相对较小）。

前面提到，非线性PK一般分为两类：1\. 暴露量随剂量增加不成比例的增长 2\. 暴露量随剂量增加超过比例的增长。一般用DNAUC（剂量归一化的AUC）去衡量。另外，峰浓度、达峰时间、半衰期这种指标也要注意。

**我们先来看** **暴露量随剂量增加不成比例的增长** **的原因（进入体内的少了和/或代谢的多了）：**

首先，涉及药物吸引的过程。口服给药后，暴露量随剂量增加不成比例的增长可能由药物吸收减少导致。大多数药物具有亲脂性，通过被动扩散吸收；因此，溶解度有限可能导致暴露量随剂量增加不成比例的增长，由于溶解度限制导致的不成比例增加是难溶小分子非常常见的原因，而在没有经过溶媒优化的情况下，溶解受限也是在所难免。

当然，吸收减少也可能由载体介导的肠道转运饱和引起。例如，加巴喷丁在高剂量下，由于负责从肠腔吸收的主动转运（L-型氨基酸转运体）饱和，暴露量随剂量增加不成比例的增长。我们都知道，申报阶段，往往需要做三个浓度条件下的caco\-2或者MDCK的渗透试验，需要评估一下药物的渗透是否与浓度相关，从而可以获得一些参考数据。

其次，涉及药物分布的过程。对于碳青霉烯类抗生素（MK-826），血浆蛋白结合饱和通过增加清除率，导致暴露量随剂量增加不成比例的增长，从而对其非线性PK特征产生贡献。当然，我们在非申报阶段做的PPB，往往是个别种属，且只有一个浓度，很难早期去预测药物是否存在浓度依赖的PPB饱和的情况。

除了上述两个过程之外，还有人会提出是否因为诱导自身代谢酶的表达，而导致清除率增加。这个就得看不同给药剂量下的酶诱导试验了。假如是单次给药，酶诱导大概不是其原因。

**我们再来看** **露量随剂量增加超过比例的增长** **的原因（排出的少了和/或代谢的少了和/或排泄的少了）：**

一般超比例增长不会是溶解和渗透的原因，更可能是涉及代谢和清除过程的代谢酶和转运体。

暴露量随剂量增加超过比例的增长最可能由清除率降低导致。苯妥英、水杨酸盐及茶碱是因饱和肝脏代谢导致清除率降低的经典药物范例。据报道，大鼠中胆汁排泄减少是导致非线性PK特征的另一原因。甲氨蝶呤主要经胆汁排泄，其胆汁排泄清除率降低会导致暴露量随剂量增加不成比例的增长，呈现非线性PK特征。胆汁排泄减少由胆小管膜上转运体饱和引起。利用Eisai高胆红素血症大鼠，证实这种转运体为多药耐药相关蛋白2（MRP2）。此外，表达于肠上皮细胞刷状缘膜上的P-糖蛋白（P-gp）可作为外排泵限制肠道吸收。他林洛尔是P-gp的良好底物，在健康受试者的治疗剂量范围内，因P-gp转运活性饱和，呈现非线性PK特征。

2\. **为何建议做桥接** **PK** **？**

首先，不管是PK试验还是毒理研究，非线性PK特征经常在临床前动物研究中被观察到。这种非线性使得剂量\-毒性及剂量\-效应关系的评估变得困难。这就是为什么，我总是建议大家在做毒理试验之前，做一下单次给药的桥接PK，顺便筛选好适合的溶媒。因为你不清楚哪个剂量范围内是暴露量线性的，突然升高剂量之后，就变成非线性甚至饱和了。

举个例子，假如你只做过大鼠的10mpk的口服PK试验，现在你要做100、200 mpk的预毒理，那你做不做100和200 mpk的桥接PK？可能许多人是不做的，到时候伴随TK结果一出来就傻眼了。暴露量不成比例的增加倒是还好，要是暴露量没有增加，高剂量组就相当于白做，到时候就要倒回来找是溶媒的问题还是其他别的原因，做无用功。而对于溶解度差且渗透性一般的PROTAC来说，溶媒异常重要，不筛选和优化溶媒直接上毒理的话，简直可能是灾难。

3\. **非线性** **PK** **有种属差异**

假如一个化合物在大鼠口服给药的PK中，剂量\-暴露量是线性的，但是小鼠或者犬上却是非线性的。如何解释？会不会出现不同动物上的药物剂量对ADME过程影响不同的现象呢？也是有可能的。

我们可能会遇见，同一个化合物，用同一种溶媒进行给药时，不同动物的口服F%可能会出现倍数的差别。药物在不同动物胃肠道的溶解度是否有区别？大致还是有区别的，动物的消化道pH、胆汁酸含量都不一样，为了避免动物胃肠道生理条件的种属差异，用澄清溶液给药可以避免很多麻烦。其次是渗透，渗透一般很少去研究不同动物的肠上皮渗透系数，所以也就通常默认渗透能力（Fa）是一样的。

比较麻烦的是代谢和转运体的种属差异。对于在某个种属代谢比较快的药物来讲，肠道和肝脏的首关代谢对生物利用度影响可能比较大，这个时候，高剂量条件下对代谢酶的饱和就可能显著影响F%。但是假如在别的种属中代谢比较慢，首关代谢贡献就比较小，或者存在代谢途径的种属差异，需要考虑底物代谢的Km，来判断是否在高剂量下，会存在代谢酶代谢速率下降的情况，过程还是相当繁琐的。

对于是外排转运体底物的药物而言，也是有可能因为外排转运体饱和导致出现剂量非线性PK的情况。假如人的转运体我们研究过了，发现化合物不是外排转运体的底物，我们是否需要对动物的转运体也进行研究呢？我认为在化合物筛选阶段做动物的转运体研究意义并不大。

总而言之，非线性PK的原因可能是多种机制共同作用的结果，没必要一定要追求完美的线性，而是找到一个线性范围。同时，对DDI进行全面的研究，为临床上的药物相互作用提供一个可靠的信息。

4\. **如何预测非线性** **PK**

当然了，比较高大尚的预测方法就是用PBPK模型，但是在早期筛选阶段或者pre-pcc阶段，也没啥人会收集如此全面的数据去建模。

有一篇日本株式会社制药的文章研究过这个问题，也提出了自己思路。他们发现，在38种CYP3A4和/或P-gp底物中，16种表现出非线性药代动力学，22种表现出线性药代动力学。说明CYP3A4和/或P-gp底物与非线性PK有非常强的相关性。

于是，他们为临床预测CYP3A4/P-gp底物的非线性药代动力学提供了简便工具：DIN=dose/Ki。还提供了决策树：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/qPA7ibWx6uicY5MymjGSQLMuTrTiaXLS3ictCGuNBPibQicg8MdYMzpHgOJoias9tmNzdWVjm4AF2cxybD3dZnxP2ib63A/640.png)

该决策树中，LIN3A4＜2.8L且LINP-gp＜0.77L的底物预测为线性药代动力学；即使LIN3A4≥2.8L或LINLINP-gp≥0.77L，若FaFg≥0.8，仍预测为线性药代动力学；若FaFg＜0.8且满足上述LIN标准（LIN3A4≥2.8L或LINP-gp≥0.77L），则预测为非线性药代动力学。该决策树对29种受试底物中的24种预测正确。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/qPA7ibWx6uicY5MymjGSQLMuTrTiaXLS3ictaswr8Rw1Wa9HwEhpRgibGDYHA75xGfGVzBic9Q7UEzKHqdGNQYjRjZxA/640.png)

这个研究主要还是考虑到首关代谢的影响。也给我们一个提示：当化合物是CYP3A4/P-gp底物时，当给药剂量达到一定时，有可能通过饱和代谢酶或转运体导致剂量\-暴露量超比例增加。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/qPA7ibWx6uicY5MymjGSQLMuTrTiaXLS3ict6BxJWL8RZVhlILHusHZjDywGmOZHnCsTaBhTpia1FnxZQNSB4tOwZBA/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/qPA7ibWx6uicY5MymjGSQLMuTrTiaXLS3ictwJuPXmLRa9pk6cMlD5AUa4l1StLqsmYwg9XoAgLicbTIkjLaleXjWbA/640.png)

**参考文献**

1\. Tachibana T, Kato M, Sugiyama Y. Prediction of nonlinear intestinal absorption of CYP3A4 and P-glycoprotein substrates from their in vitro Km values. Pharm Res. 2012 Mar;29(3):651-68\. doi: 10.1007/s11095-011-0579-2\. Epub 2011 Sep 13\. PMID: 21913031.

公众号合作CRO（火热招募中）：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/zAuuiaZa3aFVTDia9FicVfHIN8ibNQibibl67TR8tJPsibImzpLz2tqhpmiblyrxGnMlmyvb8wTOmhzT1RSHkOB6QgcdXQ/640.gif)

蛋白降解选择性

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/rzEUoibI3mHL7gZaOEzIHn1QSmzNwlDNC4tez2b1mdxWWV45xVmFImCmQy8R63VEIKy2t8Wz6So2EryxiaHISKjQ/640.gif)

惟妙生物

惟妙生物的蛋白组学平台在研究TPD药物（PROTAC、分子胶）在人和动物细胞上的蛋白降解谱上有丰富的经验。

了解平台详情，请点进下方图片进入超链接：

【深度技术解析】：定量蛋白质组学在降解剂中的应用】：

2025-11-13

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/zAuuiaZa3aFVTDia9FicVfHIN8ibNQibibl67TR8tJPsibImzpLz2tqhpmiblyrxGnMlmyvb8wTOmhzT1RSHkOB6QgcdXQ/640.gif)

CNS药效

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/rzEUoibI3mHL7gZaOEzIHn1QSmzNwlDNC4tez2b1mdxWWV45xVmFImCmQy8R63VEIKy2t8Wz6So2EryxiaHISKjQ/640.gif)

1\. 圣研生物

圣研（天津）生物科技有限公司具有多年神经类药物药效评估的经验，可提供模型鼠造模及繁育服务以及行为学研究、渐冻症、AD、PD、SMA动物药效学评价。

了解平台详情，请点进下方图片进入超链接：

如有测试需求，请联系高老师：15001299642

小鼠鞘内给药及滴鼻给药案例展示

2025-11-13

****注：公众号持续招募药物研发领域的合作方，例如类器官平台、体外药效、毒理等合作伙伴，有意者请添加下方微信，欢迎大家和我合作。**
  
  
### 加入读者交流群：

**请大家加微信入群（需备注姓名+擅长领域+单位）：**

![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/qPA7ibWx6uica9K2AxfuHqZkGkBwxgbDib6qJHjg98PO5hRzDj2xObzw5jS8I1IbthAnxMAZNOY6F8fkkdKQia5m3w/640.png)

公众号合作：产品宣传及软文插入，或者寻找项目（请有意者加我微信沟通：15210922780）
  
  
###   

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/qPA7ibWx6uicZZMlVhQc3fmOUvHndbQwzTibGRPdbwuRmw6ibuXHPmy5zIB7ML8so3VGKic2sVkNPBMhs2uIhhVcGdA/0.png) 

 药界物语 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/qPA7ibWx6uicZZMlVhQc3fmOUvHndbQwzTibGRPdbwuRmw6ibuXHPmy5zIB7ML8so3VGKic2sVkNPBMhs2uIhhVcGdA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
