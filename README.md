# CorpusIQ Documentation

![tokens saved (est.)](https://img.shields.io/endpoint?url=https%3A%2F%2Fmcp2.corpusiq.io%2Fapi%2Fv1%2Fusage%2Fpublic-counter%3Fformat%3Dshields&style=flat-square&logo=anthropic&logoColor=white)

CorpusIQ is the live-data brain you plug into Claude or ChatGPT. Connect the
tools you already pay for — QuickBooks, Shopify, Klaviyo, Google Ads, GA4,
HubSpot, Slack, Gmail, and 35+ more — then ask plain-English questions and get
real answers grounded in your own data.

This is the working documentation. Not a sales pitch. If you're trying to get
set up, run a useful prompt, or fix a broken connector, you're in the right
place.


## See It In Action

**MCP device login — 45 seconds, production server:**

https://github.com/CorpusIQ/corpusiq-docs/blob/main/assets/mcp-device-login-demo.mp4

Connect your AI agent to 36+ business data sources via a live MCP endpoint.  
Five steps. Any MCP client. OAuth 2.0 device flow — no browser required.


## 30-second pitch

You connect your business data sources once. From then on, when you ask Claude
or ChatGPT "how healthy is my business?" or "what's blocking our cash flow?",
the assistant pulls the answer from your actual books, your actual orders, your
actual ad accounts. No more copy-pasting CSVs. No more "I can't see that data."

CorpusIQ is read-only. We never write to your systems.

## Start here

**Choose your path:**

| I want to... | Go here |
|---|---|
| Chat with AI about my business data | [AI Chat Users](docs/ai-chat-users.md) — demo.corpusiq.io |
| Connect my AI agent via MCP | [AI Agent Users](docs/ai-agent-users.md) — direct MCP connection |
| See which agents work | [Supported AI Agents](docs/supported-agents.md) — Hermes, Claude, Cursor, more |

**Quick links:**

- **New?** Walk the [Quickstart](quickstart/) — five short pages, ~10 minutes.
- **Want to see what it can do?** Browse the [Prompts library](prompts/) —
  60+ copy-paste prompts ranked by business impact.
- **Need to connect a specific tool?** Jump to the [Connectors index](connectors/).
- **Building an agent or CLI tool?** See [Direct MCP Connection](https://www.corpusiq.io/mcp/direct-connection) — device login, no browser required, works with LangChain, AutoGen, llama.cpp, any MCP client.
- **Something's broken?** Try [Troubleshooting](troubleshooting/).
- **Curious how the magic works?** [How it works](how-it-works/) explains the
  connectors and skills engine in plain English.
- **Want to see what's coming?** Check the [Roadmap](roadmap/) and the
  [Changelog](changelog/).
- **Got an idea or a question?** Join the [Community](community/).

## Direct connection (CLI / agents / CI)

If your tool can't open a browser, use **OAuth 2.0 Device Authorization Grant**:

```bash
# 1. Get a device code
curl -s -X POST https://mcp2.corpusiq.io/oauth/device/authorize

# 2. Open the verification_uri, enter the user_code (once)

# 3. Poll for the token
curl -s -X POST https://mcp2.corpusiq.io/oauth/token \
  -d "grant_type=urn:ietf:params:oauth:grant-type:device_code&device_code=<device_code>"

# 4. Use the token
curl https://mcp2.corpusiq.io/mcp \
  -H "Authorization: Bearer <access_token>"
```

MCP config block (paste into any MCP client):

```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "authorizationUrl": "https://www.corpusiq.io/mcp-auth"
    }
  }
}
```

Python device login helper (zero deps beyond `requests`): [corpusiq.io/mcp/direct-connection](https://www.corpusiq.io/mcp/direct-connection)

**Two prerequisites:** a CorpusIQ account + connectors authorized in the dashboard. The token only reaches connectors already linked.

## What's in here

| Section | What it is |
|---|---|
| [quickstart/](quickstart/) | Sign up → connect Claude/ChatGPT → first connector → first prompt |
| [prompts/](prompts/) | Curated prompts grouped by category — finance, marketing, CRM, ecommerce, SEO, multi-source |
| [connectors/](connectors/) | One page per connector: what it unlocks, how to authenticate, what data it sees |
| [how-it-works/](how-it-works/) | The substrate — connectors, skills engine, privacy posture |
| [troubleshooting/](troubleshooting/) | Common failure modes and fixes |
| [roadmap/](roadmap/) | What we're building, what's planned, what's parked |
| [changelog/](changelog/) | What shipped, in plain language |
| [docs/onboarding/](docs/onboarding/) | Step-by-step setup guides for AI chat and AI agent users |
| [docs/architecture/](docs/architecture/) | System architecture, MCP endpoint, connector layer |
| [docs/security/](docs/security/) | Authentication, encryption, audit, best practices |
| [docs/search/](docs/search/) | Search capabilities and cross-source queries |
| [docs/reporting/](docs/reporting/) | Reporting workflows and data export |
| [docs/governance/](docs/governance/) | MSR source of truth, validation, reconciliation |
| [community/](community/) | Request connectors, ask questions, follow releases |

## A note on voice

Adam, our prototype user, is a SaaS founder. He's sharp, he's busy, and he's
allergic to slogans. The docs are written for him. If you see a step that
reads like marketing copy, file a bug.

Powered by CorpusIQ.

## Topics

`mcp` `model-context-protocol` `ai-connectors` `business-intelligence` `claude` `chatgpt` `shopify` `quickbooks` `google-analytics` `hubspot` `stripe` `ai-agents` `llm-tools` `operator-tools` `saas`
