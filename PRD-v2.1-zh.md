# Bab-ilu — PRD v2.1

> **日期**：2026-04-18（v2.0 重定位修订）
> **状态**：v2.0 的产品定位升级。骨架、图谱、vault 语言策略全部保留；Warburg 从"产品内核"降级为"美学透镜"，新增"学科透镜"作为产品一级概念。
> **受众**：所有使用 agent 完成知识工作的普通人——导演、设计师、工程师、研究者、医生、律师、分析师、学生。不预设领域。

---

## 0. 一句话定位

**Bab-ilu 是一个自带学科透镜的 LLM-Wiki。装上就能用——你的领域已经有经典理论替你把结构搭好了。**

---

## 0.5 理论基础与传承谱系（硬约束）

> 本节为 Bab-ilu 的核心价值命题，**写死**。所有未来设计决策、Sprint 规划、PR 评审、skill 变更都必须回溯到此节。本节 §0.5.2（核心命题）与 §0.5.3（五条原则）同步进 `CLAUDE.md`，作为每次 agent 会话的约束前置词。

### 0.5.1 传承谱系

Bab-ilu 的设计传承自三个历史节点：

**① Vannevar Bush · Memex（1945）**
提出个人策展的、文档间连接的知识库愿景——**连接的价值不低于文档本身**。Memex 未解决的问题是"谁来做维护"。

**② Andrej Karpathy · LLM-Wiki（2026）**
以三层架构（raw / wiki / schema）让 LLM 成为永不疲倦的维护者。Karpathy 的原话：

> *"You and the LLM co-evolve this [the schema] over time as you figure out what works for your domain."*

Karpathy 明示的核心机制：

- **三层架构**（raw / wiki / schema）
- **Schema co-evolution**（人与 LLM 协作演化契约——不是用户独自设计 schema）
- **Query 回存**——*"good answers can be filed back into the wiki as new pages... this way your explorations compound in the knowledge base just like ingested sources do."*
- **Lint 主动建议**——*"the LLM is good at suggesting new questions to investigate and new sources to look for."*
- **index.md + log.md** 作为导航元数据

Karpathy 解决了 Memex 的维护问题。但他的原文**有意保持抽象**——*"pick what's useful, ignore what isn't... share with your LLM agent and work together to instantiate a version that fits your needs."*——他把"世界观"和"实现"分开，自己只写世界观。

**Karpathy 的世界观中，底下持有控制论 + 晚期维特根斯坦的双轴价值观，但他不命名。**

**③ Bab-ilu（本项目，2026-）**
在 Karpathy 架构之上做三件事：

- **显性化**其底下的世界观（控制论 + 晚期维特根斯坦）
- **扩展** co-evolution 从"schema 字段级"到"整个 lens 脚手架级"（LENS EVOLUTION）
- **加入**抽象化训练环（`/taste` + 反向提示词）+ 预装 lens 插槽机制

---

### 0.5.2 核心价值命题（写死）

> **Bab-ilu 不是一个"知道规则"的系统，是一个"从实践中长出规则"的系统。**

- **控制论**（Wiener / Ashby / Beer）给"**如何从实践中长**"的工程实现——闭环、自适应、变异度匹配、晚绑定。
- **晚期维特根斯坦**（《哲学研究》——语言游戏 / 家族相似性 / 生活形式 / 规则跟随悖论）给"**为什么必须从实践中长**"的哲学依据。

**这两者不是并列的两个参考，是同一世界观的工程侧和哲学侧。**

所有与此核心命题冲突的设计决策都被拒绝，不论它在局部是否"更方便"。原则之间若产生冲突，回溯到本节决裁。

---

### 0.5.3 五条可操作原则

这五条原则约束所有未来设计决策、Sprint 规划、PR 评审、skill 变更。

| # | 原则 | 控制论依据 | 维特根斯坦依据 | 具体含义 |
|---|---|---|---|---|
| 1 | **晚绑定**（late binding） | Ashby · 控制器不能在样本不足时固化模型 | 规则跟随悖论（§201）· 规则从实践中涌现 | 任何能延迟的全局决策都延迟；优先收集 variety，再归纳 |
| 2 | **反本质**（anti-essentialism） | 系统多样性要求多态控制 | 家族相似性 · 概念族之间无共同本质 | Lens schema 松散，允许每个 lens 有独特字段；不强制共享结构 |
| 3 | **闭环优先** | Wiener · 无反馈就无控制 | 意义即用法 · 无实践即无意义 | 工程上先保证真实闭环（accept/reject 持久化 / 自适应阈值 / 反向提示词 / 跨会话学习），再考虑功能扩展 |
| 4 | **Variety 匹配** | Ashby 必要变异度定律 · 控制器变异度 ≥ 被控系统变异度 | 语言游戏 · 新生活形式需新游戏 | Lens 必须能随用户 variety 成长。LENS EVOLUTION 是 Ashby 定律的工程实现 |
| 5 | **实践优于规则** | Beer VSM · S4/S5 从实际运转中归纳 | 生活形式 · 规则嵌入共同体实践 | 不做"什么是好 lens"的教条；展示美学作为范例 + 邀请社区贡献，标准在实践中涌现 |

---

### 0.5.4 对 Karpathy 的继承与扩展清单

