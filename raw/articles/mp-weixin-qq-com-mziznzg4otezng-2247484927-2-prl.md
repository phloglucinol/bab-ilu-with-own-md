---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIzNzg4OTEzNg%3D%3D&mid=2247484927&idx=2&sn=319c6ebeecd9784029afd4bea7218959
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIzNzg4OTEzNg%3D%3D&mid=2247484927&idx=2&sn=319c6ebeecd9784029afd4bea7218959
source_domain: mp.weixin.qq.com
title: 上海交大数学学院PRL|长程相互作用系统的机器学习原子势
author: 
published_at: 
fetched_at: 2026-04-25T02:05:41Z
extractor: wechat_worker
content_hash: cdaab355571547619476cb94619378c92e349689e29551d942320923183bf3b5
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/u4tC0Vm8LdCPicVVusXxPOnZPza3zNhAZ9aou6nicQiblKFsfT2oILpFD7Njqc5Rdx5WWlDicVBq4AQ7wBykCZQsbA/0.jpg) 

# 上海交大数学学院PRL|长程相互作用系统的机器学习原子势

原创 全量子社区 全量子社区 [ 喵态盲盒实验室 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

  
All-Q

2025.10

**论文快讯**

**NEWS**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/u4tC0Vm8LdCPicVVusXxPOnZPza3zNhAZl1ibAnxPdibsmhtYw2mQ2OOuiaRTwPfblfiatKyJl1wwbFISPKOzkaNnng/640.png)

  
本文针对传统机器学习原子势（MLIPs）忽略长程相互作用的关键缺陷，提出**高斯和神经网络（SOG-Net）** 框架，通过 “短程 + 长程” 分离建模与高效数值算法，实现对多种长程作用（库仑、色散、偶极等）的自适应学习，同时保持量子级精度与近线性计算复杂度，为大规模低温量子 / 经典原子模拟提供突破性工具。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/u4tC0Vm8LdCPicVVusXxPOnZPza3zNhAZ2tk2QMe9adLshxdVWPTYUJXPF7cBZ2G1SWRv0OEVHF5wXFvc5horWQ/640.png)

## 一、研究背景：传统 MLIPs 的长程作用建模瓶颈

现有 MLIPs 虽能平衡量子精度与计算效率，但在长程相互作用（LR）建模上存在不可调和的问题，难以满足极性材料、生物体系、量子电解质等场景需求：

1. **短视性假设局限**  
多数 MLIPs 基于 “电子结构近视性原理”，仅考虑有限截断半径内的短程作用（SR），系统性忽略库仑、色散、偶极等长程作用 —— 这些作用对极性材料（如水、电解质）的结构与功能至关重要（如蛋白质折叠、电解质溶解度）。
2. **传统长程处理方法缺陷**
   * **Ewald 求和**  
   ：仅适用于1/r库仑势，无法处理1/r^p（p>1或非整数）、e^{-mu r}/r等复杂衰减形式；
   * **LODE 方法**  
   ：需手动猜测长程衰减指数p，依赖初始假设精度，适应性差；
   * **消息传递神经网络**  
   ：通过堆叠卷积层捕捉非局域作用，但长程慢衰减场景下计算成本激增（非多项式复杂度）；
   * **潜变量 Ewald 方法**  
   ：虽能学习潜变量（如部分电荷），但仍依赖 Ewald 求和，仅优化1/r作用，对非库仑长程作用提升有限。
3. **精度与效率难以兼顾**  
现有方法要么因忽略长程导致精度不足，要么因复杂算法导致计算量过大，无法满足大规模分子动力学（MD）模拟需求。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/u4tC0Vm8LdCPicVVusXxPOnZPza3zNhAZ13LibkH9ySDUY9pU1QqYWOBLW5QhNE7rKfR0vHHlLiaxBKGIPHqQcibpg/640.png)

## 二、核心创新：SOG-Net 框架的设计原理

SOG-Net 通过 “短程 - 长程分离建模 + 高效数值加速”，实现长程作用的自适应学习与低复杂度计算，核心设计分为三部分：

