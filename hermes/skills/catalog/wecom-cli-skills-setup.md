---
title: "WeCom CLI Skills — Enterprise WeChat Agent Suite Setup"
description: "wecomteam/wecom-cli — 28 skills, 153.4K installs: official WeChat Work (WeCom) docs, meetings, contacts, todos, messages, and smartsheet skills for agent assistants."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wecom-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "wecom", "wechat work", "enterprise", "productivity"]
---

# WeCom CLI Skills — Setup Guide

**Source:** [wecomteam/wecom-cli](https://skills.sh/wecomteam/wecom-cli)
**GitHub:** [wecomteam/wecom-cli](https://github.com/wecomteam/wecom-cli)
**Skills:** 28 skills · 153.4K total installs
**Category:** Enterprise Productivity
**First Seen:** catalogued August 18, 2026 sweep (wecomcli-doc on skills.sh since April 2, 2026)
**Quality Tier:** 🟡 Trusted — official WeCom team org; flagship wecomcli-doc passes Gen Agent Trust Hub and Socket, Snyk Warn (named)

The official WeChat Work (WeCom, Tencent's enterprise IM) agent suite gives assistants command-line control of enterprise docs, meetings, contacts, todos, messages, schedules, and smartsheets. At 153.4K installs across 28 skills it is the largest enterprise-productivity cluster on the platform from a first-party vendor org, with 2.7K GitHub stars and skill docs maintained in Chinese by the WeCom team.

---

## Installation

```bash
npx skills add wecomteam/wecom-cli
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/wecomteam/wecom-cli --skill wecomcli-doc
```

## Prerequisites

| Requirement | Details |
|---|---|
| **wecom-cli CLI** | `npm install -g @wecom/cli`, version 1.1.0 or higher (verified via `wecom-cli --version`) |
| **Node.js + npx** | For the skill installer and CLI runtime |
| **WeCom account** | Authenticated enterprise WeChat Work tenant for live operations |
| **wecomcli-shared skill** | Holds the common pre-checks every other skill in the suite references before running commands |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| wecomcli-doc | 17.1K | Doc creation, import, append, and content read/write |
| wecomcli-todo | 16.9K | Todo list operations and task detail management |
| wecomcli-contact | 16.9K | Contact lookup and address book access |
| wecomcli-meeting | 16.8K | Meeting discovery and retrieval |
| wecomcli-msg | 16.5K | Message reading and messaging operations |
| wecomcli-schedule | 16.3K | Calendar and schedule management |
| wecomcli-smartsheet | 12.2K | Smartsheet data operations |
| wecomcli-sheet / smartpage | 3.8K each | Spreadsheet and smart page access |
| wecomcli-manage-* | 2.5K each | Doc, smartsheet data, smartsheet schema, and schedule write paths |
| wecomcli-get-* | 2.5K each | Meeting, todo list, and message read paths |
| wecomcli-create-meeting / edit-todo | 2.4K each | Meeting creation and todo editing |
| message / shared / media / calendar / doc-manage / disk / email | 500 each | Suite tail: messaging core, shared pre-checks, media, calendar, doc administration, drive, and email |

The suite is resource-skill structured: each skill owns one business domain and the SKILL.md routing tables disambiguate near-overlap cases (doc content vs doc management, message read vs message send) before commands run.

## Quick Start

1. Install the CLI: `npm install -g @wecom/cli` and verify `wecom-cli --version` is 1.1.0+
2. Install skills: `npx skills add wecomteam/wecom-cli`
3. Read `wecomcli-shared` first — the common pre-checks are mandatory for every other skill
4. Ask in natural language, e.g. "read the latest meeting notes" or "append a row to the smartsheet"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **APAC enterprise operations** | Native WeChat Work automation for China-market operators without a translation layer |
| **Meeting intelligence** | Meeting retrieval and scheduling skills feed agent-built operational dashboards |
| **Document workflows** | Doc append and smartsheet write paths enable agent-maintained operational logs |
| **Calendar coordination** | Schedule skills bridge WeCom calendars into cross-timezone coordination |

## Limitations / Verification

- Security audits on the wecomcli-doc flagship: Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn (named in the tier)
- Publisher-page total verified (153.4K across 28 skills); 2.7K GitHub stars as of the sweep
- SKILL.md content is maintained in Chinese by the WeCom team — agents need Chinese-language instruction handling
- Requires the `@wecom/cli` npm package at 1.1.0+; the suite refuses to run on older versions
- Tail skills (message, shared, media, calendar, doc-manage, disk, email) are 500-504 installs each — early content

```bash
npx skills add wecomteam/wecom-cli   # verify install works
```

## Related

- [WeCom Unified — Routing Suite Setup](/hermes/skills/catalog/wecom-unified-skills-setup/)
- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
