---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzkzmjc1njk0mq-2247485683-1-fep
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzkzmjc1njk0mq-2247485683-1-fep.md
bloom: analyze
concepts:
  - ml-corrected-fep
  - short-trajectory-sufficiency
  - simulation-postprocessing-loop
  - qm-native-parameterization
layer_1_bolds:
  - "为了解决“高精度但难以实用”的矛盾，作者提出了一套全新的 ML-native 平台——FEP Ω：在标准化、自动化的短时模拟（无 alchemistry、无回环修正）基础上，使用机器学习对模拟产物进行后处理修正，从而在大幅降低计算量与人工调参的同时，保持或超越现有商用实现的预测精度。"
  - "即使在非常短的模拟时间（如 1 ns）下，模型在 RMSE 与 Spearman 排序上已接近或低于 1 kcal/mol，且在多数时间点能达到亚 kcal/mol 误差。"
  - "在 HIF2α 的 scaffold-hopping 试验中（用两套化学系列训练，第三套独立测试），RB FEP 与 AB FEP 均表现稳健：独立测试集 RMSE 从 0.590 降至 0.558 kcal/mol，说明 ML 校正学习到的是系统性偏差而非对 scaffold 的记忆性拟合。"
  - "FEP Ω 通过标准化短时 MD + 基于仿真特征的机器学习后处理，在无需复杂预调参数与 alchemical 网络修正的前提下，实现了与甚至优于现有商用 FEP 实现的预测精度。"
layer_2_fragments:
  - "短时标准化模拟替代长流程工艺"
  - "机器学习学习系统性偏差而非记住 scaffold"
  - "Q-Unity 的第一性原理参数化"
  - "把 FEP 变成后处理校正闭环"
  - "1 ns 也能给出可用排序"
layer_3_thesis: "FEP Ω 把自由能计算的竞争点从“谁更会调炼金协议”改写成“谁能把短时物理轨迹变成可学习、可闭环校正的误差信号”。"
status: complete
---

# mp-weixin-qq-com-mzkzmjc1njk0mq-2247485683-1-fep

## Layer 1 — bold key sentences

- **为了解决“高精度但难以实用”的矛盾，作者提出了一套全新的 ML-native 平台——FEP Ω：在标准化、自动化的短时模拟（无 alchemistry、无回环修正）基础上，使用机器学习对模拟产物进行后处理修正，从而在大幅降低计算量与人工调参的同时，保持或超越现有商用实现的预测精度。**
- **即使在非常短的模拟时间（如 1 ns）下，模型在 RMSE 与 Spearman 排序上已接近或低于 1 kcal/mol，且在多数时间点能达到亚 kcal/mol 误差。**
- **在 HIF2α 的 scaffold-hopping 试验中（用两套化学系列训练，第三套独立测试），RB FEP 与 AB FEP 均表现稳健：独立测试集 RMSE 从 0.590 降至 0.558 kcal/mol，说明 ML 校正学习到的是系统性偏差而非对 scaffold 的记忆性拟合。**
- **FEP Ω 通过标准化短时 MD + 基于仿真特征的机器学习后处理，在无需复杂预调参数与 alchemical 网络修正的前提下，实现了与甚至优于现有商用 FEP 实现的预测精度。**

## Layer 2 — bold fragments

- **短时标准化模拟替代长流程工艺**
- **机器学习学习系统性偏差而非记住 scaffold**
- **Q-Unity 的第一性原理参数化**
- **把 FEP 变成后处理校正闭环**
- **1 ns 也能给出可用排序**

## Layer 3 — one-sentence thesis

FEP Ω 把自由能计算的竞争点从“谁更会调炼金协议”改写成“谁能把短时物理轨迹变成可学习、可闭环校正的误差信号”。

## Concepts (tier_1_atoms)

- `[[ml-corrected-fep]]`：这里真正的新意不是再做一个 FEP 实现，而是把 ML 作为误差修正层叠加在标准化物理模拟之上。
- `[[short-trajectory-sufficiency]]`：短轨迹不再只是“便宜但粗糙”的近似，而被重新定义为足以提供排序与校正信号的数据源。
- `[[simulation-postprocessing-loop]]`：文章把仿真与预测连成闭环，前端负责生成稳定特征，后端负责学习系统性偏差。
- `[[qm-native-parameterization]]`：Q-Unity 说明参数化也被重新定位，不再依赖传统查表经验，而试图把第一性原理直接嵌入流水线起点。

## Back-references

- `[[mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe]]`：OpenFE 把“工业化”理解为默认协议和大规模复现验证；这篇则把“工业化”理解为用 ML 吸收协议残余误差。两篇放在一起，能看见 RBFE 正在从单一路线变成两种工程哲学。
- `[[mp-weixin-qq-com-mzk0mzyxntu0oa-2247487605-1-fep]]`：原子类型编码那篇提醒我，哪怕这里强调“无 alchemistry、少调参”，映射与参数语义仍然不会自动消失；短时模拟想可靠，前处理里关于等价原子的判断仍是硬约束。
- `[[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485036-1-chemical-reviews-2025]]`：如果这篇综述后续补完，它会把 FEP Ω 放回更广的计算药化方法谱系里，让我判断这类 ML 校正究竟是在替代传统 FEP，还是只是在特定 benchmark 上重排成本结构。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzkzmjc1njk0mq-2247485683-1-fep.md`
- Type: markdown
- Kind: other
