---
title: "Hermes Skills Catalog - Quality-Tiered Directory"
description: "Curated directory of community-validated Hermes agent skills. Quality tiers (Production/Beta/Community), starter pack, evaluation guide, and installation"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Skills Catalog

Welcome to the Hermes Skills Catalog - your directory of community-contributed, validated skills that extend what Hermes can do. Skills encode repeatable expertise into shareable packages that anyone in the Hermes community can install and use.

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

These skills are suitable for supervised use. They'll save you time but keep an eye on them - especially in the first few runs. Look for the 🟡 indicator.

### Community Tier 🔵

Community-tier skills are shared in good faith but haven't completed formal validation:

- Published by a community member
- May have been tested only on the author's setup
- Documentation may be minimal
- Error handling may be incomplete
- Best suited for learning, inspiration, and adaptation - not production reliance

These skills are valuable for the community but require due diligence before relying on them. Look for the 🔵 indicator.

| [RunComfy Agent Skills](/hermes/skills/catalog/runcomfy-agent-skills-setup) | 🟡 Beta | 30 | 61.1K | AI video, image-to-video, avatar video, video editing, music generation | `prime-skills/runcomfy-agent-skills` |

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
**What it does:** Your morning dashboard - calendar, priority emails, task list, and key metrics from connected services. One invocation replaces five separate checks.  
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
**What it does:** Aggregates activity from your connected services into a structured weekly summary - tasks completed, meetings attended, key communications, metrics trends.  
**Needs:** Project management, calendar, email (configurable).  
**Why start here:** Automates the Friday afternoon ritual. Customize the template to match your team's format.

### 5. CRM Health Check
**What it does:** Pipeline analysis, stale deals, overdue follow-ups, and contact engagement scoring. Flags accounts that need attention.  
**Needs:** CRM connector (HubSpot, Salesforce, or similar).  
**Why start here:** Your CRM has data but Hermes turns it into action items.

### 6. Data to Chart
**What it does:** Takes a dataset (from any connector or upload) and generates appropriate visualizations - time series, distribution, comparison, correlation.  
**Needs:** Any data source (accepts structured data from other skills).  
**Why start here:** Visual insight without spreadsheet wrestling.

### 7. Content Drafting Assistant
**What it does:** Drafts blog posts, social media updates, newsletters, and other content following your brand voice. Includes tone calibration and audience targeting.  
**Needs:** No specific connectors (optionally integrates with CMS or social platforms).  
**Why start here:** Beat the blank page. All output is draft - you remain the editor.

### 8. Code Review Companion
**What it does:** Reviews code changes for bugs, security issues, style consistency, and documentation completeness. Provides actionable, specific feedback.  
**Needs:** File access or repository connector.  
**Why start here:** A second pair of eyes on every PR, catching issues before humans spend time reviewing.

### 9. Travel Planner
**What it does:** Given destination and dates, gathers flight options, hotel availability, weather forecasts, and local information. Organizes into a comparison view.  
**Needs:** Calendar (for availability context).  
**Why start here:** Research acceleration - you still book, but Hermes does the hunting.

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

1. Follow the [skill development best practices](../../best-practices/skill-development)
2. Test thoroughly in your environment
3. Document setup, invocation, and expected output
4. Remove environment-specific values (use placeholders)
5. Submit through the catalog contribution process

