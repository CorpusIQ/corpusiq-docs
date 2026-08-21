---
title: "LinkedIn Ghostwriter MCP — LinkedIn Posts in Your Voice, Drafted, Scheduled and Measured"
description: "ContentIn's MCP server writes LinkedIn posts in your own voice from a VoiceDNA model trained on your real posts: ideas, drafts, scheduling, publishing via LinkedIn's official API, and post analytics — 8 tools over Streamable HTTP with an X-MCP-Key header."
category: Content & Marketing
stars: n/a (new listing)
added: 2026-08-21
source: mcp.so
relevance: ★★
tags: [linkedin, content, ghostwriting, voice, scheduling, analytics, marketing, remote-mcp]
---

# LinkedIn Ghostwriter MCP

**LinkedIn posting that sounds like you, run from any MCP client.** ContentIn's hosted server runs a voice pipeline — VoiceDNA trained on your own LinkedIn posts, your real past posts as style exemplars, and a substance bank of your material — so the main tool, `write_post_in_my_voice`, returns a draft in your voice rather than an AI's. Drafts land in your ContentIn account and can be scheduled or published through LinkedIn's official API, with post analytics read back through the same endpoint.

```
Server type: Remote (Streamable HTTP)
Auth: X-MCP-Key header (cimcp_ key from ContentIn)
Endpoint: https://mcp.contentin.io/mcp-server
Tools: 8 (draft, list, schedule, publish, repurpose, analytics)
Pricing: ContentIn plans (not published on listing)
Category: Content & Marketing
Built by: ContentIn (contentin.io)
```

## Why This Matters for Operators

Founders and operators know they should post on LinkedIn and mostly don't, because writing in public is the bottleneck — not ideas, not scheduling. **The Ghostwriter's contract is voice preservation:** the tool instructions tell the agent to pass your words as literally as possible and explicitly forbid tidying or paraphrasing, because that's how a post stops sounding like you. If the pipeline needs something only you know, it returns `needs_input: true` with a question and stops — it refuses to invent.

Publishing runs through LinkedIn's official API, so posts go out as first-party content with real analytics read back (impressions, members reached, engagement rate), measured honestly — a post with no numbers yet reports "not measured yet" rather than zeroes.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `write_post_in_my_voice` | The main tool: draft a post in your voice from your own material; saved as a draft |
| `list_posts` | List drafts, scheduled, published and ideas on the profile |
| `schedule_post` / `publish_post` | Queue or publish via LinkedIn's official API |
| `get_post_analytics` | Impressions, reach, likes, comments, shares, engagement rate |
| `repurpose_post` | Turn an existing post into a new format or angle |

Eight tools total; the listing documents the drafting, listing, analytics and repurposing families.

## Installation

```bash
claude mcp add linkedin-ghostwriter --transport http https://mcp.contentin.io/mcp-server --header "X-MCP-Key: cimcp_YOUR_KEY"
```

Setup walkthroughs for Claude, ChatGPT, Cursor and other MCP clients are published at contentin.io/linkedin-mcp-server/setup.

## Configuration

```json
{
  "mcpServers": {
    "linkedin-ghostwriter": {
      "type": "http",
      "url": "https://mcp.contentin.io/mcp-server",
      "headers": {
        "X-MCP-Key": "cimcp_YOUR_KEY"
      }
    }
  }
}
```

Voice training happens in ContentIn on your own post history; the MCP key scopes the agent to your profile. Analytics are only available for posts published through the connected LinkedIn account.

## Business Relevance

- **Founders** keep a consistent LinkedIn presence without writing posts from scratch
- **Sales leaders** turn deal stories and customer wins into voiced posts in minutes
- **Operators building personal brand** get idea generation, drafting and scheduling in one surface
- **Marketing teams** repurpose company content into executive-voiced posts

## Integration with CorpusIQ

The Ghostwriter is the outbound voice; CorpusIQ is the business engine behind it. An agent session can pull this week's real numbers through CorpusIQ (Stripe revenue, GA4 traffic, a HubSpot deal won) and hand them to `write_post_in_my_voice` as substance — so the post carries actual figures, in your voice, with the analytics read back through the same session for the next iteration. The loop turns business data into personal-brand content without a human rewriting the numbers.

## Limitations

- Requires a ContentIn account, voice training on your posts, and a linked LinkedIn account
- LinkedIn-only — no X, Threads or other platforms through this server
- `write_post_in_my_voice` takes 30-90 seconds per draft and may stop with a question instead of a draft
- Hosted vendor pipeline; content passes through ContentIn's systems
- Brand new MCP listing (Aug 2026); pricing not published on the listing page

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