### 1\. 能量分解：短程（SR）与长程（LR）分离

总势能分解为短程与长程两部分，分别建模以兼顾精度与效率：

* **短程能量（E^{SR}）**  
：沿用传统 MLIPs 思路，通过原子局部环境描述符（D\_i，含平移 / 旋转 / 置换对称性）与神经网络f\_{theta\_{SR}}计算，即E^{SR}=sum\_{i=1}^N f\_{theta\_{SR}}(D\_i)；
   * 描述符D\_i基于截断半径r\_c内的邻居原子构建，确保短程作用的局部性。
* **长程能量（\\(E^{LR}\\)）**  
：通过 “潜变量 + 高斯和（SOG）乘法器 + 傅里叶卷积” 建模，核心公式为：E^{LR}=sum\_{eta=1}^P \\frac{1}{2V}\\sum\_k \\hat{g}\_{theta\_eta}(k) \\cdot |\\hat{\\rho}\_\\eta(k)|^2其中\\hat{g}\_{\\theta\_\\eta}(k)=\\sum\_{\\ell=1}^M w\_{\\ell,\\eta} e^{-k^2/s\_{\\ell,\\eta}^2}（SOG 乘法器，w\_{ell,eta}为权重，s\_{ell,eta}为方差，均为可训练参数），rho\_eta(k)为潜变量的结构因子。

### 2\. 关键组件：自适应长程学习的核心

* **潜变量网络**  
：将短程描述符D\_i映射为多层潜变量q\_{\\eta,i}（eta=1,...,P），可物理解释为 “原子部分电荷（库仑作用）”“原子尺寸（色散作用）” 等，实现对不同长程作用的加权表征。
* **SOG 乘法器**  
：通过多个高斯函数叠加，自适应拟合傅里叶空间中的长程衰减尾 —— 高斯函数的对称性与平滑性可最优平衡空间 - 频率局域性，对数间隔的方差初始化能高效覆盖多尺度长程作用，训练后可通过模型降维减少高斯数量（M）。
* **非均匀快速傅里叶变换（NUFFT）**  
：通过 “网格化→FFT→缩放→IFFT→聚集” 流程，将长程卷积的计算复杂度降至O(N + N\_{FFT}\\log N\_{FFT})\\)（\\(N\_{FFT}为傅里叶网格数），确保近线性扩展。

## 三、实验验证：多场景下的精度与效率验证

作者通过四类典型长程体系验证 SOG-Net 的性能，核心结果均优于现有模型：

### 1\. NaCl 电解质体系（库仑 + 伦纳德 - 琼斯作用）

* **数据集**  
：1000 个粒子，训练集 4000 个构型，测试集 200 个构型（NVT ensemble，T=300\\ text{K}）；
* **关键结果**  
：
   1. 纯短程模型误差显著，SOG-Net（1 层潜变量 + 6 个高斯）将能量测试误差降低**1-2 个数量级**；
   2. 仅需21^3傅里叶网格即可实现10^{-3}相对误差，且不会对纯短程系统过拟合（长程贡献可忽略）；
   3. 与 Ewald 基模型（CACE-LR）性能相当，且无需预设1/r衰减假设。

### 2\. 六种二聚体体系（多类型长程衰减）

* **体系设计**  
：覆盖带电（C）、极性（P）、非极性（A）分子的 6 类二聚体（CC、CP、PP、CA、PA、AA），长程衰减为\\(1/r^p\\)（\\(p=1\\)至 6）；
* **关键结果**  
：
   1. 纯短程模型在分子间距 > 5Å 时能量曲线明显扁平化，SOG-Net（1 层潜变量 + 12 个高斯）可精准捕捉长程尾；
   2. 力的均方根误差（RMSE）较纯短程降低**一个数量级**：如 CC 类从 64.3\\text{meV/Å}\\)降至 3.8\\(\\text{meV/Å}\\)，AA 类从 1.13\\(\\text{meV/Å}\\)降至 0.06\\(\\text{meV/Å}\\)；
   3. 对比现有方法：LODE 需手动调p，潜变量 Ewald 仅优化 CC 类，而 SOG-Net 对 6 类二聚体均实现最优性能。

