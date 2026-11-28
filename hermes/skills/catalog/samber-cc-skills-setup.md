---
title: "Samber CC Skills - Marketing & Engineering Suite Setup"
description: "samber/cc-skills: 115.2K combined installs. Marketing and engineering agent skills for copywriting, frontend design, Chrome extensions and research."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/samber-cc-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "copywriting", "frontend design", "chrome extension"]
---

# Samber CC Skills - Setup Guide

**Source:** [samber/cc-skills](https://www.skills.sh/samber/cc-skills) via skills.sh - 115.2K combined installs across 21 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [samber/cc-skills](https://github.com/samber/cc-skills) - 332 stars, MIT, branch main, last pushed 2026-11-01; skills live under `skills/<name>/SKILL.md`, each with reference markdown, assets or eval files in its own directory.

**Category:** Marketing and content copywriting, frontend design, Chrome extension development, engineering workflows and research for agent runtimes

**Quality Tier:** 🟡 Yellow - no Fail cells across 20 sampled listings; eight Warn cells span six skills, with site-launch-checklist warned by all three scanners.

Samber CC Skills is a collection of agentic skills by [@samber](https://github.com/samber) spanning marketing, content and engineering work. The README describes the repository as "marketing and engineering skills" designed as atomic units that cross-reference each other, with each skill kept as a small SKILL.md entry point plus reference files loaded on demand so only the relevant content enters context. The author is explicit that the skills were "edited, tested, reviewed and reworked by a human" rather than shipped raw from a model.

The suite is one of several samber repositories the catalog documents, but it is a separate repository from samber/golang-skills and samber/developer-platform-skills, which cover Go engineering and API and DX skills respectively. The copywriting cluster is the largest group here, and it is deliberately cross-wired: hooks, CTAs, tone of voice, prose and two humanizers point at each other rather than overlapping. The engineering side pairs chrome-extension with a CRXJS/HMR counterpart and adds a PromQL CLI and Conventional Commits standard, so one install covers marketing and engineering work.

## Installation

The README splits installation by runtime. The skills CLI installs every skill or a single skill, Claude Code and Codex use plugin marketplaces, and the remaining runtimes clone into a cross-client discovery directory:

```text
npx skills add https://github.com/samber/cc-skills --all
# or a single skill:
npx skills add https://github.com/samber/cc-skills --skill promql-cli
```

Claude Code installs through the marketplace slash commands:

```text
/plugin marketplace add samber/cc
/plugin install cc-skills@samber
```

Codex users run `codex plugin add github:samber/cc-skills`. Gemini CLI users run `gemini extensions install https://github.com/samber/cc-skills` and update with `gemini extensions update cc-skills`. For Openclaw, Cursor, Copilot, OpenCode and Antigravity, clone the repo into the runtime's skills directory (for example `~/.cursor/skills/cc-skills`, `~/.copilot/skills/cc-skills`, `~/.agents/skills/cc-skills` or `~/.antigravity/skills/cc-skills`), which each runtime auto-discovers.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| copywriting-hooks | 6,827 | Opening hooks and post titles for long-form articles in English or French, from blog posts to newsletters. |
| frontend-design-deslop | 6,239 | Distinctive, non-generic UI with typography, OKLCH color, design tokens, layout, motion, dark mode and accessibility. |
| linkedin-ghostwriting | 6,009 | B2B LinkedIn ghostwriting with hooks, post structures and copywriting frameworks for conversion-focused posts. |
| copywriting-tone-of-voice-creator | 5,928 | A brand tone of voice guide (TONE.md) with voice attributes, a modulation matrix, lexicon and channel rules. |
| deep-research | 5,755 | Deep research with parallel web searches, multi-source validation, confidence tracking and a cited Markdown report. |
| humaniseur-fr | 5,740 | Removing AI-writing patterns from French text and injecting voice and personality. |
| copywriting-cta | 5,687 | End-of-article CTAs with copy, layout, placement, an A/B test plan and accessibility notes. |
| technical-article-writer | 5,613 | Technical articles and blog posts for developer audiences, from tutorials to postmortems. |
| site-launch-checklist | 5,551 | A pre-launch checklist for shipping a website or web app, from analytics and security headers to SEO and monitoring. |
| conventional-git | 5,498 | Conventional Commits v1.0.0 for branch naming, worktree naming and commit messages. |
| copywriting-prose-creator | 5,441 | Codifying how a person or brand writes into a PROSE.md guide: lexicon, syntax, rhythm and structure. |
| influence-and-negotiation | 5,410 | An influence and negotiation toolkit for B2B sales, salary reviews, hard conversations and diplomatic drafting. |
| chrome-extension | 5,390 | Chrome extensions with Manifest V3, from content scripts and service workers to Web Store publishing. |
| press-release-writer | 5,342 | Professional press releases for any occasion, media type and region. |
| substack-ghostwriting | 5,313 | Writing, optimizing and growing Substack content, from newsletter issues to web-first essays and growth tactics. |
| promql-cli | 5,282 | A CLI for querying Prometheus and PromQL-compatible engines with instant queries, range queries and metric discovery. |
| snyk-agent-scan-compliance | 5,194 | Compliance guidance for snyk-agent-scan, fixing alerts through content restructuring rather than suppression. |
| crxjs | 5,172 | CRXJS Chrome extension development with Vite, true HMR and type-safe manifests. |
| skill-progressive-disclosure-design | 5,136 | Deciding how to split skill content between SKILL.md and reference files for context efficiency. |
| training-report | 5,102 | A professional training or workshop report as a .docx file with participant feedback and recommendations. |
| humanizer-en-asd-ste100 | 3,579 | Rewriting English into ASD-STE100 Simplified Technical English and de-slopping technical documentation. |

All 21 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

This suite is a worked example of the atomic, cross-referencing skill pattern: each skill lives in its own directory with a small SKILL.md entry point and reference files loaded on demand, so context stays lean while depth is available. The README is explicit that skills cross-reference and that installing only a subset gives a partial, inconsistent view of the guidelines, which is a useful discipline for any builder assembling an agent skill library.

The copywriting group is the strongest cluster: hooks, CTAs, tone of voice, prose and two humanizers form a pipeline that covers English and French, which is rare among published skill suites. The engineering side pairs chrome-extension with its CRXJS counterpart and ships a PromQL CLI plus a Conventional Commits standard, so a single install spans marketing and engineering work.

The README also publishes its own evaluation numbers: 98% with skills versus 52% without, plus a per-skill error-rate gap. That transparency is uncommon for a skill collection and gives a builder a way to judge each skill before wiring it into a router. The meta skills make the suite self-describing: snyk-agent-scan-compliance teaches the scanner rules the suite must pass, and skill-progressive-disclosure-design teaches how to split skill content for lazy loading.

## Usage

| You say | What happens |
|---|---|
| "Write an opening hook for my next blog post" | Loads copywriting-hooks to propose titles and opening hooks with distinct psychological levers. |
| "Make this landing page not look like AI slop" | Loads frontend-design-deslop to build a distinctive UI with typography, OKLCH color and design tokens. |
| "Ghostwrite a LinkedIn post from this founder story" | Loads linkedin-ghostwriting to turn the story into a conversion-focused post. |
| "Do a deep dive on the competitors in this space" | Loads deep-research to run parallel searches and produce a cited Markdown report. |
| "Build me a Chrome extension with hot reload" | Loads crxjs for a Vite-based build, or chrome-extension for plain Manifest V3 architecture. |
| "Write the press release for our funding round" | Loads press-release-writer to draft the announcement with region-specific conventions. |
| "This French copy reads like ChatGPT" | Loads humaniseur-fr to strip AI patterns and inject voice. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/samber/cc-skills/main/skills/copywriting-hooks/SKILL.md
```

After a clone, confirm the layout and the number of in-tree skills:

```bash
git clone --depth 1 https://github.com/samber/cc-skills.git /tmp/cc-skills
ls /tmp/cc-skills/skills/ | wc -l
head -3 /tmp/cc-skills/skills/promql-cli/SKILL.md
```

The count should print 21 skill directories, matching the 21 indexed listings, and head should show the promql-cli frontmatter.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| copywriting-hooks | Pass | Pass | Pass |
| frontend-design-deslop | Pass | Pass | Pass |
| linkedin-ghostwriting | Pass | Pass | Pass |
| copywriting-tone-of-voice-creator | Pass | Pass | Warn |
| deep-research | Pass | Pass | Warn |
| humaniseur-fr | Pass | Pass | Pass |
| copywriting-cta | Pass | Pass | Pass |
| technical-article-writer | Pass | Pass | Pass |
| site-launch-checklist | Warn | Warn | Warn |
| conventional-git | Pass | Pass | Pass |
| copywriting-prose-creator | Warn | Pass | Pass |
| influence-and-negotiation | Pass | Pass | Pass |
| chrome-extension | Pass | Warn | Pass |
| press-release-writer | Pass | Pass | Pass |
| substack-ghostwriting | Pass | Pass | Pass |
| promql-cli | Pass | Warn | Pass |
| snyk-agent-scan-compliance | Pass | Pass | Pass |
| crxjs | Pass | Pass | Pass |
| skill-progressive-disclosure-design | Pass | Pass | Pass |
| training-report | Pass | Pass | Pass |

This guide is Yellow because no sampled listing fails any scanner, but eight Warn cells span six skills: site-launch-checklist is warned by all three scanners, Socket warns on chrome-extension and promql-cli, Snyk warns on copywriting-tone-of-voice-creator and deep-research, and the Gen Agent Trust Hub warns on copywriting-prose-creator. The verdicts cover 20 of 21 listings; humanizer-en-asd-ste100 (3,579 installs) is not in the sampled set. The repository is almost entirely Markdown plus a handful of CI workflow files, so treat the Warn flags as prompt-injection or supply-chain signals worth reading on the skills.sh security pages before production use.

## Limitations

- Snapshot data, verified 2026-11-27: 115,208 combined installs across 21 indexed listings; 332 GitHub stars; MIT; last pushed 2026-11-01. Counts drift over time.
- Security verdicts cover 20 of 21 listings; humanizer-en-asd-ste100 has no sampled verdict, so its scanner status is unknown.
- The README warns that skills cross-reference each other and that installing only a subset gives a partial, inconsistent view of the guidelines.
- The skills are opinionated guidance, not a source of truth; site-launch-checklist is opinionated toward Cloudflare and Vercel, and the README says to override with a company skill where your team's conventions conflict.
- This is a separate repository from samber/golang-skills and samber/developer-platform-skills, so do not expect the Go or API and DX skills documented elsewhere in the catalog to live here.

## Related

- [Samber Go Skills - Golang Engineering Standards](/hermes/skills/catalog/samber-golang-skills-setup)
- [Samber Developer Platform Skills - API & DX Setup](/hermes/skills/catalog/samber-developer-platform-skills-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Treat the copywriting skills as a pipeline, not a menu: hooks, CTAs, tone of voice and prose reference each other, so installing one without the others loses the cross-references the README says matter.
- Load frontend-design-deslop before any UI task and let it produce a DESIGN.md token contract, then keep that contract across the project.
- When the user asks for a Chrome extension, route on the build tool: CRXJS/Vite with HMR means crxjs, everything else means chrome-extension.
- Keep the "reworked by a human" framing in mind when judging quality; the suite publishes its own eval numbers, so check the per-skill error-rate gap before trusting any one skill.
- Install the whole set on a fresh agent profile first, then prune, rather than installing one skill at a time against the cross-reference warnings.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
