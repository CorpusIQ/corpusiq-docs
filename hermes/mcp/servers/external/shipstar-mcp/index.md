---
title: "Shipstar MCP - CorpusIQ Docs"
description: Product marketing automation from your commits — generate, review, publish, and email changelogs, blog posts, and release notes over OAuth 2.1
category: Content
stars: n/a (new listing)
added: 2026-08-13
source: mcpservers.org
relevance: ★★★
tags: [changelogs, product-marketing, release-notes, gtm, content, remote-mcp]
---

# Shipstar MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1) from Shipstar.** The full product-marketing pipeline as typed tools: generate changelogs, blog posts, feature pages, KB articles, release-note emails, X threads, and LinkedIn posts from your commits — then review, revise, approve, and publish through the same code paths as the Shipstar dashboard. Twenty-one tools with an explicit human approval step between draft and publish.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (recommended) or static bearer token
Endpoint: https://mcp.shipstar.ai/mcp
Tools: 21 (8 generation, 5 lifecycle review/approve/publish, 4 project/delivery, 4 read)
Pricing: Commercial (Shipstar plans)
Category: Product Marketing / GTM
Built by: Turbo Labs (docs.shipstar.ai)
```

## Why This Matters for Operators

Release communications are the most reliably neglected task in software: the commit ships, the changelog does not. Shipstar attacks the gap with the same discipline the Aug 12 sweeps saw in EM+x and Prose Coach — generation is cheap, but nothing publishes without a human gate. Drafts come back as pending content IDs, a reviewer revises and approves, and only approved content reaches the publish tool.

**The read tools make it a knowledge layer, not just a writer.** Support agents can answer "what is new this week" from published changelogs, and coding agents can ground answers in your own shipped KB articles instead of hallucinating APIs. Marketing pulls accurate product details from material you already published.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Generation | `generate_changelog`, `generate_blog_post`, `generate_blog_post_ideas`, `generate_feature_page`, `generate_kb_articles`, `generate_release_notes_email`, `generate_twitter_thread`, `generate_linkedin_post` |
| Lifecycle | `get_generation_status`, `get_content_draft`, `update_content`, `approve_content`, `publish_content` |
| Project & delivery | `get_project_context`, `list_destinations`, `list_mailing_lists`, `send_release_email` |
| Read | `list_changelogs`, `get_changelog`, `list_blog_posts`, `get_blog_post`, `list_kb_article_sets`, `get_kb_article_set` |

Generation tools run in the background — poll `get_generation_status`, then walk the draft through review to approval.

## Installation

```bash
claude mcp add --transport http shipstar https://mcp.shipstar.ai/mcp
```

First connect runs the OAuth flow in the browser; each authorization is scoped to one project, chosen on the consent screen. To pin a static token instead: `--header "Authorization: Bearer YOUR_API_TOKEN"` (tokens from Settings → API Tokens).

## Configuration

```json
{
  "mcpServers": {
    "shipstar": {
      "type": "http",
      "url": "https://mcp.shipstar.ai/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

## Business Relevance

- **SaaS founders** turn every release into a changelog, a blog post, and a release email without a marketing hire.
- **Product marketers** get commit-driven drafts and spend their time on positioning, not first drafts.
- **Support and CS teams** answer "what changed" from published, structured content instead of Slack archaeology.
- **Developer-relations teams** keep X threads and LinkedIn posts flowing from the same source of truth as the docs.

## Integration with CorpusIQ

Shipstar writes the story of what shipped; CorpusIQ measures the business effect of it. The composed loop: commits flow into Shipstar, drafts get approved and published, then CorpusIQ connectors verify outcomes — GA4 for the traffic the blog post and feature page pull, Search Console for the search lift, Ahrefs for ranking movement, and Klaviyo or the release email metrics for engagement. Shipstar also pairs with EM+x upstream: board deliverables describe the strategy, Shipstar turns the shipped evidence into public content, CorpusIQ scores both against revenue and traffic.

## Limitations

- Commercial platform — content generation and email sends sit on paid plans
- Per-project OAuth scoping means multi-project teams authorize each project separately
- Drafts are read-only until approved — no direct agent-to-publish path (by design)
- Publish and email tools are state-changing; the review approval flow is mandatory

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
