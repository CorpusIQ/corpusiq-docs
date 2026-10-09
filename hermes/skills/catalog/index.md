---
title: "Hermes Skills Catalog - Quality-Tiered Directory"
description: "Curated directory of community-validated Hermes agent skills. Quality tiers (Production/Beta/Community), starter pack, evaluation guide, and installation"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/"
robots: "index,follow"
last_updated: "2026-10-05"
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

1. Follow the [skill development best practices](../../best-practices/skill-development)
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
