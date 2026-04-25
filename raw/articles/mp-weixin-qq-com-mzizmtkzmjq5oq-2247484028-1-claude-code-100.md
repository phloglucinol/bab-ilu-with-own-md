---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzIzMTkzMjQ5OQ%3D%3D&mid=2247484028&idx=1&sn=6794e8e7c9525219f63626bcd51a0d28
canonical_url: https://mp.weixin.qq.com/s?__biz=MzIzMTkzMjQ5OQ%3D%3D&mid=2247484028&idx=1&sn=6794e8e7c9525219f63626bcd51a0d28
source_domain: mp.weixin.qq.com
title: Claude Code 最佳实践：这些方法让它强 100 倍
author: 
published_at: 
fetched_at: 2026-04-25T02:03:32Z
extractor: wechat_worker
content_hash: 68e648849826486c6d72fa6ef97f9631fde9cb61de3eec153ba1aac467e6e16e
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/ibFEO97QBBmDbeicYToTN7mFqxsl0yiaqka8vjx542a8kENzSLZicQibjTicMsbClkXIDauFDG0WpYFpmYNwWdicUabpjHicR12ZmEW5JRIITGjRqCI/0.jpg) 

# Claude Code 最佳实践：这些方法让它强 100 倍

原创 leemysw leemysw [ Mr杂货铺 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

> 本文信息来源为 Anthropic 官方最佳实践文档以及 Claude Code 作者 Boris Cherny 公开分享的使用技巧，结合我个人使用经验整理而成。

用 Claude Code 挺久了。说实话，刚开始的时候我的用法和大多数人一样，不过是把它当成一个更聪明的终端助手。直到我认真读完了 Anthropic 的官方最佳实践文档，又看了 Boris Cherny（Claude Code 的实际开发者）在 X 上分享的那一系列使用技巧之后，我才意识到自己之前的用法可能连这个工具潜力的 20% 都没碰到。

今天这篇文章，把我从这两个源头学到的，加上这段时间在实际项目里验证过的做法，全部整理出来。

## 你最大的敌人是上下文窗口

在讲任何具体技巧之前，有一个底层概念必须先搞清楚。

Claude 有一个上下文窗口（Context Window）。可以把它想象成一块白板。你发的每一条消息、Claude 读取的每一个文件、它执行的每一条命令，全部都会被写到这块白板上面。

白板写满了之后会怎样？Claude 的表现开始下降。它会忘记你之前说过的指令，会犯一些正常状态下不会犯的错误。

这篇文章里后面提到的几乎所有方法，归根到底都是在管理这块白板。读的时候记住这个前提。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ibFEO97QBBmBAMro24PenL7EShBVz0PyiaP1FhxFWVqX2o4GddOhSPZPkTJTIiaa48oVMTvE62c1pECXlr9F2UYIsl2c3oe2pia42WopT5aBpuA/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/ibFEO97QBBmAU0xHvgDPV4qRc6Yia8NGNphnVS58XsWePiacaW3iarFVySoVdtdPUeMcmbMDgwU3JicJdUtXLRzSX7b9iba2RbicLmKRRshzj9Hrlo/640.png)

  
## 给 Claude 一个自我检查的机制

大多数人的用法是描述自己要什么，然后祈祷 Claude 一次就做对。一旦它没做对，就得自己一个一个去检查、去纠正。这种方式用多了非常消耗精力。

更好的做法是，在你的 prompt 里面直接给出验证标准，让 Claude 自己对照着检查。

举个具体的例子。如果你想让 Claude 写一个邮箱格式校验函数，不要只说"写一个邮箱校验函数"，而是这样说：

> 写一个邮箱格式校验函数。用以下测试用例验证：hello@gmail.com 应该通过，hello@ 应该失败，@domain.com 应该失败。写完之后把测试跑一遍。

这样 Claude 就不需要你手动去验证每一个输出了，它自己就能发现问题。

视觉相关的任务也是同样的思路。如果你想让 Claude 调整页面上一个按钮的样式，你可以贴一张截图，然后说"按这个样子来改，改完之后截张图，告诉我结果和目标之间还有什么区别"。

关键在于：一旦你给了 Claude 一个可以对照的标准，你就不再是唯一的反馈回路了。

## 不要让 Claude 上来就写代码

几乎每个刚开始用 Claude Code 的人都会踩这个坑。

你有一个想法，描述了一下，Claude 马上开始写代码。十五分钟之后你发现它解决的根本不是你想要解决的那个问题。

解决办法很简单：先让 Claude 想清楚，再动手。

Claude Code 有一个叫 Plan Mode 的功能。在这个模式下，Claude 只做阅读和分析，不做任何修改。

