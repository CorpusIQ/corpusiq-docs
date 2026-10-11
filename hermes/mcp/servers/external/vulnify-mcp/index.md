---
title: "Vulnify MCP - Runtime Authorization for AI Agents"
description: "Gate agent actions with ALLOW, REVIEW or BLOCK before they run, from stored policies, with every decision recorded and auditable."
category: Security & Governance
stars: n/a (new listing)
added: 2026-10-10
source: "chatmcp/mcpso issue #5083 (submission) + vendor docs docs.vulnify.io/mcp; catalogued at the October 10, 2026 evening sweep"
relevance: ★★★
tags: [security, governance, agent-authorization, policy, audit, oauth, remote-mcp]
---

# Vulnify MCP

**Remote MCP server that puts an authorization layer in front of agent actions** - ask Vulnify before an agent reads, writes, deletes, exports or sends data, and get a decision back: ALLOW, REVIEW or BLOCK, with the reasoning recorded in an audit trail. The governance find of the October 10 evening sweep, catalogued with the hosted endpoint probed live (a bare initialize returns 401 with the OAuth challenge).

```
Server type: Remote (Streamable HTTP at https://mcp.vulnify.io/mcp); local stdio via npx -y @vulnify/mcp
Auth: Sign in with Vulnify (OAuth 2.1, scoped consent) or an API key (Authorization: Bearer or X-Vulnify-Key)
Tools: 7 - 5 in an OAuth session (get_decision, decide_action, list_policies, check_action, test_policies) and 2 more with an API key (plan_policy_changes, check_mcp_tool_call)
Category: Security & Governance
Built by: Vulnify (vulnify.io; repo github.com/vulnify/vulnify-mcp, MIT)
```

## Why This Matters for Operators

Agents increasingly take real actions in real systems: they send email, move money, change records, export data. The common control is "trust the prompt", which is not a control at all. Vulnify turns policy into a checkable step: the agent asks before it acts, the answer is ALLOW, REVIEW or BLOCK, and every recorded decision lands in a security event and audit entry. REVIEW means a person decides - the server cannot approve it, and the agent must not run the action until that person does. For teams rolling out agents against business systems, this is the difference between a demo and something an auditor can live with.

## Tools & Capabilities

| Tool | What it does | Records an event |
|---|---|---|
| `check_action` | Dry run of one action against the stored policies (no PII scan, records nothing) | No |
| `decide_action` | Records a real decision and returns it; obey finalDecision - REVIEW or BLOCK means do not run the action | Yes |
| `get_decision` | Reads one recorded decision; optional waitMs polls a REVIEW until ALLOW, BLOCK or the 30-second cap | No |
| `list_policies` | Lists policies as code, sorted by name (read-only) | No |
| `test_policies` | Evaluates up to 200 cases against proposed policies; nothing is saved | No |
| `plan_policy_changes` | Dry run of policy creates, updates and deletes (dryRun forced true; API key only) | No |
| `check_mcp_tool_call` | Decides a downstream MCP tool call and records it (API key only) | Yes |

`decide_action` and `check_mcp_tool_call` accept an `idempotencyKey`, so a retry returns the same event instead of double-recording.

## Installation

```json
{
  "mcpServers": {
    "vulnify": {
      "url": "https://mcp.vulnify.io/mcp"
    }
  }
}
```

Claude Code: `claude mcp add --transport http vulnify https://mcp.vulnify.io/mcp`. The client receives a 401, opens Sign in with Vulnify, and you choose the organization and scopes. An API key works instead, on every request, as `Authorization: Bearer vln_live_...` or `X-Vulnify-Key`.

## Configuration and Safety

- OAuth scopes map to tools: `decisions:read`, `decisions:write`, `policies:read`, `policies:test`. A missing scope returns a tool error that names the scope - that error is not an ALLOW.
- The server has no approve tool and no deny tool. A REVIEW is resolved by a person in the Vulnify app, so the approver and the agent are never the same session.
- `check_action` and `test_policies` record nothing (no security event, no audit entry). Use `decide_action` when the decision must be recorded.
- Test keys (`vln_test_`) store sandbox events that stay out of the main dashboards. API keys can carry an IP allowlist; calls through the hosted server come from its egress address, so an office-only allowlist needs the local `npx` process instead.

## Business Relevance

- **Operations and finance**: gate the agents that send email, touch invoices or move money; every action carries a recorded decision, and sensitive changes stop at a human REVIEW.
- **Compliance and security teams**: policies are code - list them, test up to 200 cases, and preview changes without applying them; the audit trail lives in one place rather than in scattered prompts.
- **Agent platform owners**: the same policy layer is available two ways, as this MCP server for assistants and IDEs, and as a gateway that sits in the production tool path and forwards allowed calls to registered upstream servers.

## Integration with CorpusIQ

The question "what is true in my business" and the question "what may the agent do next" are complementary halves of governed operations. Ask CorpusIQ for answers from your connected systems - orders, invoices, tickets, campaigns, with every number cited - and use Vulnify as the policy check in front of actions that follow. The data stays read-only on the CorpusIQ side; the action gate is explicit and auditable on the Vulnify side.

## Limitations

- The MCP server decides and records; enforcement depends on the agent or client obeying `finalDecision`. The separate gateway product is what sits inside the production tool path.
- Five tools are available in an OAuth session; `plan_policy_changes` and `check_mcp_tool_call` need an API key.
- `check_action` skips the PII scan and records nothing, so it is a preview, not an audit artifact.
- Requires a Vulnify account and organization; a personal free tier is not documented on the MCP page.

## FAQ

### Does the MCP server block actions by itself?

No. It returns the decision and, for `decide_action` and `check_mcp_tool_call`, records it. The agent is responsible for obeying REVIEW or BLOCK; the gateway product is the enforcing variant. The important part is that the decision exists outside the prompt, with an id and an audit entry.

### Can an agent approve its own REVIEW?

No. There is no approve tool. A REVIEW is resolved by a person in the Vulnify app, and `get_decision` only reads the outcome.

### What happens when a scope is missing?

The tool call returns an error naming the missing scope. Treat it as a failure, never as an ALLOW - the docs are explicit on this point.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
