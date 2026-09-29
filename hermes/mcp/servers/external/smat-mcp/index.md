---
title: "SMAT MCP - Instagram and Facebook Publishing for Agents"
description: "SMAT lets an assistant create, schedule and publish Instagram and Facebook posts, carousels and reels, under OAuth-scoped access levels."
category: Marketing
stars: n/a (new listing)
added: 2026-09-29
source: "mcpservers.org server page (smat.chat docs)"
relevance: ★★★
tags: [instagram, facebook, social-media, publishing, scheduling, oauth, remote-mcp]
---

# SMAT MCP

**An OAuth-scoped publishing workflow for social media.** SMAT connects an assistant to a brand's Instagram and Facebook presence so it can read brand context, create drafts, build carousels, generate captions and images with explicit confirmation, and prepare, publish or schedule posts - with access levels and credit limits chosen at connection time.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in, brand-scoped
Endpoint: https://api.smat.chat/api/mcp
Tools: reads, drafts, carousels, paid generation, scheduling, publishing
Pricing: included in every paid plan (Starter, Pro, Studio) and the free trial
Category: Marketing
Built by: SMAT (smat.chat)
```

## Why This Matters for Operators

Social publishing through an assistant usually means handing over the account. SMAT splits the difference: when you connect, you choose the brand, the access level (read only, create content, create with AI, or full access with publishing), how long the access is valid and, when paid actions are included, a credit limit per action. The scopes - smat:read, smat:write, smat:generate and smat:publish - are an upper bound on access, and SMAT still checks role, permissions and blockers per operation.

Paid generation never runs silently. Before paid work the assistant says what will be generated and that it is paid from brand credits by actual usage, then waits for authorization. Preparing a publication freezes its package and checks whether a disclosure is needed, and publication itself is a separate, explicit step.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Brand reads | Read brand context, saved content, schedule, topic ideas, insights, competitor posts and what needs attention |
| Drafts | Create, edit and delete drafts; attach media; preview up to three text-on-image looks |
| Carousels | Build and edit 2 to 6 slide carousels with deterministic overlay rendering |
| Paid generation | Captions, image ideas, image generation and edits, topic refreshes and competitor analysis, each with confirmation |
| Scheduling | Read the week's schedule, change rhythm, add or skip slots, move missed slots |
| Publishing | Prepare, publish to connected Facebook or Instagram destinations, or schedule, move and cancel |

Tool availability depends on the connection's scopes, the user's role and per-operation blockers.

## Installation

```bash
claude mcp add smat --transport http https://api.smat.chat/api/mcp
```

In SMAT, the MCP address lives in Settings, then Integrations under the MCP connections card, with an Add to Claude button. Leave OAuth client ID and secret fields empty. An account without a paid plan or trial cannot connect.

## Configuration

```json
{
  "mcpServers": {
    "smat": {
      "type": "http",
      "url": "https://api.smat.chat/api/mcp"
    }
  }
}
```

## Business Relevance

- **Brand owners** keep publication human-approved while delegating drafting, carousels and scheduling
- **Social managers** run several brands from one assistant, with per-brand scopes and credit limits
- **Agencies** grant time-boxed, credit-capped access per client brand instead of sharing logins
- **Founders** get consistent posting cadence with paid actions always confirmed first

## Integration with CorpusIQ

SMAT operates the publishing layer while CorpusIQ answers the performance question. An assistant can schedule SMAT content and then measure what it drove through CorpusIQ connectors - GA4 sessions, Stripe revenue, ad spend - closing the loop between a published post and the business result, with the same defined metric answered consistently in every assistant.

## Limitations

- Requires an active SMAT account with access to the target brand
- Paid generation and publishing each need their own authorization; there is no tool to withdraw a published post
- Revoking the MCP connection does not cancel an already admitted schedule
- Brand new MCP listing; the vendor's docs note that not every flow is certified on every host

## FAQ

### What access levels can I grant?

Read only, create content, create with AI, or full access with publishing. You also choose how long the access is valid and, when paid actions are included, a credit limit per action.

### Are paid actions confirmed first?

Yes. Before paid work the assistant states what will be generated or analyzed and that it is paid from brand credits by actual usage, then waits for your authorization. Permission to read or estimate is not permission to generate.

### What happens if I revoke the connection?

Revocation removes the connection but does not delete brand content or withdraw published posts, and it does not cancel already scheduled publications. Cancel scheduled publications separately.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