### 3\. 液态水体系（偶极 + 氢键长程作用）

* **数据集**  
：1900 个构型（300 个原子，\\(T=300\\ \\text{K}\\)，密度 1\\(\\text{g/mL}\\)），DFT（PBE 泛函）生成；
* **关键结果**  
：
   1. 径向分布函数（RDF）：氧 - 氧、氧 - 氢、氢 - 氢 RDF 与 DFT 完全吻合，纯短程模型在长程区域（>3Å）偏差显著；
   2. 电荷结构因子：长波长极限（\\(k→0\\)）下与 DFT 一致，纯短程模型因忽略长程静电而急剧偏离；
   3. 计算成本：仅比纯短程模型高 10%-40%，MD 模拟中实现线性规模扩展（N从 100 增至 10000 时复杂度近线性）。

### 4\. 复杂分子 / 界面体系（电荷转移 + 长程作用）

* **测试体系**  
：\\(C\_{10}H\_2/C\_{10}H\_3^+\\)（有机离子）、\\(Na\_{8/9}Cl\_8^+\\)（缺陷电解质）、\\(Au\_2/MgO(001)\\)（金属 - 氧化物界面）；
* **关键结果**  
：
   1. 能量与力误差均低于现有模型（CC-ACE、4G-HDNNP、CACE-LR）：如\\(Na\_{8/9}Cl\_8^+\\)的能量 RMSE 仅 0.124\\(\\text{meV/atom}\\)（CACE-LR 为 0.21\\(\\text{meV/atom}\\)）；
   2. 界面电荷转移：在\\(Au\_2/MgO(001)\\)体系中，准确捕捉 Al 掺杂 / 未掺杂界面的 “润湿 - 非润湿” 能量差（与 DFT 偏差仅 0.1\\(\\text{meV}\\)），并精准复现 Au-O 平衡键长（纯短程模型无法区分掺杂 / 未掺杂界面）。

## 四、核心优势：与现有方法的关键差异

| 对比维度    | 传统方法（Ewald/LODE/ 潜变量 Ewald）              | SOG-Net                                                  |
| ------- | ---------------------------------------- | -------------------------------------------------------- |
| 长程衰减适应性 | 仅支持特定形式（如\\(1/r\\)），需手动预设                | 自适应拟合多种衰减（\\(1/r^p\\)、指数衰减等），无需手动调参                      |
| 计算复杂度   | Ewald 为\\(O(N\\log N)\\)，LODE 依赖初始 guess | 近线性（\\(O(N + N\_{FFT}\\log N\_{FFT})\\)），MD 成本仅增 10%-40% |
| 精度覆盖范围  | 仅优化能量 / 结构，力的精度不足                        | 能量与力的 RMSE 均降 1-2 个数量级，与 DFT 高度吻合                        |
| 现有框架兼容性 | 难以集成到多数 MLIPs                            | 可直接嵌入 HDNNP、ACE、MACE、CACE 等现有框架                          |

## 五、应用前景与未来方向

1. **适用场景扩展**  
可直接用于量子电解质、生物分子模拟、低温量子材料（如超导界面）、空间环境压电器件等需长程作用建模的场景，尤其适合大规模 MD 模拟（\\(N>10^4\\)原子）。
2. **框架集成潜力**  
长程卷积层可无缝集成到现有 MLIPs（如 HDNNP、ACE、GAP），通过学习潜变量（部分电荷、沃尼尔中心等）实现长程衰减的自适应优化，降低现有模型的改造成本。
3. **未来优化方向**
   * 处理更高阶多体长程作用（如三体偶极 - 偶极相互作用）；
   * 结合随机批处理算法进一步降低计算成本；
   * 扩展至太赫兹（THz）频段的动态长程作用建模。

##   
  
  
\--点击底部阅读原文进入论文首页--

  
往期内容：

