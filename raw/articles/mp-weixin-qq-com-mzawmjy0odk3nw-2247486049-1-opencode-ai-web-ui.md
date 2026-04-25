---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzAwMjY0ODk3Nw%3D%3D&mid=2247486049&idx=1&sn=7ad766c1e43304fdf6a637e25a15e823
canonical_url: https://mp.weixin.qq.com/s?__biz=MzAwMjY0ODk3Nw%3D%3D&mid=2247486049&idx=1&sn=7ad766c1e43304fdf6a637e25a15e823
source_domain: mp.weixin.qq.com
title: 我用 OpenCode 跑 AI 编程工作流——桌面批注、Web UI、手机监工
author: 
published_at: 
fetched_at: 2026-04-25T02:03:33Z
extractor: wechat_worker
content_hash: 50a861c6fa55f6bc0205acabbafd70fca09e6edd797ee95b11489695f93cfb6c
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/iaDf0iaGn69rkib1AWp3t2NO5AdccicLfJ13vMms8NWtolq8VWu82gK2qTibwu3ZcHdqnMv8MRrErbNqD0FXpOCSstFbLZFDXWLtia8tSQwVpQdqI/0.jpg) 

# 我用 OpenCode 跑 AI 编程工作流——桌面批注、Web UI、手机监工

