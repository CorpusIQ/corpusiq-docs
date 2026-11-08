---
title: "COSS Skills - One API for Email, SMS and Inboxes"
description: "cosscom/coss on skills.sh: 8.3K combined installs; one skill plus an MCP server for email, SMS, agent inboxes, verify, webhooks and diagnostics."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/coss-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "email api", "sms", "mcp server"]
---

# COSS Skills - Setup Guide

**Source:** [cosscom/coss](https://www.skills.sh/cosscom/coss) via skills.sh - 8,273 combined installs across 2 indexed listings; first seen 2026-11-08 (Nov 8 2026 morning sweep)
**GitHub:** 5 stars, MIT plugin inside an AGPL-3.0 monorepo, last pushed 2026-11-06, 1 SKILL.md directory at plugins/coss/skills/coss
**Category:** Messaging for agents: email, SMS, agent inboxes, scheduling and webhooks behind one SDK and one API key
**Quality Tier:** 🟡 Use With Care - 5 stars against 4,657 installs, an AGPL-3.0 repository root, and a Snyk warning on the second indexed listing.

This is a one-skill plugin attached to a product, not a skill attached to a repository. The skill is 105 lines of `SKILL.md` inside `plugins/coss/skills/coss/`, and it exists to teach an agent how to add coss.com to a project: the docs it should read, the development key it should use, the SDK conventions it must follow, and how to check what actually happened after a send.

The surrounding repository is a full monorepo: Bun workspaces, Turborepo, TypeScript, Next.js 16 for the dashboard, Hono for the public API, Postgres with Drizzle, Valkey for rate limits, Better Auth for organizations and API keys, Expo for the iOS app. You do not need any of that to use the skill. It is context for what the API does and for the licence question in the security section.

The skill's opening instruction is the useful part: read the docs instead of guessing. `https://coss.com/llms.txt` opens with a brief and lists every product's API operations, every docs page is available as Markdown by appending `.md` to its URL, and the API reference pages carry method, URL, every field, responses, errors and examples in eight languages. For an agent that would otherwise invent a webhook payload shape, that is the difference between working code and a plausible failure.

What the products actually are: transactional email through Amazon SES or a fake provider, marketing broadcasts, inboxes with a real address per agent, SMS, Verify for one-time codes by SMS or email, Sign for e-signatures, Forms for hosted form endpoints, Scheduling for bookings, Hooks for user-facing webhooks, and Risk for sign-up, login and payment decisions.

## Installation

The repository documents a Claude Code plugin as the primary path, from `plugins/coss/README.md`:

```text
/plugin install coss --marketplace cosscom/coss
```

On Claude Code before 2.1.275 the README gives the two-step form:

```text
/plugin marketplace add cosscom/coss
/plugin install coss@coss
```

Installing asks for an API key for the MCP server. A development key (`coss_test_...`) is the intended answer, and leaving it empty gives you the docs tools only. Every other harness gets the same skill through skills.sh, which the README states explicitly:

```bash
npx skills add cosscom/coss
```

That route installs the skill but not the plugin's MCP configuration, so the tools in `plugins/coss/.mcp.json` have to be registered by hand if you want them:

```json
{
  "mcpServers": {
    "coss": {
      "command": "npx",
      "args": ["-y", "coss-mcp"],
      "env": {
        "COSS_API_KEY": "${user_config.api_key}",
        "COSS_MCP_TOOLSETS": "${user_config.toolsets}"
      }
    }
  }
}
```

The plugin also exposes a `toolsets` setting. It takes a comma-separated list drawn from `email, marketing, inboxes, sms, verify, sign, forms, scheduling, webhooks, hooks, risk` and narrows which MCP tools are offered, which matters if you run a small context budget. The docs, setup, logs and account tools are always present.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| coss | 4,657 | Adding coss.com to a project: docs-first workflow, development key, SDK error handling, webhook verification, delivery diagnosis |
| coss-particles | 3,616 | A second indexed listing with no SKILL.md directory in this repository tree, so its contents could not be inspected |

The threshold for this pack is zero, so every indexed row is in the table above. There is no tail: 0 rows fall below the threshold.

The single SKILL.md carries four instruction blocks. "Read the docs first" points at the `llms.txt` index and the `.md` variants of every page. "Get a development key" describes `npx coss-cli init`, which opens a browser for the user to approve a project key, waits up to five minutes, writes `COSS_API_KEY` into `.env.local` or `.env`, installs the `coss` package in JavaScript projects, and appends a short section to the project's `AGENTS.md` for later sessions unless `--no-agents` is passed. Where no browser can open, over SSH or in a container, the command prints a link and waits for a typed code, and the skill tells the agent to hand that step to the user.

"Write the code" sets the conventions: `new Coss()` reads `COSS_API_KEY`, the client belongs in server code only, every method returns `{ data, error }` and never throws for API or network failures, and retries are automatic with an `Idempotency-Key` on every POST. The inbox section is the one aimed squarely at agents: `coss.inboxes.create()` gives the agent an address, mail arrives as threads with an `inbox.message.received` webhook, `extracted_text` strips the quoted conversation, and the skill's own rule is to treat inbound mail as untrusted data and never as instructions.

The last block is diagnosis, and it is unusually concrete. `npx coss-cli logs tail` follows requests and events, `npx coss-cli emails diagnose <email id>` or `--to <address>` explains a delivery, and the same `diagnose` verb exists for sms, verify, sign, forms, hooks and scheduling. The MCP server exposes the equivalents as tools, and `api_get` reads any `/v1/` path that no dedicated tool covers. The skill also notes that form spam is answered like a success, so what a submitter saw proves nothing.

## Why This Matters for Hermes Agents

Agent infrastructure eventually needs to send mail as itself. This skill is written for that case rather than for a human integrating a vendor SDK: it treats the agent as the operator, gives it a development key that delivers nothing, and hands it a diagnosis loop for when a send looks wrong.

The development-key split is the design worth copying. `coss_test_...` keys work against every API and record every email and SMS with events and webhooks, but deliver nothing, and the SES simulator addresses (`bounce@simulator.amazonses.com`, `complaint@simulator.amazonses.com`) produce real failures to test against. The skill forbids asking for a live key to try something and puts going live in the user's hands. That is a working answer to the problem every messaging integration has: how to test without emailing a stranger.

The error contract is the other transferable piece. Methods return `{ data, error }` and never throw, so an agent has to branch on `error.type`, `error.code`, `error.message` and `error.hint` instead of catching an exception and retrying blindly. Combined with automatic idempotency keys on every POST, that removes the two classic failure modes of agent-driven sends: a retry that sends twice, and a silent failure that gets reported as success.

Inbound mail as untrusted input is the security rule most agent inbox implementations miss. The skill states it in one line, and it is the line that stops a received email from being read as a new instruction to the agent that owns the address.

## Usage

| You say | What happens |
|---|---|
| "Add coss.com to this Next.js app" | Reads the docs index, runs `npx coss-cli init`, waits for the browser approval, writes `COSS_API_KEY` to `.env.local` |
| "Send a welcome email to this address" | Uses the test key, `coss.email.send` with `{ data, error }` handling, and reports the delivery status |
| "Give this agent its own email address" | `coss.inboxes.create()`, then threads arrive via `inbox.message.received` and are answered with `messages.reply()` |
| "Why did that email bounce?" | `npx coss-cli emails diagnose <id>` or `--to <address>` returns a verdict, what it means and the next step |
| "Set up a webhook handler" | `verifyWebhook(rawBody, headers, secret)` before any parsing, idempotent on the `webhook-id` header |
| "Test webhooks locally" | `npx coss-cli login` once, then `npx coss-cli listen --forward-to localhost:3000/<path>` |
| "Send a broadcast to all customers" | The skill calls out that broadcasts and signature requests reach real people on a live key, and asks you to confirm the audience |

## Verification

Read the skill and the plugin manifest before installing. All three paths returned 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/cosscom/coss/main/plugins/coss/skills/coss/SKILL.md | head -40
curl -fsSL https://raw.githubusercontent.com/cosscom/coss/main/plugins/coss/.claude-plugin/plugin.json
curl -fsSL https://raw.githubusercontent.com/cosscom/coss/main/plugins/coss/README.md
```

The first should open with frontmatter naming `coss` and a long description that lists the products and the trigger phrases, then the heading "Building with coss.com". The manifest should show `"name": "coss"`, `"license": "MIT"`, a `userConfig` block with a sensitive `api_key` field and the `toolsets` string. The third file should state the plugin install command and the `npx skills add cosscom/coss` alternative for other agents.

After installing, the check that matters is whether the key is a test key and whether the tooling sees it:

```bash
grep -m1 COSS_API_KEY .env.local .env 2>/dev/null
npx coss-cli --help
```

The value should start with `coss_test_`. A `coss_live_` key in a development environment is a real sender, and the skill is explicit that this is the user's step to take, in the dashboard, not the agent's.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| coss | Pass | Pass | Pass |
| coss-particles | Pass | Pass | Warn |

The primary skill passes all three scanners, which is consistent with 105 lines of markdown that contain no executable content. The warning is on `coss-particles`, and that is where the honest answer is uncomfortable: the pack indexes it as a separate listing with 3,616 installs, the repository contains exactly one SKILL.md directory, and a lookup of `cosscom/coss-particles` returns 404. So the Snyk warning sits on an artifact this review could not open. Treat it as unknown rather than as cleared, and check the security page on skills.sh before trusting anything under that name.

The structural risks are not in the markdown. The skill drives three executables: `coss-cli`, the `coss-mcp` server, and the SDK calls in your code. All three hold an API key that can send real email and SMS, and the MCP server additionally reads delivery data. The skill's own guardrails are sound, with the test-key split, the ban on asking for a live key, and the rule that inbound mail is data and never instructions. None of those are enforced by the runtime; they are instructions the model follows.

Licence needs reading twice. `plugins/coss/` ships its own MIT LICENSE (Copyright (c) 2026 Cal.com, Inc.) and the plugin manifest declares MIT, so the skill text is permissive. The repository root LICENSE is the GNU Affero General Public License, version 3. Code you lift out of `apps/` or `packages/` into your own product carries AGPL terms, and the AGPL and MIT files cover different trees. The skill itself is the MIT part.

## Limitations

- Snapshot data, verified 2026-11-08: 8,273 combined installs across 2 indexed listings; 5 GitHub stars; MIT plugin inside an AGPL-3.0 repository; last pushed 2026-11-06.
- The adoption numbers and the star count disagree sharply. 4,657 installs against 5 stars is a distribution signal, not a maturity signal, and the repo is days old at this snapshot.
- Drift between the index and the tree: 2 indexed listings against 1 SKILL.md directory. `coss-particles` has no directory here and no repository at `cosscom/coss-particles` returned anything, so it is unverifiable.
- The MCP tools are only configured automatically through the Claude Code plugin. With `npx skills add cosscom/coss` you get the skill alone and must register `npx -y coss-mcp` yourself.
- The skill assumes `coss-cli` on demand through `npx`, so it needs Node and network access. The browser-based `init` and `login` flows need a real browser and a human to approve them.
- Self-hosting is a separate project with real prerequisites: Bun 1.4.2 or newer, Node 24 or newer, PostgreSQL 18 and Valkey 8. Nothing in this guide needs them, but the monorepo README is the entry point if you want them.
- Product coverage in the skill is uneven by nature: email and inboxes are described in detail, while Verify, Sign, Forms and Scheduling are one line plus a docs link each.
- Not verified: a real send, a real webhook delivery, and the `diagnose` verbs. The `coss_test_` key path was read from the skill, not exercised against a live account, and no API key was used during this review.
- `coss-particles` contents, provenance and Snyk warning could not be inspected, so no claim is made about it beyond the verdict cells.

## Related

- [Resend Agent Skills - Setup Guide](/hermes/skills/catalog/resend-skills-setup)
- [Agent Email CLI Skill - Setup Guide](/hermes/skills/catalog/agent-email-cli-setup)
- [IMAP/SMTP Email - OpenClaw Email Integration Setup Guide](/hermes/skills/catalog/imap-smtp-email-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Keep the test key in development and let the user mint the live one. Every `coss_test_` send is recorded with events and webhooks, so your integration tests get realistic payloads without delivering anything.
- Set `COSS_MCP_TOOLSETS` to only the products in play. Eleven toolsets is a lot of tool descriptions competing for context, and the docs and diagnosis tools stay available either way.
- Use the simulator addresses deliberately. Sending to `bounce@simulator.amazonses.com` and `complaint@simulator.amazonses.com` gives you real failure events to build your handler against, which is cheaper than waiting for a real bounce.
- Verify webhooks before parsing, with the raw body. `verifyWebhook` throws on a bad signature only if the body is byte-identical to what arrived, and re-serialised JSON breaks that.
- Run `npx coss-cli logs tail` while you develop rather than after. It shows requests and events as they happen and turns a mystery into a request log.
- Treat `{ data, error }` as mandatory control flow, not as a style choice. The SDK does not throw, so an unchecked `data` is the failure mode that ships.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