| 机制 | Karpathy 明示 | Bab-ilu v2.1 状态 | 行动 |
|---|---|---|---|
| 三层架构 raw / wiki / schema | ✅ | ✅ 已实现（raw / wiki / .agent） | — |
| index.md + log.md | ✅ | ✅ 已实现 | — |
| Schema co-evolution | ✅ | ✅ 已实现（CLAUDE.md + schema.md） | — |
| CLAUDE.md 作为纪律文档 | ✅ | ✅ 已实现 | — |
| Ingest 一次触达 10-15 页 | ✅ | ✅ 已实现 | — |
| **Query 回存为新 wiki 页** | ✅ 明示核心复利机制 | ❌ **未实现** | **Sprint 4 必须补**：`/ask` 结束时询问归档为 `wiki/syntheses/<slug>.md` |
| **Lint 建议新问题 + 新素材** | ✅ 明示 | ❌ **仅局部合规检查** | **Sprint 4 必须升级**：加入矛盾检测、过时检测、素材请求循环 |
| 多 lens 架构 | ❌ Karpathy 未提 | ✅ 已实现（aesthetic / engineering / zettelkasten） | Bab-ilu 扩展 |
| Schema co-evolution **扩展到 lens 级** | ❌ Karpathy 未提 | ❌ 未实现 | **LENS EVOLUTION**——Karpathy co-evolution 原则的工程化扩展 |
| 抽象化训练环（`/taste` + 反向提示词） | ❌ Karpathy 未提 | ⚠️ `/taste` 已实现；反向提示词被 `f956e92` 激进清理 | **Sprint 4**：revive `prompt_tester.py` + lens-aware 路由 |
| 预装 lens 插槽（压力测试通过的深度 lens） | ❌ Karpathy 未提 | ⚠️ 美学作为第一个入槽实例，资质标准未定义 | Sprint 4 只固化美学；第二个实例浮现时再归纳标准（原则 1：晚绑定） |

**继承意味着 Bab-ilu 与 Karpathy 不是"借鉴后偏离"的关系，而是"继承 + 显性化 + 扩展"**：

- **继承** Karpathy 的所有具体机制
- **显性化**他默认持有但不命名的世界观
- **扩展**在此世界观框架内（LENS EVOLUTION / 抽象化训练环 / 预装插槽），所有扩展回溯到 §0.5.2 核心命题

---

### 0.5.5 版本化承诺

- §0.5.1（谱系）、§0.5.2（核心命题）、§0.5.3（五条原则）为**不可变节**。修订它们需要重新对齐控制论与晚期维特根斯坦的理论基础。
- §0.5.4 继承清单为**活文档**——随 Sprint 完成情况更新"Bab-ilu 状态"列与"行动"列；"Karpathy 明示"列只在 Karpathy 原文被重新解读时修订。
- §0.5.2 + §0.5.3 同步进 `CLAUDE.md` 作为会话前置词。PRD 与 CLAUDE.md 中此两节若出现漂移，以 PRD 为准。

---

## 1. 为什么要做这个

### 1.1 Karpathy 的 LLM-Wiki 提出了革命性的想法

2026 年 Andrej Karpathy 在他的个人 gist 里提出了 LLM-Wiki：一个**由人和 LLM 共同演化的**私人知识库，`raw/` 存不变的原始素材，`wiki/` 存 LLM 可读可写的结构化整理，schema 是两者协商出来的契约。核心洞察：**把 LLM 当成会读会写的同事，而不是会回答问题的聊天框**。

Karpathy 的原话：*"You and the LLM co-evolve this over time as you figure out what works for your domain."*

### 1.2 Karpathy 的盲点

这个设计对 Karpathy 这样的人有效——他是世界级的结构化思考者，能自己想清楚"motif 是什么"、"它和 work 怎么关联"、"什么时候该涌现一个新层级"。

**但 99% 的用户不是 Karpathy。** 导演没学过图论，医生没学过 ontology，律师没学过聚类算法，PM 没学过图谱理论。让他们"co-evolve schema with LLM"=让他们从零搭一套本来要读博士才能搭的东西。

结果有两种：
1. 用户放弃，wiki 退化成堆文件的文件夹
2. 用户硬撑，搭出一个自相矛盾、漂移、无法聚类的垃圾图谱

### 1.3 Bab-ilu 的答案：**透镜即脚手架**

每个成熟学科已经积累了**经过几十年验证的知识组织框架**：

| 领域 | 成熟透镜 | 核心结构 |
|---|---|---|
| 美学 / 视觉创作 | Warburg Pathosformel / Panofsky 三层 | Work × Motif → Pathosformel 涌现 |
| 软件工程 | Alexander Pattern Language | Problem × Context → Pattern 涌现 |
| 科学研究 | Kuhn 范式 / Popper 反驳 | Observation × Theory → Paradigm Shift |
| 金融分析 | Minsky 流动性层级 | Event × Mechanism → Cascade Pattern |
| 法律实务 | IRAC（Issue/Rule/Application/Conclusion） | Fact × Precedent → Doctrine |
| 临床医学 | SOAP / DDx | Symptom × Sign → Diagnosis |
| 普适学习 | Zettelkasten + Bloom 分类 | Note × Concept → Understanding Tier |

这些透镜**不是我们发明的**——它们是 Warburg、Alexander、Kuhn、Minsky、Fuld、Luhmann、Bloom 经过一辈子学术劳动留下来的认知脚手架。

**Bab-ilu 的全部创新**：把底层算法设计成域无关的（bipartite 图 + Leiden 聚类 + 涌现 tier），然后把这些成熟透镜作为**可选配置**打包进产品。

用户 `/genesis` 时选一个透镜，agent 就知道：
- 在你的领域里"原子单元"叫什么
- 什么结构值得涌现
- 阈值应该设多高
- 如何写策展散文

