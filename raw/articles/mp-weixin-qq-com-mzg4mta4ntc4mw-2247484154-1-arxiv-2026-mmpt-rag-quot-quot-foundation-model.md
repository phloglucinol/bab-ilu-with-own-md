---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247484154&idx=1&sn=78210f8078fdb5dae67e259adfa1d13c
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MTA4NTc4Mw%3D%3D&mid=2247484154&idx=1&sn=78210f8078fdb5dae67e259adfa1d13c
source_domain: mp.weixin.qq.com
title: arXiv 2026 | MMPT-RAG：把药化老手的&quot;改分子直觉&quot;装进Foundation Model，这次不是在画饼
author: 
published_at: 
fetched_at: 2026-04-25T02:03:27Z
extractor: wechat_worker
content_hash: 9716f893c97784c583a8f26cb38f2e54dba2099c75839d33b657270e557362a5
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/b4dmDNrOlLvNAUVu7l4YlNClxUwuIE5aooautGpZ7YfGb6vDeSTic4cU9iadI63uricCcTD2lSeGCI8ibhWW0MjfCaXHU6AKouubVibCk6AAZ9Ks/0.jpg) 

# arXiv 2026 | MMPT-RAG：把药化老手的"改分子直觉"装进Foundation Model，这次不是在画饼

原创 陷入鞍点 陷入鞍点 [ 陷入鞍点 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

Emory大学 × 默克联合出品。核心动作：把"怎么改分子"本身变成训练目标，再用RAG把项目经验注进去。

---

0\. 先说一个项目里真实发生的场景

你坐在虚拟筛选会议上，药化同事指着你生成的一批分子皱眉头："你这个吗啉换掉了，但我根本没叫你换。我就想改这个R基——而且你改成了什么？这个链子在这位置合成起来要死人的。"

这个场景的本质矛盾，和你用什么生成模型无关，而是和生成模型的目标函数有关。

绝大多数分子生成模型学的是"长什么样"——给我一个骨架，我补出整个分子；或者给我一个分子，我生成结构相似的另一个。这两种范式有一个共同的毛病：编辑是隐式的，是整体的，是难以指定位置的。药化同事脑子里想的不是"再给我来一个Tanimoto相似度0.7的分子"，而是"这个R基通常可以换成什么"。

这是两件完全不同的事。前者是在化学空间里漫游，后者是在执行一个有名字的药化动作。

这篇Emory+默克的工作，把这个"动作"本身——也就是Matched Molecular Pair Transformation（MMPT）——变成了生成模型的第一公民。

---

1. MMPT是什么，为什么它是更自然的生成单元

Matched Molecular Pair（MMP）是药化里非常古老的概念：两个分子，只有一处局部结构不同，其余部分完全相同。这个"一处不同"就是MMPT，形式化表示是 vA → vB。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/hXWWCalxKN4Q3VCia1oEKgUp9iaqaoB86zltBB9B46Zen7WaIohOabUtfDOYsvSPiab35ezFtm0JQGcmjVI1ic1SCNuOq7UMoMHzlYBmjQsRPicI/640?from=appmsg)

Figure 1：左边是两个MMP分子，突出骨架（constant）和变量部分（variable）；右边是抽象出来的MMPT表示 \[H\]\[\*:1\] >> C\[\*:1\]

作者的核心洞察是：一旦你把不变的骨架扔掉，你就得到了一个上下文无关（context-independent）的化学动作。这个动作是可以跨骨架迁移的——"把氢换成甲基"这个改法，在头孢骨架上和在激酶抑制剂骨架上，都叫同一个动作。

之前的方法，不管是全分子生成的Transformer系列，还是LibINVENT这类"固定骨架补变量"的路数，学的都是常量→变量的条件分布（给你骨架，补出R基）。这篇工作第一次直接学的是变量→变量的分布——给你一个R基，预测它通常可以被换成什么。

这不是一个incremental改进，这是一个问题重新定义。

---

2. 架构：怎么把MMPT学进去的

2.1 数据管线（这部分比较关键，细说一下）

