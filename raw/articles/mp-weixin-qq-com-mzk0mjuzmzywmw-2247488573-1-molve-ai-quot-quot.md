---
type: raw_article
source_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247488573&idx=1&sn=c06e0bb379e4b6c1fbd3d253094b3142
canonical_url: https://mp.weixin.qq.com/s?__biz=Mzk0MjUzMzYwMw%3D%3D&mid=2247488573&idx=1&sn=c06e0bb379e4b6c1fbd3d253094b3142
source_domain: mp.weixin.qq.com
title: MolVE：开源分子可视化与评估平台，填补 AI 药物发现&quot;人机协同&quot;缺口
author: 
published_at: 
fetched_at: 2026-04-25T02:03:13Z
extractor: wechat_worker
content_hash: a0f772a3937b591d502286da15a07f82682293bd537d61d2d0287931e3c51f8e
status: captured
---

![cover_image](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_jpg/47j3PUibeTAT8CEk8UyLkY0YtGhdhV0TqXghKfqZKUpQJY4wXRRfDQTVUxFxY1Ddj7OW5gSewpP9aVkD0kibTceibe7KUz8Paibwr4RFOBB38YI/0.jpg) 

# MolVE：开源分子可视化与评估平台，填补 AI 药物发现"人机协同"缺口

原创 DrugIntel DrugIntel [ DrugIntel ](javascript:void%280%29;) 

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

# ![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/47j3PUibeTATCaWKMgFYdlLJWrmONibVkUTJ7lunUUsumMjAATzISzuajuLhicFGyJcy2C7w0CicFUeIWGpFlUD6pLdzIbI8FRKJlDX0RgnxsKs/640.png)

> **论文信息**：Rigoni D, Sperduti A, Moro S. _MolVE: An Open-Source Web Platform for Visualizing and Evaluating AI-Designed Molecules to Aid in Prioritization_. J. Chem. Inf. Model. 2026, 66, 2427–2433.  
> **DOI**：10.1021/acs.jcim.5c02412
> 
> **开源地址**：https://github.com/drigoni/MolVE

---

## ![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/47j3PUibeTAR3GYs0TCDRke8ibqZ87IqtLDezVHhkjVyHKpdPtOGktG34pCgiaBeTfJy7MhRtX0P9u9HBrOmB6Eic1Q2MZvdz8hicqKGiczBDIazY/640.png)

## 一、研究背景

### 1.1 深度生成模型重塑药物发现范式

过去十年，人工智能在分子设计领域取得了革命性进展。深度生成模型（Deep Generative Models, DGMs）、强化学习（Reinforcement Learning, RL）以及大规模化学语言模型的涌现，使得计算机能够以每秒数千个结构的速度自动生成具有潜在药理活性的分子。这一能力从根本上改变了传统药物发现的逻辑——从"合成→测试→迭代"的线性实验范式，转向"大规模生成→智能筛选→重点验证"的数据驱动范式。

这一领域的代表性工作包括：

* • **图生成模型**：DiGress（离散去噪扩散）、MIDI（混合图与3D去噪扩散）、GeoMol（扭转角几何构象生成）
* • **变分自编码器**：条件约束图 VAE（CGVAE）、关系图条件 VAE（RGCVAE）
* • **流模型**：TumFlow（面向抗癌分子的归一化流模型）
* • **强化学习**：基于 Transformer 和策略梯度的分子生成
* • **化学语言大模型**：ChemBERTa-3 等基础模型

这些方法共同推动了"从虚空探索化学空间"成为现实，大幅压缩了早期药物发现的时间成本。

### 1.2 自动化过滤的边界与不可逾越的专家壁垒

尽管生成能力强大，AI 系统产出的候选分子在进入实验室之前，通常要经历多轮计算筛选：

| 筛选层级    | 典型指标                | 工具/方法            |
| ------- | ------------------- | ---------------- |
| 化学合法性   | 价键规则、原子价态           | RDKit            |
| 基础理化性质  | 类药五规则（Lipinski RO5） | RDKit、Open Babel |
| 合成可及性   | SAS 评分（1–10）        | RDKit            |
| 预测药理性质  | 溶解性、渗透性、毒性          | ADMET 预测模型       |
| 自然产物相似性 | NPS 评分              | ertl-NP          |

