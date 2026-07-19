---
title: "Hermes Skills Catalog — Quality-Tiered Directory"
description: "Curated directory of community-validated Hermes agent skills. Quality tiers (Production/Beta/Community), starter pack, evaluation guide, and installation instructions. 456+ skills catalogued."
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

- [find-skills — Skill Discovery Tool Setup](/docs/hermes/skills/catalog/find-skills-setup.html)
- [skill-creator — Anthropic's Skill Creation Framework Setup](/docs/hermes/skills/catalog/skill-creator-setup.html)
- [remotion-best-practices — Video Production Setup](/docs/hermes/skills/catalog/remotion-best-practices-setup.html)
- [browser-act — Record-and-Replay Browser Automation Setup](/docs/hermes/skills/catalog/browser-act-setup.html)
- [firecrawl-workflows — Growth & Research Automation Setup](/docs/hermes/skills/catalog/firecrawl-workflows-setup.html)
- [Agent Browser — Vercel Labs CLI for AI Agents Setup](/docs/hermes/skills/catalog/agent-browser-setup.html)
- [Agent Flywheel Mega-Toolkit Setup Guide](/docs/hermes/skills/catalog/agent-flywheel-setup.html)
- [agent-sessions — macOS Agent Session Browser Setup](/docs/hermes/skills/catalog/agent-sessions-setup.html)
- [Agenthood Setup](/docs/hermes/skills/catalog/agenthood-setup.html)
- [Agentmint Skills Setup](/docs/hermes/skills/catalog/agentmint-skills-setup.html)
- [AgentMemory Setup — Persistent Memory for Hermes Agents](/docs/hermes/skills/catalog/agentmemory-setup.html)
- [Apify Agent Skills — Web Scraping for Hermes Setup](/docs/hermes/skills/catalog/apify-agent-skills-setup.html)
- [Apify Growth Skills — Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/docs/hermes/skills/catalog/apify-growth-skills-setup/index.html)
- [Apple Calendar Setup](/docs/hermes/skills/catalog/apple-calendar-setup.html)
- [Arxiv Setup](/docs/hermes/skills/catalog/arxiv-setup.html)
- [Ashima Setup](/docs/hermes/skills/catalog/ashima-setup/index.html)
- [Autolora Setup](/docs/hermes/skills/catalog/autolora-setup.html)
- [Awesome Copilot — MCP Server Generators & GitHub Automation Setup](/docs/hermes/skills/catalog/awesome-copilot-setup.html)
- [bb-browser-openclaw — Setup Guide](/docs/hermes/skills/catalog/bb-browser-openclaw-setup.html)
- [Blogwatcher — RSS/Atom Feed Monitoring for Hermes](/docs/hermes/skills/catalog/blogwatcher-setup.html)
- [Blueprint Orchestration Setup](/docs/hermes/skills/catalog/blueprint-orchestration-setup/index.html)
- [browser-harness Setup Guide](/docs/hermes/skills/catalog/browser-harness-setup/index.html)
- [Build Mcp Server Setup](/docs/hermes/skills/catalog/build-mcp-server-setup.html)
- [cinematic-scroll-skill — Scroll-Driven Website Builder Setup](/docs/hermes/skills/catalog/cinematic-scroll-skill-setup.html)
- [Claude Office Skills](/docs/hermes/skills/catalog/claude-office/index.html)
- [ClawDBot Feishu Suite Setup Guide](/docs/hermes/skills/catalog/clawdbot-feishu-setup.html)
- [Setup Guide: napoleond/clawdirect — Agent Self-Direction Framework (9K+ Installs)](/docs/hermes/skills/catalog/clawdirect-setup.html)
- [Setup Guide: steipete/clawdis — 14 OpenClaw Skills (37K+ Installs)](/docs/hermes/skills/catalog/clawdis-setup.html)
- [Setup Guide: cantinaxyz/clawdstrike — Agent Red-Team Security Testing (486 Installs)](/docs/hermes/skills/catalog/clawdstrike-setup.html)
- [ClawFu Skills — 175 Marketing Methodologies for AI Agents Setup](/docs/hermes/skills/catalog/clawfu-skills-setup.html)
- [Clawpilot Ecosystem Setup](/docs/hermes/skills/catalog/clawpilot-ecosystem-setup.html)
- [Clean Slate Setup](/docs/hermes/skills/catalog/clean-slate-setup.html)
- [Cli Anything Harnesses Setup](/docs/hermes/skills/catalog/cli-anything-harnesses-setup.html)
- [Cli Anything Hermes Setup](/docs/hermes/skills/catalog/cli-anything-hermes-setup.html)
- [Codex — Delegate Coding Tasks to OpenAI Codex CLI](/docs/hermes/skills/catalog/codex-setup.html)
- [Coding Posture Setup](/docs/hermes/skills/catalog/coding-posture-setup.html)
- [communication Skills](/docs/hermes/skills/catalog/communication/index.html)
- [Context Forge Rag Setup](/docs/hermes/skills/catalog/context-forge-rag-setup.html)
- [Cron Design Workflow Setup](/docs/hermes/skills/catalog/cron-design-workflow-setup.html)
- [Delegate Skills Setup](/docs/hermes/skills/catalog/delegate-skills-setup.html)
- [Design Judge Skills — Design Award Workflow Setup](/docs/hermes/skills/catalog/design-judge-skills-setup/index.html)
- [Distribute Skill To All Agents Setup](/docs/hermes/skills/catalog/distribute-skill-to-all-agents-setup.html)
- [elevenlabs Skills](/docs/hermes/skills/catalog/elevenlabs/index.html)
- [firebase Skills](/docs/hermes/skills/catalog/firebase/index.html)
- [firecrawl Skills](/docs/hermes/skills/catalog/firecrawl/index.html)
- [Gbrain Agent Operations Setup](/docs/hermes/skills/catalog/gbrain-agent-operations-setup.html)
- [Ghostwriter Setup](/docs/hermes/skills/catalog/ghostwriter-setup.html)
- [Google Workspace Skills](/docs/hermes/skills/catalog/google-workspace/index.html)
- [Halt Catch Fire Skills Setup](/docs/hermes/skills/catalog/halt-catch-fire-skills-setup.html)
- [Herman Skill Playbook Setup](/docs/hermes/skills/catalog/herman-skill-playbook-setup.html)
- [Hermes A2A Bridge Setup](/docs/hermes/skills/catalog/hermes-a2a-bridge-setup.html)
- [Hermes Advanced Memory Setup](/docs/hermes/skills/catalog/hermes-advanced-memory-setup.html)
- [AGEL-Comp Safety Framework — Setup Guide](/docs/hermes/skills/catalog/hermes-agel-comp-setup.html)
- [Hermes Agency Setup](/docs/hermes/skills/catalog/hermes-agency-setup.html)
- [Hermes Agentmesh Async Bus](/docs/hermes/skills/catalog/hermes-agentmesh-async-bus/index.html)
- [Hermes ArXiv Agent — ArXiv Paper Fetcher Setup](/docs/hermes/skills/catalog/hermes-arxiv-agent-setup.html)
- [Hermes Bible Skill Setup](/docs/hermes/skills/catalog/hermes-bible-skill-setup/index.html)
- [Hermes Browser Extension — Full Setup Guide](/docs/hermes/skills/catalog/hermes-browser-extension-setup/index.html)
- [Hermes Client Web Ui Setup](/docs/hermes/skills/catalog/hermes-client-web-ui-setup.html)
- [Hermes Cursor Dispatcher — Cursor CLI Delegation Setup](/docs/hermes/skills/catalog/hermes-cursor-dispatcher-setup/index.html)
- [Hermes Desktop Neo Theme — Setup Guide](/docs/hermes/skills/catalog/hermes-desktop-neo-theme-setup.html)
- [Hermes Engineering Curation Setup](/docs/hermes/skills/catalog/hermes-engineering-curation-setup.html)
- [Hermes Ershov Setup](/docs/hermes/skills/catalog/hermes-ershov-setup/index.html)
- [Hermes Flight Recorder Setup](/docs/hermes/skills/catalog/hermes-flight-recorder-setup.html)
- [Hermes Full Backup — Setup Guide](/docs/hermes/skills/catalog/hermes-full-backup-setup.html)
- [hermes-history-ingest Setup Guide](/docs/hermes/skills/catalog/hermes-history-ingest-setup/index.html)
- [Hermes Hybrid Memory — Full Setup Guide](/docs/hermes/skills/catalog/hermes-hybrid-memory-setup.html)
- [Hermes Memory Stack Setup](/docs/hermes/skills/catalog/hermes-memory-stack-setup.html)
- [Hermes Meshtastic Adapter — LoRa Mesh Integration Setup](/docs/hermes/skills/catalog/hermes-meshtastic-adapter-setup.html)
- [Hermes Obsidian Giveaway Pack Setup](/docs/hermes/skills/catalog/hermes-obsidian-giveaway-pack-setup.html)
- [Hermes Ponytail Setup](/docs/hermes/skills/catalog/hermes-ponytail-setup.html)
- [Hermes S6 Container Supervision Setup](/docs/hermes/skills/catalog/hermes-s6-container-supervision-setup.html)
- [Hermes Session Maintenance Setup](/docs/hermes/skills/catalog/hermes-session-maintenance-setup.html)
- [Hermes Skill Cleaner Setup](/docs/hermes/skills/catalog/hermes-skill-cleaner-setup.html)
- [hermes-top — Setup Guide](/docs/hermes/skills/catalog/hermes-top-setup.html)
- [Hermes Whatsapp Secretary Setup](/docs/hermes/skills/catalog/hermes-whatsapp-secretary-setup.html)
- [Hermes Windows Native](/docs/hermes/skills/catalog/hermes-windows-native/index.html)
- [Hermespace — Persistent Agent World Setup](/docs/hermes/skills/catalog/hermespace-setup/index.html)
- [Hermespet Macos Ai Companion Setup](/docs/hermes/skills/catalog/hermespet-macos-ai-companion-setup.html)
- [Hermex iPhone App — Setup Guide for Hermes Agent](/docs/hermes/skills/catalog/hermex-iphone-app-setup.html)
- [Honcho Integration Setup](/docs/hermes/skills/catalog/honcho-integration-setup.html)
- [Huawei Hermes Deployment Setup](/docs/hermes/skills/catalog/huawei-hermes-deployment-setup.html)
- [Humanizer Setup](/docs/hermes/skills/catalog/humanizer-setup.html)
- [Hyperframes Setup](/docs/hermes/skills/catalog/hyperframes-setup.html)
- [Idea Workflow Suite Setup](/docs/hermes/skills/catalog/idea-workflow-suite-setup.html)
- [Imap Smtp Email Setup](/docs/hermes/skills/catalog/imap-smtp-email-setup.html)
- [Impeccable Design Setup](/docs/hermes/skills/catalog/impeccable-design-setup.html)
- [Impeccable Setup](/docs/hermes/skills/catalog/impeccable-setup.html)
- [Inference Sh Skills Setup](/docs/hermes/skills/catalog/inference-sh-skills-setup.html)
- [infrastructure Skills](/docs/hermes/skills/catalog/infrastructure/index.html)
- [Jupyter Live Kernel Setup](/docs/hermes/skills/catalog/jupyter-live-kernel-setup.html)
- [Kanban Orchestrator Setup](/docs/hermes/skills/catalog/kanban-orchestrator-setup.html)
- [langgraph Skills](/docs/hermes/skills/catalog/langgraph/index.html)
- [Letta Ai Agent Harness Setup](/docs/hermes/skills/catalog/letta-ai-agent-harness-setup.html)
- [Linux Systemd Setup](/docs/hermes/skills/catalog/linux-systemd-setup.html)
- [Llm Ops Setup](/docs/hermes/skills/catalog/llm-ops-setup.html)
- [Loop Maker Setup](/docs/hermes/skills/catalog/loop-maker-setup.html)
- [Macos Computer Use Setup](/docs/hermes/skills/catalog/macos-computer-use-setup.html)
- [Macos Launchd Setup](/docs/hermes/skills/catalog/macos-launchd-setup.html)
- [Math Via Code Setup](/docs/hermes/skills/catalog/math-via-code-setup.html)
- [Matt Pocock Engineering Skills — Setup Guide for Hermes Agents](/docs/hermes/skills/catalog/matt-pocock-engineering-setup/index.html)
- [Mattpocock Skills Setup](/docs/hermes/skills/catalog/mattpocock-skills-setup.html)
- [MCP Use Setup — Fullstack MCP Framework for Hermes](/docs/hermes/skills/catalog/mcp-use-setup.html)
- [memoria-vault — Multi-Agent Research OS for Obsidian Setup](/docs/hermes/skills/catalog/memoria-vault-setup.html)
- [Memory Hygiene Setup](/docs/hermes/skills/catalog/memory-hygiene-setup.html)
- [Memory Merger Setup — Agent Session Memory Consolidation](/docs/hermes/skills/catalog/memory-merger-setup.html)
- [Metamask Openclaw Security Analysis Setup](/docs/hermes/skills/catalog/metamask-openclaw-security-analysis-setup.html)
- [Native Mcp Setup](/docs/hermes/skills/catalog/native-mcp-setup.html)
- [Nemoclaw User Guide Setup](/docs/hermes/skills/catalog/nemoclaw-user-guide-setup.html)
- [OpenClaw on Android — Full Setup Guide](/docs/hermes/skills/catalog/openclaw-android-setup/index.html)
- [OpenClaw Audit Watchdog — Setup Guide](/docs/hermes/skills/catalog/openclaw-audit-watchdog-setup.html)
- [Openclaw Auto Updater Setup](/docs/hermes/skills/catalog/openclaw-auto-updater-setup.html)
- [Openclaw Customizer Setup](/docs/hermes/skills/catalog/openclaw-customizer-setup.html)
- [Openclaw Ecosystem June26 Setup](/docs/hermes/skills/catalog/openclaw-ecosystem-june26-setup.html)
- [Openclaw Grok Search Setup](/docs/hermes/skills/catalog/openclaw-grok-search-setup.html)
- [openclaw-history-ingest Setup Guide](/docs/hermes/skills/catalog/openclaw-history-ingest-setup/index.html)
- [OpenClaw Marketing Skills — Setup Guide](/docs/hermes/skills/catalog/openclaw-marketing-skills-setup.html)
- [Openclaw Secure Linux Cloud Setup](/docs/hermes/skills/catalog/openclaw-secure-linux-cloud-setup.html)
- [Openclaw Security Hardening Setup](/docs/hermes/skills/catalog/openclaw-security-hardening-setup.html)
- [Openclaw Skill Vetter Setup](/docs/hermes/skills/catalog/openclaw-skill-vetter-setup.html)
- [OpenClaw XHS Setup — Xiaohongshu (RED) Integration](/docs/hermes/skills/catalog/openclaw-xhs-setup.html)
- [Parallel Agent Skills — Web Intelligence for Hermes Setup](/docs/hermes/skills/catalog/parallel-agent-skills-setup.html)
- [Perfectloop Setup](/docs/hermes/skills/catalog/perfectloop-setup.html)
- [Petdex — Animated Mascots for Hermes Agent](/docs/hermes/skills/catalog/petdex-setup.html)
- [platform Skills](/docs/hermes/skills/catalog/platform/index.html)
- [prisma Skills](/docs/hermes/skills/catalog/prisma/index.html)
- [Safari Web Agent Setup](/docs/hermes/skills/catalog/safari-web-agent-setup.html)
- [Security Hardening — AI Agent Security Setup](/docs/hermes/skills/catalog/security-and-hardening-setup/index.html)
- [Sentry AI Monitoring — Agent Error Tracking Setup](/docs/hermes/skills/catalog/sentry-ai-monitoring-setup/index.html)
- [Sg Arrival Card Setup](/docs/hermes/skills/catalog/sg-arrival-card-setup.html)
- [shopify Skills](/docs/hermes/skills/catalog/shopify/index.html)
- [Skill Repo Manager Setup](/docs/hermes/skills/catalog/skill-repo-manager-setup.html)
- [Skill Vetting Setup](/docs/hermes/skills/catalog/skill-vetting-setup.html)
- [Skills Gallery Setup](/docs/hermes/skills/catalog/skills-gallery-setup.html)
- [Soul Grader Setup](/docs/hermes/skills/catalog/soul-grader-setup.html)
- [Spike Setup](/docs/hermes/skills/catalog/spike-setup.html)
- [Stepfun Skills Setup](/docs/hermes/skills/catalog/stepfun-skills-setup.html)
- [Steroids Openai Image Gen Setup](/docs/hermes/skills/catalog/steroids-openai-image-gen-setup/index.html)
- [stripe Skills](/docs/hermes/skills/catalog/stripe/index.html)
- [supabase Skills](/docs/hermes/skills/catalog/supabase/index.html)
- [Tavily Search Openclaw Setup](/docs/hermes/skills/catalog/tavily-search-openclaw-setup.html)
- [Threads Growth Skill Setup](/docs/hermes/skills/catalog/threads-growth-skill-setup.html)
- [Three Agent Bridge Setup](/docs/hermes/skills/catalog/three-agent-bridge-setup.html)
- [Timesfm Forecasting Setup](/docs/hermes/skills/catalog/timesfm-forecasting-setup/index.html)
- [Trailofbits Security Setup](/docs/hermes/skills/catalog/trailofbits-security-setup.html)
- [Ultimate Humanizer Setup](/docs/hermes/skills/catalog/ultimate-humanizer-setup.html)
- [Vercel Agent Skills — Official Vercel Collection Setup](/docs/hermes/skills/catalog/vercel-agent-skills-setup.html)
- [Vps Server Management Setup](/docs/hermes/skills/catalog/vps-server-management-setup/index.html)
- [Wiki History Ingest Setup](/docs/hermes/skills/catalog/wiki-history-ingest-setup/index.html)
- [Writing Plans Subagent Development Setup](/docs/hermes/skills/catalog/writing-plans-subagent-development-setup.html)
- [wshobson/agents — Agent Plugin Marketplace Setup](/docs/hermes/skills/catalog/wshobson-agents-setup.html)
- [X Twitter Scraper Setup](/docs/hermes/skills/catalog/x-twitter-scraper-setup.html)
- [Xurl Setup](/docs/hermes/skills/catalog/xurl-setup/index.html)
- [Youtube Content Setup](/docs/hermes/skills/catalog/youtube-content-setup.html)