原始数据来自ChEMBL，经过一套严格的过滤：

* rule\_of\_druglike\_soft（medchem包的类药性规则）
* 分子量 ≥ 200 Da（过滤掉太小的碎片）
* Walters警示结构列表（PAINS等）

过滤后剩下80万个化合物。用MMPDB跑MMP提取，max-variable-ratio=0.33（变量部分不超过分子的1/3，防止"改了一半"的伪MMP），得到263万个MMP对，折叠去重后约80万个独特的MMPT。90%训练，10%测试。

这个数据过滤的逻辑是对的：变量太大，你就不是在学局部改法，是在学骨架跃迁，两个任务不能混淆。

2.2 模型：ChemT5 + 变量翻译

backbone选的是ChemT5（220M参数，12层，12个attention head，基于T5架构）。这是一个在大规模化学任务上做过预训练的encoder-decoder模型，有化学语义的底子。

在它基础上做了标准的seq2seq微调：encoder吃vA的SMARTS序列，decoder生成vB的SMARTS序列。用了teacher forcing稳定训练，学习率5e-4，batch size 64，4张A6000 48G，跑了约70小时。推理时beam search生成1000个候选，最大序列长度50。

![](https://mmecoa.qpic.cn/mmecoa_png/hXWWCalxKN5GW2QMMU21o2L3wa5I9jslY0XG1fUia5bkOfF3EtLc3RMWS1KxH1uhic2H41zk9Sbcl8aP1KB6eDbhibr8auYxwoicWcFIOcRe81Y/640?from=appmsg)

 Figure 2(a)：基础模型训练框架示意图，左边是大规模MMPT语料，右边是ChemT5→MMPT-FM

这里有个选择值得聊一下：为什么用SMARTS而不是SMILES？因为变量部分本身就是子结构，SMARTS能更精确地表达attachment point（\[\*:1\]这类）以及子结构模式。SMILES是全分子级的表示，直接用来描述一个悬挂的R基很别扭。

2.3 受控生成：Masked Template + Rényi熵树搜索

用户想指定"我要保留这个环，其他位置你来补"怎么实现？作者设计了一个Masked Template Prompting机制：把用户指定的固定部分保留，其他位置换成\[MASK\]，然后让模型做span infilling。

![](https://mmecoa.qpic.cn/mmecoa_png/hXWWCalxKN4uPDFnCicJOPSOK8v4uth99yXp4JQcV4ibhmYeva486O5PoQJ6ezanAMoXzjicztq2myohFlyQJVEgea41ny3tYPep4ZibVQPicYt8/640?from=appmsg)

 Figure 2(b)：masked template prompting流程，左边是用户指定的desired pattern，中间是masked template，右边是MMPT-FM输出的候选

搜索空间控制是个工程难点。如果每个\[MASK\]位置都全量展开，候选爆炸。作者用了Rényi熵（二阶）来动态决定每个位置的有效分支数：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/b4dmDNrOlLuAm9q5xmg6hxe4wVzCqTD5IM1STWE0oA1WYzBUF5WeMmg6Bbu43x7NxJfO0zJIgDt5NnsiccaS0xDzgxP1ldPtL2DGgd4WHkII/640.png)

这个N\_eff是有物理意义的——它是当前token分布的"有效多样性"。分布尖锐（模型很确定）时N\_eff小，分支少；分布平坦（模型不确定）时N\_eff大，多探几条路。这比固定beam宽度聪明：把计算资源花在真正有分歧的位置。

2.4 MMPT-RAG：三步走把项目经验"注进去"

![](https://mmecoa.qpic.cn/sz_mmecoa_png/hXWWCalxKN5jXGOkiaJwgJpiawNImQHibtAIf5djRXbvsJL6TgeiaQ6IILiasHibRz7eMHZd4R9JmRCrsvWCtuF7CgTrfKwDPBgc2SaYnJIBNgl0A/640?from=appmsg)

 Figure 2(c)：MMPT-RAG完整流程，从Input vA → 检索 → 聚类 & MCS提取 → Template → MMPT-FM → Outputs

整个RAG流程三步：

Step 1 - 检索：用HNSW索引（Morgan指纹+余弦距离）对输入变量vA检索最相似的参考变量，取top-500，展开得到对应的输出变量集合VB，再用Tanimoto相似度对VB重排，保证检索到的是"真正相关"的改法。

Step 2 - 聚类：对VB做基于MCS的层次聚类（平均链接法，距离矩阵用MCS大小/小分子大小来计算，阈值0.70，超过10个分子的cluster递归拆分）。每个cluster代表一类"改法套路"。

Step 3 - 模板引导生成：每个cluster取MCS得到SMARTS模板，mask掉不变核以外的位置，送入MMPT-FM做span infilling。最终输出是所有cluster生成结果的并集。

---

3. 理论为什么work：一个优雅的Bayesian解释

作者给了一个定理（Theorem 4.1），说明RAG的本质是：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/hXWWCalxKN7ic2epTelUlKQFR8C8jOk6BatxXfhILeYbic2YdichddCjuwsyAFmwY4qA2qS7Gyp2CE0K8k5ib3sTldST5Z4icenQcdTOgQR2Qxv8/640?from=appmsg)

这是模型先验和参考集分布之间的凸插值。参数α衡量的是"模型有多服从模板的约束"——完全不遵守模板，α=0，退化成纯FM；完全遵守，α=1，退化成查表。实际情况在中间，用的是项目数据做"软引导"。

这个定理的价值不只是理论自洽，更重要的是给了一个使用直觉：RAG不是fine-tuning，不需要为每个项目重新训练，只需要在推理时换一个参考库。这对工业界部署意义重大。

---

4. 实验：三个任务层层递进，最后那个才是真考验

作者设计的三个任务放到一起，堪称教科书级别的评估设计：

Task 1（通用能力）：ChEMBL held-out，看模型有没有学到通用MMPT知识。

Task 2（项目内扩展）：PMV17专利数据集（PMV Pharmaceuticals，一家做突变型p53复活的公司），看模型能不能在真实项目场景里复现药化常用改法。

Task 3（跨专利时间预测）：用PMV17（2017年）训练+RAG，预测PMV21（2021年，同一家公司的后续专利）里出现的MMPT。这是最接近真实"让模型帮你预见未来4年的药化决策"的测试。

![](https://mmecoa.qpic.cn/mmecoa_png/hXWWCalxKN71w5S4FKbfLg75bw11Vgu5ExTibAfMvkWVHycGaOGE1u4jPcOxkCgJW85tH3HfoByeckZ0B9cDb7SkOLc0mLfon2p2TC3HxjCM/640?from=appmsg)

几个数字值得细看：

* Task 1里，数据库检索能做到43.5%的Recall，但Novel=0。这说明如果你的目标只是"找已知改法"，检索就够了；但你想要有创造性的新改法，检索永远给不了。
* Task 2里，REINVENT4（LibINVENT）的Recall只有5.1%，即便它用了骨架作为额外信息（这在某种意义上是"作弊"的额外条件），还是完败。这直接说明了variable-to-variable和constant-to-variable是两个本质不同的任务。
* Task 3的Recall-o（测试集中未出现在训练集的MMPT）：数据库检索0%（当然），REINVENT4 1.87%，MMPT-FM 11.48%，MMPT-RAG 12.99%。

12.99%听起来不高——但这是在预测4年后同一个项目团队会做什么化学决策，这个难度你得有点感觉。如果换一个PMV的药化团队成员做这个预测实验，他能达到多少？

![](https://mmecoa.qpic.cn/mmecoa_png/hXWWCalxKN4arKqggVCfPqL39n4KGfnDzOJGYibB0z9TKuibLUJtWhA9jc4icSWu7lDnSwDZagGYAcGZdYsJnTcwRntB1iaBQaHGcPOW4a8NqYU/640?from=appmsg)

Figure 3：PCA空间中MMPT-FM（蓝）vs Database Retrieval（红）的化学空间覆盖对比，ChEMBL和PMV17两个子图

![](https://mmecoa.qpic.cn/mmecoa_png/hXWWCalxKN42Mfk86ZgwocBHtw03ibO57ibfOYCmu5NL8T0zRewPyw43VUEugH6riaU0Yy4O5133g8Qvcb6gcfPhrMxFficSiaiax04lPGibDzSCSs/640?from=appmsg)

 Figure 4：UMAP可视化，灰色是PMV17参考集，蓝色是FM生成的分布，红色是RAG额外覆盖的区域

Figure 4是整篇论文最直观的一张图。灰色是"项目领地"，蓝色FM生成的点大量堆在中心高概率区，但很多项目相关的小簇没覆盖到。红色的RAG点，把那些角落的"稀有但相关"的区域都填上了——这才是RAG的真正价值：不是平均意义上更好，而是把盲区补上了。

![](https://mmecoa.qpic.cn/mmecoa_png/hXWWCalxKN4cjLHhyDU21wGxVmblJApxaXia1VLSiciaaMzwAsfDheGYevvCgpJzjXZdEXY5giamRfEoyTsRLDOH22VdEzZHOZqgfV8Y0GJr6Ws/640?from=appmsg)

---

5. 批判性点评：哪里真有料，哪里要小心

真正有价值的地方：

问题定义是这篇论文最核心的贡献。variable-to-variable的MMPT formulation，在方法论层面不依赖骨架信息——这意味着训练出来的转化模式在不同骨架间是可迁移的，这是传统partial generation方法做不到的。

ChemT5的初始化选择也合理：220M参数规模够用，SMARTS词表覆盖好，不用从头学化学语法。

时间分割的专利测试设计很实诚，比那种"在benchmark上测benchmark"的工作更可信。

RAG的理论分析不是装饰——Theorem 4.1给了"调控项目导向程度"一个可量化的把手，工程上有实际意义。

需要想清楚再用的地方：

* MMP定义的单点约束是双刃剑。MMPDB的"单点差异"定义保证了变量的化学意义纯粹，但真实项目里药化同事有时候是要同时改两个点的。这套框架目前只能拆成两步串行，能不能做组合MMPT，作者在conclusion里提了但没实现。
* SMARTS不表达三维，不表达手性。对手性敏感的靶点系列（激酶、GPCR等），这个缺失可能很要命。一个（S）构型活，（R）构型没活性，SMARTS level的MMPT是完全区分不了的。
* 训练数据的来源偏差。ChEMBL里的化合物有其历史分布偏好，80万条MMPT覆盖的化学空间不是均匀的。对于PPI抑制剂、大环肽、共价药物这些"非典型"药化改法，FM的先验可能很弱，RAG能不能完全补救要打问号。

工业界落地一句话：先导化合物优化阶段的取代基扫描，这个工具非常合适。特别是你手头有一批已有类似物专利/内部数据，用RAG能显著把生成结果拉向"项目相关区域"。但骨架跃迁、初筛千万级文库、或者对三维活性构象敏感的系列，先别指望它。

---

6. 往大了想：这件事的意义不只是生成分子

这篇工作给我的最大触动，不是它的模型有多厉害，而是它在隐式地推销一种对药化知识的新型编码方式。

传统的CADD把药化经验编码成规则（Ro5、PAINS），把SAR编码成统计模型（CoMFA、QSAR）。DeepLearning时代我们把它编码成从分子到活性的端到端映射。这篇工作则是把药化经验编码成一套可检索、可迁移的"改法库"——不是规则，不是映射，而是动作本身。

这种编码方式有一个很好的性质：它和靶点无关，和适应症无关。同一套"改法先验"，在GLP-1R项目里用，换到KRAS项目里也能用，因为"把吡啶换成嘧啶看选择性"这件事本身是化学层面的，不是靶点层面的。

这意味着什么？一家公司积累了几十年的medicinal chemistry intuition，有没有可能系统性地"数字化"进这样一个Foundation Model？

如果能，这才是真正的壁垒。不是模型大小，不是算法，而是你积累的、外人没有的改分子历史。

---

7. Q&A

Q：“这玩意儿连我分子的母核都不看，凭什么说它懂化学？有些基团换上去，母核的偶极矩都变了！”

说到点子上了。这确实是该方法在物理层面上的妥协。但它的逻辑是：它提供的是一个基于大数据的“优质替换候选池”。它只保证这个替换在化学界是“高频、合理”的。至于和您具体母核的兼容性，它把决定权留给了下游的 3D 物理验证工具和您的直觉。它是个尽职的脑暴助手，不是最终的决策者。

Q：“直接用基于规则的生物电子等排体（Bioisostere）数据库不就行了吗？搞这么复杂的大模型有必要吗？”

传统的死规则有几个致命弱点：一是太僵硬，没法处理长尾的复杂替换；二是没法像 RAG 这样，根据你当前项目的参考集去动态调整生成分布（权重偏移）；三是本文的模型能够优雅地处理带多个连接点的复杂片段（Multi-attachment），这是普通规则库很难做到的。

Q：“那个 Mask 填空机制具体是怎么影响生成的？”

打个比方，常规生成是让你随便写一个“表示开心的词”。而 Mask 填空机制是，通过检索你的日记，发现你喜欢用四个字的成语，然后提取了一个模板 \[欣\]\[MASK\]\[若\]\[狂\]，强制模型在这个框架里生成，比如填出 欣喜若狂。这就保证了生成的分子在结构上带有你特定项目的“基因”。

Q：Task 3的Recall-o只有12.99%，这不是很低吗？说明模型其实没学到什么有用的东西？

这个问题好，但要先搞清楚这个任务的难度。Task 3本质上是"用2017年的数据，预测2021年的药化团队会做什么"。基准是0%（检索），REINVENT4是1.87%。12.99%是在这个极难的任务上的12.99%，不是在一个简单任务上的12.99%。另外，Recall-i在81.35%，说明模型对"已知套路的延续"预测得很好，真正的gap是"完全新颖的改法"，这部分本来就是AI最难突破的边界。

Q：RAG需要有参考数据库，但如果是first-in-class靶点，根本没有项目参考数据呢？

这正是MMPT-FM的价值。RAG是锦上添花，没有参考库的时候退化成pure FM推理——80万条ChEMBL MMPT打底，基础覆盖不差。而且PMV这个例子里，Task 1的FM itself就有67.6% recall，所以"没有项目经验时用通用FM"是个合理降级方案。

Q：和LLM直接做SMILES编辑相比，这套东西有什么优势？

LLM做SMILES编辑的问题是：1）不保证生成的是化学合法的结构；2）不能保证"只改了一个地方"；3）不能学MMPT级别的transformation prior。这篇工作的MMPT-FM在99%+的validity、单点修改保证这两件事上是有工程保障的，不靠prompt靠训练目标的约束。LLM是"能做但不稳"，MMPT-FM是"做这件特定的事非常稳"。

Q：用SMARTS做变量表示，药化同事能看懂输出结果吗？

SMARTS给算法用，不给人看。前端展示层要把SMARTS渲染成2D结构式，这是标准的cheminformatics工程问题，RDKit直接支持，没有技术障碍。真正的挑战是：生成了1000个候选，药化同事怎么筛？这篇工作在"下游怎么用"上着墨不多，需要结合打分函数（活性预测、ADMET）做级联过滤。

---

* 文章标题：Retrieval-Augmented Foundation Models for Matched Molecular Pair Transformations to Recapitulate Medicinal Chemistry Intuition

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7zibiaVPt4xq6YOATjn0icWC4ddwoYnGvBTcJRErwMnMUOEcyS3QnGFMDwQr9DZlWibmFGdvDKY0ao0A/0.png) 

 陷入鞍点 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/pUZwvicbdez7zibiaVPt4xq6YOATjn0icWC4ddwoYnGvBTcJRErwMnMUOEcyS3QnGFMDwQr9DZlWibmFGdvDKY0ao0A/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