然而，经过上述过滤仍存活的候选分子往往数量可观。此时，**人类专家（化学家、药理学家）的审查不可或缺**，原因在于：

1. 1\. **结构直觉**：有经验的化学家能够从2D骨架中迅速识别"警戒结构"（structural alerts）、不稳定官能团或难以合成的环系，而这些特征难以被规则或模型完整覆盖。
2. 2\. **领域上下文**：药物候选的评估标准高度依赖适应症、靶点和给药途径，是高度情境化的判断。
3. 3\. **创造性发现**：专家有时能在结构中发现意外的优化方向或新颖骨架，这是自动化流程所不具备的创造力。

### 1.3 现有工作流程的系统性缺陷

在 MolVE 出现之前，业界普遍采用的"人工评估"方式存在以下系统性问题：

* • **工具碎片化**：PyMOL、Maestro、Discovery Studio 等本地软件各自为政，评估结果难以统一汇总。
* • **协作成本高**：邮件传递 SDF 文件、Slack 截图讨论——信息链条分散，版本混乱。
* • **无标准化框架**：不同团队、不同专家的评估维度和粒度各异，结果难以比较和复用。
* • **无法规模化**：当候选分子从数百扩展到数万时，现有工作流几乎崩溃。
* • **AI 建议无法融入**：ML 模型的预测分数与专家判断存在于完全独立的信息孤岛中。

正是在这一背景下，MolVE 被设计为**专门服务于这一"人在回路"关键环节**的基础设施工具。![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/47j3PUibeTAQhhaNBdDkXS66ZEIDzIvRGsFia7mNRRFOqiang3icOMZYB9bOay1CXwoRKOj6bM7tUnjplBSqxk44iayvNDmicK0icfANbicFPB2piaPw/640.png)

## 二、MolVE 平台架构与核心设计

### 2.1 系统架构总览

MolVE 采用经典的**四层全栈架构**，各组件职责清晰、松耦合：

`┌─────────────────────────────────────────────┐  
│              用户（专家 / 管理员）               │  
│         浏览器访问 or API 脚本调用              │  
└───────────────┬─────────────┬───────────────┘  
                │             │  
                ▼             ▼  
┌──────────────────┐   ┌─────────────────────┐  
│   前端界面         │   │   MolVE Backend API  │  
│ React + Tailwind  │◄──►│  Node.js + Express   │  
│ TypeScript        │   │  Passport (Auth)      │  
│ JSmol + Doodle   │   │  Drizzle ORM          │  
└──────────────────┘   └──────┬──────┬────────┘  
                               │      │  
                    ┌──────────┘      └──────────┐  
                    ▼                             ▼  
         ┌─────────────────┐          ┌──────────────────┐  
         │  Python 服务 API │          │    PostgreSQL     │  
         │  FastAPI         │          │    数据库          │  
         │  ML/DL 模型      │          │  分子 + 评估数据   │  
         └─────────────────┘          └──────────────────┘`

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/mmbiz_png/47j3PUibeTASgbKHExNZh9IOjiav168dF3o95k8vQ7q6BeqKjukLfpSVyUNDRjgfXaiashVJMK6Hstl4jhScGM8asehfuRVgKFJM8Xcj26VrTk/640.png)

**各层技术选型说明：**

| 层级    | 技术                            | 选型理由                |
| ----- | ----------------------------- | ------------------- |
| 前端    | React + TypeScript            | 组件化 UI，静态类型检查保障代码质量 |
| 样式    | Tailwind CSS                  | 实用优先，快速构建响应式界面      |
| 构建工具  | Vite                          | 极速 HMR，提升开发效率       |
| 后端    | Node.js + Express             | 非阻塞事件驱动架构，适合并发请求    |
| 认证    | Passport.js + express-session | 成熟的 Node.js 认证中间件   |
| ORM   | Drizzle ORM                   | 类型安全的数据库操作，减少运行时错误  |
| 数据库   | PostgreSQL                    | 关系型，支持复杂查询和事务       |
| ML 服务 | FastAPI（Python）               | 独立隔离部署，仅与后端通信，安全隔离  |
| 容器化   | Docker + Docker Compose       | 环境一致性，一键部署          |

