---
title: "Conjointly MCP - Survey Research in Your Assistant"
description: "Read Conjointly experiments, reports and respondent data from any assistant; run analyses and exports, read-only by design."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-10-09
source: "mcpservers.org /all (October 9, 2026 evening sweep)"
relevance: ★★
tags: [survey-research, conjoint-analysis, market-research, respondent-data, analytics, oauth, read-only, remote-mcp]
---

# Conjointly MCP

**Official MCP server for Conjointly research data** - list your studies, read reports and analysis results, check respondent quality, start analyses and request exports from any assistant. Read-only by design: the server cannot create, change or delete experiments, reports, settings or respondent data.

```
Server type: Remote (Streamable HTTP at https://api.conjoint.ly/mcp)
Auth: OAuth sign-in with your Conjointly account (two-factor supported); no API token to copy
Tools: read tools (experiments, reports, respondents, account) plus start-work tools (run report analyses, request exports), which clients gate behind your approval
Safety: read-only; only analyses and exports are produced, nothing is modified or deleted
Category: Data & Analytics
Built by: Conjointly (conjointly.com; API docs at conjointly.com/api)
```

## Why This Matters for Operators

Pricing, packaging and product decisions are supposed to be tested with research, but the loop usually breaks at the interface: the study lives in one platform, the questions in another meeting, and by the time anyone opens the dashboard the decision has moved on.

Conjointly brings the research into the conversation. **"Show the attribute importances for my latest conjoint study" returns the analysis result; "which respondents look like low-quality responses" returns the quality signal** - the study, its numbers and its caveats available where the decision is being discussed. The read-only design keeps the research safe: assistants can look and analyze, not alter.

## Tools & Capabilities

| Area | What the assistant can read or start |
|---|---|
| Experiments | List and search experiments; read design, settings, sources, folders, sharing and the activity log |
| Reports | Report data, segments, pivot tables, weighting, waves, simulations and analysis results |
| Respondents | Search participants, read individual answers, URL variables and quality signals |
| Account | Team members, licence, balance, invoices, own audiences and predefined panels |
| Start work | Run report analyses (attribute importances, level preferences) and request exports (Excel, SPSS, conjoint utilities) behind client approval |

## Installation

```bash
claude mcp add --transport http conjointly https://api.conjoint.ly/mcp
```

The server is listed in Claude's connector directory (claude.ai/directory/conjointly); custom-connector steps for ChatGPT, Copilot Studio and Mistral Vibe are in the vendor docs. Sign in with your Conjointly account on first use; there is no token to copy.

## Configuration and Safety

- Every request goes through the same permission checks as the platform; the assistant sees only what you can see.
- Read tools run without prompts (marked read-only); analysis and export tools are marked as not read-only so clients ask for approval first.
- The server cannot create, change or delete experiments, reports, settings or respondent data.
- A team leader can disable MCP access for the whole team in Conjointly's team settings.

## Business Relevance

- **Product and pricing teams** pull conjoint results into the meeting where the pricing decision is actually made.
- **Research teams** answer "how is the study doing" without opening a dashboard, and monitor respondent quality with reasons.
- **Founders and operators** check the evidence behind a pricing or packaging claim before it goes into a deck.

## Integration with CorpusIQ

Research tells you what customers say they would do; CorpusIQ tells you what they actually do. Bring the conjoint findings in from Conjointly, then ask CorpusIQ for the real numbers - revenue and subscriptions from Stripe, orders from Shopify, pipeline from HubSpot - and compare stated preference against observed behavior in one thread.

## Limitations

- Requires a Conjointly account; the server reads that account's data only.
- New server, disclosed as such by the vendor, which also notes AI analysis can err and disclaims responsibility for AI-generated analyses.
- Gemini Enterprise is not supported yet (a Google-side OAuth limitation, per the vendor).
- Analysis and export actions may be approval-gated depending on the client; it is a read surface by design.

## FAQ

### Can the assistant change my experiments?

No. The MCP server is read-only: it can start analyses and request exports, but it cannot create, change or delete experiments, reports, settings or respondent data.

### Do I need an API token?

No. You sign in with your Conjointly account when you connect (two-factor supported); there is no token to copy.

### Which clients are supported?

Claude (web, desktop and Claude Code), ChatGPT in developer mode, Microsoft 365 Copilot through Copilot Studio, and Mistral Vibe; any client with remote MCP and OAuth sign-in works.

## See Also

- [Uxia MCP - AI User Testing and UX Research](/hermes/mcp/servers/external/uxia-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
