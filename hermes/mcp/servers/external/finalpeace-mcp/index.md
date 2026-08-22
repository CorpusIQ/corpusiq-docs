---
title: "FinalPeace MCP - US Estate Document Requirements for Agents"
description: "MCP server for FinalPeace, an end-of-life planning platform: look up statute-cited document execution requirements for all 50 US states, get a 27-step after-a-loss checklist ordered by urgency, and run an estate-planning gap assessment. Anonymous free tier, OAuth 2.1 member tier."
category: IP/Legal
stars: n/a (new listing)
added: 2026-08-22
source: "mcp.so GitHub issue #3681"
relevance: ★★
tags: [estate-planning, legal, wills, trusts, power-of-attorney, compliance, end-of-life]
---

# FinalPeace MCP

**Statute-cited US estate document requirements from an MCP client - 50-state execution rules, an urgency-ordered after-a-loss checklist and a planning-gap assessment, free without an account.** FinalPeace exposes end-of-life planning reference data as a remote Streamable HTTP server: an agent can ask what a specific state legally requires to execute a will, financial power of attorney or health care proxy, walk someone through the first steps after a death, and score how complete an estate plan is. Three tools work anonymously with no key; an optional OAuth 2.1 member tier unlocks personal vault contents.

```
Server type: Remote (Streamable HTTP)
Auth: None for the 3 public tools; OAuth 2.1 (dynamic client registration) for member tools
Endpoint: https://mcp.finalpeace.co/mcp
Registry: co.finalpeace/estate-planning
Tools: 4 (state requirements, after-loss checklist, gap assessment, account connect)
Pricing: Free anonymous tier; member tier via FinalPeace account
Built by: FinalPeace (finalpeace.co); repo github.com/adamblazer18/finalpeace-mcp
```

## Why This Matters for Operators

Estate execution rules change state by state and the answers sit in statute text most people never read. **FinalPeace turns that lookup into a one-line tool call** with the statute citation attached, so every legal answer carries its source and a verification date instead of a guess. For operators this matters twice: as individuals who hold wills, POAs and health care directives, and as businesses (legal, wealth, insurance, elder-care, HR benefits) whose customers ask "what does my state require?" on a daily basis.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `find_state_document_requirements` | What a specific US state legally requires to execute a will, financial power of attorney or health care proxy (witness counts, notarization, who is barred from witnessing) |
| `get_after_loss_first_steps` | 27-step checklist of what has to happen after someone dies, ordered by when it actually matters |
| `assess_estate_planning_gaps` | Scores how prepared someone's end-of-life planning is and ranks what is missing by consequence |
| `connect_finalpeace_account` | Explains the OAuth flow to connect an account for member tools (vault contents, personal checklist progress) |

All three public tools are verified live (server v2.0.0) and return reference-not-legal-advice disclaimers with every response.

## Installation

Remote HTTP server - add it directly to your MCP client, no API key needed for the public tools:

```json
{
  "mcpServers": {
    "finalpeace": {
      "type": "http",
      "url": "https://mcp.finalpeace.co/mcp"
    }
  }
}
```

Or ask it as a one-off: "What does Texas require for a will to be valid?" The member tier adds OAuth 2.1 with dynamic client registration through the FinalPeace app.

## Configuration

No configuration for the anonymous tier. To use member tools (personal vault, checklist progress), connect a FinalPeace account via the OAuth flow explained by `connect_finalpeace_account`. Every legal answer includes statute citations and a verification date (statutory sources re-verified August 2026).

## Business Relevance

- **Legal and wealth firms** answer client state-requirement questions with cited sources instead of research time
- **Insurance and benefits teams** guide beneficiaries through the after-loss checklist step by step
- **Elder-care and family services** run gap assessments before recommending an estate attorney
- **Any operator** keeps their own will, POA and health care directive compliant with their state's execution rules

## Integration with CorpusIQ

FinalPeace supplies the legal reference layer; CorpusIQ supplies the business context around it. A composed workflow has FinalPeace pull a state's execution requirements while CorpusIQ reads the client relationship from the CRM, the billable history from QuickBooks and the contract status from HubSpot, so a wealth advisor drafts a compliance checklist with the actual account state in the same session. Estate-planning engagements surfaced by the gap assessment can be tracked as deals in the CorpusIQ CRM connectors.

## Limitations

- US only - no international estate law coverage
- Reference and guidance, not legal advice (stated in every response)
- Member tier tools require a FinalPeace account connection
- New listing (Aug 2026); single vendor, young repository
- No drafting tools - it tells you requirements, it does not generate the documents

## See Also

- [Goalie Trademark Search MCP](/hermes/mcp/servers/external/goalie-trademark-search-mcp/)
- [Legalcode MCP](/hermes/mcp/servers/external/legalcode-mcp/)
- [Taiwan Law MCP](/hermes/mcp/servers/external/taiwan-law-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
