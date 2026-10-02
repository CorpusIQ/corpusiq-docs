---
title: "SuperBooks MCP - Bookkeeping for Agents"
description: "Remote MCP over a SuperBooks ledger: transactions, invoices, customers, time tracking and reports for profit and loss, burn rate and runway."
category: Finance
stars: n/a (hosted platform, superbooks.io)
added: 2026-10-02
source: "mcpservers.org server page (docs-superbooks-io-mcp)"
relevance: ★★★
tags: [finance, accounting, bookkeeping, invoices, transactions, reports, burn-rate, runway, remote-mcp]
---

# SuperBooks MCP

**An accounting ledger behind one MCP endpoint.** SuperBooks exposes a team's books to agents: bank transactions, invoices, customers, time-tracking projects, documents, receipts and a reporting layer that answers revenue, profit and loss, burn rate, runway and spending questions. Access is scoped by credential, so a read-only key can read the books without any ability to change them.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (PKCE, dynamic client registration) or an API key
Endpoint: https://api.superbooks.io/mcp
Tools: 2 MCP tools (search_tools, execute_typescript) reaching 45 backend tools across 12 domains, plus list_teams
Rate limit: 120 requests per minute, per credential
Category: Finance
Built by: superbooks.io
```

## Why This Matters for Operators

Most finance MCP servers stop at one data source: a bank feed, an invoicing tool, or a reporting API. SuperBooks is the ledger itself, so an agent can read the same numbers the accountant sees and answer the questions a founder actually asks: what did we spend last month, who owes us money, what is the burn rate and how many months of runway does it buy.

The reporting surface is the operator-relevant part. The eight report tools cover revenue, profit and loss, burn rate, runway and spending, which are the numbers that drive hiring, pricing and fundraising decisions, and they sit next to the transaction and invoice records that produce them rather than in a separate analytics tool.

## Tool Surface

The endpoint uses a **Code Mode** design: a raw `tools/list` returns exactly two tools, `search_tools` and `execute_typescript`. An assistant calls `search_tools` to discover the operations its credential can reach, then writes and runs a short TypeScript program through `execute_typescript` that calls them. Each underlying tool still carries its own scope and authentication as if called directly. The 46 real tools (45 across 12 domains, plus `list_teams`) are reached this way.

| Domain | Tools | Destructive | Covers |
|---|---|---|---|
| transactions | 5 | 1 | Bank transactions, filtering, categorisation |
| invoices | 5 | 1 | Drafting, sending and voiding invoices |
| customers | 5 | 1 | The customer book |
| tracker | 5 | 1 | Time-tracking projects and entries |
| categories | 4 | 1 | Transaction categories |
| documents | 4 | 1 | Uploaded files and their contents |
| tags | 3 | 1 | Labels across customers, transactions, projects |
| inbox | 3 | 1 | Incoming receipts and bills, and matching them |
| reports | 8 | 0 | Revenue, profit and loss, burn rate, runway, spending |
| bank_accounts | 1 | 0 | Connected accounts |
| search | 1 | 0 | Cross-domain search |
| team | 1 | 0 | The current team's profile |

The eight destructive tools are the seven `*_delete` tools plus `invoices_void`, and they are gated twice: they need the `apis.all` scope and the **Destructive AI tools** setting switched on in the team the call names.

## Authentication

Two credential types, chosen by who the code runs for:

- **API key** - for code acting on behalf of your own team. Mint one in the app at Settings, Developer. Keys start with `sb_` and belong to a single team.
- **OAuth** - for products that other SuperBooks teams sign in to. Uses PKCE with dynamic client registration, so a remote MCP client such as Claude can sign a user in through the SuperBooks consent screen with nothing to copy or store.

Scope gates the tool surface: a read-only credential sees the read tier only, and destructive tools additionally need `apis.all` plus the per-team setting.

## Installation

Claude Code, with an API key:

```bash
claude mcp add --transport http superbooks https://api.superbooks.io/mcp \
  --header "Authorization: Bearer sb_your_api_key_here"
claude mcp list
```

Cursor, in `~/.cursor/mcp.json` or a project `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "superbooks": {
      "url": "https://api.superbooks.io/mcp",
      "headers": {
        "Authorization": "Bearer sb_your_api_key_here"
      }
    }
  }
}
```

Windsurf, in `~/.codeium/windsurf/mcp_config.json`, uses the same shape with a `serverUrl` key instead of `url`.

For OAuth clients such as Claude, add a custom connector pointing at `https://api.superbooks.io/mcp`; the client registers itself and sends the user to SuperBooks to choose teams and approve scopes.

## Multiple Teams

One connection can cover more than one team. On the OAuth consent screen the user chooses **All my teams** or specific teams. When a connection covers several teams, each tool that reads or changes a team's data takes an optional `teamId`:

- `list_teams` returns the teams the connection covers with each team's id, name and role.
- A call without `teamId` when several are covered is refused with `TEAM_REQUIRED`.
- A `teamId` outside the connection is refused with `TEAM_NOT_AVAILABLE`.
- Membership is re-checked on every request, so leaving a team stops the connection reaching it immediately.

An API key belongs to one team; its tools always work on that team.

## Business Relevance

- **Founders and finance leads** ask an agent for burn rate, runway and profit and loss without opening the accounting app
- **Bookkeepers** read transactions, receipts and unmatched inbox items, and draft or send invoices through the same surface
- **Agencies and consultancies** track billable time against customers and turn it into invoices
- **Operators connecting books to revenue data** get accounting figures an agent can cross-reference with payment and marketing data from other connectors

## Integration with CorpusIQ

Accounting numbers and revenue attribution answer different halves of the same question. A composed workflow: SuperBooks reports profit and loss, burn rate and runway from the ledger, and CorpusIQ supplies the revenue side from its Stripe, GA4 and ad-platform connectors, so an operator can see which channels are actually funding the runway rather than only what was collected. Both surfaces are reachable from one agent session, which keeps the spend question and the acquisition question together.

## Limitations

- The endpoint uses Code Mode, so a raw `tools/list` always shows two tools rather than the full set; the 46 underlying operations are reached through `search_tools` and `execute_typescript`
- Destructive tools are gated twice (scope plus a per-team setting), so a credential that can read may still fail on a delete until the team setting is enabled
- The rate limit of 120 requests per minute is per credential and counts MCP requests, not the individual tool calls inside an `execute_typescript` program
- The guide describes the documented tool surface; exact tool identifiers are discoverable at runtime through `search_tools`

## FAQ

### Do I need an API key or OAuth?

An API key if the code acts for your own team. OAuth if you are building something other SuperBooks teams sign in to.

### Why does my client show only two tools?

That is Code Mode by design. `search_tools` discovers the operations your credential can reach, and `execute_typescript` runs them.

### Can an agent write to the books?

It can reach destructive tools only if the credential carries the `apis.all` scope and the target team has **Destructive AI tools** switched on.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Median MCP - Read-Only Bookkeeping for Agents](/hermes/mcp/servers/external/median-mcp/)
- [Hourtick MCP - Time Tracking, Tasks and Billing for Teams and Agents](/hermes/mcp/servers/external/hourtick-mcp/)
- [Common Paper Contracts MCP - Agreement Workflow for Agents](/hermes/mcp/servers/external/common-paper-contracts-mcp/)
