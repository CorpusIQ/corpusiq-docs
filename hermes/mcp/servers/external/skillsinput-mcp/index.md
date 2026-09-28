---
title: "SkillsInput MCP - AI Career Tools for Job Search"
description: "SkillsInput brings job search, skills intelligence, career roadmaps and resume building to AI assistants over a hosted MCP."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (skillsinput.ai)"
relevance: ★★
tags: [job-search, careers, resume, skills-intelligence, hiring, remote-mcp]
---

# SkillsInput MCP

**Career tooling your AI assistant can drive.** SKILLSINPUT.AI packages AI-powered career tools, job search, skills intelligence, career roadmaps and resume building, as a hosted MCP server at `https://mcp.skillsinput.ai/mcp`.

```
Server type: Remote (Streamable HTTP)
Auth: account auth
Endpoint: https://mcp.skillsinput.ai/mcp
Tools: job search, skills intelligence, career roadmaps, resume building
Pricing: vendor pricing (skillsinput.ai)
Category: Business Operations / Career
Built by: SKILLSINPUT.AI (skillsinput.ai)
```

## Why This Matters for Operators

Every operator eventually sits on both sides of the hiring table: running their own search or staffing their own team. The skills-intelligence angle matters because it benchmarks a candidate or a job description against market data instead of vibes, and the roadmap tool turns a gap analysis into a plan an assistant can track.

For solo operators, the resume and search tools remove the friction of maintaining job-hunt materials; for hiring managers, the same tools work from the other direction when drafting role requirements.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Job search | Find and filter open roles for a target profile |
| Skills intelligence | Benchmark skills against market demand |
| Career roadmaps | Build step-by-step development plans |
| Resume building | Draft and refine application materials |

Tool names are served from the endpoint; the table reflects the vendor's published capability set.

## Installation

```bash
npx add-mcp 'https://mcp.skillsinput.ai/mcp'
```

The install command covers Claude Code, Codex, Cursor and other MCP clients.

## Configuration

```json
{
  "mcpServers": {
    "skillsinput": {
      "type": "http",
      "url": "https://mcp.skillsinput.ai/mcp"
    }
  }
}
```

## Business Relevance

- **Operators running a search** keep materials current and searches automated
- **Founders hiring** benchmark role descriptions against skills-market data
- **Managers** turn team skill gaps into tracked roadmaps
- **Agencies** add career tooling to client service offerings

## Integration with CorpusIQ

SkillsInput pairs with the CorpusIQ CRM connectors for the hiring loop: candidate and role data in HubSpot or Close CRM stays the system of record while SkillsInput supplies the career-side intelligence an assistant uses to draft outreach and screen roles.

For an operator running their own search, the CorpusIQ Calendar connector schedules the interviews while SkillsInput keeps the materials and roadmap current, so the whole motion lives in one agent session.

## Limitations

- New listing, no track record yet
- Tool names are not published; live catalog is served from the endpoint
- Pricing not disclosed on the directory listing
- Consumer-grade career scope rather than enterprise HR

## FAQ

### Is this an HR system?

No. It is career tooling, job search, skills intelligence, roadmaps and resume building, exposed as agent tools, not a payroll or ATS replacement.

### What is the MCP endpoint?

https://mcp.skillsinput.ai/mcp, installable with npx add-mcp into Claude Code, Codex, Cursor and more.

### Can it help with hiring?

Yes. The skills-intelligence tools work from the employer side too when benchmarking role requirements against market demand.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
