---
title: Adrio MCP - Ad Research and Creative Angles
description: Remote MCP that lets an assistant search saved ads and swipe files, manage angles and audiences, and run Spark briefs for paid creative testing from inside a chat.
category: Marketing
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [marketing, advertising, creative-research, ads, angles, audiences, remote-mcp, oauth]
---

# Adrio MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the official Adrio server that brings paid-ad research and creative planning into an MCP client. Once connected, an assistant can search a team's saved ads and swipe files, work on angles and audiences, and run Spark briefs without leaving the conversation. OAuth sign-in uses an Adrio account; no API key is pasted into chat.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Adrio account)
Endpoint: https://api.adrio.ai/mcp
Tools: Brands and products, saved ads and swipe files, angles and audiences, jobs and Spark runs, plus create/edit for angles and audiences
Pricing: Adrio plan required
Category: Marketing
Built by: Adrio
```

## Why This Matters for Operators

Creative testing dies when research, angle selection and brief-writing live in three different tools. Adrio's mechanism is to **make the ad library and the creative workflow the assistant's context**: the agent reads the team's saved ads and swipe files, drafts angles and audiences against what has already been collected, and hands back Spark briefs ready to run.

For growth and marketing operators, that compresses the loop from "spend an afternoon in the ad library" to "ask, get angles grounded in our own swipe file, and ship a brief." The assistant works from the team's accumulated research rather than generic best-practice tips.

**The key advantage is a chat-native ad research and brief workflow wired to the team's own saved creative.</b>

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Look up | Brands, products, saved ads, swipe files, angles, audiences, jobs and Spark runs |
| Edit strategy | Create and edit angles and audiences from the conversation |
| Run briefs | Kick off Spark briefs for creative testing |

The Claude setup flow is two minutes: add a custom connector with the URL, sign in to Adrio and approve access. Team and Enterprise owners can add it once for the whole org.

## Installation

```bash
claude mcp add --transport http adrio https://api.adrio.ai/mcp
```

Vendor setup steps cover Claude Pro/Max and Claude Team/Enterprise separately.

## Configuration

```json
{
  "mcpServers": {
    "adrio": {
      "type": "http",
      "url": "https://api.adrio.ai/mcp"
    }
  }
}
```

OAuth opens the browser for Adrio sign-in on first connect. No API key is required.

## Business Relevance

- **Performance marketers** can pull saved ads and swipe files into a brief without tab-switching.
- **Creative strategists** can draft and iterate angles and audiences in the same thread they research in.
- **Agencies** can keep client swipe files and angles organised and searchable from any MCP client.
- **Growth leads** can turn collected ad research into Spark briefs on demand.
- **Founders running their own ads** get a lighter path to structured creative testing.

## Integration with CorpusIQ

Adrio pairs with CorpusIQ's analytics and publishing connectors. Where CorpusIQ's GA4 and Stripe connectors show which campaigns converted and what they earned, Adrio supplies the creative research behind the next test, so an assistant can close the loop from "our CAC rose last month" to "here are three angles from our swipe file worth testing."

A composed workflow: read campaign performance from a CorpusIQ GA4 connector, ask Adrio for angles and audiences grounded in the team's saved ads, then have the assistant assemble a test plan with projected spend. CorpusIQ reads the results; Adrio reads the creative that drives them.

## Limitations

- Requires an Adrio account and plan; not a free read surface.
- Ad-centric: no publishing or media-buying controls, only research and brief preparation.
- Hosted and proprietary; the server is operated by Adrio.
- Value depends on the team having saved ads and swipe files in Adrio already.
- Ad-platform coverage depends on Adrio's connected sources.

## FAQ

### Does Adrio MCP publish or buy ads?

No. It handles research, angles, audiences and briefs; it does not run campaigns.

### Do I need an API key for Adrio?

No. Connection is OAuth sign-in with an Adrio account.

### Can a whole team share one connection?

Yes. On Claude Team and Enterprise an owner adds the connector once and members connect to it.

### Who is Adrio for?

Performance marketers, creative strategists and agencies who research ads and write creative briefs.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
