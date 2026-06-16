---
title: Skills Catalog
description: Complete index of all 380+ skills available to Hermes agents — 90 native CorpusIQ skills and 290+ marketplace skills from skills.sh. Single source of truth, updated continuously.
---

# Skills Catalog

Complete index of every skill available to CorpusIQ Hermes agents. **380+ total: 90 native + 290+ marketplace.** Updated as skills are added and discovered.

Skills are reusable agent capabilities — step-by-step workflows with tools, triggers, and verification. Not static prompts. Not text files. Executable runbooks that agents read and execute. When you run an SEO audit, the agent follows the `seo-audit` skill's instructions, step by step, verifying each result before proceeding.

## How to Use This Catalog

1. **Find a skill** — Browse by category below, or use your browser's find (Ctrl+F / Cmd+F) to search by keyword.
2. **Check the category description** — Each category explains what that group of skills covers and how they relate.
3. **Install marketplace skills** — Native skills load automatically. Marketplace skills need `npx skills add <owner/repo@skill>`.
4. **Invoke** — Mention the trigger keywords in your Hermes session, or call the skill explicitly.

---

## Native CorpusIQ Skills (90)

Built and maintained for the CorpusIQ Hermes deployment. These load automatically when your agent profile matches — no installation required. Organized by functional domain.

### Growth & Engagement (13)

Community growth, social media automation, and content distribution. These skills handle the public-facing presence of your Hermes agents across platforms.

| Skill | What It Does |
|-------|-------------|
| `help-first-community-engagement` | Answer real questions on Reddit, HN, Discord before mentioning your product |
| `cross-platform-commenting-engine` | Deploy autonomous comment engines across YouTube, Reddit, X |
| `github-growth-contributions` | Submit meaningful PRs to high-star repos for visibility |
| `corpusiq-mcp-directory-maintenance` | Maintain listings across MCP server directories |
| `playwright-social-media-automation` | Automate social media posting and comment monitoring |
| `postiz-cli-social-deployment` | Deploy content across X, Reddit, Instagram, LinkedIn via Postiz CLI |
| `daily-rotating-content-automation` | Multi-avatar, multi-connector daily content rotation |
| `corpusiq-daily-ugc-video-series` | 5 rotating video formats (technical, operator, growth, tool, comparison) |
| `corpusiq-go-to-market-strategy` | Complete GTM planning and execution |
| `corpusiq-content-analysis-rules` | Rules for TikTok/YouTube video content analysis |
| `corpusiq-video-knowledge-extraction` | Extract insights from TikTok/YouTube AI videos |
| `corpusiq-video-transcript-analysis` | Synthesize learnings from video transcripts |
| `corpusiq-docs-management` | Manage docs repo, write/update/publish, skills.sh marketplace |

### Research & Intelligence (6)

Market research, competitive analysis, and autonomous intelligence gathering. These skills feed the decision-making pipeline with structured research outputs.

| Skill | What It Does |
|-------|-------------|
| `corpusiq-research-intelligence-framework` | Shared framework for all research intelligence collection |
| `corpusiq-autonomous-growth-intelligence` | Proactive gap-spotting, architectural decisions, improvement detection |
| `corpusiq-autonomous-improvement-recommendations` | Pattern for identifying system gaps and proposing fixes |
| `prospect-research-personalization` | Research prospect's business before crafting response |
| `multi-tier-partnership-qualification` | Evaluate multiple partnership opportunities simultaneously |
| `inbound-lead-analysis-domain-first` | Analyze inbound leads by email domain — business domain determines priority |

### Lead Response & Nurture (11)

End-to-end lead management: capture, classify, research, personalize, respond, and nurture. The conversion pipeline for inbound interest.

| Skill | What It Does |
|-------|-------------|
| `corpusiq-inbound-lead-response-system` | Complete pipeline: capture → qualify → respond |
| `corpusiq-autonomous-lead-capture` | Recurring email monitoring to identify and track leads |
| `corpusiq-lead-nurture-sequences` | Automated nurture sequences for qualified leads |
| `lead-response-execution` | Execute immediate responses to inbound customer inquiries |
| `inbound-response-personalization` | Deep business research + personalized response per lead |
| `professional-custom-email-templates` | Professional HTML email templates for inbound responses |
| `corpusiq-email-response-standards` | Professional email standards for all outbound communication |
| `corpusiq-email-phone-number-hard-rule` | Enforce phone number handling in ALL communications |
| `corpusiq-inbound-communication-monitoring` | Monitor + respond to inbound across email/messaging channels |
| `company-name-verification-hardcoded` | Mandatory company name verification before outbound |
| `autonomous-communication-priority` | Channel monitoring SLA hierarchy (WhatsApp > Telegram > Email) |

