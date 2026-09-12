---
title: "FormLM MCP - AI Form and Assessment Building for Agents"
description: "Official CLI and MCP server for the FormLM platform. Agents build smart forms, scoring quizzes and evaluation reports from natural language with six layered tools (generate, snapshot, skill, exec) and six SKILL.md domain resources. npm package, MIT, stdio."
category: "Productivity"
stars: 1 (new repo)
added: 2026-09-12
source: "mcp.so feed (formlm slug) + GitHub formlm/cli"
relevance: ★★
tags: [forms, surveys, assessments, quizzes, document-generation, productivity, stdio, npm]
---

# FormLM MCP

**Official CLI and MCP server (npm, stdio)** - lets an agent build and manage complete FormLM apps with no UI. Natural-language instructions become smart forms, scoring quizzes and professional evaluation reports, end to end: form design, scoring dimensions, report pages, AI styling, publishing and expert chat interpretation.

```
Server type: Local (stdio via `formlm-cli mcp`; platform calls at formlm.me)
Auth: FormLM token (FORMLM_TOKEN) or in-chat auth_login (email + password)
Transport: stdio (npm CLI, Node >= 18)
Tools: 6 layered tools + 6 SKILL.md resources
Package: @formlm/cli (npm, v0.2.1)
Source: github.com/formlm/cli (MIT, pushed Aug 2026)
Category: Productivity
Built by: FormLM (formlm.me)
```

## Tools (6)

| Tier | Tool | Purpose |
|---|---|---|
| 0 | auth_login | Log in with token or email + password |
| 0 | auth_status | Check the current session |
| 1 | formlm_generate | Build a complete app from natural language via the server-side AssessAgent pipeline (form, scales, report pages, visual styling) |
| 2 | formlm_snapshot | Aggregate state of all modules (form/scale/connect/report/expert/share), JSON or token-efficient markdown |
| 2 | formlm_skill | Fetch a module's SKILL.md domain knowledge (P0 constraints, command templates) |
| 3 | formlm_exec | Execute any whitelisted CLI command directly (fields, scales, reports, styling, publishing) |

## Resources (6)

`formlm://skills/form` (field rules), `formlm://skills/scale` (dimension and scoring rules), `formlm://skills/connect` (page styling), `formlm://skills/report` (widget types and logic), `formlm://skills/expert` (AI interpretation config), `formlm://skills/share` (publish rules).

## Connection

1. Install the CLI: `npm install -g @formlm/cli` (Node >= 18).
2. Add the server to your MCP client config:

```json
"formlm": {
  "command": "formlm-cli",
  "args": ["mcp"],
  "env": { "FORMLM_TOKEN": "..." }
}
```

3. On macOS/Linux desktop clients, add the full terminal PATH to the server env (the vendor's INSTALL.md step 4) or the client fails with command-not-found. If FORMLM_TOKEN is omitted, the agent authenticates via the auth_login tool in chat.
4. Ask in plain language, for example: "Create a workplace stress assessment with 10 questions, 3 dimensions and detailed score interpretations."

## Why This Matters for Operators

Surveys, lead-capture forms, quizzes and scored assessments are everyday operator work that normally means clicking through a form builder. FormLM moves the whole lifecycle into the agent chat: brief the assessment, get a published app with fill-in, editor and data URLs (app urls), scoring scales with ranges and polarity, report pages with chart widgets and logic rules, and an optional AI expert chat that interprets responses. The smart generate pipeline includes visual styling, so one command produces a shareable, branded assessment.

## Integration with CorpusIQ

CorpusIQ supplies the business data (CRM records, ecommerce metrics, analytics); FormLM supplies the structured collection front end. A growth or HR agent can draft a customer-feedback assessment in FormLM, publish it, then pull responses alongside CorpusIQ pipeline data to tie scores to business outcomes. FormLM is a stdio local server, so it coexists with CorpusIQ's remote OAuth connector in the same client without port or auth conflicts.

## Verification (Sep 12, 2026 midday supplement)

Directory drift: the mcp.so feed block (slug formlm, listed Aug 6) now links to a 404 detail shell, but the server itself is live and current - GitHub formlm/cli (MIT, pushed Aug 3, 2026) and npm @formlm/cli v0.2.1 both verified this sweep, and the README documents the v0.2 MCP redesign (34 flat tools replaced by 6 layered tools plus 6 resources). No remote endpoint to probe; the npm package is the authoritative install path.

## Limitations

- Local stdio install (Node >= 18) rather than a hosted remote endpoint.
- A formlm.me account is required for server-side generation; tool use beyond auth is account-scoped.
- Young project: single-digit GitHub stars, first MCP architecture redesign landed in v0.2.0 (Aug 2026).

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [ClauseAI MCP - Startup Legal Document Generation for Agents](/hermes/mcp/servers/external/clauseai-mcp/)
- [BusyMail MCP - Human-Approval Email over MCP](/hermes/mcp/servers/external/busymail-mcp/)
