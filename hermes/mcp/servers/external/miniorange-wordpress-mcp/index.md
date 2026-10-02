---
title: miniOrange WordPress MCP - Secure WordPress Gateway
description: Secure MCP gateway for WordPress and WooCommerce from miniOrange - policy enforcement, DLP redaction, human-in-the-loop approvals and immutable audit trails for every AI request
category: Business Operations
stars: n/a (new listing)
added: 2026-09-04
source: "mcp.so feed"
relevance: ★★
tags: [wordpress, woocommerce, ai-governance, policy-enforcement, dlp, audit-trail, remote-mcp]
---

# miniOrange WordPress MCP

**Remote MCP server (Streamable HTTP, OAuth) plus WordPress plugin from miniOrange that exposes a WordPress site as a governed MCP endpoint - every AI request authenticated, checked against security policies, DLP-scanned, logged, and optionally routed to human approval before execution.** Built by miniOrange, an established identity and security vendor, for organizations that want AI agents working on WordPress and WooCommerce without handing them the keys.

```
Server type: Remote (Streamable HTTP) + WordPress plugin (wordpress.org/plugins/miniorange-secure-mcp-server)
Auth: Dynamic OAuth 2.0
Endpoint: https://gateway.miniorange.ai/v2/mcp
Tools: Capability surface governed per site (no public tool list)
Pricing: Free plan; Premium governance from $249/month
Category: Business Operations & AI Governance
Built by: miniOrange (xecurify)
```

## Why This Matters for Operators

A WordPress or WooCommerce site holds customer emails, orders and payment context - and an agent connected through a plain MCP endpoint is another way to leak them. miniOrange's plugin sits between the agent and the site: it verifies every request's identity and permissions, masks PII and secrets before anything reaches the model, and routes high-risk actions (refunds, content changes, user modifications) to a human for approval. Operators get AI-assisted site management with a security boundary, not a bypass.

**Every AI action is visible.** An immutable audit trail records each request, policy decision, approval and execution, so the question "who changed this and why" has an answer. Weekly access reviews and agent reputation scoring make least-privilege a standing practice instead of a one-time setup.

## Tools & Capabilities

The listing publishes no tool list - the surface is governed per site through the plugin. Capabilities from the vendor's documentation:

| Capability | What it does |
|---|---|
| WordPress abilities governance | Discover WordPress, WooCommerce and plugin capabilities and govern them individually |
| REST API access control | Control standard WordPress API requests with per-agent permissions |
| WP-CLI monitoring | Monitor, control and audit terminal-level commands |
| Policy decision engine | Check identity, permissions and action types; return approve or deny |
| DLP redaction | Mask emails, phone numbers, API keys and other sensitive data before the model sees them |
| Human approval workflow | Route critical AI requests for human review before execution |
| Non-Human Identity registry | Unique identity per agent with tracked permissions and activity |
| Dry-run simulation | Test policies against real AI requests without affecting production |
| Prompt-injection detection | Detect hidden instructions before they influence responses |
| Rate limits and quotas | Control request volume and AI activity per agent |

## Installation

```bash
claude mcp add miniorange-wordpress --transport http https://gateway.miniorange.ai/v2/mcp
```

Install the companion plugin from the WordPress plugin directory (`miniorange-secure-mcp-server`), then connect any MCP client - ChatGPT, Claude, Cursor and Gemini walkthroughs are published by miniOrange.

## Configuration

```json
{
  "mcpServers": {
    "miniorange-wordpress": {
      "type": "http",
      "url": "https://gateway.miniorange.ai/v2/mcp"
    }
  }
}
```

First connect opens a browser window for dynamic OAuth 2.0 authorization. The free plan covers native MCP connectivity and access to all WordPress abilities; policy enforcement, human approvals, sensitive-data protection and audit trails are on the Premium plan.

## Business Relevance

- **Agency and site operators** let AI agents manage content, orders and support workflows under policy instead of trusting the agent not to break things
- **WooCommerce store owners** protect customer data while agents handle order and product operations with approval gates on sensitive actions
- **Security-conscious teams** get DLP, prompt-injection detection and an audit trail for every AI action on their WordPress estate

## Integration with CorpusIQ

CorpusIQ's commerce connectors (Shopify, WooCommerce-class store data, payments) give agents read-only business context. miniOrange WordPress MCP adds the governed write path for WordPress and WooCommerce sites: an agent can read the business from CorpusIQ and then propose site changes through miniOrange's policy engine, where human approval and audit logging decide what actually executes. Read-only business data plus governed site actions is the operator-safe combination.

## Limitations

- No public tool list - capabilities are defined by the plugin's governed ability surface
- Premium governance features (policy enforcement, approvals, DLP) start at $249/month
- WordPress-scoped - does not govern non-WordPress systems
- Brand new listing on mcp.so; the cloud gateway endpoint is vendor-hosted

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Strac MCP DLP - Sensitive Data Redaction for AI Agents](/hermes/mcp/servers/external/strac-mcp-dlp)
- [Asyntai MCP - AI Support Agent for Websites](/hermes/mcp/servers/external/asyntai-mcp)
- [iubenda MCP - Website Legal Compliance for Agents](/hermes/mcp/servers/external/iubenda-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
