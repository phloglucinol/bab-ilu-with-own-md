---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg3OTc1NDUxOQ%3D%3D&mid=2247484629&idx=1&sn=cba52acbd5884e184593ed6c61385e51
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg3OTc1NDUxOQ%3D%3D&mid=2247484629&idx=1&sn=cba52acbd5884e184593ed6c61385e51
source_domain: mp.weixin.qq.com
title: Cell Reports Method || 药物-靶标互作预测技术进展
author: 
published_at: 
fetched_at: 2026-04-25T02:04:27Z
extractor: wechat_worker
content_hash: 452fd781f34b67d795a1c5375b7a8e82ef516f9ce1b5c762775dc0aede4dc7dc
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/R3Et7ja80KGicw842UfGdqwibqibps68GtpsV8nkSdBf0SUtyyxpv3ok5Qn8ftbrZGCqumeSmlVmmbHJOvuickEliaA/0.jpg) 

# Cell Reports Method || 药物-靶标互作预测技术进展

原创 景磊 博士 景磊 博士 [ BioPrime ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/R3Et7ja80KGicw842UfGdqwibqibps68GtpNtTlD7aHD6IuDlftRLfB6Zgic8FuspI79npnGfC2PaPP8pnG7A3ryfA/640.png)

药物\-靶标相互作用（DTI）预测是药物发现过程中的关键环节，对开发新药、提高疾病治疗效果具有重要意义。传统药物开发面临高成本、低成功率和长周期等挑战，而In silico方法（计算模拟方法）通过高效利用现有数据，降低了开发成本，加速了药物发现进程。近年来，人工智能（AI）、基因编辑和高通量筛选等技术的突破，显著推动了药物开发的速度。In silico Medicine在短时间内设计出新型药物分子并进入临床试验阶段。

**早期** **的** **计算方法**

**分子对接**：通过模拟药物分子与靶标蛋白的三维结构，预测其结合模式和亲和力。然而，该方法高度依赖蛋白三维结构的可用性，且对同源建模的准确性要求较高。

**基于配体的虚拟筛选**：如定量构效关系（QSAR）和药效团模型，通过已知活性数据预测新药物分子的活性。这些方法假设化学结构与生物活性之间存在线性关系，难以捕捉复杂的非线性相互作用。

**机器学习方法的兴起**

**机器学习模型**：Yamanishi等人首次构建了整合化学和基因组信息的双层模型，用于DTI预测。随后，多种机器学习算法被应用于DTI预测，包括KronRLS、SimBoost等，这些方法通过不同的特征提取和模型构建策略，提高了预测准确性。

**深度学习突破**：深度学习技术，特别是图神经网络（GNN）和注意力机制的应用，进一步提升了DTI预测的性能。例如，DGraphDTA通过构建蛋白图并利用图卷积网络提取特征，MT-DTI模型则首次应用注意力机制改进药物。

