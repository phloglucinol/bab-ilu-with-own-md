---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MjU5NTU3MQ%3D%3D&mid=2247485141&idx=1&sn=d2b7040482c007ec1bf441cf071a1c36
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MjU5NTU3MQ%3D%3D&mid=2247485141&idx=1&sn=d2b7040482c007ec1bf441cf071a1c36
source_domain: mp.weixin.qq.com
title: 计算化学需要的 Harness
author: 
published_at: 
fetched_at: 2026-04-25T02:03:10Z
extractor: wechat_worker
content_hash: 83fdf407e87bdd080fa802237e1e67d51f4800abdfad0dc55aa697f55eb1e555
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/7zwO3pRR030c2d2AfzRibdjkibJzG48z6q3BJKWoRXldNnxPCxUeHSyFSVdpJrEZqlMMeyp2iae4r4mDHnOGta5lXHJ9dGSfbZ0fCGQqPYNdKQ/0.jpg) 

# 计算化学需要的 Harness

原创 计算化学简讯 计算化学简讯 [ 计算化学简讯 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

# 计算化学需要的 Harness

最近大家在讲 Harness engineer，本质其实很简单：模型不够，你得给它一层外部系统。

那句话已经说得很清楚了：

> Agent = Model + Harness

模型负责生成，Harness负责约束、校验、串流程，让输出变成“能用的东西”，而不是一次性的文本。

在 coding 场景里，这一层很多时候是隐形的，很多人写程序搭好CI/CD工作流基本是起手式，Harness是让Coding Agent在无人监督下自己写程序，但是这个太消耗tokens，没必要。

但在计算化学里，如果没有Harness，基本什么都跑不起来。

### 一、Workflow Harness：让它按流程走

很多人还在试图用一个 prompt 直接让 agent 跑完整个模拟流程，这件事的问题不在模型，而在结构。

只要每一步的输入输出是模糊的，Agent 就只能“猜”，最后一定崩。

真正可行的方式其实很工程化：把每个计算单元钉死。Docking 吃什么、吐什么，MD 吃什么、吐什么，全都标准化。这样 agent 做的事情就不再是“理解任务”，而是把这些模块按顺序串起来。

一旦结构稳定了，自动化模拟才成立。否则就是一次性 demo，看起来很聪明，实际上不可复现。

这也是 ChemOrchestra™ 的一个核心思路：先把工具做成标准件，再谈 agent。顺序反了基本都会失败。ChemOrchestra™ 已经支持通过自然语言构建工作流：

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/7zwO3pRR033fdM08ibQEYzXmUdSRk3LPQ3o62jHPDD0GfFYialNvkGtv2XogqSKyzYLNrJBQKonOqRrZbOVxnkU5TIicXHwlEFibcaCNA1LeVxk/640.gif)

(早在2025年，ChemOrchestra™ 便已经支持自然语言生成模拟工作流，目前迎来大升级，用更好的function calling做复杂模拟流)

### 二、Decision Harness：给化学空间探索以边界

现在模型已经可以设计分子了，但问题从来不在“能不能设计”，而在“设计的东西能不能做”。

如果不加约束，模型会自然走向复杂、极端、不可合成，最后生成一堆没法进实验室的结构。

所以必须硬加一层限制，把它锁在一个合理的化学空间里。

比如限制在可合成空间，限制骨架，控制每一步修改的幅度，甚至直接用反应规则去卡路径。本质上就是把“搜索空间”变成“合法空间”。这一层是最难的，因为已经不是简单工程问题，而是化学知识、约束设计和搜索策略混在一起。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/7zwO3pRR031GBbD6L9yETsXMUWjwyPRKYm6ibqSYb8iaZ03H5n5wbalibRyOS9ic9whY9S7s2WTYLJn61K9GgNw5jl4xkD1nIHpND9FJVyFKBTY/640.png)

最近像Claude、OpenAI 都在往生物制药走，所以ChatGPT和Claude那些模型尽量别用了。我们现在在用 Gemma 4 23B 做本地推理，调好prompt，再叠一点搜索和约束，它的决策能力其实已经能打到很高。但真正拉开差距的，不是模型，而是外面这层控制系统。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/7zwO3pRR032GNuhfmXSWN2hQc4zVQyHMGtXJ7jnuyodPkp7lgZCkPJVf2mHpC7icX0QLogfVy9mFFYk4uYabqj1DZLJZJKxQbqZW2IN9ia1Go/640.png)

（不断尝试LLM大模型的决策能力）

说白了，AI 在计算化学里从来不是“够不够聪明”的问题，而是你有没有能力让它不失控。

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/k7pH1kQonshpwPKUIiclSJjhCpy5qBa1eUrHms8xibSWYFqLQ7CEgcQel74ibK1yN8YQL9pDf2KmtCA6JyBZHnfIg/0.png) 

 计算化学简讯 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/k7pH1kQonshpwPKUIiclSJjhCpy5qBa1eUrHms8xibSWYFqLQ7CEgcQel74ibK1yN8YQL9pDf2KmtCA6JyBZHnfIg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
