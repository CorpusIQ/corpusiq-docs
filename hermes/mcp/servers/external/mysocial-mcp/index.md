---
title: "Mysocial MCP - Your Real Social Media History as Agent Memory"
description: "Hosted social media intelligence MCP that reads your real Instagram, TikTok, YouTube, LinkedIn and Threads history - posts, metrics, transcripts, comments and audience - plus Creator Universe market research, brand and creator tracking, content-gap analysis, idea originality checks and a lead pipeline. OAuth 2.1 PKCE, 50+ tools."
category: Social Media Management
stars: "n/a (hosted service, no public repo)"
added: 2026-09-02
source: "mcpservers.org /all JSON-LD (Sep 2, 2026 morning sweep)"
relevance: ★★★
tags: [mcp-server, social-media, analytics, instagram, tiktok, youtube, linkedin, creator-research]
---

# Mysocial MCP

**Your real social history, turned into evidence your assistant can reason over.** Mysocial connects your Instagram, TikTok, YouTube, LinkedIn and Threads accounts and builds a searchable memory of what you have already published: every post with its metrics, every video transcript, the comments your audience left, the topics you keep returning to, and what is working for other creators in your market. The MCP connector opens that memory to an assistant, so answers come from your actual performance data instead of guesses - plus a Creator Universe research surface, brand and creator tracking, content-gap analysis, and a lead pipeline.

```
Server type: Hosted (app.mysocial.io/mcp) plus a narrower research endpoint
Endpoint: https://app.mysocial.io/mcp (Streamable HTTP); https://app.mysocial.io/mcp/universe (Creator Universe research only)
Auth: OAuth 2.1 with PKCE and dynamic client registration; no API key to paste
Website: mysocial.io
Tools: 50+ across own-archive reads, Creator Universe research, brand studio, ideas and drafts, lead pipeline, transcription jobs
```

## Why This Matters for Operators

Social operators fly blind between channel dashboards. Mysocial makes the assistant the one place that has the evidence.

First, **cross-channel comparison becomes possible.** An assistant can compare a TikTok against a Reel, notice that a topic works on LinkedIn and dies on Threads, or find which of your videos beat your own median rather than someone else's benchmark - none of that is possible from a screenshot or a pasted export.

Second, **the Creator Universe is a market research surface.** `search_universe`, `explore_topic` and `get_universe_post` answer what is working for other creators in your market from already-collected discovery data, without reach into your own archive or drafts. The narrower `/mcp/universe` endpoint exposes exactly this surface for agents that should research the market but not touch your account.

Third, **the write tools are additive and reversible by design.** No tool deletes anything; brand sources and products keep revision histories, drafts and ideas are additive, and nothing the agent does is irreversible.

## Tools and Capabilities

Tool roster from the vendor's connector documentation (endpoints 401-verified live; OAuth required, anonymous enumeration refused).

| Area | Tools | What they do |
|------|-------|--------------|
| Orientation | `whoami`, `list_channels`, `list_workspaces` | Which accounts and workspaces the agent can see |
| Your posts | `search_posts`, `find_similar_posts`, `search_social_memory`, `read_post_transcript`, `read_post_comments`, `get_post_media`, `get_channel_analytics`, `get_top_performing_posts_with_patterns`, `get_hit_dna`, `get_post_psychology`, `get_post_creation_context`, `compare_post_candidates` | The published archive with metrics, transcripts, comments and performance patterns |
| Topics and audience | `get_topics`, `get_topic_posts`, `map_topics`, `map_territories`, `get_territory_brief`, `get_audience`, `find_content_gaps` | Topic maps, audience data and content gaps against your market |
| Creator Universe | `search_universe`, `explore_topic`, `universe_content`, `get_universe_post`, `universe_status` | Read-only market research across creators, from collected discovery data |
| Outside the platform | `search_youtube`, `search_tiktok`, `search_creators` | Platform search and creator search |
| People and brands | `search_brands`, `search_linkedin_people`, `get_entity`, `find_contacts` | Brand and person lookup with contact finding |
| Leads | `list_leads`, `get_lead`, `add_brand`, `add_creator`, `link_channel`, `save_leads`, `update_lead`, `add_note` | Lead pipeline read and write |
| Brand Studio | `list_brand_identities`, `get_brand_identity`, `list_brand_products`, `get_brand_product`, `search_brand_sources`, `read_brand_source`, `list_brand_source_revisions`, `list_content_ideas`, `get_content_idea` | Brand identity, product and idea libraries with revision history |
| Writes | `save_content_idea`, `update_content_idea_status`, `save_post_draft`, `revise_post_draft`, `check_if_idea_already_posted`, `create_brand_source`, `update_brand_source`, `create_brand_product`, `update_brand_product`, `transcribe_video_url`, `switch_workspace` | Additive writes, idea originality checks, transcription jobs |

Every tool is annotated read-only vs write, so assistants know which calls need a confirmation prompt.

## Installation

Connect your social accounts at mysocial.io, then point any MCP client at the connector URL - OAuth 2.1 with PKCE and dynamic client registration means a client that speaks MCP needs nothing but the URL:

```
https://app.mysocial.io/mcp
```

Setup guides exist per platform (Instagram, TikTok, YouTube, LinkedIn, Threads) for Claude, ChatGPT, Claude Code and Codex. Agents that should only research the market use `https://app.mysocial.io/mcp/universe` - read-only, reports what discovery has already collected, and no tool on either endpoint starts new collection or spends research credits.

## Configuration

Free gives your assistant the record; paid gives it the understanding (per the vendor pricing page). Read tools run without a confirmation prompt; write tools ask first. There are no API keys to rotate - authentication is OAuth 2.1 with dynamic client registration, managed per connected account.

## Business Relevance

- **Creators and social teams** get cross-channel analytics, content-gap analysis and hit-pattern diagnosis in one assistant conversation.
- **Brands** get brand and creator tracking plus a lead pipeline fed from social discovery.
- **Agencies** get a Creator Universe research surface that reads market data without touching client archives.

## Integration with CorpusIQ

Mysocial composes with CorpusIQ as the performance half of a social growth loop. CorpusIQ answers from the revenue and CRM side (Stripe, HubSpot) while Mysocial answers from the content side (what worked, what gap to fill, whether an idea is already posted). An operator can ask "find our content gaps, propose the next three posts, and tell me which of last month's posts actually drove revenue" and get the creative plan and the financial answer in one workflow. Pairs with Postiz publishing for the execution step and with Maeve Social for scope-gated agent publishing.

## Limitations

- Endpoints are OAuth-gated: anonymous probes return 401, so the tool table above is from vendor docs, not a live enumeration.
- No public repo found; the connector docs at mysocial.io are the source of record.
- Writes are additive only - useful for safety, but there is no delete surface for mistakes.
- Creator Universe tools report collected data only; they do not trigger new collection or spend research credits.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Social Glass MCP: Cultural Intelligence for Brand and Research Teams](/docs/hermes/mcp/servers/external/social-glass-mcp)
- [Maeve Social MCP - Social Publishing with Scope-Gated Agent Access](/docs/hermes/mcp/servers/external/maeve-social-mcp)
