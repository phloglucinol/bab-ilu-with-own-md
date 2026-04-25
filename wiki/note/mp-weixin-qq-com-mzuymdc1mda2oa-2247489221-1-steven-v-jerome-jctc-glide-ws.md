---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzuymdc1mda2oa-2247489221-1-steven-v-jerome-jctc-glide-ws
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247489221-1-steven-v-jerome-jctc-glide-ws.md
bloom: analyze
concepts:
  - explicit-water-aware-scoring
  - abfep-calibrated-docking
  - false-positive-control-as-primary-metric
  - docking-needs-second-stage-sampling
layer_1_bolds:
  - "大量计算得分靠前的化合物，在实验验证中并未表现出相应的结合活性。"
  - "其重要原因之一，在于传统打分函数对结合口袋中水分子与去溶剂化效应的刻画仍较为粗糙。"
  - "借助绝对结合自由能微扰（absolute binding free energy perturbation，ABFEP）计算进行系统性标定，将WScore发展为经过规则优化和精细调试的物理打分函数Glide WS。"
  - "Glide WS在上述各项指标上均稳定优于Glide SP，不仅显著提升了筛选富集能力，同时有效降低了排名靠前分子的假阳性风险。"
layer_2_fragments:
  - "显式水网络进入打分而不是留给想象"
  - "ABFEP 被拿来给经验规则做物理标定"
  - "假阳性控制比单纯命中率更重要"
  - "高分辨率第二阶段采样用于穿越局部惩罚路径"
  - "对接流程的改进点应落在复筛和重打分层"
layer_3_thesis: "Glide WS 最值得记住的不是又多了一个 docking 分数，而是它把‘降低假阳性’正式当成主目标，并用显式水物理和 ABFEP 标定去重写打分函数该奖励什么、惩罚什么。"
status: complete
---

# mp-weixin-qq-com-mzuymdc1mda2oa-2247489221-1-steven-v-jerome-jctc-glide-ws

## Layer 1 — bold key sentences

- **大量计算得分靠前的化合物，在实验验证中并未表现出相应的结合活性。**
- **其重要原因之一，在于传统打分函数对结合口袋中水分子与去溶剂化效应的刻画仍较为粗糙。**
- **借助绝对结合自由能微扰（absolute binding free energy perturbation，ABFEP）计算进行系统性标定，将WScore发展为经过规则优化和精细调试的物理打分函数Glide WS。**
- **Glide WS在上述各项指标上均稳定优于Glide SP，不仅显著提升了筛选富集能力，同时有效降低了排名靠前分子的假阳性风险。**

## Layer 2 — bold fragments

- **显式水网络进入打分而不是留给想象**
- **ABFEP 被拿来给经验规则做物理标定**
- **假阳性控制比单纯命中率更重要**
- **高分辨率第二阶段采样用于穿越局部惩罚路径**
- **对接流程的改进点应落在复筛和重打分层**

## Layer 3 — one-sentence thesis

Glide WS 最值得记住的不是又多了一个 docking 分数，而是它把“降低假阳性”正式当成主目标，并用显式水物理和 ABFEP 标定去重写打分函数该奖励什么、惩罚什么。

## Concepts (tier_1_atoms)

- [[explicit-water-aware-scoring]]：这篇的核心不是“考虑水”，而是把显式水网络的保留与置换收益真正写入打分规则。
- [[abfep-calibrated-docking]]：ABFEP 在这里不是替代 docking，而是作为更可信的自由能参照去校准经验打分函数。
- [[false-positive-control-as-primary-metric]]：文章把假阳性率控制抬到了和富集能力同等甚至更高的位置，这是很有工业味道的评价重心。
- [[docking-needs-second-stage-sampling]]：高分辨率第二阶段采样说明很多正确姿势需要暂时穿过惩罚路径，单阶段搜索会系统性错过它们。

## Back-references

- [[mp-weixin-qq-com-mzu5otu3nzyyoq-2247489426-1-jctc]]：那篇把侧链重排引入姿势生成阶段，这篇则把显式水和自由能校准引入重打分阶段；两篇合起来能看到 docking 改进到底该放在“采样”还是“评分”哪一层。
- [[mp-weixin-qq-com-mzu5otu3nzyyoq-2247491227-1-angew-chem]]：Angew 那篇解释了为什么某些水不是噪音而是选择性结构件，这正好给 Glide WS 中“显式水该奖励还是该保留”的规则提供物理背景。
- [[mp-weixin-qq-com-mzk0mjuzmzywmw-2247486863-1-openfe]]：OpenFE 代表的是把自由能计算做成默认协议；这篇说明自由能方法还可以反过来服务 docking，不是替代，而是给打分函数做校准教师。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzuymdc1mda2oa-2247489221-1-steven-v-jerome-jctc-glide-ws.md`
- Type: markdown
- Kind: other
