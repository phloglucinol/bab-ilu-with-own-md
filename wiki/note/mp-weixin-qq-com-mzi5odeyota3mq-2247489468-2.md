---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzi5odeyota3mq-2247489468-2
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzi5odeyota3mq-2247489468-2.md
bloom: apply
concepts:
  - "[[symmetry-aware-molecular-descriptors]]"
  - "[[acsf-encodes-local-environment]]"
  - "[[coulomb-matrix-needs-canonicalization]]"
  - "[[distance-angle-features-miss-chirality]]"
layer_1_bolds:
  - "你说得很对，直接将原子坐标作为机器学习的输入特征，确实无法保证平移不变性和旋转不变性。"
  - "为了解决这个问题，我们需要进行特征工程，将原始的几何结构转换成具有不变性的描述符。"
  - "你提到的原子中心对称函数 (ACSF)和库仑矩阵正是两种经典且有效的方案。"
  - "基于距离和角度的描述符（如ACSF）天生无法区分手性分子的对映异构体。"
layer_2_fragments:
  - "别把笛卡尔坐标直接喂给模型"
  - "用距离和角度硬编码对称性"
  - "ACSF 更适合局部环境刻画"
  - "库仑矩阵要靠排序补置换不变"
  - "手性是经典描述符的盲区"
layer_3_thesis: "这篇最值得记住的不是 dscribe 的用法，而是一个更基础的建模纪律：如果输入表示先天不尊重分子的对称性，后面的模型再复杂也只是在拟合坐标系而不是拟合化学。"
status: complete
---

# mp-weixin-qq-com-mzi5odeyota3mq-2247489468-2

## Layer 1 — bold key sentences

- **你说得很对，直接将原子坐标作为机器学习的输入特征，确实无法保证平移不变性和旋转不变性。**
- **为了解决这个问题，我们需要进行特征工程，将原始的几何结构转换成具有不变性的描述符。**
- **你提到的原子中心对称函数 (ACSF)和库仑矩阵正是两种经典且有效的方案。**
- **基于距离和角度的描述符（如ACSF）天生无法区分手性分子的对映异构体。**

## Layer 2 — bold fragments

- **别把笛卡尔坐标直接喂给模型**
- **用距离和角度硬编码对称性**
- **ACSF 更适合局部环境刻画**
- **库仑矩阵要靠排序补置换不变**
- **手性是经典描述符的盲区**

## Layer 3 — one-sentence thesis

这篇最值得记住的不是 `dscribe` 的用法，而是一个更基础的建模纪律：如果输入表示先天不尊重分子的对称性，后面的模型再复杂也只是在拟合坐标系而不是拟合化学。

## Concepts (tier_1_atoms)

- `[[symmetry-aware-molecular-descriptors]]` — 这篇把分子表示的核心约束明确压到平移、旋转、置换不变性上。
- `[[acsf-encodes-local-environment]]` — ACSF 的价值在于把局部化学环境拆成可调的径向与角度指纹。
- `[[coulomb-matrix-needs-canonicalization]]` — 库仑矩阵不是天然完美表示，仍需要排序或填充来补原子置换问题。
- `[[distance-angle-features-miss-chirality]]` — 文章明确点出一个容易被忽略的代价：只靠距离和角度时，镜像异构体会坍缩成同一表示。

## Back-references

- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247483849-1-tmlr-2025-gnn-transformer-3d]]` — 那篇主张标准 Transformer 也能从坐标里学出几何，这篇则提醒若不先处理不变性，直接坐标输入本身就会带来表示歧义；两篇之间的张力正好逼我区分“理论可学”与“工程上该不该这么喂”。
- `[[mp-weixin-qq-com-mzkzmzkxnjq4nw-2247494089-1-nat-comput-sci-if-18-3]]` — qGNN 试图直接从笛卡尔坐标学习承诺函数，这篇会让我回头多问一步：什么任务值得保留原始几何自由度，什么任务更适合先做对称性描述。
- `[[mp-weixin-qq-com-mzg4mta4ntc4mw-2247484032-2-jcim-2025-amp-openadmet-adme]]` — OpenADMET 那篇把手性看作 2D 表示的硬盲区，这篇进一步说明即便到了 3D 手工描述符层，如果仍只靠距离和角度，也一样可能继续看不见手性。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzi5odeyota3mq-2247489468-2.md`
- Type: markdown
- Kind: other
