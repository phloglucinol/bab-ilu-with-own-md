---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mziwmtc4ode0mw-2247719075-1-muon-mamba-gram
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mziwmtc4ode0mw-2247719075-1-muon-mamba-gram.md
bloom: analyze
concepts:
  - symmetric-structure-aware-optimization
  - iterate-in-smaller-space
  - optimizer-overhead-can-dominate
layer_1_bolds:
  - "对比 AdamW，Muon 达到特定损失值所需的优化器步数更少，但单步计算开销显著增加。"
  - "算法的核心在于转移迭代空间：不再对庞大的矩形输入矩阵进行迭代，而是转移至尺寸更小且对称的方形 Gram 矩阵。"
  - "更关键的是，算法执行期间产生的诸多中间矩阵具备对称结构，常规计算路线未能有效利用这一数学特性，导致半数计算工作冗余。"
layer_2_fragments:
  - "优化器瓶颈来自正交化而不是梯度本身"
  - "把矩形迭代改写到对称 Gram 空间"
  - "对称中间量没被利用就会浪费一半算力"
  - "数值稳定性修补与算子调度要一起设计"
layer_3_thesis: "Gram Newton-Schulz 证明了训练系统里最值钱的优化常常不是把同一件事算快一点，而是先承认你在错误的表示空间里计算。"
status: complete
---

# 优化器的提速有时来自重写表示而不是重写 kernel

## Layer 1

- **对比 AdamW，Muon 达到特定损失值所需的优化器步数更少，但单步计算开销显著增加。**
- **算法的核心在于转移迭代空间：不再对庞大的矩形输入矩阵进行迭代，而是转移至尺寸更小且对称的方形 Gram 矩阵。**
- **更关键的是，算法执行期间产生的诸多中间矩阵具备对称结构，常规计算路线未能有效利用这一数学特性，导致半数计算工作冗余。**

## Layer 2

- **优化器瓶颈来自正交化而不是梯度本身**
- **把矩形迭代改写到对称 Gram 空间**
- **对称中间量没被利用就会浪费一半算力**
- **数值稳定性修补与算子调度要一起设计**

## Layer 3

Gram Newton-Schulz 证明了训练系统里最值钱的优化常常不是把同一件事算快一点，而是先承认你在错误的表示空间里计算。

## Concepts

- `[[symmetric-structure-aware-optimization]]`：如果中间量天然对称，就不该继续假装它是一般矩阵。
- `[[iterate-in-smaller-space]]`：真正的提速来自把迭代搬到更小更合适的空间，而不是原地硬算。
- `[[optimizer-overhead-can-dominate]]`：当优化器比前后向更贵时，训练性能瓶颈就已经转移了。

## Back-references

- `[[mp-weixin-qq-com-mziwmtc4ode0mw-2247717801-1-adam-muon-google-magma-sota]]`：Magma 那篇把“少做一些更新”解释成几何正则化，因此会把这篇从纯工程提速改读成同一类结构性干预，只是发生在表示层而不是更新选择层。
- `[[mp-weixin-qq-com-mziznzg4otezng-2247484927-2-prl]]`：SOG-Net 也通过改变长程相互作用的计算表示来获得近线性扩展，所以它会强化我对这篇的理解：算法设计的核心是找到可学习又可计算的中间表述。
- `[[mp-weixin-qq-com-mzizmtkzmjq5oq-2247484028-1-claude-code-100]]`：Claude Code 最佳实践里强调先做 plan 再动手；放到这里，它提醒我 Gram trick 也是一种“先换问题表述再执行”的工程方法，而不是单点微优化。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mziwmtc4ode0mw-2247719075-1-muon-mamba-gram.md`
- Type: markdown
- Kind: other
