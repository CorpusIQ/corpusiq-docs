---
title: PendPost MCP - Local-First Social Publishing with Approval
description: "PendPost is a free, open-source, local-first social MCP server: an agent drafts and schedules posts across Instagram, Facebook, LinkedIn, YouTube, X, Telegram, Discord, Mastodon, Nostr, WordPress and Ghost behind a human approval gate. Read-only tools can never publish, nothing publishes until approved, and auto-approve is owner-only."
category: Social Media Management
stars: 7
added: 2026-09-07
source: "chatmcp/mcpso issue #3982"
relevance: ★★★
tags: [social-media, scheduling, approval-gate, local-first, stdio, publishing]
---

# PendPost MCP - Local-First Social Publishing with Approval Gates

**Local stdio MCP server (npm, MIT; optional local Streamable HTTP)** - PendPost drafts and schedules posts across eleven platforms from a local-first server the operator controls. Platform credentials live in a local .env minted through per-engine CLI ceremonies, so no secret ever reaches the server operator. Publishing is gated by design: read-only tools can never publish, nothing publishes until it is approved, and auto-approve is owner-only.

```
Server type: Local (stdio via npx pendpost --stdio; optional Streamable HTTP at 127.0.0.1:8090/mcp)
Auth: None to start (mock mode); platform credentials stay in a local .env
Tools: Drafting, scheduling, publishing, approval queue, long-form posting
Pricing: Free, open source
Category: Social Media Management
Built by: PendPost (pendpost.com); repo github.com/pendpost/pendpost
```

## Why This Matters for Operators

Social publishing agents are only as safe as their publish path. PendPost's answer is to make the human the gate: the agent drafts and schedules, the operator approves, and only then does anything leave the machine. The mock mode means the whole workflow is testable before a single credential is minted.

**The local-first stance is the trust story: credentials never leave the operator's machine, the server binds to 127.0.0.1, and the approval queue is the only route to publication.**

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Drafting | Drafts posts for all supported platforms, including long-form blogs on WordPress and Ghost |
| Scheduling | Schedules posts and threads per platform |
| Approval queue | Routes every publish through a human approval gate the operator controls |
| Publishing | Publishes approved posts; read-only tools can never publish |
| Platform coverage | Instagram, Facebook, LinkedIn, YouTube, X, Telegram, Discord, Mastodon, Nostr, WordPress, Ghost |

## Installation

```bash
npx -y pendpost --stdio
```

## Configuration

```json
{
  "mcpServers": {
    "pendpost": {
      "command": "npx",
      "args": ["-y", "pendpost", "--stdio"]
    }
  }
}
```

Platform credentials are minted through per-engine CLI ceremonies into a local .env; mock mode works with no credentials for testing.

## Business Relevance

- **Founders** run their own social agent on their own machine with no third party holding the accounts.
- **Content teams** move drafts through an approval queue instead of copy-paste into schedulers.
- **Privacy-conscious operators** keep platform credentials local rather than in a hosted vendor vault.
- **Developers** self-host the optional HTTP transport for team workflows.

## Integration with CorpusIQ

PendPost ships the content; CorpusIQ measures whether it worked. A composed workflow: the agent drafts a post from the month's best-performing signal in CorpusIQ's GA4 and Stripe data, routes it through the PendPost approval queue, and the operator publishes with the numbers already in hand.

## Limitations

- Brand new listing (issue #3982, Sep 7, 2026); 7-star repo created Jun 2026.
- Local-first means the server runs where the operator runs it; no hosted mode.
- Platform credential ceremonies are per-engine; initial setup takes one pass per platform.
- Long-form support covers WordPress and Ghost; other CMS integrations are not listed.

## See Also

- [PostBazooka MCP - Social Publishing with Commit Proof](/docs/hermes/mcp/servers/external/postbazooka-mcp)
- [PurrPlan MCP - Agent-Driven Social Scheduling and Inbox](/docs/hermes/mcp/servers/external/purrplan-mcp)
- [Antwork MCP - Social Publishing with Learned Brand Voice](/docs/hermes/mcp/servers/external/antwork-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