| **工具**                                | **药物表征**                              | **蛋白表征**                                                          | **工具的描述**                                                                                                |
| ------------------------------------- | ------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| AGraphDTA                             | 基于图神经网络（GNN）的药物分子图特征                  | 基于卷积神经网络（CNN）的氨基酸序列特征；基于图卷积网络的蛋白质接触图特征                            | 通过神经网络提取的蛋白质图特征和氨基酸序列特征具有相同的维度，通过逐元素矩阵加法进行融合，从而提供了对蛋白质复杂信息的更全面的表征                                        |
| BINDTI                                | 基于图神经网络（GNN）的药物分子图特征                  | 基于自注意力机制和卷积的氨基酸序列特征                                               | 药物的特征和目标通过双向意图网络融合，该网络结合了意图机制和多头注意力机制                                                                    |
| BindingSiteDTI                        | 基于GNN 的药物分子固定尺度亚结构特征                  | 基于GNN的蛋白质图谱多尺度子结构特征                                               | 明确提取目标的多尺度子结构和药物的固定尺度子结构，以促进结构相似的子结构标记的识别，并在子结构层面建立隐藏关系，以构建交互特征                                          |
| BiComp-DTA                            | 基于可分离卷积层从药物序列中提取特征                    | 使用全连接神经网络从编码蛋白质序列中提取特征                                            | 从蛋白质序列中提取信息特征，提出了一种统一的度量BiComp，该度量基于无对齐（即Lempel-Ziv-Markov链算法\[LZMA\]）和基于对齐（即Smith-Waterman）相似性度量。       |
| CPInformer                            | 功能类指纹（FCFP）与结构GCN特征融合，作为化合物的最终表示。     | 从不同网络层提取的具有不同感受野的多尺度蛋白质特征                                         | 在化合物特征的指导下，ProbSparse自注意力被应用于蛋白质特征，以消除信息冗余并提高CPInformer的准确性。                                             |
| CPGL                                  | 基于图注意力网络（GAT）表示药物分子信息                 | 基于长短期记忆神经网络（LSTM）表示蛋白质信息                                          | LSTM能够学习序列中相隔较远的单词之间的关系。这种独特的LSTM使用方式可以更好地提取蛋白质结构的空间特征。                                                  |
| DeepDTA                               | 基于卷积神经网络从药物SMILES序列中学习表征              | 基于卷积神经网络从原始蛋白质序列中学习表征                                             | 首个基于深度学习的DTA预测模型                                                                                         |
| DeepConv-DTI                          | 基于全连接层提取药物指纹信息                        | 基于卷积神经网络提取目标蛋白质序列的局部残基模式                                          | 使用卷积神经网络捕捉局部残基模式的方法成功丰富了原始序列中的蛋白质特征                                                                      |
| DataDTA                               | 基于代数图的复合结构信息指纹特征化，基于卷积神经网络提取SMILE序列特征 | 蛋白质结合位点描述符，基于CNN提取蛋白质序列特征                                         | 开发了一种双重交互聚合神经网络策略，以确保有效学习多尺度交互特征。                                                                        |
| DeepGLSTM                             | 引入了一个图卷积网络（GCN）模块，利用功率图表示来处理药物化合物     | 使用双向长短期记忆层处理蛋白质序列                                                 | 基于GCN和LSTM的方法，能够预测FDA批准的药物与SARS-CoV-2病毒蛋白之间的结合亲和力值                                                       |
| DrugVQA                               | 基于多头自注意力双向长短期记忆网络提取SMILES特征           | 基于动态CNN 蛋白质距离图的特征提取                                               | 受视觉问答（VQA）范式启发的可解释模型，能够根据蛋白质距离图和分子SMILES直接预测DPI。                                                         |
| DeepAffinity                          | 基于双向递归神经网络（RNN）提取SMILES序列特征           | 用结构和物理化学性质的新字母表示蛋白质序列，然后基于双向RNN提取特征                               | 在有限标记数据的新蛋白质类别上的表现可以通过迁移学习进一步提高。此外，我们开发了独立的和联合的注意机制，并将其嵌入到我们的模型中，以增强其可解释性。                               |
| DGraphDTA                             | 基于图神经网络提取药物分子图特征                      | 基于图神经网络提取蛋白质接触图特征                                                 | 所提出的方法是基于蛋白质接触图构建蛋白质图的首次尝试                                                                               |
| DeepCDA                               | 基于卷积神经网络编码药物SMILEs                    | 基于LSTM对蛋白质序列进行编码                                                  | 对抗域适应方法用于学习测试域的特征编码网络，以处理训练域和测试域之间不同的分布。                                                                 |
| DeepEmbedding-DTI                     | 使用带注意力机制的图神经网络提取药物分子图特征               | 双向编码器表示的Transformer（BERT）模型从由这些蛋白质词语组成的文本中学习嵌入向量。                 | 为了提高训练效率，引入了一种来自Transformer的双向编码器表示预训练方法，以从蛋白质序列中提取子结构特征，同时引入了局部广度优先搜索以从分子图中学习子图信息。                      |
| FusionDTA                             | BiLSTM被用作药物SMILES的特征编码器               | BiLSTM被用作蛋白质序列的特征编码器                                              | 为了应对隐式信息的损失，采用了一种新颖的多头线性注意力机制来取代粗糙的池化方法。FusionDTA能够基于注意力权重聚合全局信息，而不是像最大池化那样选择最大信息。                       |
| GraphCPI                              | 使用图神经网络学习化合物的图表示                      | 使用卷积神经网络（CNN）构建块来学习蛋白质序列的低维向量表示                                   | 提出了一种框架，该框架结合了化合物的先进图神经表示与用于蛋白质序列的预训练嵌入技术。据我们所知，这项研究是首个将局部化学环境和拓扑结构结合起来，以学习化合物\-蛋白质对之间的相互作用的研究。          |
| GraphDTA                              | 基于GCNGATGINGAT-GCN的药物分子图表示学习          | 基于卷积神经网络的蛋白质序列学习                                                  | 第一项使用图神经网络进行药物\-靶点相互作用预测的研究                                                                              |
| HyperAttentionDTI                     | 使用卷积神经网络学习药物的特征矩阵                     | 使用卷积神经网络学习蛋白质的特征矩阵                                                | 与之前的基于注意力的模型不同，我们的模型为每个氨基酸\-原子对推断出一个注意力向量。这些注意力向量不仅捕捉氨基酸和原子之间的相互作用，还控制跨通道的特征表示。                          |
| IIFDTI                                | GAT用于提取药物的独立特征，可以捕捉原子之间的拓扑信息。         | 使用不同核规模的卷积结构来提取蛋白质的独立特征                                           | 融合药物和靶点之间的相互作用和独立特征，以预测药物靶点相互作用(DTI)                                                                     |
| MIDTI                                 | GCN被用作编码器，从集成的药物相似性网络中学习药物嵌入。         | GCN还被用作编码器，从集成目标相似性网络中学习目标嵌入。                                     | 提出了一种新颖的多视角相似性网络融合策略，该策略利用多视角注意力机制以无监督方式整合不同的相似性网络，只要这些网络的节点和尺寸是一致的。                                     |
| MGraphDTA                             | 基于多尺度图神经网络提取药物特征                      | 多尺度卷积神经网络提取目标特征                                                   | 提出了一种多尺度图神经网络和一种名为梯度加权亲和激活映射的新颖视觉解释方法，用于DTA预测和解释。                                                        |
| MCANet                                | 基于CNN从药物序列中学习低维表示特征                   | 基于CNN从蛋白质序列中学习低维表示特征                                              | 使用交叉注意力机制提取药物与蛋白质之间的交互特征，从而增强药物和蛋白质的特征表示能力。此外，还采用了PolyLoss函数来缓解药物靶点数据集中出现的过拟合和类别不平衡问题。                   |
| MATT-DTI                              | 基于卷积神经网络提取序列特征                        | 基于卷积神经网络提取序列特征                                                    | 提出了一种关系感知自注意力模块，用于从SMILES 数据中建模药物，同时考虑原子之间的相关性。相对自注意力模块增强了化合物中原子之间的相对位置信息，同时考虑所有元素之间的关系。                 |
| MMDG-DTI                              | 应用图卷积网络来提取原子之间的关系                     | 蛋白质的局部特征由3D卷积神经网络表示，以表示结合位点的空间特征。蛋白质的全局特征由一维卷积神经网络表示，以表示氨基酸序列的特征。 | 我们提出了一种多尺度卷积网络，利用不同类型的卷积网络来提取蛋白质的局部和全局特征以及化合物的拓扑特征。                                                      |
| MFR-DTA                               | 基于BioMLP处理FCFP信息，并基于GNN提取分子结构特征       | 基于BioCNN处理序列、氨基酸嵌入和词嵌入信息                                          | BioMLP/CNN是第一个旨在提取生物序列元素个体特征的模块，同时从序列中提取元素的个体特征和关系特征。                                                    |
| Masashi Tsubaki ’send-to-end approach | 使用图神经网络提取复合子图特征                       | 使用卷积神经网络提取序列特征                                                    | 使用神经注意机制缓解了深度学习黑箱特性中可解释性差的问题，使我们能够识别在预测药物化合物相互作用时蛋白质中哪些子序列更为重要。                                          |
| TC-DTA                                | 基于卷积神经网络提取序列特征                        | 使用Transformer的编码器模块提取氨基酸序列特征                                      | 本研究的结果表明，Transformer 编码器和卷积神经网络在从序列中提取有意义的表示方面是有效的。                                                      |
| TEFDTA                                | 基于MACCS指纹和转换器中的编码器提取分子特征              | 基于卷积神经网络提取蛋白质序列特征                                                 | 大多数方法主要是为预测非共价结合亲和力而开发的，目前还没有专门用于预测共价结合亲和力的深度学习方法。在本文中，我们提出了一种新的模型，用于预测药物与蛋白质相互作用中的共价（结合）和非共价（非结合）结合亲和力。 |
| TransformerCPI                        | 基于图卷积网络解决分子表示问题                       | 蛋白质的 word2vec 是基于其序列获得的，然后将蛋白质的序列特征向量传递给编码器，以学习更抽象的蛋白质表示。         | 学习所需的交互特征并降低隐藏配体偏差的风险。通过将注意力权重映射到蛋白质序列和化合物原子上，我们可以探索模型的可解释性，这有助于我们判断预测是否可靠和在物理上有意义。                      |
| TransformerCPI2.0                     | 基于图卷积网络提取化合物分子图特征                     | 使用预训练的蛋白质语言模型TAPE-BERT 计算蛋白质序列表示                                  | 证明了序列到药物模型可以达到接近基于结构的方法的虚拟筛选性能（无需依赖任何蛋白质三维结构的先验知识），并且验证了将这一概念应用于药物发现的可行性。                                |

