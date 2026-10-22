---
title: "DrUrls MCP - SEO Audit With Fixes and Indexability"
description: "DrUrls crawls a site, scores it, lists every issue with its fix, checks what blocks Google indexing, and can order a real person to test a device."
category: Marketing
stars: n/a (no public repo)
added: 2026-10-22
source: "mcp.so /feed page 1 (card posted 2026-10-21T20:50:13Z)"
relevance: ★★★
tags: [seo, seo-audit, technical-seo, google-indexing, core-web-vitals, accessibility, site-health, remote-mcp, oauth]
---

# DrUrls MCP

**Most SEO tools tell you a page scores 68. DrUrls tells you the eight things costing the other 32 points, what each one is worth in crawl terms, and which single fix touches the most pages.**

```
Server type: Remote (Streamable HTTP) at https://drurls.com/mcp
Auth: OAuth 2.1 with dynamic client registration on first connect; a dashboard API key also works
Live check: POST initialize returned HTTP 200 (serverInfo drurls 1.0.0, title "DrUrls - SEO intelligence", protocol 2025-03-26, tools capability); tools/list returned 11 tools
Real call: free_page_check on https://corpusiq.io returned HTTP 200 with score 91, grade A, 8 open issues, 133 internal links, 11 external links, 85 images with 0 missing alt, 149 ms response time
Tools: 11 (audits, issue search, Google visibility, improvement plan, report generation, tester marketplace)
Pricing: Free $0 with 5 credits a month, Pro $29 ($24 annual) with 250, Agency $79 ($66) with 1250, Enterprise $199 ($166) unlimited; extra credits $0.80 / $0.50 / $0.30 / $0.20 by tier
Vendor: DrUrls (drurls.com)
```

## Why This Matters for Operators

An SEO audit is only useful if it ends in a ranked list of work. The failure mode is familiar: a crawler produces four hundred findings across five severity levels, nobody can tell which ones matter, and the report gets filed next to the last one. Six weeks later the same findings come back.

Two things change that. The first is ranking by blast radius rather than severity: a missing meta description on one page and a missing canonical template on two hundred pages are not the same job, and a tool that says so collapses the list to what a small team can actually ship. The second is keeping the score history per site, so the question stops being "how are we doing" and becomes "did the thing we shipped on Tuesday move it".

## What It Actually Does

DrUrls is a crawler with an MCP face on it. `start_scan` launches a real crawl of a site (creating the site in the organization if it is new) and `get_scan_status` shows what is in flight and the last ten runs finished or failed. `list_sites` returns every site with its latest score, grade, issues found and pages crawled, which is the portfolio view an agency needs before it looks at any single site.

From there the reads are specific. `get_site_report` deep-dives one site: score, issue counts by severity, the most frequent issue types with counts, and social presence. `find_issues` searches open issues across all sites or one, grouped by type, with an example page and a page count per group. `check_google_visibility` answers the question that actually matters for traffic: noindex tags, robots blocks, sitemap errors, canonical problems and redirect chains that stop a page being indexed. `get_improvement_plan` ranks fixes by severity and by how many pages each one touches, and `generate_report` compiles the client-ready version for one site or the whole organization.

The eleventh tool is the unusual one. `list_tester_offers` and `hire_tester` order a real person on a real device: mobile UX on a handset, an end-to-end checkout, a screen-reader pass. A crawler cannot check any of those, and the gap between "the audit is clean" and "the checkout works on an iPhone" is where money is lost.

`free_page_check` is the keyless entry point: any public URL, no account, no key. It returns the same score, grade, category breakdown, and every issue with `whyItMatters`, `howToFix` and a confidence value.

## Installation

```bash
claude mcp add --transport http drurls https://drurls.com/mcp
```

The first call opens DrUrls for sign-in and approval. Approval issues a key that works only against the MCP server, carries no team or billing rights, and can be revoked from the dashboard.

## Configuration

```json
{
  "mcpServers": {
    "drurls": {
      "type": "http",
      "url": "https://drurls.com/mcp"
    }
  }
}
```

