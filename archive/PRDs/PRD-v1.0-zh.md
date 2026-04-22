# Bab-ilu — 为 AI 创作时代设计的美学知识系统

> **PRD v1.4** | 2026-04-16 (additive 扩展自 v1.3 同日早盘)
> **形态**：基于 [skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki) v0.1.0 的硬 fork,独立演化。
> OmegaWiki 提供学术研究 pipeline 基座；Bab-ilu 的差异化在**带学术血统的高质量创作提示词**——当用户做 UI 设计、生成图像、生成视频、规划 UX 流程、研究绘画传统时,Bab-ilu 产出有考据、有来源、可追溯的提示词和卡片,而非通用风格标签堆砌。
>
> **v1.4 新增**（见 `archive/MIGRATIONS/1.3-to-1.4.md`）：
> - **三轴对齐**（Karpathy UX + OmegaWiki 学术落地 + 多从业者覆盖）
> - 域枚举 +`ux` + `painting`
> - 受控词表三元组 AAT + Wikidata + **Iconclass**
> - 16 个可选博物馆/机构 ID 字段
> - 3 个可选 prompt 模态 `ux_flow` / `painting` / `motion`
> - §11 硬规则：每张 aesthetic / panel 至少一个权威字段非空
> - `wiki/_refs/` 权威参考骨架（3 spine + 10 institutions + 9 domains = 22 条 canonical）
> - `wiki/index.md` + `wiki/log.md` Karpathy primitives
> - 18 个 OmegaWiki 学术 skill + MCP `llm-review` + 10 Python tools + 33 tests + daily-arxiv cron 物理落地
>
> 三条硬约束:**Karpathy 三层架构**(`raw/` · `wiki/` · `schema.md`)、**万物皆 Markdown**、**学术血统重档且用户零成本**。

---

## 0. 核心定位

Bab-ilu 是一个**为 AI 创作时代设计的美学知识系统**。

当用户在终端运行 `/taste` 分析一张参考图、或在 Obsidian 中打开一张 Aesthetic 卡片时,他看到的是:
- 结构化的美学分析(Panofsky 三层)
- 跨时空的视觉母题归属(Warburg Nachleben / 图像后世)
- 可直接粘贴到 Midjourney / Flux / Nano Banana / Runway / Sora / Kling 的**高质量提示词**
- 每个提示词都声明其学术出处(Getty AAT 术语、Warburg 面板、签名作者)

**美学考古(TASTE)是引擎,学术锚点(Warburg / Panofsky / Getty AAT)是血统来源,提示词是最终交付物。**

分析与考古是手段。**更好的生成输出是目的。** 系统中每一个机制都必须以这个目的为准绳进行验证。

---

## 1. 产品概览与愿景

### 1.1 Bab-ilu 是什么

Bab-ilu 是一个基于 Obsidian、人与 agent 共同进化的美学知识框架。用户 clone 仓库,运行 `/genesis`,所有已安装的 AI agent(Claude Code、Hermes、Codex、OpenClaw 等)自动接入共享的结构化知识库。

框架在两个层面运作:
- **运行时**:用户做 UI 设计 / 生图 / 生视频时,agent 生成带学术血统的提示词并写入 Aesthetic 卡片。用户也可用 `/ask` 跨 vault 查询。
- **进化**:通过反复使用、生成回测、用户策展,知识库与 agent 的效能随时间复利增长;经过验证的提示词被提升为可复用的配方。

用户往 `raw/` 里丢素材(图、视频、链接、笔记),Agent 负责组织、交叉链接、生成提示词、追踪学术出处。真正的平台是文件系统(markdown + YAML frontmatter);Obsidian 是推荐的查看器。

### 1.2 为什么要做

