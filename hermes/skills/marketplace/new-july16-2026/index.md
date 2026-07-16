---
title: New Skills Discovery — July 16, 2026
description: 4 new skills discovered via skills.sh batch sweep. Agent Browser (38K⭐), Vercel Agent Skills (29K⭐), Apify Agent Skills (2.2K⭐), and ClawFu Skills (134⭐) — browser automation, development quality, web scraping, and marketing methodologies.
---

# New Skills — July 16, 2026

Morning sweep across 33 broad search terms on skills.sh surfaced **4 new skills** not previously catalogued in the Hermes docs. These span browser automation (38K⭐ Vercel Labs), development quality (29K⭐ Vercel), web scraping (2.2K⭐ Apify), and marketing methodologies (134⭐ ClawFu). Combined install base: **70,000+ GitHub stars**.

## Skills Discovered

| Skill | Stars | Source | Category |
|---|---|---|---|
| [agent-browser](#agent-browser) | 38,590 | vercel-labs/agent-browser | Browser Automation |
| [vercel-agent-skills](#vercel-agent-skills) | 29,139 | vercel-labs/agent-skills | Development / Quality |
| [apify-agent-skills](#apify-agent-skills) | 2,232 | apify/agent-skills | Web Scraping |
| [clawfu-skills](#clawfu-skills) | 134 | guia-matthieu/clawfu-skills | Marketing |

---

## agent-browser

**Source:** [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) · **38,590⭐** · **Rust + Node.js**

Fast native Rust CLI for browser automation, purpose-built for AI agents. Uses Chrome for Testing with accessibility-tree-based interaction (snap + refs) plus traditional CSS selectors. No Playwright or Node.js runtime dependency for the daemon. Install via npm, Homebrew, or Cargo.

### Capabilities
- **Accessibility snapshots:** `agent-browser snapshot` returns tree with refs (@e1, @e2...)
- **Ref-based interaction:** Click, fill, and get text using accessibility refs — no selectors needed
- **Traditional selectors:** CSS selector support for direct element targeting
- **JavaScript evaluation:** Execute arbitrary JS in page context
- **Daemon mode:** Persistent browser sessions across multiple operations
- **Screenshots:** Full-page and viewport capture

### Installation
```bash
npm install -g agent-browser
agent-browser install
```

### Hermes/CorpusIQ Relevance
Massive for competitive research, social media monitoring, and web scraping. The accessibility-tree approach means agents don't need to build fragile CSS selectors — they can work with semantic element refs that survive DOM changes. At 38K stars, this is the most popular agent-specific browser tool.

**Setup guide:** [agent-browser-setup.md](/hermes/skills/catalog/agent-browser-setup/)

---

## vercel-agent-skills

**Source:** [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) · **29,139⭐** · **JavaScript**

Vercel's official collection of 4 skills for AI coding agents: vercel-optimize (cost/performance audit), react-best-practices (40+ rules), web-design-guidelines (100+ rules), and writing-guidelines (80+ rules). Follows the Agent Skills format.

### Capabilities
- **vercel-optimize:** Audit Vercel projects for cost, performance, caching, function usage
- **react-best-practices:** 40+ rules across 8 categories (waterfalls, bundle size, SSR, re-renders)
- **web-design-guidelines:** 100+ rules for accessibility, performance, UX, dark mode
- **writing-guidelines:** 80+ rules for voice, structure, content types, typography

### Installation
```bash
npx skills add vercel-labs/agent-skills
```

### Hermes/CorpusIQ Relevance
Directly applicable to corpusiq-docs maintenance. `vercel-optimize` can find billing savings on our Vercel deployment. `web-design-guidelines` catches a11y issues before launch. `react-best-practices` enforces performance standards. `writing-guidelines` ensures consistent content quality across 1,000+ docs pages.

**Setup guide:** [vercel-agent-skills-setup.md](/hermes/skills/catalog/vercel-agent-skills-setup/)

---

## apify-agent-skills

**Source:** [apify/agent-skills](https://github.com/apify/agent-skills) · **2,232⭐** · **Python**

Production-grade web scraping and automation skills for AI coding agents. 5 skills covering site scraping, Actor building, code Actorization, output schema generation, and API integration. Access to 30,000+ pre-built Actors across social, search, maps, real estate, reviews, and commerce platforms.

### Capabilities
- **Scrape any site:** 130+ curated Actors + 30,000+ Store fallback
- **Build new Actors:** Generate, debug, deploy serverless Actors in JS/TS/Python
- **Actorize code:** Wrap any script/library/CLI as a runnable Actor
- **Output schemas:** Auto-derive dataset schemas from Actor source
- **API integration:** Call Actors programmatically via apify-client or REST

### Installation
```bash
npx skills add apify/agent-skills
```

### Hermes/CorpusIQ Relevance
Transforms competitive intel and market research capabilities. Instead of building custom scrapers for each platform, agents can leverage Apify's maintained Actor library. Instagram, TikTok, LinkedIn, Reddit, Google Maps, Yelp — all accessible through one skill set. MCP-compatible for native Hermes tool integration.

**Setup guide:** [apify-agent-skills-setup.md](/hermes/skills/catalog/apify-agent-skills-setup/)

---

## clawfu-skills

**Source:** [guia-matthieu/clawfu-skills](https://github.com/guia-matthieu/clawfu-skills) · **134⭐** · **Python (MCP Server)**

175 expert marketing methodologies encoded as agent-readable skills. Dunford on positioning, Schwartz on copywriting, Cialdini on persuasion, Ogilvy on advertising, Hormozi on offers, Voss on negotiation — 28 categories delivered as an MCP server. Free, MIT licensed.

### Capabilities
- **Content (24 skills):** Copywriting, storytelling, persuasion, SEO writing
- **Strategy (17 skills):** Positioning, competitive analysis, JTBD, cognitive biases
- **Validation (8 skills):** Mom Test, customer discovery, lean canvas, pricing validation
- **Growth (4 skills):** Growth loops (Reforge), PLG (Wes Bush), referral systems
- **Sales (6 skills):** Sales narrative, SPIN selling, MEDDIC, negotiation
- **Plus:** SEO Tools, RevOps, SDR Automation, Funnels, Startup, Product, Leadership, Crisis, Branding, Analytics

### Installation
```bash
npx @clawfu/mcp-skills
```

### Hermes/CorpusIQ Relevance
This is the marketing brain CorpusIQ agents have been missing. Instead of improvising growth tactics, agents can now load battle-tested frameworks from the world's best marketers. Positioning (Dunford) for competitive messaging. Copywriting (Schwartz) for landing pages. Mom Test for customer discovery. Growth Loops (Reforge) for sustainable acquisition. Delivered as MCP — native Hermes tool integration.

**Setup guide:** [clawfu-skills-setup.md](/hermes/skills/catalog/clawfu-skills-setup/)

---

## Discovery Method

Sweep conducted using `npx skills search` CLI fallback (skills.sh website returned 500/Vercel error). 33 search terms queried: hermes, openclaw, clawd, claw, gbrain, browser, email, social, video, marketing, growth, mcp, memory, cron, backup, security, monitor, agent, skill, docs, github, deploy, seo, content, lead, outreach, forecasting, research, image, desktop, plugin, hyperframes, remotion.

78 unique repos surfaced. Cross-referenced against 108 existing catalog entries. 4 new skills identified. Compared against all July 2026 discovery pages to confirm no prior capture.

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Powered by CorpusIQ*