Headless agents can skip OAuth and send `Authorization: Bearer <key>` with a key minted at drurls.com/dashboard/api-keys.

## What a Free Check Actually Returns

Run against this site's own homepage at capture time, `free_page_check` returned a JSON body rather than a paragraph of prose, which is what makes it usable inside an agent:

```json
{
  "score": 91,
  "grade": "A",
  "responseTimeMs": 149,
  "wordCount": 4056,
  "links": {"internal": 133, "external": 11, "total": 144},
  "images": {"total": 85, "withoutAlt": 0}
}
```

with category scores for crawlability, indexability, metadata, content and internal links, and eight open issues carrying codes such as `CORS_WILDCARD`, `RENDER_BLOCKING_RESOURCES`, `EXCESSIVE_DOM_SIZE`, `CSP_UNSAFE_INLINE`, `IMAGE_FORMAT_NOT_MODERN`, `IMAGE_MISSING_SRCSET`, `META_KEYWORDS_PRESENT` and `CONTENT_LANGUAGE_HEADER_MISSING`. Each issue carries `severity`, `category`, `whyItMatters` and `howToFix`. That structure is the point: an agent can group them, cost them and sequence them without a human reading a PDF.

## Business Relevance

- **Marketing leads** get a prioritized fix list per site instead of a score to defend.
- **Agencies** run every client site from one organization, keep run history per site, and hand over a report that names the cost of each issue.
- **Founders without an SEO hire** get a plain answer to "is Google able to index this", which is the question that precedes every ranking question.
- **Ecommerce operators** can order a real-device checkout test rather than trusting a crawl that never pressed a button.
- **Developer teams** get the fix in the issue record, with the affected element and the expected value, so the ticket writes itself.

## Integration with CorpusIQ

The useful pairing runs both directions. CorpusIQ already answers "which pages earn traffic and which queries convert" from the Search Console and GA4 connectors; DrUrls answers "what is structurally wrong on those pages". Together the sequence is: pull the pages that earn impressions but not clicks from CorpusIQ, audit those exact URLs in DrUrls, and take the improvement plan back into CorpusIQ to ask whether the fix landed once it ships.

The second direction is verification. When a page is edited, `check_google_visibility` is the specific test for whether the edit broke indexability, which is the failure that costs weeks and shows up in no dashboard.

## Limitations

- Credits meter every action: a scan is 1 credit, a screenshot 1, an AI review 2, a test run 2, a video 5. The free plan's 5 credits a month covers a handful of scans, not a portfolio.
- The free check audits one page. Site-wide crawling, history and org-level issue tracking need a key.
- OAuth grants operate inside the organization the key belongs to, so a multi-client agency needs the Agency or Enterprise tier for seat structure.
- The tester marketplace is a paid human service billed in credits on top of the plan; it is not an automated check.
- New listing without an independent track record. The scores are DrUrls' own model, so treat the number as comparable across sites within DrUrls, not against another vendor's scale.

## FAQ

### Is there a free way to try it without an account?

Yes. `free_page_check` takes a public URL and returns the full score, grade, category breakdown and issue list with no key and no account, which is what the example above used.

### How is this different from other SEO servers in this catalog?

The SEO class here is carried by single-page scorers and content generators. DrUrls adds three things they do not: an org-wide crawl with score history per site, a Google indexability check that names noindex, robots, sitemap, canonical and redirect problems specifically, and a paid human test on a real device. The gap it does not close is content generation, which is a different job.

### Can an agent write the findings somewhere?

The tools are reads plus `start_scan` for new crawls and `hire_tester` to place a human test order. There is no write-back into a CMS, so the fix still goes through the team that owns the code.

### Does it need my Search Console data?

No. It crawls the public site. Connecting Search Console separately is what turns "what is wrong" into "what is worth fixing first" in revenue terms.

## See Also

- [Misar SEO MCP](/hermes/mcp/servers/external/misarseo-mcp)
- [SEOmely MCP](/hermes/mcp/servers/external/seomely-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
