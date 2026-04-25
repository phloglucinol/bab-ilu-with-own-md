---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzixmjywota4oq-2247485714-1-drugclip-posebench-immunostruct
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzixmjywota4oq-2247485714-1-drugclip-posebench-immunostruct.md
bloom: analyze
concepts:
  - shared-embedding-for-retrieval
  - benchmark-exposes-generalization-gaps
  - multimodal-structure-improves-prediction
layer_1_bolds:
  - "DrugCLIP 这一对比学习框架将蛋白口袋与小分子编码到共享的潜在空间中，实现利用蛋白靶点对大型化合物库的高速查询。"
  - "PoseBench 的实证分析表明，深度学习共折叠方法整体上优于可比的传统对接算法，但在面对全新的蛋白-配体结合构象时仍然存在明显挑战。"
  - "ImmunoStruct 通过融合序列、结构和生化特征，实现对多等位基因 I 类肽-MHC 免疫原性的预测。"
layer_2_fragments:
  - "共享嵌入空间把筛选问题改写成检索问题"
  - "强 benchmark 的价值在于揭露泛化缺口"
  - "多模态输入不是装饰而是补掉单模态盲区"
  - "速度、结构精度、功能预测对应不同能力层"
layer_3_thesis: "把 DrugCLIP、PoseBench 和 ImmunoStruct 放在一起看，我会把药物 AI 分成三层能力：先大规模召回候选，再验证结构泛化，最后再预测真正与生物功能相关的下游效应。"
status: complete
---

# 这组三篇 paper 放在一起看 才会暴露药物 AI 的真正分层

## Layer 1

- **DrugCLIP 这一对比学习框架将蛋白口袋与小分子编码到共享的潜在空间中，实现利用蛋白靶点对大型化合物库的高速查询。**
- **PoseBench 的实证分析表明，深度学习共折叠方法整体上优于可比的传统对接算法，但在面对全新的蛋白-配体结合构象时仍然存在明显挑战。**
- **ImmunoStruct 通过融合序列、结构和生化特征，实现对多等位基因 I 类肽-MHC 免疫原性的预测。**

## Layer 2

- **共享嵌入空间把筛选问题改写成检索问题**
- **强 benchmark 的价值在于揭露泛化缺口**
- **多模态输入不是装饰而是补掉单模态盲区**
- **速度、结构精度、功能预测对应不同能力层**

## Layer 3

把 DrugCLIP、PoseBench 和 ImmunoStruct 放在一起看，我会把药物 AI 分成三层能力：先大规模召回候选，再验证结构泛化，最后再预测真正与生物功能相关的下游效应。

## Concepts

- `[[shared-embedding-for-retrieval]]`：把蛋白-配体匹配问题变成向量检索，规模才真正上去。
- `[[benchmark-exposes-generalization-gaps]]`：好的 benchmark 不是证明模型强，而是暴露它在哪些真实条件下会失效。
- `[[multimodal-structure-improves-prediction]]`：序列、结构和生化特征的组合，往往比单模态更接近真实生物任务。

## Back-references

- `[[mp-weixin-qq-com-mziwnte5mza2nw-2247501577-1]]`：片段对接那篇会迫使我把 PoseBench 读得更严厉，因为它说明真实筛选场景中的任务迁移比 paper 里的重对接更难。
- `[[mp-weixin-qq-com-mzixmjywota4oq-2247485483-1-acc-chem-res]]`：自由能那篇增加了一层机制视角，所以它会让我把 DrugCLIP 的成功理解为“高效召回”，而不是已经逼近物理解释。
- `[[mp-weixin-qq-com-mzizmjqynzq5ma-2247726606-1-ai]]`：蛋白拓扑与动力学那篇提醒我，结构预测里可能压缩了深层物理约束，这会改变我对 ImmunoStruct 的理解：多模态并不只是拼特征，而是在复原这些约束。

## Source

- Input: `raw/articles/mp-weixin-qq-com-mzixmjywota4oq-2247485714-1-drugclip-posebench-immunostruct.md`
- Type: markdown
- Kind: other
