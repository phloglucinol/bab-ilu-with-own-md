---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzg4MjU5NTU3MQ%3D%3D&mid=2247485034&idx=1&sn=c0c66fa28ba1bf4291f85d91a567557c
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzg4MjU5NTU3MQ%3D%3D&mid=2247485034&idx=1&sn=c0c66fa28ba1bf4291f85d91a567557c
source_domain: mp.weixin.qq.com
title: 盘点计算化学的数据/网络安全措施
author: 
published_at: 
fetched_at: 2026-04-25T02:03:26Z
extractor: wechat_worker
content_hash: 7048c0723f230433739cbedfa54304117d1d37ed4a2b90ebf8925e71658bed22
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/7zwO3pRR033aUmkgDw0j5ISicql70AXgciaTqXbVVurZskTLKxPGVkr97V2icabmUicZW0tArwsBcrKYPWw1UqAGib6NO4sT1BnlDjXr5WEaEyIo/0.jpg) 

# 盘点计算化学的数据/网络安全措施

原创 计算化学简讯 计算化学简讯 [ 计算化学简讯 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

最近聊“养龙虾”的人不少。其实对于有服务器操作经验，懂网关、SSH的人来说，这事儿安全性不算低。关键的一点是，别把你的“龙虾”拉进有陌生人的群，然后服务器防护到位，基本出不了大问题。

服务器防护分等级，咱们从高到低聊聊。

## 第一等：物理隔离

### 安全性

这种方式最稳。服务器搁在独立房间，物理断网，跟互联网完全不沾边。物理层面的隔绝是安全的天花板。

### 便捷性

这就非常麻烦了。你想查个数据或者跑个程序，得人肉跑到机房去，坐在服务器跟前操作。这种方式没法远程办公，效率比较低。

---

## 第二等：知名云厂商

### 安全性

像Azure，AWS这种大厂，登录选手机查动态验证码，也就是多因素认证。只要你坚持用公钥登录，坚决不用弱口令，数据库里的东西就非常安全。云厂商有专门的团队盯着漏洞，比自己瞎折腾强得多。

### 便捷性

非常方便。你在家、在咖啡馆，只要有网就能登录管理。公钥配置好以后，登录也就是秒级的事，兼顾了安全和速度。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/k7pH1kQonsgVYhic1SiavgKMIqcCcjOXFibkBicawdW2X0Ef5iaibz5SVAIfvsACpTDYagNbQNmWg04krHLQia8J9FoZA/640.png)

（ChemOrchestra平台能完成大部分计算任务）

ChemOrchestra用的就是Azure做管理节点，非常安全。我每次登录需要用动态口令先解锁，然后公钥ssh才能上去，异常登录地址会报告。

用户每次拉取数据，需要登陆取得第三方公钥，然后传输到服务器鉴权，通过了才会发数据包。公钥是动态的，由Google管理。也就是说没有鉴权我没法通过正常渠道看你的计算内容。

而且云计算厂商的算力已经远远超越高校了，便捷而且便宜。

---

## 第三等：公网局域网混用环境

### 安全性

这是很多大学科研人员的现状，隐患不小。虽然学校会给学生发个代理（Proxy），开着代理连内网稍微安全点，但架不住有人私自开跳板机连通公网和内网。一旦有人开了后门，这一层的安全性就会直接掉到第四等。加多少堡垒机都没用，白花钱。

### 便捷性

还行。只要连上学校的代理，就能访问校内资源，但也受限于代理的带宽和稳定性。

---

## 第四等：私接跳板机

### 安全性

基本属于裸奔。有些人为了在家偷懒，嫌远程桌面麻烦，非要弄个SSH跳板机来回登。最坑的是一个跳板机给好几个人用，只要其中一个人用了弱口令，整个网络瞬间就会被攻破。

### 便捷性

最高。怎么登都行，怎么方便怎么来。但这种便捷是拿安全换的，属于典型的“省事不省心”。

---

大家得评估一下自己数据的价值。如果只是普通的科研数据，被黑了之后，黑客通常也就是拿你的超算资源去挖矿，损失点算力。但如果你是在药企，那情况就完全不同了。很多高价值的知识产权信息一旦被偷走，损失没法估量。防护等级一定要跟数据价值匹配。

有自己服务器的朋友肯定知道，端口几乎每个小时都在被扫描，现在黑客小偷都是自动运行的了。

企业建议就是数据物理隔离，麻烦点也没办法。

企业想部署AIDD/CADD计算资源，请联系我们，我们目前队列满了没法免费帮部署，可以提供些免费咨询，聆听您在工作中的难点和痛点，寻找AI解决之道。

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/7zwO3pRR0306ib8jbV7HDVJOGjaFQqZ5NAdTrH5MibtxQhzn619icBQrZN7pVfUAwU5WEaKPB2CuyEOeyeq070RH9UVEFHvC2vSlmfTex27Yw4/640.png)
  
  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/k7pH1kQonsjtD3AzMBNRibbMIVJK83PicfxQKKxcZgAqONLpL7dw6c1iaS99ymSibJzOQefoduiaP36S3jtAr6csR4A/640.png)

  
ChemOrchestra地址: www.quantabricks.xyz

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
