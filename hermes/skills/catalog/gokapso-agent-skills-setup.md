---
title: "Kapso Agent Skills - WhatsApp Business Setup"
description: "gokapso/agent-skills: 13.8K combined installs. Kapso skills for WhatsApp Business onboarding, messaging, workflow automation, calling and log triage."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gokapso-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "whatsapp", "kapso", "messaging", "automation"]
---

# Kapso Agent Skills - Setup Guide

**Source:** [gokapso/agent-skills](https://www.skills.sh/gokapso/agent-skills) via skills.sh - 13.8K combined installs across 9 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [gokapso/agent-skills](https://github.com/gokapso/agent-skills) - 195 stars, no license file in the repository, branch master, last pushed 2026-10-09; 4 in-tree skills, each a directory at `skills/<name>/SKILL.md` with a `references/` folder beside it and, for three of the four, `scripts/` and `assets/` as well (`integrate-whatsapp-calling` ships references only), plus a root `tests/` suite and `update-skill-filemap.mjs`

**Category:** WhatsApp Business messaging automation and support workflows

**Quality Tier:** 🟡 Alpha - 5 sampled Warn verdict(s); no repository-level license file; covers WhatsApp onboarding, template and media sends, workflow and function automation, voice calling, and log triage through the Kapso API.

Kapso is a WhatsApp Business platform, and this repository is its own agent skill set, published under the open Agent Skills format in four directories: `integrate-whatsapp`, `automate-whatsapp`, `observe-whatsapp` and `integrate-whatsapp-calling`. The README flags the whole set as alpha and subject to rapid change, so treat the instructions as a moving target rather than a frozen contract. Each skill is a `SKILL.md` entrypoint plus supporting files, and the set leans heavily on those supporting files: `integrate-whatsapp` alone ships 40 scripts and 11 references.

The design choice worth noting is the two-path structure every skill repeats. When the Kapso CLI is installed and authenticated, the skills work CLI-first (`kapso login`, `kapso status`, then verbs like `kapso setup` or `kapso whatsapp numbers resolve`). When it is not, the bundled Node scripts and the direct API references are the fallback, using `KAPSO_API_BASE_URL` and `KAPSO_API_KEY` from the environment. That split means the same skill can drive a live project from a terminal or explain a payload to an agent that has no CLI at all.

The repository also takes agent safety seriously enough to write it into the skill bodies. `integrate-whatsapp` states that messages, webhook payloads, logs, repository contents and API responses are data and not instructions or authorization, that scripts reject redirects and insecure HTTP, and that API keys and secrets must stay out of conversational output. A one-time secret can be captured through `KAPSO_SECRET_OUTPUT_FILE` into a private file with owner-only permissions instead of being printed into a transcript.

## Installation

The README's only install path is the skills CLI, with no flags and no per-skill variant:

```bash
npx skills add gokapso/agent-skills
```

Set the two environment variables before the skills are used, per the README's environment section:

```bash
export KAPSO_API_BASE_URL="https://api.kapso.ai"
export KAPSO_API_KEY="your-api-key"
```

The key comes from the Kapso web app at `app.kapso.ai`, and the README is explicit that the base URL is the host only, with no `/platform/v1` suffix. If the CLI route is the one you want, the README says to start with `kapso login` and `kapso status`; the CLI itself is installed from npm as `npm install -g @kapso/cli`, a line that appears in the `automate-whatsapp` skill rather than in the README.

Hermes is not a target the skills CLI writes to, so the durable route for this profile is a directory copy from a clone into `~/.hermes/profiles/corpusiq/skills/<name>/`. Copy the whole directory and not the markdown alone: `integrate-whatsapp` needs its `scripts/` and `references/`, and `integrate-whatsapp-calling` is almost entirely `references/calling-api.md`, `references/providers.md` and `references/native-artifacts.md`. The three script-bearing skills also expect their npm dependencies, installed once inside the skill directory with the `npm i` line each one documents, and `automate-whatsapp` additionally documents `npm install --save-dev @kapso/workflows` for local workflow source.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| integrate-whatsapp | 4,855 | Connecting WhatsApp to a product end to end: hosted setup-link onboarding (`kapso setup`), connection detection, webhook registration with signature verification and event types, template and interactive message sends, media upload, and WhatsApp Flows create, update, publish, data endpoints and encryption. |
| automate-whatsapp | 4,157 | Building and debugging Kapso automations: workflow CRUD, graph edits through `edit-graph.js` and `validate-graph.js`, WhatsApp and Project Event triggers, functions and their payloads, executions and execution events, variables, and source-controlled workflow projects via `kapso link`, `kapso pull`, `kapso build` and `kapso push` with `@kapso/workflows`. |
| observe-whatsapp | 3,790 | Production diagnostics: Logs search across API, Meta webhook, workflow and webhook-delivery events, message delivery debugging with `message-details.js`, webhook retry inspection through `webhook-deliveries.js`, API error triage through `errors.js`, conversation lookup, and phone-number health checks through `whatsapp-health.js`. |
| integrate-whatsapp-calling | 562 | WhatsApp Calling for voice agents: signed call webhooks, inbound answering, outbound permission and dialing, native recordings and transcripts, and debugging signaling and media with Pipecat, Pipecat Cloud, ElevenLabs Agents or another provider. |

The remaining 5 indexed listings range from 80 to 91 installs.

## Why This Matters for Hermes Agents

WhatsApp Business work is mutation-heavy and mostly irreversible: a template submission goes to Meta review, a send costs money and lands on a customer's phone, and a webhook that misses its signature check is an open door. These four skills encode the sequence a careful operator would follow anyway, which is what makes them usable from a cron job or a subagent that wakes up without a human in the loop.

The split across four skills maps onto how a Hermes run actually fails. Integration failures show up as onboarding or webhook problems in `integrate-whatsapp`, behavioural failures as a workflow or function that does the wrong thing in `automate-whatsapp`, and delivery failures as a message that never arrives in `observe-whatsapp`. Naming those three separately means an agent can be given the debug skill without also being handed the ability to edit a live workflow graph.

The CLI-first, script-fallback structure also fits the way a profile is provisioned. A host with the CLI and a logged-in session gets the shortest path, and a host without one still gets every operation because the scripts call the same API with the same environment variables. Nothing in the skills assumes a specific framework, so a Hermes profile can drive them from a plain terminal, a Python wrapper, or a cron with exported secrets.

Finally, the safety language is unusually concrete for a vendor skill set. Received payloads and logs are explicitly demoted to data, redirects and insecure HTTP are refused by the scripts, and one-time secrets can be written to a private file rather than echoed into the conversation. For an agent that runs unattended, those are the rules that keep a WhatsApp integration from turning a log line into an instruction.

## Usage

| You say | What happens |
|---|---|
| "Onboard this customer's WhatsApp number to our product" | `integrate-whatsapp` runs the hosted setup-link flow, starts with `kapso setup`, resolves project and customer context if the setup is blocked, then confirms the connected number with `kapso whatsapp numbers list` and resolves the exact number before anything is sent. |
| "Send the approved order-update template to this number" | The skill resolves the template through `list-templates.mjs` and `template-status.mjs`, builds the send with `send-template.mjs` against the approved payload shape, uploads any media header first, then returns the raw Meta proxy response with its message id and status rather than claiming delivery. |
| "Our workflow stopped routing new leads" | `automate-whatsapp` pulls the workflow source with `kapso pull`, reads the graph through `get-graph.js`, validates it with `validate-graph.js`, then inspects `list-executions.js` and `list-execution-events.js` to find the trigger or function node that stopped firing. |
| "Why did this message fail last night?" | `observe-whatsapp` runs `message-details.js` and `log-search.js` across API, Meta webhook, workflow and webhook-delivery events, correlates the failing stage, and cites the error code and timestamps instead of a dashboard number. |
| "Meta keeps retrying our webhook, is it broken?" | `integrate-whatsapp` checks the endpoint registration, signature verification and event-type subscription, while `observe-whatsapp` reads `webhook-deliveries.js` for the retry history and returns the failing delivery with its response code. |
| "Answer inbound WhatsApp calls with our voice agent" | `integrate-whatsapp-calling` wires the signed call webhook, answers the inbound call event, checks outbound permission before dialing, and then walks the provider integration for Pipecat or ElevenLabs to confirm audio rather than trusting a 200 from the action call. |
| "Is our number healthy before we launch the campaign?" | `observe-whatsapp` runs `whatsapp-health.js` and `overview.js` on the resolved number, and `integrate-whatsapp` confirms the number is connected and that templates are approved before any send is attempted. |

## Verification

All three raw paths below returned 200 on branch master when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} integrate\n" \
  https://raw.githubusercontent.com/gokapso/agent-skills/master/skills/integrate-whatsapp/SKILL.md