**结论**：Bab-ilu = Karpathy 的 LLM-Wiki（raw/ + wiki/ + schema co-evolution） + 学科透镜库（替普通人把 schema 搭好了）。

### 1.4 为什么 Warburg 是第一个透镜

因为美学是**最难的**。

图像意义是最抽象的、最不结构化的、最依赖跨时代/跨文化关联的知识形式。如果我们能让 agent 在美学领域做出 Pathosformel 涌现聚类，其他领域——工程范式、科学范式、金融级联——都只会更容易。

这是**压力测试**，不是产品身份。

哲学锚点是**晚期维特根斯坦**（与 §0.5 同一锚点）：美学是一种特殊的**语言游戏**——图像生产从来不是艺术家从无到有的独创，而是他**参与了历史上的视觉对话**（阅读、观赏、临摹是既有 language game 的 moves；创作是在同一游戏里投下新 move）。Warburg 的 Pathosformel 正是这个语言游戏里的**家族相似性**：跨时代、跨文化的图像之间没有共同本质，但共享可识别的重叠特征。

如果 agent 能在美学这个"家族相似性最稀薄、跨文化依赖最重"的语言游戏里识别结构，其他领域（工程 / 科学 / 法律 / 医学）的语言游戏——家族成员更密集、结构约定更稳定——只会更容易。

---

## 2. 核心哲学：四条硬约束

### ① 透镜优先于领域惯例

一个 vault 在 `/genesis` 时被绑定一个透镜（`vault_lens:` 字段），这个透镜决定：
- 实体类型的解释（Work 在美学 vault 是"一幅画"，在工程 vault 是"一次事故"）
- 聚类的命名规则（Pathosformel / Pattern / Paradigm / Cascade / Doctrine / Diagnosis）
- 阈值微调（美学 k=3, l=3；工程 k=5, l=4 因为 Pattern 要求更多证据）
- `/taste`、`/gap`、`/ask` 的分析契约（Panofsky 三层 / Alexander Problem-Context-Forces-Solution / Kuhn Observation-Anomaly-Paradigm）

**透镜是**：`.agent/lenses/<lens-id>/` 目录里的一组配置 + prompt 模板 + 示例库。
**透镜不是**：可选功能开关。vault 级别强制绑定一个。换透镜 = 新建 vault。

### ② 人类层与 Agent 层物理分离

（继承自 v2.0）`wiki/` 是你在 Obsidian 里读的散文 + wikilinks；`.agent/` 是机器读的 ontology 文件、schema、透镜配置、状态（Obsidian 默认隐藏）。两层同步但互不污染。学术锚点（AAT / Iconclass / ULAN / CVE / ICD-10 / LegiCode 等——透镜定义）双层都保留。

### ③ Vault 语言是 per-vault 配置

（继承自 v2.0）`/genesis` 询问 vault 主体语言（中/英/西/法/日/……），写入 `.agent/CLAUDE.md` 的 `vault_language:` 字段。跨语言源材料用 vault 语言**认知重构**（不是翻译）。此规则对所有透镜通用。

### ④ 图谱算法域无关

Work × Motif 二部图 + Leiden 聚类 + Jaccard 投影 + 自适应阈值 + 聚合节点过滤——这套算法**不知道自己在算美学还是工程**。透镜只改变输入/输出的语义解释，不改算法。

这条约束保证：
- 同一套 `tools/graph_analyzer.py` 服务所有透镜
- 新透镜的开发成本 = **写配置 + prompt 模板**，不是写代码
- 算法改进（更好的聚类、更稳的阈值）一次性惠及所有透镜

---

## 3. 用户体验：四个领域的场景

### 3.1 第一次打开（所有透镜通用）

`/genesis` 问你 5 个问题：

1. vault 主体语言？（中/英/其他）
2. **vault 透镜？**（选择：aesthetic-warburg / engineering-alexander / science-kuhn / finance-minsky / law-irac / medicine-soap / general-zettelkasten / 自定义）
3. 你的工作主场？（透镜内的子领域，比如 aesthetic 透镜下的"电影/摄影/绘画/建筑/UI/平面/游戏/综合"；engineering 透镜下的"分布式/前端/ML/嵌入式/安全/综合"）
4. 要不要导入演示 seed kit？（每个透镜自带一套 20-30 条公共领域 seed；`/reset --seeds` 一键删除）
5. 你已经有积累的素材吗？（如果有，当场跑 `/ingest`）

回答完成后你在 Obsidian 里打开 vault。左侧文件栏只显示：

```
raw/          ← 你的素材（你丢进来的，系统不改）
wiki/         ← 你要读的
output/       ← 你要拿走的
```

`.agent/`（含透镜配置）被 Obsidian 隐藏。

展开 `wiki/`——**目录名由透镜决定**：

<details>
<summary>aesthetic-warburg 透镜</summary>

```
wiki/
  index.md · log.md · _glossary.md
  works/          ← 具体作品：某幅画、某一帧、某个 UI 截图
  motifs/         ← 命名的视觉母题："北面窗光"、"倾斜脖颈的哀伤"
  pathosformel/   ← 涌现的 tier 1 聚类
  topoi/          ← 涌现的 tier 2 聚类（gated）
  people/ · sources/ · questions/
```
</details>

<details>
<summary>engineering-alexander 透镜</summary>

```
wiki/
  index.md · log.md · _glossary.md
  incidents/      ← 具体事故/issue/PR/系统变更
  forces/         ← 命名的工程力："强一致 vs 可用性"、"p99 延迟 vs 吞吐"
  patterns/       ← 涌现的 tier 1 聚类（Alexander Pattern）
  pattern-languages/  ← tier 2 涌现（若干 pattern 共同构成的语言）
  systems/ · sources/ · questions/
```
</details>