### 2.2 用户权限体系

平台实现了**基于角色的访问控制（RBAC）**，分为两种账户类型：

**管理员（Administrator）**：

* • 访问管理后台仪表盘，查看全局统计（分子总数、评估数量、优先级分布）
* • 上传/删除 SDF 格式分子文件
* • 配置分子展示模式
* • 管理用户账户（增删、权限变更）
* • 设定访客访问策略（是否允许未登录浏览）
* • 导出完整评估数据集

**普通用户（Evaluator）**：

* • 登录后访问评估界面
* • 浏览分子的 2D/3D 结构与属性
* • 提交定性评估与标记

### 2.3 分子展示的三种模式

这是 MolVE 设计中体现**研究方法论**最深的部分，三种模式对应不同的实验设计需求：

#### 模式一：随机展示（Random Display Mode）

分子以随机顺序呈现，允许同一分子被**多位专家独立评估**，也允许同一专家对同一分子**重复评估**。

* • **用途 A — 多专家聚合**：化学家评估合成可行性，药理学家评估活性潜力，可后续加权融合多专家意见。
* • **用途 B — 专家一致性分析**：通过计算同一专家对同一分子的评估方差，可量化其评估的随机性与可靠性，为结果质量控制提供数据依据。

#### 模式二：未评优先（Unassessed-First Display Mode）

优先展示**尚无任何评估记录**的分子，确保大规模候选集的广覆盖。

* • **适用场景**：当分子集规模远超评估资源时，此模式最大化覆盖率，避免部分分子被重复评估而其他分子被忽略。

#### 模式三：共识优先（Consensus-based Display Mode）

平台允许同时上传来自**不同生成模型**的分子集（每个集合附带模型来源标签）。此模式优先展示**出现在多个模型输出中的分子**。

* • **设计灵感**：类比"专家委员会投票"——当多个独立模型不约而同推荐同一结构，该分子的置信度显著高于仅被单一模型产出的候选。
* • **应用价值**：在多模型比较实验中，可高效聚焦于真正具有跨模型共识的优质候选。

### 2.4 评估界面的信息架构

评估页面整合了多维度信息，辅助专家做出有据可查的判断：

**展示的分子属性：**

| 属性               | 说明                                 |
| ---------------- | ---------------------------------- |
| Canonical SMILES | 标准化线性分子表示，可下载 .sdf 文件              |
| 分子量（MW）          | 单位 g/mol                           |
| LogP             | 脂水分配系数，反映亲脂性                       |
| 氢键供体数（HBD）       | 影响口服吸收                             |
| 氢键受体数（HBA）       | 影响口服吸收                             |
| 合成可及性评分（SAS）     | 1（易）–10（难），Ertl & Schuffenhauer 方法 |
| 天然产物评分（NPS）      | 与已知天然产物的结构相似度                      |
| NPS 置信度          | 模型预测的置信区间                          |
| ML 优先级预测         | 随机森林模型输出的优先级建议                     |

**交互可视化组件：**

* • **2D 结构**：ChemDoodle Web Components 渲染，支持原子标注
* • **3D 结构**：JSmol 渲染，支持旋转、缩放、显示风格切换（球棍/棍状/空间填充）、颜色方案自定义

**结构化反馈表单：**

`优先级评分（三选一，单选）：  
  ○ ✦ 优先推进（Prioritize）  
  ○ ～ 边界情况（Borderline）  
  ○ ✕ 不予推进（Do Not Prioritize）  
  
问题标记（多选）：  
  □ 溶解性（Solubility）  
  □ 合成可及性（Synthetic Accessibility）  
  □ 分子尺寸（Dimension）  
  □ 膜渗透性（Permeability）  
  
附加注释（自由文本）：  
  [ 在此输入对该分子的补充说明... ]`

