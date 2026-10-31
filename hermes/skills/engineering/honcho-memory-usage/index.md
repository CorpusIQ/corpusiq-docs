---
title: "honcho-memory-usage - CorpusIQ Docs"
description: When and how to read/write Honcho  --  the catalog memory-provider plugin for server-side semantic memory that complements (does not replace) MEMORY.md and USER.md. The cold-storage pattern that survives session reset.
canonical: "https://www.corpusiq.io/docs/hermes/skills/engineering/honcho-memory-usage/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Honcho Memory Usage

Honcho is a server-side semantic memory store. It ships as a **catalog memory-provider plugin** maintained by Plastic Labs, so it is installed rather than bundled: `hermes plugins install honcho` (which pulls the `honcho-ai` SDK), then `hermes memory setup` and pick honcho. `hermes memory status` shows whether it is the active provider.

Two rules follow from that. Only **one** external memory provider can be active at a time, so Honcho either is the provider or it is not. And the built-in MEMORY.md + USER.md remain the hot path (injected into every system prompt for free); Honcho is the cold path - a server-side semantic store you query on demand.

## Mental model

| Layer | What it holds | Cost | Latency |
|---|---|---|---|
| MEMORY.md / USER.md | ~12KB hand-curated declarative facts | injected every turn (in token bill) | zero  --  already in prompt |
| Skills | Procedural runbooks loaded on demand | one tool call when loaded | ~1s |
| session_search (SQLite FTS5) | Past conversation transcripts | one tool call | ~100ms local |
| **Honcho (this skill)** | Semantic representation built from messages the provider syncs | one provider roundtrip + Honcho processing | ~500ms-2s per call |
| Honcho `honcho_reasoning` (dialectic) | Theory-of-mind queries against the representation | model call inside Honcho | ~2-5s |

Honcho is empty by default. It only knows what we tell it. Querying an empty workspace returns nothing useful  --  by design.

## When to WRITE to Honcho

The bar for writing is high. Most "save this" instincts should go to MEMORY.md instead. Honcho is for facts that:

- Are **too verbose for the prompt budget** (multi-paragraph context, longer narrative facts)
- Require **semantic search** to retrieve (you'll query by intent, not by key)
- Survive **across sessions** but don't need to be in every turn's context

Examples that belong in Honcho:
- "The 2026-06-10 architecture review decision: we picked Cloud Run over Lambda because of cold-start latency in the auth flow. Here's the full reasoning..."
- "Detailed customer profile facts: their team structure, their security posture, their tooling preferences, the specific objections they've raised over four calls"
- "Long-form vendor-specific lessons: every gotcha we hit during the Stripe integration over six months"

Examples that belong in MEMORY.md instead:
- "User prefers concise responses"
- "Project uses pytest with xdist"
- "Server-local time is GMT-7"

If you can express the fact in one sentence and it'll be useful every session, MEMORY.md. If it's multi-paragraph and you'll search for it semantically, Honcho.

## When to READ from Honcho

Read when:
- A topic comes up that you suspect has substantial prior context
- The user references a past decision you don't have in MEMORY.md
- You're starting work on a domain where Honcho might have stored context (e.g. "let's pick up the Stripe migration" → query for Stripe-related facts)

Don't read on every turn  --  Honcho roundtrips cost real latency. Use it like a card catalog, not like a system prompt.

## API shape (provider tools)

An active Honcho provider adds five tools (verified against the official memory-providers docs on Hermes Agent v0.22.5, 2026-10-30):

| Tool | Purpose |
|---|---|
| `honcho_profile` | Read or update the peer card - the compact biographical fact list |
| `honcho_search` | Semantic search across what Honcho knows |
| `honcho_context` | Session context: summary, representation, peer card, recent messages |
| `honcho_reasoning` | LLM-synthesized answer about the peer (the dialectic) |
| `honcho_conclude` | Create or delete conclusions - use for facts not derived from messages |

If Honcho is instead wired as a plain MCP server rather than the memory provider, the same capabilities surface as MCP tools named after the server (for example `add_messages_to_session`, `query_conclusions`, `get_peer_context`, `get_peer_card`, `create_conclusions`). Check `hermes memory status` and the tool list before assuming which shape you have - the query patterns below apply to both.

## Workspace + peer naming

Each Hermes profile maps to a Honcho **workspace**. Multiple agents/sessions inside the same profile share a workspace. The **peer** identifies a single real human  --  typically the user's email or a stable identifier.

Confusing the boundary leads to "I queried Honcho and got nothing useful"  --  usually because you queried the wrong workspace or wrong peer.

## Cost discipline

Honcho is not free. Each dialectic call (`honcho_reasoning`) invokes a model inside Honcho's substrate, so:

- Default reasoning level: `low` or `medium` for most queries
- Use `high` or `max` only when the query is genuinely complex and the answer matters
- `honcho_search` is cheaper than `honcho_reasoning`  --  prefer it when you want raw matched facts, not a synthesized answer
- The `dialecticCadence` and `dialecticDepth` settings in `honcho.json` cap how often the LLM call fires and how many passes it makes (1-3)

## When NOT to use Honcho

- You're trying to remember WHAT happened in a past session  --  use `session_search` against the local SQLite FTS5 store. Honcho's job is "what does Hermes know about the user/topic," not "what did we discuss on Tuesday."
- The fact is a one-liner  --  use MEMORY.md.
- You're building procedural knowledge ("how to do X")  --  use a skill, not Honcho.
- You need the fact in every turn's prompt  --  use MEMORY.md.

## Related

- [scheduled-jobs](../scheduled-jobs/)  --  cron jobs that need cross-session memory often want Honcho rather than ad-hoc state files

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
