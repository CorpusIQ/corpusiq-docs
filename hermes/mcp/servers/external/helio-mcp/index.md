---
title: "Helio MCP - Governance Proxy for AI Agent Tool Calls"
description: "Open-source MCP governance proxy that sits between AI agents and their MCP servers. Every tool call passes through Helio, which enforces policy rules, routes risky actions to human approval, caps cumulative spend, and records an audit trail - without changing agent code or MCP servers. Apache-2.0, npm @gethelio/proxy 0.14.0, self-hosted."
category: Security
stars: 200+ (GitHub, open source)
added: 2026-09-14
source: "mcpservers.org /all page 1 (Sep 14 evening crawl) + repo docs at github.com/gethelio/helio"
relevance: ★★★
tags: [governance, security, policy, audit, approval, spend-limits, mcp-proxy, open-source, apache-2, agent-infrastructure]
---

# Helio MCP

**Open-source governance proxy for AI agents.** Helio is an MCP proxy that sits between your AI agents and the tools they use. Every tool call passes through it: policies are enforced, risky actions route to human approval, cumulative spend is capped, and every decision is recorded - without changing your agent code or your MCP servers. It governs what agents do to the rest of the world across any MCP-compatible client: Claude, ChatGPT, LangChain, CrewAI or a custom framework.

```
Server type: Local proxy (stdio or HTTP upstreams it fronts)
Auth: none by default (it governs other servers' auth)
Install: npx @gethelio/proxy init
Version: 0.14.0 (npm, verified)
License: Apache-2.0
Repo: github.com/gethelio/helio (verified live)
Category: Security
Dashboard: bundled web UI (localhost:3100 by default)
```

## Why This Matters for Operators

The failure mode every team running agents hits eventually: an agent calls an API you did not expect, spends money you did not authorize, or modifies a production record you cannot easily undo. Model providers are building governance for their own platforms, but agents run across several clients and frameworks, and none of them govern what happens in downstream systems like Stripe, Salesforce or GitHub.

Helio puts the control in the path instead of the prompt. A rule in Helio is not in the model's context, so a long session cannot evict it and an injection cannot argue it away. A tool call routed through Helio is decided before it is forwarded, whatever the model has been told. Every attempt to reload the policy file, including one that removes a rule, is itself an audit record, and each record carries the hash of the config in force when it was written, so a policy change shows up against the decisions made under it.

## How It Works

Two integration paths:

1. **Proxy only.** Point your MCP client at Helio instead of your MCP server. Zero code changes, immediate governance.
2. **Proxy plus SDK.** Add the thin Python SDK to annotate tool calls with evidence context and action dependencies. Richer governance, under 500 lines of code.

Helio records the enforcement grade it achieved per call:

| Grade | Path | Meaning |
|---|---|---|
| Structural | stdio MCP | Helio owns the child process it spawned; nothing on the MCP path routes around it |
| Network | HTTP MCP | Structural, given you control the upstream's egress |
| Host-enforced | Hook adapters (e.g. OpenClaw) | The framework's hook gate enforces; Helio decides, and labels the grade honestly |

## Policy Capabilities

- **Deny rules** on tool-name globs, for example blocking `delete_*` outright.
- **Rate limits** per tool, for example `search_*` capped at 100 calls per hour.
- **Spend limits** on payment tools, reading an amount field from the call arguments.
- **Cross-tool budgets**: one depleting pot shared by every tool that spends, per session, with `deny` or `require_approval` on exceed.
- **Session identity**: ordered identity sources (header, legacy header) so calls resolve to a session; unresolved sessions can be denied.
- **Audit trail**: SQLite storage with configurable retention and optional response bodies included.
- **Dashboard**: bundled UI for reviewing decisions and spend.

## Installation

```bash
npx @gethelio/proxy init
```

That single package ships the proxy runtime and the bundled dashboard. Running your agent in a container? `npx @gethelio/proxy init --sandbox` writes a sidecar layout instead.

**Heads up:** Helio starts in audit-only mode. `init` scaffolds the `policies` section commented out, so out of the box it records every tool call but blocks nothing. Uncomment and edit `policies` to start enforcing.

## Configuration

```yaml
version: '1'

upstream:
  url: 'http://localhost:8080/mcp'   # your existing MCP server
  transport: streamable-http

listen:
  port: 3000

policies:
  default: allow
  rules:
    - match: { tool: 'delete_*' }
      action: deny
      feedback: { message: 'Destructive operations are disabled' }
    - match: { tool: 'create_payment' }
      action: spend_limit
      limits:
        max_spend: { field: '$.amount', limit: 5000, currency: 'GBP', window: 24h }

budgets:
  - name: agent-payments
    limit: 50
    currency: USD
    window: session
    on_exceed: require_approval
    contributors:
      - match: { tool: 'stripe_*' }
        field: '$.amount'

audit:
  storage: sqlite
  retention: 90d
```

To govern more than one MCP server, replace `upstream:` with a named `upstreams:` list. Tool sets are never merged: each named upstream is served at its own `/mcp/<name>` door.

## Business Relevance

- **Operators running agents against production systems** get a hard boundary on destructive calls without touching agent code.
- **Finance and ops teams** get cumulative spend caps across every paying tool, with human approval as the over-limit path.
- **Compliance-minded teams** get a durable audit trail with config-backed decisions, which turns "the agent did what?" into a query.
- **Platform teams** get one governance layer across heterogeneous clients and frameworks instead of per-platform rules.

## Integration with CorpusIQ

Helio and CorpusIQ cover opposite halves of the agent stack, and they pair cleanly. CorpusIQ is the read side: it lets any AI client read authorized business data from 40+ tools (Stripe, Shopify, HubSpot, GA4, QuickBooks and more) with source-cited answers and no write path. Helio is the control side for anything that acts. A team can run CorpusIQ for trusted business reads and route agent actions through Helio, so analysis stays read-only while every action tool call is governed, capped and logged.

## Limitations

- **Self-hosted only.** You run and upgrade the proxy; there is no hosted cloud service.
- **The default local install runs the proxy as the same user as the agent.** The project's own security notes state the config, secret and audit store should be outside the agent's reach; run Helio as its own user or in its own container to close that gap.
- **Policy language has a learning curve** (YAML rules with glob matching and JSONPath amount fields).
- **The host-enforced grade is cooperative**: frameworks like OpenClaw enforce through their hook gate rather than in the transport path.
- **Brand new to this catalog** (npm 0.14.0); no third-party case studies yet.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [Governance](/docs/hermes/governance)
- [Security](/docs/hermes/security)
