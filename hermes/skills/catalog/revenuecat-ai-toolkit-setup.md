---
title: "RevenueCat AI Toolkit - In-App Purchase Setup"
description: "Official RevenueCat toolkit: 17.6K combined installs across 20 listings for purchases, paywalls, entitlements and subscription data"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/revenuecat-ai-toolkit-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "revenuecat", "in-app purchases", "subscriptions", "mobile monetization"]
---

# RevenueCat AI Toolkit - Setup Guide

**Source:** [revenuecat/ai-toolkit](https://www.skills.sh/revenuecat/ai-toolkit) via skills.sh - 17.6K combined installs across 20 indexed listings (17,555 exact); first seen 2026-11-10 (Nov 10, 2026 sweep)
**GitHub:** 79 stars, MIT license, `main` branch, last pushed 2026-11-09, 46 `SKILL.md` files among 144 blobs, skill directories split between `revenuecat/skills/<name>/` (the cross-platform plugin) and `revenuecat-play-billing/skills/<name>/` (the Android billing plugin, synced from a separate repository)
**Category:** Mobile monetization: in-app purchases, paywalls, entitlements, subscription analytics and identity
**Quality Tier:** 🟡 Solid with caveats - all 20 listings pass Agent Trust Hub and Socket, but Snyk warns on four, and the suite edits application code while holding a live store credential.

RevenueCat is the subscription backend most small mobile apps end up on, and this repository is its official agent toolkit rather than a community wrapper. It ships two plugins. `revenuecat` carries the RevenueCat MCP server configuration plus cross-platform integration skills for iOS, Android, Kotlin Multiplatform, Flutter and React Native. `revenuecat-play-billing` is a deeper Android track covering Google Play's subscription lifecycle, and its own README names `RevenueCat/play-billing-skills` as the source of truth that it is synced from.

The 20 indexed listings divide cleanly into three jobs. Project skills create and inspect the RevenueCat side: apps, products, entitlements, offerings and API keys, all through the MCP server or the `rc` CLI. Integration skills edit the app: install the SDK, add the purchase and restore flow, render a paywall, gate a feature on an entitlement, wire identity to your own auth. Data skills answer questions: charts, KPIs, project health, and diagnostics when something in the funnel does not match the dashboard.

What makes the collection worth a guide is the ordering. The skills are written to be run in sequence on a new app, and each one states the precondition it expects, which is the difference between an agent that configures RevenueCat correctly in one pass and one that invents a second entitlement with a slightly different identifier.

## Installation

The README's primary route is a plugin marketplace, and it differs per client. Claude Code:

```
/plugin install revenuecat --marketplace RevenueCat/ai-toolkit
```

Add the Android billing plugin on top if you ship Google Play:

```
/plugin install revenuecat-play-billing --marketplace RevenueCat/ai-toolkit
```

Codex uses the same marketplace with a different command, and needs an explicit login step because installing a plugin does not authenticate the MCP server:

```bash
codex plugin marketplace add RevenueCat/ai-toolkit
codex mcp login RevenueCat
```

Cursor installs from its own marketplace with `/add-plugin revenuecat`, and Gemini CLI takes the repository as a single extension:

```bash
gemini extensions install https://github.com/RevenueCat/ai-toolkit
```

For any other agent, including Hermes, the README's fallback installs the skills only:

```bash
npx skills add RevenueCat/ai-toolkit
```

That last command is the important distinction. `npx skills add` copies skill text into the agent's skills directory and does nothing about the MCP server, so the dashboard-side skills have no transport until you point the agent at `https://mcp.revenuecat.ai/mcp` yourself. The README says so directly and links its own MCP setup documentation. Read a skill before running it and check whether it calls an MCP tool or a CLI command; the two kinds fail differently.

Authentication is OAuth against the RevenueCat account, granted per account rather than per project, which means one bad scope decision exposes every project in the organization. Do the authorization in a session where you know which projects matter.

## What It Provides

All 20 indexed listings clear the 500-install threshold, so every one appears below:

| Skill | Installs | Use For |
|---|---|---|
| integrate-revenuecat | 1,191 | End-to-end integration: creates the project, app and public API key through the MCP server or `rc` CLI, then installs and configures the Purchases SDK. |
| revenuecat-paywall | 1,185 | Displays a RevenueCat paywall inside the app with the RevenueCatUI SDK, including the presentation entry point. |
| revenuecat-purchase-flow | 1,085 | Implements the purchase and restore flow: buy a package, restore purchases, handle the result states. |
| revenuecat-testing-setup | 1,000 | Builds a testing environment for purchases without charging real money, including test store configuration. |
| create-revenuecat-project | 977 | Creates a complete project from scratch: apps, products, entitlements, offerings and packages, then returns the API keys. |
| revenuecat-troubleshoot | 969 | Diagnoses integration faults by inspecting dashboard configuration through the MCP server. |
| revenuecat-entitlements-gate | 940 | Checks whether a user currently holds a paid feature via entitlements, and gates a UI path on the answer. |
| revenuecat | 931 | Catch-all for RevenueCat work the specific skills do not cover. |
| revenuecat-status | 928 | Summarizes project configuration: apps, products, entitlements and offerings in one pass. |
| revenuecat-identify-user | 883 | Ties RevenueCat identity to the app's own auth system so purchases attach to the right account. |
| revenuecat-charts | 837 | Answers data questions by querying revenue, conversion and retention charts and reporting the KPIs behind them. |
| revenuecat-customer-center | 801 | Adds the Customer Center self-service subscription management surface to an app. |
| revenuecat-migrate | 783 | Migrates from raw StoreKit or Google Play Billing, or upgrades the SDK across a major version. |
| rc-webhooks | 734 | Consumes RevenueCat webhooks on a backend, including request authentication and event handling. |
| revenuecat-store-state | 732 | Inspects or changes the state of products in App Store Connect and Google Play Console. |
| rc-security | 725 | Hardens an Android integration: Trusted Entitlements response validation and related checks. |
| rc-subscriptions | 721 | Models subscriptions through RevenueCat's Android object model: Offerings, Packages, Products. |
| rc-setup | 713 | Sets up a RevenueCat project for Android specifically, including app creation and store credentials. |
| rc-backend | 711 | Backend reads and writes of RevenueCat state on Android. |
| rc-configuring-the-sdk | 709 | Adds and configures the RevenueCat Android SDK, including artifact and dependency wiring. |

Fourteen skills sit in the cross-platform `revenuecat` plugin and six in `revenuecat-play-billing`. The split matters when you install: a Claude Code or Cursor user gets both plugins and can choose, while the Gemini extension and the `npx skills` route take the cross-platform skills only. The Android billing depth is not in the default install.

Read down the table and the dependency order is visible. Project creation precedes SDK configuration, SDK configuration precedes the purchase flow, the purchase flow precedes the paywall, and everything precedes the charts that prove it worked.

## Why This Matters for Hermes Agents

Subscription code is a place where a plausible implementation costs money. An entitlement identifier that differs by one character from the dashboard leaves users who paid without access. A purchase flow that skips `restorePurchases` passes every manual test on a fresh install and fails every user who reinstalls. A price hard-coded into the client instead of read from an offering breaks silently when pricing changes.

These skills encode those as ordered steps with named preconditions. `create-revenuecat-project` exists so an agent does not improvise a project layout, and `revenuecat-entitlements-gate` is separate from `revenuecat-paywall` so that gating a feature and drawing a paywall stay distinct operations, which is how production subscription apps actually behave.

The appeal for an agent workflow is that the same session can hold both halves. The MCP server reaches the RevenueCat dashboard, the skills reach the codebase, and a question like "why does this user not have access" can be answered by checking the entitlement in the dashboard and the gate in the app rather than guessing at one.

Two properties need saying plainly. The skills write application code with session permissions, and they touch a payment path, which means a bad edit is a revenue incident rather than a broken build. And the OAuth grant covers every project in the account, so the blast radius of an agent mistake is the organization, not one app.

## Usage

| You say | What happens |
|---|---|
| "Set up RevenueCat for this app" | Project creation runs first, producing apps, products, entitlements, an offering and the public API keys, then the integration skill installs and configures the Purchases SDK |
| "Put the pro features behind a paywall" | The entitlement gate adds the access check at the render path, and the paywall skill draws the RevenueCatUI surface for users who fail it |
| "Why does this account not see the paid plan?" | Troubleshoot inspects dashboard configuration through the MCP server, then the entitlements skill checks the gate in code, and the two answers are compared |
| "Add subscription management to settings" | Customer Center adds the self-service surface for plan changes, cancellations and refunds without building that UI |
| "How is revenue trending this month?" | Charts queries the revenue and conversion charts and reports the KPI values behind them rather than a narrative |
| "Migrate us off StoreKit" | The migration skill walks the move to RevenueCat, keeping the receipt and transaction handling intact |
| "Test purchases without charging a card" | Testing setup configures a test environment and test store so the flow can be exercised end to end |

## Verification

Each cross-platform listing resolves to a raw `SKILL.md` one directory below `revenuecat/skills/`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/revenuecat/ai-toolkit/main/revenuecat/skills/integrate-revenuecat/SKILL.md | head -5
```

It should open with frontmatter holding `name: integrate-revenuecat` and a folded description beginning `End-to-end RevenueCat integration`, followed by the delimiter and the instruction body. The Android skills live at a parallel path under `revenuecat-play-billing/skills/<name>/SKILL.md`.

After an install, confirm the skill landed as a directory holding `SKILL.md`:

```bash
ls -d ~/.claude/skills/*/ | head -20
test -f ~/.claude/skills/revenuecat-paywall/SKILL.md && echo ok
```

The plugin route keeps its bundle in the plugin cache instead, so use the `/plugin` listing for that install and the directory check for the `npx skills` route.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| integrate-revenuecat | Pass | Pass | Warn |
| revenuecat-paywall | Pass | Pass | Pass |
| revenuecat-purchase-flow | Pass | Pass | Pass |
| revenuecat-testing-setup | Pass | Pass | Pass |
| create-revenuecat-project | Pass | Pass | Pass |
| revenuecat-troubleshoot | Pass | Pass | Pass |
| revenuecat-entitlements-gate | Pass | Pass | Pass |
| revenuecat | Pass | Pass | Pass |
| revenuecat-status | Pass | Pass | Pass |
| revenuecat-identify-user | Pass | Pass | Pass |
| revenuecat-charts | Pass | Pass | Pass |
| revenuecat-customer-center | Pass | Pass | Pass |
| revenuecat-migrate | Pass | Pass | Warn |
| rc-webhooks | Pass | Pass | Warn |
| revenuecat-store-state | Pass | Pass | Pass |
| rc-security | Pass | Pass | Pass |
| rc-subscriptions | Pass | Pass | Pass |
| rc-setup | Pass | Pass | Pass |
| rc-backend | Pass | Pass | Warn |
| rc-configuring-the-sdk | Pass | Pass | Pass |

Agent Trust Hub and Socket pass all 20 listings. Snyk warns on four: `integrate-revenuecat` (the one skill that stands up a whole project), `revenuecat-migrate`, `rc-webhooks` and `rc-backend`. No listing fails a scanner, which is why the tier is solid rather than experimental.

The scanner verdicts score skill files, not the code an agent writes while following them. Three properties need your own review. First, `revenuecat-store-state` reads and changes product state in App Store Connect and Google Play Console, which is a production action on a store listing. Second, the OAuth grant is per account and covers every project, so scope it by authorizing a session dedicated to one app. Third, `rc-webhooks` operates on a backend endpoint that receives subscription events, and a misconfigured handler that trusts unsigned payloads lets anyone grant themselves entitlement.

## Limitations

- Snapshot data, verified 2026-11-10: 17,555 combined installs across 20 indexed listings; 79 GitHub stars; MIT license for the main plugin, Apache 2.0 for the synced Android billing plugin; last pushed 2026-11-09. Counts drift over time.
- The skills.sh source page renders 20 listings, and this guide covers that rendered set. The tree carries 46 `SKILL.md` files across two plugin trees, so the index is a subset rather than the whole toolkit.
- The `npx skills add` route installs skill text only. Dashboard-side skills call MCP tools that do not exist until the RevenueCat MCP server is configured, and the failure looks like an agent improvising rather than an error.
- The Android billing skills are synced from a separate repository. When the upstream changes, this copy can lag, and the README is the only place that discloses the sync.
- Nothing here tests a real purchase end to end. The testing skill sets up a sandbox; verifying that a paid user actually receives entitlement still requires a store sandbox account and a human.
- Store Console access through `revenuecat-store-state` changes live product configuration and has no undo of its own.

## Related

- [Superwall Skills - iOS Paywall Setup](/hermes/skills/catalog/superwall-skills-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [Stripe Link CLI Skills - Agent Payments Setup](/hermes/skills/catalog/stripe-link-cli-setup)

## Pro Tips

- Ask for the project status before any change. `revenuecat-status` costs one turn and shows whether the apps, products and offerings already exist, which prevents a second set of identifiers being created beside the first.
- Pin the entitlement identifiers in the prompt. Give the agent the exact string from the dashboard rather than a description, because the skills will happily create a new entitlement that reads almost the same.
- Install `revenuecat-play-billing` only when you ship Android. On an iOS-only product it adds six skills about Google Play behaviour that nothing in your codebase will call.
- Keep the dashboard-side and the code-side work in separate sessions when the change is large. One session that creates products and edits the purchase flow produces a diff you cannot review in one pass.
- Run the migration skill on a branch and read the receipt-handling diff yourself. That is the one skill where a plausible-looking change silently stops restoring purchases for existing users.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
