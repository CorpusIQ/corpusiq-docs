---
title: "AEO Engine MCP - How AI Engines Describe a Site"
description: "A keyless AI visibility report per engine with share of voice, competitor evidence, the measured questions and a shareable report URL."
category: Marketing / AI Visibility
stars: ★★★ (free, keyless, two tools)
added: 2026-10-28
source: "live JSON-RPC probes on https://aeoengine.ai/mcp answering initialize as aeo-engine-aeo-report 2.0.0 on protocol 2025-03-26 and tools/list returning run_aeo_report and get_aeo_report_status with their full input schemas, plus the mcp.so feed card filed 2026-10-28 and the vendor page aeoengine.ai"
relevance: ★★★
tags: [aeo, geo, ai-visibility, share-of-voice, competitor-analysis, chatgpt, perplexity, keyless, streamable-http]
last_updated: "2026-10-28"
---

# AEO Engine MCP

**A company can now be summarised wrongly by four assistants at once and never find out, because the wrong answer is delivered to someone else and nobody forwards it back.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://aeoengine.ai/mcp
Auth:        none, keyless
Tools:       2 (run_aeo_report, get_aeo_report_status)
Engines:     ChatGPT, Perplexity, Claude (public profile)
Input:       domain plus a real work email, MX validated
Output:      emailed report plus a shareable report URL
Cost:        free on the public path
```

## Why This Matters for Operators

Search visibility had a referee: the results page. Assistant visibility does not. Each engine answers differently, cites differently and changes without notice, and the only way to know what it says about a business is to ask it the same question repeatedly and record the answer.

This server does that measurement as a job. `run_aeo_report` takes a domain and an email, runs the engine cohort, and returns a report that breaks the result down per engine with provenance, plus competitor gaps, coverage, methodology, the exact questions that were measured, competitor evidence and a named share of voice. The finished report is emailed to the address supplied and a shareable URL comes back.

The `markdown_summary` field is the part that matters for an assistant workflow: it is written to be read out to a person, so the agent does not have to invent the narrative from a JSON tree.

## What It Returns, Verified

Driven end to end without a key. `initialize` on `https://aeoengine.ai/mcp` returned HTTP 200 as `aeo-engine-aeo-report` 2.0.0 on protocol `2025-03-26`, advertising the tools capability. `tools/list` returned exactly two tools.

`run_aeo_report` requires `domain` and `email`. The schema is unusually explicit for a free surface:

- `email` is the user's real work address, MX validated, with disposable domains rejected, because the report is sent there
- `wait_seconds` waits inline up to about 50 seconds; the run itself can take up to roughly ten minutes, so a client that cannot wait polls
- `customQuestions` takes 5 to 20 exact questions and preserves their text and order verbatim, which is how the same prompt set gets compared month over month
- `competitor` pins one domain on the public path, while `competitors` accepts up to five only with an agency key
- `context` accepts a vertical hint, a city and region, and up to eight focus terms
- `report_profile` selects the engine cohort, `public` or `aio`
- `fresh` forces a new run instead of a cached report
- `idempotency_key` is 16 to 128 printable characters and is required for a trusted create, so a retried call maps to one job

`get_aeo_report_status` polls a submitted job once. The status vocabulary is honest about the middle: `queued`, `preparing`, `needs_review` and `running` mean keep polling, while `complete`, `partial` and `failed` are terminal, and `state` carries the phase and the reason. On completion it returns the structured report, the `report_url` and the `markdown_summary`.

Two schema details are worth more than a feature list. The company field is off limits in the prompt guidance, which reads as a deliberate guard against an agent inventing an entity. And an unusable `context` value is rejected with a reason, 422 on the public path or 400 with an agency key, rather than being silently dropped.

## Limits Worth Recording

- **It measures, it does not fix.** The output names coverage gaps and prioritised fixes; nobody edits the site for you.
- **One competitor on the free path.** Five-way comparison requires an agency key.
- **The email is the price.** There is no anonymous path to a report, and the report arrives in that mailbox. An agent should not fill it with its own address; the instruction is explicit about the user's real one.
- **Cached by default.** A repeated call may return a cached report unless `fresh` is set, so a month-over-month comparison has to force the run.
- **Partial is a real outcome.** A `partial` report means some engines answered and others did not. Reading it as a complete picture is the mistake the status field exists to prevent.
- **No published pricing for the agency path.** The public report is free; anything beyond one competitor, custom questions at scale or more frequent runs goes through an agency key whose terms are not on the server.

## Wiring It Up

```json
{
  "mcpServers": {
    "aeo-engine": {
      "url": "https://aeoengine.ai/mcp"
    }
  }
}
```

Ask for a report on your own domain, give a real address, and poll with the returned job id if the client timeout is under a minute. For a repeatable baseline, send the same `customQuestions` set every month with `fresh: true` so the questions and the order never drift.

## FAQ

### Does it need an API key?

No. Both tools answer on a keyless connection. The report is gated by an email address rather than a credential.

### Which engines does it measure?

The public profile covers ChatGPT, Perplexity and Claude. The `report_profile` parameter selects the cohort, and the report breaks results down per engine with provenance.

### How long does a report take?

Up to about ten minutes. `wait_seconds` can hold the call inline for about 50 seconds, after which the job id has to be polled with `get_aeo_report_status`.

### Can I compare more than one competitor?

One on the public path. Up to five are accepted with an agency key, and the public report pins exactly one.
