---
title: "SalesTouch MCP: LinkedIn GTM Prospecting for AI Agents"
description: "AI-native GTM prospecting platform exposing LinkedIn research, qualification, conversation, outreach, follow-up, publishing, durable scheduling, queue and paginated extraction tools through an OAuth-protected remote MCP endpoint at salestouch.io/api/mcp. Version 0.8.0, MIT licensed, Claude plugin marketplace enabled, and LinkedIn credentials are never shared with the AI client."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-08-24
source: mcpservers.org /all page 1
relevance: ★★★
tags: [linkedin, sales, prospecting, outreach, gtm, oauth, remote-mcp]
---

# SalesTouch MCP

**The LinkedIn MCP for AI agents: research prospects, build audiences, start conversations, manage follow-ups, and execute controlled LinkedIn outreach through one OAuth-protected endpoint.** SalesTouch (v0.8.0) is an AI-native GTM prospecting platform exposing account, conversation, lookup, outreach, engagement, publishing, durable scheduling, queue, and paginated extraction tools over Streamable HTTP at `https://www.salestouch.io/api/mcp`. The browser OAuth flow grants scoped SalesTouch access; LinkedIn passwords, cookies, and authentication secrets are never shared with the AI client. Not affiliated with LinkedIn.

```
Server type: Remote (Streamable HTTP, OAuth-protected)
Auth: OAuth browser flow (no static API keys, no LinkedIn credentials in config)
Endpoint: https://www.salestouch.io/api/mcp
Repo: github.com/antoineDsh/salestouch (MIT, v0.8.0, Apr 2026)
Tools: Account, conversation, lookup, outreach, engagement, publishing, scheduling, queue, paginated extraction
```

## Why This Matters for Operators

LinkedIn outreach is the highest-value GTM workflow most operators still run by hand: look up a profile, read recent posts, draft a message, wait, follow up, publish. SalesTouch makes each step a tool an agent can call, with a hard line between read and mutate: nothing is sent until a mutation tool is authorized, and OAuth keeps LinkedIn credentials out of the agent entirely. The result is a prospecting pipeline that drafts in seconds, executes on approval, and keeps every conversation in a durable, scheduled queue.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Account | Lists and manages the LinkedIn accounts connected to the SalesTouch workspace |
| Lookup | Resolves profile URLs into structured prospect records |
| Conversation | Searches by profile URL and reads bounded message history |
| Outreach | Drafts and sends connection requests and messages as authorized mutations |
| Engagement | Reads recent posts and engagement context for personalization |
| Publishing | Creates LinkedIn posts through the controlled endpoint |
| Scheduling | Durable follow-up scheduling so no conversation thread goes cold |
| Queue | Prioritized outreach queue with paginated extraction of results |

## Installation

Claude Desktop, Cowork, or Claude Code:

```text
/plugin marketplace add antoinedsh/salestouch
/plugin install salestouch@salestouch
/mcp
```

Cursor or any Streamable HTTP client:

```json
{
  "mcpServers": {
    "salestouch": {
      "url": "https://www.salestouch.io/api/mcp"
    }
  }
}
```

The client discovers the SalesTouch OAuth flow automatically. No static API key or LinkedIn credential belongs in the MCP configuration.

## Configuration

On first use, the browser authorization flow grants scoped SalesTouch access to the workspace. Verify with a read-only request ("List the LinkedIn accounts connected to my SalesTouch workspace") before sending anything. Drafts are reviewed by the operator; no message is sent until a mutation tool is authorized, which keeps human approval in the loop by design.

## Example Prompts

- "Look up this profile URL, read their recent posts, and draft a connection message."
- "Search the conversation with this prospect and draft an exact reply without sending it."
- "Queue follow-ups for every connection accepted this week and show me the schedule."
- "Publish this approved post through SalesTouch and list the results."

## Business Relevance

- **Founders and SDRs** run LinkedIn prospecting from the same agent that tracks the pipeline
- **GTM teams** keep outreach, follow-ups, and publishing in one durable, approved queue
- **Agencies** manage multiple LinkedIn accounts through scoped OAuth workspaces
- **Operators wary of scraper-based tools** get a consent-first, credential-isolated flow

## Integration with CorpusIQ

SalesTouch handles the LinkedIn conversation layer; CorpusIQ answers what happens after the reply. An agent can qualify a prospect with SalesTouch (profile, posts, conversation), then pull that account's commercial history, revenue, and open pipeline from CorpusIQ to decide the next step, all without leaving the agent conversation. Outreach execution from SalesTouch, business truth from CorpusIQ.

## Limitations

- Early product (v0.8.0, 2 GitHub stars at listing time); expect API surface churn.
- LinkedIn-scoped only; other social channels require separate tools.
- Mutations are gated on operator authorization, which adds review friction by design.
- Not affiliated with or endorsed by LinkedIn; account health remains the operator's responsibility.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [LinkedIn MCP GTM](/docs/hermes/mcp/servers/external/linkedin-mcp-gtm) - LinkedIn go-to-market workflow tools
- [LinkedIn Ghostwriter MCP](/docs/hermes/mcp/servers/external/linkedin-ghostwriter-mcp) - profile-aware LinkedIn post drafting
- [Xverum MCP](/docs/hermes/mcp/servers/external/xverum-mcp) - X direct-message outreach for agents
- [Leadgen MCP](/docs/hermes/mcp/servers/external/leadgen-mcp) - B2B lead generation and enrichment
