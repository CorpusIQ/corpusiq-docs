---
title: "FoundRole MCP - Fact-Checked AI Job Search and Application Tracking"
description: "Hosted job-search MCP: live openings from company career pages with ghost-posting, real-pay and visa-sponsorship fact-checks on every posting, plus match scoring, deterministic resume parsing, a Kanban application tracker, follow-up reminders and H1B wage data. OAuth 2.1 PKCE, free account, npm stdio bridge."
category: Business Operations
stars: "0 (new listing, foundrole/jobs-mcp-proxy)"
added: 2026-09-02
source: "chatmcp/mcpso GitHub issue #3891 (Sep 2, 2026 morning sweep)"
relevance: ★★★
tags: [mcp-server, jobs, hiring, recruiting, salary-data, h1b, visa-sponsorship, application-tracking]
---

# FoundRole MCP

**Run the whole job search from your AI assistant, with every posting fact-checked before you spend an evening on it.** FoundRole connects ChatGPT, Claude or Cursor to a live job board built from company career pages, refreshed hourly across 40+ industries. Each posting comes back with three checks answered from evidence: ghost-posting risk, real pay against what employers actually file, and visa sponsorship history counted year by year. The same OAuth account carries match scoring, a deterministic resume parser, a Kanban application tracker, follow-up reminders with calendar invites, and email alerts. The server never applies or emails as the user.

```
Server type: Hosted (www.foundrole.com/mcp) plus npm stdio bridge
Endpoint: https://www.foundrole.com/mcp (Streamable HTTP)
Auth: OAuth 2.1 with PKCE, no API key; free account, sign in once in the browser
npm: @foundrole/ai-job-search-mcp v1.1.11 (stdio bridge for clients without remote MCP)
Repo: github.com/foundrole/jobs-mcp-proxy (MIT, created Aug 2025)
Website: foundrole.com
Tools: capability-level (OAuth-gated; anonymous enumeration refused, endpoint 401-verified live)
```

## Why This Matters for Operators

Hiring-market intelligence is the same asset whether you are hiring, job hunting, or benchmarking. FoundRole is the first MCP that returns job openings with the three diligence questions answered per posting.

First, **the pay data is filed data, not a guess.** Hidden salary ranges get checked against what employers in that market really file, and the H1B wage explorer draws on certified wages filed with the US Department of Labor. That turns "what does this role pay" from vibes into a citation.

Second, **ghost-posting risk is computed.** Roles reposted for months or built to fish for resumes get flagged, so a team does not burn recruiting or application effort on listings that are not real.

Third, **the tracker and reminders close the loop inside the chat.** Saved to Applied to Interviewing is Kanban state the assistant manages, with follow-up reminders landing as calendar invites - the operator workflow the Worklittle class of jobs servers does not carry.

## Tools and Capabilities

Capability-level table from the vendor docs and submission issue; exact tool names require OAuth sign-in (anonymous initialize returns HTTP 401, which confirms the endpoint is live). npm package verified published (v1.1.11).

| Area | Capabilities |
|------|--------------|
| Job search | Live openings from company career pages, refreshed hourly across 40+ industries; natural-language filters: title, location, company, salary range, posting date |
| Posting fact-checks | Ghost-posting risk, pay against market filings, visa sponsorship history counted year by year |
| Fit and matching | Match scoring against resume and profile, ranked recommendations, side-by-side role comparison on fit, pay, sponsorship and posting risk |
| Resume analysis | Deterministic ATS parser read: title, years, recognized skills, sections, contact details, plus what the parser loses |
| Application tracker | Kanban board operations (Saved to Applied and beyond), follow-up reminders with calendar invites, weekly email alerts |
| Research | Company directory, industry sectors, hiring by location, H1B salary explorer and sponsor rankings |
| Pasting | Paste a posting from LinkedIn or a careers page for the same checks and tracker entry - nothing crawls the site |

## Installation

Point any remote-MCP client at the endpoint, or bridge stdio-only clients with npx:

```bash
npx @foundrole/ai-job-search-mcp
```

Claude (web/desktop): Settings, Connectors, Add custom connector, paste `https://www.foundrole.com/mcp`. Cursor installs from the marketplace plugin; VS Code uses `{"servers": {"foundrole": {"type": "http", "url": "https://www.foundrole.com/mcp"}}}`. ChatGPT users add the FoundRole app from the app directory. Approve the FoundRole sign-in once and every session is authenticated.

## Configuration

The account is free: search, fact-checks, tracker, reminders and alerts have no usage limits. Pro adds screening filters - remote-only, sponsors-only, a salary floor, risky postings hidden, a minimum match - applied before the assistant sees the list, with a note when filters were not applied on the free tier. No API key exists to copy or rotate; OAuth 2.1 with PKCE plus dynamic client registration and redirect-URI validation.

## Business Relevance

- **Founders and hiring managers** get filed-wage benchmarks before writing an offer, plus visa-sponsorship history before sourcing a candidate.
- **Recruiters** get a live, fact-checked candidate-facing surface and a tracker that runs in the chat.
- **Operators benchmarking markets** get salary and hiring data by industry, sector, location and role - the Worklittle competitive-intelligence pattern applied to the labor market.

## Integration with CorpusIQ

FoundRole composes with CorpusIQ as the labor half of a hiring economics workflow. CorpusIQ answers from the revenue and pipeline side (Stripe, HubSpot, payroll) while FoundRole answers from the market side (what this role really pays, who sponsors visas, which postings are real). An operator can ask "benchmark the pay for this role against our current burn, then flag which of these candidates we can actually afford" and get the market number and the financial number in one conversation.

## Limitations

- Endpoint is OAuth-gated: anonymous initialize returns 401, so exact tool names need a signed-in session; the tool table above is capability-level.
- Brand-new repo with zero stars; expect early-stage changes.
- H1B and wage data is US-centric; ghost-posting and pay checks draw on US employer filings.
- The server never applies or emails as the user - tracking and reminders only, no autonomous outreach.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/docs/hermes/mcp/servers/external/worklittle-jobs)
