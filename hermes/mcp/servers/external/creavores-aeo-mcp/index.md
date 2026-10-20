---
title: "Creavores AEO Audit MCP - Page-Level AEO Scoring"
description: "Free npx MCP server that scores any URL for AI-search readiness: direct answer, JSON-LD, llms.txt, E-E-A-T, agentic browsing and citable passages."
category: SEO
stars: 0
added: 2026-10-20
source: "mcpservers.org /all page 3 via the r.jina.ai reader proxy (tresor4k/creavores-aeo-mcp)"
relevance: ★★
tags: [seo, aeo, geo, llms-txt, json-ld, eeat, agentic-browsing, ai-citation, mcp-server, nodejs]
---

# Creavores AEO Audit MCP

**A deterministic AEO score for one page, in one call, with no key and no account** - crawlability, structure for AI extraction and trust are scored out of 100, and each failing check comes back with the fix rather than the complaint.

```
Server type: Local stdio (Node), run straight from npx
Package: creavores-aeo-mcp 1.1.0 on npm (MIT, author Les Créavores, published 2026-07-10, last modified 2026-10-12)
Install: npx -y creavores-aeo-mcp
Repo: github.com/tresor4k/creavores-aeo-mcp
Auth: none. No API key, no environment variables, no configuration
Tools: 8 - audit_aeo, check_direct_answer, extract_structured_data, check_llms_txt, check_eeat_signals, check_agentic_readiness, simulate_ai_citation, compare_aeo
```

Verified live in this sweep: `initialize` returned serverInfo `creavores-aeo-mcp 1.1.0` on protocol 2025-06-18, and `tools/list` returned all eight tools with schemas.

## Why This Matters for Operators

Answer engines do not rank a page, they extract from it. The three things that decide whether they can - a page a crawler can read, a passage that makes sense on its own, and signals that say a named human is accountable for it - are the same three things a page audit can measure without waiting for a ranking to move.

The scoring is split in a way worth knowing before you read a number: crawlability 30 points, content structure for AI extraction 35, and E-E-A-T trust 35, plus separate checks for `llms.txt` and AI-bot access in robots.txt. That weighting is the vendor's opinion, stated plainly, and it is a reasonable one: a perfect passage behind a blocked crawler scores zero in practice.

The differentiator tool is `check_agentic_readiness`, which is aligned with Lighthouse's new Agentic Browsing audit category: heading hierarchy sanity, image alt-text coverage, ARIA landmarks, meta robots directives, and whether the named AI crawlers are blocked. That is the check that separates "a search crawler can index this" from "an agent can use this", and most AEO tools stop at the first.

## Tools & Capabilities

| Tool | Input | Returns |
|---|---|---|
| `audit_aeo` | `url` | score out of 100, verdict, the three sub-scores, llms.txt status, per-bot AI access, prioritized recommendations and an issue list |
| `check_direct_answer` | `url` | the 40 to 60 word passage under the H1, its word count, and a pass or fail verdict |
| `extract_structured_data` | `url` | every JSON-LD block, its `@type` list, parse errors, common schema.org mistakes, and whether the data ships server-side in the raw HTML |
| `check_llms_txt` | `domain` | existence, a 0 to 100 compliance score against llmstxt.org, the section headings and the extracted links |
| `check_eeat_signals` | `url` | byline, publish and modified dates, source citations, About and methodology links, legal and privacy links |
| `check_agentic_readiness` | `url` | llms.txt, heading structure, alt-text coverage, ARIA landmarks, meta robots, and AI-crawler access in robots.txt |
| `simulate_ai_citation` | `url` | the single passage most likely to be quoted, scored against paragraphs, list items, table rows and FAQ answers for self-containedness, with the reason it would or would not win |
| `compare_aeo` | 2 to 3 `url` values | the AEO scores side by side, for a page against a competitor's |

One live audit in this sweep, on a public marketing page, returned `score: 100`, `verdict: "excellent"`, sub-scores 30 of 30, 35 of 35 and 35 of 35, `issueCount: 0`, and seven AI crawlers checked (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended) with none blocked. A second call, `check_llms_txt`, returned `exists: true`, `httpStatus: 200`, `score: 100`, 13 sections and 37 links parsed. Both calls were fast enough to run in a loop.

## Installation

```bash
claude mcp add creavores-aeo -- npx -y creavores-aeo-mcp
```

