---
title: "Uxia MCP - AI User Testing and UX Research"
description: "Uxia connects AI assistants to synthetic-user usability testing, so operators catch UX friction before real users walk away."
category: Content & Research
stars: n/a (new listing)
added: 2026-09-28
source: "mcp.so server page (uxia.app)"
relevance: ★★★
tags: [user-research, usability-testing, ux-research, product-validation, remote-mcp, oauth]
---

# Uxia MCP

**AI-simulated usability testing an assistant can run inside ChatGPT.** Uxia lets product managers, UX designers and researchers evaluate websites, interactive prototypes and onboarding flows with AI testers: configure tasks and scenarios, add survey questions, pick synthetic audiences, preview the cost, then approve a launch and read back severity-ranked findings with screenshot evidence.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth with PKCE (Uxia workspace account)
Endpoint: https://platform.uxia.app/api/mcp-v2/mcp
Tools: audience and tester management, research drafts, launch preview, findings read-back
Pricing: Uxia account credits (vendor pricing, uxia.app)
Category: Content & Research / User Research
Built by: Uxia (uxia.app)
```

## Why This Matters for Operators

Usability problems are the most expensive ones to find late. Operators usually learn about confusing flows through support tickets, refunds and abandoned carts - weeks after shipping. Uxia compresses that loop: an assistant drafts a test, configures AI testers that match the target audience, previews the cost, and reads back findings ranked by severity with screenshot evidence, all before a single real user touches the flow.

The mechanism is AI-simulated testers, not real participants, so the results are directional input to a decision rather than primary research. But for catching navigation dead-ends, unclear copy and broken onboarding steps, that is exactly the cheap-failure layer most small teams never run at all.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Audience management | Discover and manage workspace audiences and AI testers |
| Research drafts | Create and edit tests with tasks, surveys and supported test blocks |
| Launch preview | Preview participants, readiness and cost before an approved launch |
| Findings read-back | Read test progress, severity-ranked findings and screenshot evidence |

Tool names are served from the endpoint; the table reflects the vendor's published capability set.

## Installation

```bash
claude mcp add uxia --transport http https://platform.uxia.app/api/mcp-v2/mcp
```

Connect instructions and the OAuth flow live at platform.uxia.app/docs/integrations/mcp.

## Configuration

```json
{
  "mcpServers": {
    "uxia": {
      "type": "http",
      "url": "https://platform.uxia.app/api/mcp-v2/mcp"
    }
  }
}
```

## Business Relevance

- **Product teams** test prototypes and onboarding flows before launch
- **Founders** catch navigation dead-ends and unclear copy early
- **Marketers** evaluate landing pages and funnel friction
- **Agencies** run usability passes for clients without recruiting panels

## Integration with CorpusIQ

Uxia pairs with CorpusIQ analytics connectors as a find-then-fix loop. GA4 funnel and page-path reports surface where drop-off happens; Uxia runs AI testers against those exact screens to find why, with severity-ranked findings and screenshot evidence. The fix can then be measured through the same GA4 connector.

For landing pages driven by paid traffic, correlate the Meta Ads or Google Ads connectors with Uxia tests: test the page before scaling spend, then watch conversion rate move after the fix ships.

## Limitations

- Brand new listing, no track record yet
- AI-simulated testers are directional, not a replacement for real user research
- No published tool catalog; tool names are served from the endpoint
- Test launches consume Uxia account credits
- Requires a Uxia workspace account and OAuth authorization

## FAQ

### How is this different from a real usability study?

Real studies need recruitment, scheduling and incentives. Uxia runs AI-simulated testers against the live experience in minutes, with cost previewed before launch, which makes it a cheap first pass you run before deciding whether real research is worth it.

### What can agents actually do with it?

Draft tests with tasks and surveys, configure synthetic audiences, preview participants and cost, approve a launch, then read back progress, severity-ranked findings and screenshot evidence.

### Does it replace real user interviews?

No. Treat AI-tester findings as directional input and confirm important issues with real users before committing budget.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
