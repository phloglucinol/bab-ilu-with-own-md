---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzI5ODEyOTA3MQ%3D%3D&mid=2247489468&idx=2&sn=39d7dc7b6c491745b783cd04a1f5f211
canonical_url: https://mp.weixin.qq.com/s?__biz=MzI5ODEyOTA3MQ%3D%3D&mid=2247489468&idx=2&sn=39d7dc7b6c491745b783cd04a1f5f211
source_domain: mp.weixin.qq.com
title: 直接将原子坐标作为机器学习的输入特征，确实无法保证平移不变性和旋转不变性
author: 
published_at: 
fetched_at: 2026-04-25T02:03:24Z
extractor: wechat_worker
content_hash: ca4e8584d8fe48bb28c2b5e86a0fd40cd958f47b4ca71888243cb9dcd0b8e373
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/NgMsvvMKwS7icIzGS28VzYka7ue1W5OkGnt9PflZymtO7NK4cGibCUJYoibBUwMIic6QtXoINb9NO1tmoJmFRjDy9I0Xx6zUYxAia2qD3qGy5p94/0.jpg) 

# 直接将原子坐标作为机器学习的输入特征，确实无法保证平移不变性和旋转不变性

原创 少儿编程培养 少儿编程培养 [ 基于UE5技术谈工业孪生与仿真 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/NgMsvvMKwS5VFmwnUYX5zaQcbzyic2BBDm3j1YWFTR6l52L8c92AicR7KWHLyCooFzSC5GrurAiaQia9dkUoLvqTOPiblSZNibu7dgvibQYEQ8M6Fw/640.png)

Bohrium百科对ACSF的原理剖析非常透彻，用平移不变性、旋转不变性、置换不变性三条规则解释得很清楚，还详细拆解了径向函数G2和角度函数G4的数学形式。TUM官网介绍了DScribe的学术背景，显示这是正经的学术软件包，有发表论文支撑。DScribe的PyPI页面和CSDN教程都提供了实用的代码示例，包括如何创建CoulombMatrix和SOAP描述符。

还有一篇ScienceDirect的学术论文介绍了"物理启发的ACSF"，将原子半径自然地融入描述符，这对理解参数选择的物理意义很有帮助。MolML的PyPI页面展示了类似工具，但dscribe更主流。

你说得很对，直接将原子坐标作为机器学习的输入特征，确实无法保证**平移不变性**和**旋转不变性**。这意味着同一个分子，只要在空间中位置或朝向变了，输入给模型的数值就会完全不同，导致模型无法学到真正的物理规律。

为了解决这个问题，我们需要进行特征工程，将原始的几何结构转换成具有**不变性**的描述符。你提到的**原子中心对称函数 (ACSF)**和**库仑矩阵**正是两种经典且有效的方案。下面为你展开讲讲它们的原理，并重点介绍如何用 `dscribe`库来高效实现。

### 🧠 理论篇：为什么需要对称性描述符？

这两个描述符的核心思想，都是通过只使用原子间距离、角度等本身就具有不变性的物理量来构建特征，从而“教会”模型宇宙的基本对称性。

| 特征描述符               | 核心思想                                                                                       | 优点                                                        | 局限性                                                 |
| ------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- |
| **原子中心对称函数 (ACSF)** | 为每个原子构建一个描述其局部化学环境的“指纹”向量。这个向量由一系列径向函数和角度函数的值组成，分别探测以该原子为中心、在一定截断半径内的邻居原子的距离分布和角度分布。       | 非常精细地刻画了原子的局域环境，是构建高精度神经网络势能面（如Behler-Parrinello神经网络）的基础。 | 参数（如截断半径、高斯函数的宽度等）的选择需要一定经验，可能需要进行调试。               |
| **库仑矩阵**            | 为整个分子构建一个矩阵，矩阵的对角线元素表示原子的电负性（通常用原子序数的2.4次方近似），非对角线元素表示两个原子间的库仑相互作用（$Z\_i Z\_j / R\_{ij}$）。 | 形式简单，包含了整体的静电信息，对分子整体性质的预测效果不错。                           | 矩阵的大小取决于原子数，需要对不同大小的分子进行统一填充或排序处理；对分子朝向敏感（未做特殊处理时）。 |

### 💻 实践篇：使用 `dscribe`生成描述符

`dscribe`是一个专门为材料科学和分子科学设计的Python库，它将上述复杂的描述符生成过程封装成了简单易用的API，是你将理论付诸实践的理想工具。

#### 1\. 安装与环境

你可以通过 `pip`轻松安装：

```
pip install dscribe
```

`dscribe`通常与 `ase`(Atomic Simulation Environment) 配合使用，用于处理原子结构。建议一并安装：

```
pip install ase
```

#### 2\. 核心代码示例

下面分别展示如何用 `dscribe`生成库仑矩阵和ACSF。

