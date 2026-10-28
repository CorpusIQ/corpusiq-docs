---
title: "App Store Connect MCP - Sales, Reviews and Releases"
description: "Drive your own App Store Connect account from an agent: sales and proceeds, the analytics funnel, reviews, TestFlight and releases across 76 tools, read-only by default with a human gate on anything public."
category: App Business / Mobile Analytics
stars: 1 (MIT, single Go binary, published October 2026)
added: 2026-10-26
source: "vendor repository idoo/app-store-connect-mcp read at 2026-10-26 (README, docs/TOOLS.md generated tool reference listing 76 tools with read/write/destructive classes and confirm modes) + brew tap idoo/homebrew-tap answering HTTP 200 + official MCP registry entry io.github.idoo/app-store-connect-mcp, latest 0.13.0 + chatmcp/mcpso submission #6189. Not probed live: the server is local stdio and needs an App Store Connect API key."
relevance: ★★★
tags: [app-store, ios, mobile, sales-reports, proceeds, reviews, testflight, app-analytics, local-stdio]
last_updated: "2026-10-27"
---

# App Store Connect MCP

**The revenue numbers for an app business live behind App Store Connect, and this is the first server in this catalog that reads them from Apple's own API inside the assistant rather than from a third-party estimate.**

```
Server type: Local (stdio), optional Streamable HTTP when self-hosted
Install:     brew install idoo/tap/app-store-connect-mcp
             curl -fsSL .../releases/latest/download/install.sh | sh
             docker run ghcr.io/idoo/app-store-connect-mcp
Auth:        App Store Connect API key (ASC_KEY_ID, ASC_ISSUER_ID,
             ASC_PRIVATE_KEY_PATH or ASC_PRIVATE_KEY)
Tools:       76, in 16 toolsets
Built by:    Ivan Verevkin (github.com/idoo), MIT
Registry:    io.github.idoo/app-store-connect-mcp, latest 0.13.0
```

## Why This Matters for Operators

An app business has two data problems that look like one. The first is marketing: what is happening in the store, which keywords move, what competitors look like. The second is money: units, proceeds by currency, refunds, subscription revenue, and the funnel from impression to install. The catalog already carries the first problem through [AppSigma's public App Store data](/hermes/mcp/servers/external/appsigma-app-store-data-mcp), which reads the store as a market.

This server answers the second problem from the account side, through Apple's own App Store Connect API. The distinction matters because a third-party estimate cannot reconcile to a payout, and a keyword rank is useless next to a proceeds figure that came from somewhere else.

## What It Actually Does

The tool reference is generated from the source, which is why it can be quoted precisely: **76 tools**, each classified **R** read, **W** write or **D** destructive or public, with a confirm mode of `none`, `flag` (preview then `confirm:true`), `plan` (preview then `plan_id`) or `human` (`confirm:true` plus approval via elicitation). Sixteen toolsets: core, release, testflight, metadata, reviews, reports, screenshots, uploads, monetization, signing, xcodecloud, webhooks, admin, store, insights and library. Six are on by default, so an agent sees a small surface until a toolset is switched on with `--toolsets +insights`.

| Tool | What it answers |
|---|---|
| `sales_report` | Sales and Trends aggregates: units by category, proceeds per currency, top-N, for a period from `from`/`to` or `frequency` + `report_date`; `include_rows` returns the full CSV link |
| `analytics_report` | With `report`: sums the metrics of an app's newest analytics segments by dimension; without `report`: lists the analytics reports. Data lags 24 to 48 hours |
| `analytics_setup` | Ensures an ONGOING analytics report request exists, optionally a ONE_TIME_SNAPSHOT for history - the prerequisite for the funnel |
| `insights_summary` | The first call for "how is my app doing": units and proceeds against the previous period, ratings, versions, TestFlight feedback and analytics, each section either ok or unavailable with the reason |
| `analytics_funnel_report` | Impressions to page views to downloads, with conversion by source and territory, sessions, crashes, installs against deletions, compared with the previous period, with coverage and lag stated |
| `reviews_list` | Customer reviews newest first with responses; `since:last_seen` returns only new ones |
| `release_status` | Preflight of a version: build, compliance, What's New, listing, screenshots, review contact, age rating, pricing, products, submission |
| `apps_get` | One app at a glance: live version per platform, in-flight versions with state, five latest builds, listing locales |
| `doctor` | Health check of the key, JWT, Apple reachability, clock skew, rate limit, spec, write mode, toolsets and vendor number, each with a fix - run first on a 401 or 403 |
| `testflight_feedback_list` | Tester screenshot and crash feedback, newest first, up to four screenshots as images |

The release side is a full workflow rather than a bag of REST calls: `release_prepare` applies a plan (`plan_id` from `desired`), `release_submit` submits the version plus IAPs and subscriptions for review, `release_publish` releases a pending-developer-release version, `release_phased` pauses or resumes a seven-day rollout, and `release_cancel` empties an unsent draft. Everything public or hard to undo is `D` class with a human gate.

## Safety Model, as Documented

- **Read-only by default.** Writes are additionally gated by toolset, and the six default toolsets are the read-heavy ones.
- **Destructive operations need more than a flag.** Publishing, submitting, cancelling a review, expiring builds and raw API writes (`asc_api_request`) require `confirm:true` plus approval through elicitation, so the human in the client sees the exact action.
- **Spec validation before the call.** `asc_api_get` and `asc_api_request` validate against a pinned App Store Connect spec first, and a mismatch returns the skeleton instead of making the call.
- **Untrusted text is treated as data.** Review text and tester feedback are labelled as untrusted in the tool descriptions, and the README states the injection guard explicitly.

## Limitations Recorded

- **Local stdio only.** There is no hosted endpoint to probe, so this entry rests on the repository, the generated tool reference and the registry, and no tool was executed here.
- **It needs an App Store Connect API key**, which an Apple Developer account issues per team. That is a real credential with account reach, and the human approval gates exist because of it.
- **Analytics lag 24 to 48 hours** and the funnel needs `analytics_setup` to have been run; a fresh setup returns `not_set_up` rather than an empty chart, which is the honest failure but still a wait.
- **Reviewer messages are not in the API.** `release_review_status` covers submissions and item states; the Resolution Center conversation stays in the web UI.
- **A young, single-maintainer project**: 1 star, first published in October 2026, version 0.13.0. The tool reference is generated and the README compares itself openly against three other App Store Connect servers, which is a good sign, and it is still a new dependency for a money-touching workflow.
- Write operations were not verified live, so the approval behaviour described here is the documented behaviour.

## FAQ

### How is this different from the App Store data server already in this catalog?
[AppSigma](/hermes/mcp/servers/external/appsigma-app-store-data-mcp) reads the public store: competitor rankings, keyword data, sponsored slots, reviews of any app. This one reads your account: your units, your proceeds, your reviews, your releases. One is market research, the other is bookkeeping and operations.

### Can my agent ship a release on its own?
No. Submission, publishing, phased-release changes and cancellation are destructive-class tools that require an explicit confirmation plus human approval in the client. Metadata edits preview as a plan first.

### Does it replace the App Store Connect web UI?
For reporting, yes: sales, proceeds, the funnel and reviews are all readable from chat. For anything Apple only exposes in the Resolution Center or the developer portal's authenticated forms, no.

## See Also

- [AppSigma App Store Data MCP - ASO and app analytics](/hermes/mcp/servers/external/appsigma-app-store-data-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ analytics and advertising connectors](/hermes/mcp/)
