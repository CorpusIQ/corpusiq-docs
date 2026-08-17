---
title: githunt-mcp Server
description: "Setup and usage guide for githunt-mcp Server. Part of the Hermes resource directory. URL: https://github.com/githunt-agent/githunt-mcp."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/githunt-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# githunt-mcp Server

**URL:** https://github.com/githunt-agent/githunt-mcp
**mcpservers.org:** https://mcpservers.org/servers/githunt-agent/githunt-mcp
**Category:** Recruiting / Developer Tools
**Priority:** LOW

## What It Does for Operators

Search, rank, and analyze GitHub developers for tech recruiting. Location/role/skill search over millions of ranked profiles with AI scoring and contact discovery. Install via `npx githunt-mcp` or use the hosted server at `https://mcp.githunt.ai/mcp`.

## Installation

```bash
npx githunt-mcp
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "githunt": {
      "command": "npx",
      "args": ["githunt-mcp"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `search_developers` | Search by location, role, skills |
| `rank_profiles` | AI-powered profile scoring |
| `discover_contact` | Contact information discovery |
| `analyze_contributions` | GitHub contribution analysis |

## Operator Use Cases

1. **Technical recruiting** — find developers by skill, location, and activity
2. **Competitive intelligence** — analyze competitor engineering teams
3. **Vendor assessment** — evaluate open-source contributors for partnerships
4. **Talent mapping** — identify skilled developers in target regions

## CorpusIQ Angle

Niche tool for tech recruiting. CorpusIQ operators who need to hire developers can use this as an AI-native alternative to LinkedIn Recruiter for GitHub talent.

## Limitations

- Focused on GitHub only (not LinkedIn/other platforms)
- Contact discovery varies by profile publicness
- Hosted option may have rate limits

---
**Discovered:** July 24, 2026 via awesome-mcp-servers PR #10795
**Repo:** githunt-agent/githunt-mcp
