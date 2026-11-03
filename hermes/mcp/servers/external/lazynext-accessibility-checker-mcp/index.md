---
title: "Lazynext Accessibility Checker MCP - WCAG Audits From Chat"
description: "Scan any public page for WCAG 2.1 and 2.2 violations from an MCP client: a rendered-browser audit returns a 0 to 100 score, rule-level findings with a fix each, a section 508 clause map and a shareable report URL."
category: Business Operations
stars: n/a (free tier, 3 rendered scans a day)
added: 2026-10-31
source: "The chatmcp/mcpso submission issue #6529 filed on 2026-11-01 at 03:22:32Z; a keyless JSON-RPC initialize, tools/list, list_rules and two scan_url calls against https://checker.lazynext.com/mcp; and the vendor site at https://checker.lazynext.com read for pricing and plan gates"
relevance: ★★★
tags: [accessibility, wcag, a11y, section-508, compliance, web-audit, rendered-scan, remote-mcp, streamable-http, free-tier]
last_updated: "2026-11-01"
---

# Lazynext Accessibility Checker MCP

**Accessibility is the one website requirement that arrives as a deadline rather than a preference: a procurement form, a public-sector contract, a state remediation letter. This connector turns that deadline into a scan from the chat, with the failing criterion named and one sentence of repair per finding.**

```
Server type: Remote (Streamable HTTP, JSON-RPC)
Endpoint:    https://checker.lazynext.com/mcp
Auth:        none for the free tier, optional Pro license email for higher limits
Tools:       4 (scan_url, scan_html, get_report, list_rules)
Rules:       75 WCAG criteria, each tagged static or rendered
Pricing:     Free 3 rendered scans/day; Pro $9/mo ($90/yr); Agency $39/mo ($390/yr)
```

## What it does

Four tools, and the split between them is the whole design:

- `scan_url` renders a live page in a real browser engine and returns `score`, `issues`, and a `report` URL. It takes `url`, an optional `site` boolean for a same-origin crawl (3 pages free, 10 on Pro), an optional `viewport` of `mobile` (390x844 handset, the default) or `desktop`, and an optional `license` email to lift limits.
- `scan_html` audits pasted markup against the static rules only, with no render and no quota, which is what a developer wants before a deploy.
- `get_report` fetches a stored report by id.
- `list_rules` returns every criterion the scanner can emit with its name, WCAG level, WCAG version, detection path (`static` or rendered) and a one-line description of what it detects. The call returned **75** rules.

Every finding carries three fields that decide whether it is actionable: `rule` (for example `wcag-2.5.3`), `message` (the element as the scanner saw it), and `fix` (one sentence naming the repair).

## What this pass measured

The surface answered on the first request, with no key. `initialize` returned **HTTP 200** in 0.19 seconds, `protocolVersion` `2025-03-26`, `serverInfo` name `accessibility-checker` at version **1.0.0**, and `tools/list` returned all four tools with their input schemas in 1,399 bytes. `list_rules` returned 34,954 bytes of rule data. So this is a measured surface rather than a vendor description, and two live scans were made against `https://www.corpusiq.io/`.

**Mobile viewport, the default.** The scan answered in **12.97 seconds** with score **46** on `score_model` `weighted-v1`, `rendered: true`, `plan: "free"`, and **28** issues across **12** distinct criteria. The rule histogram is the useful part: `wcag-2.4.9` (link purpose) nine times, `wcag-1.1.1` (non-text content) seven times, `wcag-1.4.6` (contrast enhanced) twice, `wcag-2.5.3` (label in name) twice, and one each of `1.4.3`, `1.4.10`, `1.4.11`, `2.4.5`, `2.4.12`, `2.5.5`, `2.5.8` and `4.1.2`. The section 508 block came back `conforms: false` against the basis it states, WCAG 2.0 AA incorporated by 36 CFR 1194 E205.4, with **12** criteria failed and **5** clauses implicated: 302.1, 302.2, 302.3, 302.7 and 302.9. The benchmark field placed the score at the **54th** percentile of **26** sites, and the report is persisted at `https://checker.lazynext.com/report/c036dcc1-4e6`.

**Desktop viewport.** The first attempt timed out at a 60-second client limit with no bytes returned, and the retry with a 150-second limit returned **HTTP 200** in **61.1 seconds** with score **46**, **29** issues and a benchmark of the **52nd** percentile of **27** sites. Same score, one more finding, one more site in the cohort, and the cohort itself moved between the two calls a minute apart, which is worth knowing before treating a single-digit score change as a regression.

**The findings are specific enough to fix.** Two examples, verbatim. `wcag-2.5.3` on an `aria-label` reading "Explore CorpusIQ for your business funct" because it does not contain the visible text "explore your business", which is the label-in-name failure that breaks voice control on a marketing section. And `wcag-1.4.10` on a `<div>` with a fixed 1000px width that cannot reflow at 320px, which is the failure that makes a page unusable at 400 percent zoom. Seven `wcag-1.1.1` findings were all the same class of shortcut: `alt` text that repeats the filename, "Shopify", "HubSpot", "eBay", "HighLevel", "Odoo", "ActiveCampaign".

