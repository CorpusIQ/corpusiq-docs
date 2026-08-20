# PROGRESS.md — corpusiq-docs build status

Current state and ongoing work for the public docs repository.

## File count (updated August 20, 2026)

- **Total Markdown files:** 1,852
- **Total HTML files:** 1,769 (MkDocs build output)
- **Hermes subdirectory:** 29 directories covering skills, MCP servers, setup guides, blueprints, ecosystem discovery, prompts, and more
- **Docs subdirectory:** 20 directories — SEO-optimized product pages, connector guides, troubleshooting, and comparison pages
- **Skills catalog:** 491 setup guides for Hermes skills
- **MCP servers:** 488 server listing markdown pages (+ HTML companions)
- **SEO pages:** 126 programmatic landing pages targeting high-intent operator keywords

## Site architecture

- **Main docs:** `https://www.corpusiq.io/docs/` — MkDocs Material, served on corpusiq.io
- **Hermes knowledge base:** `https://corpusiq.github.io/corpusiq-docs/hermes/` — GitHub Pages
- **SEO pages:** 100+ programmatic pages targeting high-intent keywords (e.g., "connect Shopify to ChatGPT," "MCP for ecommerce")
- **Daily automation:** Ecosystem discovery cron, skills.sh marketplace monitoring, MCP.so/mcpservers.org scans

## Items punting / skipped

- **No separate FAQ.** Folded into `how-it-works/` and `troubleshooting/` — a formal FAQ page can be added if user questions warrant it.

## Current status — August 20, 2026

The repo is actively maintained with daily automated updates:

- **Ecosystem discovery:** Nightly GitHub scan finds new Hermes-related repos.
- **MCP server scans:** MCP.so + mcpservers.org scanned daily. 488 servers listed with integration guides.
- **Skills.sh marketplace:** Daily scan for new Hermes skills. 491 setup guides published.
- **SEO pages:** 126 programmatic landing pages targeting operator search intent.
- **Content ops:** Automated internal linking, meta descriptions, OG tags, and sitemap generation.
- **Broken link repair:** Proactive weekly audit.

## Ongoing doc gaps

- **Maintenance ✅ (Aug 20, 2026):** Normalized 5 connector-count stragglers (36+ → 40+) across docs/architecture/README.md, odoo-mcp.md (x2), datamcp-mcp, and refreshed stale ecosystem stats (36+ pages → 1,700+, 326+ repos → 450+, 133+ skills → 490+). Refreshed PROGRESS.md stats (1,852 MD files, 491 skills, 488 MCP servers, 126 SEO pages). Internal links: 0 broken. Frontmatter: all valid. Deployed to Vercel, changed pages verified HTTP 200.
- **Maintenance ✅ (Aug 19, 2026):** Refreshed 21 stale `last_updated` dates (18 docs/*.md SEO pages stuck on 2026-06-16 + docs/index.md, hermes/index.md, hermes/README.md). Repointed 19 dead `skills.sh/aradotso/*` links to live GitHub repos (aradotso profile 404s on skills.sh) across 17 catalog/marketplace files. Fixed vibgrate trust link (`/mcp-trust` → `/trust`, was 404). Sanitized example private IP (10.0.0.100 → agent-a.local in meshtastic setup, verified absent upstream). Refreshed hermes-sitemap.xml (193 URLs) + sitemap-index.xml lastmod → 2026-08-19. Internal links: 0 broken. Deployed to Vercel, all changed pages HTTP 200.
- **Maintenance ✅ (Aug 17, 2026):** Fixed 2 broken internal links in skills catalog (chrome-devtools + oh-my-hermes setup guides → /hermes/best-practices/security/). Refreshed all 3 sitemaps (sitemap.xml 323 URLs + hermes-sitemap.xml 193 URLs + sitemap-index.xml) from 2026-08-10/2026-06-17 → 2026-08-17. Refreshed PROGRESS.md stats (1,742 MD files, 473 skills, 423 MCP servers).
- **Stale .html duplicates ✅ (Aug 15, 2026):** Removed 202 stale static .html files in hermes/ (22.8 MB) superseded by .md builds. They were copied into the site output as orphan pages with broken relative links (../../../quick-start.html → 404) and duplicate content. All had .md twins; none referenced in nav, sitemap, or .md content.
- **Sanitization ✅ (Aug 15, 2026):** Removed 5 internal-info instances: internal hostname + sweep ops note (new-aug15-2026 sweep page), personal name (etincel-mcp page), media@/info@ inbox handles (busymail-mcp page), hello@corpusiq.io demo value → hello@example.com (chrome-devtools setup), "on an internal worker" sweep note (new-aug12-2026-evening page).
- **Maintenance ✅ (Aug 16, 2026):** 103 user-facing files normalized 37+ → 40+ connectors (zero stragglers). Refreshed 2 stale dates (mcp-vs-data-warehouse, enterprise-ai-data-access). Removed internal outreach tracker (hermes/data/directory_submissions.json) + unreferenced demo asset; restored demo.mp4 (still linked from 2 pages). Sanitized historical PROGRESS.md identifiers. Internal links: 0 broken.
- **Root-level .html legacy files (119, ~12 MB):** Still in repo root but auto-excluded from MkDocs build (404 in production). Dead weight only; candidate for a future dedicated sweep.
- **Connector count consistency ✅ (Aug 10, 2026):** Website updated to "40+ connected business tools." Normalized README.md (6 instances) from 37+ → 40+ to match corpusiq.io. Remaining 37+ instances in older published-content/ and hermes/launch/ files are technically still true (40 > 37) but flagged for next sweep.
- **Screenshots:** Quickstart screenshots pending — low priority, no user complaints.
- **DOC-GAP connectors:** 7 connectors (amazon_seller, gohighlevel, google_workspace, gunbroker, mongodb, postgres, postscript) in the connector registry need verified vendor setup steps — tracked in connector registry, not docs repo.
- **Sitemap dates ✅ (Aug 14, 2026):** Updated hermes-sitemap.xml (193 URLs) + sitemap-index.xml from 2026-06-17 to 2026-08-14.
- **Stale dates ✅ (Aug 14, 2026):** 43 top-level docs/ SEO pages refreshed from 2026-07 → 2026-08-14.
- **Sanitization ✅ (Aug 14, 2026):** Removed invented 10.0.0.50/51 example IPs from hermes-plugins-42evey-setup.md (not in upstream repo) → replaced with agent-a.local/agent-b.local. Meshtastic 10.0.0.100 example verified as upstream content, kept.

---

*Last updated: August 20, 2026. This repo is updated daily via automated crons. Canonical connector count: 40+ per corpusiq.io.*
---