Skills are reviewed by community maintainers before publication. The review checks for documentation completeness, error handling, security considerations, and community value - not whether every edge case is handled (that's what quality tiers communicate).

## Finding More Skills

The catalog here represents community-validated skills. Additional skills are discoverable through:

- **[skills.sh](https://skills.sh)** - Large open marketplace
- **[agentskills.io](https://agentskills.io)** - Curated premium and community skills
- **[hermeshub](https://hermeshub.nousresearch.com)** - Official Hermes skill registry
- **[skilldock.io](https://skilldock.io)** - Enterprise-focused skill marketplace
- **GitHub** - Search for "hermes-skill" or "hermes-skill-" prefixed repositories

See [Skill Marketplaces](../skill-marketplaces) for detailed guidance on each marketplace.

The catalog is a living resource. Skills are added weekly. Check back often, and consider contributing what you build.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*


## All Skills Catalog Pages

### New - September 30, 2026 Sweep (8 publisher guides)

- [Assistant UI Skills - AI Chat Interface Dev Suite Setup](/hermes/skills/catalog/assistant-ui-skills-setup)
- [Claude MPM Skills - 96-Skill Dev Toolchain Collection Setup - Setup Guide](/hermes/skills/catalog/claude-mpm-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Gemini Skills - Official Google AI Development Suite Setup](/hermes/skills/catalog/gemini-skills-setup)
- [Harmony Next Skills - Setup Guide](/hermes/skills/catalog/harmony-next-skills-setup)
- [James Rochabrun Skills - Setup Guide](/hermes/skills/catalog/jamesrochabrun-skills-setup)
- [Meta Quest Agentic Tools - Horizon OS VR Dev Suite Setup](/hermes/skills/catalog/meta-quest-agentic-tools-setup)
- [Skill From Masters - Domain Expert Methodology Suite Setup - Setup Guide](/hermes/skills/catalog/skill-from-masters-setup)

### New - September 29, 2026 Sweep (64 publisher guides)

- [AAHL Skills - Smart Home & TTS Setup](/hermes/skills/catalog/aahl-skills-setup)
- [Open WebSearch Skills - Agent Web Search Setup](/hermes/skills/catalog/open-websearch-setup)
- [Actionbook Rust Skills - Rust Guidelines Setup](/hermes/skills/catalog/actionbook-rust-skills-setup)
- [Aktsmm Agent Skills - Copilot & Claude Setup](/hermes/skills/catalog/aktsmm-agent-skills-setup)
- [OpenClaw Token Optimizer Skills Setup](/hermes/skills/catalog/openclaw-token-optimizer-setup)
- [Bagelhole DevOps Security Skills Setup](/hermes/skills/catalog/bagelhole-devops-security-skills-setup)
- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)
- [Boshu2 AgentOps Skills - AI Coding Ops Setup](/hermes/skills/catalog/boshu2-agentops-setup)
- [Celigo AI Skills - Celigo Integrations Setup](/hermes/skills/catalog/celigo-ai-skills-setup)
- [CodeStable Skills - AI Coding Workflow Setup](/hermes/skills/catalog/codestable-skills-setup)
- [Coleam00 Skills - PIV Loop & AI Layer Setup](/hermes/skills/catalog/coleam00-skills-setup)
- [CopilotKit Skills - Agent Frontend Stack Setup](/hermes/skills/catalog/copilotkit-copilotkit-skills-setup)
- [CopilotKit Skills - Dev Lifecycle Setup](/hermes/skills/catalog/copilotkit-skills-setup)
- [AI Dev Standards Skills - Design Setup](/hermes/skills/catalog/ai-dev-standards-skills-setup)
- [Decentraland SDK Skills - Scene Building Setup](/hermes/skills/catalog/decentraland-sdk-skills-setup)
- [Openwork Skills - Agent Workspace Setup](/hermes/skills/catalog/openwork-skills-setup)
- [Helmor Skills - Multi-Agent Workbench Setup](/hermes/skills/catalog/helmor-skills-setup)
- [Dotnet Skills - .NET AI Coding Setup](/hermes/skills/catalog/dotnet-skills-setup)
- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)
- [Dzhng Skills - Software Factory Setup](/hermes/skills/catalog/dzhng-skills-setup)
- [Eachlabs Skills - Creative Generation Setup](/hermes/skills/catalog/eachlabs-skills-setup)
- [Flightclaw Skills - Flight Agent Setup](/hermes/skills/catalog/flightclaw-agents-setup)
- [Frames Engineering Skills - Agent Tools Setup](/hermes/skills/catalog/frames-engineering-skills-setup)
- [Gemini Watermark Remover Skills Setup](/hermes/skills/catalog/gemini-watermark-remover-setup)
- [Taches CC Resources Skills - Claude Tools Setup](/hermes/skills/catalog/taches-cc-resources-setup)
- [Google Antigravity SDK Skills Setup](/hermes/skills/catalog/google-antigravity-sdk-setup)
- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup)
- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [Hedera Skills - Web3 Dev Tools Setup](/hermes/skills/catalog/hedera-skills-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)
- [Open Browser Use Skills - Browser Automation Setup](/hermes/skills/catalog/open-browser-use-setup)
- [Open Computer Use Skills - Codex Alternative Setup](/hermes/skills/catalog/open-computer-use-setup)
- [Jeff Allan Claude Skills - Full-Stack Dev Setup](/hermes/skills/catalog/jeffallan-claude-skills-setup)
- [Finance Skills - Financial Services Suite Setup](/hermes/skills/catalog/joellewis-finance-skills-setup)
- [Spellbook Skills - Cross-Runtime Setup](/hermes/skills/catalog/majiayu000-spellbook-setup)
- [Claude GTM Plugin Skills - GTM Teams Setup](/hermes/skills/catalog/claude-gtm-plugin-setup)
- [Luxor Claude Marketplace Skills Setup](/hermes/skills/catalog/luxor-claude-marketplace-setup)
- [Marimo Skills - Notebook Agents Setup](/hermes/skills/catalog/marimo-skills-setup)
- [Claude Skills Generator - Coding Setup](/hermes/skills/catalog/claude-skills-generator-setup)
- [Ant Design Skills - Official antd Agent Suite Setup](/hermes/skills/catalog/ant-design-skills-setup)
- [AntiGravity Lazy Pack Skills Setup](/hermes/skills/catalog/antigravity-lazy-pack-setup)
- [Microsoft Learn MCP Skills Setup](/hermes/skills/catalog/microsoft-learn-mcp-skills-setup)
- [Mindrally Skills - 255+ Coding Setup](/hermes/skills/catalog/mindrally-skills-setup)
- [Mosif16 Codex Skills - iOS Design Setup](/hermes/skills/catalog/mosif16-codex-skills-setup)
- [Context Engineering Skills Setup](/hermes/skills/catalog/context-engineering-skills-setup)
- [K-Skill - Korean Agent Skills Setup](/hermes/skills/catalog/k-skill-setup)
- [OKX OnchainOS Skills - Wallet & DEX Setup](/hermes/skills/catalog/okx-onchainos-skills-setup)
- [OKX CEX Agent Skills - Exchange Trading Suite Setup](/hermes/skills/catalog/okx-cex-agent-skills-setup)
- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)
- [PluggyAI Agent Skills - Open Finance Setup](/hermes/skills/catalog/pluggyai-agent-skills-setup)
- [Amplihack Skills - Agentic Coding Setup](/hermes/skills/catalog/amplihack-setup)
- [FreeRide Skill - Free AI for OpenClaw Setup](/hermes/skills/catalog/freeride-setup)
- [somasays Skill Creator - Claude Skills Setup](/hermes/skills/catalog/somasays-skill-creator-setup)
- [Awesome Cursor Skills - Cursor Agent Setup](/hermes/skills/catalog/awesome-cursor-skills-setup)
- [Tech Leads Club Skills - Secure Registry Setup](/hermes/skills/catalog/tech-leads-club-skills-setup)
- [GD Agentic Skills - Godot 4 Agent Setup](/hermes/skills/catalog/gd-agentic-skills-setup)
- [OpenUI Skill - Generative UI Setup](/hermes/skills/catalog/openui-setup)
- [travisjneuman Claude Toolkit Skills Setup](/hermes/skills/catalog/travisjneuman-claude-toolkit-setup)
- [Upstash Skills - Serverless Backend Setup](/hermes/skills/catalog/upstash-skills-setup)
- [OpenViking Skills - Agent Context Database Setup](/hermes/skills/catalog/openviking-setup)
- [AI Berkshire Skills - Value Investing Setup](/hermes/skills/catalog/ai-berkshire-setup)
- [Phaser 4 GameDev Skills Setup](/hermes/skills/catalog/phaser4-gamedev-setup)
- [Nature Skills - Academic Writing Setup](/hermes/skills/catalog/nature-skills-setup)
- [Agent Email CLI Skill Setup](/hermes/skills/catalog/agent-email-cli-setup)
- [Marketing Skills - Content Ops Setup](/hermes/skills/catalog/zc277584121-marketing-skills-setup)
- [Claw Multi-Agent Skill Setup](/hermes/skills/catalog/claw-multi-agent-setup)
- [Ziniao Skills - ERP and Store Automation Setup](/hermes/skills/catalog/ziniao-open-skills-setup)


- [find-skills - Skill Discovery Tool Setup](/hermes/skills/catalog/find-skills-setup)
- [skill-creator - Anthropic's Skill Creation Framework Setup](/hermes/skills/catalog/skill-creator-setup)
- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [browser-act - Record-and-Replay Browser Automation Setup](/hermes/skills/catalog/browser-act-setup)
- [firecrawl-workflows - Growth & Research Automation Setup](/hermes/skills/catalog/firecrawl-workflows-setup)
- [Firecrawl Agent - AI-Powered Structured Data Extraction Setup](/hermes/skills/catalog/firecrawl-agent-setup)
- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [Agent Flywheel Mega-Toolkit Setup Guide](/hermes/skills/catalog/agent-flywheel-setup)
- [agent-sessions - macOS Agent Session Browser Setup](/hermes/skills/catalog/agent-sessions-setup)
- [Agenthood Setup](/hermes/skills/catalog/agenthood-setup)
- [Agentmint Skills Setup](/hermes/skills/catalog/agentmint-skills-setup)
- [AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup)
- [Alibaba Cloud AIOps Skills - 270-Skill Cloud Operations Suite Setup](/hermes/skills/catalog/alibaba-cloud-aiops-skills-setup)
- [Alireza Rezvani Claude Skills - 341 Engineering & Marketing Skills Setup](/hermes/skills/catalog/alirezarezvani-claude-skills-setup)
- [Antigravity Manager - Multi-Account LLM Proxy & Rotation Setup](/hermes/skills/catalog/antigravity-manager-setup)
- [Apify Agent Skills - Web Scraping for Hermes Setup](/hermes/skills/catalog/apify-agent-skills-setup)
- [Apify Growth Skills - Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/hermes/skills/catalog/apify-growth-skills-setup)
- [Apify Ultimate Scraper - Universal Web Scraping for 15+ Platforms Setup](/hermes/skills/catalog/apify-ultimate-scraper-setup)
- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup)
- [Apidojo Agent Skills - 100-Skill Social & Market Data Extraction Setup](/hermes/skills/catalog/apidojo-agent-skills-setup)
- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Apple Calendar Setup](/hermes/skills/catalog/apple-calendar-setup)
- [Arxiv Setup](/hermes/skills/catalog/arxiv-setup)
- [Ashima Setup](/hermes/skills/catalog/ashima-setup)
- [Autolora Setup](/hermes/skills/catalog/autolora-setup)
- [Awesome Copilot - MCP Server Generators & GitHub Automation Setup](/hermes/skills/catalog/awesome-copilot-setup)
- [bb-browser-openclaw - Setup Guide](/hermes/skills/catalog/bb-browser-openclaw-setup)
- [Blacktwist Social Media Skills - 14-Skill Content Suite Setup](/hermes/skills/catalog/blacktwist-social-media-skills-setup)
- [Blogwatcher - RSS/Atom Feed Monitoring for Hermes](/hermes/skills/catalog/blogwatcher-setup)
- [Blueprint Orchestration Setup](/hermes/skills/catalog/blueprint-orchestration-setup)
- [browser-harness Setup Guide](/hermes/skills/catalog/browser-harness-setup)
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)
- [cinematic-scroll-skill - Scroll-Driven Website Builder Setup](/hermes/skills/catalog/cinematic-scroll-skill-setup)
- [Charlie Hills Social Media Skills - 17-Skill Content System Setup](/hermes/skills/catalog/charlie-hills-social-media-skills-setup)
- [Claude Office Skills](/hermes/skills/catalog/claude-office)
- [ClawDBot Feishu Suite Setup Guide](/hermes/skills/catalog/clawdbot-feishu-setup)
- [Setup Guide: napoleond/clawdirect - Agent Self-Direction Framework (9K+ Installs)](/hermes/skills/catalog/clawdirect-setup)
- [Setup Guide: steipete/clawdis - 14 OpenClaw Skills (37K+ Installs)](/hermes/skills/catalog/clawdis-setup)
- [Setup Guide: cantinaxyz/clawdstrike - Agent Red-Team Security Testing (486 Installs)](/hermes/skills/catalog/clawdstrike-setup)
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup)
- [Clawpilot Ecosystem Setup](/hermes/skills/catalog/clawpilot-ecosystem-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Claude Handoff - Session Handoff Pattern Setup](/hermes/skills/catalog/claude-handoff-setup)
- [Claude SEO - 31-Skill Universal SEO Suite Setup](/hermes/skills/catalog/claude-seo-setup)
- [Clean Slate Setup](/hermes/skills/catalog/clean-slate-setup)
- [Clerk Auth Skills - Authentication & User Management Setup](/hermes/skills/catalog/clerk-auth-skills-setup)
- [Cli Anything Harnesses Setup](/hermes/skills/catalog/cli-anything-harnesses-setup)
- [Cli Anything Hermes Setup](/hermes/skills/catalog/cli-anything-hermes-setup)
- [Cline Skills - Official Cline 43-Skill Collection Setup](/hermes/skills/catalog/cline-skills-setup)
- [Codex - Delegate Coding Tasks to OpenAI Codex CLI](/hermes/skills/catalog/codex-setup)
- [Coding Posture Setup](/hermes/skills/catalog/coding-posture-setup)
- [Chrome DevTools MCP Skills - Browser Debugging & Automation Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup)
- [communication Skills](/hermes/skills/catalog/communication)
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup)
- [Context Forge Rag Setup](/hermes/skills/catalog/context-forge-rag-setup)
- [Cron Design Workflow Setup](/hermes/skills/catalog/cron-design-workflow-setup)
- [Deep Agents Memory - LangChain Persistent Memory Setup](/hermes/skills/catalog/deep-agents-memory-setup)
- [Delegate Skills Setup](/hermes/skills/catalog/delegate-skills-setup)
- [Design Judge Skills - Design Award Workflow Setup](/hermes/skills/catalog/design-judge-skills-setup)
- [Distribute Skill To All Agents Setup](/hermes/skills/catalog/distribute-skill-to-all-agents-setup)
- [Dogfood - Systematic QA Testing Setup](/hermes/skills/catalog/dogfood-setup)
- [elevenlabs Skills](/hermes/skills/catalog/elevenlabs)
- [firebase Skills](/hermes/skills/catalog/firebase)
- [firecrawl Skills](/hermes/skills/catalog/firecrawl)
- [Gbrain Agent Operations Setup](/hermes/skills/catalog/gbrain-agent-operations-setup)
- [Ghostwriter Setup](/hermes/skills/catalog/ghostwriter-setup)
- [Guizang Social Card Skill - Social Card Generation Setup](/hermes/skills/catalog/guizang-social-card-skill-setup)
- [Google Workspace Skills](/hermes/skills/catalog/google-workspace)
- [Halt Catch Fire Skills Setup](/hermes/skills/catalog/halt-catch-fire-skills-setup)
- [Herman Skill Playbook Setup](/hermes/skills/catalog/herman-skill-playbook-setup)
- [Hermes A2A Bridge Setup](/hermes/skills/catalog/hermes-a2a-bridge-setup)
- [Hermes Advanced Memory Setup](/hermes/skills/catalog/hermes-advanced-memory-setup)
- [Hermes Agent Core - Official Skill Setup Guide](/hermes/skills/catalog/hermes-agent-setup)
- [Hermes Agent Self-Evolution - Auto-Learning Framework Setup](/hermes/skills/catalog/hermes-agent-self-evolution-setup)
- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)
- [AGEL-Comp Safety Framework - Setup Guide](/hermes/skills/catalog/hermes-agel-comp-setup)
- [Hermes Agency Setup](/hermes/skills/catalog/hermes-agency-setup)
- [Hermes Agentmesh Async Bus](/hermes/skills/catalog/hermes-agentmesh-async-bus)
- [Hermes ArXiv Agent - ArXiv Paper Fetcher Setup](/hermes/skills/catalog/hermes-arxiv-agent-setup)
- [Hermes Bible Skill Setup](/hermes/skills/catalog/hermes-bible-skill-setup)
- [Hermes Browser Extension - Full Setup Guide](/hermes/skills/catalog/hermes-browser-extension-setup)
- [Hermes Client Web Ui Setup](/hermes/skills/catalog/hermes-client-web-ui-setup)
- [Hermes Cursor Dispatcher - Cursor CLI Delegation Setup](/hermes/skills/catalog/hermes-cursor-dispatcher-setup)
- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup)
- [Hermes Desktop Neo Theme - Setup Guide](/hermes/skills/catalog/hermes-desktop-neo-theme-setup)
- [Hermes Engineering Curation Setup](/hermes/skills/catalog/hermes-engineering-curation-setup)
- [Hermes Ershov Setup](/hermes/skills/catalog/hermes-ershov-setup)
- [Hermes Flight Recorder Setup](/hermes/skills/catalog/hermes-flight-recorder-setup)
- [Hermes Full Backup - Setup Guide](/hermes/skills/catalog/hermes-full-backup-setup)
- [hermes-history-ingest Setup Guide](/hermes/skills/catalog/hermes-history-ingest-setup)
- [Hermes Hybrid Memory - Full Setup Guide](/hermes/skills/catalog/hermes-hybrid-memory-setup)
- [Hermes Imports - Workflow Sanitization & Export Setup](/hermes/skills/catalog/hermes-imports-setup)
- [Hermes Labyrinth - Observability Dashboard Plugin for Hermes Agent](/hermes/skills/catalog/hermes-labyrinth-observability-setup)
- [Hermes Marketing Dashboard - AI Agent Marketing Ops Setup](/hermes/skills/catalog/hermes-marketing-dashboard-setup)
- [Hermes Memory Stack Setup](/hermes/skills/catalog/hermes-memory-stack-setup)
- [Hermes Meshtastic Adapter - LoRa Mesh Integration Setup](/hermes/skills/catalog/hermes-meshtastic-adapter-setup)
- [Hermes Obsidian Giveaway Pack Setup](/hermes/skills/catalog/hermes-obsidian-giveaway-pack-setup)
- [Hermes Ponytail Setup](/hermes/skills/catalog/hermes-ponytail-setup)
- [Hermes S6 Container Supervision Setup](/hermes/skills/catalog/hermes-s6-container-supervision-setup)
- [Hermes Session Maintenance Setup](/hermes/skills/catalog/hermes-session-maintenance-setup)
- [Hermes Skill Cleaner Setup](/hermes/skills/catalog/hermes-skill-cleaner-setup)
- [hermes-top - Setup Guide](/hermes/skills/catalog/hermes-top-setup)
- [Hermes Whatsapp Secretary Setup](/hermes/skills/catalog/hermes-whatsapp-secretary-setup)
- [Hermes Windows Native](/hermes/skills/catalog/hermes-windows-native)
- [Hermespace - Persistent Agent World Setup](/hermes/skills/catalog/hermespace-setup)
- [Hermespet Macos Ai Companion Setup](/hermes/skills/catalog/hermespet-macos-ai-companion-setup)
- [Hermex iPhone App - Setup Guide for Hermes Agent](/hermes/skills/catalog/hermex-iphone-app-setup)
- [Honcho Integration Setup](/hermes/skills/catalog/honcho-integration-setup)
- [Huawei Hermes Deployment Setup](/hermes/skills/catalog/huawei-hermes-deployment-setup)
- [HuggingFace Agent Skills - Datasets, Papers, ML Tools Setup](/hermes/skills/catalog/huggingface-agent-skills-setup)
- [Humanizer Setup](/hermes/skills/catalog/humanizer-setup)
- [Hyperframes Setup](/hermes/skills/catalog/hyperframes-setup)
- [Idea Workflow Suite Setup](/hermes/skills/catalog/idea-workflow-suite-setup)
- [Imap Smtp Email Setup](/hermes/skills/catalog/imap-smtp-email-setup)
- [Impeccable Design Setup](/hermes/skills/catalog/impeccable-design-setup)
- [Impeccable Setup](/hermes/skills/catalog/impeccable-setup)
- [Inference Sh Skills Setup](/hermes/skills/catalog/inference-sh-skills-setup)
- [infrastructure Skills](/hermes/skills/catalog/infrastructure)
- [Jupyter Live Kernel Setup](/hermes/skills/catalog/jupyter-live-kernel-setup)
- [Kanban Orchestrator Setup](/hermes/skills/catalog/kanban-orchestrator-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)
- [LangChain Agent Skills - Memory, RAG, Persistence & Middleware Setup](/hermes/skills/catalog/langchain-skills-setup)
- [langgraph Skills](/hermes/skills/catalog/langgraph)
- [LaunchDarkly Agent Skills - Feature Flags & AgentControl Setup](/hermes/skills/catalog/launchdarkly-agent-skills-setup)
- [Letta Ai Agent Harness Setup](/hermes/skills/catalog/letta-ai-agent-harness-setup)
- [Linux Systemd Setup](/hermes/skills/catalog/linux-systemd-setup)
- [Llm Ops Setup](/hermes/skills/catalog/llm-ops-setup)
- [Loop Maker Setup](/hermes/skills/catalog/loop-maker-setup)
- [Macos Computer Use Setup](/hermes/skills/catalog/macos-computer-use-setup)
- [Macos Launchd Setup](/hermes/skills/catalog/macos-launchd-setup)
- [Math Via Code Setup](/hermes/skills/catalog/math-via-code-setup)
- [Matt Pocock Engineering Skills - Setup Guide for Hermes Agents](/hermes/skills/catalog/matt-pocock-engineering-setup)
- [Mattpocock Skills Setup](/hermes/skills/catalog/mattpocock-skills-setup)
- [codebase-design - Deep Module Design Vocabulary Setup](/hermes/skills/catalog/codebase-design-setup)
- [Resolving Merge Conflicts - Matt Pocock Merge Protocol Setup](/hermes/skills/catalog/resolving-merge-conflicts-setup)
- [Matt Pocock Agent Workflow Suite - 20-Skill Setup](/hermes/skills/catalog/mattpocock-agent-workflow-suite-setup)
- [impeccable-design-polish - Post-Generation Design Polish Setup](/hermes/skills/catalog/impeccable-design-polish-setup)
- [MCP Use Setup - Fullstack MCP Framework for Hermes](/hermes/skills/catalog/mcp-use-setup)
- [Monitoring Expert - Observability & Monitoring Setup](/hermes/skills/catalog/monitoring-expert-setup)
- [memoria-vault - Multi-Agent Research OS for Obsidian Setup](/hermes/skills/catalog/memoria-vault-setup)
- [Memory Hygiene Setup](/hermes/skills/catalog/memory-hygiene-setup)
- [Memory Merger Setup - Agent Session Memory Consolidation](/hermes/skills/catalog/memory-merger-setup)
- [Media Use Setup - Agent Media OS for HyperFrames (182.7K installs)](/hermes/skills/catalog/media-use-setup)
- [Metamask Openclaw Security Analysis Setup](/hermes/skills/catalog/metamask-openclaw-security-analysis-setup)
- [Native Mcp Setup](/hermes/skills/catalog/native-mcp-setup)
- [Nemoclaw User Guide Setup](/hermes/skills/catalog/nemoclaw-user-guide-setup)
- [Netlify Agent Skills - Serverless Deployment for Hermes Setup](/hermes/skills/catalog/netlify-agent-skills-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [OpenClaw Agent Skills - Official OpenClaw Org Skill Suite Setup](/hermes/skills/catalog/openclaw-agent-skills-setup)
- [OpenClaw on Android - Full Setup Guide](/hermes/skills/catalog/openclaw-android-setup)
- [OpenClaw Audit Watchdog - Setup Guide](/hermes/skills/catalog/openclaw-audit-watchdog-setup)
- [Openclaw Auto Updater Setup](/hermes/skills/catalog/openclaw-auto-updater-setup)
- [OpenClaw Backup - Encrypted Agent Workspace Backup Setup](/hermes/skills/catalog/openclaw-backup-setup)
- [OpenClaw Control Center - Agent Monitoring Dashboard for OpenClaw](/hermes/skills/catalog/openclaw-control-center-setup)
- [Openclaw Customizer Setup](/hermes/skills/catalog/openclaw-customizer-setup)
- [Openclaw Ecosystem June26 Setup](/hermes/skills/catalog/openclaw-ecosystem-june26-setup)
- [Openclaw Grok Search Setup](/hermes/skills/catalog/openclaw-grok-search-setup)
- [openclaw-history-ingest Setup Guide](/hermes/skills/catalog/openclaw-history-ingest-setup)
- [OpenClaw Marketing Skills - Setup Guide](/hermes/skills/catalog/openclaw-marketing-skills-setup)
- [Openclaw Secure Linux Cloud Setup](/hermes/skills/catalog/openclaw-secure-linux-cloud-setup)
- [Openclaw Security Hardening Setup](/hermes/skills/catalog/openclaw-security-hardening-setup)
- [Openclaw Skill Vetter Setup](/hermes/skills/catalog/openclaw-skill-vetter-setup)
- [OpenClaw XHS Setup - Xiaohongshu (RED) Integration](/hermes/skills/catalog/openclaw-xhs-setup)
- [OpenAI Codex Skills - Official Skills Catalog Setup](/hermes/skills/catalog/openai-codex-skills-setup)
- [OpenTUI - Terminal UI Framework Setup](/hermes/skills/catalog/opentui-setup)
- [OPC Skills - Solopreneur Toolkit (SEO, Reddit, Branding, Launch) Setup](/hermes/skills/catalog/opc-skills-setup)
- [Oh My Hermes (OMH) Suite - Multi-Agent Orchestration Skills Setup](/hermes/skills/catalog/oh-my-hermes-omh-suite-setup)
- [Parallel Agent Skills - Web Intelligence for Hermes Setup](/hermes/skills/catalog/parallel-agent-skills-setup)
- [Perfectloop Setup](/hermes/skills/catalog/perfectloop-setup)
- [Petdex - Animated Mascots for Hermes Agent](/hermes/skills/catalog/petdex-setup)
- [Popular Web Designs - 54 Design Systems as HTML/CSS Templates Setup](/hermes/skills/catalog/popular-web-designs-setup)
- [PowerPoint - Create, Read, Edit .pptx Decks Setup](/hermes/skills/catalog/powerpoint-setup)
- [platform Skills](/hermes/skills/catalog/platform)
- [prisma Skills](/hermes/skills/catalog/prisma)
- [Railway Agent Skills - Infrastructure Deployment Setup](/hermes/skills/catalog/railway-agent-skills-setup)
- [Reason Machines DevTools Skills - Auto-Generated CLI Tool Skill Farm Setup](/hermes/skills/catalog/reason-machines-devtools-skills-setup)
- [Reddit Automation - Honest Reddit Engagement Setup](/hermes/skills/catalog/reddit-automation-setup)
- [Redis Agent Skills - Official Data Modeling & Caching Setup](/hermes/skills/catalog/redis-agent-skills-setup)
- [ResumeSkills - AI-Powered Resume Optimization Setup](/hermes/skills/catalog/resumeskills-setup)
- [Safari Web Agent Setup](/hermes/skills/catalog/safari-web-agent-setup)
- [Salesforce Skills Library (sf-skills) - 330+ Agent Skills Setup](/hermes/skills/catalog/salesforce-sf-skills-setup)
- [Security Hardening - AI Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)
- [Sentry AI Monitoring - Agent Error Tracking Setup](/hermes/skills/catalog/sentry-ai-monitoring-setup)
- [Sg Arrival Card Setup](/hermes/skills/catalog/sg-arrival-card-setup)
- [Shopify Development - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/shopify-development-setup)
- [shopify Skills](/hermes/skills/catalog/shopify)
- [Skill Repo Manager Setup](/hermes/skills/catalog/skill-repo-manager-setup)
- [Skill Vetting Setup](/hermes/skills/catalog/skill-vetting-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)
- [Skills Gallery Setup](/hermes/skills/catalog/skills-gallery-setup)
- [Social Content - Multi-Platform Social Media Creation Setup](/hermes/skills/catalog/social-setup)
- [Soul Grader Setup](/hermes/skills/catalog/soul-grader-setup)
- [Spike Setup](/hermes/skills/catalog/spike-setup)
- [Stepfun Skills Setup](/hermes/skills/catalog/stepfun-skills-setup)
- [Steroids Openai Image Gen Setup](/hermes/skills/catalog/steroids-openai-image-gen-setup)
- [stripe Skills](/hermes/skills/catalog/stripe)
- [supabase Skills](/hermes/skills/catalog/supabase)
- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)
- [Tavily Search Openclaw Setup](/hermes/skills/catalog/tavily-search-openclaw-setup)
- [Tavily Search - Official LLM-Optimized Web Search CLI Setup](/hermes/skills/catalog/tavily-search-setup)
- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup)
- [Threads Growth Skill Setup](/hermes/skills/catalog/threads-growth-skill-setup)
- [Three Agent Bridge Setup](/hermes/skills/catalog/three-agent-bridge-setup)
- [Timesfm Forecasting Setup](/hermes/skills/catalog/timesfm-forecasting-setup)
- [Trailofbits Security Setup](/hermes/skills/catalog/trailofbits-security-setup)
- [Ultimate Humanizer Setup](/hermes/skills/catalog/ultimate-humanizer-setup)
- [Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Vercel Eve Agent Skills - Official Eve Agent Framework Skills Setup](/hermes/skills/catalog/vercel-eve-agent-skills-setup)
- [Vps Server Management Setup](/hermes/skills/catalog/vps-server-management-setup)
- [Wiki History Ingest Setup](/hermes/skills/catalog/wiki-history-ingest-setup)
- [Writing Plans Subagent Development Setup](/hermes/skills/catalog/writing-plans-subagent-development-setup)
- [wshobson/agents - Agent Plugin Marketplace Setup](/hermes/skills/catalog/wshobson-agents-setup)
- [X Twitter Scraper Setup](/hermes/skills/catalog/x-twitter-scraper-setup)
- [Xurl Setup](/hermes/skills/catalog/xurl-setup)
- [Youtube Content Setup](/hermes/skills/catalog/youtube-content-setup)
- [Yuanbao - Tencent Group Chat Integration Setup](/hermes/skills/catalog/yuanbao-setup)
- [Better Auth Skills - Authentication Infrastructure Setup](/hermes/skills/catalog/better-auth-skills-setup)
- [Google Agents CLI - Google ADK Setup](/hermes/skills/catalog/google-agents-cli-setup)
- [GTM Agents - Go-to-Market Sales Skills Setup](/hermes/skills/catalog/gtm-agents-setup)
- [Knowledge Work Plugins - Anthropic Productivity Setup](/hermes/skills/catalog/knowledge-work-plugins-setup)
- [Lenny Skills - PM Methodology from Lenny Rachitsky Setup](/hermes/skills/catalog/lenny-skills-setup)
- [Sanity Agent Toolkit - Headless CMS Setup](/hermes/skills/catalog/sanity-agent-toolkit-setup)
- [SERP Downloaders - Content Downloader Skills Setup](/hermes/skills/catalog/serpdownloaders-setup)
- [Skills Collective AI Media - Image & Video Gen Setup](/hermes/skills/catalog/skills-collective-ai-media-setup)
- [Midscene Skills - AI-Powered Visual Browser Automation Setup](/hermes/skills/catalog/midscene-skills-setup)
- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup)
- [Playwright Social Media Automation - API-First Browser Fallback Setup](/hermes/skills/catalog/playwright-social-media-automation-setup)
- [Ruflo - Multi-Agent Orchestration Platform Setup](/hermes/skills/catalog/ruflo-setup)
- [Stitch Skills - Google Design-to-Code Pipeline Setup](/hermes/skills/catalog/stitch-skills-setup)
- [just-scrape - AI-Powered Web Scraping CLI Setup](/hermes/skills/catalog/just-scrape-setup)
- [Terminal Skills - System Administration Pack Setup](/hermes/skills/catalog/terminal-skills-setup)
- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)
- [Songwriting & AI Music - Creative Music Generation Setup](/hermes/skills/catalog/songwriting-and-ai-music-setup)
- [Debugging Hermes TUI Commands - Slash Command Troubleshooting Setup](/hermes/skills/catalog/debugging-hermes-tui-commands-setup)
- [Hermes Attestation Guardian - Security Verification Setup](/hermes/skills/catalog/hermes-attestation-guardian-setup)
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup)
- [Plan Mode - Plan-Only Execution Mode Setup](/hermes/skills/catalog/plan-mode-setup)
- [Godmode - Autonomous Execution Mode Setup](/hermes/skills/catalog/godmode-setup)
- [p5js - Creative Coding & Generative Art Setup](/hermes/skills/catalog/p5js-setup)
- [Polymarket - Prediction Market Integration Setup](/hermes/skills/catalog/polymarket-setup)
- [Simplify Code - Parallel Review & Cleanup Setup](/hermes/skills/catalog/simplify-code-setup)
- [Subagent-Driven Development - Multi-Agent Task Dispatch Setup](/hermes/skills/catalog/subagent-driven-development-setup)
- [HeartMuLa - Open-Source AI Music Generation Setup](/hermes/skills/catalog/heartmula-setup)
- [Creative Ideation - Constraint-Driven Brainstorming Setup](/hermes/skills/catalog/ideation-setup)
- [Linear Integration - Issue & Project Management Setup](/hermes/skills/catalog/linear-setup)
- [Webhook Subscriptions - External Service Trigger Setup](/hermes/skills/catalog/webhook-subscriptions-setup)
- [WeRead Skills - Tencent WeChat Reading Agent Skill Setup](/hermes/skills/catalog/weread-skills-setup)
- [OpenClaw Carapace - Design System Skills Setup](/hermes/skills/catalog/openclaw-carapace-setup)
- [OpenClaw Graph New Skills - Procedural Generation, ARKit, Testing Setup](/hermes/skills/catalog/openclaw-graph-new-skills-setup)
- [MCP OAuth Remote Gateway - Official Hermes Skill Setup](/hermes/skills/catalog/hermes-mcp-oauth-remote-gateway-setup)
- [Mnemosyne Hermes Memory Providers - Local-First Agent Memory Setup](/hermes/skills/catalog/mnemosyne-hermes-memory-providers-setup)
- [Audit Hermes Agent Skills - Skill Usage Audit & Cleanup Setup](/hermes/skills/catalog/cnife-audit-hermes-agent-skills-setup)
- [Volces Hermes & OpenClaw Skills - ByteDance Registry Cluster Setup](/hermes/skills/catalog/volces-hermes-openclaw-skills-setup)
- [Grounded Citations - Verifiable Source Citations Setup](/hermes/skills/catalog/grounded-citations-setup)
- [Lark & Feishu Skills - Office Suite Automation Setup](/hermes/skills/catalog/lark-feishu-skills-setup)
- [RigorPilot Skills - AI Research & Paper Reproduction Setup](/hermes/skills/catalog/rigorpilot-skills-setup)
- [Caveman Skills - Agent Coding Workflow Suite Setup](/hermes/skills/catalog/caveman-skills-setup)
- [Skills-101 Superpowers - AI Media & Automation Pack Setup](/hermes/skills/catalog/skills-101-superpowers-setup)
- [Warp Common Skills - Spec-Driven Development Workflow Setup](/hermes/skills/catalog/warpdotdev-common-skills-setup)
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup)
- [Stably Orca - Agent Orchestration CLI Setup](/hermes/skills/catalog/stablyai-orca-setup)
- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup)
- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)
- [GenMedia Skills - AI Media Generation Cluster Setup](/hermes/skills/catalog/genmedia-skills-setup)
- [Pika Plugins - Marketing Video Skill Pack Setup](/hermes/skills/catalog/pika-plugins-setup)
- [FlowKit Reddit Automation - Community Engagement Setup](/hermes/skills/catalog/flowkit-reddit-automation-setup)
- [HumanLayer Skills - Human-in-the-Loop Patterns Setup](/hermes/skills/catalog/humanlayer-skills-setup)
- [NuShell Pro - Structured Shell Scripting Setup](/hermes/skills/catalog/nushell-pro-setup)
- [Fetcher Skills - Social Platform API Cluster Setup](/hermes/skills/catalog/fetcher-skills-setup)
- [Convex Agent Skills - Backend Platform (BaaS) Setup](/hermes/skills/catalog/convex-agent-skills-setup)
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)
- [UI/UX Pro Max - Design System Skill Pack Setup](/hermes/skills/catalog/ui-ux-pro-max-setup)
- [Higgsfield Skills - AI Video & Image Generation Cluster Setup](/hermes/skills/catalog/higgsfield-skills-setup)
- [OSINT Skills - Open-Source Intelligence Suite Setup](/hermes/skills/catalog/osint-skills-setup)
- [Wind Skills - Financial Terminal Research Cluster Setup](/hermes/skills/catalog/wind-skills-setup)
- [Momentic Skills - AI QA Testing Suite Setup](/hermes/skills/catalog/momentic-skills-setup)
- [Planning With Files - Agent Planning Methodology Setup](/hermes/skills/catalog/planning-with-files-setup)
- [Wonda CLI - Terminal AI Content Creation Setup](/hermes/skills/catalog/wonda-setup)
- [SquirrelScan Skills - Website Audit Tool Setup](/hermes/skills/catalog/squirrelscan-skills-setup)
- [Solana Dev Skill - Blockchain Development Setup](/hermes/skills/catalog/solana-dev-skill-setup)
- [Genkit Skills - Firebase Genkit AI Framework Setup](/hermes/skills/catalog/genkit-skills-setup)
- [Firecrawl Skills - Web Scraping, Research & Workflow Suite Setup](/hermes/skills/catalog/firecrawl-skills-setup)
- [Nexscope E-Commerce Skills - Shopify, Etsy, TikTok Shop & Marketplace Growth Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [n8n Skills - Workflow Automation for Business Operators Setup](/hermes/skills/catalog/n8n-skills-setup)
- [Review Loop Skill - Continuous Code Review Discipline Setup](/hermes/skills/catalog/review-loop-skill-setup)
- [ECC Engineering Skills - Enterprise Engineering Suite Setup](/hermes/skills/catalog/ecc-engineering-skills-setup)
- [Flutter Agent Plugins - Official Flutter Skills Setup](/hermes/skills/catalog/flutter-agent-plugins-setup)
- [Sentry Dev Skill - Official Sentry CLI Setup](/hermes/skills/catalog/sentry-dev-skills-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)
- [SEOJuice Skills - SEO Suite Setup](/hermes/skills/catalog/seojuice-skills-setup)
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup)
- [CodeRabbit Skills - AI Code Review Setup](/hermes/skills/catalog/coderabbit-skills-setup)
- [Awesome LLM Apps Skills - Role-Based Agent Skills Setup](/hermes/skills/catalog/awesome-llm-apps-skills-setup)
- [CaffeineLabs Extension Skills - Agent Platform Extensions Setup](/hermes/skills/catalog/caffeinelabs-extension-skills-setup)
- [OpenCLI Skills - Agent CLI with Browser Automation Setup](/hermes/skills/catalog/opencli-skills-setup)
- [CMUX Skills - Agent Terminal Multiplexer Setup](/hermes/skills/catalog/cmux-skills-setup)
- [Agentix CEO Skill - AI Worker Team Orchestration Setup](/hermes/skills/catalog/agentix-ceo-skill-setup)
- [LiarJS Skills - Browser Fingerprint & Playwright Stealth Setup](/hermes/skills/catalog/liarjs-fingerprint-skills-setup)
- [Huashu Design Skill - HTML-First Agent Design Setup](/hermes/skills/catalog/huashu-design-setup)
- [Replicas Agent Skill - Cloud Workspace Coding Agent Setup](/hermes/skills/catalog/replicas-agent-skill-setup)
- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)
- [Agent Pulse Skill - Local AI Agent Activity Monitor Setup](/hermes/skills/catalog/agent-pulse-skill-setup)
- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [Oh Story ClaudeCode Skills - Long-Form Writing & Browser CDP Setup](/hermes/skills/catalog/oh-story-claudecode-skills-setup)
- [VueJS AI Skills - Vue Best Practices Suite Setup](/hermes/skills/catalog/vuejs-ai-skills-setup)
- [Rivet Skills - Real-Time Backend & Agent Infrastructure Setup](/hermes/skills/catalog/rivet-dev-skills-setup)
- [Interface Design Skill - Non-Templated Product UI Setup](/hermes/skills/catalog/interface-design-skill-setup)
- [Feature-Sliced Design Skill - Frontend Architecture Setup](/hermes/skills/catalog/feature-sliced-design-skill-setup)
- [RampStack Claude Skills - Growth & Marketing Suite Setup](/hermes/skills/catalog/rampstack-claude-skills-setup)
- [Tailwind 4 Docs Skill - Local Docs Snapshot Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup)
- [Claude Video Watch Skill - Agent Video Input Setup](/hermes/skills/catalog/claude-video-watch-skill-setup)
- [Tiangong AI Skills - Email & Research Data Fetching Suite Setup](/hermes/skills/catalog/tiangong-ai-skills-setup)
- [RKnall Claude Skills - SVG Logo & GitLab Stack Setup](/hermes/skills/catalog/rknall-claude-skills-setup)
- [Superdesign Skill - Canvas Design & Inspiration Setup](/hermes/skills/catalog/superdesign-skill-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)
- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)
- [Trail of Bits Skills Curated - Agent Security Suite Setup](/hermes/skills/catalog/trailofbits-skills-curated-setup)
- [Sentry Agent Skills - Security & Code Review Suite Setup](/hermes/skills/catalog/sentry-agent-skills-setup)
- [Three.js Agent Skills - 3D & WebGL Suite Setup](/hermes/skills/catalog/threejs-agent-skills-setup)
- [Emblem Company Agent Skills - Portfolio & Market Research Setup](/hermes/skills/catalog/emblem-company-agent-skills-setup)
- [CTF Security Skills - Offensive Security Suite Setup](/hermes/skills/catalog/ctf-security-skills-setup)
- [Bright Data Agent Skills - Web Scraping & Research Setup](/hermes/skills/catalog/brightdata-agent-skills-setup)
- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Langfuse Agent Skills - LLM Observability Setup](/hermes/skills/catalog/langfuse-agent-skills-setup)
- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup)
- [MiniMax H3 Skills - AI Video Prompt Writing & Generation Setup](/hermes/skills/catalog/minimax-h3-skills-setup)
- [Mintlify Docs Skills - Documentation Platform Setup](/hermes/skills/catalog/mintlify-docs-skills-setup)
- [Motion Design Skill - LottieFiles Animation Setup](/hermes/skills/catalog/lottiefiles-motion-design-skill-setup)
- [Mobile App UI Design Skill - Mobile Interface Setup](/hermes/skills/catalog/mobile-app-ui-design-skill-setup)
- [Cursor Plugins Skills - Engineering Discipline Suite Setup](/hermes/skills/catalog/cursor-plugins-skills-setup)
- [Vercel Plugin Skills - Full Vercel Ecosystem Agent Setup](/hermes/skills/catalog/vercel-plugin-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [Angular Skills - Framework Development Setup](/hermes/skills/catalog/angular-skills-setup)
- [Inngest Skills - Durable Workflow Orchestration Setup](/hermes/skills/catalog/inngest-skills-setup)
- [OXC Project Skills - Linter & Formatter Migration Setup](/hermes/skills/catalog/oxc-project-skills-setup)
- [Alibaba Open Code Review - AI Code Review CLI Setup](/hermes/skills/catalog/alibaba-open-code-review-setup)
- [Brian Lovin Agent Config - Design Engineering Suite Setup](/hermes/skills/catalog/brianlovin-agent-config-setup)
- [last30days Skill - Recent-Activity Research Setup](/hermes/skills/catalog/last30days-skill-setup)
- [Herdr Skills - Terminal Workspace Orchestration Setup](/hermes/skills/catalog/herdr-skills-setup)
- [Web Access Skill - Unified Browsing & Scraping Setup](/hermes/skills/catalog/web-access-skill-setup)
- [Stop Slop - AI-Prose Pattern Cleaner Setup](/hermes/skills/catalog/stop-slop-setup)
- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)
- [M. Collina Node Skills - Fastify & Node.js Agent Suite Setup](/hermes/skills/catalog/mcollina-node-skills-setup)
- [Zhaono1 Agent Playbook - 24-Role Agent Workflow Suite Setup](/hermes/skills/catalog/zhaono1-agent-playbook-setup)
- [Nx AI Agents Config - Monorepo Agent Skills Setup](/hermes/skills/catalog/nx-ai-agents-config-skills-setup)
- [WeCom CLI Skills - Enterprise WeChat Agent Suite Setup](/hermes/skills/catalog/wecom-cli-skills-setup)
- [WeCom Unified Skill - WeChat Work Routing Suite Setup](/hermes/skills/catalog/wecom-unified-skills-setup)
- [Mastra AI Skills - TypeScript Agent Framework Setup](/hermes/skills/catalog/mastra-ai-skills-setup)
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup)
- [Claude for Legal Skills - Anthropic Legal Workflow Suite Setup](/hermes/skills/catalog/claude-for-legal-skills-setup)
- [PCL Domain Expert Skills - 104 Persona Skill Pack Setup](/hermes/skills/catalog/pcl-domain-expert-skills-setup)
- [VTEX Skills - Commerce Platform Development Suite Setup](/hermes/skills/catalog/vtex-skills-setup)
- [Genshijin Skills - Japanese Concise-Reply Framework Setup](/hermes/skills/catalog/genshijin-skills-setup)
- [Hono Skill - Edge Web Framework Setup by the Hono Author](/hermes/skills/catalog/hono-skill-setup)
- [Capawesome Skills - Capacitor and Ionic Ecosystem Suite Setup](/hermes/skills/catalog/capawesome-skills-setup)
- [Wyatt Walsh Agents - Skill Governance and Orchestration Suite Setup](/hermes/skills/catalog/wyattowalsh-agents-setup)
- [Hermes Field Kit - Field-Tested Hermes Operations Skill Suite Setup](/hermes/skills/catalog/hermes-field-kit-setup)
- [AtlasOmnia Hermes Custom Pack - 60+ Skill Independent Pack Setup](/hermes/skills/catalog/atlasomnia-hermes-custom-pack-setup)
- [Buzz Skills - Hermes Agent on Nostr via Block's Buzz Setup](/hermes/skills/catalog/buzz-skills-setup)
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup)
- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Autonnel Skills - Conversion & Funnel Optimization Suite Setup](/hermes/skills/catalog/autonnel-skills-setup)
- [GPT-Image-2 Style Library - Industrial Prompt & Style Templates Setup](/hermes/skills/catalog/gpt-image-2-style-library-setup)
- [gh-issue-sync - Local Markdown GitHub Issues Skill Setup](/hermes/skills/catalog/gh-issue-sync-setup)
- [System Atlas - Explorable Architecture Map Skill Setup](/hermes/skills/catalog/system-atlas-setup)
- [Makerskills - Personal Operator Agent Suite Setup](/hermes/skills/catalog/makerskills-setup)
- [Tech Logos - Brand Logo Installer for shadcn/ui Setup](/hermes/skills/catalog/tech-logos-setup)
- [Generative Media Skills - 153-Skill Media Production Suite Setup](/hermes/skills/catalog/generative-media-skills-setup)
- [Podo Design Agent Skills - 151-Skill Design Catalog Setup](/hermes/skills/catalog/podo-design-agent-skills-setup)
- [pp-mercury - Mercury Banking CLI Setup](/hermes/skills/catalog/pp-mercury-setup)
- [Printing Press Library - 472-CLI Agent Tool Catalog Setup](/hermes/skills/catalog/printing-press-library-setup)
- [Revenue-Centric Design Skill - SaaS Conversion Playbook Setup](/hermes/skills/catalog/revenue-centric-design-setup)
- [Telegram Mini App Skill - Telegram Web App Builder Setup](/hermes/skills/catalog/telegram-mini-app-setup)
- [gh-stack - GitHub Stacked PRs Skill Setup](/hermes/skills/catalog/gh-stack-setup)
- [Hallmark - Anti-AI-Slop Design Skill Setup](/hermes/skills/catalog/hallmark-setup)
- [Dart Language Skills - Official Dart Team Suite Setup](/hermes/skills/catalog/dart-lang-skills-setup)
- [HubSpot Agent CLI Skills - CRM Operations Suite Setup](/hermes/skills/catalog/hubspot-agent-cli-skills-setup)
- [Basic Memory Skills - Agent Knowledge Graph Suite Setup](/hermes/skills/catalog/basic-memory-skills-setup)
- [Meng To Skills - Frontend & Motion Design Suite Setup](/hermes/skills/catalog/mengto-skills-setup)
- [Low-Level Dev Skills - Systems Programming Suite Setup](/hermes/skills/catalog/low-level-dev-skills-setup)
- [Daymade Claude Code Skills - General-Purpose Suite Setup](/hermes/skills/catalog/daymade-claude-code-skills-setup)
- [LJG Skills - Personal Knowledge Work Suite Setup](/hermes/skills/catalog/ljg-skills-setup)
- [InsForge Skills - AI App Backend-as-a-Service Suite Setup](/hermes/skills/catalog/insforge-skills-setup)
- [Matt Pocock Skills (简体中文) - Localized Engineering Suite Setup](/hermes/skills/catalog/mattpocock-skills-zh-cn-setup)
- [Owl Listener Designer Skills - 107-Skill Design Suite Setup](/hermes/skills/catalog/owl-listener-designer-skills-setup)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup)
- [Petr Kindlmann QA Skills - 50-Skill Test Automation Suite Setup](/hermes/skills/catalog/petrkindlmann-qa-skills-setup)
- [Paperthin - Agentic Design Patterns Toolkit Setup](/hermes/skills/catalog/paperthin-skills-setup)
- [Inkeep Open Knowledge Skills - Collaborative Knowledge Base Suite Setup](/hermes/skills/catalog/inkeep-open-knowledge-skills-setup)
- [Vigiles - Agent Harness Quality Suite Setup](/hermes/skills/catalog/vigiles-setup)
- [Hithink Finance - Tonghuashun A-Share Data Skill Setup](/hermes/skills/catalog/hithink-finance-setup)
- [Task Observer - Meta-Skill for Continuous Skill Improvement Setup](/hermes/skills/catalog/task-observer-setup)
- [Hermes Agent Official Skills - Bundled Batch Setup](/hermes/skills/catalog/hermes-agent-official-skills-batch-setup)
- [Sleek Design Mobile Apps - AI Mobile App Design Skill Setup](/hermes/skills/catalog/sleek-design-mobile-apps-setup)
- [Marketing Mindset - B2B Marketing OS for AI Agents Setup](/hermes/skills/catalog/marketing-mindset-setup)
- [Book-to-Skill - Book to Agent Skill Converter Setup](/hermes/skills/catalog/book-to-skill-setup)
- [Samber DevRel Skills - Open Source Growth Suite Setup](/hermes/skills/catalog/samber-devrel-skills-setup)
- [Layer Skills - AI Game Asset Creation Suite Setup](/hermes/skills/catalog/layerai-skills-setup)
- [AE-CLI Skills - AgenticEngine Platform Suite Setup](/hermes/skills/catalog/ae-cli-skills-setup)
- [Coinos Skills - AiCoin Crypto Trading Suite Setup](/hermes/skills/catalog/coinos-trading-skills-setup)
- [A Smart Bear Skills - Positioning & PMF Suite Setup](/hermes/skills/catalog/asmartbear-skills-setup)
- [Make Skills - Automation Platform Suite Setup](/hermes/skills/catalog/make-skills-setup)
- [Picsart Gen-AI Skills - Generative Media Suite Setup](/hermes/skills/catalog/picsart-gen-ai-skills-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)
- [Kangarooking Skills - Agent Harness Suite Setup](/hermes/skills/catalog/kangarooking-skills-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [Jezweb Skills - 96-Skill Web Dev & Design Suite Setup](/hermes/skills/catalog/jezweb-skills-setup)
- [OmniRoute Skills - 70.9K⭐ AI Gateway Suite Setup](/hermes/skills/catalog/omniroute-skills-setup)
- [rlaope Oh My Hermes - 130-Skill All-in-One Plugin Setup](/hermes/skills/catalog/rlaope-oh-my-hermes-setup)
- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup)
- [Dboeckli AI Agent Skills - CLI & Best Practices Setup](/hermes/skills/catalog/dboeckli-ai-agent-skills-setup)
- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Riekelt Principal Engineer - Engineering Discipline Suite Setup](/hermes/skills/catalog/riekelt-principal-engineer-setup)
- [01coder Agent Skills - Content, Publishing & Security Toolkit Setup](/hermes/skills/catalog/01coder-agent-skills-setup)
- [Steipete Agent Scripts - Portable Agent Skills & Helpers Setup](/hermes/skills/catalog/steipete-agent-scripts-setup)
- [Callicrate Skills - AGENTS.md & Documentation Authoring Setup](/hermes/skills/catalog/callicrate-skills-setup)
- [CrewAI Skills - Official Agent Design Suite Setup](/hermes/skills/catalog/crewai-skills-setup)
- [Moonlight Lupin Agent Skills - Hermes Skill Suite Setup](/hermes/skills/catalog/moonlight-lupin-agent-skills-setup)
- [Goldsky Agent Skills - Blockchain Data Pipeline Setup](/hermes/skills/catalog/goldsky-agent-skills-setup)
- [Callstack Agent Skills - React Native Skill Suite Setup](/hermes/skills/catalog/callstackincubator-agent-skills-setup)
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)
- [Amplitude Agent Skills - Product Analytics Setup](/hermes/skills/catalog/amplitude-agent-skills-setup)
- [mbfinotti Business Skills - Sales, RevOps & Advertising](/hermes/skills/catalog/mbfinotti-skills-setup)
- [Cloudflare Security Audit Skill - Agent Code Auditing Setup](/hermes/skills/catalog/cloudflare-security-audit-setup)
- [Limrun Skills - Cloud iOS & Android Simulator Setup](/hermes/skills/catalog/limrun-skills-setup)
- [TypeSafe AI Skills - Typed AI Judgments Setup](/hermes/skills/catalog/typesafe-ai-setup)
- [Yomiyasu - Japanese AI Prose Refinement Setup](/hermes/skills/catalog/yomiyasu-setup)
- [Proseify - Anti-Prose-Slop Book Writing Setup](/hermes/skills/catalog/proseify-setup)
- [Modern Web Guidance - Google Chrome Agent Skill Setup](/hermes/skills/catalog/googlechrome-modern-web-guidance-setup)
- [Baoyu Skills - Content Generation & Publishing Suite Setup](/hermes/skills/catalog/baoyu-skills-setup)
- [UI Skills - Design Engineer Skill Registry Setup](/hermes/skills/catalog/ibelick-ui-skills-setup)
- [Meticulous Agent Skills - Visual Regression Testing Setup](/hermes/skills/catalog/meticulous-agent-skills-setup)
- [Designer Skills - Design Process Suite Setup](/hermes/skills/catalog/designer-skills-setup)
- [Medusa Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/medusa-agent-skills-setup)
- [Garden Skills - ConardLi's Web Video & Design Suite Setup](/hermes/skills/catalog/garden-skills-setup)
- [Wondelai Skills - Book Framework Business & Design Setup](/hermes/skills/catalog/wondelai-skills-setup)
- [Starchild Official Skills - Agent Platform Library Setup](/hermes/skills/catalog/starchild-official-skills-setup)
- [Cargo Skills - GTM Engineering Suite for Agents Setup](/hermes/skills/catalog/cargo-skills-setup)
- [Compound Engineering Plugin - Every Inc Workflow Suite Setup](/hermes/skills/catalog/compound-engineering-plugin-setup)
- [Samber Developer Platform Skills - API & DX Setup](/hermes/skills/catalog/samber-developer-platform-skills-setup)
- [Open Mercato Skills - Enterprise ERP Engineering Setup](/hermes/skills/catalog/open-mercato-skills-setup)
- [Bencium Marketplace - Design & Product Skills Suite Setup](/hermes/skills/catalog/bencium-marketplace-setup)
- [MiniMax AI Skills - Official Dev & Document Suite Setup](/hermes/skills/catalog/minimax-ai-skills-setup)
- [PM Skills - Product Management Lifecycle Suite Setup](/hermes/skills/catalog/pm-skills-setup)
- [Dimillian Skills - Apple Platform Engineering Suite Setup](/hermes/skills/catalog/dimillian-skills-setup)
- [Skills for Antigravity - Game & Research Collection Setup](/hermes/skills/catalog/skills-for-antigravity-setup)
- [Three.js Game Skills - 3D Game Development Suite Setup](/hermes/skills/catalog/threejs-game-skills-setup)
- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup)
- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)
- [Trigger.dev Skills - Background Jobs & Realtime Setup](/hermes/skills/catalog/trigger-dev-skills-setup)
- [LangSmith Skills - LLM Evaluation & Tracing Setup](/hermes/skills/catalog/langsmith-skills-setup)
- [Botpress Skills - Agent Development Kit (ADK) Setup](/hermes/skills/catalog/botpress-skills-setup)
- [Delegate Skills - CLI Agent Fleet Orchestration Setup](/hermes/skills/catalog/amelnagdy-delegate-skills-setup)
- [Claude Design Skillstack - 3D & Animation Setup](/hermes/skills/catalog/claudedesignskills-setup)
- [Sanyuan Skills - Production Agent Skills Suite Setup](/hermes/skills/catalog/sanyuan-skills-setup)
- [Sentimony Skills - Dev Workflow & Review Gates Setup](/hermes/skills/catalog/sentimony-skills-setup)
- [Ghost Security Skills - AppSec Agent Plugin Setup](/hermes/skills/catalog/ghostsecurity-skills-setup)
- [Some Claude Skills - 180+ Skill Collection Setup](/hermes/skills/catalog/some-claude-skills-setup)
- [Dify Skills - Official Dev Workflow Suite Setup](/hermes/skills/catalog/dify-skills-setup)
- [CodexSkills - Agent Orchestration Skills Setup](/hermes/skills/catalog/am-will-codex-skills-setup)
- [Agentation - Visual Feedback for Agents Setup](/hermes/skills/catalog/agentation-setup)
- [Journalism Agent Skills - Media Workflows Setup](/hermes/skills/catalog/claude-skills-journalism-setup)
- [BuilderOS - Product Builder Workflow Suite Setup](/hermes/skills/catalog/builder-os-setup)
- [Platform Design Skills - HIG & Material Setup](/hermes/skills/catalog/platform-design-skills-setup)
- [CloudBase Skills - Tencent Full-Stack Apps Setup](/hermes/skills/catalog/cloudbase-skills-setup)
- [ulpi Skills - Browse, SEO & Dev Utilities Setup](/hermes/skills/catalog/ulpi-io-skills-setup)
- [Srinitude Skills - Portable Agent Skills Setup](/hermes/skills/catalog/srinitude-skills-setup)
- [Antigravity Skill Vault - 300+ Skills Setup](/hermes/skills/catalog/antigravity-skill-vault-setup)
- [Mies - Design Taste Skill for Interfaces Setup](/hermes/skills/catalog/mies-setup)
- [Vibe Motion Skills - SVG & Motion Renders Setup](/hermes/skills/catalog/vibe-motion-skills-setup)
- [Vapi Skills - Voice AI Agent Building Setup](/hermes/skills/catalog/vapi-skills-setup)
- [Sergiodxa Agent Skills - Frontend Practice Setup](/hermes/skills/catalog/sergiodxa-agent-skills-setup)
- [Appllama Skills - Mobile App Design Patterns Setup](/hermes/skills/catalog/appllama-skills-setup)
- [Mastepanoski Skills - UX & AI Compliance Audits Setup](/hermes/skills/catalog/mastepanoski-skills-setup)
- [MagicPath Agent Skills - UI Component Workflow Setup](/hermes/skills/catalog/magicpath-agent-skills-setup)
- [EvoSkills - Scientific Research Skill Packs Setup](/hermes/skills/catalog/evoskills-setup)
- [Claude Code Extensions - Agents, Skills & Hooks Setup](/hermes/skills/catalog/nodnarbnitram-claude-code-extensions-setup)
- [Wayne Sutton Builder Skills - Convex App Development Setup](/hermes/skills/catalog/waynesutton-builder-skills-setup)
- [TestDino Playwright Skills - 79-Guide Testing Suite Setup](/hermes/skills/catalog/testdino-playwright-skill-setup)
- [GMGN Agent Skills - On-Chain Analytics and Trading Setup](/hermes/skills/catalog/gmgn-skills-setup)
- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)
- [ASO Skills - App Store Optimization Suite Setup](/hermes/skills/catalog/aso-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [CLI Printing Press - Agent-Native CLI Generator Setup](/hermes/skills/catalog/cli-printing-press-setup)
- [Mapbox Agent Skills - Location Development Suite Setup](/hermes/skills/catalog/mapbox-agent-skills-setup)
- [ScrapeCreators Social Research Skills - Setup Guide](/hermes/skills/catalog/scrapecreators-social-research-setup)
- [AI Agent Skills - Creative and Platform Stack Setup](/hermes/skills/catalog/ai-agents-skills-setup)

## Previously unlinked pages (added 2026-10-06)

Linked from this index so the pages are reachable by crawl.

### Skill setup guides

- [Agent Architect - Agent System Design Setup](/hermes/skills/catalog/agent-architect-setup)
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup)
- [Anthropic Cybersecurity Skills Setup Guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup)
- [Chainlink Agent Skills Setup Guide](/hermes/skills/catalog/chainlink-agent-skills-setup)
- [ECC - Agent Harness Performance Optimization](/hermes/skills/catalog/ecc-agent-harness-setup)
- [Hermes Dojo - Self-Improvement System Setup Guide](/hermes/skills/catalog/hermes-dojo-setup)
- [Hermes Learns Manim - Math Animation Setup Guide](/hermes/skills/catalog/hermes-learns-manim-setup)
- [Hermes Nextcloud Integration Setup Guide](/hermes/skills/catalog/hermes-nextcloud-setup)
- [Hermes Plugins (42-evey) Setup Guide](/hermes/skills/catalog/hermes-plugins-42evey-setup)
- [MCP Client - MCP Client Operations Setup](/hermes/skills/catalog/mcp-client-setup)
- [Microsoft Workspace Skill Setup Guide](/hermes/skills/catalog/microsoft-workspace-skill-setup)
- [Obsidian Agent Skills Setup Guide](/hermes/skills/catalog/obsidian-skills-setup)
- [RunAPI CLI Skill Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/runapi-cli-skill-setup)
- [Skills.sh Sweep - August 10, 2026](/hermes/skills/catalog/skills-sweep-aug-10-2026)
- [Skills.sh Sweep - August 11, 2026](/hermes/skills/catalog/skills-sweep-aug-11-2026)
- [Skills.sh Sweep - August 12, 2026](/hermes/skills/catalog/skills-sweep-aug-12-2026)
- [agentiko-hermes - Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/agentiko-hermes-setup)
- [hermes-studio-dashboard - Setup Guide](/hermes/skills/catalog/hermes-studio-dashboard-setup)
- [html-ppt-hermes-cyber-terminal - Setup Guide](/hermes/skills/catalog/html-ppt-hermes-cyber-terminal-setup)
- [taste-skill - Design-to-Code & AI Image Generation for](/hermes/skills/catalog/taste-skill-setup)
- [web-quality-skills - Google-Grade Web Quality Audits](/hermes/skills/catalog/web-quality-skills-setup)
- [Dontbesilent dbskill - 35-Skill Business Toolkit Setup](/hermes/skills/catalog/dontbesilent-dbskill-setup)
- [Ponytail Skills - Lazy Senior Dev Coding Setup](/hermes/skills/catalog/ponytail-skills-setup)
- [Stripe Link CLI Skills - Agent Payments Setup](/hermes/skills/catalog/stripe-link-cli-setup)
- [Anatomy Skill - Isometric SVG Explainer Setup](/hermes/skills/catalog/anatomy-skill-setup)
- [SEO Skill - Search Console MCP for Agents Setup](/hermes/skills/catalog/iannuttall-seo-setup)
- [Binance Skills Hub - Crypto Trading Skills Setup](/hermes/skills/catalog/binance-skills-hub-setup)
- [Solana Mobile Skills - Android Wallet Dev Setup](/hermes/skills/catalog/solana-mobile-skills-setup)
- [Anthony Fu Skills - Vue, Vite and TS Tooling Setup](/hermes/skills/catalog/antfu-skills-setup)
- [shadcn Improve - Codebase Audit to Plan Setup](/hermes/skills/catalog/shadcn-improve-setup)
- [Hypit - AI Video Clone Production Setup](/hermes/skills/catalog/hypit-skills-setup)
- [Masseater Skills - Engineering Judgment Suite](/hermes/skills/catalog/masseater-skills-setup)
- [Ultracite - Zero-Config Lint Preset Setup](/hermes/skills/catalog/ultracite-skills-setup)
- [Waza - Engineering Habit Skills for Coding Agents](/hermes/skills/catalog/waza-skills-setup)
- [Diagram Design - Editorial HTML and SVG Diagrams](/hermes/skills/catalog/diagram-design-setup)
- [REA - Reverse Engineer Anything Skill Setup](/hermes/skills/catalog/rea-setup)

