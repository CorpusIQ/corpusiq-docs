---
title: "Novu Skills - Multi-Channel Notification Setup"
description: "novuhq/skills: 3.3K combined installs across 9 listings for email, SMS, push and in-app notification workflows with agents"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/novu-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "novu", "notifications", "email", "in-app inbox"]
---

# Novu Skills - Setup Guide

**Source:** [novuhq/skills](https://www.skills.sh/novuhq/skills) via skills.sh - 3.3K combined installs across 9 indexed listings (3,299 exact); first seen 2026-11-10 (Nov 10, 2026 sweep)
**GitHub:** 4 stars, MIT license, `main` branch, last pushed 2026-09-04, 8 `SKILL.md` files under `skills/<name>/`, one directory per listing plus a single namespaced alias
**Category:** Notifications: workflow design, multi-channel delivery, in-app inbox, subscriber and preference management
**Quality Tier:** 🟠 Community with one failure - seven of nine listings are near-identical in installs and mostly pass, but Snyk fails one skill and warns on two, and the repository is new with a single maintainer footprint.

Novu is an open-source notification infrastructure product, and this repository is its official agent skill set rather than a community wrapper. The README frames the product as a single `<Inbox />` component over a multi-channel delivery layer, and the skills are written against that framing: design the workflow, author the content, trigger it, and manage who receives it.

The nine indexed listings correspond to eight skill directories plus one legacy alias. Seven of them sit between 460 and 469 installs, which is the flattest distribution in this sweep and a useful signal in itself: nobody installs one Novu skill, they install the set. The eighth, `novu-connect-agent`, sits at 4 installs and is the newest and most agent-specific of the group. The alias `novu` at 41 installs is the pre-namespacing name that the README says is superseded.

The set covers both halves of the product. The SDK half is `novu-framework-integration` for code-first workflows in TypeScript with the Bridge Endpoint, and `novu-inbox-integration` for the React, Next.js or vanilla inbox component. The dashboard half is `novu-design-workflow` and `novu-dashboard-workflows`, which encode how Novu expects a workflow to be structured: channels, severity, digest defaults, step conditions and content per step.

## Installation

The README's route is the skills CLI against the repository:

```bash
npx skills add novuhq/skills
```

The README describes exactly what this does: it pulls the skills from the GitHub repository and makes them available to the agent. There is no plugin marketplace route and no MCP server in this repository, so the CLI is the only install path.

Two prerequisites are stated up front: a Novu account, and a secret key from the dashboard's API keys page. Both are needed before any triggering skill can do anything.

The README also carries a breaking-change note that matters if you installed this earlier. Skills were renamed to a `novu-*` namespace and moved under `skills/`, so a machine holding the old single `novu` skill should re-run the install to pick up the eight discrete skills. The alias listing at 41 installs is the residue of that rename.

## What It Provides

Seven listings clear the 300-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| novu-trigger-notification | 469 | Sends single, bulk, broadcast and topic-based notifications across email, SMS, push, chat and in-app channels. |
| novu-manage-preferences | 467 | Sets workflow-level and subscriber-level preferences, including default channels per subscriber. |
| novu-inbox-integration | 466 | Integrates the in-app notification inbox into React, Next.js or vanilla JavaScript applications. |
| novu-framework-integration | 466 | Defines code-first workflows with `@novu/framework`: Bridge Endpoint, steps, controls, React Email and GitOps deployment. |
| novu-manage-subscribers | 463 | Creates, updates, searches and deletes subscribers, and manages topics for group targeting. |
| novu-design-workflow | 463 | Designs a workflow the Novu way: channel selection, severity, criticality, digest defaults and step conditions, with nine reference templates. |
| novu-dashboard-workflows | 460 | Authors step content (subject, body, editor type, headers, conditions) for workflows defined in the dashboard or through the Novu MCP. |

The remaining 2 indexed listings are the legacy `novu` alias (41 installs) and `novu-connect-agent` (4 installs), which walks an agent through creating a Novu managed agent and connecting a channel such as Slack, email, Telegram or WhatsApp.

The seven-row table is close to a complete skill set: design, author, trigger, target, and two integration paths. What it does not contain is a testing or a deliverability skill, which is where notification work usually goes wrong.

## Why This Matters for Hermes Agents

Notification code has a specific failure shape. It runs, it returns success, and the message never arrives, or arrives twice, or arrives on a channel the user turned off. None of those produce an exception, so an agent that writes notification code without a model of the delivery path will report success on all three.

These skills supply the model. `novu-design-workflow` is the one that matters most, because it forces the decisions that are usually implicit: which channels, what severity, whether the workflow is critical enough to bypass preferences, and what the digest window should be. Those four choices determine delivery behaviour more than any code.

The framework integration skill is the one that fits an agent workflow. Workflows defined in TypeScript with Zod controls and a Bridge Endpoint are files in the repository, which means an agent can add a notification workflow in the same session where it adds the feature that triggers it, and the workflow is reviewable in the diff.

For a Hermes operator the angle is operational rather than purely technical. An agent that can trigger a notification is an agent that can report to a human on schedule, and the subscriber and topic skills are what make that multi-recipient without a mailing list.

## Usage

| You say | What happens |
|---|---|
| "Notify the on-call engineer when this job fails" | A workflow is designed with a critical severity and an in-app plus email channel, then triggered from the failure path |
| "Add an in-app notification bell to the app" | The inbox integration adds the React or Next.js component and its provider, wired to the subscriber identity |
| "Send this to everyone on the beta list" | Subscribers are created and tagged into a topic, then a topic-based trigger broadcasts to the group |
| "Let users choose email or SMS" | Preference management sets default channels per workflow and per subscriber, and the trigger respects them |
| "Build the notification workflow in code, not the dashboard" | Framework integration defines steps, controls and content in TypeScript with a Bridge Endpoint and GitOps deployment |
| "Write the email body for the digest step" | Dashboard workflows authors subject, body, editor type and conditions for that step |

## Verification

Each listing resolves to a raw `SKILL.md` one directory below `skills/`, and the directory name is the listing name without the `novu-` prefix. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/novuhq/skills/main/skills/trigger-notification/SKILL.md | head -5
```

It should open with frontmatter holding `name: novu-trigger-notification` and a description beginning `Trigger Novu notification workflows`, then the delimiter and the instruction body. Note the mismatch that will catch a hand-written URL: the directory is `trigger-notification` while the skill name is `novu-trigger-notification`.

After an install, confirm the skill landed as a directory holding `SKILL.md`:

```bash
ls -d ~/.claude/skills/*/ | head -20
test -f ~/.claude/skills/novu-trigger-notification/SKILL.md && echo ok
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| novu-trigger-notification | Pass | Pass | Pass |
| novu-manage-preferences | Pass | Pass | Pass |
| novu-inbox-integration | Pass | Warn | Warn |
| novu-framework-integration | Pass | Pass | Pass |
| novu-manage-subscribers | Pass | Pass | Pass |
| novu-design-workflow | Pass | Pass | Pass |
| novu-dashboard-workflows | Pass | Pass | Pass |
| novu | Pass | Pass | Warn |
| novu-connect-agent | Pass | Pass | Fail |

Agent Trust Hub passes all nine listings. Socket warns on one, Snyk warns on two, and Snyk fails `novu-connect-agent`, the skill that provisions an agent and connects it to a channel. That single failure is why the tier is marked with a caution rather than a plain pass.

The failing skill deserves reading rather than avoiding. It creates an agent identity in a third-party system and connects a channel to it, which is a credential-provisioning action, and a scanner that fails it is pointing at exactly the property to check by hand: what it creates, under whose authority, and how it is revoked.

The other property the scanners cannot score is that these skills trigger real messages to real people. An agent looping over a subscriber list with a broken filter sends that loop. Keep the API key on a development project until a workflow has been exercised once, and use a test subscriber before the real one.

## Limitations

- Snapshot data, verified 2026-11-10: 3,299 combined installs across 9 indexed listings; 4 GitHub stars; MIT license; last pushed 2026-09-04. Counts drift over time.
- The repository has a very small public footprint relative to the product it fronts. Four stars against roughly 460 installs per skill means adoption is happening inside projects, not through repository attention, so do not read the star count as a quality signal in either direction.
- One skill fails a security scanner (`novu-connect-agent`), and it is the one that provisions an agent identity and connects a channel.
- There is no testing, simulation or deliverability skill in the set. Everything about whether a message actually lands is outside what these skills describe.
- `novu-dashboard-workflows` assumes a workflow already exists, either authored in the dashboard or through the Novu MCP. It writes step content, not workflow structure.
- The README states nine skills but the tree holds eight `SKILL.md` files, the difference being the legacy `novu` alias that the namespacing change superseded.

## Related

- [Webhook Subscriptions - External Service Trigger Setup](/hermes/skills/catalog/webhook-subscriptions-setup)
- [AgentMail Skills - Agent Email Inbox Setup](/hermes/skills/catalog/agentmail-skills-setup)
- [React Email Skill - Template Authoring for Agents](/hermes/skills/catalog/react-email-skill-setup)

## Pro Tips

- Start with `novu-design-workflow` even if you plan to build in code. It carries the nine reference templates and the severity and digest rules, which are the decisions you cannot change cheaply later.
- Decide critical versus non-critical before writing any trigger. Critical workflows bypass subscriber preferences, and discovering that after launch means re-notifying everyone who muted you.
- Keep the subscriber identity mapping in one place. The inbox integration and the trigger path both need it, and two mappings is how a user gets notifications for someone else's account.
- Prefer the framework route for anything that ships. Workflows as TypeScript files are reviewable in a pull request; workflows clicked together in the dashboard are not.
- Read `novu-connect-agent` before running it, not after. It is the one skill here that creates an identity in another system, and it is the one Snyk fails.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
