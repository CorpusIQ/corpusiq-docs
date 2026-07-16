# PROGRESS.md — corpusiq-docs build status

Current state and ongoing work for the public docs repository.

## File count (updated July 16, 2026)

- **Total Markdown files:** 1,034
- **Total HTML files:** 1,085 (MkDocs build output)
- **Total lines:** ~109,600 across all docs
- **Hermes subdirectory:** 175 directories covering skills, MCP servers, setup guides, blueprints, and ecosystem discovery
- **Docs subdirectory:** 13 directories — SEO-optimized product pages, connector guides, troubleshooting, and comparison pages

## Site architecture

- **Main docs:** `https://www.corpusiq.io/docs/` — MkDocs Material, served on corpusiq.io
- **Hermes knowledge base:** `https://corpusiq.github.io/corpusiq-docs/hermes/` — GitHub Pages, 1,034 markdown pages
- **SEO pages:** 100+ programmatic pages targeting high-intent keywords (e.g., "connect Shopify to ChatGPT," "MCP for ecommerce")
- **Skills catalog:** 112 setup guides for Hermes skills
- **MCP servers:** 200+ server listings with integration guides
- **Daily automation:** Ecosystem discovery cron, skills.sh marketplace monitoring, MCP.so/mcpservers.org scans

## Items punting / skipped

- **No separate FAQ.** Folded into `how-it-works/` and `troubleshooting/` — a formal FAQ page can be added if user questions warrant it.

## Current status — July 16, 2026

The repo is actively maintained with daily automated updates:

- **Ecosystem discovery:** Nightly GitHub scan finds new Hermes-related repos. 15-20 new repos/week added to pending review.
- **MCP server scans:** MCP.so + mcpservers.org scanned daily. 200+ servers listed with integration guides.
- **Skills.sh marketplace:** Daily scan for new Hermes skills. 112 setup guides published.
- **SEO pages:** 100+ programmatic landing pages targeting operator search intent.
- **Content ops:** Automated internal linking, meta descriptions, OG tags, and sitemap generation.
- **Broken link repair:** Proactive weekly audit fixes 404s and redirects.

## Ongoing doc gaps

- **Screenshots:** 11 placeholder markers in `quickstart/` still need real captures.
- **DOC-GAP connectors:** 7 connectors in the registry (amazon_seller, gohighlevel, google_workspace, gunbroker, mongodb, postgres, postscript) need verified vendor setup steps.
- **Prompt library expansion:** Only 5 of 17 planned prompt categories currently published.

---

*Last updated: July 16, 2026. This repo is updated daily via automated crons.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
