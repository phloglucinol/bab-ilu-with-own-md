---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-jacs-so3lr
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-jacs-so3lr.md
bloom: analyze
concepts:
  - hybrid-ml-force-field
  - half-local-plus-physical-tail
  - transferable-biomolecular-simulation
layer_1_bolds:
  - SO3LR方法将快速且稳定的SO3krates神经网络用于半局域相互作用，并结合了为短程排斥、长程静电和色散相互作用设计的通用成对力场。
  - SO3LR在一个包含400万个分子构象的庞大、多样化的量子力学数据集上进行了训练。
  - SO3LR模型及其开源框架为分子模拟领域提供了一个强大而通用的工具，极大地推动了我们向“无需为特定体系定制参数即可进行普适性量子精度模拟”这一终极目标迈进。
layer_2_fragments:
  - 半局域神经网络加物理成对势
  - 单GPU可扩展到超大体系
  - 训练集外体系仍保留泛化
  - 量子精度与经典效率混搭
layer_3_thesis: 通用力场不是把所有作用都交给一个更大的网络，而是先承认哪些相互作用应该继续由物理尾项负责，再让网络学剩下那部分难写规则的局部多体效应。
status: complete
---

# mp-weixin-qq-com-jacs-so3lr

## Layer 1 — bold key sentences

- **SO3LR方法将快速且稳定的SO3krates神经网络用于半局域相互作用，并结合了为短程排斥、长程静电和色散相互作用设计的通用成对力场。**
- **SO3LR在一个包含400万个分子构象的庞大、多样化的量子力学数据集上进行了训练。**
- **SO3LR模型及其开源框架为分子模拟领域提供了一个强大而通用的工具，极大地推动了我们向“无需为特定体系定制参数即可进行普适性量子精度模拟”这一终极目标迈进。**

## Layer 2 — bold fragments

- **半局域神经网络加物理成对势**
- **单 GPU 可扩展到超大体系**
- **训练集外体系仍保留泛化**
- **量子精度与经典效率混搭**

## Layer 3 — one-sentence thesis

通用力场不是把所有作用都交给一个更大的网络，而是先承认哪些相互作用应该继续由物理尾项负责，再让网络学剩下那部分难写规则的局部多体效应。

## Concepts (tier_1_atoms)

- [[hybrid-ml-force-field]]：把可解析物理项和数据驱动项分层，而不是互相替代。
- [[half-local-plus-physical-tail]]：局部多体由网络学，长程尾部由显式物理项接管。
- [[transferable-biomolecular-simulation]]：真正的可迁移不是跨几个 benchmark，而是训练外体系仍能稳定跑动力学。

## Back-references

- [[mp-weixin-qq-com-mze5mte0njg3nq-2247485326-1-ai]]：CACE-SOG也是短程描述符加长程模块，这篇把同样的分治思路推进到大尺度生物分子模拟，说明“拆作用机制”比“堆统一网络”更稳。
- [[mp-weixin-qq-com-j-chem-theory-comput]]：电荷模型提供静电接口，SO3LR提供动力学主干；前者解决表示问题，后者解决演化问题，两者组合起来才像完整的可计算分子世界。

## Source
- Input: `raw/articles/mp-weixin-qq-com-jacs-so3lr.md`
- Type: markdown
- Kind: other
