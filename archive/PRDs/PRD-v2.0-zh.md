# Bab-ilu — PRD v2.0

> **日期**：2026-04-17（第二轮修订，应用 7 项头脑风暴决议）
> **状态**：彻底重构方案。v1.4 作废归档（见 §11）。
> **受众**：开源发布目标是视觉创作者、导演、设计师、美学研究者。中文作为参考实例语言，非全局默认。

---

## 0. 一句话定位

**Bab-ilu 是一个以 Warburg 方法为内核的美学发现引擎——它帮你在素材里发现别人没发现过的视觉共振，创作提示词是这个过程的可选副产物。**

---

## 1. 为什么要重构

v1.4 把自己建成了 OmegaWiki 的扩展——11 种 entity、12 种 relation、30+ 个 frontmatter 字段、25 个 skill、526 行 schema——这是一个**学术知识档案馆**的架构，不是**美学创作工坊**的架构。

三个结构性问题：

1. **它不知道自己的形状**。LLM 扫 wiki 回答问题时，产出的永远是"最可能的答案"——回归均值。没有机制感知拓扑空洞。Karpathy 自己承认了这个缺陷；InfraNodus 用知识图谱 gap 分析回答了它。
2. **"Prompt 作为终端交付物"把创作者降级成提词工程师**。导演的真痛点不是"给我一个 prompt"——Midjourney 默认 prompt 已经够用——是"我想做一个别人没拍过的镜头"，这需要发现、连接、拼贴。Warburg 1924 年在黑色面板上钉照片做的正是这个。
3. **人类可读和 agent 可读混在一个文件里**。一个 Aesthetic MD 的前 30 行是 YAML 字段，散文只占尾巴。打开 Obsidian 看到的是数据库报表，不是一篇可读的美学条目。

v2.0 的总纲：**图谱结构做 Warburg 方法的计算化身 · 人类层和机器层物理分离 · vault 语言策略支持跨语言认知重构**。

---

## 2. 核心哲学：三条硬约束

**① Warburg 方法优先于 wiki 惯例。** Pathosformel 是涌现的聚类，不是预设的 entity type。Nachleben（图像的"来世"）通过图谱的 gap 分析发现，不靠手填 `relations:` 字段。如果某个机制与 Warburg 方法的计算化冲突，砍掉它。**注意**：gap 分析是 Warburg 组合方法的计算化身，不等同于 Warburg 情感姿态学（Pathosformel 的命名和情感诠释仍需人类策展）。

**② 人类层与 Agent 层物理分离。** `wiki/` 是你在 Obsidian 里读的散文 + wikilinks；`.agent/` 是机器读的 ontology 文件、schema、状态（Obsidian 默认隐藏）。两层同步但互不污染。学术锚点（AAT / Iconclass / ULAN）**双层都保留**——人类散文里是可读脚注，机器 ontology 里是结构化关系（`[[motif]] [anchoredTo] aat:300015650`），以保证机器可查的完整引用链。

**③ Vault 语言是 per-vault 配置，不是全局默认。** `/genesis` 初始化时询问 vault 主体语言（中文 / 英文 / 西 / 法 / ……），写入 `.agent/CLAUDE.md` 的 `vault_language:` 字段；所有 agent 读此字段决定输出语言。跨语言源材料吸收时用 vault 语言**认知重构**（不是翻译）——留白 ≠ negative space 的翻译，是中国绘画传统里它本来应该怎么被理解。所有 motif 在图谱里一律对等，按文化来源分级会违反 Warburg 方法（反对按文化/年代分类）。

---

## 3. 用户体验：三个场景

### 3.1 第一次打开

`/genesis` 问你 4 个问题：

1. vault 主体语言？（中文 / 英文 / 其他）
2. 你的创作实践主场？（电影 / 摄影 / 绘画 / 建筑 / 平面 / UI / 游戏 / 综合）
3. 要不要导入演示 seed kit？（20-30 条公共领域策展美学条目，带 `seed: true` 标记，`/reset --seeds` 可一键删除）
4. 你已经有积累的素材吗？（如果有，当场跑 `/ingest`）

回答完成后你在 Obsidian 里打开 Bab-ilu 目录。左侧文件栏只显示三个顶级文件夹：

```
raw/          ← 你的素材（你丢进来的，系统不改）
wiki/         ← 你要读的
output/       ← 你要拿走的
```

你**看不到** `.agent/`（被 Obsidian 的 exclude files 规则隐藏）。

展开 `wiki/` 是八个子文件夹：

```
wiki/
  index.md            ← 这里有什么（Karpathy 式内容目录）
  log.md              ← 最近发生了什么（append-only 日志）
  _glossary.md        ← 术语表（第一公民，双语对照）
  works/              ← 具体作品：某幅画、某一帧、某个 UI 截图
  motifs/             ← 命名的视觉母题："北面窗光"、"倾斜脖颈的哀伤"
  pathosformel/       ← 涌现的 Pathosformel（tier 1 聚类，策展叙述）
  topoi/              ← 涌现的 meta-Pathosformel（tier 2，|pathosformel| ≥ 15 时自动激活）
  people/             ← 创作者：维米尔、塔可夫斯基、佐藤可士和
  sources/            ← 书、论文、机构档案、设计方法论
  questions/          ← gap 生成的开放问题
```

如果选择了 seed kit，此时 `wiki/` 非空——20-30 条带 `seed: true` 的条目覆盖 5-6 个 domain。否则是真正的空 vault（除 `_glossary.md` 和 `index.md` / `log.md` 外）。

右侧栏默认开着 InfraNodus Obsidian plugin，把 `motifs/` 和 `works/` 渲染成 3D 图谱。

### 3.2 往里丢素材

