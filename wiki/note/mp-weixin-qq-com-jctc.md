---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-jctc
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-jctc.md
bloom: analyze
concepts:
  - pinn-for-molecular-pde
  - architecture-as-numerical-method
  - experimental-constraints-in-pde-learning
layer_1_bolds:
  - 最精确的架构利用了输入和输出缩放层、随机傅里叶特征层、可训练的激活函数以及损失平衡算法。
  - 作者实现的精度在10e-2到10e-3的数量级。
  - 作者还探讨了将实验信息融入模型的可能性，并讨论了面临的挑战和未来的工作，尤其是在非线性PBE方面。
layer_2_fragments:
  - PINN不是单一架构而是一组数值技巧
  - 多域接口问题决定建模难度
  - 损失平衡直接影响求解精度
  - 实验信息可作为额外边界约束
layer_3_thesis: 在PINN里，网络结构本身就是数值方法的一部分，所以“调模型”经常等价于“重写求解器”。
status: complete
---

# mp-weixin-qq-com-jctc

## Layer 1 — bold key sentences

- **最精确的架构利用了输入和输出缩放层、随机傅里叶特征层、可训练的激活函数以及损失平衡算法。**
- **作者实现的精度在10e-2到10e-3的数量级。**
- **作者还探讨了将实验信息融入模型的可能性，并讨论了面临的挑战和未来的工作，尤其是在非线性PBE方面。**

## Layer 2 — bold fragments

- **PINN 不是单一架构而是一组数值技巧**
- **多域接口问题决定建模难度**
- **损失平衡直接影响求解精度**
- **实验信息可作为额外边界约束**

## Layer 3 — one-sentence thesis

在 PINN 里，网络结构本身就是数值方法的一部分，所以“调模型”经常等价于“重写求解器”。

## Concepts (tier_1_atoms)

- [[pinn-for-molecular-pde]]：把分子静电问题直接表述为受物理约束的神经求解任务。
- [[architecture-as-numerical-method]]：缩放层、傅里叶特征、激活函数和损失平衡都在改写数值性质。
- [[experimental-constraints-in-pde-learning]]：实验数据不是事后验证，也可以进入求解约束。

## Back-references

- [[mp-weixin-qq-com-jcim-rinpy-python]]：RIN把连续结构离散成图，这篇把连续静电场交给PINN；一个强调拓扑摘要，一个强调场方程求解，恰好是两种互补的结构视角。
- [[mp-weixin-qq-com-mze5mte0njg3nq-2247484463-1-jcim-dcc]]：DCC说明评估框架本身会强烈影响结论，这篇则说明PINN架构细节会强烈影响求解精度；两者都在提醒我不要把“方法外壳”误当成中性容器。

## Source
- Input: `raw/articles/mp-weixin-qq-com-jctc.md`
- Type: markdown
- Kind: other
