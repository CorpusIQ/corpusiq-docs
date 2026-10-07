---
title: "PageProofer MCP - Website Feedback for Coding Agents"
description: "Let Claude Code or Cursor read your website feedback notes, fix the issues, comment the commit and move the note to review."
category: Development
stars: n/a (hosted platform, pageproofer.com)
added: 2026-10-07
source: "mcpservers.org /all page 1 (Oct 7, 2026 midday sweep)"
relevance: ★★
tags: [website-feedback, agencies, bug-reports, qa, claude-code, cursor, api-token, remote-mcp]
---

# PageProofer MCP

**Hosted MCP server (Streamable HTTP) that closes the website feedback loop** - let an AI coding agent read your PageProofer notes, fix the issues in the code, and report back on the note. Ask "fix the open notes on the Northwind site" or "what is wrong with note 12" and work from there.

```
Server type: Hosted (Streamable HTTP)
Auth: Bearer token created in My Settings - AI agents
Endpoint: https://app.pageproofer.com/mcp
Tools: Site and note listing with filters, full note reads, screenshots and attachments, comments, status changes
Pricing: AI agent access is included on every plan, free trial included
Built by: PageProofer
```

## Why This Matters for Operators

Website feedback usually lives in screenshots, chat threads and memory. PageProofer notes carry the context an agent needs to fix things: the feedback, the page, the element it was pinned to, the reporter's browser and window size, console errors and failed network requests, plus every comment. The loop stays accountable: the agent acts as you, changes are marked "via AI agent" in the activity tab, and agents can never mark a note complete - they move it to Review so a person checks the fix and closes it.

## Tools & Capabilities

| Capability | What the agent can do |
|---|---|
| List sites and notes | Filter by status, #tags, page, assignee or overdue |
| Read a note in full | Feedback, page, pinned element, browser and window size, console errors, failed requests, comments |
| Attachments | Look at screenshots and read attached text files |
| Comment | Say what changed and in which commit |
| Update | Change status, priority, assignee or due date (Review, never Complete or Closed) |

## Installation

```
claude mcp add --transport http pageproofer https://app.pageproofer.com/mcp --header "Authorization: Bearer <your-token>"
```

Create the token first: My Settings - AI agents - Create token (shown once). Any agent that supports streamable HTTP MCP connects with the same URL and header.

## Configuration

```json
{
  "mcpServers": {
    "pageproofer": {
      "url": "https://app.pageproofer.com/mcp",
      "headers": { "Authorization": "Bearer <your-token>" }
    }
  }
}
```

## Business Relevance

- **Agencies:** hand the client feedback queue to the coding agent and review fixes instead of forwarding screenshots.
- **Web teams:** reports arrive with console errors and environment attached, so triage starts with the facts.
- **Freelancers:** the same fix loop on the client's notes, without building an internal tool.

## Integration with CorpusIQ

CorpusIQ answers what your business data says from the systems you connect. PageProofer answers what your website still needs fixed, with the evidence attached. Keep the two questions apart and both stay answerable from the same chat.

## Limitations

- Agents cannot close notes: fixes land in Review for a person to verify.
- A token acts as its user - anyone with it can read and comment on your notes; revoke per machine.
- AI access pauses if the trial ends or the subscription lapses and resumes with a plan.
- Notifications behave as usual; agent comments email the people on the note.

## FAQ

### How do I create an agent token?

My Settings - AI agents tab - Create token. Name it per machine or tool; it is shown once and can be revoked any time.

### What does it cost?

AI agent access is included on every PageProofer plan, including during the free trial.

### Can the agent close issues?

No - agents move notes to Review. A person checks the fix and closes the note.

### Which clients work?

Claude Code, Cursor and any agent that supports HTTP MCP servers, with the bearer header.

## See Also

- [Sitegoalie MCP - WordPress Operations for Agencies](/hermes/mcp/servers/external/sitegoalie-mcp)
- [Uxia MCP - AI User Testing and UX Research](/hermes/mcp/servers/external/uxia-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
