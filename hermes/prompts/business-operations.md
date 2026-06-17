---
title: Business Operations Prompts for Hermes Agent — Email, Meetings & Project Planning
description: Hermes Agent business operations prompts for email communication, meeting management, project planning, and task organization. Replace bracketed text with your team context, tools, and workflow preferences.
category: prompts
tags: [hermes-agent, prompts, business-operations, email, meetings, project-planning, task-management, workflow]
last_updated: 2026-06-16
---

# Business Operations Prompts — Email, Meetings & Project Planning

---

## Email Drafting

### Professional Correspondence

```
Draft a professional email with the following context:

Sender role: [YOUR ROLE]
Recipient: [RECIPIENT ROLE AND RELATIONSHIP]
Purpose: [INFORM/REQUEST/FOLLOW-UP/INTRODUCTION/APOLOGY]
Key points to communicate:
1. [POINT 1]
2. [POINT 2]
3. [POINT 3]

Tone: [FORMAL/FRIENDLY/URGENT/DIPLOMATIC]
Desired outcome: [WHAT YOU WANT THEM TO DO AFTER READING]

Structure:
- Clear subject line (under 60 characters)
- Friendly opening
- Concise body (3 short paragraphs max)
- Specific ask or next step
- Professional closing

Include a "read this if you only have 10 seconds" one-sentence summary at the top.
```

### Difficult Conversation Email

```
Help me draft a diplomatic email for a sensitive situation:

Context: [DESCRIBE THE SITUATION — e.g., project delay, scope change, pricing increase]
Relationship importance: [CRITICAL/IMPORTANT/TRANSACTIONAL]
What cannot be compromised: [NON-NEGOTIABLE POINTS]
What I'm willing to offer: [CONCESSIONS OR ALTERNATIVES]

Tone guidelines:
- Empathetic but clear
- No passive-aggressive language
- Own the message (use "I" not "we" for personal accountability)
- Provide a path forward, not just bad news

Draft two versions: one more direct, one with more cushioning language. Note which situations each is appropriate for.
```

### Weekly Update Template

```
Create a standardized weekly update email template for [TEAM/PROJECT].

Sections:
1. Top-line: One sentence on the most important thing that happened
2. Wins (3 bullet max) — celebrate progress and people
3. Blockers — what's stuck and who can help
4. Priorities for next week (ranked, 3-5 items)
5. Metrics snapshot — [2-3 KEY NUMBERS] with arrows showing direction
6. Asks — specific requests of the reader

Make it scannable in under 60 seconds. Include guidance on what NOT to include (status on everything, excessive detail, blame language).
```

---

## Meeting Summaries

### Post-Meeting Recap

```
Summarize this meeting transcript/notes into a structured recap:

[PASTE NOTES OR TRANSCRIPT]

Meeting: [MEETING NAME]
Date: [DATE]
Attendees: [LIST]
Duration: [LENGTH]

Format:
- Decisions made (numbered, with who owns each)
- Action items (table format: task, owner, deadline)
- Open questions (questions raised but not resolved)
- Next meeting: [DATE/TIME] with proposed agenda
- Key discussion points (max 5 bullet points, one sentence each)

Distribute within [X] hours of meeting end. Keep total length under [N] words.
```

### Meeting Preparation Brief

```
Create a meeting preparation brief for my [MEETING TYPE] with [WHO].

Background: [WHAT LED TO THIS MEETING]
My goals:
1. [GOAL 1]
2. [GOAL 2]

Their likely perspective: [WHAT YOU KNOW ABOUT THEIR POSITION]

Include:
- Opening statement (first 60 seconds — set the tone and purpose)
- Key talking points with supporting data
- Anticipated objections and my responses
- Questions to ask them
- What "success" looks like at the end of this meeting
- BATNA (best alternative to negotiated agreement)
```

---

## Project Planning

### Project Kickoff Brief

```
Create a project kickoff document for [PROJECT NAME].

Context:
- Problem being solved: [1-2 SENTENCES]
- Stakeholders: [ROLES AND NAMES]
- Timeline: [START DATE] to [TARGET COMPLETION]
- Budget/Resources: [ANY CONSTRAINTS]

Sections:
1. Executive summary (3 sentences max)
2. Success criteria (measurable, 3-5 items)
3. Scope: in-scope and explicitly out-of-scope
4. Milestones with dates and deliverables
5. Risk register: top 5 risks with mitigations
6. Communication plan: who gets updated when and how
7. Decision rights: who can approve what

This should fit on 2 pages and be usable as the project's north star document.
```

### Sprint/Iteration Planning

```
Given this backlog, plan a [DURATION]-week sprint for a [TEAM SIZE]-person team.

Team composition: [ROLES AND SENIORITY]
Velocity history: [STORY POINTS PER SPRINT]
Backlog items:
[LIST PRIORITIZED ITEMS WITH ESTIMATES]

Output:
1. Sprint goal (one sentence)
2. Selected items with rationale for inclusion/exclusion
3. Capacity check: person-days available vs estimated
4. Dependency mapping: what must finish before what
5. Stretch goals if the team finishes early
6. Items deferred to next sprint with reasoning

Flag any items where estimates seem unreliable and suggest spike tasks.
```

---

## Task Management

### Task Breakdown

```
Break down this high-level initiative into actionable tasks:

Initiative: [DESCRIPTION]
Definition of done: [WHAT "FINISHED" MEANS]

For each task provide:
- Title (action-oriented, starts with verb)
- Description (1-2 sentences)
- Estimated effort ([HOURS/STORY POINTS])
- Dependencies (must complete task #[X] first)
- Assignee role (not name — describe the skills needed)
- Acceptance criteria (how to verify it's done)

Organize tasks into phases (phase 1, 2, 3) based on dependency order and value delivery. Identify the MVP threshold — the minimum set of tasks that delivers standalone value.
```

### Daily Standup Format

```
Generate my daily standup update for [TEAM/CHANNEL].

Context from yesterday:
[WHAT I WORKED ON]

Today:
[PLANNED WORK]

Blockers:
[CURRENT BLOCKERS]

Format as:
- Yesterday: [1-2 bullets, max 40 words total]
- Today: [1-2 bullets, max 40 words total]
- Blockers: [0 or 1 items — only if I need help]

The update should take under 30 seconds to speak aloud. Be specific about what shipped, not what I "worked on."
```

---

## General Tips

- **Specify the recipient relationship.** "My peer" vs "my skip-level manager" produces meaningfully different emails.
- **Give the model your brand voice examples.** Paste 2-3 emails you've written that you like as style references.
- **For sensitive communications, always review.** AI drafts are starting points — add your human judgment.
- **Chain operations prompts.** Use "task breakdown → sprint plan → standup update" as a connected workflow.


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
