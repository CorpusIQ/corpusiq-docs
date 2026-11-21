---
title: "Caido Skills - Interception Proxy Security Setup"
description: "caido/skills: a caido-mode skill giving coding agents Caido SDK access for HTTP history search, replay and match-and-replace - 2.9K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/caido-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "security testing", "proxy", "http"]
---

# Caido Skills - Interception Proxy Security Setup

**Source:** [caido/skills](https://www.skills.sh/caido/skills) via skills.sh - 2.9K combined installs across 1 indexed listing; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [caido/skills](https://github.com/caido/skills) - 296 stars, MIT license, main branch, last pushed Nov 8, 2026; a single `skills/caido-mode/` directory holding `SKILL.md` plus a TypeScript client library under `lib/`.
**Category:** Security Testing and Interception Proxy
**Quality Tier:** 🟢 Green - the single sampled skill passes Gen Agent Trust Hub, Socket and Snyk.

Caido publishes a single skill, caido-mode, that gives coding agents the full Caido SDK through the official `@caido/sdk-client`. Caido is an interception proxy for web application security testing, and the skill lets an agent search HTTP history with HTTPQL, replay and edit requests, manage match-and-replace rules, and organize handoffs into named replay sessions and collections.

The family is one skill in the install index. Frame the skill for authorized testing only: it drives a proxy you control against targets you are permitted to test. Personal access token (PAT) auth is recommended. First seen in the Nov 21, 2026 morning sweep.

## Installation

```bash
pnpm dlx skills add caido/skills --skill='*'
```

Or install all skills globally:

```bash
pnpm dlx skills add caido/skills --skill='*' -g
```

The skill talks to a running Caido instance, so install Caido first and walk through the setup guide in the Caido documentation. Authenticate with a personal access token for headless use.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| caido-mode | 2,874 | full Caido SDK access: search HTTP history with HTTPQL, replay and edit requests, and manage match-and-replace rules |

No indexed listings fall below the threshold; the single indexed listing appears above.

## Why This Matters for Hermes Agents

This skill turns a manual interception proxy into something an agent can query and drive, so HTTP history search and request replay become natural-language operations instead of mouse work. Match-and-replace rules give repeatable, consistent test variants, and named replay sessions organize a set of requests so a test run can be replayed and reviewed. The client caches authentication in reusable static curl config files, so repeated tests do not re-handshake each time.

Because the skill wraps the official SDK client rather than shelling out to ad-hoc scripts, an agent stays within the SDK surface and inherits its request handling. The useful scope is narrow and safe to bound: an agent inspects and replays traffic through a proxy you already run, against targets you already own or are authorized to test.

## Usage

| You say | What happens |
|---|---|
| Search my HTTP history for requests to /api/v1 | caido-mode runs an HTTPQL query over the Caido HTTP history |
| Replay that POST request with a changed host header | the skill replays the request through Caido, optionally into a named session |
| Add a match-and-replace rule to swap the Authorization header | caido-mode writes the rule into Caido |
| Export that request as a curl command | the skill renders the request as curl, with auth cached in a static config file |
| Show the findings from my last scan | caido-mode lists findings from Caido |
| Test this endpoint through the Caido proxy | the skill runs a curl request proxied through Caido |

## Verification

Confirm the skill landed, then review its SKILL.md before driving the proxy:

```bash
ls ~/.claude/skills 2>/dev/null; ls skills 2>/dev/null
```

```bash
curl -sL https://raw.githubusercontent.com/caido/skills/main/skills/caido-mode/SKILL.md | head -40
```

The skill needs a running Caido instance and, for most operations, a personal access token; test only against targets you own or are authorized to assess.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| caido-mode | Pass | Pass | Pass |

Caido is an interception proxy used for security testing. Use it only against systems you own or are authorized to test, and treat HTTP history and replay output as sensitive data.

## Limitations

- Snapshot data, verified Nov 21, 2026: 2,874 combined installs across 1 indexed listing; 296 GitHub stars; MIT license; last pushed Nov 8, 2026. Counts drift over time.
- The family is one skill: the install index has a single caido-mode listing, which is the whole repository's skill surface.
- The skill requires a running Caido instance and PAT auth for most operations; it does not bundle Caido itself.
- It is a security-testing tool, so scope use to authorized targets and treat intercepted traffic as sensitive data.
- Behaviour depends on the Caido SDK client version, which updates independently of the skill files.

## Related

- [CTF Security Skills - Offensive Security Suite Setup](/hermes/skills/catalog/ctf-security-skills-setup)
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup)
- [Ghost Security Skills - AppSec Agent Plugin Setup](/hermes/skills/catalog/ghostsecurity-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Authenticate with a PAT rather than an interactive login so repeated requests run headless.
- Use match-and-replace rules for consistent test variants instead of editing each request by hand.
- Save related requests into named replay sessions so a test run is replayable and reviewable.
- Review the SKILL.md and the SDK client before driving the proxy against a shared environment.
- State the authorized target explicitly in your prompt before the agent runs any replay.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