<details>
<summary>science-kuhn 透镜</summary>

```
wiki/
  index.md · log.md · _glossary.md
  observations/   ← 具体实验/观测/论文发现
  anomalies/      ← 命名的反常现象
  paradigms/      ← 涌现的 tier 1 聚类（Kuhn 范式）
  revolutions/    ← tier 2 涌现（范式转移的候选）
  scientists/ · sources/ · questions/
```
</details>

<details>
<summary>finance-minsky 透镜</summary>

```
wiki/
  events/         ← 具体市场事件/成交/流动性冲击
  mechanisms/     ← 命名的传导机制："抵押链条"、"期限错配"
  cascades/       ← 涌现的 tier 1 聚类（Minsky 级联）
  regimes/        ← tier 2 涌现（金融体制）
  actors/ · sources/ · questions/
```
</details>

<details>
<summary>medicine-soap 透镜</summary>

```
wiki/
  cases/          ← 具体病例
  signs/          ← 命名的症状/体征/生理指标
  diagnoses/      ← 涌现的 tier 1 聚类（鉴别诊断）
  syndromes/      ← tier 2 涌现
  clinicians/ · sources/ · questions/
```
</details>

不管用哪个透镜，右侧栏默认开 InfraNodus Obsidian plugin 渲染 3D 图谱。

### 3.2 丢素材进去（所有透镜通用）

你把材料丢进 `raw/`，对 Claude Code 说 `/ingest`。十几分钟后：

- `raw/` 里的素材被整理
- `wiki/` 底层节点（works/incidents/observations/events/cases）多出若干新页面
- `wiki/` 中层节点（motifs/forces/anomalies/mechanisms/signs）多出若干新页面（或旧页面加新引用）
- `wiki/log.md` 追加一行记录

右侧栏的 InfraNodus gap 面板：*"底层节点簇 A 和簇 B 之间只差 1-2 条边。要看吗？"*

### 3.3 日常工作（按透镜举例）

**导演（aesthetic-warburg）**：
> "我想要 [[挥刀的游者]] 和 [[风暴作为宣泄]] 的交汇点。给我几个还没被拍过的镜头构想。"

**工程师（engineering-alexander）**：
> "我们在做多租户数据库，[[强一致]] 和 [[租户隔离]] 这两组力在 Spanner、CockroachDB、Neon 的历史 issue 里有没有涌现过新 pattern？"

**研究员（science-kuhn）**：
> "我的领域里 [[小样本学习]] 和 [[对比表征]] 最近半年出现过反常实验结果吗？是否在形成新范式？"

**分析师（finance-minsky）**：
> "[[期限错配]] 和 [[抵押链条]] 在过去三次流动性冲击里共同出现过——有没有我忽略的第三个机制？"

**医生（medicine-soap）**：
> "[[反复晕厥]] + [[心悸]] + [[家族心源性猝死史]] 的病例里，我现有笔记没覆盖的鉴别方向是什么？"

所有这些问题，agent 的处理流程是**同一套**：`/gap` 定位簇、`/ask` 查证据、返回结构化答案 + 建议是否把 gap 沉淀为新 question 页面。

---

## 4. 系统架构

### 4.1 完整目录

```
Bab-ilu/
├── raw/                         # 你的素材（不变）
│
├── wiki/                        # 人类可读（目录名由透镜决定，见 §3.1）
│   ├── index.md · log.md · _glossary.md
│   ├── <tier-0>/                # 底层节点（透镜特定名）
│   ├── <tier-1-motifs>/         # 中层节点（透镜特定名）
│   ├── <tier-1-clusters>/       # tier 1 涌现聚类
│   ├── <tier-2-clusters>/       # tier 2 涌现聚类（gated）
│   ├── people|actors|scientists|clinicians/  # 透镜特定
│   ├── sources/
│   └── questions/
│
├── output/                      # 交互产物（prompts / notes）
│
├── .agent/                      # Agent 可读（Obsidian 隐藏）
│   ├── schema.md                # ≤200 行契约（通用骨架）
│   ├── CLAUDE.md                # ≤100 行项目说明（含 vault_language、vault_lens）
│   ├── lenses/                  # ★ 新增：透镜库
│   │   ├── aesthetic-warburg/
│   │   │   ├── lens.yaml        # 实体类型、聚类命名、阈值微调
│   │   │   ├── prompts.md       # LLM 在本透镜下的分析契约
│   │   │   ├── examples.md      # 示例 motif/cluster 供 agent 参考
│   │   │   └── glossary.md      # 透镜专属术语（Pathosformel / Nachleben）
│   │   ├── engineering-alexander/
│   │   ├── science-kuhn/
│   │   ├── finance-minsky/
│   │   ├── law-irac/
│   │   ├── medicine-soap/
│   │   └── general-zettelkasten/
│   ├── graph/                   # Ontology 文件（机器图谱记忆，透镜无关）
│   │   ├── base.md              # 底层×中层 bipartite 边
│   │   ├── tier1.md             # tier 1 聚类输出
│   │   ├── tier2.md             # tier 2 聚类输出
│   │   ├── anchors.md           # 学术/权威锚点（透镜指定哪些是锚点）
│   │   ├── terminology.md       # 跨语言术语迁移决策
│   │   └── full.md              # 全图（/lint --rebuild-graph 派生）
│   ├── spec/gap-algorithm.md    # 算法规范（域无关）
│   ├── skills/                  # /genesis /ingest /taste /gap /ask /prompt /distill /lint
│   ├── subagents/ · mcp/ · todos/ · state/
│
├── archive/                     # v1.4 及历史归档
├── .obsidian/                   # Obsidian 配置
└── README.md
```

