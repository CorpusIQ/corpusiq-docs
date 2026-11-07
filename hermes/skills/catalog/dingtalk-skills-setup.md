---
title: "DingTalk Skills - Enterprise Messaging for Agents"
description: "breath57/dingtalk-skills on skills.sh: 5.5K combined installs across 10 listings; curl-only DingTalk docs, tables, messages and calendar skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dingtalk-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "dingtalk", "enterprise messaging", "curl"]
---

# DingTalk Skills - Setup Guide

**Source:** [breath57/dingtalk-skills](https://www.skills.sh/breath57/dingtalk-skills) via skills.sh - 5.5K combined installs across 10 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 101 stars, no LICENSE file in the repository root, branch `main`, last pushed 2026-06-26, 10 `SKILL.md` directories under `.agents/skills/<name>/` with `AGENTS.md` at the root
**Category:** DingTalk operations for agents: documents, knowledge base, AI tables, group messages, calendars, to-dos and contacts over curl
**Quality Tier:** 🟡 Yellow - three of five sampled skills pass all three scanners while two carry a Snyk Warn, the repository has no LICENSE file, and the source docs are Chinese only.

DingTalk is Alibaba's enterprise messaging and work platform, widely used in Chinese companies for chat, documents, approval flows, attendance and calendars. This project wraps its OpenAPI as ten Agent Skills so an agent can read a knowledge base, add rows to an AI table, post a Markdown notice to a group, or create a to-do without anyone writing HTTP calls by hand.

The design constraint is stated twice in the README: depend on `curl` and nothing else. No SDK, no Python runtime, no third-party libraries, so the skills run wherever the host has `curl`. The second stated goal is token economy, keeping `SKILL.md` and `references/api.md` short enough that loading them does not dominate the context.

One practical note for English-speaking users: the README and every `SKILL.md` description are written in Chinese, and the repository links a `README_EN.md` for English. The skills also list English trigger keywords such as "dingtalk doc", "web search" and "send message", so an English prompt still matches, but the instructions the agent reads are Chinese.

## Installation

The README documents three routes per skill, all verified in the file. ClawHub first:

```bash
clawhub install breath57/dingtalk-document
```

The generic skills.sh route, which the README says works with Cursor, Claude, Copilot, OpenClaw and most other agents:

```bash
npx skills add breath57/dingtalk-skills@dingtalk-document
```

And the Hermes route, which is the one to use here:

```bash
npx skills add breath57/dingtalk-skills@dingtalk-document --agent hermes-agent -y
```

To install the whole suite in one command, the README gives this form for Hermes:

```bash
npx skills add breath57/dingtalk-skills \
  --skill dingtalk-document dingtalk-ai-table dingtalk-message dingtalk-todo dingtalk-contact dingtalk-ai-web-search dingtalk-calendar dingtalk-knowledge-search \
  --agent hermes-agent -y
```

Configuration happens on first use, not at install. The agent checks `~/.dingtalk-skills/config`, asks once for whatever is missing (`appKey`, `appSecret`, and the operator's DingTalk `userId`), and writes the answers there so later skills reuse them without asking again. Before that works you need an internal app created on the DingTalk open platform with the relevant API permissions enabled.

## What It Provides

Three listings clear the 500-install threshold, and they are the three highest-traffic surfaces in the product: documents, messages and AI tables.

| Skill | Installs | Use For |
|---|---|---|
| dingtalk-document | 1,822 | Knowledge base and document operations: list workspaces, browse the node tree, create docs and folders, read and write body blocks, manage member permissions |
| dingtalk-message | 1,589 | Sending messages: group webhook robot in text, Markdown, ActionCard, Link and FeedCard form, with signing, plus app-robot single and group chat, recall, read receipts and work notifications |
| dingtalk-ai-table | 666 | AI table (multi-dimensional table) work: list and manage sheets, read field definitions, batch insert records, page through records, update and delete by recordId |

The remaining 7 indexed listings range from 43 to 419 installs.

The tail covers the rest of the office suite. `dingtalk-todo` (419) creates, queries, updates and completes to-dos. `dingtalk-contact` (323) searches users and departments and returns full profiles, including the unionId and userId conversions. `dingtalk-calendar` (276) handles calendar events, free/busy queries, video meetings, meeting rooms and check-in links, including recurring events. `dingtalk-ai-web-search` (180) is web search with time-range filters and JSON output. `dingtalk-skill-creator` (86) and `skill-creator` (43) are authoring helpers, the first specific to new DingTalk skills, and `dingtalk-knowledge-search` (72) searches the knowledge base and exports documents to Markdown with image, diagram and CSV handling.

The README also lists three planned skills that are not shipped: `dingtalk-approval`, `dingtalk-attendance` and `dingtalk-meeting`. Do not plan around them.

## Why This Matters for Hermes Agents

Most agent work happens in English-language SaaS: Slack, Google Workspace, Notion. A company that runs on DingTalk has none of that, and the usual answer is a custom integration. Ten skills that speak the OpenAPI with `curl` turn that into a configuration task.

The dependency story is the strongest argument. A skill that needs a Python SDK needs a runtime, a virtualenv and a version pin inside whatever sandbox the agent runs in. These skills need `curl`, which every Unix-like host and most agent containers already have, so an agent can operate DingTalk from a minimal environment.

The shared config store is the second gain. One prompt for `appKey`, `appSecret` and the operator id, one write to `~/.dingtalk-skills/config`, and every skill in the suite reads from it. That also creates a single file to protect, which is easier to reason about than credentials spread across ten skill directories.

The third is that the trigger lists are unusually thorough. Each Chinese description enumerates the phrases and English keywords that should activate it, which is what makes an agent pick the calendar skill for "book a room" instead of guessing at an API.

## Usage

| You say | What happens |
|---|---|
| "List my DingTalk knowledge bases" | `dingtalk-document` calls the wiki workspace endpoint with the operator id and returns the workspaces the account can access |
| "Add a record to the requirements sheet: title login rework, priority high" | `dingtalk-ai-table` reads the field definitions, matches the column names, then inserts the row |
| "Post to the team group that v2.1 shipped, Markdown" | `dingtalk-message` builds a Markdown webhook payload, signs it if the robot uses the signed mode, and posts it |
| "What is Zhang San's phone number and department?" | `dingtalk-contact` searches users, fetches the profile and returns phone, job number, position and department path |
| "Book a one hour review tomorrow at 3pm" | `dingtalk-calendar` creates the event under the primary calendar in UTC ISO8601, and can attach a meeting room by roomId |
| "Create a to-do to finish the competitor report by next Friday" | `dingtalk-todo` sets the due date, priority and description, then creates the task |
| "Pull the background docs for project A into this repo as Markdown" | `dingtalk-knowledge-search` searches the knowledge base, exports the bodies, localises images and writes files |

## Verification

Read a skill before installing it. Both paths returned HTTP 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/breath57/dingtalk-skills/main/.agents/skills/dingtalk-document/SKILL.md | head -30
curl -fsSL https://raw.githubusercontent.com/breath57/dingtalk-skills/main/.agents/skills/dingtalk-message/SKILL.md | head -30
```

The first should open with `name: dingtalk-document` and a Chinese description listing document triggers. The second should list the webhook, app-robot and work-notification operations, along with the rule that credentials are never printed in full.

After install, confirm the directory count matches the index:

```bash
ls .agents/skills | wc -l
```

The repository tree holds 10 skill directories, and the index lists 10 listings, so the counts agree here. Then confirm the config file exists after your first run:

```bash
ls -l ~/.dingtalk-skills/config
```

If it is missing, the agent never reached its configuration step; ask it to set up DingTalk explicitly.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| dingtalk-document | Pass | Pass | Warn |
| dingtalk-ai-table | Pass | Pass | Warn |
| dingtalk-calendar | Pass | Pass | Pass |
| dingtalk-skill-creator | Pass | Pass | Pass |
| skill-creator | Pass | Pass | Pass |

Two of the five sampled skills carry a Snyk Warn, and both are among the three most installed listings. The likely reason is the shape of the work rather than anything malicious: these skills hold long API reference files and shell snippets that post to an external service, which is exactly the pattern scanners flag. Read `references/api.md` in the skills you plan to use before you trust them with a production tenant.

Credentials are the real risk surface. The design collects `appKey`, `appSecret` and an operator id into `~/.dingtalk-skills/config`, and the installed `SKILL.md` states that credentials must never be printed in full, showing only the first four characters on confirmation. That is a good rule, but it is enforced by instructions to the model, not by code, so treat the config file as a secret and keep it out of any repository. Scope the DingTalk app to the APIs you actually need, because an agent with a broad app secret can read the whole corporate directory.

The repository has no LICENSE file in its root, even though the README's licence section says MIT. Until a file exists, treat the terms as stated but not formally granted.

## Limitations

- Snapshot data, verified 2026-11-07: 5,476 combined installs across 10 indexed listings; 101 GitHub stars; no LICENSE file; last pushed 2026-06-26. Counts drift over time.
- Documentation is Chinese. The README, every `SKILL.md` description and the API references are written in Chinese, with a `README_EN.md` link for the README only, so the agent and the reviewer both need to read Chinese to audit a skill properly.
- No LICENSE file in the repository root, despite the README's licence section stating MIT. Reuse terms are stated rather than granted in the usual way.
- The curl-only claim does not hold for every skill. The project structure section lists `scripts/cli.py` for `dingtalk-knowledge-search` and a `pdftotext` dependency for its PDF mode, so one skill is not pure shell.
- Two Snyk Warns in the sample (`dingtalk-document`, `dingtalk-ai-table`), on listings that carry most of the installs.
- Everything is gated on a DingTalk enterprise tenant: an internal app, enabled API permissions and a real `userId` are prerequisites, so the suite cannot be evaluated against a throwaway account.

## Related

- [Lark & Feishu Skills - Office Suite Automation Setup](/hermes/skills/catalog/lark-feishu-skills-setup)
- [WeCom Unified Skill - WeChat Work Routing Suite Setup](/hermes/skills/catalog/wecom-unified-skills-setup)
- [Tencent CloudBase Agent Skills - WeChat Dev](/hermes/skills/catalog/tencent-cloudbase-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill first. `dingtalk-document` at 1,822 installs is the most exercised path and the quickest way to prove the config flow before you add the rest.
- Ask in Chinese if the answer looks thin. The trigger lists are Chinese first, and the same request phrased in Chinese lands closer to the enumerated phrases the skill matches on.
- Keep the config file out of backups you share. `~/.dingtalk-skills/config` holds the app secret in plain text by design.
- Prefer the AI table skill over document append for structured data. Records have field definitions and recordIds, so updates and deletes are possible later.
- Check the `references/api.md` of any skill you adopt for write operations. The PATCH and DELETE bodies are where an agent's mistake is least recoverable.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
