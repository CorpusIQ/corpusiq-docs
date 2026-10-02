---
title: Kuudo Amazon MCP Suite - Selling Partner and Vendor Central
description: "Kuudo's Amazon MCP suite runs Amazon Seller (Selling Partner API) and Amazon Vendor Central operations from an agent: orders, listings, pricing, FBA and reimbursements for sellers, plus Direct Fulfillment, Retail Procurement, Data Kiosk, Retail Analytics and A+ Content for vendors. Deployed into the operator's own cloud with a Kuudo API key."
category: Commerce & E-Commerce
stars: 0
added: 2026-09-07
source: mcpservers.org /all
relevance: ★★★
tags: [amazon, selling-partner-api, vendor-central, fba, ecommerce, remote-mcp, byoc]
---

# Kuudo Amazon MCP Suite - Selling Partner and Vendor Central Operations

**Remote MCP server pair (Streamable HTTP, deployed in the operator's own cloud)** - Kuudo publishes two Amazon MCP servers: one over the Selling Partner API (orders, listings, pricing, FBA, reimbursements, A+ Content, Data Kiosk, AWD, EasyShip) and one over Vendor Central (Direct Fulfillment, Retail Procurement, Data Kiosk, Retail Analytics, A+ Content). Both deploy through the Kuudo Community plan into the operator's cloud, and the client connects to that deployment.

```
Server type: Remote (Streamable HTTP) per deployment; catalog-only stub images available
Auth: Kuudo API key as bearer header against the operator's deployment host
Endpoints: https://<your-host>/mcp per deployment
Tools: Full SP-API and Vendor Central catalogs (hundreds of read and write operations, catalog published)
Pricing: Kuudo Community plan plus pricing at kuudo.com/pricing.md
Category: Commerce & E-Commerce
Built by: Kuudo (kuudo.com); metadata repos github.com/KuudoAI/amazon-selling-partner-mcp and amazon-vendor-central-mcp
```

## Why This Matters for Operators

Amazon operations live in two worlds: Seller Central for marketplace (3P) sellers and Vendor Central for wholesale (1P) vendors, each with its own API generation and portal. Kuudo's pair normalizes both behind one vendor, one auth model and one deployment pattern - and because the deployment runs in the operator's own cloud, the data path stays in the operator's infrastructure instead of a third-party multi-tenant host.

**The catalog-first design is the unusual part: the public stubs serve the complete tools/list and a catalog resource so registries and clients can inspect the entire surface before anything connects to Amazon - and the live server runs only in the operator's deployment.**

## Tools & Capabilities

| Server | Surface |
|---|---|
| Amazon Selling Partner MCP | Orders, listings, pricing, FBA and reimbursements; A+ Content lifecycle; Data Kiosk queries; AWD inbound inventory; EasyShip scheduling; CustomerFeedback review topics; AppIntegrations notifications |
| Amazon Vendor Central MCP | Direct Fulfillment, Retail Procurement, Data Kiosk, Retail Analytics and A+ Content for 1P vendors |

## Installation

Deploy one instance of each server into your cloud through the Kuudo Community plan, then point any Streamable HTTP client at the deployment host.

```json
{
  "mcpServers": {
    "amazon-vendor-central-mcp": {
      "url": "https://<your-host>/mcp",
      "headers": {
        "Authorization": "Bearer <your Kuudo API key>"
      }
    }
  }
}
```

## Configuration

Replace the host with the deployment hostname and the bearer value with the Kuudo API key. The repos carry registry metadata and catalog-only stubs (MIT); live server source is not published. Full tool reference at kuudo.com/docs/mcp-reference/tools.

## Business Relevance

- **3P sellers** automate orders, listings, pricing and FBA operations from the agent.
- **1P vendors** run Direct Fulfillment and Retail Procurement workflows without portal logins.
- **E-commerce agencies** deploy per-client instances in their own cloud with per-client keys.
- **Compliance-minded operators** keep Amazon data inside their own infrastructure.

## Integration with CorpusIQ

Kuudo operates the Amazon channel; CorpusIQ consolidates the business picture. A composed workflow: the agent reconciles Amazon orders and reimbursements through the Kuudo deployment, then folds them into the multi-channel P&L alongside Stripe, Shopify and QuickBooks data in CorpusIQ.

## Limitations

- Brand new listing (mcpservers.org /all, Sep 2026); metadata repos have 0 stars; live server source is not published.
- Bring-your-own-cloud deployment model; no vendor-hosted multi-tenant endpoint to probe.
- Requires a Kuudo account and API key per deployment.
- Tool names are catalog-level from the vendor's published reference; live enumeration happens only inside a deployment.

## See Also

- [AMZ Vault MCP - Amazon Seller Central and Ads for Agents](/hermes/mcp/servers/external/amz-vault-mcp)
- [ShopSynch MCP - E-Commerce Operations for AI Agents](/hermes/mcp/servers/external/shopsynch-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
