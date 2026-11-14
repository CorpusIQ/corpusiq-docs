---
title: "Spanish Top Tech Companies MCP - Salary Medians"
description: "A keyless MCP server returning salary medians for Spain by role, region and company, plus live job postings and their application forms."
category: "HR / Compensation Data"
stars: "The open-source project behind it is public; the MCP server is keyless"
added: 2026-11-14
source: "the mcp.so submission #7336 filed 2026-11-14T13:48:01Z, the official registry records io.github.pugarte7/spanish-top-tech-companies 1.20.0 and 1.20.1 both active and published 2026-11-14, and a live session on this host: initialize, tools/list, and seven tools/call requests including a company breakdown reproduced by hand against https://spanishtoptechcompanies.com/mcp"
relevance: ★★★
tags: [salary, compensation, benchmarking, spain, levels fyi, job postings, greenhouse, recruiting, hiring, mcp, remote]
last_updated: "2026-11-14"
---

# Spanish Top Tech Companies MCP

**Every salary negotiation starts with a number the person on the other side has and you do not.** A candidate in Spain asking for 62,000 needs to know that the median in the market is 55,000 and that the middle half runs from 42,000 to 72,000, because that is what the employer's recruiter is looking at. A hiring manager approving a budget needs to know that the same title pays 126,000 median at Shopify and 105,000 at Meta.

Spanish Top Tech Companies is a free, open-source project that answers both questions from Levels.fyi submissions and publishes the answer as an MCP server. It is keyless, and it is honest in a way that is unusual for this class: the medians are reported only where five or more people back them, fewer than five is marked, and the tool says so before you quote a number.

```text
Server type:   remote Streamable HTTP, JSON-RPC 2.0, session header issued
Endpoint:      https://spanishtoptechcompanies.com/mcp
Server:        "tech-pay-spain" titled "Spanish Top Tech Companies", 1.20.1,
               protocol 2025-06-18, capabilities: tools
Registry:      io.github.pugarte7/spanish-top-tech-companies 1.20.1, active,
               published 2026-11-14
Auth:          none
Tools:         8
Currency:      euro, gross base per year; totals add bonus and stock
Rounding:      to the nearest 1,000
Source:        Levels.fyi submissions for people working in Spain
```

## The evidence tier

Keyless, session-issuing, and every tool that answers for a person's question was driven. Seven `tools/call` requests were made across five tools; the two write-adjacent tools (`report_application`, `application_guide`) return instructions rather than touching an account.

## What a role pays across Spain

`salary_stats` for `software-engineer`, the widest selection the tool takes without a company filter:

| Measure | Value |
|---|---|
| People behind the figure | 4,925 |
| Median base | 55,000 EUR |
| 25th percentile | 42,000 EUR |
| 75th percentile | 72,000 EUR |
| Median total (base plus bonus and stock) | 60,000 EUR |
| Share at or above 60,000 base | 45.9% |

The response carries its own caveat, and it is the kind that saves an argument: *Backend is counted as software-engineer on Levels.fyi, so these figures are for every software engineer, not only Backend.*

`list_filters` returns the vocabulary the other tools accept: **35 roles** and a region map keyed on the Spanish autonomous-community codes (**CT** Catalonia, **MD** Madrid, **AN** Andalusia and the rest), so a narrowing of the selection is a filter rather than a free-text guess.

## What a single company pays, by seniority

`company_salaries` for Glovo returned **441** salaries in Spain across Barcelona and Madrid, median base **70,000**, p25 **57,000**, p75 **80,000**, median total **77,000**, and **72.8%** of that population at or above 60,000 base. The same call breaks the population into year bands:

| Years | People | Median base | Median total |
|---|---|---|---|
| 0 to 1 | 17 | 35,000 | 35,000 |
| 2 to 4 | 91 | 53,000 | 57,000 |
| 5 to 7 | 165 | 68,000 | 75,000 |
| 8 to 11 | 111 | 78,000 | 87,000 |
| 12 to 19 | 55 | 88,000 | 100,000 |
| 20+ | 2 | 94,000 | 115,000 (few) |

