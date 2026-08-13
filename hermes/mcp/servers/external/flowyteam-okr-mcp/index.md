---
title: FlowyTeam OKR MCP
description: Native OKR MCP server — connect Claude, ChatGPT, or n8n to objectives, key results, and tasks; post check-ins and move KR progress
category: Productivity
stars: n/a (new)
added: 2026-08-12
source: mcp.so
relevance: ★★
tags: [okr, kpi, performance-management, project-management, hr, productivity, oauth]
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/flowyteam-okr-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# FlowyTeam OKR MCP

**Native OKR MCP server from FlowyTeam** (MIT license). Connect Claude Desktop/web/mobile, ChatGPT, Claude Code, or n8n and your agent can read every objective and key result in the workspace, post check-ins, and move key-result progress — goal tracking as a tool call instead of a dashboard chore.

```
Server type: Remote + self-hostable
Auth: OAuth
Repo: https://github.com/flowy-team/okr-mcp-server
Setup guide: https://flowyteam.com/get/mcp-server
API reference: https://flowyteam.com/get/mcp-docs
Category: Productivity / OKR
```

## Why This Matters for Operators

OKRs die in dashboards — the system only works when check-ins happen. FlowyTeam's MCP puts the OKR system where the work already happens: the agent a team uses daily can read objectives, file check-ins, and move KR progress without anyone opening the OKR tool. That closes the "set-and-forget" gap that kills most goal frameworks by week six.

## Tools & Capabilities

- **Read workspace** — every objective, key result, and task, live
- **Check-ins** — post progress updates from any MCP client
- **KR progress** — move key-result progress directly
- **OAuth connector** — per-user scoped access, documented at flowyteam.com/mcp-docs
- **n8n support** — embed OKR reads and check-ins in automation workflows

## Installation

```bash
git clone https://github.com/flowy-team/okr-mcp-server
```

Setup guide and OAuth connector docs: [flowyteam.com/get/mcp-server](https://flowyteam.com/get/mcp-server) and [flowyteam.com/get/mcp-docs](https://flowyteam.com/get/mcp-docs). No standard parseable MCP config block is published in the README — follow the repo install instructions and OAuth flow.

## Configuration

The server uses FlowyTeam's OAuth connector for authentication. Follow the setup guide at flowyteam.com/get/mcp-server for the client-specific config; the OAuth flow grants the agent per-user access to objectives and key results.

## Business Relevance

- **Founders and operators** get weekly check-in cadence enforced by the tool, not by willpower
- **HR and people teams** can pull OKR status into review prep without chasing managers
- **Teams running n8n** can trigger notifications off KR movement automatically
- **MIT-licensed** — auditable and self-hostable for data-sensitive orgs

## Integration with CorpusIQ

FlowyTeam OKR pairs with CorpusIQ's business-data connectors to turn goals into measurable reality: objectives live in FlowyTeam, actuals live in CorpusIQ (Stripe revenue, Shopify sales, GA4 traffic). An agent can pull a KR from FlowyTeam, compare it against the real number from CorpusIQ, and file an evidence-backed check-in — replacing the "manager copy-pastes a dashboard screenshot" ritual with a single composed workflow. For a team running weekly goal reviews, that's the difference between check-ins that happen and ones that don't.

## Limitations

- New — listed Aug 2026; ecosystem track record minimal
- README lacks a standard MCP config block; setup requires the FlowyTeam platform docs and OAuth flow
- Tool list not auto-published on directories — verify against the API reference before production use
- Value depends on team adoption of FlowyTeam itself
- OAuth setup is the main friction point for local/stdio use

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
