---
title: Multi-Model Routing
description: "Intelligent model routing for Hermes agents — cost optimization, task classification, and provider fallback chains."
---

# Multi-Model Routing

Multi-model routing cuts operational costs by matching task complexity to the appropriate model. Simple tasks run on free local models. Complex tasks escalate to premium APIs. Result: significant cost savings versus single-model approaches.

## Routing Matrix

| Task Complexity | Model Class | Provider | Relative Cost |
|-----------------|-------------|----------|---------------|
| Routine execution | Small local model | Ollama (local) | Free |
| Content generation | Mid local model | Local GPU | Free |
| Complex reasoning | Frontier reasoning model | API | $ |
| Strategic analysis | Premium model | API | $$ |
| Architecture | Premium model | API | $$$ |
| Code generation | Code-specialist model | API | $ |

## Classification Logic

Tasks classified by context length, reasoning depth, output quality requirements, latency tolerance, and cost budget.

## Fallback Chains

```
Premium API → Reasoning API → Local model → Alert
```

Each tier falls back when the previous one fails, rate-limits, or exceeds its context window. The chain ends in an alert, never a silent failure.

## Implementation Tips

1. **Route by task signature, not vibes.** Parse the prompt for signal: code fences → code model; long context → big-window model; "summarize" → cheap model.
2. **Cache common classifications.** Re-classifying identical tasks wastes tokens.
3. **Log every route.** Cost attribution requires knowing which model handled what.
4. **Re-evaluate monthly.** Model pricing changes constantly; a routing matrix is only as good as its last audit.
