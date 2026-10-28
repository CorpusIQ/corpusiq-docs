---
title: "Prompt Caching for AI Agents: 98% Cache Hit Rate"
description: How Hermes Agent holds a 96 to 98 percent prompt cache hit rate. The structural rules that produce it, the four events that break it, and the exact queries for measuring cache hit rate on your own deployment.
category: best-practices
tags: [hermes-agent, prompt-caching, token-cost, cost-optimization, deepseek, anthropic, context-management, cache-hit-rate]
last_updated: 2026-10-27
canonical: "https://www.corpusiq.io/docs/hermes/best-practices/prompt-caching/"
robots: "index,follow"

---

# Prompt Caching  --  How an Agent Holds a 98% Cache Hit Rate

Prompt caching is the single largest cost lever in a long-running agent, and it is almost never a setting you turn on. A high cache hit rate falls out of how the prompt is built: a large, byte-stable prefix that gets re-sent every turn, and a small delta on top of it. Get the structure right and the hit rate sits at 96 to 99 percent by construction. Get it wrong and it collapses toward zero without any error being raised.

This page documents the mechanics and the measurement method used on a production Hermes Agent deployment (running DeepSeek V4.1 Flash and V4 Pro), so you can reproduce the numbers on your own install.

## Measured result

Measured on a production Hermes Agent deployment over a two-day window:

| Model | Hit rate |
|---|---:|
| deepseek-flash | 98.70% |
| deepseek-v4-pro | 96.81% |
| **All traffic** | **98.67%** |

The hit rate is not uniform across sessions, and the distribution is the useful part:

| Percentile | Hit rate |
|---|---:|
| Median session | 98.63% |
| 10th percentile | 97.29% |
| 90th percentile | 99.24% |
| Worst session | 60.24% |

Every session in the bottom tail is a short one (one to three API calls). A session that ends early never amortises the prefix it paid for, which is the whole story of the misses.

## Why 98% is structural, not tuned

The miss tokens come out at almost exactly one cold prefix per session:

```
miss tokens per session       =  one prefix  (about 47,000 tokens here)
miss share of all tokens sent =  1.33%
cache read per API call       =  about 103,000 tokens
```

Read that last line again. Every turn ships a prefix of roughly 100,000 tokens, and the provider charges the cached rate for about 98,700 of them. The cost driver is prefix volume, not per-token price, and the prefix is nearly free.

### Hit versus miss pricing

DeepSeek V4.1 bills cache hits at a small fraction of misses. Off-peak Flash pricing is $0.003 per million cached input tokens against $0.15 per million uncached  --  a 50x gap. Pro charges more on both sides ($0.022 cached against $0.66 uncached), so the ratio narrows to 30x while the dollar spread widens from about 15 cents to about 64 cents per million tokens.

Applied to a window where the cache covered 98.7 percent of input, the bill lands at roughly 3 to 4 percent of what the same traffic would cost uncached. That is what the hit rate buys. Anthropic's prompt caching shows the same shape at different absolute numbers: cache reads bill at roughly 10% of base input, and cache writes carry a small premium, so the crossover comes after a couple of turns rather than immediately.

## The four structural rules

### 1. Keep a large byte-stable prefix

System prompt, skills, memory, tool schemas and repo context belong in the prefix, and that block must not change between turns. In the deployment measured here that block is roughly 45,000 tokens and is identical call to call. Cache lookup is a prefix match: the moment any byte inside the block changes, everything from that byte onward is a miss.

Practical consequence: put volatile content (timestamps, run IDs, "current time is...") at the *end* of the prompt, never in the system block. A single `datetime.now()` interpolation in a system prompt guarantees a permanent zero percent hit rate.

### 2. Run long sessions and amortise the cold start

A cold start costs one full prefix prefill. Spread over 100 turns it is noise; spread over two turns it is the entire session cost. The measured worst sessions are 1 to 3 calls at 60 to 68 percent, and they exist because cron jobs and one-shot scripts open a fresh session to ask one question.

Practical consequence: for repetitive background work, prefer a `no_agent` script over an agent session. A script costs zero tokens and pays no cold prefix.

### 3. Never mutate the prefix mid-session

These four actions all rewrite the cached prefix and turn into a miss spike:

