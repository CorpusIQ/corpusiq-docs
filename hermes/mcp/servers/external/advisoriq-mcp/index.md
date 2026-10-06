---
title: "AdvisorIQ MCP - Advisor CE and RIA Firm Data"
description: "Continuing education rules, deadlines and RIA firm data for US financial advisors, with official sources and citations on every answer, keyless."
category: Finance
stars: n/a (new listing)
added: 2026-10-06
source: "mcp.so feed (Oct 6, 2026 midday sweep)"
relevance: ★★
tags: [financial-advisors, compliance, continuing-education, ria, form-adv, finra, remote-mcp, keyless]
---

# AdvisorIQ MCP

**Remote MCP server (Streamable HTTP, read-only, no sign-in)** - continuing education rules and firm-level data for the US financial advice industry. AdvisorIQ tracks CE requirements across the major designations and state IAR rules, and publishes Form ADV data on every US registered investment adviser, with official sources and checked dates on every answer.

```
Server type: Remote (Streamable HTTP)
Auth: None (read-only, no sign-in)
Endpoint: https://mcp.advisoriq.com
Tools: CE rules, CE calculator, deadlines, webinars, RIA directory, rankings, market data
Pricing: Free to connect
Built by: AdvisorIQ (advisoriq.com)
Registry: via mcp.advisoriq.com
```

## Why This Matters for Operators

Compliance questions have an ugly failure mode: an AI assistant answers from memory, and memory is wrong about deadlines, state rules and credit hours. AdvisorIQ's server is built as a citation machine instead - every figure carries the official source and the date it was checked, and the tools refuse rather than guess when a rule is not confirmed.

The surface covers both sides of the industry: the rules advisors must satisfy (CFP, CIMA, CPWA, RMA, CIMC, CFA designations and state IAR CE, with a CE calculator and compliance deadlines) and the RIA market itself, from SEC Form ADV - firm search, a firm's full profile, national and state rankings, and market data on every registered investment adviser.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| CE requirements | Rules per designation and per state IAR program, with official sources and verified dates |
| CE calculator | Work out credit hours and gaps for a given situation |
| Deadlines | Compliance deadlines with checked dates |
| Education content | AdvisorIQ webinars, replays and research |
| RIA directory | Search US registered investment advisers, read one firm's profile from Form ADV |
| Rankings and market data | National and state rankings, market stats across the RIA universe |

## Installation

```bash
claude mcp add advisoriq --transport http https://mcp.advisoriq.com
```

No sign-in required. Any Streamable HTTP MCP client works.

## Configuration

```json
{
  "mcpServers": {
    "advisoriq": {
      "url": "https://mcp.advisoriq.com"
    }
  }
}
```

## Business Relevance

- **Advisors and compliance staff** check CE rules, deadlines and credit calculations with a citation instead of a search across four websites.
- **Firms** researching peers, competitors or acquisition targets read Form ADV profiles and rankings in the conversation.
- **Recruiters and consultants** in wealth management get firm-level market data on demand.
- **Anyone** preparing a licensing or registration question gets an answer that names its source and checked date.

## Integration with CorpusIQ

CorpusIQ reads the operator's own systems read-only; AdvisorIQ adds the regulatory and market layer around them. For advisory businesses, that means one conversation can hold both the firm's own numbers (from the connected stack) and the industry facts that surround them - who is registered, what rules apply, and what the rankings say - each with its source visible.

## Limitations

- US market only; the CE and Form ADV coverage does not extend to non-US regulators.
- Read-only: no filing, registration or submission actions.
- Refusals are deliberate - an error means the rule was not confirmed, not that the tool is broken.
- New listing: no track record in this catalog yet.

## FAQ

### Do I need an account?

No. AdvisorIQ's MCP server does not require authentication; connect with the endpoint URL directly.

### What is covered for continuing education?

CE rules for CFP, CIMA, CPWA, RMA, CIMC, CFA and state IAR CE, a CE calculator and compliance deadlines, each with the official source and checked date.

### Where does the firm data come from?

SEC Form ADV filings, surfaced as firm search, individual profiles, national and state rankings and market stats.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [X1 Wealth MCP - Cited Family Office Records](/hermes/mcp/servers/external/x1-wealth-mcp/)
- [Truthifi MCP - Verified Household Finance Records](/hermes/mcp/servers/external/truthifi-mcp/)
