---
title: "User Intuition MCP - Qualitative Research With Real People"
description: "Runs qualitative studies from any MCP client: recruit from a 4M consumer panel, AI-moderated voice, chat or video interviews."
category: Market Research / Customer Discovery
stars: ★★ (OAuth workspace, recruited panel)
added: 2026-10-28
source: "live probe of https://mcp.userintuition.ai/mcp returning HTTP 401 with the body invalid_token missing Authorization header, plus submission issue chatmcp/mcpso #6308, the vendor site userintuition.ai and the registry entry ai.userintuition/research"
relevance: ★★★
tags: [market-research, user-research, interviews, panel, qual, oauth, streamable-http]
last_updated: "2026-10-28"
---

# User Intuition Research MCP

**A business that stops talking to its customers starts guessing about them, and the guesses arrive as confident product decisions.**

```
Server type: Remote (Streamable HTTP), OAuth browser sign in
Endpoint:    https://mcp.userintuition.ai/mcp
Registry:    ai.userintuition/research
Panel:       4M+ recruited consumers
Interviews:  AI moderated voice, chat or video, 20 to 30 minutes
Languages:   80+
Repository:  github.com/user-intuition/skills
```

## Why This Matters for Operators

Quantitative data tells you what happened. Qualitative research tells you why, and it is the only input that catches the question your survey never asked. The reason most operators run it once a year instead of once a quarter is logistics: recruiting the right people, scheduling them, moderating consistently and synthesising the transcripts is a project, not a task.

This server collapses that project into a conversation. The agent plans the study first, from a brief, before anything is recruited, which means the research design is reviewable rather than implied. Then it recruits from a vetted panel of over four million consumers or from your own user list, and runs AI-moderated interviews across voice, chat or video in more than eighty languages.

## What It Returns, Verified

The endpoint is live and gated correctly: a bare `POST initialize` on `https://mcp.userintuition.ai/mcp` returned **HTTP 401** with the body `{"error":"invalid_token","error_description":"Missing Authorization header"}`, which is the right shape for an OAuth workspace surface rather than a fake-open endpoint.

The documented surface, from the submission and the vendor site:

- Design a study from a brief, with the agent planning it before recruitment
- Recruit participants from a vetted panel of over four million consumers, or from your own users
- Run AI-moderated interviews by voice, chat or video, typically twenty to thirty minutes each
- Work in more than eighty languages
- Start with no account, because the planning step comes first

The registry entry is `ai.userintuition/research`, and the published skills repository is `github.com/user-intuition/skills`.

## Limits Worth Recording

The panel is a recruiting channel, not a sample design. A vetted consumer panel answers a consumer question well and a B2B question badly, so the audience selection matters more than the moderation. AI moderation is also consistent in a way human moderators are not, which is a strength for comparability across interviews and a weakness when the conversation needs someone to break the script and chase an unexpected answer. Read the transcripts before acting on the synthesis, because the synthesis is a model's summary of a model's interview.

## FAQ

### Do I need an account to start?
No. The agent plans the study first, from a brief, and the account comes in when you recruit and run interviews.

### Can I interview my own users instead of the panel?
Yes. Recruitment works from a vetted panel of over four million consumers or from your own user base.

### What interview formats does it run?
Voice, chat or video, AI-moderated, typically twenty to thirty minutes per participant, across more than eighty languages.

### Is this a substitute for a survey?
No, it is the other half. A survey tells you how many, this tells you why, and the useful quarter is one where both were run against the same question.
