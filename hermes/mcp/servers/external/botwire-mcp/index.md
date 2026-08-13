---
title: "The Bot Wire MCP — Integration Guide"
description: "40 real-time primary-source data wires — SEC EDGAR, Federal Register, federal court opinions, congressional bills, SEC/FTC enforcement, FDA approvals"
category: mcp
tags: [mcp-server, regulatory-data, legal-intelligence, financial-data, economic-data, compliance, hermes-agent]
last_updated: 2026-07-31
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/botwire-mcp/"
robots: "index,follow"

---

# The Bot Wire MCP — Primary-Source Regulatory & Economic Intelligence

**Rating:** ★★★ | **Category:** Finance & Compliance | **Transport:** Streamable HTTP

## What It Does

The Bot Wire provides 40 real-time primary-source data wires covering SEC EDGAR filings, Federal Register rules, federal court opinions (Supreme Court, 2nd/9th/Federal Circuits), congressional bills, SEC/FTC enforcement actions, DOJ announcements, FDA approvals, Federal Reserve/FOMC statements, ECB policy releases, BLS/BEA economic releases, CISA CVEs, and cloud provider status. Unlike news aggregators, Bot Wire reads original documents directly — your AI agent answers questions about post-cutoff events with actual primary-source citations.

## Why Business Operators Need This

Compliance officers, financial analysts, competitive intelligence teams, and legal researchers spend hours manually monitoring regulatory sources. The Bot Wire automates this: your agent can answer "What did the Federal Reserve say about rates this week?" or "Are there new SEC filings from our top 3 competitors?" with original-source citations — no news summaries, no middle layers. For operators in regulated industries (fintech, healthcare, defense, energy), this is the difference between being informed and being blindsided. First MCP to read regulatory/legal/economic primary sources directly.

## Quick Start

```
# Install via npx (stdio transport)
npx botwire-mcp

# Remote endpoint (Streamable HTTP)
Endpoint: https://thebotwire.com/mcp
```

### Hermes Agent Configuration

```json
{
  "mcpServers": {
    "botwire": {
      "transport": "http",
      "url": "https://thebotwire.com/mcp"
    }
  }
}
```

### Claude Code

```bash
claude mcp add botwire https://thebotwire.com/mcp
```

### Environment Variables

```bash
export BOTWIRE_API_KEY="bw_..."
```

## Key Tools

The Bot Wire organizes its 40 data wires into categories:

| Category | Wires | What You Get |
|----------|-------|--------------|
| **SEC Filings** | EDGAR 10-K, 10-Q, 8-K, S-1, 13F, insider trades | Real-time SEC filing alerts with full text access |
| **Federal Register** | Rules, proposed rules, notices, presidential documents | New federal regulations as they're published |
| **Federal Courts** | Supreme Court, 2nd Circuit, 9th Circuit, Federal Circuit | Opinions and orders from key appellate courts |
| **Congress** | Bills, resolutions, committee reports | Legislative tracking with bill text |
| **Enforcement** | SEC enforcement, FTC actions, DOJ announcements | Regulatory enforcement monitoring |
| **Health** | FDA drug approvals, device clearances, recalls | Life sciences regulatory intelligence |
| **Monetary Policy** | Federal Reserve, FOMC statements, ECB | Central bank policy tracking |
| **Economic Data** | BLS employment, BEA GDP, CPI, PPI | Key economic indicator releases |
| **Cybersecurity** | CISA CVEs, vulnerability alerts | Critical infrastructure threat intelligence |
| **Infrastructure** | AWS, Azure, GCP status | Cloud provider health monitoring |

## Pricing

Free tier available with rate-limited access to all 40 wires. Paid tiers unlock higher frequency, historical data access, and priority polling. Check [thebotwire.com](https://thebotwire.com) for current plans.

## Authentication

API key-based authentication. Get your key at [thebotwire.com](https://thebotwire.com). The free tier includes a key with rate-limited access.

## Source

- **GitHub:** [github.com/ArasPasha/botwire-mcp](https://github.com/ArasPasha/botwire-mcp) (0★, created 2026-07-27)
- **Website:** [thebotwire.com](https://thebotwire.com)
- **MCP Endpoint:** `https://thebotwire.com/mcp`
- **npm:** `npx botwire-mcp`
- **Registry:** `io.github.ArasPasha/botwire-mcp`

## Verdict: ★★★ — Essential for Compliance & Regulatory Operators

The Bot Wire is the first MCP server that brings primary-source regulatory, legal, and economic data to AI agents. For any operator in regulated industries or anyone who needs to answer questions with original-source citations post-training-cutoff, this is a category-defining tool. The breadth — 40 wires spanning SEC to CISA to cloud status — makes it a single integration for regulatory awareness.

**Strengths:** 40 primary-source wires across regulatory/legal/economic/compliance domains, reads original documents directly (not news coverage), free tier, remote HTTP endpoint, simple setup.

**Limitations:** Brand new (0 stars, created July 27, 2026), free tier rate limits unknown, historical data depth unclear, wire polling frequency not documented.

**Best for:** Compliance officers, financial analysts, legal researchers, competitive intelligence teams, operators in regulated industries (fintech, healthcare, defense, energy).
