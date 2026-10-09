---
title: "Modern Web Guidance - Google Chrome Agent Skill Setup"
description: "Setup guide for googlechrome/modern-web-guidance: official Google Chrome skills for modern web best practices and Chrome extension development."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/googlechrome-modern-web-guidance-setup/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skill setup", "google chrome", "web development", "frontend", "chrome extensions"]
---

# Modern Web Guidance - Setup Guide

**Source:** [googlechrome/modern-web-guidance](https://www.skills.sh/googlechrome/modern-web-guidance/modern-web-guidance) via skills.sh - 37,119 combined installs across 2 indexed listings (modern-web-guidance 28,432; chrome-extensions 8,687); first seen Oct 9, 2026 (morning sweep)
**GitHub:** [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) (2,455 stars, Apache-2.0 license; very active - pushed Oct 7, 2026; two skills under `skills/`: `modern-web-guidance` and `chrome-extensions`)
**Category:** Web Development / Browser Platform / Chrome Extensions
**Quality Tier:** 🟢 Production - official Google Chrome publisher (Chrome and Edge team supported), Apache-2.0, very active; Gen Agent Trust Hub Pass on both skills, Socket Warn on both, Snyk Warn + Pass - verified Oct 9, 2026

The official Modern Web Guidance skills from the Google Chrome team keep coding agents current on the web platform. The premise: coding agents default to legacy patterns because their training data is full of old code, so they generate bloated JavaScript for problems the platform now solves natively. These skills fix that at the source. A CLI searches and retrieves expert-curated, token-efficient guides - modern browser APIs, CSS layout and color, view transitions and scroll-driven animation, Core Web Vitals performance, accessibility, built-in AI APIs, and native UI components - and a second skill covers Chrome extension development end to end with Manifest V3 and Chrome Web Store publishing. The project is supported by the Google Chrome team, the Microsoft Edge team, and the web development community, and it is agent-neutral: it ships plugin manifests for Claude Code, Codex, Cursor, and Grok alongside the standard skills layout.

The `modern-web-guidance` skill is designed to run BEFORE implementation: its SKILL.md marks it mandatory for HTML/CSS and client-side JavaScript tasks, and deliberately does not trigger for backend, CI/CD, or generic scripting work. The agent searches with an action-oriented query, inspects the ranked matches (id, category, features used, token count, similarity score), retrieves the full guide, and implements from it.

---

## Installation

```bash
# Skills CLI - repo shorthand (two skills live in this repo)
npx skills add googlechrome/modern-web-guidance --skill modern-web-guidance
npx skills add googlechrome/modern-web-guidance --skill chrome-extensions

# Official installer wizard (repo quickstart)
npx modern-web-guidance@latest install
```

No install is needed to try the guide content: the CLI can search and retrieve guides directly (see Verification). The repository also ships plugin manifests for Claude Code, Codex CLI, Cursor, and Grok agents (`.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.grok-plugin/`).

## What It Provides

| Skill | What it does | Installs |
|---|---|---|
| modern-web-guidance | Search and retrieve curated guides for modern HTML/CSS/client-side JS: view transitions, scroll-driven animation, container queries, `:has()`, popovers and anchor positioning, `oklch` color, subgrid, LCP/INP performance, content-visibility, local filesystem and WebUSB APIs, plus framework adaptation (React, Vue, Angular) | 28,432 |
| chrome-extensions | Manifest V3 extension development end to end: service workers, content scripts, side panel, declarativeNetRequest, storage, messaging, omnibox, and Chrome Web Store publishing (review checklist, permission justifications, privacy policy, store listing) | 8,687 |

The guides are token-efficient by design - the Chrome team runs evals to prune content models already know - and cover the platform up to the cutting edge. Reference material ships in the repo under `skills/modern-web-guidance/guides/` (accessibility, built-in AI, CSS, performance, UX) and `skills/chrome-extensions/references/` (extensions + webstore).

## Why This Matters for Hermes Agents

Every agent that writes frontend code inherits stale habits from its training data: legacy polyfills, jQuery-era patterns, hand-rolled components that the platform now ships natively. This skill is the browser vendor's own counter-measure - the Chrome and Edge teams maintain the guidance, so the patterns reflect both build-time best practice and real-world browser compatibility data. Because it is a plain skill plus a CLI, a Hermes agent adds it the same way it adds any other skill, with no platform lock-in and no runtime service dependency beyond the package registry.

## Usage

| You say | What happens |
|---|---|
| "Build a modal with a smooth backdrop animation" | The skill searches, retrieves the top-layer/dialog animation guide, and the agent implements with native dialog + CSS instead of a legacy library |
| "Make the hero image load faster" | Fetch-priority and preload guidance for the LCP candidate image |
| "Add a swipeable carousel" | Scroll-driven animation and scroll-snap guidance |
| "Create a Chrome extension that saves tabs" | The chrome-extensions skill drives manifest V3, service worker, storage, and side panel |
| "Get my extension through Web Store review" | Review checklist, permission justifications, and privacy-policy references from `references/webstore/` |

The modern-web-guidance workflow is three steps: search with an action-oriented query, inspect the ranked results, then retrieve the full guide by id and implement.

## Verification

```bash
# Confirm the skills are installed
npx skills list | grep -E "modern-web-guidance|chrome-extensions"

# Smoke test the search CLI directly (works without installing)
npx -y modern-web-guidance@latest search "animate a dialog modal backdrop"
```

Working output is ranked JSON: each match carries an id, category, features used, token count, and similarity score. Retrieve a full guide by id, for example `npx -y modern-web-guidance@latest retrieve "animate-to-from-top-layer"`, and browse everything with `npx -y modern-web-guidance@latest list`.

## Security

skills.sh verdicts for both skills (verified Oct 9, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| modern-web-guidance | Pass | Warn | Warn |
| chrome-extensions | Pass | Warn | Pass |

Note: both skills drive a CLI that is fetched at runtime via `npx -y ...@latest` - normal supply-chain hygiene applies, and the CLI accepts `--skill-version` pins or a vendored copy if your environment requires reproducible installs. The repository itself is Apache-2.0 and maintained by the Google Chrome team.

## Limitations

- Preview release: the Chrome team states it is actively adding content (contributions via the `GoogleChrome/modern-web-guidance-src` repo).
- The guidance covers browser platform features as supported in Chrome and Edge; cross-browser support varies by feature and is part of the shipped compatibility data.
- These are guidance skills, not automation: the agent still authors the code; the skill steers it away from legacy patterns.
- Runtime fetch via npx; fully offline or air-gapped environments need a pinned or vendored copy.
- Snapshot data, verified Oct 9, 2026: 37,119 combined skills.sh installs; 2,455 GitHub stars; Apache-2.0; last pushed Oct 7, 2026. Counts drift over time.

## Related

- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup) - component-layer counterpart for React projects
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - interaction and motion craft for the UI layer
- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup) - accessibility auditing to pair with this skill's a11y guidance
- [web-quality-skills - Google-Grade Web Quality Audits](/hermes/skills/catalog/web-quality-skills-setup) - post-implementation quality audits
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Search with an action-oriented query ("animate a dialog modal backdrop"), not a keyword list - the search is semantic.
- Check `similarity` and `tokenCount` on each match before retrieving; low similarity means the query needs refining or the topic needs `list` browsing.
- Run the search BEFORE writing frontend code, not after - the whole point is preventing the legacy default.
- For extension work, start with the chrome-extensions skill from the first line of manifest work: most broken extensions fail on icons, side-panel triggers, and CSP-violating code execution, all covered in its mandatory rules.
- Pin `--skill-version` in regulated environments so the retrieved guidance is reproducible.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
