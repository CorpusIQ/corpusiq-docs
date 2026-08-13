---
title: "Lawstronaut MCP — Integration Guide"
description: "Legal research infrastructure for AI agents — 50M+ laws and court cases from 155+ jurisdictions via MCP. Structured legal data, continuously updated."
category: mcp
tags: [mcp-server, legal-research, compliance, regulatory, legal-data, governance, hermes-agent]
last_updated: 2026-08-10
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/lawstronaut-mcp/"
robots: "index,follow"

---

# Lawstronaut MCP — Legal Research for AI Agents

**Rating:** ★★★ | **Category:** Legal & Compliance | **Transport:** Streamable HTTP

## What It Does

Lawstronaut is the infrastructure layer that connects AI agents to millions of legal documents across 155+ jurisdictions — laws, regulations, court cases, guidance, and official sources. Structured legal data, continuously updated, accessible via MCP. Paid subscription required; OAuth 2.0 and Bearer token authentication supported.

## Why Business Operators Need This

For operators in regulated industries, compliance isn't optional — it's existential. Lawstronaut makes legal research an agent-native capability: your AI can answer "What are the current data residency requirements for SaaS in Germany?" or "Has there been any new FTC enforcement action in our category?" with citations to actual laws and cases. Unlike general web search, Lawstronaut returns structured legal data from official sources — not summaries, not blog posts, not hallucinated statutes. The 155+ jurisdiction coverage means this scales internationally.

**Competitive landscape:** The Bot Wire MCP (catalogued Jul 31) covers regulatory/economic primary sources but focuses on SEC, Federal Register, and US federal agencies. Lawstronaut is broader (155+ jurisdictions) and deeper (court cases, not just regulations). The two are complementary: Bot Wire for real-time regulatory monitoring, Lawstronaut for structured legal research.

## Quick Start

### Connection Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (Remote) |
| **Endpoint** | `https://mcp.lawstronaut.com` |
| **Authentication** | OAuth 2.0 (client_id + client_secret) or Bearer token |
| **Pricing** | Paid subscription required |
| **GitHub** | `Lawstronaut-FZCO/lawstronaut-mcp` (1★, created Jul 9, 2026) |

### Option A: Bearer Token (CLI, Scripts, Claude Code)

```bash
export LAWSTRONAUT_MCP_BEARER_TOKEN="your-token-here"

# Claude Code
claude mcp add --transport http lawstronaut https://mcp.lawstronaut.com \
  -H "Authorization: Bearer $LAWSTRONAUT_MCP_BEARER_TOKEN"
```

```json
{
  "mcpServers": {
    "lawstronaut": {
      "transport": "http",
      "url": "https://mcp.lawstronaut.com",
      "headers": {
        "Authorization": "Bearer your-token-here"
      }
    }
  }
}
```

### Option B: OAuth 2.0 (Claude Desktop, ChatGPT, Cursor)

OAuth endpoints:
- **Authorization:** `https://mcp.lawstronaut.com/oauth/authorize`
- **Token:** `https://mcp.lawstronaut.com/oauth/token`
- **Discovery:** `https://mcp.lawstronaut.com/.well-known/oauth-authorization-server`

Flow: `response_type=code` → redirect with `code` → exchange at `/oauth/token` with `grant_type=authorization_code`.

### Get Credentials

1. Purchase a subscription at [lawstronaut.com](https://lawstronaut.com)
2. Log into the [developer portal](https://dev-portal.filerskeepersapi.co/)
3. Open **MCP server access** from the Home menu
4. Create a **client ID + client secret** (OAuth) or a **bearer token**

## Key Tools

Lawstronaut's tools cover the full legal research workflow:

| Category | Capability |
|----------|-----------|
| **Search** | Full-text search across 50M+ legal documents with jurisdiction, date, and document-type filters |
| **Retrieve** | Fetch complete legal documents with structured metadata (citation, court, date, parties, statutes cited) |
| **Browse** | Navigate legal hierarchies — jurisdiction → court → case type → year |
| **Citations** | Trace citation networks — what cites this case, what this case cites |
| **Updates** | Check for newer treatments (overruled, distinguished, affirmed) and regulatory amendments |
| **Export** | Structured output in markdown with proper legal citations |

## Example Usage

### Regulatory Research

Ask your agent: *"What are the current data protection requirements for SaaS companies operating in the EU, UK, and California?"*

The agent searches Lawstronaut across GDPR (EU), UK DPA 2018, and CCPA/CPRA (California), returning relevant statutes with citations and effective dates.

### Compliance Check

Ask your agent: *"Has there been any new SEC enforcement action against AI companies in Q3 2026?"*

The agent searches for recent SEC actions filtered by industry and date, returns cases with summaries and links to full documents.

### Competitive Legal Intelligence

Ask your agent: *"What patent litigation involves our top 3 competitors?"*

The agent searches court records across jurisdictions for patent cases naming your competitors, returns case summaries and status.

### Cross-Jurisdiction Analysis

Ask your agent: *"Compare employment termination requirements across Germany, Japan, and Brazil."*

The agent retrieves relevant labor laws from all three jurisdictions, structures the comparison, and cites sources.

## Pricing

Paid subscription required. Plans vary by document access volume and jurisdiction coverage. Check [lawstronaut.com](https://lawstronaut.com) for current pricing.

## Repository & Resources

| Resource | URL |
|----------|-----|
| **GitHub** | [github.com/Lawstronaut-FZCO/lawstronaut-mcp](https://github.com/Lawstronaut-FZCO/lawstronaut-mcp) |
| **Website** | [lawstronaut.com](https://lawstronaut.com) |
| **Developer Portal** | [dev-portal.filerskeepersapi.co](https://dev-portal.filerskeepersapi.co/) |
| **Server Card** | `https://mcp.lawstronaut.com/.well-known/mcp/server-card.json` |
| **MCP Endpoint** | `https://mcp.lawstronaut.com` |

## Verdict: ★★★ — Essential for Compliance & Legal Operations

Lawstronaut is the most comprehensive legal research MCP server available — 155+ jurisdictions, 50M+ documents, structured data with proper citations. For any operator in a regulated industry or any business operating across multiple jurisdictions, this closes the gap between "ask your AI lawyer" and "get actual legal citations from official sources."

**Strengths:** 155+ jurisdictions, 50M+ documents, OAuth + Bearer token auth, proper legal citations, structured document metadata, continuously updated, public server card for tool discovery.

**Limitations:** Paid subscription required (no free tier), proprietary license, 1 GitHub star (early stage), documentation still maturing, requires understanding of legal research concepts to use effectively.

**Best for:** Compliance officers, legal operations teams, in-house counsel, regulated industry operators (fintech, healthcare, defense), and businesses operating across multiple international jurisdictions.
