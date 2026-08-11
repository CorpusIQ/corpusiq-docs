---
title: "FLINT Network MCP — Agent identity and authority verification before transactions"
description: "Verify an AI agent's identity, integrity, and authority before it moves money. FLINT's MCP server exposes the verify-before-pay loop — issue passports, authorize actions, verify at transaction time, and record outcomes. Remote Streamable HTTP."
category: mcp
tags: [mcp-server, agent-identity, fraud-prevention, financial-transactions, agent-commerce, verification]
source: mcp.so
discovered: 2026-08-11
stars: 0
author: FLINT Network (thefraudfather)
github: https://github.com/thefraudfather/flint-plugin
mcp_endpoint: https://flint.network/mcp
transport: Streamable HTTP
auth: None required to start (free verification)
---

# FLINT Network MCP Server

**Know Your Agent at transaction time.** Verify an AI agent's integrity and authority with FLINT before it moves money, and keep a signed record of what was checked. FLINT is the neutral verification network for AI agents that transact — it does not issue agents and it does not move money. It verifies, at the moment value moves, that the specific agent asking to pay is who it claims to be, is within its granted authority, and has not been compromised.

## Why It Matters for Operators

As AI agents are handed spending authority across stablecoin and card rails, the fraud and identity stack built for humans (device, session, KYC) doesn't apply. An agent transacting directly against an API has none of that. For business operators who:

- Deploy AI agents with spending authority
- Accept payments from AI agents
- Build agent-to-agent commerce systems
- Need an audit trail for agent transactions

FLINT provides the missing verification layer:

- *"Before my agent pays this invoice, verify the recipient agent is authorized"*
- *"At transaction time, confirm the paying agent hasn't been compromised since authorization"*
- *"Keep a signed record of every agent verification for our compliance audit"*
- *"Issue an agent passport so counterparties can verify our agent before transacting"*

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (remote — nothing to run locally) |
| **Auth** | None required to start |
| **Endpoint** | `https://flint.network/mcp` |
| **Tools** | `issue_agent_passport`, `issue_authorization_record`, `verify_agent_authority`, `submit_transaction_outcome` |
| **Verdict model** | Four-state: **allow**, **step-up**, **review**, or **block** |
| **Passport** | Free, hybrid-signed, returns a public verifiable URL |
| **Records** | Signed verification records kept as evidence by counterparty |
| **License** | MIT |

## Setup

### Claude Code / Cowork (plugin install)

```
/plugin marketplace add thefraudfather/flint-plugin
/plugin install flint@flint-network
```

This installs both the remote MCP connector and the `verify-agent-integrity` skill.

### Any MCP Client (connector only)

```json
{
  "mcpServers": {
    "flint": {
      "type": "streamable-http",
      "url": "https://flint.network/mcp"
    }
  }
}
```

Connect from [flint.network/connect](https://flint.network/connect).

## The Verify-Before-Pay Loop

FLINT's workflow runs a four-step loop — call the tools directly or use the bundled `verify-agent-integrity` skill:

| Step | Tool | What It Does |
|------|------|-------------|
| **1. Issue** | `issue_agent_passport` | Create a verifiable identity for your agent. Free, hybrid-signed, returns a public URL. Agent name or ID is enough. |
| **2. Authorize** | `issue_authorization_record` | Bind the agent to a specific action scope — what it can spend, how much, to whom — before any money moves. |
| **3. Verify** | `verify_agent_authority` | At transaction moment, confirm the agent is still authorized and uncompromised. Returns four-state verdict: allow, step-up, review, or block. |
| **4. Record** | `submit_transaction_outcome` | After the transaction completes (or is disputed/reviewed), submit the outcome. Feeds the cross-merchant reputation signal and creates a retained record. |

## For Business Operators

FLINT addresses a problem most operators haven't encountered yet but will: **agent counterparty risk.** When your AI agent is authorized to spend $5,000/month on cloud infrastructure, how does AWS know it's really your agent and not a compromised clone? When an AI procurement agent places a $50,000 order with a supplier, how does the supplier verify the agent's authority?

The existing fraud stack (device fingerprinting, session cookies, human KYC) was never designed for agent-to-agent transactions. FLINT builds the verification layer specifically for this world — neutral, signed, verifiable, and free to start.

**For operators building agent infrastructure:** FLINT's MCP server can be integrated into any agent workflow that involves spending authority. The four-step loop (issue → authorize → verify → record) creates an audit trail suitable for compliance and dispute resolution.

**Current state:** Early stage (0 stars, 7 commits, last updated June 2026). The concept is sound but the network effects aren't there yet. Worth tracking for operators building agent payment infrastructure.

---

*MIT License. Built by [FLINT Network](https://flint.network). GitHub: [thefraudfather/flint-plugin](https://github.com/thefraudfather/flint-plugin)*
