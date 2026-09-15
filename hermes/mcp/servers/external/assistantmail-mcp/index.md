---
title: AssistantMail MCP - Managed Mailboxes for AI Agents
description: Managed mailbox MCP for AI agents, built for OpenClaw and Hermes operators. Agents send and receive email under allowlists, consent, retention rules and spend caps you control. Install with npx, authenticate with an API key, and keep a real inbox without handing agents raw SMTP access.
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★
tags: [email, mailboxes, allowlist, consent, retention, hermes, openclaw, remote-mcp]
---

# AssistantMail MCP - Managed Mailboxes for AI Agents

**MCP server (stdio via npx, hosted mailbox backend)** - gives AI agents a managed mailbox to send and receive email, built for personal and small-team OpenClaw and Hermes operators who want agent email with allowlists, consent, retention rules and spend caps they control. Agents get a real inbox without raw SMTP access, and every message routes through guardrails the operator configures. Listed on ClawHub for easy install.

```
Server type: stdio (npx) with hosted mailbox backend
Auth: API key (ASSISTANT_MAIL_API_KEY, amk_ prefix)
Endpoint: npx -y @assistantmail/assistantmail-mcp
Tools: mailbox send, receive and management (served from the package)
Pricing: free tier - 1 agent, 25 messages/day - paid plans above
Category: Communication & Email
Built by: AssistantMail (assistant-mail.ai)
```

## Why This Matters for Operators

Autonomous agents that email on their own behalf are exactly as dangerous as they are useful: one hallucinated reply to a customer, or one unfiltered outbound blast, and the domain reputation is gone. AssistantMail's answer is a managed mailbox layer where the operator configures the guardrails once - who the agent may write to (allowlist), what consent applies, how long mail is retained and how much the agent can spend - and the agent never touches SMTP directly.

**The guardrails are the product: allowlist, consent, retention and spend caps are first-class settings rather than afterthoughts, so the operator's policy travels with the mailbox instead of living in the agent's prompt.** For OpenClaw and Hermes operators specifically, the install is one ClawHub command (`openclaw skills install @assistantmail/assistant-mail`) or one npx invocation, and the free tier (1 agent, 25 messages/day) is enough to evaluate the whole flow before paying.

The positioning is deliberate - agent email with controls - and the same MCP package works across Claude Desktop, Cursor, OpenClaw and Hermes, so one mailbox policy covers every harness.

## Tools & Capabilities

| Capability | What an agent can do |
|---|---|
| Send | Send email from the managed mailbox under the configured allowlist and spend caps |
| Receive | Read inbound messages with retention rules applied |
| Mailbox management | Manage the mailbox surface (threads, folders) through MCP tools |
| Policy enforcement | Every operation resolves against operator-set allowlist, consent, retention and spend settings |

The full tool list is served from the npm package once installed; the table above follows the vendor's published description. The API key is minted in the AssistantMail app and shown only once at creation.

## Installation

```bash
npx -y @assistantmail/assistantmail-mcp
```

Or on OpenClaw:

```bash
openclaw skills install @assistantmail/assistant-mail
```

Create a free account, generate an API key in the app (shown once - copy it immediately), and set it in the environment for your MCP client. Requires Node 24+.

## Configuration

```json
{
  "mcpServers": {
    "assistantmail": {
      "command": "npx",
      "args": ["-y", "@assistantmail/assistantmail-mcp"],
      "env": {
        "ASSISTANT_MAIL_API_KEY": "amk_your_key"
      }
    }
  }
}
```

The same key works across clients. Policy settings (allowlist, consent, retention, spend caps) live in the AssistantMail app, not in client config, so the operator controls them from one place.

## Business Relevance

- **Autonomous agent operators** get agent email with spend caps and allowlists instead of raw SMTP credentials
- **OpenClaw and Hermes users** get a one-command install and one policy surface across harnesses
- **Small teams** keep consent and retention rules uniform across every agent mailbox
- **Domain-reputation owners** bound outbound volume and destinations before the first send

## Integration with CorpusIQ

AssistantMail complements CorpusIQ's media@ and info@ email handling by giving autonomous agents their own managed mailbox under operator guardrails. CorpusIQ's inbound email connectors read the business inboxes with the operator's rules; AssistantMail gives agents a separate, policy-bound surface for outbound sequences and automated replies, so agent mail never mixes with the company's primary reputation. A composed workflow: CorpusIQ identifies a lead worth following up through its CRM and enrichment connectors, and the agent drafts the follow-up through AssistantMail under the configured allowlist and spend caps, with consent and retention policy enforced by the mailbox layer itself.

## Limitations

- New listing (September 2026) - young product, small track record
- Free tier is thin (1 agent, 25 messages/day) and intended for evaluation
- stdio transport via npx - no hosted remote endpoint published
- Guardrail enforcement depends on the operator actually configuring the policy settings
- Email delivery reputation ultimately sits with the AssistantMail infrastructure

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
