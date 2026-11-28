---
title: "Build With Claude - Claude Skills and Plugins Discovery Hub"
description: "davepoon/buildwithclaude: 15.2K combined installs. A discovery hub for Claude skills, agents, commands, hooks, plugins and marketplace collections."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/buildwithclaude-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "plugins", "marketplace"]
---

# Build With Claude - Setup Guide

**Source:** [davepoon/buildwithclaude](https://www.skills.sh/davepoon/buildwithclaude) via skills.sh - 15.2K combined installs across 96 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude) - 3,807 stars, MIT, branch main, last pushed 2026-11-26; skills live under plugins/all-skills/skills/<name>/SKILL.md, agents under plugins/agents-*/agents, commands under plugins/commands-*/commands and hooks under plugins/hooks-*/hooks, with a Next.js web UI in web-ui/.

**Category:** Claude Code extension discovery - skills, agents, commands, hooks, plugins and marketplace collections

**Quality Tier:** 🟡 Yellow - no Fail cells in the 20-skill sample; eight skills carry Warn cells: one Gen Agent Trust Hub Warn (server-actions), six Socket Warns and five Snyk Warns.

Build With Claude is a discovery hub, not a single product suite. It aggregates Claude Skills, Agents, Commands, Hooks, Plugins and Marketplace collections that extend Claude Code, Claude Desktop, the Agent SDK and OpenClaw. The repository curates those pieces as bundled plugins under plugins/, with the README counting 117 agents, 175 commands, 28 hooks and 26 skills, and ships a Next.js web UI at buildwithclaude.com that indexes the wider ecosystem (20k+ community plugins, 4,500+ MCP servers and 1,100+ plugin marketplaces).

The skills.sh index lists 96 entries for this hub, and the install band is flat: anti-ui-slop leads at 884 installs, the only listing above 500, and the rest run from 356 down to 124. That shape is the tell of a hub of many small skills rather than a product suite with flagship entries. A reader installing from this repo gets a large catalog of small, single-purpose skills, more than half of them automation skills named for the service they wrap, alongside the agent, command and hook collections that ship with them.

## Installation

Build With Claude installs as a Claude Code plugin marketplace. The README quick start adds the marketplace, then installs individual plugins:

```text
/plugin marketplace add davepoon/buildwithclaude
/plugin search @buildwithclaude
/plugin install <plugin-name>@buildwithclaude
```

The README recommends the marketplace path. To install specific collections, target the category plugins (agents-python-expert, commands-version-control-git, hooks-notifications), or install the whole bundled sets:

```text
/plugin install all-agents@buildwithclaude
/plugin install all-commands@buildwithclaude
/plugin install all-hooks@buildwithclaude
```

The manual path clones the repository and copies the markdown files into the Claude Code directories:

```bash
git clone https://github.com/davepoon/buildwithclaude.git
cd buildwithclaude
find plugins/agents-*/agents -name "*.md" -exec cp {} ~/.claude/agents/ \;
find plugins/commands-*/commands -name "*.md" -exec cp {} ~/.claude/commands/ \;
```

Restart Claude Code afterward. For non-Claude runtimes there is no packaged installer: the skill, agent, command and hook files are plain markdown, so the practical path is to read the SKILL.md files you want and adapt them into your own agent's skill directory.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| anti-ui-slop | 884 | Stop agents shipping generic UI by defining a design contract against real product screens. |
| file-organizer | 356 | Organize files and folders, find duplicates and automate cleanup. |
| webapp-testing | 305 | Test local web apps with Playwright: verify frontends, debug UI, capture screenshots. |
| competitive-ads-extractor | 288 | Extract and analyze competitor ads from Facebook and LinkedIn ad libraries. |
| artifacts-builder | 264 | Build multi-component claude.ai HTML artifacts with React, Tailwind and shadcn/ui. |
| xlsx | 259 | Create, edit and analyze spreadsheets with formulas, formatting and visualization. |
| canvas-design | 259 | Create posters and static visual art as .png and .pdf files. |
| content-research-writer | 236 | Research, cite and iterate on long-form written content. |
| server-actions | 204 | Next.js Server Actions for data mutations and form submissions. |
| docx | 202 | Create, edit and analyze Word documents with tracked changes and comments. |
| macos-design | 200 | Design native-feeling macOS application UIs. |
| brand-guidelines | 196 | Apply Anthropic brand colors and typography to artifacts. |
| auth-patterns | 184 | Next.js authentication: NextAuth, middleware auth and session management. |
| pptx | 170 | Create, edit and analyze PowerPoint presentations. |
| image-enhancer | 170 | Improve image resolution, sharpness and clarity, especially screenshots. |
| lead-research-assistant | 162 | Identify high-quality leads and contact strategies for a product. |
| instagram-automation | 162 | Automate Instagram posts, carousels and insights via Rube MCP (Composio). |
| bitbucket-automation | 162 | Automate Bitbucket repos, pull requests and issues via Rube MCP (Composio). |
| obsidian-markdown | 159 | Create and edit Obsidian Flavored Markdown with wikilinks and callouts. |
| json-canvas | 159 | Create and edit JSON Canvas files with nodes, edges and groups. |
| outlook-calendar-automation | 159 | Automate Outlook calendar tasks. |
| server-components | 158 | Next.js Server Components for data fetching and composition. |
| changelog-generator | 156 | Generate changelogs. |
| route-handlers | 153 | Next.js route handlers for CRUD APIs and HTTP methods. |
| app-router | 153 | Next.js App Router routing, layouts and loading states. |
| skill-creator | 153 | Scaffold and package new skills. |
| theme-factory | 152 | Apply visual themes (color and typography sets) to artifacts. |
| meeting-insights-analyzer | 152 | Analyze meetings for insights. |
| mcp-builder | 151 | Build MCP servers and tools. |
| obsidian-bases | 151 | Create and edit Obsidian Bases databases. |
| invoice-organizer | 151 | Organize invoices. |
| canva-automation | 151 | Automate Canva design tasks. |
| domain-name-brainstormer | 150 | Brainstorm domain names. |
| pdf | 149 | Create, edit and analyze PDF documents. |
| youtube-automation | 144 | Automate YouTube tasks. |
| tailored-resume-generator | 143 | Generate tailored resumes. |
| developer-growth-analysis | 143 | Analyze developer growth. |
| slack-gif-creator | 142 | Create animated GIFs for Slack. |
| google-calendar-automation | 142 | Automate Google Calendar tasks. |
| skill-share | 141 | Share skills. |
| internal-comms | 141 | Draft internal communications and updates. |
| tiktok-automation | 140 | Automate TikTok tasks. |
| outlook-automation | 140 | Automate Outlook tasks. |
| clickup-automation | 139 | Automate ClickUp tasks. |
| agent-analytics | 137 | Analyze agent usage. |
| oiloil-ui-ux-guide | 136 | UI and UX design guidance. |
| github-automation | 136 | Automate GitHub tasks. |
| raffle-winner-picker | 136 | Pick raffle winners. |
| ios-hig-design-guide | 134 | Apple Human Interface Guidelines for iOS design. |
| airtable-automation | 134 | Automate Airtable tasks. |
| google-drive-automation | 133 | Automate Google Drive tasks. |
| asana-automation | 133 | Automate Asana tasks. |
| amplitude-automation | 132 | Automate Amplitude tasks. |
| todoist-automation | 131 | Automate Todoist tasks. |
| linkedin-automation | 131 | Automate LinkedIn tasks. |
| jira-automation | 131 | Automate Jira tasks. |
| gmail-automation | 131 | Automate Gmail tasks. |
| dropbox-automation | 131 | Automate Dropbox tasks. |
| confluence-automation | 131 | Automate Confluence tasks. |
| twitter-algorithm-optimizer | 130 | Optimize Twitter/X posting for the algorithm. |
| google-analytics-automation | 130 | Automate Google Analytics tasks. |
| figma-automation | 130 | Automate Figma tasks. |
| zoom-automation | 129 | Automate Zoom tasks. |
| telegram-automation | 129 | Automate Telegram tasks. |
| salesforce-automation | 129 | Automate Salesforce tasks. |
| twitter-automation | 128 | Automate Twitter/X tasks. |
| notion-automation | 128 | Automate Notion tasks. |
| whatsapp-automation | 128 | Automate WhatsApp tasks. |
| slack-automation | 128 | Automate Slack tasks. |
| googlesheets-automation | 128 | Automate Google Sheets tasks. |
| discord-automation | 128 | Automate Discord tasks. |
| activecampaign-automation | 128 | Automate ActiveCampaign tasks. |
| supabase-automation | 127 | Automate Supabase tasks. |
| reddit-automation | 127 | Automate Reddit tasks. |
| klaviyo-automation | 127 | Automate Klaviyo tasks. |
| freshdesk-automation | 127 | Automate Freshdesk tasks. |
| webflow-automation | 126 | Automate Webflow tasks. |
| shopify-automation | 126 | Automate Shopify tasks. |
| pipedrive-automation | 126 | Automate Pipedrive tasks. |
| pagerduty-automation | 126 | Automate PagerDuty tasks. |
| microsoft-teams-automation | 126 | Automate Microsoft Teams tasks. |
| hubspot-automation | 126 | Automate HubSpot tasks. |
| calendly-automation | 126 | Automate Calendly tasks. |
| brevo-automation | 126 | Automate Brevo tasks. |
| trello-automation | 125 | Automate Trello tasks. |
| sendgrid-automation | 125 | Automate SendGrid tasks. |
| render-automation | 125 | Automate Render tasks. |
| make-automation | 125 | Automate Make tasks. |
| gitlab-automation | 125 | Automate GitLab tasks. |
| docusign-automation | 125 | Automate DocuSign tasks. |
| sentry-automation | 124 | Automate Sentry tasks. |
| segment-automation | 124 | Automate Segment tasks. |
| one-drive-automation | 124 | Automate OneDrive tasks. |
| monday-automation | 124 | Automate Monday.com tasks. |
| mailchimp-automation | 124 | Automate Mailchimp tasks. |
| linear-automation | 124 | Automate Linear tasks. |

All 96 indexed listings appear in the table above. The install band is flat (124 to 884) because this is a hub of many small skills, not a product suite with flagship entries.

## Why This Matters for Hermes Agents

Build With Claude is a reference for the marketplace pattern more than a place to grab one killer skill. It shows how to bundle many small capabilities into category plugins (agents-*, commands-*, hooks-*, all-skills) and expose them through a single plugin.json marketplace entry, which is the same structure a Hermes builder needs when publishing a library of skills.

The content is portable by construction. Skills, agents, commands and hooks are all plain markdown with YAML frontmatter, so any agent runtime can read them directly; a Hermes agent does not need Claude Code to mine the SKILL.md files for ideas or to adapt a workflow. The only Claude Code-specific surface is the install ergonomics: the /plugin slash commands and the ~/.claude/ copy target.

The repo also ships its own registry tooling: schema files (skill-schema.json, command-schema.json, hook-schema.json) and validators (validate-skills.js, validate-commands.js, validate-hooks.js) that run as part of the plugin test workflow. That is a working, copyable validation pipeline for a skill catalog, complete with a generate-registry.js script that builds the marketplace manifest.

The flat install band is a useful read on discovery hubs generally. When one repo aggregates many small, single-purpose skills, usage spreads thin across them instead of concentrating in a flagship. That is why the top listing (anti-ui-slop, 884 installs) is the only one above 500, and why the catalog is worth browsing for specific gaps rather than installing wholesale.

## Usage

| You say | What happens |
|---|---|
| "Audit this UI for generic AI-slop design" | Loads anti-ui-slop, the top-listed skill, to define a design contract against real product screens. |
| "Test this local web app and show me the browser logs" | Uses webapp-testing to drive the app with Playwright and capture screenshots and console logs. |
| "Build a multi-file HTML artifact with React and Tailwind" | Uses artifacts-builder to scaffold a multi-component claude.ai artifact. |
| "Create a report with tracked changes" | Uses docx to create and edit a Word document with comments and tracked changes. |
| "Make a spreadsheet with formulas from this data" | Uses xlsx to build the workbook with formulas, formatting and visualization. |
| "Automate my Jira workflow" | Uses jira-automation to drive Jira tasks. |
| "Set up authentication in my Next.js app" | Uses auth-patterns for NextAuth, middleware auth and session management. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/davepoon/buildwithclaude/main/plugins/all-skills/skills/anti-ui-slop/SKILL.md
```

After a clone, confirm the plugin layout and read a skill before adapting it:

```bash
git clone --depth 1 https://github.com/davepoon/buildwithclaude.git /tmp/buildwithclaude
ls /tmp/buildwithclaude/plugins/all-skills/skills/ | head
head -5 /tmp/buildwithclaude/plugins/all-skills/skills/anti-ui-slop/SKILL.md
```

The first command should list skill directories under the all-skills plugin, and head should show the anti-ui-slop frontmatter (its name and description). Because every skill, agent, command and hook is plain markdown with YAML frontmatter, you can read any file directly before deciding what to carry into a Hermes profile.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| anti-ui-slop | Pass | Pass | Warn |
| file-organizer | Pass | Pass | Pass |
| webapp-testing | Pass | Warn | Warn |
| competitive-ads-extractor | Pass | Pass | Warn |
| artifacts-builder | Pass | Warn | Pass |
| xlsx | Pass | Warn | Pass |
| canvas-design | Pass | Pass | Pass |
| content-research-writer | Pass | Pass | Pass |
| server-actions | Warn | Warn | Pass |
| docx | Pass | Pass | Pass |
| macos-design | Pass | Pass | Pass |
| brand-guidelines | Pass | Pass | Pass |
| auth-patterns | Pass | Pass | Pass |
| pptx | Pass | Pass | Pass |
| image-enhancer | Pass | Pass | Pass |
| lead-research-assistant | Pass | Pass | Pass |
| instagram-automation | Pass | Warn | Warn |
| bitbucket-automation | Pass | Warn | Warn |
| obsidian-markdown | Pass | Pass | Pass |
| json-canvas | Pass | Pass | Pass |

This guide is Yellow because the sample has no Fail cells but eight of twenty skills carry Warn cells. The Gen Agent Trust Hub warns once, on server-actions. Socket warns on six skills (webapp-testing, artifacts-builder, xlsx, server-actions, instagram-automation and bitbucket-automation), and Snyk warns on five (anti-ui-slop, webapp-testing, competitive-ads-extractor, instagram-automation and bitbucket-automation). The repository is mostly markdown skills, agents, commands and hooks plus a Next.js web app and Node.js validation scripts, so the flags are worth reading on the skills.sh security pages before installing into a production profile.

## Limitations

- Snapshot data, verified 2026-11-27: 15,215 combined installs across 96 indexed listings; 3,807 GitHub stars; MIT; last pushed 2026-11-26. Counts drift over time.
- This is a discovery hub, not a product suite: the install band is flat (124 to 884) and the top listing is the only one above 500, so ranking by installs is a catalog signal, not a quality signal.
- Installation is Claude Code-centric: the marketplace and plugin commands are Claude Code slash commands, and the manual path copies files into ~/.claude/ directories, so other runtimes must read and adapt the markdown files directly.
- Some skill names ship under more than one plugin: json-canvas and obsidian-markdown appear in both all-skills and obsidian-skills, and the Next.js skills (auth-patterns, server-actions, server-components, route-handlers, app-router) live in the nextjs-expert plugin.
- Twenty of ninety-six listings are sampled for security verdicts; the other seventy-six have no published verdicts in this snapshot, so treat the sample as indicative rather than exhaustive.

## Related

- [Claude Office Skills Suite - Business Document Skills](/hermes/skills/catalog/claude-office-skills-suite-setup)
- [Skill Vetting Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/skill-vetting-setup)
- [Advanced Skill Creator - Custom Skill Generation Setup](/hermes/skills/catalog/advanced-skill-creator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install via the marketplace on Claude Code (the README's recommended option) rather than the manual copy, so plugin updates and the marketplace catalog arrive together.
- Treat the flat install counts as a catalog signal: anti-ui-slop is the only listing above 500 installs, so browse for specific gaps instead of installing the whole hub.
- Read each SKILL.md before carrying it into a Hermes profile: every skill, agent, command and hook is plain markdown with YAML frontmatter, so there is no conversion step and nothing executes on install.
- Watch the Socket and Snyk Warn cells on the automation skills. The two with published descriptions (instagram-automation and bitbucket-automation) both wrap Composio's Rube MCP, so these integrate live third-party services rather than local logic.
- Steal the registry tooling: schema files (skill-schema.json, hook-schema.json, command-schema.json) plus validate-skills.js and generate-registry.js are a working, copyable validation pipeline for a skill catalog.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