## The containment worth reading twice

Every tool reads. `scan_url` fetches a public page, `scan_html` takes a string, `get_report` reads a stored result, `list_rules` serves the rulebook. Nothing writes to the scanned site, nothing authenticates against it, and nothing reaches a page behind a login, which also means the tool cannot audit what it cannot see. Any authenticated or intranet surface needs `scan_html` with markup the operator already has.

The second containment is that findings are not verdicts. The scanner reports failing criteria and the repair; whether a finding is a true positive on a page whose visible text is generated client-side is a judgement the report does not make for the reader, and the `benchmark.pct` figure moves with the cohort as sites are added.

## The operator decision this answers

Two decisions, actually. The first is commercial: a procurement questionnaire asks whether the site conforms to WCAG 2.0 AA, and "we think so" is not an answer. A score, twelve failed criteria and a clause map is an answer with a work list attached, and the same report can be re-run after the fixes to show the number moved.

The second is cheaper and more common: a redesign ships, someone changes an image component, and alt text quietly becomes filenames again. A daily scan with an email alert is the difference between noticing in a week and noticing in the accessibility complaint.

For an operator without an accessibility specialist, the `fix` string on each finding is the first-line triage. Most of what this pass found is a content edit, not an engineering project: alt text, a fixed width, an aria-label that replaced visible text instead of containing it.

## Where it sits in this catalogue

There is no accessibility entry in this catalogue, which is why this one shipped on first sight rather than being weighed against peers. The nearest neighbours audit a different question:

- [SEO Audit Console MCP](/hermes/mcp/servers/external/seo-audit-console-mcp/) and the other SEO scanners check what a search engine can read, which is a ranking question.
- [Squirrelscan](/hermes/mcp/servers/external/squirrelscan-mcp/) touches accessibility inside a broader site audit, and it does not return criterion-level WCAG findings with a repair per finding.
- The rendering and page-speed entries measure how fast or how faithfully a page loads, not who can operate it.

The distinction that matters in practice: "our site is slow" and "our site fails WCAG 2.5.3 on two controls" are answered by different tools, and only the second one produces a document a compliance reviewer accepts.

## What this pass did not establish

The pricing page and the MCP surface disagree, and the disagreement is recorded rather than resolved. `https://checker.lazynext.com` lists API, MCP and A2A access as a **Pro** feature at **$9 per month** ($90 per year), with the free tier described as 3 rendered scans a day and 3-page crawls. The MCP endpoint nevertheless accepted a keyless `initialize`, ran two scans, and labelled both results `plan: "free"`. Whether that is a launch window, a plan label that has not caught up, or a genuinely open endpoint is not stated anywhere this pass could read, so the assumption to test before depending on it is that the free tier is the operative limit and the Pro gate is documented but not enforced on MCP.

Also unmeasured: `scan_html` and `get_report` were not called, so the static rule split and report persistence are documented rather than driven; the `site: true` crawl was not run; white-label reports, monitors and email alerts, the A2A endpoint and the 14-day trial are vendor statements; how the `benchmark` cohort of 26 or 27 sites is composed is not published; and the repository at `github.com/Lazynext-AI/accessibility-checker` is described as **source available**, not open source, so self-hosting is not an assumption to make.

## FAQ

### Does it need an API key?
No. `initialize`, `tools/list`, `list_rules` and two `scan_url` calls all answered with no authorization header. A Pro license email can be passed as `license` to lift limits, and the vendor site sells OAuth-style plan access, but the MCP path here worked anonymously.

### Does it scan behind a login or a staging password?
No. `scan_url` renders a public URL. Internal pages, staging builds behind basic auth and anything requiring a session are out of reach, and `scan_html` on saved markup is the workaround rather than a replacement, because it can only apply the static rules.

### What does the score of 46 mean?
It is a weighted aggregate of the rule findings on one rendered page under `score_model` `weighted-v1`, and it is relative: the same scan reported the 54th percentile of a 26-site cohort. Treat it as a trend line for one site over time, not a cross-site ranking, and expect small movement when the cohort changes.

### Can an agent fix the findings?
It can propose them, because every finding ships a `fix` sentence. Applying a change to the site is a separate action with a separate approval, and this connector does not touch the site.

### How fast is a scan?
Mobile returned in 12.97 seconds. Desktop exceeded a 60-second client timeout on the first attempt and returned in 61.1 seconds on the retry, so a client timeout under 90 seconds will lose desktop scans.

### What is the free tier limit?
3 rendered scans a day per IP address and 3-page site crawls, with `scan_html` outside the quota because it does not render.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [Squirrelscan MCP](/hermes/mcp/servers/external/squirrelscan-mcp/) - broader site signals, accessibility among them
- [SEO Audit Console MCP](/hermes/mcp/servers/external/seo-audit-console-mcp/) - the same generated-site question, asked about search
