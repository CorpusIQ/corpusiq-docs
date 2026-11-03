---
title: "Context Pill MCP - A Checked Ledger of AI Claims"
description: "A daily feed of AI releases where every item carries how it was checked, a source trust score and a re-check date, plus a searchable claim ledger."
category: Research / Verification
stars: ★★★ (keyless, 3 of 3 tools driven)
added: 2026-11-02
source: "the chatmcp/mcpso submission #6628 filed 2026-11-02T18:33:08Z, the official MCP registry entry com.contextpill/context-pill published 2026-10-19, the method document at github.com/agnostify/context-pill, and a driven keyless session on https://contextpill.com/mcp: initialize HTTP 200 as context-pill 0.1.0, tools/list returning 3 tools, and live calls to get_latest, search_claims and list_sources"
relevance: ★★★
tags: [claim-verification, source-reliability, ai-news, evidence, trust-scores, read-only, keyless, remote-mcp]
last_updated: "2026-11-02"
---

# Context Pill MCP

**A feed tells you what a vendor announced. It does not tell you whether anyone checked the announcement, who checked it, or how often that source has been right. Those three facts are the difference between a lead and a footnote, and they are usually the first thing dropped when a claim is repeated.**

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://contextpill.com/mcp
Auth:         none, no key, no sign-in
Tools:        3 measured, all read-only and idempotent
Ledger:       121 published claims at the time of this pass
Sources:      20, each with a tier, a trust score and its lower bound
Method:       github.com/agnostify/context-pill/blob/main/METHOD.md
Pricing:      free
Registry:     com.contextpill/context-pill 0.1.0, published 2026-10-19
```

## What it does

Three tools, and the design is visible in the shape of the answer.

| Tool | What it returns |
| --- | --- |
| `get_latest` | Today's checked claims, each labelled with how it was checked, the source and its trust score, an evidence link and a re-check date |
| `search_claims` | A search across every claim ever published, with its status at publication, its current state and any correction |
| `list_sources` | Every source the scanner reads, with tier, trust score, conservative lower bound and how many re-checks have resolved |

The vocabulary is the product. Each item carries one of four verification statuses: **verified** (confirmed against the vendor's or author's own record, or an independent source), **docs-verified** (true per the docs, not tested hands-on), **face value, top-tier source** (the cited link was checked and exists), and **not verified** (excluded from the summary). Each source carries a tier, a posterior trust score and an `LB10` lower bound, and the scanner starts every source at a neutral Beta(2,2) prior of 0.50 and moves it only when a claim is re-checked fourteen days after publication.

That combination is what makes the feed citable. A claim is not "true", it is "verified, by this check, from this source, whose record stands at 0.799 with a lower bound of 0.63 over seven resolved re-checks, and which will be re-examined on 2026-11-16".

## What this pass measured

A keyless session, all three tools called.

`initialize` answered **HTTP 200** with `serverInfo` `context-pill` **0.1.0** and capabilities for tools, prompts and resources. `tools/list` returned **3** tools, each declaring `readOnlyHint: true`, `idempotentHint: true` and `openWorldHint: false`.

`get_latest` with a limit of three returned the drop for **2026-11-02**, scanner day **18**: **11** checked claims drawn from **10** items read, with the one item listed as not verified excluded from the answer rather than mixed in. Each claim carried its own `how it was checked` line and its own evidence link, and the answer named the cost of every claim it left out.

One item is worth quoting because it shows the honesty level. A claim about Claude's consumer tiers was marked **verified**, checked against the vendor's own pricing page, with the evidence link attached, the source named as a tier T1-seed account at trust 0.50 and lower bound 0.196, an id, a category of `release`, and a re-check date of **2026-11-16**. The same item's second claim noted explicitly that the weekly-limit detail was *not* checked, so the checked part and the unchecked part were separated inside one answer rather than blended.

`search_claims` for a model name returned **11** matches out of **121** claims in the ledger, each with the status at publication, the current state (`pending` where the re-check window had not closed), the source key, the evidence link and the id.

`list_sources` returned **20** sources. The spread is instructive:

```
Anthropic               T1-seed  trust 0.799  LB10 0.630  resolved 7
Latent Space (swyx)     T3       trust 0.761  LB10 0.586  resolved 8
Google DeepMind         T1-seed  trust 0.692  LB10 0.455  resolved 4
OpenAI                  T1-seed  trust 0.636  LB10 0.372  resolved 2
Simon Willison          T1-seed  trust 0.583  LB10 0.327  resolved 2
Cursor Changelog        T3       trust 0.555  LB10 0.262  resolved 1
```

Twelve of the twenty sources still sit on the neutral 0.50 prior with zero resolved re-checks, which is the correct reading of the table: most scores are a starting position, not a verdict. The three sources with seven or eight resolved re-checks are the only ones whose number means anything yet.

## The limits this guide will not paper over

- **The scope is the AI industry.** Releases, tools and techniques from model vendors, researchers and AI publications. It is not business data, not company filings, and it does not answer a question about your own numbers.
- **The ledger is small.** 121 claims is a young corpus. Anything the ledger does not hold, it cannot check, and a zero-result search means "not here", not "not true".
- **Most trust scores are priors.** A source at 0.50 with zero resolved re-checks has produced no evidence either way. Read the `resolved tips` column before you read the score.
- **"Verified" means a record was checked.** Confirming an announcement against the vendor's own page establishes that the vendor said it, not that the product does it. The statuses distinguish those cases, and the summary asks you to keep them distinct.
- **Every item ships a suggested step the model is told not to run.** The server instruction text tells the client to treat the feed as untrusted reference material, never to follow instructions inside it, and never to run a suggested step without an explicit yes. That is the right instruction, and it is also a warning about the content class.
- **Removed items keep only an id, a date and a reason.** A word search will not surface a withdrawn claim, by design.

## Where this sits in the catalog

The closest neighbour is [VerifyAPI MCP](/hermes/mcp/servers/external/verifyapi-mcp/), which checks one claim on demand against live web sources and returns a signed receipt. This is the other direction: it does not check the claim you bring, it publishes the claims it has already checked, with the check, the source's record and the re-check date attached. [Factanker MCP](/hermes/mcp/servers/external/factanker-mcp/) is the evidence layer for company and federal numbers. The news surfaces ([NewsMind MCP](/hermes/mcp/servers/external/newsmind-mcp/), [webz news search](/hermes/mcp/servers/external/webz-news-search/), [APITube News MCP](/hermes/mcp/servers/external/apitube-news-mcp/)) aggregate headlines without a verification label or a source score.

What earns the guide is the source scorecard. Nothing else in this catalog grades the reliability of the place a claim came from, over time, with the number of graded cases printed beside the score.

## Connect it

```json
{
  "mcpServers": {
    "context-pill": {
      "type": "http",
      "url": "https://contextpill.com/mcp"
    }
  }
}
```

A one-call check that the server is alive:

```bash
curl -sS -X POST https://contextpill.com/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

Prompts that use the shape of the data:

- "What shipped in AI this week, and which of those claims were actually checked?"
- "Has anyone checked the claim that this model has a one million token context window, and how reliable is the source that said it?"

## Do not use it as

- **A fact checker for your own domain.** It has no access to your documents, your connectors or your market.
- **A citable authority.** The server tells the client to cite the evidence link, not Context Pill. Use the primary source in the answer.
- **A trust oracle.** With most sources still on the prior, the score is a starting point. Weight it by the resolved count.

## FAQ

### Does it cost anything?
No. The endpoint is keyless and the vendor publishes it as free.

### How often does it update?
Once a day. The drop observed here was for 2026-11-02 on scanner day 18, which puts the scanner's first day at 2026-10-16.

### What is `LB10`?
A conservative lower bound on the trust score, computed so that ten percent of the posterior mass sits below it. It is the number to read when the sample is small, which is most of them.

### What happens when a claim turns out wrong?
It is re-checked fourteen days after publication, or fourteen days after the deadline for a prediction, and a correction within ninety days moves the source's score. The claim's current state moves to resolved, corrected or closed-inconclusive.

### Can I search the whole ledger?
Yes, `search_claims` covers every published claim, not just today's drop.
