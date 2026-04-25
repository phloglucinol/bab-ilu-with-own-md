---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mze5odgwota0nq-2247485295-1-pnas-2025-siteaf3-alphafold3
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mze5odgwota0nq-2247485295-1-pnas-2025-siteaf3-alphafold3.md
bloom: analyze
concepts:
  - site-specific-folding
  - conditional-diffusion-docking
  - msa-bias-masking
  - structure-first-affinity-later
layer_1_bolds:
  - "SiteAF3是一种基于AF3并采用条件扩散策略实现位点特异折叠的新方法。"
  - "SiteAF3通过固定受体结构并可选地引入结合口袋与热点残基信息，从而优化扩散过程。"
  - "SiteAF3在蛋白–小分子、蛋白–肽段、双链DNA与RNA的复合物预测中均稳定优于AF3。"
  - "口袋引导可有效消除MSA模板中隐藏的偏差。"
layer_2_fragments:
  - "固定受体、只更新配体坐标"
  - "口袋与热点信息进入MSA"
  - "对全长MSA做口袋mask以消除错误位点偏置"
  - "低置信度样本也能拉高准确率"
  - "显存下降使高通量筛选可行"
layer_3_thesis: "SiteAF3真正提出的不是一个更强的AF3变体，而是一种把“先决定在哪个口袋折叠”写进扩散过程里的结构控制接口，因此它同时改善准确率、鲁棒性和算力成本。"
status: complete
---

# mp-weixin-qq-com-mze5odgwota0nq-2247485295-1-pnas-2025-siteaf3-alphafold3

## Layer 1 — bold key sentences

- **SiteAF3是一种基于AF3并采用条件扩散策略实现位点特异折叠的新方法。**
- **SiteAF3通过固定受体结构并可选地引入结合口袋与热点残基信息，从而优化扩散过程。**
- **SiteAF3在蛋白–小分子、蛋白–肽段、双链DNA与RNA的复合物预测中均稳定优于AF3。**
- **口袋引导可有效消除MSA模板中隐藏的偏差。**

## Layer 2 — bold fragments

- **固定受体、只更新配体坐标**
- **口袋与热点信息进入MSA**
- **对全长MSA做口袋mask以消除错误位点偏置**
- **低置信度样本也能拉高准确率**
- **显存下降使高通量筛选可行**

## Layer 3 — one-sentence thesis

SiteAF3真正提出的不是一个更强的AF3变体，而是一种把“先决定在哪个口袋折叠”写进扩散过程里的结构控制接口，因此它同时改善准确率、鲁棒性和算力成本。

## Concepts (tier_1_atoms)

- `[[site-specific-folding]]` — 这篇把“复合物预测”从整体共折叠改写成“在既定口袋里完成折叠”，是后面理解 DREAM 与 Boltz2 的共同参照。
- `[[conditional-diffusion-docking]]` — 关键不是普通扩散，而是把口袋中心、固定受体和局部更新三件事合成一个条件化对接过程。
- `[[msa-bias-masking]]` — 文章指出 MSA 既提供先验也带来错误位点偏置，口袋 mask 的价值在于抑制这种隐性误导。
- `[[structure-first-affinity-later]]` — SiteAF3优先解决“结构放对”，并在结论里显式把亲和力模块留给其他框架拼接，适合与 Boltz2 对照。

## Back-references

- `[[mp-weixin-qq-com-mjm5mtcymtq5oq-2647507459-1-boltz2]]` — 这篇会把 Boltz2 看成“把评分体系和推理旋钮公开化”的框架；回看 SiteAF3，就会更清楚它的创新点不在评分，而在把位点约束嵌入生成过程本身。
- `[[mp-weixin-qq-com-mzkyntmznzm3nq-2247483762-1-af3-dream-20-35-ai]]` — DREAM 把 AF3 反转成设计器，SiteAF3 则把 AF3 改造成受口袋条件支配的结构生成器；两者一起说明 AF3 时代真正稀缺的不是更大的模型，而是可控接口。
- `[[mp-weixin-qq-com-mze5odgwota0nq-2247486046-1-acs-cent-sci-2026-prompt-drug]]` — 如果 prompt-based 药物设计强调“用语言指定目标分子性质”，那 SiteAF3 补上的就是更硬的几何约束层：性质提示不够，口袋位置也要进入生成闭环。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mze5odgwota0nq-2247485295-1-pnas-2025-siteaf3-alphafold3.md`
- Type: markdown
- Kind: other