- Switching model mid-session (different cache namespace entirely)
- Reloading configuration, which rebuilds the system block
- Adding a skill or tool after turn one, which changes the tool schema region
- Context compression, which rewrites history

One compression event per long session is free. Five in one session is a miss pump. If a session must load extra skills, load them in the first turn so the prefix stabilises once.

### 4. Respect the cache TTL on idle gaps

Caches expire. Anthropic's short-lived tier is around five minutes by default, extendable; DeepSeek's automatic prefix cache tolerates longer idle gaps but is not permanent. An agent that thinks for 20 minutes, takes one call, then thinks again, re-prefills on every call.

Practical consequence: batch work into continuous bursts rather than spreading the same calls across hours, if latency allows.

## Measuring cache hit rate on your own install

Hermes records per-session, per-model token usage in the profile's `state.db`. Nothing here requires an API key or a dashboard.

```sql
-- Overall hit rate by model
select model,
       sum(api_call_count)                     as calls,
       sum(input_tokens)                       as miss_tokens,
       sum(cache_read_tokens)                  as hit_tokens,
       round(100.0 * sum(cache_read_tokens)
             / (sum(cache_read_tokens) + sum(input_tokens)), 2) as hit_pct
from session_model_usage
group by model
order by sum(cache_read_tokens) desc;
```

```sql
-- Sessions where the hit rate is worst: your cold-start offenders
select session_id, model, api_call_count, input_tokens, cache_read_tokens,
       round(100.0 * cache_read_tokens
             / (cache_read_tokens + input_tokens), 1) as hit_pct
from session_model_usage
where input_tokens + cache_read_tokens > 5000
order by hit_pct asc
limit 10;
```

```bash
sqlite3 -readonly ~/.hermes/profiles/<profile>/state.db \
  "select model, sum(api_call_count), sum(input_tokens), sum(cache_read_tokens) \
   from session_model_usage group by model;"
```

Three readings matter:

1. **Miss tokens divided by session count.** If that number is close to your prefix size, the caching is healthy and every miss is a legitimate cold start.
2. **The bottom 10 percent of sessions.** Confirm they are short sessions. If they are long sessions, something is mutating the prefix and needs finding.
3. **Cache read per call.** A rising value means the prefix is growing (more skills, more memory, longer history) and is the earliest warning that cost per turn is drifting up.

## Common mistakes

**Chasing the hit rate instead of protecting the prefix.** A hit rate is an outcome. The actions that improve it are structural: longer sessions, stable prefix, no mid-session mutation, fewer cold starts.

**Putting a timestamp in the system prompt.** The classic silent failure. The agent works perfectly and every single call is a full-price prefill.

**Compressing aggressively on short sessions.** Compression on a session that is about to end rewrites the prefix for no benefit. Compress at natural boundaries on long sessions.

**Assuming caching is off because the invoice is high.** At a billion tokens of monthly traffic, an invoice that looks large is usually volume, not a caching failure. Multiply tokens by the miss price to see what the cache is already saving you.

## FAQ

### Is prompt caching automatically enabled in Hermes Agent?

Yes for providers that support it. Hermes sends a stable prefix and does not strip the cache markers, so both Anthropic-style explicit caching and DeepSeek-style automatic prefix caching engage without configuration. The variable is your prompt structure, not a flag.

### What cache hit rate should I expect?

Long agent sessions with a stable prefix typically land between 96 and 99 percent. Anything under 90 percent on sessions longer than ten calls points to prefix mutation. One to three call sessions will always look poor and are not worth optimising individually.

### Does prompt caching work with local models?

Local inference servers have their own prefix caching, and it changes the economics differently: cached prefill saves latency rather than money. The structural rules are identical, so a prompt built for a cloud cache is also a fast local prompt.

### Why is the hit rate higher on the cheaper model?

Two reasons: high-volume daily work runs long sessions on the cheap model, and the expensive model gets the interrupted, sensitive tasks that are more likely to be one-off. Route the boring volume to the model with the longest sessions.

## Related Pages

- [Best Practices Overview](/hermes/best-practices)  --  All guides
- [Model Selection](model-selection.md)  --  Task-to-model mapping and fallback chains
- [Memory Management](memory-management.md)  --  Keeping the prefix small and stable
- [Cron Design](cron-design.md)  --  Avoiding cold starts in scheduled work

---

Protect the prefix, not the percentage.

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  445+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
