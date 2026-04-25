---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzg3otc1nduxoq-2247484629-1-cell-reports-method
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzg3otc1nduxoq-2247484629-1-cell-reports-method.md
bloom: understand
concepts:
  - dti-prediction-is-a-data-problem-first
  - cold-start-dti
  - representation-and-split-coupling
  - feature-engineering-to-foundation-models
layer_1_bolds:
  - "DTI预测成功的关键因素包括数据质量与数量。"
  - "冷启动问题：测试集中出现训练集中未见的药物或靶标时，预测难度显著增加。"
  - "利用LLMs从大量未标注数据中学习语义和结构信息，改进特征表示。"
  - "数据质量、特征表示和实验设置等方面仍存在挑战。"
layer_2_fragments:
  - "DTI难点首先是数据分布不是模型结构"
  - "训练测试划分方式决定你在测什么"
  - "冷启动暴露真实泛化能力"
  - "表征工程正在从手工特征转向预训练表示"
layer_3_thesis: "这篇综述最重要的提醒是，DTI模型的进步不能只看网络从CNN换到Transformer，而要同时看数据源、特征表示和切分协议如何共同定义了任务本身，否则所谓性能提升常常只是在更宽松的实验设置里自我奖励。"
status: complete
---

# mp-weixin-qq-com-mzg3otc1nduxoq-2247484629-1-cell-reports-method

## Layer 1 — bold key sentences

> DTI预测成功的关键因素包括数据质量与数量。

> 冷启动问题：测试集中出现训练集中未见的药物或靶标时，预测难度显著增加。

> 利用LLMs从大量未标注数据中学习语义和结构信息，改进特征表示。

> 数据质量、特征表示和实验设置等方面仍存在挑战。

## Layer 2 — bold fragments

- **DTI难点首先是数据分布不是模型结构**
- **训练测试划分方式决定你在测什么**
- **冷启动暴露真实泛化能力**
- **表征工程正在从手工特征转向预训练表示**

## Layer 3 — one-sentence thesis

这篇综述最重要的提醒是，DTI模型的进步不能只看网络从CNN换到Transformer，而要同时看数据源、特征表示和切分协议如何共同定义了任务本身，否则所谓性能提升常常只是在更宽松的实验设置里自我奖励。

## Concepts (tier_1_atoms)

- [[dti-prediction-is-a-data-problem-first]] — 综述反复指出，DTI 性能上限先被数据质量、稀疏性和数据库整合方式决定，而不是先被模型花样决定。
- [[cold-start-dti]] — 冷启动场景最能刺穿“平均分很高”的幻觉，因为它逼模型面对训练中没见过的药物或靶标。
- [[representation-and-split-coupling]] — 这篇的重要性在于把表征方法和数据划分绑在一起谈，说明它们共同决定了任务到底是在测记忆、插值还是泛化。
- [[feature-engineering-to-foundation-models]] — 从分子指纹和序列描述符到预训练表示与 LLM，这条演进线说明“特征工程”并没有消失，只是被上移到了预训练阶段。

## Back-references

- [[mp-weixin-qq-com-mzg4mta4ntc4mw-2247484032-2-jcim-2025-amp-openadmet-adme]] — OpenADMET 那篇把同样的问题在 ADME 上重演了一遍：随机切分指标很好看，骨架切分就塌，这正好证明这里说的 split 会重新定义任务难度。
- [[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483849-1-tmlr-2025-gnn-transformer-3d]] — GNN/Transformer/3D 表征之争看似在比模型结构，但这篇会逼我追问：这些表征提升究竟是在更严格冷启动里成立，还是只在宽松划分里自我加分。
- [[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483860-1-biorxiv-2025-molgenbench]] — MolGenBench 对生成模型重做更贴近实战的评测，这和本文强调 DTI 评测协议的重要性其实是一回事：评测设计本身就是方法学的一半。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzg3otc1nduxoq-2247484629-1-cell-reports-method.md`
- Type: markdown
- Kind: other