### 4.2 透镜的内部结构（`.agent/lenses/<lens-id>/`）

**`lens.yaml`**（机器读）：

```yaml
id: aesthetic-warburg
display_name: 美学 · Warburg 透镜
display_name_en: Aesthetic · Warburg Lens

tiers:
  tier_0:
    slug: works
    display: 作品
    display_en: Work
    instances_of: [painting, film-frame, photograph, ui-screenshot, architectural-photo]
  tier_1_atom:
    slug: motifs
    display: 视觉母题
    display_en: Motif
  tier_1_cluster:
    slug: pathosformel
    display: 情感公式
    display_en: Pathosformel
    activation: always
  tier_2_cluster:
    slug: topoi
    display: Topos
    activation: |pathosformel| >= 15
  satellite:
    - slug: people
      display: 创作者
    - slug: sources
      display: 文献与档案
    - slug: questions
      display: 开放问题

thresholds:
  k_min: 3
  l_min: 3
  density_multiplier: 3.0

anchors:
  - name: AAT
    pattern: aat:\d+
    url: http://vocab.getty.edu/aat/{id}
  - name: Iconclass
    pattern: iconclass:[\w-]+
  - name: ULAN
    pattern: ulan:\d+

analysis_contract:
  taste:
    - pre_iconographic: 看见了什么（色、光、构图、材质）
    - iconographic: 这在文化里叫什么（wardrobe、典故、类型）
    - iconological: 这暗示什么世界观（情感、政治、宗教、时代精神）
  prompt:
    segments: [pre_iconographic, iconographic, iconological, lineage]

emergence_naming:
  tier_1: 由人类命名 Pathosformel；agent 提议候选
  tier_2: 由人类命名 Topos；agent 提议候选
```

**`prompts.md`**（LLM 读）：透镜专属的系统 prompt 片段，会被 `/taste`、`/gap`、`/ask`、`/prompt` 在运行时拼接到上下文。包含：
- 本透镜的核心判断法则（比如 Warburg 透镜要求 agent 做 Nachleben 追溯）
- 常见陷阱（Warburg 透镜警告 agent 不要按"风格类别"归类）
- 命名风格（motif 用"名词+形容词"短语而非学术术语）

**`examples.md`**（LLM 读）：10-20 个示范 motif / cluster 条目，供 agent 在冷启动时看齐。

**`glossary.md`**（人类 + LLM 读）：透镜专属术语表，会被合并进 `wiki/_glossary.md`。

### 4.3 图谱架构（继承自 v2.0，表述泛化）

**基座：Tier-0 × Tier-1-atom 二部图。**
- Tier-0：底层节点（作品/事故/观测/事件/病例）
- Tier-1-atom：中层节点（母题/力/反常/机制/体征）
- 边：`Tier-0 exemplifies Tier-1-atom`

**tier 1 涌现（基座活跃）**：tier-1-atom 聚成 tier-1-cluster（Pathosformel / Pattern / Paradigm / Cascade / Doctrine / Diagnosis / Concept-Cluster），算法用 Leiden on Jaccard projection + 自适应阈值 `k,l = max{3, ⌈log₂(n)⌉}`。

**tier 2 涌现（gated at |tier-1-cluster| ≥ 15）**：tier-1-cluster 聚成 tier-2-cluster（Topoi / Pattern-Language / Revolution / Regime / Meta-Doctrine / Syndrome）。

**算法流程对所有透镜同构**（见 `.agent/spec/gap-algorithm.md`）。透镜只改变：
- 节点命名
- 阈值微调（在 `lens.yaml` 声明）
- 聚类命名的 LLM prompt（来自 `prompts.md`）

### 4.4 人类可读 vs Agent 可读的分离（继承自 v2.0）

人类读 `wiki/`，agent 读 `.agent/graph/`。Wikilinks 写在散文里（不在 frontmatter）。Frontmatter ≤3 字段。Ontology 增量追加、不整体重写、retraction 通过追加行。

---

## 5. 命令表

8 个命令对所有透镜通用。透镜配置改变命令的 prompt，不改变命令的 CLI 接口。

| 命令 | 做什么 | 透镜如何介入 |
|---|---|---|
| `/genesis [--seeded] [--lens=<id>]` | 首次初始化 vault。交互式问 5 个问题（语言、透镜、子领域、seed、已有素材），创建目录 + `.agent/` 脚手架 + 拷贝选定透镜到 `.agent/lenses/active/` | 透镜决定 `wiki/` 目录名、`.obsidian/` 配色、seed kit 来源 |
| `/ingest <path 或 query>` | 吃素材 → 生成 tier-0/tier-1-atom 页面 + 更新 ontology | 透镜 prompts.md 指导 agent 如何识别 tier-1-atom（motif/force/anomaly/…） |
| `/taste <素材>` | 单项素材的结构化分析：提议 tier-1-atom（不落盘） | 透镜的 `analysis_contract.taste` 定义输出段（Panofsky 三层 / Alexander 四力 / Kuhn 三问 / ……） |
| `/gap [--tier=1\|2\|all]` | 跑 gap 分析 → 生成 questions + 写入 todos | 透镜 lens.yaml 的阈值 + prompts.md 的命名风格 |
| `/ask <问题>` | 查询 vault，合成带引用的 vault-语言答案 | 透镜 prompts.md 的推理风格（Warburg 要做 Nachleben；Alexander 要找 rootcause-force；SOAP 要做 DDx） |
| `/prompt <target>` | 下游产出（不同透镜交付物不同） | 美学透镜产出生成模型 prompt；工程透镜产出 pattern 卡片；科研透镜产出 hypothesis；金融透镜产出风险报告；医学透镜产出 SBAR 汇报 |
| `/distill <source>` | 跨语言源材料认知重构 + 更新 terminology.md | 透镜的 anchors 规则决定哪些术语锚定 |
| `/lint [--rebuild-graph]` | 健康检查：孤儿页、ontology/wiki 不一致 | 透镜的 anchors 规则决定哪些节点应该有锚点 |

