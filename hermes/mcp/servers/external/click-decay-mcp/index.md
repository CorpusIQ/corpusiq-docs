---
title: "Click Decay MCP - CTR Math That Refuses a Number"
description: "Driven live: a Search Console click drop split into impressions and CTR, the arithmetic re-checked by hand, and figures withheld in Google's anomaly window"
category: "SEO / Analytics"
stars: "0 (MIT, github.com/meelis545/clickdecay-mcp)"
added: 2026-11-12
source: "the submission queue entry #7237, the official registry record com.clickdecay/mcp-server 1.0.0 (published 2026-11-12T23:10:41Z), the vendor page clickdecay.com/mcp-server/ read the same day, and a live session on this host: keyless initialize, tools/list and eleven tools/call requests against https://clickdecay.com/mcp"
relevance: ★★★
tags: [seo, search-console, gsc, ctr, analytics, evidence-labels, keyless, data-integrity, mcp, remote]
last_updated: "2026-11-12"
---

# Click Decay MCP

**The most expensive sentence in a traffic report is "our CTR dropped", said by someone who never split the change into the part that came from impressions.** A site loses 1,000 clicks after a site migration and the room agrees on the cause: rankings fell, the snippets got worse, an algorithm update. The arithmetic that would settle it takes one line - clicks at the old CTR applied to the new impressions - and almost nobody runs it, because the person reporting is the person whose explanation depends on the answer. Click Decay is a free hosted server from a small Estonian research shop that runs that line for you and then labels what it just did: every number comes back as `observed`, `calculated`, `modelled` or `not_established`, and when Google's own Search Console notices cover the dates, the figures that depend on impressions come back **null with a reason** instead of a number.

```text
Server type:  remote Streamable HTTP, plain JSON responses, no session, keyless
Endpoint:     https://clickdecay.com/mcp
Server:       clickdecay 1.0.0 (serverInfo), protocol 2025-06-18, capabilities: tools only
Registry:     com.clickdecay/mcp-server 1.0.0, active, remote declared as the same URL
Licence:      MIT (github.com/meelis545/clickdecay-mcp, 0 stars at reading)
Vendor:       QQQ OÜ, reg. 10975665, Tallinn - ai@qqq.ee
Tools:        4, every one annotated readOnlyHint true, idempotentHint true,
              openWorldHint false
Limits:       ~60 requests a minute per connection; takes numbers, dates and a
              source name only - no queries, page URLs, site names or files
```

## The evidence tier

This one is fully driven. A keyless `initialize` answered **200** with no authentication challenge of any kind, no session header, and `capabilities` carrying `tools` and nothing else - no resources, no prompts, no sampling. Four tools came back from `tools/list`, and each carries a complete annotation block (`readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: false`), which is what lets a client decide without asking a human whether a call is safe.

`com.clickdecay/mcp-server` **1.0.0** answers in the official registry as active, published **2026-11-12T23:10:41Z**, with the remote declared as the same URL and the description *CTR change, click decomposition and known Search Console data anomalies for numbers you provide*.

The server's own `instructions` string states the contract before any tool is called: it *calculates CTR changes from Search Console totals that the user provides*, and *every number carries an evidence label*. That is the whole design, and it is the reason this entry exists.

## What the four tools do

```text
compare_ctr_periods            two equal-length, non-overlapping periods of
                               clicks and impressions -> CTR for each, the click
                               delta, and the split of that delta into an
                               impressions component and a CTR component
project_clicks_at_ctr          impressions x a CTR you choose (a what-if)
impressions_needed_for_clicks  clicks / a CTR you choose (sizing a target)
check_gsc_reporting_issues     the known Search Console notices overlapping
                               your dates, with Google's own source link
```

## The calls that were driven

Eleven calls against the endpoint. The comparison below used **illustrative** totals, not any site's data: a prior period of 3,000 clicks from 100,000 impressions and a current period of 3,150 clicks from 125,000 impressions, 28 days each and non-overlapping.