[崛起！25年国人科学家已在Nature Photonics发表文章63篇，占比超52%：本文详细统计](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484866&idx=1&sn=6add502a4bad0efc7e6fd63b2bf37289&scene=21#wechat%5Fredirect)

[Nature Physics 纠缠光子的生成可以由电子能量来预报：基于自由电子与集成光子波导相互作用](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484668&idx=1&sn=2dbf0a72d4766c1af47f1196783ea510&scene=21#wechat%5Fredirect)

[PRL | 太赫兹带宽的电光调制器：操控单光子级脉冲](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484659&idx=2&sn=861adfb44d193b327b05b0e7016298d7&scene=21#wechat%5Fredirect)

[&lt;世界纪录&gt;IBM Quantum实现了史上最大的薛定谔猫量子态：120个比特的GHZ state](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484574&idx=1&sn=65e0b146d581d2e49acbea9c2c182a96&scene=21#wechat%5Fredirect)

[博后招聘|ASML与荷兰先进光刻研究中心、牛津、香港大学、南洋理工、斯坦福、新加坡国立等](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484496&idx=1&sn=b23c1839977d9b4b8b300e59f7a2e029&scene=21#wechat%5Fredirect)

[复旦大学最新Nature打破芯片壁垒：全球首颗二维硅基混合架构闪存芯片](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484468&idx=1&sn=e0cc42598f9b6cd66605c471c96d606a&scene=21#wechat%5Fredirect)

[arXiv最新快讯-10月2日](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484302&idx=1&sn=eb4e1efa6a62e1c2a7a17f1be4c9c3d9&scene=21#wechat%5Fredirect)

[arXiv.org快讯 | NVIDIA, MIT, Harvard等最新研究成果](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484283&idx=1&sn=07504f6cd4a7b81cf80740cbad6629f8&scene=21#wechat%5Fredirect)

[arXiv.org快讯|MIT, 哥本哈根等最新研究成果](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484260&idx=1&sn=9fa554d2f603a11b20166ca64af040ed&scene=21#wechat%5Fredirect)

[超宽带即插即用光子张量内核封装，损耗低于 1dB](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484260&idx=3&sn=2922769705860587a8d5f67ab44a7adf&scene=21#wechat%5Fredirect)

[加州理工: 通过很少的单量子比特测量来认证几乎所有量子态](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484037&idx=3&sn=516845cc5ade930b26948b99b4ae993e&scene=21#wechat%5Fredirect)

[西班牙ICFO：通过莫尔超晶格中的负差导率实现单光子检测发表于SCIENCE](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484164&idx=2&sn=7905f5bde1c914606d6ad78b5d90137a&scene=21#wechat%5Fredirect)

[哈佛Lukin组：用于通用量子计算的低开销横向容错](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484142&idx=2&sn=363b7c6f2fb63f8af787b6482e660c68&scene=21#wechat%5Fredirect)

[多模压缩态实现单模式量子增强多参数传感](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzIzNzg4OTEzNg==&mid=2247484142&idx=3&sn=aae7aa154b12c17dc404056a6f9de871&scene=21#wechat%5Fredirect)

  
**END**

免责声明：本公众号发布的所有内容，包括但不限于文字、图片、图表、标志、标识、广告、域名、软件、程序等，除特别标明外，均来源于网络或用户投稿，版权归原作者或原出处所有。我们致力于保护原作者版权，若涉及版权问题，请及时联系我们进行处理。
  
  
预览时标签不可点

[阅读原文](javascript:;) 

修改于 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/u4tC0Vm8LdAJwGHuRibw0cn2Elqs6vOkLxLEwoczbfpEdI9e8wjibpYZgvgCffIuQkTjuQpOIZuK2TSO9XMjMauw/0.png) 

 喵态盲盒实验室 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/u4tC0Vm8LdAJwGHuRibw0cn2Elqs6vOkLxLEwoczbfpEdI9e8wjibpYZgvgCffIuQkTjuQpOIZuK2TSO9XMjMauw/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