表1 DTI和DTA（药物-靶标亲和力）预测主要工具汇总 （引自\[1\]）

| **分子**            | **工具**                                                                      | **链接**                 |
| ----------------- | --------------------------------------------------------------------------- | ---------------------- |
| 蛋白                | BioPython                                                                   | https://biopython.org/ |
| PyMOL             | https://pymol.org/                                                          |                        |
| DSSP              | https://swift.cmbi.umcn.nl/gv/dssp/                                         |                        |
| iFeature          | https://github.com/Superzchen/iFeature                                      |                        |
| Pfeature          | https://github.com/raghavagps/Pfeature                                      |                        |
| ProtDCal          | http://bioinf.sce.carleton.ca/ProtDCal/                                     |                        |
| ModlAMP           | https://modlamp.org/                                                        |                        |
| ProtParam         | https://web.expasy.org/protparam/                                           |                        |
| 药物                | RDKit                                                                       | http://rdkit.org/      |
| Open Babel        | http://openbabel.org/wiki/Main\_Page                                        |                        |
| OpenChem          | https://mariewelt.github.io/OpenChem/html/index.html                        |                        |
| ChemPy            | https://chempy.readthedocs.io/en/latest/                                    |                        |
| ChemAxon Marvin   | https://chemaxon.com/marvin                                                 |                        |
| PaDEL\-Descriptor | https://github.com/ecrl/padelpyhttp://www.yapcwsoft.com/dd/padeldescriptor/ |                        |
| ChemAxon JChem    | https://chemaxon.com/jchem-engines                                          |                        |
| Pybel             | https://pypi.org/project/pybel/                                             |                        |
| ChemDes           | https://github.com/ifyoungnet/ChemDes                                       |                        |
| CDK               | https://cdk.github.io/                                                      |                        |
| DeepChem          | https://deepchem.io/                                                        |                        |