### New - October 26, 2026 Sweep (14 publisher guides)

- [Slavingia Skills - Minimalist Entrepreneur Business Suite](/hermes/skills/catalog/slavingia-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [Arize Skills - LLM Observability and Evaluation Setup](/hermes/skills/catalog/arize-skills-setup)
- [Longbridge Skills - Brokerage Data and Trading Suite](/hermes/skills/catalog/longbridge-skills-setup)
- [Dynatrace for AI - Observability Skills Setup](/hermes/skills/catalog/dynatrace-for-ai-setup)
- [Nuxt Skills - Vue, Nuxt and NuxtHub Agent Setup](/hermes/skills/catalog/onmax-nuxt-skills-setup)
- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [Brand Building Skills - Brand Strategy Suite Setup](/hermes/skills/catalog/arnabbagxd-brand-building-skills-setup)
- [Sales Skills - B2B Sales Playbook Suite Setup](/hermes/skills/catalog/louisblythe-sales-skills-setup)
- [Agent Research Skills - Academic Paper Suite Setup](/hermes/skills/catalog/lingzhi227-agent-research-skills-setup)
- [Nia Skill - Code and Docs Indexing Setup](/hermes/skills/catalog/nozomio-nia-skill-setup)
- [Recoup Skills - Music Label Agent Suite Setup](/hermes/skills/catalog/recoupable-skills-setup)
- [NotebookLM Skill - Archived Notebook Query Setup](/hermes/skills/catalog/notebooklm-skill-setup)
- [AI Labs Claude Skills - 27 Skill Business Suite Setup](/hermes/skills/catalog/ailabs-claude-skills-setup)

### New - October 26, 2026 Evening Sweep (8 publisher guides)

- [Yaklang Hack Skills - Offensive Security Toolkit Setup](/hermes/skills/catalog/hack-skills-setup)
- [Dev Event Organizer Skills - Conferences and Meetups Setup](/hermes/skills/catalog/dev-event-organizer-skills-setup)
- [Aaron Marketing Skills - Full Marketing Department Setup](/hermes/skills/catalog/aaron-marketing-skills-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)
- [Reddit Research Skills - Market Research Setup Guide](/hermes/skills/catalog/reddit-research-skills-setup)
- [Indexion Skills - Source Code Exploration for Agents Setup](/hermes/skills/catalog/indexion-skills-setup)
- [Superagent Security Skills - Agent Security Audit Setup](/hermes/skills/catalog/superagent-skills-setup)
- [Darwin Skill - Autonomous Skill Optimization Setup](/hermes/skills/catalog/darwin-skill-setup)

### New - November 2, 2026 Morning Sweep (13 publisher guides)

Thirteen repository clusters surfaced by a widened 68-query topic probe, documented for **901,643 combined installs across 568 indexed listings**:

- [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup) - gamedev-skills/awesome-gamedev-agent-skills, 581,262 combined, 78 listings, 6,525 stars, Apache-2.0, 77 game-dev skills across Godot, Unity, Unreal and Phaser, one directory per listing with a router skill that picks the stack
- [Syncfusion React UI Skills - Component Suite Setup](/hermes/skills/catalog/syncfusion-react-ui-skills-setup) - syncfusion/react-ui-components-skills, 42,927 combined, 62 listings, 3 stars, no LICENSE file, one skill per React component family for grid, scheduler, Gantt, charts and editors, with no LICENSE file and a commercial component licence running alongside the skill files
- [Karpathy Guidelines - Coding Discipline Skill](/hermes/skills/catalog/karpathy-guidelines-setup) - multica-ai/andrej-karpathy-skills, 43,921 combined, 1 listings, 228,252 stars, no LICENSE file, one skill carrying four coding principles drawn from Andrej Karpathy's observations on wrong assumptions, overcomplication and orthogonal edits, 228,253 stars and no LICENSE file while the README and plugin manifest both say MIT
- [SwiftUI Pro - Apple UI Development Skill](/hermes/skills/catalog/twostraws-swiftui-pro-setup) - twostraws/swiftui-agent-skill, 36,507 combined, 1 listings, 6,438 stars, MIT, Paul Hudson's single SwiftUI skill with reference files behind a router SKILL.md, MIT licensed and every sampled audit a Pass
- [Motion Graphics Skills - Launch Video Suite](/hermes/skills/catalog/motion-graphics-skills-setup) - charlie947/motion-graphics-skills, 28,476 combined, 15 listings, 524 stars, MIT, 13 rendered motion-graphics skills under HyperFrames with storyboard, kinetic type and 3D scene packs, 15 directories against 15 listings
- [Syncfusion Blazor UI Skills - Component Suite Setup](/hermes/skills/catalog/syncfusion-blazor-ui-skills-setup) - syncfusion/blazor-ui-components-skills, 23,778 combined, 66 listings, 4 stars, no LICENSE file, one skill per Blazor component family across Server, WebAssembly and Hybrid hosting, 69 directories against 66 listings and no LICENSE file
- [Microsoft Learn Agent Skills - Azure and .NET Docs](/hermes/skills/catalog/microsoftdocs-agent-skills-setup) - microsoftdocs/agent-skills, 39,644 combined, 198 listings, 804 stars, CC-BY-4.0, Microsoft's own curated catalogue of Azure service skills, 201 in-tree directories against 198 indexed listings, CC-BY-4.0 and every sampled verdict a Pass
- [Qodex AI Agent Skills - 81 Skill Starter Library](/hermes/skills/catalog/qodex-ai-agent-skills-setup) - qodex-ai/ai-agent-skills, 21,371 combined, 81 listings, 47 stars, no LICENSE file, 81 general-purpose agent skills spanning research, coding, content and business work, with no LICENSE file and a README carried over from the upstream Anthropic skills repository
- [Linear CLI - Issue Tracking from the Terminal](/hermes/skills/catalog/linear-cli-setup) - schpet/linear-cli, 19,086 combined, 2 listings, 1,033 stars, ISC, two skills over a Rust CLI for issue tracking from the terminal: list, start, link and close issues and open pull requests, ISC licensed
- [AntV Chart Visualization Skills - Data to Charts](/hermes/skills/catalog/antvis-chart-visualization-setup) - antvis/chart-visualization-skills, 18,128 combined, 13 listings, 524 stars, MIT, AntV grammar-of-graphics guidance for statistical and narrative charts, 13 listings against nine in-tree directories, one Snyk Warn in the sample
- [Encore Skills - Backend Service Development Setup](/hermes/skills/catalog/encore-skills-setup) - encoredev/skills, 16,784 combined, 40 listings, 30 stars, Apache-2.0, 38 skills for Encore.ts and Encore.go covering APIs, databases, queues and infrastructure from code, Apache-2.0 with two indexed listings that have no directory
- [Noiz AI Skills - Voice and Speech for Agents](/hermes/skills/catalog/noizai-skills-setup) - noizai/skills, 15,285 combined, 10 listings, 532 stars, no LICENSE file, ten voice skills over the Noiz AI API for text to speech, voice cloning and speech to text, no LICENSE file and a Snyk Warn on the single sampled listing
- [ElysiaJS Skill - Bun Web Framework Setup](/hermes/skills/catalog/elysiajs-skills-setup) - elysiajs/skills, 14,474 combined, 1 listings, 70 stars, no LICENSE file, one skill for Elysia on Bun covering routing, validation, plugins and Eden end-to-end types, no README and no LICENSE file in the repository

### New - November 1, 2026 Evening Sweep (8 publisher guides)

Eight repository clusters drained from the queue the morning fire left, documented for **47,624 combined installs across 135 indexed listings**:

- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup) - melvynx/video-agent-skills, 7,837 combined, 24 listings, 86 stars, MIT, thirteen Claude Code skills for short-form video from script to publish: a week of scripts with hooks scored from 22 formulas, hook and outlier research, an editing skill shipping its own Node and ffmpeg render engine, voice-cloned translation and publishing, with two Gen Agent Trust Hub FAILs and a Snyk Warn in the sampled set
- [News Aggregator Skill - Multi-Source News Digest](/hermes/skills/catalog/news-aggregator-skill-setup) - cclank/news-aggregator-skill, 6,015 combined, 1 listing, 1,317 stars, no LICENSE file, one Python skill over 44+ RSS and community sources with OPML extension, Playwright deep fetch and Chinese briefing presets, where scripts/rss_parser.py fetches with TLS verification disabled and the Snyk Warn sits on the only listing
- [LlamaParse Skills - Document Parsing for Agents](/hermes/skills/catalog/llamaparse-agent-skills-setup) - run-llama/llamaparse-agent-skills, 5,979 combined, 4 listings, 85 stars, MIT, three LlamaIndex skills split by where parsing runs: local liteparse with no key, cloud LlamaParse behind LLAMA_CLOUD_API_KEY and agentic retrieval over a LlamaCloud Index v2, three directories against four listings with the fourth named as an index-only row
- [Vue Ecosystem Skills - Version-Aware Vue Context](/hermes/skills/catalog/vue-ecosystem-skills-setup) - skilld-dev/vue-ecosystem-skills, 5,930 combined, 35 listings, 184 stars, MIT, version-aware Vue ecosystem context rebuilt from each published package: Vue 3.6, Pinia, Vue Router, Reka UI, VueUse, Vuetify and TanStack, 20 rows at or above 104 installs, three directories unreachable by the plugin route and every sampled verdict a Pass
- [LLM Code Skills - Cross-Tool Documentation Pack](/hermes/skills/catalog/llm-code-setup) - itechmeat/llm-code, 5,960 combined, 49 listings, 24 stars, MIT, documentation-based skills that work across Copilot, Claude and Cursor from one agentskills.io folder: Vite, FastAPI, Bun, Mantine, Vitest, Kubernetes and more, 38 directories against 49 listings with 11 indexed names carrying no directory and three Snyk Warns in the sample
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup) - qodo-ai/qodo-skills, 5,429 combined, 10 listings, 59 stars, MIT, the Qodo local review workflow as provider-neutral skills: setup, codebase wisdom, local review, PR review resolution and an opt-in standards package, 35 SKILL.md directories that are seven canonical skills plus four generated provider projections, Snyk Warns on the review and rules listings
- [Web AI Agent Skills - Browser AI APIs and WebMCP](/hermes/skills/catalog/web-ai-agent-skills-setup) - webmaxru/web-ai-agent-skills, 5,317 combined, 11 listings, 53 stars, no LICENSE file, browser AI APIs as skills: Prompt API, Language Detector, Translator, Writing Assistance, Proofreader, WebMCP and WebNN, each with a per-Chrome-milestone compatibility reference and a deterministic target scanner, four of the eleven listings being repository-maintenance skills
- [Tushare Finance Skill - China Market Data for Agents](/hermes/skills/catalog/tushare-finance-skill-setup) - stanleychanh/tushare-finance-skill-for-claude-code, 5,157 combined, 1 listing, 79 stars, MIT, master branch, one skill wrapping 220+ Tushare Pro interfaces for A-share, Hong Kong and US equities, funds, futures, bonds and macro data behind a TUSHARE_TOKEN, with a Socket FAIL on the single listing and a README that claims Apache-2.0 where the LICENSE file says MIT