你把 20 张图片、3 篇 PDF、一个 Vimeo 链接丢进 `raw/`，对 Claude Code 说：

```
/ingest
```

十几分钟后：

- `raw/` 里的素材被整理（按类型、来源）
- `wiki/works/` 多了 20 个 work 页面（每个是一段 vault 语言散文 + 一张图 + 几个 `[[motif]]` 链接）
- `wiki/motifs/` 多了 30 个 motif 页面（部分新建、部分旧的加了新 work）
- `wiki/people/` 多了提到的创作者
- `wiki/log.md` 追加一行：`## [2026-04-17] ingest | 20 图 · 3 论文 · 1 视频 → 20 works · 30 motifs (8 新)`

你打开 Obsidian 的图谱视图，几十个新节点按文件夹上色（works 浅黄、motifs 浅蓝）。右侧栏的 InfraNodus gap 面板提示：*"motif 簇 A 和 motif 簇 B 之间只差 1 条边就连上了。要看吗？"*

### 3.3 日常工作

你在做一个短片，需要某种"暴雨中的爆发"的视觉。你对 Claude Code 说：

> "我想要 [[挥刀的游者\|wandering-blade]] 和 [[风暴作为宣泄\|storm-as-catharsis]] 这两条脉络的交汇点。给我几个还没被拍过的镜头构想。"

Agent 跑 `/gap` 定位这两个 motif 簇，跑 `/ask` 查 `wiki/works/` 里相关作品，返回：

> 黑泽明《七武士》最后一战有 wandering-blade + rain-as-memory，没有 storm-as-catharsis。
> 宫崎骏《幽灵公主》有 storm-as-catharsis + wandering-blade 但不在雨里。
> **没有任何现存 work 同时占据这三个 motif。你可能在踩一个原创点。**
>
> 三个具体镜头构想：……
>
> 要把这个 gap 记成 `wiki/questions/rain-catharsis-blade-convergence.md` 吗？我可以写段 Nachleben 评论。

你说要。一个新 question 页面诞生。未来如果你（或别人）往 vault 里加入填这个 gap 的素材，这个 question 可能升级为新的 Pathosformel。

---

## 4. 系统架构

### 4.1 完整目录

```
Bab-ilu/
├── raw/                         # 你的素材（不变）
│   ├── images/
│   ├── references/
│   └── notes/
│
├── wiki/                        # 人类可读（Obsidian 主视野）
│   ├── index.md                # 内容目录
│   ├── log.md                  # 时序日志
│   ├── _glossary.md            # 术语表（双语）
│   ├── works/                  # 具体作品
│   ├── motifs/                 # 视觉母题
│   ├── pathosformel/           # Tier 1 涌现的跨时代共振
│   ├── topoi/                  # Tier 2 涌现的 meta-Pathosformel（gated）
│   ├── people/                 # 创作者
│   ├── sources/                # 书、论文、机构档案、设计方法论
│   └── questions/              # gap 生成的开放问题
│
├── output/                      # 交互产物
│   ├── prompts/                # 生成提示词（Midjourney/Sora 等）
│   └── notes/                  # 你从系统里提炼的工作笔记
│
├── .agent/                      # Agent 可读（Obsidian 隐藏）
│   ├── schema.md               # ≤200 行契约
│   ├── CLAUDE.md               # ≤100 行项目说明（含 vault_language）
│   ├── graph/                  # Ontology 文件（机器图谱记忆）
│   │   ├── motifs.md           # Work × Motif bipartite 边
│   │   ├── pathosformel.md     # Pathosformel cluster 边（tier 1 输出）
│   │   ├── topoi.md            # Topos cluster 边（tier 2 输出）
│   │   ├── anchors.md          # AAT / Iconclass / ULAN 结构化锚点
│   │   ├── terminology.md      # 跨语言术语迁移决策
│   │   └── full.md             # 全图（由 /lint --rebuild-graph 派生）
│   ├── spec/                   # 技术规范
│   │   └── gap-algorithm.md    # 两阶段聚类算法正式规范
│   ├── skills/                 # Agent 命令定义
│   ├── subagents/              # 复合任务的子 agent
│   ├── mcp/                    # MCP server（llm-review 等可选附属）
│   ├── todos/                  # gap 驱动的研究清单
│   └── state/                  # 运行状态
│
├── archive/                    # v1.4 及历史归档
│   └── v1.4-vault-20260417.tar.gz
│
├── .obsidian/                   # Obsidian 配置（含 .agent/ 隐藏规则）
└── README.md                    # 对外（双语）
```

### 4.2 两层图谱架构

**基座：Work × Motif 二部图。** 两类节点，一类边：

- **Work**——具体作品/片段（维米尔挤奶女工、《1917》某一帧、iOS 启动页）
- **Motif**——命名的视觉操作（"北面窗光"、"倾斜脖颈的哀伤"、"作为仪式的劳作"）
- **边**：`Work exemplifies Motif`

基座是**严格二部**的。但从基座上派生出**涌现聚合节点**（Pathosformel、Topos），加上辅助节点（Person、Source），整个 vault 在存储层面是**多类型异构图**。聚类永远只在同类型节点子集上运行；聚合节点排除在被聚类输入之外（消除自循环 bug，见 §4.3）。

**从基座涌现**（tier 1，基座活跃）：

| 涌现对象 | 数学定义 | Warburg 对应 |
|---|---|---|
| Pathosformel | 一组 motif 通过共享足够多 work 形成的簇 | 一块 Mnemosyne 面板 |
| Nachleben | 一个 motif 的 work 集横跨多个时代 | 图像的"来世" |
| 原创点 | 一个孤立 work 同时承载多个平时不共现的 motif | 新 Pathosformel 的起点 |
| Gap | 两个 motif 簇之间几乎无 work 交集 | 未被连接的传统 |