```text
priorCtr                       0.03      observed
currentCtr                     0.0252    observed
clickDelta                     +150      observed      (the business already knew this)
impressionDelta                +25,000   observed
ctrChangePp                    -0.48     observed      percentage points
relativeCtrChangePercent       -16.0     observed
clicksAtPriorCtr               3,750     modelled      what 125,000 impressions earn at 3%
gapToPriorCtrScenario          -600      modelled      clicks given up to the CTR change
impressionsComponent           +750      calculated    clicks gained from more impressions
ctrComponent                   -600      calculated    clicks lost to the CTR change
warnings                       ["NO_AI_CAUSATION"]
versions                       server 1.0.0, engine 0.1.0, contract 0.2.0,
                               anomalyRegistry 2026-10-12
```

**The control is the point: the decomposition was re-done by hand and matched.** 125,000 impressions at the prior CTR of 3 percent is 3,750 clicks; 3,750 minus the observed 3,000 is the **+750** the server calls the impressions component; 3,150 minus 3,750 is the **-600** CTR component; and the two add back to the observed **+150**. A reporting tool that gets this wrong is worse than no tool, and this one is reproducible to the click on the arithmetic it declares `calculated`.

The two what-if tools answered the same way, and both said what they are: `project_clicks_at_ctr` with 125,000 impressions at 2.52 percent returned **3,150** labelled `modelled`; `impressions_needed_for_clicks` for 4,000 clicks at 2.5 percent returned **160,000**, also `modelled`.

## The behaviour that earns the guide

Google published an impressions-logging anomaly running **2025-05-13 to 2026-04-27** that makes CTR reading unreliable for any site in that span. Ask Click Decay for a comparison that touches it and the answer changes shape rather than changing tone:

```text
periods      2026-02-01..02-28  vs  2026-03-02..03-29  (28 days each)
priorCtr, currentCtr, impressionDelta, ctrChangePp,
relativeCtrChangePercent, clicksAtPriorCtr,
gapToPriorCtrScenario, impressionsComponent, ctrComponent
              value null, nullReason "GSC_REPORTING_ANOMALY"   (each one)
clickDelta    +200    observed   <- clicks are still compared
anomalies     [{ id: GSC_IMPRESSIONS_ANOMALY_2025_2026, ... }]
```

Every figure that depends on impressions is **withheld with a reason code**, the anomaly is named in the response, and the one thing that can still be trusted - the click count - is still returned. Run the same call on dates after the anomaly and the numbers come back. That is a calculator that will not produce a number it cannot stand behind, which is a different thing from a calculator that produces a number with a disclaimer underneath.

`check_gsc_reporting_issues` with no arguments returns the registry the server is working from, **two** records at reading: `GSC_IMPRESSIONS_ANOMALY_2025_2026` (affects impressions, ctr and position; applies to all; effect `block_ctr_diagnostics`) and `GSC_BULK_EXPORT_MISSING_DAYS_2026` (2026-02-28 to 2026-03-01; affects rows; applies to bulk export; effect `warn`). Both carry `sourceUrl` `https://support.google.com/webmasters/answer/6211453` - Google's own notice - rather than a vendor claim.

## The refusals, and one defect

Three bad inputs were tried and all three were refused with a machine-readable code and `isError: true`:

```text
28 days vs 14 days        {"errors": [{"code": "PERIOD_LENGTH_MISMATCH", "field": "periods"}]}
periods that overlap      {"errors": [{"code": "PERIOD_OVERLAP", "field": "periods"}]}
300,000 clicks on 100,000 impressions
                          {"errors": [{"code": "CLICKS_GT_IMPRESSIONS", "field": "prior.clicks"}]}
```

