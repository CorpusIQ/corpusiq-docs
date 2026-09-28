---
title: "Postfleet MCP - Email Infrastructure for AI Agents"
description: "Postfleet gives AI agents email infrastructure with inbox parsing, schema extraction, prompt-injection screening and approval drafts."
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (postfleet.ai)"
relevance: ★★★
tags: [email-infrastructure, inbox-parsing, prompt-injection, mail-automation, communication, remote-mcp]
---

# Postfleet MCP

**Email infrastructure built for agents, with a security posture operators can audit.** Postfleet gives an AI agent its own email address: inbound mail is parsed, classified, extracted to your schema and screened for prompt injection before the agent reads a word.

```
Server type: Remote (hosted) or stdio (npm @postfleet/mcp)
Auth: Bearer pf_ API key
Endpoint: https://api.postfleet.ai/api/mcp
Tools: 16 (mailboxes, domains, send and reply, inbox, drafts with approval)
Pricing: vendor pricing (postfleet.ai)
Category: Communication & Email
Built by: Postfleet (postfleet.ai, npm @postfleet/mcp)
```

## Why This Matters for Operators

Email is the highest-risk surface to hand an agent: inbound mail can carry prompt injection, and outbound mail can be sent without review. Postfleet addresses both. Inbound messages are screened for injection and extracted to your schema before the agent reads them, and the draft lifecycle lets a human approve before mail goes out, a send that hits the gate returns 202 pending_approval instead of failing.

Sixteen named tools cover the whole motion, mailboxes, domains, sending, inbox and drafts, and every tool is thin over the same REST API your key already reaches, so auth, scoping and quotas are enforced once.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Mailboxes and domains | list_mailboxes, create_mailbox, list_domains, create_domain, verify_domain |
| Send and reply | send_email, reply_email |
| Inbox | list_inbox, read_email, wait_for_email |
| Draft lifecycle | create_draft, list_drafts, get_draft, update_draft, send_draft, delete_draft |

The full OpenAPI spec is published at postfleet.ai/openapi.json.

## Installation

```bash
claude mcp add --transport http postfleet https://api.postfleet.ai/api/mcp \
  --header "Authorization: Bearer pf_YOUR_KEY"
```

Local stdio install: npx @postfleet/mcp. Keys are minted at postfleet.ai.

## Configuration

```json
{
  "mcpServers": {
    "postfleet": {
      "url": "https://api.postfleet.ai/api/mcp",
      "headers": {
        "Authorization": "Bearer pf_YOUR_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Founders** give agents email without opening a prompt-injection hole
- **Support teams** run draft-gated replies where a human approves every send
- **Ops teams** parse inbound mail into schemas before agents read it
- **Developers** use the same API key scope for scripts and agents alike

## Integration with CorpusIQ

Postfleet slots into the same CorpusIQ email pattern as Faivelo and Cooper: human mailboxes stay on the CorpusIQ Gmail connectors while agent-facing addresses run through Postfleet, with inbound extraction feeding structured data into the CorpusIQ HubSpot or ActiveCampaign connectors.

For invoice-style workflows, Postfleet's schema extraction can route parsed content toward QuickBooks through CorpusIQ connectors, with the draft gate ensuring a human approves before anything commits.

## Limitations

- New listing, no track record yet
- Hosted service and npm package are both young
- Draft approval adds a step to every gated send
- Self-hosted deployments carry the usual infrastructure burden

## FAQ

### How does it stop prompt injection?

Inbound mail is screened for prompt injection before the agent reads a word, and extraction lands in your schema first.

### What happens when a send needs approval?

The send returns 202 pending_approval, which is a gate, not a failure. A human approves and the draft goes out.

### Is there a local option?

Yes. The server ships as an npm package, @postfleet/mcp, for npx stdio installs alongside the hosted endpoint.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
