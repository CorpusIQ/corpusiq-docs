---
title: HarborRank MCP - Live SEO Data for AI Agents
description: "HarborRank's SEO MCP server: keyword estimates, live SERPs, backlinks, rank tracking and read-only Search Console with no Google Cloud setup."
category: SEO
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + harborrank.com/features/mcp"
relevance: ★★★
tags: [seo, keyword-research, serp, search-console, backlinks, rank-tracking, competitor-analysis, remote-mcp]
---

# HarborRank MCP

**An SEO research surface your agent can drive, with first-party Search Console data and no Google Cloud project.** HarborRank is an authenticated remote MCP server that gives agents provider-backed keyword metrics, live SERP results, domain and backlink overviews, saved keyword opportunities, rank-tracking reads and read-only Search Console performance plus URL inspection from a connected hosted project. The server URL and per-client setup steps are maintained in the HarborRank docs at harborrank.com/features/mcp.

```
Server type: Remote (authenticated MCP client)
Auth: HarborRank account (Search Console reads via connected hosted project)
Endpoint: docs-managed (harborrank.com/features/mcp)
Tools: keyword research, SERPs, competitor, backlinks, rank tracker, GSC
Pricing: HarborRank plans; GSC tools are read-only and credit-free
Category: SEO
Built by: HarborRank (harborrank.com)
```

## Why This Matters for Operators

SEO decisions are usually made on screenshots and exports that an operator has to assemble by hand. HarborRank MCP removes the assembly step. The agent can run a first-pass keyword research sweep over seed topics, pull a competitor's domain overview and ranking keywords, and then check the live SERP before recommending a change, all inside the conversation.

The differentiator is Search Console access without the usual setup tax. Reading GSC performance and URL inspection data normally means a Google Cloud project and OAuth credentials. HarborRank reads those signals from a connected hosted project, read-only and without consuming credits, so page-two keywords worth pushing to page one can be found by asking.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Keyword research | Keyword ideas with volume, CPC, difficulty and intent by market |
| SERP results | Live Google organic results for a keyword |
| Save keywords | Store promising keywords and tags for review in the UI |
| Rank tracker | Read tracked positions and latest results per project |
| Domain overview | Summarize a domain's organic footprint |
| Domain keywords | List keywords a domain already ranks for |
| Backlinks overview | Backlink and referring-domain statistics |
| GSC performance | Read clicks, impressions, CTR and position from Search Console |
| URL inspection | Check index coverage, crawl, canonical, mobile and rich results |

## Installation

Connect the server URL from the HarborRank docs in any MCP client that supports authenticated remote servers:

```bash
claude mcp add --transport http harborrank <server-url-from-docs>
```

Claude desktop and claude.ai users add it under Settings > Connectors > Add custom connector. Codex setup and troubleshooting are documented on the same page.

## Configuration

```json
{
  "mcpServers": {
    "harborrank": {
      "type": "http",
      "url": "<server-url-from-harborrank-docs>"
    }
  }
}
```

Authentication happens against the HarborRank account; the Search Console tools read from a project connected inside HarborRank and require no Google Cloud OAuth.

## Business Relevance

- **SEO operators** get keyword, SERP and backlink research as conversation turns
- **Content teams** get striking-distance lists of page-two keywords worth a push
- **Agencies** can run competitor teardowns per client without switching tools
- **Founders without an SEO hire** get an agent-driven first pass over any topic

## Integration with CorpusIQ

HarborRank complements the CorpusIQ SEO connectors directly: Search Console clicks and impressions already flow through CorpusIQ's search_console connector, and HarborRank can take those queries further by pulling live SERPs and competitor backlink context for the same keywords. Ahrefs and Semrush connectors cover the deep historical view while HarborRank covers the agent-native workflow with saved keywords and GSC inspection in one place.

## Limitations

- Endpoint and setup live in vendor docs rather than a single published URL
- GSC access is read-only through the hosted project
- Keyword and SERP depth depends on the selected HarborRank plan
- New listing; the feature page is the primary documentation surface

## FAQ

### Where is the HarborRank MCP endpoint?

The server URL and per-client setup steps are maintained in the vendor docs at harborrank.com/features/mcp.

### Does Search Console access need Google Cloud setup?

No. GSC performance and URL inspection read from a connected hosted project, read-only and credit-free.

### What data does the agent see?

Keyword metrics, live SERPs, domain and backlink overviews, rank-tracking reads and Search Console signals.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
