---
title: "Memory Management Best Practices for Hermes Agent"
description: "Hermes Agent memory management: built-in MEMORY.md, one external memory provider (Honcho or others), GBrain-style indexes, session search, compaction strategies, anti-patterns."
category: best-practices
tags: [hermes-agent, memory-management, honcho, gbrain, memory-provider, context-optimization, persistent-memory, session-search]
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/best-practices/memory-management/"
robots: "index,follow"

---

# Memory Management Best Practices  --  Persistent AI Agent Context

Memory is what separates a stateless tool from a persistent AI assistant in Hermes Agent. But memory also consumes context, increases latency, and introduces staleness risks. These memory management best practices cover when and how to use each memory tier for optimal agent performance.

## Overview

Hermes Agent layers memory instead of storing one blob. Four tiers ship with the agent, and one external provider can be added on top of them:

- **Built-in memory** - MEMORY.md and USER.md, injected into every turn for free.
- **Session search** - past transcripts in a local SQLite FTS5 store, queried on demand.
- **One external memory provider** - Honcho, Mem0, Hindsight, Supermemory, OpenViking, Holographic, Memori, RetainDB or ByteRover, installed from the plugin catalog.
- **Skills** - procedural knowledge, versioned and loaded only when relevant.

Only **one** external provider can be active at a time, and the built-in memory always runs alongside it. `hermes memory status` shows what is active, `hermes memory setup` runs the interactive picker, and `hermes memory off` disables the external provider without touching MEMORY.md or USER.md.

Organizational indexes and retrieval services that live outside Hermes - an indexing layer such as GBrain, or a separate retrieval service - sit beside these tiers. They are companion systems, not Hermes memory providers, and they carry their own sync discipline.

## How It Works

### The Memory Hierarchy

| Tier | System | Use Case | Persistence |
|---|---|---|---|
| **Built-in** | MEMORY.md / USER.md | Stable facts, preferences, standing conventions | Every turn |
| **Peer / user model** | [Honcho](/hermes/knowledge) or another external provider | User identity, preferences, decisions, bans | Cross-session |
| **Organizational** | [GBrain](/hermes/knowledge) and similar indexes | File/code indexing, project relationships | Cross-session |
| **Conversation history** | `session_search` (SQLite FTS5) | What happened in past sessions | Cross-session |
| **Conversation** | In-session context | Task continuity within current chat | Ephemeral |
| **Procedural** | [Skills](/hermes/skills/creating-skills) | Reusable workflows, tool chains | Versioned |

## When to Add Memory

Ask these questions before storing:

- **Does this fact change rarely?** Stable preferences → memory. Current task focus → conversation context.
- **Is it referenced across sessions?** Multi-session project → memory. One-off question → don't store.
- **Does it save meaningful context tokens?** If storing saves re-explaining each session, it's worth it.
- **Is it factual or procedural?** Facts → memories. Workflows → [skills](/hermes/skills/creating-skills). Config → [env vars](/hermes/best-practices/security).

## Compaction Strategies

When context windows fill up:

- **Sliding window**: Keep last N messages verbatim; summarize older. Best for linear task-focused conversations.
- **Hierarchical summarization**: Summarize sections into bullet points; summarize summaries when chain gets long.
- **Selective retention**: Flag key decisions/code to "keep forever"; summarize everything else.
- **Semantic retrieval**: Index conversation turns by embedding; retrieve relevant chunks on demand.

## Memory Anti-Patterns

| Anti-Pattern | Why It Hurts | Fix |
|---|---|---|
| Memory as dumping ground | 500 stale entries = noise | Prune periodically |
| Contradictory memories | Confusion across sessions | Audit for conflicts |
| No expiration | "Working on Q2 report" stale in Q3 | Add implicit/project expiry |
| Memory replacing config | API keys in memory = breach | Use [secrets manager](/hermes/best-practices/security) |

## Benefits

- **No session amnesia**: Agents remember who you are, what you're building, and what happened last session
- **Reduced re-explanation**: Stable preferences stored once, referenced forever
- **Faster onboarding**: Team knowledge indexed and queryable via GBrain
- **Lower token costs**: Compacted context means less wasted context window

## FAQ

### What's the difference between Honcho and GBrain memory?
Honcho stores peer identity  --  who the user is, preferences, decisions, bans. GBrain indexes organizational knowledge  --  where files are, what code does what, project relationships. They solve different problems and should both be used in production.

### How do I prevent my Hermes Agent memory from getting stale?
Prune memories periodically (monthly review), add expiration to project-specific memories, audit for contradictions, and use the dream cycle (nightly consolidation) to merge duplicates and strengthen frequently accessed paths.

### Can I use just one memory system?
You can, but you'll have gaps. Hermes allows one external memory provider at a time, so pick the one that matches your dominant need rather than stacking several; built-in memory and session search always run underneath it. A peer-modeling provider such as [Honcho](/hermes/knowledge) does not index your files, and an indexing layer such as [GBrain](/hermes/knowledge) does not answer "who is the user?" - run one external provider for user modeling and a separate index for organizational knowledge.

## Related Pages

- [Memory Architecture Guide](/hermes/knowledge)  --  Full triple-stack documentation
- [Best Practices Overview](/hermes/best-practices)  --  All guides
- [Security](security.md)  --  Don't store credentials in memory
- [Skill Development](skill-development.md)  --  Procedural knowledge vs memory
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