Andrej Karpathy 的 LLM Wiki 模式证明了一件事:LLM 擅长知识簿记——整理、链接、维护知识库的繁琐活儿。[OmegaWiki](https://github.com/skyllwt/OmegaWiki) 已经把"学术研究 pipeline"这条路跑通:8 实体、23 skill、2263 测试、完整的学术闭环。

但在 AI 生成内容(AIGC)已经成为设计与影像主流工具的当下,仍然有一整块盲区:

1. **提示词依然是通用风格标签堆砌**——"cinematic, moody, teal and orange"的套路。通用标签在 Midjourney v6+、Flux、Sora、Kling 这代生成模型面前,输出模糊、同质、缺乏作者性。
2. **美学知识没有结构化知识基础**——OmegaWiki 的 schema 是为文字知识而建的,图像在 wiki 中只是被引用的 source,无法作为被结构化理解与复用的知识。
3. **母语用户的认知重构缺失**——OmegaWiki 通过 `setup.sh --lang=zh` 翻译了 agent 指令(L1 本地化),但知识内容本身仍以 LLM 临时选择的语言写成。对需要用母语构造 mental model 的用户来说,这只是"指令本地化",不是"知识本地化"。

Bab-ilu 不重写 OmegaWiki,而是**在它之上叠两层**:
- **美学考古与创作提示词(TASTE)**——核心差异化
- **认知重构式的母语化(L2 本地化)**——辅助差异化

### 1.3 与基底(OmegaWiki)及同类方案的关系

> **定位**:OmegaWiki 不是竞争对手,而是 Bab-ilu 的基底。
> 以下表格分两行对照:第一部分为继承能力,第二部分为 Bab-ilu 的 delta。

| 层 | 能力 | OmegaWiki v0.1.0 基底 | Bab-ilu 叠加 |
|---|------|----------------------|--------------|
| Schema | 实体类型 | 8(papers/concepts/topics/people/ideas/experiments/claims/summaries) | +2(aesthetic / prompt)+ question = **11** |
| Schema | 关系类型 | 9 | +3(applies / exemplifies / frames)= **12** |
| Skill | 研究生命周期 skill | 23(完整科研流程) | 继承 21,重命名 2(`/init → /genesis`、`/daily-arxiv → /daily-feed`),移至附录 |
| Skill | 核心命令 | — | **7 个 Bab-ilu 核心命令**(genesis / ingest / ask / taste / distill / check / prompt),另加可选 panel / glossary |
| Agent | 多 agent 支持 | 主 Claude Code | Claude Code + Hermes 为主,Codex/OpenClaw/Cursor/Gemini 尽力支持 |
| 语言 | 本地化层次 | L1:agent 指令翻译 | L2:知识内容母语重构 + 双语术语锚 + `/glossary` 治理 |
| 视觉 | 视觉 / 美学知识 | 无结构化支持 | Aesthetic 实体 + 3–5 taste-* subagent + Warburg 面板库 |
| 创作 | 生成提示词 | 无 | **三模态提示词自动生成(UI / image / video)**,含 Panofsky 三层骨架 + AAT 术语锚 + Warburg 面板引用 |
| 学术 | 学术锚点 | 学术 citation 图 | +Warburg Nachleben + Panofsky 三层图像学 + Getty AAT / Wikidata 外部锚 |

**学术对标**(不是同类方案,是 Bab-ilu 进入的学术生态位):

| 对标 | 意义 |
|------|------|
| [Warburg Institute Mnemosyne Atlas 数字化版](https://warburg.sas.ac.uk/archive/archive-collections/mnemosyne-atlas) | Aby Warburg 1924–29 的图像考古原典——Bab-ilu 的 Warburg 面板直接继承这一传统 |
| [Getty AAT](http://vocab.getty.edu/aat/) | 55,000 概念的受控艺术/建筑词表,四十年积累——Bab-ilu 的 Aesthetic frontmatter 引用 AAT ID |
| [Wikidata LOD](https://www.wikidata.org/) | 全球链接开放数据——Bab-ilu 通过 wikidata QID 字段参与 LOD federation |
| [Panofsky 图像学三层](https://en.wikipedia.org/wiki/Iconology) | 1939 年定义的视觉解释方法论——Bab-ilu 提示词骨架直接对应三层 |

**其他同类知识框架**(功能相近的参考点,不是基底):

| 项目 | 形态 | 与 Bab-ilu 的关系 |
|------|------|---------------------|
| [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | 多 agent skill 架构的最小实现 | 借鉴 setup 思路,无直接继承 |
| [MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki) | L1/L2 缓存架构 | 思想启发,实现不继承 |
| [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | 原始模式定义(raw / wiki / schema 三层) | **哲学基底**,Bab-ilu 核心架构与其对齐 |

### 1.4 目标用户

- **主用户**:做 UI 设计、AI 生图、AI 生视频的设计师、导演、视觉从业者——他们需要高质量提示词
- **次用户**:每天使用 AI 编程 agent 并管理个人知识库的开发者、研究者
- **次用户**:消费英文内容的非英语用户(通过 L2 本地化获益)

### 1.5 分发方式

开源仓库。用户 clone、运行 setup、开始使用。无云依赖。Obsidian 是查看器,文件系统是数据库,agent 是工人。

### 1.6 平台哲学 —— Karpathy 三层

Bab-ilu 的真正平台是文件系统,严格对齐 Karpathy LLM Wiki 模式的三层架构:

| 层 | 目录 | 所有者 | 可变性 |
|---|------|-------|--------|
| Raw sources | `raw/` | 用户 | 不可变,LLM 永不修改 |
| Knowledge | `wiki/` | LLM | LLM 写入与维护,用户可策展 |
| Conventions | `schema.md`(项目根) | LLM 读,人类项目负责人编辑 | 仅在明确决策下变更,版本化 |

**任何提议的新机制必须能落到三层之一,否则砍。** 这是 v1.3 对 v1.2 的主要位移——v1.2 的 L0/L1/L2 token 分层不属于三层中的任何一层,被移除。

Markdown 文件 + YAML frontmatter 是规范数据格式。Obsidian 是推荐查看器,但不是依赖项。系统必须在仅有 agent 的情况下完全可用,不需要任何 Obsidian 专属功能。

任何会产生 Obsidian 绑定的功能(插件 API、Obsidian URI scheme、Obsidian 专属元数据)都需要明确论证,且必须提供回退路径。所有关系数据存在 frontmatter YAML 中。行内 wikilink 是为 Obsidian 图谱视图生成的便利产物,不是权威数据源。

### 1.7 为什么 Bab-ilu 经得住 LLM 进化

随着上下文窗口增长、模型获得原生持久记忆、生成模型质量指数提升,外部知识结构的必要性似乎在减弱。但 Bab-ilu 有四层持久价值:

1. **多 agent 一致性。** 模型原生记忆是 per-agent 的。Bab-ilu 是 Claude、Hermes、Codex 以及未来任何新 agent 之间的共享知识层。没有任何单一模型的记忆能解决这个问题。
2. **用户所有权与可移植性。** 模型托管的记忆是被平台锁定的。换了供应商,知识跟着 Bab-ilu 走,不跟模型走。
3. **可审计性与溯源。** 文件系统上的知识有 diff 和溯源链。生成的每个提示词都带学术出处(Warburg / Panofsky / AAT / Wikidata),可追溯、可反驳。模型托管的记忆是黑箱。
4. **提示词质量与生成模型解耦。** 生成模型每半年换一代,通用提示词技巧随之过时;但学术锚点(Warburg 母题、Panofsky 层次、AAT 术语)是视觉文化的结构常量,跨代有效。Bab-ilu 赌这条常量。

### 1.8 Upstream 关系(Fork 策略)

Bab-ilu 是 OmegaWiki v0.1.0 的**硬 fork,独立演化**。不定期 merge upstream。

**为什么是硬 fork 而不是跟踪式 fork**:
- Bab-ilu 的差异化在美学创作与学术血统,需要改动 schema(新增 aesthetic/prompt 实体)、重写核心命令集、新增 `.claude/agents/` 与 `wiki/_panels/` 等结构,这些改动与 OmegaWiki 的学术研究取向不同向,回并不可期
- 命名优先级:`/init → /genesis` 等重命名体现 Bab-ilu 自身身份,不为 upstream 合并妥协
- 两条演化路径分开走:OmegaWiki 深化学术 pipeline,Bab-ilu 深化美学与创作

**实践含义**:
- Bab-ilu 自由改写任何继承自 OmegaWiki 的文件,无需考虑合并冲突
- 继承的 Python 基础设施(`tools/research_wiki.py` 20 CLI、`mcp-servers/`、`tests/` 2263 测试)作为 Bab-ilu 的**内部实现依赖**维护,不进主叙事,不作卖点
- OmegaWiki 后续的新 skill 或 schema 改动,按 case-by-case 评估是否**移植**(不是 merge)
- `references/OmegaWiki/` 保留为历史参考快照

**记录基线 commit**:发布 v1.0 前,在 `docs/UPSTREAM.md` 中记录 fork 时 OmegaWiki 的 commit SHA。

### 1.9 学术血统宣言

Bab-ilu 明确继承三条美学学术血脉作为 TASTE 引擎的基因:

**1. Aby Warburg — Mnemosyne Atlas(1924–1929)与 Nachleben 原则**
> 视觉母题不属于单一时代或作者;它们跨世纪迁徙、变异、再现。

Warburg 的未完成图像档案由约 63 张黑色面板组成,每张面板并置分属不同媒介与时代的图像,追踪共享的视觉姿态、构图张力或情感程式(*Pathosformel*)。Bab-ilu 的 Warburg 面板(`wiki/_panels/`)是这一传统在 LLM 时代的数字化延续——也是生成端最有力的"在传统中创作"工具。

**2. Erwin Panofsky — Studies in Iconology(1939)三层图像学**
> 前图像志(pre-iconographic)→ 图像志(iconographic)→ 图像学(iconological)

Panofsky 定义的三层视觉解释,是 Bab-ilu 提示词骨架的直接来源。高质量的图像 / 视频提示词必须同时涵盖三层——这不是装饰性引用,而是让 Midjourney v6+、Flux、Sora、Kling 等生成模型真正响应的结构。

**3. Getty AAT + Wikidata + Iconclass(v1.4 加入)— 受控词表三元组**
> Getty AAT: 55,000 艺术与建筑概念,四十年维护历史。
> Wikidata: 1 亿 Q 实体,链接开放数据中枢。
> **Iconclass(v1.4 新增)**: Leiden 1973, Henri van de Waal 创立,Warburg–Panofsky 图像学方法的**直接后裔分类系统**,覆盖"画面描绘什么"的主题内容。欧洲主要博物馆 Rijksmuseum / Prado / KHM / British Museum 全部使用。

AAT 术语在生成模型训练集里大量出现(通过博物馆元数据、Wikipedia、LAION 图注流入),这意味着 **AAT + Iconclass 锚定的提示词比民间风格标签产出更具体** 。Bab-ilu 的 Aesthetic 实体同时引用 AAT ID(风格/材料)、Iconclass notation(叙事主题)、Wikidata QID(实体链接),自动获得 LOD 互操作性。v1.4 还加入 16 个可选的博物馆/机构 ID 字段(Met / MoMA / Cooper Hewitt / Rijks / Tate / NGA / BFI / Magnum / Archnet / RIBA / LoC / GCD / MobyGames / IGDB / ISO / NN/g),让每张 aesthetic 卡可以指向制度性权威存档。

**重档承诺(v1.4 硬规则)**:每个 Aesthetic MD 正文末尾自动生成"学术溯源"小节,明示 Warburg 面板、Panofsky 层、AAT ID、**Iconclass notation**、Wikidata QID、机构 ID——对学者可读,对普通用户可忽略,对 Bab-ilu 自身则是诚信承诺。**每张 aesthetic / panel 至少有一个权威字段非空**(`aat_id` / `wikidata` / `iconclass` / `ulan_id` / 任一博物馆 ID / `iso_standard` / `nng_url`),由 `/check` Category 10 强制审计。

---

## 2. Schema 设计

完整 schema 定义见项目根 `schema.md`——LLM 在每次会话读取,用户不读。本节为摘要。

### 2.1 实体类型(11 种)

| 类型 | 继承自 OmegaWiki | 描述 |
|------|--------------|------|
| `source` | yes | 任何带溯源信息的摄入材料:论文、文章、视频、播客、代码仓库、图像集 |
| `concept` | yes | 命名的、已建立的知识单元。理解的原子构件。`role` metadata 承担方法论/哲学/基础/问题等语义 |
| `topic` | yes | 将其他实体分组的广泛主题领域 |
| `person` | yes | 作者、研究者、艺术家、导演、设计师 |
| `idea` | yes | 推测性、未验证的想法。`maturity`:seed / developing / mature / failed |
| `experiment` | yes | 可重现的试验,带过程与结果 |
| `claim` | yes | 可证伪的命题 |
| `summary` | yes | 压缩概览 |
| `question` | yes | 开放问题、知识缺口 |
| `aesthetic` | **新增** | 视觉/美学单元:风格、运动、签名、母题。TASTE 核心。自动生成三模态提示词 |
| `prompt` | **新增** | 可复用、经验证的提示词配方,由用户从 Aesthetic MD 自动生成提示词中提升而来。`wiki/_prompts/` |

**合并说明**:v1.2 的 Methodology / Prompt / Philosophy / Foundations 已合并处理。Methodology / Philosophy / Foundations 作为 `concept` 的 `role` metadata,不独立成实体。Prompt 因其一等公民创作输出性质,独立为 `prompt` 实体。

### 2.2 关系类型(12 种)

OmegaWiki 继承 9 种:`extends` · `contradicts` · `supports` · `inspired_by` · `tested_by` · `invalidates` · `supersedes` · `addresses_gap` · `derived_from`

Bab-ilu 新增 3 种:
- `applies` — 抽象被应用于具体(方法论 → 实验/摘要)
- `exemplifies` — 具体是抽象的实例(实验 → 概念,Aesthetic → Warburg 面板)
- `frames` — 哲学或美学透镜为理解提供框架

**v1.2 删除**:`composes` / `categorized_by` / `authored_by` 因与其他关系或 frontmatter 字段重叠被删除。作者归属由 frontmatter `authors:` 承担,不是关系。

### 2.3 Frontmatter 契约

**通用字段**(所有实体):

```yaml
---
id: kebab-case-slug
type: <entity type>
title: Display title
aliases: [alt names]
language: en | zh | ...
original_terms:                # 双语锚,遵循 Getty AAT 多语言约定
  - term: <foreign term>
    lang: <lang code>
freshness_class: evergreen | stable | volatile | dated
confidence: 0.0–1.0
last_validated: YYYY-MM-DD
schema_version: 1.3.0
relations:
  - {type: <relation>, target: [[wikilink]]}
---
```

**Aesthetic 专属字段**:

```yaml
type: aesthetic
aat_id: "300015650"                    # Getty AAT 概念 ID,LLM 自动填
aat_uncertainty: null                  # 不确定时记候选:"candidate:300020000, reason: ..."
wikidata: "Q4692"                      # Wikidata QID,LLM 自动填
wikidata_uncertainty: null
warburg_panel: [[[panel-id]]]          # 所属 Warburg 面板
panofsky_layer: pre_iconographic | iconographic | iconological
domain: cinema | photo | ui | graphic | game | architecture   # soft hint
prompts:                               # LLM 自动生成,三模态
  ui:    {generated, last_tested, test_score}
  image: {generated, last_tested, test_score, compatible_models: [midjourney | sd | nano-banana | flux | ...]}
  video: {generated, last_tested, test_score, compatible_models: [runway | sora | kling | pika | ...]}
```

**Prompt 专属字段**(独立 `type: prompt` 实体):

```yaml
type: prompt
modality: ui | image | video
promoted_from: [[aesthetic-wikilink]]
compatible_models: [verified-compatible generators]
panofsky_structure: true | false
aat_anchors: [<aat-id>, ...]
warburg_panels: [[[panel-wikilinks]]]
usage_count: <integer>
tested_runs:
  - {date, model, score, note}
```

其他实体(source / experiment / panel 等)的扩展字段见 `schema.md`。

### 2.4 关系存储

**权威源**:frontmatter YAML。
**生成产物**:
- `_index/edges.jsonl` — 双向边索引,惰性构建(查询时按需重建并缓存)
- 条目底部 `## Relations` 部分的 `[[wikilinks]]` — 写入时从 frontmatter 生成,供 Obsidian 图谱视图使用

**写入安全性**:所有 vault 写入使用原子操作(临时文件 + 重命名)。Frontmatter 写入前必须通过 schema 验证。完全重建的索引文件是单写者的。

### 2.5 Schema 演进策略

**仅增量**:添加新实体类型或字段始终可选;废弃类型在 `schema.md` 中标记 deprecated;移除类型或必填字段需大版本升级并附迁移指南。Bab-ilu 当前 `schema_version: 1.3.0`。

---

## 3. 核心命令集

> **Fork lens**:OmegaWiki v0.1.0 提供 23 skill 作为继承基座。v1.3 将 Bab-ilu 的核心命令缩到 **7 个**(+2 可选),将 OmegaWiki 的 21 个学术生命周期 skill 整体移至附录 §3.A。
>
> | 来源 | 数量 | 备注 |
> |------|-----|------|
> | **Bab-ilu 核心命令** | 7 | `/genesis` `/ingest` `/ask` `/taste` `/distill` `/check` `/prompt` |
> | Bab-ilu 可选命令 | 2 | `/panel` `/glossary` |
> | OmegaWiki 继承(附录) | 21 | 学术科研闭环,按 case 启用,见 §3.A |
> | OmegaWiki 重命名(附录) | 2 | `/init → /genesis`、`/daily-arxiv → /daily-feed` |

### 3.1 核心命令(7 个)

| # | 命令 | 描述 |
|---|------|------|
| 1 | `/genesis` | 初始化 vault 三层结构(`raw/` · `wiki/` · `schema.md`),检测已安装 agent 并创建 symlink,输出下一步提示 |
| 2 | `/ingest` | 摄入 `raw/` 中的任何素材(URL / PDF / 图片 / 视频 / 文本),自动触发 `/compile`(实体提取 + 关系)和 `/distill`(如果需要母语重构)。`--panel` 触发 Warburg 面板综合。 |
| 3 | `/ask` | 跨 vault 查询,综合回答并附条目链接。支持 `--depth hook | summary | full` |
| 4 | `/taste` | 美学考古入口:接收视觉素材,调度 3–5 taste-* subagent,产出 Aesthetic MD(含三模态提示词 + 学术溯源)。详见 §5.2 |
| 5 | `/distill` | 英文来源 → 母语知识卡片。认知重构,保留术语双语锚。详见 §5.5 |
| 6 | `/check` | 健康审计:schema 一致性、未解 AAT ID、学术溯源缺失、提示词测试过期、断链、过期内容、孤儿页。详见 §9 |
| 7 | `/prompt` | 从 Aesthetic wikilink 或 Warburg 面板按指定模态(ui/image/video)重新生成或提升提示词。提升为 `type: prompt` 独立实体时记入 `wiki/_prompts/` |

### 3.2 可选命令(2 个)

| # | 命令 | 描述 |
|---|------|------|
| 8 | `/panel` | 主动创建或编辑 Warburg 面板。多数面板由 `/ingest --panel` 自动产生,此命令供用户显式策展 |
| 9 | `/glossary` | 管理双语术语映射表(`wiki/_glossary.md`)。首次出现 `注意力机制 (Attention Mechanism)`,之后 `注意力机制` |

### 3.A 附录:OmegaWiki 继承的学术科研命令(21 个)

这些命令继承自 OmegaWiki v0.1.0 基底,服务于学术研究闭环(文献扫描 → 新颖性检查 → 想法生成 → 实验设计 → 论文撰写 → 同行评审)。Bab-ilu 不重述其设计,仅链接到 OmegaWiki 原文档。

| 类别 | 命令 |
|------|------|
| 核心管道(OmegaWiki 原有) | `/setup` `/compile` `/cross-link` `/export` `/reset` `/status` `/edit` `/refine` |
| 研究发现 | `/research` `/survey` `/novelty` `/ideate` `/daily-feed`(重命名自 `/daily-arxiv`) |
| 实验生命周期 | `/exp-design` `/exp-run` `/exp-eval` `/exp-status` |
| 知识产出 | `/paper-plan` `/paper-draft` `/paper-compile` `/rebuttal` `/review` `/prefill` |

**v1.3 从 v1.2 删除的命令**:
- `/lineage`(v1.1 定义)→ 下沉到 `taste-lineage` subagent 内部机制,不是命令
- `/lens`(v1.1 定义)→ 由 3–5 个 taste-* subagent 取代
- `/mood-board` → 面板(panel)机制覆盖,收益低于维护成本

---

## 4. 架构

### 4.1 Karpathy 三层架构

```
Bab-ilu/                         # 仓库根
├── raw/                         # 【第 1 层】不可变原料(用户所有)
│   ├── articles/
│   ├── images/                  # 用户拖入的参考图、截图
│   ├── videos/
│   └── papers/
├── wiki/                        # 【第 2 层】知识(LLM 所有)
│   ├── aesthetics/              # Aesthetic 实体(带三模态提示词 + 学术溯源)
│   │   ├── cinema/
│   │   ├── photo/
│   │   ├── ui/
│   │   └── ...
│   ├── _panels/                 # Warburg 面板(跨时空视觉母题)
│   ├── _prompts/                # 提升为独立实体的可复用提示词
│   ├── _evals/                  # 评估样本(~120 条,6 领域 × 20)
│   ├── _glossary.md             # 双语术语治理单文件
│   ├── ml/ · engineering/ · ... # 其他领域文件夹,随用户添加内容生长
│   ├── _index/                  # 自动生成索引
│   │   ├── entry-index.yaml
│   │   └── edges.jsonl          # 惰性构建
│   └── _log/
│       └── usage.jsonl          # 追加日志
└── schema.md                    # 【第 3 层】约定 + 学术锚点 prompt(LLM 读)
```

**内部实现依赖**(不属于三层,不入主叙事):

```
.claude/
├── skills/                      # 7 核心命令 + 可选命令定义
└── agents/                      # 3–5 taste-* subagent 定义
.agents/skills/                  # Symlink,供 OpenClaw/Hermes 等
tools/                           # OmegaWiki 继承的 Python 工具集
mcp-servers/                     # OmegaWiki 继承
tests/                           # OmegaWiki 继承(2263 测试)
i18n/                            # OmegaWiki 继承(L1 agent 指令翻译)
docs/UPSTREAM.md                 # Fork 基线 commit SHA
requirements.txt                 # Python 依赖
setup.sh                         # 一键 setup
CLAUDE.md                        # Claude Code 项目 schema
```

### 4.2 Vault 组织

文件按**领域**(用户视角,直觉)组织,不按实体类型:

```
wiki/
├── ml/
│   ├── attention-mechanism.md      ← type: concept
│   └── transformer-paper.md        ← type: source
├── aesthetics/
│   ├── cinema/
│   │   └── wong-kar-wai-chromatic-nostalgia.md   ← type: aesthetic
│   ├── ui/
│   │   └── bauhaus-ui-legacy.md                  ← type: aesthetic
│   └── ...
└── _panels/
    └── saturation-as-memory.md                   ← type: panel
```

实体类型存在 frontmatter `type:` 字段。领域不预设——随用户添加内容自然生长。

### 4.3 双语内容架构

**方案 C:单语文件 + 双语术语锚 + `/glossary` 治理。**

- 文件用用户母语书写
- 英文来源通过 `/distill` 后才进入 wiki
- 母语来源直接通过 `/compile`
- frontmatter 的 `original_terms` 字段存储双语映射,遵循 Getty AAT 的多语言约定(equivalent terms across languages while preserving a canonical ID)
- 搜索索引包含两种语言
- 原始来源材料保存在 `raw/` 供溯源

**定位校正**:v1.2 曾将"母语作为一等公民"写为与 OmegaWiki 的核心差异,经审计后发现 OmegaWiki 已有 L1 本地化(通过 `setup.sh --lang=zh`)。Bab-ilu 的实际 delta 是 **L2 知识内容认知重构**,不是"填 L1 空白"。v1.3 据此降调定位。

**提示词语言特例**:生成模型(Midjourney / Flux / Sora / Kling)训练集以英文为主,AAT 官方术语也是英文。因此 Aesthetic MD 自动生成的提示词主体保留英文,MD 散文可以是中文。这让中文用户可以读懂解释,同时把机器能用的提示词原汁原味交给生成模型。

### 4.4 多 Agent 支持

**主要目标**:Claude Code、Hermes。
**尽力支持**:Codex、OpenClaw、Cursor、Gemini。

一套 skill 源文件。`setup.sh` 检测已安装的 agent 并创建 symlink:

```
Claude Code  → .claude/skills/
Hermes       → (Hermes skill path)
Codex        → ~/.codex/skills/
OpenClaw     → .agents/skills/
Cursor       → .cursor/skills/
Gemini       → ~/.gemini/skills/
```

Skill 文件使用最大兼容性的 markdown 格式。Agent 特定元数据放在 frontmatter `aliases:` 中。

**Subagent 兼容性**:Claude Code 原生支持 subagent;其他 agent 无此抽象时,`/taste` 降级为顺序 prompt chain,功能等价但延迟累加。降级路径在 setup 时检测并自动选择。

### 4.5 内部实现依赖

OmegaWiki 继承的 Python 工具集(`tools/` 20 CLI、`mcp-servers/`、`tests/`)作为 Bab-ilu 的内部依赖维护,**不是产品卖点**。修改继承工具时使用显式 patch 标注。跨语言 agent(Hermes、Codex)调用 Python 工具通过 CLI 边界实现,不要求 agent 本身是 Python。

---

## 5. 差异化特性 —— TASTE

Bab-ilu 的核心价值。本章全面重写自 v1.2,结构为:学术血统 → 运行机制 → 用户产出形态 → 母语化 → 评估。

### 5.1 学术血统与基因

TASTE 不是"AI 工程师对美学的结构化想象",而是**三条美学学术血脉在 LLM 时代的延续**。完整的 prompt 级定义在 `schema.md §5`,供 subagent 在调用时读取。本节为产品叙事。

**血脉一:Warburg Nachleben(图像后世)** —— 驱动 `taste-lineage` subagent

视觉母题不属于单一作者或时代,它们跨世纪迁徙、变异、再现。王家卫的饱和色彩可上溯至维米尔的光线处理与马蒂斯的情感色彩;Bauhaus 的几何构图在 1920 年代的海报与 2020 年代的 iOS 控制中心有同一 Pathosformel。`taste-lineage` 的职责是识别这些跨时空视觉谱系,并将分析对象归入某张 Warburg 面板(`wiki/_panels/`)。**禁止的推理模式**:纯粹风格标签、只看年代不看母题、无视觉物证的影响链附会。

**血脉二:Panofsky 三层图像学** —— 驱动 `taste-icon` 与 `taste-synthesis`

1. **前图像志(pre-iconographic)**:具体可见——颜色、光线、构图、材质、镜头
2. **图像志(iconographic)**:文化约定——时代、场景、服饰、可识别符号
3. **图像学(iconological)**:内在意义——世界观、精神底色、文化时刻

`taste-icon` 产出前两层,`taste-synthesis` 产出第三层并完成跨模态提示词装配。**三层的严格分离是 Bab-ilu 提示词高质量的结构性来源**——通用提示词把三层压成形容词汤("cinematic, moody, vintage"),Bab-ilu 让三层结构显性,这正是生成模型(MJ v6+ / Flux / Sora / Kling)响应具体性的机制。

**血脉三:Getty AAT + Wikidata** —— 驱动外部锚点与术语词汇

Getty AAT 是四十年积累的 55,000 概念受控艺术与建筑词表。这些术语大量出现在生成模型的训练数据中(博物馆元数据 → Wikipedia → LAION)——**AAT 锚定的提示词比民间风格标签产出具体一个数量级**。Wikidata QID 则让 Aesthetic 实体进入 Linked Open Data 生态,未来可与 Europeana、Getty Research 等机构联邦化。

### 5.2 运行机制

`/taste` 是 orchestrator,调度 3–5 个 taste-* subagent,定义在 `.claude/agents/`(markdown + YAML frontmatter,Claude Code 原生格式)。

```
共享层(3 个核心 + 1 个可选)
├── taste-icon         Panofsky 前图像志 + 图像志层
├── taste-lineage      Warburg Nachleben + 跨时空母题追踪
├── taste-synthesis    Panofsky 图像学层 + 三模态提示词装配 + AAT 词汇一致性检查
└── taste-eye(可选)  域检测与首印象(仅在输入模糊时启用)
```

**v1.2 → v1.3 位移**:从 15 subagent 缩到 3–5。砍掉 6 领域 × 2 角色(craft/structure)的双角色矩阵——它是工程结构,不是问题本质。领域信息下沉为 Aesthetic frontmatter 的 `domain` soft hint,由 `taste-synthesis` 的 prompt 根据 domain 调整词汇重点,不再分裂为独立 subagent。

**为什么 `taste-synthesis` 同时负责图像学层和提示词装配**:iconological 层是整张 Aesthetic MD 的思想核心,也是提示词 `[iconological]` 段的内容来源——由同一 subagent 产出保证一致性。提示词装配还要做三件事:
- 整合三层的前图像志与图像志(来自 `taste-icon`)与图像学(自己产出)为结构化提示词骨架
- 引入 `taste-lineage` 提供的 Warburg 面板和签名作者
- 对照 Getty AAT 词表,将民间风格描述替换为 AAT 规范术语(这是提示词质量跃迁的关键一步)

#### Orchestration 拓扑

```
[用户:/taste + 视觉素材]
       ↓
  taste-eye(可选)检测域 → {domain hint}
       ↓
  taste-icon 产出前图像志 + 图像志层
       ↓
  taste-lineage 读 icon 输出 → 追母题归属 → 给出 Warburg 面板 wikilink
       ↓
  taste-synthesis 合并 icon + lineage → iconological 层 + 三模态提示词装配 + AAT 词汇校对
       ↓
  写入 wiki/aesthetics/{domain}/<slug>.md(含 prompts 与学术溯源小节)
  必要时更新或新增 wiki/_panels/<panel>.md
```

### 5.3 用户产出形态

每次 `/taste` 的产出是一张 Aesthetic MD,尾部自动生成两个小节(顺序:先 Prompts,后学术溯源——**用户先看到创作输出,再看到学术背书**)。

#### Aesthetic MD 范例

**输入**:用户拖入 10 张王家卫《重庆森林》剧照到 `raw/images/wkw/`,运行 `/ingest --panel`。

**输出 1** `wiki/aesthetics/cinema/wong-kar-wai-chromatic-nostalgia.md`:

```markdown
---
type: aesthetic
title: 王家卫式色彩乡愁
aat_id: "300015541"
wikidata: "Q1398191"
warburg_panel: [[[saturation-as-memory]]]
panofsky_layer: iconological
domain: cinema
prompts:
  ui:    {generated: 2026-04-16, last_tested: null, test_score: null}
  image: {generated: 2026-04-16, last_tested: null, test_score: null, compatible_models: [midjourney-v6, flux-1.1-pro, nano-banana]}
  video: {generated: 2026-04-16, last_tested: null, test_score: null, compatible_models: [runway-gen3, kling-1.6]}
schema_version: 1.3.0
---

## Core observation
<LLM 生成的正文,三段左右,描述这组图像共同的美学指纹>

<!-- llm:section-start prompts -->
## Prompts

### UI prompt
[pre-iconographic] saturated teal and amber palette (primary #1a1a2e · accent #e94560 · highlight #fdeaa7), 
OKLCH split-complementary, heavy text/title contrast, Helvetica Neue with slight condensed,
grid-breaking vertical rhythm, warm paper texture overlay at 8% opacity
[iconographic] late-1990s Hong Kong editorial web / contemporary narrative product UI
[iconological] chromatic nostalgia — saturation as memory, UI as emotional reverberation
[lineage] Warburg panel: [[saturation-as-memory]] · AAT: Expressive Color (aat:300056452) · signature: Wong Kar-wai editorial legacy

### Image prompt (compatible: midjourney v6+, flux-1.1-pro, nano-banana)
[pre-iconographic] saturated teal and amber, handheld slight sway, slow zoom on corridor, 
wet neon reflection, step-printed motion blur, 35mm telephoto compression
[iconographic] 1960s-90s Hong Kong tenement corridor, cheongsam silhouette, steam from noodle stall, 
neon signage in Traditional Chinese
[iconological] chromatic nostalgia — saturation as memory, compressed time, romantic solitude
[lineage] Warburg panel: [[saturation-as-memory]] · AAT: Chinese Modern (aat:300015541) · signature: Wong Kar-wai / Christopher Doyle cinematography
--ar 16:9 --style raw

### Video prompt (compatible: runway gen-3, sora, kling 1.6, pika)
[pre-iconographic] handheld telephoto, step-printed motion blur 6fps within 24fps base,
slow zoom from 35mm to 50mm equivalent, wet neon reflection, shallow depth with bokeh
[iconographic] Hong Kong corridor, passing cheongsam figure, mirror reflection intermediate shot
[iconological] chromatic nostalgia arc — from hope to resignation across 6 seconds
[lineage] Warburg panel: [[saturation-as-memory]] · AAT: Chinese Modern (aat:300015541) · director signature: Wong Kar-wai
duration: 6s · transition: dissolve with saturation lift
<!-- llm:section-end prompts -->

<!-- llm:section-start academic-lineage -->
## 学术溯源 (Academic Lineage)

- **Warburg 面板**:[[saturation-as-memory]] —— 饱和色彩作为时间淤积的 Pathosformel;跨越维米尔室内光线、马蒂斯情感色彩、Wong Kar-wai 香港夜景
- **Panofsky 层**:iconological —— 色彩在此不是视觉属性,而是文化记忆的象征结构
- **Getty AAT**:[aat:300015541](http://vocab.getty.edu/aat/300015541) —— Styles and Periods > Asian > East Asian > Chinese Modern
- **Wikidata**:[wikidata:Q1398191](https://www.wikidata.org/wiki/Q1398191)
- **跨传统笔记**:本 Pathosformel 可上溯至维米尔的色温处理(Dutch Golden Age 内景)与马蒂斯的表现主义色彩(20 世纪早期 Fauvism);当代 Nachleben 出现在电影(王家卫)、摄影(Nan Goldin 部分作品)、游戏美术(Disco Elysium 叙事场景)三处媒介
<!-- llm:section-end academic-lineage -->
```

**输出 2** `wiki/_panels/saturation-as-memory.md`(Warburg 面板,若首次触发则 LLM 新建):

```markdown
---
type: panel
title: "Saturation as Memory: 饱和色彩作为时间淤积"
curator: llm
panofsky_anchor: iconological
members:
  - [[wong-kar-wai-chromatic-nostalgia]]
cross_era: true
cross_medium: true
generator_ready: false  # 仅 1 member, 需 ≥5
---

## Pathosformel statement
跨越 17 世纪尼德兰室内画、20 世纪早期野兽派、现代华语电影与当代游戏的一条视觉母题:
饱和色彩不再承担描述功能,而成为情感与记忆的结构性载体。

## Visual evidence
- [[wong-kar-wai-chromatic-nostalgia]]
- _[未来扩展:vermeer-interior-light · matisse-the-red-room · disco-elysium-nostalgia]_

## Nachleben commentary
<LLM 生成:母题如何迁徙 / 变异 / 再现>

## Scholarly cross-references
- Warburg Institute 数字档案:[相关面板编号]
- Getty AAT 父概念:Expressive Color (aat:300056452)
```

**用户要做什么**:拖 10 张图、跑 `/ingest --panel`、看结果。**用户从不接触 aat_id、从不读 Warburg 是谁、从不编写提示词骨架**——但产出自带学术血统,提示词可直接粘贴到 Midjourney / Runway。

### 5.4 提示词作为核心交付物

这是 Bab-ilu 在 v1.3 的关键重新定位——TASTE 的终点不是分析,是创作。

**结构骨架**(三模态共用):每个生成提示词含四段标记:
- `[pre-iconographic]` — 具体可见
- `[iconographic]` — 文化约定
- `[iconological]` — 情绪与世界观
- `[lineage]` — 明示出处:Warburg 面板、AAT 术语、签名作者

标记是字面文本,不是元数据——它们出现在提示词中。**标记的存在本身就会让生成模型从"风格标签混合"切换到"构成式思考"**。这是 Midjourney 社区三年摸索出的"层次法"的学术版本。

**模态差异**:
- **UI 提示词**:输出设计 token(HEX + OKLCH 色板、真实字体名、间距节奏、交互母题)+ 参考血统。面向 Claude Code / Cursor 等 AI 编程 agent 从美学 brief 实现前端
- **图像提示词**:为 Midjourney v6+、Flux、Nano Banana、Stable Diffusion 写作。含长宽比、焦段/镜头、光线方向、负空间。AAT 术语**原样保留**
- **视频提示词**:为 Runway、Sora、Kling、Pika 写作。加时间规格(镜头类型、摄像机运动、时长、转场节奏)。Pathosformel 有明确电影出处时,点名签名导演

**面板级提示词**:当 Warburg 面板 `generator_ready: true`(成员 ≥5 且有 ≥0.7 生成回测分)时,`/prompt --panel <panel>` 生成**跨面板提示词**——综合面板所有成员的 Pathosformel,输出在传统中创作而非模仿单一作品。这是 Nachleben 机制的操作化:**你在一条跨时空的视觉谱系中生成,而不是在复制单一参考**。

**提示词生命周期**:
1. `/taste` 或 `/ingest` 时自动生成
2. 用户用提示词做生成(`/prompt --use` 记录用量)
3. `generative_regression` 评估(§5.5.3)
4. 高质量的被提升为 `type: prompt` 独立实体,存 `wiki/_prompts/`,反向 `derived_from` 源 Aesthetic

### 5.5 母语化(L2 深度本地化)

继承自 v1.2,降调为"深度 L2"(不再声称填 L1 空白)。

`/distill` 把英文来源重构为母语知识卡片——不是翻译,是**用母语思维框架重构内容**,保留关键英文术语作为双语锚点(首次出现 `注意力机制 (Attention Mechanism)`,之后 `注意力机制`)。

`/glossary` 维护 `wiki/_glossary.md`——单文件、一表一语言对。遵循 Getty AAT 多语言约定:不同语言的等价术语共享一个规范 ID。

**用户体验**:用户全程用母语工作,外语只在输入边界存在。搜索两种语言都能用。**但自动生成的提示词主体保留英文**(因为 AAT 术语是英文,生成模型以英文训练)——解释是中文,可直接用于生成的提示词是英文。

### 5.6 评估方法

美学没有评估 = Bab-ilu 是"花哨的提示词集合"。v1 必须交付三种评估,每种在 6 领域有基线数据。评估样本全部以 markdown 文件形式存在 `wiki/_evals/`——万物皆 MD。

**(a) 反向识别测试** —— 评估 `taste-lineage` 的识别准确率
- 准备已知 Pathosformel 的视觉素材集(6 领域 × 20 张 = 120 张,见 §5.7)
- 不给元数据,看 subagent 能否独立识别 Warburg 面板归属
- 指标:Top-3 识别准确率 ≥ 0.7(并以 inter-coder agreement 计分)

**(b) 盲验对比测试** —— 评估综合审美判断
- 同一素材由人类专家和 subagent 组分别出 Aesthetic 卡片
- 双盲对比核心维度(色板、panofsky_layer、warburg_panel 归属)的重合度
- 与 Getty AAT 层级、Wikidata 声明交叉核验——**分歧标记为待审,不自动判错**(LLM 可能在 Getty 沉默的领域正确)

**(c) 生成回测** —— **核心用户验证方法** (v1.3 升格)
- Aesthetic 卡片自动生成的提示词,跑到它声明的兼容模型(Midjourney / Flux / Nano Banana / Runway / Sora / Kling)
- 生成输出给人类审阅者,判断"这是哪个 Aesthetic 出来的"
- 识别准确率 ≥ 0.7 = 提示词合格
- **这个方法直接验证产品承诺:Bab-ilu 的提示词真的能生成符合血统的内容**

三种评估在 v1 都必须有基线数据;v1.5+ 每次 subagent prompt 改动都跑一遍作为回归测试。

### 5.7 评估集策展流程(AI 自举 + 人审)

6 领域 × ~20 张 = ~120 张标杆样本,不由人从零策展:

1. **LLM 拉候选清单**——扫公开 canon(AFI Top100、Apple Design Award、TDC 年鉴、Pritzker、Magnum 代表作、D.I.C.E. 游戏美术奖),按 Pathosformel 桶分组,附选样理由
2. **人审**——用户只做三种动作:通过 / 改 / 删。不从零挑,只做筛选。改写反哺下次选样
3. **写入**——通过的条目写入 `wiki/_evals/<method>/<slug>.md`,版本化
4. **自动提升**——AI 定期扫描新进 Aesthetic 卡片,识别是否该提升为评估集成员,用户确认

**这个流程本身是"人机共同进化"的微型实例**——AI 做列举苦活,人做审美判断。

---

## 6. 用户流程

### 6.1 安装

```
用户 clone Bab-ilu 仓库
       ↓
用户运行:/genesis
       ↓
系统检测已安装 agent(Claude Code、Hermes 等)
       ↓
创建 symlink 到每个 agent 的 skill 目录
       ↓
初始化三层:raw/(空)、wiki/(空)、schema.md(版本化)
       ↓
构建初始空索引
       ↓
就绪。打印下一步提示:"运行 /ingest <url> 或拖图到 raw/images/ 后 /taste 试试。"
```

### 6.2 端到端范例:Wong Kar-wai 色彩乡愁 → 生成视频

```
步骤 1:用户拖 10 张《重庆森林》剧照到 raw/images/wkw/
步骤 2:用户运行 /ingest --panel raw/images/wkw/

系统(自动):
  · taste-eye 检测域 → cinema
  · taste-icon 逐图产出前图像志 + 图像志层
  · taste-lineage 识别共同 Pathosformel → 归入 "Saturation as Memory" 面板
    (如不存在则新建 wiki/_panels/saturation-as-memory.md)
  · taste-synthesis 合并 → 生成 wiki/aesthetics/cinema/wong-kar-wai-chromatic-nostalgia.md
    · aat_id: "300015541"(auto-filled)
    · wikidata: "Q1398191"(auto-filled)
    · Prompts 小节(UI / image / video)
    · 学术溯源小节
  · 惰性重建 edges.jsonl

步骤 3:用户打开 Obsidian → 看到新 Aesthetic 卡片

步骤 4:用户复制视频提示词到 Runway
       → 得到 6 秒片段
       → (可选)/prompt --use wong-kar-wai-chromatic-nostalgia video
         记录用量 + 评分(用于 generative_regression 评估)

步骤 5(可选):用户觉得此提示词特别好用
       → /prompt --promote wong-kar-wai-chromatic-nostalgia video
       → 创建 wiki/_prompts/saturation-nostalgia-video.md
         (type: prompt, derived_from: [[wong-kar-wai-chromatic-nostalgia]])
       → 未来可直接被其他项目引用
```

**用户接触到的概念**:拖图、`/ingest --panel`、打开 MD、复制提示词、`/prompt --use`。**与 Karpathy 原版 LLM Wiki 等价**——加了一个动作(复制提示词到生成模型),但这正是产品核心价值所在。

### 6.3 查询流程

```
用户:/ask 有哪些 Aesthetic 使用了 "Saturation as Memory" 面板?

系统:
  · 读 wiki/_panels/saturation-as-memory.md 的 members
  · 遍历 edges.jsonl 找所有 exemplifies → saturation-as-memory 的 Aesthetic
  · 综合回答 + 条目链接

回答:"3 个 Aesthetic 沿这一 Pathosformel 生长:
  · [[Wong Kar-wai 色彩乡愁]] — 电影,iconological 层
  · [[Nan Goldin 夜色]] — 摄影,iconological 层
  · [[Disco Elysium 叙事场景]] — 游戏美术,iconological 层
  面板详见 [[Saturation as Memory]]。"
```

### 6.4 英文文章摄入(辅助流程)

```
用户:/ingest https://anthropic.com/engineering/harness-design

系统:
  · 获取 → raw/articles/harness-design.md
  · 检测语言:英文
  · /distill → 生成中文知识卡片
  · /compile → 提取:
      - concept (role: methodology): harness-design.md
      - concept: context-reset.md
      - person: anthropic-engineering.md
  · 自动交叉链接 → 惰性重建索引

用户打开 Obsidian → engineering/ 下看到新条目,中文内容 + 英文术语锚
```

---

## 7. 相关项目格局与学术对标

> OmegaWiki 不在此表——它是 Bab-ilu 的**基底**,见 §1.3 和 §1.8。

### 7.1 学术对标(Bab-ilu 进入的生态位)

| 对标 | 形态 | 与 Bab-ilu 的关系 |
|------|------|---------------------|
| [Warburg Institute Mnemosyne Atlas 数字化版](https://warburg.sas.ac.uk/) | 学术图像档案 | Bab-ilu 的 `wiki/_panels/` 直接继承 Warburg 面板传统 |
| [Getty AAT](http://vocab.getty.edu/aat/) | 受控艺术与建筑词表 | Aesthetic 实体的 `aat_id` 字段直接引用 |
| [Wikidata LOD](https://www.wikidata.org/) | 全球链接开放数据 | `wikidata` 字段,未来可 federate |
| [Europeana](https://www.europeana.eu/) | 欧洲数字文化遗产聚合 | 潜在的未来联邦化伙伴 |

### 7.2 功能相近的同类方案(非基底)

| 项目 | 优势 | 与 Bab-ilu 的关系 |
|------|------|---------------------|
| [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | 多 agent skill 架构最小实现 | Skill 集很少(6 个),无视觉知识,无双语;借鉴 setup 思路 |
| [MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki) | 双平台(Obsidian + Logseq) | Schema 更简单,无美学 |
| [Obsidian LLM Wiki 插件](https://forum.obsidian.md/t/new-plugin-llm-wiki-turn-your-vault-into-a-queryable-knowledge-base-privately/113223) | 原生 Obsidian 插件,本地隐私(Ollama) | 仅插件,无多 agent,有限 schema |

---

## 8. 技术参考

### 已克隆的参考仓库(`references/`)

| 目录 | 来源 | 为什么参考它 |
|------|------|-------------|
| `references/OmegaWiki/` | [skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki) v0.1.0 | **Fork 基底**,见 §1.8,保留为历史快照 |
| `references/obsidian-wiki/` | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | 多 agent skill 架构。setup.sh / skill 目录结构 |
| `references/llm-wiki/` | [MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki) | 双平台 Obsidian + Logseq 思路 |
| `references/llm-wiki-agent/` | [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 轻量实现,纯 markdown ingest/compile/query 流程 |
| `references/obsidian-claude-code-mcp/` | [iansinnott/obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp) | MCP 集成模式参考 |
| `references/claude-code-analysis/` | [liuup/claude-code-analysis](https://github.com/liuup/claude-code-analysis) | Claude Code 内部结构参考 |

### 外部参考(未克隆)

- [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — **三层架构哲学基底**
- [Panofsky, "Studies in Iconology"(1939)](https://en.wikipedia.org/wiki/Iconology) — 图像学三层
- [Warburg Institute Mnemosyne Atlas](https://warburg.sas.ac.uk/archive/archive-collections/mnemosyne-atlas) — 面板传统原典
- [Getty AAT Online](http://vocab.getty.edu/aat/) — AAT 在线词表
- [Wikidata](https://www.wikidata.org/) — LOD
- [Anthropic Harness Design](https://www.anthropic.com/engineering/harness-design-long-running-apps) — 多 agent 架构方法论

---

## 9. 错误恢复与维护

### 9.1 恢复模型

Vault 的恢复模型基于**不可变 raw + 可重建 wiki + 稳定 schema.md**:

- `raw/` 不可变
- `wiki/` 条目可通过 `/ingest`(含 `/compile` 与 `/distill`)从 `raw/` 重新派生
- `_index/` 可通过 `tools/rebuild-index.sh` 从 frontmatter 完全重建
- `schema.md` 版本化,是 LLM 行为的稳定锚
- `.claude/agents/` 的 subagent prompt 引用 `schema.md §x.y` 章节号,schema 更新时 prompt 自动继承

### 9.2 常见恢复场景

| 场景 | 恢复路径 |
|------|---------|
| 摄入出错 | 删除 `wiki/` 生成的条目,重新 `/ingest` |
| 索引损坏 | `tools/rebuild-index.sh` 从 frontmatter 重建 |
| Aesthetic 缺"学术溯源"小节 | `/check` 检出 → 自动 `/taste` 重跑该条目 |
| Aesthetic 的 aat_id/wikidata 卡在 null 超过 14 天 | `/check` 列出 → 用户确认候选 |
| 提示词测试过期(>30 天) | `/check` 标记 → 触发 generative_regression 回测 |
| 面板 member < 3 | `/check` 标记为 "potentially unstable",建议合并或补充 |
| 双语 glossary 漂移 | `/check` 检出 → 手工或 `/glossary` 修复 |
| schema_version 漂移 | `/check` 提议迁移 |

### 9.3 `/check` 规格

`/check` 读 `schema.md` 并报告以下偏差:

- Aesthetic `aat_id: null` 超过 14 天窗口
- Aesthetic 缺 `<!-- llm:section-start prompts -->` 块
- Aesthetic 缺 `<!-- llm:section-start academic-lineage -->` 块
- Prompt 缺兼容模型测试超过 30 天
- 面板成员少于 3 个
- 面板 `generator_ready: true` 但缺跨面板提示词
- 双语 glossary 漂移
- 评估样本缺 inter-coder agreement
- MD 的 schema_version 与 schema.md 版本漂移

### 9.4 规模上限

Bab-ilu v1 设计支持最多 **10,000 条目**的 vault。在此规模下:
- `edges.jsonl` 的惰性重建仍可管理(约 30K 边,约 3MB)
- `entry-index.yaml` 以压缩格式能完整读入
- `/cross-link` 的 frontmatter 解析在合理时间内完成

### 9.5 备份哲学

- **不依赖 git**。Bab-ilu 从 day-1 假设用户可能不用 git,恢复路径不包含"从 git 找回"
- `raw/` 不可变 + `schema.md` 稳定 + `wiki/` 可重建 ≡ 完整系统
- 用户可自行加 git 做版本控制,但这是用户选择,不是系统需求

---

> PRD v1.3 完。此文档的权威版本为中文。英文镜像位于 `PRD.md`,内容需与本文档一致。
> Schema 细节(LLM 读)位于 `schema.md`。本 PRD 引用 schema 章节号但不重述内容。
