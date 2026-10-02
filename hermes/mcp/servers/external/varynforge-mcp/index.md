---
title: VarynForge MCP - Agent-Native SEO Research and Briefing
description: OAuth-gated SEO research MCP that reads an operator's site, anchors to the niche and forges prioritised content plans. Opportunity clusters, per-channel writer-ready briefs, draft linting, distribution tracking and a 30-day market radar across 57 tools at a probe-verified endpoint.
category: SEO
stars: n/a (new listing)
added: 2026-09-08
source: mcp.so
relevance: ★★★
tags: [seo, content-strategy, keyword-research, content-briefs, content-planning, market-radar, remote-mcp]
---

# VarynForge MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - VarynForge turns an agent into a full SEO research operation. The server starts from the operator's own site, anchors to the niche, runs research that produces ranked opportunity clusters, and forges writer-ready briefs for article, X, LinkedIn, Reels and YouTube channels, then tracks every article through a five-stage Kanban to publish with a distribution ledger.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (openid, profile, email, offline_access scopes; RS256)
Endpoint: https://app.varynforge.com/api/mcp
Tools: 57 (projects, research runs, opportunities, keywords, briefs, linting, radar)
Pricing: Free tier (project creation, niche analysis, sitemap mapping); research runs consume credits
Category: SEO
Built by: VarynForge (varynforge.com)
```

## Why This Matters for Operators

Generic SEO tools dump keyword spreadsheets scored against the whole internet. None of them know what the operator's site already covers, and none of them say what to write next. **VarynForge MCP starts from the site, anchors to the niche, and forges a prioritised plan with briefs ready to ship** - the operator's agent stops guessing and starts executing a defensible roadmap.

The deliverable is a Kanban of articles in five stages (Planned, Generating Brief, Brief Ready, Out for Writing, Monitoring), where every card carries a writer-ready brief. A research run also lights a 30-day market radar that synthesises rising narratives from news, Reddit and Hacker News, flags hot picks with a 48-hour act window, and lets the agent file radar-born article suggestions straight into the content plan.

## Tools & Capabilities

| Area | Tools | Purpose |
|---|---|---|
| Agent & account | `get_instructions`, `get_changelog`, `get_writer_system_prompt`, `get_account_status`, `list_organizations`, `get_onboarding_guide`, `send_feedback` | Workflow guide, product changelog, per-channel writer prompts, plan and credit status, guided setup, feedback channel |
| Projects & assets | `create_project`, `get_project`, `list_projects`, `get_project_asset`, `update_niche`, `set_posting_cadence`, `list_destinations`, `add_destination`, `update_asset_profile`, `resync_asset_profile`, `remap_asset` | Project creation from URL or niche, niche profiles, publishing destinations, posting cadence, asset profile corrections and re-crawls |
| Competitors | `list_competitors`, `set_competitor_importance`, `add_competitor_by_domain`, `get_competitor_detail` | Competitor tracking with importance weighting and SERP discovery |
| Research & opportunities | `start_research_run`, `get_research_status`, `get_project_overview`, `list_opportunities`, `get_opportunity_detail`, `set_opportunity_status`, `set_excluded_terms`, `get_pitch_report_payload`, `get_starting_point_report` | Credit-gated research runs, ranked opportunity clusters, goal filters, exclusion terms, client-ready pitch reports, free starting-point report |
| Keywords & pages | `list_keywords`, `get_keyword_detail`, `list_pages`, `get_page_dossier` | Tracked keywords with intent and difficulty, ranked pages with ownership, page dossiers with outlines and content analysis |
| Content plan | `list_article_suggestions`, `create_content_plan_from_opportunities`, `add_article_suggestion`, `create_article_suggestion_with_input`, `update_article_status`, `generate_article_brief`, `get_article_suggestion`, `get_article_brief`, `delete_article_suggestion`, `download_brief_markdown`, `get_write_handoff`, `get_draft_status`, `mark_article_published`, `register_derived_asset` | Kanban pipeline from plan to publish, brief generation per channel, brief download, writer handoff, published-article ledger, derived asset registration |
| Verification | `get_lint_rubric`, `lint_draft` | Draft verification against the brief with pass/flag verdicts and per-check detail |
| Ideas | `expand_idea`, `accept_idea`, `check_idea` | Score raw ideas against the niche, commit them to the plan, attach real search data with daily and monthly caps |
| Radar | `list_radar_topics`, `expand_radar_topic`, `add_radar_topic` | Emergent-topic radar snapshot, candidate angles, radar-born article suggestions |

## Installation

```bash
claude mcp add varynforge --transport http https://app.varynforge.com/api/mcp
```

Claude Desktop, Claude Code, Cursor and ChatGPT apps all work. The vendor ships an OAuth-authenticated server with dynamic client registration, so the first connect opens a browser sign-in on app.varynforge.com. Tool discovery is public; tool calls are RS256-protected.

## Configuration

```json
{
  "mcpServers": {
    "varynforge": {
      "type": "http",
      "url": "https://app.varynforge.com/api/mcp"
    }
  }
}
```

No API key is minted manually - the OAuth flow issues the token. The OAuth protected-resource metadata lives at app.varynforge.com/api/auth/.well-known/oauth-protected-resource and lists openid, profile, email and offline_access scopes with RS256 resource signing.

## Business Relevance

- **SEO agencies** get a client-ready pitch report payload per research run and an auditable Kanban that shows exactly what was planned, briefed and published.
- **Content operators** run the full loop in chat: brief generation, draft linting against the brief rubric, and a distribution ledger that records every published URL and derived asset.
- **Founders and indie operators** start free - project creation, niche analysis and sitemap mapping need no card - and only pay credits when a research run fires.
- **AI-native teams** let agents watch the market radar and file article suggestions before the team's morning standup, with a 48-hour act window on hot picks.

## Integration with CorpusIQ

VarynForge's niche profiling wants the same business truth CorpusIQ already holds. GA4 and Shopify connectors in CorpusIQ tell the operator which products and pages actually convert; that context sharpens the VarynForge project's niche profile and exclusion terms, so the research run ranks opportunities against real revenue behavior instead of generic keyword volume.

The composed monthly loop: CorpusIQ surfaces the niche and customer language, VarynForge forges the content plan with briefs, the team publishes, and CorpusIQ's GA4 dashboards close the loop by measuring the organic impact of every article the ledger says went live. Stripe revenue data in CorpusIQ also backs the pitch-report numbers agencies take to clients.

## Limitations

- Brand new - listed on mcp.so September 8, 2026 with no public repo; no track record yet.
- OAuth required for tool calls - discovery is public but every call needs an authenticated account.
- Research runs consume credits, and idea checks carry daily and monthly caps on every tier.
- Deliberately narrow scope: no backlink crawling, no weekly position polling, no Core Web Vitals audits, and no multi-language support (the vendor lists these as out of scope).
- Hosted only - no self-host option. The mcp.so listing tagline still reads as flight search, stale copy; the live endpoint (v1.21.0) serves the SEO research platform described here.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [KD Scout MCP - Keyword Research Arithmetic](/hermes/mcp/servers/external/kd-scout-mcp)
- [SEOmatic MCP - Real Search Console Data with Approval-Gated Fixes](/hermes/mcp/servers/external/seomatic-mcp)
- [CiteRank MCP - AI Search Visibility Audits](/hermes/mcp/servers/external/citerank-mcp)
