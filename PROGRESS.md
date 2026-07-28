# PROGRESS.md — corpusiq-docs build status

Current state and ongoing work for the public docs repository.

## File count (updated July 28, 2026)

- **Total Markdown files:** 976
- **Total HTML files:** 1,300+ (MkDocs build output)
- **Hermes subdirectory:** 25 directories covering skills, MCP servers, setup guides, blueprints, ecosystem discovery, prompts, and more
- **Docs subdirectory:** 13 directories — SEO-optimized product pages, connector guides, troubleshooting, and comparison pages
- **Skills catalog:** 415 setup guides for Hermes skills
- **MCP servers:** 167 server listing markdown pages (+ HTML companions)
- **Prompt library:** 16 published categories

## Site architecture

- **Main docs:** `https://www.corpusiq.io/docs/` — MkDocs Material, served on corpusiq.io
- **Hermes knowledge base:** `https://corpusiq.github.io/corpusiq-docs/hermes/` — GitHub Pages
- **SEO pages:** 100+ programmatic pages targeting high-intent keywords (e.g., "connect Shopify to ChatGPT," "MCP for ecommerce")
- **Daily automation:** Ecosystem discovery cron, skills.sh marketplace monitoring, MCP.so/mcpservers.org scans

## Items punting / skipped

- **No separate FAQ.** Folded into `how-it-works/` and `troubleshooting/` — a formal FAQ page can be added if user questions warrant it.

## Current status — July 28, 2026

The repo is actively maintained with daily automated updates:

- **Ecosystem discovery:** Nightly GitHub scan finds new Hermes-related repos.
- **MCP server scans:** MCP.so + mcpservers.org scanned daily. 255+ servers listed with integration guides.
- **Skills.sh marketplace:** Daily scan for new Hermes skills. 415 setup guides published.
- **SEO pages:** 100+ programmatic landing pages targeting operator search intent.
- **Content ops:** Automated internal linking, meta descriptions, OG tags, and sitemap generation.
- **Broken link repair:** Proactive weekly audit — 0 real broken links found (July 28 audit).

## Ongoing doc gaps

- **Connector count inconsistency (July 28, 2026):** ~15 pages still use "50+ connectors" while the canonical number is "37+". Fixed in `docs/index.md` and `docs/connectors.md` this cycle. Remaining pages needing sweep: `docs/best-ai-data-connector.md`, `docs/corpusiq-vs-custom-rag.md`, `docs/how-to-connect-business-data-to-chatgpt.md`, `docs/how-to-use-ai-with-business-data.md`, `docs/hubspot-business-intelligence.md`, `docs/security.md`, `docs/ai-for-business-intelligence.md`, `docs/best-mcp-server-for-business.md`, `docs/how-to-create-an-ai-data-layer.md`.
- **ai-agent-users.md:** Uses "38+" — should be "37+" for consistency.
- **Screenshots:** Quickstart screenshots pending — low priority, no user complaints.
- **DOC-GAP connectors:** 7 connectors (amazon_seller, gohighlevel, google_workspace, gunbroker, mongodb, postgres, postscript) in the connector registry need verified vendor setup steps — tracked in connector registry, not docs repo.

---

*Last updated: July 28, 2026. This repo is updated daily via automated crons.*
---
