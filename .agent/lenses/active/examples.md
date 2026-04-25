# general-zettelkasten · worked examples

*Two progressive-summaries executed under this lens. Claude reads these
to calibrate voice, Bloom-level honesty, and how concepts surface from
raw material. Wikilinks come in two shapes: (a) plain `[[slug]]` links
resolve to a real file in `seed-kit/general-zettelkasten/` (these are
concepts that have already earned ≥2 independent references); (b) links
tagged `(proposed)` are candidate atoms that a second independent
reference has not yet materialized — they exist in the note body as
signals for future cross-linking, not as promoted concept files. This
is the same honesty protocol the engineering-alexander examples.md
uses.*

---

## Example 1 — Sutton, *The Bitter Lesson* (2019)

### Source
- **Kind**: essay, 1 page
- **URL**: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
- **Author**: Rich Sutton
- **Vault anchor**: `[[sutton-bitter-lesson-2019]]`

### Layer 1 — bold key sentences

> The biggest lesson that can be read from 70 years of AI research is that **general methods that leverage computation are ultimately the most effective, and by a large margin**.

> We have to learn the bitter lesson that **building in how we think we think does not work in the long run**.

> The two methods that seem to scale arbitrarily in this way are **search** and **learning**.

> We want AI agents that can discover like we can, not which contain what we have discovered. **Building in our discoveries only makes it harder to see how the discovering process can be done**.

### Layer 2 — bold fragments

- **general methods that scale arbitrarily with computation**
- **human-knowledge approaches help short-term, plateau long-term**
- **the actual contents of minds are tremendously, irredeemably complex**
- **build in meta-methods, not the discoveries themselves**

### Layer 3 — one-sentence thesis

If a method's success depends on baking in domain knowledge, it trades a short-term edge for a long-term ceiling that Moore's law will always puncture — the durable bets are on search and learning because only those two absorb compute gracefully.

### Concepts surfaced (tier_1_atoms)

- `[[scaling-hypothesis]]` — progress comes from graceful absorption of compute rather than from clever encoding
- `[[search-and-learning]]` — the two primitive operations Sutton identifies as arbitrarily-scaling
- `[[meta-method]] *(proposed)*` — a method that finds methods, as opposed to a method that encodes a known method
- `[[human-knowledge-trap]] *(proposed)*` — the pattern of investing in domain-baked shortcuts that Moore's law eventually overtakes
- `[[bitter-lesson]]` — the name for the whole pattern

