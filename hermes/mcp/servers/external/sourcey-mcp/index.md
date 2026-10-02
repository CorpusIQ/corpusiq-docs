---
title: "Sourcey MCP - Startup Credits and Agent Readiness Data"
description: "Hosted and stdio MCP server with evidence-backed startup credits, cloud credits, SaaS discounts, grants, and Agent Readiness report cards. Keyless catalog reads with a signed change feed."
category: Business Operations
stars: n/a (new listing, sourcey/mcp-server)
added: 2026-08-29
source: "chatmcp/mcpso issue #3823"
relevance: ★★
tags: [mcp-server, startup-credits, saas-deals, agent-readiness, grants, evidence, vendor-intelligence, remote-mcp]
---

# Sourcey MCP

**A hosted MCP server that lets agents find and compare evidence-backed startup offers - cloud credits, SaaS discounts, free tiers, grants, and partner deals - plus Agent Readiness report cards for API and SaaS products.** Every offer carries inspectable provenance with exact revisions and a signed change feed, so the catalog is auditable rather than a wall of marketing claims. Public catalog reads are keyless; paid HTTP and x402 services are discoverable without settling payments inside MCP.

```
Server type: Remote (Streamable HTTP), hosted + stdio bridge (npx @sourcey/mcp-server)
Auth: None for public catalog reads
Endpoint: https://mcp.sourcey.com/mcp
Tools: 8 (search_offers, compare_offers, inspect_evidence, get_changes, search_readiness, get_readiness, prepare_declaration, get_services)
Pricing: Free catalog reads; paid services listed but paid outside MCP
Category: Business Operations / Startup Resources
Built by: Sourcey (sourcey.com); registry com.sourcey/sourcey@1.2.0; MIT
```

## Why This Matters for Operators

Startup credits and SaaS deals are scattered across every accelerator, cloud marketplace, and vendor partner program, each with different eligibility rules and freshness. Sourcey collapses that into one searchable, evidence-backed catalog: an agent can pull the current credit stack for a company's profile, compare two offers side by side with exact eligibility and freshness, and inspect the evidence revision behind any claim before acting on it.

The Agent Readiness side answers the other half of the equation: report cards grading how well an API or SaaS product actually supports agent use - authentication, payments, provisioning, operations, and recovery - so operators choosing vendor tools for an agent stack can read a structured assessment instead of guessing from marketing pages. The signed change feed means every catalog update is traceable.

**One catalog replaces the fragmented credit-hunting loop, with evidence and change provenance attached to every offer.**

## Tools & Capabilities

Live-probed August 29, 2026 (anonymous initialize returned all eight tools).

| Tool | Purpose |
|---|---|
| `search_offers` | Search startup credits and deals - cloud credits, SaaS discounts, free tiers, grants, perks, partner offers - with filters |
| `compare_offers` | Compare two to ten offers side by side: value, access requirements, eligibility, freshness, evidence |
| `inspect_evidence` | Resolve exact revisions of supporting events and observations behind a claim |
| `get_changes` | Track added, changed, withdrawn, and removed offers through the signed change feed |
| `search_readiness` | Search published Agent Readiness report cards for APIs, SaaS products, auth, payments, provisioning, ops, recovery |
| `get_readiness` | Get one report card with its A+ to F grade, five service-use stages, findings, and blockers |
| `prepare_declaration` | Prepare canonical GitHub-ready YAML for an independent Agent Readiness assessment of one vendor product |
| `get_services` | Discover enabled paid agent services with exact request/response contracts and pricing |

## Installation

```bash
claude mcp add --transport http sourcey https://mcp.sourcey.com/mcp
```

For local stdio use: `npx -y @sourcey/mcp-server`. A container image is published from the sourcey/mcp-server repo packages.

## Configuration

```json
{
  "mcpServers": {
    "sourcey": {
      "type": "http",
      "url": "https://mcp.sourcey.com/mcp"
    }
  }
}
```

Public catalog reads require no authentication. Paid services listed via get_services are settled outside the MCP flow, so no wallet or card lives in the client config.

## Business Relevance

- **Founders** get the full current stack of credits, grants, and free tiers for their stage in one search instead of chasing each program's page.
- **Procurement and finance teams** compare offers with eligibility and evidence attached, so the chosen deal is defensible.
- **Operators building agent workflows** read Agent Readiness report cards before wiring a vendor API into an agent, cutting failed-integration risk.
- **Developer-platform teams** use prepare_declaration to ship a canonical readiness YAML for their own product's listing.

## Integration with CorpusIQ

Sourcey's offer catalog is procurement intelligence that pairs with CorpusIQ's accounting connectors: a CorpusIQ workflow can surface a startup's active credits next to its QuickBooks spend, flagging where the current stack leaves money unclaimed, and log the chosen offer's evidence link into the deal record. For operators standardizing on an agent stack, Sourcey's readiness grades feed the same vendor-evaluation step CorpusIQ workflows already run against connector data, so tooling decisions and business data live in one audit trail.

## Limitations

- Brand new listing - first sweep August 29, 2026.
- Catalog quality depends on Sourcey's evidence pipeline; verify critical claims against the vendor directly.
- Paid services are discoverable but settled outside MCP - the catalog does not execute purchases.
- Agent Readiness grades are Sourcey's framework, not a certification body.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [PreVibe MCP - Product Research for Lean SaaS Founders](/hermes/mcp/servers/external/previbe-mcp)
- [Founders Os MCP - Startup Operating System Tools](/hermes/mcp/servers/external/founders-os)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