**为何选择定性标签而非数字量表？**

作者对这一设计选择给出了明确的方法论解释：不同背景的化学家对"5分"与"7分"的区别理解可能存在根本性差异，这种个体内在量表的不一致性会在聚合时引入高噪声。相比之下，"推进/不推进"这类决策导向的定性标签，直接对应研究流程中的实际决策节点，具有更强的语义一致性和可比性。

---

## 三、机器学习模块深度解析

### 3.1 当前内置模型

**模型类型**：随机森林分类器（Random Forest Classifier）

**特征工程**：Morgan 圆形指纹（Morgan Circular Fingerprints）

* • 由 Morgan（1965）提出，广泛用于分子相似性计算
* • 通过迭代聚合邻域原子信息，将分子编码为固定长度的二进制向量

**训练数据构成**：

| 类别      | 来源                  | 标签                |
| ------- | ------------------- | ----------------- |
| 正例（推进）  | FDA 批准药物数据集         | Prioritize        |
| 负例（不推进） | TumFlow 生成的高 SAS 分子 | Do Not Prioritize |

**训练策略**：5 折交叉验证，增强泛化能力

**部署方式**：封装于独立的 FastAPI Python 服务，仅对后端暴露接口，不直接对外开放，保障安全隔离。

**触发时机**：每次通过 REST API 上传新分子时，后端自动调用 ML 服务，将预测结果写入数据库并在评估界面展示。

### 3.2 模型局限性与未来方向

当前模型存在以下已知局限：

1. 1\. **训练集偏差**：正例全部来自 FDA 药物，负例来自特定生成模型，训练集分布可能无法代表真实的专家评估行为。
2. 2\. **任务单一**：目前仅预测"推进/不推进"二分类，不具备结构问题的细粒度预测能力（如无法区分"合成困难"与"溶解性差"）。
3. 3\. **缺乏适应性**：模型固定，无法根据具体项目的靶点和适应症进行调整。

**作者规划的演进路径**：

`第一阶段（当前）  
  随机森林 + Morgan 指纹 → 二分类优先级预测  
  
第二阶段（近期）  
  利用 MolVE 收集的专家标注数据  
  → 训练更强的分类模型  
  → 扩展为多标签预测（溶解性/合成性/渗透性问题识别）  
  
第三阶段（远期）  
  类 RLHF 框架：  
  专家反馈 → 奖励模型训练 → 指导生成模型产出更优分子  
  → 将 MolVE 嵌入强化学习闭环`

这一路线图体现了对 NLP 领域 RLHF（Reinforcement Learning from Human Feedback）思路的跨领域迁移，具有重要的方法论参考价值。

### 3.3 API 接口与编程集成

MolVE 提供 REST API，支持以下操作：

* • 批量上传 SDF 格式分子文件（附带元数据，如来源模型名称）
* • 查询特定分子的 ML 预测结果
* • 获取评估进度统计
* • 导出评估数据集（含用户身份、评分、标记、注释、时间戳）

这使得 MolVE 可无缝嵌入现有的计算化学流水线，例如：

`import requests  
  
# 上传一批 TumFlow 生成的分子  
with open("tumflow_molecules.sdf", "rb") as f:  
    response = requests.post(  
        "https://your-molve-instance/api/molecules",  
        files={"sdf": f},  
        data={"label": "TumFlow_v2"},  
        headers={"Authorization": "Bearer <token>"}  
    )  
  
# 查询评估结果  
evaluations = requests.get(  
    "https://your-molve-instance/api/evaluations/export",  
    headers={"Authorization": "Bearer <token>"}  
).json()`

---

## 四、案例研究：TumFlow 分子评估实践

为验证平台实际可用性，作者以 **TumFlow**（一种基于归一化流的抗癌分子生成模型）生成的分子集为对象，进行了完整的端到端演示：

### 流程回顾

