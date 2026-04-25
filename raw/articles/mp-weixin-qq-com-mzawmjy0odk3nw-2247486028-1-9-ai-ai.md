---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzAwMjY0ODk3Nw%3D%3D&mid=2247486028&idx=1&sn=b4283fe00981b9de4ccf4f15f7ea476b
canonical_url: https://mp.weixin.qq.com/s?__biz=MzAwMjY0ODk3Nw%3D%3D&mid=2247486028&idx=1&sn=b4283fe00981b9de4ccf4f15f7ea476b
source_domain: mp.weixin.qq.com
title: 用了 9 个月 AI 编程后，我只推荐这一套工作流——别让 AI 直接写代码
author: 
published_at: 
fetched_at: 2026-04-25T02:03:36Z
extractor: wechat_worker
content_hash: 07ee598554bf2dd47dd6fd1f8ab91e40c68c80f5d7d0d793bafae75614815216
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/iaDf0iaGn69rnXiaGsRQAp4fe1Lzl2EGRV2JFjTNSBkrqyV6qic5gCkB6p1VibTelL4ZaUfYyv9L1W7iaAATAobjHyHedVRicsehtSic37MdtHDuxHo/0.jpg) 

# 用了 9 个月 AI 编程后，我只推荐这一套工作流——别让 AI 直接写代码

