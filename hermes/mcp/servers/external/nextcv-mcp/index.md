---
title: "NextCV MCP - CV Scores and Job Keyword Gaps"
description: "A keyless CV checker that scores structure and ATS fit, then names the job-ad keywords a CV is missing, in English, Swedish and French."
category: "HR and Recruiting"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-25
source: "Submission chatmcp/mcpso #8088 filed 2026-11-25T17:19:04Z; official registry record net.nextcv/cv-tools 1.0.0 published 2026-11-25T13:58:13Z; keyless initialize, a two-tool tools/list and eight tools/call requests driven against https://nextcv.net/api/mcp on 2026-11-25"
relevance: "★★☆"
tags: [careers, hiring, resume, cv, ats, keywords, multilingual, keyless, remote-mcp]
last_updated: "2026-11-25"
---

# NextCV MCP

**A CV checker returns a number, and the number is the least useful thing in the answer.** What an operator or a job seeker can act on is the list underneath it: which rule failed, what to change, and which words the job ad used that the CV never mentions. NextCV answers both halves from one keyless endpoint, in English, Swedish and French, and it refuses to score a document it has not actually read.

```
Server type: Remote (Streamable HTTP, stateless, POST only)
Endpoint:    https://nextcv.net/api/mcp
Auth:        none, no key and no account
Registry:    net.nextcv/cv-tools 1.0.0, published 2026-11-25T13:58:13Z
Pricing:     free, no stated limit and no signup
Tools:       2, read from a keyless tools/list
```

No `Mcp-Session-Id` comes back on `initialize`, the transport answers `text/event-stream` over a single POST, and `Server` is `Vercel`. That is the stateless shape: every call stands alone, so an agent can fire `check_cv` in a pipeline without holding a session open.

## What the two tools do

| Tool | What it needs | What it answers |
| --- | --- | --- |
| `check_cv` | `cvText`, optional `locale` | a score out of 100, word count, estimated pages, and every issue with a severity, a problem and a fix |
| `match_cv_to_job` | `cvText`, `jobText`, optional `locale` | a score out of 100, a band, the keywords matched, the keywords missing, and how many keywords the ad carried |

Both return the payload twice, once as a JSON string in `content` and once as `structuredContent`, plus a `url` that lands on the site in the matching locale (`/en/cv-check?src=mcp`, `/fr/cv-check?src=mcp`, `/sv/cv-check?src=mcp`). The site link is the hand-off point for a person who wants to paste the CV themselves.

## The score is a rule list, and the rules are readable

Three CVs, same day, same endpoint:

| CV | Words | Score | Issues returned |
| --- | --- | --- | --- |
| Contact block, two roles with dates, five skills | 96 | **93** | 1 warning: looks too short |
| Same content plus a summary, bullet points and skills line | 134 | **91** | 2 warnings: no LinkedIn URL, looks too short |
| Contact block removed, dates removed, bullets removed | 94 | **64** | 2 critical: no email, no phone. 4 warnings: no LinkedIn URL, some roles missing dates, looks too short, no bullet points |

Read the first two rows together, because they are the finding. A longer, better-structured CV scored **two points lower**, and the reason is visible in the issue list: the second document happened to omit a LinkedIn URL, which the first also omitted. Warnings are worth a couple of points and criticals are worth far more. The gap between the first row and the third, **29 points**, is the whole weight of missing contact details plus its knock-on warnings.

**No email address and no phone number are the two criticals a CV cannot survive.** A CV in a document-management system with the header block stripped out is a real case: the text arrives, the person is uncontactable, and the score says so before a recruiter does.

## What the keyword match actually computes

`match_cv_to_job` on a CV and a job ad returned:

- **60, band medium**, 7 keywords matched, 4 missing, **11 keywords in the ad**.
- Matched: `dbt`, `python`, `snowflake`, `sql`, `tableau`, `analyst`, `operations`.
- Missing: `analytics`, `automation`, `forecasting`, `stakeholder`.
- And `7 + 4 = 11` holds exactly, so the missing list is the complement of the matched list rather than a separate ranking.

The same two tools on a stronger CV returned **94, band high**, 9 matched and 1 missing against **10 keywords in the ad**, again summing to the ad total.

**The score is not the ratio, and that is the measurement worth keeping.** Seven of eleven is **63.6%** and the tool reported **60**. Nine of ten is **90%** and the tool reported **94**. The weights are not published, so treat the score as an ordering signal and read `matchedKeywords` when the decision matters. Two documents can share a score with different gaps.

`missingKeywords` and `missingSkills` are returned as duplicate arrays with identical contents. Nothing breaks, but a client that concatenates both will double-count every gap.

## Where the extractor gives up

A short but perfectly readable job ad, **13 words**, describing an ICU nursing role, returned `keywordsInAd: 0`, `band: low`, an empty matched list and this note:

> *"No keywords could be taken from the job ad. Pass the full ad text, not only the title."*

The ad was not a title. It was a sentence with a role, a qualification and a shift. The extractor has a floor, and a short ad falls under it and returns a zero match rather than a partial one. For an agent, that zero is indistinguishable from "this CV shares nothing with the job" unless the note is read, so check `keywordsInAd` before reporting a low match as a verdict.

The CV side has the same kind of floor, stated plainly. Under **40 words** the server refuses to score in detail, returns `score: 0` and adds:

> *"Fewer than 40 words were found, so the CV was not scored in detail. Pass the full CV text."*

A CV that extracted badly from a PDF lands here, which makes the refusal the most useful answer the tool gives: zero with that note means fix the extraction, not the CV.

## Three locales, enforced by the schema

`locale` accepts `en`, `sv` and `fr` and nothing else. The enum is enforced at the protocol layer, so an unsupported code fails before the tool runs:

> *"Input validation error: Invalid arguments for tool check_cv: locale: Invalid option: expected one of "en"|"sv"|"fr""*

A missing required argument fails the same way and just as clearly, naming the field: `jobText: Invalid input: expected string, received undefined`. In `fr` and `sv` the issue text and the fix text are translated and the returned `url` changes with them, for example *"Votre CV semble trop court"* with the fix *"Détaillez davantage votre expérience et vos compétences"*.

## Limits measured this pass

- The vendor states `no AI model, no signup, nothing stored`. The stateless transport and the absence of any account or key are consistent with that, and the storage claim itself cannot be verified from outside.
- The score has no published rubric and no per-rule weights. Two documents at 91 and 93 are not meaningfully different; a gap of 29 points is.
- The 40-word floor and the short-ad floor both return a zero with an explanatory note rather than an error, so a client must surface the note or the zero will be read as a result.
- `match_cv_to_job` returns nothing about seniority, years of experience or education level. It is a vocabulary comparison, and a CV that lists every keyword without the underlying experience will score high.
- Both tools take the CV as plain text. Nothing in the protocol accepts a file, so the extraction step belongs to the client.

## See also

- [JobYap MCP](/hermes/mcp/servers/external/jobyap-mcp/) for job postings and salary signal from company career sites.
- [Level Jobs MCP](/hermes/mcp/servers/external/level-jobs-mcp/) for searching a job board directly.
- [WorkLittle Jobs](/hermes/mcp/servers/external/worklittle-jobs/) for the other job-search surface in this catalog.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