实际可行的工作流程是这样的：

**第一步**，进入 Plan Mode，让 Claude 读取相关的文件，理解各个部分之间的关系。

**第二步**，让 Claude 写一份完整的计划。哪些文件需要改？改动的顺序是什么？哪些地方可能出问题？

**第三步**，你自己读一遍这个计划。觉得有问题的地方调整一下。

**第四步**，切回 Normal Mode，让 Claude 按照计划开始执行。

**第五步**，让 Claude 提交代码并附上一条清晰的 commit message。

前面多花十分钟做计划，后面能省好几个小时的返工时间。

Boris 说他的团队在每个复杂任务上都会走这个流程。他团队里有一个人甚至会让一个 Claude 写计划，然后启动第二个 Claude 来审查这个计划，就像让一个高级工程师做 code review 一样。他们对这个步骤的重视程度可见一斑。

  
## 描述要具体，模糊的 prompt 就是在浪费时间

Claude 能从上下文里推断出很多东西，但它没办法读你的心思。

"给 auth.py 加点测试" 和 "给 auth.py 写测试，重点覆盖用户 session 在请求中途过期的场景，不要用 mock，关注 token 表面看着合法但实际上已经过期的那种边界情况"，这两句话要的是同一件事，出来的结果完全是两个东西。

你也可以直接指定 Claude 去哪里找信息。比如，与其问"这个函数为什么表现这么奇怪"，不如说"看一下这个文件的 git 历史，找出这个行为是在哪个 commit 引入的，以及当时为什么要那样写"。

前者 Claude 只能给你猜测，后者 Claude 给你的是有依据的答案。

## CLAUDE.md 比你想象的强大得多

如果你在日常工作中频繁使用 Claude Code 但还没有设置 CLAUDE.md 文件，那你浪费了大量本可以不必浪费的精力。

CLAUDE.md 是一个 Claude 在每次会话开始时都会读取的文件。你放在里面的内容会影响 Claude 在整个会话期间的行为模式。

想一想你平时总是在重复的那些指令。比如"永远用 ES modules，不要用 CommonJS""测试里面不要用 mock""每次改完代码自动跑一遍 linter""分支命名格式是 feature/工单号"。没有 CLAUDE.md 的时候你每次都要打一遍。有了之后你说一次就够了。

Boris 的团队有一个做法特别值得学。当 Claude 犯了一个错误、你纠正了之后，在对话结尾加一句：

> 把刚才学到的更新到 CLAUDE.md 里，下次别再犯同样的错。

Claude 会自己写一条规则。下一次会话它会自动遵守。时间久了，CLAUDE.md 就变成了一份不断进化的文档，让 Claude 越来越懂你的工作习惯和偏好。

但有一点要注意：保持精简。如果你的 CLAUDE.md 膨胀到了几百行，Claude 会开始忽略其中一部分内容，因为太多规则在争夺它的注意力。每一行都应该能回答这个问题："如果没有这一行，Claude 会犯什么错？"回答不出来的，删掉。

## 同时跑多个会话

这个做法听到之后会觉得理所当然，但大多数人确实没有这样做过。

你可以同时运行多个 Claude Code 会话，每个处理一个不同的任务。

Boris 说这是他的团队发现的最大的生产力提升手段。他们中有些人同时跑三到五个并行会话，借助 git worktree（同一个仓库的多个独立工作副本，互相不干扰）来实现。

一个实际的用法是这样的：Session A 正在写一个新功能。Session B 拿到 Session A 产出的代码，做 code review，找边界情况和潜在问题。你把 Session B 的反馈带回 Session A。一个 Claude 写，另一个 Claude 审，出来的代码质量比单个会话又写又审要好得多。

也可以用来做测试驱动开发。一个会话先写测试用例，另一个会话写代码让测试通过。核心工作由 Claude 完成，你做的是协调和最终把关。

## 用 Subagent 保持主会话干净

回到白板那个比喻。

当 Claude 调查一个问题的时候，它会读取大量的文件。每读一个，白板上就多写一行。等它研究完你的代码库、准备开始写代码的时候，白板已经被填了一半了。留给实际编码的空间就不多了。

Subagent 解决的就是这个问题。

Subagent 是一个独立的 Claude 实例，它在自己的上下文窗口里做调查工作，完了之后把结论汇报回来。这个过程不占用你主会话的白板空间。

用法很简单，在任何研究类的 prompt 前面加上"use subagents"就可以了。比如：

> Use subagents to figure out how our payment flow handles failed transactions.