### Email Operations (7)

Production email infrastructure: multi-account monitoring, OAuth management, template enforcement, and delivery verification.

| Skill | What It Does |
|-------|-------------|
| `corpusiq-dual-email-account-control` | Unified master monitor for multiple email inboxes |
| `corpusiq-dual-account-oauth-automation` | Persistent OAuth token management for multiple Gmail accounts |
| `corpusiq-email-account-setup` | Gmail account configuration and management |
| `corpusiq-email-operating-rules` | Authoritative email operating policy |
| `corpusiq-email-send-checklist` | Hard pre-send gate for every outbound email |
| `dual-email-account-management` | Consolidated system for two email accounts |
| `headless-oauth-automation` | Localhost callback servers for Google OAuth |

### Video Production (6)

AI-powered video generation and distribution. These skills handle the full pipeline from script to published video across platforms.

| Skill | What It Does |
|-------|-------------|
| `corpusiq-heygen-video-automation` | End-to-end HeyGen video generation + multi-platform posting |
| `corpusiq-heygen-video-generation-workflow` | HeyGen video generation for UGC series |
| `corpusiq-heygen-video-pipeline` | End-to-end UGC video pipeline using HeyGen video-agent |
| `corpusiq-video-production` | End-to-end UGC video production via HeyGen |
| `heygen-skills-install` | First-time HeyGen setup for Hermes agents |
| `video-voiceover-production` | Voiceover narration and captions for screen recordings |

### Social Media Automation (4)

Cross-platform social media management at scale.

| Skill | What It Does |
|-------|-------------|
| `instagram-tiktok-heygen-video-automation` | Automated video generation + posting to Instagram/TikTok |
| `instagram-tiktok-video-posting-automation` | Instagram + TikTok video posting via Postiz CLI |
| `rate-limit-pivot-execution` | Detect API rate limits, pivot to alternative platforms |
| `corpusiq-social-cadence-engine` | All-platform posting schedule: X, Reddit, TikTok, IG, YT, Discord, GH, HN, LinkedIn |

### LinkedIn Integration (3)

LinkedIn API for market intelligence and content distribution.

| Skill | What It Does |
|-------|-------------|
| `linkedin-api-integration` | LinkedIn API for reading posts, analyzing market signals |
| `linkedin-api-token-and-feed-integration` | Authentication, token lifecycle, feed reading |
| `linkedin-api-authentication-troubleshooting` | Auth patterns, token validation, error resolution |

### Reddit Automation (2)

Reddit API automation for community engagement.

| Skill | What It Does |
|-------|-------------|
| `reddit-oauth-praw-automation` | End-to-end Reddit API automation via OAuth credentials |
| `reddit-praw-automation` | Reddit automation via PRAW (Python Reddit API Wrapper) |

### Session & Execution (6)

Agent session management and execution discipline. These skills govern how the agent operates, not what it does.

| Skill | What It Does |
|-------|-------------|
| `corpusiq-session-start` | Mandatory session start ritual — check email before anything |
| `corpusiq-autonomous-growth-agent` | Constraints, preferences, and autonomous execution workflows |
| `corpusiq-done-only-reporting` | Never report scheduled/queued/planned — only completed work |
| `execution-first-communication` | Minimize explanation, maximize action |
| `corpusiq-execution-discipline` | Hard rules to prevent analysis inflation |
| `corpusiq-session-handoff` | Write session context for cross-session continuity |

### System Governance (8)

Rules, audits, and enforcement mechanisms that keep the agent ecosystem healthy.

| Skill | What It Does |
|-------|-------------|
| `corpusiq-system-governance` | Governance baseline: seven rules, session, email, cron, monitoring |
| `corpusiq-system-audit` | Six-category audit to find and fix degradation before it breaks |
| `corpusiq-cron-delivery-audit` | Audit all crons — verify user-facing ones actually deliver |
| `corpusiq-session-db-optimization` | Three-phase session DB optimization to slash context window |
| `corpusiq-tool-exclusivity-doctrine` | Enforce "use X only" exclusive tool policies |
| `autonomous-system-discovery-audit` | Comprehensive environment audit for installed tools |
| `system-audit-before-automation` | System inspection and config discovery before automation |
| `openclaw-system-inspection` | Discover what's actually configured on OpenClaw |

### Infrastructure (5)

Hardware, model routing, and deployment infrastructure.

| Skill | What It Does |
|-------|-------------|
| `corpusiq-mac-mini-worker` | Worker node setup: SSH, crontab, Playwright, Hermes |
| `corpusiq-local-ai-infrastructure` | Architecture, model selection, setup for local AI |
| `corpusiq-llm-cost-and-model-routing` | Cost analysis, benchmarking, multi-model routing |
| `corpusiq-llm-routing-and-model-selection` | Model selection strategy |
| `corpusiq-model-router` | Qwen-first routing with DeepSeek escalation |