### New - November 1, 2026 Morning Sweep (14 publisher guides)

Fourteen repository clusters drained from the standing queue, documented for **179,773 combined installs across 476 indexed listings**:

- [Syncfusion Angular UI Skills - Vendor Component Pack](/hermes/skills/catalog/syncfusion-angular-ui-skills-setup) - 17,636 combined installs across 61 listings; 0 stars; no LICENSE file; Syncfusion's Angular component skills: one skill per component family for grid, scheduler, Gantt, charts and editors, 65 SKILL.md directories against 61 listings, with the commercial component licence separate from the skill files
- [ChatGPT Skills - 12-Suite Deterministic Toolkit](/hermes/skills/catalog/chatgpt-skills-setup) - 16,721 combined installs across 106 listings; 126 stars; no LICENSE file; twelve shipped suites for OCR document processing, spreadsheets, file conversion and research work behind 106 indexed listing names, so most rows name capability with nothing to install
- [Huashu Skills - 22-Skill Content Production Pack](/hermes/skills/catalog/huashu-skills-setup) - 16,023 combined installs across 37 listings; 2147 stars; MIT; 22 Chinese-first content production skills for HTML-first design, markdown to PDF, social cards and video scripting, against 37 listings that include 15 older names for skills already covered
- [VectorBT Backtesting Skills - Quant Workflow Setup](/hermes/skills/catalog/vectorbt-backtesting-skills-setup) - 15,152 combined installs across 6 listings; 217 stars; no LICENSE file; six quant backtesting skills over vectorbt, from data loading and indicator setup through portfolio construction and walk-forward evaluation, one directory per listing
- [Slack Skills Plugin - MCP Plus Nine Slack Skills](/hermes/skills/catalog/slack-skills-plugin-setup) - 15,188 combined installs across 9 listings; 163 stars; MIT; official Slack package: a hosted Slack MCP server plus nine skills split between using Slack and building on it, with Snyk W012 on the two skills that fetch live docs at task time
- [QwenCloud AI Skills - Multimodal Suite Setup](/hermes/skills/catalog/qwencloud-ai-setup) - 15,120 combined installs across 10 listings; 44 stars; Apache-2.0; Qwen Cloud multimodal skills for vision, OCR, speech and image generation through the cloud API, ten directories behind ten listings
- [Full Stack Skills - 788-Skill Catalog for Agents](/hermes/skills/catalog/full-stack-skills-setup) - 14,932 combined installs across 102 listings; 718 stars; Apache-2.0; a navigation hub for 788 skill entries across 51 separately installable packages since the June 2026 split, so this repository is the directory rather than the install source
- [Supabase Pentest Skills - 24-Skill Audit Suite](/hermes/skills/catalog/supabase-pentest-skills-setup) - 13,050 combined installs across 25 listings; 73 stars; NOASSERTION; 24 Supabase security-audit skills led by RLS and auth checks, where the README read-only claim is qualified because one skill creates a test user and the evidence directory holds sampled rows
- [Startup OS Skills - Sales, Product and Video Pack](/hermes/skills/catalog/startup-os-skills-setup) - 12,860 combined installs across 53 listings; 53 stars; no LICENSE file; 54 startup operating skills across sales, product, marketing and video, one directory per listing plus one unindexed directory
- [AgentMail Skills - Agent Email Inbox Setup](/hermes/skills/catalog/agentmail-skills-setup) - 10,705 combined installs across 11 listings; 25 stars; no LICENSE file; AgentMail email skills for inbox provisioning, send and receive, MCP configuration and framework adapters, with two deprecated alias listings inflating the total and Snyk W011 on the two package-install skills
- [Awesome Android Agent Skills - Compose and Kotlin Setup](/hermes/skills/catalog/awesome-android-agent-skills-setup) - 9,948 combined installs across 18 listings; 998 stars; Apache-2.0; 17 Android skills under .github/skills covering Compose, coroutines, ViewModel, architecture, migration, testing and accessibility, plus an Agent.md that every agent reads implicitly
- [Shenzjd Skills - DevOps and AI Image Pack](/hermes/skills/catalog/shenzjd-skills-setup) - 7,887 combined installs across 16 listings; 4 stars; MIT; eight DevOps and AI image directories behind 16 listings, with a Snyk FAIL (E005) on the two skills that write executable workflow and hook files
- [Robust Skills - Architecture and Platform Suite](/hermes/skills/catalog/robust-skills-setup) - 7,780 combined installs across 12 listings; 61 stars; MIT; architecture and platform skills for DDD, hexagonal boundaries, contract-first APIs and state ownership, eleven directories plus one index-only listing
- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup) - 6,771 combined installs across 10 listings; 3094 stars; Apache-2.0; market analysis skills for news sentiment, alpha research and factor work, with Snyk W011 and W012 on the two skills that reach the network for live market data