---

## 6. Vault 语言 & Vault 透镜：双轴配置

### 6.1 两个独立维度

`.agent/CLAUDE.md` 头部：

```yaml
---
vault_language: zh          # 写作语言
vault_lens: engineering-alexander  # 知识组织透镜
vault_subdomain: distributed-systems  # 子领域（可选）
---
```

- **语言** 是写给谁看（你自己 / 合作者 / 开源读者）的选择
- **透镜** 是用什么框架组织知识的选择
- 两者独立组合：中文+Alexander、英文+Warburg、日文+Kuhn 都合法

### 6.2 认知重构规则（继承自 v2.0）

吸收外文源材料时用 vault 语言**重构意义**，不翻译。这条对所有透镜通用。

### 6.3 切换透镜 = 新建 vault

不支持热切换。理由：
- 透镜决定目录结构（`works/` vs `incidents/`）
- 透镜决定已涌现聚类的语义（把 Pathosformel 改名成 Pattern 是错的）
- 一个人的多个知识领域本来就应该是多个 vault

**建议模式**：`~/vaults/aesthetic-vault/`（warburg 透镜）+ `~/vaults/eng-vault/`（alexander 透镜）+ `~/vaults/life-vault/`（zettelkasten 透镜）。

---

## 7. 图谱与 Obsidian（继承自 v2.0）

InfraNodus Obsidian plugin 可选（可视化），不依赖 SaaS/MCP。Graph View 7 色配色由**透镜指定**：

- 美学透镜：works 黄、motifs 蓝、pathosformel 红、topoi 紫、people 灰、sources 绿、questions 橙
- 工程透镜：incidents 红、forces 蓝、patterns 金、pattern-languages 紫、systems 灰、sources 绿、questions 橙
- 医学透镜：cases 青、signs 蓝、diagnoses 红、syndromes 紫、clinicians 灰、sources 绿、questions 橙

Wikilink-only 写作规则对所有透镜通用。

---

## 8. 透镜库

v2.1 ship 时包含以下透镜。每个透镜在 `.agent/lenses/<id>/` 下有完整配置 + prompts + examples + glossary + 20-30 条 seed 条目。

### 8.1 Tier-0 必选透镜（v2.1 Sprint 2 交付）

#### 🎨 `aesthetic-warburg`（美学透镜）
- 理论基础：Aby Warburg《Mnemosyne Atlas》、Erwin Panofsky 三层图像学、Ernst Gombrich 《艺术的故事》
- 结构：Work × Motif → Pathosformel（tier 1）→ Topoi（tier 2）
- 锚点：AAT / Iconclass / ULAN
- 分析契约：Panofsky 三层（pre-iconographic / iconographic / iconological）
- 交付物：生成模型 prompt（Midjourney/Sora 四段骨架）
- 状态：**已完成**（v2.0 Sprint 1 骨架 + Sprint 2 完善）

#### 🏗️ `engineering-alexander`（工程透镜）
- 理论基础：Christopher Alexander《A Pattern Language》、《Timeless Way of Building》；Gang of Four《Design Patterns》（作为应用示范）
- 结构：Incident × Force → Pattern（tier 1）→ Pattern-Language（tier 2）
- 锚点：CVE / RFC / IETF / W3C / 知名 post-mortem（AWS/Cloudflare/Google SRE Book）
- 分析契约：Alexander Problem-Context-Forces-Solution-Consequences
- 交付物：Pattern 卡片（给 ADR / RFC / design review 直接用）
- 状态：**v2.1 Sprint 3 交付**（第一个非美学透镜，验证透镜架构通用性）

#### 📚 `general-zettelkasten-bloom`（通用学习透镜）
- 理论基础：Niklas Luhmann Zettelkasten、Benjamin Bloom 认知层级（记忆/理解/应用/分析/评价/创造）
- 结构：Note × Concept → Concept-Cluster（tier 1，按 Bloom 层级自动标注）→ Meta-Understanding（tier 2）
- 锚点：Wikipedia / Wikidata / DOI / ISBN
- 分析契约：Luhmann 卡片三问（What/Why/So-what）+ Bloom 层级归类
- 交付物：Progressive Summarization（Tiago Forte 风格的递进摘要）
- 状态：**v2.1 Sprint 4 交付**（作为"没合适透镜"时的 fallback）

### 8.2 Tier-1 扩展透镜（v2.2 Sprint 5-6 交付）

#### 🔬 `science-kuhn`（科研透镜）
- 理论基础：Thomas Kuhn《科学革命的结构》、Karl Popper 反驳主义、Imre Lakatos 研究纲领
- 结构：Observation × Anomaly → Paradigm（tier 1）→ Revolution（tier 2）
- 锚点：DOI / arXiv / PubMed / ORCID
- 交付物：Hypothesis 候选 + 反驳设计（Popperian falsification plan）