原创 春秋 春秋 [ 春秋Daneel ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

# 你用 AI 写代码的流程是什么样的？

大概率是这样：打一段 prompt，等 AI 吐代码，看一眼，不太对，再改 prompt，再等，再看 循环几轮，代码勉强能跑，但你说不清它为什么这么写，也不确定改了会不会炸

更"高级"一点的玩家，可能在折腾各种 loop、MCP、自动化链路 但结果往往是一团乱麻，碰到稍微复杂的需求就崩

Boris Tane（Cloudflare 工程负责人）用 Claude Code 做主力开发工具用了 9 个月，总结出一套完全不同的工作流，核心原则只有一句话：

**永远不要让 AI 写代码，直到你审核并批准了一份书面计划**

把规划和执行分开，是他做的最重要的一件事 这样做能防止浪费精力，让你始终掌控架构决策，并且用更少的 token 产出明显更好的结果

我照着这套流程跑了一段时间，确实好用 今天把整个流程完整拆开讲清楚

干货向，建议收藏

---

## 工作流全貌

```
Research → Plan → Annotate（循环 1-6 次）→ Todo List → Implement → Feedback & Iterate

```

每个阶段都有明确的输入和输出，下面逐个拆

---

## 第一步：Research — 让 AI 先读懂代码，再做任何事

每次开始一个有意义的任务，第一件事不是让 AI 写代码，而是让它**深读**相关代码 而且必须把研究结果写进一个持久化的 markdown 文件里——不是在聊天里口头总结一下就完了

Boris 给出了几个他实际使用的 prompt：

> read this folder in depth, understand how it works deeply, what it does and all its specificities. when that's done, write a detailed report of your learnings and findings in research.md
> 
> _深入阅读这个文件夹，深刻理解它的工作原理、功能和所有特殊之处。完成后，把你的学习和发现写成一份详细的 research.md 报告_

> study the notification system in great details, understand the intricacies of it and write a detailed research.md document with everything there is to know about how notifications work
> 
> _仔细研究通知系统的每一个细节，理解它的复杂之处，写一份详细的 research.md 文档，包含关于通知如何工作的所有信息_

> go through the task scheduling flow, understand it deeply and look for potential bugs. there definitely are bugs in the system as it sometimes runs tasks that should have been cancelled. keep researching the flow until you find all the bugs, don't stop until all the bugs are found. when you're done, write a detailed report of your findings in research.md
> 
> _仔细走一遍任务调度流程，深入理解它，寻找潜在的 bug。系统里肯定有 bug，因为它有时候会运行本应被取消的任务。持续研究这个流程直到找到所有 bug，找不完不要停。完成后，写一份详细的发现报告到 research.md_

注意用词——**"deeply"**、**"in great details"**、**"intricacies"**、**"go through everything"**这不是废话，没有这些强调词，AI 会浮在表面 它会读一个文件，看看函数签名层面做了什么，然后就跳过了 你得明确告诉它，浅尝辄止不可接受

**为什么要写成文件？** 因为 `research.md` 是你的审查面 你可以打开它，验证 AI 是不是真的理解了系统，在任何规划发生之前纠正误解 如果研究阶段就错了，后面的计划会错，实现会更错，Garbage in, garbage out

这一步防的是 AI 编程中**最昂贵的失败模式**——不是语法错误，不是逻辑 bug，而是**写出来的代码在隔离环境下能跑，但放进真实系统就炸**一个忽略了现有缓存层的函数，一个没考虑 ORM 约定的数据库迁移，一个重复造轮子的 API 端点 Research 阶段就是为了防这些

---

## 第二步：Plan — 让 AI 出计划，不是出代码

Research 审核通过后，让 AI 写一份详细的实现计划，输出到单独的 plan.md 文件

> I want to build a new feature <name and description> that extends the system to perform <business outcome>. write a detailed plan.md document outlining how to implement this. include code snippets
> 
> _我想构建一个新功能 <名称和描述>，扩展系统以实现 <业务目标>。写一份详细的 plan.md 文档，说明如何实现。包含代码片段_

> the list endpoint should support cursor-based pagination instead of offset. write a detailed plan.md for how to achieve this. read source files before suggesting changes, base the plan on the actual codebase
> 
> _列表接口需要从 offset 分页改成 cursor 分页。写一份详细的 plan.md。先读源文件再建议修改，计划要基于实际代码_

生成的计划应该包含：方法的详细说明、展示实际修改的代码片段、要修改的文件路径、以及权衡和注意事项

**为什么不用工具自带的 plan mode？** Boris 的原话是"内置的 plan mode 很烂" 自己的 markdown 文件给你完全的控制权——你可以在编辑器里打开它、加批注、它作为一个真实的文件留在项目里持久存在

**一个他反复使用的技巧：** 如果你在开源项目里见过类似功能的好实现，把那段代码贴给 AI 当参考 比如你想加排序 ID，就把某个做得好的项目的 ID 生成代码贴过来，说"这是他们做排序 ID 的方式，写一份 plan.md 说明我们怎么采用类似方案" AI 有具体参考实现时，表现会好得多——比让它从零设计强太多

但计划文档本身不是最有趣的部分，有趣的是接下来发生的事

---

## 第三步：Annotate — 整个工作流最值钱的环节

这是 Boris 工作流里最独特的部分，也是人类价值最大的地方

拿到 plan.md 后，你不是直接说"开始写吧" 你在编辑器里打开这个文件，**直接在文档里加批注**这些批注用来纠正假设、否决方案、添加约束、或者提供 AI 不具备的领域知识

批注的长度差异很大，有时候只有两个字："非可选"——写在 AI 标记为可选的参数旁边 有时候是一整段话，解释一个业务约束，或者贴一段代码展示你期望的数据结构

Boris 给出的真实批注示例：

* **"use drizzle:generate for migrations, not raw SQL"** — AI 不知道的领域知识
* **"no — this should be a PATCH, not a PUT"** — 纠正错误假设
* **"remove this section entirely, we don't need caching here"** — 否决一个提议的方案
* **"the queue consumer already handles retries, so this retry logic is redundant. remove it and just let it fail"** — 解释为什么某个东西应该改
* **"this is wrong, the visibility field needs to be on the list itself, not on individual items. when a list is public, all items are public. restructure the schema section accordingly"** — 重新定向计划的整个章节

然后把带批注的文件交回给 AI：

> I added a few notes to the document, address all the notes and update the document accordingly. don't implement yet
> 
> _我在文档里加了一些批注，处理所有批注并相应地更新文档。先不要实现_

**这个循环通常重复 1 到 6 次**

那句"don't implement yet"的护栏至关重要，没有它，AI 一觉得计划差不多了就会跳去写代码 但"差不多"不够——什么时候够好，你说了算

### #为什么这招这么好用

plan.md 文件充当了你和 AI 之间的**共享可变状态**你可以按自己的节奏思考，精确地在出问题的地方加批注，然后重新开始对话而不丢失上下文 你不是在聊天消息里试图解释所有事情——你是**指着文档里的确切位置**，把你的修正写在那里

这和试图通过聊天消息来引导实现有本质区别 计划是一份结构化的、完整的规格说明，你可以整体审查 聊天记录是你得翻来翻去才能重建决策的东西，计划每次都赢

三轮"我加了批注，更新计划"就能把一份通用的实现计划变成一份完美契合现有系统的方案 AI 擅长理解代码、提出方案、写实现，但它不知道你的产品优先级、用户痛点、或者你愿意做的工程权衡**批注循环就是你注入这些判断的过程**

### #生成 Todo List

在开始实现之前，Boris 总是要求生成一份细粒度的任务分解：

> add a detailed todo list to the plan, with all the phases and individual tasks necessary to complete the plan - don't implement yet
> 
> _在计划里添加一份详细的 todo list，包含所有阶段和完成计划所需的每个单独任务——先不要实现_

这会创建一份清单，在实现过程中充当进度追踪器 AI 完成一项就标记一项，你随时可以扫一眼计划，看到进度到哪了，在持续数小时的会话中尤其有用

---

## 第四步：Implement — 计划确认后才写代码

当计划准备好了，Boris 会发出实现指令，他把这个打磨成了一个跨会话复用的标准 prompt：

> implement it all. when you're done with a task or phase, mark it as completed in the plan document. do not stop until all tasks and phases are completed. do not add unnecessary comments or jsdocs, do not use any or unknown types. continuously run typecheck to make sure you're not introducing new issues.
> 
> _全部实现。完成一个任务或阶段后，在计划文档中标记为已完成。不要停下来，直到所有任务和阶段都完成。不要添加不必要的注释或 jsdoc，不要使用 any 或 unknown 类型。持续运行类型检查，确保你没有引入新问题_

这一条 prompt 编码了所有重要的事：

* **"implement it all"**：执行计划里的所有内容，不要挑着做
* **"mark it as completed in the plan document"**：计划是进度的唯一真相来源
* **"do not stop until all tasks and phases are completed"**：不要在中途暂停等确认
* **"do not add unnecessary comments or jsdocs"**：保持代码干净
* **"do not use any or unknown types"**：维持严格类型
* **"continuously run typecheck"**：尽早发现问题，不要等到最后

他几乎在每个实现会话中都用这个措辞（略有变化） 到他说"implement it all"的时候，每个决策都已经做完并验证过了

**实现变成了机械性的，而不是创造性的** ——这是刻意的 他希望实现阶段是无聊的，创造性的工作发生在批注循环里 一旦计划对了，执行应该是直截了当的

没有规划阶段会怎样？AI 在早期做一个合理但错误的假设，在上面构建 15 分钟，然后你不得不回滚一连串的修改 "don't implement yet"这个护栏彻底消除了这个问题

---

## 实现过程中的反馈

一旦 AI 开始执行计划，你的角色从架构师变成了监工，你的 prompt 会变得极短

规划阶段的批注可能是一整段话，但实现阶段的纠正往往只有一句话：

* "You didn't implement the deduplicateByTitle function."
* "You built the settings page in the main app when it should be in the admin app, move it."

AI 有计划的完整上下文和整个会话的记忆，所以简短的纠正就够了

**前端工作是最需要反复迭代的部分**，Boris 在浏览器里测试，然后快速发出纠正：

* "wider"
* "still cropped"
* "there's a 2px gap"

视觉问题有时候直接贴截图，一张表格没对齐的截图比文字描述快得多

他还会大量引用现有代码：

> "this table should look exactly like the users table, same header, same pagination, same row density."
> 
> _"这个表格应该跟用户表长得一模一样，同样的表头、同样的分页、同样的行密度"_

这比从零描述一个设计精确得多，成熟代码库里的大多数功能都是现有模式的变体 一个新的设置页面应该长得像现有的设置页面，指向参考就传达了所有隐含的需求，不用一一拼写出来 AI 通常会先读参考文件，再做修改

**当方向跑偏时，不要试图修补**，回滚 git 变更，重新限定范围：

> "I reverted everything. Now all I want is to make the list view more minimal — nothing else."
> 
> _"我回滚了所有东西。现在我只想让列表视图更简洁——别的什么都不要动"_

回滚后缩小范围，几乎总是比试图渐进式修复一个错误方向产出更好的结果

---

## 保持控制权

即使把执行委托给了 AI，Boris 也从不给它完全的自主权，他在 plan.md 文档里完成了绝大部分的主动引导

这很重要，因为 AI 有时候会提出技术上正确但对项目来说是错误的方案 也许方案过度工程化了，或者它改了一个其他部分依赖的公共 API 签名，或者它选了一个更复杂的选项而简单的就够了 你有关于更大系统、产品方向和工程文化的上下文，AI 没有

几个具体的引导方式：

**从提议中挑选：** 当 AI 识别出多个问题时，逐个过："第一个，直接用 Promise.all，不要搞得太复杂；第三个，提取成单独的函数提高可读性；第四个和第五个忽略，不值得增加复杂度。" 你在根据自己对当前优先级的了解做逐项决策

**砍范围：** 当计划包含锦上添花的内容时，主动砍掉。"从计划里删掉下载功能，我现在不想实现这个。" 防止范围蔓延

**保护现有接口：** 当你知道某些东西不应该变时，设硬约束："这三个函数的签名不能变，调用方去适配，不是库去改。"

**覆盖技术选择：** 有时候你有 AI 不知道的特定偏好："用这个模型而不是那个" 或者 "用这个库的内置方法，不要自己写一个"。快速、直接的覆盖

**AI 处理机械性的执行，你做判断性的决策**计划在前期捕获大决策，选择性的引导处理实现过程中冒出来的小决策

---

## 单个长会话

Boris 在一个长会话里跑完研究、规划和实现，而不是拆成多个会话 一个会话可能从深读一个文件夹开始，经过三轮计划批注，然后跑完整个实现——全在一个连续的对话里

他说他没有看到大家说的"上下文窗口用到 50% 之后性能下降"的问题 实际上，到他说"implement it all"的时候，AI 已经花了整个会话在构建理解：研究阶段读文件，批注循环中完善心智模型，吸收他的领域知识修正

当上下文窗口满了，AI 的自动压缩会保留足够的上下文继续工作 而计划文档——那个持久化的产物——以完整的保真度存活过压缩，你随时可以把 AI 指向它

---

## 一句话总结

**深入阅读，写计划，批注计划直到满意，然后让 AI 一口气执行完，过程中持续做类型检查**

没有魔法 prompt，没有精心设计的系统指令，没有花哨的 hack 只是一条纪律严明的流水线，把思考和打字分开 Research 防止 AI 在不理解的情况下乱改，Plan 防止它做错误的修改 批注循环注入你的判断，实现指令让它在所有决策都做完之后不间断地执行

Boris 原文的最后一句话说得好：

> Try my workflow, you'll wonder how you ever shipped anything with coding agents without an annotated plan document sitting between you and the code.
> 
> _试试我的工作流，你会想不通以前没有一份批注过的计划文档挡在你和代码之间，你是怎么用编程 Agent 交付任何东西的_

下一篇我会讲我用 OpenCode 跑这套流程的具体体验——桌面端的批注功能、Web UI + 手机监工，以及怎么让这套工作流的摩擦降到最低

  
你的 AI 编程流程是什么样的？欢迎在评论区分享你的经验

---

> 参考：
> 
> * Boris Tane 原文：How I Use Claude Code\[1\]

#### References

1. How I Use Claude Code: https://boristane.com/blog/how-i-use-claude-code/

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/fKq9Pwmwg3QcD3KnKlRlsrg3ib80oic3002JT8ykRlibI6icAy8sgD5AiagDvyK2q9WkMClVvb8l5MTyhlk9rqmm9NQ/0.png) 

 春秋Daneel 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/fKq9Pwmwg3QcD3KnKlRlsrg3ib80oic3002JT8ykRlibI6icAy8sgD5AiagDvyK2q9WkMClVvb8l5MTyhlk9rqmm9NQ/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
