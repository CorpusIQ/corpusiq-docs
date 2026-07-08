# MCP Security Best Practices — Read-Only, OAuth-Native, Zero Storage

Connecting business data to AI raises security questions. Here's what you need to know about MCP security — and the questions to ask any provider.

## The three pillars of MCP security

**1. Read-only by design**
The AI should query data, not modify it. This should be architectural — not a setting you can accidentally toggle. OAuth scopes should only request read access. API calls should only use GET methods. There should be no write path.

**2. OAuth-native authentication**
No API keys to manage, rotate, or leak. Each user authenticates via their own OAuth flow — the same way you log into apps with Google. Revoke access instantly from your admin console. Full audit trail of who queried what.

**3. No data storage**
Data should flow directly from source tool to AI response. Not stored. Not cached. Not used for training. When the response is generated, the data is gone. No second copy to secure.

## Questions to ask any MCP provider

| Question | Red flag if they say... |
|----------|----------------------|
| "Is it read-only?" | "You can configure it" — should be architectural |
| "Where does my data go?" | "Our servers process it" — should be direct to AI |
| "How is auth handled?" | "API keys" — should be OAuth |
| "Are you audited?" | "We're working on it" — look for CASA, SOC 2 |
| "Can I revoke access?" | "Submit a ticket" — should be instant |
| "Who sees my data?" | Any third party mentioned — should be nobody |

## CorpusIQ security

- **Read-only:** Architectural. No write path exists.
- **Auth:** OAuth-native. Per-user. Instant revoke.
- **Storage:** None. Data queried live, gone after response.
- **Certification:** CASA Tier 2, SOC 2.
- **No third parties:** Direct bridge between your tools and your AI.

---

*CorpusIQ: Secure MCP for business data. Read-only. OAuth-native. CASA Tier 2. [corpusiq.io](https://www.corpusiq.io)*
