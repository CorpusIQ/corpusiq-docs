---
title: "New Skills - October 10, 2026"
description: "Skills.sh sweep (Oct 10): 894 skills checked; 17 new publisher guides (~1.2M combined) incl. Wondelai (275.9K), Starchild (179.7K), Cargo (142.8K)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct10-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 10, 2026 (Morning Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. This was the first fire of the v3 sweep plan: the 15 Hermes-focused queries plus a new five-query generic pass (agent skills, claude skills, design engineering skill, ui design skill, frontend skill), added after the Oct 9 probe showed the general publisher space is not served by Hermes-specific terms alone. The standard window plus the generic pass served 894 unique skills across 20 queries (0 failed), cross-referenced in a one-pass rg run (~21s) on the Mac Mini: 46 NEW, 313 PARTIAL.

The generic pass immediately paid off. The top of the Oct 9 probe queue converted to guides tonight (wondelai, starchild, cargo, samber, open-mercato, bencium, minimax, dimillian), and the morning's NEW set supplied the rest of a 17-guide batch: official and platform publishers (WordPress, Trigger.dev, LangSmith, MiniMax, Botpress), company-backed suites (Compound Engineering by Every Inc, Cargo, Open Mercato), and specialist collections (PM Skills, Dimillian, Xcode Build Optimization, Three.js Game Skills, Skills for Antigravity). Two source reconciles closed open flags (Composio successor repo; Mastra framework-repo skills), and one candidate was excluded on security verdicts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 894 (20 queries, 0 failed) |
| NEW (not in catalog) | 46 |
| PARTIAL (source known, skill not cataloged) | 313 |
| New publisher guides | 17 (~1.2M combined installs) |
| Source reconciles | 2 (Composio successor repo; Mastra framework-repo skills) |
| Excluded on security verdicts | 1 (zhaoxuya520/reverse-skill) |
| Queued for upcoming fires | 19 sources (~269K combined) |

## New Publisher Guides

### 1. Wondelai Skills - Book Framework Business & Design (275.9K)

