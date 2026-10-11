---
title: "New Skills - October 10, 2026 (Evening)"
description: "Skills.sh sweep (Oct 10 evening): 893 skills checked; 24 new publisher guides (~453K combined) incl. Delegate Skills (65.9K); queue drained."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct10-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 10, 2026 (Evening Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The v3 window (15 Hermes-focused queries plus the 5-query generic pass) served 893 unique skills, cross-referenced in a one-pass rg run on the Mac Mini (~39s): 24 NEW, 306 PARTIAL. Tonight's fire drained the entire 19-source queue left by the morning sweep and ran a full zero-catalog audit over every PARTIAL source at 100+ installs (61 sources).

The queue drain converted all 19 queued publishers, and the audit added the night's largest find: [amElnagdy/delegate-skills](https://www.skills.sh/amElnagdy/delegate-skills) at 65.9K combined installs - a single agy-delegate row had been skipped in August and the family was never sized until now. The audit also converted langgenius/dify, sentimony/skills, and mastepanoski/claude-skills; resolved one coverage false positive (a case-sensitivity artifact on the mukul975 guide, now carrying a roster snapshot note); and recorded one skip (a deleted source repository, below). The sweep's own NEW set contributed fresh findings including [freshtechbro/claudedesignskills](https://www.skills.sh/freshtechbro/claudedesignskills) (60.8K).

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 893 (20 queries: 15 Hermes-focused + 5 generic) |
| NEW (not in catalog) | 24 |
| PARTIAL (source known, skill not cataloged) | 306 |
| New publisher guides | 24 (~453K combined installs) |
| Queue status | Fully drained: 19/19 sources converted |
| Zero-catalog audit | 61 PARTIAL sources at 100+ checked; 4 converts + 1 re-qualification + 1 false positive resolved + 1 skip |
| Roster reconciles | 1 (mukul975 roster snapshot note) |

## New Publisher Guides

### 1. Delegate Skills - CLI Agent Fleet Orchestration (65.9K)

**Source:** [amElnagdy/delegate-skills](https://www.skills.sh/amElnagdy/delegate-skills) (65.9K combined installs)

Fleet-of-lanes orchestration: discover installed implementer CLIs, group them into lanes (feature, tests, ui), delegate per lane or per implementer, review the diff, land the commit. 18 implementer skills spanning Codex, Claude, OpenCode, Cursor, Gemini CLI family, Kimi, Grok, Copilot, Aider, and more; MIT, 2,355 stars, relay-smoke CI. Zero-catalog audit re-qualification: a single agy-delegate row was skipped in August as Antigravity-specific and the family was never sized - at 65.9K combined it is one of the largest converts of the week. Documented under its own filename (amelnagdy-delegate-skills-setup) to stay distinct from an earlier June 2026 guide for a different project of the same name (bassemZohdy/delegate-skills); the two guides cross-link.

-> [Setup guide](/hermes/skills/catalog/amelnagdy-delegate-skills-setup)

### 2. Claude Design Skillstack - 3D, WebGL & Animation (60.8K)

**Source:** [freshtechbro/claudedesignskills](https://www.skills.sh/freshtechbro/claudedesignskills) (60.8K combined installs)

Professional design-agency skillstack for 3D/WebGL and animation: Three.js, React Three Fiber, Babylon.js, PixiJS, A-Frame, PlayCanvas, plus Framer Motion, GSAP ScrollTrigger, Anime.js, Lottie, Rive, React Spring, and scroll systems (Locomotive, Barba). 23 indexed listings, all above 1,993 installs; MIT; smallest finding here is the top of most other publishers.

-> [Setup guide](/hermes/skills/catalog/claudedesignskills-setup)

### 3. Sanyuan Skills - Production Agent Skills (30.0K)

**Source:** [sanyuan0704/sanyuan-skills](https://www.skills.sh/sanyuan0704/sanyuan-skills) (30.0K combined installs)

Six production-grade skills from Sanyuan: code-review-expert (13,310 installs - senior review across SOLID, security, performance, error handling), sigma (Bloom two-sigma AI tutor), skill-forge (12-technique skill creation), skill-review (skill quality audit), book-study, and wiki-ingest. MIT, 3,939 stars.

-> [Setup guide](/hermes/skills/catalog/sanyuan-skills-setup)

### 4. Sentimony Skills - Dev Workflow & Review Gates (28.3K)

**Source:** [sentimony/skills](https://www.skills.sh/sentimony/skills) (28.3K combined installs)

Twenty-five dev-workflow skills in a plugin layout: TypeScript, web-debug, vitest, echarts, plan-crafting, scope-triage, dashfix, negafix, commit-all, maintaining-agent-context, plus a review-gate cluster (tdd, parallel-agents, subagent-plan-dev, git-worktree-isolation, verification-gate). Developer-discipline flavor: scope checks and review loops.

-> [Setup guide](/hermes/skills/catalog/sentimony-skills-setup)

### 5. Ghost Security Skills - AppSec Agent Plugins (28.0K)

**Source:** [ghostsecurity/skills](https://www.skills.sh/ghostsecurity/skills) (28.0K combined installs)

Company-backed AppSec suite (Ghost Security): secret scanning (Poltergeist), dependency scanning (Wraith, OSV-powered), code scanning, an MITM proxy, validation, and reporting - all inside the agent workflow via two Claude Code plugins (ghost + exo). Apache-2.0, active September 2026.

-> [Setup guide](/hermes/skills/catalog/ghostsecurity-skills-setup)

### 6. Some Claude Skills - 180+ Skill Collection (27.1K)

**Source:** [curiositech/some_claude_skills](https://www.skills.sh/curiositech/some_claude_skills) (27.1K combined installs)

A 180+ skill collection from Erich Owens (ex-Meta ML engineer): video processing/editing, interior design, CV creation, personal finance, photo composition, PWA, metal shaders, and a long utility tail. Ships two MCP servers (prompt-learning, cv-creator). GitHub redirects the README alias (erichowens) to the canonical curiositech repo.

-> [Setup guide](/hermes/skills/catalog/some-claude-skills-setup)

### 7. Dify Skills - Official Dev Workflows (22.6K)

**Source:** [langgenius/dify](https://www.skills.sh/langgenius/dify) (22.6K combined installs)

Official skills from the Dify repository (158,105 stars): frontend-code-review (9,983), frontend-testing, component-refactoring, backend-code-review, and related workflow skills under .agents/skills/ (with .claude/skills/ symlinks). For teams building on or extending Dify.

-> [Setup guide](/hermes/skills/catalog/dify-skills-setup)

### 8. CodexSkills - Agent Orchestration (20.2K)

**Source:** [am-will/codex-skills](https://www.skills.sh/am-will/codex-skills) (20.2K combined installs)

Nineteen Codex-oriented skills usable from any agent: planners (planner, plan-harder, swarm-planner), parallel task execution, multi-agent llm-council with a monitoring UI, documentation access (Context7, OpenAI docs, read-github), and frontend design. No LICENSE file - noted in the guide.

-> [Setup guide](/hermes/skills/catalog/am-will-codex-skills-setup)

### 9. Agentation - Visual Feedback for Agents (20.2K)

**Source:** [benjitaylor/agentation](https://www.skills.sh/benjitaylor/agentation) (20.2K combined installs)

Click-to-annotate visual feedback for coding agents: click elements on your page, add notes, copy structured output that points the agent at the exact code. React drop-in plus an optional MCP server for direct sync (localhost:4747). 4,917 stars; the top two listings carry 13,353 and 6,810 installs.

-> [Setup guide](/hermes/skills/catalog/agentation-setup)

### 10. Journalism Agent Skills - Media & Research Workflows (18.9K)

**Source:** [jamditis/claude-skills-journalism](https://www.skills.sh/jamditis/claude-skills-journalism) (18.9K combined installs)

Sixty-seven indexed skills for journalists and researchers: web scraping, academic writing, page monitoring, fact-check workflows, FOIA requests, source verification, newsroom style, editorial workflow, crisis communications, and data journalism. Docs site at skills.amditis.tech.

-> [Setup guide](/hermes/skills/catalog/claude-skills-journalism-setup)

### 11. BuilderOS - Product Builder Workflow Suites (15.7K)

**Source:** [buildgreatproducts/builder-os](https://www.skills.sh/buildgreatproducts/builder-os) (15.7K combined installs)

The successor to PLAID: a repeatable system from idea to launch - idea generator/validator, product planner, design system, design-better, build loops for Claude Code/Codex/Cursor, build-mvp, and a launch checklist. All 10 listings above 1,000 installs; skills chain through docs/ documents.

-> [Setup guide](/hermes/skills/catalog/builder-os-setup)

### 12. Platform Design Skills - HIG, Material & WCAG Rules (12.8K)

**Source:** [ehmo/platform-design-skills](https://www.skills.sh/ehmo/platform-design-skills) (12.8K combined installs)

450+ platform design rules scraped and distilled from the Apple Human Interface Guidelines, Material Design 3, and WCAG 2.2: one exhaustive skill per platform (macOS, iOS, iPadOS, watchOS, visionOS, tvOS, Android, web). All 8 listings above 850 installs.

-> [Setup guide](/hermes/skills/catalog/platform-design-skills-setup)

### 13. CloudBase Skills - Official Tencent Full-Stack (12.5K)

**Source:** [tencentcloudbase/cloudbase-skills](https://www.skills.sh/tencentcloudbase/cloudbase-skills) (12.5K combined installs)

Official Tencent CloudBase skills for web, mini program, and native app development: platform detection, auth flows, NoSQL/MySQL, cloud functions, storage, and AI integration. Backed by CloudBase MCP. One dominant listing (12,195 installs) plus a fresh tiny tail.

-> [Setup guide](/hermes/skills/catalog/cloudbase-skills-setup)

### 14. ulpi Skills - Browse, SEO & Dev Utilities (10.7K)

**Source:** [ulpi-io/skills](https://www.skills.sh/ulpi-io/skills) (10.7K combined installs)

Sixty skills including a notable browse-* family: browse (headless browser CLI, 76+ commands), browse-stealth (camoufox), browse-seo, browse-aeo, browse-geo (GEO monitoring), browse-qa, plus codemap, plan-to-task DAGs, Laravel tooling, and dev utilities. No LICENSE file - noted in the guide.

-> [Setup guide](/hermes/skills/catalog/ulpi-io-skills-setup)

### 15. Srinitude Skills - Portable Skills + Local MCP (10.6K)

**Source:** [srinitude/skills](https://www.skills.sh/srinitude/skills) (10.6K combined installs)

An Agent Plugins v1.0.0 package: 23 portable skills with validation suites (trigger, behavior, failure, recovery evaluations) and a bundled read-only local MCP server. Focus on skill engineering and discipline: starting-point, skill-factory, simplify-skill, outcome-bounded-work, logic-audit, dedupe.

-> [Setup guide](/hermes/skills/catalog/srinitude-skills-setup)

### 16. Antigravity Skill Vault - 300+ Ported Skills (10.1K)

**Source:** [rmyndharis/antigravity-skills](https://www.skills.sh/rmyndharis/antigravity-skills) (10.1K combined installs)

A curated 300+ skill collection for Google Antigravity, ported from the wshobson/agents ecosystem: specialist personas (backend-architect, database-architect, ui-ux-designer) and domain packs across languages, ops, security, and business. Distinct from the omer-metin collection - both are cross-linked.

-> [Setup guide](/hermes/skills/catalog/antigravity-skill-vault-setup)

### 17. Mies - Design Taste Skill (8.8K)

**Source:** [deeflect/mies](https://www.skills.sh/deeflect/mies) (8.8K combined installs)

A single design-taste skill that removes what an interface does not need, then perfects what is left: proportion, spacing, alignment, type, color, state, motion, and copy. Modes Frame, Set, Compose; run with /mies in Claude Code. 8,774 installs on one listing.

-> [Setup guide](/hermes/skills/catalog/mies-setup)

### 18. Vibe Motion Skills - SVG & Motion Renders (8.3K)

**Source:** [vibe-motion/skills](https://www.skills.sh/vibe-motion/skills) (8.3K combined installs)

Sixteen motion and animation skills: SVG assembly, Remotion renders (3D tickers, candlesticks, vinyl players), procedural fish, light spotlights, pixel2motion logo animation, brand launch videos, and a Disney animation-rule skill. README marks the project no longer maintained - carried prominently in the guide.

-> [Setup guide](/hermes/skills/catalog/vibe-motion-skills-setup)

### 19. Vapi Skills - Voice AI Agent Building (8.0K)

**Source:** [vapiai/skills](https://www.skills.sh/vapiai/skills) (8.0K combined installs)

Official Vapi skills for voice AI agents: create assistants, calls, tools, squads, workflows, phone numbers, webhooks, and API key setup - plus a Codex plugin build path. No LICENSE file - noted in the guide.

-> [Setup guide](/hermes/skills/catalog/vapi-skills-setup)

### 20. Sergiodxa Agent Skills - Frontend Practice Suite (7.9K)

**Source:** [sergiodxa/agent-skills](https://www.skills.sh/sergiodxa/agent-skills) (7.9K combined installs)

Eleven frontend best-practices skills from Sergio Xalambri: testing, OWASP security checks, React, accessibility, Tailwind, React Router, async patterns, i18n, Ruby on Rails, and skill-writing. Tight, high-signal practice guides for frontend work.

-> [Setup guide](/hermes/skills/catalog/sergiodxa-agent-skills-setup)

### 21. Appllama Skills - Mobile App Design Patterns (7.6K)

**Source:** [appllama/appllama-skills](https://www.skills.sh/appllama/appllama-skills) (7.6K combined installs)

Skills from Appllama - the design library of top-grossing mobile apps with revenue context: study winning screens, extract the category design language, and build native-quality screens to a simulator-verified bar. MIT, 2,537 stars; appllama.io/mcp companion.

-> [Setup guide](/hermes/skills/catalog/appllama-skills-setup)

### 22. Mastepanoski Skills - UX & AI Compliance Audits (6.3K)

**Source:** [mastepanoski/claude-skills](https://www.skills.sh/mastepanoski/claude-skills) (6.3K combined installs)

Professional UX/UI evaluation and AI governance skills: WCAG accessibility audits, UI design review, UX audit rethinks, Nielsen heuristics, cognitive walkthroughs, Don Norman principles, OWASP LLM Top 10, ISO 42001, NIST AI RMF, and GDPR audits. Audit-style skills with methodology grounding.

-> [Setup guide](/hermes/skills/catalog/mastepanoski-skills-setup)

### 23. MagicPath Agent Skills - UI Component Workflow (6.3K)

**Source:** [magicpathai/agent-skills](https://www.skills.sh/magicpathai/agent-skills) (6.3K combined installs)

Official MagicPath skill teaching agents to search, preview, inspect, install, export, create, and edit MagicPath UI components via the magicpath-ai CLI - with a focus on preserving 1:1 fidelity when moving designs into local code. Install for Cursor, Claude Code, Codex, or via npx skills.

-> [Setup guide](/hermes/skills/catalog/magicpath-agent-skills-setup)

### 24. EvoSkills - Scientific Research Packs (5.6K)

**Source:** [evoscientist/evoskills](https://www.skills.sh/evoscientist/evoskills) (5.6K combined installs)

The official skill repository for EvoScientist: research-ideation, paper-planning, paper-writing, paper-review, paper-rebuttal, academic-slides, experiment pipelines, and persistent research memory. Purpose-built for EvoScientist, compatible with any coding agent.

-> [Setup guide](/hermes/skills/catalog/evoskills-setup)

## Zero-Catalog Audit - Findings

- **Re-qualified: amElnagdy/delegate-skills (65.9K)** - a single row (agy-delegate) was skipped in August as Antigravity-specific and the family was never sized; the audit's publisher follow-up surfaced 18 listings and one of the night's largest clusters. Guide above. The filename collided with an existing guide for a same-named, different project (bassemZohdy/delegate-skills, June 2026), so the new guide ships as `amelnagdy-delegate-skills-setup` with reciprocal cross-links.
- **Converted: langgenius/dify (22.6K), sentimony/skills (28.3K), mastepanoski/claude-skills (6.3K)** - all three were single-row or batch-page-only references with no dedicated guide; each sized well above the floor. Guides above.
- **False positive resolved: mukul975/anthropic-cybersecurity-skills** - coverage checks missed it on a case difference (skills.sh indexes lowercase; the guide links the repo's own capitalization). The existing guide now carries a roster snapshot note (94 listings / 38,503 combined).
- **Skipped: 404kidwiz/claude-supercode-skills (20,036 across 96 listings)** - the source repository is no longer resolvable on GitHub (API metadata and raw probes return 404; not present in the owner's repository list). Recorded for re-verification; a deleted source cannot back a working install command.
- The remaining 16 zero-catalog sources from the audit are tonight's converts listed above.

## Queue - Fully Drained

No above-floor sources remain queued from the prior fire. The below-floor working set carries the evening's remaining NEW finds for triage (top: melodic-software/claude-code-plugins 4,042 across 96 listings; manager-dot-dev/manager-skills 3,496; gogf/skills 3,186 - official GoFrame org; zzci/skills 3,141; cuellarfr/design-skills 2,931; nodeops-app/skills 2,684; chadboyda/agent-gtm-skills 2,562; kv0906/cc-skills 2,013; heyeddi-com/heyeddi-skills 1,879).

## Roster Reconciles

- **Anthropic Cybersecurity Skills (mukul975 family):** roster snapshot note added - skills.sh serves 94 indexed listings / 38,503 combined installs; the source string is indexed lowercase (`mukul975/anthropic-cybersecurity-skills`) while the guide links the repo's own capitalization.
  -> [Updated guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup)
- **Delegate Skills (name collision):** the new amElnagdy guide and the June 2026 bassemZohdy guide now cross-link, so the two same-named projects stay distinguishable in future sweeps.
  -> [New guide](/hermes/skills/catalog/amelnagdy-delegate-skills-setup) | [Existing guide](/hermes/skills/catalog/delegate-skills-setup)

## Notes

- **Queue mechanics:** the morning fire re-queued 19 sources; this fire converted all 19 (plus the audit finds). The queue drains fastest by combined installs and is now empty above the floor.
- **Sizing discipline:** every number on this page and in the guides is an exact-source API sum, re-dumped at this fire (not trending-window or probe figures).
- **New failure classes recorded:** (a) a source repository deleted after indexing (404kidwiz) - first observed; (b) a case-sensitivity coverage false positive (mukul975) - now handled by the snapshot note; (c) an index-vs-tree drift case where the top indexed listing was removed from the repo (vibe-motion, carried in its guide).
- **Duplicate defense:** no Oct 10 evening skills-sweep commit existed at the remote tip (2f1c397e6); single scheduled fire for the 0500z slot.
- **Mechanics:** one-pass rg crossref on the Mac Mini; all guides and this page drafted against Oct 10, 2026 evening snapshots.

---

*Sweep run: Oct 10, 2026, skills-monitor cron (evening). Includes the 24 publisher setup guides listed above, the 19-source queue drain, the zero-catalog audit converts, and the mukul975 roster snapshot note.*
