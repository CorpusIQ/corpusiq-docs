---
title: "Genchi MCP - Project Deadline Risk from Team Votes"
description: "Anonymous one-click confidence votes from engineers via Slack become portfolio-level project risk scores, trends and blockers, readable from any MCP assistant."
category: Project Management
stars: n/a (hosted platform, genchi.com)
added: 2026-09-30
source: "mcp.so server page (genchi)"
relevance: ★★★
tags: [project-management, engineering-leadership, deadline-risk, team-signals, slack, oauth, remote-mcp]
---

# Genchi MCP

**Project deadline risk read from the people doing the work.** Genchi shows engineering leaders a prediction of which projects are heading for a missed deadline and which are not, sourced from an anonymous one-click confidence vote each engineer gives in response to a regular, automated Slack prompt. Votes are combined by project into a single score and tracked over time, so leaders can spot trouble sooner and, more usefully, know which teams to leave alone. The MCP connector renders the portfolio, confidence trends and blockers as interactive views in chat.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (sign in with Genchi account)
Endpoint: https://genchi.com/api/mcp
Tools: 6 (portfolio, confidence, blockers, weekly summary, create initiative, Slack status)
Pricing: free for teams up to 10; 2-week free trial above
Category: Project Management
Built by: genchi.com
```

## Why This Matters for Operators

Status reporting is a tax on both sides: engineers write updates nobody reads closely and leads still get surprised by a slipped deadline. Genchi replaces the written status with a one-click anonymous vote, aggregated per project. The signal an operator actually needs is not "is this project fine" but "which projects should I be worried about this week" and "where is confidence dropping week over week": both are answerable straight from the agent.

The privacy design is deliberate: no tool ever returns a name alongside a confidence vote, individual values are shuffled on every response, each user sees only the projects they are part of, and any user (or their admin) can revoke a connection at any time.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| List initiatives | Renders the portfolio, or a tree of one project and everything under it |
| Get confidence | Confidence score and its trend for one project, with the confidence chart |
| Get blockers | Current blockers, and who raised them |
| Get weekly summary | What changed this week |
| Create initiative | Set up a new project |
| Slack connection status | Whether Slack is connected, and how to finish setup |

Example questions the server answers: "Which of my projects should I be worried about this week?", "How is the payments migration tracking?", "Where is confidence dropping week over week?", "What's blocking the platform rebuild, and who raised it?"

## Installation

```
Connector URL: https://genchi.com/api/mcp
```

Add the connector URL to your assistant, then sign in with your Genchi email and password over OAuth. Works in Claude, ChatGPT, Grok and any MCP-compatible assistant.

## Configuration

```json
{
  "mcpServers": {
    "genchi": {
      "type": "http",
      "url": "https://genchi.com/api/mcp"
    }
  }
}
```

Each user connects their own account and sees only the projects they own, work on or observe.

## Business Relevance

- **Engineering leaders** get a portfolio verdict on deadline risk without chasing written updates
- **Program managers** track confidence trends across a program tree and catch week-over-week drops
- **Delivery and ops leads** see blockers and who raised them in the same view as the risk score
- **Team members** spend less time on status reporting and get visibility into how dependencies are tracking

## Integration with CorpusIQ

Team signals pair with delivery numbers. A composed workflow: Genchi reports that confidence is dropping on the payments migration, and CorpusIQ supplies the live support volume, churn or revenue context from its Zendesk, Stripe and GA4 connectors, so a delivery risk and its business impact are read in the same session. For operators running both, the engineering-risk question and the business-impact question sit together.

## Limitations

- Requires a Genchi account; the connector is not usable anonymously
- Free tier is capped at teams of up to 10, with a 2-week trial above that
- The score depends on Slack prompts being answered; a quiet team produces a thin signal
- Vote values are intentionally never attributable to a name, so individual-level drill-down is not available by design

## FAQ

### Can I see which engineer voted low?

No. No tool returns a name alongside a confidence vote, and individual values are shuffled on every response.

### Does it need Slack?

Yes. Votes are collected through an automated Slack prompt, so a Slack connection is part of setup.

### Does it work outside Claude?

Yes. It works in Claude, ChatGPT, Grok and any other MCP-compatible assistant.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Structured Project Memory MCP - Project Context for Agents](/hermes/mcp/servers/external/spm-structured-project-memory/)
- [Coding Agent PM MCP - Project Management for Coding Agents](/hermes/mcp/servers/external/coding-agent-pm-mcp/)
