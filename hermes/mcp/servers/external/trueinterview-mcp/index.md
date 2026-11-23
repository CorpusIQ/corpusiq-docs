---
title: "TrueInterview MCP - Interview Questions by Company and Round"
description: "Forty-one tools and thirteen OAuth scopes for interview questions by company and round; every call refused the submitter's no-sign-in claim."
category: "Career & Hiring"
stars: n/a (vendor-hosted, closed source)
added: 2026-11-22
source: "chatmcp/mcpso submission #7837 filed 2026-11-22T17:24:29Z; keyless initialize and tools/list, four tools/call probes and the protected-resource document on 2026-11-22"
relevance: ★★★
tags: [interview-prep, hiring, job-search, oauth, remote-mcp, career]
last_updated: "2026-11-22"
---

# TrueInterview MCP

**Remote MCP server (Streamable HTTP) - the first interview-preparation surface in this catalogue.** A candidate's agent can read company intelligence, search a bank of interview questions by company, type and difficulty, pull a job feed, then tailor a resume, draft answers and track the application. Everything past discovery needs the candidate's own sign-in.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://trueinterview.io/api/mcp
Server:      trueinterview 1.26.0, protocol 2025-06-18
Tools:       41
Registry:    io.trueinterview/trueinterview 1.26.0, published 2026-11-22T17:10:44Z
Auth:        OAuth 2.1, 13 scopes; no public repository
```

## Why This Matters for Operators

Interview preparation is where a job search either converts or stalls, and the work is specific: which questions this company asks at this round, what the company actually does, and whether the resume answers the posting. A candidate asking a general assistant gets generic advice. A surface that holds the question bank and the company record can answer with the thing that was asked.

This guide is deliberately thin on tool output, because there is no keyless tool output to show. What it can document is the shape of the surface, the full scope list, and one submitter claim that measurement disproved.

## Measured Behaviour

Probed on 2026-11-22 from a clean client with no credentials.

| Probe | Result |
|---|---|
| `initialize` | **200**, `trueinterview 1.26.0`, protocol `2025-06-18` |
| `tools/list` | **200**, **41** tools, no session id issued |
| `search_questions` (`distributed systems`, company `google`) | **401** `{"error":"unauthorized"}` |
| `get_company_intel` (`stripe`) | **401**, same body |
| `search_jobs` (`machine learning engineer`, remote, 7 days) | **401**, same body |
| `search_site_content` (`system design`) | **401**, same body |
| `/.well-known/oauth-protected-resource/api/mcp` | **200**, 13 scopes, issuer `https://trueinterview.io` |

Every 401 carried the same challenge header, which is what makes this a documented gate rather than a broken server:

```text
WWW-Authenticate: Bearer scope="jobs:read intel:read prep:read prep:write
  resume:read profile:write tracker:read tracker:write contacts:read
  contacts:write history:read notes:read notes:write"
  resource_metadata="https://trueinterview.io/.well-known/oauth-protected-resource/api/mcp"
```

### The submission claimed four tools work without signing in

The queue entry states that *company intel, question search, site search and job search work without signing in*. All four were called without a token and all four returned **401**. The guide records the measurement, not the claim: treat the whole surface as gated until a signed-in call proves otherwise. This is the discovery-open, execution-gated tier - the tool list is real and readable, the data behind it is not.

## What the 41 Tools Cover

The inventory is the useful part, because it shows what an operator can wire before paying anything:

```text
Prep         search_questions (company, type, difficulty, page, limit)
             get_prep_plan, get_playbook (task)
Intel        get_company_intel (company), search_site_content (kinds, company)
             get_trueinterview_resource (url_or_id, kind)
Jobs         search_jobs, recommend_jobs, get_job, skip_job
Application  prepare_application, tailor_resume, write_cover_letter
             generate_application_documents, draft_answers, match_resume_to_job
             screen_jobs, report_application, prepare_application
Tracker      list_applications, track_application, update_application
             get_application_checklist, update_job_search, update_application_answers
Contacts     list_contacts, find_contacts, update_contact
Profile      get_resume, update_resume, import_resume
Notes        list_context_notes, save_context_note, delete_context_note
History      list_my_conversations, get_my_conversation, get_my_progress
Meta         get_account, claim_setup_handoff, report_setup_progress,
             report_mcp_issue, get_playbook
```

The write tools matter as much as the reads: `update_resume`, `tailor_resume` and `draft_answers` change the candidate's own documents, which is why `prep:write`, `profile:write` and `tracker:write` are separate scopes instead of one blanket grant.

## Setup

`claude mcp add --transport http trueinterview https://trueinterview.io/api/mcp` then sign in when the client prompts. The OAuth flow is dynamic client registration with PKCE; the protected-resource document above tells the client which scopes to request.

## What It Cannot Do

- **No keyless read of anything.** Initialize and the tool list only.
- **No public source repository.** The submission says so: closed-source hosted service. Nothing here can be reviewed, only driven.
- **No price is published in the payload.** The account endpoint is gated, so plan terms are a website question, not a measured one.

## See Also

- [Jobyap MCP - Job Postings With a Discussion Thread](/hermes/mcp/servers/external/jobyap-mcp/) - the job feed half, keyless and measured
- [Level Jobs MCP - Job Postings by Function](/hermes/mcp/servers/external/level-jobs-mcp/) - a second postings source
- [Phonotheca MCP - Interview Transcript Search for Agents](/hermes/mcp/servers/external/phonotheca-mcp/) - interview content as research material
