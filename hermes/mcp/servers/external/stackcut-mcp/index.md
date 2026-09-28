---
title: Stackcut MCP - SaaS Cost Reduction for AI Agents
description: "Stackcut gives agents 17 tools to find cheaper plans, alternatives and build-it-yourself paths for paid software."
category: Finance
stars: n/a (new listing)
added: 2026-09-27
source: "mcp.so server page (stackcut.io)"
relevance: ★★★
tags: [finops, saas-cost, cost-optimization, subscription-audit, vendor-alternatives, savings, remote-mcp]
---

# Stackcut MCP

**An agent that knows what your software stack really costs, and what to cut.** Stackcut exposes a remote MCP server at `https://stackcut.io/mcp` with 17 tools for SaaS cost reduction: cheaper plans, alternatives, open-source paths, pay-per-use options, agent skills and build-it-yourself routes, priced from public list prices and the operator's own usage numbers. Recipe cards carry modeled first-year savings, and whole-stack audits separate prices the operator confirmed from modeled list prices.

```
Server type: Remote
Auth: endpoint-managed (agent codes for saved plans are read-only and expire)
Endpoint: https://stackcut.io/mcp
Tools: 17
Pricing: vendor pricing (stackcut.io)
Category: Finance / FinOps
Built by: Stackcut (stackcut.io)
```

## Why This Matters for Operators

Software spend creeps upward one renewal at a time, and the analysis to stop it is genuinely tedious: pull every plan, read every cap, model every usage. Stackcut mechanizes it. The agent can re-cost one product at the operator's actual price and usage, run an audit across every subscription a business holds, and return the few missing facts that would change the answer, ranked by what is at stake.

Privacy design is explicit: Stackcut stores tool-call arguments to improve recommendations, but account keys only as one-way hashes, never IP addresses, billing sources or secrets, and operators are told not to send personal data.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| search_recipes / get_recipe | Find and open replacement recipe cards with modeled savings |
| find_alternatives | Re-cost one product at the operator's own price and usage |
| audit_stack / start_audit | Whole-stack audits separating confirmed and modeled prices |
| find_paid_services | Locate paid services in a codebase locally, sending only names |
| workflow recipes | Reviewed runbooks for migrations, consolidation and retirement |
| choose_stack / plan_stack_from_spec | Price vendor picks at given volumes or from a product brief |
| agent_plan | Read-only sca_ codes that unlock a personal savings plan |

## Installation

```bash
claude mcp add stackcut --transport http https://stackcut.io/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "stackcut": {
      "type": "http",
      "url": "https://stackcut.io/mcp"
    }
  }
}
```

Agent codes start with `sca_`, are copied from "Send to my agent" on stackcut.io, are read-only and expire.

## Business Relevance

- **Founders** audit the whole subscription stack and cut what does not earn its seat
- **Finance operators** get savings models with sources and cancel paths per vendor
- **Dev teams** replace tools with open-source or build-it routes when they fit
- **Agencies** re-cost client stacks before renewal season

## Integration with CorpusIQ

Stackcut pairs with CorpusIQ's Stripe connector: Stripe balance transactions and charges give CorpusIQ the real spend record, and Stackcut turns that spend into candidate cuts. CorpusIQ's business recaps can surface Stackcut's modeled savings alongside actual cash flow from QuickBooks so operators see the opportunity next to the reality.

## Limitations

- Savings are modeled from public list prices; real renewal terms can differ
- Runbooks are guidance, not proof a migration ran
- Operators must feed usage numbers for accurate re-costing
- New listing; the recipe catalog depth is still growing

## FAQ

### Where do the savings numbers come from?

Public list prices plus the operator's own usage numbers; prices the operator confirms are kept separate from modeled estimates.

### What data should not be sent?

Personal data and secrets; Stackcut hashes account keys one-way and never stores IP addresses.

### Are the runbooks proof a migration ran?

No. Runbooks are guidance, not evidence of a completed migration.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
