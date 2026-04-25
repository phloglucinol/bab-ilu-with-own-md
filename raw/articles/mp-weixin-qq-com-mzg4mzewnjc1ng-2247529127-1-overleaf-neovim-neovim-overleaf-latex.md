---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MzEwNjc1Ng%3D%3D&mid=2247529127&idx=1&sn=0d275b9cda17b712182d0ce83d96e0fc
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MzEwNjc1Ng%3D%3D&mid=2247529127&idx=1&sn=0d275b9cda17b712182d0ce83d96e0fc
source_domain: mp.weixin.qq.com
title: 告别 Overleaf 难用的网页编辑器！Neovim 实时协作神器现身：在 Neovim 里优雅地白嫖 Overleaf 的协作功能，LaTeX 生产力封神
author: 
published_at: 
fetched_at: 2026-04-25T02:03:39Z
extractor: wechat_worker
content_hash: 124e00ab8c7daf368af62541e5cb50551c5b928e4fccb6f66994dd8c4b05a99e
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/vibrboZtNUDPicDwBASZtlfHPxqvveiaeu3A8EFWTLr9jK940G4rI3m1mSdjGs8LNx45ibkUAv8chk4CSib1rEc8RCEaC27PibdUhprxnlwBUVaRo/0.jpg) 

# 告别 Overleaf 难用的网页编辑器！Neovim 实时协作神器现身：在 Neovim 里优雅地白嫖 Overleaf 的协作功能，LaTeX 生产力封神

原创 texer texer [ LaTeX工作室 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

点击👇“**LaTeX工作室**” **关注公众号**

精致科研生活从这里开始

  
对于很多科研党和研究生来说，Overleaf 是协作写 LaTeX 的不二之选。但说实话，Overleaf 的网页编辑器虽然方便，但在长期习惯了 Neovim/Vim 的老司机眼里，它缺少了太多的灵魂：没有极速的快捷键操作，没有定制化的 LSP 补全，更没有丝滑的 AI 插件（如 Copilot）支持。

虽然 Overleaf 官方提供了 Git 接入，但那是**非实时**的，每次都要 `git push` 和 `pull`，甚至还要加钱买 Pro 才能用。

今天，我们要安利一个硬核插件：**overleaf.nvim**。

#### 为什么它是“降维打击”？

这款插件彻底打通了 Neovim 与 Overleaf 的壁垒。它通过模拟 Overleaf 网页端的 WebSocket 通讯协议（OT 算法），实现了真正的**实时同步**。

1. **真正的实时协作**：你在 Neovim 里打出的每一个字符，Overleaf 网页端的导师几乎能瞬间看到。反之亦然，你甚至能在 Neovim 缓冲区里看到其他协作者的光标跳动。
2. **本地生态全开**：这是最爽的一点。你可以在编辑 Overleaf 项目时，使用你的 `LuaSnip` 快速输入复杂公式，开启 `TexLab` 进行语法检查，甚至让 `GitHub Copilot` 帮你写绪论。
3. **顺手的文件树**：插件内置了类似 `nvim-tree` 的侧边栏，新建、重命名、移动 LaTeX 文件直接在编辑器内搞定，改动会自动同步到云端。
4. **编译不再切屏**：一个命令直接触发云端编译，PDF 实时回传，整个流程完全不需要离开终端。

#### 如何开启？

安装非常简单（以 `lazy.nvim` 为例）：

```
{
  'richwomanbtc/overleaf.nvim',
  config = function()
    require('overleaf').setup()
  end,
  build = 'cd node && npm install' -- 需要 node 环境支持
}


```

_注：目前该插件通过自动提取 Chrome 浏览器的 Cookie 来实现认证（macOS 用户福利），非常方便。_

  
`overleaf.nvim` 填补了 Neovim 生态中最后一个“重磅场景”。它让“极致的本地编辑体验”与“极致的在线云端协作”完美融合。如果你正面临论文高压，又不想忍受网页编辑器的笨重，赶紧去 GitHub 给作者点个 Star 吧！

**项目地址：**`https://github.com/richwomanbtc/overleaf.nvim`

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/vibrboZtNUDOZ4RGWaz8Hnncd5opicklkDzLa3qk2NADCRMU6ictUuNF4UnL1lcNyoW2IiaiaA9eUic7kiadxnicvpSZbVgbrmRpQYE48Uxsr6fgKs4/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/iaSX7RicXX7kbaNxPURfn33XnA5M4Zx0W1oyR7UZB8icjiafSOJEvlVMuU5MicO9zUVqz88uw2yjwqmfY9IsiaY8s0yg/640.png)

更懂中文用户的 LaTeX 在线平台来了，点击领取福利！

**www.texhub.com**

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/iaSX7RicXX7kZI8Y8EHYWSdibfS0TUJ5INNkThdR5upIeh53bIRyOxVGchl3ChCYkehS123HczHL28hvpUP5q6XqA/640.jpg)

点击👇“**LaTeX工作室**” **关注公众号**

  
![图片](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_gif/NjA8gwicXyeLogiaTtO5FxiaHKoG9PkNcf1b9jFAz19hLdZ7ypHBHJfhZ0Sic2UzkLLNrRjMxjvQcO4fHHJV4Zk9Ig/640.gif)

● [LaTeX 重制最牛最难《中学数学实验教材》共 6 册-免费下载 - 增加百度网盘](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4MzEwNjc1Ng==&mid=2247517769&idx=3&sn=03d7ce6b45194540e1d70e96fb3a849c&scene=21#wechat%5Fredirect)

● [2026 最新国家自然科学基金项目 LaTeX 模版，科研党的福音来了！](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4MzEwNjc1Ng==&mid=2247528618&idx=3&sn=b726e39be1086b2b9dedfe4c0f965a70&scene=21#wechat%5Fredirect)

● [MathLive —— 轻松编辑数学公式的宝藏神器！即时渲染、支持 LaTeX 输入，完美公式编辑体验！](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4MzEwNjc1Ng==&mid=2247520326&idx=1&sn=ecf1129dbc0ed993c5f2746fbf505a6a&scene=21#wechat%5Fredirect)  

● [LaTeX 公式排版超级备忘录 - 各类场景全覆盖](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4MzEwNjc1Ng==&mid=2247513695&idx=1&sn=0f27998943a6f5e1057694950c883c9d&scene=21#wechat%5Fredirect)

● [高中物理甲种本第一册重制豪华版来了](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4MzEwNjc1Ng==&mid=2247520040&idx=1&sn=2d5702cfd8c05cf751cb778f3c2d2985&scene=21#wechat%5Fredirect)（附全套教材下载）

● [LaTeX 重排 838页 《数学分析新讲·三册》](https://mp.weixin.qq.com/s?%5F%5Fbiz=Mzg4MzEwNjc1Ng==&mid=2247521598&idx=1&sn=4dfe81e3b9f52db09d95a645fe1b7078&scene=21#wechat%5Fredirect)

  
预览时标签不可点

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/iaSX7RicXX7kYOcdkLHg3TLqZX6SgYd4hvcwNPFQzGhrI1icZ1hlPLfQDKg1kkjq3DunD6NhAGMzoyAdicyGcHJy1A/0.png) 

 LaTeX工作室 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/iaSX7RicXX7kYOcdkLHg3TLqZX6SgYd4hvcwNPFQzGhrI1icZ1hlPLfQDKg1kkjq3DunD6NhAGMzoyAdicyGcHJy1A/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