**The defect, measured and recorded:** those refusals arrive as HTTP **200** with `structuredContent.errors` and **no `content` block at all**. A client that renders only `content` - which is most of them - shows the operator an empty answer rather than "the two periods must be the same length". The same shape appears in the null path: `ctrPercent: 0` on `impressions_needed_for_clicks` returned `{"value": null, "nullReason": "ZERO_RATE"}` with `isError` **absent**, so a null is not an error, it is a value with a reason attached - correct in the data model, easy to drop in a chat window.

A second, smaller artifact: two observed figures come back unrounded, `ctrChangePp` as **-0.47999999999999987** and `relativeCtrChangePercent` as **-15.999999999999993**. A formatter in the client hides it; nothing in the response does.

## What it does not do

No Search Console connection, no OAuth, no file upload, and no reading of your property - the totals are typed or pasted, which is either a limitation or the entire point, depending on whether you are willing to hand a third party a Search Console scope to get arithmetic. The vendor states the tool takes numbers, dates and the name of the data source only, calculates in memory, stores nothing, and publishes a roughly 60 requests a minute limit per connection. It also does not explain *why* clicks or CTR moved, and every comparison says so in the `NO_AI_CAUSATION` warning rather than leaving the reader to assume the assistant concluded something.

## How to connect

```text
Claude Code     claude mcp add --transport http clickdecay https://clickdecay.com/mcp
Claude web/app  Settings -> Connectors -> add a custom connector named Click Decay,
                address https://clickdecay.com/mcp, no authentication
ChatGPT         developer mode in the advanced connector settings, then a connector
                with the same address and no authentication
Cursor          {"mcpServers": {"clickdecay": {"url": "https://clickdecay.com/mcp"}}} in .cursor/mcp.json
VS Code         {"servers": {"clickdecay": {"type": "http", "url": "https://clickdecay.com/mcp"}}} in .vscode/mcp.json
```

If you run several data surfaces in one assistant, the practical order is: read the totals from your Search Console connector, hand the two period totals to Click Decay, and keep its labelled answer beside the reader's raw rows. The decomposition is arithmetic on published numbers, so the labelled calculation is the part you can quote to someone who will check it.

## Where it sits in this catalog

The SEO slice here is well covered by **readers and connectors** - [Google Search Console (ni-c)](/hermes/mcp/servers/external/google-search-console-ni-c-mcp), [Otto MCP](/hermes/mcp/servers/external/otto-mcp), [AgentGrown MCP](/hermes/mcp/servers/external/agentgrown-mcp), Metrinel, GSCPAP, Sequel, SEOmatic, Sorank, HyperGSC and SearchDock all get the numbers out of a property. Click Decay does not read a property at all: it takes the totals and adjudicates the arithmetic, keeps the observed apart from the modelled, and withholds what a Google notice makes untrustworthy. That refusal is the reason it is catalogued and the readers are not duplicated.

### What does the evidence label on each number actually mean?

`observed` is arithmetic on the numbers you supplied. `calculated` is an exact decomposition of the change - the impressions component and the CTR component add back to the observed click delta. `modelled` depends on an assumption you or the tool chose, such as a target CTR. `not_established`, and the `nullReason` codes beside a null, mean the server declined to produce a figure and said why.

### What happens when a known Search Console issue covers the dates?

Every impressions-dependent figure comes back null with `nullReason: "GSC_REPORTING_ANOMALY"`, the issue is listed in `anomalies` with Google's source link, and the click comparison is still returned. The tool does not quietly compute a CTR it knows Google's own data makes unreliable.

### Does it need Search Console access or an API key?

No. There is no account, no key, no OAuth and no file input. You supply totals and dates; the server computes in memory and stores nothing. That also means it cannot verify the numbers you give it - the labels describe the arithmetic, not the provenance of the inputs.

### What are the limits worth knowing before you rely on it?

Roughly 60 requests a minute per connection, four tools, no per-query, per-page or per-property analysis, and refusals that arrive without a human sentence - a client that shows only `content` will look empty on a bad input. Two observed figures come back unrounded, so format them in the client.
