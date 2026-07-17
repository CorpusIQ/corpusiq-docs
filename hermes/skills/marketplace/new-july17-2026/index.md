---
title: New Skills Discovery — July 17, 2026
description: 5 new skills discovered via skills.sh batch sweep. find-skills (2.5M⭐), skill-creator (317K⭐), remotion-best-practices (430K⭐), browser-act (99K⭐), and firecrawl-workflows (120K⭐ combined) — skill discovery, creation, video production, browser automation, and growth workflows.
---

# New Skills — July 17, 2026

Morning sweep across 35 broad search terms on skills.sh surfaced **5 new skills** not previously catalogued in the Hermes docs. These span skill discovery (2.5M⭐ Vercel Labs), skill creation (317K⭐ Anthropic), video production (430K⭐ Remotion), browser automation (99K⭐ Browser Act), and growth workflows (120K⭐ Firecrawl combined). Combined install base: **3.5M+ GitHub stars**.

## Skills Discovered

| Skill | Stars/Installs | Source | Category |
|---|---|---|---|
| [find-skills](#find-skills) | 2,500,000 | vercel-labs/skills | Skill Discovery |
| [remotion-best-practices](#remotion-best-practices) | 430,200 | remotion-dev/skills | Video Production |
| [skill-creator](#skill-creator) | 317,700 | anthropics/skills | Skill Development |
| [browser-act](#browser-act) | 99,500 | browser-act/skills | Browser Automation |
| [firecrawl-workflows](#firecrawl-workflows) | 120,000+ | firecrawl/firecrawl-workflows | Growth & Research |

---

## find-skills

**Source:** [vercel-labs/skills](https://github.com/vercel-labs/skills) · **2.5M installs** · **JavaScript**

The official skill discovery tool from Vercel Labs. Searches across skills.sh, agentskills.io, npm, and GitHub to find agent skills matching any query. Returns installable skill references with metadata — source repo, install count, category, and compatibility info. At 2.5M installs, this is the most-used skill in the ecosystem.

### Capabilities
- **Multi-marketplace search:** skills.sh, agentskills.io, npm, GitHub — all in one query
- **Install-count ranking:** Results sorted by community adoption
- **Category filtering:** Narrow by browser, marketing, development, operations, etc.
- **Hermes compatibility detection:** Flags skills compatible with Hermes agent runtime
- **Direct install path:** Each result includes the `npx skills add` command

### Installation
```bash
npx skills add vercel-labs/skills@find-skills
```

### Hermes/CorpusIQ Relevance
This is the definitive skill discovery tool for Hermes agents. Instead of running 30+ manual `npx skills search` queries, agents can use `find-skills` to search across all marketplaces in one call. For CorpusIQ's skill catalog maintenance, this automates the daily "check for new skills" workflow — making the entire catalog operation self-sustaining.

**Setup guide:** [find-skills-setup.md](/hermes/skills/catalog/find-skills-setup/)

---

## remotion-best-practices

**Source:** [remotion-dev/skills](https://github.com/remotion-dev/skills) · **430.2K installs** · **TypeScript**

Official Remotion best practices for AI coding agents. Covers programmatic video creation patterns: composition structure, rendering optimization, audio synchronization, caption generation, and asset management. At 430K installs, this is the most-installed video production skill in the ecosystem — used by HeyGen HyperFrames, Google Labs Stitch, and thousands of AI video projects.

### Capabilities
- **Composition patterns:** Correct use of `<Composition>`, `<Sequence>`, `<AbsoluteFill>`
- **Rendering optimization:** Parallel rendering, concurrency tuning, caching strategies
- **Audio workflow:** `useAudioData()`, audio trimming, crossfade patterns
- **Caption generation:** Word-level timing, animation presets, multi-speaker support
- **Asset management:** `staticFile()`, remote assets, lazy loading, preloading
- **Common pitfalls:** Duration mismatches, frame rate drops, memory leaks in long renders

### Installation
```bash
npx skills add remotion-dev/skills@remotion-best-practices
```

### Hermes/CorpusIQ Relevance
Directly applicable to CorpusIQ's UGC video pipeline. The HyperFrames integration uses Remotion under the hood — these best practices prevent the frame drops, audio drift, and memory leaks that plagued earlier video automation attempts. Also relevant for the daily UGC video series and any programmatic content generation.

**Setup guide:** [remotion-best-practices-setup.md](/hermes/skills/catalog/remotion-best-practices-setup/)

---

## skill-creator

**Source:** [anthropics/skills](https://github.com/anthropics/skills) · **317.7K installs** · **Python**

Anthropic's official skill creation framework for AI coding agents. Guides agents through the complete skill authoring lifecycle: scoping the workflow, writing the SKILL.md with correct YAML frontmatter, testing with dry runs, handling error paths, and publishing to marketplaces. The same framework used internally by Anthropic for their 60+ published skills.

### Capabilities
- **Workflow scoping:** Identify the right granularity — neither too broad nor too narrow
- **YAML frontmatter:** Required fields, optional metadata, trigger configuration
- **Tool manifest:** Declare required tools and connectors with version constraints
- **Error handling:** Pattern library for timeouts, rate limits, missing data, auth failures
- **Verification gates:** Pre/post conditions, dry-run support, idempotency checks
- **Publishing:** Format for skills.sh, GitHub, npm — with compatibility metadata

### Installation
```bash
npx skills add anthropics/skills@skill-creator
```

### Hermes/CorpusIQ Relevance
Essential for CorpusIQ's 133+ skill library. Replaces ad-hoc skill authoring with a structured framework. Ensures every new skill meets quality standards before deployment. The error-handling pattern library alone prevents the "skill breaks silently in production" failures that have cost hours of debugging. Used in conjunction with `find-skills` to complete the skill lifecycle: discover → create → publish.

**Setup guide:** [skill-creator-setup.md](/hermes/skills/catalog/skill-creator-setup/)

---

## browser-act

**Source:** [browser-act/skills](https://github.com/browser-act/skills) · **99.5K installs** · **Python + Playwright**

Agent-native browser automation framework built on Playwright. Unlike agent-browser (Rust/accessibility-tree), browser-act uses a "skill forge" approach — agents record browser interactions as reusable skill templates, then replay them with parameter substitution. Includes browser-act-skill-forge (78.7K installs) for creating new interaction templates.

### Capabilities
- **Skill recording:** Record browser interactions as reusable templates
- **Parameter substitution:** Replace recorded values (URLs, search terms, form data) at runtime
- **Anti-detection:** Built-in fingerprint randomization and bot detection evasion
- **Playwright-native:** Full Playwright API access for complex interactions
- **Skill forge:** Visual editor for creating and debugging interaction templates
- **Session persistence:** Browser state survives across skill invocations

### Installation
```bash
# Core browser automation
npx skills add browser-act/skills@browser-act

# Skill forge for creating templates
npx skills add browser-act/skills@browser-act-skill-forge
```

### Hermes/CorpusIQ Relevance
Complements agent-browser for CorpusIQ's browser automation needs. Where agent-browser excels at accessibility-tree interaction (fast, semantic, selector-free), browser-act excels at recording reusable workflows. Use browser-act for: social media monitoring templates (login → check notifications → extract mentions), competitive research (visit competitor sites → screenshot → extract pricing), and form automation. The anti-detection features are critical for platforms that block headless browsers.

**Setup guide:** [browser-act-setup.md](/hermes/skills/catalog/browser-act-setup/)

---

## firecrawl-workflows

**Source:** [firecrawl/firecrawl-workflows](https://github.com/firecrawl/firecrawl-workflows) · **120K+ combined installs** · **TypeScript**

Production-grade web research and growth workflows from Firecrawl. Four high-value workflows: deep-research (30.5K, multi-page research synthesis), lead-gen (29.1K, automated lead discovery and enrichment), market-research (29.4K, competitive landscape analysis), and seo-audit (29.2K, technical SEO analysis). All built on Firecrawl's web scraping infrastructure with built-in rate limiting, proxy rotation, and JavaScript rendering.

### Capabilities

**firecrawl-deep-research (30.5K):**
- Multi-page research with source tracking and citation
- Automatic sub-question generation for comprehensive coverage
- Structured output: executive summary, key findings, sources

**firecrawl-lead-gen (29.1K):**
- Domain-filtered lead discovery from target websites
- Contact enrichment: email, LinkedIn, company size, funding
- CRM-ready output format

**firecrawl-market-research (29.4K):**
- Competitive landscape mapping
- Feature comparison matrices
- Pricing analysis and positioning insights

**firecrawl-seo-audit (29.2K):**
- Technical SEO crawl (broken links, redirects, metadata)
- Content gap analysis
- Competitor keyword comparison

### Installation
```bash
npx skills add firecrawl/firecrawl-workflows@firecrawl-deep-research
npx skills add firecrawl/firecrawl-workflows@firecrawl-lead-gen
npx skills add firecrawl/firecrawl-workflows@firecrawl-market-research
npx skills add firecrawl/firecrawl-workflows@firecrawl-seo-audit
```

### Hermes/CorpusIQ Relevance
Directly powers CorpusIQ's growth and research operations. `firecrawl-deep-research` replaces hours of manual competitive analysis. `firecrawl-lead-gen` automates prospect discovery for outreach campaigns. `firecrawl-market-research` feeds the product roadmap with competitive intelligence. `firecrawl-seo-audit` maintains corpusiq-docs' search visibility. All four workflows integrate with Hermes via the existing Firecrawl MCP connector.

**Setup guide:** [firecrawl-workflows-setup.md](/hermes/skills/catalog/firecrawl-workflows-setup/)

---

## Discovery Method

Sweep conducted using `npx skills search` CLI (skills.sh website returned 500/Vercel errors — CLI fallback functional). 35 search terms queried: hermes, openclaw, clawd, claw, gbrain, browser, email, social, video, marketing, growth, mcp, memory, cron, backup, security, monitor, agent, skill, docs, github, deploy, seo, content, lead, outreach, forecasting, research, image, desktop, plugin, hyperframes, remotion, coding, automation.

120+ unique repos surfaced. Cross-referenced against 108 existing catalog entries and all 12 marketplace discovery pages (June 15 — July 16, 2026). 5 new skills identified. Compared against all prior discovery pages to confirm no prior capture.

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Powered by CorpusIQ*