表2 用于蛋白质和化合物特征提取的工具包 （引自\[1\]）

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/R3Et7ja80KGicw842UfGdqwibqibps68GtpYMWckOuYMbycGCHejaWdLBxAhm7cmlHicyCyjdmtNhZOBQOUuOobA9w/640.png)

图1 数据源、数据表示和特征之间的层次关系 （引自\[1\]）

**DTI预测成功的** **关键因素与主要的挑战**

 DTI预测通常被定义为二分类问题（判断药物与靶标是否相互作用）或回归问题（预测药物与靶标之间的结合亲和力）。DTI预测成功的关键因素包括:

（1） 数据质量与数量：数据冗余与不一致性，即不同数据库间存在数据冗余和格式不一致问题，影响模型性能。

（2） 数据稀疏性：已知的DTI相互作用远少于未知相互作用，导致正负样本不平衡。

（3）数据整合挑战：需要从多个来源整合数据，以构建全面且具有代表性的数据集。

（4）表征工程**（** **Feature engineering** **）的** **问题**

 **手工表征**：如分子指纹、描述符和序列组成等，需要深厚的专业知识且难以捕捉复杂关系。

 **自动特征学习**：深度学习模型能够自动从数据中学习特征，但模型解释性较差，且需要大量超参数调整。

