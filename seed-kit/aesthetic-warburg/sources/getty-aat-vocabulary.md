---
type: source
seed: true
---

# Getty Art & Architecture Thesaurus（AAT）

> http://vocab.getty.edu/aat/

Getty 艺术与建筑词表。约 55,000 个概念，按七大层面组织：相关概念、物理属性、风格与时期、主体、活动、材料、对象。

1990 年起持续维护。是国际博物馆元数据、学术文献、图像标注数据集、包括 LAION 等 AI 训练数据集的共通词表锚点。

Bab-ilu 的双层锚点架构（`schema.md §6`）要求所有 motif 在有 AAT 匹配时锚定到对应 ID。生成 prompt 时优先使用 AAT 词——这是它们比 Midjourney 风格词更可靠的原因：它们已被四十年的博物馆文献和图像字幕训练到生成模型里了。

## 相关词表（双层锚点同时使用）
- **Iconclass** — 图像主题分类（https://iconclass.org）
- **ULAN** — Getty Union List of Artist Names（http://vocab.getty.edu/ulan）
- **TGN** — Getty Thesaurus of Geographic Names（http://vocab.getty.edu/tgn）

---
*#seed*
