---
title: "Sequel MCP - Google Search Console in Natural Language"
description: "Hosted MCP from Sequel: ask your Google Search Console data questions in plain English and join answers across GA4, Stripe, HubSpot, Ahrefs and 20+ sources; the Sequel CLI provisions a read-only OAuth connection into your agent."
category: Marketing
stars: "n/a (no public repo)"
added: 2026-08-30
source: mcpservers.org /all
relevance: ★★
tags: [mcp-server, seo, google-search-console, analytics, oauth, hosted, marketing, natural-language]
---

# Sequel MCP (Google Search Console)

**Hosted MCP from Sequel, the natural-language data platform (sequel.sh), for Google Search Console.** Instead of copying keys and hand-writing config, the Sequel CLI signs you in, provisions an org-scoped read-only Google OAuth connection, and writes the MCP config directly into your agent - supported install targets include Claude Code, Claude, Cursor, VS Code, Windsurf, Zed, Codex, OpenClaw, and **Hermes**. Your agent then answers SEO questions from Search Console data in plain English, with no SQL, no dashboards and no CSV exports.

```
Server type: Hosted MCP, provisioned by the Sequel CLI (no raw public endpoint)
Auth: Read-only Google OAuth, org-scoped API key issued by the CLI
Install: curl -fsSL https://sequel.sh/install | sh · sequel login · sequel install <agent>
Data: GSC Search Analytics API - clicks, impressions, CTR, average position by query, page, device, country, date
Limits: up to 25,000 rows per request, queries up to 16 months back, GSC data lag 2-4 days
Pricing: free to start (sequel.sh)
Built by: Sequel (sequel.sh)
```

```bash
curl -fsSL https://sequel.sh/install | sh
sequel login
sequel install hermes # also: claude-code, claude, cursor, vscode, windsurf, zed, codex, openclaw
```

## Why This Matters for Operators

Search Console is the only first-party source of truth for what search demand actually reaches your site, and it is chronically under-read because it is a pivot-table product. Sequel turns it into a conversation: an agent can ask "which pages lost the most impressions month-over-month", "show me queries ranking 8-15 with over 1,000 impressions", "what is average CTR by device", and get the answer with the pagination and date-range handling done for it.

The bigger unlock is **cross-source joins**. Connect GA4 alongside GSC and ask questions like "which pages have high GSC impressions but poor GA4 engagement" - the exact query a growth operator builds pivot tables to answer, now a single prompt. Sequel's source list extends far beyond SEO: PostgreSQL, MySQL, ClickHouse, BigQuery, Google Sheets, Stripe, Polar, PostHog, Mixpanel, Amplitude, HubSpot, Ahrefs, and Apollo.io are all connectable, so the same conversational layer can span marketing, revenue and CRM data.

## Example Prompts (from the vendor's docs)

- "What are my top 10 queries by clicks this month?"
- "Which pages lost the most impressions compared to last month?"
- "Show me queries ranking between position 8 and 15 with more than 1,000 impressions"
- "What's the average CTR by device type?"
- "Which countries send the most organic traffic?"

## Notes and Caveats

- **No raw public endpoint is published** - connection flows through the Sequel CLI, which provisions an org-scoped key into the agent's config; a tool-level list is not published on the source page. Treat the CLI as the source of truth for the current tool surface.
- OAuth is read-only for Search Console; Sequel queries GSC directly and shows what Google has (the standard 2-4 day data lag applies).
- The same platform ships an "MCP Server" source that lets Sequel query *other* MCP-compatible servers - that is a client-side integration and distinct from this server listing.
