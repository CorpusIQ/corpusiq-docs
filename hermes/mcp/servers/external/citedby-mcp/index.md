---
title: "CitedBy MCP - Whether AI Assistants Can Find and Cite a Page"
description: "Four read-only tools over MCP: a page audit with the fix for each finding, AI crawler access for eight bots, llms.txt checks and Common Crawl backlinks."
category: Marketing / AI Visibility
stars: n/a (free, no account, read-only; whole-site audits on a plan)
added: 2026-10-26
source: "live keyless MCP session on citedby.eu + tools/list + four tool executions against corpusiq.io + mcpservers.org card"
relevance: ★★★
tags: [aeo, geo, ai-visibility, seo, llms-txt, robots-txt, ai-crawlers, structured-data, backlinks, common-crawl]
last_updated: "2026-10-26"
---

# CitedBy MCP

**The audit that asks the only question that matters now: when a person asks an assistant about your market, is your page readable and does it get cited.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://citedby.eu/mcp
Transport:   JSON-RPC 2.0 over HTTP
Auth:        none - every tool is free and read-only
Tools:       4
Built by:    CitedBy (citedby.eu)
Registry:    not listed in the official MCP registry
```

## Why This Matters for Operators

Search visibility was a ranking problem and is now a readability problem. An assistant answering a question reads a handful of pages, and it can only cite the ones it was allowed to fetch, could parse, and could attribute. A site that blocks GPTBot or ships a page whose structured data Google rejects is invisible in a way that never shows up as a traffic drop you can explain.

Most AEO tooling sells a score. This one returns a finding, the reason it matters, and the exact fix, and it refuses to score what it could not read.

## What It Actually Does

The endpoint answered without a key in this sweep. `initialize` returned HTTP 200 as `citedby` 1.0.0 on protocol 2025-06-18, and `tools/list` returned four tools in 2.9 KB of schema.

| Tool | What it returns |
|---|---|
| `check_page` | Fetches one page as `CitedBot` with robots.txt respected: score, findings, and for each finding the severity, the check name, why it matters and the fix. Deterministic checks only. |
| `check_ai_crawler_access` | For GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot: allowed by robots.txt, and answered by the server, or not. |
| `check_llms_txt` | Whether `/llms.txt` exists, whether its links resolve, whether `/llms-full.txt` exists. Drafts one from the site's own pages when there is none. |
| `backlinks` | How many domains link to a domain and the strongest referrers, from the Common Crawl domain web graph. |

All four were executed against `corpusiq.io` in this session, which makes the output concrete.

`check_ai_crawler_access` returned **8 of 8 crawlers can read the site**, dated `2026-10-26`, robots.txt okay, each line naming what that bot does: GPTBot for model training, OAI-SearchBot for citing you in answers, ChatGPT-User for opening a page when a person asks about it, PerplexityBot for citing you, ClaudeBot for training, Google-Extended for Gemini grounding, Bingbot and Googlebot for citing you.

`check_llms_txt` returned `present: true`, `status: 200`, **11,256 bytes, 10 links checked, 0 broken**, and `/llms-full.txt` answering 200.

`check_page` on `https://www.corpusiq.io/` returned **score 90/100 with 2 findings**, both real:

- `schema_rejected` (warning): `SoftwareApplication` is missing `offers.price`, one of `aggregateRating` or `review`. The response carries the consequence in plain words: the markup parses, but a type Google builds results from is failing its rich-result check, and schema is not a ranking lever, so a rejected block is an error in Search Console rather than a penalty. The suggested fix names the alternative: a subscription service is a `Service`, not a `Product`.
- `render_blocking` (notice): 0 scripts and 7 stylesheets block rendering.

`backlinks` on `corpusiq.io` returned `in_data: false` and said so plainly rather than reporting zero: the dataset covers domains with 100 or more referring domains under `.eu`, EU and UK country domains, 264,847 domains, plus the most-linked sites, from the Common Crawl graph `cc-main-2026-aug-sep-oct` read on 2026-10-23. A domain absent from that data says nothing about how many links it has, and the tool states that.

## What It Does Not Do

- No whole-site crawl on the free tier. One page per `check_page` call; every page with answer analysis needs a plan at citedby.eu/plans.
- `backlinks` is Common Crawl open data, so a US small business is usually outside the coverage window. It is a sanity check, not an Ahrefs replacement.
- Nothing is connected and nothing is written. It reads public pages.
- The page score is the sum of deterministic checks. It does not measure whether the writing answers a question, only whether the page is structurally citable.
- `check_page` respects robots.txt, so a site that blocks the crawler returns that fact instead of a score.

## FAQ

### Is a rejected schema block actually hurting us?
Not as a ranking signal. It hurts because a rich result you could have shown is being suppressed and reported as an error, which hides real breakage in a report you have to read anyway. Fix the missing property or change the type.

### Why does crawler access matter more than the score?
A blocked crawler means no citation at all, which the score cannot express. Eight of eight open is the only acceptable answer for a business site that wants to be quoted in AI answers.

### What is llms.txt good for here?
It is the page an assistant reads to know what your site contains and where the canonical pages live. A tool that checks the links and the `llms-full.txt` companion turns a hand-maintained file into something verifiable.

### Can this run on a schedule?
Each tool is a single request with a stable shape, so yes: crawler access and the page audit are cheap enough to check weekly and diff, which is how a robots.txt edit by someone else gets caught before the citations disappear.

## The Operator Test

Point `check_ai_crawler_access` at your own domain first. If any line reads "cannot read the site", every AEO effort is decoration until that is fixed. Then run `check_page` on the page that should win your money question and read the two findings.

Pairs with `creavores-aeo-mcp` and the AI visibility entries already in this catalog, and with the site-health entries, because a page that cannot be fetched cannot be cited.
