# Bab-ilu

*你读过的书、看过的论文、存下的参考图、闪过又忘掉的念头——它们散落在 Notion、Markdown、iCloud、微信收藏里，互相不认识。*

Bab-ilu 让 Claude 在你本地把这些零散材料接成一张会自己生长的知识之网。你不用写一条 wikilink，不用维护一个交叉引用，不用整理一次目录——簿记全由 LLM 做。你只需要丢素材、问问题、做判断。

灵感来自 Andrej Karpathy 的 [LLM-Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：*知识库最累的部分从来不是读与想，而是簿记；而 LLM 最擅长簿记。* Bab-ilu 是这个想法的一个实现，另外加了两件 Karpathy 原文没有、但在这之上有用的延伸。

> v2.2 alpha · 2026-04-21 · 本地运行，素材不出你的机器 · [English](README.en.md)

---

## 一次普通会话

你过去一个月读了两本书，做了些笔记。一本是 Donald Schön 的《反思性实践者》，另一本是 Richard Sennett 的《匠人》。笔记散在几个 markdown 文件里，概念之间从未相互认识。

你打开 Claude Code，进入项目目录：

```text
你 ›       /ingest book-notes/
Claude ›   读完两份笔记。为每本书建了一条 source 条目，抽出七个概念
           （knowing-in-action、tacit-knowledge、craft-as-dialogue……），
           在 wiki/ 里铺好了交叉引用。两本书共享三个概念，自动相连。

你 ›       /ask 这两本书关于"专家怎么思考"的观点如何互补？
Claude ›   [一段六百字的综合，带具体页码引用]
           要把这次综合存为 wiki/syntheses/ 里的新页吗？(y/n)
你 ›       y

（你继续读别的。一周后又 ingest 了三份新笔记。）

你 ›       /gap
Claude ›   发现一个概念簇（专家知识 / 隐性技能 / 反思）没有和另一个概念簇
           （工匠实践 / 学徒模型）明示相连，可它们共享两条 Sennett 的引用。
           要不要替你建一条桥？

你 ›       /evolve-lens
Claude ›   观察到你近三个月的笔记一直围着同一个问题打转——"专家如何在行动中思考"。
           这个问题的结构和 Donald Schön 1983 年《The Reflective Practitioner》
           的三层框架（knowing-in-action / reflection-in-action / reflection-on-action）
           完全同构。要不要装一盏 schon-reflective-practice 的 lens，让之后的
           笔记按这三层自动归位？
```

从头到尾，你没写过一条 markdown，没维护过一条 wikilink，没画过一张脑图。Claude 替你做了全部簿记。你只做了三件事——选择读什么、问什么、接受什么。

---

## 如果你做视觉创作

电影、设计、建筑、插画、游戏原画——Bab-ilu 为你打磨了一盏深度更沉的 lens，叫 **aesthetic-warburg**。名字里的两个人是它的骨架：

**Aby Warburg**（1866–1929）是汉堡一个银行家的长子。成年那天他对弟弟说："家族的生意你全拿走，这辈子我买书你要付账。" 他靠这个交易活了一生，最后留下一座藏书几万卷的文化科学图书馆（今天在伦敦，仍然运作，叫 The Warburg Institute），以及一部未完成的遗作——《记忆女神图集》：近一千张照片和图像被他并置在六十三块黑板上，没有文字说明，只靠视觉的共鸣让观者自己看出——古希腊的一个舞者姿态、文艺复兴的圣经插画、十九世纪的邮票、同时代的米其林轮胎广告——**之间藏着同一个"情感公式"（Pathosformel），以不同外壳在两千年里一再重生（Nachleben）。** Warburg 相信：图像之间可以自己说话，只要你把它们放得够近、够多。

**Erwin Panofsky**（1892–1968）是 Warburg 在汉堡的年轻同事，后来被纳粹赶到美国，在普林斯顿高等研究院把 Warburg 的直觉磨成了一套严谨的分析框架。他 1939 年的《图像学研究》提出读一张图要分三层：先读它作为形式事实是什么（前图像志），再读它的文化典故是什么（图像志），最后读它透露出一个时代的世界观是什么（图像学）。这三层今天是全世界艺术史研究生院的基础课。

他们两人加起来把"怎么系统地读一张图像、怎么追踪一个视觉母题跨越时代的迁移"做到了人类能做到的最高水平。**Bab-ilu 不发明新方法——只把他们的方法装进 LLM 循环里。** 你即将看到的 `/taste` 三层输出，是 Panofsky 1939 年的分析框架；你会看到的 Pathosformel / Nachleben / Mnemosyne Panel，是 Warburg 的本名。

你丢一张剧照进来：

```text
你 ›       /taste raw/images/blade-runner-2049-orange-void.jpg
Claude ›
  前图像志 · 一个人物的背影，站在大片橙色光雾里。构图单体中景偏右，
             水平地平线压在下三分之一，色温极度统一。
  图像志   · "Rückenfigur"——背身人物。这是 Caspar David Friedrich
             1808 年《海边的僧侣》确立的德国浪漫主义公式：一个人面向无限，
             观者的目光越过他的肩膀看出去。Villeneuve 在 Blade Runner 2049
             里重新激活了这个公式。
  图像学   · 这是 Warburg 意义上的 Pathosformel——一个跨越两百年的
             情感公式。它携带的不是浪漫主义的图像学内容，而是"个体
             面对无限"这个姿势结构。从 Friedrich 到 Tarkovsky《潜行者》
             到 Villeneuve，同一公式活在不同的文化载体里。

  在 motifs/ 里建了 rueckenfigur-modern；
  在 pathosformel/ 里建了 sublime-solitude-against-void panel；
  Nachleben 引用链连到 friedrich-monk-by-sea、tarkovsky-stalker-zone。

你 ›       /prompt rueckenfigur-modern ui
Claude ›   为 UI 模态生成了一份四段式的 Midjourney 提示词。要点：这份提示词
           不是在复制任何一张具体的图，它在告诉生成模型——请画一张
           "站在这个 Pathosformel 谱系里"的新图。电影帧的权威锚点用
           IMDB（tt1856101）；跨媒介 motif 的锚点走 Wikidata 与 Getty AAT。

你 ›       /gap
Claude ›   这个 panel 目前三个成员——Friedrich、Tarkovsky、Villeneuve，
           全是西方与俄国。这个 Pathosformel 在东亚视觉传统里的变体——
           浮世绘里的"遥望"主题、宋元山水里的点景人物——还没进 vault。
           要我生成一条素材请求吗？
```

从 ingest 到可以拿走的 AI 提示词，再到发现谱系里还缺哪一块——全程没写一句簿记。

别的 lens 暂时还做不到这种厚度——不是技术做不到，是需要把 Warburg 一百多年的学术传承、Panofsky 的三层框架、Getty 的 AAT / Iconclass / ULAN 机构锚点体系、以及把概念反向产成生成模型提示词的管道，一笔笔接进来。第一个做好的是美学，因为视觉分析是最难的；其他领域会跟上。

---

## 和 ChatGPT 聊天的区别

每次你关掉 ChatGPT 的对话框，你问过的问题、发现的连接、整理的笔记都消失了。下次从零开始。

Bab-ilu 让 LLM 把每一次发现都写进一张持久的、会交叉引用的本地 wiki 里。你的知识在每次使用中复利生长——一年之后你的 vault 比一年前厚十倍，不是因为你勤快，而是因为 LLM 不会厌倦簿记。

---

## 快速上手

需要 Python 3.10 或更新，以及 [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) 或 Codex。Bab-ilu 的工作流入口要在 agent 对话里输入，不是在 bash 里直接执行：Claude Code 用 `/genesis` 这类 slash 命令，Codex 用 `$genesis` 这类 skill 调用；不需要 `ANTHROPIC_API_KEY`，推理在当前会话内完成。读 vault 用你喜欢的任何 markdown 编辑器——Obsidian、VSCode、Zed 都可以。Codex 用户可直接看 [docs/codex-quickstart.md](docs/codex-quickstart.md)。

```bash
git clone https://github.com/<your-username>/bab-ilu.git
cd bab-ilu
pip install -r requirements.txt
```

然后进入 agent 会话，在对话里输入对应运行时的入口：

```text
Claude Code:
/genesis
/ingest raw/stuff/
/ask "..."

Codex:
$genesis
$ingest raw/stuff/
$ask "..."
```

`/genesis`（在 Codex 中对应 `$genesis`）会问你五件事：vault 语言，选哪盏 lens，工作方向，要不要装 demo 种子，现在就 ingest 素材吗。装 demo 种子会给你三到五条示例条目，五分钟就能看出 Bab-ilu 是怎么工作的。

---

## 工作流入口

| Claude Code | Codex | 做什么 |
|---|---|---|
| `/genesis` | `$genesis` | 建一个新 vault |
| `/wx2md-worker <mp.weixin.qq.com URL>` | `$wx2md-worker <mp.weixin.qq.com URL>` | 把微信公众号文章通过 worker 固化到 `raw/articles/`，再决定是否 ingest |
| `/ingest <path>` | `$ingest <path>` | 把素材写进 vault——原件入 `raw/`，LLM 分析入 `wiki/` |
| `/ask <问题>` | `$ask <问题>` | 用自然语言查 vault，答案可归档为 syntheses 里的新页 |
| `/gap` | `$gap` | 让 Claude 找你还没注意到的概念簇之间的缺失连接 |
| `/lint` | `$lint` | vault 健康审计：矛盾、过时、缺失素材、孤立节点 |
| `/distill <source>` | `$distill <source>` | 把非母语素材在你自己的 schema 里重新搭一遍（不是翻译） |
| `/prompt <entity>` | `$prompt <entity>` | 把一个概念或笔记变成可用的 Midjourney / Sora 提示词 |
| `/taste <image>` | `$taste <image>` | aesthetic lens 下跑 Panofsky 三层创意分析；其他 lens 下回归为该 lens 的分析报告模式 |
| `/evolve-lens` | `$evolve-lens` | 进阶：让 Claude 从你的使用模式里提议一盏新的 lens |

---

## Lens 的两层与成熟度

**预装层：成熟 lens**

- **aesthetic-warburg** 🏛 **旗舰** — 上面展示的那盏。接进了 Warburg 的方法、Panofsky 的三层、Getty 的 AAT / Iconclass / ULAN 机构锚点、Nachleben 谱系、反向提示词管道。47 份 seed-kit markdown、9 份 reverse-prompt 种子套件。压力测试通过证明——跨千年跨文明跨符号系统的视觉分析能跑顺，其他领域会更容易。

**预装层：管道已通，种子持续生长**

- **engineering-alexander** 🔧 — Christopher Alexander 的模式语言方向。29 份 seed-kit markdown，lens.yaml + prompts.md + examples.md 完整，3 份 reverse-prompt 模式卡种子（Context→Problem→Forces→Solution），专用抽取器 `tools/incident_extractor.py`。适合工程师做事故复盘、决策记录。
- **general-zettelkasten** 📇 — Luhmann 的卡片盒方法。29 份 seed-kit markdown，完整三件套（yaml + prompts.md + examples.md），3 份 progressive-summary 种子，专用抽取器 `tools/note_extractor.py`。万能兜底，适合任何学科快速起步。

这三盏不可能覆盖所有人。所以 Bab-ilu 有第二层，叫 LENS EVOLUTION：一个在后台看着你行为的 observer——你 ingest 什么、问什么、接受什么、拒绝什么。当它认出你的实际工作模式和某个有几十年学术传承的框架（Schön、Polanyi、Bourdieu、Merleau-Ponty……）结构同构时，会提议把那个框架变成一盏新 lens，装进你的 vault。

三条硬约束：不预设你是什么职业，不凭空发明框架（候选必须是真实学术传统，独立的第二次 LLM 核实引用真实性），不自动安装（总是提议，由你决定）。

这是 Bab-ilu 对 Karpathy 的核心延伸——Karpathy 让 LLM 做簿记，Bab-ilu 多做一步：让 LLM 认出你不自觉地在用哪种思考框架。

---

## 三层架构

```
raw/        你的原始素材；不可变，Claude 永远不碰
wiki/       LLM 写的人类可读层；markdown + wikilink，任何编辑器都能读
.agent/     机器记忆——图、schema、lens 配置、observer 的状态
```

---

## 常见问题

**我一定要用 Obsidian 吗？**
不。Bab-ilu 不挑编辑器。图谱本身不是给你看的——你通过 `/gap`、`/ask`、`/evolve-lens` 以语义的方式感受它在长，不用盯着节点和边。如果你喜欢可视化，Obsidian、VSCode 加 Foam 都能用。

**我的素材会上传到哪吗？**
不会。所有推理跑在你启动的那个 Claude Code 会话里，vault 是本地的 markdown 文件，从不离开你的机器。

**是不是只给视觉创作者用的？**
视觉创作者今天能吃到最深的一碗饭——美学 lens 是现阶段最成熟的一盏，拿来就能用。其他行业从 general-zettelkasten 起步，用一段时间让 LENS EVOLUTION 观察你，它会提议一盏专属你学科的真实学术 lens。视觉创作者今天吃到，其他行业几周后长出。

**要付 API 费用吗？**
不需要。所有 LLM 推理由你的 Claude Code 会话原生执行，没有外部 API 调用，所以也不需要 `ANTHROPIC_API_KEY`。

**和 Obsidian、Logseq、Notion 是什么关系？**
它们是读写工具，Bab-ilu 是写作工具——LLM 替你写 wiki、建 wikilink、做综合。你用 Bab-ilu 生产 vault，用 Obsidian 或其他任何编辑器读它。不冲突。

---

## 它不是什么

它不是 SaaS——本地跑，素材不出你的机器。它不是搜索引擎——你不是在"查已存信息"，你是在让素材之间长出结构。它不是写作辅助——它帮你发现，你自己的长文写在 `wiki/my/` 这个私有命名空间里，LLM 只读不写。它不需要 API key——Claude Code 会话里原生跑。

---

## 这个名字

Bab-ilu 是阿卡德语 *Bāb-ilu*——"神之门"，Babylon 最初的名字。用来暗示项目的野心：在不同语言、文化、领域的概念之间接线。是通天塔之前的 Babylon——那个还在连接的版本，还没被语言的混乱切开。

---

## 想再往下走一层

项目为什么这样设计——控制论加晚期维特根斯坦的理论基础、五条可操作原则、§0.5 的北极星命题——请看 [PRD-v2.1-zh.md](PRD-v2.1-zh.md)。

想贡献、改 bug、提 lens 候选——[CONTRIBUTING.md](CONTRIBUTING.md)。

---

## License

MIT · Copyright (c) 2026 Phoenix Ye and Bab-ilu contributors. 详见 [LICENSE](LICENSE)。

这个项目站在很多人的肩膀上。

Andrej Karpathy 给了 LLM-Wiki 的原型——raw / wiki / .agent 三层骨架是他先画出来的。Aby Warburg 让图像自己说话，Erwin Panofsky 教人怎么读——他们是美学 lens 的根。Christopher Alexander 给了工程 lens 的骨架（《模式语言》），Niklas Luhmann 给了兜底 lens 的方法（Zettelkasten）。

**特别致敬 [skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki)**——Bab-ilu 是它的硬分叉。v1.x 那套跑得通的 ingest / lint / check / graph 循环、skill 编排节律、原子写入与 log-append 纪律，都是 OmegaWiki 先把它做成了"可用"。v2.1 的 lens-aware 重写只是把那层底座改成了可替换的透镜——**没有 OmegaWiki 先把地基打好，Bab-ilu 就没有今天的第一天**。MIT 许可证兼容让我们可以正大光明地承认这份继承。

完整致谢在 PRD 里。
