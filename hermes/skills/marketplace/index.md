---
title: Skills Marketplace
description: Discover and install community skills from skills.sh  --  290+ curated skills across 22 categories. Browse by category, check trending skills, submit your own. Updated weekly.
---

# Skills Marketplace

The Skills Marketplace is the community hub for discovering, installing, and sharing Hermes agent skills. Every skill listed here is a production-ready, executable workflow from [skills.sh](https://skills.sh)  --  install with a single command and use immediately.

**469+ curated skill repos across 22 categories.** Updated weekly as new skills are published.

## How to Discover Skills

### Browse by Category

The marketplace organizes skills into functional categories. Click any category to jump to the detailed listing:

| Category | Skills | Top Picks |
|----------|:------:|-----------|
| [Marketing & Growth](#marketing--growth) | 45 | `seo-audit` (132K), `copywriting` (122K), `content-strategy` (86K) |
| [Development & GitHub](#development--github) | 10 | `requesting-code-review` (121K), `github-actions-docs` (206K) |
| [Agent Infrastructure](#agent-infrastructure) | 8 | `agent-browser` (432K), `web-design-guidelines` (377K) |
| [MCP & API Integration](#mcp--api-integration) | 5 | `mcp-builder` (71K), `claude-api` (37K) |
| [Code Quality & Review](#code-quality--review) | 4 | `code-review-excellence` (22K), `python-testing-patterns` (24K) |
| [Testing & QA](#testing--qa) | 4 | `webapp-testing` (92K), `e2e-testing-patterns` (18K) |
| [Content & Social](#content--social) | 5 | `persona-content-creator` (17K), `social-publisher` (3K) |
| [AI Media](#ai-media) | 5 | `frontend-design` (521K), `video-edit` (217K) |
| [Operations & Productivity](#operations--productivity) | 5 | `email-to-task` (18K), `changelog-automation` (9K) |
| [Orchestration & RAG](#orchestration--rag) | 6 | `rag-implementation` (9.5K), `langchain-rag` (8.6K) |
| [Infrastructure & DevOps](#infrastructure--devops) | 5 | `neon-postgres` (40.3K), `docker-expert` (18.9K) |
| [Platform Integrations](#platform-integrations) | 11 | `notion-api` (42.1K), `agent-email-inbox` (3.3K) |
| [Communication Bots](#communication-bots) | 4 | `whatsapp-automation` (3.4K), `telegram-bot` (3.1K) |
| [Hermes Agent Variants](#hermes-agent-variants) | 30 | `dogfood` (3.6K), `claude-code` (131) |
| [Hermes Ecosystem](#hermes-ecosystem) | 53 | `hermes-webui-agent` (193), `hermes-desktop-companion` (152) |
| [Security Suite](#security-suite) | 16 | `skill-auditor` (590), `setup-auditor` (384) |

### Check Trending Skills

Install count is the best signal of a skill's usefulness. Here are the top marketplace skills by installs:

| Skill | Installs | What It Does |
|-------|----------|-------------|
| `frontend-design` | 521K | Design and UI generation |
| `vercel-react-best-practices` | 462K | React patterns and conventions |
| `agent-browser` | 432K | Browser automation via Playwright |
| `web-design-guidelines` | 377K | Web UI best practices |
| `video-edit` | 217K | AI video editing |
| `vercel-composition-patterns` | 205K | Vercel composition architecture |
| `github-actions-docs` | 206K | GitHub Actions reference |
| `use-my-browser` | 200K | Browser session reuse |
| `seo-audit` | 132K | Full SEO audit |
| `copywriting` | 122K | Marketing copy generation |

New skills take time to accumulate installs. Don't dismiss a 500-install skill  --  it might be the best tool for a specific problem. Check the skill's README and `SKILL.md` for quality signals: clear trigger conditions, specific tools required, concrete outputs.

### Search by Use Case

Looking for something specific? The marketplace is searchable by keyword:

```bash
# Search skills.sh API directly
curl -s "https://skills.sh/api/skills?q=email" | jq '.'

# Or browse the catalog pages
# → [Email operations →](/hermes/skills/catalog/#email-operations)
# → [SEO skills →](/hermes/skills/catalog/#marketing--growth)
```

## Installing Skills

Every marketplace skill installs with a single command:

```bash
# Install a skill (the @ syntax specifies which skill from the repo)
npx skills add coreyhaines31/marketingskills@seo-audit

# Install all skills from a repo (the full pack)
npx skills add coreyhaines31/marketingskills

# Install with automatic agent assignment
npx skills add coreyhaines31/marketingskills@seo-audit -a hermes-agent -y

# List installed marketplace skills
hermes skills list --marketplace

# Check a skill's metadata
hermes skills inspect seo-audit
```

After installation, the skill is available in any Hermes session. Invoke it by mentioning trigger keywords or calling it directly:

```
"Run a full SEO audit on example.com"
```

## Community Submissions

The marketplace grows through community contributions. To submit a skill:

### 1. Publish on skills.sh

Create a repository on GitHub with a `SKILL.md` file at the root. The file must follow the skills.sh format:

```markdown
---
name: my-skill
description: What the skill does, in one sentence
triggers:
  - keyword that activates it
  - another trigger
tools:
  - terminal
  - web_extract
---

# Skill Name

## Step 1: First action
Instructions the agent follows...

## Verification
What to check to confirm success...
```

Publish to npm via skills.sh:

```bash
npx skills publish ./my-skill-repo
```

### 2. Submit for Curation

Once published on skills.sh, your skill can be added to the Hermes community hub marketplace. The curation criteria:

- **Production readiness**  --  Has the skill been tested with real agent invocations? (Not required, but strongly preferred)
- **Clear value proposition**  --  Is it obvious what problem the skill solves?
- **Complete trigger conditions**  --  Does the skill activate under well-defined circumstances?
- **Verification steps**  --  Does the skill include checks that confirm success?
- **No duplication**  --  Is this distinct from existing marketplace skills?

Submit via the [Hermes community GitHub repository](https://github.com/nousresearch/hermes-agent)  --  create an issue with the `skill-submission` label, linking to your skills.sh page.

### 3. What Happens Next

Submitted skills go through automated discovery sweeps that run weekly. The curation process checks:

1. The skill installs without errors (`npx skills add <repo>@<skill>`)
2. The SKILL.md is well-formed and parseable
3. The skill category matches the existing marketplace taxonomy
4. The install count is reported accurately

Approved skills appear on the next marketplace update page with install commands and category placement.

## Marketplace Updates

New skills are discovered weekly through automated sweeps of skills.sh. Each discovery gets a dedicated update page:

- [🆕 June 30, 2026 (Update) — Matt Pocock Engineering Suite, ChromaDB, OpenClaw Loader (7 skills, 1.3M+ installs, 1 setup guide)](/hermes/skills/marketplace/new-june30-2026-update/)
- [🆕 June 30, 2026 — OpenClaw Expansion, HermesPet, MCP Dev Toolkit (14 repos, 24 skills, 2 setup guides)](/hermes/skills/marketplace/new-june30-2026/)
- [🆕 June 29, 2026 — Coding Posture, Ultimate Humanizer, Clean Slate, Delegate Skills, AutoLoRA, WhatsApp Secretary, Safari Web Agent (7 repos, 7 skills, 7 setup guides)](/hermes/skills/marketplace/new-june29-2026/)
- [🆕 June 29, 2026 (Update) — OpenClaw/Clawd Ecosystem: clawdis (14), clawdirect (2), clawdstrike + 8 more repos (9 repos, 25 skills, 3 setup guides)](/hermes/skills/marketplace/new-june29-2026-update/)
- [🆕 June 28, 2026 — Threads Growth Skill, NemoClaw User Guide, Huawei Hermes Deployment (3 skills)](/hermes/skills/marketplace/new-june28-2026/)
- [🆕 June 28, 2026 (Update) — OpenClaw Email, Security, Finance, DevOps (14 repos, 17 skills, 4 setup guides)](/hermes/skills/marketplace/new-june28-2026-update/)
- [🆕 June 28, 2026 (Update 2) — sundial-org OpenClaw Collection, Marketing Skills, Audit Watchdog (2 repos, 9 skills, 2 setup guides)](/hermes/skills/marketplace/new-june28-2026-update2/)
- [🆕 June 28, 2026 (Update 3) — Agent Flywheel Mega-Toolkit, ClawDBot Feishu Suite + 7 standalone skills (9 repos, 44+ skills, 2 setup guides)](/hermes/skills/marketplace/new-june28-2026-update3/)
- [🆕 June 27, 2026 — Skills Gallery (1,672+ skills), A2A Bridge, Flight Recorder + 6 more (9 repos)](/hermes/skills/marketplace/new-june27-2026/)
- [🆕 June 26, 2026 (Afternoon) — Agenthood 14-Agent Team + Letta AI Full 24-Skill Harness (2 repos, 38 skills)](/hermes/skills/marketplace/new-june26-2026-afternoon/)
- [🆕 June 26, 2026 — Matt Pocock Toolkit, OpenClaw Ecosystem, Impeccable, CLI-Anything Harnesses (9 repos, 43 skills)](/hermes/skills/marketplace/new-june26-2026/)
- [🆕 June 22, 2026 (Late Sweep)  --  Blueprint Orchestration (1 repo, 12 skills)](/hermes/skills/marketplace/new-june22-2026-late/)
- [🆕 June 20-22, 2026  --  Hermes Bible, Steroids Image Gen, Ershov Memory Engine (6 repos, 15 skills)](/hermes/skills/marketplace/new-june20-22-2026/)
- [🆕 June 25, 2026 (Update) — CLI-Anything, Hermes Web UI, X/Twitter Scraper (3 repos, 3 skills)](/hermes/skills/marketplace/new-june25-2026-update/)
- [🆕 June 25, 2026 — GBrain Operations Expansion (1 repo, 33 skills)](/hermes/skills/marketplace/new-june25-2026/)
- [🆕 June 24, 2026 (Evening) — Hermes Agency, ContextForge RAG, Advanced Memory (4 setup guides)](/hermes/skills/marketplace/new-june24-2026-evening/)
- [🆕 June 24, 2026 — Ashima, SG Arrival Card, Perfectloop, Three-Agent Bridge (4 setup guides, 22 repos discovered)](/hermes/skills/marketplace/new-june24-2026/)
- [🆕 June 23, 2026  --  Engineering Curation, Ghostwriter, Cron Workflow, StepFun (8 repos, 3 setup guides)](/hermes/skills/marketplace/new-june24-2026/)
- [🆕 June 19-20, 2026  --  Ponytail, SkillSpector, AgentMint (12 skills)](/hermes/skills/marketplace/new-june19-20-2026/)
- [🆕 June 19, 2026 (Batch 2)  --  Infrastructure, Platform, Tools (15 repos, 20+ skills)](/hermes/skills/marketplace/new-june19-2026-batch2/)
- [🆕 June 19, 2026 (Update)  --  ECC-Hermes 36-Pack, SkillSpector Vetting, AgentMint (6 repos, 60+ skills)](/hermes/skills/marketplace/new-june19-2026-update/)
- [🆕 June 19, 2026  --  AgentMesh Async Bus + Windows Native (4 skills)](/hermes/skills/marketplace/new-june19-2026/)
- [🆕 June 28, 2026 (Update) — Skills.sh Late Sweep (3 repos)](/hermes/skills/marketplace/new-june28-2026-update/)
- [🆕 June 28, 2026 — Skills Ecosystem Expansion (12 repos, 30+ skills)](/hermes/skills/marketplace/new-june28-2026/)
- [🆕 June 27, 2026 — Hermes Ecosystem Discovery (10 repos, 28+ skills)](/hermes/skills/marketplace/new-june27-2026/)
- [🆕 June 26, 2026 (Afternoon) — Skills.sh API Sweep Round 2 (8 repos, 18+ skills)](/hermes/skills/marketplace/new-june26-2026-afternoon/)
- [🆕 June 26, 2026 — Skills.sh API Mega-Sweep (43 skills, 1.8M+ installs)](/hermes/skills/marketplace/new-june26-2026/)
- [🆕 June 25, 2026 (Update) — Late Sweep Additions (5 repos, 12+ skills)](/hermes/skills/marketplace/new-june25-2026-update/)
- [🆕 June 25, 2026 — Skills Ecosystem Expansion (8 repos, 20+ skills)](/hermes/skills/marketplace/new-june25-2026/)
- [🆕 June 24, 2026 (Evening) — Evening Sweep (4 repos, 10+ skills)](/hermes/skills/marketplace/new-june24-2026-evening/)
- [🆕 June 24, 2026 — Skills Discovery (6 repos, 15+ skills)](/hermes/skills/marketplace/new-june24-2026/)
- [🆕 June 23, 2026 — Skills Discovery (5 repos, 12+ skills)](/hermes/skills/marketplace/new-june23-2026/)
- [🆕 June 22, 2026 (Late) — Late Evening Sweep (3 repos, 8+ skills)](/hermes/skills/marketplace/new-june22-2026-late/)
- [🆕 June 20-22, 2026 — Weekend Discovery (8 repos, 18+ skills)](/hermes/skills/marketplace/new-june20-22-2026/)

- [🆕 June 18, 2026 (Final Sweep)  --  OpenClaw Extensions (8 skills)](/hermes/skills/marketplace/new-june18-2026-final-sweep/)
- [🆕 June 18, 2026 (Update 2)  --  HyperFrames Video Ecosystem (6 skills)](/hermes/skills/marketplace/new-june18-2026-update2/)
- [🆕 June 18, 2026 (Batch 2)  --  Full Catalog Sweep (107 skills)](/hermes/skills/marketplace/new-june18-2026-batch2/)
- [🆕 June 18, 2026 (Ecosystem)  --  Honcho + GBrain Skills (12 skills)](/hermes/skills/marketplace/new-june18-2026-ecosystem/)
- [🆕 June 18, 2026 (Batch 1)  --  nousresearch/hermes-agent (32 skills)](/hermes/skills/marketplace/new-june18-2026/)
- [🆕 June 17, 2026  --  nousresearch/hermes-agent (6 skills)](/hermes/skills/marketplace/new-june17-2026/)
- [🆕 June 16, 2026  --  ClawPilot ecosystem (5 skills)](/hermes/skills/marketplace/new-june16-2026/)
- [June 15, 2026  --  Nous Research Expansion (23 skills)](/hermes/skills/marketplace/new-june15-2026/)
- [June 12, 2026 Update  --  OpenClaw Security Suite (13 skills)](/hermes/skills/marketplace/new-june12-2026-update/)
- [June 12, 2026  --  Hermes Security Attestation (3 skills)](/hermes/skills/marketplace/new-june12-2026/)
- [June 11, 2026 Update 2  --  OpenClaw Ecosystem (23 skills)](/hermes/skills/marketplace/new-june11-2026-update2/)
- [June 11, 2026 Update  --  Agent Architecture (19 skills)](/hermes/skills/marketplace/new-june11-2026-update/)
- [June 11, 2026  --  Hermes Ecosystem (38 skills)](/hermes/skills/marketplace/new-june11-2026/)
- [June 10, 2026  --  Web Scraping, MCP, Testing, Stripe (42 skills)](/hermes/skills/marketplace/new-june10-2026/)
- [June 9, 2026  --  Initial Marketplace Discovery (42 skills)](/hermes/skills/marketplace/new-june9-2026/)

---

**Total: 527+ curated skill repos across 22 categories.** Install any with `npx skills add <owner/repo@skill>`. Updated as new skills are published.

*← [Skills Home](/hermes/skills/) | [Skills Catalog](/hermes/skills/catalog/) | [Latest Discoveries →](/hermes/skills/marketplace/new-june29-2026/)*

*Powered by CorpusIQ*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
