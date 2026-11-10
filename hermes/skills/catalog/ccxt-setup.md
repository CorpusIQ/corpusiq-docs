---
title: "CCXT Skills - Unified Crypto Exchange API Setup"
description: "CCXT on skills.sh: 4.8K combined installs; per-language skills plus the official MCP server for 100+ exchange APIs"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ccxt-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "ccxt", "crypto", "market data", "mcp"]
---

# CCXT Skills - Setup Guide

**Source:** [ccxt/ccxt](https://www.skills.sh/ccxt/ccxt) via skills.sh - 4.8K combined installs across 12 indexed listings (4,794 exact); first seen 2026-11-10 (Nov 10, 2026 sweep)
**GitHub:** 44,846 stars, MIT license, `master` branch, last pushed 2026-11-10, 25 `SKILL.md` files, with skill directories at `.claude/skills/<name>/` and a second set under `.agents/skills/`
**Category:** Market data and trading: exchange APIs, WebSocket streams, order execution, MCP server
**Quality Tier:** 🟡 Solid with caveats - the project is heavily maintained and all 12 listings pass Agent Trust Hub, but Socket warns on six and Snyk on eleven, and the trading skills can move real money.

CCXT is the longest-running library in crypto market access: a single interface over more than a hundred exchange APIs in eight languages. The repository carries 44.8K stars, is pushed to daily, and ships agent skills as a first-class artefact rather than an afterthought. The README's own section on AI skills names the clients it supports, and a separate section documents the official MCP server that runs locally over stdio so API keys never reach the model.

The 12 indexed listings are one skill per language, plus three narrower entries. `ccxt-python`, `ccxt-typescript`, `ccxt-cli`, `ccxt-go`, `ccxt-csharp`, `ccxt-php`, `ccxt-java` and `ccxt-rust` each cover the same surface for their language: install the package, connect to an exchange, fetch market data, place and cancel orders, handle rate limits and pagination. `new-exchange` scaffolds a new exchange integration against the certified-exchange template. `ccxt-mcp` documents the MCP server. The two `binance` listings are newer companions under `.agents/skills/` that drive `binance-cli` and a Binance wallet flow.

The interesting design decision is that the skills are language skills, not task skills. There is no "build a portfolio rebalancer" skill. The agent gets the library's real API surface for the language in front of it, and the composition is left to the prompt.

## Installation

The README documents the skills install in one line:

```bash
npx skills add ccxt/ccxt
```

That pulls the skill set, and individual listings install by name:

```bash
npx skills add ccxt/ccxt --skill ccxt-python
```

The library itself is a normal package install per language, and the README carries each one. Python and JavaScript are the two most-used paths:

```bash
pip install ccxt
npm install ccxt
```

For Go, the README uses the module path directly:

```bash
go install github.com/ccxt/ccxt/go/v4@latest
```

The CLI is a separate npm package, which is the listing most useful to an agent that should not be writing library code at all:

```bash
npm install -g ccxt-cli
```

The MCP server is the third route and the one that fits an agent host best. It runs locally over stdio, so keys stay on the machine and the model references accounts by name:

```bash
claude mcp add ccxt \
-- npx -y ccxt-mcp
```

The README is explicit that trading, withdrawals and raw endpoint access are separate opt-in capability tiers, off by default, behind confirmation flows, notional caps and an audit journal. Leave them off until you have read the skill that turns them on.

## What It Provides

Six listings clear the 150-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| ccxt-python | 2,259 | Python access to 100+ exchanges: REST and WebSocket, market data, order placement, pagination and rate-limit handling. |
| ccxt-typescript | 913 | The same surface for TypeScript and JavaScript in Node.js and the browser. |
| ccxt-cli | 669 | Drives exchanges from the shell through `ccxt-cli`, which lets an agent trade and query without writing application code. |
| ccxt-go | 220 | CCXT for Go developers, REST and WebSocket. |
| ccxt-csharp | 198 | CCXT for C# and .NET developers, REST and WebSocket. |
| ccxt-php | 191 | CCXT for PHP developers, REST and WebSocket. |

The remaining 6 indexed listings range from 1 to 130 installs: `new-exchange` (130), `ccxt-java` (102), `ccxt-mcp` (70), `ccxt-rust` (40), and the two `binance` companions at 1 each.

The install distribution is honest about how people work. Two thirds of the installs sit on Python and TypeScript, and the remaining language skills exist for parity rather than adoption. If you are choosing a language for a new agent tool, the install counts point at the two that carry the most current documentation inside the skill.

`ccxt-mcp` sitting at 70 installs against 4,000 for the language skills is the most useful signal on the page. The MCP route is the newest and least adopted, and it is the one that removes the most work from an agent session.

## Why This Matters for Hermes Agents

Exchange APIs are hostile to improvisation. Each one names the same concept differently, rate limits differ per endpoint, pagination is cursor-based on some venues and page-based on others, and an order request that is nearly right is rejected with a message that does not say which field was wrong.

CCXT's value to an agent is that it collapses that variance into one call surface, and the skills describe the surface rather than the venues. An agent that knows `fetchOHLCV` and `createOrder` and the unified symbol format can work against any of the hundred exchanges without learning each dialect.

The CLI and MCP routes matter more for Hermes than the library skills. A skill that teaches an agent to write Python is useful in a coding session. `ccxt-cli` and `ccxt-mcp` let the same agent answer a market-data question in a session where nobody is writing code, which is the common case for a chat-driven operator workflow.

The risk is concentrated in one place. These skills can place orders and, if the opt-in tiers are enabled, withdraw. The README's default is deliberately conservative, and the skills inherit that posture only if you do not flip the capability tiers while debugging.

## Usage

| You say | What happens |
|---|---|
| "What is the spread on BTC/USDT right now?" | The Python or CLI skill fetches the ticker through the unified symbol format and reports bid, ask and last |
| "Pull daily candles for the last 90 days" | `fetchOHLCV` with the exchange, symbol and timeframe, returning a normalised OHLCV series regardless of venue |
| "Compare fees across three exchanges" | The skill fetches market metadata per exchange and reports taker and maker fees from the unified structure |
| "Place a limit order but do not execute" | Order construction runs against the sandbox or a dry path, and the README's capability tiers decide whether execution is even available |
| "Add support for a new exchange" | `new-exchange` scaffolds an integration against the certified-exchange template, walking the required methods |
| "Let my agent read balances" | The MCP server exposes balances read-only while trading and withdrawal tiers stay off |

## Verification

Each language listing resolves to a raw `SKILL.md` one directory below `.claude/skills/`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/ccxt/ccxt/master/.claude/skills/ccxt-python/SKILL.md | head -5
```

It should open with frontmatter holding `name: ccxt-python` and a description beginning `CCXT cryptocurrency exchange library for Python developers`, then the delimiter and the instruction body. The two Binance companions live under `.agents/skills/<name>/SKILL.md` instead, so check the tree path before writing a URL by hand.

After an install, confirm the skill landed as a directory holding `SKILL.md`:

```bash
ls -d ~/.claude/skills/*/ | head -20
test -f ~/.claude/skills/ccxt-python/SKILL.md && echo ok
```

If you took the MCP route, verify the server registers rather than trusting the add command:

```bash
claude mcp list | grep -i ccxt
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ccxt-python | Pass | Warn | Warn |
| ccxt-typescript | Pass | Pass | Warn |
| ccxt-cli | Pass | Warn | Warn |
| ccxt-go | Pass | Pass | Warn |
| ccxt-csharp | Pass | Warn | Warn |
| ccxt-php | Pass | Pass | Warn |
| new-exchange | Pass | Pass | Pass |
| ccxt-java | Pass | Warn | Warn |
| ccxt-mcp | Pass | Pass | Warn |
| ccxt-rust | Pass | Warn | Warn |
| binance | Pass | Pass | Warn |
| binance-agentic-wallet | Pass | Warn | Warn |

Agent Trust Hub passes all 12. Socket warns on six and Snyk on eleven of twelve, leaving `new-exchange` as the only listing with three clean verdicts. The warnings concentrate on the skills that describe network calls to exchanges and on the ones that handle credentials, which is the expected shape for this kind of package rather than a specific defect.

The scanner scores the skill text. What it cannot score is the decision to enable trading. The README's capability tiers, confirmation flows and notional caps are the actual control, and they default to off; an operator who turns them on for a debugging session has removed the only guardrail between a confused prompt and a filled order.

Keys are the second exposure. The MCP route keeps them local by design, and the library skills assume keys arrive through environment variables or a config file. Never paste an exchange key into a prompt, and give each agent a sub-account with withdrawals disabled rather than the trading account you use yourself.

## Limitations

- Snapshot data, verified 2026-11-10: 4,794 combined installs across 12 indexed listings; 44,846 GitHub stars; MIT license; last pushed 2026-11-10. Counts drift over time.
- Installs are concentrated: two listings carry 3,172 of the 4,794 combined installs. The language parity skills are recent additions with thin adoption, so their depth varies.
- The skills are API-surface references, not workflow guides. Nothing here sequences a strategy, sizes a position or explains a risk model; that is left to the prompt.
- Trading and withdrawal capability is opt-in and off by default. Enabling it is a configuration decision made outside the skill, and no listing tells you the notional caps in force.
- The two `binance` listings live under a different directory (`.agents/skills/`) and one of them requires authentication before it does anything useful, which is not apparent from its install count.
- Exchange APIs change without notice. A skill that documents a venue's parameter set today can be stale next month, and the library version in use decides which behaviour you actually get.

## Related

- [Binance Skills Hub - Crypto Trading Skills Setup](/hermes/skills/catalog/binance-skills-hub-setup)
- [OKX CEX Agent Skills - Exchange Trading Suite Setup](/hermes/skills/catalog/okx-cex-agent-skills-setup)
- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)

## Pro Tips

- Start with `ccxt-mcp` if the agent only needs to answer questions. It removes the whole code-writing step and keeps keys out of the transcript.
- Read the capability tier section of the README before the first trading session, not after. The default is safe; the failure mode is an operator who turns everything on to test one call.
- Use `ccxt-cli` for exploration. `ccxt-cli markets --exchange kraken` answers a venue question in one command, where the library skill would have the agent write a script.
- Check the exchange-specific section of the skill before composing an order. The unified surface hides a lot, and the per-venue notes are where the exceptions live.
- Keep one skill per session. Loading Python and TypeScript variants together invites the agent to mix idioms from both into a single snippet.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