`import numpy as np` `from ase.build import molecule` `from dscribe.descriptors import CoulombMatrix, ACSF` `  
` `# 1. 创建一个分子结构（以水分子为例）` `# 使用ASE创建分子，它也可以轻松地从PLAMS或其它格式转换过来` `water = molecule('H2O')` `# water对象包含了原子的符号、坐标和晶格信息` `  
` `# --- 示例A：生成库仑矩阵 ---` `print("-" * 20 + "库仑矩阵" + "-" * 20)` `# 初始化：n_atoms_max 需要设为整个数据集中最大的原子数，不够的会自动补零` `# permutation="sorted_l2" 通过对矩阵进行排序来保证原子置换不变性，这是一个常用技巧` `cm_desc = CoulombMatrix(n_atoms_max=3, permutation="sorted_l2")` `  
` `# 为水分子创建库仑矩阵` `coulomb_matrix = cm_desc.create(water)` `print("库仑矩阵 (已展平为一维数组):\n", coulomb_matrix)` `# 输出是一个一维numpy数组，可以作为特征向量输入模型` `  
` `# --- 示例B：生成原子中心对称函数 (ACSF) ---` `print("-" * 20 + "原子中心对称函数 (ACSF)" + "-" * 20)` `# ACSF需要为每种原子类型分别设置参数，因为它会为每个原子生成一个特征向量` `# 这里以水分子中的氧和氢为例` `acsf_desc = ACSF(` `    species=["O", "H"],  # 体系中存在的元素种类` `    r_cut=6.0,           # 截断半径，只考虑此距离内的邻居` `    g2_params=[[1, 1], [1, 2], [1, 3]],  # 径向函数 (G2) 的参数，格式为 [eta, Rs]` `    g4_params=[[1, 1, 1], [1, 2, 1], [1, 1, -1], [1, 2, -1]] # 角度函数 (G4) 的参数，格式为 [eta, zeta, lambda]` `)` `  
` `# 为水分子生成ACSF。centers=[0,1,2]表示我们为所有原子（索引0,1,2）生成特征` `acsf_features = acsf_desc.create(water, centers=[0, 1, 2])` `print("ACSF 特征 (每个原子的特征向量):\n", acsf_features)` `# 输出是一个形状为 (n_atoms, n_features) 的矩阵` `# 例如，可以取所有原子特征的平均或求和作为整个分子的描述符` `# molecular_descriptor = np.mean(acsf_features, axis=0)` `  
` `# 你也可以并行处理多个结构` `# samples = [molecule('H2O'), molecule('CH4'), molecule('NH3')]` `# all_cm = cm_desc.create(samples, n_jobs=4) # 使用4个进程`

#### 3\. 参数选择的实用建议

* **ACSF参数**：这是一项经验性工作，但有规律可循。通常，径向函数 (`G2`) 的 `Rs`参数需要覆盖重要的化学键长范围，而 `eta`控制高斯函数的宽度。角度函数 (`G4`) 的 `zeta`控制角度分布的尖锐程度。你可以从文献中的常用值开始尝试。
* **原子序数特征**：如果使用ACSF，它会自动考虑原子种类。如果使用库仑矩阵，除了矩阵本身，有时也会将原子序数作为额外特征拼接起来。
* **局限性**：基于距离和角度的描述符（如ACSF）**天生无法区分手性分子**的对映异构体，因为它们的镜像结构具有完全相同的距离和角度。如果你的研究涉及手性，需要考虑更高级的描述符（如 `dscribe`中也提供的SOAP），或者引入额外的特征。

### 🚀 整合到你的工作流

有了 `dscribe`，你就可以轻松地将上一轮对话中的特征提取部分替换掉，生成真正具有物理不变性的高质量特征，然后用它们来训练你的PyTorch模型。

`# 在你的数据处理循环中` `from ase import Atoms` `from dscribe.descriptors import ACSF` `  
` `# 假设你用PLAMS得到了一个分子对象 'plams_mol'，你需要先将其转换为ASE的Atoms对象` `# 这里简化为直接使用ASE创建` `atoms_list = [molecule('H2O'), molecule('CH4')] # 从你的AMS任务结果中收集` `  
` `acsf_desc = ACSF(species=["H", "C", "O"], r_cut=6.0, ...) # 初始化` `features_list = []` `energies_list = [] # 对应的能量标签` `  
` `for atoms in atoms_list:` `    # 为当前分子中的所有原子生成ACSF，然后合并成分子指纹（例如取平均）` `    atom_features = acsf_desc.create(atoms, centers=range(len(atoms)))` `    mol_feature = np.mean(atom_features, axis=0)` `    features_list.append(mol_feature)` `    # energies_list.append( 从AMS结果中获取的能量 )` `  
` `# 接下来就可以用 features_list 和 energies_list 来训练你的PyTorch模型了`

希望这个结合了原理与实践的补充，能帮助你构建更可靠的代理模型。如果你在具体实现中遇到问题，比如ACSF的参数调试，随时可以再一起讨论。

  
预览时标签不可点

作者提示: 内容由AI生成

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IT4zXMc83j6H4XKuPE5wXrd7pyPxicugibvPlV0HQguFzeGfkWlic7yiaSjQ3ibCFDI04FNxfkseVStibkD7jyfdTJUQ/0.png) 

 基于UE5技术谈工业孪生与仿真 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/IT4zXMc83j6H4XKuPE5wXrd7pyPxicugibvPlV0HQguFzeGfkWlic7yiaSjQ3ibCFDI04FNxfkseVStibkD7jyfdTJUQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
