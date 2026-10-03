---
title: "MagicMarkets MCP - Sports Markets for Agents"
description: "MCP over the Magic Markets v2 API: stream live sports prices, quote selections, place and manage orders, and inspect positions."
category: "Finance"
stars: n/a (hosted platform, magicmarkets.com)
added: 2026-10-02
source: "mcpservers.org server page (magicmarkets/magicmarkets-cli)"
relevance: ★★
tags: [prediction-markets, trading, sports, api, orders, positions, stdio]
---

# MagicMarkets MCP

**Local MCP server (stdio) plus a CLI, over a hosted API** - `magicmarkets-cli` is a single static Go binary for the Magic Markets v2 API that streams live sports prices, quotes selections, places and manages orders and inspects positions, with the same API also exposed as MCP tools over stdio or the streamable HTTP transport on localhost.

```
Server type: Local (stdio, launched as a subprocess) or localhost Streamable HTTP
Auth: One API key (no request signing, no private keys)
Endpoint: local `magicmarkets mcp` subprocess
Tools: markets, offers, betslip, order and position operations
Pricing: Magic Markets account required
Category: Finance
Built by: Magic Markets (github.com/magicmarkets/magicmarkets-cli)
```

## Why This Matters for Operators

Prediction and sports markets are a data surface most business agents never reach. Magic Markets exposes live prices, priced selections, order placement and position state through one authenticated API with no request signing, so an agent can read the market and act on it inside the same workflow that reads the rest of the business.

**The delivery model is the notable part.** A single static binary means no dependency chain and no service to host; the CLI and the MCP server are the same artifact, so a script and an agent use identical commands.

## Tools & Capabilities

| Command | Purpose |
|---|---|
| `magicmarkets markets --sport <code>` | Find events with live prices |
| `magicmarkets offers <sport> <selection>` | List priced bet types for a selection |
| `magicmarkets betslip create ...` | Build a betslip and wait for quotes |
| `magicmarkets order place --betslip <id> --price <p> --stake <s>` | Place an order at a given price and stake |
| Position inspection | Inspect current positions and manage orders |

The same surface is available as MCP tools over stdio (`magicmarkets mcp` as a subprocess) or through the streamable HTTP transport on localhost.

## Installation

```bash
git clone https://github.com/magicmarkets/magicmarkets-cli
cd magicmarkets-cli
make install
```

`make where` prints the install location. If the binary is not found afterwards, add the Go bin directory to `PATH`. To install without touching `PATH`, `make build` produces `./build/magicmarkets`.

## Configuration

Authenticate with one API key; there is no request signing and no private key. Launch the MCP server as a local subprocess:

```json
{
  "mcpServers": {
    "magicmarkets": {
      "command": "magicmarkets",
      "args": ["mcp"]
    }
  }
}
```

The streamable HTTP transport is served on localhost when requested instead of stdio.

## Business Relevance

- **Analysts** read live market prices as a forecasting input alongside their usual data.
- **Quants and operators** script the CLI and the agent against the same commands.
- **Finance teams** track positions and order state without a separate dashboard.
- **Researchers** use priced selections as a probabilistic signal in market studies.

## Integration with CorpusIQ

Magic Markets adds an external market signal to the business picture CorpusIQ already assembles. An agent reading Stripe or Shopify for a merchant's trading volume can compare it against live market prices for related events, and a finance team tracking positions can log them next to the QuickBooks numbers so exposure sits in one place. One server answers "what does the market think", CorpusIQ answers "what is the business doing", and a composed workflow reconciles the two.

## Limitations

- Brand new, no track record yet.
- Requires a Magic Markets account and API key.
- Local delivery only: the CLI must run where the agent runs.
- Scope is sports and prediction markets, not general financial instruments.
- Order placement is a live, irreversible market action and should be gated in any autonomous workflow.

## FAQ

### Does MagicMarkets MCP need a private key or request signing?

No. It authenticates with one API key, with no request signing and no private keys.

### How is the MCP server delivered?

As a local subprocess. The same static binary runs the CLI and `magicmarkets mcp` for stdio, or serves the streamable HTTP transport on localhost.

### Can an agent place orders, not just read prices?

Yes, the order flow is exposed (betslip creation, price quoting and order placement), so any autonomous use should gate writes the way it would any live trading action.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