**The bands add up to the total**: 17 + 91 + 165 + 111 + 55 + 2 = **441**, the same figure the summary line reports. That is the arithmetic control this guide ran by hand, and it held, which is more than most compensation tools survive.

`top_companies` ranks **643** companies by median base for one role, with two rules stated in the response: a company with fewer than three salaries in the selection sorts after every company with three or more, and `few: true` marks a figure from fewer than five people. The head of the list for software engineers:

| Company | People | Median base | Median total |
|---|---|---|---|
| Shopify | 18 | 126,000 | 127,000 |
| Automattic | 3 (few) | 120,000 | 120,000 |
| Workato | 12 | 120,000 | 120,000 |
| Adobe | 7 | 110,000 | 166,000 |
| Meta | 11 | 105,000 | - |

Adobe is the row worth reading twice: a 110,000 base against a 166,000 total, because that is what equity does to a Spanish offer.

## The jobs half: from a posting to a filled form

`find_jobs` is a live index, not a cached table. On 2026-11-14 it reported **7,523** postings in the index; filtering to `software-engineer` gave **1,595** matched postings merged into **1,438** results, and the free-text query `python` gave **1,135** into **1,051**. The grouping rule is stated in the response: one company's postings with the same title, ignoring the places it names, count as one result, and the variants ride in `also_posted_as`.

The chain past the posting is where this server is different from a job board:

- `job_questions` reads the **application form of one posting**, live from its board, so the agent knows what the employer actually asks before it starts drafting.
- `application_guide` returns the procedure for applying **on someone's behalf** rather than doing it silently.
- `report_application` records the outcome after sending, or after failing to, so the record is part of the system rather than a note in a chat.

Two honesty markers are worth recording because they are policy, not copy. The index states `salary_data_as_of: 2026-11-09`, five days before the run, next to a `generated_at` of the same minute - the salary layer and the postings layer are refreshed on different clocks and the response says which is which. And the self-reported rule is enforced: a selection with fewer than five people returns no percentile at all rather than a confident-looking number built from two.

## A note addressed to the person, not the agent

Every `find_jobs` response carries a `note_for_the_person` block. It is a message from the maintainer to the human in the conversation, asking for a GitHub star, and its own instructions to the agent are explicit: pass it on **once**, under the postings, never star without the person's yes, and if a state document is kept, write the date and their answer on the Support line so it is not repeated.

That is the cleanest version of this pattern in the catalog. It solves a real problem - a free tool maintained by one person needs distribution - without turning the agent into a marketing channel, because the request is scoped, addressed to the wrong party on purpose, and carries its own do-not-repeat rule.

## What does not work

- **`company_salaries` rejects `company`** and requires `name`. The error is a readable sentence (*name is required: a company such as Glovo*) rather than a schema dump, which is the right way to fail but still a name an agent will guess wrong first.
- **`company_salaries` with no company in the table returns an error**, not an empty set.
- **Spain only.** There is no fallback country, and `region` takes Spanish community codes rather than free text.
- **Salary figures are rounded to the nearest 1,000** and come from self-submitted Levels.fyi data, so they are reported medians rather than payroll records.
- **The salary layer lags the postings layer** by five days in this measurement, and the response says so rather than blending them.

## Frequently asked questions

### Does this server require an API key or an account?

No. `initialize` and all seven `tools/call` requests in this pass answered without a credential, and the server issues a session header rather than a token.

### Are these figures reliable enough to quote in an offer?

They are medians from self-submitted data, rounded to the nearest 1,000, with a stated minimum of five people behind any percentile. Quote them as a market range with the sample size attached, which is how the tool presents them.

### Can it apply for a job on my behalf?

It can read the form, prepare the application and record the outcome. The guide tool sets out the procedure for applying on someone else's behalf and the server treats the send as a step the person approves.

### What is the difference between `median_base` and `median_total`?

`median_base` is gross salary. `median_total` adds bonus and stock, which is why a company like Adobe shows 110,000 against 166,000 and a cash-heavy company shows the two figures nearly equal.

## Limits recorded

Spanish market only, euro only, Levels.fyi sourced. The salary layer and the postings layer have separate refresh clocks and the response reports both. Coverage of a company depends on how many people at that company submitted, so a company with three salaries is marked `few` and should not be compared against one with eighteen.
