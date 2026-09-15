---
title: Accordio MCP - Back Office Time, Billing and Invoicing for Agents
description: Accordio gives AI assistants a back office through one MCP URL. Twenty-eight tools cover time tracking, clients, projects, unbilled hours, invoices, contracts, proposals, tasks, expenses and calendar. Tracking is free forever, with a paid tier for invoice and proposal drafting.
category: Productivity
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [time-tracking, invoicing, proposals, contracts, expenses, back-office, oauth, remote-mcp]
---

# Accordio MCP

**Remote MCP server (Streamable HTTP, scoped OAuth)** - the back office Claude was missing. One MCP URL and 28 tools give an assistant real figures from tracked time, clients, unbilled hours, invoices, contracts, proposals, tasks, expenses and calendar. The assistant drafts; the operator sends.

```
Server type: Remote (Streamable HTTP)
Auth: Scoped OAuth, approved by the account owner, revocable in settings
Endpoint: https://mcp.accordio.ai/mcp
Tools: 28 (26 free, 2 on the Legend plan)
Pricing: Free forever for tracking · Legend $39/mo ($29/mo billed yearly) for drafting
Category: Productivity
Built by: Accordio (independent, not affiliated with Anthropic)
```

## Why This Matters for Operators

Solopreneurs and small studios bill from memory: hours scattered across a tracker, clients in a spreadsheet, invoices typed by hand. Accordio removes the glue work by giving the assistant direct reads on what actually happened. **Tracked hours become an invoice draft in one prompt, and every draft opens in Accordio for the human to check the numbers and press send.**

The security model is deliberately narrow. There is no send, sign, delete or payment verb on the connector at all: an assistant can never send an invoice, sign a contract, delete anything or move money. The Mac time tracker that feeds real hours into the system is open source, so the capture engine is reviewable before install.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_time_summary` | What was worked, by day, week or month, grouped by client, project or category |
| `get_current_activity` | What is being tracked right now and for how long |
| `start_timer` / `stop_timer` | Start or stop a timer against the right client |
| `log_time_entry` | Log a forgotten hour on the day it happened |
| `list_time_entries` / `update_time_entry` | List and fix or reassign individual entries |
| `list_clients_projects` | List clients and projects for correct attribution |
| `create_client` / `create_project` | Create a client or project from what the assistant already knows |
| `get_unbilled_time` | Hours worked but not billed, in money |
| `get_business_snapshot` | Open invoices, live projects and what is coming up |
| `get_setup_status` | What is connected and what is missing |
| `list_invoices` / `list_contracts` / `list_proposals` | Invoice, contract and proposal status in each currency |
| `list_tasks` / `create_task` / `complete_task` | Task list with priority ordering |
| `get_expense_summary` / `log_expense` | Expense totals by category and one-prompt filing |
| `check_calendar` / `check_availability` / `create_event` | Read the calendar, find gaps, add events |
| `list_booking_links` | Hand out booking links on the operator's terms |
| `draft_invoice_from_time` (Legend) | Turn unbilled hours into a priced invoice draft |
| `draft_proposal` / `draft_contract` (Legend) | Draft a proposal or contract from a brief in your own templates |

## Installation

```bash
claude mcp add --transport http accordio https://mcp.accordio.ai/mcp
```

The automatic time tracker is Mac-only and installs with `brew install --cask accordio-ai/tap/accordio`. Without it, timers and manual hour logging still work. Claude Code and Codex can set up connector plus tracker from a single pasted prompt.

## Configuration

```json
{
  "mcpServers": {
    "accordio": {
      "url": "https://mcp.accordio.ai/mcp"
    }
  }
}
```

Auth notes: scoped OAuth with an exact list of approved tools shown before consent; revoke anytime in Accordio settings. No API keys to copy. ChatGPT works through developer mode on any paid plan.

## Business Relevance

- **Freelancers and solo operators** turn tracked time into invoiced revenue without spreadsheet glue.
- **Small studios** keep clients, projects and unbilled hours attributed correctly from one conversation.
- **Proposal-driven shops** draft proposals and contracts from a brief in their own templates, then review before sending.
- **Calendar-heavy operators** hand out booking links and find gaps without opening a scheduler.

## Integration with CorpusIQ

Accordio is the execution layer under CorpusIQ's reporting layer. An operator asks for the business snapshot (Accordio: open invoices, unbilled hours, live projects), then pulls Stripe collections and QuickBooks records through CorpusIQ to reconcile the two views in one conversation. CorpusIQ reads the money that already moved; Accordio reads the work and drafts the next invoice from it.

## Limitations

- No send, sign, delete or payment verb exists on the connector by design; drafts always route through the Accordio app.
- Automatic tracking is Mac-only today; other platforms log hours manually.
- Invoice, proposal and contract drafting sits behind the $39/mo Legend plan.
- Brand new listing on the directories; no public track record yet.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [TheLuckyStrike Ops Suite - Invoicing, Time Tracking and Spreadsheets](/docs/hermes/mcp/servers/external/theluckystrike-mcp-suite)
- [Watchgoose MCP - Cron Monitoring and Failure Forensics for Agents](/docs/hermes/mcp/servers/external/watchgoose-mcp)
