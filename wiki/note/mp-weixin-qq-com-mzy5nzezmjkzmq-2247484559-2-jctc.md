---
type: note
lens: general-zettelkasten
slug: mp-weixin-qq-com-mzy5nzezmjkzmq-2247484559-2-jctc
kind: other
ingested_at: 2026-04-25T02:31:15Z
input_type: markdown
source_path: raw/articles/mp-weixin-qq-com-mzy5nzezmjkzmq-2247484559-2-jctc.md
bloom: analyze
concepts:
  - data-free-inverse-design
  - qm-in-the-loop-rl
  - diversity-reward-prevents-local-traps
  - representation-shapes-search-space
layer_1_bolds:
  - "其核心创新在于完全摒弃预训练数据集，将强化学习与即时量子力学计算深度耦合，实现从第一性原理出发的分子从头设计。"
  - "P-SMILES基于经典SMILES表示法，但通过限制每个结构基元最多使用两个字符来编码，大幅降低了语法复杂性，消除了SMILES语法中因编码不等价性而产生的生成偏差。"
  - "模型的总奖励函数将化学奖励与多样性奖励相结合。"
  - "PROTEUS在9次中均成功找到了全局最优解，平均仅需评估约1000个分子。"
layer_2_fragments:
  - "不用预训练集，直接用量子化学当老师"
  - "表示法先收缩，搜索才不会乱跑"
  - "层次化RL是在适配化学语法，不只是堆模型"
  - "多样性奖励决定能不能跳出局部最优"
  - "先在可枚举空间里做严格基准很重要"
layer_3_thesis: "PROTEUS让我看到，真正稀缺的不是再换一个生成器，而是把表示、奖励和量子化学评估闭成一个无数据偏置的搜索回路。"
status: complete
---

# mp-weixin-qq-com-mzy5nzezmjkzmq-2247484559-2-jctc

## Layer 1

- **其核心创新在于完全摒弃预训练数据集，将强化学习与即时量子力学计算深度耦合，实现从第一性原理出发的分子从头设计。**
- **P-SMILES基于经典SMILES表示法，但通过限制每个结构基元最多使用两个字符来编码，大幅降低了语法复杂性，消除了SMILES语法中因编码不等价性而产生的生成偏差。**
- **模型的总奖励函数将化学奖励与多样性奖励相结合。**
- **PROTEUS在9次中均成功找到了全局最优解，平均仅需评估约1000个分子。**

## Layer 2

- **不用预训练集，直接用量子化学当老师**
- **表示法先收缩，搜索才不会乱跑**
- **层次化RL是在适配化学语法，不只是堆模型**
- **多样性奖励决定能不能跳出局部最优**
- **先在可枚举空间里做严格基准很重要**

## Layer 3

PROTEUS让我看到，真正稀缺的不是再换一个生成器，而是把表示、奖励和量子化学评估闭成一个无数据偏置的搜索回路。

## Concepts

- [[data-free-inverse-design]]：重要，因为它把“生成前先吃大数据”从默认前提改成了可被绕开的工程选择。
- [[qm-in-the-loop-rl]]：重要，因为这类方法的价值不在 RL 本身，而在量子化学评估被直接拉进训练闭环。
- [[diversity-reward-prevents-local-traps]]：重要，因为分子优化里多数失败都不是不会爬坡，而是过早收敛。
- [[representation-shapes-search-space]]：重要，因为 P-SMILES 说明表示法不是输入格式，而是搜索边界条件。

## Back-references

- [[mp-weixin-qq-com-mzg4mju5ntu3mq-2247485141-1-harness]]：这篇会把 PROTEUS 看成一个完整 harness，而不是一个“无数据 RL 模型”；关键差别在于量子化学验证管线本身就是控制系统。
- [[mp-weixin-qq-com-mzyymzi1ndi3ma-2247486416-1-science-advances-2026-sefmol]]：SeFMol 强调在生成过程中做策略校正，回看这篇就会发现 PROTEUS 的强化学习不是后验 rerank，而是生成路径本身的控制器。
- [[mp-weixin-qq-com-mzyzota3njkxmg-2247583036-1-j-med-chem]]：AutoOptimizer 依赖专家规则和迁移学习扩展策略库，这会反过来凸显 PROTEUS 的激进之处：它尽量不借人类已有化学偏见。

## Source
- Input: `raw/articles/mp-weixin-qq-com-mzy5nzezmjkzmq-2247484559-2-jctc.md`
- Type: markdown
- Kind: other