`TumFlow 生成分子  
      ↓  
REST API 批量导入（SDF 格式 + 来源元数据）  
      ↓  
MolVE 后端自动解析 → 存入 PostgreSQL  
      ↓  
触发 ML 模型预测 → 优先级分数写入数据库  
      ↓  
评估界面展示：2D/3D 结构 + 理化属性 + ML 预测  
      ↓  
药物化学家通过浏览器评估（无需安装任何软件）  
采用"未评先行"模式，确保分子集全覆盖  
      ↓  
每位专家提交：定性标签 + 问题标记 + 注释  
      ↓  
所有记录归档至 PostgreSQL（含用户 ID、时间戳）  
      ↓  
管理员导出评估数据集 → 后续分析 / 模型训练`

### 案例揭示的关键价值

1. 1\. **模型无关性验证**：TumFlow 通过 API 接入，证明 MolVE 可作为**任意生成模型的通用前端评估界面**。
2. 2\. **人机判断对齐分析**：ML 模型预测与专家判断在同一界面并列呈现，化学家能够快速聚焦于**两者存在分歧的分子**——这类分子往往最具研究价值（要么是模型的假阳性，要么是人类直觉的盲区）。
3. 3\. **分布式评估可行性**：所有操作通过浏览器完成，无需部署专有软件，显著降低了多地团队协作的技术门槛。
4. 4\. **数据资产积累**：每一次专家评估都被结构化记录，形成可复用的**带人工标注的分子数据集**，为未来训练更强的预测模型奠定基础。

---

## 五、平台独特性总结

在现有化学信息学工具生态中，MolVE 的独特性体现在以下四个维度的协同：

### 5.1 以"优先级决策"为核心的评估框架

现有工具大多以**可视化或属性计算**为核心，评估决策是附加功能甚至缺失的。MolVE 将\*\*"是否推进该分子"\*\*作为第一设计原则，所有功能均服务于这一决策目标。

### 5.2 可配置的实验设计支持

三种展示模式（随机/未评先行/共识优先）不是简单的排序功能，而是**方法论层面的实验设计工具**，支持：

* • 多专家一致性研究
* • 多模型比较实验
* • 大规模数据集的系统性覆盖

### 5.3 人机协同的闭环架构

`AI 生成模型  →  大规模候选分子  
      ↓  
MolVE ML 服务  →  自动初筛（优先级建议）  
      ↓  
专家评估界面  →  人工审查（覆盖 AI 盲区）  
      ↓  
结构化评估数据  →  导出为标准格式  
      ↓  
反哺 AI 训练  →  更优的生成/预测模型  
      ↓（循环）`

### 5.4 评估数据的机器可读性

所有评估记录（分数、标记、注释、用户身份、时间戳）以**标准化格式**存储和导出，可直接用于：

* • 训练/微调 ML 分类模型
* • 构建强化学习的奖励信号
* • 进行专家一致性统计分析
* • 支持跨项目的元分析

---

## 六、部署与使用指南

### 6.1 快速部署

MolVE 完全容器化，部署仅需以下步骤：

`# 克隆仓库  
git clone https://github.com/drigoni/MolVE.git  
cd MolVE  
  
# 启动全部服务（前端、后端、数据库、Python ML 服务）  
docker-compose up -d  
  
# 访问平台  
open http://localhost:3000`

预览时标签不可点

[阅读原文](javascript:;) 

微信扫一扫  
关注该公众号

继续滑动看下一个 

轻触阅读原文 

![](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icaZmJVvQe5nCiabibOyaceianZY23nlsXAkxR5uiajvHibdBJvESicc58tOeibVXmVTp4HVVADZh79C1iczA/0.png) 

 DrugIntel 

向上滑动看下一个 

[知道了](javascript:;) 

 微信扫一扫  
使用小程序 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

[取消](javascript:void%280%29;) [允许](javascript:void%280%29;) 

× 分析 

![作者头像](https://mp-r2.084817.xyz/mmbiz_qpic_cn/sz_mmbiz_png/KoRXqKjLA9icaZmJVvQe5nCiabibOyaceianZY23nlsXAkxR5uiajvHibdBJvESicc58tOeibVXmVTp4HVVADZh79C1iczA/0.png) 

微信扫一扫可打开此内容，  
使用完整服务

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
