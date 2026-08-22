---
title: "Hermes Skills Catalog — Quality-Tiered Directory"
description: "Curated directory of community-validated Hermes agent skills. Quality tiers (Production/Beta/Community), starter pack, evaluation guide, and installation"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/"
robots: "index,follow"
last_updated: "2026-08-19"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Skills Catalog

Welcome to the Hermes Skills Catalog  --  your directory of community-contributed, validated skills that extend what Hermes can do. Skills encode repeatable expertise into shareable packages that anyone in the Hermes community can install and use.

## Skill Quality Tiers

Not all skills are created equal. We use three quality tiers to help you understand what you're installing:

### Production Tier 🟢

Production-tier skills meet all of these criteria:

- Tested by at least three independent community members
- Includes comprehensive error handling for all known failure modes
- Documentation covers setup, invocation, expected output, and troubleshooting
- Confirmation gates on all write/destructive operations
- Maintained actively (updated within 30 days of reported issues)
- Pinned dependencies and explicit version requirements
- Audit trail for all data access

These skills are safe for production use. You can rely on them as components of your automated workflows. Look for the 🟢 indicator in the catalog.

### Beta Tier 🟡

Beta-tier skills are functional and well-tested by their authors but haven't completed community validation:

- Tested by the author and at least one other person
- Handles common error cases but may have gaps in edge-case handling
- Documentation covers basic usage but may lack troubleshooting depth
- May lack comprehensive confirmation gates
- Updated within 90 days

These skills are suitable for supervised use. They'll save you time but keep an eye on them  --  especially in the first few runs. Look for the 🟡 indicator.

### Community Tier 🔵

Community-tier skills are shared in good faith but haven't completed formal validation:

- Published by a community member
- May have been tested only on the author's setup
- Documentation may be minimal
- Error handling may be incomplete
- Best suited for learning, inspiration, and adaptation  --  not production reliance

These skills are valuable for the community but require due diligence before relying on them. Look for the 🔵 indicator.

| [RunComfy Agent Skills](/hermes/skills/catalog/runcomfy-agent-skills-setup/) | 🟡 Beta | 30 | 61.1K | AI video, image-to-video, avatar video, video editing, music generation | `prime-skills/runcomfy-agent-skills` |

## How to Evaluate a Skill Before Installing

Before you trust a skill with your data and credentials, do this five-minute review:

### 1. Read the Skill Description
Does it clearly state what it does, what connectors it needs, and what output it produces? A skill that can't explain itself in three sentences is a red flag.

### 2. Check the Required Permissions
What connectors and tools does the skill call? Does "Generate weekly report" really need write access to your CRM? If the permission scope exceeds the stated purpose, investigate before installing.

### 3. Review the Error Handling
Open the skill file and look for error handling blocks. Does it handle timeouts? Rate limits? Missing data? A skill with no error handling will fail silently or confusingly.

### 4. Look for Confirmation Gates
If the skill can modify data, does it require confirmation before doing so? Any skill that writes without explicit user approval is a production risk.

### 5. Check Recency and Maintenance
When was the skill last updated? A skill that hasn't been touched in 12 months may have broken dependencies or incompatible API versions. Check the changelog.

### 6. Read Community Feedback
Look for comments, issues, or reviews from other community members. "Works great on my setup" from one person is positive. "Breaks when the dataset exceeds 100 records" is actionable.

### 7. Test in a Safe Environment
Run the skill first in a read-only mode or with limited data. Before you let it loose on your production CRM, test it on your sandbox.

## Curated Starter Pack

New to Hermes? These 10 skills are the most commonly recommended starting points. They cover essential workflows and are all Production-tier verified.

### 1. Daily Briefing
**What it does:** Your morning dashboard  --  calendar, priority emails, task list, and key metrics from connected services. One invocation replaces five separate checks.  
**Needs:** Calendar, email, and optionally CRM or project management connectors.  
**Why start here:** Replaces your morning routine with a single command. Immediate time savings.

### 2. Email Digest
**What it does:** Summarizes unread emails from a configurable time window, groups by thread, flags urgent items, and drafts suggested replies for routine messages.  
**Needs:** Email connector (Gmail or Outlook).  
**Why start here:** The average knowledge worker spends 2+ hours on email daily. This cuts it substantially.

### 3. Meeting Prep
**What it does:** Before a meeting, gathers relevant emails, documents, previous meeting notes, and action items related to the attendees and topic. Produces a one-page briefing.  
**Needs:** Calendar, email, and optionally drive or project management connectors.  
**Why start here:** Never walk into a meeting underprepared again.

### 4. Weekly Report Generator
**What it does:** Aggregates activity from your connected services into a structured weekly summary  --  tasks completed, meetings attended, key communications, metrics trends.  
**Needs:** Project management, calendar, email (configurable).  
**Why start here:** Automates the Friday afternoon ritual. Customize the template to match your team's format.

### 5. CRM Health Check
**What it does:** Pipeline analysis, stale deals, overdue follow-ups, and contact engagement scoring. Flags accounts that need attention.  
**Needs:** CRM connector (HubSpot, Salesforce, or similar).  
**Why start here:** Your CRM has data but Hermes turns it into action items.

### 6. Data to Chart
**What it does:** Takes a dataset (from any connector or upload) and generates appropriate visualizations  --  time series, distribution, comparison, correlation.  
**Needs:** Any data source (accepts structured data from other skills).  
**Why start here:** Visual insight without spreadsheet wrestling.

### 7. Content Drafting Assistant
**What it does:** Drafts blog posts, social media updates, newsletters, and other content following your brand voice. Includes tone calibration and audience targeting.  
**Needs:** No specific connectors (optionally integrates with CMS or social platforms).  
**Why start here:** Beat the blank page. All output is draft  --  you remain the editor.

### 8. Code Review Companion
**What it does:** Reviews code changes for bugs, security issues, style consistency, and documentation completeness. Provides actionable, specific feedback.  
**Needs:** File access or repository connector.  
**Why start here:** A second pair of eyes on every PR, catching issues before humans spend time reviewing.

### 9. Travel Planner
**What it does:** Given destination and dates, gathers flight options, hotel availability, weather forecasts, and local information. Organizes into a comparison view.  
**Needs:** Calendar (for availability context).  
**Why start here:** Research acceleration  --  you still book, but Hermes does the hunting.

### 10. Knowledge Base Q&A
**What it does:** Searches your organization's documentation, wikis, and shared drives to answer questions. "What's our vacation policy?" "How do I set up the VPN?"  
**Needs:** Drive, wiki, or documentation connectors.  
**Why start here:** Reduces the "just ask Bob" tax on your organization's experts.