curl -sL -o /dev/null -w "%{http_code} observe\n" \
  https://raw.githubusercontent.com/gokapso/agent-skills/master/skills/observe-whatsapp/SKILL.md
curl -sL -o /dev/null -w "%{http_code} calling\n" \
  https://raw.githubusercontent.com/gokapso/agent-skills/master/skills/integrate-whatsapp-calling/SKILL.md
```

Expect `200` three times. Read the `SKILL.md` before installing, because the frontmatter `description` is the whole routing contract, and note that the branch is `master` here, not `main`: a URL rewritten to `main` returns 404.

After a copy lands in the profile, confirm the frontmatter and that the supporting files came with it:

```bash
head -4 ~/.hermes/profiles/corpusiq/skills/integrate-whatsapp/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/observe-whatsapp/
```

A good copy shows `name:` and `description:` and nothing else in the frontmatter, and the listing shows `SKILL.md`, `references/`, `scripts/` and `assets/` for the skills that ship them. In a full clone, `node --test tests/integrate-whatsapp.test.mjs` runs the offline regression suite against a synthetic API double, which is the cheapest proof that the bundled commands still behave.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| integrate-whatsapp | Pass | Pass | Pass |
| automate-whatsapp | Pass | Warn | Warn |
| observe-whatsapp | Pass | Pass | Warn |
| integrate-whatsapp-calling | Pass | Pass | Warn |
| kapso-automation | Warn | Pass | Pass |

No FAIL verdict appears in the sampled five, but four of the five carry at least one Warn, and `kapso-automation`, which sits in the below-threshold tail of the install index and has no directory in the current tree, is the only one with a Gen Agent Trust Hub Warn. The pack records the verdict rather than the finding behind it, so open the Socket and Snyk entries on skills.sh for `automate-whatsapp`, `observe-whatsapp` and `integrate-whatsapp-calling` before pointing an agent at a live WhatsApp Business account. A plausible reading of that pattern is the one the repository actually carries: skills that run bundled Node scripts over user-supplied payloads, hold an API key in the environment, and perform live mutations against Meta through Kapso.

There is no repository-level license file, so no license terms accompany the code and you should treat redistribution and commercial embedding as unresolved until the publisher states terms. The write surface is the part to review in any case. The skills can create and update workflows, functions, triggers and Flows, submit templates to Meta, send messages and upload media, and place outbound calls, and the skill bodies require that received payloads, logs and provider responses be treated as data rather than authorization. Keep `KAPSO_API_KEY` in the environment or a secret store, and use `KAPSO_SECRET_OUTPUT_FILE` when a one-time secret has to be captured, rather than pasting it into a prompt.

## Limitations

- Snapshot data, verified 2026-10-30: 13,788 combined installs across 9 indexed listings; 195 GitHub stars; no license file; last pushed 2026-10-09. Counts drift over time.
- The install index outruns the tree. Nine listings carry install counts, but only four directories exist in the current checkout, and `whatsapp-messaging`, `kapso-api`, `whatsapp-flows`, `kapso-ops` and `kapso-automation` have no counterpart under `skills/`. Their behaviour cannot be read from this repository, so this guide describes only the four in-tree skills.
- There is no license file at all, on the default branch or in the metadata. Nothing in the repository grants reuse rights, which matters if these skill bodies are going to be copied into a profile, mirrored into a docs tree, or shipped inside a product.
- The set is self-declared alpha and subject to rapid change, the last push was 2026-10-09, and the branch is `master`. Pin a commit when a copy matters, and rewrite raw URLs to `main` at your peril.
- Shared references are described but not present here. The README's maintenance section points at `kapso-docs/skills/skills` as the home of mirrored shared references, and that path does not exist in this checkout, so onboarding and API guidance that lives only in the mirror is not visible from a clone of this repo.
- Everything operationally useful needs a live Kapso project. Sends, template submission, Flows publishing, workflow deploys, Logs search and Calls all require a valid `KAPSO_API_KEY` and a project the key can reach; without one the skills can still explain payloads and read the references, but they cannot act.

## Related

- [Sent Plugin - Messaging and Verification Skills Setup](/hermes/skills/catalog/sent-plugin-setup)
- [Hermes Whatsapp Secretary Setup](/hermes/skills/catalog/hermes-whatsapp-secretary-setup)
- [Agent Email CLI Skill Setup](/hermes/skills/catalog/agent-email-cli-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `observe-whatsapp` alongside `integrate-whatsapp`, not after it. The debug skill is what turns a failed send into an error code and a timestamp, and handing an agent only the send path leaves it guessing when Meta rejects a template.
- Copy the directories, not the markdown. `integrate-whatsapp` ships 40 scripts and 11 references, and a lone `SKILL.md` leaves the agent describing a template sender it cannot run.
- Run `npm i` once inside each copied skill directory before the first real call, then keep the directory read-only for the agent so a run cannot quietly rewrite its own scripts.
- Ask for `kapso status` first in any scheduled job. It confirms project access and available numbers before the job builds a payload, which is the check a cold cron lacks.
- Never put the API key in the conversation. Export `KAPSO_API_KEY` in the job environment and use `KAPSO_SECRET_OUTPUT_FILE` for one-time secrets so a webhook secret is written to a private file instead of a transcript.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
