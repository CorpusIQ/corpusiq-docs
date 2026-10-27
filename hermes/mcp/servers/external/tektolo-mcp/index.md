---
title: "Tektolo MCP - Rental Turnover and Deposit Settlement"
description: "Priced make-ready estimates and state-statute deposit settlement for US rental turnovers: deterministic engines with every rule cited."
category: Property Management
stars: n/a (new listing)
added: 2026-10-12
source: "chatmcp/mcpso issue #5189 (Oct 12, 2026 midday sweep)"
relevance: ★★
tags: [property-management, rentals, landlord, estimating, deposits, compliance, keyless, remote-mcp]
last_updated: "2026-10-24"
---

# Tektolo MCP

**Remote MCP server (Streamable HTTP, no account or API key)** - deterministic engines for the move-out side of US rental property: what a turnover costs, what to return from a security deposit under the state statute, and whether a deposit came back on time.

```
Server type: Remote (Streamable HTTP)
Auth: None required; an optional free personal key is available from tektolo.com/connect-your-ai
Endpoint: https://tektolo.com/mcp/rental-property
Tools: 5 (turnover estimates, issue codes, deposit settlement, settlement rules)
Pricing: Free to try (50 estimates a day on the web); the MCP endpoint is free keyless
Built by: Tektolo (tektolo.com; repo github.com/tektolo/skills)
Listing: chatmcp/mcpso issue #5189 (Oct 12, 2026)
```

## Why This Matters for Operators

Move-out math is where landlords and small property managers lose money quietly. A turnover estimate assembled from memory is either padded, and the owner overpays, or thin, and the difference shows up later as a callback. A deposit settlement assembled from general knowledge misses the state statute, and a mistaken deduction is a claim waiting to happen.

Tektolo keeps the rules where the numbers are: the same engines that run on the web run over MCP, deterministic, with every rule cited back to its source. An agent can price a standard turn, scope it as work items, look up the issue codes behind the estimate, settle a deposit under the state's rules and check the statute's deadline for returning it.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| property_turnover_quick_estimate | A vendor-ready turnover cost estimate for a unit |
| property_turnover_scope | Scope a turnover as work items rather than a single number |
| property_turnover_issue_codes | The issue codes the turnover estimates are built on |
| deposit_settlement_settle | Settle a security deposit under the state's rules |
| deposit_settlement_rules | The deposit rules themselves, for the state in question |

## Installation

```
claude mcp add tektolo --transport http https://tektolo.com/mcp/rental-property
```

Any MCP client that supports remote Streamable HTTP servers can add the same URL. No sign-in, no account, no key. An optional free personal key from tektolo.com/connect-your-ai is available for regular use.

## Configuration

```json
{
  "mcpServers": {
    "tektolo": {
      "type": "http",
      "url": "https://tektolo.com/mcp/rental-property"
    }
  }
}
```

## Business Relevance

- **Landlords and small property managers** price turns and settle deposits without assembling the statutes by hand
- **Maintenance and make-ready vendors** get the same estimate the owner runs, on the same rules
- **Bookkeepers and property accountants** keep settlements tied to the cited statute
- **Agents and advisors working with rental portfolios** answer move-out questions from a deterministic engine rather than a guess

## Integration with CorpusIQ

Tektolo covers the rental-operations layer: turnover economics and deposit compliance. CorpusIQ answers the surrounding business question from connected sources such as Gmail, Sheets and accounting, so a deposit or turnover discussion that starts in email can pull the statutory math alongside it.

Used together: ask CorpusIQ for the portfolio view (rent roll, expenses, communication history) and ask Tektolo for the settlement view (what to return, under which rule, inside which deadline). Tektolo stays the source of record for the settlement math; CorpusIQ remains the place the rest of the question is answered alongside.

## Limitations

- Rental property is the one area of work so far: three web tools and five MCP tools
- United States coverage, tracked per state statute
- v0.1.0, brand new, no track record yet
- Estimates and settlements are operational tools, not legal advice; verify against the cited rule before withholding anything disputed

## FAQ

### Is it really keyless?

Yes. The endpoint answers without an account or API key; the optional personal key from the vendor is for regular use. A plain `tools/list` returns all five tools with no credentials.

### What exactly does it cover?

Turnover economics (a quick estimate, scoped work items and the issue codes behind them) and deposit settlement (the settlement itself plus the statute rules it applies).

### Where do the numbers come from?

Each tool is a deterministic engine rather than a model guess, and every rule is cited. The vendor counts 459 cited sources across the rental-property tools.

### What does it cost?

The web tier is free to try at 50 estimates a day, and the MCP endpoint is free keyless.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
