---
title: site-spec MCP - Machine-Readable Website Audits
description: "Local stdio MCP server that audits the invisible layer of a website - robots.txt, llms.txt, canonical and noindex signals, JSON-LD, Open Graph, headers, accessibility, trackers - with 40 deterministic checks and automatic repairs for 17 of them. Apache-2.0, no account, no API key."
category: SEO
stars: n/a (new listing, github.com/ariaxhan/site-spec)
added: 2026-08-29
source: mcpservers.org /all page 1
relevance: ★★★
tags: [mcp-server, seo, geo, structured-data, accessibility, llms-txt, site-audit, self-hosted]
---

# site-spec MCP

**A local MCP server that audits the part of a website a browser does not render - robots.txt, llms.txt, canonical and noindex signals, JSON-LD, Open Graph, response headers, accessibility semantics, and the tracker and cookie surface - then applies deterministic repairs.** It runs the site-spec engine in-process over stdio with Node 20+, zero runtime dependencies, no account, and no API key. The audit engine is deterministic (no model decides what counts as broken), running 40 checks, 17 of which carry an automatic repair.

```
Server type: stdio (local)
Auth: None (no account, no API key)
Install: npx -y site-spec-mcp
Tools: 4 (list_checks, audit_site, fix_issue, compile_spec)
Checks: 40, 17 with automatic repair
Pricing: Free, open source (Apache-2.0)
Category: SEO / Site Health
Built by: ariaxhan; repo github.com/ariaxhan/site-spec, created Jul 14, 2026
```

## Why This Matters for Operators

AI can generate a beautiful website in seconds, but the layer that decides whether that site gets found, ranked, cited, and trusted is invisible in a browser - and it is broken on almost every generated site. A gorgeous hero section over a robots.txt that blocks ChatGPT, invalid or self-serving JSON-LD, a stray noindex hiding pages from Google, fonts leaking visitor IPs in violation of GDPR. Nobody notices until the site silently fails at distribution.

site-spec gives an operator's assistant four tools over that layer: learn the check catalog, audit a live URL or a local build directory, preview and apply a repair, and compile a site spec from a business brief. Because the engine is deterministic, two runs on the same input give the same findings - audits are reproducible evidence, not model opinion. The repair path defaults to dry run, showing diffs before anything is written, and refuses to write to remote servers entirely.

**Search, AI-citation, and trust readiness become a repeatable audit with diffs, not a guess.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| list_checks | No arguments. Returns count, fixable, and every check with id, description, category, and fixable flag. Call first. |
| audit_site | Audits a URL, bare hostname, or local directory. Optional check-id filter and maxPages (1-200, default 25 for live crawls). Returns ok, mode, errors, warnings, and findings. |
| fix_issue | Dry run by default (returns diffs, writes nothing). write:true requires a local directory target and is refused for URLs. |
| compile_spec | Generates a site spec from a business brief (pack, brief, site, spec objects), optionally writing files to out_dir. |

## Installation

```bash
claude mcp add site-spec -- npx -y site-spec-mcp
```

Codex and other clients use the same npx command in their MCP config (see the repo llms.txt for exact shapes). No signup, no token, no telemetry account.

## Configuration

```json
{
  "mcpServers": {
    "site-spec": {
      "command": "npx",
      "args": ["-y", "site-spec-mcp"]
    }
  }
}
```

Typical flow: call list_checks to learn the check ids, audit_site on the live URL, fix_issue for one finding in dry-run mode to see the diff, then fix_issue with write:true against the local build directory that produces the site.

## Business Relevance

- **Site owners** catch the invisible distribution failures - robots.txt blocking AI crawlers, noindex accidents, invalid structured data - before they cost traffic.
- **Agencies** produce reproducible audit evidence per client and apply repairs as reviewed diffs.
- **AI-built-site operators** get the exact checks that matter for a generated site: llms.txt, canonical signals, JSON-LD validity, tracker and cookie surface.
- **Compliance-minded teams** get the GDPR-relevant findings (font/tracker leaks) in the same report as the SEO findings.

## Integration with CorpusIQ

site-spec pairs directly with CorpusIQ's docs and site operations: the docs repo runs SEO/AEO/GEO passes (frontmatter, llms.txt, JSON-LD) and a nightly ecosystem-discovery pipeline, and site-spec turns those into a local, deterministic pre-publish gate. A CorpusIQ workflow can run audit_site against docs.corpusiq.io staging, have fix_issue propose the structured-data or canonical repairs as diffs, and only then commit. The compile_spec tool feeds a site spec into the same documentation pipeline CorpusIQ uses for client deliverable pages, keeping the audit record and the spec in one repo.

## Limitations

- New listing with no stars and a short public history (repo created Jul 14, 2026).
- Local-only server - it audits from your machine and writes only to local directories; no hosted option.
- The 17 auto-fixable checks cover the machine-readable layer, not content quality, design, or ranking strategy.
- Deterministic means conservative: genuinely ambiguous issues are reported, not auto-resolved.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CiteRank MCP - AI Search Visibility Audits](/hermes/mcp/servers/external/citerank-mcp)
- [Askline MCP - AI Search Visibility and Brand Monitoring](/hermes/mcp/servers/external/askline-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