**从 tier 1 涌现**（tier 2，`|pathosformel| ≥ 15` 时自动激活）：

| 涌现对象 | 数学定义 | 意义 |
|---|---|---|
| Topos | 一组 Pathosformel 通过共享足够多 motif 形成的簇 | 跨 Pathosformel 的 meta 级视觉-情感结构 |
| Meta-gap | 两个 Pathosformel 簇之间几乎无 motif 交集 | 可能通向的更深跨传统桥接 |

**架构无限扩展**：聚类规则通用化为 "每个 tier 只聚类同层同类型节点，排除所有上层聚合节点"。Tier N 输出是 Tier N+1 的输入。v2.0 ship 时 tier 1 活跃、tier 2 gated，tier 3+ 架构已就位等待未来数据。

### 4.3 涌现机制（两层通用）

**不手工创建 Pathosformel 或 Topos**。

**Tier 1 流程：**
1. `/ingest` 素材 → `works/` 和 `motifs/` 页面累积
2. `.agent/graph/motifs.md` 增量记录 `[[motif-a]] [coOccurs] [[motif-b]]` 和 `[[motif]] [exemplifiedBy] [[work]]`
3. 当一组 motif 满足**自适应阈值**（`k, l = max{3, ⌈log₂(n)⌉}`，默认种子 k=l=3）且聚类内部密度超过空模型期望的 3 倍时，agent 把候选写进 `.agent/todos/`
4. 你跑 `/gap`（或下次会话 agent 主动询问）：*"检测到一个候选 Pathosformel。要命名并创建页面吗？"*
5. 你同意、给个名字，agent 生成 `pathosformel/<slug>.md`——Nachleben 策展散文 + motif/work wikilinks
6. 新 Pathosformel 进入图谱，**但被从未来 tier 1 聚类输入中过滤**（消除自循环）

**Tier 2 流程（gated）：**
- 激活条件：`|pathosformel| ≥ 15`（或手动 `/gap --tier=2`）
- 输入：Pathosformel-Pathosformel 图，边 weight = 共享 motif 数的 Jaccard 归一
- 算法：与 tier 1 同构（Leiden on projection），阈值相应调整
- 输出：Topos 候选写入 `.agent/todos/`，用户命名后生成 `wiki/topoi/<slug>.md`
- Topos 节点从未来 tier 2 聚类输入中过滤

**撤销协议**：错误的 ontology 推断通过追加 retraction 行修正：`[[a]] [retracts-exemplifiedBy] [[b]] (ts=..., reason=...)`。`/gap` 在预处理时应用 retraction，保留 append-only 契约。

**没有 `generator_ready` flag、没有 `curator: llm|user`、没有手填 `members` 字段**。涌现的就是涌现的，人类只做命名和最终审查。

### 4.4 人类可读 vs Agent 可读的分离

#### 人类读的（`wiki/` 目录）

**一个 work 页面**：

````markdown
---
type: work
---

# 挤奶女工 — 维米尔，约 1657
*Rijksmuseum SK-A-2344 · 布面油画 · 45.5 × 41 cm*

![[vermeer-milkmaid.jpg]]

一个女人站在小窗旁，从陶罐往瓷碗里倒牛奶。房间素朴。光从左侧进。

四百年来这幅画不断回到电影、摄影、UI 设计里。为什么？

- [[北面窗光|north-light-domestic]]——背阳窗口的冷直光，荷兰室内画的签名
- [[静默的在场|contained-silence]]——开口会扰动某种看不见的东西
- [[作为仪式的劳作|manual-labor-sacred]]——平实动作被赋予仪式的重量

这是 [[静室之光|quiet-interior-light]] 的一个传承节点。

---
*[[维米尔|vermeer]] 作 · 另见 [[描绘的艺术|alpers-art-of-describing]] · Iconclass 41C32*
````

Frontmatter 就两行。其余信息全在散文 + wikilinks 里。

**一个 motif 页面**：

````markdown
---
type: motif
---

