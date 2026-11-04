---
title: "Batch Tool Execution: Cutting MCP Round-Trip Latency"
description: "Why multi-source AI answers are slow, and a read-only batch_execute design that collapses sequential MCP tool round trips into one call."
category: "MCP"
tags: ["mcp", "batch tool execution", "agent latency", "read-only tools", "mcp tool design", "multi-source answers"]
last_updated: "2026-11-04"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/spec/batch-tool-execution-latency/"
robots: "index,follow"
---

# Batch Tool Execution - Cutting Round-Trip Latency in MCP Tool Loops

A question that spans several business systems is not one retrieval. It is a chain.

Search Console, then analytics, then orders, then payments. The model calls one tool, reads the result, reasons, then calls the next. Five sources means five sequential round trips and five separate reasoning passes. The wall clock is dominated by the waiting between decisions, not by the retrieval itself.

This page is the design note for a read-only batch tool that collapses that chain into a single call.

## The cost is in the gaps, not the queries

Each individual connector call is fast. The delay comes from what sits between them: the model has to finish one turn, parse the response, decide the next call, and start again. Multiply that by the number of sources in the question and the seconds add up in the part of the loop no connector can optimize.

Users do not experience this as "the database was slow." They experience it as the assistant hesitating before it answers.

## Proposal: one read-only batch tool

One new MCP tool, `batch_execute`, limited to reads:

```
batch_execute(calls: [{tool: string, arguments: object}], concurrency?: 1-4)
-> [{tool, ok, result | error, elapsed_ms}]
```

Server side, every entry is validated against the same allowlist the single-call path already uses, then run concurrently. Default concurrency is 2 with a cap of 4, a per-call timeout of 8 seconds, and a total wall clock cap of 10 seconds. All results come back in one response. A single failed call never fails the batch: that entry returns `ok=false` with its error and the rest still return.

## Five invariants

1. **Read-only allowlist.** Any tool classified as a connector configuration write, an auth change, or a mutation is rejected at validation with a typed error. The allowlist is the same source of truth as the single-call path, never a second list that can drift.
2. **No credentials in the payload.** Each call resolves its own connector context server side, exactly as it does today.
3. **Bounded.** Concurrency cap 4, total wall clock cap 10 seconds, maximum 8 calls per batch. Above 8 is rejected, not truncated, so a caller never silently loses work.
4. **Deterministic order.** Results are returned in request order regardless of completion order. Callers must be able to index into the response without matching on tool names.
5. **Feature flagged, absent by default.** With the flag off the tool is absent from the tool list, not present and failing. A bad batch can never degrade the normal single-call path.

## Out of scope

Writes of any kind, including connector configuration. Ordering, retry and compensation for mutations stay sequential. Parallel writes need a recovery model that does not exist yet, and putting configuration changes into a batch is the last thing that should be done, not the first.

## How it gets measured

The same question is run down both paths, with wall clock recorded server side:

- **sequential:** today's path, N single calls
- **batched:** one `batch_execute` with N entries

Success criteria are p50 and p95 latency improvement on questions spanning four or more sources, with zero change in answer content and zero increase in connector error rate.

## First slice

Read-only fan-out for the four highest-traffic read connectors only. Measure, confirm the error rate holds, then widen the allowlist. The narrow start is deliberate: it proves the invariant that matters, that batching changes latency and nothing else.

## FAQ

### Why are AI answers that span several business tools slow?

Because each tool call is a full turn: the model calls, waits, reads, reasons, then calls the next. The retrieval is fast; the gaps between decisions are not. Five sources means five of those gaps.

### Does batching change the answer?

It must not, and the measurement treats any content change as failure. The batch path returns the same results in request order, so the model reasons over an identical set, just sooner.

### Can batch execution write to a connected system?

No. Writes, auth changes and connector configuration changes are rejected at validation. Mutations need ordering, retry and compensation, which stay on the sequential path.

### What happens when one call in a batch fails?

That entry returns an error and the other calls still return. A batch never fails as a whole because one connector is unavailable, which is the same partial-failure behaviour a user already expects from a single call.

### Is the batch tool on by default?

No. It ships behind a flag and is absent from the tool list while the flag is off, so it cannot degrade the normal path if something goes wrong.