Subagent 会去读取所有它需要的文件，你的主会话保持干净。等调查报告回来之后，你仍然有充裕的上下文空间来做实际的开发工作。

Boris 的团队甚至用一个由 Opus 4.5 驱动的 Subagent 来处理权限审批请求，这个 Subagent 会扫描请求内容判断是否安全，安全的就自动批准。

## 重复的事情做成 Skill

如果一个操作你一天做不止一次，它就应该被做成 Skill。

Skill 本质上是一个保存好的工作流。你把步骤写一遍、起个名字。下次需要的时候直接调用名字就行了。

Boris 团队有一个 BigQuery 的 Skill，团队里任何人可以直接在 Claude Code 里跑数据分析查询，不需要写 SQL。

一个你今天就可以搭起来的 Skill 是这样的，做一个叫 `/fix-issue`的自动化流程：

> 读取 GitHub issue 内容 → 找到代码库里的相关文件 → 完成修复 → 编写并运行测试 → 创建 Pull Request

你输入 `/fix-issue 447`，Claude 把整件事情处理完。一条命令，零次上下文切换。

Boris 的原则是：团队里任何一天做超过一次的事情，就做成 Skill。

## 修 bug 的时候别微操，把原始信息丢给 Claude

这一点是我读到的时候觉得最反直觉的。

大多数人修 bug 的方式是这样的：自己先看一遍错误，用自己的理解把问题描述给 Claude 听，然后看着 Claude 猜来猜去，纠正几轮之后才修好。

更快的方式是：把原始的错误信息直接给 Claude，然后让它自己去搞清楚。

Boris 的团队连了 Slack 的 MCP。有 bug 报告进来的时候，他们把 Slack 对话线程贴给 Claude，就说一个词：fix。

不做描述，不做铺垫。Claude 自己读对话内容，自己定位问题，自己修。

或者他们说一句"去修掉失败的 CI 测试"然后就不管了。不指定是哪个测试，不解释为什么失败。Claude 自己去搞定。

关键在于，你给 Claude 的应该是真实的原始数据，比如 Slack 对话线程、错误日志、Docker 输出，而不是你对问题的二次加工和解读。Claude 在阅读分布式系统日志和追踪故障发生位置方面比你预期的要强很多。

## 上下文脏了就清掉

你在一个 Claude 会话里工作了一个小时。先修了一个 bug，然后问了一个和 bug 无关的问题，又跳回来继续改 bug，中间又随口问了点别的。到这个时候，会话的上下文里已经堆满了半相关的零碎内容，Claude 的回答开始跑偏了。

这就是上下文污染（Context Pollution），它会直接拖垮会话的表现。

处理方法很粗暴但很管用：输入 `/clear`。

直接清空上下文，用你这一个小时学到的东西重新写一个更精准的起始 prompt。

很多人抗拒这样做，因为感觉像是在扔掉之前的进度。但实际上，一个干净的会话配合一个写得好的 prompt，表现几乎总是优于一个纠结了三个小时的脏会话。

一个值得遵守的原则：如果你纠正了 Claude 两次、它仍然没有做对，不要再纠正第三次了。清空上下文，重新写一个更好的起始 prompt。

还有一个偏柔和的方式叫 `/compact`，你可以告诉 Claude 保留哪些信息然后压缩掉其他的。比如 `/compact focus on the payment integration changes`，保留重要的部分，清理掉无关的噪音。

## 把 Checkpoint 当成游戏里的存档点

Claude 每次做改动的时候都会自动创建一个 Checkpoint，类似于游戏里的存档。

如果 Claude 走的方向不对，你可以回退到之前任意一个 Checkpoint。可以只恢复对话，也可以只恢复代码，或者两个一起恢复。

这改变了你应该怎么看待"冒险"这件事。不需要在 Claude 每次动手之前都反复斟酌，你完全可以说"试试这个激进的方案"。成了就继续往下走，没成就回退到存档点、换个思路，没有任何损失。

Checkpoint 即使关掉终端也会保留。第二天回来你仍然可以回退到昨天的某个节点。

需要注意的一点：Checkpoint 记录的是 Claude 做的改动，不是其他进程做的改动。它不能替代 git，两者配合使用。

## 用反向角色来逼出更好的结果

Boris 分享了几个他团队在使用中发现的技巧，大多数人不太会想到这样用。

当 Claude 给出了一个感觉凑合能用但不够好的方案之后，你可以说：

> 你现在对这个问题已经了解得很透彻了。把现在的方案扔掉，重新来一版优雅的。

这个做法之所以有效，是因为 Claude 在第一轮有时候会走捷径。让它在已经充分理解问题之后重新来过，产出的东西往往比你一开始就要求"写一个优雅的方案"更好。

