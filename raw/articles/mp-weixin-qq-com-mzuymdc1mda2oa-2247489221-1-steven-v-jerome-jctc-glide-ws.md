---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489221&idx=1&sn=13b6fc3f2160c4b81c611c68f99eb546
canonical_url: https://mp.weixin.qq.com/s?__biz=MzUyMDc1MDA2OA%3D%3D&mid=2247489221&idx=1&sn=13b6fc3f2160c4b81c611c68f99eb546
source_domain: mp.weixin.qq.com
title: 【佳作推荐】薛定谔公司Steven V. Jerome等人JCTC论文：改进显式水分子建模与自由能标定驱动的分子对接打分函数Glide WS
author: 
published_at: 
fetched_at: 2026-04-25T02:04:03Z
extractor: wechat_worker
content_hash: e2aa9dce753184a16f7f606c5c837409a654a741cc2f01b0cdfd5f58b037b0ee
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EfbZPQYGHkdBpDr67Jl0MLjMhiciaI7UeV1zJEqxEO89K0ppL892MnFdJ2pYicG69FAD7RlYibYal7nwA/0.jpg) 

# 【佳作推荐】薛定谔公司Steven V. Jerome等人JCTC论文：改进显式水分子建模与自由能标定驱动的分子对接打分函数Glide WS

原创 ComputArt ComputArt [ ComputArt计算有乐趣 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EfbZPQYGHkdBpDr67Jl0MLjOwZI1B1Pd9bE3U0ahGCbCL1v8kibMAm1rV6BeiarxdrF5icUFZPzI4pCA/640.jpg)

基于分子对接的虚拟筛选是计算机辅助药物设计中的重要工具，其目标是在庞大的化学空间中高效识别潜在活性分子。然而，在实际应用中，假阳性率偏高始终是制约其命中效率的关键问题：大量计算得分靠前的化合物，在实验验证中并未表现出相应的结合活性，显著增加了后续实验筛选的成本。其重要原因之一，在于传统打分函数对结合口袋中水分子与去溶剂化效应的刻画仍较为粗糙。在空间受限的口袋环境中，水分子往往形成稳定而复杂的氢键网络，其置换或保留对配体结合自由能具有决定性影响，但这类细节很难通过隐式溶剂模型准确描述。

针对这一难题，薛定谔公司的 Steven V. Jerome 团队在其此前报道的分子对接程序与经验打分函数WScore中，系统性地将分子动力学模拟得到的结合口袋内水分子与氢键网络信息引入了对接与打分任务【1】。在此基础上，作者团队借助多年来内部虚拟筛选项目所积累的实验数据与实践经验，并借助绝对结合自由能微扰（absolute binding free energy perturbation，ABFEP）计算进行系统性标定，将WScore发展为经过规则优化和精细调试的物理打分函数Glide WS，且同步改进了其构象采样算法，用于复筛和重打分任务，最终在结合模式预测与降低虚拟筛选假阳性率方面均取得了显著提升。相关成果近日发表在美国化学会期刊 Journal of Chemical Theory and Computation 上【2】。

作为Glide WS的前身，WScore采用WaterMap方法，通过对移除原有配体后的结合口袋进行分子动力学模拟，定量刻画了水分子的空间分布、热力学和动力学特征，并将这些信息编码为一组水分子识别模体（molecular recognition motifs），直接参与对接构象的优化和打分。然而，随着WScore和后续Glide WS在内部虚拟筛选项目与迭代优化中的广泛应用，其在复杂体系中仍暴露出假阳性率偏高的问题，这一现象反映出水分子氢键网络、去溶剂化效应与张力能等能量项对局部结构与环境的高度敏感，也提示其规则和参数仍有进一步的优化空间。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EfbZPQYGHkdBpDr67Jl0MLjKZich2kLsz0MZ49Xp2Mo7UvC4rsRjiaRbrNkDfUFicbmFL2iaP6LovPAMw/640.jpg)

**图1：PDE5a复合物中的魔法甲基案例（PDB：1UDT）。**

Glide WS的打分函数可被写为：WScore = 𝑐 × 𝐸vds + 𝐸hydrophobic + 𝐸HB （氢键项）+ 𝐸MR （分子识别项）+ 𝐸strain （张力能项）+ 𝐸desolvation （去溶剂化项）+ 𝐸reorg。其中范德华项、疏水项及蛋白构象转变项基本沿用了WScore的定义和算法，主要改进集中在余下四组与溶剂环境密切相关的能量项中。作者进一步区分了不同类型氢键在溶剂暴露条件下的稳定性，引入更精细的惩罚与奖励规则；同时针对狭小疏水空腔中的高能水分子，补充了与“魔法甲基（magic methyl）”效应相关的识别规则，用以评估合理置换此类水分子所带来的潜在能量收益（图1）。对于带电基团与极性相互作用，Glide WS则结合溶剂暴露程度与偶极相互作用，对去溶剂化贡献进行了更具物理一致性的修正。

在关注局部结构和环境的能量项不断完善细化的同时，作者发展了WScore中基于MM-GBSA最小化的离域张力能（delocalized strain energy）校正，以评估配体整体与结合口袋的匹配程度。该校正以已知蛋白配体复合物为参考，通过关键参数GBSHIFT进行约束，避免配体为了获取局部奖励而整体形成不合理构象。另一方面，随着ABFEP方法的精度不断提高（RMSE = 1.1 kcal/mol），作者使用该方法为活性配体与虚拟筛选试验中所有排名靠前的阴性样本计算了其结合自由能，将其作为实验亲合性数据的可靠估计，从而为上述精细规则的参数标定和虚拟筛选性能评价提供了坚实的数据基础。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EfbZPQYGHkdBpDr67Jl0MLjpOGIVYLYvIanT1bJHibDlOnD7g4nu2rDQUg5An3lgrbLhUofdFH6VQg/640.jpg)