**Source:** [wondelai/skills](https://www.skills.sh/wondelai/skills) (275.9K combined across 65 indexed listings; 2,372 stars, MIT; top: web-typography 8,475, refactoring-ui 8,194)

65 skills: 51 expert frameworks from bestselling business, design, and coding books plus 14 metaskills that orchestrate them, packaged as spec-conformant Agent Plugins and compatible with Claude, Codex, Cursor, OpenClaw, and Hermes Agent. All sampled verdicts Pass. Queue lead from the Oct 9 probe.

-> [Setup guide](/hermes/skills/catalog/wondelai-skills-setup)

### 2. Starchild Official Skills - Agent Platform Library (179.7K)

**Source:** [starchild-ai-agent/official-skills](https://www.skills.sh/starchild-ai-agent/official-skills) (179.7K combined across 96 indexed listings - API cap; top: coinglass 11,466, wallet 8,856, hyperliquid 8,634)

The Starchild platform's maintained skill library spanning data, trading, and automation. Low GitHub traction (27 stars) and mixed sampled verdicts are recorded in the guide.

-> [Setup guide](/hermes/skills/catalog/starchild-official-skills-setup)

### 3. Cargo Skills - GTM Engineering Suite (142.8K)

**Source:** [getcargohq/cargo-skills](https://www.skills.sh/getcargohq/cargo-skills) (142.8K combined across 28 indexed listings; MIT; pushed Oct 9, 2026; top: cargo-connection 8,747, cargo-gtm 8,560)

Nineteen GTM engineering skills that turn any skills.sh-compatible agent into a go-to-market workstation: lead lists, enrichment, email find/verify, CRM sync, orchestration, and workspace management.

-> [Setup guide](/hermes/skills/catalog/cargo-skills-setup)

### 4. Compound Engineering Plugin - Every Inc Workflow Suite (124.2K)

**Source:** [everyinc/compound-engineering-plugin](https://www.skills.sh/everyinc/compound-engineering-plugin) (124.2K combined across 96 indexed listings - API cap; 25,450 stars, MIT; pushed Oct 10, 2026; top: ce-brainstorm 3,794)

Every Inc's official plugin around a compound engineering loop: brainstorm, plan, work, simplify, review, compound. Runs on 14 agent hosts; /ce-setup configures a project and /lfg drives the pipeline hands-off. Mixed sampled verdicts (Pass/Warn).

-> [Setup guide](/hermes/skills/catalog/compound-engineering-plugin-setup)

### 5. Samber Developer Platform Skills - API & DX (95.1K)

**Source:** [samber/developer-platform-skills](https://www.skills.sh/samber/developer-platform-skills) (95.1K combined across 32 indexed listings; MIT; top: api-reference-quality 3,047, app-marketplace-review 3,037)

Skills for the developer-facing surface of a SaaS product: public APIs and their lifecycle, webhooks, SDKs, the developer portal, and the connector marketplace. Design and policy work, tool-agnostic. samber family extension - cross-linked to the documented samber-devrel and samber-golang guides.

-> [Setup guide](/hermes/skills/catalog/samber-developer-platform-skills-setup)

### 6. Open Mercato Skills - Enterprise ERP Engineering (79.0K)

**Source:** [open-mercato/skills](https://www.skills.sh/open-mercato/skills) (79.0K combined across 63 indexed listings; 231 stars, MIT; pushed Oct 5, 2026; top: om-apply-upgrade-notes 2,773)

63 enterprise ERP engineering skills: PR loop automation (om-auto-continue-pr, om-auto-create-pr), upgrade notes, module conventions, and onboarding. Snyk Warn on sampled skills is recorded in the guide.

-> [Setup guide](/hermes/skills/catalog/open-mercato-skills-setup)

### 7. Bencium Marketplace - Design & Product Skills (53.1K)

**Source:** [bencium/bencium-marketplace](https://www.skills.sh/bencium/bencium-marketplace) (53.1K combined across 17 indexed listings; 446 stars, MIT; top: bencium-innovative-ux-designer 6,918)

Seventeen design, UX, marketing, and productivity skills - including bencium-impact-designer, design-audit, bencium-aeo, eu-ai-act-reviewer, and typography. All sampled verdicts Pass.

-> [Setup guide](/hermes/skills/catalog/bencium-marketplace-setup)

### 8. MiniMax AI Skills - Official Dev & Document Suite (48.3K)

**Source:** [minimax-ai/skills](https://www.skills.sh/minimax-ai/skills) (48.3K combined across 24 indexed listings; 13,683 stars; top: pptx-generator 5,814)

The official MiniMax dev suite: frontend/fullstack/mobile scaffolds plus pptx-generator, minimax-docx, minimax-pdf, and minimax-xlsx document generators. README marks the project Beta; last pushed Apr 2026. Sibling of the documented minimax-h3 guide.

-> [Setup guide](/hermes/skills/catalog/minimax-ai-skills-setup)

### 9. PM Skills - Product Management Lifecycle Suite (44.7K)

**Source:** [product-on-purpose/pm-skills](https://www.skills.sh/product-on-purpose/pm-skills) (44.7K combined across 71 indexed listings; 716 stars, Apache-2.0; top: deliver-acceptance-criteria 1,002)

68 product management skills covering the complete lifecycle - acceptance criteria, PRDs, user stories, edge cases, competitive analysis - plus templates, workflows, and 200+ sample outputs. All sampled verdicts Pass.

-> [Setup guide](/hermes/skills/catalog/pm-skills-setup)

### 10. Dimillian Skills - Apple Platform Engineering (33.8K)

**Source:** [dimillian/skills](https://www.skills.sh/dimillian/skills) (33.8K combined across 18 indexed listings; 3,989 stars, MIT; top: swiftui-performance-audit 9,505)

SwiftUI and Apple platform engineering from Thomas Ricouard: swiftui-performance-audit, swiftui-liquid-glass, swiftui-ui-patterns, ios-debugger-agent, and more. Last pushed Mar 2026.

-> [Setup guide](/hermes/skills/catalog/dimillian-skills-setup)

### 11. Skills for Antigravity - Game & Research Collection (25.6K)

**Source:** [omer-metin/skills-for-antigravity](https://www.skills.sh/omer-metin/skills-for-antigravity) (25.6K combined across 96 indexed listings - API cap; Apache-2.0; top: game-ui-design 3,496)

A collection aimed at Google Antigravity workflows: game UI design, pixel-art sprites, quantitative research, technical analysis, and 3D modeling. Independent publisher - Community tier.

-> [Setup guide](/hermes/skills/catalog/skills-for-antigravity-setup)

### 12. Three.js Game Skills - 3D Game Development Suite (24.0K)

**Source:** [majidmanzarpour/threejs-game-skills](https://www.skills.sh/majidmanzarpour/threejs-game-skills) (24.0K combined across 9 indexed listings; 2,465 stars, MIT; top: threejs-3d-generator 2,970)

Nine Three.js skills covering 3D generation, gameplay systems, game UI, AAA-style graphics, and direction. All sampled verdicts Pass.

-> [Setup guide](/hermes/skills/catalog/threejs-game-skills-setup)

### 13. Xcode Build Optimization - iOS Build Performance (20.6K)

**Source:** [avdlee/xcode-build-optimization-agent-skill](https://www.skills.sh/avdlee/xcode-build-optimization-agent-skill) (20.6K combined across 6 indexed listings; 1,254 stars, MIT; top: xcode-build-fixer 3,563)

Six Xcode build diagnostics and optimization skills from Antoine van der Lee: xcode-build-fixer, xcode-build-orchestrator, xcode-project-analyzer, xcode-compilation-analyzer, and xcode-build-benchmark.

-> [Setup guide](/hermes/skills/catalog/xcode-build-optimization-setup)

### 14. WordPress Agent Skills - Official WP Development (17.7K)

**Source:** [wordpress/agent-skills](https://www.skills.sh/wordpress/agent-skills) (17.7K combined across 7 indexed listings; 2,217 stars; default branch `trunk`; top: wp-playground 4,251)

Official WordPress skills: wp-playground, blueprint, wp-plugin-directory-guidelines, and the wp-abilities audit/verify pair. GPL-family license (NOASSERTION on GitHub).

-> [Setup guide](/hermes/skills/catalog/wordpress-agent-skills-setup)

### 15. Trigger.dev Skills - Background Jobs & Realtime (14.6K)

**Source:** [triggerdotdev/skills](https://www.skills.sh/triggerdotdev/skills) (14.6K combined across 13 indexed listings; official Trigger.dev org; top: trigger-tasks 2,827)

Official Trigger.dev skills for background jobs and realtime work: trigger-tasks, trigger-setup, trigger-realtime, trigger-config, and trigger-agents. No LICENSE file in the repo - noted in the guide.

-> [Setup guide](/hermes/skills/catalog/trigger-dev-skills-setup)

### 16. LangSmith Skills - LLM Evaluation & Tracing (14.4K)

**Source:** [langchain-ai/langsmith-skills](https://www.skills.sh/langchain-ai/langsmith-skills) (14.4K combined across 5 indexed listings; 160 stars, MIT; top: langsmith-evaluator 4,764)

Official LangChain repo for LangSmith: evaluator, trace, dataset, custom-apps, and online-eval-engineering skills. Nonstandard layout (`config/skills/`) and Snyk Warn on two sampled skills are recorded. Sibling of the documented langchain-skills guide.

-> [Setup guide](/hermes/skills/catalog/langsmith-skills-setup)

### 17. Botpress Skills - Agent Development Kit (11.2K)

**Source:** [botpress/skills](https://www.skills.sh/botpress/skills) (11.2K combined across 7 indexed listings; 12 stars, MIT; top: adk 2,034)

Official Botpress ADK skills for building, debugging, and evaluating agents: adk, adk-frontend, adk-evals, adk-debugger, and adk-docs.

-> [Setup guide](/hermes/skills/catalog/botpress-skills-setup)

## Source Reconciles

- **Composio - Awesome Claude Skills:** the guide now carries a successor-repo note for [composio-community/awesome-claude-plugins](https://www.skills.sh/composio-community/awesome-claude-plugins) (16.6K combined across 23 indexed listings; 1,936 stars; overlapping skill set incl. canvas-design, mcp-builder, theme-factory, senior-frontend). skills.sh serves both sources.
  -> [Updated guide](/hermes/skills/catalog/composiohq-awesome-claude-skills-setup)
- **Mastra AI Skills:** the guide now carries an additional-source note for the framework repository [mastra-ai/mastra](https://github.com/mastra-ai/mastra), which ships agent skills under `.claude/skills/` (30 indexed listings, ~12,987 combined; top: react-best-practices 2,810). Distinct from the mastra-ai/skills suite.
  -> [Updated guide](/hermes/skills/catalog/mastra-ai-skills-setup)

## Excluded - Security Verdicts

| Source | Combined | Note |
|---|---|---|
| zhaoxuya520/reverse-skill | 47,544 | Excluded: Gen Agent Trust Hub Fail + Socket Fail on sampled skills (reverse-engineering, pentest-tools) - recorded for transparency, no guide |

## Queued for Upcoming Fires

Exact-source sizes; above the guide floor, no catalog coverage yet. The queue drains fastest by combined installs:

| Source | Listings | Combined | Note |
|---|---|---|---|
| sanyuan0704/sanyuan-skills | 6 | 29,906 | Code review expertise suite (Oct 9 queue) |
| ghostsecurity/skills | 8 | 27,900 | AppSec skills from Ghost Security (Oct 9 queue) |
| curiositech/some_claude_skills | 96 | 27,047 | Video processing/editing, design, and dev utilities collection |
| am-will/codex-skills | 19 | 20,182 | Codex-oriented dev skills (frontend design, context7, planner) |
| benjitaylor/agentation | 2 | 20,140 | Visual feedback tooling for agents (Oct 9 queue) |
| jamditis/claude-skills-journalism | 67 | 18,908 | Journalism, media, and academia collection (Oct 9 queue) |
| buildgreatproducts/builder-os | 10 | 15,706 | Product/design workflow suite (design-system, product-planner) |
| ehmo/platform-design-skills | 8 | 12,727 | 450+ platform design rules (Oct 9 queue) |
| tencentcloudbase/cloudbase-skills | 33 | 12,468 | Official Tencent CloudBase full-stack skills (Oct 9 queue) |
| ulpi-io/skills | 60 | 10,681 | Frontend design and Laravel toolkit |
| srinitude/skills | 23 | 10,585 | Design system extraction and dev utilities |
| rmyndharis/antigravity-skills | 96 | 10,068 | Antigravity skill pack (unity-developer lead) |
| deeflect/mies | 1 | 8,705 | Design-taste skill (Oct 9 queue) |
| vibe-motion/skills | 16 | 8,263 | Motion and SVG animation skills |
| vapiai/skills | 16 | 7,975 | Assistant/squad creation skills |
| sergiodxa/agent-skills | 11 | 7,886 | Frontend testing and React best practices |
| appllama/appllama-skills | 3 | 7,566 | Mobile app design patterns (Oct 9 queue) |
| magicpathai/agent-skills | 1 | 6,303 | MagicPath design skills (Oct 9 queue) |
| evoscientist/evoskills | 18 | 5,592 | Scientific research skills |

The remainder of today's NEW set (below 5K combined) and the probe tail stay in the sweep working set for triage.

## Notes

- **First fire of the v3 plan:** 15 Hermes-focused + 5 generic queries; the generic pass surfaced the general publisher space (compound-engineering, wordpress, trigger.dev, langsmith, mastra, and more) that the Hermes-focused window structurally missed.
- **Queue mechanics working as designed:** the top 8 sources of the Oct 9 probe queue converted tonight; the queue refilled from today's NEW set (19 sources, ~269K).
- **Sizing discipline:** every number on this page and in the guides is an exact-source API sum; trending-window and probe figures undercount clusters by 10-250x.
- **Duplicate defense:** no Oct 10 skills-sweep commit existed at the remote tip (399f6c8d4); single scheduled fire for the 1100z slot.
- **Mechanics:** one-pass rg crossref on the Mac Mini; 0 failed queries; all guides and this page drafted against Oct 10, 2026 snapshots.

---

*Sweep run: Oct 10, 2026, skills-monitor cron (morning, 0400 MST). Includes the 17 publisher setup guides listed above, the Composio and Mastra source reconciles, and the refreshed queue.*