### New - October 31, 2026 Evening Sweep (16 publisher guides)

Sixteen repository clusters drained from the same queue the morning fire worked, documented for **332,009 combined installs across 515 indexed listings**:

- [Awesome Codex Skills - Curated Codex Index](/hermes/skills/catalog/composio-awesome-codex-skills-setup) - 24,951 combined installs across 61 listings; 17,150 stars; no LICENSE file; 880 in-tree SKILL.md directories behind 61 listings, a curated index drawn from many publishers with a Snyk Warn on three sampled entries
- [CXUU Golang Skills - Go Engineering Suite](/hermes/skills/catalog/cxuu-golang-skills-setup) - 24,917 combined installs across 20 listings; 188 stars; Apache-2.0; Go skills covering concurrency, interfaces, testing and module layout, one directory per listing, with a Trust Hub Warn on the sampled go-interfaces skill
- [9arm Skills - Thai Dev Agent Suite](/hermes/skills/catalog/9arm-skills-setup) - 24,419 combined installs across 6 listings; 3,244 stars; no LICENSE file; six skills from a single practitioner portfolio led by scrutinize at 5,233 installs, one directory per listing
- [Neo4j Skills - Graph Database Agent Suite](/hermes/skills/catalog/neo4j-skills-setup) - 24,115 combined installs across 32 listings; 119 stars; MIT; thirty Neo4j skills across Cypher, modelling, imports, GraphRAG, five drivers, GDS, Aura, Kafka and Spark, plugin manifests for four harnesses, two listings with no directory, and a licence that reads MIT in the file but Apache-2.0 in the manifests
- [CC DevOps Skills - Kubernetes and IaC Suite](/hermes/skills/catalog/cc-devops-skills-setup) - 22,236 combined installs across 31 listings; 330 stars; Apache-2.0; 31 DevOps skills across Kubernetes, Terraform, CI and log tooling, where ansible-validator warns on Gen Agent Trust Hub, Socket and Snyk
- [Aaronontheweb Dotnet Skills - Akka.NET Suite](/hermes/skills/catalog/aaronontheweb-dotnet-skills-setup) - 21,954 combined installs across 40 listings; 1,244 stars; MIT; Akka.NET and .NET engineering skills against 39 directories, a separate repository from the official dotnet/skills suite already in the catalog, with one Snyk Warn in the sample
- [Gemini CLI Skills - Repository Workspace Pack](/hermes/skills/catalog/gemini-cli-skills-setup) - 21,729 combined installs across 19 listings; 108,637 stars; Apache-2.0; Google's own CLI monorepo where the listings sit under .gemini/skills and the packages builtins rather than a top-level skills tree, with two Snyk Warns in the sample
- [ast-grep Skill - Structural Code Search](/hermes/skills/catalog/ast-grep-agent-skill-setup) - 20,794 combined installs across 2 listings; 900 stars; no LICENSE file; two skills only, ast-grep at 18,303 and outline at 2,491, carrying 20,794 installs between them
- [Metabase Skills - BI and Dashboard Agent Suite](/hermes/skills/catalog/metabase-skills-setup) - 20,284 combined installs across 28 listings; 50,069 stars; NOASSERTION; skills split across resources/mcp/v2/skills and .claude/skills inside a 50,069-star analytics monorepo, five data-app listings with no directory, one Snyk Warn
- [Academic Writing Skills - Paper Workflow](/hermes/skills/catalog/academic-writing-skills-setup) - 18,655 combined installs across 11 listings; 528 stars; no LICENSE file; academic writing skills led by latex-paper-en at 5,973 installs, with one listing that has no directory
- [Modular Skills - Mojo and MAX Agent Suite](/hermes/skills/catalog/modular-skills-setup) - 18,312 combined installs across 12 listings; 207 stars; NOASSERTION; Mojo and MAX skills in eleven directories, where the GitHub licence field reads NOASSERTION over an Apache 2.0 file with LLVM exceptions
- [Guard Skills - Code Safety Review Pack](/hermes/skills/catalog/guard-skills-setup) - 18,122 combined installs across 5 listings; 1,301 stars; MIT; five guardrail review skills led by clean-code-guard at 4,746 installs, five listings against five directories and every sampled verdict a Pass
- [Catalyst by Zoho Skills - Serverless Suite](/hermes/skills/catalog/catalystbyzoho-agent-skills-setup) - 17,987 combined installs across 19 listings; 70 stars; Apache-2.0; Zoho Catalyst serverless skills covering functions, data store, auth and deployment, one directory per listing, with Warns on the 36-install tail listing
- [ClaudeKit Skills - Full Stack Agent Toolkit](/hermes/skills/catalog/claudekit-skills-setup) - 17,978 combined installs across 33 listings; 2,230 stars; no LICENSE file; 45 SKILL.md directories under .claude/skills covering document work, UI styling, MCP building and code review, with one listing and one directory that do not pair
- [Awesome Ecommerce Skills - Commerce Index](/hermes/skills/catalog/awesome-ecommerce-skills-setup) - 17,780 combined installs across 178 listings; 60 stars; MIT; a flat install curve against 181 in-tree directories, where the top 20 sit at or above 144 installs and the leader reads 301
- [Layers Skills - Design System Agent Pack](/hermes/skills/catalog/layers-skills-setup) - 17,776 combined installs across 18 listings; 314 stars; MIT; nine design-system directories behind 18 listings, with nine bare-name listings at 1 to 2 installs that have no directory

### New - October 31, 2026 Morning Sweep (16 publisher guides)

Sixteen repository clusters from the queue the October 30 evening probe left behind, documented for **536,147 combined installs across 835 indexed listings**:

- [Jaganpro SF Skills - Salesforce Agent Suite](/hermes/skills/catalog/jaganpro-sf-skills-setup) - 43,852 combined installs across 46 listings; 424 stars; MIT; Apex, LWC, Flow, SOQL, metadata, deploy and Agentforce skills scored against fixed point budgets, where the repository is archived with a documented successor at forcedotcom/afv-library and nine indexed names have no directory
- [Anti-Slop - AI Copywriting Quality Skill](/hermes/skills/catalog/anti-slop-setup) - 41,307 combined installs across 6 listings; 7,670 stars; MIT; Six skills that strip generic AI tells from UI, copy, mobile layout and code comments, with a contrast checker script, a Hermes-aware installer and a Trust Hub Warn on the core skill the others reference
- [Browserbase Skills - Agent Browser Automation](/hermes/skills/catalog/browserbase-skills-setup) - 40,127 combined installs across 20 listings; 3,747 stars; no LICENSE file; the official Browserbase suite: sessions, fetch, search, tracing, UI testing and agent functions, where one sampled skill fails Gen Agent Trust Hub
- [JEO Skills - Presentation and Document Suite](/hermes/skills/catalog/jeo-skills-setup) - 37,915 combined installs across 112 listings; 53 stars; no LICENSE file; a 112-listing flat .agent-skills tree weighted toward presentations and office deliverables, where rtk fails Gen Agent Trust Hub and the guide leads with it
- [CCFA Skills - Academic Paper and Research Suite](/hermes/skills/catalog/ccfa-skills-setup) - 33,935 combined installs across 24 listings; 3,358 stars; MIT; academic paper work across 24 listings: literature search, LaTeX templates for 141 venues, reviewer simulation and rebuttal, with six indexed names that have no directory
- [TanStack Agent Skills - Query and Router Setup](/hermes/skills/catalog/deckardger-tanstack-agent-skills-setup) - 32,849 combined installs across 4 listings; 228 stars; MIT; TanStack Query, Router, Start and integration conventions as four skills, each with a rules folder of numbered documents, all sampled verdicts clean
- [Chris Banes Skills - Compose and Kotlin Suite](/hermes/skills/catalog/chrisbanes-skills-setup) - 32,776 combined installs across 35 listings; 1,133 stars; Apache-2.0; Compose, coroutines, Gradle and Kotlin Multiplatform skills from a Compose maintainer, 20 directories against 35 indexed names with a README migration table covering 13 of the gaps
- [Paul Berg Agent Skills - Solidity and Foundry](/hermes/skills/catalog/paulrberg-agent-skills-setup) - 32,742 combined installs across 97 listings; 104 stars; MIT; Solidity and Foundry engineering skills plus code polish, commit and dependency-bump tooling over 43 directories against 97 indexed listings
- [Maggy Skills - Android and Kotlin Agent Suite](/hermes/skills/catalog/maggy-skills-setup) - 32,037 combined installs across 73 listings; 710 stars; MIT; 73 Android and Kotlin skills with 25 slash commands, 13 hooks, 9 conditional rules and a Cortex MCP server, every indexed listing present in the tree
- [SAP Skills - BTP, CAP and ABAP Agent Suite](/hermes/skills/catalog/sap-skills-setup) - 31,778 combined installs across 45 listings; 482 stars; GPL-3.0; SAP BTP, CAP, ABAP and integration skills, 40 of them shipped as plugins with their own commands, agents and marketplace manifest
- [Tencent CloudBase Agent Skills - WeChat Dev](/hermes/skills/catalog/tencent-cloudbase-agent-skills-setup) - 30,797 combined installs across 37 listings; 80 stars; MIT; WeChat mini-program and CloudBase skills from Tencent, a separate repository from the cloudbase-skills guide already in the catalog, with one Snyk Fail inside the sample
- [OrchestKit - Orchestration and DevOps Skills](/hermes/skills/catalog/orchestkit-skills-setup) - 30,386 combined installs across 151 listings; 300 stars; MIT; 115 orchestration and delivery skills with 161 hooks, 36 agents and a build mirror of the same skill set, aimed at plan, deploy, review and release gates
- [Cypress AI Toolkit - E2E Testing Skills](/hermes/skills/catalog/cypress-ai-toolkit-setup) - 30,426 combined installs across 5 listings; 46 stars; MIT; the official Cypress end-to-end testing toolkit as five skills plus a streamable-http MCP endpoint, with Snyk Warns on the authoring and cloud skills
- [Asyraf Hussin Skills - Clean Code Suite](/hermes/skills/catalog/asyrafhussin-agent-skills-setup) - 29,010 combined installs across 24 listings; 95 stars; MIT; 24 engineering-standards skills, each with a rules folder and metadata, carrying no scripts and no hooks, with one Socket Warn in the sample
- [Tigris Data Skills - Object Storage for Agents](/hermes/skills/catalog/tigrisdata-skills-setup) - 28,128 combined installs across 19 listings; 2 stars; MIT; Tigris object storage as 19 skills, where all 18 directories are paired with a .zip distribution package and the sample carries one Socket Warn
- [Xiaohongshu Skills - RED Content Operations](/hermes/skills/catalog/xiaohongshu-skills-setup) - 28,082 combined installs across 137 listings; 515 stars; no LICENSE file; 137 RED content-operation skills in nine Chinese-named category folders, with three disagreeing counts between the README, the plugin manifest and the tree

### New - October 30, 2026 Evening Sweep (16 publisher guides)

Sixteen publisher clusters from a 68-query topic probe, the largest install weight this catalog has recorded for a single fire: **1,101,389 combined installs across 1,717 indexed listings**.

- [Text to CAD Skills - 3D Model and URDF Setup](/hermes/skills/catalog/text-to-cad-skills-setup) - 124,096 combined installs across 18 listings; 24,377 stars; MIT; text-to-CAD and URDF generation with a viewer and a robot-motion skill, six indexed listings with no directory at main
- [Context Engineering Kit - Prompt and MCP Setup](/hermes/skills/catalog/context-engineering-kit-setup) - 110,374 combined installs across 138 listings; 1,795 stars; GPL-3.0; prompt engineering, context engineering and agent workflow patterns across 204 SKILL.md files on a master branch
- [Science Skills - PubMed, arXiv and Lab Data Setup](/hermes/skills/catalog/science-skills-setup) - 87,871 combined installs across 42 listings; 3,363 stars; Apache-2.0; Google DeepMind science skills for literature search, genomics, structural biology and chemistry, every retrieval step delegated to bundled uv scripts
- [SecondSky Claude Skills - Backend and API Suite Setup](/hermes/skills/catalog/secondsky-claude-skills-setup) - 85,061 combined installs across 200 listings; 240 stars; MIT; the largest single-owner Claude skill collection in this batch, 187 SKILL.md files across 145 plugin directories
- [Adobe Skills - PDF, Document and Creative Suite Setup](/hermes/skills/catalog/adobe-skills-setup) - 76,451 combined installs across 137 listings; 318 stars; Apache-2.0; Adobe product skills for AEM, Creative Cloud, Commerce, Analytics and the document skills, 178 SKILL.md files in per-product plugins
- [Jwynia Agent Skills - Presentation and Writing Suite](/hermes/skills/catalog/jwynia-agent-skills-setup) - 65,356 combined installs across 119 listings; 180 stars; no LICENSE file at root; presentation design, writing and research skills from a single author, one directory for every indexed listing
- [ByteDance MediaKit CLI - Video Processing Setup](/hermes/skills/catalog/mediakit-cli-skills-setup) - 61,321 combined installs across 5 listings; 218 stars; MIT; ByteDance MediaKit as five skills over a CLI for audio, video, image and editing pipelines, all five inside 38 installs of each other
- [DeerFlow Skills - Deep Research Agent Setup](/hermes/skills/catalog/deer-flow-skills-setup) - 60,292 combined installs across 26 listings; 84,743 stars; MIT; the skills that ship inside the ByteDance deep research harness, most of them for working with the harness itself
- [LinkFox Skills - IP, Legal and Trade Data Setup](/hermes/skills/catalog/linkfox-skills-setup) - 58,424 combined installs across 200 listings; 115 stars; MIT; cross-border ecommerce and IP data skills for patents, trademarks, Amazon, Ozon and 1688, 270 SKILL.md files with Chinese descriptions throughout
- [Application Skills - SaaS Integration Suite Setup](/hermes/skills/catalog/application-skills-setup) - 57,985 combined installs across 200 listings; 270 stars; no LICENSE file at root; Membrane managed-integration skills, 3,074 flat directories of about 173 lines each, every one requiring a Membrane account
- [Patricio Skills - Full Stack Engineering Suite Setup](/hermes/skills/catalog/patricio-skills-setup) - 56,693 combined installs across 153 listings; 63 stars; MIT; 155 markdown skills in ten discipline folders from scaffolding through animation, API design, CI/CD, testing and AI engineering
- [Apollo GraphQL Skills - GraphQL and Rust Setup](/hermes/skills/catalog/apollographql-skills-setup) - 56,575 combined installs across 15 listings; 123 stars; MIT; official GraphQL skills for Apollo Client, Federation, Router, GraphOS and schema work, plus a general Rust style guide at the top of the install table
- [Patterns.dev Skills - UI and Rendering Patterns Setup](/hermes/skills/catalog/patterns-dev-skills-setup) - 53,715 combined installs across 58 listings; 258 stars; no LICENSE file at root; design and rendering pattern cards for JavaScript, React and Vue, one directory for every indexed listing, idle since April 2026
- [Scenario Labs Skills - Custom Model Training Setup](/hermes/skills/catalog/scenario-labs-skills-setup) - 53,338 combined installs across 173 listings; 1,284 stars; MIT; game and creative asset generation skills over the Scenario platform, 174 skill directories including a Blender expert and consistency tooling
- [Android Skills - Play Policy and App Quality Setup](/hermes/skills/catalog/android-skills-setup) - 48,501 combined installs across 35 listings; 10,111 stars; Apache-2.0; Google's official Android skills for Play policy, edge-to-edge, navigation, R8 and app quality, 36 SKILL.md files across 18 domain folders
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup) - 45,336 combined installs across 198 listings; 585 stars; MIT; DevOps and delivery skills numbered ln-1xx to ln-8xx inside plugin suites, 41 SKILL.md files against 198 indexed listings
### New - October 30, 2026 Morning Sweep (19 publisher guides)

Nineteen repository-scoped clusters drained from the queue the October 29 evening probe left behind, for **345,882 combined installs across 264 indexed listings**:

- [Remotion Framework Skills - Programmatic Video Setup](/hermes/skills/catalog/remotion-framework-skills-setup) - 47,489 combined installs across 73 listings; 69,018 stars; NOASSERTION while LICENSE.md carries the two-tier Remotion License; the React video framework's own skill library: 13 public skills around a router plus 63 internal maintainer skills, 88 `SKILL.md` files in three layouts, and four indexed names with no directory at main
- [Auth0 Agent Skills - Identity and OAuth Setup](/hermes/skills/catalog/auth0-agent-skills-setup) - 28,077 combined installs across 47 listings; 55 stars; Apache-2.0; official Auth0 identity skill consolidated into a single skill and a 144-file reference set, against 47 indexed per-framework names that are the retired ones
- [Upstash Context7 - Versioned Library Docs Setup](/hermes/skills/catalog/upstash-context7-setup) - 25,472 combined installs across 8 listings; 63,945 stars; MIT; Context7 documentation retrieval as four skills over the cx7 CLI and the remote MCP endpoint, master branch, with three listings that have no directory in the tree
- [Svelte AI Tools - Official Svelte and SvelteKit Setup](/hermes/skills/catalog/svelte-ai-tools-setup) - 24,570 combined installs across 2 listings; 335 stars; MIT; the official Svelte MCP in two skills, `svelte-code-writer` and `svelte-core-bestpractices`, shipped across five harness layouts with a static autofixer CLI
- [Prisma Next Skills - Typed Database Access Setup](/hermes/skills/catalog/prisma-next-skills-setup) - 23,921 combined installs across 40 listings; 411 stars; Apache-2.0; Prisma Next as 13 published skills plus 18 contributor skills, with migration review, upgrade walkthroughs and per-transition codemods
- [Axiom Skills - Observability and Event Queries Setup](/hermes/skills/catalog/axiom-skills-setup) - 23,872 combined installs across 15 listings; 17 stars; MIT; official Axiom observability skills for APL queries, dashboards, alerting, SPL conversion and cost control, where v1.2.0 renamed the skills with an `axiom-` prefix
- [Lavish AXI - Agent Experience Interface Setup](/hermes/skills/catalog/lavish-axi-setup) - 23,474 combined installs across 3 listings; 4,358 stars; MIT; one agent-facing UI skill backed by a CLI: a design vocabulary, hook and plugin targets, and a publish path to a hosted page
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup) - 19,509 combined installs across 1 listing; 82 stars; no licence file; a four-adversary review protocol with a synthesis pass that turns competing critiques of a spec or plan into one decision list
- [Pulumi Agent Skills - Infrastructure as Code Setup](/hermes/skills/catalog/pulumi-agent-skills-setup) - 16,370 combined installs across 17 listings; 78 stars; Apache-2.0; official Pulumi IaC skills in four plugin groups: authoring and ESC secrets, five migration converters for Terraform, CDK, CloudFormation, ARM and Bicep, provider maintenance and Neo handoff
- [components.build - UI Component Standards Setup](/hermes/skills/catalog/vercel-components-build-setup) - 14,813 combined installs across 1 listing; 802 stars; NOASSERTION while the LICENSE file is Apache-2.0 and the README says MIT; the components.build specification as a skill: 16 spec pages, 19 languages of translations and an accessibility reference set
- [Kapso Agent Skills - WhatsApp Business Setup](/hermes/skills/catalog/gokapso-agent-skills-setup) - 13,788 combined installs across 9 listings; 195 stars; no licence file; Kapso WhatsApp Business skills for integration, automation, calls and observability, master branch, with five indexed listings that have no directory
- [Dotneet Claude Code Marketplace - Plugin Collection Setup](/hermes/skills/catalog/dotneet-claude-code-marketplace-setup) - 12,917 combined installs across 10 listings; 3 stars; no licence file; a six-plugin marketplace for review, prompt improvement and agent session work, where `call-claude` fails Snyk and the guide leads with it
- [Swift Concurrency Skill - Structured Concurrency Setup](/hermes/skills/catalog/swift-concurrency-skill-setup) - 12,209 combined installs across 1 listing; 578 stars; MIT; twostraws' Swift 6 concurrency expert: tasks, actors and isolation, with 12 reference files covering hotspots, diagnostics and migration
- [Vectorize Hindsight Skills - Agent Memory Setup](/hermes/skills/catalog/vectorize-hindsight-skills-setup) - 11,470 combined installs across 15 listings; 56,373 stars; MIT; agent memory as 20 skills plus a first-class Hermes memory-provider plugin, with self-hosted and cloud deployment paths
- [Amazon Devices Agent Skills - Fire TV and Vega Setup](/hermes/skills/catalog/amazon-devices-agent-skills-setup) - 10,978 combined installs across 2 listings; 6 stars; MIT; Amazon's own Fire TV and Vega skills: a five-phase multi-TV migration with templates and a validation checklist, plus React Native TV UI rules
- [Vinta Django AI Plugins - Django and Celery Setup](/hermes/skills/catalog/vintasoftware-django-ai-plugins-setup) - 8,390 combined installs across 5 listings; 166 stars; no licence file; Django and Celery experts with safe-migration and reviewer skills from a Django consultancy, five skills over ten `SKILL.md` files
- [Vercel Chat SDK Skills - Chat Bot Development Setup](/hermes/skills/catalog/vercel-chat-sdk-skills-setup) - 6,118 combined installs across 3 listings; 2,434 stars; MIT; the Chat SDK and its adapter-writing workflow, with four byte-identical `SKILL.md` copies and a published agent-skills index
- [Better Icons - Icon Search Skill Setup](/hermes/skills/catalog/better-auth-better-icons-setup) - 6,047 combined installs across 1 listing; 1,445 stars; MIT; icon search and selection as one skill over a CLI with preferences, history and a library-wide naming convention
- [Google ADK Docs - Agent Development Kit Setup](/hermes/skills/catalog/google-adk-docs-setup) - 16,398 combined installs across 11 listings; 1,530 stars; Apache-2.0; Google's Agent Development Kit documentation as six skills covering the dev guide, cheatsheet, evaluation, deployment, streaming and observability, where the indexed names outrun the tree