#### 💰 `finance-minsky`（金融透镜）
- 理论基础：Hyman Minsky 金融不稳定性假说、Gary Gorton 金融危机机制、Perry Mehrling 货币视角
- 结构：Event × Mechanism → Cascade（tier 1）→ Regime（tier 2）
- 锚点：CUSIP / ISIN / LEI / SEC filings / 中央银行通告
- 交付物：风险报告（Cascade 触发条件 + 缓解机制）

#### ⚖️ `law-irac`（法律透镜）
- 理论基础：IRAC（Issue/Rule/Application/Conclusion）+ CRAC（Conclusion/Rule/Application/Conclusion）+ 判例法分析方法
- 结构：Fact × Rule → Doctrine（tier 1）→ Meta-Doctrine（tier 2）
- 锚点：WestLaw citation / 中国裁判文书网 / CELEX
- 交付物：Memo（IRAC 格式的法律分析备忘录）

#### 🏥 `medicine-soap-ddx`（医学透镜）
- 理论基础：SOAP（Subjective/Objective/Assessment/Plan）+ 鉴别诊断（DDx）+ 循证医学五级证据
- 结构：Case × Sign → Diagnosis（tier 1，附 DDx 排除树）→ Syndrome（tier 2）
- 锚点：ICD-10 / ICD-11 / SNOMED CT / PubMed PMID
- 交付物：SBAR 汇报（Situation-Background-Assessment-Recommendation）

### 8.3 透镜贡献协议（v2.2+）

`docs/lens-contribute.md` 定义：社区可贡献新透镜。要求：
- 基于公开出版的成熟理论（≥10 年学术验证）
- 至少 3 名相关领域专业人士背书
- 提供 30+ 条种子数据 + 10+ 个示例涌现聚类
- 通过 Bab-ilu 维护团队的 lens-review

---

## 9. Prompt / 交付物（按透镜变形）

每个透镜在 `lens.yaml` 里声明自己的 `deliverable_types`。`/prompt <target>` 的输出格式由透镜决定。

| 透镜 | `/prompt` 默认交付物 |
|---|---|
| aesthetic-warburg | 四段式生成 prompt（给 Midjourney/Sora/Kling） |
| engineering-alexander | Pattern 卡片（Problem/Context/Forces/Solution/Consequences） |
| general-zettelkasten | Progressive Summary（3 级递进摘要 + Bloom 层级标签） |
| science-kuhn | Hypothesis + Falsification Plan |
| finance-minsky | Cascade Risk Report |
| law-irac | IRAC Memo |
| medicine-soap | SBAR + DDx Tree |

**共同骨架**：所有透镜的 prompt 输出都分两版：
1. 完整带结构标签的 analysis 版
2. Clean 版（去标签的纯文本，直接 copy-paste）

---

## 10. 从 v2.0 → v2.1 的差分

v2.0 Sprint 1 已完成（15/15 任务；tag `v2.0-sprint1-complete`）。v2.1 是 v2.0 的**产品定位升级**——骨架完全保留，主要改动在 `.agent/lenses/` 这一层的引入。

| 层次 | v2.0 状态 | v2.1 改动 |
|---|---|---|
| `raw/` | 不变 | 不变 |
| `wiki/` 架构 | 硬编码为美学目录（works/motifs/pathosformel/topoi/people/sources/questions） | 目录名由 `vault_lens` 决定；美学透镜 vault 的结构与 v2.0 完全一致 |
| `.agent/schema.md` | 单一美学 schema | 泛化为透镜无关骨架；美学专属规则移到 `.agent/lenses/aesthetic-warburg/prompts.md` |
| `.agent/CLAUDE.md` | `vault_language:` | 加 `vault_lens:` + `vault_subdomain:` |
| `.agent/lenses/` | 不存在 | **新增**：7 个透镜配置（Sprint 2 ship 3 个：aesthetic/engineering/general；Sprint 5-6 加 4 个：science/finance/law/medicine） |
| `.agent/graph/` | motifs.md / pathosformel.md / topoi.md / anchors.md | 改名为 base.md / tier1.md / tier2.md / anchors.md（内容格式不变；只是命名泛化） |
| `.agent/spec/gap-algorithm.md` | 美学术语 | 泛化为 tier-0/tier-1-atom/tier-1-cluster/tier-2-cluster；算法本身不变 |
| `tools/graph_analyzer.py` | 不变 | 不变（本来就域无关） |
| 8 个命令 | 美学语境 | 接受 lens 配置；对美学 vault 行为与 v2.0 完全一致 |
| Seed kit | 一套美学 seed | 每个透镜有自己的 seed kit |

**向后兼容**：v2.0 的美学 vault 可以零成本升级到 v2.1——运行一次迁移脚本把 `vault_lens: aesthetic-warburg` 写入 CLAUDE.md，其他不变。

---

## 11. 外部依赖（继承自 v2.0 §11.4）

| 依赖 | v2.1 状态 |
|---|---|
| OmegaWiki | 作为硬分叉的血统源；v2.1 已完全重写为 lens-aware 架构，v2.2 删除了全部 legacy 学术管线（`fetch_*` / `research_wiki` / `reset_wiki` / `paper-*` / `exp-*` / `ideate` / `survey` / `novelty` / `rebuttal` / `refine` / `review` / `daily-arxiv` 全部 git rm） |
| InfraNodus SaaS / MCP server | 不依赖 / 不安装 |
| InfraNodus Obsidian plugin | 建议安装（可视化；不影响核心） |
| networkx + leidenalg | **必需**（/gap 用） |
| Getty AAT / Wikidata / Iconclass | 美学透镜的锚点源 |
| CVE / RFC / IETF | 工程透镜的锚点源 |
| DOI / arXiv / PubMed / ORCID | 科研/医学透镜的锚点源 |
| ICD-10 / SNOMED CT | 医学透镜的锚点源 |

