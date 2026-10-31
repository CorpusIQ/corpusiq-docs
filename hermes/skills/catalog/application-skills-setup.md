---
title: "Application Skills - SaaS Integration Suite Setup"
description: "membranedev/application-skills: 58.0K combined installs. 3,074 per-app skills let an agent drive Membrane's managed integrations for 3,000+ SaaS apps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/application-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "saas integrations", "membrane", "oauth", "api"]
---

# Application Skills - Setup Guide

**Source:** [membranedev/application-skills](https://www.skills.sh/membranedev/application-skills) via skills.sh - 58.0K combined installs across 200 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [membranedev/application-skills](https://github.com/membranedev/application-skills) - 270 stars, no LICENSE file at root (GitHub license field: none), branch main, last pushed 2026-04-28; 3,074 flat directories under `skills/`, each holding exactly one `SKILL.md` and nothing else

**Category:** Per-app SaaS integrations packaged as Agent Skills over Membrane's managed auth layer

**Quality Tier:** 🟡 Yellow - four of the five sampled skills carry a Snyk Warn, and the repository has no LICENSE file at root, so the audit trail and the licence both need a human pass before production use

Membrane publishes this as `membranedev/application-skills`: one skill per SaaS app, 3,074 of them, covering the long tail from Google Drive and Outlook to NetSuite, Sitecore and Cisco Meraki. Each skill is a single markdown file that teaches an agent the app's structure (entities such as files, permissions and shared drives), the actions Membrane already exposes for it, and how to run those actions through the Membrane CLI. The README frames the promise plainly: drop-in support for OpenClaw, Cursor, Claude Code, GitHub Copilot, Gemini CLI and anything else that reads the Agent Skills spec.

The important caveat is in the frontmatter of every one of the 3,074 files. The `compatibility` field reads "Requires network access and a valid Membrane account (Free tier supported)", and the body of each skill routes every real call through `membrane login`, `membrane connection ensure` and `membrane action run`. These are not self-contained API wrappers: they are thin, well-written instructions for driving Membrane's managed integration layer, which holds the OAuth tokens and API keys server-side on the user's behalf. Install one and you get an agent that knows which actions exist for that app; you do not get an agent that can call the app without a Membrane account or API key behind it.

## Installation

The README states only one install route, `npx skills add`, keyed by skill name, and the skill name is the folder name:

```bash
npx skills add membranedev/application-skills --skill google-drive
```

Every skill also needs the Membrane CLI, which is where the actual work happens. This block is copied from the body of the skill files themselves:

```bash
npm install -g @membranehq/cli@latest
membrane login --tenant --clientName=<agentType>
```

In a headless session the login prints an authorization URL for the user to open, and the flow finishes with the code it returns:

```bash
membrane login complete <code>
```

Because each skill is one file in one flat directory, a plain copy is an equally valid install and is the route that fits a Hermes profile with no skills CLI in the loop:

```bash
cp -r skills/google-drive ~/.hermes/profiles/corpusiq/skills/google-drive
```

The checkout used for this guide holds 3,074 skill directories, each with a `SKILL.md` and no companion `scripts/`, `references/` or `assets/` folder, so nothing is lost by copying the directory. There is no suite-wide manifest and no single file that installs all of them: pick the apps you actually use.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| google-drive | 2,911 | Files, folders, shared drives and permissions: list and get items, create folders, and share or unshare by creating and deleting permissions. |
| microsoft-outlook | 2,538 | Communication data and records for an Outlook mailbox: email, calendar events, contacts and tasks. |
| confluence | 2,048 | Document management work in a Confluence site: spaces, pages, blog posts and attachments. |
| asana | 1,900 | Project and ticketing data: tasks, projects, sections, workspaces and users. |
| microsoft-sharepoint | 1,609 | Site collections and the lists and libraries underneath them. |
| dropbox | 1,339 | Accounts, files, folders and shared links in Dropbox storage. |
| salesforce | 1,329 | CRM and marketing automation records: leads, accounts, contacts, opportunities and the workflows around them. |
| onedrive | 1,302 | OneDrive accounts, files and folders for personal and shared storage. |
| box | 1,256 | Folders, users, groups and collaborations, including who can see what. |
| hubspot | 858 | CRM and marketing automation records: contacts, companies, deals and pipelines. |
| gmail | 782 | Communication records in a Gmail mailbox: messages, threads and labels. |
| freshdesk | 653 | Support queues: tickets, contacts, companies, agents, groups and forums. |
| google-sheets | 575 | Analytics data and records held in Google Sheets workbooks. |
| zoho-crm | 574 | CRM and marketing automation records inside Zoho CRM. |
| slack | 569 | Communication and notification work: channels, messages and users. |
| dynamics-crm | 544 | CRM and sales records in Microsoft Dynamics 365. |
| google-tasks | 481 | Task lists and tasks, plus the workflow steps around them. |
| monday | 424 | Boards, items and groups for project management work. |
| pipedrive | 415 | CRM and sales records: deals, people, organizations and pipelines. |
| calendly | 394 | Users and scheduled events for booking and meeting workflows. |

The remaining 180 indexed listings range from 149 to 383 installs.

The twenty rows above are the only listings at or above the pack threshold. The files are generated from one template and it shows: the app overview, install the CLI, authentication, connecting to the app, searching for actions, a Popular actions table, running actions, a proxy escape hatch, then best practices. A count across the checkout finds the proxy section and the best practices block in all 3,074 files, and the setup steps worded identically in roughly 3,000 of them. That uniformity is the point and also the limit, and it makes the Popular actions table the most useful part of any single file.

## Why This Matters for Hermes Agents

The hard part of giving an agent real SaaS access has never been the HTTP call, it is the credential lifecycle. Every skill here is written to keep secrets out of the prompt and out of the profile: the agent runs `membrane connection ensure` against the app's own URL, the user completes OAuth or hands an API key to Membrane in a browser, and the agent only ever sees a connection id it can pass to `membrane action run`. For a Hermes profile that touches client systems, that split is worth more than the action list, because a leaked connection id is revocable and a leaked refresh token is not.

The per-app granularity is the second win. Capability is scoped by which directories you copy: a profile that only needs Drive and Sheets gets two skills, not a 3,074-skill catalog that dilutes routing and burns context on every session. Each file is one markdown document, around 173 lines and 12 KB on average, so the whole install stays cheap, and the `description` field names the app and the trigger situation, which is what a skills index uses to decide whether to load it.

The generated uniformity also removes a common failure mode. Because the workflow, the auth dance and the proxy pattern are identical across every app, an agent that has read one of these files can operate any of the others, and a fix to the pattern propagates by regenerating rather than by hand-editing thousands of documents. The counterweight is depth: these files describe actions Membrane already exposes and link to official app docs for everything else, so genuinely unusual endpoints end up going through `membrane request` with the agent authoring the path and body itself.

## Usage

| You say | What happens |
|---|---|
| "Connect to Google Drive and find last quarter's invoices" | The Drive skill runs `membrane connection ensure "https://drive.google.com/drive" --json`, and if the connection comes back `BUILDING` it long-polls `connection get <id> --wait` until the state reads `READY`. |
| "Who still has access to the board deck?" | The skill resolves the file id, runs the permissions lookup, and reports each permission with its role and type instead of guessing from the sharing UI. |
| "Stand up a Confluence page from these meeting notes" | The Confluence skill picks the space, creates the page, and attaches the notes, all through actions on the existing connection. |
| "File this as a Freshdesk ticket for the support group" | The Freshdesk skill resolves the group and contact ids first, then runs the create action with those ids rather than free text. |
| "Append today's numbers to the metrics sheet" | The Sheets skill finds the append action for the target range and writes the row, keeping the header row untouched. |
| "There is no action for this endpoint" | The skill falls back to `membrane request CONNECTION_ID /path/to/endpoint`, which appends the app's base URL and injects auth headers plus transparent refresh. |
| "Do not put my API key in the prompt" | The best practices block in every file says to create a connection instead, so credentials stay on Membrane's side and the agent only holds the connection id. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/membranedev/application-skills/main/skills/google-drive/SKILL.md
```

Expect `200`. Read the file before installing it: the two fields that matter for routing are `description`, which should name the app and the situations it covers, and `compatibility`, which should still say a Membrane account is required, because that sentence is the honest statement about what the skill can do on its own.

After the copy lands in the profile, confirm the file and the tree it came from:

```bash
head -12 ~/.hermes/profiles/corpusiq/skills/google-drive/SKILL.md
ls -d /tmp/oct30e/repos/membranedev-application-skills/skills/*/ | wc -l
membrane login --tenant --clientName=<agentType>
```

A good copy shows `name: google-drive`, the one-line description, `license: MIT` and the `compatibility` line naming the Membrane account, the directory count reads `3074`, and the login either opens a browser or prints an authorization URL you can hand to the user.

## Security

Four of the five sampled skills carry a Snyk Warn, so treat this suite as warned rather than clean: a Snyk warning means the scan flagged something in the package it could not clear automatically, and on a skill that runs a CLI against live SaaS accounts that is a reason to read the file and the CLI release notes before pointing it at client data. The one clean sample, `dispatch`, passed all three auditors, which shows the warnings are per-file rather than a blanket verdict on the repository. Verdicts below are skills.sh results sampled on 2026-10-30 - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| google-drive | Pass | Warn | Warn |
| microsoft-outlook | Pass | Pass | Warn |
| confluence | Pass | Pass | Warn |
| asana | Pass | Warn | Warn |
| dispatch | Pass | Pass | Pass |

No Gen Agent Trust Hub failure appears in the sample, so the risk is not a hostile or obfuscated package. The real exposure is architectural and worth stating plainly: every skill asks the agent to authenticate against Membrane and then to run remote actions on the user's connected accounts, which means the app data passes through a third party and the blast radius of a bad action is whatever that connection can reach. The `membrane request` proxy is the sharpest edge in the set, because it will forward a hand-written path and body to a live API with valid credentials attached, and no scanner can review a request that does not exist yet.

## Limitations

- Snapshot data, verified 2026-10-30: 57,985 combined installs across 200 indexed listings; 270 GitHub stars; no LICENSE file at root; last pushed 2026-04-28. Counts drift over time.
- The licence is unresolved. Every `SKILL.md` carries `license: MIT` and the README badge links to a `LICENSE` file, but the repository root holds only `README.md`, `skills/` and `.github/images`, so the MIT grant cannot be confirmed from the tree. Ask before redistributing.
- The index covers a fraction of the tree: 200 indexed listings against 3,074 skill directories, so roughly 2,874 skills have no install signal at all, and the numbers above describe the popular head rather than the suite.
- Nothing works without Membrane. The free tier is supported, but every skill needs network access and a Membrane account, actions run on Membrane's servers, and the app data transits that layer. There is no offline or self-hosted path documented in the files.
- The files are generated and deliberately shallow. Each one is the same template around a Popular actions table and a link to the app's official API docs, so edge cases, app-specific quirks and rate limit handling are the agent's problem.
- The repository was last pushed 2026-04-28, about six months before this guide. The pattern still holds, but individual apps ship API changes faster than that, so verify the action list against the live app before trusting it.

## Related

- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [Anthropic Claude API Skills - Official Claude API](/hermes/skills/catalog/anthropics-claude-api-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy one directory per app, not the suite. The checkout is about 38 MB across 3,074 folders, and a profile that loads a thousand app skills spends its routing budget on apps it will never call.
- Read the Popular actions table before writing any HTTP. It is a name, key and description per action, and it is the difference between one `action run` and a hand-rolled request that misses pagination and field mapping.
- Use `membrane connection ensure "<app url>"` as the default connect step, and pass `--json`. It normalizes the URL to a domain, builds a connector if none exists, and returns the connection id the rest of the workflow needs.
- Treat a `BUILDING` state as normal rather than as an error. `connection get <id> --wait` long-polls until the connector is ready, and the state tells you whether the user must act (`CLIENT_ACTION_REQUIRED`) or whether you can proceed.
- Keep `--json` on every call and read the `output` field of the response. The skills document it as the result location for action runs, and parsing prose instead is where most of these integrations break.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