### New - October 29, 2026 Evening Sweep (12 publisher guides)

Twelve publisher clusters found by a widened 47-query topic probe after the standing window (top row 295) and the trending board (600 entries, 77 sources, all covered) both came back empty, for **821,254 combined installs across 372 indexed listings**:

- [Elastic Agent Skills - Elasticsearch and Kibana Suite](/hermes/skills/catalog/elastic-agent-skills-setup) - 128,923 combined installs across 54 listings; 603 stars; Apache-2.0; the official Elastic suite where 62 in-tree files are 31 skills mirrored across two trees, and 23 indexed names were removed in v0.6.0 while still carrying install counts
- [claude-mem - Persistent Memory for Coding Agents Setup](/hermes/skills/catalog/claude-mem-setup) - 101,470 installs across 34 listings; 104,989 stars; Apache-2.0; session history compressed into a searchable memory store, with search, explore, plan and report skills on top of it
- [Claude Ads - Paid Media Skill Suite Setup](/hermes/skills/catalog/claude-ads-setup) - 98,745 installs across 34 listings; 10,586 stars; MIT; a conductor plus per-platform specialists for Meta, Google, TikTok, X, Amazon and Apple, with the Snyk warns on the skills that touch live ad accounts
- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup) - 97,018 installs across 100 listings; 14,111 stars; MIT; 98 atomic ML research skills across eleven numbered topic directories, installed a category at a time by a CLI whose positional argument matches category ids
- [K2F - Document Generation Skills Setup](/hermes/skills/catalog/k2f-setup) - 62,502 installs across 42 listings; 3 stars; Apache-2.0; semantic JSON compiled into Word, PowerPoint, fillable PDF and IDML, with a schema, a template catalog and a pack verifier behind the core skill
- [Roblox Brain - Roblox Studio Development Skills Setup](/hermes/skills/catalog/roblox-brain-setup) - 61,628 installs across 37 listings; 143 stars; MIT; 29 Roblox Studio skills covering Luau, architecture, building, lighting, animation, GUI, economy, testing and publishing, with a FAIL on the testing listing the guide leads with
- [Bailian CLI - Alibaba Model Studio Agent Skills Setup](/hermes/skills/catalog/modelstudio-cli-setup) - 59,841 installs across 9 listings; 366 stars; Apache-2.0; Alibaba Cloud's own `bl` CLI taught by nine skills for generation, fine-tuning, managed agents, web search and knowledge bases, documented from INSTALL.md because the README carries no skills commands
- [Coralogix cx CLI - Observability Agent Skills Setup](/hermes/skills/catalog/coralogix-cx-cli-setup) - 58,206 installs across 32 listings; 233 stars; Apache-2.0; 19 end-user observability skills plus four contributor-only skills under `.claude/skills/` that must never be presented as product skills; master branch
- [Sent Plugin - Messaging and Verification Skills Setup](/hermes/skills/catalog/sent-plugin-setup) - 54,176 installs across 21 listings; 49 stars; MIT; SMS, WhatsApp and RCS messaging, compliance and migration in 84 files that are the same 21 skills across four adapter layouts, with a 27-tool remote MCP endpoint
- [Base44 Skills - AI App Builder Platform Suite Setup](/hermes/skills/catalog/base44-skills-setup) - 51,043 installs across 6 listings; 92 stars; MIT; SDK, CLI, remote dev, sandbox and production troubleshooting for the platform, on pre-release manifests with one plugin's skills dir shipped as a git symlink
- [SwiftUI Agent Skill - Apple UI Development Setup](/hermes/skills/catalog/avdlee-swiftui-agent-skill-setup) - 37,853 installs across 2 listings; 3,791 stars; MIT; the batch's only Production-tier guide, all verdicts Pass: one expert skill with 33 reference files and a checklist, plus an Apple docs rescan skill under a soft-deprecation rule
- [Slack CLI Skill - Agent-Driven Workspace Automation Setup](/hermes/skills/catalog/paymog-slack-cli-setup) - 9,849 installs across 1 listing; 0 stars; MIT; a Go CLI giving agents JSON reads and writes on a workspace without a resident MCP server, from the publisher behind the Groundcover and incident.io CLI guides

### New - October 29, 2026 Morning Sweep (10 publisher guides)

Ten publisher clusters documented from the queue the previous fire left behind, plus one find the trending board understated 66x, for **109,244 combined installs across 14 indexed listings**:

- [Transitions.dev Skills - CSS Motion Suite Setup](/hermes/skills/catalog/transitions-dev-setup) - 34,026 combined installs across 5 listings; 5,888 stars; crafted CSS transitions, a polish skill and a generation reveal, from a repository that is the product website as well as the skills; non-OSI licence
- [NotebookLM - Unofficial Gemini Notebook CLI and Skill Setup](/hermes/skills/catalog/notebooklm-py-setup) - 9,973 installs; 19,968 stars; MIT; an unofficial Python API and CLI for Google Gemini Notebook wrapped in one agent operating contract
- [PDF Converter (MinerU) - PDF to Markdown Skill Setup](/hermes/skills/catalog/pdf-converter-mineru-setup) - 9,620 installs; 55 stars; no licence file; a thin instruction file over the MinerU Open API CLI, and the weakest security profile in the batch with two auditor FAILs
- [Unlazy - Completion Gates and Depth Tree Setup](/hermes/skills/catalog/unlazy-setup) - 9,609 installs; 4,168 stars; MIT; a gate ledger with runnable CHECK and EXPECT pairs, approval bound to the exact command, and the Depth Tree decomposition
- [Groundcover CLI - Observability API Setup Guide](/hermes/skills/catalog/groundcover-cli-setup) - 9,602 installs; 1 star; MIT; a Go CLI plus a 512-line skill for Groundcover dashboards, monitors, logs, traces and Kubernetes queries, with a Gen Agent Trust Hub FAIL the guide leads with
- [incident.io CLI - Incident and On-Call API Setup](/hermes/skills/catalog/incidentio-cli-setup) - 9,298 installs; 0 stars; no licence file; 324 OpenAPI-generated commands and the batch's only Snyk FAIL, on credential handling
- [Elestio Skill - Managed DevOps Deployment Setup](/hermes/skills/catalog/elestio-skill-setup) - 7,467 installs; 1 star; no licence file; the vendor's own managed hosting skill with a 24-row CLI-to-MCP map and a Trust Hub FAIL on an infrastructure-granting file
- [Chrome DevTools AXI - Agent Browser CLI Setup](/hermes/skills/catalog/chrome-devtools-axi-setup) - 7,072 installs; 445 stars; MIT; a snapshot-first CLI over the Chrome DevTools Protocol with stale-reference checks and performance traces
- [Playwright Skill - Code-First Browser Automation Setup](/hermes/skills/catalog/playwright-skill-setup) - 7,056 installs; 3,250 stars; MIT; the agent writes and runs real Playwright programs, with dev-server detection and CDP attach, from a different publisher than the TestDino guide
- [Autopilot Skill - End-to-End Build Orchestration Setup](/hermes/skills/catalog/nick-vels-skills-setup) - 5,521 installs; 564 stars; MIT; a dictated idea through eight build stages to blind acceptance, and the only three-pass verdict set in the batch

### New - October 28, 2026 Evening Sweep (12 publisher guides)

- [Pilio Skills - Image and PDF Utility API Skills Setup](/hermes/skills/catalog/pilioai-skills-setup)
- [QianWen AI Skills - Alibaba Qwen Multimodal Suite Setup](/hermes/skills/catalog/qianwen-ai-setup)
- [NestJS Best Practices - 40-Rule Agent Skill Setup Guide](/hermes/skills/catalog/agent-nestjs-skills-setup)
- [Ejiro Agent Skills - Svelte, Vue, NestJS and Exa Setup](/hermes/skills/catalog/ejirocodes-agent-skills-setup)
- [Java Development Plugin - 12-Skill Java Engineering Setup](/hermes/skills/catalog/custom-plugin-java-setup)
- [Proactive Agent - WAL Memory and Compaction Recovery Setup](/hermes/skills/catalog/proactive-agent-setup)
- [Kami - PDF, PNG and Editable PPTX Layout Skill Setup](/hermes/skills/catalog/kami-setup)
- [ego lite - AI Agent Browser and ego-browser Skill Setup](/hermes/skills/catalog/ego-lite-setup)
- [Refero Design - Research-First UI Design Skill Setup](/hermes/skills/catalog/refero-design-setup)
- [OpenCode Workflows - Command and Agent Template Suite Setup](/hermes/skills/catalog/opencode-workflows-setup)
- [Fallow Skills - Codebase Intelligence for TS and JS Setup](/hermes/skills/catalog/fallow-rs-fallow-skills-setup)
- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)

### New - October 28, 2026 Morning Sweep (9 publisher guides)

- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [BMad Method Skills - Agile AI Development Suite Setup](/hermes/skills/catalog/bmad-method-setup)
- [PStack Skills - Engineering Discipline Suite Setup](/hermes/skills/catalog/pstack-setup)
- [PixiJS Skills - 2D WebGL and WebGPU Rendering Suite Setup](/hermes/skills/catalog/pixijs-skills-setup)
- [MSW AI Coding Plugins - MapleStory Worlds Suite Setup](/hermes/skills/catalog/msw-ai-coding-plugins-setup)
- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)
- [PriceWin Skills - Hotel Deal and Flight Search Setup](/hermes/skills/catalog/pricewin-skills-hub-setup)
- [365 Skills - Diagram, Research and Media Suite Setup](/hermes/skills/catalog/agents365-skills-setup)
- [OpenSEO - Self-Hosted SEO Platform, MCP and Skills Setup](/hermes/skills/catalog/open-seo-setup)

### New - October 27, 2026 Evening Sweep (9 publisher guides)

- [Capgo Skills - Capacitor Mobile Release Suite Setup](/hermes/skills/catalog/capgo-skills-setup)
- [Agent Skills - UI, Design and Shipping Suite Setup](/hermes/skills/catalog/mblode-agent-skills-setup)
- [Ship Shit Dev Skills - 14 Command Routers Setup](/hermes/skills/catalog/shipshitdev-skills-setup)
- [Sumsub Agent Skills - KYC and AML Platform Setup](/hermes/skills/catalog/sumsub-agent-skills-setup)
- [Qdrant Skills - Vector Search, Retrieval and Memory Setup](/hermes/skills/catalog/qdrant-skills-setup)
- [Customware Skills - Low-Code App Builder Suite Setup](/hermes/skills/catalog/customware-ai-skills-setup)
- [Liquid Skills - Shopify Theme Standards and A11y Setup](/hermes/skills/catalog/liquid-skills-setup)
- [Claude Code Next.js Skills - Next.js 16 and AI SDK Setup](/hermes/skills/catalog/claude-code-nextjs-skills-setup)
- [Melodic Software Claude Code Plugins - Marketplace Setup](/hermes/skills/catalog/melodic-claude-code-plugins-setup)

### New - October 27, 2026 Morning Sweep (5 publisher guides)

- [Anthropic Financial Services Skills - Deal Workflow Suite](/hermes/skills/catalog/anthropics-financial-services-setup)
- [Motion Design Skills - After Effects and Remotion Setup](/hermes/skills/catalog/motion-design-skills-setup)
- [Astronomer Agents - Airflow Data Engineering Setup](/hermes/skills/catalog/astronomer-agents-setup)
- [Deep Agents - Batteries-Included Agent Harness Setup](/hermes/skills/catalog/deepagents-setup)
- [Pydantic Skills - Logfire and Pydantic AI Suite Setup](/hermes/skills/catalog/pydantic-skills-setup)

### New - November 2, 2026 Evening Sweep (11 publisher guides)

- [Reverse Engineering Skills - Frida and IDA Setup](/hermes/skills/catalog/p4nda0s-reverse-skills-setup)
- [YouTube Skills - Transcript API Suite for Agents](/hermes/skills/catalog/youtube-skills-setup)
- [Lynx Agent Skills - DevTool and ReactLynx Setup](/hermes/skills/catalog/lynx-community-skills-setup)
- [Supabase Server Skill - Edge Function Auth Setup](/hermes/skills/catalog/supabase-server-skills-setup)
- [TikTok Video Skills - Short-Form Video Suite Setup](/hermes/skills/catalog/tiktok-video-skills-setup)
- [Infisical AI Skills - Secrets Management Setup](/hermes/skills/catalog/infisical-ai-skills-setup)
- [Stageshow - Faux Product UI Skill Setup](/hermes/skills/catalog/benjitaylor-skills-setup)
- [Semgrep Skills - Secure Code and Static Analysis](/hermes/skills/catalog/semgrep-skills-setup)
- [NotebookLM nblm Skill - Source-Grounded Answers](/hermes/skills/catalog/magicseek-nblm-setup)
- [Cline SDK Skill - Build AI Agents on @cline/sdk](/hermes/skills/catalog/cline-sdk-skill-setup)
- [Next.js Cache Architecture - Setup Guide](/hermes/skills/catalog/nextjs-cache-architecture-setup)

### New - November 3, 2026 Evening Sweep (13 publisher guides)

Thirteen repository clusters surfaced by a widened 172-query topic probe plus one trending board find, documented for **461,248 combined installs across 634 indexed listings**:

- [OpenMontage - Video Production Studio for Agents](/hermes/skills/catalog/openmontage-setup) - calesthio/openmontage, 101,840 combined, 90 listings, 76,073 stars, AGPL-3.0, Video production for agents: cutting, captions, avatars, motion and rendered social clips through one studio suite
- [PostPlus Skills - Marketing Research and Publishing](/hermes/skills/catalog/postplus-skills-setup) - postplusai/postplus-skills, 46,456 combined, 82 listings, 27 stars, NOASSERTION, Marketing for agents: platform research, asset routing and campaign publishing across social channels
- [CC Blender Skill - 3D Production for Agents](/hermes/skills/catalog/cc-blender-skill-setup) - roble3/cc-blender-skill, 36,728 combined, 30 listings, 141 stars, MIT, Blender for agents: modeling, UV, materials, lighting, cameras, animation and export handled like a senior 3D artist
- [Oh My ClaudeCode - Agent Workflow Suite Setup](/hermes/skills/catalog/oh-my-claudecode-setup) - yeachan-heo/oh-my-claudecode, 36,471 combined, 98 listings, 40,550 stars, MIT, Agent orchestration: planning, parallel delegation, review, debugging and delivery skills for coding agents
- [Unreal Engine Skills - Game Dev Suite for Agents](/hermes/skills/catalog/unreal-engine-skills-setup) - quodsoler/unreal-engine-skills, 35,564 combined, 31 listings, 436 stars, MIT, Unreal Engine for agents: Blueprints, C++ gameplay, materials, animation and packaging guidance
- [Borghei Claude Skills - 385 Business Skill Library](/hermes/skills/catalog/borghei-claude-skills-setup) - borghei/claude-skills, 34,493 combined, 200 listings, 1,043 stars, NOASSERTION, Business operations for agents: pricing, churn, deal desk, partnerships, CRO and compliance audit skills
- [MiniMax CLI - Multimedia Generation for Agents](/hermes/skills/catalog/minimax-cli-setup) - minimax-ai/cli, 32,370 combined, 2 listings, 2,211 stars, no LICENSE file, Multimedia generation for agents: text, images, video and speech from the official MiniMax command line
- [Webflow Skills - Site Building for Agents Setup](/hermes/skills/catalog/webflow-skills-setup) - webflow/webflow-skills, 29,425 combined, 45 listings, 135 stars, MIT, Webflow for agents: CMS collections, components, accessibility audits and safe publishing through the Webflow MCP server
- [Stark AI Agent Skills - Engineering Workflow Kit](/hermes/skills/catalog/stark-ai-agent-skills-setup) - stark-ai-de/agent-skills, 29,204 combined, 15 listings, 8 stars, Apache-2.0, Engineering workflow for agents: PRDs, ADRs, repo maps, plan slicing, debugging and review-fix swarms
- [Coinbase Agentic Wallet - USDC Payments Skill](/hermes/skills/catalog/coinbase-agentic-wallet-setup) - coinbase/agentic-wallet-skills, 27,257 combined, 11 listings, 127 stars, MIT, Agent payments: sign in, read balances, send USDC and trade tokens through the Coinbase agentic wallet CLI
- [IART Web Animation Skills - GSAP and SVG Suite](/hermes/skills/catalog/iart-web-animation-skills-setup) - iart-ai/web-animation-skills, 26,178 combined, 9 listings, 76 stars, MIT, Web animation for agents: GSAP timelines, SVG and Lottie motion, micro-interactions and 60fps performance
- [HeyGen Skills - Avatar Video Production Setup](/hermes/skills/catalog/heygen-skills-setup) - heygen-com/skills, 20,185 combined, 15 listings, 538 stars, MIT, Avatar video for agents: creator avatars, scripted video generation and translation through the HeyGen v3 pipeline
- [Agent Desktop - Computer Use for Agents Setup](/hermes/skills/catalog/agent-desktop-setup) - vercel-labs/agent-desktop, 5,077 combined, 6 listings, 13,273 stars, Apache-2.0, Computer use for agents: see and drive macOS, Windows and Linux desktop apps through the OS accessibility tree

### New - November 3, 2026 Night Sweep (17 publisher guides)

