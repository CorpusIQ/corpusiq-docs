---
title: "Milemarker MCP - Run a Wealth Platform by Asking"
description: "Operate a Milemarker wealth platform from your assistant: governed data queries, dashboards, users and projects, fully audited."
category: Finance
stars: n/a (new listing)
added: 2026-10-09
source: "mcpservers.org /all + chatmcp/mcpso issues (October 9, 2026 evening sweep)"
relevance: ★★
tags: [wealth-management, ria, firm-operations, dashboards, governance, audit, tenant-isolation, remote-mcp]
---

# Milemarker MCP

**The AI interface for the Milemarker wealth-management platform** - query firm data, deploy dashboards, manage users and run projects by asking, with every action flowing through Milemarker's governed APIs and a full audit trail. Rolling out across Milemarker partner firms.

```
Server type: Remote (Streamable HTTP; each firm is served a tenant-routed /mcp/{tenant} URL)
Auth: Scoped token issued by Milemarker (request access from your account team)
Tools: capability surface - data queries, dashboard deployment, user management, search and AI navigators, platform-wide projects; the live tool list comes from your tenant endpoint
Platform: 140+ connected systems through the unified data layer (CRM, custodians, portfolio accounting, compliance, billing, planning)
Security: governed APIs only, tenant isolation, SOC 2 Type II, every action audited
Category: Finance
Built by: Milemarker (milemarker.co; docs.milemarker.co)
```

## Why This Matters for Operators

A wealth firm's operations team spends its week translating questions into tickets: a report request, a dashboard change, a user update, a bulk fix. Milemarker MCP collapses that queue into conversation - **ask for the number and get the number**, in place of the SQL worksheet, the configurator and the admin screen.

The governance model is the point. Every action runs through the same governed APIs the platform already uses, respects tenant boundaries, produces auditable artifacts, and logs every query, deployment and user change. For a regulated firm that is what makes the surface usable at all: the AI gets an operator's reach without skipping policy.

## Tools & Capabilities

| Area | What the assistant can do |
|---|---|
| Query data | Ask a question of the firm's data and get the answer back - no BI ticket, no SQL; the question becomes a governed query |
| Dashboards and metrics | Describe what leadership needs, and the assistant builds and deploys the dashboard |
| Search and navigators | Turn on natural-language search and pre-built AI navigators across the firm's data |
| Users and access | Add advisors, assign teams, set permissions and send invitations in bulk |
| Platform projects | Bulk deployments, mass updates, migrations and audits as one conversation instead of a ticket queue |

The live tool list is served from your firm's tenant endpoint; the areas above are the vendor-documented capabilities.

## Installation

Setup runs through Milemarker: request a scoped token from your account team, drop the configuration snippet into your AI client, and reload. The server address is tenant-routed (`/mcp/{tenant}`), so your firm's URL comes with the token. Clients include Claude, ChatGPT, Codex and Gemini - the platform is model-agnostic by design.

## Configuration and Safety

- Every action flows through Milemarker's governed APIs; nothing bypasses policy.
- Multi-tenant isolation means no firm ever sees another firm's data.
- The platform is built for SOC 2 Type II with 256-bit SSL and 24/7 monitoring, and every action is logged and reviewable.
- The same tenant works across Claude, ChatGPT, Codex and Gemini, and the firm can switch models at any time.

## Business Relevance

- **Firm operations teams** answer data questions the same day instead of waiting on a report queue.
- **Executives** get dashboards built and deployed before the next leadership meeting.
- **Compliance officers** get one place to oversee what AI did and on whose authority.
- **Advisor support** handles user, team and permission changes in bulk from a paragraph.

## Integration with CorpusIQ

Milemarker governs the wealth platform; CorpusIQ keeps the business numbers consistent across everything around it. When a firm question spans both - AUM and households in Milemarker, revenue and spend across Stripe, billing and the CRM - ask each system in the same conversation and compare like-for-like figures: the platform's numbers and the business's numbers, both traceable to source.

## Limitations

- Requires a Milemarker platform subscription: this is the AI interface for an existing tenant, not a standalone connector.
- Access is gated behind a scoped token from Milemarker; there is no self-serve public endpoint.
- Capability descriptions are vendor-provided and the tool list is served from your tenant; specifics vary by firm configuration.
- Wealth-management scope: RIAs, broker-dealers, aggregators and fund managers rather than general business operations.

## FAQ

### Can I try it without Milemarker?

No. The MCP server operates on top of your Milemarker tenant, so access starts with a Milemarker account and a scoped token from the account team.

### How does the platform keep AI actions compliant?

Every action goes through the same governed APIs the platform already uses, respects tenant boundaries, and is logged and auditable; the vendor states SOC 2 Type II certification.

### Which AI assistants can connect?

Any MCP-compatible assistant: today that includes Claude, ChatGPT, Codex and Gemini, and the same tenant works across all of them.

## See Also

- [X1 Wealth MCP - Cited Family Office Records](/hermes/mcp/servers/external/x1-wealth-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
