---
title: LinkIntel MCP - Social Post Performance Evidence
description: Remote MCP that measures your own X posts daily and returns a cited content brief, so an assistant grounds its next draft in posts that actually performed.
category: Marketing
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [marketing, social-media, content, analytics, x, linkedin, remote-mcp, oauth]
---

# LinkIntel MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - LinkIntel gives an assistant evidence for its next social post. Connect X once and it measures your own recent original posts daily and stores the snapshots; you can also hand it public X posts to learn from, stored with their public performance and source links. The assistant reads both back as a cited content brief. It never publishes anything.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (Google sign-in) plus X connection
Endpoint: https://www.getlinkintel.com/api/mcp
Tools: Own-post measurement, public-post capture, cited content briefs
Pricing: $39 USD/month, billed monthly in advance
Category: Marketing
Built by: LinkIntel
```

## Why This Matters for Operators

AI-written posts fall flat when the model guesses what performs. LinkIntel's mechanism is to **replace the guess with your own performance history**: it snapshots your recent original posts daily, stores any public posts you point it at with their metrics and source links, and returns a brief that says what the evidence supports, what it does not, and what is worth testing.

For founders and content operators who draft with an assistant, that means the next draft is grounded in posts that worked for their audience rather than generic advice. Because it only reads and never publishes, it is a safe research layer beside whatever publishing tool the team already uses.

**The key advantage is a cited, evidence-backed content brief from your own post history, with zero publishing risk.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Measure own posts | Snapshots your recent original X posts daily |
| Capture public posts | Stores public X posts with performance and source links |
| Read brief | Returns a cited brief of what the evidence supports and what to test |

Connect X from the account page or the link the assistant offers. It confirms the list of posts before storing anything.

## Installation

```bash
claude mcp add --transport http linkintel https://www.getlinkintel.com/api/mcp
```

Add it as a remote MCP server in any MCP-compatible client; OAuth opens the browser for Google sign-in.

## Configuration

```json
{
  "mcpServers": {
    "linkintel": {
      "type": "http",
      "url": "https://www.getlinkintel.com/api/mcp"
    }
  }
}
```

Activation requires confirming the $39 monthly charge before the assistant can use the server. LinkedIn support is on the broader roadmap.

## Business Relevance

- **Founders building in public** can ground drafts in their own best-performing posts.
- **Content operators** get a cited brief instead of generic posting advice.
- **Social managers** can study public posts with their real metrics attached.
- **Growth teams** can test hypotheses against measured evidence rather than hunches.
- **Anyone drafting with an AI assistant** gets output tied to their own audience signal.

## Integration with CorpusIQ

LinkIntel feeds CorpusIQ's content and publishing workflow. Where CorpusIQ tracks publishing cadence and reach across platforms, LinkIntel supplies the performance evidence behind each draft, so an assistant can answer "what should we post this week" with a brief grounded in measured results.

A composed workflow: read recent reach and engagement from CorpusIQ's social analytics, ask LinkIntel for a cited brief from your own X history, then have the assistant draft next week's posts against that evidence and schedule them through your publishing connector. CorpusIQ reads the channel; LinkIntel reads what works on it.

## Limitations

- Paid only: $39 USD/month with no free trial.
- Read-only: it never publishes or schedules posts.
- Coverage starts with X; LinkedIn is described as coming to the broader workflow.
- Hosted and proprietary; no self-hosting.
- Value depends on having an established posting history to measure.

## FAQ

### Does LinkIntel publish my posts?

No. It only reads and measures; it never publishes anything.

### Is there a free trial?

No. Activation is $39 USD/month billed in advance after confirmation.

### Which platforms does it cover?

X first, with LinkedIn described as coming to the broader workflow.

### How does it keep drafts grounded?

It snapshots your posts and any public posts you supply, then returns a brief citing what the evidence supports and what to test.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
