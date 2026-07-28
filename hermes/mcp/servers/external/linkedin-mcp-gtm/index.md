---
title: "LinkedIn MCP by GTM API — Integration Guide"
description: "Managed LinkedIn MCP server for AI agents — search, connect, message, and enrich on LinkedIn. 20,000+ accounts at <1% ban rate."
category: "Sales & Outreach"
stars: "★★★"
source: mcpservers.org
github: https://github.com/gtm-api/linkedin-mcp
date_added: 2026-07-28
---

# LinkedIn MCP by GTM API

The first production-grade, ban-resistant LinkedIn MCP server. Managed by GTM API, this server handles the entire anti-bot stack — rotating residential IPs, browser fingerprinting, session management, and CAPTCHA solving — so your AI agent can focus on LinkedIn actions, not infrastructure.

## What It Does

- **Search:** Find people and companies on LinkedIn with filters (industry, role, location, company size)
- **Connect:** Send connection requests with personalized notes
- **Message:** Send InMail and direct messages through LinkedIn Messaging
- **Enrich:** Pull full profile data, company pages, and relationship graphs
- **Track:** Monitor profile views, post engagement, and connection acceptance rates

## Why It Matters for Operators

Before this MCP, AI-driven LinkedIn outreach meant:
1. Human copies a lead list from Apollo/ZoomInfo
2. Human logs into LinkedIn and manually connects/messages
3. Human tracks responses in a CRM
4. Human follows up

Now: AI agent searches LinkedIn → enriches with Apollo.io data → sends connection request → follows up with message → logs to CRM — all in one workflow.

## Setup

### Prerequisites
- GTM API account (sign up at [gtmapi.com](https://gtmapi.com))
- API key from GTM API dashboard

### Claude Desktop
```json
{
  "mcpServers": {
    "linkedin-gtm": {
      "type": "streamable-http",
      "url": "https://api.gtmapi.com/mcp/linkedin",
      "headers": {
        "Authorization": "Bearer YOUR_GTM_API_KEY"
      }
    }
  }
}
```

### Cursor / VS Code
```json
{
  "mcpServers": {
    "linkedin-gtm": {
      "type": "streamable-http",
      "url": "https://api.gtmapi.com/mcp/linkedin",
      "headers": {
        "Authorization": "Bearer YOUR_GTM_API_KEY"
      }
    }
  }
}
```

### Hermes Agent
```yaml
# ~/.hermes/config.yaml
mcp_servers:
  linkedin-gtm:
    type: streamable-http
    url: https://api.gtmapi.com/mcp/linkedin
    headers:
      Authorization: "Bearer ${GTM_API_KEY}"
```

## Tools

| Tool | Description |
|------|-------------|
| `search_people` | Search LinkedIn profiles by keyword, title, company, location |
| `get_profile` | Get full profile details by LinkedIn URL or profile ID |
| `send_connection_request` | Send a connection request with optional note |
| `send_message` | Send a direct message to a 1st-degree connection |
| `get_messages` | Retrieve recent conversation threads |
| `search_companies` | Search company pages by name, industry, size |
| `get_company` | Get full company page details |
| `enrich_email` | Find LinkedIn profile from email address |
| `get_network_graph` | Get mutual connections and relationship paths |
| `check_connection_status` | Check connection degree to any profile |

## Pricing

| Tier | Price | Includes |
|------|-------|----------|
| Starter | Free | 100 searches/month, 50 connection requests |
| Growth | $49/mo | 1,000 searches, 500 connection requests, messaging |
| Scale | $199/mo | 10,000 searches, 5,000 connection requests, enrichment |
| Enterprise | Custom | Unlimited, dedicated IP pool, priority support |

## Anti-Ban Architecture

GTM API's infrastructure includes:
- **Rotating residential IPs:** 50K+ IPs across 195 countries — no datacenter IP blocks
- **Browser fingerprinting:** Real Chrome fingerprints with consistent WebGL, canvas, and font profiles
- **Session management:** Persistent sessions with human-like activity patterns (random delays, scroll behavior)
- **CAPTCHA solving:** Automatic FunCaptcha and reCAPTCHA resolution
- **Rate limiting:** Intelligent backoff based on LinkedIn's current enforcement posture

This is why they achieve <1% ban rate across 20,000+ accounts — operators don't need to understand any of this. The AI agent just calls tools.

## Use Cases

### B2B Lead Generation
```
Agent: "Find VP of Engineering at Series B SaaS companies in the Bay Area with 50-200 employees who posted about AI in the last month"
→ search_people → enrich with Apollo.io → send_connection_request → follow up with message
```

### Competitive Research
```
Agent: "Who are the top salespeople at [competitor] and what are they posting about?"
→ search_people at competitor → get_profile for each → analyze recent posts
```

### Investor Outreach
```
Agent: "Find partners at AI-focused VC firms who invested in devtools in the last 12 months"
→ search_people by title "Partner" at VC firms → get_profile → cross-reference portfolio
```

### Talent Sourcing
```
Agent: "Find ML engineers at FAANG companies who contribute to PyTorch on GitHub"
→ search_people → get_profile → cross-reference with GitHub activity
```

## Limitations

- **Not for scraping at scale:** GTM API enforces fair-use limits. This is for relationship-building, not data mining.
- **LinkedIn's terms of service:** Automated LinkedIn activity carries risk. GTM API's managed infrastructure mitigates this, but operators should understand compliance implications.
- **1st-degree messaging only:** `send_message` requires an existing connection. For cold outreach, use `send_connection_request` with a note first.

## See Also

- [[apollo-io-mcp]] — B2B contact enrichment (complementary)
- [[x-use-mcp]] — X/Twitter automation (similar approach)
- [[mercury-mcp]] — Banking for operators (fintech stack)
