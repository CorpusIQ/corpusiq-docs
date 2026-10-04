---
title: PhoneScreen MCP - AI Hiring and Screening
description: Remote MCP that scores resumes, runs AI phone screens in 34 languages, and checks references, reporting every score back to the assistant for the hiring team to decide.
category: Business Operations
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [hr, hiring, recruiting, resume-screening, interviews, references, remote-mcp, oauth]
---

# PhoneScreen MCP

**Remote MCP server (Streamable HTTP, account auth)** - PhoneScreen's server lets an assistant run hiring from a chat. It drafts roles from a job post, scores stacks of resumes, invites candidates to phone screens in 34 languages, places AI screening calls on demand, reads back every score, and checks references. The assistant reports; the hiring team decides.

```
Server type: Remote (Streamable HTTP)
Auth: PhoneScreen account
Endpoint: https://app.phonescreen.ai/mcp
Tools: Role creation, resume scoring, screen invitations, AI phone calls, score reading, reference checks
Pricing: PhoneScreen plan
Category: Business Operations
Built by: PhoneScreen
```

## Why This Matters for Operators

Hiring is a backlog problem: resumes pile up, screens wait on calendars, and references rarely get called. PhoneScreen's mechanism is to **make the pipeline conversational**: paste a job post and it drafts the role and screening questions; attach resumes ten at a time and each returns a fit score with reasons; candidates screen 24/7 in their own time, and references are texted and called automatically with the answers scored.

For founders and hiring managers, that turns days of coordination into a single thread where the assistant surfaces the strongest candidates first, with reasoning, flags and transcripts attached. Decisions stay with the human; the legwork does not.

**The key advantage is an end-to-end screening pipeline that runs from a chat and reports back scored, reasoned results.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Create role | Drafts a role and five screening questions from a job post |
| Score resumes | Returns a fit score out of 100, a Yes/Maybe/No, and the reasons |
| Invite to screen | Emails candidates a phone-screen link, available 24/7 in 34 languages |
| Call now | Places an AI phone screen immediately to US and Canada numbers |
| Read scores | Returns each answer scored out of 100 with reasoning and flags |
| Check references | Texts for references, then calls each one and scores what they say |

## Installation

```bash
claude mcp add --transport http phonescreen https://app.phonescreen.ai/mcp
```

Works with ChatGPT, Claude and any MCP-capable assistant; setup follows the standard custom-connector flow.

## Configuration

```json
{
  "mcpServers": {
    "phonescreen": {
      "type": "http",
      "url": "https://app.phonescreen.ai/mcp"
    }
  }
}
```

Sign in to the PhoneScreen account the assistant should act within; results land in the PhoneScreen dashboard.

## Business Relevance

- **Founders hiring their first team** can screen a stack of resumes in one prompt.
- **Recruiters** can invite, screen and shortlist without leaving the assistant.
- **Ops and HR leads** get reference checks that actually happen, scored and logged.
- **Distributed teams** can screen candidates 24/7 in 34 languages.
- **Managers** can compare candidates on consistent fit scores rather than gut feel.

## Integration with CorpusIQ

PhoneScreen is the people layer beside CorpusIQ's business data. Where CorpusIQ's Stripe and GA4 connectors show revenue and pipeline, PhoneScreen covers the hiring side of growth, so an assistant can answer "can we staff this expansion?" by pairing headcount pipeline with revenue run-rate.

A composed workflow: read monthly revenue and pipeline from CorpusIQ connectors, ask PhoneScreen for the active candidate pipeline and scores, then have the assistant draft a hiring plan tied to the growth numbers. CorpusIQ reads the business; PhoneScreen reads the team being built around it.

## Limitations

- Requires a PhoneScreen account and plan.
- Immediate AI calling is limited to US and Canada numbers where offered.
- Phone screens and reference checks are automated, so review transcripts before deciding.
- Hosted and proprietary; no self-hosting.
- Vertical scope is hiring; not a general HRIS.

## FAQ

### Does PhoneScreen make the hiring decision?

No. It scores, screens and reports; the hiring team decides.

### What languages do the phone screens support?

34 languages, and candidates can screen on their own schedule.

### Can it check references too?

Yes. It texts the candidate for references, then calls each one and scores the responses.

### Which clients support PhoneScreen?

ChatGPT, Claude and any MCP-capable assistant.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
