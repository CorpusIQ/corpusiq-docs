---
title: Reflexion Self-Improving Agents
description: Self-improving agent loops via Reflexion. Evaluation, reflection generation, working memory updates, iterative improvement.
---

# Reflexion Self-Improvement

[Reflexion](https://arxiv.org/abs/2303.11366) (NeurIPS 2023) gives agents the ability to learn from their own mistakes through structured self-reflection loops.

## Architecture

```
Attempt → Evaluate → Reflect → Update Memory → Retry
   ↑                                              ↓
   └────────── Improved Attempt ←────────────────┘
```

## How It Works

1. **Attempt**: Agent performs a task (write code, draft content, run analysis)
2. **Evaluate**: Output is tested/scored against success criteria
3. **Reflect**: Agent analyzes what went wrong and why
4. **Update Memory**: Lessons are stored in working memory
5. **Retry**: Agent tries again with the improved understanding

```python
class ReflexionLoop:
    def __init__(self, max_attempts=5):
        self.max_attempts = max_attempts
        self.memory = []
    
    def run(self, task, evaluate_fn, reflect_fn):
        for attempt in range(self.max_attempts):
            # 1. Attempt
            output = task.execute(memory=self.memory)
            
            # 2. Evaluate
            score, feedback = evaluate_fn(output)
            
            if score >= task.threshold:
                return {"status": "success", "output": output, "attempts": attempt + 1}
            
            # 3. Reflect
            reflection = reflect_fn(output, feedback, self.memory)
            
            # 4. Update memory
            self.memory.append({
                "attempt": attempt + 1,
                "output": output,
                "score": score,
                "reflection": reflection,
                "lesson": f"Avoid: {reflection['mistake']}. Try: {reflection['fix']}"
            })
        
        return {"status": "failed", "attempts": self.max_attempts, "memory": self.memory}
```

## CorpusIQ Usage

Reflexion powers self-improving agent behaviors:
- **Content quality improvement** — post → measure engagement → reflect → improve next post
- **Cold email optimization** — send → track response rate → reflect → adjust messaging
- **Code review loops** — PR → review feedback → reflect → improve future commits
- **SEO tuning** — publish → track rankings → reflect → adjust content

## Key Concepts

| Concept | Description |
|----------|------------|
| Attempt | A single execution of the task |
| Evaluation | Scoring output against criteria |
| Reflection | Analysis of what failed and why |
| Working Memory | Accumulated lessons across attempts |
| Threshold | Success bar for stopping the loop |
| Max Attempts | Hard limit to prevent infinite loops |

## Patterns

1. **Binary evaluation** — pass/fail on correctness (code compilation)
2. **Numeric scoring** — 0-100 on quality metrics (engagement rate)
3. **LLM-as-judge** — another agent evaluates output quality
4. **Human feedback** — pause loop, wait for human review

## Pitfalls

- **Overfitting**: Agent may optimize for the evaluation metric, not the real goal
- **Context bloat**: Memory grows with each attempt, need compaction
- **Diminishing returns**: After 3-4 attempts, improvements are marginal
- **Wrong evaluation**: If your eval function is wrong, reflection teaches wrong lessons

## Resources

- [Reflexion Paper (NeurIPS 2023)](https://arxiv.org/abs/2303.11366)
- [LangGraph Reflexion Implementation](https://blog.langchain.dev/reflexion/)
- [Reflexion GitHub](https://github.com/noahshinn/reflexion)

---

*← [LangGraph](/hermes/orchestration/langgraph/) | [Orchestration ↑](/hermes/orchestration/)*
