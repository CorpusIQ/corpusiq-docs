---
title: "MentionFox MCP - Cited Reports and Mention Scans"
description: "Cited reports on people and companies, credential checks against official records, and daily brand mention scans with sentiment and buy-intent flags."
category: Research
stars: n/a (no public repo)
added: 2026-09-30
source: "mcpservers.org server page (mentionfox.com)"
relevance: ★★
tags: [research, brand-monitoring, people-search, credentials, reports, sentiment, due-diligence, remote-mcp]
---

# MentionFox MCP

**Cited reports, credential checks and mention scans inside your AI assistant.** MentionFox is a hosted MCP server that writes one-page briefs and long section-by-section reports on people, firms and publications from the public record, verifies claimed credentials against the official lists that would record them, and scans the last day of posts, comments, articles and videos for brand mentions with sentiment and a buy-ready flag. Every report ends with its sources and is fixed as of the day it was made.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in) or personal access key
Endpoint: https://mentionfox.com/mcp
Tools: 9
Pricing: credit-based, per-tool costs visible to the agent before it runs
Category: Research
Built by: mentionfox.com
```

## Why This Matters for Operators

Due diligence and brand monitoring both fail silently when they are done from memory. MentionFox ties every claim back to a source link: source_check answers verified, partly verified, could not verify, or contradicted by the record, with a link for each claim. A founder vetting a vendor, an agency checking a prospect, or an operator watching who talks about their brand gets evidence instead of vibes.

The mention scan closes the loop on social listening. It finds posts, comments and videos from the last day mentioning a brand, product, topic or person, with a link, sentiment and a flag for anyone who sounds ready to buy, so the research feed and the lead feed are the same tool.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| source_check | Verifies claimed credentials (doctor, lawyer, broker, director) against official records with a link per claim |
| enrich_person | Finds email, phone, current role and profile links for a named person |
| get_snapshot | One-page brief on a person, firm or publication, as text plus a shareable link |
| get_full_report | Long section-by-section report ending with its sources, dated |
| get_dossier | Everything on file about one person: history, associates, coverage, public statements |
| compare_people | Side-by-side table of two to five researched people, framed by purpose |
| scan_for_mentions | Daily brand, product, topic or person mentions with link, sentiment and buy-ready flag |
| export_report | Export to web page, print-ready PDF or plain text with your branding |
| get_my_recent_research | Lists prior research so nothing is looked up twice |

## Installation

```bash
claude mcp add --transport http mentionfox https://mentionfox.com/mcp
```

First connect opens a MentionFox sign-in page in the browser. For clients that cannot do browser sign-in, create a personal access key at mentionfox.com/dashboard/mcp-token and send it as a bearer Authorization header. Everything done through MCP is tied to your MentionFox account.

## Configuration

```json
{
  "mcpServers": {
    "mentionfox": {
      "url": "https://mentionfox.com/mcp"
    }
  }
}
```

ChatGPT connects the same URL through Developer mode connectors with OAuth, or through the Responses API with the personal access key. Cursor adds the entry to .cursor/mcp.json.

## Business Relevance

- **Founders and operators** vet vendors, partners and hires with credential checks instead of trusting a LinkedIn line
- **Agencies** produce branded, source-cited briefs and dossiers for clients
- **Growth teams** run daily brand mention scans that double as lead capture via the buy-ready flag
- **Sales and BD** enrich named contacts before first outreach

## Integration with CorpusIQ

MentionFox covers the outside view of people and brands; CorpusIQ covers the inside view of business performance. A composed workflow: a MentionFox dossier confirms who a prospect is and what they say publicly, then CorpusIQ answers their company's revenue, churn or ad spend from Stripe, HubSpot and GA4 connectors. The combined session turns vetting and enrichment into one evidence-first conversation.

## Limitations

- Hosted service with credit-based pricing; costs vary by tool and the agent sees them before running
- No public repository or open-source option
- Reports are fixed as of the day they were made; no live subscription updates
- Coverage quality depends on what official records are publicly queryable per jurisdiction

## FAQ

### How does source_check verify a credential?

It checks the claimed credential against the official lists that would record it and answers verified, partly verified, could not verify, or contradicted by the record, with a link for each claim.

### Does the mention scan catch everything?

It covers posts, comments, articles and videos from the last day. Anything older needs a fresh run; the tool is scoped to daily monitoring.

### Are my searches private?

Everything through MCP is tied to your own MentionFox account, same as the dashboard.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Deeplead MCP - Verified B2B Contacts for AI Agents](/hermes/mcp/servers/external/deeplead-mcp/)
- [iMario MCP - Synthetic Audience Research for Agents](/hermes/mcp/servers/external/imario-mcp/)
- [Family Office Registry MCP - Sourced Investor Data](/hermes/mcp/servers/external/family-office-registry-mcp/)