# 北面窗光
*north-light-domestic · AAT [300015650](http://vocab.getty.edu/aat/300015650)*

背阳窗口的冷直侧光。不扁平、不生硬——带出质感，不夸张。

维米尔把它写成法典。哈默修尔把它变成忧伤。迪金斯把它放进《1917》
的黎明农舍。UI 设计师在摄影式产品图里叫它 "ambient north light"。

## 出现在
- [[挤奶女工|vermeer-milkmaid]]
- [[哈默修尔的室内|hammershoi-interior]]
- [[1917 农舍黎明|deakins-1917-farmhouse]]

## 常与之同行
- [[静默的在场|contained-silence]]
- [[作为仪式的劳作|manual-labor-sacred]]

## 所属
[[静室之光|quiet-interior-light]]

---
*别名：冷侧光、维米尔式光线、北面窗光*
````

#### Agent 读的（`.agent/graph/`）

**`motifs.md`**（基座二部图 + motif-motif 共现）：
```
[[north-light-domestic]] [exemplifiedBy] [[vermeer-milkmaid]]
[[north-light-domestic]] [exemplifiedBy] [[hammershoi-interior]]
[[north-light-domestic]] [exemplifiedBy] [[deakins-1917-farmhouse]]
[[contained-silence]] [exemplifiedBy] [[vermeer-milkmaid]]
[[contained-silence]] [coOccurs] [[north-light-domestic]]
[[manual-labor-sacred]] [exemplifiedBy] [[vermeer-milkmaid]]
```

**`pathosformel.md`**（tier 1 聚类输出）：
```
[[quiet-interior-light]] [cluster] [[north-light-domestic]]
[[quiet-interior-light]] [cluster] [[contained-silence]]
[[quiet-interior-light]] [cluster] [[manual-labor-sacred]]
```

**`anchors.md`**（结构化学术锚点，双层的机器侧）：
```
[[north-light-domestic]] [anchoredTo] aat:300015650
[[vermeer-milkmaid]] [anchoredTo] rijks:SK-A-2344
[[vermeer-milkmaid]] [anchoredTo] iconclass:41C32
[[vermeer]] [anchoredTo] ulan:500024067
```

这些是 LLM 做 gap 分析时读的。**增量追加，永不整体重写**（InfraNodus 规则）。retraction 通过追加行实现，不改旧行。

**Ontology 与 wiki 的同步**：wiki 是散文层源头。`/ingest` 写 wiki 时同步写 ontology；`/lint --rebuild-graph` 从 wiki wikilinks 全量重建权威 `.agent/graph/full.md`（衡量 wiki 和增量 ontology 的漂移）。LLM 推断的 motif-motif 共现、cluster 关系只存在于 ontology 侧，append-only 计算，不从 wiki 派生。

---

## 5. 命令表

从 v1.4 的 25 个 skill 砍到 **6 个核心 + 1 个初始化 + 1 个辅助**：

| 命令 | 做什么 | 读 | 写 |
|---|---|---|---|
| `/genesis [--seeded]` | 首次初始化 vault；交互式问 4 个问题（vault 语言、创作主场、seed 选项、已有素材），创建目录结构 + `.agent/` 脚手架 + `.obsidian/` 配置。`--seeded` 导入 Bab-ilu 项目维护的公共领域 seed kit | 无 | 全部初始结构 |
| `/ingest <path 或 query>` | 吃素材 → 生成 work/motif 页面 + 更新 ontology | `raw/` | `wiki/` + `.agent/graph/` + `wiki/log.md` |
| `/taste <image 或 file>` | 单张图做美学分析：提议 motif（不落盘，等你决定） | 图像 + 现有 motif 库 | 仅对话 |
| `/gap [--tier=1\|2\|all]` | 跑 gap 分析 → 生成 questions + 写入 todos；默认 `--tier=1`；`--tier=2` 需数据满足激活条件 | `.agent/graph/*` | `wiki/questions/` + `.agent/todos/` |
| `/ask <问题>` | 查询 vault，合成带引用的 vault-语言答案；可选落盘为新 wiki 页 | `wiki/` + `.agent/graph/*` | 可选 `wiki/` |
| `/prompt <work/motif/pathosformel/topos>` | **可选**下游：为生成模型产出英文 prompt | `wiki/` 目标节点 + 相邻节点 | `output/prompts/` |
| `/distill <source-path>` | 跨语言源材料的认知重构；更新 terminology.md | 外文 source | `wiki/sources/` + `.agent/graph/terminology.md` |
| `/lint [--rebuild-graph]` | 健康检查：孤儿页、ontology/wiki 不一致、stale 引用 | 全 vault | 修补 wiki/ontology，报告未决 |

v1.4 继承的 18 个 OmegaWiki 学术 skill **全部下架到 `.agent/skills/legacy-academic/`**——可选启用，不是主线。`/research`（带 MCP llm-review 的学术文献搜索）作为可选辅助保留，审计员推荐未来可能恢复 `/survey`、`/novelty` 为一等公民（见 §12 未来特性）。

---

## 6. Vault 语言策略

### 6.1 原则：vault 语言 per vault，认知重构不是翻译

`/genesis` 初始化时问："这个 vault 的主体写作语言是什么？"用户回答（中 / 英 / 西 / 法 / 日 / ……）写入 `.agent/CLAUDE.md` 的 `vault_language:` 字段。所有后续 agent 行为读此字段决定 prose 输出语言。

跨语言吸收外文源材料时，agent **不翻译**——用 vault 语言的思维词汇**重新构造**意义。

对照（vault 语言为中文时）：
- 坏：*"the negative space carries the composition"* → "消极空间承载了构图"
- 好：*"the negative space carries the composition"* → "这幅画的**留白**是整个构图的骨架"

"留白"不是"negative space"的翻译，是中国绘画传统里它本来应该怎么被理解。反过来，vault 语言为英文时遇到"留白"，也不简单译为 negative space——用描述性英文保留 pinyin 锚点（`liubai (intentional negative space, Chinese painting tradition)`）。

### 6.2 语言分工矩阵

| 层 | 语言 | 理由 |
|---|---|---|
| 文件名（slug） | 英文 kebab-case（或 pinyin/其他罗马化） | 稳定机器身份；跨平台/CLI/git 安全；建立后不改 |
| 页面标题 + 正文 | vault 语言 | 你的读物 |
| Wikilinks 显示 | `[[vault-语言显示\|english-slug]]` | Obsidian 管道语法：链目标是 slug，显示是 vault 语言 |
| Frontmatter 字段名 | 英文 | 机器契约 |
| Frontmatter 字段值 | 按字段语义 | `type: work`（英）；`title: 挤奶女工`（vault 语言） |
| Ontology 文件 | 英文关系码 + 英文 slug | 机器读，人类不开 |
| 学术锚点（AAT/Iconclass/ULAN） | 英文原文保留 | 国际标准术语，相当于拉丁学名 |
| 生成 prompt（给模型） | 英文 | 生成模型是英文训练的；AAT 词汇是英文标准 |
| 围绕 prompt 的说明 | vault 语言 | 你要读的 |
| schema.md / CLAUDE.md | 双语 | vault 作者读 vault 语言侧，开源读者读英文侧 |
| README.md | 双语 | 对外入口 |
| `wiki/_glossary.md` | 双语条目 | 对非母语英文读者的术语桥梁 |

### 6.3 词表覆盖是工程问题，不是身份等级

所有 motif 在图谱里对等。AAT / Iconclass / ULAN 是**可选的命名规范**——覆盖时锚定，未覆盖时用描述性标题 + 可选 english_alias。这条规则对所有来源的 motif 一视同仁，不按文化分级。

词表覆盖的常见未覆盖区包括但不限于：
- 中国/日本/印度等非西方传统美学概念（留白、写意、侘寂、rasa）
- 亚文化与新兴媒介（游戏美学、迷因视觉语法、TikTok 剪辑风格）
- 被主流研究低估的传统（非洲雕塑语法、拉美魔幻现实主义视觉）
- 尚未被 AAT 收录的当代现象（AI 生成美学本身）

对所有这些，处理方式相同：
- slug 用罗马化（kebab-case 英文或 pinyin）
- 标题用 vault 语言描述
- `english_alias` 给描述性英文短语（不假装它是 canonical）
- 生成 prompt 时直接用 slug + 括号解释：`liubai (intentional negative space, Chinese painting tradition)` / `wabi-sabi (imperfect weathered beauty, Japanese aesthetic)`

v1.4 的 hard rule "至少一个 authoritative anchor non-null" 废除——改为 `/lint` 的软提醒：**仅在 agent 判断词表应该覆盖此 motif 却未成功解析时才提示**。

### 6.4 `/distill` 与术语决策

`/distill <source-path>`：Agent 读外文源材料 → 用 vault 语言认知重构写到 `wiki/sources/` → 显式做**概念迁移判断**：

- 哪些术语保留原文（AAT 锚点）
- 哪些改写为 vault 语言传统对应词（留白 ↔ negative space）
- 哪些需要描述性再表达

每次判断记到 `.agent/graph/terminology.md`，字段：`source_term` / `target_term` / `scope` / `counter_usage` / `reviewer`。形成活的跨语言术语对照表。下一次遇到同一概念时 agent 先查这张表，保持术语一致性。

### 6.5 `wiki/_glossary.md` ——开源读者桥梁

vault 级第一公民词表。`/genesis` 生成基础版（Work/Motif/Pathosformel/Topos/Nachleben/Gap 等核心术语），用户可增补 vault 特有约定。格式：

```markdown
## Pathosformel（情感公式 / 视觉形态）

瓦尔堡术语。指跨时代反复出现的视觉-情感公式——一种姿势张力、
构图势能或情感配方，它迁移、变形、在不同文化语境里重现。

在 Bab-ilu 里，Pathosformel 不是预设类别，而是由 /gap 分析从
motif 共现中涌现的簇（tier 1 输出）。

学术出处：Aby Warburg, Mnemosyne Atlas (1924-29); Gombrich,
Warburg Intellectual Biography (1970).

例子：wiki/pathosformel/quiet-interior-light.md
```

---

## 7. 图谱与 Obsidian

### 7.1 InfraNodus Obsidian plugin 集成

**装 InfraNodus 的 Obsidian 插件**（免费；AI 分析需自备 API key）。它把你的 `wiki/` 里的 `[[wikilinks]]` 和未显式链接的概念一起渲染成 3D 图谱。

**不依赖 InfraNodus SaaS/MCP server**。Bab-ilu 的 `/gap` 命令自己实现结构分析（读 `.agent/graph/*.md` + networkx + Leiden），InfraNodus 插件只负责**可视化**。这符合 Path B 的承诺：借鉴架构，独立实现。

### 7.2 Graph 视图配色（Obsidian 原生 Graph View）

`.obsidian/graph.json` 按文件夹上色：

| 文件夹 | 颜色 | 语义 |
|---|---|---|
| `works/` | 浅黄 | 具体作品 |
| `motifs/` | 浅蓝 | 抽象视觉操作 |
| `pathosformel/` | 深红 | Tier 1 涌现的跨代结构 |
| `topoi/` | 深紫 | Tier 2 涌现的 meta 结构 |
| `people/` | 灰 | 创作者 |
| `sources/` | 浅绿 | 学术/机构档案 |
| `questions/` | 橙 | 带注意力的 gap |

打开 Graph View 就能看到分层结构——黄色 work 节点环绕蓝色 motif 节点，红色 pathosformel 是星团中心，深紫 topos 是星系中心。

### 7.3 Wikilink-only 写作规则

所有跨页面连接**必须**用 `[[wikilinks]]` 写在散文里，**不在 frontmatter 的 `relations:` 块里**。两个效果：

1. Obsidian 图谱视图自然绘制
2. 人类读散文就能看到连接，不用去读 YAML

Frontmatter 只保留**不可从散文/wikilinks 推导的信息**（类型、创作日期等），大部分页面只有 1-3 行 frontmatter。

---

## 8. 学术锚点

三个学术传统继承自 v1.4，但**从 frontmatter 字段升级为双层架构**（散文脚注 + 机器结构化关系）。

### 8.1 Warburg：Nachleben 驱动 `/gap`

schema.md 的 Warburg 章节用 vault 语言讲清楚 Pathosformel 和 Nachleben 原则，agent 读这段在做 gap 分析时内化：**"这个 motif 是哪个 Pathosformel 的实例"**，不是"这属于什么风格类别"。

**边界声明**：Bab-ilu 的 bipartite 图 + Leiden 聚类是 Warburg 组合方法的计算化身，**不是** Warburg 情感姿态学（Pathosformel 作为情感公式的语义诠释）的替代。命名 Pathosformel、撰写 Nachleben 评论、判断哪个聚类有情感连续性——这些仍然是人类策展劳动，算法只提供候选。

### 8.2 Panofsky：三层做分析透镜，不做字段

v1.4 在每个 aesthetic MD 塞 `panofsky_layer: iconographic` 字段——这是把分析方法论降格成数据标签。v2.0：**Panofsky 三层（pre-iconographic / iconographic / iconological）作为 `/taste` 和 `/prompt` 的强制输出契约**。`/taste` 分析一张图必须分三段：看见了什么（pre-iconographic）/ 这在文化里叫什么（iconographic）/ 这暗示什么世界观（iconological）。`/lint` 检查 motif 页面散文是否视觉上区分了三层（不混为一团形容词），保持分析纪律。

### 8.3 AAT / Iconclass / ULAN：双层锚点

**人类层（散文脚注）**：Motif 页面的副标题引用 AAT ID。Iconclass 在画作/插画/摄影 work 的脚注里引用。ULAN 在 person 页面的脚注里引用。都是 human-readable 脚注格式。

**机器层（`.agent/graph/anchors.md`）**：同时结构化保存为 `[[motif]] [anchoredTo] aat:300015650`、`[[work]] [anchoredTo] rijks:SK-A-2344`、`[[person]] [anchoredTo] ulan:500024067`。这让机器图谱能够机器可查地追踪引用链——学者提问"你这个 Pathosformel 的每个 work 的机构编号是什么"时，系统可直接从 anchors.md 导出完整引用表。

**双层同步**：`/ingest` 和 `/distill` 写散文脚注时同步写 anchors.md。`/lint` 跑 hash 对比，报告不一致。

Agent 的词表解析过程（"这个 motif 可能对应 AAT 300015650"的判断）记录在 `.agent/state/vocabulary_resolution.md`，用户不需要看。

---

## 9. 生成 prompt：作为下游可选输出

### 9.1 触发时机

**不在 ingest 时自动生成**（v1.4 每个 aesthetic MD 自动生成三模态 prompt 的设定废除）。

Prompt 是用户**需要**时才调用 `/prompt <target>` 生成，落在 `output/prompts/YYYY-MM-DD-<slug>.md`。

### 9.2 结构骨架（Panofsky 三层）

生成的 prompt 带四段式标签：

```
[pre-iconographic] 具体视觉/感官规格（色、光、构图、材质、景别）
[iconographic] 文化/时代/类型标记（wardrobe、建筑、道具）
[iconological] 情绪/世界观/内在含义
[lineage] Pathosformel / AAT term / signature author
```

这四段不是装饰——是让 Midjourney v6+、Flux、Sora、Kling 从"风格词堆砌"跳到"组合式视觉语法"的结构骨架。

**输出双版本**：
1. 完整带标签的 analysis 版（给人阅读、理解系统判断）
2. **Clean 版**（去除所有 `[pre-iconographic]` 等标签后的纯 prompt 文本），供直接 copy-paste 到生成模型

### 9.3 模态

`/prompt` 接收目标类型参数，决定模态：

| 目标 | 默认模态 | 兼容模型 |
|---|---|---|
| `image` | 静态图像 | Midjourney v6+ / Flux / Nano Banana / Stable Diffusion |
| `video` | 视频 | Runway Gen-3 / Sora / Kling / Pika |
| `ui` | UI 设计 token + 引用谱系 | 给 Claude Code / Cursor 做前端实现 |
| `motion` | UI 微交互时序 | AE / Rive / Lottie / Framer Motion / CSS |

（v1.4 的 `ux_flow` 和 `painting` 模态**暂时收起**——等有真实用户需求和配对评估数据再加回。YAGNI。）

---

## 10. 被裁掉的东西（v1.4 → v2.0）

| v1.4 机制 | 处置 | 理由 |
|---|---|---|
| 11 种 entity type | 缩到 6 种（work / motif / pathosformel / topos / person / source / question） | aesthetic 拆为 work + motif；idea/experiment/claim/summary/concept 不是美学图谱的核心 |
| 12 种 relation type | 全部移到 wikilinks + ontology 关系码 | 关系在散文里是 `[[link]]`，在机器图谱里是 `[relationCode]`，不再是 frontmatter 字段 |
| 30+ frontmatter 字段 | 每种类型 ≤3 字段 | 信息搬到散文/wikilinks/ontology 里；frontmatter 只留"不可推导的元数据" |
| v1.4 hard rule "至少一个 authoritative anchor" | 降为 `/lint` 软提醒（且仅在词表应覆盖却未解析时触发） | 词表覆盖是工程问题，不是身份等级 |
| `panofsky_layer` 字段 | 删 | Panofsky 方法论升级为 `/taste` + `/prompt` 的强制输出契约，不做数据标签 |
| 16 个可选博物馆 ID 字段 | 删除字段，保留脚注 + 结构化 anchors.md | 双层锚点架构代替字段堆砌 |
| `_refs/_spine/_institutions/_domains/` 结构 | 合并到 `wiki/sources/` | 对用户呈现一个扁平 sources 目录就够 |
| 现有 6 个 panel MD + 34 个 aesthetic MD + 13 个 _refs MD + 8 个 people MD | **全归档**（`archive/v1.4-vault-*.tar.gz`） | 决议 5：现有内容是 v1.4 实验产物，非严格策展；v2.0 从零开始 |
| 每个 aesthetic 自动生成三模态 prompt | 改为按需 `/prompt` 调用 | YAGNI + 解耦 |
| `ux_flow` / `painting` prompt 模态 | 暂时收起 | 没有配对评估数据 |
| 18 个 OmegaWiki 学术 skill | 下架到 `.agent/skills/legacy-academic/` | 不是主线；可选启用。审计员标注 `/research` / `/survey` / `/novelty` 未来可恢复为一等公民（见 §12） |
| `taste-icon` / `taste-lineage` / `taste-synthesis` 三段式 subagent | 废除，重设计为整体 subagent | 新架构里 `/taste` 是整体动作，不是流水线 |
| 14 个 Python 工具 | 保留 `graph_analyzer.py`（大幅重构为 Leiden + Jaccard projection）+ `lint.py`（重写），其余删 | 对齐新命令表 |
| MCP `llm-review` server | 保留但降级为 `/research` 可选依赖 | 学术 skill 下线后的附属品 |
| `mcp-servers/` 目录 | 移入 `.agent/mcp/` | 不污染顶级视野 |

---

## 11. 迁移方案

### 11.1 代码：彻底重做

- `.claude/skills/` 全部重写（25 → 8）
- `.claude/agents/` 全部重写（4 → 2-3，具体见 §12 Sprint 2）
- `tools/` 只保留 `graph_analyzer.py`（重构为 Leiden + Jaccard 投影，支持 tier 1/tier 2）+ `lint.py`（重写）
- `schema.md` 从 525 行重写到 ≤200 行
- `CLAUDE.md` 从 164 行重写到 ≤100 行
- `PRD.md`（英文镜像）从本 PRD 翻译后**人工校验**产出
- `tests/` 重写：skill-structure 测试（7 个 skill × 1 测试）+ `/gap` 算法确定性测试（tier 1 + tier 2）+ LLM 输出 snapshot 测试（合成 fixtures）

### 11.2 内容：全归档

**v2.0 内容层从零开始。** v1.4 的 89+ 个 MD 文件（6 panel + 34 aesthetic + 13 \_refs + 8 people + misc）打包归档为 `archive/v1.4-vault-20260417.tar.gz`，不做字段级迁移。决议 5 的理由：现有条目是 v1.4 实验性产出，策展深度不足以作为 v2.0 样本。

**例外**：`.github/workflows/daily-arxiv.yml` 依赖 `tools/fetch_arxiv.py`。v2.0 删除 fetch_arxiv.py 时同步禁用或删除 workflow，防止 CI 08:00 每日静默失败。

### 11.3 Seed kit（作为冷启动策略）

v2.0 附带一个**独立维护的** seed kit 仓库（`seed-kit/`），作为 Bab-ilu 项目的公共资产：

- 20-30 条公共领域策展美学条目
- 覆盖 5-6 个 domain（painting / cinema / photo / architecture / graphic / ui）
- 每条带 `seed: true` frontmatter + `#seed` Obsidian 标签
- 学术锚点完整（AAT / Iconclass / ULAN 全部解析到）
- 公共领域图像或 Wikimedia Commons 授权图像
- `/reset --seeds` 可一键删除所有 seed 条目

`/genesis --seeded` 在初始化时拷贝 seed-kit 内容到当前 vault 的 `wiki/` 下。seed 条目在 Obsidian 图谱视图可用过滤开关"hide seeds"隐藏。

**Seed kit 作为开源资产的价值**：
1. 新用户第一天就有可交互图谱，不至于"空 vault 三小时后流失"
2. 演示 v2.0 架构的真实运作（Work / Motif / Pathosformel / Topos 的具体样子）
3. 未来可扩展：`/seed-contribute` 让社区用户贡献策展条目（需审查）

### 11.4 外部依赖

| 依赖 | v1.4 状态 | v2.0 状态 |
|---|---|---|
| OmegaWiki（skyllwt/OmegaWiki） | 硬 fork 基座 | 不再视为基座，legacy skill 可选启用 |
| InfraNodus SaaS | 未使用 | **不依赖** |
| InfraNodus MCP server | 未安装 | **不安装**（违反 Path B） |
| InfraNodus Obsidian plugin | 未安装 | **建议安装**（可视化用；不影响核心功能） |
| Getty AAT / Wikidata / Iconclass | 手动引用 | 双层锚点架构（散文脚注 + `.agent/graph/anchors.md`） |
| networkx + python-louvain / leidenalg | 未依赖 | **新增依赖**：用于 `/gap` 的图谱分析 |
| `llm-review` MCP | 学术 skill 核心 | 降级为 `/research` 附属，默认不启用 |

---

## 12. 路线图

**实际总估：7-8 周**（PRD 原 5 周）。审计员估 8-9 周，决议 5 的全归档把 Sprint 3 从 1.5 周缩到 3-5 天，抵消了决议 3 的 tier 2 架构代价。

### Sprint 1（重构骨架，~1 周）
- [ ] `.agent/schema.md` 重写到 ≤200 行（含 §2 三条硬约束、§4 两层架构、§6 vault 语言策略、§8 学术锚点 prompt）
- [ ] `.agent/CLAUDE.md` 重写到 ≤100 行，含 `vault_language:` 字段规范
- [ ] `.agent/spec/gap-algorithm.md` 编写：正式规范 Leiden + Jaccard 投影 + 自适应阈值 + 聚合节点过滤 + retraction 协议（Sprint 2 前必完成）
- [ ] `wiki/` 新目录结构创建 + `index.md` / `log.md` / `_glossary.md` 初始化
- [ ] `.agent/` 目录脚手架（graph/、spec/、todos/、state/、skills/、subagents/、mcp/）
- [ ] `.obsidian/` 配置：exclude `.agent/`、graph 视图 7 色配色
- [ ] **Seed kit 初版**：20-30 条公共领域条目（以 painting + cinema 为主，其他 domain 各 2-3 条），测试 `/genesis --seeded` 加载机制
- [ ] v1.4 vault 打包归档为 `archive/v1.4-vault-20260417.tar.gz`
- [ ] 禁用/删除 `.github/workflows/daily-arxiv.yml`

### Sprint 2（核心命令，~4 周）
- [ ] `/genesis`（含交互式 4 问 + `--seeded` 选项）
- [ ] `/ingest`（支持图/视频/PDF/URL；partial failure 可恢复）
- [ ] `/taste`（单次整体分析，Panofsky 三层硬输出契约）
- [ ] `/gap`（tier 1：networkx + Leiden + Jaccard projection + LLM 验证命名层）
- [ ] `/gap --tier=2`（tier 2 gated 架构就位，触发条件逻辑完成；data 不足时返回"insufficient data"）
- [ ] `/ask`（集成 ontology 查询）
- [ ] `/prompt`（四段式骨架 + dual 输出）
- [ ] `/distill`（跨语言认知重构 + 更新 terminology.md）
- [ ] `/lint`（含 `--rebuild-graph`、双层 anchor 同步检查）
- [ ] Python 工具：`graph_analyzer.py` 重构 + `lint.py` 重写，其他删除
- [ ] 测试：skill-structure 测试、`/gap` tier 1/tier 2 确定性单元测试、LLM snapshot 测试（合成 fixtures）

### Sprint 3（冷启动验证与 seed kit 扩展，~3-5 天）
- [ ] `/genesis --seeded` 端到端验证
- [ ] Seed kit 扩展到 30 条，确保覆盖完整
- [ ] 跑 `/ingest` + `/gap --tier=1` on seed kit，验证 tier 1 能涌现至少 1 个候选 Pathosformel
- [ ] Phoenix 本人 dry-run：用 v2.0 重新 ingest 他的真实素材（不是 v1.4 的随便跑），记录摩擦点

### Sprint 4（母语化强化 + 学术锚点完善，~1-1.5 周）
- [ ] `.agent/graph/terminology.md` 初始化 30 条种子跨语言术语决策（以中-英为例）
- [ ] `.agent/graph/anchors.md` 完成 AAT/Iconclass/ULAN 双层同步逻辑
- [ ] `/distill` 端到端测试：吃一本英文美术史书 → 产出 vault 语言（中文）的 `wiki/sources/` 条目 + terminology.md 增量更新
- [ ] 跑 `/prompt` 验证英文生成 prompt + vault 语言框架双输出
- [ ] `wiki/_glossary.md` 扩展到 20+ 核心术语

### Sprint 5（观测、策展、开源准备，~1 周）
- [ ] InfraNodus Obsidian plugin 安装指南 + 配置模板
- [ ] `/lint --report` 生成可视化健康报告
- [ ] 导出 `output/notes/` 为外部可发布材料（moodboard PNG / PDF 网格）
- [ ] 双语 README.md / CONTRIBUTING.md / INSTALL.md
- [ ] Seed kit 贡献指南（`docs/seed-contribute.md`）
- [ ] v2.0 beta 公开发布

### 未来特性（v2.x，不在 v2.0 ship 范围）
- `/research` / `/survey` / `/novelty` 恢复为一等公民学术能力（需求：用户需要"这个发现是真的原创吗？"的学术验证闭环）
- Pinterest-style 视觉优先浏览模式（需求：导演审计员提的"我想先看图再读文字"）
- 逆向搜索（给一张外部图，找 vault 里最相似的 work 和 motif）
- 项目级作用域（`projects/<name>/` 子 vault，跨 vault 的 Pathosformel 共享策略）
- 多人协作与共享 vault
- meta-Topos（tier 3 聚类，`|topos| ≥ 15` 自动激活）

---

## 13. 附录：词汇表

| 术语 | 定义 |
|---|---|
| Work | 一个具体的视觉作品/片段：画、帧、UI 截图、照片 |
| Motif | 一个命名的视觉操作，跨作品可复用；对应 Pathosformel 的原子单元 |
| Pathosformel | Warburg 术语：跨时代重现的视觉-情感公式。在 Bab-ilu 里是 motif 的 tier 1 涌现聚类 |
| Topos | 古典学术语（复数 topoi）：更高一级抽象的反复出现的视觉公式。在 Bab-ilu 里是 Pathosformel 的 tier 2 涌现聚类 |
| Nachleben | Warburg 术语：图像的"来世"——视觉母题在不同时代的重现 |
| Gap | 图谱里两个簇之间的结构性空洞；可能暗示未被连接的传统或原创机会 |
| Tier | Bab-ilu 图谱的聚类层级：tier 1 = motif → Pathosformel；tier 2 = Pathosformel → Topos；可扩展到 tier N |
| 聚合节点 / Aggregate node | 聚类输出的节点（Pathosformel、Topos）。被从未来聚类输入中过滤，防止自循环 |
| Vault 语言 | Per-vault 配置的主体写作语言。写入 `.agent/CLAUDE.md` 的 `vault_language:` 字段 |
| 认知重构 | 从外文源吸收内容时用 vault 语言的思维词汇重写，不是翻译 |
| 学术锚点 | Warburg/Panofsky/AAT/Iconclass/ULAN——用作命名规范和推理透镜。双层存储：人类散文脚注 + 机器 `.agent/graph/anchors.md` 结构化关系 |
| Work × Motif 二部图 | Bab-ilu 基座图谱结构；一边具体作品，一边抽象母题。Tier 1 聚类的输入 |
| Ontology 文件 | `.agent/graph/*.md`，机器可读的图谱记忆，增量追加 + retraction 行 |
| Seed | `seed: true` frontmatter + `#seed` tag 标记的条目，来自 Bab-ilu 项目的 seed kit，可一键删除 |

---

*本 PRD 将作为 v2.0 重构的唯一权威文档。`.agent/schema.md` 从本 PRD 派生；实现计划从本 PRD 派生。v1.4 PRD（`PRD-zh.md` / `PRD.md`）保留为历史档案。*

*修订历史：*
- *2026-04-17 初版（第一轮起草）*
- *2026-04-17 第二轮（应用 7 项头脑风暴决议：citation chain C、gap algorithm C、Pathosformel B 架构+gated、vault 语言策略重写、PRD 自相矛盾清扫 + 全归档、sprint ~7-8 周、冷启动 seed kit B）*
