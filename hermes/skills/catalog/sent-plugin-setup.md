---
title: "Sent Plugin - Messaging and Verification Skills Setup"
description: "sentdm/sent-plugin: 54.2K combined installs. Official Sent agent skills for SMS, WhatsApp and RCS sends, Sender Profiles, compliance and migration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sent-plugin-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "sms", "whatsapp", "rcs", "mcp"]
---

# Sent Plugin - Setup Guide

**Source:** [sentdm/sent-plugin](https://www.skills.sh/sentdm/sent-plugin) via skills.sh - 54.2K combined installs across 21 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [sentdm/sent-plugin](https://github.com/sentdm/sent-plugin) - 49 stars, MIT License, branch main, last pushed 2026-10-20; 84 `SKILL.md` files across four parallel layouts of the same 21 skills, `skills/<name>/SKILL.md`, `packages/sent/skills/<name>/SKILL.md`, `plugins/sent/skills/<name>/SKILL.md` and `claude-plugins/sent/skills/<name>/SKILL.md`, beside `evals/`, `scripts/`, `schemas/`, `adapter-sources/`, `plugin.json` and `mcp.json`

**Category:** Business messaging (SMS, WhatsApp, RCS), CPaaS integration, carrier compliance and delivery diagnosis

**Quality Tier:** 🟡 Beta - two Snyk Warns (messaging-performance-analyzer, template-builder-ui) in the sampled six; MIT, messaging and verification APIs

Sent is a business messaging platform, and this repository is its official agent plugin: a skills collection plus a remote Model Context Protocol endpoint at `https://mcp.sent.dm/mcp`, declared as Streamable HTTP in `mcp.json`. The plugin ships 21 skills, one dispatcher named `sent` and 20 specialists, and the split is deliberate. Eight skills drive live operations through MCP tools (`messages.send`, `messages.get`, `contacts.*`, `templates.*`, `sender_profiles.*`, `compliance.*`, `dashboard.*`, `balance.get`), and the rest are engineering and compliance guidance that works from a payload, an export or a plan rather than a live call.

What makes the collection interesting for an agent builder is that it treats messaging as a mutation-heavy workflow rather than a query surface. The skills carry a shared contract in the README: preview the exact organization, Sender Profile, target and payload before every send or delete, get explicit confirmation immediately before the call, never auto-retry an ambiguous send, and treat `accepted` or `queued` as processing states rather than proof of delivery. Sends are template-only, so a skill must resolve a real template ID through `templates.list` before it can send at all, which removes most of the free-text failure modes that make agent messaging dangerous.

The repository is also packaged four ways. `packages/sent` is the canonical portable Agent Plugins 1.0.0 artifact, and `plugins/sent` (Codex) and `claude-plugins/sent` (Claude Code) are generated host adapters, with `scripts/generate_adapters.py` and `scripts/validate.py` keeping them in step. The Claude Code adapter is not a byte copy: it overlays host policy on some skills, which is worth knowing before you point a client at it.

## Installation

The README's first route is the skills CLI, and `--list` is the only call that touches nothing:

```bash
npx skills add https://github.com/sentdm/sent-plugin --list
```

Install the dispatcher when you want the agent to route broad Sent requests on its own:

```bash
npx skills add https://github.com/sentdm/sent-plugin --skill sent
```

Install focused skills when the task is already known, or the whole set at once:

```bash
npx skills add https://github.com/sentdm/sent-plugin \
  --skill sent-messaging \
  --skill messaging-performance-analyzer
```

```bash
npx skills add https://github.com/sentdm/sent-plugin --skill '*'
```

The README is explicit that the CLI installs agent instructions only: live account reads and mutations additionally require the Sent MCP server through a compatible, authorized client. The Claude Code route is the plugin marketplace, and a local checkout can be loaded directly for development:

```text
/plugin marketplace add sentdm/sent-plugin
/plugin install sent@sent
```

```bash
claude --plugin-dir ./claude-plugins/sent
```

Hermes is not one of the two adapters this repository generates, so the durable route for this profile is a directory copy rather than an adapter install. Copy `packages/sent/skills/<name>/` from a clone into `~/.hermes/profiles/corpusiq/skills/<name>/`, because that is the tree the README calls the canonical source. Copy the whole directory and not the markdown alone: `messaging-performance-analyzer`, `migrate-to-sent`, `sent-integration-starter`, `sent-webhook-engineer`, `sms-10dlc-registration` and `waba-template-author` each ship `references/` and `scripts/` next to `SKILL.md`, and several others ship `references/` or `agents/openai.yaml`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sent | 2,921 | Router for broad or ambiguous Sent work: picks a live MCP operation or a specialist skill, asks only the channel, workflow, geography and surface questions needed to choose a lane, and states a proposed order when a request spans several skills. |
| waba-template-author | 2,919 | Writing, classifying, linting and repairing WhatsApp utility, marketing and authentication templates against the Sent v3 template contract, including Meta rejection, variables, buttons and OTP payloads; ships `scripts/lint_waba_template.py`. |
| waba-embedded-signup | 2,905 | WhatsApp Business Account onboarding through Sent: dashboard Embedded Signup versus organization WABA inheritance versus direct child-profile credentials, access-token handling, phone-number mapping and completion callbacks. |
| messaging-performance-analyzer | 2,904 | Message-level diagnosis of MDR and activity funnels, delivery failures, error-code clusters, read-rate gaps and channel fallback; ships `scripts/analyze_mdr_funnel.py` with fixtures. |
| template-builder-ui | 2,903 | Designing and auditing tenant-facing template builders: editor forms, variables, channel overrides, WhatsApp review states, RCS suggestion chips and authentication templates. |
| sms-10dlc-registration | 2,903 | US A2P 10DLC brand and campaign packets: inheritance, campaign use cases, opt-in evidence, sample-message policy, TCR status and rejection remediation; ships two payload validators with fixtures. |
| rcs-agent-onboarding | 2,903 | RCS Business Messaging launch: carrier approval evidence, capability decisions, text and suggestion-chip templates, Sender Profile readiness, SMS fallback and broadcast prevention. |
| sender-profile-architect | 2,901 | Tenancy and brand boundaries for Sender Profiles: API-key scoping, `x-profile-id` isolation, inheritance, sharing, billing, WABA and 10DLC ownership, webhook routing and tenant offboarding. |
| sent-templates | 2,900 | Finding existing template records by name or ID and reading language, channel, category and status, or deleting one; content authoring is handed to waba-template-author and UI work to template-builder-ui. |
| sent-messaging | 2,900 | Template-only sends over MCP with payload preview and confirmation, `scheduledAt` windows from 1 minute to 30 days, `idempotencyKey` replay, and per-message delivery evidence from the activity list. |
| sent-contacts | 2,900 | Contact records through MCP: list, get, bulk create, deduplicate, message summary and delete, with confirmation gates before creates and deletes. |
| sent-analytics | 2,900 | Aggregate dashboard volume and deliverability, contact growth, period comparisons and phone-number capability lookup, with the caveat that number lookup is a capability signal and not consent. |
| sent-account-readiness | 2,900 | Preflight on the authorized connection: which organization and Sender Profile the grant covers, balance, onboarding and KYC status, and what is blocking a launch. |
| sent-webhook-engineer | 2,736 | Webhook receiver construction and debugging: endpoint registration, HMAC `x-webhook-signature` verification, replay rejection, event dedupe, retry and auto-disable recovery, secret rotation; ships `scripts/verify_signature.py`. |
| sent-two-way-messaging | 2,736 | Inbound and consent flows: STOP and HELP keyword handling, consent state on contacts, auto-replies inside the WhatsApp 24-hour window, RCS STOP chips and conversation history paging. |
| sent-routing-strategist | 2,735 | Channel selection and route diagnosis: automatic versus pinned channels, what the channel array does, fallback and reroute behavior, FAILED, FILTERED and BLOCKED outcomes, and duplicate charges. |
| sent-integration-starter | 2,735 | Standing up a Sent v3 integration: SDK choice, `x-api-key` wiring, idempotent sends, retry and 429 or 409 handling, the 46-code error catalog, sandbox verification; ships `scripts/preflight.py`. |
| migrate-to-sent | 2,735 | Moving off Twilio, Sinch, Infobip, Vonage or MessageBird: call and status vocabulary mapping, webhook signature schemes, opt-out stores, dual-run metrics, cutover gates and rollback; ships `scripts/inventory_scan.py`. |
| sent-profile-provisioning | 2,734 | Executing the Sender Profile lifecycle over MCP and REST: `POST /v3/profiles`, inherit versus dedicated resources, completion callbacks, per-profile 10DLC campaigns, users and roles. |

The remaining 2 indexed listings range from 3 to 3 installs.

## Why This Matters for Hermes Agents

Most messaging skills available to an agent stop at the API reference, which leaves the dangerous part, the decision to send, entirely to the model. This collection puts the guardrail inside the skill: a preview of organization, Sender Profile, template ID and variables, an explicit confirmation immediately before the call, and a rule that a changed payload or a retry needs a fresh preview. For a Hermes profile that sends on someone else's behalf, that structure is the difference between a reviewable action and an incident.

The template-only send path is the second useful constraint. `messages.send` accepts a template and its declared parameters, and the skill is told to resolve the template through `templates.list` in the same acting scope before building the payload, so an agent cannot invent message text and call it a template. Combined with `idempotencyKey` reuse for 24 hours, an ambiguous timeout becomes a reconciliation problem rather than a duplicate-message problem.

The scope model also maps cleanly onto how Hermes runs jobs. An organization grant can act as an owned Sender Profile through a `profileId`, a profile grant cannot, and `sender_profiles.*` rejects acting profiles outright. `sent-account-readiness` exists to read that grant before anything mutates, which is exactly the preflight a cron or subagent needs when it wakes up without conversational context.

Finally, the specialist skills carry real local tooling rather than prose. `analyze_mdr_funnel.py`, `validate_10dlc_packet.py`, `lint_waba_template.py`, `verify_signature.py`, `preflight.py` and `inventory_scan.py` all run offline against files you supply and each takes a `--self-test` flag, which means a Hermes cron can validate a webhook signature or a 10DLC packet without holding a live credential or touching the network.

## Usage

| You say | What happens |
|---|---|
| "Send the approved order-update template to this number" | The skill reads the template through `templates.list`, builds the exact `messages.send` arguments, previews organization, profile, channel, destination, template content and variables, waits for confirmation, then reports the returned state as queued or accepted rather than delivered. |
| "Did message msg_123 actually deliver?" | `messages.get` returns the current record and `messages.activities.list` returns lifecycle events, so the answer cites timestamps and status evidence, with the recipient masked and the body omitted. |
| "Why did SMS delivery drop last week?" | `sent-analytics` answers aggregate totals, and `messaging-performance-analyzer` takes the MDR export for funnel drop-off, error-code clusters and channel fallback, then names the failing stage instead of the dashboard number. |
| "Our webhook endpoint returns 401 on every delivery" | `sent-webhook-engineer` works through signature verification with `verify_signature.py` against the raw captured body and headers, then checks the replay window, dedupe keys and whether the endpoint was auto-disabled. |
| "Register a 10DLC campaign for this brand" | `sms-10dlc-registration` assembles the brand and campaign packet, validates the payload locally, checks opt-in and sample-message policy, and maps each rejection reason to a remediation step. |
| "We are modelling 50 messaging tenants, one per brand" | `sender-profile-architect` decides the profile boundary, API-key scoping and webhook routing, then `sent-profile-provisioning` creates the profiles over MCP or `POST /v3/profiles` and handles completion callbacks and roles. |
| "We are moving off Twilio next quarter" | `migrate-to-sent` scans the repository for send calls and status handling with `inventory_scan.py`, maps the vocabularies, and produces dual-run comparison metrics plus rollback conditions before any cutover. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code} analyzer\n" \
  https://raw.githubusercontent.com/sentdm/sent-plugin/main/claude-plugins/sent/skills/messaging-performance-analyzer/SKILL.md
