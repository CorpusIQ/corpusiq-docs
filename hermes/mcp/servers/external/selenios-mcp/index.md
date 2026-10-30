---
title: Selenios MCP - Recruiting Pipelines Inside Chat
description: "Remote MCP server for Selenios recruiting: 45 tools over candidates, interview transcripts, pipelines and hiring metrics, scoped to your role."
category: Recruiting & HR
stars: n/a (new listing)
added: 2026-10-29
source: "mcp.so GitHub issue #6408"
relevance: ★★★
tags: [recruiting, ats, hr, hiring, candidates, interview-transcripts, oauth, remote-mcp, latam]
last_updated: "2026-10-29"
---

# Selenios MCP

**A recruiting platform exposed to the agent with the same permissions the person already has in the app - so a shortlist, a stage move and a rejection reason are one instruction instead of five screens.**

Selenios is an AI recruiting platform used by HR teams across Latin America. Its MCP server sits at `https://back.selenios.com/api/mcp` over Streamable HTTP, answers a bare `initialize` with **HTTP 401** `{"error":"invalid_token","error_description":"Missing Authorization header"}`, and publishes a protected-resource document naming the resource, the authorization server and a single scope, `mcp:tools`.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration (no API keys)
Endpoint: https://back.selenios.com/api/mcp
Scope: mcp:tools
Tools: 45 (vendor-published count)
Built by: Selenios (selenios.com)
```

## Why This Matters for Operators

Hiring is the one process where the data lives in the tool and the judgement lives in the conversation, and every attempt to join them has meant an export. You pull the candidate list, paste three CVs, describe the vacancy from memory, and the assistant answers well about a system it cannot see.

The root cause is that an ATS holds records with permissions attached - assigned vacancies, confidential searches, role-restricted views - and a paste has none of that. This server keeps the permissions and moves the interface. Read the vendor's own line: an assistant connected here cannot do anything the user could not do in the app, and a tool the role cannot use is never even offered to the assistant.

The result for a small team is that screening questions get answered at the speed of the conversation: who mentioned SAP in this week's interviews, which candidates cleared 80 and have not been contacted, how many days the technical stage really takes. The same surface then acts - tag, note, email from a template, move stage, reject with a reason, recalculate a score - and every write runs the platform's own business rules and integrations.

## Tools and Capabilities

The vendor documents **45 tools** for external assistants, grouped by intent rather than by endpoint.

| Capability | What it covers |
|---|---|
| Candidate search | Text, semantic and natural-language search by name, email, LinkedIn or stage |
| Vacancy shortlist | Candidates per vacancy ordered by AI score, with per-criterion breakdown and disqualifying requirements |
| Candidate profile | Full profile with CV link and the answers from the application form |
| Interviews | Meetings, transcripts with speaker identification, interview reports, and keyword search across every transcript at once |
| Vacancy data | Openings, job descriptions, pipelines, average days per stage, screening configuration, organisation KPIs |
| Outreach | Contact templates, rejection reasons, and candidate email replies not yet read |
| Pipeline writes | Tag, note, send email from free text or a template, move stage, reject, recalculate score |
| Vacancy writes | AI vacancy draft, create or update a job description, change status, set closing date, configure multiposting |
| Pipeline design | Add and reorder stages, edit screening questions and form fields, set whether the Career Site shows the salary range |

## Connecting

1. Add a custom connector in the assistant and paste the Selenios MCP URL.
2. Sign in with the Selenios account in the browser tab that opens.
3. Return to the conversation; only the tools the role allows are offered.

In ChatGPT Business or Enterprise and Claude Team or Enterprise, a workspace administrator may have to enable custom connectors before any individual can connect an account.

## Permission Model

| Rule | Behaviour |
|---|---|
| Same permissions as the app | Each tool requires the permission of its in-app equivalent |
| Company isolation | Every query is limited to the caller's own company |
| Assigned vacancies | Hiring managers and restricted roles see only assigned vacancies |
| Confidential searches | Invisible from the assistant when the user is not on them, notes and candidates included |
| Writes | Run the same business rules and integrations as the interface |

## Limits Worth Knowing

The endpoint sits behind OAuth, so this pass verified the authorization boundary and the scope rather than enumerating the tool list. The 45-tool count is the vendor's published figure from 21 October 2026, not a count this catalogue drove.

Discovery has a path quirk: `/.well-known/oauth-protected-resource` returns **200** at the host root, while the `/mcp` suffix form returns **404**. A client that only guesses the suffix will fail discovery against a server that works.

Documentation and the product surface are Spanish-first. An English-language reader can follow the tool descriptions but the setup guide and prompt examples are written for Spanish-speaking teams.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [All sweep reports](/hermes/mcp/sweeps/)

## FAQ

### What does the Selenios MCP server do?

It connects Claude, ChatGPT or any MCP client to a Selenios recruiting account, so the assistant reads candidates, interview transcripts, pipelines and hiring metrics, and performs pipeline and vacancy actions with the user's own permissions.

### Does it need an API key?

No. Authentication is OAuth 2.1 with dynamic client registration. The person signs in with their Selenios account in a browser tab and the connection operates in their name.

### Can the assistant see more than the user can?

No. Each tool requires the same permission as the equivalent in-app action, tools the role cannot use are not offered, queries are limited to the caller's company, and confidential searches the user is not part of stay invisible.

### Which assistants can connect to it?

Any client that supports MCP connectors or custom connectors, including Claude and ChatGPT. In enterprise workspaces an administrator may need to enable custom connectors first.

### What actions can it take, not just read?

Tag and note candidates, send email from free text or a template, move stage, reject with a reason, recalculate AI scores, create and edit vacancies, add pipeline stages and edit screening questions and form fields.
