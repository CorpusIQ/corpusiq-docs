---
title: AngelOne MCP - Indian Market Trading and Portfolio Data
description: "Python MCP server wrapping Angel One's SmartAPI with 32 tools for trading, portfolio, market data, GTT rules, and margin across Indian markets, with TOTP login and rate-limit pacing."
category: Finance
stars: n/a (new listing, pyalgobot/angelone-mcp)
added: 2026-08-29
source: mcpservers.org /all page 2
relevance: ★★
tags: [mcp-server, trading, portfolio, market-data, indian-markets, smartapi, options, self-hosted]
---

# AngelOne MCP

**A Python MCP server wrapping Angel One's SmartAPI - trading, portfolio, market data, GTT rules, and margin/brokerage - so any MCP client can query an account and place orders through natural conversation.** Thirty-two tools cover the documented SmartAPI surface, with TOTP login, automatic re-login on token expiry, and self-pacing against the broker's rate limits. Apache-2.0 licensed.

```
Server type: Local (Python, stdio)
Auth: SmartAPI API key + TOTP base32 secret (Angel One trading account required)
Endpoint: n/a (local; talks to Angel One SmartAPI)
Tools: 32 (orders, positions, holdings, GTT, options, market data, margin)
Pricing: Free open source; broker charges are your own account
Category: Finance / Trading
Built by: pyalgobot/angelone-mcp; Apache-2.0
```

## Why This Matters for Operators

Indian-market traders and operators monitor positions, options Greeks, and order books across the NSE and BSE, and the broker's own interfaces are built for clicking, not asking. This server puts the whole SmartAPI surface behind 32 typed tools, so an agent can answer "what is my exposure across holdings" or "where are my open GTT rules" in one conversation, with the warning built into the README: it places real orders on a real account, and test quantities first.

The TOTP handling is the notable engineering: the login flow uses the base32 secret behind the authenticator (not the six-digit code), so the client can self-heal expired tokens without a human in the loop - the reason most broker integrations die quietly.

**The full Angel One account surface - orders, Greeks, GTT, margin - becomes 32 agent tools with self-healing TOTP login.**

## Tools & Capabilities

| Area | Tools |
|---|---|
| Auth & account | login, logout, get_profile, get_margin, get_rms_limit |
| Orders | place_order, modify_order, cancel_order, get_order_book, get_trade_book, get_individual_order_details |
| Portfolio | get_positions, get_holdings, get_all_holdings, convert_position |
| GTT rules | gtt_list, gtt_details, gtt_create_rule, gtt_modify_rule, gtt_cancel_rule |
| Market data | get_ltp, get_market_quote, get_candle_data, get_nse_intraday_data, get_bse_intraday_data, search_scrip, get_gainers_losers |
| Options & derivatives | get_oi_data, get_oi_buildup, get_put_call_ratio, get_option_greeks |
| Charges | estimate_charges (brokerage estimator) |

## Installation

```bash
pip install -r requirements.txt
python -m angelone_mcp.server
```

Prerequisites: an Angel One trading account with SmartAPI access, a SmartAPI app (for the API key), and the TOTP base32 secret from the authenticator setup. The repo documents per-client MCP config (Claude Desktop, Claude Code).

## Configuration

```json
{
  "mcpServers": {
    "angelone": {
      "command": "python",
      "args": ["-m", "angelone_mcp.server"],
      "env": {
        "SMARTAPI_API_KEY": "your-key",
        "SMARTAPI_CLIENT_CODE": "your-client-code",
        "SMARTAPI_TOTP_SECRET": "your-base32-secret"
      }
    }
  }
}
```

Keep the TOTP secret out of version control and chat logs - it is account-equivalent. The client auto-relogs on token expiry and paces requests against SmartAPI's documented limits.

## Business Relevance

- **Traders** read positions, Greeks, and OI data in conversation instead of broker screens.
- **Operators with Indian market exposure** get portfolio and margin answers from an agent with a documented, self-healing login.
- **Algo-curious teams** prototype order flows through MCP tools before committing to a custom integration.
- **Researchers** pull candles, quotes, and gainers/losers across NSE and BSE with one toolset.

## Integration with CorpusIQ

AngelOne MCP extends the catalog's regional finance coverage: where CorpusIQ connectors hold the business books (QuickBooks, Stripe), this server holds the brokerage account surface, so a CorpusIQ-driven workflow can reconcile market exposure against business cash position in one agent pass. For operators with Indian operations, the combination reads both the ledger and the live broker state, and the GTT and margin tools give the agent the same visibility the operator gets on the broker console.

## Limitations

- Brand new - first sweep August 29, 2026; zero-star repo, single maintainer.
- Real-order capability - the README's own warning; test with small quantities and respect the no-undo reality of filled orders.
- Requires an Angel One account with SmartAPI access and TOTP setup - onboarding is account-heavy.
- Indian markets only (NSE/BSE via Angel One); not a multi-broker or multi-market tool.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Hermes Plant MCP Server - Deterministic Finance and Quant APIs](/docs/hermes/mcp/servers/external/hermesplant-mcp-server)
- [Equibles MCP - SEC Filings and Market Data for AI Agents](/docs/hermes/mcp/servers/external/equibles-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