curl -sL -o /dev/null -w "%{http_code} webhook\n" \
  https://raw.githubusercontent.com/sentdm/sent-plugin/main/claude-plugins/sent/skills/sent-webhook-engineer/SKILL.md
```

Expect `200` twice. Those URLs are the Claude Code adapter copies, which is what the pack sampled; the canonical file for the same skill sits at `packages/sent/skills/<name>/SKILL.md` and carries the identical frontmatter. Read one before installing, because the description is the whole routing contract: a good Sent skill description names the trigger phrases, the MCP tools it will call and the skill it should hand off to.

After a copy lands in the profile, confirm the frontmatter and the shape of the directory:

```bash
head -6 ~/.hermes/profiles/corpusiq/skills/sent-messaging/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/sent-webhook-engineer/
```

A good copy shows `name:` and `description:` in the frontmatter and no other fields, and the directory listing shows `SKILL.md`, `agents/`, `references/` and `scripts/` for the skills that ship them. License and version live in `packages/sent/plugin.json` (MIT, version 0.3.0), not in the skill file. The bundled helpers self-test offline, which is the cheapest way to prove the copy is intact:

```bash
python3 ~/.hermes/profiles/corpusiq/skills/sent-webhook-engineer/scripts/verify_signature.py --self-test
python3 ~/.hermes/profiles/corpusiq/skills/sent-integration-starter/scripts/preflight.py --self-test
```

In the repository itself, `python3 scripts/validate.py` is the gate the maintainers run; it validates the portable package, skills, evals and adapters.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sent | Pass | Pass | Pass |
| waba-template-author | Pass | Pass | Pass |
| waba-embedded-signup | Pass | Pass | Pass |
| messaging-performance-analyzer | Pass | Pass | Warn |
| template-builder-ui | Pass | Pass | Warn |
| sent-compliance | Pass | Pass | Pass |

No FAIL verdict appears in the sampled six. The worst result is a Snyk Warn on `messaging-performance-analyzer` and `template-builder-ui`, and the pack records the verdict rather than the finding behind it, so read those two Snyk entries on skills.sh before you install them. In practice a Warn on this repository most plausibly tracks the class of risk it actually carries: skills that instruct an agent to run bundled Python over user-supplied exports and payloads, and a collection whose other half performs live writes against a messaging account.

The write surface is the part to review, not the markdown. The skills can send messages, create and delete contacts, create and delete Sender Profiles and send feedback to Sent staff, and the README's own contract requires a preview and explicit confirmation before each of those. Authentication is client-managed OAuth 2.1 with PKCE and dynamic client registration, the plugin does not accept or store Sent credentials, and the repository repeats the rule that API keys and tokens must never be pasted into a prompt. Two per-account limits are worth knowing before you point an agent at a paid account: number lookup is billed and capped at 1000 calls per authenticated account scope per UTC day, and feedback is capped at 20 calls per scope per UTC day with 2000 characters per report.

## Limitations

- Snapshot data, verified 2026-10-29: 54,176 combined installs across 21 indexed listings; 49 GitHub stars; MIT License; last pushed 2026-10-20. Counts drift over time.
- The index count and the tree disagree by design. skills.sh indexes 21 listings, one per skill name, while the checkout holds 84 `SKILL.md` files: the same 21 skills in four parallel layouts, `skills/<name>/SKILL.md`, `packages/sent/skills/<name>/SKILL.md`, `plugins/sent/skills/<name>/SKILL.md` for Codex and `claude-plugins/sent/skills/<name>/SKILL.md` for Claude Code. Only `packages/sent` is canonical, and the other three are generated, so edits belong there and a copy taken from an adapter tree is a generated copy.
- Install counts do not rank these skills. Nineteen listings sit between 2,734 and 2,921 installs, which is publication noise rather than adoption signal, and the two lowest, `sent-feedback` and `sent-compliance` at 3 installs each, are real skills with live MCP backing. Judge a skill by its `SKILL.md` and its evals, not by the number beside it.
- Behaviour is not identical across adapters. The Claude Code copy of `sent-messaging` adds host policy that the canonical file does not carry, limiting a call to one recipient and refusing MARKETING-category templates on Claude connections, and the Claude adapter copy of `sent` narrows Sender Profile creation and deletion to the dashboard. A guide, a prompt or a test written against one layout can be wrong on the other.
- Half of the collection is inert without a compatible MCP client. The skills that read or mutate live data need the remote server at `https://mcp.sent.dm/mcp`, an authorized connection and a selected organization, and the README notes that the hosted connector path restricts profile create and delete and applies organization-wide send quotas. Without that client the skills still plan payloads and explain failures, and they will say so rather than pretend to have sent anything.
- There is no MCP reschedule or cancellation tool, profile create and delete require an `idempotencyKey`, and an interrupted outcome requires reconciliation before the next operation. Any workflow that assumes an agent can cancel or edit a queued message needs to route through the dashboard instead.

