---
title: "Pitstop MCP - Nothing Leaves Without a Yes"
description: "Agent memory plus an approval gate for advisory firms: notes persist across chats, and anything outbound emails the owner a one-time link."
category: Productivity
stars: ★★★ (401 + OAuth protected-resource verified)
added: 2026-10-29
source: "live probe of https://mcp.ai-agents-pitstop.com/mcp answering HTTP 401 empty, and its protected-resource document at /.well-known/oauth-protected-resource/mcp advertising the resource, authorization server, scope pitstop and resource_name Pitstop; product behaviour from https://ai-agents-pitstop.com"
relevance: ★★★
tags: [approvals, agent-governance, professional-services, memory, oauth, remote-mcp]
last_updated: "2026-10-29"
---

# Pitstop MCP

**An assistant that can send email is an assistant that will eventually send the wrong email. The fix is not better prompting. The fix is a gate that stands between the draft and the recipient.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.ai-agents-pitstop.com/mcp
Auth:        OAuth 2.1
Discovery:   https://mcp.ai-agents-pitstop.com/.well-known/oauth-protected-resource/mcp
Scope:       pitstop
Approval:    one-time link emailed to the owner per outbound item
```

## Why This Matters for Operators

The interesting thing about this server is not that it stores notes. Plenty of servers store notes. It is that the approval step is explicit, per item, and carries the exact content that will leave.

The vendor's framing is the correct operational one: agents do the work around the client work, meaning research, first drafts, follow-ups, meeting notes and the CRM, and anything that leaves the firm waits for a person's yes. A validation request emails the owner a one-time approval link, and the decision bounds what happens next rather than being advisory.

That design shows up in the audience too. The product is built for executive search, advisory and consulting firms, which are businesses whose output is communication and whose risk is the sentence that should not have gone out. The onboarding advice on the site is unusually disciplined for a hosted tool: start with one recurring task set to ask first, and run it that way for 30 days before loosening anything.

The persistence is the second property. Notes about preferences, projects and people carry across conversations in Claude, ChatGPT, Claude Code and Codex, so the assistant that drafts the follow-up knows what was agreed in the meeting rather than reconstructing it from the thread.

## What Was Verified

A bare `initialize` POST to `https://mcp.ai-agents-pitstop.com/mcp` returned **HTTP 401** with an empty body, which is a live endpoint rejecting an unauthenticated session.

The protected-resource document at `https://mcp.ai-agents-pitstop.com/.well-known/oauth-protected-resource/mcp` returned **HTTP 200** with resource `https://mcp.ai-agents-pitstop.com/mcp`, authorization server `https://mcp.ai-agents-pitstop.com`, a single scope named `pitstop`, bearer methods supported in the header, and `resource_name` Pitstop.

The approval mechanic and the target audience come from the vendor's own site, which shows a sample morning of agent requests with what leaves, to whom, and the status of each.

## Limits Worth Recording

The surface is credential gated, so no tool inventory was read this pass. The behaviour described here is the vendor's published description plus the OAuth contract.

A single scope means the approval surface and the notes surface arrive together. There is no published read-only scope, so an assistant connected for context also holds whatever the `pitstop` scope allows.

Approvals route to the owner by email. That makes the owner the bottleneck by design, which is correct for a two-partner advisory firm and worth measuring before deploying to a larger team.

The one-time link depends on the mailbox being reachable. If the approval email is missed, the draft waits, and nothing in this pass suggests a fallback channel.

## FAQ

### What stops an agent from sending something unapproved?

The approval step is part of the server, not part of the prompt. An outbound item produces a validation request, and the owner approves it through a one-time link.

### Does it remember anything between conversations?

Yes. Notes on preferences, projects and people persist across conversations and across the clients named by the vendor.

### Who is it built for?

Executive search, advisory and consulting firms, and the site is explicit that the intended starting posture is one recurring task at ask first for 30 days.

## See Also

- [Productivity servers in this catalogue](/hermes/mcp/servers/external/)
- [Connecting CorpusIQ to your own data sources](/hermes/mcp/)
