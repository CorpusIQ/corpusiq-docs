---
title: "Hermes Skills Catalog - Quality-Tiered Directory"
description: "Curated directory of community-validated Hermes agent skills. Quality tiers (Production/Beta/Community), starter pack, evaluation guide, and installation"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/"
robots: "index,follow"
last_updated: "2026-10-31"
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
