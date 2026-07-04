---
title: Crustdata MCP Integration Guide
description: Full setup guide for Crustdata MCP — real-time B2B company and people intelligence with 15+ live data sources covering 1B+ people and 100M+ companies
---

# Crustdata MCP — Integration Guide

**Real-time B2B company and people intelligence for AI agents.** Crustdata connects to 15+ live data sources so you can search companies, find and enrich contacts, run job and social-post searches, and set up monitoring watchers across 1B+ people and 100M+ companies.

> **Source:** mcp.so · **Last seen:** July 4, 2026 Feed

## What It Does

Crustdata is a B2B intelligence layer for AI agents. Instead of manually searching LinkedIn, crunchbase, job boards, and company databases, your AI agent queries Crustdata over MCP and gets structured results from all sources simultaneously. Set up watchers that monitor target accounts and people for changes — new job posts, leadership moves, funding events, and social signals.

## Key Capabilities

- **Company Search** — Find and enrich company profiles with firmographics, funding, and news
- **People Search** — Find and enrich contact profiles with role, history, and social presence
- **Job Intelligence** — Search job postings, track hiring patterns, identify growth signals
- **Social Monitoring** — Track social posts and presence for companies and key people
- **Watchers** — Set up persistent monitors that alert on changes to target accounts/people
- **15+ Data Sources** — Aggregated from public and licensed B2B data providers

## Installation

```bash
# Contact Crustdata for access and API credentials
# Expected configuration (verify with official docs):
npx -y crustdata-mcp
```

## Hermes / Claude Desktop Configuration

```json
{
  "mcpServers": {
    "crustdata": {
      "command": "npx",
      "args": ["-y", "crustdata-mcp"],
      "env": {
        "CRUSTDATA_API_KEY": "your-api-key"
      }
    }
  }
}
```

## CorpusIQ Use Cases

### 1. Account Research
```
"Give me a full profile on Acme Corp: company size, funding, key executives, 
recent news, and current job openings."
```
Agent queries Crustdata across all sources and delivers a comprehensive company dossier.

### 2. Lead Enrichment
```
"Enrich these 20 company names with HQ location, employee count, industry, 
and the LinkedIn profiles of their CTO and VP of Engineering."
```
Batch enrichment for outbound prospecting — fills CRM gaps automatically.

### 3. Trigger-Based Outreach
```
"Set up watchers for these 10 target accounts. Alert me when any of them 
post new engineering job listings or have leadership changes."
```
Automated account monitoring replaces manual LinkedIn/alert tracking.

### 4. Competitive Intelligence
```
"Compare the hiring velocity and social presence of our top 3 competitors 
over the last quarter."
```
Cross-references job postings, social activity, and company updates for competitive analysis.

## Operator Value

| Use Case | Manual Effort | With Crustdata MCP |
|----------|--------------|-------------------|
| Single account research | 20-30 min (LinkedIn + Crunchbase + news) | 30 seconds (one prompt) |
| Batch lead enrichment (20 companies) | 2-3 hours of manual lookup | 2-3 minutes automated |
| Ongoing account monitoring | Hours/week checking alerts | Set once, agent monitors |

## Prerequisites

- Crustdata API key (contact Crustdata for access)
- MCP client (Claude Desktop, Cursor, Hermes)
- Internet access for live data queries

## Troubleshooting

| Issue | Fix |
|-------|-----|
| API key rejected | Verify key with Crustdata; check environment variable name |
| Rate limited | Crustdata may have tiered limits; check your plan |
| Slow enrichment | Batch queries in groups of 10-20 for optimal throughput |

## Data Coverage

- **Companies:** 100M+ globally
- **People:** 1B+ profiles
- **Jobs:** Real-time listings across major platforms
- **Social:** Company and executive social presence monitoring
- **Refresh:** Live data from 15+ continuously updated sources

## Related Resources

- [External MCP Server Catalog](/hermes/mcp/servers/external/) — full curated catalog
- [CorpusIQ MCP Connectors](/hermes/mcp/connectors/) — 37+ native business data connectors
- [ENTIA Entity Verification](/hermes/mcp/servers/external/#entia-entity-verification) — complementary business verification MCP

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Servers Home](/hermes/mcp/servers/) →*

*Guide created July 4, 2026. Crustdata is available via mcp.so. Check official channels for API access and pricing.*
