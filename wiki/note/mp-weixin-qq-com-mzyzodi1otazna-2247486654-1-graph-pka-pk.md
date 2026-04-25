---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzyzodi1otazna-2247486654-1-graph-pka-pk
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzyzodi1otazna-2247486654-1-graph-pka-pk.md
bloom: apply
concepts:
  - micro-pka-from-macro-labels
  - mil-for-ionization-sites
  - similar-molecules-anchor-predictions
  - pka-as-operational-drug-design-signal
layer_1_bolds:
  - "Graph-pKa 的基于多实例学习与图神经网络的pKa预测模型。"
  - "Graph-pKa 能够自动将预测的宏观 pKₐ 解构为离散的微观 pKₐ 值，实现原子级的精准洞察。"
  - "升级版的 Graph-pKa 已正式上线 SciMiner 平台。"
  - "系统还会自动检索并展示数据库中结构相似的分子及其实验测定的 pKₐ 真实值。"
layer_2_fragments:
  - "宏观 pKa 可以拆回到具体原子位点"
  - "多实例学习适合看不见真实发生活性位点的标签"
  - "预测值旁边给相似分子证据更实用"
  - "pKa 不只是理化性质表格字段"
  - "上线工具的价值在于支持快速决策"
layer_3_thesis: "Graph-pKa的真正价值不只是把误差压低，而是把 pKa 从静态性质预测变成可以落到具体位点、并能拿相似分子作参照的操作信号。"
status: complete
---

# mp-weixin-qq-com-mzyzodi1otazna-2247486654-1-graph-pka-pk

## Layer 1

- **Graph-pKa 的基于多实例学习与图神经网络的pKa预测模型。**
- **Graph-pKa 能够自动将预测的宏观 pKₐ 解构为离散的微观 pKₐ 值，实现原子级的精准洞察。**
- **升级版的 Graph-pKa 已正式上线 SciMiner 平台。**
- **系统还会自动检索并展示数据库中结构相似的分子及其实验测定的 pKₐ 真实值。**

## Layer 2

- **宏观 pKa 可以拆回到具体原子位点**
- **多实例学习适合看不见真实发生活性位点的标签**
- **预测值旁边给相似分子证据更实用**
- **pKa 不只是理化性质表格字段**
- **上线工具的价值在于支持快速决策**

## Layer 3

Graph-pKa的真正价值不只是把误差压低，而是把 pKa 从静态性质预测变成可以落到具体位点、并能拿相似分子作参照的操作信号。

## Concepts

- [[micro-pka-from-macro-labels]]：重要，因为很多实验标签只给宏观值，模型能否拆回微观位点直接决定可用性。
- [[mil-for-ionization-sites]]：重要，因为多实例学习是这里把“哪个原子在起作用”变成可学问题的关键。
- [[similar-molecules-anchor-predictions]]：重要，因为对药化决策来说，裸预测值远不如“预测值+相似物证据”。
- [[pka-as-operational-drug-design-signal]]：重要，因为 pKa 会同时影响溶解度、通透性、代谢和结合状态。

## Back-references

- [[mp-weixin-qq-com-mzyymjazmzc3ng-2247484240-1-jmc-f-pk-c-f]]：氟代那篇会把 pKa 变化解释为 PK 改变的重要来源，所以这篇相当于给那种解释补上了预测工具。
- [[mp-weixin-qq-com-mzyymjazmzc3ng-2247484062-1]]：那篇说“好设计”要同时处理理化与PK问题，回看这里，就能把 pKa 预测视作设计前置筛查而不是末端检测。
- [[mp-weixin-qq-com-mzyzota3njkxmg-2247583036-1-j-med-chem]]：AutoOptimizer 若没有类似 pKa 这样的中间性质信号，很容易只会优化活性；这篇提示了自动化优化缺的一块反馈。 

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzyzodi1otazna-2247486654-1-graph-pka-pk.md`
- Type: markdown
- Kind: other
