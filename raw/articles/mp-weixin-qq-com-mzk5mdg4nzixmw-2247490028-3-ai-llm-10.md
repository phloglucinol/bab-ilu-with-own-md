---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk5MDg4NzIxMw%3D%3D&mid=2247490028&idx=3&sn=1a4af3bbd5bef9131ee68ea3c20b8f17
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk5MDg4NzIxMw%3D%3D&mid=2247490028&idx=3&sn=1a4af3bbd5bef9131ee68ea3c20b8f17
source_domain: mp.weixin.qq.com
title: 当 AI 接管“祖传代码”：LLM 智能体如何让经典分子动力学软件提速 10 倍？
author: 
published_at: 
fetched_at: 2026-04-25T02:03:20Z
extractor: wechat_worker
content_hash: e82326e1b4a6b1768ff59bf664ec510e7634c63a07234ba72da622ae305b016e
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/go7AJtwLtFjudCVLnBQb4p17s4hH84dvCiaRyxc8ORqqhREtN06MlKxJC78BM3IicjicSWGvQ4Oa12VPUlCEaMxPDqJOjc6Av4gwhyuynRPV54/0.jpg) 

# 当 AI 接管“祖传代码”：LLM 智能体如何让经典分子动力学软件提速 10 倍？

原创 科研小猪莹 科研小猪莹 [ 科研小猪莹 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/go7AJtwLtFiad02ibP5RoPQHSIsZQHF0XSECefTzvQV20YDuaAX7kyglx2J40LPOm58xvQItOIURl0sQnjevULzkE9BaYdGRtjCfsoEvnv1Zg/640.png)

# **摘要概括**

 大语言模型（LLM）正迅速从简单的代码辅助工具演变为能够自主读写、修改和测试代码库的“智能体”。本文展示了如何利用最新的 LLM 智能体（如 Claude Code），解决经典分子动力学套件 AMBER 中参数化工具 LEaP 的性能瓶颈。

 面对处理百万原子级别体系时的 复杂度合并算法和 32 位整数溢出问题，研究者借助 LLM 实现了算法优化和 64 位索引升级。这一改进将中型体系的参数化时间缩短了 10 倍以上，并使得千万级原子体系的参数化成为可能。该案例不仅展示了 LLM 在现代科学计算工具开发中的巨大潜力，也引发了关于软件开发模式和科学验证的新思考。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/go7AJtwLtFgd4baLNkwKarKNCQadOGd3GvQJbH8A6Xfkeond4OJodNTiccm9ddJuu9iccyRL6adicrbZ3HiaUNJ2hCQsjXViaqjOHk57cOmcAY68/640.png)

# **研究背景**

 近年来，大语言模型（LLM）在软件工程领域引发了革命。从最初的代码补全，发展到如今以 Claude Code、OpenAI Codex 为代表的“Agentic AI”工具，AI 已经能够直接连接本地代码库，进行复杂的上下文理解、代码修改和调试。

 与此同时，在生物和化学信息学领域，许多核心算法虽然经典，但代码库往往建于上世纪 90 年代（如 AMBER 套件中的 LEaP）。这些“祖传代码”虽然科学上正确，但受限于当时的硬件视野和编程习惯，往往未针对现代超大规模体系（如数百万原子）进行优化，且代码量庞大、逻辑复杂，人工重构难度极高。

# **研究问题**

 AMBER 分子动力学套件中的核心参数化工具 **LEaP** 在处理超大规模体系（如包含数百万水分子的盒子）时面临严重性能瓶颈：

1. **运行时间过长**  
：随着原子数增加，某些合并操作的时间复杂度呈 $O(N^2)$ 增长，导致参数化过程耗时甚至超过一天。
2. **程序崩溃**  
：当体系原子数超过约 600 万时，程序会因为 32 位整数溢出而崩溃，限制了现代超大规模模拟的开展。

 传统的优化手段需要开发者深入理解数百万行代码的逻辑，成本极高。本文试图回答：**当前的 LLM 智能体是否能够介入这一过程，辅助科学家高效地诊断并解决这些深层的软件工程问题？**  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/go7AJtwLtFia1BpmjAEnDia96DmBWMKbGibQibzIDNjRpW2nuSiaHZwA8g2Do8dZ6mibat3rLpyhEMEn8pojsMsRDAhaTcM0XrefJQYA24bialpAyY/640.png)

# **研究方案**

 研究者采用了具备“智能体”能力的 LLM 工具，具体流程如下：

1. **性能剖析**  
：研究者首先对 LEaP 代码进行编译并开启性能分析选项，将 `gprof` 生成的性能分析数据提供给 LLM 智能体。
2. **瓶颈识别**  
：LLM 通过分析数据，迅速定位到性能瓶颈在于“单元合并”函数。原代码在每次合并时都需遍历所有残基以查找最高编号，导致 $O(N^2)$ 的复杂度。
3. **算法优化**  
：LLM 提出了采用哈希方法的优化策略，将复杂度降低至 $O(N)$。经进一步讨论，最终确定了直接赋值的优化方案。
4. **Bug 修复与扩展**  
：在大幅提升运行速度后，LLM 协助定位了导致大体系崩溃的根因——数组索引使用了 32 位整数。研究者将相关索引升级为 64 位，从而解除了原子数量的硬性限制。  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/go7AJtwLtFgSn0GfuYql452edzu8fFO7TLLJU8vLFfIRocslpwyQgmHETIfyPsRhDeecPfhibwgZEbl3qOq5qzZcuXnE0XsnM7bPCajh3Ehc/640.png)

# **研究结论与创新点**

