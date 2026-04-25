---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mziwmtc4ode0mw-2247717801-1-adam-muon-google-magma-sota
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mziwmtc4ode0mw-2247717801-1-adam-muon-google-magma-sota.md
bloom: analyze
concepts:
  - adaptive-sparsity-as-regularization
  - momentum-alignment-as-signal-filter
  - geometry-aware-update-masking
layer_1_bolds:
  - "在优化过程中随机掩码（即直接丢弃）一半的参数更新，不仅没有让训练崩溃，反而大幅提升了收敛性能。"
  - "这种现象的本质在于，块级别的随机掩码天然引入了一种依赖于曲率的几何正则化。"
  - "Magma 是一个即插即用的封装器，直接将乘入现有自适应优化器产生的更新方向中，不引入任何额外的内存或计算开销。"
layer_2_fragments:
  - "随机丢弃更新也能变成几何正则化"
  - "动量与梯度对齐比“是否保留”更重要"
  - "异质曲率比同质曲率更需要选择性更新"
  - "零额外开销的改动更容易进入真实训练栈"
layer_3_thesis: "Magma 的关键不是“更稀疏”而是把掩码从信息损失改写成结构偏置，只让和长期动量一致的更新穿过高曲率噪声。"
status: complete
---

# Magma 让我重新看待“丢信息”这件事

## Layer 1

- **在优化过程中随机掩码（即直接丢弃）一半的参数更新，不仅没有让训练崩溃，反而大幅提升了收敛性能。**
- **这种现象的本质在于，块级别的随机掩码天然引入了一种依赖于曲率的几何正则化。**
- **Magma 是一个即插即用的封装器，直接将乘入现有自适应优化器产生的更新方向中，不引入任何额外的内存或计算开销。**

## Layer 2

- **随机丢弃更新也能变成几何正则化**
- **动量与梯度对齐比“是否保留”更重要**
- **异质曲率比同质曲率更需要选择性更新**
- **零额外开销的改动更容易进入真实训练栈**

## Layer 3

Magma 的关键不是“更稀疏”而是把掩码从信息损失改写成结构偏置，只让和长期动量一致的更新穿过高曲率噪声。

## Concepts

- `[[adaptive-sparsity-as-regularization]]`：这篇把“少更新一些”从算力妥协改成了几何归纳偏置。
- `[[momentum-alignment-as-signal-filter]]`：动量不再只是优化状态，而是用来区分稳定信号与抖动噪声的过滤器。
- `[[geometry-aware-update-masking]]`：掩码的价值来自损失景观结构，而不是来自稀疏本身。

## Back-references

- `[[mp-weixin-qq-com-mziwmtc4ode0mw-2247719075-1-muon-mamba-gram]]`：那篇说明 Muon 的瓶颈可以靠重写矩阵迭代来解决，因此它会把这篇从“随机掩码很神奇”改读成“优化器真正可改的是表示与结构，不只是超参”。
- `[[mp-weixin-qq-com-mzixmjywota4oq-2247485483-1-acc-chem-res]]`：自由能那篇提醒我，很多计算方法真正难的是采样到有效路径；它反过来让我把这篇理解成训练里的“路径选择”问题，Magma 在更新空间里减少的是坏路径，不只是减少步数。
- `[[mp-weixin-qq-com-mziznzg4otezng-2247484927-2-prl]]`：SOG-Net 那篇把长程作用拆成短程加可学习长程项，这会改变我对本 note 的理解：Magma 不是粗暴剪枝，而是在已有优化器外再叠一层结构化修正项。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mziwmtc4ode0mw-2247717801-1-adam-muon-google-magma-sota.md`
- Type: markdown
- Kind: other
