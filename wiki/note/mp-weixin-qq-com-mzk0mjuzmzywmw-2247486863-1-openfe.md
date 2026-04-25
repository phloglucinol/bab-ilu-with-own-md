---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe.md
bloom: analyze
concepts:
  - industrial-grade-open-rbfe
  - default-protocol-as-product
  - mbar-overlap-as-qc-signal
  - pose-quality-bottleneck
layer_1_bolds:
  - "**该研究通过覆盖95个蛋白-配体系统、超1700个配体的严苛验证，证实了开源工具OpenFE的RBFE协议在准确性、 可重复性和吞吐量上已达到工业级应用标准，其 开箱即用 性能比肩商业解决方案，为药物研发领域提供了兼具专业性与开放性的全新选择。**"
  - "**在435个重叠模拟边的对比中，OpenFE的 edgewise RMSE为1.32 kcal/mol，虽略高于手动调参后的FEP+（1.02 kcal/mol），但在配体排序准确率（Kendall's τ）和最佳配体识别率上与FEP+无统计学差异（p=0.25），且无需手动优化参数，更适合高通量部署。**"
  - "**三次独立重复模拟中，公共数据集83.5%的模拟边误差范围小于1 kcal/mol，私有数据集71.7%的模拟边满足该标准；若筛选MBAR重叠度>0.03的收敛模拟边，这一比例分别提升至88.6%和79.5%，高于行业可接受阈值。**"
  - "**针对P38片段数据集的配体对齐优化实验显示，通过RDKit的open3Dalign方法进行形状对齐后，pairwise RMSE从2.06 kcal/mol降至1.52 kcal/mol，证实配体输入姿态质量是影响结果的关键因素，而OpenFE的模块化设计支持集成第三方对齐工具。**"
layer_2_fragments:
  - "**开箱即用的工业级协议**"
  - "**默认参数胜过手工调参依赖**"
  - "**MBAR重叠度作为质量过滤信号**"
  - "**输入姿态质量决定误差下限**"
  - "**模块化流水线允许替换映射与对齐部件**"
layer_3_thesis: "OpenFE 真正证明的不是“开源也能算 FEP”，而是只要默认协议、质控信号和模块接口足够稳，RBFE 就能从高手艺变成可协作扩展的基础设施。"
status: complete
---

# mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe

## Layer 1 — bold key sentences

- **该研究通过覆盖95个蛋白-配体系统、超1700个配体的严苛验证，证实了开源工具OpenFE的RBFE协议在准确性、 可重复性和吞吐量上已达到工业级应用标准，其 开箱即用 性能比肩商业解决方案，为药物研发领域提供了兼具专业性与开放性的全新选择。**
- **在435个重叠模拟边的对比中，OpenFE的 edgewise RMSE为1.32 kcal/mol，虽略高于手动调参后的FEP+（1.02 kcal/mol），但在配体排序准确率（Kendall's τ）和最佳配体识别率上与FEP+无统计学差异（p=0.25），且无需手动优化参数，更适合高通量部署。**
- **三次独立重复模拟中，公共数据集83.5%的模拟边误差范围小于1 kcal/mol，私有数据集71.7%的模拟边满足该标准；若筛选MBAR重叠度>0.03的收敛模拟边，这一比例分别提升至88.6%和79.5%，高于行业可接受阈值。**
- **针对P38片段数据集的配体对齐优化实验显示，通过RDKit的open3Dalign方法进行形状对齐后，pairwise RMSE从2.06 kcal/mol降至1.52 kcal/mol，证实配体输入姿态质量是影响结果的关键因素，而OpenFE的模块化设计支持集成第三方对齐工具。**

## Layer 2 — bold fragments

- **开箱即用的工业级协议**
- **默认参数胜过手工调参依赖**
- **MBAR重叠度作为质量过滤信号**
- **输入姿态质量决定误差下限**
- **模块化流水线允许替换映射与对齐部件**

## Layer 3 — one-sentence thesis

OpenFE 真正证明的不是“开源也能算 FEP”，而是只要默认协议、质控信号和模块接口足够稳，RBFE 就能从高手艺变成可协作扩展的基础设施。

## Concepts (tier_1_atoms)

- [[industrial-grade-open-rbfe]]：这篇的中心不是算法新奇性，而是开源协议第一次通过多药企、多数据源验证，获得“工业可用”的社会性证明。
- [[default-protocol-as-product]]：文章强调的是默认流程本身的价值；能不靠手动调参维持排序与命中识别能力，才叫可部署。
- [[mbar-overlap-as-qc-signal]]：MBAR 重叠度不只是后验统计量，而是筛出“不值得相信的边”的运行时质控信号。
- [[pose-quality-bottleneck]]：P38 对齐实验说明误差不总来自采样或力场，很多时候下限先由输入姿态和映射质量决定。

## Back-references

- [[mp-weixin-qq-com-mzkzmjc1njk0mq-2247485683-1-fep]]：FEP Ω 把价值押在“短时标准化模拟 + ML 后处理”；这篇则说明另一条路也成立，即不引入学习器，只靠稳定默认协议与质控就能接近商用品质。两者把“工业化”的重心放在不同层。
- [[mp-weixin-qq-com-mzk0mzyxntu0oa-2247487605-1-fep]]：原子类型编码与映射策略那篇会改变我对这里“模块化”的理解；模块化不是好看，而是因为映射规则必须跟随力场语义变化，不能被硬编码成单一原理。
- [[mp-weixin-qq-com-mzixmjywota4oq-2247485714-1-drugclip-posebench-immunostruct]]：如果这个结构建模笔记后续补完，它会把这里“输入姿态质量决定误差下限”的观察外推到更广的结构预测链条，说明 FEP 精度常常受制于上游构象生成而不是下游统计收敛。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe.md`
- Type: markdown
- Kind: other
