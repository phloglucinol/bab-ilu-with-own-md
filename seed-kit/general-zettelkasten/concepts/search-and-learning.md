---
type: concept
seed: true
bloom: understand
source: "[[sutton-bitter-lesson-2019]]"
---

# Search and Learning

Sutton's compound primitive: the two methods that absorb arbitrary amounts of computation without structural rework. Search = systematic exploration of a solution space (chess game-tree search, AlphaGo MCTS); Learning = function approximation that improves with more data + compute (self-play value functions, deep learning). Named together because Sutton treats them as *one pair* — a system that can only search but can't learn plateaus when the tree grows too large; a system that can only learn but can't search plateaus when training data runs out.

The slug is deliberately compound. Splitting into [[search]] and [[learning]] would lose the "one primitive pair" framing that's load-bearing in [[bitter-lesson]].

## Why it's a concept, not a note

Referenced from ≥2 independent notes:
- [[bitter-lesson]] — names search-and-learning as the pair that wins long-term
- [[scaling-hypothesis]] — references it as the mechanism of compute-absorption