当你想在提交之前做一轮检查的时候，可以这样说：

> 审一下这些改动。问我每一个刁钻的问题。在你满意之前不要提交 PR。

角色反转过来了。Claude 变成审查者，你来回答问题、为自己的决策辩护。这种做法听起来有点怪，但确实能抓到你自己会忽略的问题。

当你想要验证某个修复确实生效的时候：

> 证明给我看这个改动起作用了。展示 main 分支和当前分支在行为上的具体区别。

不要只看测试通过了就完事。让 Claude 把实际的行为差异展示出来。

## 语音输入让你的 prompt 质量翻倍

这个听起来和 Claude Code 没什么关系，但实际体验下来差别很大。

打字的时候你倾向于写得简短。打字毕竟慢，你会下意识地省略很多上下文信息。这些被省略的部分恰好是 Claude 做好工作所需要的。

说话的时候，你会自然地给出更多细节。你会解释背景，提到约束条件，描述你到底想要什么样的结果。

Boris 的团队日常大量使用语音输入。Mac 上双击 Fn 键就能开启听写功能，你正常说话，系统自动转写。

通过语音得到的 prompt 几乎总是比打字得到的 prompt 更好，因为它们包含了更多 Claude 需要的上下文。试一次你可能就不想回去了。

## 用 Claude Code 学东西

大多数人把 Claude Code 当作一个生产输出的工具。但如果换个用法，它也是一个很好的学习工具。

进入一个新的代码库的时候，你可以问 Claude 这些问题：

> 这个项目里的日志系统是怎么工作的？

> 这个函数具体在做什么？它为什么调用的是这个方法而不是那个方法？

> 用户登录的时候从第一个请求到 session 创建完成，整个流程走一遍。

这些问题你平时会去问一个资深工程师。Claude 给出的回答质量不输于一个有经验的人，而且你问第二遍第三遍它也不会烦。

Boris 的团队用 Claude 来生成 HTML 幻灯片，把不熟悉的代码用可视化的方式解释清楚。Claude 也可以画 ASCII 风格的系统架构图，展示各个部分之间的连接关系。这些做法听起来不太严肃，但实际用过之后你会发现它们让复杂的东西变得清晰的速度远超预期。

还有一种用法是间隔重复学习：你向 Claude 解释你对某个东西的理解，Claude 会追问来找出你理解上的漏洞，把这些漏洞记录下来，之后再回来专门考你。整个学习流程完全在 Claude Code 里完成。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ibFEO97QBBmCN3AyMuMiaLdmPgexw5mibHbyxsYq7KKGutGLHZnKicSibJRfCmdxRou5nCCcdFyRNkTqia3xBefJAycCHgO2JrYrtKt0D99wpINR8/640.png)

## 四种会毁掉会话的常见失误

**厨房水槽式会话。**你从一个任务开始，中途漫游到五个不同的话题。上下文里堆满了和当前问题毫无关系的内容。应对方式：不同任务之间用 `/clear`清掉上下文。

**纠正死循环。**Claude 做错了，你纠正它。还是错的，你再纠正。到第三次的时候，上下文里全是失败的尝试，Claude 已经搞不清楚你到底想要什么了。应对方式：纠正两次还不对，清空一切，重新写一个更清楚的起始 prompt。

**CLAUDE.md 臃肿。**你的指令文件太长了，Claude 在噪音里找不到重要的规则。应对方式：对每一行问自己"没有这行 Claude 会犯什么错"，回答不上来的就删。

**无边界的探索。**你让 Claude 去调查一个问题但没给范围。Claude 读了几百个文件，上下文在你开始写任何代码之前就耗尽了。应对方式：给调查任务限定范围，或者用 Subagent 让探索发生在独立的上下文里。

---

`> 信息来源：  
> 1. [Anthropic 官方最佳实践文档](https://code.claude.com/docs/en/best-practices)  
> 2. [Boris Cherny (Claude Code 作者) 的 X 分享](https://x.com/bcherny/status/2017742741636321619)  
> 3. [@meer_aiit 的整合分析](https://x.com/meer_aiit/status/2027509711722188976)`

预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/LXicaHocBrJdiaT8wB0WydjmrKnrGQH9YFriaAukp7Q4KArbqPx2OydpqEjLKibgI6Js9vfzrvoqrAwcKQhfXFsOEg/0.png) 

 Mr杂货铺 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/LXicaHocBrJdiaT8wB0WydjmrKnrGQH9YFriaAukp7Q4KArbqPx2OydpqEjLKibgI6Js9vfzrvoqrAwcKQhfXFsOEg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