### Browser & Web (3)

Browser automation and web extraction infrastructure.

| Skill | What It Does |
|-------|-------------|
| `browser-web-extraction-setup` | Configure Hermes browser and web extraction backends |
| `mac-mini-worker` | Worker node — SSH, Hermes, OpenClaw, FFmpeg |
| `corpusiq-mcp-oauth-auth` | Authenticate Hermes agents to the CorpusIQ MCP server |

### Core Knowledge (4)

Foundational knowledge every agent must have.

| Skill | What It Does |
|-------|-------------|
| `corpusiq-fundamentals` | Complete product knowledge, core thesis, positioning |
| `corpusiq-guardrails` | Hard guardrails enforced before any external action |
| `corpusiq-daily-html-reporting` | Automated daily HTML report |
| `automated-email-report-format` | HTML assessment reports with standardized formatting |

### Engineering (8) — Platform Construction

Skills for building and maintaining the platform itself. See the [Engineering Skills page](/hermes/skills/engineering/) for detailed descriptions.

| Skill | What It Does |
|-------|-------------|
| `consultant-connector-audit` | 13-section audit pass for non-core-authored connectors |
| `mcp-architecture` | Field guide for 50k+ LOC MCP server |
| `metric-spec-registry` | Canonical KPI definitions, live resolution, drift detection |
| `api-development` | Cloud Run + FastAPI patterns from production audits |
| `frontend-development` | Next.js + Vercel patterns for marketing + dashboard |
| `scheduled-jobs` | Hermes cron operating manual |
| `honcho-memory-usage` | Server-side semantic memory via Honcho MCP |
| `subagent-resilience` | Checkpoint-based resilience for subagents |

### DevOps & Kanban (1)

| Skill | What It Does |
|-------|-------------|
| `kanban-worker` | Pitfalls, examples, edge cases for Hermes Kanban workers |

### GBrain Operations (1)

| Skill | What It Does |
|-------|-------------|
| `corpusiq-gbrain-operations` | Operate GBrain — agent brain layer |

---

## Marketplace Skills (290+)

