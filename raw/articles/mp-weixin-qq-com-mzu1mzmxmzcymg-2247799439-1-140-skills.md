---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=MzU1MzMxMzcyMg%3D%3D&mid=2247799439&idx=1&sn=3e5ff04480c43f1fdbe0782fe2125fae
canonical_url: https://mp.weixin.qq.com/s?__biz=MzU1MzMxMzcyMg%3D%3D&mid=2247799439&idx=1&sn=3e5ff04480c43f1fdbe0782fe2125fae
source_domain: mp.weixin.qq.com
title: 上智院“浑天绫”开源：集成140+Skills协同，助力药物研发等科研流程端到端闭环
author: 
published_at: 
fetched_at: 2026-04-25T02:03:07Z
extractor: wechat_worker
content_hash: 71a7903bc3d431071f7b19c46f70c7f79d99a95e3cf4308b146b40f638dbb3da
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/r6tmXME0C0Mwsm1HRHPLM0av7gEmpgrQAm2Aq80c644ia1uC5SnXkeflfkA7EGE5JaZBpNEzDDxibvumfdnkAsMv3zcNia6Odq6iawibBJEB2580/0.jpg) 

# 上智院“浑天绫”开源：集成140+Skills协同，助力药物研发等科研流程端到端闭环

生物世界 生物世界 [ 生物世界 ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/r6tmXME0C0ON8pJGnOLrLN5JuIrhMbCgtrib5lm9gH12NVkassa1IrEVnpicicjmiamE3fz8NvRXvvPXsKLDkPaK4T787iaTggygzfw7W5gG8S7w/640.png)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/HO0Z9pUcnJlV2jS7njo2yHWKXEuoVJgqj6Ty7PyFickrkUtvlHflZpy6pPlSegh0ebfiaZ8OITW9oeryhfkh7BYw/640.other)

编辑丨王多鱼

排版丨水成文

  
物质科学研究领域不缺优秀的 AI 工具。

  
结构预测、分子生成、性质计算、反应模拟……各类模型在各自擅长的任务上表现出色，却彼此割裂。科研工作者的日常，往往陷在 N 个工具切换里：从一个平台导出数据，转换格式，导入下一个工具，重新调参——机械操作挤占了本该用于科学判断的时间。

  
工具本身不是问题，协作才是。

  
**“浑天绫”，就是上海科学智能研究院（Shanghai Academy of AI for Science，简称上智院）针对这一问题给出的系统性开源方案。**

继燧人物质科学系列模型，作为上智院在物质科学方向的又一落子，“浑天绫”现已覆盖药物发现、材料设计、催化剂优化、新能源研发等多个领域。基于其开源底座，上智院重点孵化企业“格物智研”将面向产业需求持续优化，提供产品化封装、企业级支持与商业扩展服务。

  
超 **140 个 Skills，“浑天绫”覆盖物质科学研发全流程**

作为一个开源物质科学发现系统，“浑天绫”目前已集成 4 大科学方向 140+ Skills。以药物发现为例，核心的 14 个 Skills 覆盖从靶点到候选分子的完整链条，展示了这套协作逻辑如何在真实流程中运转。

  
**第一步：自主调研。**输入靶点名称（例如“TYK2治疗自身免疫性疾病靶点”），进行靶点调研与专利查询，检索文献、提取生物学信息、排查已有专利。原本需要 1-2 天的文献整理工作，可压缩至 10 分钟以内。
  
  
**第二步：结合构象发现。**系统自动完成蛋白标准化处理（去水、加氢、优化侧链），若已有复合物晶体结构，进行分子生成；若无，先运行MD模拟优化，再通过口袋发现Skill定位药物结合位点。
  
  
**第三步：分子设计与筛选。**根据蛋白口袋进行分子生成，采用“粗筛+精算”策略：先用分子对接 Skill 从数百乃至数千个候选分子中快速筛出几十个，再用 FEP 计算 Skill 精确评估，锁定结合亲和力最强的分子。逆合成分析 Skill 进一步确定合成路线，确保设计的分子不只理论新颖，更具备落地合成的条件。

  
**第四步：确认与流转。**系统可以生成内部确认流程，并可直接对接合成询价系统。通过验证的候选分子完成入库，形成可供实验验证的先导化合物清单。

  
整个流程的核心价值不是单步更快，而是以统一环境部署的方式运行，所有环节由平台统一托管，数据在任务流中自动贯通，实现端到端的无缝衔接。科学家从工具操作中解放出来，专注于需要高度判断力的问题：选择哪个靶点、哪些分子值得验证、实验结果不理想时如何调整方向。

  
**为什么是 Skills 协作，而不是一个超大模型**

这是一个合理的疑问：既然要串联这么多模型和工具，何不训练一个统一的超大模型？

  
答案是：既不现实，也不必要。

  
分子对接依赖经过长期验证的物理化学算法，FEP 计算依托成熟的统计力学方法论，逆合成分析积累了化学家数十年的反应规则——这些专业能力早已经过充分验证，具备可靠性与可解释性。用通用大模型取代它们，不仅训练成本极高，更关键的是，科学家无法信任一个出了问题却无法追溯的“黑箱”。

  
“浑天绫”的方法论因此很清晰：**保留各环节专业模型和工具的核心能力，集中解决它们之间的协作问题。**

这套逻辑不只适用于药物发现，例如：

