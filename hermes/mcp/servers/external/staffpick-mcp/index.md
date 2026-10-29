---
title: "StaffPick MCP - Hire Tested Remote Staff From Chat"
description: "Search tested remote workers with real test scores, benchmark monthly pay by role and hours, and request an intro without leaving the conversation."
category: Business Operations
stars: ★★★ (200 keyless, 5 tools verified)
added: 2026-10-28
source: "live probe of https://staffpick.ai/api/mcp answering HTTP 200 keyless on initialize as staffpick 2.2.0 with a full tools/list of 5 tools, plus https://staffpick.ai/mcp returning HTTP 401 with resource_metadata for the full OAuth surface, and chatmcp/mcpso issue #6333"
relevance: ★★★
tags: [hiring, remote-work, staffing, salary-benchmark, hr, keyless, oauth, remote-mcp]
last_updated: "2026-10-28"
---

# StaffPick MCP

**A job post is a guess about the market. The number that decides whether the hire works is what the same role actually pays somewhere else.**

```
Server type: Remote (Streamable HTTP), two endpoints
Search:      https://staffpick.ai/api/mcp (no sign-in, 5 tools)
Full:        https://staffpick.ai/mcp (OAuth 2.1 with PKCE)
Server:      staffpick 2.2.0
Tools:       5 at tools/list on the search endpoint
Coverage:    Remote workers across support, bookkeeping, development and more
```

## Why This Matters for Operators

Hiring a remote assistant or bookkeeper is the first operational hire most small businesses make and the one with the least reliable market information. Rates quoted by an agency, a rate seen in a forum and a rate a competitor pays are three different numbers, and none of them is attached to a person who was tested.

This server turns three real questions into tools: who fits a role and what did they actually score, what does this role pay at these hours, and what should the brief say. `salary_benchmark` returns the 25th to 75th percentile of monthly pay for a role at the given weekly hours, computed from the rates of approved profiles on the platform rather than from a survey.

It is a different slice from what the catalogue already holds. `Ruzora` places LATAM engineers with compliance built in, `Ashton & Forge` lists vetted AI implementation agencies and the `lemon-io` entry hires senior developers. None of them scores candidates on a graded test and prices the role at the same time.

## What It Returns, Verified

A bare `initialize` on `https://staffpick.ai/api/mcp` returned **HTTP 200** with no credential as `staffpick` **2.2.0**, declaring the MCP Apps UI extension, and `tools/list` returned **five tools**:

- **`search_talent`** searches tested remote workers across virtual assistants, support, bookkeeping, developers and more, and every result carries the test scores taken on StaffPick rather than self-reported skills.
- **`get_talent`** returns one anonymised profile: summary, skills, tools, languages, availability, the business hours covered, rates, and test results with dates, including a CEFR band for English.
- **`salary_benchmark`** returns typical monthly pay in USD for a role at given weekly hours, as the 25th to 75th percentile from real approved profiles, and says `not enough data` rather than inventing a figure.
- **`create_role_brief`** takes the hiring request in the operator's own words, for example part-time bookkeeper who knows Xero, mornings in Sydney, under $1,000 a month, and turns it into a structured brief.
- **`request_intro`** returns a StaffPick link the human opens to request an introduction. It deliberately never returns contact details, so a conversation with a candidate cannot start without the operator acting.

## Limits Worth Recording

The search endpoint is read-only and anonymous, and it is the surface this entry verified. The signed-in endpoint at `https://staffpick.ai/mcp` requires OAuth 2.1 with PKCE, answered the probe with **HTTP 401** and a `resource_metadata` pointer, and is where the platform's own actions live. Candidacy rates, availability and scores describe the platform's own pool, so the benchmark is a real market signal and not the whole market. `request_intro` means the platform owns the introduction, which is the opposite of a lead list and should be read that way before someone expects contact details.

## FAQ

### Do I need an account to try it?
No. The five search and benchmark tools answer without a credential, which is how this entry was verified.

### Where do the salary numbers come from?
The rates of real approved StaffPick profiles, returned as a 25th to 75th percentile for a role at a given number of weekly hours in USD, with an explicit not-enough-data answer when the sample is thin.

### Does it hand over candidate contact details?
No. `request_intro` returns a link the operator opens to request an introduction, and the tool description states it never returns contact details.

### Is this a recruitment agency?
It is a marketplace of tested remote workers with a search and intro surface exposed to agents. The testing and the intro are the platform's, and the hiring decision stays with the operator.

### How is this different from the other hiring entries here?
`Ruzora` is LATAM engineering placement with compliance, `Ashton & Forge` is a directory of AI implementation agencies and `lemon-io` targets senior developers. This one carries graded test scores and a salary benchmark for general remote roles.
