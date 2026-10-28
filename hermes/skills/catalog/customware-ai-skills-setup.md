---
title: "Customware Skills - Low-Code App Builder Suite Setup"
description: "Customware's sandbox skills: 14.3K combined installs. Domain context, task workflow, CPQ, CRM and trades builders, plus Playwright QA."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/customware-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "customware", "low-code", "crm", "playwright"]
---

# Customware Skills - Setup Guide

**Source:** [customware-ai/skills](https://www.skills.sh/customware-ai/skills) via skills.sh - 14.3K combined installs across 17 indexed listings (snapshot 2026-10-27, Oct 27 sweep)

**GitHub:** [customware-ai/skills](https://github.com/customware-ai/skills) - 2 stars, MIT, branch main, last commit 2026-10-23, one flat tree of 17 skill directories at `skills/<name>/SKILL.md` with no plugin, marketplace or manifest layer

**Category:** Low-code application building (CRM, CPQ, trades) with sandbox QA

**Quality Tier:** 🟡 Beta - vendor maintained, 2 stars, 17 indexed listings against 17 in-tree skill directories

Customware is a low-code builder for small business applications, and this repository is the skill set its own builder agents run inside the Customware sandbox. The repo description is one line, "Skills to be used in the customware sandbox", and the README is two lines of boilerplate, so the actual content lives entirely in the 17 `SKILL.md` files. Those files are not tutorials. They are operating procedures with required readings, checklists, blocking rules and a defined completion state.

The suite has four layers. A domain and process layer (`domain-context`, `task-workflow`, `existing-project-migration`, `backend-integration`) governs how an agent learns a customer's business, works a task, and moves an app onto the standard React Router plus Hono stack. A vertical layer (`crm-builder`, `cpq-builder`, `trades-builder`) turns a `DOMAIN.md` into a shape for contacts, quoting or field service work. A visual layer (`frontend-design`, `design-taste`, `source-html-to-app-ui`) holds the design contract. A platform layer (`customware-ai`, `customware-email`, `customware-support-widget`) covers the vendor surfaces: the AI Gateway, Postmark email, and the support chat widget. Two Playwright skills provide the verification loop.

## Installation

The README documents no installer, CLI or plugin marketplace. The pack's install path is a shallow clone plus a directory copy, which is the whole mechanism since every skill directory is self contained:

```bash
git clone --depth 1 https://github.com/customware-ai/skills.git customware-skills
mkdir -p ~/.hermes/skills
cp -R customware-skills/skills/domain-context ~/.hermes/skills/
cp -R customware-skills/skills/task-workflow ~/.hermes/skills/
```

For a Claude Code host, the same copy lands in `~/.claude/skills/` instead. Copy only the directories a session needs. Several skills carry `references/`, `assets/` and `agents/` subfolders that the agent opens lazily, so copying the parent directory rather than the bare `SKILL.md` is what preserves the depth.

`task-workflow` states that reading it makes the workflow mandatory, in order, with no reinterpretation, so do not install it alongside a competing workflow skill and expect the agent to reconcile them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| domain-context | 2,550 | Building a living domain knowledge base under `.tasks/domain.md` through Progressive Domain Crystallization, with session start reads, inline gap markers and proposed updates a human confirms. |
| customware-support-widget | 2,457 | Installing the `<customware-chat>` support widget in a React Router SPA: script loading in `root.tsx`, route placement, required org and project ids, and bubble versus full mode. |
| task-workflow | 1,902 | Running a task end to end under a strict instruction contract: discovery, implementation, real UI verification, repair, and a defined completion state. |
| frontend-design | 1,588 | Enforcing visual guardrails on any UI change: spacing, typography, contrast, surface hierarchy, cardless and no-sidebar defaults, and the anti-pattern list, on top of a vertical skill's structure. |
| crm-builder | 1,391 | Shaping a `DOMAIN.md` into a CRM tool: section layout, entity views and mapping rules for contacts, leads, deals, pipelines and accounts. |
| cpq-builder | 1,231 | Shaping a `DOMAIN.md` into a configure price quote app: lifecycle indicators, product configurator patterns, business rule templates and mapping rules for quoting workflows. |
| trades-builder | 1,127 | Shaping a `DOMAIN.md` into a trades operations tool: section layout, config schema and mapping rules for estimates, job specs, field scheduling, subtrade payments and project stages. |
| customware-ai | 654 | Adding AI chat, generation, tools and structured JSON output through the server-only Customware AI Gateway, with the AI SDK on Hono and AI Elements in the client. |
| playwright-in-sandbox | 508 | Running browser verification in two explicit modes, interactive signoff or deterministic E2E authoring, with selector ordering, screenshot evidence and a no-fake-green rule. |
| playwright-interactive-sandbox | 400 | Driving a persistent Playwright script for fast iterative UI debugging, starting from a written QA inventory of the claims the agent intends to make. |
| source-html-to-app-ui | 232 | Rebuilding an approved source HTML application as a real target app with authored routes, components and local state, proven with paired Playwright captures. |

The remaining 6 indexed listings range from 5 to 175 installs: `customware-email` (175), `existing-project-migration` (59), `backend-integration` (30), `design-taste` (29), and `task-workflow-skill` and `task-workflow-new` at 5 each.

## Why This Matters for Hermes Agents

Vertical app work is where agents improvise most. Told to "build a CRM", an agent invents an entity model, a navigation scheme and a card layout from generic memory, and the result is plausible and wrong for the customer. `crm-builder`, `cpq-builder` and `trades-builder` replace that guess with a written mapping from `DOMAIN.md` into section layout, entity views, lifecycle indicators and config schema, and each one names its own trigger signals so a router can pick it.

The process skills carry the discipline. `task-workflow` is explicit that it is not one possible way to do the task but the required way, and the surrounding rules forbid the failure modes agents drift into: guessing filenames instead of listing, weakening a test to make a bad behavior look green, widening into unrelated cleanup, or finishing a backend before proving one user journey.

`domain-context` attacks the memory problem directly. It reads `.tasks/domain.md` at session start, marks undefined terms inline as `[UNKNOWN: ...]`, and proposes domain updates for human confirmation at session end instead of auto-applying them, which keeps a knowledge base from being silently corrupted by a confident agent.

The verification pair is the part worth stealing even if you never use Customware. `playwright-in-sandbox` requires a QA inventory before touching a browser, splits interactive signoff from durable regression coverage, and states plainly that if the browser proves the behavior is wrong you fix the product rather than the test. That is the correct posture for any agent that reports its own work as done.

## Usage

| You say | What happens |
|---|---|
| "Learn how our quoting process actually works" | domain-context reads `.tasks/domain.md`, loads only the relevant detail files, then works in the customer's own entity names and marks terms it cannot resolve. |
| "Build a CRM for our sales pipeline" | crm-builder classifies the domain as contact and pipeline management, maps it into section layout and entity views, and frontend-design enforces the shared visual rules inside that structure. |
| "Turn this spreadsheet quoting workflow into an app" | cpq-builder applies the configurator and lifecycle pattern for a small business, with business rule templates and a prototype aimed at feeling better than Excel. |
| "Add AI chat to this app" | customware-ai wires the server-only AI Gateway with AI SDK and a fixed gateway URL, puts AI Elements in the client, then runs the mandatory live model and structured output checks. |
| "Why is this page broken" | playwright-interactive-sandbox writes a QA inventory, starts the app in a persistent session, drives the changed flow and inspects screenshots rather than DOM state alone. |
| "Rebuild this approved mockup as the real app" | source-html-to-app-ui discovers the source pages and interactions, authors real routes and components, and pairs source and target captures at matching viewports and themes. |
| "Move this uploaded app onto your stack" | existing-project-migration reads the artifacts under `.import/`, preserves routes, workflows and styling, and replaces only the runtime foundation against its own grading gates. |

## Verification

Fetch a skill before installing it. The tree is flat, so the path is predictable, and these probes returned 200 on 2026-10-27:

```bash
for p in skills/domain-context/SKILL.md \
         skills/task-workflow/SKILL.md \
         skills/crm-builder/SKILL.md \
         skills/playwright-in-sandbox/SKILL.md \
         skills/source-html-to-app-ui/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/customware-ai/skills/main/$p"
done
```

Read the two that move credentials or write to a tenant before running them:

- https://raw.githubusercontent.com/customware-ai/skills/main/skills/customware-ai/SKILL.md
- https://raw.githubusercontent.com/customware-ai/skills/main/skills/customware-email/SKILL.md

After a copy, confirm the directory is present with its supporting folders intact, for example `ls ~/.hermes/skills/domain-context`, which should show `SKILL.md`, `references/`, `assets/`, `README.md` and `LICENSE`. There is no installer to report success, so the check is the filesystem. Count the skill directories against the index yourself: 17 `SKILL.md` files are in the tree today and each one carries a `name:` in its frontmatter.

## Security

skills.sh verdicts for the Gen Agent Trust Hub, Socket and Snyk auditors were not sampled this fire, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| domain-context | Not checked | Not checked | Not checked |
| customware-support-widget | Not checked | Not checked | Not checked |
| task-workflow | Not checked | Not checked | Not checked |
| frontend-design | Not checked | Not checked | Not checked |
| crm-builder | Not checked | Not checked | Not checked |
| cpq-builder | Not checked | Not checked | Not checked |
| trades-builder | Not checked | Not checked | Not checked |
| customware-ai | Not checked | Not checked | Not checked |
| playwright-in-sandbox | Not checked | Not checked | Not checked |
| playwright-interactive-sandbox | Not checked | Not checked | Not checked |
| source-html-to-app-ui | Not checked | Not checked | Not checked |

The risk in this suite is credential and data flow into a vendor tenant, not local code execution. `customware-ai` reads `CUSTOMWARE_AI_GATEWAY_KEY` and posts to a tenant scoped endpoint, `https://app.customware.ai/api/orgs/${orgId}/projects/${projectId}/ai/v1`, so prompts, tool arguments and app data sent to the model leave the local process for Customware's gateway. It mitigates the obvious mistakes: the key stays server-only, is never surfaced in the UI, and the skill forbids a second browser to gateway path.

Three more observations from the files. `customware-support-widget` loads `https://app.customware.ai/support-widget/customware-chat.js` into the host document at `root.tsx`, which is third party script execution in the customer's app and should be a deliberate decision. `customware-email` requires `POSTMARK_INBOUND_WEBHOOK_SECRET` and `POSTMARK_SERVER_TOKEN`, sends real outbound mail through the Postmark server, and persists received mail in the app database, so a test run can reach a real inbox. And the migration skill reads uploaded customer code and database dumps from `.import/`, which is untrusted third party content the agent is instructed to treat as the authority on behavior.

The Playwright skills are safe by default but easy to misdirect: they run against `127.0.0.1:4444` in a persistent session, and every click and form submission is a real write. Pointed at a live tenant rather than a local sandbox, that is production traffic.

## Limitations

- Snapshot data, verified 2026-10-27: 14,343 combined installs across 17 indexed listings; 2 GitHub stars; MIT; branch main. Counts drift over time.
- The skills assume the Customware sandbox. Three of them declare a running Customware SPA instance as a compatibility requirement, several reference `.tasks/` inputs and a `template-be-setup` reference repository, and the vertical skills exist to feed the Customware builder. Portability to another stack is unproven, and the procedure-shaped skills (workflow, Playwright, design guards) are the realistic candidates for reuse elsewhere.
- Directory and listing drift: the tree carries `task-workflow-v2` and `source-html-to-app-ui-v2`, both of which declare the same `name:` in frontmatter as their base skill, and two low install listings, `task-workflow-skill` and `task-workflow-new` at 5 each, have no matching directory. Neither v2 directory appears in the install index under its own name, so the index and the tree are not in a one to one mapping despite both counting 17.
- The README is two lines, so there is no install command, compatibility table or skill index in the repository. Every fact above about behavior comes from the individual `SKILL.md` files, and the pack's install command is the copy path rather than a vendor documented installer.
- No manifests, plugin marketplace or slash commands exist at the root, so hosts that expect a plugin bundle, such as Claude Code or Codex marketplaces, get plain skill directories only.
- The v2 rewrites are shorter than their originals (66 lines against 606 for `task-workflow`), and nothing in the repository states which one the builder loads. Check dates and content before assuming the newer file is the one in use.

## Related

- [Hono Skill - Edge Web Framework Setup by the Hono Author](/hermes/skills/catalog/hono-skill-setup)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [TestDino Playwright Skills - 79-Guide Testing Suite Setup](/hermes/skills/catalog/testdino-playwright-skill-setup)
- [CloudBase Skills - Tencent Full-Stack Apps Setup](/hermes/skills/catalog/cloudbase-skills-setup)

## Pro Tips

- Install `domain-context` and `task-workflow` first and run them on a real project before adding a vertical builder. The builders assume a `DOMAIN.md` exists and is trusted, and the quality of their output tracks the quality of that file.
- Pick exactly one vertical skill per app. `crm-builder`, `cpq-builder` and `trades-builder` each define their own section layout and mapping rules, and loading two gives the agent two competing structures for the same page.
- Keep the Playwright pair on a local sandbox and on port 4444. They are written for a local target and their clicks are real writes, so the blast radius of a wrong `TARGET_URL` is whatever environment that URL resolves to.
- Treat `frontend-design` as a guardrail applied after the domain skill, not as a design system of its own. Its own text says the domain skill owns structure and it owns visual quality, and it is meant to run on every UI build.
- Read `customware-ai` before any AI feature and obey its env rule: gateway calls go through the Hono server with the key read only from `CUSTOMWARE_AI_GATEWAY_KEY`, and the fixed gateway URL stays hardcoded.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
