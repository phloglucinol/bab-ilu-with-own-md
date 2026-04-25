---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzi2mju4mdywoa-2247491447-1-kv-cache-turboquant-rabitq
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzi2mju4mdywoa-2247491447-1-kv-cache-turboquant-rabitq.md
bloom: analyze
concepts:
  - distribution-whitening-before-quantization
  - inner-product-preserving-compression
  - kv-cache-is-not-weight-quantization
  - theory-lineage-matters
layer_1_bolds:
  - "TurboQuant的核心技术，随机旋转加极低比特量化，与RaBitQ早已提出的技术框架高度重合。"
  - "在足够高的维度下，通过一个与数据无关的线性变换，可以将任意复杂的原始分布标准化成一个简单的、可控的分布。"
  - "在随机旋转后的标准化空间中进行两阶段量化。"
  - "KV缓存的压缩，可实现内存占用大幅降低的同时，保证注意力计算中Query与Key之间的内积尽可能准确。"
layer_2_fragments:
  - "随机旋转把复杂分布压成 Beta 型近零坐标"
  - "压缩目标是内积无偏而不是向量逐坐标还原"
  - "KV cache 压缩与权重量化是两类问题"
  - "理论源头决定方法边界与正当性"
  - "宣传尺度不能替代理论与公平对比"
layer_3_thesis: "TurboQuant 与 RaBitQ 共同揭示的核心不是某个压缩率纪录，而是先用随机旋转把分布白化，再围绕“内积保持”而非“坐标还原”设计量化器，这才是 KV cache 极低比特压缩成立的真正条件。"
status: complete
---

# mp-weixin-qq-com-mzi2mju4mdywoa-2247491447-1-kv-cache-turboquant-rabitq

## Layer 1

- **TurboQuant的核心技术，随机旋转加极低比特量化，与RaBitQ早已提出的技术框架高度重合。**
- **在足够高的维度下，通过一个与数据无关的线性变换，可以将任意复杂的原始分布标准化成一个简单的、可控的分布。**
- **在随机旋转后的标准化空间中进行两阶段量化。**
- **KV缓存的压缩，可实现内存占用大幅降低的同时，保证注意力计算中Query与Key之间的内积尽可能准确。**

## Layer 2

- **随机旋转把复杂分布压成 Beta 型近零坐标**
- **压缩目标是内积无偏而不是向量逐坐标还原**
- **KV cache 压缩与权重量化是两类问题**
- **理论源头决定方法边界与正当性**
- **宣传尺度不能替代理论与公平对比**

## Layer 3

TurboQuant 与 RaBitQ 共同揭示的核心不是某个压缩率纪录，而是先用随机旋转把分布白化，再围绕“内积保持”而非“坐标还原”设计量化器，这才是 KV cache 极低比特压缩成立的真正条件。

## Concepts

- [[distribution-whitening-before-quantization]]：先标准化分布再量化，是这篇里最可迁移的工程原则。
- [[inner-product-preserving-compression]]：这里真正要保真的对象是注意力内积，不是坐标逐点复原。
- [[kv-cache-is-not-weight-quantization]]：这篇把在线 KV 压缩与离线权重量化彻底分开了。
- [[theory-lineage-matters]]：当方法依赖理论边界时，传承关系和定性准确性就是方法的一部分。

## Back-references

- [[mp-weixin-qq-com-mziwmtc4ode0mw-2247717801-1-adam-muon-google-magma-sota]]：Magma 那篇会让我把这里读成同一类工作，即先找准几何结构，再谈优化或压缩，不是纯工程堆料。
- [[mp-weixin-qq-com-mziwmtc4ode0mw-2247716057-1-transformer]]：如果 Transformer 那篇把 attention 解释成几何推理机，这篇就会变成“如何压缩推理机状态而不毁掉其几何核心”。
- [[mp-weixin-qq-com-mziwmtc4ode0mw-2247716247-1-kl-loss-bengio-reward]]：Bengio 那篇强调找准真正优化对象，这篇对应的是找准真正保真对象，两篇一起看会让我更警惕错把代理指标当目标。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzi2mju4mdywoa-2247491447-1-kv-cache-turboquant-rabitq.md`
- Type: markdown
- Kind: other