## Related

- [Hermes Whatsapp Secretary Setup](/hermes/skills/catalog/hermes-whatsapp-secretary-setup)
- [Agent Email CLI Skill Setup](/hermes/skills/catalog/agent-email-cli-setup)
- [Nexscope E-Commerce Skills - Shopify, Etsy, TikTok Shop & Marketplace Growth Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole directory, not the markdown. Six of the 21 skills carry `scripts/` and most carry `references/`; a lone `SKILL.md` leaves the agent describing a validator it cannot run.
- Start with `sent` plus one working skill, not `--skill '*'`. The dispatcher is cheap to hold, and a 21-skill install puts 21 descriptions into routing context before the agent has done anything useful.
- Wire `sent-account-readiness` into any cron that sends. It answers which profile, which balance and whether the account can send at all, which is exactly the context a scheduled job lacks when it wakes up cold.
- Run the bundled helpers with `--self-test` in CI. `verify_signature.py`, `preflight.py`, `inventory_scan.py`, `analyze_mdr_funnel.py` and the 10DLC validators all run offline, so a fixture check proves the copy works without a Sent account or a network call.
- Keep the credential out of the transcript. Every skill repeats the rule, and it is the one rule worth enforcing in the prompt as well: no API keys or tokens in chat, OAuth through the client, and revoke by deactivating the connection's API key in the Sent dashboard when a grant is no longer needed.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
