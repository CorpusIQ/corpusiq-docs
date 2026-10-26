---
title: ZenSched MCP - Field Workforce Scheduling for Agents
description: Field workforce scheduling over MCP - account creation, verified GPS punches, worker invites, shifts, forms, webhooks and timesheets with no human dashboard required.
category: ERP
stars: n/a (new listing)
added: 2026-09-02
source: mcp.so
relevance: ★★
tags: [workforce, scheduling, field-operations, gps, timesheets, remote-mcp]
last_updated: "2026-10-19"
---

# ZenSched MCP

**Remote MCP server (Streamable HTTP, no authentication to connect)** - field workforce scheduling built agent-first by ZenShows LLC. Eleven tools cover account creation, verified GPS punches, worker invites, shifts, forms, webhooks and timesheets, with no human dashboard required. The account lifecycle itself is agent-native: create an org without email, recover keys with emailed codes, and reconnect without rotating credentials.

```
Server type: Remote (Streamable HTTP)
Auth: None to connect; per-org zsc_ API key for org operations
Endpoint: https://mcp.zensched.com/mcp
Tools: 11 (account lifecycle, scheduling, punches, forms, webhooks, timesheets)
Pricing: Free to connect; org plans at zensched.com
Category: ERP
Built by: ZenShows LLC
```

## Why This Matters for Operators

Field scheduling tools are built for human dispatchers, which makes them awkward for agent-driven operations. ZenSched flips the assumption: the agent is the dispatcher. An MCP client can stand up an org, invite workers, publish shifts and collect verified GPS punches and timesheets without a human clicking through a scheduler.

The account flow shows the agent-first design. **`account_create` returns an org and API key immediately with no email and no OTP, and every recovery path - signin, key rotation, full key revocation - is a two-step emailed-code flow the agent can drive itself.** A feedback tool works even before an account exists, and a human reads every submission.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `zensched_guide` | The agent guide: connect, fund, locations, workers, shifts, timesheets |
| `feedback_submit` | File a grievance or product recommendation, free, before account creation |
| `account_create` | Create an org without email; returns org id plus zsc_ key immediately |
| `account_signup_start` / `account_signup_verify` | Two-step email-verified org creation |
| `account_recover_start` / `account_recover_verify` | Key recovery with emailed code; revokes all previous keys |
| `account_signin_start` / `account_signin_verify` | Reconnect an existing org without rotating keys |
| `account_use_key` | Authenticate with an existing zsc_ API key |
| `account_auth_status` | Check connector sign-in state before org calls |

Beyond the account surface, org tools handle locations, workers, shifts, forms, webhooks and timesheets.

## Installation

```bash
claude mcp add zensched --transport http https://mcp.zensched.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "zensched": {
      "type": "http",
      "url": "https://mcp.zensched.com/mcp"
    }
  }
}
```

Connect with no authentication; the org tools authenticate with the zsc_ API key issued at account creation.

## Business Relevance

- **Field-service operators** run scheduling, punches and timesheets from an agent instead of a dispatcher console
- **Franchises** stand up a scheduling org per location without email-based setup flows
- **Staffing teams** get verified GPS punches as structured data instead of honor-system clock-ins
- **Platform builders** embed workforce scheduling into agent workflows via webhooks

## Integration with CorpusIQ

ZenSched produces the workforce data that CorpusIQ's business connectors put in context. An agent running both can pull timesheet totals and verified punches from ZenSched, join them against payroll runs and labour cost in QuickBooks via CorpusIQ, and flag sites where labour spend diverges from scheduled hours. For a multi-site operator the composed workflow is a weekly cost control loop: schedule in ZenSched, pay in QuickBooks, reconcile through one agent.

## Limitations

- Brand new listing with no track record yet
- Listing documents the account-surface tools in detail; org tools are documented in the platform guide
- Scheduling depth (optimization, shift swapping) is not yet visible from the published surface
- US-oriented field-operations tooling; check payroll and compliance fit per state
