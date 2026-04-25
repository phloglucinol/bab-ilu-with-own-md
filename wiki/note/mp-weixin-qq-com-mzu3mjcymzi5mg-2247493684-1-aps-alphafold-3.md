---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzu3mjcymzi5mg-2247493684-1-aps-alphafold-3
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzu3mjcymzi5mg-2247493684-1-aps-alphafold-3.md
bloom: analyze
concepts:
  - cofolding-beats-covalent-docking
  - similarity-dependent-generalization-in-af3
  - blind-reactive-site-hinting
layer_1_bolds:
  - 共折叠方法在预测精度上显著优于传统方法。
  - 共折叠方法的性能仍然高度依赖于测试数据与训练数据的相似性。
  - AlphaFold 3 展现出了隐式的化学反应“直觉”。
layer_2_fragments:
  - 共折叠优于传统共价对接
  - 泛化强依赖训练相似性
  - 盲显反应位点是新能力
  - 记忆和规律还没真正分清
layer_3_thesis: AF3在共价复合物上的突破是真实的，但这篇更重要的判断是它的成功仍大量建立在相似性记忆上，因此“会做结构预测”和“会发现新化学”还不是一回事。
status: complete
---

# mp-weixin-qq-com-mzu3mjcymzi5mg-2247493684-1-aps-alphafold-3

## Layer 1 — bold key sentences

- **共折叠方法在预测精度上显著优于传统方法。**
- **共折叠方法的性能仍然高度依赖于测试数据与训练数据的相似性。**
- **AlphaFold 3 展现出了隐式的化学反应“直觉”。**

## Layer 2 — bold fragments

- **共折叠优于传统共价对接**
- **泛化强依赖训练相似性**
- **盲显反应位点是新能力**
- **记忆和规律还没真正分清**

## Layer 3 — one-sentence thesis

AF3在共价复合物上的突破是真实的，但这篇更重要的判断是它的成功仍大量建立在相似性记忆上，因此“会做结构预测”和“会发现新化学”还不是一回事。

## Concepts (tier_1_atoms)

- [[cofolding-beats-covalent-docking]]：在共价复合物结构预测上，共折叠已明显强于传统对接。
- [[similarity-dependent-generalization-in-af3]]：AF3类模型对训练相似性的依赖仍然很高。
- [[blind-reactive-site-hinting]]：即便不给共价约束，模型也可能隐式指出潜在反应位点。

## Back-references

- [[mp-weixin-qq-com-mzkxndizmtcxnw-2247522405-1-nature-machine-intelligence-2025.md]]：那篇把数据泄漏当成药物AI的系统性幻觉来源，这篇给出结构预测版本的具体证据，说明高相似度记忆能把泛化错觉推得很高。
- [[mp-weixin-qq-com-mzkzmty0nzmzng-2247485327-1-pre-antti-j-niemi]]：如果蛋白功能变化真受局部拓扑改革支配，那么AF3目前的短板可能正是没有真正学到这些拓扑事件，只是学到了相似口袋下的构象复写。
- [[mp-weixin-qq-com-mzu0mzm3odu1na-2247487927-1-jacs-proteinmpnn]]：ProteinMPNN说明结构模型可以反过来服务设计，这篇则提醒在把AF3当设计引擎前，必须先分清它学到的是化学规律还是训练集记忆。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzu3mjcymzi5mg-2247493684-1-aps-alphafold-3.md`
- Type: markdown
- Kind: other