- [Runpod Plugin - GPU Pod and Serverless Skill Setup](/hermes/skills/catalog/runpod-plugins-official-setup)
- [JSON Render - Generative UI Framework Setup](/hermes/skills/catalog/json-render-setup)
- [Turborepo Skill - Monorepo Build System Setup](/hermes/skills/catalog/turborepo-skill-setup)
- [LobeHub Skills - Agent Platform Engineering Setup](/hermes/skills/catalog/lobehub-skills-setup)
- [JS Mastery Skills - Agentic Development Workflow](/hermes/skills/catalog/jsmastery-skills-setup)
- [Agent Device - Mobile Device Control for Agents](/hermes/skills/catalog/agent-device-setup)
- [Game Dev Agentic Skills - Godot and Bevy Suite](/hermes/skills/catalog/game-dev-agentic-skills-setup)
- [Understand Anything - Code to Knowledge Graph Setup](/hermes/skills/catalog/understand-anything-setup)
- [React Doctor - React Codebase Diagnostics Setup](/hermes/skills/catalog/react-doctor-setup)
- [Hairyf Skills - Vue, Nuxt and Tooling Collection](/hermes/skills/catalog/hairyf-skills-setup)
- [MAD Agents Skills - Dart and Flutter Suite Setup](/hermes/skills/catalog/mad-agents-skills-setup)
- [Effective HTML - Artifact and Prototype Skills](/hermes/skills/catalog/effective-html-setup)
- [Tons of Skills - Agent Skills Marketplace Platform](/hermes/skills/catalog/tons-of-skills-marketplace-setup)
- [Linear Release - Release Tracking CLI Setup](/hermes/skills/catalog/linear-release-setup)
- [Software Mansion Skills - React Native Suite Setup](/hermes/skills/catalog/software-mansion-skills-setup)
- [Security Skills - Pentest and Compliance Suite](/hermes/skills/catalog/securityskills-setup)
- [Astral Plugins - Python uv, ruff and ty Setup](/hermes/skills/catalog/astral-sh-claude-code-plugins-setup)
- [Game Creator - Playable Intelligence Game Skills](/hermes/skills/catalog/game-creator-setup) - playableintelligence/game-creator, 31,774 combined, 31 listings, 355 stars, no LICENSE file, Game production for agents: ideation, core loop design, level and systems tuning, art direction and playtest loops
- [Drama Skills - AI Short Drama Production Suite](/hermes/skills/catalog/drama-skills-setup) - zenstory-ai/drama-skills, 23,558 combined, 12 listings, 3,764 stars, MIT, Short-form drama for agents: story beats, shot lists, character continuity and episode packaging for serialized AI video
- [R3F Skills - React Three Fiber for Agents](/hermes/skills/catalog/r3f-skills-setup) - enzed/r3f-skills, 23,479 combined, 11 listings, 133 stars, no LICENSE file, 3D on the web for agents: React Three Fiber scenes, materials, lighting, physics and performance budgets
- [HTML PPT Skill - Slide Decks From Markdown](/hermes/skills/catalog/html-ppt-skill-setup) - lewislulu/html-ppt-skill, 21,226 combined, 1 listings, 8,974 stars, MIT, Presentations for agents: single-file HTML decks, layouts, typography and speaker notes generated from an outline
- [Genjutsu - Front-End Craft Skills for Agents](/hermes/skills/catalog/genjutsu-setup) - athevon/genjutsu, 18,070 combined, 20 listings, 741 stars, NOASSERTION, Front-end craft for agents: layout systems, motion, component polish and design review in one skill library
- [Brave Search Skills - Web Grounding for Agents](/hermes/skills/catalog/brave-search-skills-setup) - brave/brave-search-skills, 18,032 combined, 13 listings, 193 stars, MIT, Web search for agents: official Brave Search API skills for grounding, news, local and summarization workflows
- [AI Native Camp 2 - Builder Skills Collection](/hermes/skills/catalog/ai-native-camp-skills-setup) - ai-native-camp/camp-2, 16,606 combined, 12 listings, 19 stars, no LICENSE file, Builder curriculum for agents: AI-native product work, prototyping and shipping loops from the Camp 2 cohort
- [Agent Reference Skills - 174 Role Playbooks](/hermes/skills/catalog/agent-reference-skills-setup) - fandhe-ai/agent-reference-skills, 15,776 combined, 135 listings, 4 stars, no LICENSE file, Role playbooks for agents: 174 reference skills covering engineering, marketing, finance, ops and design functions
- [Khazix Skills - Agent Workflow Toolkit](/hermes/skills/catalog/khazix-skills-setup) - kkkkhazix/khazix-skills, 15,100 combined, 9 listings, 21,933 stars, MIT, Agent workflow for builders: planning, research, writing and delivery skills wired for Claude Code and Hermes
- [GEO SEO Claude - Generative Engine Optimisation](/hermes/skills/catalog/geo-seo-claude-setup) - zubair-trabzada/geo-seo-claude, 14,666 combined, 16 listings, 11,491 stars, MIT, AI search visibility: answer-engine optimization, AI citation auditing, schema and content restructuring for LLM discovery
- [Hyva AI Tools - Magento Front-End for Agents](/hermes/skills/catalog/hyva-ai-tools-setup) - hyva-themes/hyva-ai-tools, 13,964 combined, 13 listings, 85 stars, OSL-3.0, Magento storefronts for agents: Hyva theme conventions, Alpine and Tailwind patterns and checkout customization
- [Kotlin Agent Skills - Official JVM Guidance](/hermes/skills/catalog/kotlin-agent-skills-setup) - kotlin/kotlin-agent-skills, 12,236 combined, 10 listings, 1,105 stars, Apache-2.0, Kotlin for agents: idiomatic coding standards, coroutines, Gradle build craft and migration guidance from JetBrains
- [Drawio Skills - Diagram Authoring for Agents](/hermes/skills/catalog/drawio-skills-setup) - bahayonghang/drawio-skills, 9,628 combined, 2 listings, 299 stars, MIT, Diagrams for agents: draw.io XML authoring, layout rules and export workflows for architecture and flow documents
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup) - duckdb/duckdb-skills, 9,377 combined, 9 listings, 616 stars, MIT, Local analytics for agents: DuckDB querying, file formats, extensions and analytical patterns over local data

### New - November 4, 2026 Evening Sweep (16 publisher guides)

- [Microsoft VS Code Skills - Editor Workflow Suite](/hermes/skills/catalog/microsoft-vscode-skills-setup) - microsoft/vscode, 28,011 combined, 13 listings, 194,645 stars, MIT, 
- [PyTorch Agent Skills - Contributor Workflow Suite](/hermes/skills/catalog/pytorch-agent-skills-setup) - pytorch/pytorch, 26,667 combined, 16 listings, 105,148 stars, NOASSERTION, 
- [Phaser Skills - HTML5 Game Development Suite](/hermes/skills/catalog/phaserjs-phaser-skills-setup) - phaserjs/phaser, 26,289 combined, 28 listings, 40,649 stars, MIT, 
- [AceDataCloud Skills - Hosted AI API Suite](/hermes/skills/catalog/acedatacloud-skills-setup) - acedatacloud/skills, 19,364 combined, 124 listings, 17 stars, NOASSERTION, 
- [Julius Brussee Skills - Agent Coding Drills](/hermes/skills/catalog/juliusbrussee-skills-setup) - juliusbrussee/skills, 18,811 combined, 9 listings, 175 stars, MIT, 
- [Laurigates Claude Plugins - Python and Ops Suite](/hermes/skills/catalog/laurigates-claude-plugins-setup) - laurigates/claude-plugins, 17,424 combined, 197 listings, 59 stars, MIT, 
- [Swift Concurrency Agent Skill - Swift 6 Setup](/hermes/skills/catalog/avdlee-swift-concurrency-setup) - avdlee/swift-concurrency-agent-skill, 17,351 combined, 1 listings, 1,702 stars, MIT, 
- [Circle Skills - USDC and Arc Payments Setup](/hermes/skills/catalog/circlefin-skills-setup) - circlefin/skills, 15,869 combined, 20 listings, 162 stars, Apache-2.0, 
- [Julianobarbosa Skills - Data and Editor Toolkit](/hermes/skills/catalog/julianobarbosa-claude-code-skills-setup) - julianobarbosa/claude-code-skills, 14,078 combined, 173 listings, 15 stars, MIT, 
- [21st.dev Skills - Registry and UI Build Setup](/hermes/skills/catalog/21st-dev-skill-setup) - 21st-dev/skill, 13,330 combined, 8 listings, 34 stars, Apache-2.0, 
- [Marswave Skills - Voice, TTS and Slides Setup](/hermes/skills/catalog/marswaveai-skills-setup) - marswaveai/skills, 12,967 combined, 20 listings, 82 stars, MIT, 
- [CronTap Skills - Scheduled Job Setup](/hermes/skills/catalog/crontap-skills-setup) - crontap/skills, 12,632 combined, 12 listings, 1 stars, MIT, 
- [Docker Agent Skills - Container Workflow Suite](/hermes/skills/catalog/docker-agent-skills-setup) - docker/skills, 12,666 combined, 12 listings, 615 stars, Apache-2.0, 
- [Appwrite Skills - Backend SDK Suite Setup](/hermes/skills/catalog/appwrite-skills-setup) - appwrite/skills, 11,600 combined, 11 listings, 29 stars, BSD-3-Clause, 
- [Superwall Skills - iOS Paywall Setup](/hermes/skills/catalog/superwall-skills-setup) - superwall/skills, 11,365 combined, 12 listings, 30 stars, MIT, 
- [Fal AI Community Skills - Media Generation Setup](/hermes/skills/catalog/fal-ai-community-skills-setup) - fal-ai-community/skills, 11,172 combined, 31 listings, 260 stars, no LICENSE file, 

### New - November 5, 2026 Morning Sweep (15 publisher guides)

- [Qt Agent Skills - QML, C++ and Figma Setup](/hermes/skills/catalog/qt-agent-skills-setup) - theqtcompanyrnd/agent-skills, 9,871 combined, 14 listings, 523 stars, NOASSERTION, Official Qt development suite: QML and C++ review, documentation generation, profiling, testing, CMake projects and Figma design handoff
- [next-safe-action Skills - Forms and Validation](/hermes/skills/catalog/next-safe-action-skills-setup) - next-safe-action/skills, 9,435 combined, 9 listings, 1 stars, no LICENSE file, Next.js server action layer: typed clients, form and hook integration, middleware, validation errors and Vitest coverage
- [Qiaomu OpenCLI Skills - Social Site CLI Setup](/hermes/skills/catalog/qiaomu-opencli-skills-setup) - joeseesun/qiaomu-opencli-skills, 9,424 combined, 7 listings, 998 stars, MIT, CLI-first website and desktop app control: reusable browser sessions, search routing and adapter generation
- [Exa Agent Skills - Neural Search API Setup](/hermes/skills/catalog/exa-labs-agent-skills-setup) - exa-labs/agent-skills, 9,481 combined, 5 listings, 65 stars, MIT, Search and research API suite: semantic web search, contents extraction, company research and ICP lead generation
- [Explainer Video Skills - Script to Render Setup](/hermes/skills/catalog/explainer-video-skills-setup) - iart-ai/explainer-video-skills, 9,615 combined, 5 listings, 81 stars, MIT, Motion graphics for agents: narrated explainers, animated diagrams, whiteboard and isometric scenes, and wrapped-style recaps
- [Effect Skills - TypeScript Effect System Setup](/hermes/skills/catalog/effect-ts-skills-setup) - effect-ts/skills, 9,189 combined, 2 listings, 114 stars, MIT, TypeScript effect-system guidance for agents: repository setup conventions and a bounded Effect v3 to v4 migration
- [Payload CMS Skills - Schema and Migration Setup](/hermes/skills/catalog/payloadcms-skills-setup) - payloadcms/skills, 9,058 combined, 2 listings, 172 stars, no LICENSE file, Payload CMS development guidance for agents: collections, fields, hooks, access control, queries and content migration
- [SASjs Skills - SAS and Analytics Pipeline Setup](/hermes/skills/catalog/sasjs-skills-setup) - sasjs/skills, 9,267 combined, 8 listings, 3 stars, MIT, SAS language and SASjs toolchain for agents: pure SAS, core macros, CLI, adapter, framework, lint, server and package management
- [Instagram Scraper Skill - Social Data Extraction](/hermes/skills/catalog/skillify-instagram-scraper-setup) - skillify-sh/skills, 7,997 combined, 1 listings, 0 stars, MIT, Public social media data extraction: Instagram profiles, posts, reels, comments, hashtags and mentions
- [Terraform Skill - IaC Testing and Modules Setup](/hermes/skills/catalog/terraform-skill-setup) - antonbabenko/terraform-skill, 7,835 combined, 1 listings, 2,443 stars, NOASSERTION, Infrastructure as code for agents: Terraform and OpenTofu testing, modules, state management and CI/CD
- [Sentimony Agentic Workflow - Spec to PR Setup](/hermes/skills/catalog/sentimony-agentic-workflow-setup) - sentimony/agentic-workflow, 8,863 combined, 11 listings, 4 stars, MIT, Spec-to-PR delivery workflow for coding agents: specify, plan, implement, verify, review and finalize
- [Margelo React Native Skills - Native Modules Setup](/hermes/skills/catalog/margelo-react-native-skills-setup) - margelo/react-native-skills, 7,670 combined, 9 listings, 179 stars, no LICENSE file, React Native native-module engineering for agents: Nitro modules, MMKV storage, VisionCamera, networking and Swift, Kotlin and C++ APIs
- [5dive Skills - Knowledge Compile and Dev Loop Setup](/hermes/skills/catalog/5dive-skills-setup) - 5dive-ai/skills, 7,291 combined, 17 listings, 1 stars, MIT, Agent runtime operations, knowledge compilation, research, review and loop authoring
- [Claude Office Skills - XLSX, DOCX and PPTX Setup](/hermes/skills/catalog/tfriedel-claude-office-skills-setup) - tfriedel/claude-office-skills, 7,002 combined, 4 listings, 849 stars, no LICENSE file, Office document workflows for agents: spreadsheet, word processor, presentation and PDF production
- [Rust Skills - 265 Rules Across 26 Categories](/hermes/skills/catalog/rust-skills-setup) - leonardomso/rust-skills, 6,765 combined, 1 listings, 670 stars, MIT, Rust engineering standards: ownership, error handling, async, unsafe, API design, performance and testing
### New - November 5, 2026 Evening Sweep (19 publisher guides)

- [Obsidian Visual Skills - Canvas, Excalidraw and Mermaid](/hermes/skills/catalog/axton-obsidian-visual-skills-setup) - axtonliu/axton-obsidian-visual-skills, 6,718 combined, 3 listings, 3,677 stars, MIT, Obsidian vault visuals for agents: canvas boards, Excalidraw sketches and Mermaid diagrams generated from a prompt
- [PracticalSwan Agent Skills - 253 Skill Library](/hermes/skills/catalog/practicalswan-agent-skills-setup) - practicalswan/agent-skills, 6,614 combined, 200 listings, 24 stars, MIT, Cross-client skill library: 253 skills shared across Claude Code, Codex and GitHub Copilot with host-aware routing
- [BMAD Labs Skills - Architecture and Delivery Toolkit](/hermes/skills/catalog/bmad-labs-skills-setup) - bmad-labs/skills, 6,558 combined, 74 listings, 19 stars, MIT, BMAD delivery for agents: architecture design, trade-off analysis, root-cause reports, release and multi-repo git work
- [Claude Code Java - Spring and JVM Review Suite](/hermes/skills/catalog/claude-code-java-setup) - decebals/claude-code-java, 6,495 combined, 18 listings, 770 stars, MIT, Java review infrastructure: Spring Boot patterns, JPA, concurrency and SOLID checks, Maven audits and migration guidance
- [PSKoett AI Skills - Self-Improving Agent Loops](/hermes/skills/catalog/pskoett-ai-skills-setup) - pskoett/pskoett-ai-skills, 6,493 combined, 25 listings, 328 stars, no LICENSE file, Self-improving agent loops: plan interviews, context surfing, eval creation and self-healing recovery
- [GPUI Kit - Rust Desktop UI Components for Agents](/hermes/skills/catalog/gpui-kit-setup) - longbridge/gpui-kit, 6,323 combined, 19 listings, 19,462 stars, no LICENSE file, Rust desktop UI for agents: GPUI component patterns and design guides for cross-platform applications
- [Bankr Skills - DeFi and Onchain Agent Toolkit](/hermes/skills/catalog/bankrbot-skills-setup) - bankrbot/skills, 6,157 combined, 123 listings, 1,209 stars, no LICENSE file, Onchain agent toolkit: DeFi monitoring, token distribution, prediction markets and wallet operations
- [Stream Agent Skills - Chat, Feeds and Video SDK](/hermes/skills/catalog/getstream-agent-skills-setup) - getstream/agent-skills, 5,989 combined, 12 listings, 21 stars, Apache-2.0, In-app chat and feeds for agents: Stream SDK scaffolding across React, React Native, Flutter, Swift, Unity and Unreal
- [Oracle Skills - Database, OCI and APEX Guidance](/hermes/skills/catalog/oracle-skills-setup) - oracle/skills, 5,978 combined, 7 listings, 914 stars, custom licence file, Oracle estate for agents: Database, OCI, APEX, Fusion applications and GraalVM with source-backed guidance
- [Alchemy Skills - Blockchain API and MCP Setup](/hermes/skills/catalog/alchemy-skills-setup) - alchemyplatform/skills, 5,947 combined, 7 listings, 55 stars, MIT, Blockchain APIs for agents: Alchemy live queries, CLI and MCP wiring plus application-code integration
- [WPS Skills - Office Automation via MCP Tools](/hermes/skills/catalog/wps-skills-setup) - lc2panda/wps-skills, 5,916 combined, 4 listings, 685 stars, MIT, Document automation for agents: WPS Office Excel, Word and PPT control through 243 MCP tools
- [Playwriter - Agent Control of Your Own Chrome](/hermes/skills/catalog/playwriter-setup) - remorses/playwriter, 5,905 combined, 1 listings, 4,061 stars, MIT, Browser control for agents: Playwright snippets against your logged-in Chrome through a CLI or MCP server
- [Roblox Skills - Game Systems for Agents Setup](/hermes/skills/catalog/roblox-skills-setup) - sentinelcore/roblox-skills, 5,579 combined, 7 listings, 29 stars, no LICENSE file, Roblox development for agents: datastores, remote events, GUI, monetization and performance
- [BMAD Planning and Orchestrator - Claude Code Plugin](/hermes/skills/catalog/aj-geddes-claude-code-bmad-skills-setup) - aj-geddes/claude-code-bmad-skills, 5,524 combined, 5 listings, 493 stars, MIT, BMAD planning shipped as a Claude Code plugin: PRD, architecture, sprint planning and course correction
- [AvdLee Swift Testing Skill - XCTest Migration Setup](/hermes/skills/catalog/avdlee-swift-testing-agent-skill-setup) - avdlee/swift-testing-agent-skill, 5,422 combined, 1 listings, 479 stars, MIT, Swift Testing for agents: parameterized tests, traits and tags, async patterns and XCTest migration
- [Willem4130 Claude Code Skills - PowerPoint Designer](/hermes/skills/catalog/willem4130-claude-code-skills-setup) - willem4130/claude-code-skills, 5,382 combined, 1 listings, 9 stars, no LICENSE file, Slide design for agents: one elite PowerPoint designer skill covering layout, typography and templates
- [Hyperskills - Review, Research and Orchestration Skills](/hermes/skills/catalog/hyperskills-setup) - hyperb1iss/hyperskills, 5,348 combined, 28 listings, 36 stars, MIT, Agent craft: cross-model review, PR review, research, orchestration and terminal UI design
- [MemPalace - Local-First AI Memory for Agents](/hermes/skills/catalog/mempalace-setup) - mempalace/mempalace, 5,306 combined, 9 listings, 60,419 stars, MIT, Local-first agent memory: verbatim storage, pluggable backends, recall and task memory over a CLI
- [CodexThemes Skills - Theme Build and Install Setup](/hermes/skills/catalog/codexthemes-skills-setup) - codexthemes/skills, 5,154 combined, 6 listings, 7 stars, Apache-2.0, Codex desktop theming: create, find, install, switch and submit native-safe themes

### New - November 6, 2026 Morning Sweep (19 publisher guides)

