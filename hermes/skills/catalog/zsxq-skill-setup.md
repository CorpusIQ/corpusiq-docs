---
title: "ZSXQ Skill - Community Operations for Agents"
description: "unnoo/zsxq-skill on skills.sh: 25.2K combined installs; the official Knowledge Planet skill for posting, comment sweeps, digests and paid renewals."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zsxq-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "zsxq", "community operations", "wechat pay"]
---

# ZSXQ Skill - Setup Guide

**Source:** [unnoo/zsxq-skill](https://www.skills.sh/unnoo/zsxq-skill) via skills.sh - 25.2K combined installs across 6 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 323 stars, MIT licence, last pushed 2026-11-06, one SKILL.md at skills/zsxq/ with 35 operation references and 15 scenario scripts beside it
**Category:** Chinese community operations for agents: comment sweeps, digests, scheduled posts, paid renewals and content search
**Quality Tier:** 🟡 Review - an official vendor skill with clean Agent Trust Hub verdicts and a real MIT licence, held back by Socket and Snyk warnings on some of the sampled skills.

Knowledge Planet (zsxq) is a paid-community platform: operators run groups, publish topics, answer questions, curate digests and sell memberships. The skill in this repository is the official one, written and maintained by the platform team, and it is built around a single `zsxq` entry point that routes every operation over one of two channels, the local `zsxq-cli` binary or an MCP tool called `call_zsxq_api`.

The reason the repository exists is stated plainly in its README: the usual third-party automation for the platform reverse engineers the private interface and asks you to paste a cookie or password into a config file, which risks account control actions, breaks when the interface changes, and leaves nobody accountable. This skill uses official OAuth 2.0 device authorization with a QR or link confirmation, keeps the token in the system keychain, and covers the same operations through documented endpoints.

Behind the single skill entry point sit 35 operation references, one per unit of work (topic search, topic scheduling, digest flags, tags, member lists, columns, notes, share links, payments and more), plus 15 scripted operating scenarios. That split matters in practice: the skill reads one narrow reference per task instead of loading a monolithic prompt, and the scenario files are what turn "check my group today" into a fixed sequence of queries.

## Installation

Prerequisites are Node 18 or newer, since the CLI ships as an npm package:

```bash
npm install -g zsxq-cli
```

The skill itself installs through the skills CLI, with the repository URL form the README uses:

```bash
npx skills add https://github.com/unnoo/zsxq-skill --yes
```

The repository's INSTALL.md, which is written for an agent to execute, adds a user-wide install and a mirror for networks where GitHub is unreachable:

```bash
npx skills add https://github.com/unnoo/zsxq-skill --yes --global
npx skills add https://gitee.com/unnoo/zsxq-skill --yes --global
```

Login is a device-authorization flow. The command prints a link and a verification code, and the account holder confirms in a browser or on a phone:

```bash
zsxq-cli auth login
```

Check the result before running anything that writes:

```bash
zsxq-cli auth status
```

There is a second, CLI-free route. Create a key on the platform's key management page, copy the MCP link that carries the api-key, add it to the host's MCP configuration or use the page's one-click buttons, and install the skill the same way. The skill prefers the CLI channel whenever `zsxq-cli` is on the path, and falls back to `call_zsxq_api` when it is not.

If neither channel is available the skill is supposed to stop and tell you to install the CLI or attach the MCP server, rather than guess at an endpoint.

## What It Provides

Six indexed listings, all above the threshold, and the split is historical: five of them are the older per-domain skills that the project has since consolidated into one.

| Skill | Installs | Use For |
|---|---|---|
| zsxq-shared | 4,576 | The legacy shared layer: authentication, channel detection and common error handling, now folded into the single zsxq skill |
| zsxq-topic | 4,563 | Topic work: search, publish, edit, delete, comment, nested replies, answers, scheduled posts and scheduled answers |
| zsxq-group | 4,561 | Group work: list and search groups, browse topic streams, hashtags, member lists, expiry dates and columns |
| zsxq-note | 4,556 | Personal notes: create, edit, read and delete public notes |
| zsxq-user | 4,546 | Account and footprint work: own profile, cross-group posting history, NPS feedback |
| zsxq | 2,373 | The consolidated skill: every operation above plus digest flags, pinning, tags, group settings, Skill Pay purchases and the 15 operating scenarios |

All 6 indexed listings clear the 500-install threshold and appear in the table above.

The five legacy names still carry most of the install count because they were installed separately before the merge. INSTALL.md documents a migration path for machines that have them: ask the agent to check and migrate the old skills, and it scans the install locations, reports, and only moves files after confirmation, with a backup it can roll back. Checking without cleaning is a supported mode too.

## Why This Matters for Hermes Agents

The write operations are real. The README's security section is blunt about it: the tool runs as your account, and posting, commenting, answering and deleting take effect on the live platform. The skill's own guardrails are intent confirmation before writes and deletes, a token kept in the keychain rather than in terminal output or logs, scope limited to permissions the account already has, and a payment rule that requires the price to be queried and the amount confirmed before an order is created.

That last rule is the interesting one for an agent. `PAYMENT_REQUIRED` means exactly what it says, a pending payment, not a failure and not a success, and the skill is instructed not to retry order creation automatically. A payment state machine that a model cannot misinterpret is worth more than a shorter prompt.

Channel selection is deterministic, which is what makes it usable inside a Hermes session. If the host can run `zsxq-cli`, the CLI is used, because its shortcuts validate arguments and do local orchestration. If not, and the host exposes `call_zsxq_api`, that is used with a documented method and path. If neither exists, the skill stops. The one thing it is forbidden to do is invent an endpoint, and the reference file `endpoint-catalog.md` is the list of what counts as supported.

The scenario layer is where the operational value sits. Daily patrol, comment triage, digest and tag curation, batch tagging, weekly operations reports, poster generation, video generation, risky-content monitoring, expiring-member renewals, answering inbound questions from the help centre, and the Skill Pay purchase flow are each written down as a multi-step procedure. An agent asked to "run my group for the morning" follows a recipe instead of improvising a sweep.

For developers, the CLI also emits `--json` output with semantic exit codes, so the same skill can sit behind a scheduled job without parsing prose.

## Usage

| You say | What happens |
|---|---|
| "What groups am I in, and which have expiring members?" | The agent lists your groups, then the member list with expiry dates, and sorts the ones closest to lapsing |
| "Search this group for posts about agent evaluation" | Full-text search inside the group, with a relevance summary and the closest topics when there is no exact match |
| "Reply to that comment and keep the thread civil" | Topic detail is fetched, the reply is drafted, and the reply is posted under the right comment id after you confirm |
| "Post this tomorrow at 9am" | A scheduled topic is created, then the pending task list and the remaining quota are read back to confirm it exists |
| "Mark this post as a digest and tag it methodology" | Digest flag and hashtag are applied to the topic, along with a column placement if you name one |
| "Draft the weekly operations report for this group" | The operations report scenario pulls the week's topics, comments and questions, then writes the report and a poster |
| "Who is about to lapse, and what should I send them?" | The renewal scenario lists expiring members and drafts renewal messages against each tenure band |

## Verification

Read the skill before installing it. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/unnoo/zsxq-skill/main/skills/zsxq/SKILL.md | head -20
```

The frontmatter should name `zsxq` and describe the CLI and the underlying interface, and the body should open with the channel decision: CLI first, MCP as a fallback, stop if neither is present.

After install, confirm the reference tree landed, because the skill is only as complete as those files. Installed through Claude Code, the directory is `~/.claude/skills/zsxq`; other runtimes place it under their own skills path:

```bash
ls ~/.claude/skills/zsxq/references | wc -l
ls ~/.claude/skills/zsxq/references/scenarios | wc -l
```

Those should report 35 and 15. Then confirm the account side, which no amount of file copying proves:

```bash
zsxq-cli auth status
```

A logged-in account means the skill can act. If the CLI reports no session, run `zsxq-cli auth login` again and complete the confirmation in the browser before asking the agent to do anything that writes.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| zsxq-shared | Pass | Pass | Warn |
| zsxq-topic | Pass | Pass | Warn |
| zsxq-note | Pass | Warn | Pass |
| zsxq-user | Pass | Pass | Pass |
| zsxq | Pass | Warn | Warn |

The install surface is markdown plus a Python build script that generates the distributable skill package; the runtime spend is the npm CLI, which is where the actual network calls happen. Four of the five sampled skills carry at least one warning from Socket or Snyk, and the consolidated `zsxq` skill carries both. The likely explanation is the combination of network calls, payment-related operations and shell invocation in the CLI wrapper, but that is an inference, not something the skill declares, so read the Snyk report rather than trusting a summary.

The credential design is the strongest part. Authorization is OAuth 2.0 device flow, so no password ever reaches the tool, and the token is stored in the operating system keychain instead of a plaintext config file. That removes the two failure modes that make third-party scrapers dangerous: a password in a dotfile and a cookie in a shell history.

The risk that remains is authority. Everything the account can do, the skill can do, including deleting topics and creating payment orders. If you are pointing this at a group with paying members, give the agent a review step before writes, and keep the Skill Pay route behind explicit human confirmation of the amount.

The licence is MIT, held by the platform, so reuse and redistribution terms are clear, which is more than most repositories in this catalog can claim.

## Limitations

- Snapshot data, verified 2026-11-06: 25,175 combined installs across 6 indexed listings; 323 GitHub stars; MIT licence; last pushed 2026-11-06. Counts drift over time.
- The documentation is Chinese-first. SKILL.md, the 35 references and all 15 scenarios are written in Chinese, so an English-only agent will translate on the fly and lose precision on operational vocabulary.
- It is a single-vendor surface. The skill talks to one platform's interface, and its usefulness begins and ends with accounts on that platform.
- Channel parity is imperfect. The README states some operations exist on one channel only, for example Skill Pay order creation on MCP and background or highlight image upload on the CLI.
- Payment states need human eyes. The skill will not retry order creation by itself, which is correct, and also means a stalled purchase needs an operator to look at it.
- The examples are synthetic by design. SKILL.md warns that every id, order number and payment code in its examples is fictitious, so an agent that copies an example id will fail rather than act on the wrong resource.

## Related

- [Xiaohongshu Skills - RED Content Operations](/hermes/skills/catalog/xiaohongshu-skills-setup)
- [Claw Multi-Agent Skill - Setup Guide](/hermes/skills/catalog/claw-multi-agent-setup)
- [Tavily Research - AI-Powered Deep Research with Citations](/hermes/skills/catalog/tavily-research-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Make the channel explicit in the prompt. "Use the CLI" or "use the MCP tool" removes a detection step, and the CLI route is the one with argument validation.
- Ask for the read-back after a write. Scheduled posts, tags and digests all return state you can query, and a read-back is the only proof the operation landed.
- Start with the migration check if this machine ever had the old five-skill set. Two of the same operations installed twice will produce conflicting instructions in the agent's skill list.
- Keep a separate group for experiments. The skill acts with your permissions, and a test post in a paid group is still a test post your members can see.
- Treat the scenario files as the prompt library. Naming the scenario ("run the daily patrol") is more reliable than describing the sweep from scratch each morning.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