**图2：Glide WS计算CPU用时分布及其与可旋转键数、分子量的相关图。**

此外，为了在采样过程中更有机会穿越具有较高惩罚但必要的构象路径，以发挥精细化打分函数能量项的判别能力，作者提出了第二阶段的高分辨率采样策略。该方法采用基于树结构的生长式搜索算法，在可控的计算成本下系统遍历构象空间，保留那些能避免惩罚项的分支，从而更好得到最优的配体结合构象。在一项覆盖26个筛选任务、超过1.6万个配体的数据集对接测试上，Glide WS计算单个分子的平均CPU用时约为8.9分钟，与主流复筛和重打分方法在同一水平（图2）。

为了系统评估Glide WS在构象预测与虚拟筛选任务中的性能，作者分别在对接准确性基准数据集以及三个虚拟筛选测试集上进行了测试，并将结果与经典分子对接与打分程序Glide SP进行了对比。所有体系均使用 Schrödinger Suite 2025-2版本完成结构准备，包括蛋白与配体的标准化处理以及互变异构体的枚举与打分。对接准确性测试数据集由其内部数据集更新而来，包含了1477个收集自PDB数据库的蛋白配体复合物，其中的每个靶点都至少包含5个受体结构完全解析的复合物，并排除了晶体堆积或其他可能干扰对接的异常结构。在对接准确性测试中，以构象RMSD ≤ 2.5 Å作为成功判据，Glide WS的对接成功率由Glide SP的83.89 %提升至91.47 %，在预测准确性与稳健性方面均表现出显著改进。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/IBYsyRibb4EfbZPQYGHkdBpDr67Jl0MLjuN05QDFZ6ic52nsPISicial4Fyy2FNgia0y1s60yscPqibMMx0VIZxzAU4g/640.jpg)

**图3：以PubChem为阴性样本来源的15项虚拟筛选测试结果。**

在虚拟筛选性能评估中，作者共设计了53项测试任务。其中，23项测试的靶点和正负样本（活性配体经过聚类）来自DUD-E基准数据集，且大多数靶点未参与Glide WS的开发过程；其余30项测试沿用了WScore研究中使用的15个训练集体系，但阴性样本则分别从Enamine Real和PubChem两个来源获取，以和每个配体性质匹配的至少50个分子作为诱饵。为了贴合真实虚拟筛选项目的场景，作者并未对所有分子的整体排序进行分析，而是仅考察每项测试中排名前100的配体（不足时仅分析打分优于-8.0 kcal/mol的配体），并将其称为保留配体集（retained ligand set，RLS）。基于RLS，作者从命中率、阴性样本的平均ABFEP预测值、ABFEP预测为弱亲合性（阈值为-7.0 kcal/mol）的阴性样本数量，以及得分最高配体与首个ABFEP预测为弱亲合性的阴性样本之间的能量差四个维度，对筛选结果进行了综合评估。结果显示，在来自不同阴性样本来源的全部53项测试中，Glide WS在上述各项指标上均稳定优于Glide SP，不仅显著提升了筛选富集能力，同时有效降低了排名靠前分子的假阳性风险，并为潜在活性化合物保留了更宽的能量判别窗口（图3）。

**小编总结**  

该工作在 WScore 显式刻画水分子与氢键网络的基础上，进一步结合绝对自由能计算与丰富的案例，对打分规则与参数进行了系统性优化，使 Glide WS 在构象预测、筛选富集与假阳性控制等关键任务上均取得了稳健提升。借助更高精度的自由能计算得到的活性数据标签与更精细的物理建模规则，作者为经验打分函数的持续改进提供了一条更具物理一致性、也更贴近真实应用场景的发展路径。

**参考文献**

\[1\] Robert B. Murphy, Matthew P. Repasky, Jeremy R. Greenwood, Ivan Tubert-Brohman, Steven Jerome, Ramakrishna Annabhimoju, Nicholas A. Boyles, Christopher D. Schmitz, Robert Abel, Ramy Farid, and Richard A. Friesner\*, WScore: A Flexible and Accurate Treatment of Explicit Water Molecules in Ligand–Receptor Docking. Journal of Medicinal Chemistry, 2016, 59(9), 4364-4384\. https://doi.org/10.1021/ acs.jmedchem.6b00131.

\[2\] Richard A. Friesner, Robert B. Murphy, Yuqi Zhang, Yeyue Xiong, Pierre A. Devlaminck, Ivan Tubert-Brohman, and Steven V. Jerome\*, Glide WS: Methodology and Initial Assessment of Performance for Docking Accuracy and Virtual Screening. Journal of Chemical Theory and Computation, 2025, ASAP. https://doi.org/10.1021/acs.jctc.5c01316.

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IBYsyRibb4EcibThuywhbNciciaiauxu6DUhtp75nQZnrPxniaYia0RMN9XgXMVCiaqEOxkU4EjMoIsmD98kDTcLz5NC3w/0.png) 

 ComputArt计算有乐趣 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IBYsyRibb4EcibThuywhbNciciaiauxu6DUhtp75nQZnrPxniaYia0RMN9XgXMVCiaqEOxkU4EjMoIsmD98kDTcLz5NC3w/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
