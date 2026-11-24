---
title: "China Workday Calendar MCP - Statutory Workday Data"
description: "State Council holidays and 调休 makeup workdays for mainland China, plus package vulnerability checks, from two keyless read-only tools."
category: "Business Operations"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-24
source: "Submission chatmcp/mcpso #7991 filed 2026-11-24T15:07:50Z; a keyless initialize on the execute-api endpoint answering 200 as cn-calendar 1.0.0 with two tools; six tool calls driven 2026-11-24 including the argument refusals; the State Council notice 国办发明电〔2025〕7号 at gov.cn/zhengce/zhengceku/202511/content_7047091.htm fetched and read the same day"
relevance: "★★★"
tags: [china, workday, holiday-calendar, statutory, payroll, scheduling, supply-chain, osv, vulnerabilities, remote-mcp, keyless]
last_updated: "2026-11-24"
---

# China Workday Calendar MCP

**A China holiday is not one date. It is a block of days off and a set of Saturdays and Sundays that become working days to pay for them, published once a year by the State Council as 调休.** Every delivery promise, payroll run, invoice due date and support rota that crosses China needs those two lists, and most software carries only the first. This server carries both, quotes the notice, and answers a 366-day range at a time.

```
Server type: Remote (Streamable HTTP, stateless)
Endpoint:    https://mvqz0m8d6g.execute-api.ap-northeast-1.amazonaws.com/mcp
Auth:        none - 20 free tool calls per IP per day, then per-call x402 payment
Server name: cn-calendar 1.0.0, protocol 2025-06-18
Tools:       2 (cn_workday_check, package_advisories)
Pricing:     free tier 20 calls/IP/day; paid calls priced in the error that follows
```

## The instructions string is the product brief

The server advertises its own limits in the handshake rather than in documentation:

> China workday calendar (holidays and 调休 makeup workdays) and package vulnerability advisories. 20 free tool calls per IP per day; after that each tool error names the paid x402 URL and price.

A client that never reads a vendor page still learns the quota, the data model and the payment mechanism. That is the honest shape: no account, no key, no trial that expires, just a per-IP allowance and a price you are told before you pay it.

## One date, answered with the notice attached

`cn_workday_check` with **date 2026-11-24** returned:

```json
{"date":"2026-11-24","weekday":2,"is_workday":true,"is_public_holiday":false,
 "is_makeup_workday":false,"holiday_name":null,"kind":"workday",
 "source_url":"https://www.gov.cn/zhengce/zhengceku/202511/content_7047091.htm",
 "data_updated":"2026-11-05"}
```

The same call on **2026-02-17** returned `is_workday false`, `is_public_holiday true`, `is_makeup_workday false`, `kind public_holiday`, `holiday_name 春节` (Spring Festival) and the same gov.cn URL. `weekday` is 2 for 2026-11-24, so the numbering is ISO-style Monday 1 through Sunday 7, which is worth knowing before you branch on it.

## The 2026 arrangement, quoted from the source and reproduced by the tool

The citation resolves to the State Council notice **国办发明电〔2025〕7号**, issued **2025-11-04**, and the tool's answers reproduce it exactly:

| Holiday | Days off | Weekend days worked (调休) |
|---------|----------|---------------------------|
| New Year | Jan 1 (Thu) to Jan 3 (Sat), 3 days | Jan 4 (Sun) |
| Spring Festival | Feb 15 (Sun) to Feb 23 (Mon), 9 days | Feb 14 (Sat), Feb 28 (Sat) |
| Qingming | Apr 4 (Sat) to Apr 6 (Mon), 3 days | none |
| Labour Day | May 1 (Fri) to May 5 (Tue), 5 days | May 9 (Sat) |
| Dragon Boat | Jun 19 (Fri) to Jun 21 (Sun), 3 days | none |
| Mid-Autumn | Sep 25 (Fri) to Sep 27 (Sun), 3 days | none |
| National Day | Oct 1 (Thu) to Oct 7 (Wed), 7 days | Sep 20 (Sun), Oct 10 (Sat) |

Two range calls check it from the other direction. **2026-02-14 to 2026-02-28** returned 15 calendar days and **6 workdays**: 02-14, then 02-24, 02-25, 02-26, 02-27, 02-28. The nine-day block sits in the middle and the two make-up Saturdays open and close it. **2026-10-01 to 2026-10-10** returned 10 calendar days and **3 workdays**: 10-08, 10-09 and 10-10, so the seven-day National Day block ends on the 7th and the country returns to work including the make-up Saturday.

## Is the free quota enough?

Twenty calls a day, and a range answer costs one call. A monthly delivery calendar for one China region needs roughly twelve calls a year; a payroll close needs one per period. The quota is sized for an agent answering questions, not for bulk date expansion, and that is the right trade: nothing about a workday calendar should require a subscription.

## Refusals cost nothing, and say why

Three refusals were reproduced and none was charged:

- `start_date` / `end_date` returned `invalid_arguments: pass date (YYYY-MM-DD), or from and to. Not counted against the free quota.` The parameter names are **date**, or **from** and **to**, and the refusal teaches them.
- A 400-day range returned `range_too_large: range is 400 days; maximum is 366 days inclusive. Not counted against the free quota.` The 366-day ceiling is enforced, not just documented.
- The range answer carries `data_updated 2026-11-05` but **no `source_url`**, while every single-date answer carries the gov.cn link. If your audit trail needs the citation, ask for the date rather than the range.

## The second tool: package advisories from OSV

The same server answers "is this version safe to install" across npm, PyPI, Go, crates.io and Maven, over OSV.dev:

- **npm lodash 4.17.20** returned `vulnerable: true`, **4** advisories, including `GHSA-29mw-wpgm-hmr9` (CVE-2020-28500, MODERATE, ReDoS) and `GHSA-35jh-r3h4-6jhm` (CVE-2021-23337, HIGH, command injection), with affected ranges and `fixed_versions ["4.17.21"]`.
- **PyPI requests 2.31.0** returned `vulnerable: true`, **6** advisories, the first being `GHSA-9hjg-9r4m-mvj7` (CVE-2024-47081, .netrc credential leak on malicious URLs) with `fixed 2.32.4`.

Names are matched as published and case-sensitive for npm, Maven takes `groupId:artifactId`, and Go takes the module path, so the answer is about one exact version rather than about a package in general.

## Who runs it

The submission names a single developer repository and the official MCP registry name `io.github.walkley/cn-calendar`. There is no company page, no pricing page and no privacy policy on the endpoint: the whole commercial surface is the x402 pay-per-call path that appears once the daily allowance is spent. Treat it as a utility with a public data source, not as a vendor with a support desk.

## How to connect

```
claude mcp add --transport http cn-calendar https://mvqz0m8d6g.execute-api.ap-northeast-1.amazonaws.com/mcp
```

The host is an AWS `execute-api` URL rather than a branded domain, so paste it as given. Nothing else is required.

## What this guide can and cannot certify

Verified on 2026-11-24: the keyless handshake and the two schemas, the single-date and range answers above, the 366-day ceiling, the two advisory lookups, and the citation to the State Council notice, which was fetched independently and matches the tool's table line for line. Not verified: coverage beyond 2020 to 2027, whether the x402 paid path works as priced, and whether advisory results track OSV in real time rather than on a refresh cycle.

## Verdict

The catalogue carries country data for tax, payroll and invoicing, and it had nothing that answers the make-up-Saturday question for China. **A nine-day holiday is easy to remember; the Saturday you have to work to pay for it is the one that breaks a delivery date.**