**（5）实验设置**

**数据分布**：DTI预测任务中的药物和靶标实体在训练集和测试集中的分布对模型性能有显著影响。

 **冷启动问题**：测试集中出现训练集中未见的药物或靶标时，预测难度显著增加。需采用严格的数据划分策略，如基于药物或靶标的聚类进行划分。

**解决策略与未来方向**

**数据层面**：高质量数据源：选择权威数据库，进行数据预处理和去重，确保数据一致性。

**数据增强与主动学习**：通过主动学习迭代优化模型训练，利用数据增强技术缓解数据稀疏性问题。

**特征表示**：多视图多模态表示：结合分子序列、图结构等多种数据模态，提高特征表示的全面性。

**异构网络信息整合**：整合药物\-靶标相互作用网络中的异构信息，提升模型生物解释性。

**大型语言模型（LLMs）应用**：利用LLMs从大量未标注数据中学习语义和结构信息，改进特征表示。

**实验优化**：消除高度相似样本：在实验前去除结构高度相似的药物或靶标，减少数据冗余。

**基于聚类的划分**：通过聚类算法对药物或靶标进行分组，确保训练集和测试集的独立性。

**AlphaFold的影响**：AlphaFold提供的可靠蛋白三维结构预测，显著提高了虚拟筛选的准确性。通过整合AlphaFold生成的结构数据，可以更精确地识别结合位点，优化药物设计。

In silico方法在DTI预测中发挥了重要作用，显著提高了药物发现的效率和准确性。然而，数据质量、特征表示和实验设置等方面仍存在挑战。

未来研究应聚焦于获取和整合高质量DTI数据集，开发先进的特征表示方法，并解决冷启动和预测精度等问题。随着技术的不断进步，In silico方法将在药物发现中发挥更加关键的作用，推动全球健康事业的持续发展。

本文的通讯作者是斯坦福大学的**Wu Han**和电子科技大学（衢州）长江三角洲地区研究院的**邹权**教授。

**参考文献**

1. Ru, Xiaoqing et al.In silico methods for drug-target interaction prediction. Cell Reports Methods, Volume 0, Issue 0, 101184

对本文的内容感兴趣的，欢迎加个人微信交流：（添加时请备注“微信文章交流”）

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/R3Et7ja80KGicw842UfGdqwibqibps68GtpfbBAIQpn4icj4k1RETYl6Uicf2R1Komq5IRVdcQ7reibFCf3hs50iazUog/640.png)

欢迎大家关注我的视频号：景磊讲文献

我们将在每周六晚上8点半至9点半对当周新发表的重要文章进行Journal Club直播交流。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/R3Et7ja80KGicw842UfGdqwibqibps68GtpalemCWqO4VmnLcoF0HHgsqgWGX8YUWU3jp4tBqYyPCWiafdDUyxldiaA/640.png)

对本文内容有需要交流或转载的，请联系：gzbiodiscovery@126.com

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/R3Et7ja80KGRJwZ5HeMxXBrUl6TxhSps37cLHCgnibqAria45xjQiagd89yJPolhTWkTMBZiaV8RQe0MOPr9pxHCdA/0.png) 

 BioPrime 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/R3Et7ja80KGRJwZ5HeMxXBrUl6TxhSps37cLHCgnibqAria45xjQiagd89yJPolhTWkTMBZiaV8RQe0MOPr9pxHCdA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
