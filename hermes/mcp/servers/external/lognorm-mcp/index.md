---
title: "LogNorm MCP - Growth Audit and Agent Backlog"
description: "Remote MCP that audits a site's growth and AI-readiness, ranks the gaps, and hands agents a backlog of fixes it re-validates on the live site."
category: "Marketing"
stars: n/a (hosted platform, lognorm.com)
added: 2026-10-03
source: "mcpservers.org server page (lognorm/lognorm-mcp)"
relevance: ★★★
tags: [marketing, seo, geo, growth, audit, llms-txt, agent-backlog, remote-mcp]
---

# LogNorm MCP

**Hosted MCP server** - LogNorm finds what is holding a website's growth back, ranks it, and hands agents a backlog of moves to work next to a team: fixes in the repo, posts with images, research. It re-checks every fix on the live site and measures what moved.

```
Server type: Hosted (streamable HTTP, remote)
Auth: OAuth 2.1 with dynamic client registration and PKCE
Endpoint: https://lognorm.com/api/mcp
Pricing: free plan available; agents run on your own Claude or Codex plan
Docs: https://lognorm.com/docs/agents
Category: Marketing
Built by: LogNorm (lognorm.com)
```

## Why This Matters for Operators

LogNorm pairs two things that usually live in separate tools: a technical audit (broken pages, metadata, indexing, AI-crawler access, llms.txt, structured data) and a ranked action backlog that people and agents share. The agent reads the audit, fixes the cause in the codebase, opens a pull request, then calls `validate_fix` so LogNorm re-checks the affected pages on the live site.

The AI-readiness half is the differentiator. It tracks how ChatGPT, Gemini and Google AI Overviews answer a buyer's prompts and turns the gaps into moves, which is the work of getting cited in AI answers rather than only ranked in search. Every claim, comment, draft and fix is attributed to the agent that produced it on the dashboard, so an operator keeps an audit trail of who changed what.

## Tools

`search`, `execute`, `claim_move`, `create_move`, `plan_move`, `update_move`, `validate_fix`, `start_run`, `research_brief`, `save_brief`, `save_draft`, `generate_image`, `plan_topic`, `keyword_lookup`, `add_competitor`, `add_ai_prompts`, `brain_add`, and more.

Workflows are exposed as MCP prompts: `weekly_growth`, `growth_review`, `fix_audit`, `write_post`, `plan_topic`, `ai_visibility`.

## Connect

```
claude mcp add --transport http --scope user lognorm https://lognorm.com/api/mcp
```

Then run `/mcp`, pick lognorm, authenticate, and allow in the browser. Codex uses `codex mcp add lognorm --url https://lognorm.com/api/mcp`. Cursor, Claude desktop and any other client add a remote Streamable HTTP server named `lognorm` with the same URL; the endpoint answers 401 with OAuth metadata, so clients that support MCP authorization start sign-in themselves.

## Limitations

- The service is proprietary; the agent skill and docs are MIT.
- Agents run on your own Claude or Codex plan, billed separately from LogNorm.
- Validation covers the pages a fix touched, not a full re-audit each time.

## FAQ

### How does LogNorm verify a fix?

After the agent changes code, `validate_fix` re-checks the affected pages on the live site and records the result against the move.

### Does it handle AI-search visibility, not just SEO?

Yes. It tracks how ChatGPT, Gemini and Google AI Overviews answer buyer prompts and converts the gaps into backlog moves.

### Is there a free entry point?

Yes. A free plan exists, and because the agent runs on your own Claude or Codex plan, you can start without a paid LogNorm tier.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