**1\. 惊人的性能提升**  
优化后的 LEaP 在处理百万原子体系时，速度提升了 100 倍以上。对于一个包含 540 万原子的蛋白-膜体系，原本需要约 1 天的参数化过程，现在仅需不到 3 分钟即可完成。

**2\. 突破体系大小限制**  
通过将 32 位整数更新为 64 位，LEaP 现在可以处理超过千万级原子的体系（目前上限受限于文件格式，约为 1100 万原子），且这些改进已并入 AMBER26 版本。

**3\. 开发范式的转变（创新点）**  
本文最大的创新在于展示了“氛围编程”在科学计算领域的可行性。科学家不再需要逐行编写底层代码，而是作为“架构师”引导 AI 智能体进行代码重构。这表明，对于非计算机专业出身的科研人员，利用 LLM 智能体维护和现代化老旧的科学计算软件已成为一种高效的新路径。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/go7AJtwLtFjD0lsr481uQoj5bSEHQZFCkjIj5tJm7PK9qxYL5zDLjCqeV8bbPHbK17sicQkkMJg9GQR4NlE8bKFNbibIXDbyTOfIlBRYbnH14/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/4lAAmTGicmg0WqvUAo1R60SvV1wrJ6LSaibmHYufQHntqQU1nZVTWzWvSyPQZbXvy9bUVoHCicKTwVCbgGoib39A1g/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/xrUbVt0eL75B6SbmKeCuTp08jYbYreGlRjurRKroibjc1HvSxnrUcGWmL1XMaCTa8LCiaxHUKHa1cZem1Ih9iaUUg/640.png)

点击下载原文

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/dTxkmqQ6SznicxdpxUKbBLoJzSlpvNfyfeGn8PIB1Wx5kSbhECECnibDwEYfQrkyyjQibSo1zMUX5sJo4KzcibF9GQ/640.gif)

chat-driven-computational-(bio)chemistry-using-llm-agents-to-accelerate-bio-and-chemoinformatics.pdf

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/4ZCae4yl53klulj6O0b7N5ze7sPltptcv23a1eYD0799Y8awib665MZbVGTgeeAHQH3hFnibibXNL2OzSRmaoic5ww/640.gif)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0hGlkrDOFIcm5MrJ8RHlb2qVOo0KGk4rlMlGuun6icrsibp7vHagF29FIAGxkUowpMKoicPCQJPUibEQ/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/4ZCae4yl53klulj6O0b7N5ze7sPltptcv23a1eYD0799Y8awib665MZbVGTgeeAHQH3hFnibibXNL2OzSRmaoic5ww/640.gif)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0hGlkrDOFIcm5MrJ8RHlb2Hyq2kjQ8GhktGfMNPtYx3Q5dtWI142tzhmXJdicAFnxkoVYF7tDjUCg/640.png)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_gif/4ZCae4yl53klulj6O0b7N5ze7sPltptcv23a1eYD0799Y8awib665MZbVGTgeeAHQH3hFnibibXNL2OzSRmaoic5ww/640.gif)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0hGlkrDOFIcm5MrJ8RHlb2KgqDQxBVUD8qYWoHbnicWn3Yzwx8FTJ5LBfUFodR80DYYicwksQ1CibvA/640.png)

[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/ukAs1n8gyX2PBVf5rPPkrmo8LcUX2V0HxRNyrKJWnyLgsicFQINzHgHkMUIAPNHutxoILvOiaCVmSM99krKq2aKQ/640.jpg)](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzk5MDg4NzIxMw==&mid=2247484900&idx=1&sn=f0c125f9bf6c1f42548e07eec0c89107&scene=21#wechat%5Fredirect)

[9.9分子对接带你从0-100](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzk5MDg4NzIxMw==&mid=2247484900&idx=1&sn=f0c125f9bf6c1f42548e07eec0c89107&scene=21#wechat%5Fredirect)

  
[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/ukAs1n8gyX1xcKwuFoWbnuxNAseuQZfnIU0SBxFXPfWP5Nw8QBEvTpI9oGYuVXicoQseEsX7sN1dcavN3cf9c6A/640.jpg)](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzk5MDg4NzIxMw==&mid=2247486139&idx=1&sn=d07decfbf48c91b3f8973303aaa1283c&scene=21#wechat%5Fredirect)

[9.9 独家蛋白对接](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzk5MDg4NzIxMw==&mid=2247486139&idx=1&sn=d07decfbf48c91b3f8973303aaa1283c&scene=21#wechat%5Fredirect)

  
[![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/ukAs1n8gyX0hGlkrDOFIcm5MrJ8RHlb2pLicLOxQic33oSYkia4pfiavKG5ESZ4I9ibPNIKKXZcTdnN17c93GicfjJFg/640.jpg)](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzk5MDg4NzIxMw==&mid=2247488322&idx=1&sn=71cf2123d8acb0832fa67f12375ca9af&scene=21#wechat%5Fredirect)

[9.9 单蛋白模拟](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzk5MDg4NzIxMw==&mid=2247488322&idx=1&sn=71cf2123d8acb0832fa67f12375ca9af&scene=21#wechat%5Fredirect)
  
  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0K5tG3KpVl4QZEn5BE5WWicAYLShBmlhVLWhHBAuOQFX0YkGHF1s9M4A2I2iapd7wJOB3OQm3rMNyg/0.png) 

 科研小猪莹 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/ukAs1n8gyX0K5tG3KpVl4QZEn5BE5WWicAYLShBmlhVLWhHBAuOQFX0YkGHF1s9M4A2I2iapd7wJOB3OQm3rMNyg/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