## Installing a Skill

Skills from the catalog install with a single command. From the catalog page, copy the install command and run it in your Hermes terminal. The skill and its dependencies are installed to your profile.

```bash
hermes skills install skill-id
```

After installation, configure any required connectors. Most skills include a setup guide that walks through connector authentication. Test with a dry run before relying on the skill in production workflows.

## Contributing to the Catalog

The skills catalog thrives on community contributions. If you've built something useful:

1. Follow the [skill development best practices](../../best-practices/skill-development.md)
2. Test thoroughly in your environment
3. Document setup, invocation, and expected output
4. Remove environment-specific values (use placeholders)
5. Submit through the catalog contribution process

Skills are reviewed by community maintainers before publication. The review checks for documentation completeness, error handling, security considerations, and community value  --  not whether every edge case is handled (that's what quality tiers communicate).

## Finding More Skills

The catalog here represents community-validated skills. Additional skills are discoverable through:

- **[skills.sh](https://skills.sh)**  --  Large open marketplace
- **[agentskills.io](https://agentskills.io)**  --  Curated premium and community skills
- **[hermeshub](https://hermeshub.nousresearch.com)**  --  Official Hermes skill registry
- **[skilldock.io](https://skilldock.io)**  --  Enterprise-focused skill marketplace
- **GitHub**  --  Search for "hermes-skill" or "hermes-skill-" prefixed repositories

See [Skill Marketplaces](../skill-marketplaces.md) for detailed guidance on each marketplace.

The catalog is a living resource. Skills are added weekly. Check back often, and consider contributing what you build.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*


## All Skills Catalog Pages

- [find-skills — Skill Discovery Tool Setup](/docs/hermes/skills/catalog/find-skills-setup/)
- [skill-creator — Anthropic's Skill Creation Framework Setup](/docs/hermes/skills/catalog/skill-creator-setup/)
- [remotion-best-practices — Video Production Setup](/docs/hermes/skills/catalog/remotion-best-practices-setup/)
- [browser-act — Record-and-Replay Browser Automation Setup](/docs/hermes/skills/catalog/browser-act-setup/)
- [firecrawl-workflows — Growth & Research Automation Setup](/docs/hermes/skills/catalog/firecrawl-workflows-setup/)
- [Firecrawl Agent — AI-Powered Structured Data Extraction Setup](/docs/hermes/skills/catalog/firecrawl-agent-setup/)
- [Agent Browser — Vercel Labs CLI for AI Agents Setup](/docs/hermes/skills/catalog/agent-browser-setup/)
- [Agent Flywheel Mega-Toolkit Setup Guide](/docs/hermes/skills/catalog/agent-flywheel-setup/)
- [agent-sessions — macOS Agent Session Browser Setup](/docs/hermes/skills/catalog/agent-sessions-setup/)
- [Agenthood Setup](/docs/hermes/skills/catalog/agenthood-setup/)
- [Agentmint Skills Setup](/docs/hermes/skills/catalog/agentmint-skills-setup/)
- [AgentMemory Setup — Persistent Memory for Hermes Agents](/docs/hermes/skills/catalog/agentmemory-setup/)
- [Alireza Rezvani Claude Skills — 341 Engineering & Marketing Skills Setup](/docs/hermes/skills/catalog/alirezarezvani-claude-skills-setup/)
- [Apify Agent Skills — Web Scraping for Hermes Setup](/docs/hermes/skills/catalog/apify-agent-skills-setup/)
- [Apify Growth Skills — Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/docs/hermes/skills/catalog/apify-growth-skills-setup/)
- [Apify Ultimate Scraper — Universal Web Scraping for 15+ Platforms Setup](/docs/hermes/skills/catalog/apify-ultimate-scraper-setup/)
- [Apple Calendar Setup](/docs/hermes/skills/catalog/apple-calendar-setup/)
- [Arxiv Setup](/docs/hermes/skills/catalog/arxiv-setup/)
- [Ashima Setup](/docs/hermes/skills/catalog/ashima-setup/)
- [Autolora Setup](/docs/hermes/skills/catalog/autolora-setup/)
- [Awesome Copilot — MCP Server Generators & GitHub Automation Setup](/docs/hermes/skills/catalog/awesome-copilot-setup/)
- [bb-browser-openclaw — Setup Guide](/docs/hermes/skills/catalog/bb-browser-openclaw-setup/)
- [Blogwatcher — RSS/Atom Feed Monitoring for Hermes](/docs/hermes/skills/catalog/blogwatcher-setup/)
- [Blueprint Orchestration Setup](/docs/hermes/skills/catalog/blueprint-orchestration-setup/)
- [browser-harness Setup Guide](/docs/hermes/skills/catalog/browser-harness-setup/)
- [Build Mcp Server Setup](/docs/hermes/skills/catalog/build-mcp-server-setup/)
- [cinematic-scroll-skill — Scroll-Driven Website Builder Setup](/docs/hermes/skills/catalog/cinematic-scroll-skill-setup/)
- [Claude Office Skills](/docs/hermes/skills/catalog/claude-office/)
- [ClawDBot Feishu Suite Setup Guide](/docs/hermes/skills/catalog/clawdbot-feishu-setup/)
- [Setup Guide: napoleond/clawdirect — Agent Self-Direction Framework (9K+ Installs)](/docs/hermes/skills/catalog/clawdirect-setup/)
- [Setup Guide: steipete/clawdis — 14 OpenClaw Skills (37K+ Installs)](/docs/hermes/skills/catalog/clawdis-setup/)
- [Setup Guide: cantinaxyz/clawdstrike — Agent Red-Team Security Testing (486 Installs)](/docs/hermes/skills/catalog/clawdstrike-setup/)
- [ClawFu Skills — 175 Marketing Methodologies for AI Agents Setup](/docs/hermes/skills/catalog/clawfu-skills-setup/)
- [Clawpilot Ecosystem Setup](/docs/hermes/skills/catalog/clawpilot-ecosystem-setup/)
- [Claude Code Skills — Agentic Coding & Skill Development Setup](/docs/hermes/skills/catalog/claude-code-skills-setup/)
- [Claude Handoff — Session Handoff Pattern Setup](/docs/hermes/skills/catalog/claude-handoff-setup/)
- [Clean Slate Setup](/docs/hermes/skills/catalog/clean-slate-setup/)
- [Clerk Auth Skills — Authentication & User Management Setup](/docs/hermes/skills/catalog/clerk-auth-skills-setup/)
- [Cli Anything Harnesses Setup](/docs/hermes/skills/catalog/cli-anything-harnesses-setup/)
- [Cli Anything Hermes Setup](/docs/hermes/skills/catalog/cli-anything-hermes-setup/)
- [Codex — Delegate Coding Tasks to OpenAI Codex CLI](/docs/hermes/skills/catalog/codex-setup/)
- [Coding Posture Setup](/docs/hermes/skills/catalog/coding-posture-setup/)
- [Chrome DevTools MCP Skills — Browser Debugging & Automation Setup](/docs/hermes/skills/catalog/chrome-devtools-mcp-skills-setup/)
- [communication Skills](/docs/hermes/skills/catalog/communication/)
- [Content Strategy — Full Planning Framework Setup](/docs/hermes/skills/catalog/content-strategy-setup/)
- [Context Forge Rag Setup](/docs/hermes/skills/catalog/context-forge-rag-setup/)
- [Cron Design Workflow Setup](/docs/hermes/skills/catalog/cron-design-workflow-setup/)
- [Deep Agents Memory — LangChain Persistent Memory Setup](/docs/hermes/skills/catalog/deep-agents-memory-setup/)
- [Delegate Skills Setup](/docs/hermes/skills/catalog/delegate-skills-setup/)
- [Design Judge Skills — Design Award Workflow Setup](/docs/hermes/skills/catalog/design-judge-skills-setup/)
- [Distribute Skill To All Agents Setup](/docs/hermes/skills/catalog/distribute-skill-to-all-agents-setup/)
- [Dogfood — Systematic QA Testing Setup](/docs/hermes/skills/catalog/dogfood-setup/)
- [elevenlabs Skills](/docs/hermes/skills/catalog/elevenlabs/)
- [firebase Skills](/docs/hermes/skills/catalog/firebase/)
- [firecrawl Skills](/docs/hermes/skills/catalog/firecrawl/)
- [Gbrain Agent Operations Setup](/docs/hermes/skills/catalog/gbrain-agent-operations-setup/)
- [Ghostwriter Setup](/docs/hermes/skills/catalog/ghostwriter-setup/)
- [Guizang Social Card Skill — Social Card Generation Setup](/docs/hermes/skills/catalog/guizang-social-card-skill-setup/)
- [Google Workspace Skills](/docs/hermes/skills/catalog/google-workspace/)
- [Halt Catch Fire Skills Setup](/docs/hermes/skills/catalog/halt-catch-fire-skills-setup/)
- [Herman Skill Playbook Setup](/docs/hermes/skills/catalog/herman-skill-playbook-setup/)
- [Hermes A2A Bridge Setup](/docs/hermes/skills/catalog/hermes-a2a-bridge-setup/)
- [Hermes Advanced Memory Setup](/docs/hermes/skills/catalog/hermes-advanced-memory-setup/)
- [Hermes Agent Core — Official Skill Setup Guide](/docs/hermes/skills/catalog/hermes-agent-setup/)
- [Hermes Agent Self-Evolution — Auto-Learning Framework Setup](/docs/hermes/skills/catalog/hermes-agent-self-evolution-setup/)
- [Hermes Agent Skill Authoring — Official SKILL.md Writing Guide](/docs/hermes/skills/catalog/hermes-agent-skill-authoring-setup/)
- [AGEL-Comp Safety Framework — Setup Guide](/docs/hermes/skills/catalog/hermes-agel-comp-setup/)
- [Hermes Agency Setup](/docs/hermes/skills/catalog/hermes-agency-setup/)
- [Hermes Agentmesh Async Bus](/docs/hermes/skills/catalog/hermes-agentmesh-async-bus/)
- [Hermes ArXiv Agent — ArXiv Paper Fetcher Setup](/docs/hermes/skills/catalog/hermes-arxiv-agent-setup/)
- [Hermes Bible Skill Setup](/docs/hermes/skills/catalog/hermes-bible-skill-setup/)
- [Hermes Browser Extension — Full Setup Guide](/docs/hermes/skills/catalog/hermes-browser-extension-setup/)
- [Hermes Client Web Ui Setup](/docs/hermes/skills/catalog/hermes-client-web-ui-setup/)
- [Hermes Cursor Dispatcher — Cursor CLI Delegation Setup](/docs/hermes/skills/catalog/hermes-cursor-dispatcher-setup/)
- [Datadog Agent Skills — Observability & Monitoring Setup](/docs/hermes/skills/catalog/datadog-agent-skills-setup/)
- [Hermes Desktop Neo Theme — Setup Guide](/docs/hermes/skills/catalog/hermes-desktop-neo-theme-setup/)
- [Hermes Engineering Curation Setup](/docs/hermes/skills/catalog/hermes-engineering-curation-setup/)
- [Hermes Ershov Setup](/docs/hermes/skills/catalog/hermes-ershov-setup/)
- [Hermes Flight Recorder Setup](/docs/hermes/skills/catalog/hermes-flight-recorder-setup/)
- [Hermes Full Backup — Setup Guide](/docs/hermes/skills/catalog/hermes-full-backup-setup/)
- [hermes-history-ingest Setup Guide](/docs/hermes/skills/catalog/hermes-history-ingest-setup/)
- [Hermes Hybrid Memory — Full Setup Guide](/docs/hermes/skills/catalog/hermes-hybrid-memory-setup/)
- [Hermes Imports — Workflow Sanitization & Export Setup](/docs/hermes/skills/catalog/hermes-imports-setup/)
- [Hermes Marketing Dashboard — AI Agent Marketing Ops Setup](/docs/hermes/skills/catalog/hermes-marketing-dashboard-setup/)
- [Hermes Memory Stack Setup](/docs/hermes/skills/catalog/hermes-memory-stack-setup/)
- [Hermes Meshtastic Adapter — LoRa Mesh Integration Setup](/docs/hermes/skills/catalog/hermes-meshtastic-adapter-setup/)
- [Hermes Obsidian Giveaway Pack Setup](/docs/hermes/skills/catalog/hermes-obsidian-giveaway-pack-setup/)
- [Hermes Ponytail Setup](/docs/hermes/skills/catalog/hermes-ponytail-setup/)
- [Hermes S6 Container Supervision Setup](/docs/hermes/skills/catalog/hermes-s6-container-supervision-setup/)
- [Hermes Session Maintenance Setup](/docs/hermes/skills/catalog/hermes-session-maintenance-setup/)
- [Hermes Skill Cleaner Setup](/docs/hermes/skills/catalog/hermes-skill-cleaner-setup/)
- [hermes-top — Setup Guide](/docs/hermes/skills/catalog/hermes-top-setup/)
- [Hermes Whatsapp Secretary Setup](/docs/hermes/skills/catalog/hermes-whatsapp-secretary-setup/)
- [Hermes Windows Native](/docs/hermes/skills/catalog/hermes-windows-native/)
- [Hermespace — Persistent Agent World Setup](/docs/hermes/skills/catalog/hermespace-setup/)
- [Hermespet Macos Ai Companion Setup](/docs/hermes/skills/catalog/hermespet-macos-ai-companion-setup/)
- [Hermex iPhone App — Setup Guide for Hermes Agent](/docs/hermes/skills/catalog/hermex-iphone-app-setup/)
- [Honcho Integration Setup](/docs/hermes/skills/catalog/honcho-integration-setup/)
- [Huawei Hermes Deployment Setup](/docs/hermes/skills/catalog/huawei-hermes-deployment-setup/)
- [HuggingFace Agent Skills — Datasets, Papers, ML Tools Setup](/docs/hermes/skills/catalog/huggingface-agent-skills-setup/)
- [Humanizer Setup](/docs/hermes/skills/catalog/humanizer-setup/)
- [Hyperframes Setup](/docs/hermes/skills/catalog/hyperframes-setup/)
- [Idea Workflow Suite Setup](/docs/hermes/skills/catalog/idea-workflow-suite-setup/)
- [Imap Smtp Email Setup](/docs/hermes/skills/catalog/imap-smtp-email-setup/)
- [Impeccable Design Setup](/docs/hermes/skills/catalog/impeccable-design-setup/)
- [Impeccable Setup](/docs/hermes/skills/catalog/impeccable-setup/)
- [Inference Sh Skills Setup](/docs/hermes/skills/catalog/inference-sh-skills-setup/)
- [infrastructure Skills](/docs/hermes/skills/catalog/infrastructure/)
- [Jupyter Live Kernel Setup](/docs/hermes/skills/catalog/jupyter-live-kernel-setup/)
- [Kanban Orchestrator Setup](/docs/hermes/skills/catalog/kanban-orchestrator-setup/)
- [Kostja94 Marketing Skills — Copywriting, SEO, Ads Setup](/docs/hermes/skills/catalog/kostja94-marketing-skills-setup/)
- [LangChain Agent Skills — Memory, RAG, Persistence & Middleware Setup](/docs/hermes/skills/catalog/langchain-skills-setup/)
- [langgraph Skills](/docs/hermes/skills/catalog/langgraph/)
- [LaunchDarkly Agent Skills — Feature Flags & AgentControl Setup](/docs/hermes/skills/catalog/launchdarkly-agent-skills-setup/)
- [Letta Ai Agent Harness Setup](/docs/hermes/skills/catalog/letta-ai-agent-harness-setup/)
- [Linux Systemd Setup](/docs/hermes/skills/catalog/linux-systemd-setup/)
- [Llm Ops Setup](/docs/hermes/skills/catalog/llm-ops-setup/)
- [Loop Maker Setup](/docs/hermes/skills/catalog/loop-maker-setup/)
- [Macos Computer Use Setup](/docs/hermes/skills/catalog/macos-computer-use-setup/)
- [Macos Launchd Setup](/docs/hermes/skills/catalog/macos-launchd-setup/)
- [Math Via Code Setup](/docs/hermes/skills/catalog/math-via-code-setup/)
- [Matt Pocock Engineering Skills — Setup Guide for Hermes Agents](/docs/hermes/skills/catalog/matt-pocock-engineering-setup/)
- [Mattpocock Skills Setup](/docs/hermes/skills/catalog/mattpocock-skills-setup/)
- [MCP Use Setup — Fullstack MCP Framework for Hermes](/docs/hermes/skills/catalog/mcp-use-setup/)
- [Monitoring Expert — Observability & Monitoring Setup](/docs/hermes/skills/catalog/monitoring-expert-setup/)
- [memoria-vault — Multi-Agent Research OS for Obsidian Setup](/docs/hermes/skills/catalog/memoria-vault-setup/)
- [Memory Hygiene Setup](/docs/hermes/skills/catalog/memory-hygiene-setup/)
- [Memory Merger Setup — Agent Session Memory Consolidation](/docs/hermes/skills/catalog/memory-merger-setup/)
- [Media Use Setup — Agent Media OS for HyperFrames (182.7K installs)](/docs/hermes/skills/catalog/media-use-setup/)
- [Metamask Openclaw Security Analysis Setup](/docs/hermes/skills/catalog/metamask-openclaw-security-analysis-setup/)
- [Native Mcp Setup](/docs/hermes/skills/catalog/native-mcp-setup/)
- [Nemoclaw User Guide Setup](/docs/hermes/skills/catalog/nemoclaw-user-guide-setup/)
- [Netlify Agent Skills — Serverless Deployment for Hermes Setup](/docs/hermes/skills/catalog/netlify-agent-skills-setup/)
- [OpenClaw Agent Skills — Official OpenClaw Org Skill Suite Setup](/docs/hermes/skills/catalog/openclaw-agent-skills-setup/)
- [OpenClaw on Android — Full Setup Guide](/docs/hermes/skills/catalog/openclaw-android-setup/)
- [OpenClaw Audit Watchdog — Setup Guide](/docs/hermes/skills/catalog/openclaw-audit-watchdog-setup/)
- [Openclaw Auto Updater Setup](/docs/hermes/skills/catalog/openclaw-auto-updater-setup/)
- [OpenClaw Backup — Encrypted Agent Workspace Backup Setup](/docs/hermes/skills/catalog/openclaw-backup-setup/)
- [Openclaw Customizer Setup](/docs/hermes/skills/catalog/openclaw-customizer-setup/)
- [Openclaw Ecosystem June26 Setup](/docs/hermes/skills/catalog/openclaw-ecosystem-june26-setup/)
- [Openclaw Grok Search Setup](/docs/hermes/skills/catalog/openclaw-grok-search-setup/)
- [openclaw-history-ingest Setup Guide](/docs/hermes/skills/catalog/openclaw-history-ingest-setup/)
- [OpenClaw Marketing Skills — Setup Guide](/docs/hermes/skills/catalog/openclaw-marketing-skills-setup/)
- [Openclaw Secure Linux Cloud Setup](/docs/hermes/skills/catalog/openclaw-secure-linux-cloud-setup/)
- [Openclaw Security Hardening Setup](/docs/hermes/skills/catalog/openclaw-security-hardening-setup/)
- [Openclaw Skill Vetter Setup](/docs/hermes/skills/catalog/openclaw-skill-vetter-setup/)
- [OpenClaw XHS Setup — Xiaohongshu (RED) Integration](/docs/hermes/skills/catalog/openclaw-xhs-setup/)
- [OpenAI Codex Skills — Official Skills Catalog Setup](/docs/hermes/skills/catalog/openai-codex-skills-setup/)
- [OpenTUI — Terminal UI Framework Setup](/docs/hermes/skills/catalog/opentui-setup/)
- [OPC Skills — Solopreneur Toolkit (SEO, Reddit, Branding, Launch) Setup](/docs/hermes/skills/catalog/opc-skills-setup/)
- [Oh My Hermes (OMH) Suite — Multi-Agent Orchestration Skills Setup](/docs/hermes/skills/catalog/oh-my-hermes-omh-suite-setup/)
- [Parallel Agent Skills — Web Intelligence for Hermes Setup](/docs/hermes/skills/catalog/parallel-agent-skills-setup/)
- [Perfectloop Setup](/docs/hermes/skills/catalog/perfectloop-setup/)
- [Petdex — Animated Mascots for Hermes Agent](/docs/hermes/skills/catalog/petdex-setup/)
- [Popular Web Designs — 54 Design Systems as HTML/CSS Templates Setup](/docs/hermes/skills/catalog/popular-web-designs-setup/)
- [PowerPoint — Create, Read, Edit .pptx Decks Setup](/docs/hermes/skills/catalog/powerpoint-setup/)
- [platform Skills](/docs/hermes/skills/catalog/platform/)
- [prisma Skills](/docs/hermes/skills/catalog/prisma/)
- [Railway Agent Skills — Infrastructure Deployment Setup](/docs/hermes/skills/catalog/railway-agent-skills-setup/)
- [Reddit Automation — Honest Reddit Engagement Setup](/docs/hermes/skills/catalog/reddit-automation-setup/)
- [ResumeSkills — AI-Powered Resume Optimization Setup](/docs/hermes/skills/catalog/resumeskills-setup/)
- [Safari Web Agent Setup](/docs/hermes/skills/catalog/safari-web-agent-setup/)
- [Security Hardening — AI Agent Security Setup](/docs/hermes/skills/catalog/security-and-hardening-setup/)
- [Sentry AI Monitoring — Agent Error Tracking Setup](/docs/hermes/skills/catalog/sentry-ai-monitoring-setup/)
- [Sg Arrival Card Setup](/docs/hermes/skills/catalog/sg-arrival-card-setup/)
- [shopify Skills](/docs/hermes/skills/catalog/shopify/)
- [Skill Repo Manager Setup](/docs/hermes/skills/catalog/skill-repo-manager-setup/)
- [Skill Vetting Setup](/docs/hermes/skills/catalog/skill-vetting-setup/)
- [Skill Vetter — Security Audit for Hermes Skills Setup](/docs/hermes/skills/catalog/skill-vetter-setup/)
- [Skills Gallery Setup](/docs/hermes/skills/catalog/skills-gallery-setup/)
- [Social Content — Multi-Platform Social Media Creation Setup](/docs/hermes/skills/catalog/social-setup/)
- [Soul Grader Setup](/docs/hermes/skills/catalog/soul-grader-setup/)
- [Spike Setup](/docs/hermes/skills/catalog/spike-setup/)
- [Stepfun Skills Setup](/docs/hermes/skills/catalog/stepfun-skills-setup/)
- [Steroids Openai Image Gen Setup](/docs/hermes/skills/catalog/steroids-openai-image-gen-setup/)
- [stripe Skills](/docs/hermes/skills/catalog/stripe/)
- [supabase Skills](/docs/hermes/skills/catalog/supabase/)
- [Superpowers — Agentic Skills Framework Setup](/docs/hermes/skills/catalog/superpowers-setup/)
- [Tavily Search Openclaw Setup](/docs/hermes/skills/catalog/tavily-search-openclaw-setup/)
- [Tavily Search — Official LLM-Optimized Web Search CLI Setup](/docs/hermes/skills/catalog/tavily-search-setup/)
- [Tavily Research — AI-Powered Deep Research Setup](/docs/hermes/skills/catalog/tavily-research-setup/)
- [Threads Growth Skill Setup](/docs/hermes/skills/catalog/threads-growth-skill-setup/)
- [Three Agent Bridge Setup](/docs/hermes/skills/catalog/three-agent-bridge-setup/)
- [Timesfm Forecasting Setup](/docs/hermes/skills/catalog/timesfm-forecasting-setup/)
- [Trailofbits Security Setup](/docs/hermes/skills/catalog/trailofbits-security-setup/)
- [Ultimate Humanizer Setup](/docs/hermes/skills/catalog/ultimate-humanizer-setup/)
- [Vercel Agent Skills — Official Vercel Collection Setup](/docs/hermes/skills/catalog/vercel-agent-skills-setup/)
- [Vps Server Management Setup](/docs/hermes/skills/catalog/vps-server-management-setup/)
- [Wiki History Ingest Setup](/docs/hermes/skills/catalog/wiki-history-ingest-setup/)
- [Writing Plans Subagent Development Setup](/docs/hermes/skills/catalog/writing-plans-subagent-development-setup/)
- [wshobson/agents — Agent Plugin Marketplace Setup](/docs/hermes/skills/catalog/wshobson-agents-setup/)
- [X Twitter Scraper Setup](/docs/hermes/skills/catalog/x-twitter-scraper-setup/)
- [Xurl Setup](/docs/hermes/skills/catalog/xurl-setup/)
- [Youtube Content Setup](/docs/hermes/skills/catalog/youtube-content-setup/)
- [Yuanbao — Tencent Group Chat Integration Setup](/docs/hermes/skills/catalog/yuanbao-setup/)
- [Better Auth Skills — Authentication Infrastructure Setup](/docs/hermes/skills/catalog/better-auth-skills-setup/)
- [Google Agents CLI — Google ADK Setup](/docs/hermes/skills/catalog/google-agents-cli-setup/)
- [GTM Agents — Go-to-Market Sales Skills Setup](/docs/hermes/skills/catalog/gtm-agents-setup/)
- [Knowledge Work Plugins — Anthropic Productivity Setup](/docs/hermes/skills/catalog/knowledge-work-plugins-setup/)
- [Lenny Skills — PM Methodology from Lenny Rachitsky Setup](/docs/hermes/skills/catalog/lenny-skills-setup/)
- [Sanity Agent Toolkit — Headless CMS Setup](/docs/hermes/skills/catalog/sanity-agent-toolkit-setup/)
- [SERP Downloaders — Content Downloader Skills Setup](/docs/hermes/skills/catalog/serpdownloaders-setup/)
- [Skills Collective AI Media — Image & Video Gen Setup](/docs/hermes/skills/catalog/skills-collective-ai-media-setup/)
- [Midscene Skills — AI-Powered Visual Browser Automation Setup](/docs/hermes/skills/catalog/midscene-skills-setup/)
- [Browser-Use Automation — AI Browser for Anti-Bot Sites Setup](/docs/hermes/skills/catalog/browser-use-automation-setup/)
- [Playwright Social Media Automation — API-First Browser Fallback Setup](/docs/hermes/skills/catalog/playwright-social-media-automation-setup/)
- [Ruflo — Multi-Agent Orchestration Platform Setup](/docs/hermes/skills/catalog/ruflo-setup/)
- [Stitch Skills — Google Design-to-Code Pipeline Setup](/docs/hermes/skills/catalog/stitch-skills-setup/)
- [just-scrape — AI-Powered Web Scraping CLI Setup](/docs/hermes/skills/catalog/just-scrape-setup/)
- [Terminal Skills — System Administration Pack Setup](/docs/hermes/skills/catalog/terminal-skills-setup/)
- [Finance Skills — Financial Analysis for Agents Setup](/docs/hermes/skills/catalog/finance-skills-setup/)
- [Songwriting & AI Music — Creative Music Generation Setup](/docs/hermes/skills/catalog/songwriting-and-ai-music-setup/)
- [Debugging Hermes TUI Commands — Slash Command Troubleshooting Setup](/docs/hermes/skills/catalog/debugging-hermes-tui-commands-setup/)
- [Hermes Attestation Guardian — Security Verification Setup](/docs/hermes/skills/catalog/hermes-attestation-guardian-setup/)
- [Research Paper Writing Pipeline — Academic ML/AI Paper Production Setup](/docs/hermes/skills/catalog/research-paper-writing-setup/)
- [Plan Mode — Plan-Only Execution Mode Setup](/docs/hermes/skills/catalog/plan-mode-setup/)
- [Godmode — Autonomous Execution Mode Setup](/docs/hermes/skills/catalog/godmode-setup/)
- [p5js — Creative Coding & Generative Art Setup](/docs/hermes/skills/catalog/p5js-setup/)
- [Polymarket — Prediction Market Integration Setup](/docs/hermes/skills/catalog/polymarket-setup/)
- [Simplify Code — Parallel Review & Cleanup Setup](/docs/hermes/skills/catalog/simplify-code-setup/)
- [Subagent-Driven Development — Multi-Agent Task Dispatch Setup](/docs/hermes/skills/catalog/subagent-driven-development-setup/)
- [HeartMuLa — Open-Source AI Music Generation Setup](/docs/hermes/skills/catalog/heartmula-setup/)
- [Creative Ideation — Constraint-Driven Brainstorming Setup](/docs/hermes/skills/catalog/ideation-setup/)
- [Linear Integration — Issue & Project Management Setup](/docs/hermes/skills/catalog/linear-setup/)
- [Webhook Subscriptions — External Service Trigger Setup](/docs/hermes/skills/catalog/webhook-subscriptions-setup/)
- [OpenClaw Carapace — Design System Skills Setup](/docs/hermes/skills/catalog/openclaw-carapace-setup/)
- [OpenClaw Graph New Skills — Procedural Generation, ARKit, Testing Setup](/docs/hermes/skills/catalog/openclaw-graph-new-skills-setup/)
- [MCP OAuth Remote Gateway — Official Hermes Skill Setup](/docs/hermes/skills/catalog/hermes-mcp-oauth-remote-gateway-setup/)
- [Mnemosyne Hermes Memory Providers — Local-First Agent Memory Setup](/docs/hermes/skills/catalog/mnemosyne-hermes-memory-providers-setup/)
- [Audit Hermes Agent Skills — Skill Usage Audit & Cleanup Setup](/docs/hermes/skills/catalog/cnife-audit-hermes-agent-skills-setup/)
- [Volces Hermes & OpenClaw Skills — ByteDance Registry Cluster Setup](/docs/hermes/skills/catalog/volces-hermes-openclaw-skills-setup/)
- [Grounded Citations — Verifiable Source Citations Setup](/docs/hermes/skills/catalog/grounded-citations-setup/)
- [Lark & Feishu Skills — Office Suite Automation Setup](/docs/hermes/skills/catalog/lark-feishu-skills-setup/)
- [RigorPilot Skills — AI Research & Paper Reproduction Setup](/docs/hermes/skills/catalog/rigorpilot-skills-setup/)
- [Caveman Skills — Agent Coding Workflow Suite Setup](/docs/hermes/skills/catalog/caveman-skills-setup/)
- [Skills-101 Superpowers — AI Media & Automation Pack Setup](/docs/hermes/skills/catalog/skills-101-superpowers-setup/)
- [Warp Common Skills — Spec-Driven Development Workflow Setup](/docs/hermes/skills/catalog/warpdotdev-common-skills-setup/)
- [Uizze UI Skills — Anti-UI-Slop Design Quality Setup](/docs/hermes/skills/catalog/uizze-ui-skills-setup/)
- [Stably Orca — Agent Orchestration CLI Setup](/docs/hermes/skills/catalog/stablyai-orca-setup/)
- [Extract Design System — UI Token & Component Extraction Setup](/docs/hermes/skills/catalog/extract-design-system-setup/)
- [App Store Connect CLI — Mobile Release Automation Setup](/docs/hermes/skills/catalog/app-store-connect-cli-skills-setup/)
- [GenMedia Skills — AI Media Generation Cluster Setup](/docs/hermes/skills/catalog/genmedia-skills-setup/)
- [Pika Plugins — Marketing Video Skill Pack Setup](/docs/hermes/skills/catalog/pika-plugins-setup/)
- [FlowKit Reddit Automation — Community Engagement Setup](/docs/hermes/skills/catalog/flowkit-reddit-automation-setup/)
- [HumanLayer Skills — Human-in-the-Loop Patterns Setup](/docs/hermes/skills/catalog/humanlayer-skills-setup/)
- [NuShell Pro — Structured Shell Scripting Setup](/docs/hermes/skills/catalog/nushell-pro-setup/)
- [Fetcher Skills — Social Platform API Cluster Setup](/docs/hermes/skills/catalog/fetcher-skills-setup/)
- [Convex Agent Skills — Backend Platform (BaaS) Setup](/docs/hermes/skills/catalog/convex-agent-skills-setup/)
- [Emil Kowalski Skills — Design Engineering Suite Setup](/docs/hermes/skills/catalog/emilkowalski-skills-setup/)
- [UI/UX Pro Max — Design System Skill Pack Setup](/docs/hermes/skills/catalog/ui-ux-pro-max-setup/)
- [Higgsfield Skills — AI Video & Image Generation Cluster Setup](/docs/hermes/skills/catalog/higgsfield-skills-setup/)
- [OSINT Skills — Open-Source Intelligence Suite Setup](/docs/hermes/skills/catalog/osint-skills-setup/)
- [Wind Skills — Financial Terminal Research Cluster Setup](/docs/hermes/skills/catalog/wind-skills-setup/)
- [Momentic Skills — AI QA Testing Suite Setup](/docs/hermes/skills/catalog/momentic-skills-setup/)
- [Planning With Files — Agent Planning Methodology Setup](/docs/hermes/skills/catalog/planning-with-files-setup/)
- [Wonda CLI — Terminal AI Content Creation Setup](/docs/hermes/skills/catalog/wonda-setup/)
- [SquirrelScan Skills — Website Audit Tool Setup](/docs/hermes/skills/catalog/squirrelscan-skills-setup/)
- [Solana Dev Skill — Blockchain Development Setup](/docs/hermes/skills/catalog/solana-dev-skill-setup/)
- [Genkit Skills — Firebase Genkit AI Framework Setup](/docs/hermes/skills/catalog/genkit-skills-setup/)
- [Firecrawl Skills — Web Scraping, Research & Workflow Suite Setup](/docs/hermes/skills/catalog/firecrawl-skills-setup/)
- [Nexscope E-Commerce Skills — Shopify, Etsy, TikTok Shop & Marketplace Growth Setup](/docs/hermes/skills/catalog/nexscope-ecommerce-skills-setup/)
- [SEO GEO Claude Skills — SEO & Generative Engine Optimization Suite Setup](/docs/hermes/skills/catalog/seo-geo-claude-skills-setup/)
- [n8n Skills — Workflow Automation for Business Operators Setup](/docs/hermes/skills/catalog/n8n-skills-setup/)
- [Review Loop Skill — Continuous Code Review Discipline Setup](/docs/hermes/skills/catalog/review-loop-skill-setup/)
- [ECC Engineering Skills — Enterprise Engineering Suite Setup](/docs/hermes/skills/catalog/ecc-engineering-skills-setup/)
- [Flutter Agent Plugins — Official Flutter Skills Setup](/docs/hermes/skills/catalog/flutter-agent-plugins-setup/)
- [Sentry Dev Skill — Official Sentry CLI Setup](/docs/hermes/skills/catalog/sentry-dev-skills-setup/)
- [Pexo Video Skills — AI Video Generation Suite Setup](/docs/hermes/skills/catalog/pexo-video-skills-setup/)
- [SEOJuice Skills — SEO Suite Setup](/docs/hermes/skills/catalog/seojuice-skills-setup/)
- [Better UI Skills — Interface Polish Suite Setup](/docs/hermes/skills/catalog/better-ui-skills-setup/)
- [CodeRabbit Skills — AI Code Review Setup](/docs/hermes/skills/catalog/coderabbit-skills-setup/)
- [Awesome LLM Apps Skills — Role-Based Agent Skills Setup](/docs/hermes/skills/catalog/awesome-llm-apps-skills-setup/)
- [CaffeineLabs Extension Skills — Agent Platform Extensions Setup](/docs/hermes/skills/catalog/caffeinelabs-extension-skills-setup/)
- [OpenCLI Skills — Agent CLI with Browser Automation Setup](/docs/hermes/skills/catalog/opencli-skills-setup/)
- [CMUX Skills — Agent Terminal Multiplexer Setup](/docs/hermes/skills/catalog/cmux-skills-setup/)
- [Agentix CEO Skill — AI Worker Team Orchestration Setup](/docs/hermes/skills/catalog/agentix-ceo-skill-setup/)
- [LiarJS Skills — Browser Fingerprint & Playwright Stealth Setup](/docs/hermes/skills/catalog/liarjs-fingerprint-skills-setup/)
- [Huashu Design Skill — HTML-First Agent Design Setup](/docs/hermes/skills/catalog/huashu-design-setup/)
- [Replicas Agent Skill — Cloud Workspace Coding Agent Setup](/docs/hermes/skills/catalog/replicas-agent-skill-setup/)
- [Design Doc Mermaid Skill — Diagram & Documentation Setup](/docs/hermes/skills/catalog/design-doc-mermaid-setup/)
- [Agent Pulse Skill — Local AI Agent Activity Monitor Setup](/docs/hermes/skills/catalog/agent-pulse-skill-setup/)
- [Academic Research Skills — Paper Pipeline for Agents Setup](/docs/hermes/skills/catalog/academic-research-skills-setup/)
- [Argent Skills — Mobile Dev Agent Toolkit Setup](/docs/hermes/skills/catalog/argent-mobile-agent-skills-setup/)
- [Oh Story ClaudeCode Skills — Long-Form Writing & Browser CDP Setup](/docs/hermes/skills/catalog/oh-story-claudecode-skills-setup/)
- [VueJS AI Skills — Vue Best Practices Suite Setup](/docs/hermes/skills/catalog/vuejs-ai-skills-setup/)
- [Rivet Skills — Real-Time Backend & Agent Infrastructure Setup](/docs/hermes/skills/catalog/rivet-dev-skills-setup/)
- [Interface Design Skill — Non-Templated Product UI Setup](/docs/hermes/skills/catalog/interface-design-skill-setup/)
- [Feature-Sliced Design Skill — Frontend Architecture Setup](/docs/hermes/skills/catalog/feature-sliced-design-skill-setup/)
- [RampStack Claude Skills — Growth & Marketing Suite Setup](/docs/hermes/skills/catalog/rampstack-claude-skills-setup/)
- [Tailwind 4 Docs Skill — Local Docs Snapshot Setup](/docs/hermes/skills/catalog/tailwind-4-docs-skill-setup/)
- [Claude Video Watch Skill — Agent Video Input Setup](/docs/hermes/skills/catalog/claude-video-watch-skill-setup/)
- [Tiangong AI Skills — Email & Research Data Fetching Suite Setup](/docs/hermes/skills/catalog/tiangong-ai-skills-setup/)
- [RKnall Claude Skills — SVG Logo & GitLab Stack Setup](/docs/hermes/skills/catalog/rknall-claude-skills-setup/)
- [Superdesign Skill — Canvas Design & Inspiration Setup](/docs/hermes/skills/catalog/superdesign-skill-setup/)
- [Design Motion Principles Skill — Motion & Interaction Setup](/docs/hermes/skills/catalog/design-motion-principles-skill-setup/)
- [Swift Testing Pro Skill — Swift Testing Suite Setup](/docs/hermes/skills/catalog/swift-testing-pro-skill-setup/)
- [Trail of Bits Skills Curated — Agent Security Suite Setup](/docs/hermes/skills/catalog/trailofbits-skills-curated-setup/)
- [Sentry Agent Skills — Security & Code Review Suite Setup](/docs/hermes/skills/catalog/sentry-agent-skills-setup/)
- [Three.js Agent Skills — 3D & WebGL Suite Setup](/docs/hermes/skills/catalog/threejs-agent-skills-setup/)
- [Emblem Company Agent Skills — Portfolio & Market Research Setup](/docs/hermes/skills/catalog/emblem-company-agent-skills-setup/)
- [CTF Security Skills — Offensive Security Suite Setup](/docs/hermes/skills/catalog/ctf-security-skills-setup/)
- [Bright Data Agent Skills — Web Scraping & Research Setup](/docs/hermes/skills/catalog/brightdata-agent-skills-setup/)
- [Claude Code Video Toolkit — Video Pipeline Skills Setup](/docs/hermes/skills/catalog/claude-code-video-toolkit-setup/)
- [Langfuse Agent Skills — LLM Observability Setup](/docs/hermes/skills/catalog/langfuse-agent-skills-setup/)
- [Deep Research Skill — Citation-Tracked Research Setup](/docs/hermes/skills/catalog/claude-deep-research-skill-setup/)
- [Mintlify Docs Skills — Documentation Platform Setup](/docs/hermes/skills/catalog/mintlify-docs-skills-setup/)
- [Motion Design Skill — LottieFiles Animation Setup](/docs/hermes/skills/catalog/lottiefiles-motion-design-skill-setup/)
- [Mobile App UI Design Skill — Mobile Interface Setup](/docs/hermes/skills/catalog/mobile-app-ui-design-skill-setup/)
- [Cursor Plugins Skills — Engineering Discipline Suite Setup](/docs/hermes/skills/catalog/cursor-plugins-skills-setup/)
- [Vercel AI SDK Skills — TypeScript AI Development Setup](/docs/hermes/skills/catalog/vercel-ai-skills-setup/)
- [Angular Skills — Framework Development Setup](/docs/hermes/skills/catalog/angular-skills-setup/)
- [Inngest Skills — Durable Workflow Orchestration Setup](/docs/hermes/skills/catalog/inngest-skills-setup/)
- [OXC Project Skills — Linter & Formatter Migration Setup](/docs/hermes/skills/catalog/oxc-project-skills-setup/)
- [Alibaba Open Code Review — AI Code Review CLI Setup](/docs/hermes/skills/catalog/alibaba-open-code-review-setup/)
- [Brian Lovin Agent Config — Design Engineering Suite Setup](/docs/hermes/skills/catalog/brianlovin-agent-config-setup/)
- [last30days Skill — Recent-Activity Research Setup](/docs/hermes/skills/catalog/last30days-skill-setup/)
- [Herdr Skills — Terminal Workspace Orchestration Setup](/docs/hermes/skills/catalog/herdr-skills-setup/)
- [Web Access Skill — Unified Browsing & Scraping Setup](/docs/hermes/skills/catalog/web-access-skill-setup/)
- [Stop Slop — AI-Prose Pattern Cleaner Setup](/docs/hermes/skills/catalog/stop-slop-setup/)
- [Avoid AI Writing — AI-Pattern Audit & Rewrite Setup](/docs/hermes/skills/catalog/avoid-ai-writing-setup/)
- [M. Collina Node Skills — Fastify & Node.js Agent Suite Setup](/docs/hermes/skills/catalog/mcollina-node-skills-setup/)
- [Zhaono1 Agent Playbook — 24-Role Agent Workflow Suite Setup](/docs/hermes/skills/catalog/zhaono1-agent-playbook-setup/)
- [Nx AI Agents Config — Monorepo Agent Skills Setup](/docs/hermes/skills/catalog/nx-ai-agents-config-skills-setup/)
- [WeCom CLI Skills — Enterprise WeChat Agent Suite Setup](/docs/hermes/skills/catalog/wecom-cli-skills-setup/)
- [WeCom Unified Skill — WeChat Work Routing Suite Setup](/docs/hermes/skills/catalog/wecom-unified-skills-setup/)
- [Mastra AI Skills — TypeScript Agent Framework Setup](/docs/hermes/skills/catalog/mastra-ai-skills-setup/)
- [Strix Security Skills — Autonomous Pentesting Suite Setup](/docs/hermes/skills/catalog/strix-security-skills-setup/)
- [Claude for Legal Skills — Anthropic Legal Workflow Suite Setup](/docs/hermes/skills/catalog/claude-for-legal-skills-setup/)
- [PCL Domain Expert Skills — 104 Persona Skill Pack Setup](/docs/hermes/skills/catalog/pcl-domain-expert-skills-setup/)
- [VTEX Skills — Commerce Platform Development Suite Setup](/docs/hermes/skills/catalog/vtex-skills-setup/)
- [Genshijin Skills — Japanese Concise-Reply Framework Setup](/docs/hermes/skills/catalog/genshijin-skills-setup/)
- [Hono Skill — Edge Web Framework Setup by the Hono Author](/docs/hermes/skills/catalog/hono-skill-setup/)
- [Capawesome Skills — Capacitor and Ionic Ecosystem Suite Setup](/docs/hermes/skills/catalog/capawesome-skills-setup/)
- [Wyatt Walsh Agents — Skill Governance and Orchestration Suite Setup](/docs/hermes/skills/catalog/wyattowalsh-agents-setup/)
- [Hermes Field Kit — Field-Tested Hermes Operations Skill Suite Setup](/docs/hermes/skills/catalog/hermes-field-kit-setup/)
- [AtlasOmnia Hermes Custom Pack — 60+ Skill Independent Pack Setup](/docs/hermes/skills/catalog/atlasomnia-hermes-custom-pack-setup/)
- [Buzz Skills — Hermes Agent on Nostr via Block's Buzz Setup](/docs/hermes/skills/catalog/buzz-skills-setup/)
- [design-review — Visual UI Audit & Fix Setup](/docs/hermes/skills/catalog/design-review-setup/)
- [Agentic Awesome Skills — 2,000+ Skill Catalog Setup](/docs/hermes/skills/catalog/agentic-awesome-skills-setup/)