* **高分子材料设计**：原子尺度建模\-稳态结构生成\-性能模拟\-合成路线规划；
* **催化剂优化**：反应机理探索→反应数字化表征→反应构效关系建模→催化剂虚拟筛选→实验条件优化；
* **新能源研发**：基于性质约束的分子生成\-高通量氧化还原电位计算\-合成路线规划。
* 凡是具有明确研发流程、各阶段工具成熟、核心挑战在于环节整合的领域，均可适配。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/r6tmXME0C0Nciat8Su6OP7QnM2kicmMVEmJDNyngNltXOYibQDtLb4S9JQVocWW0btPjzwKVnaichJx6L0C6dGia0stiaa7hCnWWcLRI0oibnWGNR4/640.jpg)

  
**一个关键拐点，一套完整体系**

“浑天绫”的出现，根植于上智院对科学智能发展以及物质科学研究范式的整体判断。

  
科学智能（AI for Science）正处在一个关键的技术拐点：大语言基座模型提供逻辑推理，智能体系统实现流程编排，科学垂域模型融入领域机理，自动化实验室提供物理世界反馈——四者贯通之后，科研流程第一次具备了端到端自动化闭环的可能。

  
上智院物质科学团队由此出发：燧人物质科学系列模型首次统一建模了微观电子结构与宏观统计行为，使分子模型从经验拟合转向物理约束驱动，从专用工具升级为通用引擎。

  
然而，想法与可设计可合成之间仍存在显著断点。围绕这一痛点，上智院进一步布局了**浑天绫 Scientific Skills**（将算法、数据、算力、实验四类科研要素标准化为可组合的生产单元）、**智能实验设计智能体**（将高维设计需求转化为具体实验路径）、以及**自动化实验室**（应对非标物理操作、攻克后处理瓶颈、实现实验数据结构化）等关键技术，正着力构建**干实验\-连接层\-湿实验\-数据回流**的完整闭环。

  
**作为这一完整技术体系的产业化承载主体，“格物智研”正负责将系列原创成果推向真实产业场景，形成从基础模型到湿实验验证的平台级服务能力。**

**4 月新增一揽子物质科学开源 Skills**

本月，上智院物质科学团队新增开源一系列模型、数据与工具，包括燧人 AI 计算模型、craton 计算化学模型等，药物、材料、能源等领域用户可通过“浑天绫”调用，同时最新Skills 也已收录在星河启智科学智能开放平台（https://aistudio.ai4s.com.cn/）。

  
期待开源聚力，欢迎社区共建。

项目地址：https://github.com/golab-ai

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/73icnXvmN7wOI0rvtgpcAvoymzwXc4GsnicX7nxUa21NoWg2J48JaZ95yswdzic3MZ3Hagz97n5zdXiaMtm7ic36oTA/640.other)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/r6tmXME0C0O8rz6PGAUaLZsD04mzicCzE8VU45Us28icEfJAnic6bQyQibKONSvXtrYopMMRkYfwjhVfzJ6j8DdnObicqGyJhVnKvewAeA8bvYd8/640.jpg)

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/HO0Z9pUcnJmPk4iag8IdicOQhSkCOEhI10vnQicwUlPf2ialpAYdmzYrlVpcicLWjT7Hib8ajEo8Bbz1t52iaM6zZkubQ/640.other)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/HO0Z9pUcnJmPk4iag8IdicOQhSkCOEhI10gJJRKwUNkKhUqcj55lBzaMXv2Y2iaExAqFBf4CXibk9TP1LLzzgqZCuQ/640.other)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/HO0Z9pUcnJmPk4iag8IdicOQhSkCOEhI10iaZ62PXgrHr1RhZhPcddeFsKn5m2p5LElTzZTLnVnSK49vbJmm7cxPw/640.other)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/HO0Z9pUcnJmPk4iag8IdicOQhSkCOEhI10o3qRJVpkVYVkAvT13XS2DUTkibXVVWXuEcg0ic7gO2iaaYia11J5j2dKYg/640.other)

设置**星标**，不错过精彩推文

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_jpg/HO0Z9pUcnJkrZeMyHWr8nm80OyVfDQBpsT8rnQMxic0BEicTN0D4xTnoicumrbrBjUCh5uFtJEib7CLIeX8yxlUxcg/640.other)

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/HO0Z9pUcnJkmevYiaqUYPrQo4e6MgLEQP9TGLE88v8QWKaic8ricVmCA52SkIX35mtMzAiaQNibKmDhYNeK4uMzGRicQ/640.other)

**开放转载**

欢迎转发到朋友圈和微信群

 **微信加群** 

为促进前沿研究的传播和交流，我们组建了多个**专业交流群**，长按下方二维码，即可添加小编微信进群，由于申请人数较多，添加微信时请备注：**学校**/**专业**/**姓名**，如果是**PI**/**教授**，还请注明。

  
![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/HO0Z9pUcnJlXd8xpTjuxrR42rUB5g9TNU1N6Qj1tyRwfGJIKKDn85DRJk7kfyLfYP5XsvVVPqa9sE8pcfaevbQ/640.other)

  
**点** **在看** **，传递你的品味**

预览时标签不可点

修改于 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/HO0Z9pUcnJnhwMTrs8nr07jG4yxAmzK56h62nyc3WPlKeoMibr21GzCK75lPrysAjOkC2v6tvSllVv8ZBZqrlww/0.png) 

 生物世界 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/HO0Z9pUcnJnhwMTrs8nr07jG4yxAmzK56h62nyc3WPlKeoMibr21GzCK75lPrysAjOkC2v6tvSllVv8ZBZqrlww/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
