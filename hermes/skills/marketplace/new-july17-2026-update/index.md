---
title: New Skills Discovery — July 17, 2026 (Afternoon Update)
description: 5 new skills discovered via skills.sh afternoon sweep. marketingskills (160K⭐+ combined), ai-video-generation (196K⭐), taste-skill (156K⭐), web-quality-skills (37K⭐), and rigorpilot-skills (140K⭐) — marketing, video, design, web quality, and AI research.
---

# New Skills — July 17, 2026 (Update)

Afternoon follow-up sweep across 35 search terms on skills.sh surfaced **5 new high-value skills** not previously catalogued. This sweep specifically targeted repos that appeared in the morning's broad scan but weren't captured in the initial discovery set. Combined install base: **690,000+ installs**.

## Skills Discovered

| Skill | Stars/Installs | Source | Category |
|---|---|---|---|
| [marketingskills](#marketingskills) | 160,000+ | coreyhaines31/marketingskills | Marketing Suite |
| [ai-video-generation](#ai-video-generation) | 196,300 | 101-skills/skills | AI Media / Video |
| [taste-skill](#taste-skill) | 156,100 | leonxlnx/taste-skill | Design / Image Gen |
| [rigorpilot-skills](#rigorpilot-skills) | 140,100 | lllllllama/rigorpilot-skills | Research / AI |
| [web-quality-skills](#web-quality-skills) | 37,000 | addyosmani/web-quality-skills | Web Quality / SEO |

---

## marketingskills

**Source:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · **160K+ combined installs** · **JavaScript/Python**

The most comprehensive marketing skill suite on skills.sh — 12 production-grade skills covering SEO, copywriting, psychology, content strategy, lead generation, social media, and AI-powered marketing. At 160K+ combined installs, this is the #1 marketing toolkit for AI coding agents.

### Skills Included

| Skill | Installs | Category |
|---|---|---|
| `seo-audit` | 163.9K | Technical SEO analysis |
| `copywriting` | 154.1K | Persuasive marketing copy |
| `marketing-psychology` | 113.0K | Consumer behavior & persuasion |
| `content-strategy` | 108.4K | Content planning & calendars |
| `programmatic-seo` | 104.0K | Automated SEO at scale |
| `marketing-ideas` | 101.1K | Creative campaign generation |
| `ai-seo` | 92.4K | AI-optimized SEO |
| `lead-magnets` | 70.8K | Lead capture & conversion |
| `social-content` | 67.5K | Social media content creation |
| `product-marketing-context` | 61.6K | Positioning & messaging |
| `image` | 44.9K | Marketing image generation |
| `social` | 36.8K | Social media strategy |

### Installation

```bash
# Install individual skills as needed
npx skills add coreyhaines31/marketingskills@seo-audit
npx skills add coreyhaines31/marketingskills@copywriting
npx skills add coreyhaines31/marketingskills@content-strategy

# Or install the full suite (if available as a bundle)
npx skills add coreyhaines31/marketingskills
```

### Hermes/CorpusIQ Relevance

This is the marketing brain CorpusIQ needs. Instead of reinventing growth tactics, agents can leverage battle-tested frameworks: `seo-audit` for corpusiq-docs optimization, `copywriting` for landing pages and ads, `content-strategy` for the content calendar, `lead-magnets` for conversion optimization, and `social-content` for the daily posting cadence. Combined with the existing clawfu-skills (175 methodologies), this creates the most complete AI marketing stack available.

**Setup guide:** [marketingskills-setup.md](/hermes/skills/catalog/marketingskills-setup/)

---

## ai-video-generation

**Source:** [101-skills/skills](https://github.com/101-skills/skills) · **196.3K installs** · **TypeScript/Python**

Production-grade AI video generation skill for coding agents. Covers the complete video creation pipeline: script generation, scene composition, AI avatar integration, voiceover synthesis, and multi-format export. The `ai-avatar-video` companion skill (195.8K installs) adds AI presenter capabilities — synthetic avatars that deliver scripts with natural motion and lip-sync.

### Capabilities

- **Script-to-video pipeline:** Generate complete videos from text descriptions
- **Scene composition:** Multi-scene videos with transitions and effects
- **AI avatars:** Synthetic presenters with lip-sync and gestures (`ai-avatar-video`)
- **Voiceover synthesis:** TTS integration with emotion and pacing control
- **Multi-format export:** MP4, WebM, GIF, and social-media-optimized formats
- **Template library:** Pre-built templates for product demos, tutorials, social clips

### Installation

```bash
npx skills add 101-skills/skills@ai-video-generation
npx skills add 101-skills/skills@ai-avatar-video
```

### Hermes/CorpusIQ Relevance

Directly powers CorpusIQ's UGC video pipeline alongside HyperFrames and Remotion. `ai-video-generation` handles the end-to-end production workflow while `ai-avatar-video` provides the synthetic presenter layer — enabling fully automated daily video content without human recording sessions. At 196K installs, this is the most-installed AI video skill in the ecosystem.

**Setup guide:** [ai-video-generation-setup.md](/hermes/skills/catalog/ai-video-generation-setup/)

---

## taste-skill

**Source:** [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) · **156.1K installs** · **TypeScript**

AI-powered design-to-code and image generation skill. Three high-install capabilities: `image-to-code` (156.1K) converts screenshots and designs into production-ready frontend code, `imagegen-frontend-web` (155.5K) generates web UI from text descriptions, and `imagegen-frontend-mobile` (151.9K) generates mobile UI designs. Built on top of modern AI image models with design-system awareness.

### Capabilities

- **image-to-code:** Screenshot → React/Vue/HTML with Tailwind/styled-components
- **imagegen-frontend-web:** Text prompt → responsive web UI with component hierarchy
- **imagegen-frontend-mobile:** Text prompt → React Native/Flutter mobile screens
- **Design system awareness:** Respects existing design tokens, color palettes, typography
- **Iterative refinement:** "Make the button more rounded" → targeted regeneration
- **Accessibility-first:** Generated code includes ARIA labels, semantic HTML, color contrast

### Installation

```bash
npx skills add leonxlnx/taste-skill@image-to-code
npx skills add leonxlnx/taste-skill@imagegen-frontend-web
npx skills add leonxlnx/taste-skill@imagegen-frontend-mobile
```

### Hermes/CorpusIQ Relevance

Transforms CorpusIQ's design workflow. `image-to-code` bridges the design↔development gap — screenshot a competitor's UI and generate equivalent code. `imagegen-frontend-web` accelerates landing page and dashboard creation. For the corpusiq-docs site, generates consistent, accessible page designs. At 156K installs, this is the top design-to-code skill on skills.sh.

**Setup guide:** [taste-skill-setup.md](/hermes/skills/catalog/taste-skill-setup/)

---

## rigorpilot-skills

**Source:** [lllllllama/rigorpilot-skills](https://github.com/lllllllama/rigorpilot-skills) · **140.1K installs** · **Python**

Scientific-grade AI research skills for coding agents. Two complementary capabilities: `ai-research-explore` (140.1K) performs deep literature reviews, hypothesis generation, and gap analysis across academic and technical domains. `ai-research-reproduction` (139.8K) validates research claims by reproducing experiments, checking methodologies, and verifying statistical results.

### Capabilities

- **Literature review:** Multi-source search across arXiv, PubMed, Semantic Scholar, papers with code
- **Hypothesis generation:** Identify research gaps and propose testable hypotheses
- **Gap analysis:** Map existing research landscape, flag underexplored areas
- **Experiment reproduction:** Re-run published experiments, verify claims
- **Methodology audit:** Check statistical methods, sample sizes, p-value validity
- **Citation graph:** Map paper influence, identify seminal works, track idea lineage

### Installation

```bash
npx skills add lllllllama/rigorpilot-skills@ai-research-explore
npx skills add lllllllama/rigorpilot-skills@ai-research-reproduction
```

### Hermes/CorpusIQ Relevance

Elevates CorpusIQ's competitive intelligence and market research capabilities. `ai-research-explore` complements firecrawl-deep-research with academic-grade rigor — find the papers behind the products. `ai-research-reproduction` validates competitor claims by checking if their published benchmarks actually reproduce. Essential for the "data-driven" doctrine when evaluating AI tools and platforms.

**Setup guide:** [rigorpilot-skills-setup.md](/hermes/skills/catalog/rigorpilot-skills-setup/)

---

## web-quality-skills

**Source:** [addyosmani/web-quality-skills](https://github.com/addyosmani/web-quality-skills) · **37K installs** · **JavaScript**

Web quality audit skills from Addy Osmani (Google Chrome engineering lead). Four skills covering accessibility (37K), SEO (33.4K), performance (23.5K), and comprehensive web quality audits (16.5K). Encodes Google's own web quality standards — the same criteria used by Lighthouse, PageSpeed Insights, and Chrome DevTools.

### Capabilities

- **accessibility:** WCAG 2.1 AA/AAA audit, ARIA validation, screen reader testing, color contrast
- **seo:** Technical SEO crawl, meta tag audit, structured data validation, Core Web Vitals
- **performance:** Lighthouse audit, bundle analysis, render-blocking detection, LCP/INP/CLS optimization
- **web-quality-audit:** Combined accessibility + SEO + performance in one pass, prioritized fix list

### Installation

```bash
npx skills add addyosmani/web-quality-skills@accessibility
npx skills add addyosmani/web-quality-skills@seo
npx skills add addyosmani/web-quality-skills@performance
npx skills add addyosmani/web-quality-skills@web-quality-audit
```

### Hermes/CorpusIQ Relevance

Directly applicable to corpusiq-docs quality. The `seo` skill ensures every docs page meets Google's ranking criteria. `accessibility` catches a11y issues before they affect users. `performance` optimizes Core Web Vitals for better search rankings. `web-quality-audit` combines all three into a single automated check — perfect for CI integration. From the Chrome engineering lead himself — these are the definitive web quality standards.

**Setup guide:** [web-quality-skills-setup.md](/hermes/skills/catalog/web-quality-skills-setup/)

---

## Discovery Method

Afternoon sweep conducted using `npx skills search` CLI (skills.sh website and Firecrawl still down — CLI only path). Same 35-term query list as the morning sweep: hermes, openclaw, clawd, claw, gbrain, browser, email, social, video, marketing, growth, mcp, memory, cron, backup, security, monitor, agent, skill, docs, github, deploy, seo, content, lead, outreach, forecasting, research, image, desktop, plugin, hyperframes, remotion, coding, automation.

120+ unique repos surfaced. Cross-referenced against 113 existing catalog entries and all 13 marketplace discovery pages (June 9 — July 17 morning). Focused specifically on repos that appeared in the morning's broad scan but weren't captured in the initial discovery set. 5 new high-value skills identified.

The `coreyhaines31/marketingskills` repo was mentioned as "previously catalogued" in the June 11 discovery page but never received a dedicated setup guide — now fully documented with all 12 constituent skills.

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Powered by CorpusIQ*