Community-contributed skills from [skills.sh](https://skills.sh). Install with `npx skills add <owner/repo@skill>`. See the [Marketplace page](/hermes/skills/marketplace/) for detailed descriptions, install counts, and trending skills.

### Marketing & Growth — 45 skills

From [coreyhaines31/marketingskills](https://skills.sh/coreyhaines31/marketingskills) (1.8M+ total installs). The top marketing skill pack — every skill is production-tested. Covers SEO, CRO, copywriting, ads, content strategy, competitive analysis, community growth, and cold outreach. See the [Marketing Skills page](/hermes/skills/marketing/) for category breakdowns and workflow patterns.

Top skills: `seo-audit` (132K), `copywriting` (122K), `marketing-psychology` (90K), `content-strategy` (86K), `programmatic-seo` (83K).

### Development & GitHub — 10 skills

GitHub workflows, code review, CI/CD, and codebase analysis. From `obra/superpowers`, `wshobson/agents`, and `corpusiq-docs`. See the [Development Skills page](/hermes/skills/development/) for detailed workflows.

Top skills: `github-actions-docs` (206K), `requesting-code-review` (121K), `receiving-code-review` (98K).

### Agent Infrastructure — 8 skills

Browser automation, web design, and agent orchestration. Core infrastructure for Hermes operations.

Top skills: `agent-browser` (432K, Playwright), `vercel-react-best-practices` (462K), `web-design-guidelines` (377K).

### MCP & API Integration — 5 skills

MCP server development, API patterns, and web scraping at scale.

Top skills: `mcp-builder` (71K), `claude-api` (37K), `apify-ultimate-scraper` (12K).

### Code Quality & Review — 4 skills

Code review standards, testing patterns, and quality enforcement.

Top skills: `requesting-code-review` (121K), `receiving-code-review` (98K), `python-testing-patterns` (24K).

### Testing & QA — 4 skills

Browser testing, E2E patterns, and test automation.

Top skills: `webapp-testing` (92K), `e2e-testing-patterns` (18K).

### Content & Social — 5 skills

Content creation, research-backed writing, and social publishing.

Top skills: `persona-content-creator` (17K), `content-research-writer` (5K).

### AI Media — 5 skills

AI avatar generation, video editing, image generation, and UI design.

Top skills: `frontend-design` (521K), `video-edit` (217K), `ai-avatar-video` (118K).

### Operations & Productivity — 5 skills

Email-to-task automation, changelog generation, CI/CD pipeline design, and CRM automation.

### Orchestration & RAG — 6 skills

Multi-agent orchestration, RAG implementation, and workflow patterns.

Top skills: `rag-implementation` (9.5K), `langchain-rag` (8.6K), `workflow-orchestration-patterns` (8.2K).

### Infrastructure & DevOps — 5 skills

Docker, Kubernetes, serverless Postgres, and monitoring for agent services.

Top skills: `neon-postgres` (40.3K), `docker-expert` (18.9K), `kubernetes-specialist` (10.2K).

### Platform Integrations — 11 skills

Notion, Resend, Airtable, Salesforce, SharePoint, Dropbox, Box, and more.

Top skills: `notion-api` (42.1K), `agent-email-inbox` (3.3K), `notion-automation` (2.7K).

### Communication Bots — 4 skills

Telegram, WhatsApp, Slack, and Discord bot integrations for Hermes agents.

Top skills: `whatsapp-automation` (3.4K), `telegram-bot` (3.1K).

### Hermes Agent Variants — 30 skills

Alternative agent configurations from `nousresearch/hermes-agent`. Includes UI frameworks, creative tools, development integrations, and platform connectors. Install with `npx skills add nousresearch/hermes-agent@<variant>`.

Top variants: `dogfood` (3.6K), `yuanbao` (443), `popular-web-designs` (169).

### Hermes Ecosystem — 20 skills

Full Hermes agent skill suite from `aradotso/hermes-skills`. Web UIs, desktop companions, mission control, self-evolution, and multi-agent orchestration.

Top skills: `hermes-webui-agent` (193), `hermes-agent-self-evolution` (186).

### OpenClaw Ecosystem — 23 skills

Deployment, control centers, Chinese platform integrations, security, and community resources.

### Security Suite — 16 skills

Runtime security attestation, skill vetting, prompt injection detection, credential scanning, dependency auditing, and incident response. From `prompt-security/clawsec` and `useai-pro/openclaw-skills-security`.

Top skills: `skill-auditor` (590), `setup-auditor` (384), `skill-guard` (489).

### ClawPilot Ecosystem — 5 skills (June 16, 2026)

Mobile-to-agent bridge: pair PocketClaw (iOS) with Hermes/OpenClaw/cc-connect hosts. See the [June 16 Discovery page](/hermes/skills/marketplace/new-june16-2026/).

### Community Standalone — 10 skills

Independent community contributions: Hermes importers, alternative wrappers, platform integrations, and tools.

---

## Category Summary

| Category | Count |
|----------|:----:|
| Growth & Engagement | 13 |
| Research & Intelligence | 6 |
| Lead Response & Nurture | 11 |
| Email Operations | 7 |
| Video Production | 6 |
| Social Media Automation | 4 |
| LinkedIn Integration | 3 |
| Reddit Automation | 2 |
| Session & Execution | 6 |
| System Governance | 8 |
| Infrastructure | 5 |
| Browser & Web | 3 |
| Core Knowledge | 4 |
| Engineering | 8 |
| DevOps & Kanban | 1 |
| GBrain | 1 |
| **Native subtotal** | **90** |
| Marketing & Growth (marketplace) | 45 |
| Development (marketplace) | 10 |
| Agent Infrastructure (marketplace) | 8 |
| MCP & API (marketplace) | 5 |
| Code Quality (marketplace) | 4 |
| Testing & QA (marketplace) | 4 |
| Content & Social (marketplace) | 5 |
| AI Media (marketplace) | 5 |
| Operations & Productivity (marketplace) | 5 |
| Orchestration & RAG (marketplace) | 6 |
| Infrastructure & DevOps (marketplace) | 5 |
| Platform Integrations (marketplace) | 11 |
| Communication Bots (marketplace) | 4 |
| Hermes Variants (marketplace) | 30 |
| Hermes Ecosystem (marketplace) | 20 |
| OpenClaw Ecosystem (marketplace) | 23 |
| Security Suite (marketplace) | 16 |
| ClawPilot (marketplace) | 5 |
| Community Standalone (marketplace) | 10 |
| **Marketplace subtotal** | **290+** |
| **Grand Total** | **380+** |

---

## Quick Install

```bash
# Top marketing skill
npx skills add coreyhaines31/marketingskills@seo-audit

# Top development skill
npx skills add obra/superpowers@requesting-code-review

# Top infrastructure skill
npx skills add vercel-labs/agent-browser

# Install a full pack
npx skills add coreyhaines31/marketingskills

# List installed skills
hermes skills list
```

---

*← [Skills Overview](/hermes/skills/) | [Marketplace](/hermes/skills/marketplace/) → | ↑ [Home](/hermes/)*

*Powered by CorpusIQ*
