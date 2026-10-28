---
title: "Sumsub Agent Skills - KYC and AML Platform Setup"
description: "Sumsub's first-party API suite: 25.0K combined installs. KYC levels, questionnaires, WebSDK, AML rules, and Travel Rule integration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sumsub-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "kyc", "aml", "identity verification"]
---

# Sumsub Agent Skills - Setup Guide

**Source:** [sumsub/agent-skills](https://www.skills.sh/sumsub/agent-skills) via skills.sh - 25.0K combined installs across 28 indexed listings; verified 2026-10-27 (Oct 27 sweep)

**GitHub:** [sumsub/agent-skills](https://github.com/sumsub/agent-skills) - 7 stars, no license file at repo root (the README states MIT, the GitHub API reports no SPDX license), branch main, 28 self-contained skill directories under `skills/`, each with a `SKILL.md` entry point plus optional `scripts/`, `references/` and `examples/`

**Category:** Identity verification and AML compliance API integration

**Quality Tier:** 🟡 Beta - first-party vendor suite, 7 stars, no license declared at repo root, 28 indexed listings against 28 in-tree skill directories

Sumsub is a KYC, KYB and AML provider, and this repository is the vendor's own skill set for configuring its platform through an agent rather than the dashboard. The stated purpose in the repo description is narrow and accurate: agent skills for the Sumsub API. Every one of the 28 directories wraps a specific surface, from HMAC-signed authentication and applicant levels through questionnaires, Proof-of-Address presets, WebSDK wiring, Mobile SDK theming and Travel Rule submission.

The suite is organised as a loop rather than a list. `sumsub-analyze-regulation` reads a regulation or policy document and produces a Sumsub configuration plan that names levels, questionnaires, PoA presets, transaction monitoring rules and workflows. The `create-*` skills then build each piece through the public API, and `sumsub-conformance` closes the loop by tracing every requirement of the same document through the deployed config graph and flagging requirements that are collected and scored but never enforced. `sumsub-api-generic` is the documented fallback for anything the named skills do not cover: it searches a bundled OpenAPI schema, inspects the operation, signs the request and calls it.

Two design decisions stand out for agents. First, the credential policy is enforced rather than documented: the README requires an agent-scoped sandbox token pair and states that the helper scripts refuse any token that does not start with `sbx:`. Second, most skills carry preconditions and refuse to proceed until earlier state is confirmed, which is what makes a multi-step KYC configuration survivable when no human is watching each call.

## Installation

The README's primary path installs every skill in the repository through the skills CLI:

```bash
npx skills add sumsub/agent-skills --all -y
```

That fetches the repo and installs each skill into your agent's skills directory. For Claude Code the README notes `~/.claude/skills/` for a global install and `.claude/skills/` for a project-local one.

The manual path is a clone plus a copy of the directories you want, which is also the practical route for a Hermes install directory such as `~/.hermes/skills/`:

```bash
git clone --depth 1 https://github.com/sumsub/agent-skills.git
cp -r skills/sumsub-create-questionnaire ~/.hermes/skills/
```

Credentials come next. The README documents generating an agent-scoped sandbox token pair in the Sumsub dashboard under "Connect Sumsub to your AI agent", then supplying the pair as environment variables to the agent. The Claude Code example writes them into a gitignored `.claude/settings.local.json`:

```json
{
  "env": {
    "SUMSUB_APP_TOKEN": "sbx:...",
    "SUMSUB_SECRET_KEY": "..."
  }
}
```

The README lists the runtime requirements as `bash`, `curl`, `openssl` and `python3` (standard library only) on `PATH`. There are no bundled MCP servers, plugins or hooks, and no manifest at the repo root other than `package.json` and `skills.json`, which is the skills manifest (version 1.5.0 in the clone) carrying names, paths and descriptions.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sumsub-api-auth | 1,217 | Authenticating to api.sumsub.com with an App Token and secret, HMAC-SHA256 request signing, and diagnosing 401 responses. Sandbox tokens only. |
| sumsub-api-generic | 1,213 | Anything Sumsub-API-related the named skills do not cover: searches the bundled OpenAPI schema, inspects the operation, signs with the App Token and calls it. |
| sumsub-check-skills-version | 1,209 | Checking whether the installed skills are current by fetching the canonical version from api.sumsub.com/llms.txt and comparing it with the local copy. |
| sumsub-create-poa-preset | 1,203 | Creating, patching and reading a `PoaStepSettings` Proof-of-Address preset whose returned id attaches to a level's `PROOF_OF_RESIDENCE` doc-set. |
| sumsub-manage-webhooks | 1,202 | Listing, reading, creating and patching `clientWebhooks` event subscriptions. Sandbox only; production webhook setup stays in the dashboard. |
| sumsub-create-level | 1,201 | Building an `ApplicantLevel` payload with its doc-sets and optional `questionnaireDefId`, and creating, patching or reading it by id. |
| sumsub-integrate-websdk | 1,200 | Wiring the WebSDK end to end: level setup, server-signed access-token endpoint, `snsWebSdk` init in vanilla and React, lifecycle events, webhook signature verification and a go-live checklist. |
| sumsub-analyze-regulation | 1,199 | Turning a regulation document into a Sumsub configuration plan, mapping each requirement to levels, questionnaires, PoA presets, transaction monitoring rules and workflows. |
| sumsub-create-cross-check-preset | 1,198 | Creating POI-to-POA name and address comparison rules, only when the default preset is explicitly to be overridden. |
| sumsub-create-questionnaire | 1,194 | Building a `QuestionnaireDefinition` from a compact spec into a localized payload, then creating or updating it, with 409 and 404 handling for duplicate and missing ids. |
| sumsub-create-transaction | 1,191 | Submitting a `KytTxnData` payload to Transaction Monitoring, auto-routed between the existing-applicant and non-existing-applicant endpoints. |
| sumsub-check-permissions | 1,169 | Reading the tenant's enabled entitlements as an allowed-checks map, which the create-* skills use to gate entitlement-dependent features before building a payload. |
| sumsub-conformance | 1,007 | Auditing whether the deployed config satisfies a regulation or policy document, tracing each requirement to where it is collected, scored and enforced, and flagging collected-but-not-enforced gaps. Advisory and read-only. |
| sumsub-create-kyt-rules | 1,004 | Translating described conditions such as amount thresholds, country lists and aggregations into `KytTxnRule` scoring rules, which start in test mode. |
| sumsub-integrate-id-connect | 993 | Adding the ID Connect OIDC flow: button or raw OIDC frontend, backend code, access-token exchange, share-token mint, partner-consent share link and applicant materialisation. |
| sumsub-integrate-dint-websdk | 993 | Adding Device Intelligence to an existing WebSDK integration, including capture settings on the level, Fisherman lifecycle, device signals and risk labels. |
| sumsub-integrate-dint-standalone | 992 | Adding Device Intelligence to pages without the WebSDK widget, such as login, signup, checkout and 2FA, using a behavior access token and `@sumsub/fisherman`. |
| sumsub-integrate-msdk | 991 | Adding KYC to a native iOS or Android app, from SDK installation through permissions to a runnable integration file with token refresh and lifecycle callbacks. |
| sumsub-supported-id-documents | 648 | Reading the built-in supported document catalogue and editing per-country overrides through a read-modify-write against the country mappings endpoint. |
| sumsub-manage-applicant-tags | 647 | Adding, overwriting or removing tags on an applicant profile, with read-back through the applicant record. |
| sumsub-create-workflow | 555 | Building an `ApplicantWorkflow` from a node and edge spec, creating it as a draft and publishing through the revision status endpoint. |

The remaining 7 indexed listings range from 188 to 480 installs: sumsub-create-aml-resolution-rules (480), sumsub-resolve-currency (478), sumsub-manage-wallet-address-book (478), sumsub-integrate-travel-rule (478), sumsub-theme-msdk (445), sumsub-check-databases (189) and sumsub-manage-client-lists (188). Those cover the AML Resolution Rule Chain, currency resolution for transactions, the Travel Rule wallet address book, the full Travel Rule flow, Mobile SDK theming, database check-source discovery and client lists.

## Why This Matters for Hermes Agents

Compliance configuration is a domain where plausible output is dangerous. An agent that invents a questionnaire field name, a document type code or a workflow condition produces a config that either fails to publish or publishes with a gap, and the gap is only visible at audit time. These skills are written against the real enums and parameter names, and `sumsub-analyze-regulation` explicitly requires concrete values such as `docTypes: [PASSPORT, ID_CARD, DRIVERS]` and `videoRequired: passiveLiveness` rather than prose descriptions.

The suite also encodes the order of operations that the dashboard hides. Entitlements have to be checked before a payload is built, check-sources have to be confirmed as enabled for the tenant and the environment before a level references them, and a questionnaire id has to exist before a level can wire it in. Those dependencies are where a hand-rolled integration loses hours, and each one is a gate inside a skill rather than a paragraph in a doc.

The generate-then-verify pairing is the part worth copying. `sumsub-analyze-regulation` builds a plan from a regulation, the create skills implement it, and `sumsub-conformance` resolves the deployed graph and reports per requirement whether it is collected, scored and enforced. Its headline finding, collected-but-not-enforced, is exactly the failure a builder cannot see by reading their own config back.

Finally, the sandbox discipline makes the suite usable by an autonomous agent. The helper scripts refuse tokens without the `sbx:` prefix, the README states that an agent token is scoped to sandbox data, and several skills declare themselves sandbox only. That is a stronger safety posture than most vendor skill sets ship, even though it has documented holes.

## Usage

| You say | What happens |
|---|---|
| "Read this regulation PDF and tell me what our Sumsub config needs" | sumsub-analyze-regulation extracts the obligations and returns a plan mapping them to levels, questionnaires, PoA presets, transaction monitoring rules and workflows, with concrete parameter names. |
| "Build the retail KYC level with a source-of-funds questionnaire" | sumsub-check-permissions confirms entitlements, sumsub-check-databases confirms the check-sources, sumsub-create-questionnaire creates the definition, and sumsub-create-level wires the returned id into the level. |
| "Does our live config actually satisfy this policy document" | sumsub-conformance resolves the deployed graph and traces each requirement through collection, scoring and enforcement, flagging requirements that are collected but never enforced. |
| "Add the WebSDK to our React checkout" | sumsub-integrate-websdk sets up the level, generates the server-signed access-token endpoint, initialises `snsWebSdk`, wires lifecycle events and shows how to verify webhook signatures locally with ngrok. |
| "Auto-clear false positive sanctions hits under this threshold" | sumsub-create-aml-resolution-rules upserts the rules into the draft AML Resolution Rule Chain and stops there, publishing only when explicitly asked because the chain is shared with production. |
| "Verify identity inside our iOS app" | sumsub-integrate-msdk detects the platform, walks through Swift Package Manager or CocoaPods installation and permissions, and produces a runnable integration file with token refresh and lifecycle callbacks. |
| "Add device intelligence to our login page, no widget" | sumsub-integrate-dint-standalone mints a behavior access token, initialises `@sumsub/fisherman`, fingerprints the device and shows where to read the resulting signals. |

## Verification

Clone at the branch the pack records and count what landed:

```bash
git clone --depth 1 https://github.com/sumsub/agent-skills.git
cd agent-skills
ls skills | wc -l
find skills -name SKILL.md | wc -l
```

Both counts print 28 in the current tree. To read a skill before installing it, fetch its `SKILL.md` directly from `main`:

```bash
for p in skills/sumsub-api-auth/SKILL.md \
         skills/sumsub-conformance/SKILL.md \
         skills/sumsub-create-aml-resolution-rules/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/sumsub/agent-skills/main/$p"
done
```

Each of those three returned 200 on 2026-10-27, and the same path shape holds for all 28 directories:

- https://raw.githubusercontent.com/sumsub/agent-skills/main/skills/sumsub-api-auth/SKILL.md
- https://raw.githubusercontent.com/sumsub/agent-skills/main/skills/sumsub-create-aml-resolution-rules/SKILL.md
- https://raw.githubusercontent.com/sumsub/agent-skills/main/skills/sumsub-integrate-websdk/SKILL.md

After install, confirm the directories are visible to the agent and that the CLI did not silently skip one:

```bash
ls ~/.hermes/skills | grep -c '^sumsub-'
```

Then run `sumsub-check-skills-version`. It compares the installed copy against the canonical version published at `https://api.sumsub.com/llms.txt` and recommends `npx skills add sumsub/agent-skills --all` when the local copy is behind. A successful run of `sumsub-api-auth` against a sandbox token is the other useful smoke test: it verifies signing, and a 401 there points at the token pair rather than at the skill.

## Security

skills.sh verdicts for the Gen Agent Trust Hub, Socket and Snyk auditors were not sampled for this suite, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sumsub-api-auth | Not checked | Not checked | Not checked |
| sumsub-api-generic | Not checked | Not checked | Not checked |
| sumsub-check-skills-version | Not checked | Not checked | Not checked |
| sumsub-create-poa-preset | Not checked | Not checked | Not checked |
| sumsub-manage-webhooks | Not checked | Not checked | Not checked |
| sumsub-create-level | Not checked | Not checked | Not checked |
| sumsub-integrate-websdk | Not checked | Not checked | Not checked |
| sumsub-analyze-regulation | Not checked | Not checked | Not checked |
| sumsub-create-cross-check-preset | Not checked | Not checked | Not checked |
| sumsub-create-questionnaire | Not checked | Not checked | Not checked |
| sumsub-create-transaction | Not checked | Not checked | Not checked |
| sumsub-check-permissions | Not checked | Not checked | Not checked |
| sumsub-conformance | Not checked | Not checked | Not checked |
| sumsub-create-kyt-rules | Not checked | Not checked | Not checked |
| sumsub-integrate-id-connect | Not checked | Not checked | Not checked |
| sumsub-integrate-dint-websdk | Not checked | Not checked | Not checked |
| sumsub-integrate-dint-standalone | Not checked | Not checked | Not checked |
| sumsub-integrate-msdk | Not checked | Not checked | Not checked |
| sumsub-supported-id-documents | Not checked | Not checked | Not checked |
| sumsub-manage-applicant-tags | Not checked | Not checked | Not checked |
| sumsub-create-workflow | Not checked | Not checked | Not checked |

The compliance surface is the risk here, not code execution. The skills handle four categories of sensitive material. First, credentials: an App Token and secret used for HMAC-SHA256 request signing, which the README warns must be sandbox scoped because a production token grants full access to live applicant PII. Second, applicant personal data: names, dates of birth, addresses and tax identifiers flow through level, questionnaire, tag and transaction payloads. Third, screening results: with the WATCHLISTS entitlement, PEP, sanctions and adverse media hits are produced and dispositioned, and the AML Resolution Rule Chain decides which of those hits are auto-cleared, confirmed or whitelisted. Fourth, identity artefacts: the skills configure collection of document images and selfies with liveness settings, so the config they build determines how biometric and document data is gathered and scored.

What the skills do not do is equally specific. They do not maintain sanctions lists, do not perform regulatory reporting or set data retention, and do not enable a check-source, since there is no public API for that. `sumsub-conformance` states plainly that it is an advisory gap assistant rather than a compliance guarantee, and `sumsub-analyze-regulation` lists retention, reporting and list maintenance as out of scope for Sumsub. Nothing here substitutes for compliance sign-off.

Recommendation for anyone handling real personal data: run against a sandbox tenant with an `sbx:` token only, keep the token pair in the agent's environment or a gitignored settings file rather than in prompts or skill directories, and use the bundled `examples/` fixtures instead of pasting real applicant records. Note that a sandbox token is not a complete safety boundary: the AML Resolution Rule Chain and workflow revisions are shared across live and sandbox, so publishing either one changes production behaviour. Treat any publish step as a change that requires a human decision, and strip applicant identifiers from transcripts and logs, because whatever the agent reads stays in its context.

## Limitations

- Snapshot data, verified 2026-10-27: 24,962 combined installs across 28 indexed listings; 7 GitHub stars; no license declared at repo root; branch main. Counts drift over time.
- The license status is inconsistent across sources: the README's final line says MIT, while the GitHub API reports no SPDX license and there is no LICENSE file at the repo root. Until the vendor adds one, treat redistribution terms as unconfirmed.
- Directory and listing correspondence is 1:1: 28 `SKILL.md` directories in the tree against 28 indexed listings, and the same 28 entries in `skills.json`. The README's own skills table documents only 26 of them; the two it omits, `sumsub-create-aml-resolution-rules` and `sumsub-check-databases`, are described here from their own `SKILL.md` files and manifest entries.
- Sandbox scope is partial, not total. Webhook management is sandbox only with production setup staying in the dashboard, while the AML Resolution Rule Chain and workflow revisions are tenant-wide and shared between live and sandbox, so an `sbx:` token does not isolate a publish.
- The skills call `api.sumsub.com` directly through shell and Python helpers and require `bash`, `curl`, `openssl` and `python3` on `PATH`. There is no offline mode and no MCP server, so an air-gapped or network-restricted agent gets nothing from the suite.
- `sumsub-check-databases` covers individual KYC check-sources only; the skill states that company (KYB) database verification is not exposed through that endpoint yet. It also warns that the unfiltered catalogue is large enough to overflow a context window, so pass a country code.

## Related

- [Anthropic Financial Services - Setup Guide](/hermes/skills/catalog/anthropics-financial-services-setup)
- [Better Auth Skills - Setup Guide](/hermes/skills/catalog/better-auth-skills-setup)
- [Webhook Subscriptions - Setup Guide](/hermes/skills/catalog/webhook-subscriptions-setup)
- [Ghost Security Skills - Setup Guide](/hermes/skills/catalog/ghostsecurity-skills-setup)

## Pro Tips

- Start with `sumsub-check-permissions` and `sumsub-check-databases` before building anything. Entitlements and enabled check-sources decide which level you can actually build, and both are cheaper to read than to discover from a failed publish.
- Use `sumsub-analyze-regulation` as the entry point when a regulation is in play. Jumping straight to `sumsub-create-level` produces a level that satisfies the prompt and misses the obligation.
- Install the whole set even if you only need one surface. The skills cross-reference each other by name, and a missing sibling turns a routed step into an improvised one.
- Re-run `sumsub-conformance` after every config change, not just at the end. Its value is the collected-but-not-enforced gap list, and that list grows quietly as levels are edited.
- Never publish from an unprompted turn. The AML rule chain and workflow revisions are shared with production, so keep publish behind an explicit instruction and a human review of the diff.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
