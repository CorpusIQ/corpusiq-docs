---
title: "MCP Server Discovery - November 28, 2026 (Midday Supplement)"
description: "A canonical flat to the key set one hour after the midday read, seven fresh filings, one intake server catalogued and one OAuth chain walked."
category: "MCP Ecosystem"
last_updated: "2026-11-28"
---

# MCP Server Discovery - November 28, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick **one hour** after the midday pass, which had already shipped two driven guides. A one-hour window does not produce a new directory; it produces a settlement. Both large surfaces were re-read and both were flat, the submission queue added seven filings, and the pass spent its evidence budget on the two things a flat hour can still settle: the auth chain behind the newest feed card, which had been held as an unverified label, and a queue filing that turned out to be the first intake-origination surface on this shelf.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 17 maps named, 15 server-bearing maps read
raw <loc>, all server maps    39,098   (midday read 39,098, unchanged)
  servers/1 ..... 4,067   distinct 1,987      servers/8 ..... 2,774   distinct 2,000
  servers/2 ..... 2,510   distinct 1,990      servers/9 ..... 2,574   distinct 2,000
  servers/3 ..... 2,949   distinct 1,994      servers/10 .... 2,577   distinct 2,000
  servers/4 ..... 3,173   distinct 1,999      servers/11 .... 2,523   distinct 2,000
  servers/5 ..... 3,341   distinct 1,996      servers/12 .... 2,407   distinct 2,000
  servers/6 ..... 2,843   distinct 2,000      servers/13 .... 1,211   distinct 1,067
  servers/7 ..... 5,889   distinct 2,000      priority .....   245   distinct 34
                                              remote .......    15   distinct 0
union of keyed slugs          25,067   (stored 04:30 baseline 25,067)
                              0 additions, 0 removals across 25,067 keys
server-map lastmod rows       35,544   newest 2026-11-28T10:48:03Z
                              0 rows at or after the 18:00Z read
```

The flat reading is arithmetic rather than a count. The per-map distinct totals sit on the **2,000** sitemap ceiling on seven shards, `servers/13` reads **1,067** against 1,068 at the night capture, and the keyed union normalised on the owner and slug path diffs to **zero additions and zero removals** against the 04:30 baseline stored on disk. Not one of the 35,544 stamp rows moved inside the hour.

The **mcp.so** feed answered **200** at **158,026** bytes against 158,029 an hour earlier, with the same top card - `pdfcraft` at **2026-11-28T16:24Z** - and no card above the midday set. The submission queue carried **seven** filings, **#8310** to **#8316**, newest **17:52:31Z**, unbroken from the midday pass's top of #8309.

## Shipped: Klarefi, the first intake surface here

- [Klarefi MCP - Applicant Intake Where a Person Decides](/hermes/mcp/servers/external/klarefi-mcp/) - **keyless at the applicant boundary.** `klarefi-mcp` **0.4.0** answered `initialize` **200** with no credential on protocol **2025-11-25** to a **2025-06-18** request, listed **21** tools (9 read-only, 12 that write or stage), and named one **MCP Apps** resource. `resources/read` on `ui://klarefi/case-review` returned the whole **2,115-byte** template keylessly: a facts grid of label, value and status pill, a blockers list, one `esc()` helper, and a content-security block declaring **no** connect or resource domains. The design boundary is in the tools rather than the marketing: `submit_case_review` accepts `checks_go` as `go`, `not_now` or `withdraw` and **cannot complete or reopen a case**, `save_workflow_draft` **cannot publish or activate**, connectors **stage for operator approval**, consent is recorded with the **agent and client** that gave it, and `get_case_package` leaves as a `case_package.v1` artifact with a signed read-only case-file link. **Three defects:** auth refusals arrive in band as HTTP **200** with `isError: true` and one identical sentence that never names the missing scope, argument validation runs before authentication, and the app renders only on a `message` event so a host delivering `structuredContent` another way shows the placeholder.

## Settled and held: PDFCraft

`pdfcraft` was the midday pass's hold on an unverified auth label. Four HTTP calls settle it, and the settlement is what makes the hold defensible rather than the reverse:

- `initialize` with no credential answers **401** with `WWW-Authenticate: Bearer scope="pdfcraft:use", resource_metadata="https://api.pdfcraft.ai/.well-known/oauth-protected-resource/v1/mcp"`.
- That document answers **200**: resource `https://api.pdfcraft.ai/v1/mcp`, **one** authorization server at `https://api.oomol.com`, one scope `pdfcraft:use`, `bearer_methods_supported: ["header"]`.
- The authorization-server metadata answers **200** at `api.oomol.com`: authorize, token, revoke and registration endpoints, `S256` only, token endpoint auth method **none**, and **five** product scopes on one account - `connector:use`, `openflow:use`, `pdfcraft:use`, `postlookup:use`, `social:use`. The same document path on `api.pdfcraft.ai` answers **404**, which is correct and worth recording because the protected-resource document names a different host.
- A dynamic client registration POST to the vendor's registration endpoint answered **201** with a `client_id` and no secret; the authorize endpoint with an unknown `client_id` answered **400**, so the client cannot be aliased.

What keeps it a hold is the next layer down. The service states its protocol version as **2026-07-28** and says plainly that older 2025 initialization and session flows are not supported, which is a compatibility floor no other entry on this shelf carries. Its own documentation never names a tool beyond `get_capabilities`, and the tool list is auth-gated, so the capability set - conversion, and the translation of PDFs and EPUB books that would make it distinct from the four document-conversion entries already here - remains the vendor's claim. The metering is recorded for the next pass: **1 credit equals 1 USD**, charged on the pages or source words actually processed, pay-as-you-go credits that do not expire, subscriptions that grant credits monthly at a lower rate, Stripe checkout, and a balance that syncs across the web app, desktop, iOS, the REST API and MCP.

## Held with the class named

- **PennyFinch** - budgeting and net-worth dashboard, read-only through Plaid with per-action consent. Consumer personal finance, the class Glideworth already owns.
- **TruthSpine** - local project memory shared across AI clients, which lists **Hermes Agent** among its supported tools. Agent memory, carried by five entries already.
- **Health MCP** - Apple Health with per-chunk encryption on the phone and the key never reaching the server. Consumer health, and the encryption story is good; the data is one person's step count.
- **mambalabsdev, eighth wave** - `mcp-fda-clearance-recall-monitor`, `mcp-court-docket-monitor` and `mcp-github-repo-search`, three single-tool Apify actors over stdio with an `APIFY_TOKEN`. Held as one line on the carried actor-fleet class.
- **watchfor** - uptime monitoring for agents, keyless with 20-plus tools at the night probe. Monitoring, carried by Cronitor, Runheed and uptrack.

## Counts

Canonical **25,067** against **25,067** with **0 additions and 0 removals** and **39,098** raw on both reads; **35,544** stamp rows with the newest at **10:48:03Z** and none in the window; mcp.so **158,026** bytes with the same top card; queue **7** filings, **#8310** to **#8316**; **4** auth documents read for PDFCraft (**401**, protected resource **200**, authorization server **200**, registration **201**) plus **2** controls (**404** on the wrong host, **400** on an unknown client); **7** MCP calls against Klarefi (**initialize**, **tools/list**, **resources/list**, **resources/read**, and five `tools/call` attempts); **1** server catalogued and **1** guide.