---

## 12. 路线图

**v2.0 Sprint 1**：已完成（2026-04-18，tag `v2.0-sprint1-complete`）。骨架、schema、CLAUDE.md、`.agent/` 脚手架就绪。

### Sprint 2（v2.1 核心命令 + 3 个透镜 ship，~4 周，2026-04-21 启动）

**并行 track A：核心命令实现**
- `/genesis`（含 `--lens` 参数 + 5 问交互 + 透镜拷贝）
- `/ingest`（图/视频/PDF/URL；partial failure 恢复）
- `/taste`（接受透镜的 analysis_contract）
- `/gap`（tier 1 主路径 + tier 2 gated 架构）
- `/ask`（集成 ontology 查询 + 透镜 prompts.md 注入）
- `/prompt`（接受透镜的 deliverable_types）
- `/distill`（跨语言认知重构 + terminology.md）
- `/lint`（含 `--rebuild-graph` + 透镜 anchor 规则检查）

**并行 track B：透镜架构基础**
- `.agent/lenses/` 目录规范
- `lens.yaml` schema 定义 + 加载器（`tools/lens_loader.py`）
- 透镜 prompts 的运行时注入机制
- Seed kit 的透镜化（每透镜独立 seed）

**并行 track C：3 个首发透镜**
- `aesthetic-warburg`（迁移自 v2.0 硬编码）
- `engineering-alexander`（**第一个验证透镜通用性**；与 Warburg 并列交付）
- `general-zettelkasten-bloom`（fallback 透镜）

**Sprint 2 门禁**：
- 3 个透镜每个都能通过 `/genesis --lens=<id>` 正常初始化
- 3 个透镜的 seed kit 跑 `/ingest + /gap --tier=1` 至少涌现 1 个候选 cluster
- 所有 v2.0 测试（38/38）+ 新的透镜架构测试通过

### Sprint 3（v2.1 冷启动验证 + 手机远程迭代，~1 周）
- Phoenix dry-run 美学 vault（真实素材）+ 工程 vault（真实 codebase issue 史）
- 记录摩擦点；透镜 prompts 调优
- 手机端 Claude Code 远程操作流程验证

### Sprint 4（v2.1 公开发布准备，~1-2 周）
- 双语 README / CONTRIBUTING / INSTALL
- 三份快速上手指南（每透镜一份）
- v2.1 beta tag

### Sprint 5-6（v2.2 扩展透镜，~3 周）
- `science-kuhn` + `finance-minsky` 透镜 + seed
- `law-irac` + `medicine-soap-ddx` 透镜 + seed
- 透镜贡献协议 `docs/lens-contribute.md`

### 未来（v2.3+）
- Pinterest-style 视觉优先浏览（美学透镜专属）
- 逆向搜索（给输入，找 vault 里最相似节点）
- 多人协作 vault
- tier 3 聚类架构（`|tier-2| ≥ 15` 自动激活）
- 透镜组合（实验性，比如 aesthetic + engineering 的跨域 vault）

---

## 13. 词汇表（v2.1 新增）

| 术语 | 定义 |
|---|---|
| **Lens（透镜）** | 一个绑定到 vault 的知识组织框架配置，由 `.agent/lenses/<id>/` 定义。决定实体类型、聚类命名、阈值、分析契约、交付物格式 |
| **Tier-0** | 图谱底层节点（作品/事故/观测/事件/病例）。透镜特定的命名 |
| **Tier-1-atom** | 中层原子节点（母题/力/反常/机制/体征）。透镜特定 |
| **Tier-1-cluster** | tier 1 涌现聚类（Pathosformel / Pattern / Paradigm / Cascade / Doctrine / Diagnosis / Concept-Cluster） |
| **Tier-2-cluster** | tier 2 涌现聚类（Topoi / Pattern-Language / Revolution / Regime / Meta-Doctrine / Syndrome / Meta-Understanding） |
| **Analysis Contract** | 透镜对 `/taste`、`/prompt` 输出的强制结构契约（Panofsky 三层 / Alexander 四力 / Kuhn 三问 / ……） |
| **Deliverable Type** | 透镜声明 `/prompt` 的默认交付物（生成模型 prompt / Pattern 卡片 / Memo / SBAR / ……） |
| **Lens Anchor** | 透镜指定的权威术语/标识符来源（AAT / CVE / DOI / ICD-10 / ……）。在 `lens.yaml.anchors` 声明 |

其他术语（Work / Motif / Pathosformel / Nachleben / Gap / Ontology 文件 / Seed / 认知重构）继承自 v2.0 §13。

---

*本 PRD 是 v2.0 的定位升级。v2.0 骨架 + 算法 + vault 语言策略完全保留；核心改动是引入"学科透镜"作为产品一级概念。*

*修订历史：*
- *2026-04-17 v2.0 第一轮*
- *2026-04-17 v2.0 第二轮（7 项头脑风暴决议）*
- *2026-04-18 v2.0 Sprint 1 完成（tag v2.0-sprint1-complete）*
- *2026-04-18 v2.1 产品定位升级（透镜即脚手架，填补 Karpathy LLM-Wiki 对非结构化思考者的盲点）*
