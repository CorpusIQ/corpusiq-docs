---
title: seodraft MCP - Drafted SEO Content with Rule Checks
description: "seodraft's remote MCP server gives agents 37 tools for topic proposals, drafts, evidence-bank rules and delivery, with versioned writes."
category: SEO
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + seodraft.app"
relevance: ★★★
tags: [seo, content-drafting, serp-briefs, keyword-topics, evidence-bank, content-rules, oauth, remote-mcp]
---

# seodraft MCP

**One stateless endpoint where your agent drafts SEO content against your rules and your evidence.** seodraft publishes a remote MCP server at `https://seodraft.app/mcp` with 37 tools covering the profile, the evidence bank, topics, drafts, the rules engine, the calendar and delivery. Every call arrives as your workspace and reads and writes the same data the browser shows, so a post drafted in chat is already on the calendar when you open the app. A `get_skill` tool returns the exact pipeline the agent follows before drafting.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: OAuth via Clerk (discovery, DCR and PKCE from the endpoint)
Endpoint: https://seodraft.app/mcp
Tools: 37
Pricing: 7 days free, no card; then $5/month
Category: SEO / Content
Built by: seodraft (seodraft.app)
```

## Why This Matters for Operators

SEO drafting breaks down when the brief lives in one tab, the evidence in another and the house rules in someone's head. seodraft MCP puts all three into the agent's context: measured topics, SERP briefs, your evidence bank and the rules that check each draft. The agent proposes, drafts and runs the rules, and you approve.

Two engineering details matter for operator trust. Every post carries a version, and writes against stale versions are refused instead of overwriting edits. The server is stateless with no session ID, so a dropped connection has nothing to resume and the client simply sends the next request.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Profile | Read workspace profile and preferences |
| Topics | Propose measured topic clusters and SERP briefs |
| Evidence bank | Store and retrieve the sources and claims a draft must use |
| Rules | Run the rule checks that gate every draft |
| Drafts | Create and iterate posts with versioned writes |
| Calendar | Schedule and view publishing slots |
| Delivery | Export the finished file |

## Installation

```bash
claude mcp add --transport http seodraft https://seodraft.app/mcp
```

OAuth discovery, dynamic client registration and PKCE all start from the same address, so there is no client ID or API key to paste anywhere.

## Configuration

```json
{
  "mcpServers": {
    "seodraft": {
      "type": "http",
      "url": "https://seodraft.app/mcp"
    }
  }
}
```

First connect opens the Clerk sign-in; subsequent requests carry their own token.

## Business Relevance

- **SEO managers** get drafts that already pass the rules they set in the app
- **Agencies** can run many client workspaces through one endpoint
- **Solo operators** get a $5/month drafting assistant with a free trial week
- **Content teams** keep the approval step human while the assembly is agent-driven

## Integration with CorpusIQ

seodraft pairs with CorpusIQ's search_console connector: Search Console queries and impressions identify the topics worth drafting, seodraft turns them into rule-checked posts, and CorpusIQ recaps the publishing impact afterwards. Keyword and SERP context from the Semrush or Ahrefs connectors can seed seodraft's evidence bank so briefs are built on measured demand rather than guesses.

## Limitations

- Cloud-only remote server; no self-hosted option published
- Small paid plan after the trial week
- Rule and evidence quality still depends on what the operator configures
- New listing with a young user base

## FAQ

### What does the agent draft with seodraft?

Measured topics, SERP briefs and posts that run against the evidence bank and rules configured in the seodraft app.

### How are stale edits handled?

Every post carries a version; writes against old versions are refused instead of overwriting edits.

### What does it cost?

Seven days free with no card, then $5 per month.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
