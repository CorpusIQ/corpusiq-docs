---
title: "GAIP Agents MCP - Agent Verification and Evidence Receipts"
description: "Read-only verification of AI agents and MCP servers - reachability, change watching, failure diagnosis and evidence receipts."
category: Compliance
stars: n/a (no public repo)
added: 2026-09-29
source: "mcp.so server page (gaipagents.com)"
relevance: ★★
tags: [agent-verification, monitoring, receipts, evidence, conformance, a2a, read-only, remote-mcp]
---

# GAIP Agents MCP

**Evidence about agents, before and after you trust them with work.** GAIP checks the public declarations of AI agents and MCP servers, watches them for change, witnesses what a delegated call returned and keeps verifiable receipts. Free, read-only, no account or API key - every result states what was observed and when, and explicitly is not a certification, endorsement, ranking or score.

```
Server type: Remote (Streamable HTTP)
Auth: None (public, read-only)
Endpoint: https://www.gaipagents.com/mcp
Tools: 4 core (gaip_check, gaip_watch, gaip_diagnose, gaip_verify) plus gaip_quickstart and a specialist catalogue
Pricing: Free
Category: Compliance
Built by: GAIP (gaipagents.com); broker gaip-broker v1.6.1, live-verified Sep 29, 2026
```

## Why This Matters for Operators

Operators now hand real work to third-party agents - scheduling, research, outreach - with almost no way to check what they are delegating to. GAIP answers the practical questions: does the agent actually work, is it reachable and valid, has it changed since you approved it, and did it deliver what was promised? Each check returns a one-line verdict with observed facts and a timestamp.

Because GAIP is read-only and keyless, checking costs nothing and creates no account surface to compromise. Conformance submissions are never retained - only a summary of codes, score and hashes is kept, so the receipt verifies without storing the underlying data.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| gaip_check | Is an AI agent, MCP server or API working, reachable and valid? Has it changed? Returns a one-line verdict (READY, FIXES_NEEDED, NO_AGENT) |
| gaip_watch | Follow an agent or server for changes: no-account feed links, latest dated changes, optional webhook alerts |
| gaip_diagnose | Why did a call fail and how to fix it: pass the error text and/or HTTP status, with observed changes from the service URL |
| gaip_verify | Did it deliver what was promised? Check claims and citations for accuracy against the cited pages |
| gaip_quickstart | Guided first call with a ready-to-run example for each tool |

The full catalogue is listed at gaipagents.com/mcp/all and per specialist at /mcp/agents/{agent_id}. Prompts ship ready-made requests (check an agent, why did my call fail, watch an MCP server); resources serve llms.txt, the products guide, the receipt specification and the Observatory summary.

## Installation

```bash
claude mcp add gaip-agents --transport http https://www.gaipagents.com/mcp
```

No sign-up and no API key. The endpoint publishes the standard MCP resource list, so any MCP client can browse the receipt specification and products guide before making a call.

## Configuration

```json
{
  "mcpServers": {
    "gaip-agents": {
      "url": "https://www.gaipagents.com/mcp"
    }
  }
}
```

## Business Relevance

- **Operators delegating to agent services** check reachability, validity and change history before and during a delegation
- **Procurement and compliance leads** collect evidence packs and incident bundles from retained receipts
- **Builders publishing agents** point suppliers and customers at a public, free verification endpoint
- **Support teams** diagnose failed agent calls with a bounded repair plan instead of re-reading error logs

## Integration with CorpusIQ

GAIP verifies the agents around a CorpusIQ workflow while CorpusIQ answers from live business data. A composed workflow: before an assistant hands a task to a third-party agent, it runs gaip_check on the agent's declaration; after the delegated call returns, gaip_verify checks that cited pages actually contain the quoted text. Receipts land in the evidence ledger, giving operators an audit trail for every delegated step alongside their business data.

## Limitations

- Observation-only: GAIP reports facts with timestamps, it does not certify, endorse or score
- Read-only design means no payments, external side effects or automatic evidence credit
- New listing; the vendor publishes the full catalogue at gaipagents.com/mcp/all
- Verdicts reflect what was observed at call time, not a guarantee of future behaviour

## FAQ

### Does checking an agent cost anything or need an account?

No. GAIP is free, read-only and keyless - the endpoint serves public checks with no account surface.

### Is a GAIP result a certification?

No. Every result states what was observed and when, and is explicitly not a certification, endorsement, ranking or score, and not legal, financial or insurance advice.

### What is kept when I submit a conformance declaration?

Only a summary - codes, score and hashes - is retained, so the receipt verifies without storing the underlying submission.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
