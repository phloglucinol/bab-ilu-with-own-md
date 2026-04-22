# Glossary 术语表

> First-class vault reference. Bilingual entries for every core term.
> Extend this file as vault-specific conventions emerge.

## Work · 作品

A specific visual artifact: a painting, a film frame, a UI screenshot, a photograph. In Bab-ilu's bipartite graph, Works are the "concrete" node type; Motifs are the "abstract" type exemplified by Works.

一个具体的视觉作品——某幅画、某一帧、某个 UI 截图、一张照片。在 Bab-ilu 的二部图里，Work 是"具体"一极的节点；Motif 是 Work 所示例的"抽象"节点。

**Examples:** `[[vermeer-milkmaid]]`, `[[deakins-1917-farmhouse-dawn]]`

## Motif · 母题

A named visual operation reusable across Works. Not an adjective, not a style label — an identifiable compositional / perceptual / gestural formula. Motifs are the atoms of Pathosformel.

命名的视觉操作，可跨 Work 复用。不是形容词、不是风格标签——一个可识别的构图/感知/姿势公式。Motif 是 Pathosformel 的原子。

**Examples:** `[[north-light-domestic]]`, `[[contained-silence]]`, `[[manual-labor-sacred]]`

## Pathosformel · 情感公式

(Warburg term.) A cross-era recurring visual-emotional formula — a gesture, compositional tension, or affective formula that migrates, mutates, and resurfaces across centuries and media. In Bab-ilu, Pathosformel is **emergent** (tier 1 `/gap` clustering output), not pre-declared.

（瓦尔堡术语）跨时代反复出现的视觉-情感公式——一种姿势、构图张力或情感配方，在不同世纪和媒介间迁移、变形、重现。在 Bab-ilu 里，Pathosformel 是 tier 1 `/gap` 聚类的**涌现产物**，不是预先声明的。

**Academic source:** Aby Warburg, *Mnemosyne Atlas* (1924–29); Gombrich, *Aby Warburg: An Intellectual Biography* (1970).

## Topos · 视觉类型

(Classical term, plural *topoi*.) A tier-2 emergent cluster: Pathosformel that share motif vocabulary, suggesting a deeper-level visual-philosophical structure. Activated when `|pathosformel| ≥ 15`.

（古典学术语，复数 topoi）Tier 2 涌现聚类——共享 motif 词汇的 Pathosformel 群，暗示更深层的视觉-哲学结构。当 `|pathosformel| ≥ 15` 时自动激活。

## Nachleben · 来世 / 图像之后

(Warburg term.) The "afterlife" of images — visual motifs that resurface in contexts where they historically shouldn't appear. A contemporary film frame may be the Nachleben of a Renaissance fresco.

（瓦尔堡术语）图像的"来世"——视觉母题在历史上本不该出现的语境里重现。一帧当代电影画面可能是文艺复兴壁画的 Nachleben。

## Gap · 结构性空洞

A structural hole in the graph: two clusters of motifs that almost-but-don't connect. Often signals an unexplored tradition or an original creative opportunity.

图谱里的结构性空洞：两组 motif 几乎连上但没连上。往往暗示一个未被探索的传统或原创机会。

## Tier · 聚类层级

Bab-ilu's clustering hierarchy. Tier 1: motif → Pathosformel. Tier 2: Pathosformel → Topos. Extensible to tier 3+ when data density warrants.

Bab-ilu 的聚类层级。Tier 1: motif → Pathosformel；Tier 2: Pathosformel → Topos；数据密度足够时可扩展到 tier 3+。

## Aggregate Node · 聚合节点

Nodes that are outputs of clustering (Pathosformel, Topos). **Excluded from being clustered in subsequent `/gap` runs** to prevent self-cycle.

聚类输出的节点（Pathosformel、Topos）。**从未来 `/gap` 聚类输入中过滤**以防止自循环。

## Vault Language · Vault 语言

The main prose language of this vault, set at `/genesis` in `.agent/CLAUDE.md`. All agent output to user uses this language. Cross-language source material is processed via `/distill` (cognitive reconstruction, not translation).

本 vault 的主体散文语言，在 `/genesis` 时写入 `.agent/CLAUDE.md`。所有 agent 的用户端输出使用此语言。跨语言源材料通过 `/distill` 做认知重构（不是翻译）。

## 认知重构 · Cognitive Reconstruction

When ingesting foreign-language sources, agents **do not translate** — they rewrite meaning using the thinking vocabulary of the vault's language. E.g., "negative space" → "留白" is not a translation but a conceptual repositioning in the Chinese painting tradition.

吸收外文源材料时，agent **不翻译**——用 vault 语言的思维词汇重写意义。例："negative space" → "留白" 不是翻译，是在中国绘画传统里的概念重新定位。

## Seed · 种子条目

Entries imported from Bab-ilu's public-domain seed kit via `/genesis --seeded`. Marked with `seed: true` frontmatter and `#seed` Obsidian tag. Removable any time with `/reset --seeds`.

通过 `/genesis --seeded` 从 Bab-ilu 项目公共种子 kit 导入的条目。带 `seed: true` frontmatter 和 `#seed` 标签。任何时候可 `/reset --seeds` 一键删除。

---

*Add vault-specific terms below as conventions emerge.*