原创 春秋1 春秋1 [ 春秋Daneel ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

从方法论到落地的工具

上一篇讲了 Boris Tane 的 AI 编程工作流：Research → Plan → Annotate → Implement

[用了 9 个月 AI 编程后，我只推荐这一套工作流——别让 AI 直接写代码](https://mp.weixin.qq.com/s?%5F%5Fbiz=MzAwMjY0ODk3Nw==&mid=2247486028&idx=1&sn=b4283fe00981b9de4ccf4f15f7ea476b&scene=21#wechat%5Fredirect)

方法论是通用的，任何 AI 编程工具都能跑 但工具的体验差异会直接影响你能不能坚持这套流程

我目前用的是 OpenCode 先说说为什么选它，再讲怎么用它跑工作流的每个阶段

**纯实操干货，建议收藏**

---

## 为什么是 OpenCode

OpenCode 是一个开源的 AI 编程 Agent，GitHub 100K+ stars，700+ 贡献者，每月 250 万开发者在用

它不是一个"好用的终端工具"——它有三种完整形态：**桌面端、Web UI、终端 TUI**三种形态共享同一套会话和状态，这意味着你可以在桌面端写计划、加批注，然后用手机打开 Web UI 监控 AI 的执行进度

这种多形态架构天然适配上一篇讲的工作流：

* **Research + Plan + Annotate**：在桌面端完成，利用原生批注功能直接在计划上做标注
* **Implement 监工**：通过 Web UI 在手机上看进度、回复 AI 提问

除了形态，还有几个对工作流很重要的能力：

* **自动加载 LSP**：AI 在 Research 阶段读代码时能拿到类型信息和诊断结果，理解更准确
* **多会话并行**：可以同时开多个 Agent，一个在跑 Research，另一个处理独立的小任务
* **75+ 模型供应商**：Anthropic、OpenAI、GitHub Copilot、ChatGPT Plus/Pro 都支持，也内置免费模型
* **完全开源免费**：没有订阅费，没有 vendor lock-in

---

## 安装

macOS 桌面端一行命令：

```
brew install --cask opencode-desktop

```

也可以去 opencode.ai/download 下载安装包，支持 macOS / Windows / Linux

装好登录你的 AI 账号就能开始了

  
![下载 OpenCode](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/iaDf0iaGn69rmibEbMy5G93wic1ibYDK1OBxdr2S6FATic5bxm8nlGUgfVFqoXtbdH5RwCwpcPC47tVPCMXQjiafTEeqS2ld7FkicGNOy3DRdUT8cPc/640.png)

下载 OpenCode

  
---

## Research + Plan：桌面端搞定

工作流的前两步——Research 和 Plan——我都在 OpenCode 桌面端完成

在对话里发 Research 指令，AI 读完代码后直接生成 research.md 审阅没问题，接着让它出 plan.md 整个过程不需要切窗口，所有东西都在一个界面里

而且在 Research 阶段，它会自动调用子 Agent 帮你收集信息——查互联网、确认 API 文档、搜开源实现 这些子 Agent 是并行跑的，用的是便宜的模型（比如 Gemini Flash），各自独立上下文，不污染主对话，还省钱

  
![分配任务给子agent](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/iaDf0iaGn69rnTJGicopuicqBUWn2EdYBOqczX9QuiahpytgA68IGj2VnUBg0VQiaU3VeeZ1OxdmBursyqLS3G0vlO6eokbGAAm81o7AkrvDwNQZQ/640.png)

分配任务给子agent

  
---

## Annotate：桌面端的批注功能

工作流里最核心的 Annotate 环节——在计划里加批注，让 AI 根据批注修改——OpenCode 有原生支持

你可以直接在桌面端界面里对 AI 生成的计划做标注，不需要手动在 markdown 里插 `[NOTE]` 标记

操作很直观：看到计划里哪里不对，直接在那个位置加批注 比如给一个字段补充更多信息，或者纠正一个错误的假设 AI 会读到你的标注并据此修改计划，整个思路完全不会被打断，非常顺滑

  
![项目，会话管理](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/iaDf0iaGn69rkxQKMicFOBsUnz1pcCyDokYew1PCnYjdPR7q67ASbOwiaJH8FMczuD0N0XJ3ZibVzo2JAaTCOibLswcACDtuXdpyicFVxicVYDP511A/640.png)

项目，会话管理

  
不用来回切窗口、手动改文件，批注完 AI 直接改 摩擦小了，你就愿意多批几轮——多批几轮出来的计划，质量差别是肉眼可见的

---

## Implement 监工：Web UI + 手机

实现阶段，AI 在执行计划，你的角色变成了监工

这个阶段不需要一直坐在电脑前，OpenCode 的 Web UI 让你可以在手机上做监工

### 推荐：用 Cloudflare Tunnel 直接暴露到公网

我直接推荐用 Cloudflare Tunnel（免费），比局域网方案更方便，而且更安全

```
brew install cloudflare/cloudflare/cloudflared
opencode web --port 4096 --hostname 0.0.0.0
cloudflared tunnel --url http://localhost:4096

```

cloudflared 会给你一个公网地址，手机浏览器打开就能用 不管你在公司、咖啡厅还是地铁上，都能直接访问

Quick Tunnel 生成的是随机 URL，只有你自己知道，基本安全够用

如果你想更稳妥，可以配置 Cloudflare Access（Zero Trust，免费额度够个人用） 绑定自己的域名后，可以开启邮箱验证码登录 + 白名单，只有你的邮箱能访问 这需要一个 Cloudflare 账号和一点额外配置，但安全性比密码方式好很多

### 手机端体验

OpenCode 的 Web UI 在手机上适配得很好，页面是响应式的，对话界面在小屏幕上也很清晰

我实际的监工场景：

* **通勤时**：打开手机看一眼，AI 是不是还在正常跑，有没有卡住，有没有在等我回答问题。如果它问了什么，直接在手机上回复，不用等回到电脑前
* **午饭时**：问几个简单的技术问题，让 AI 帮忙查个 API 用法
* **睡前**：看一眼今天的会话进度，想想明天要怎么继续

Review 计划、加批注这些重活还是在电脑上做更舒服 手机端的价值是让你随时能看到 AI 的工作状态，不会出现"AI 卡了半小时等你回复一个问题，你却不知道"的情况

![手机监工](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/iaDf0iaGn69rkB7ZBpxctBB5LMxwl6icCIVicxrRLPVpnWq6aEEdbk2yWoVc6Ric8nmMSZayx6vRqicaF4HGG3YARy3AIM2SxiaqJWN9JEMGK6c7mw/640.jpg)

手机监工

### 桌面 + 手机同步

你可以同时用桌面端和 Web UI 连接同一个服务，共享会话和状态：

```
# 终端 1：启动 Web 服务
opencode web --port 4096

# 终端 2：用桌面端或 TUI 连接同一个服务
opencode attach http://localhost:4096

```

在电脑上用桌面版写代码、做批注，手机上用 Web UI 做监工，两边实时同步

---

## 总结：工具对应工作流

| 工作流阶段           | OpenCode 形态 | 做什么                          |
| --------------- | ----------- | ---------------------------- |
| Research + Plan | 桌面端         | 发指令、审阅 research.md 和 plan.md |
| Annotate        | 桌面端批注功能     | 直接在计划上加标注，循环修改               |
| Implement 监工    | Web UI + 手机 | 看进度、回复 AI 提问、简单纠正            |

工具不改变方法论，但好的工具让正确的方法论更容易坚持 OpenCode 让工作流的每个阶段都有对应的最佳形态，这是我觉得它用起来顺手的原因

^小声打个广告：如果需要 Token，可以来 aicodewith.com 看看^ ^支持 OpenCode、OpenClaw 等第三方应用，不用操心账号和付款问题^

如果觉得不错，欢迎点赞收藏转发，大家的支持是我创作的动力！非常感谢！

---

> 参考：
> 
> * 上一篇：别让 AI 直接写代码——用了 9 个月 AI 编程后，我只推荐这一套工作流
> * Boris Tane 原文：How I Use Claude Code\[1\]
> * OpenCode 官网：https://opencode.ai\[2\]
> * OpenCode 下载：https://opencode.ai/download\[3\]
> * Cloudflare Tunnel：https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/\[4\]

#### References

1. How I Use Claude Code: https://boristane.com/blog/how-i-use-claude-code/
2. https://opencode.ai: https://opencode.ai
3. https://opencode.ai/download: https://opencode.ai/download
4. https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/: https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/

  
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
