---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzixmjywota4oq-2247485483-1-acc-chem-res
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzixmjywota4oq-2247485483-1-acc-chem-res.md
bloom: understand
concepts:
  - path-based-free-energy
  - mechanism-vs-throughput-tradeoff
  - collective-variable-selection-bottleneck
layer_1_bolds:
  - "炼金术方法如自由能微扰（FEP）和热力学积分（TI）已被广泛应用于药物工业中的相对自由能计算，但其在绝对自由能预测、机制解释和动力学分析方面存在局限。"
  - "相比之下，路径法如 MetaDynamics、伞形采样和牵引分子动力学能够提供结合路径、自由能剖面和机制洞察。"
  - "CV 选择一直是路径法的瓶颈，人工设定易引入偏差。"
layer_2_fragments:
  - "高通量方法往往牺牲机制可见性"
  - "路径法真正贵在变量选择而不是模拟本身"
  - "非平衡模拟可以换取并行效率"
  - "机器学习更像流程自动化器而不是物理替代品"
layer_3_thesis: "自由能计算没有单一最优方法，真正的决策轴是你此刻需要排序相似化合物，还是需要看见结合过程本身。"
status: complete
---

# 自由能计算的分歧不在精不精确 而在你到底想知道什么

## Layer 1

- **炼金术方法如自由能微扰（FEP）和热力学积分（TI）已被广泛应用于药物工业中的相对自由能计算，但其在绝对自由能预测、机制解释和动力学分析方面存在局限。**
- **相比之下，路径法如 MetaDynamics、伞形采样和牵引分子动力学能够提供结合路径、自由能剖面和机制洞察。**
- **CV 选择一直是路径法的瓶颈，人工设定易引入偏差。**

## Layer 2

- **高通量方法往往牺牲机制可见性**
- **路径法真正贵在变量选择而不是模拟本身**
- **非平衡模拟可以换取并行效率**
- **机器学习更像流程自动化器而不是物理替代品**

## Layer 3

自由能计算没有单一最优方法，真正的决策轴是你此刻需要排序相似化合物，还是需要看见结合过程本身。

## Concepts

- `[[path-based-free-energy]]`：把自由能问题理解成沿路径重建能量地形，而不只是比较两个端点。
- `[[mechanism-vs-throughput-tradeoff]]`：工业主流方法与机制解释方法服务的是不同问题。
- `[[collective-variable-selection-bottleneck]]`：路径法最难的地方常常不是采样，而是先把正确的描述变量挑出来。

## Back-references

- `[[mp-weixin-qq-com-mziwnte5mza2nw-2247501577-1]]`：那篇对接评估会把这里的“方法选择”推得更具体，因为它提醒我同一个计算目标在不同任务里会失效，所以自由能方法的适用性也必须绑定问题场景。
- `[[mp-weixin-qq-com-mzixmjywota4oq-2247485714-1-drugclip-posebench-immunostruct]]`：DrugCLIP 与 PoseBench 说明了大规模检索和真实结构评估之间的错位，这会改变我对本 note 的理解：自由能方法不是要取代检索，而是补足检索无法提供的机制层。
- `[[mp-weixin-qq-com-mziwmtc4ode0mw-2247717801-1-adam-muon-google-magma-sota]]`：Magma 用动量对齐过滤坏更新，让我把路径法中的 CV 选择理解为同类动作，都是在高维空间里挑出真正控制行为的坐标。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzixmjywota4oq-2247485483-1-acc-chem-res.md`
- Type: markdown
- Kind: other
