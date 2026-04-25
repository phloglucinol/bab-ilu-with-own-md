---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzu5otu3nzyyoq-2247492421-1-nature-ml
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzu5otu3nzyyoq-2247492421-1-nature-ml.md
bloom: analyze
concepts:
  - "[[posebench-tests-realistic-docking-failures]]"
  - "[[cocfolding-beats-docking-but-still-fragile]]"
  - "[[msa-sensitivity-is-a-hidden-failure-mode]]"
  - "[[structural-accuracy-and-chemical-specificity-trade-off]]"
layer_1_bolds:
  - "**还没有任何研究系统地探讨过最新对接和结构预测方法在以下广泛应用场景中的表现。**"
  - "**作者引入了 PoseBench，这是一个用于广泛应用的蛋白质-配体对接的综合基准测试平台。**"
  - "**深度学习协同折叠方法通常优于可比较的传统和深度学习对接基线算法。**"
  - "**像 AlphaFold 3 这样的流行方法在预测具有新蛋白质-配体结合构象的目标时仍然面临挑战。**"
  - "**深度学习方法难以在结构准确性和化学特异性之间取得平衡。**"
layer_2_fragments:
  - "**真实基准要包含未知结合位点与多配体**"
  - "**协同折叠赢了但没有赢透**"
  - "**MSA 依赖性会让结果不稳定**"
  - "**几何对了不等于化学对了**"
layer_3_thesis: "PoseBench 逼你接受一个不那么舒服的事实：深度学习在对接上已经能超过很多传统基线，但一到未知结合构象、多配体和无结合位点先验这些真实场景，结构正确和化学合理仍经常只能二选一。"
status: complete
---
# 要评估对接方法，就别只挑它最擅长的题做

## Layer 1 — bold key sentences

<!-- Bold verbatim sentences from the source that carry the highest
     conceptual weight. Never paraphrase in Layer 1. -->

- **还没有任何研究系统地探讨过最新对接和结构预测方法在以下广泛应用场景中的表现。**
- **作者引入了 PoseBench，这是一个用于广泛应用的蛋白质-配体对接的综合基准测试平台。**
- **深度学习协同折叠方法通常优于可比较的传统和深度学习对接基线算法。**
- **像 AlphaFold 3 这样的流行方法在预测具有新蛋白质-配体结合构象的目标时仍然面临挑战。**
- **深度学习方法难以在结构准确性和化学特异性之间取得平衡。**

## Layer 2 — bold fragments

<!-- 3–5 conceptual fragments (not 'interesting phrases').
     Each fragment must anchor at least one downstream concept-atom. -->

- **真实基准要包含未知结合位点与多配体**
- **协同折叠赢了但没有赢透**
- **MSA 依赖性会让结果不稳定**
- **几何对了不等于化学对了**

## Layer 3 — one-sentence thesis

<!-- Your synthesis, not the author's thesis. One sentence, no hedges.
     If you need two sentences the note is not atomic yet. -->

PoseBench 逼你接受一个不那么舒服的事实：深度学习在对接上已经能超过很多传统基线，但一到未知结合构象、多配体和无结合位点先验这些真实场景，结构正确和化学合理仍经常只能二选一。

## Concepts (tier_1_atoms)

<!-- Propose concept wikilinks that appear in ≥2 notes.
     Format: `[[concept-slug]]` — explanation of why it earns its place. -->

- `[[posebench-tests-realistic-docking-failures]]`：基准本身就是一套“别自欺”的测试设计。
- `[[cocfolding-beats-docking-but-still-fragile]]`：协同折叠有优势，但优势高度情境化。
- `[[msa-sensitivity-is-a-hidden-failure-mode]]`：输入依赖性是实际部署时的隐性不稳定源。
- `[[structural-accuracy-and-chemical-specificity-trade-off]]`：对接结果常在形状和化学之间拉扯。

## Back-references

<!-- Each back-ref must include a specific claim about HOW the other
     note shifts interpretation of this one — not just 'related to X'. -->

- `[[mp-weixin-qq-com-mzu5otu3nzyyoq-2247489426-1-jctc]]`：ApoDock 之所以要先做条件侧链重排，可以被这篇理解成对 PoseBench 失败模式的一种局部修补，因为很多真实失败正来自非结合态结构的口袋几何偏差。
- `[[mp-weixin-qq-com-mzu5otu3nzyyoq-2247491848-2-jcim-biofusiondti]]`：BioFusionDTI 选择用多模态表示和对接一致性做解释，这篇给它提供了背景：当复合物几何预测本身不稳时，纯几何端到端路线未必比混合路线更可靠。
- `[[mp-weixin-qq-com-mzuymdc1mda2oa-2247489221-1-steven-v-jerome-jctc-glide-ws]]`：Glide WS 在显式水与假阳性控制上做得更细，这篇提醒你即便深度学习大步前进，传统 docking 里那些“水、化学特异性、负样本”问题依然没有消失。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzu5otu3nzyyoq-2247492421-1-nature-ml.md`
- Type: markdown
- Kind: other