Each non-`(proposed)` slug above resolves to a real file in `seed-kit/general-zettelkasten/concepts/`; slugs marked `(proposed)` are candidate atoms awaiting a second independent reference before being promoted to a concept file (per this lens's `concept-two-reference-principle`).

### Bloom level

**Analyze** — the note reconstructs Sutton's pattern (chess → Go → speech → vision) as a single recurrence. Not Evaluate, because I'm not judging it against a rival frame yet; see Layer-3-thesis honesty.

### Concept-cluster candidate

`[[general-methods-vs-domain-knowledge]] *(proposed)*` — groups `[[scaling-hypothesis]]`, `[[search-and-learning]]`, `[[meta-method]] *(proposed)*`, `[[human-knowledge-trap]] *(proposed)*`. Cluster is valid per lens.thresholds.cluster_member_min=3. Spans at least Bloom-levels Understand (what scales) + Analyze (why it scales) — passes the "≥2 Bloom levels" cluster test.

### Back-references (what this unlocks in the vault)

- `[[first-principles-thinking]] *(proposed)*` — Varol's move (strip domain framings, reconstruct from axioms) runs parallel to Sutton's move, but Sutton goes further: don't even trust your *own* first principles if they're still encoded as content. Sutton's bitter-lesson and Varol's first-principles are **not** redundant — they attack the human-centric trap at different layers.
- `[[moores-law]] *(proposed)*` — pre-existing concept; Sutton inverts it from "hardware keeps getting faster" to "stop building anything that can't ride this wave".
- `[[redundancy-as-safety-margin]] *(proposed)*` — interesting negative link: rocket engineering's redundancy ≠ AI research's redundancy. Varol celebrates redundancy for resilience; Sutton would call it human-knowledge encoding that can't scale. Worth a note of its own in the cluster `[[epistemic-humility-under-uncertainty]]`.

### Traps I avoided in this note

- Did **not** paraphrase Sutton's essay (Layer 3 is my own synthesis, not a précis)
- Did **not** inflate `[[search-and-learning]]` into `[[search]] *(proposed)*` + `[[learning]] *(proposed)*` as two separate concepts; they earn the compound slug because Sutton treats them as one primitive pair
- Did **not** tag Bloom=Create (I am not creating new theory here, only analyzing Sutton's)

---

## Example 2 — Varol, *像火箭科学家一样思考*, ch.1 《与不确定性共舞》

### Source
- **Kind**: book chapter
- **Author**: Ozan Varol (奥赞·瓦罗尔, trans.)
- **Chapter**: 第1章 与不确定性共舞
- **Vault anchor**: `[[varol-uncertainty-2020]]`

### Layer 1 — bold key sentences

> 我们对确定性的渴望致使我们追求看似安全的解决方案，也就是**在路灯下寻找钥匙**。

> **"发现的最大障碍，不是无知，而是自以为博学。"** ——Daniel J. Boorstin

> **"我们不能生活在一个永远充满怀疑的状态中。所以我们编造了最好的故事，并把它们当作生活的真相。"** ——Daniel Kahneman

> 只有当我们敢于牺牲确定性答案，敢于冒险，**敢于远离路灯的时候**，才能真正实现突破。

### Layer 2 — bold fragments

- **路灯下找钥匙**（在已知的确定性里反复搜索，而非未知）
- **自以为博学**（illusion of expertise as the real epistemic blocker）
- **为知识真空编造故事**（narrative filling of epistemic voids）
- **不确定性鉴赏家**（treating ambiguity as signal, not noise）

### Layer 3 — one-sentence thesis

对确定性的渴望不是中性的——它把我们锁在已经照亮的区域里反复搜索，而真正的突破要求对自己"为知识真空编造的故事"反向警惕。

### Concepts surfaced (tier_1_atoms)

- `[[drunkard-under-streetlight]]`（路灯下找钥匙）— 识别"在确定性区域内搜索"行为的启发式比喻；不是 Varol 原创（Feynman 讲过），但他首次把它装进认知风险框架
- `[[illusion-of-knowledge]]`（自以为博学）— Boorstin 命名的真正阻碍发现的机制
- `[[narrative-filling]]`（故事填补）— Kahneman 的认知空洞机制；解释为什么阴谋论和迷信能站稳脚跟
- `[[uncertainty-literacy]]`（不确定性鉴赏）— 把模糊性当信号不当噪音的能力

### Bloom level

**Understand** — 我在重构 Varol 的概念框架（醉汉故事 → Boorstin → Kahneman 的逻辑链），还没进入 Apply（把 drunkard-under-streetlight 用到我自己某个决策上）。诚实标注是 Understand 而非 Analyze，因为我还没把 Varol 的框架与其它框架对撞。

### Concept-cluster candidate

`[[epistemic-humility-under-uncertainty]]` — 绑定 `[[drunkard-under-streetlight]]`, `[[illusion-of-knowledge]]`, `[[narrative-filling]]`, `[[uncertainty-literacy]]`. 跨 Bloom-level: Understand (机制是什么) + Evaluate (哪些行为算 narrative filling)，满足 cluster 条件。

### Back-references

- `[[bitter-lesson]]` — Sutton 从方法论层攻击 human-centric 陷阱（"别把你的脑内结构编码到系统里"）；Varol 从认知层攻击它（"别把你对未知的焦虑用故事填满"）。两个方向同宗不同路。这条 back-ref 本身值得独立一条 note: `[[human-centrism-as-epistemic-trap]]`。
- `[[first-principles-thinking]] *(proposed)*` — Varol 第 2 章直接建立在此之上。第 1 章的"远离路灯"是一种阈值准备，为第 2 章的"拆到不可再拆"腾出心理空间。
- `[[redundancy-as-safety-margin]] *(proposed)*` — 第 1 章末尾出现的冗余讨论：冗余不是多余的，它是对"我们知道的不够多"这件事的物理承认。正好和 Sutton 的"别 over-encode"唱反调——同一个 cluster 里的建设性张力。

### Traps I avoided

- Did **not** let 醉汉故事 become its own concept — 它是一个 heuristic，挂在 `[[drunkard-under-streetlight]]` 下；本身不单独成 concept
- Did **not** 对 Boorstin 和 Kahneman 的引用做"权威压重"—— 他们是来源，不是论证。Layer 3 是我的 thesis，不是他们的
- Did **not** 把 Bloom level 打成 Create（我没有创造新理论；我只是在理解 Varol 的框架、准备把它和 Sutton 对撞）

---

## How these examples calibrate Claude's behavior

When a new source arrives under this lens, follow this shape:

1. **Layer 1 bolds verbatim** — never paraphrase in Layer 1. If the source is translated (like Varol here), bold the Chinese as-published; only move to vault-language synthesis in Layer 3.
2. **Layer 2 fragments must carry conceptual weight** — not "interesting phrases". If a fragment doesn't anchor a downstream concept-atom, drop it.
3. **Layer 3 is yours, one sentence, no hedges** — if you need two sentences, the note isn't atomic yet.
4. **Concepts earn their place by appearing in ≥2 notes** — on first ingestion you're *proposing* the atoms; only promote to full concept file after a second independent reference arrives.
5. **Bloom level is observation, not aspiration** — tag what the note *actually does*, not what you wished it did. "Understand" is not a failure grade; it's the truthful state for most notes.
6. **Back-references matter more than forward-links** — each back-ref should be a specific claim ("X and Y attack the same trap at different layers"), not a category bucket ("related to X").

## Anti-patterns these examples guard against

- **The précis trap**: a Layer-3 that restates the author's thesis instead of synthesizing it. Both examples above deliberately *reformulate* the source instead of echoing it.
- **Bloom inflation**: both examples tag themselves honestly (Analyze / Understand), not aspirationally (Create / Evaluate).
- **Concept inflation**: every proposed concept has ≥2 downstream reference targets explicitly named; none are "TODO: populate later".
- **The one-way-link trap**: each note's back-references include at least one *specific* claim about *how* the other note shifts interpretation — not just "related to X".
