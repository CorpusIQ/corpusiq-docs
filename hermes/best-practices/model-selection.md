# Model Selection Guide

Choosing the right model for each task is one of the highest-leverage decisions you make with Hermes. A well-chosen model saves latency, cost, and context — missteps waste all three.

## The Decision Framework

Ask three questions before every model selection:

1. **What does the task require** — reasoning depth, factual precision, creative generation, or tool orchestration?
2. **What is the latency budget** — real-time user interaction, batch processing, or background work?
3. **What is the cost tolerance** — per-request budget, daily volume, or fixed monthly spend?

The answers push you toward different points on the speed/capability/cost tradeoff triangle.

## Task-to-Model Mapping

**Routine classification and routing.** These tasks (intent detection, simple extraction, triage) don't need frontier models. A capable small model handles them at 5-10x lower cost and 3-5x lower latency. Examples: routing user questions to the right skill, extracting structured fields from emails, classifying support ticket categories.

**Data extraction and summarization.** Mid-tier models shine here. You need reliable reading comprehension but not novel reasoning. Summarizing meeting transcripts, extracting action items from Slack threads, pulling structured data from unstructured text — all work well with balanced cost/capability models.

**Complex reasoning and code generation.** Frontier models earn their cost here. Multi-step reasoning, debugging across files, architectural decisions, and complex tool orchestration benefit from the strongest models. The cost premium is justified because failed reasoning causes cascading errors downstream.

**Creative and narrative generation.** These tasks depend on style more than correctness. Choose models known for prose quality in your domain. Test with real users — your intuition about what "reads well" may not match audience preferences.

## Cost Optimization Strategies

**Caching.** Before you touch model selection, implement prompt and response caching. If 40% of your queries are variants of the same 5 intents, caching those results eliminates unnecessary inference.

**Prompt compression.** Long context is expensive. Summarize conversation history before passing it to expensive models. Strip irrelevant tool output. Use the shortest prompt that produces reliable results — every token saved is cost saved.

**Task batching.** If you have 50 similar records to process, can they share context? Batch processing reduces per-item overhead. Some providers offer batch endpoints at 50% discount for non-urgent work.

**Model fallback chains.** Implement cascading fallbacks: try the cheapest model first; if confidence is low, escalate to a mid-tier model; if still uncertain, invoke the frontier model. This "progressive enhancement" approach gives you frontier quality on hard cases while keeping average cost low.

## Local vs. Cloud: The Real Tradeoffs

**Local models win when:** data privacy is non-negotiable, latency must be sub-50ms, you operate in disconnected environments, or you process enough volume that fixed hardware cost beats per-token pricing. They lose when you need frontier reasoning, when your hardware is underpowered, or when model maintenance overhead exceeds your team's capacity.

**Cloud models win when:** you need the strongest reasoning, want zero infrastructure maintenance, need elastic scaling, or require multi-region availability. They lose when data sovereignty is at stake, when per-token costs balloon on high volume, or when API latency adds unacceptable delay.

**Hybrid is practical for most teams.** Classify and extract with local models; reason and generate with cloud models. This gives you privacy, low latency for routine work, and frontier capability on demand.

## The Fallback Chain Pattern

Implement this decision tree:

1. **Check cache.** If an identical or semantically equivalent query was answered recently, return the cached result.
2. **Try primary model.** Send to your default model for this task class.
3. **Validate output.** Check for required structure, completeness, confidence scores.
4. **Escalate if needed.** If validation fails, retry with a stronger model and expanded prompt.
5. **Track fallback rate.** If escalation exceeds 10% of requests, your primary model is too weak for this task.

## Practical Decision Tree

```
Is the task classification/routing? → Small model
Is it data extraction from known formats? → Mid-tier model
Is it summarization of medium-length text? → Mid-tier model
Is it multi-step reasoning or debugging? → Frontier model
Is it creative writing or brand content? → Style-appropriate model (test!)
Is it a background batch job? → Cheapest model that's reliable
Is latency critical (sub-second)? → Local model or fastest cloud option
Is data sensitive/regulated? → Local model or approved cloud with BAAs
```

## Measuring What Matters

Don't optimize model selection by vibes. Track:

- **Task success rate** per model (did the output require human correction?)
- **End-to-end latency** (model + validation + post-processing)
- **Cost per successful task** (not per token — per useful output)
- **Fallback rate** (how often the primary model delegates)

Revisit your model choices monthly. Model quality and pricing change fast, and yesterday's optimal choice may be today's wasteful default.
