# Memory Management in Hermes

Memory is what separates a stateless tool from a persistent assistant. But memory also consumes context, increases latency, and introduces staleness risks. This guide covers when and how to use each memory mechanism.

## The Memory Hierarchy

Hermes provides three persistence tiers. Each has different characteristics:

**Conversation context** is ephemeral — it lives within a single session and disappears when the session ends. Use it for task continuity: "remember that I asked about quarterly reports earlier in this chat."

**Memories** are persistent, cross-session facts about the user. They survive restarts and sessions. Use them for stable user preferences, project contexts, and recurring workflows. "The user prefers PostgreSQL syntax in SQL examples" is a memory.

**Skills, plugins, and crons** are persistent procedural knowledge. They encode how to do things — the steps, tool chains, and validation rules for repeatable tasks. They are the "muscle memory" of your Hermes setup.

## When to Add Memory

Not everything belongs in memory. Ask yourself:

**Does this fact change rarely?** If it changes every session, storing it as memory creates staleness. The user's preferred programming language (stable) belongs in memory. Their current task focus (changes hourly) belongs in conversation context.

**Is it referenced across sessions?** A one-off question doesn't need persistent memory. "Remember I'm working on the authentication module" (multi-session project) goes in memory. "Help me debug this one function" does not.

**Does it save meaningful context tokens?** If storing a fact as memory saves you from re-explaining it each session, it's worth the memory write. If the explanation is shorter than the memory reference, keep it in conversation.

**Is it factual or procedural?** Factual knowledge (preferences, configurations, project state) belongs in memories. Procedural knowledge (workflows, tool sequences, validation rules) belongs in skills.

## Compaction Strategies

Context windows fill up. When they do, you need compaction — summarizing older conversation into denser representations.

**Sliding window.** Keep the last N messages verbatim; summarize everything older. Simple and predictable. Works well for conversations with clear temporal locality.

**Hierarchical summarization.** Summarize sections into bullet points; summarize summaries when the chain gets too long. Good for very long conversations with distinct topic segments.

**Selective retention.** Flag certain messages as "keep forever" (key decisions, generated code, user preferences). Summarize everything else. Requires discipline about what to flag.

**Semantic retrieval.** Instead of keeping a linear history, index conversation turns by embedding and retrieve relevant chunks when needed. More complex to implement but handles very long histories better.

Choose compaction strategy based on conversation patterns. If conversations are linear and task-focused, sliding window works. If they meander across many topics, semantic retrieval is worth the complexity.

## Context Window Optimization

Every token counts against your model's context limit:

**Strip irrelevant tool output.** When a tool returns 2,000 lines of JSON and you need 3 fields, extract what you need and discard the rest before the next model call.

**Compress before expensive calls.** If you're about to invoke a frontier model with a large context, compress the conversation history first. Summarize earlier turns. Drop completed subtask threads.

**Use structured formats economically.** JSON and XML add framing overhead. When context is tight, prefer compact formats or strip unnecessary whitespace.

**Batch tool calls.** Making 5 sequential tool calls with full conversation history between each burns context. Batch independent calls into a single turn.

## What Goes Where: A Decision Guide

| Information Type | Storage | Rationale |
|-----------------|---------|-----------|
| User's timezone, language, name | Memory | Stable, cross-session, saves tokens |
| Current project context | Memory | Multi-session, saves re-explanation |
| Preferred output format | Memory | Stable preference |
| Debugging session state | Conversation | Ephemeral, task-specific |
| Generated code | Conversation or file | Depends on permanence need |
| Recurring workflow steps | Skill | Procedural, versioned, shareable |
| Scheduled task configuration | Cron | Scheduled, idempotent |
| Tool connection credentials | Plugin config | Security isolation |
| Team conventions | Memory (shared) | Cross-user consistency |
| Ad-hoc "remember this for later" | Memory (ephemeral flag) | Single-session carryover |

## Memory Anti-Patterns

**Memory as a dumping ground.** Don't store everything that happens. Prune stale memories periodically. A memory system with 500 entries is just noise.

**Contradictory memories.** "User prefers TypeScript" and "User's primary language is Python" stored in different sessions create confusion. Audit memories for contradictions.

**Memory without expiration.** Not every memory should live forever. "Working on Q2 report" is stale in Q3. Add implicit or explicit expiration to project-specific memories.

**Memory that replaces documentation.** "Remember to use this specific API key" is not memory — it's configuration that belongs in environment variables or a secrets manager.

## Memory Lifecycle

1. **Capture.** During or after a session, flag facts worth persisting.
2. **Validate.** Is this fact accurate? Will it still be true next week?
3. **Store.** Write to the appropriate memory tier with a clear key.
4. **Retrieve.** At session start, load relevant memories into context.
5. **Update.** When facts change, update memories — don't create duplicates.
6. **Prune.** Periodically review and remove stale memories.

A memory system is a garden, not a junkyard. Tend it.
