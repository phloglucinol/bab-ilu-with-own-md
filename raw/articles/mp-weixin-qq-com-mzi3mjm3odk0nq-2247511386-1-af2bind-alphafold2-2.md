---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzI3MjM3ODk0NQ%3D%3D&mid=2247511386&idx=1&sn=f934af0512b34c29b492f160b3de2d3f
canonical_url: https://mp.weixin.qq.com/s?__biz=MzI3MjM3ODk0NQ%3D%3D&mid=2247511386&idx=1&sn=f934af0512b34c29b492f160b3de2d3f
source_domain: mp.weixin.qq.com
title: AF2BIND问世：用AlphaFold2的「内部语言」预测超2万个小分子结合位点，加速药物发现
author: 
published_at: 
fetched_at: 2026-04-25T02:03:23Z
extractor: wechat_worker
content_hash: 87d38a8cf9467eaa3e41bfb21f27a5600548aab45eb23ee19f82505a889e4519
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/5hq6GFHibJv7Exm8dfnMwCj3nWPTkic2DZbGOONfsiaiafTrWKPsYxTJXJB9Wo5XMll2h3Sia4nIOIEIg3u1tIKB3d8o6JM18F27KjHLAShdlDcc/0.jpg) 

# AF2BIND问世：用AlphaFold2的「内部语言」预测超2万个小分子结合位点，加速药物发现

ScienceAI ScienceAI [ ScienceAI ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

---

将 **ScienceAI** 设为**星标**

第一时间掌握

新鲜的 AI for Science 资讯

****![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/cbQsE5QH8RqlDSgibPlwuRlZ2tBFFcVcOGBEtNYpKmkbSLK9YYKWZMpxriaX1OnEzPghic8FIffyxbJgMbxQRHTwA/640.gif "动态黑色音符")**

---

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/5hq6GFHibJv6lkqskOLKB4JG7XBTxeaxLQWz9tDMQJZtTWs2QvUOnoBFRvlcHsZbKvsNcauB4hLHomAbPKNMVTSnRkicaddicRch3LTAdCvmIQ/640.png)

编辑丨&

在药物研发的漫长链条中，找到蛋白质上能与小分子药物结合的口袋（结合位点），是关键的起点。传统方法要么依赖已知结构的同源比对，要么从头训练神经网络。但前者受限于已知数据，后者则常因训练数据不足而泛化能力有限。

而现在，哈佛医学院、MIT 与达纳-法伯癌症研究所等提供了一个全新的思路：与其从头训练，不如从 AlphaFold2 这个已经「学富五车」的蛋白质结构预测模型中，直接提取它学会的关于蛋白质相互作用的「内部语言」。

这个名为 AF2BIND 的工具，仅用一个简单的逻辑回归模型，就实现了对小分子结合位点的高精度预测，并构建了一个包含上万个人类蛋白质组中全新结合位点的数据库，为药物发现提供了宝贵的资源。

相关研究以「_AF2BIND: predicting small-molecule binding sites using the pair representation of AlphaFold2_」为题，于 2026 年 3 月 11 日发布在《_Nature Methods_》。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/5hq6GFHibJv5IdBAF8MXg5UKa0n5NEob3iaLr5IYWnjPbcbrXIUsz2Ap8uL4712oEN7SITa6u6ib0DPSWv1ibORIe3AnIU1NQPy11hn4Z6K9xyI/640.png)

论文链接：_https://www.nature.com/articles/s41592-026-03011-2_

**AF2BIND**

AlphaFold2（AF2）本是为了预测蛋白质的单链结构而训练的。但研究团队敏锐地意识到，AF2 在训练过程中，「见过」成千上万个包含小分子的蛋白质复合物结构。这些知识，很可能已经内化在其网络内部的对表示（pair representation）中。问题就在于，如何「唤醒」这部分沉睡的知识？

AF2BIND 的巧妙之处在于：**它给 AF2 输入目标蛋白的结构（作为模板），同时在其序列末尾，像「钓鱼」一样接上20个「诱饵氨基酸」——每个标准氨基酸类型各一个，且彼此之间用很大的残基索引间隔隔开。**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/5hq6GFHibJv7hXoE6z8GiaZO2FcmSrsr3eSdLV8vvtEsyIvc4D73Co4sTktTPIpZXLppfnzr3DmZrBtcqq4OrUniacmBjQbXtz90xYyVKiaFo8E/640.png)

图 1：AF2BIND 利用 AlphaFold2 的特征预测靶蛋白中的小分子结合残基。