- [Claude Plugin Marketplace - Azure and DevOps Packs](/hermes/skills/catalog/claude-plugin-marketplace-setup) - josiahsiegel/claude-plugin-marketplace, 41,688 combined, 200 listings, 59 stars, MIT, Azure, Azure DevOps, Databricks and language plugin packs for Claude Code
- [Dembrandt Skills - Design System Judgment for Agents](/hermes/skills/catalog/dembrandt-skills-setup) - dembrandt/dembrandt-skills, 38,341 combined, 45 listings, 184 stars, MIT, Design-system judgment: component families, colour tokens, elevation, forms and information architecture
- [Posit Skills - R, Quarto and Maintainer Workflows](/hermes/skills/catalog/posit-dev-skills-setup) - posit-dev/skills, 19,262 combined, 36 listings, 556 stars, MIT, R and Quarto work: package checks, CRAN release passes, alt text and maintainer replies
- [Apple Design Skill - HIG Review Across Frameworks](/hermes/skills/catalog/apple-design-skill-setup) - dickwu/apple-design-skill, 13,047 combined, 1 listings, 2,880 stars, no LICENSE file, Apple HIG review translated to Flutter, React Native, Tauri, Electron and native frameworks
- [Instagram Agent Skill - Thirteen Account Skills](/hermes/skills/catalog/instagram-agent-skill-setup) - jakeschincariol/instagram-agent-skill, 12,524 combined, 13 listings, 5,054 stars, MIT, Instagram operations: reel hooks, caption linting, carousels, DMs, replies and weekly planning
- [Motion Graphics Skills - B-roll and Explainer Video](/hermes/skills/catalog/barty-motion-graphics-setup) - barty-bart/motion-graphics, 12,248 combined, 6 listings, 1,086 stars, MIT, Video editing: motion B-roll from a transcript, object separation and three explainer cuts
- [AMD Skills - ROCm, Ryzen AI and Kernel Authoring](/hermes/skills/catalog/amd-skills-setup) - amd/skills, 11,896 combined, 18 listings, 481 stars, MIT, AMD hardware: ROCm setup, Ryzen AI local models, FlyDSL kernels and rocprofiler analysis
- [MLflow Skills - Tracing, Evaluation and LLMOps](/hermes/skills/catalog/mlflow-skills-setup) - mlflow/skills, 10,794 combined, 21 listings, 89 stars, Apache-2.0, LLMOps: MLflow tracing, evaluation, trace analysis and SageMaker deployment
- [Composio Skills - Tool Router and Trigger Patterns](/hermes/skills/catalog/composio-community-skills-setup) - composio-community/skills, 10,697 combined, 3 listings, 185 stars, MIT, Composio Tool Router sessions, authentication, framework integration and webhook triggers
- [LiveKit Agent Skills - Voice Agent Lifecycle](/hermes/skills/catalog/livekit-agent-skills-setup) - livekit/agent-skills, 7,898 combined, 9 listings, 74 stars, MIT, Voice agents: build, test, debug, operate and simulate LiveKit agents with docs lookup
- [SpriteCook Skills - Pixel Art and Game Assets](/hermes/skills/catalog/spritecook-skills-setup) - spritecook/skills, 7,401 combined, 10 listings, 54 stars, MIT, Game art: sprite and tileset generation, animation, UI kits and Godot import over MCP
- [Sonilo Skills - Music, SFX and Dubbing for Video](/hermes/skills/catalog/sonilo-skills-setup) - sonilo-ai/skills, 7,071 combined, 16 listings, 117 stars, MIT, Audio: licensed music scored to a finished video, sound effects, dubbing and ducking
- [Rebyte Skills - Template Setup and Deploy Skills](/hermes/skills/catalog/rebyte-skills-setup) - rebyteai-template/rebyte-skills, 6,971 combined, 50 listings, 18 stars, no LICENSE file, Starter templates: setup and deploy skills across Astro, FastAPI, Axum, Deno, Express and Next stacks
- [belt CLI - Cloud Platform Control for Agents](/hermes/skills/catalog/belt-cli-setup) - belt-sh/cli, 6,657 combined, 1 listings, 7 stars, MIT, Agent command line for hosted apps, skill search and publishing, and MCP server calls
- [AI Design Skills - Landing Pages and Figma](/hermes/skills/catalog/elayadesign-ai-design-skills-setup) - elayadesign/ai-design-skills, 5,289 combined, 3 listings, 14,497 stars, MIT, Landing pages from intake to visual system, and structured Figma files with variables
- [WebGL Animation Skills - Three.js and Shaders](/hermes/skills/catalog/iart-webgl-animation-skills-setup) - iart-ai/webgl-animation-skills, 5,279 combined, 3 listings, 51 stars, MIT, Three.js animation, GLSL shaders and GPU particle systems with render troubleshooting
- [Data Animation Skills - Charts That Move](/hermes/skills/catalog/iart-data-animation-skills-setup) - iart-ai/data-animation-skills, 5,125 combined, 3 listings, 17 stars, MIT, Animated charts, bar chart races, count-up tickers and presentation cuts from a CSV
- [Codex PPT Skill - Image-Based Slide Decks](/hermes/skills/catalog/codex-ppt-skill-setup) - ningzimu/codex-ppt-skill, 5,121 combined, 1 listings, 7,677 stars, MIT, Image-based PowerPoint decks produced with GPT-Image through one skill
- [Svelte Skills Kit - Runes, Data Flow and Deployment](/hermes/skills/catalog/svelte-skills-kit-setup) - spences10/svelte-skills-kit, 5,040 combined, 11 listings, 94 stars, no LICENSE file, SvelteKit: runes, template directives, data flow, remote functions, styling and deployment

### New - November 6, 2026 Evening Sweep (16 publisher guides)

- [Cognite Builder Skills - Industrial Flows Apps](/hermes/skills/catalog/cognite-builder-skills-setup) - cognitedata/builder-skills, 45,575 combined, 38 listings, 6 stars, Apache-2.0, Industrial data apps for agents: Flows app scaffolding, Atlas MCP connections, CDF functions and code-quality passes
- [Fandhe Agent CLI Skills - Commit and PR Workflows](/hermes/skills/catalog/fandhe-agent-cli-skills-setup) - fandhe-ai/agent-cli-skills, 37,965 combined, 32 listings, 2 stars, no LICENSE file, CLI workflows for agents: Conventional Commits, PR creation, issue triage, review passes and skill authoring
- [Paseo Skills - A Fleet of Coding Agents](/hermes/skills/catalog/paseo-orchestration-skills-setup) - getpaseo/paseo, 32,407 combined, 14 listings, 23,334 stars, Apache-2.0, Multi-agent orchestration for agents: advisor and committee modes, handoffs, provider switching and release workflows
- [Guizang PPT Skill - Editorial HTML Slide Decks](/hermes/skills/catalog/guizang-ppt-skill-setup) - op7418/guizang-ppt-skill, 28,412 combined, 1 listings, 29,395 stars, custom licence file, HTML decks for agents: magazine and Swiss layouts, image prompts, social covers and a low-power presentation runtime
- [ZSXQ Skill - Community Operations for Agents](/hermes/skills/catalog/zsxq-skill-setup) - unnoo/zsxq-skill, 25,175 combined, 6 listings, 323 stars, MIT, Chinese community operations for agents: comment sweeps, digests, scheduled posts, paid renewals and content search
- [Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup) - dceoy/speckit-agent-skills, 23,609 combined, 12 listings, 170 stars, custom licence file, Spec-driven development for agents: constitution, specify, clarify, plan, tasks, implement, analyze and converge passes
- [Claude Scholar - Research Pipeline for Agents](/hermes/skills/catalog/claude-scholar-setup) - galaxy-dawn/claude-scholar, 19,910 combined, 57 listings, 6,006 stars, MIT, Academic research for agents: ideation, literature review, citation verification, experiments, paper writing and rebuttals
- [PUA Skill - Drive and Pushback for Agents](/hermes/skills/catalog/pua-agent-drive-setup) - tanweai/pua, 19,212 combined, 34 listings, 19,812 stars, no LICENSE file, Agent behaviour for agents: a review persona that forces root-cause work, evidence and pushback instead of partial answers
- [daisyUI Skills - Tailwind Component Tokens](/hermes/skills/catalog/daisyui-skills-setup) - saadeghi/daisyui, 12,998 combined, 5 listings, 42,764 stars, MIT, daisyUI for agents: install, config, theme colours and component usage from the 42K-star Tailwind component library
- [Story Skills - End-to-End Fiction Writing](/hermes/skills/catalog/story-skills-setup) - danjdewhurst/story-skills, 11,914 combined, 24 listings, 394 stars, MIT, Fiction writing for agents: discovery drafting, character management, chapter craft, editorial review and adaptation passes
- [Rstack Skills - Rspack Ecosystem Maintenance](/hermes/skills/catalog/rstack-agent-skills-setup) - rstackjs/agent-skills, 11,707 combined, 24 listings, 98 stars, MIT, Rspack ecosystem work for agents: docs writing, release notes, PR creation, CI debugging and repo maintenance passes
- [AI Evals Skills - Product-Specific Evaluations](/hermes/skills/catalog/ai-evals-skills-setup) - ai-evals-course/evals-skills, 9,483 combined, 11 listings, 1,716 stars, Apache-2.0, Evaluation work for agents: eval audits, error discovery, synthetic data, RAG evaluation and evaluator validation
- [ASD-STE100 Skill - Simplified Technical English](/hermes/skills/catalog/asd-ste100-skill-setup) - danyuchn/asd-ste100-skill, 9,357 combined, 2 listings, 6,166 stars, MIT, Controlled English for agents: rewrites dense output into ASD-STE100 Simplified Technical English so steps cannot be misread
- [Tiangong Skills - Data Fetch and Report Utilities](/hermes/skills/catalog/tiangong-agent-skills-setup) - tiangong-ai/agent-skills, 9,130 combined, 62 listings, 11 stars, MIT, Research utilities for agents: RSS and paper fetching, image conversion, environmental data and recurring summary jobs
- [Dodo Payments Skills - Billing and Checkout](/hermes/skills/catalog/dodopayments-skills-setup) - dodopayments/skills, 9,036 combined, 18 listings, 13 stars, MIT, Payments for agents: checkout, subscriptions, credit billing, discounts, customer management and MCP usage patterns
- [ADHD Skill - Divergent Thinking for Agents](/hermes/skills/catalog/adhd-skill-setup) - uditakhourii/adhd, 7,589 combined, 1 listings, 4,509 stars, MIT, Creative reasoning for agents: tree-of-thought fan-out under fixed cognitive frames, scoring, pruning and deepening

### New - November 7, 2026 Morning Sweep (13 publisher guides)

- [Astro Skills - Island Architecture for Agents](/hermes/skills/catalog/astrolicious-astro-setup) - astrolicious/agent-skills, 18,959 combined, 1 listings, 13 stars, no LICENSE file, Astro work for agents: island architecture, content collections, view transitions and static deployment checks
- [Graphite Skills - Stacked Pull Requests for Agents](/hermes/skills/catalog/graphite-agent-skills-setup) - withgraphite/agent-skills, 9,989 combined, 1 listings, 7 stars, no LICENSE file, Stacked pull requests for agents: branch creation, stack restacking, review submission and trunk sync through the Graphite CLI
- [Korean Skills - Hangul Writing and Style Checks](/hermes/skills/catalog/korean-skills-setup) - daleseo/korean-skills, 8,457 combined, 3 listings, 250 stars, MIT, Korean writing for agents: grammar correction, style-guide enforcement and human-sounding Korean prose
- [ModelStudio Skills - Alibaba Video and Data Tools](/hermes/skills/catalog/modelstudio-skills-setup) - modelstudioai/skills, 7,703 combined, 13 listings, 59 stars, Apache-2.0, Alibaba Cloud Model Studio for agents: video generation pipelines, model selection, training jobs and documentation lookup
- [10x CLI Skills - Course Content for Agents](/hermes/skills/catalog/10x-cli-skills-setup) - przeprogramowani/10x-cli, 6,668 combined, 3 listings, 87 stars, no LICENSE file, Skill distribution for agents: fetch, verify and apply course skills, prompts and configs into a workspace with one CLI
- [Alan Skills - Plan, Test and Review PRs](/hermes/skills/catalog/alan-skills-setup) - supatest-ai/alan-skills, 6,365 combined, 6 listings, 0 stars, Apache-2.0, Delivery workflow for agents: implementation planning, feature testing and pull-request review passes from a software factory agent
- [HVE Core - Microsoft Agentic SDLC Framework](/hermes/skills/catalog/hve-core-setup) - microsoft/hve-core, 5,822 combined, 107 listings, 1,606 stars, MIT, Agentic SDLC for agents: context management, artefact authoring, code review, data science and MLOps instruction packs
- [Unslop - De-AI Writing Skill for Agents](/hermes/skills/catalog/unslop-setup) - theclaymethod/unslop, 5,624 combined, 1 listings, 982 stars, no LICENSE file, Editing for agents: flags formulaic AI tells, rebuilds drafts under preservation gates and mimics a taught voice
- [pg-aiguide - Postgres Skills from Timescale](/hermes/skills/catalog/pg-aiguide-setup) - timescale/pg-aiguide, 5,562 combined, 12 listings, 1,885 stars, Apache-2.0, Postgres expertise for agents: schema design, vector and hybrid search, migrations and TimescaleDB hypertables
- [DingTalk Skills - Enterprise Messaging for Agents](/hermes/skills/catalog/dingtalk-skills-setup) - breath57/dingtalk-skills, 5,476 combined, 10 listings, 101 stars, no LICENSE file, DingTalk operations for agents: documents, knowledge base, AI tables, group messages, calendars, to-dos and contacts over curl
- [React Router Skills - Data and Framework Modes](/hermes/skills/catalog/react-router-agent-skills-setup) - remix-run/agent-skills, 5,250 combined, 3 listings, 134 stars, MIT, React Router guidance for agents: framework, data and declarative modes with routes, loaders, actions and type safety
- [CC Godot - Game Development Plugin for Agents](/hermes/skills/catalog/cc-godot-setup) - zate/cc-godot, 5,217 combined, 4 listings, 19 stars, no LICENSE file, Godot game development for agents: project setup, GDScript development, debugging and rendering optimisation
- [Julianromli Skills - Frontend and Product Craft](/hermes/skills/catalog/julianromli-ai-skills-setup) - julianromli/ai-skills, 5,054 combined, 43 listings, 214 stars, no LICENSE file, Frontend craft for agents: design engineering, motion, landing-page cloning, Convex data patterns and deployment to Vercel

### New - November 7, 2026 Evening Sweep (13 publisher guides)

- [Useful AI Prompts - 260 Skill Prompt Library Setup](/hermes/skills/catalog/useful-ai-prompts-setup) - aj-geddes/useful-ai-prompts, 128,658 combined, 200 listings, 378 stars, MIT, 260+ skills of production-ready prompts and code patterns.
- [Claude Blog - AI Blog Writing and SEO Plugin Setup](/hermes/skills/catalog/claude-blog-setup) - agricidaniel/claude-blog, 79,486 combined, 33 listings, 2,672 stars, MIT, 32 blog skills for research, writing, SEO and GEO.
- [Axiom Swift Skills - Apple Platform Skill Suite Setup](/hermes/skills/catalog/axiom-swift-skills-setup) - charleswiltgen/axiom, 64,084 combined, 200 listings, 1,253 stars, MIT, Apple platform skills for Swift 6, SwiftUI, Xcode and data.
- [AI Engineering from Scratch - Course Tutor Skills Setup](/hermes/skills/catalog/ai-engineering-from-scratch-setup) - rohitg00/ai-engineering-from-scratch, 47,043 combined, 28 listings, 77,600 stars, MIT, skills that tutor a 542-lesson AI curriculum.
- [OpenClaudia Skills - 78-Skill Marketing Toolkit Setup](/hermes/skills/catalog/openclaudia-skills-setup) - openclaudia/openclaudia-skills, 33,390 combined, 82 listings, 731 stars, MIT, 78 marketing skills for SEO, ads, email and social.
- [UI Craft - Design Engineering System Setup](/hermes/skills/catalog/ui-craft-setup) - educlopez/ui-craft, 23,168 combined, 32 listings, 441 stars, MIT, anti-slop UI rules, design review and a design memory for agents.
- [Universal Modder - AI Game Modding Skills Setup](/hermes/skills/catalog/universal-modder-setup) - rehan-remade/universal-modder, 20,760 combined, 13 listings, 9,510 stars, MIT, skills that take an agent from game recon to a published mod.
- [Cyrus - Agent Orchestration Setup Skills](/hermes/skills/catalog/cyrus-agent-skills-setup) - cyrusagents/cyrus, 18,195 combined, 19 listings, 888 stars, Apache-2.0, setup and workflow skills for the Cyrus issue-to-pull-request agent.
- [Uniswap AI - DeFi Integration Skills Setup](/hermes/skills/catalog/uniswap-ai-skills-setup) - uniswap/uniswap-ai, 15,296 combined, 19 listings, 236 stars, MIT, swap, liquidity, v4 hook and trading bot skills for Uniswap work.
- [Tesseract Video Skills - Agent Creative Suite Setup](/hermes/skills/catalog/tesseract-video-skills-setup) - mirage-hq/tesseract, 13,051 combined, 5 listings, 285 stars, custom licence file, video editing, motion graphics, 3D and design skills for agents.
- [Claude Cortex - Multi-Model Development Orchestration](/hermes/skills/catalog/claude-cortex-setup) - nickcrew/claude-cortex, 11,752 combined, 150 listings, 66 stars, MIT, engineering skills behind a multi-model review loop.
- [PM Prompt Skills - Product Management Suite Setup](/hermes/skills/catalog/claude-plugin-product-management-setup) - pmprompt/claude-plugin-product-management, 10,352 combined, 30 listings, 57 stars, MIT, PM skills for PRDs, prioritisation and strategy.
- [AI Native Camp 1 - Korean Claude Code Curriculum](/hermes/skills/catalog/ai-native-camp-bootcamp-setup) - ai-native-camp/camp-1, 10,140 combined, 9 listings, 242 stars, no LICENSE file, a Korean 7-day Claude Code camp shipped as skills.

### New - November 8, 2026 Morning Sweep (12 publisher guides)

- [React Email Skill - Template Authoring for Agents](/hermes/skills/catalog/react-email-skill-setup) - resend/react-email, 9,922 combined, 1 listings, 19,916 stars, MIT via LICENSE.md, `canary` branch, react Email components, local preview workflow and sending through Resend
- [Angular Framework Skills - Official Repo Agent Guides](/hermes/skills/catalog/angular-framework-agent-skills-setup) - angular/angular, 9,733 combined, 7 listings, 101,466 stars, MIT, framework conventions, signals and forms references, compiler and CLI guidance plus PR review standards
- [Fernando Skills - Spec-Driven Development for Agents](/hermes/skills/catalog/fernando-skills-setup) - klerith/fernando-skills, 9,073 combined, 3 listings, 372 stars, MIT, write the spec first, implement against it, and keep code and intent in sync
- [Actionbook - Research Behind Logins and Paywalls](/hermes/skills/catalog/actionbook-skills-setup) - actionbook/actionbook, 8,945 combined, 11 listings, 1,626 stars, Apache-2.0 LICENSE at the repo root, web actions, extraction, deep research and article export across paywalled sources
- [COSS Skills - One API for Email, SMS and Inboxes](/hermes/skills/catalog/coss-skills-setup) - cosscom/coss, 8,273 combined, 2 listings, 5 stars, MIT plugin inside an AGPL-3.0 monorepo, email, SMS, agent inboxes, scheduling and webhooks behind one SDK and one API key
- [Email Best Practices Skill - Deliverability for Agents](/hermes/skills/catalog/email-best-practices-skill-setup) - resend/email-best-practices, 8,225 combined, 1 listings, 147 stars, no licence file in the repo root, `main` branch, sender authentication, list hygiene, sending patterns and rendering rules for transactional email
- [Sepia - De-AI Writing Skills for Any Agent](/hermes/skills/catalog/sepia-writing-skills-setup) - nanako0129/sepia, 7,322 combined, 6 listings, 3,687 stars, MIT, narrative structure, de-AI rewriting, review passes and Hemingway-style compression
- [shadcn-svelte Skill - Svelte UI Components for Agents](/hermes/skills/catalog/shadcn-svelte-skill-setup) - huntabyte/shadcn-svelte, 7,148 combined, 1 listings, 9,247 stars, MIT, shadcn-svelte component copy-in, Tailwind styling and accessible Svelte 5 patterns
- [Interface Skills - Animation and UI Craft for Agents](/hermes/skills/catalog/raphaelsalaja-skills-setup) - raphaelsalaja/skills, 6,201 combined, 42 listings, 62 stars, MIT, animation principles, motion tokens, layout, colour, icons and UI audit playbooks
- [Eval Skills - AI Evaluation Workflows for Agents](/hermes/skills/catalog/hamelsmu-evals-skills-setup) - hamelsmu/evals-skills, 6,048 combined, 7 listings, 1,674 stars, MIT with a LICENSE file in the repo root, error analysis, judge prompts, RAG evals, synthetic data and human review interfaces
- [Arize Phoenix Skills - LLM Observability for Agents](/hermes/skills/catalog/arize-phoenix-skills-setup) - arize-ai/phoenix, 5,516 combined, 8 listings, 12,201 stars, Elastic License 2.0 at the repo root, tracing, evals, error analysis and CLI workflows on the open-source Phoenix server
- [ImageGen Skills - Design Images for Coding Agents](/hermes/skills/catalog/imagegen-skills-setup) - leonxlnx/imagegen-skills, 5,046 combined, 4 listings, 72 stars, MIT LICENSE at the repo root, website comps, mobile screens, brand kits and an image-to-code handoff pipeline

### New - November 8, 2026 Evening Sweep (6 publisher guides)

- [Brag - Launch Video Skill for Agents](/hermes/skills/catalog/brag-launch-video-setup) - latent-spaces/brag, 36,286 combined, 2 listings, 20,778 stars, MIT, launch videos for a finished project: story plan, Hyperframes render, music and share copy
- [AGI Pro Trading Skills - 68 Quant and DeFi Skills](/hermes/skills/catalog/agiprolabs-trading-skills-setup) - agiprolabs/claude-trading-skills, 33,316 combined, 68 listings, 515 stars, MIT via LICENSE.md, trading research: market data, on-chain analytics, backtesting, risk and tax reporting
- [Education Agent Skills - 165 Teaching Skills](/hermes/skills/catalog/education-agent-skills-setup) - garethmanning/education-agent-skills, 20,064 combined, 149 listings, 966 stars, CC BY-SA 4.0 per the README, lesson planning, assessment, curriculum design and student study support
- [Cybersecurity Skills - 42 Audit and Pentest Skills](/hermes/skills/catalog/briiirussell-cybersecurity-skills-setup) - briiirussell/cybersecurity-skills, 13,252 combined, 42 listings, 513 stars, MIT, OWASP and cloud audits, dependency review, incident triage, forensics and compliance mapping
- [Episodic Memory - Semantic Search for Coding Agents](/hermes/skills/catalog/episodic-memory-setup) - obra/episodic-memory, 9,225 combined, 1 listings, 499 stars, MIT, semantic search over past coding conversations so an agent can recall the why, not just the what
- [Temporal Developer Skill - Durable Execution](/hermes/skills/catalog/temporal-developer-skill-setup) - temporalio/skill-temporal-developer, 5,014 combined, 1 listings, 236 stars, MIT, durable execution across eight SDK languages: workflows, activities, retries, versioning and workers