```json
{
  "mcpServers": {
    "creavores-aeo": { "command": "npx", "args": ["-y", "creavores-aeo-mcp"] }
  }
}
```

No key, no account, no configuration. The server fetches pages directly with a self-identifying User-Agent (`creavores-aeo-mcp/1.0 (+https://lescreavores.fr)`) and a 15-second timeout, and the vendor states it never throws: every tool returns clean JSON, including an `{ "error": "..." }` object on failure, so it is safe to call inside an agent loop.

## Configuration

None. The only tunable is which URL you point it at, and whether you use the batch tool to compare two or three pages in one call.

If you care about the score's provenance: the logic is compatible with, and extends, the public `@macalc/aeo-score` npm package, and the vendor states the numbers match their free hosted audit tool at lescreavores.fr. That makes the score reproducible outside this server, which is more than most graders offer.

## Business Relevance

**Pre-publish gate.** Run `audit_aeo` on a draft before it ships, in the same loop that writes it. A failing direct answer, a missing FAQ schema and a client-side JSON-LD injection are all things that are cheap to fix on the draft and expensive to notice a month later.

**Competitor comparison in one call.** `compare_aeo` puts two or three pages side by side, which is the honest way to answer "why do they get cited and we do not" without a visibility subscription.

**Agency deliverables.** A weighted score with a prioritized fix list is a report a client accepts, and it costs nothing per run.

**The agentic-readiness check as a release gate.** If you publish anything an agent is expected to operate, the ARIA, heading and alt-text checks belong next to your accessibility tests.

## Integration with CorpusIQ

The catalog already carries AEO scoring in [Ranki](/hermes/mcp/servers/external/ranki-mcp) (22 tools, hosted, free tier at 5 calls per IP per day) and [Prognosite](/hermes/mcp/servers/external/prognosite-mcp) (SEO and AEO intelligence for publishers), so this entry is deliberately filed as an ★★ rather than a gap-closer. What it adds is packaging rather than a new category: MIT, local, no key, no rate limit, eight focused tools, and the agentic-browsing and citable-passage angles that the hosted graders do not expose separately.

That makes it the right pick when you want to run hundreds of checks in a loop - auditing a whole sitemap page by page, or gating every publish - and the wrong pick if you want one dashboard. For our own AEO work the useful pattern is: use this for the per-page deterministic check, and a visibility measurement tool for how engines actually answer.

## Limitations

- **One page at a time.** There is no site crawl, no sitemap walk and no queue; a whole-site audit is your loop to write.
- **Heuristics, not measurement.** A 100 does not mean an engine cites the page, and the `simulate_ai_citation` output is a self-containedness score, not a prediction from a model.
- **Public pages only.** No auth means anything behind a login is out of reach.
- **Field-of-one taste in the weights.** Crawlability 30, structure 35, trust 35 is a considered opinion, not a standard; treat a 90 that fails `check_direct_answer` as a real problem.
- **New and small.** Version 1.1.0, five releases since July 2026, a single maintainer agency, and no star history to speak of. The code is MIT and short enough to read.

## FAQ

### Does it replace an AI visibility tool?

No. Visibility tools measure how ChatGPT, Perplexity and AI Overviews answer and cite. This measures whether a page is built so that they can. You need the second one to fix the first.

### Why score 100 on some pages and 60 on others?

The three buckets are structural. A page with a clean H1, a direct-answer paragraph, server-rendered JSON-LD, an author and a date will score high even if the writing is poor; a well-written page with client-side schema and no author byline will not. Read the `issues` array, not just the total.

### What is agentic readiness and why is it separate?

It is the Lighthouse category for whether an agent can operate a page, not just index it: landmarks, labels, alt text, heading order, and whether AI crawlers are allowed in at all. A page can pass an SEO audit and fail this one.

### Is anything sent anywhere?

Each call fetches the URL you name, from your machine, with a User-Agent that identifies the tool. There is no vendor account and no telemetry endpoint in the install path.

### Can I run it against pages I do not own?

Yes, that is what `compare_aeo` is for. Be aware that the site sees the request and can see the identifying User-Agent.

## See Also

- [Ranki MCP - Free SEO and AEO Audits for AI Agents](/hermes/mcp/servers/external/ranki-mcp)
- [Prognosite MCP - SEO and AEO Intelligence for Publishers](/hermes/mcp/servers/external/prognosite-mcp)
- [New Term Radar MCP - New Names Before Keyword Tools](/hermes/mcp/servers/external/new-term-radar/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