AF2 会尝试「完成折叠」，在这个过程中，诱饵氨基酸会与目标蛋白的潜在结合位点产生注意力交互。而 AF2BIND，则截取目标蛋白每个残基与这 20 个诱饵氨基酸之间的初始注意力，并将对表示拼接后，输入一个逻辑回归模型进行训练，目标是预测该残基是否是小分子结合位点。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/5hq6GFHibJv543eia8fLuib0Q5Trs3STqDricN5qj06nv5VtU6iaiafV1SLKiakxTjibylS988FE7MpapwZib11O5sn7OX7icx0hSusIg89db9Mk2QrzE/640.png)

图 2：AlphaFold2 的对表示被用作逻辑回归模型 AF2BIND 的输入，用于预测配体结合残基。

这种方法优雅地避开了从头训练深度网络所需的海量标注数据，直接利用了 AF2 强大的预训练知识。同时，逻辑回归模型的选择，也为后续的可解释性埋下了伏笔。

**训练与成果**

为了避免数据泄漏（即测试集与训练集存在同源蛋白），团队建立了一个极为严苛的拆分标准。们不仅按序列相似性（30% identity）聚类，还结合了结构相似性（Foldseek）、进化分类（ECOD）、结构域注释（CATH, PFAM）乃至结合口袋本身的形状相似性（TM-score）。

最终的测试集包括 67 个不同小分子结合蛋白的结构，这些结构与训练集或验证集中的任何蛋白质在结构、序列或口袋上均无相似性。

结果显示，仅用 AF2 的 pair 特征，AF2BIND 就达到了 66% 的结合残基恢复率，ROC-AUC 为 0.936。将多种特征结合，性能略有提升，但 AF2 无疑是信息最丰富的单一来源。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/5hq6GFHibJv48SO5J1dXW0rxbaTS95UD53OyRqUtrp2qXyGpQFUL9YOdDWQu3Z8sqkUujw86mknI8Gaz3NPMjc46nicJHbN3XhZ1E55CjTNdo/640.png)

图 3：AF2 的配对表示在结合-残基预测方面最为有效。

验证算法性能后，研究团队将 AF2BIND 应用于一个更宏大的目标：整个人体蛋白组。他们利用 AlphaFold2 已预测的结构数据库，对所有蛋白进行系统分析。

结果显示：共有 20,302 个潜在结合位点，分布于 13,686 个蛋白质中。更重要的是，其中 15,755 个位点 在已有数据库中完全没有对应记录。换句话说，这些位点是此前几乎无法通过同源结构转移或传统方法识别的。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/5hq6GFHibJv7w9AnicagdGJ1VLLRAIK12ic1ZQD5dJtfV2gudDzE1xYlGstWcU5SmuGCOATgwGibbiavRRbceicAWrKj2KJ7JlALriaia0QDQb6EzCU/640.png)

图 4：AF2BIND 预测了人类蛋白质组中未通过同源建模（AlphaFill）或 P2Rank 发现的可药物位点。

**高质量的药物地图**

AF2BIND 证明了预训练模型的「知识迁移」能力：一个为结构预测而训练的模型，其内部表示竟能如此有效地迁移到预测蛋白质-小分子相互作用这一看似正交的任务上。这为未来利用这些强大模型解决更广泛的生物医药问题（如配体设计、蛋白质设计）提供了范例。

AF2BIND 不仅指出位点在哪里，还通过诱饵分析，提供了关于「什么样的分子可能适合这里」的线索。

如论文作者所言，AF2BIND 的预测可以与能处理小分子的新一代结构预测工具（如AlphaFold3、Boltz-1）协同，其识别的位点可以作为「口袋条件」，引导这些工具进行更精准的共结构预测或分子对接。  

**人工智能** **×** **\[ 生物 神经科学 数学 物理 化学 材料 \]**

**「ScienceAI」关注人工智能与其他前沿技术及基础科学的交叉研究与融合发展** **。**

**欢迎** **关** **注标星** **，并点击右下角** **点赞** **和** **在看** **。**

**点击** **阅** **读原文** **，加入专业从业者社区，以获得更多交流合作机会及服务。**

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/XLCp9HBkwLls7SBSrPNH0iafx9YKFxoSewNSqfpuK04lO3ibfdQfaQk6QgSQnPvY9rvuy4bLwYu8frx4b9CRU3cQ/0.png) 

 ScienceAI 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/XLCp9HBkwLls7SBSrPNH0iafx9YKFxoSewNSqfpuK04lO3ibfdQfaQk6QgSQnPvY9rvuy4bLwYu8frx4b9CRU3cQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
