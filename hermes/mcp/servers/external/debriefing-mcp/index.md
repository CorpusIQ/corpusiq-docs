---
title: "Debriefing MCP - Competitor Moves with Evidence"
description: "B2B competitive intelligence over MCP: tracked competitors, evidence-backed signals, digests and battlecards, worked on from any AI client."
category: Competitive Intelligence
stars: n/a (hosted platform, debriefing.io)
added: 2026-10-05
source: "chatmcp/mcpso issues (#4779)"
relevance: ★★
tags: [competitive-intelligence, b2b, signals, battlecards, sales, oauth, registry, remote-mcp]
---

# Debriefing MCP

**Competitor moves, each with the receipt.** Debriefing watches the competitors a B2B team nominates, finds their moves (a price change, a launch, a new hire), and backs every signal with the source evidence. Its MCP server lets Claude, ChatGPT or any other client work a Debriefing workspace directly: read the dossiers and signals, pull the latest digest, prep a sales battlecard, and annotate what the team learns. The exact catalog of every move stays in one place; the AI conversation becomes the place you ask about it.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (PKCE, dynamic client registration) or a dbk_ API key; public tools need none
Endpoint: https://debriefing.io/mcp
Tools: 41 across public, read, write and spend scopes
Pricing: A paid plan is required for workspace features; free tools and brief requests available
Registry: io.debriefing/debriefing
Built by: Debriefing
```

## Why This Matters for Operators

Competitive intelligence usually dies in a spreadsheet nobody reads. Debriefing's model is monitoring first: you name the competitors and the pages that matter (pricing pages included), it runs monitoring cycles, and the findings arrive as dated signals with sources. The MCP layer is what makes it usable in the tools people already work in: a founder asks "what changed this week", a seller asks for the battlecard before a call, a marketer pulls the evidence behind a pricing change and drafts the positioning response.

**Every claim carries its source.** `get_evidence` returns each source excerpt with its URL and date, so a signal is never just an assertion. And permissions are explicit: the connection asks for `read`, `write` and `spend` scopes separately, each tool checks role and plan, and a refusal links directly to the fix.

## Tools

Four public tools work with no account; the workspace surface adds read, write and spend groups:

| Public tool | What it does |
|---|---|
| `search_public_briefs` | Search the competitive briefs Debriefing publishes about named companies, newest first |
| `get_public_brief` | One brief: summary, dated findings and numbered public sources |
| `search_guides` | Searches the public CI library: guides, glossary, comparisons, company profiles |
| `get_free_brief_link` | Links to request a free brief or compare plans; sends nothing |

| Read tool | What it does |
|---|---|
| `get_workspace` | The workspace, your role, the connection's scopes and plan |
| `get_plan_and_limits` | Plan limits: competitor slots, research allowance, daily caps, cadences |
| `list_competitors` | Tracked competitors with ids for the other tools |
| `get_competitor` | One dossier: company facts, risk and opportunity, stored reads |
| `search_signals` | Open signals, newest first, filterable by competitor, severity, text or time |
| `list_digests`, `get_digest` | Digests that sum up moves over a period, by id or the newest |
| `list_battlecards`, `get_battlecard` | Talk tracks for sales calls against each competitor |
| `get_evidence` | The source excerpts behind one signal |
| `get_company_profile` | Your own profile: positioning lists and the ideal customer profile every move is read against |
| `get_delivery_settings`, `list_members` | Monitoring cadence and delivery channels; who is in the workspace |
| `what_changed` | Everything new since a time: signals, digests, battlecards |

Write tools cover adding and renaming competitors, monitored pages, pins, saved signals, notes, ratings, share links, invitations, cadence and delivery settings. Spend tools use plan allowances: `research_competitor`, `refresh_watchlist`, `generate_battlecard`, `update_icp` and `draft_positioning`.

## Installation

Claude Code:

```bash
claude mcp add --transport http debriefing https://debriefing.io/mcp
```

JSON clients:

```json
{
  "mcpServers": {
    "debriefing": { "url": "https://debriefing.io/mcp" }
  }
}
```

Claude (web and desktop): Settings, Connectors, Add custom connector, paste the URL. ChatGPT adds it as a connector in developer mode. For non-OAuth clients, create a `dbk_` key in Organization settings under Integrations and send it as `Authorization: Bearer` or `X-API-Key`.

## Business Relevance

- **Founders and PMM teams** track pricing, launches and positioning changes with evidence attached, ready to reuse in posts, pages and investor updates.
- **Sales teams** pull a fresh battlecard per competitor before a call, and add back what they learn from the field.
- **Agencies and consultants** run a client's competitive watch from the same workspace the client reviews, with share links to individual signals.
- **Anyone with Slack** can have finished monitoring cycles delivered by email and Slack; the MCP side then answers follow-ups.

## Integration with CorpusIQ

Debriefing is the outside view; CorpusIQ is the inside view. CorpusIQ answers what happened in your systems: revenue movement in Stripe, pipeline in the CRM, traffic in GA4. Debriefing answers what changed out in the market: a competitor's price cut, a launch, a new page. Put together, "our pricing page changed and so did theirs" questions have both halves in the same conversation, each from a read-only source. CorpusIQ never leaves your systems, Debriefing never touches them; the composition is in the answer, not the plumbing.

## Limitations

- A paid plan is required for workspace features; free workspaces get public tools and brief request links only.
- Monitoring cadence, competitor slots and battlecard generation are plan-limited, and spend tools draw from weekly and daily allowances.
- Public brief tools only read what Debriefing publishes on debriefing.io, not arbitrary competitors.
- The service is proprietary (the listing repo is MIT, the service is not); no self-hosting.
- Slack delivery needs a paid plan and a Slack connection made in the app.

## FAQ

### Do I need an account to use it?

No for the four public tools (`search_public_briefs`, `get_public_brief`, `search_guides`, `get_free_brief_link`). Workspace tools need a Debriefing account, and a paid plan for most write and spend actions.

### How is a signal verified?

Every signal links to source excerpts with URLs and dates. `get_evidence` returns them per signal, and briefs number their public sources.

### Which scopes does the connection ask for?

Three, separately: `read` (always), `write` (changes that cost nothing) and `spend` (actions that use a plan allowance). You can grant less and add later.

### Can it send things or move data out?

Share links are public pages for one signal, created by explicit tool calls. Nothing else leaves the workspace, and the assistant sends nothing on its own.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Signal Six MCP - Cited Competitive Intelligence](/hermes/mcp/servers/external/signal-six-mcp/)
- [Klarix Intelligence Engine MCP - B2B Competitive Intelligence](/hermes/mcp/servers/external/klarix-intelligence-engine-mcp/)
