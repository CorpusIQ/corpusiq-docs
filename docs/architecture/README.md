---
meta_title: "CorpusIQ Architecture — MCP Endpoint, Connector Layer, and Data Flow"
meta_desc: "Complete CorpusIQ system architecture: MCP endpoint, OAuth 2.0 authentication layer, 36+ connector adapters, data flow from AI agent to business source, security model, and deployment infrastructure."
category: "Documentation"
tags: ["corpusiq architecture", "mcp endpoint", "connector layer", "data flow", "system design", "ai agent architecture", "oauth architecture"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/architecture"
robots: "index,follow"
---
# Architecture

CorpusIQ connects AI agents and chat interfaces to 36 business data sources through a single MCP endpoint.

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AI Clients                            │
│  Claude Desktop · Cursor · Hermes · ChatGPT · Windsurf  │
└────────────────────┬────────────────────────────────────┘
                     │ MCP Protocol
┌────────────────────▼────────────────────────────────────┐
│              CorpusIQ MCP Endpoint                       │
│           corpusiq.io/mcp/direct-connection              │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ OAuth 2.0    │  │ Tool Registry│  │ Prompt Store  │  │
│  │ Device Flow  │  │              │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                 Connector Layer                          │
│                                                          │
│  Stripe · Shopify · Quickbooks · HubSpot · PostgreSQL   │
│  GA4 · Meta Ads · Klaviyo · Gmail · Slack · MongoDB     │
│  ... 26 more connectors                                  │
└─────────────────────────────────────────────────────────┘
```

## Key Components

### MCP Endpoint
The single entry point for all AI interactions. Implements the Model Context Protocol specification. Supports `tools/list`, `tools/call`, `resources/list`, `resources/read`, `prompts/list`, and `prompts/get`.

### Authentication Layer
OAuth 2.0 Device Authorization Grant for AI agents. Email-based authentication for chat users. Each data source connection requires one-time OAuth authorization.

### Connector Layer
Individual adapters for each of the 36 supported business data sources. Each connector handles authentication, data retrieval, normalization, and error handling for its specific API.

### Data Flow

1. AI agent sends a query via MCP
2. MCP endpoint authenticates the request
3. Tool registry maps the query to the appropriate connector(s)
4. Connector retrieves data from the source API
5. Data is normalized and returned to the agent
6. Agent presents the answer to the user

## Security Model

- Read-only access to all connected data sources
- OAuth 2.0 with refresh token rotation
- Device flow prevents credential exposure
- HTTPS/TLS for all connections
- Audit logging of all queries
- Scoped access per data source

## Deployment

CorpusIQ is a hosted service. The MCP endpoint runs on production infrastructure with automatic scaling and high availability.

The [demo.corpusiq.io](https://demo.corpusiq.io) chat interface is a web application that connects to the same MCP endpoint used by AI agents.

## Frequently Asked Questions

**Q: What is the CorpusIQ system architecture?**  
A: CorpusIQ uses a three-layer architecture: AI clients (Claude, ChatGPT, Cursor) connect via MCP protocol to the CorpusIQ MCP endpoint, which routes queries through the connector layer to 36+ business data sources. All access is read-only via OAuth 2.0.

**Q: How does data flow through CorpusIQ?**  
A: AI agent sends query via MCP → MCP endpoint authenticates request → Tool registry maps query to connectors → Connector retrieves data from source API → Data is normalized and returned → Agent presents answer to user. All steps are logged for audit.

**Q: Is CorpusIQ self-hosted or a managed service?**  
A: CorpusIQ is a fully managed hosted service with automatic scaling and high availability. The MCP endpoint runs on production infrastructure — no servers to manage, no software to install.


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the CorpusIQ system architecture?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CorpusIQ uses a three-layer architecture: AI clients (Claude, ChatGPT, Cursor) connect via MCP protocol to the CorpusIQ MCP endpoint, which routes queries through the connector layer to 36+ business data sources. All access is read-only via OAuth 2.0."
      }
    },
    {
      "@type": "Question",
      "name": "How does data flow through CorpusIQ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI agent sends query via MCP \u2192 MCP endpoint authenticates request \u2192 Tool registry maps query to connectors \u2192 Connector retrieves data from source API \u2192 Data is normalized and returned \u2192 Agent presents answer to user. All steps are logged for audit."
      }
    },
    {
      "@type": "Question",
      "name": "Is CorpusIQ self-hosted or a managed service?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CorpusIQ is a fully managed hosted service with automatic scaling and high availability. The MCP endpoint runs on production infrastructure \u2014 no servers to manage, no software to install."
      }
    }
  ]
}}
</script>
## Internal Links

- **[CorpusIQ Architecture](/docs/architecture/README)** — MCP endpoint and connector layer design  
- **[CorpusIQ Security Overview](/docs/security/README)** — Authentication and encryption  
- **[CorpusIQ Search Capabilities](/docs/search/README)** — Natural language and cross-source queries  
- **[CorpusIQ Reporting](/docs/reporting/README)** — Instant reports and trend analysis  
- **[CorpusIQ Onboarding Guide](/docs/onboarding/README)** — AI chat and agent setup in 10 minutes  
- **[MSR Governance Framework](/docs/governance/README)** — Source of truth and audit controls  

*Powered by CorpusIQ — the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
