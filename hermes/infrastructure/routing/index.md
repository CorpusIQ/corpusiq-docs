---
title: "Multi-Model Routing - CorpusIQ Docs"
description: "Intelligent model routing for Hermes agents - cost optimization, task classification, and provider fallback chains."
canonical: "https://www.corpusiq.io/docs/hermes/infrastructure/routing/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes agent", "ai agent", "nous research"]

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

## What the local tier needs to be trustworthy

A local model only saves money if it cannot hold up the request. Four requirements, taken from a running deployment:

1. **An OpenAI-compatible endpoint on loopback.** One served model behind `/v1/chat/completions` on `127.0.0.1` keeps the router code identical for local and hosted models.
2. **Two deadlines, not one.** A soft deadline (10 seconds here) flags the call as slow while it finishes; a hard deadline (20 seconds) abandons it and records a failure. A single timeout value cannot express both.
3. **The router owns escalation.** The local model never decides to escalate. A timeout or transport failure returns control to the router, which chooses the next tier.
4. **A circuit breaker with a long cool-off.** After repeated failures in a short window, the local tier is disabled for the day rather than re-probed on every request.

## Implementation Tips

1. **Route by task signature, not vibes.** Parse the prompt for signal: code fences → code model; long context → big-window model; "summarize" → cheap model.
2. **Cache common classifications.** Re-classifying identical tasks wastes tokens.
3. **Log every route.** Cost attribution requires knowing which model handled what.
4. **Re-evaluate monthly.** Model pricing changes constantly; a routing matrix is only as good as its last audit.
