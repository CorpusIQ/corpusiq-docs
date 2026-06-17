---
title: honcho-memory-usage
description: When and how to read/write Honcho via the honcho MCP server — server-side semantic memory that complements (does not replace) MEMORY.md and USER.md. The cold-storage pattern that survives session reset.
---

# Honcho Memory Usage

Honcho is a server-side semantic memory store wired into Hermes as an **MCP server**, NOT as the active memory provider. The built-in MEMORY.md + USER.md remain the hot path (injected into every system prompt for free). Honcho is the cold path: server-side semantic store you query on-demand via tool calls.

## Mental model

| Layer | What it holds | Cost | Latency |
|---|---|---|---|
| MEMORY.md / USER.md | ~12KB hand-curated declarative facts | injected every turn (in token bill) | zero — already in prompt |
| Skills | Procedural runbooks loaded on demand | one tool call when loaded | ~1s |
| session_search (SQLite FTS5) | Past conversation transcripts | one tool call | ~100ms local |
| **Honcho (this skill)** | Semantic representation built from messages we explicitly write | one MCP roundtrip + Honcho processing | ~500ms-2s per call |
| Honcho `chat` (dialectic) | Theory-of-mind queries against the representation | model call inside Honcho | ~2-5s |

Honcho is empty by default. It only knows what we tell it. Querying an empty workspace returns nothing useful — by design.

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

Don't read on every turn — Honcho roundtrips cost real latency. Use it like a card catalog, not like a system prompt.

## API shape (MCP-exposed tools)

The Honcho MCP server exposes (depending on configuration):

| Tool | Purpose |
|---|---|
| `mcp_honcho_add_messages_to_session` | Append messages to a session (the substrate Honcho builds the representation from) |
| `mcp_honcho_query_conclusions` | Semantic search over derived conclusions (facts/observations about a peer) |
| `mcp_honcho_chat` | Natural-language Q&A against the representation ("what does Honcho know about <topic>?") |
| `mcp_honcho_get_peer_card` | Compact biographical fact list |
| `mcp_honcho_get_peer_context` | Combines representation + peer card |
| `mcp_honcho_create_conclusions` | Manually inject conclusions (use for facts not derived from messages) |

## Workspace + peer naming

Each Hermes profile maps to a Honcho **workspace**. Multiple agents/sessions inside the same profile share a workspace. The **peer** identifies a single real human — typically the user's email or a stable identifier.

Confusing the boundary leads to "I queried Honcho and got nothing useful" — usually because you queried the wrong workspace or wrong peer.

## Cost discipline

Honcho is not free. Each `chat` call invokes a model inside Honcho's substrate, so:

- Default reasoning level: `low` or `medium` for most queries
- Use `high` or `max` only when the query is genuinely complex and the answer matters
- `query_conclusions` is cheaper than `chat` — prefer it when you want raw matched facts, not a synthesized answer

## When NOT to use Honcho

- You're trying to remember WHAT happened in a past session — use `session_search` against the local SQLite FTS5 store. Honcho's job is "what does Hermes know about the user/topic," not "what did we discuss on Tuesday."
- The fact is a one-liner — use MEMORY.md.
- You're building procedural knowledge ("how to do X") — use a skill, not Honcho.
- You need the fact in every turn's prompt — use MEMORY.md.

## Related

- [scheduled-jobs](../scheduled-jobs/) — cron jobs that need cross-session memory often want Honcho rather than ad-hoc state files


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
