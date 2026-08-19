---
title: "SandBase CLI - MCP Bridge to 2,000 Plus AI Models and APIs"
description: "SandBase CLI is a local MCP bridge connecting 25 AI client targets to a catalog of 2,000 plus AI models and APIs with discovery, inspection, execution and cost tracking tools"
category: AI Infrastructure
stars: 17
added: 2026-08-19
source: "mcp.so GitHub issue #3640"
relevance: ★★
tags: [ai-models, model-catalog, api-bridge, cost-tracking, dev-tools, npm, local-mcp]
---

# SandBase CLI

**A local MCP bridge that connects 25 AI client targets to a catalog of 2,000+ AI models and APIs, with discovery, inspection, execution, and cost tracking.** SandBase CLI is a TypeScript/Node stdio server (Apache-2.0) that gives any MCP-capable assistant a searchable catalog of models, multimodal generation, and sandboxed execution — plus per-run cost accounting.

```
Server type: Local (npm, stdio MCP bridge)
Auth: SandBase account (balance-based)
Package: npx -y @sandbaseai/cli (Apache-2.0)
Tools: 6 (discover, inspect, run, run_get, runs, account)
Client targets: 25 (Codex, Claude Code, Cursor, Windsurf, Gemini CLI, OpenCode, Kiro, Warp, Amp, Hermes, OpenClaw and more)
Category: AI Infrastructure
Built by: SandBase
```

## Why This Matters for Operators

Model choice is now a cost and capability decision, not a technical one, and the catalogs live behind ten different vendor docs. SandBase normalizes the whole surface: one search across 2,000+ models and APIs, schema and pricing inspection before calling, execution with async polling, and a runs ledger that shows what each call cost. For an operator running agents, the `sandbase_runs` and `sandbase_account` tools turn model spend from a monthly surprise into a per-run line item.

The bridge design also removes per-client setup: the CLI installs the connection into whichever of the 25 supported clients is in use, so the same catalog serves Codex, Cursor, Hermes, and the rest without reconfiguration.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `sandbase_discover` | Search the 2,000+ model and API catalog |
| `sandbase_inspect` | Inspect schemas, pricing, and request templates |
| `sandbase_run` | Execute a model or API call |
| `sandbase_run_get` | Poll asynchronous run results |
| `sandbase_runs` | Inspect recent calls and their costs |
| `sandbase_account` | Check account balance |

## Installation

```bash
npx -y @sandbaseai/cli connect
```

The connect command walks through linking the bridge to the AI client in use. Local stdio transport, no hosted endpoint required.

## Configuration

```json
{
  "mcpServers": {
    "sandbase": {
      "command": "npx",
      "args": ["-y", "@sandbaseai/cli", "mcp"]
    }
  }
}
```

Apache-2.0 licensed, repository at `github.com/sandbaseai/cli`. Account balance is managed at SandBase; runs bill against the account.

## Business Relevance

- **Operators running agents** get per-run cost visibility instead of monthly model-bill surprises
- **Builders** compare models on pricing and schema before committing to one
- **Automation teams** run one catalog across Codex, Cursor, Hermes, and other clients
- **FinOps** audit agent model spend from the runs ledger
- **Evaluators** test candidate models through a single inspection surface

## Integration with CorpusIQ

CorpusIQ brings the business data layer (GA4, Search Console, Ahrefs, CRM) while SandBase brings the model execution layer. An operator can run both in one agent session: CorpusIQ for business metrics and connectors, SandBase for model catalog discovery, execution, and cost tracking — with the runs ledger feeding the same cost discipline CorpusIQ applies to marketing spend.

## Limitations

- New listing (Aug 2026), 17 stars, early-stage CLI (v0.1.x)
- Requires a SandBase account with balance for execution
- Local-only bridge: no hosted streamable-HTTP endpoint published
- Catalog quality depends on SandBase's listings and uptime

## See Also

- [Routara LLM Gateway MCP — Multi-Provider LLM Routing](/hermes/mcp/servers/external/routara-llm-gateway-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
