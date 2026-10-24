---
title: "Solana Mobile Skills - Android Wallet Dev Setup"
description: "Solana Mobile: 64.6K combined installs. Seven skills for Android wallet integration, .skr domains, Seeker gating and dApp Store publishing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/solana-mobile-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "solana", "android", "mobile wallet"]
---

# Solana Mobile Skills - Setup Guide

**Source:** [solana-mobile/solana-mobile-skills](https://www.skills.sh/solana-mobile/solana-mobile-skills) via skills.sh - 64.6K combined installs across 9 indexed listings; repository active since January 2026, new to this catalog in the Oct 24, 2026 sweep

**GitHub:** [solana-mobile/solana-mobile-skills](https://github.com/solana-mobile/solana-mobile-skills) - 8 stars, Apache-2.0, last pushed 2026-10-21, branch main, 7 skill directories under `skills/` each with its own `references/` folder

**Category:** Blockchain / Solana Mobile Development

**Quality Tier:** 🟡 Beta - official Solana Mobile repository under Apache-2.0 with CI validation and seven self-contained skills, but a small star count and two Snyk warnings on the money-path listings

Solana Mobile maintains the Android side of the Solana ecosystem: the Mobile Wallet Adapter standard, the Seeker phone, and the dApp Store. This repository is that team's own agent skill set, and it covers the whole path from an empty project to a published release APK, with .skr naming, Seeker device gating and Privy login as the branches most apps need.

What makes it interesting for an agent is the shape rather than the install count. Every skill is a self-contained directory with a short procedure in `SKILL.md` and the long-form detail pushed into `references/` that the agent loads only when the task reaches it, which keeps activation cheap. The README states the portability rules the repo enforces in CI: frontmatter `name` matches the directory, relative links never escape the skill folder, no host-specific tool names in prose, `SKILL.md` under 500 lines. That is a cleaner distribution contract than most suites ship.

It is also narrow on purpose. Mobile and Seeker work only. General Solana program development belongs to the Solana Foundation's `solana-dev` skill, which `npx solana-mobile@latest create` installs into every scaffolded project, so the two sit side by side instead of overlapping.

## Installation

The README uses the `skills` installer, the same one the scaffolder calls:

```bash
npx -y skills add solana-mobile/solana-mobile-skills
```

That prompts for which skills and which agents. To take everything without prompts:

```bash
npx -y skills add solana-mobile/solana-mobile-skills --all
```

The useful flags, all from the README:

```bash
npx -y skills add solana-mobile/solana-mobile-skills -l          # list without installing
npx -y skills add solana-mobile/solana-mobile-skills -g          # install globally
npx -y skills add solana-mobile/solana-mobile-skills -s solana-mobile-wallet
```

Skills land in `.agents/skills/`, which most agents read directly, and are symlinked into the agent-specific locations that need it. A `skills-lock.json` records the source and a content hash per skill, so an install is reviewable in a diff. Installing by hand also works: copy any `skills/<name>/` directory into your agent's skills directory, because each one is self-contained.

The repository is additionally packaged as an Agent Plugin: the root `plugin.json` manifest against the Agent Plugins schema plus the `skills/` directory, so schema-aware clients can load it as a plugin.

Requirements the README states plainly: an Expo React Native project, a development build (Expo Go does not work), and an Android development environment. `npx solana-mobile@latest doctor` checks the toolchain.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| integration-privy | 10,646 | Privy authentication layered on Mobile Wallet Adapter through Sign-In-With-Solana: installing `@privy-io/expo`, mounting the provider, `useLoginWithSiws`, linking a wallet to an existing Privy account and reading the access token server-side. |
| solana-mobile | 10,586 | Project scaffolding and the `solana-mobile` CLI: `create` from the template catalog, `doctor` for the Android toolchain, `emu` for emulators, `device` for connected hardware, `localnet` for a validator the phone can reach and `playground` to exercise a wallet without an app. |
| solana-mobile-wallet | 10,583 | Mobile Wallet Adapter in React Native: connect and disconnect, show the connected address, sign messages, Sign-in-with-Solana, transfer SOL and send any transaction, with the kit and web3.js stacks kept apart. |
| seeker-genesis-token | 10,576 | Seeker device ownership checks: verifying the Seeker Genesis Token with Sign-in-with-Solana plus server-side verification, gating rewards, anti-Sybil checks and one-claim-per-device logic. |
| seeker-domains | 10,574 | `.skr` naming in both directions: resolving a domain to an address, reverse-looking up an address to a domain, validating input, and showing names instead of addresses in profiles, friend lists and history. |
| seeker-connect | 5,915 | Seeker Connect for Expo, Kotlin and web dapps: registering the Wallet Standard wallet, the `seeker-connect-button` element, the `SeekerConnectButton` native view, the Nostr relay for `relayDomain`, and `SeekerConnectError` codes such as `association-failed`. |
| solana-mobile-publishing | 5,674 | Release path for the dApp Store: signing a release APK, first-time publishing, shipping an update, publisher account and App NFT setup, and debugging a release build that works in debug. |

The remaining 2 indexed listings carry 10 installs each, `skr-address-resolution` and `genesis-token`, and neither has a directory in the current `skills/` tree.

## Why This Matters for Hermes Agents

Wallet work is the part of mobile development where an agent can do real damage, and it is also the part where documentation goes stale fastest, because it moves with the chain, the client library and the store. These skills are written as procedures rather than prose: the agent reads the procedure, calls the CLI, and the reference file loads only if the task reaches a signature or a publishing step.

The strongest structural detail is that the skills read `package.json` before writing wallet code. Two client stacks coexist in this ecosystem, `@wallet-ui/react-native-kit` with `@solana/kit` as the current default and `@wallet-ui/react-native-web3js` with `@solana/web3.js` as the legacy path, and their provider props, hook return values and transaction construction all differ. An agent that mixes them produces code that compiles and fails at runtime, so a suite that checks first removes a whole failure class.

The Seeker skills are the ones with no substitute. Device ownership verification through the Seeker Genesis Token, `.skr` resolution in both directions and Seeker Connect for a dapp that runs in the phone's browser are specific to this platform and not documented as agent procedures anywhere else.

The honest limit is that this suite is younger than its installs suggest: eight stars, one organization behind it, no third-party ecosystem yet. Install it for the procedures, keep the release and money paths supervised, and treat the Snyk warnings on the two signing skills as the reason to prove flows on a test build first.

## Usage

| You say | What happens |
|---|---|
| "Create a new Solana mobile app" | The solana-mobile skill scaffolds from the template catalog with `npx solana-mobile@latest create`, then runs `doctor` to check the Android toolchain. |
| "Add a connect wallet button to my Expo app" | The solana-mobile-wallet skill reads `package.json` to pick the kit or web3.js stack, then wires Mobile Wallet Adapter connect, address display and disconnect. |
| "Send SOL from my React Native app" | The same skill builds and sends the transfer through the adapter, and needs a connected wallet session before the signature. |
| "Gate this screen to Seeker owners" | seeker-genesis-token verifies the Seeker Genesis Token with Sign-in-with-Solana and a server-side check before the gate opens. |
| "Show .skr names instead of wallet addresses" | seeker-domains resolves addresses to domains in the direction the screen needs and validates typed input. |
| "Add Privy login to my Solana mobile app" | integration-privy installs `@privy-io/expo`, mounts the provider and logs the user in with `useLoginWithSiws` over Mobile Wallet Adapter. |
| "Publish this build to the dApp Store" | solana-mobile-publishing signs the release APK and drives the `dapp-store` CLI through first publish or an update. |

## Verification

Confirm the layout on main before installing. Every skill in this repository uses the same one:

```bash
for p in skills/solana-mobile/SKILL.md \
         skills/solana-mobile-wallet/SKILL.md \
         skills/integration-privy/SKILL.md \
         plugin.json; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/solana-mobile/solana-mobile-skills/main/$p"
done
```

Read the two money-path procedures before granting anything, because both reach a signature:

- https://raw.githubusercontent.com/solana-mobile/solana-mobile-skills/main/skills/solana-mobile-wallet/SKILL.md
- https://raw.githubusercontent.com/solana-mobile/solana-mobile-skills/main/skills/seeker-connect/SKILL.md

Two local checks after install: the skills should appear under `.agents/skills/` (with `skills-lock.json` recording each source and hash), and `npx solana-mobile@latest doctor` should report a working Android toolchain. A `--list` install first (`npx -y skills add solana-mobile/solana-mobile-skills -l`) shows what the index resolves to without writing anything.

## Security

skills.sh verdicts for sampled skills (verified October 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| integration-privy | Pass | Pass | Pass |
| solana-mobile | Pass | Pass | Pass |
| solana-mobile-wallet | Pass | Pass | Warn |
| seeker-genesis-token | Pass | Pass | Pass |
| seeker-domains | Pass | Pass | Pass |
| seeker-connect | Pass | Pass | Warn |
| solana-mobile-publishing | Pass | Pass | Pass |

Two listings carry a Snyk warning, and both are the ones that reach a signature: `solana-mobile-wallet` connects, signs and sends, and `seeker-connect` wires a dapp to the phone's built-in wallet, which is the same authority from the other direction. Snyk records W009, direct money access, on both. The five read and setup skills pass all three auditors, including the ones that touch the toolchain and the publishing CLI.

The risk model is legible: the skills write code that asks a human to approve a transaction on the device, so the wallet is the approval surface and the agent never holds a key. Keep it that way. Prove a send flow on a test wallet or `localnet` before a real one, and keep the release signing step (`solana-mobile-publishing`) in a supervised session, because a signed APK is a distribution artifact rather than a code change.

## Limitations

- Snapshot data, verified October 24, 2026: 64,574 combined installs across 9 indexed listings; 8 GitHub stars; Apache-2.0; last pushed 2026-10-21. Counts drift over time.
- The install index outruns the tree: 9 indexed listings against 7 skill directories. `skr-address-resolution` and `genesis-token` carry 10 installs each and no directory under the current `skills/`; the commits API shows both paths last modified by the 2026-08-05 "Restructure skills and rewrite against current APIs" commit that moved every skill under `skills/`.
- Android only. iOS builds run, but they have no wallet support, so the wallet and Seeker skills do not apply there.
- Expo Go will not work. Mobile Wallet Adapter depends on native Android modules Expo Go does not bundle, which the README names as the most common cause of a wallet integration that appears broken.
- Two client stacks coexist with incompatible APIs: `@wallet-ui/react-native-kit` with `@solana/kit` is the default, `@wallet-ui/react-native-web3js` with `@solana/web3.js` is legacy. Code written for one fails silently on the other.
- The community footprint is small (8 stars, 8 forks), so the maturity comes from the maintaining organization rather than from third-party use.
- Scope stops at mobile: general Solana program work, Anchor and Pinocchio development, Codama generation and program security review belong to `solana-dev`, which the scaffolder installs alongside.

## Related

- [Solana Dev Skill - Blockchain Development Setup](/hermes/skills/catalog/solana-dev-skill-setup)
- [Callstack Agent Skills - React Native Skill Suite Setup](/hermes/skills/catalog/callstackincubator-agent-skills-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)

## Pro Tips

- Run `npx solana-mobile@latest doctor` before asking an agent to write wallet code. The toolchain check catches the missing Android SDK or emulator that otherwise shows up much later as a failed build.
- Ask for a development build explicitly. Expo Go cannot load the native modules Mobile Wallet Adapter needs, and "wallet does not connect" is almost always this.
- Install `solana-mobile-wallet` or `seeker-connect`, not both, when debugging a signing flow. They cover the same authority from different directions and the agent will pick whichever description matches first.
- Use `npx -y skills add solana-mobile/solana-mobile-skills -l` to see what the index resolves before writing anything to disk, then `-s <skill>` to install one skill at a time.
- Keep release signing supervised. `solana-mobile-publishing` produces a signed store artifact, so it belongs in a session where a human reads the output.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
