# PROGRESS.md — corpusiq-docs build status

Current state and ongoing work for the public docs repository.

## File count (updated August 12, 2026)

- **Total Markdown files:** 1,440
- **Total HTML files:** 445 (MkDocs build output; reduced after build optimization)
- **Hermes subdirectory:** 30 directories covering skills, MCP servers, setup guides, blueprints, ecosystem discovery, prompts, and more
- **Docs subdirectory:** 17 directories — SEO-optimized product pages, connector guides, troubleshooting, and comparison pages
- **Skills catalog:** 345 setup guides for Hermes skills
- **MCP servers:** 312 server listing markdown pages (+ HTML companions)
- **SEO pages:** 120 programmatic landing pages targeting high-intent operator keywords

## Site architecture

- **Main docs:** `https://www.corpusiq.io/docs/` — MkDocs Material, served on corpusiq.io
- **Hermes knowledge base:** `https://corpusiq.github.io/corpusiq-docs/hermes/` — GitHub Pages
- **SEO pages:** 100+ programmatic pages targeting high-intent keywords (e.g., "connect Shopify to ChatGPT," "MCP for ecommerce")
- **Daily automation:** Ecosystem discovery cron, skills.sh marketplace monitoring, MCP.so/mcpservers.org scans

## Items punting / skipped

- **No separate FAQ.** Folded into `how-it-works/` and `troubleshooting/` — a formal FAQ page can be added if user questions warrant it.

## Current status — August 10, 2026

The repo is actively maintained with daily automated updates:

- **Ecosystem discovery:** Nightly GitHub scan finds new Hermes-related repos.
- **MCP server scans:** MCP.so + mcpservers.org scanned daily. 312 servers listed with integration guides.
- **Skills.sh marketplace:** Daily scan for new Hermes skills. 343 setup guides published.
- **SEO pages:** 120 programmatic landing pages targeting operator search intent.
- **Content ops:** Automated internal linking, meta descriptions, OG tags, and sitemap generation.
- **Broken link repair:** Proactive weekly audit.

## Ongoing doc gaps

- **Connector count consistency ✅ (Aug 10, 2026):** Website updated to "40+ connected business tools." Normalized README.md (6 instances) from 37+ → 40+ to match corpusiq.io. Remaining 37+ instances in older published-content/ and hermes/launch/ files are technically still true (40 > 37) but flagged for next sweep.
- **Screenshots:** Quickstart screenshots pending — low priority, no user complaints.
- **DOC-GAP connectors:** 7 connectors (amazon_seller, gohighlevel, google_workspace, gunbroker, mongodb, postgres, postscript) in the connector registry need verified vendor setup steps — tracked in connector registry, not docs repo.
- **Sitemap dates:** Updated to 2026-08-10 (previously all showing 2026-06-17).

---

*Last updated: August 10, 2026. This repo is updated daily via automated crons. Canonical connector count: 40+ per corpusiq.io.*
---
