---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mze5mte0njg3nq-2247485326-1-ai
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mze5mte0njg3nq-2247485326-1-ai.md
bloom: analyze
concepts:
  - learnable-long-range-tail
  - fixed-kernel-limitation
  - short-range-backbone-long-range-head
layer_1_bolds:
  - 与其预设物理规律，不如让模型从数据中直接学习长程相互作用的“尾部”衰减行为。
  - SOG-Net 的核心创新在于，它用一组可训练的高斯函数来拟合相互作用在傅里叶空间中的核。
  - CACE-SOG模型不仅精度更高，而且在参数数量上比同类模型减少了一个数量级以上。
layer_2_fragments:
  - 长程尾部不必固定成1/r
  - 短程描述符与可学习长程模块拼接
  - 智能初始化提升训练稳定性
  - 复杂界面屏蔽效应需要可变衰减
layer_3_thesis: 长程相互作用真正麻烦的地方不是“作用范围远”，而是它的衰减律会随着环境变形，所以把核函数写死本身就是错误假设。
status: complete
---

# mp-weixin-qq-com-mze5mte0njg3nq-2247485326-1-ai

## Layer 1 — bold key sentences

- **与其预设物理规律，不如让模型从数据中直接学习长程相互作用的“尾部”衰减行为。**
- **SOG-Net 的核心创新在于，它用一组可训练的高斯函数来拟合相互作用在傅里叶空间中的核。**
- **CACE-SOG模型不仅精度更高，而且在参数数量上比同类模型减少了一个数量级以上。**

## Layer 2 — bold fragments

- **长程尾部不必固定成 1/r**
- **短程描述符与可学习长程模块拼接**
- **智能初始化提升训练稳定性**
- **复杂界面屏蔽效应需要可变衰减**

## Layer 3 — one-sentence thesis

长程相互作用真正麻烦的地方不是“作用范围远”，而是它的衰减律会随着环境变形，所以把核函数写死本身就是错误假设。

## Concepts (tier_1_atoms)

- [[learnable-long-range-tail]]：让长程相互作用尾部随数据学习而非预设。
- [[fixed-kernel-limitation]]：固定核函数会系统性错过环境依赖的衰减模式。
- [[short-range-backbone-long-range-head]]：用强短程表示加专门长程头处理不同物理尺度。

## Back-references

- [[mp-weixin-qq-com-jacs-so3lr]]：SO3LR也是短程网络加物理尾项，但这里更激进，把尾项本身也做成可学习核；说明“物理分解”之后，剩下的问题仍然是该固定多少、学习多少。
- [[mp-weixin-qq-com-mze5mte0njg3nq-2247484476-1-jacs]]：JACS 张量框架通过输出头写进张量语法，这篇通过 SOG-Net 写进可变长程语法；二者都把难题从主干转移到专用头部设计。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mze5mte0njg3nq-2247485326-1-ai.md`
- Type: markdown
- Kind: other
