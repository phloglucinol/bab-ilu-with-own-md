---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg5otkynjqxna-2247485656-1-fokker-planck
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg5otkynjqxna-2247485656-1-fokker-planck.md
bloom: understand
concepts:
  - probability-dynamics-over-trajectories
  - noise-induced-state-transition
  - potential-landscape-from-sde
  - barrier-height-controls-fate-switch
layer_1_bolds:
  - "Fokker-Planck方程（FPE）描述了概率密度的演化。"
  - "假设稳态分布可表示为玻尔兹曼分布。"
  - "噪声使系统有概率跨越势垒。"
  - "低噪声（强确定性）下系统稳定在势谷，高噪声下可能跨越势垒，对应肿瘤从休眠态向逃逸态的转变。"
layer_2_fragments:
  - "从 SDE 推到概率密度演化"
  - "把稳态写成势能景观"
  - "势垒高度决定状态切换难度"
  - "噪声强度改变命运分布而非单条轨迹"
  - "肿瘤休眠/逃逸可被势谷语言表达"
layer_3_thesis: "Fokker-Planck 方程最有用的地方不是再写一个动力学方程，而是把随机系统从“单条轨迹怎么走”改写成“整体概率如何在势谷与势垒之间流动”，于是状态转变就能被势景观直接解释。"
status: complete
---

# mp-weixin-qq-com-mzg5otkynjqxna-2247485656-1-fokker-planck

## Layer 1

- **Fokker-Planck方程（FPE）描述了概率密度的演化。**
- **假设稳态分布可表示为玻尔兹曼分布。**
- **噪声使系统有概率跨越势垒。**
- **低噪声（强确定性）下系统稳定在势谷，高噪声下可能跨越势垒，对应肿瘤从休眠态向逃逸态的转变。**

## Layer 2

- **从 SDE 推到概率密度演化**
- **把稳态写成势能景观**
- **势垒高度决定状态切换难度**
- **噪声强度改变命运分布而非单条轨迹**
- **肿瘤休眠/逃逸可被势谷语言表达**

## Layer 3

Fokker-Planck 方程最有用的地方不是再写一个动力学方程，而是把随机系统从“单条轨迹怎么走”改写成“整体概率如何在势谷与势垒之间流动”，于是状态转变就能被势景观直接解释。

## Concepts

- [[probability-dynamics-over-trajectories]]：这篇把关注对象从单条轨迹换成概率密度，适合拿来理解很多“分布比样本更重要”的建模问题。
- [[noise-induced-state-transition]]：噪声在这里不是误差项，而是会改写状态切换概率的驱动力。
- [[potential-landscape-from-sde]]：把 SDE 改写成势能景观后，随机动力学开始有了可解释的几何语言。
- [[barrier-height-controls-fate-switch]]：真正决定命运切换难度的不是稳态标签，而是中间势垒有多高。

## Back-references

- [[mp-weixin-qq-com-mzkwode2otmzma-2247483756-1-science-bioemu]]：BioEmu 那篇会让我把这里的“概率密度演化”读成构象分布迁移，而不只是教科书上的随机过程推导。
- [[mp-weixin-qq-com-mzu2odu3mzc4nw-2247513112-1-ai-anewsampling-alphafold3]]：AnewSampling 强调重采样 AF3 分布后，我会反过来把这篇理解成一种更一般的“状态间跃迁控制”语言，而不是肿瘤例子的专用数学。
- [[mp-weixin-qq-com-mzi3mjm3odk0nq-2247511386-1-af2bind-alphafold2-2]]：AF2BIND 先找口袋热点，再回看这篇，就会把“低势区”理解成一种可被模型识别的功能位点，而不只是抽象几何概念。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg5otkynjqxna-2247485656-1-fokker-planck.md`
- Type: markdown
- Kind: other
