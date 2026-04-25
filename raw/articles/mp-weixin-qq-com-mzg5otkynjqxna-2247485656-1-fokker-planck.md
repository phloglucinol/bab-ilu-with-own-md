---
type: raw_article
source_url: http://mp.weixin.qq.com/s?__biz=Mzg5OTkyNjQxNA%3D%3D&mid=2247485656&idx=1&sn=e3f28a26229b4c171e3b084c245b3e8a
canonical_url: http://mp.weixin.qq.com/s?__biz=Mzg5OTkyNjQxNA%3D%3D&mid=2247485656&idx=1&sn=e3f28a26229b4c171e3b084c245b3e8a
source_domain: mp.weixin.qq.com
title: Fokker-Planck方程的简单示例
author: 
published_at: 
fetched_at: 2026-04-25T02:04:37Z
extractor: wechat_worker
content_hash: 19bbd30ceeb76efde7a2bcf3e0ac800410498f505e42e86cb526460562d4d51a
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/zNAUUG5R8Nr3WjKEr06e9KicUfG7OVb7WwgA7qEj6HvHbArhOicMZm4UxsKrzuw9RkZUialCPHDSckR5o9Mu9EBvw/0.jpg) 

# Fokker-Planck方程的简单示例

原创 人间星海 人间星海 [ 数学科学的探索之旅 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

### 一、简化示例：一维肿瘤细胞密度的随机动力学模型

为了便于理解，我们从原三维模型中提取核心思想，构建一个**一维简化模型**，仅考虑肿瘤细胞密度  的动态变化，并引入随机噪声描述微环境的不确定性。

#### **1\. 确定性动力学模型（漂移项）**

假设肿瘤细胞的确定性增长遵循 **逻辑斯谛模型** 并包含线性降解：

其中：

* 表示密度依赖的增长（承载能力归一化为1），
* 表示线性降解（如免疫清除或自然死亡）。  
稳态解为：
1. **消除态**：，
2. **存活态**：（当  时存在）。

#### **2\. 引入随机噪声（扩散项）**

假设微环境噪声为 **高斯白噪声**，对应的随机微分方程（SDE）为：

其中：

* 为噪声强度（ 是小参数，表征噪声方差），
* 为维纳过程（满足 ，）。

### 二、Fokker-Planck方程的详细推导

Fokker-Planck方程（FPE）描述了概率密度  的演化，其推导需从随机微分方程出发，利用 **泰勒展开** 和 **伊藤引理**。

#### **1\. 一维FPE的一般形式**

对于SDE：

其中  为漂移系数， 为扩散系数。  
概率密度  满足：

**推导步骤**：

1. **状态转移概率**：设  为  时刻在  处的粒子在  时刻转移到  处的概率密度。
2. **泰勒展开**：对  在  附近展开至二阶：同时，考虑粒子在  内从  转移到  的概率，利用维纳过程的增量 ，得：
3. **统计平均**：计算  和  的期望：高阶矩（如 ）在  时可忽略。
4. **代入连续性方程**：通过质量守恒，得：即一维Fokker-Planck方程。

#### **2\. 代入简化模型参数**

在简化模型中：

因此FPE为：

### 三、稳态解与势能景观构建

当系统达到稳态时，，稳态概率密度  满足：

#### **1\. 势能函数定义**

假设稳态分布可表示为 **玻尔兹曼分布**，引入势能  满足：

则：

代入稳态FPE并忽略高阶小项，得：

即势能梯度与漂移项成正比：

积分得势能函数（设积分常数为0）：

#### **2\. 稳态点与势景观**

1. **消除态（）**：  
势能 （参考点）。
2. **存活态（）**：  
代入得：
3. **鞍点（势垒顶点）**：  
势能导数为0处：  
或  
但中间的极大值点在 （当  时），此处势能为：该点为两稳态间的势垒，高度为 。

### 四、噪声影响与状态跃迁

噪声使系统有概率跨越势垒：

* **从消除态到存活态**：需克服势垒 ，概率与  成反比，噪声越强（ 越大），跃迁概率越高。
* **稳态分布形状**：当  时，概率密度集中在稳态点附近，形成“势谷”；当  增大，分布展宽，势谷变浅。

### 五、与原模型的联系

简化模型中的FPE推导可推广至原三维系统：

1. **高维FPE**：对于 ，FPE为：其中  为散度， 为拉普拉斯算子。
2. **势能景观**：原模型中的消除态、休眠态、逃逸态对应多维空间中的“势谷”，鞍点对应势垒，高斯混合近似用于描述多稳态分布。

### 六、结论

通过一维简化模型，我们展示了：

1. **Fokker-Planck方程的推导**：从随机微分方程出发，利用泰勒展开和统计平均，得到概率密度演化方程。
2. **势能景观构建**：通过稳态FPE解，定义势能函数，量化不同稳态间的势垒，揭示噪声驱动的状态跃迁机制。
3. **生物学意义**：低噪声（强确定性）下系统稳定在势谷，高噪声下可能跨越势垒，对应肿瘤从休眠态向逃逸态的转变。

该框架为理解肿瘤微环境的随机动力学提供了数学工具，可进一步扩展至多维系统，结合实验数据校准参数，指导免疫治疗策略（如通过降低MDSCs活性，增加势垒高度，稳定肿瘤休眠态）。

### 参考文献

\[1\] Wang S, Wang T F, Wu S N, Zhang L, Zou X F. Mathematical modeling and solution landscape reveal cancer progression dynamics in tumor ecological microenvironment\[J\]. SIAM Journal on Applied Mathematics, 2025, 85(1): 50-77\. DOI: 10.1137/23M1593061.

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/plk5ojzXAEXw4h3bc7srb94p9UxBkGlAWgtbASQia4ZdFGMxBRnRyUIeic3QkVOBP7yvuiawR0iaHcwohy1iab7L0PrCC0zsicibNEveHHkBaZhHn0/0.png) 

 数学科学的探索之旅 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/plk5ojzXAEXw4h3bc7srb94p9UxBkGlAWgtbASQia4ZdFGMxBRnRyUIeic3QkVOBP7yvuiawR0iaHcwohy1iab7L0PrCC0zsicibNEveHHkBaZhHn0/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
