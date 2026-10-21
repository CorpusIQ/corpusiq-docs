---
title: "UXArmy MCP - Run User Research From the Assistant"
description: "UXArmy turns a study plan into a live usability test, survey or card sort, recruits from its panel after approval and returns themes and quotes."
category: Design & Product
stars: n/a (hosted, no public repo)
added: 2026-10-21
source: "mcpservers.org /all page 1 (card uxarmy-com-mcp-server)"
relevance: ★★★
tags: [user-research, usability-testing, surveys, participant-recruitment, product-management, voice-of-customer, remote-mcp]
---

# UXArmy MCP

**Most research MCP servers read studies you already ran. UXArmy runs a new one: plan it, price the panel, launch it after you say so, and get the themes and quotes back in the same conversation.**

```
Server type: Remote (Streamable HTTP) at https://app.uxarmy.com/mcp
Auth: sign in to the UXArmy account on first connect
Live check: POST initialize returned HTTP 401 Unauthorized without a session
Panel: 7M+ participant network, targeted by country, age and device; panel credits bought separately
Plans: every plan including Free; every plan can also invite its own participants
Vendor: UXArmy (uxarmy.com)
```

## Why This Matters for Operators

Product decisions rot when research is a quarterly project. The question is already formed in the chat where the work is happening, and by the time it reaches a research team it has been rewritten twice and the answer arrives after the decision shipped. The gap is not analysis, it is the round trip from a question to a live study with real participants.

UXArmy closes that round trip inside the assistant, and it keeps the approval in the middle. The agent drafts the study, the screener and the targeting, then stops; the study opens to participants only after a person says launch. Results come back as themes, sentiment, verbatim quotes and per-participant detail rather than a dashboard to interpret.

## What It Actually Does

Reading the research already done: search projects and studies by description with no IDs, extract themes, sentiment and exact quotes from every study type, flag studies that are below target or have tasks nobody reached, pull interview transcripts with speaker labels and timestamps, return original-language transcripts so the assistant translates without losing the quotes, and open one participant to see their device, every task answer, the tasks they never reached and a replay link.

Running new research: recommend the method that fits the question (usability test, survey, card sort, tree test or user interview), build a survey from a prompt or notes, turn a study plan into a usability study with scenario, screener, tasks, rating scales and open questions, trim tasks to a target duration and flag setup risks, set panel targeting by country, age and device, draft screener questions from niche criteria, and launch only on approval.

Account work is included as well: workspaces, roles, team and projects, with AI features enabled only on confirmation.

## Installation

```
Add a custom connector in Claude or ChatGPT pointing at:
https://app.uxarmy.com/mcp
```

The vendor lists setup for Claude, ChatGPT, Cursor and Gemini CLI. Connecting is free; the account signs in and the study work happens against that account's plans and panel credits.

## Where It Sits in This Catalog

The catalogued usability entry, Uxia, simulates usability testing and returns research over tests you have already run. UXArmy is the other half: real participants from a 7M+ panel, real screener questions, and a launch the assistant cannot perform alone. The vendor's own comparison puts UserTesting in the same recruit-and-launch category but restricted to select early access teams.

## FAQ

### Can the agent launch a study on its own?

No. The study goes live only after the operator confirms the launch in the conversation. Recruitment targeting and screener drafts are prepared before that point.

### Do I need panel credits to use it?

Only for recruiting from the UXArmy panel. Every plan including Free can invite its own participants, and panel recruiting draws on credits bought separately from the plan.

### What comes back from a finished study?

Themes, sentiment and verbatim quotes per study, transcripts with speaker labels and timestamps in the original language, and per-participant detail including device, task answers, unreached tasks and a replay link.

## See Also

- [Design and product servers](/hermes/mcp/servers/external/) in this catalog
- [CorpusIQ connectors](/docs/hermes/mcp/servers/) for read-only business data behind the same questions
