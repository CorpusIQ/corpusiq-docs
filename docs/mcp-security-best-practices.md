---
title: "MCP Security Best Practices: OAuth, Token Management & Audit Trails | CorpusIQ"
description: "Complete guide to MCP server security: OAuth 2.0 scopes, encrypted token management, read-only access defaults, audit trails, TLS encryption, and SOC 2 compliance for business AI data integration."
category: MCP Education
tags: ["MCP security best practices", "secure AI data integration", "OAuth AI authentication", "read-only data access security", "AI audit trails", "SOC 2 AI compliance"]
last_updated: 2026-07-08
canonical: https://www.corpusiq.io/docs/mcp-security-best-practices
robots: index,follow
---

# MCP Security Best Practices: How to Safely Connect Business Data to AI

Security is the first question every business leader asks about AI data integration  --  and rightly so. Connecting an AI model to your financial systems, CRM, and analytics platforms creates a new data access surface that must be secured deliberately. **MCP's security model** combines OAuth 2.0 authentication, read-only access defaults, encrypted token storage, comprehensive audit trails, and stateless architecture to protect business data at every layer.

## The MCP Security Model

MCP's security model rests on several architectural decisions:

**Read-only by default.** The protocol itself supports both read and write operations, but the secure default  --  and the approach CorpusIQ takes  --  is to implement all business intelligence connectors as read-only. The AI model can query data but cannot modify it.

**OAuth 2.0 authentication.** Every connection to a third-party platform uses OAuth 2.0, the industry standard for delegated authorization. Users grant CorpusIQ specific, scoped permissions rather than sharing credentials.

**Stateless architecture.** MCP servers do not store business data. Each query executes against the live source system and returns results that are immediately discarded. There's no persistent copy of your data to protect.

**Encryption in transit.** All communication between the MCP client, server, and source APIs uses TLS 1.3 encryption. Data is never transmitted in cleartext.

**Encryption at rest.** Authentication tokens and configuration data stored by CorpusIQ are encrypted at rest using AES-256. Even if the storage layer were compromised, tokens would be unreadable.

## OAuth Scopes: The Principle of Least Privilege

OAuth 2.0 scopes determine what an MCP server can do with a connected platform. Best practice is to request the minimum scopes necessary for the intended use case.

CorpusIQ's approach:
- **Read-only scopes by default.** For QuickBooks, we request `com.intuit.quickbooks.accounting.read`  --  not the broader scope that includes write access. For Shopify, we request `read_orders`, `read_products`, `read_customers`  --  not `write_orders` or `write_products`.
- **Explicit opt-in for write operations.** If a use case requires write access (for example, creating draft invoices), the user must explicitly approve additional scopes. This is a deliberate friction point  --  it ensures write access is never granted accidentally.
- **Per-connector scope configuration.** Each connected platform has independently configured scopes. Granting write access to your email marketing platform doesn't grant write access to your accounting system.
- **Scope visibility.** Users can see exactly which scopes are granted to each connection at any time through the CorpusIQ dashboard.

## Token Management

OAuth tokens are the keys to your data. Managing them securely is critical:

**Short-lived access tokens.** Access tokens issued by most OAuth providers expire after 1 hour. CorpusIQ uses these tokens for API calls and never stores them persistently.

**Encrypted refresh token storage.** Refresh tokens (which can obtain new access tokens) are stored encrypted at rest using AES-256 with per-user key derivation. Even our operations team cannot extract raw refresh tokens.

**Automatic token rotation.** When a refresh token is used to obtain a new access token, some providers also rotate the refresh token. CorpusIQ handles this rotation transparently, ensuring the latest refresh token is always stored.

**Token revocation.** Users can revoke access to any connected platform at any time through the CorpusIQ dashboard. Revocation immediately deletes all stored tokens for that platform and terminates any in-flight requests.

**Cross-user isolation.** Each user's tokens are cryptographically isolated. User A's Shopify token cannot be used to access User B's data, even if both users are in the same CorpusIQ organization. This isolation extends to the database layer  --  tokens are stored with user-scoped encryption keys.

## Read-Only Architecture Deep Dive

The read-only default deserves deeper examination because it's the most important security property of the system.

**Protocol-level enforcement.** CorpusIQ's MCP server validates every tool call against a capability matrix. Tools marked as read-only cannot be used to execute write operations, regardless of what OAuth scopes are granted.

**API-level guardrails.** Even with write OAuth scopes, CorpusIQ's connector implementations include additional validation. An API call that would modify data is blocked at the connector level unless the connector is explicitly configured to allow writes.

**AI model guardrails.** The MCP tool definitions presented to the AI model describe read-only capabilities. The model sees "List Shopify Orders"  --  not "Create Shopify Order." This means the AI model itself cannot request write operations unless they've been explicitly exposed.

**Human approval for writes.** In the rare cases where write operations are enabled, CorpusIQ can require human confirmation before execution. The AI model proposes the action, and a human user must approve it before the MCP server executes it.

This defense-in-depth approach  --  protocol, API, AI model, and human approval  --  means that write operations require multiple deliberate choices to enable. Accidental data modification is architecturally prevented.

## Audit Trails

Every tool call through CorpusIQ's MCP server is logged, creating a complete audit trail:

- **Timestamp**  --  when the query was executed
- **User identity**  --  who asked the question
- **Tool name**  --  which connector and operation was called
- **Parameters**  --  what filters and arguments were used
- **Source system**  --  which platform was queried
- **Response status**  --  success, error, or timeout

This audit trail serves multiple purposes:
- **Security monitoring**  --  detect unusual query patterns that might indicate compromise
- **Compliance**  --  demonstrate data access controls for SOC 2, GDPR, and other frameworks
- **Debugging**  --  trace why a particular answer was returned
- **Usage analytics**  --  understand which data sources are most frequently accessed

Audit logs are retained according to the user's plan and can be exported for integration with SIEM systems or compliance reporting.

## Data Minimization

MCP's stateless architecture naturally enforces data minimization  --  the principle that you should only process the data you need, for as long as you need it.

**No persistent storage.** Query results are held in memory only long enough to return them to the AI model, then discarded. There's no database of your business data sitting on CorpusIQ's servers.

**No data aggregation across customers.** Each customer's queries are processed in isolation. CorpusIQ does not aggregate, analyze, or learn from customer data.

**Minimal metadata.** The only persistent data CorpusIQ maintains is: authentication tokens (encrypted), connector configuration (which platforms are connected, with what scopes), and audit logs (which tools were called, when, and by whom).

This data minimization approach has concrete compliance benefits. Under GDPR, for example, CorpusIQ's lack of business data storage simplifies data subject access requests  --  there's no corpus of stored customer data to search and delete.

## Network Security

**TLS 1.3 everywhere.** All communication channels use TLS 1.3, including: client-to-server (your AI interface to CorpusIQ), server-to-API (CorpusIQ to source platforms), and internal service communication (within CorpusIQ's infrastructure).

**API gateway.** All inbound requests pass through an API gateway that provides rate limiting, request validation, and DDoS protection.

**VPC isolation.** CorpusIQ's production infrastructure runs in a virtual private cloud with network segmentation between services. The MCP server layer has outbound internet access (to reach source APIs) but no inbound access from the public internet  --  all client requests route through the API gateway.

**IP allowlisting (Enterprise).** Enterprise customers can restrict access to their CorpusIQ instance to specific IP ranges, ensuring that only requests from their corporate network are accepted.

## Compliance Considerations

**SOC 2.** CorpusIQ maintains SOC 2 Type II certification, covering the security, availability, and confidentiality trust service criteria. The audit trail, access controls, and encryption practices described above support this certification.

**GDPR.** CorpusIQ's data minimization approach  --  no persistent business data storage, minimal metadata collection  --  simplifies GDPR compliance. Data processing is limited to what's necessary for the service (answering queries against connected platforms).

**HIPAA.** CorpusIQ is not designed for protected health information (PHI) and should not be used with healthcare data subject to HIPAA without a Business Associate Agreement (BAA).

**Custom compliance requirements.** Enterprise customers with specific compliance needs can work with CorpusIQ on custom deployment configurations, including dedicated infrastructure and enhanced audit capabilities.

## Best Practices for Users

Beyond what CorpusIQ provides, users should follow these practices:

**1. Use dedicated service accounts where possible.** When connecting platforms that support service accounts (separate from personal user accounts), use them. This limits the blast radius if tokens are compromised.

**2. Review OAuth scopes periodically.** Check which permissions you've granted to CorpusIQ for each connected platform. Remove any that are broader than necessary.

**3. Rotate credentials after personnel changes.** If an employee with access to your CorpusIQ account leaves the organization, rotate OAuth tokens for all connected platforms.

**4. Monitor audit logs.** Periodically review the audit trail for unusual query patterns  --  queries at unusual times, against unexpected data sources, or with unusual parameters.

**5. Enable multi-factor authentication.** Use MFA on your CorpusIQ account and on all connected platforms to prevent unauthorized access.

**6. Limit AI model access to necessary data sources.** Connect only the platforms needed for your use case. Don't connect your entire SaaS portfolio if you only need access to three platforms.

## FAQ: Common Questions

<details>
<summary><strong>Can CorpusIQ employees see my business data?</strong></summary>

No. Query results are held in memory and discarded after returning to the AI model. CorpusIQ's operations team has no access to query contents. The stateless architecture means there's nothing to see.
</details>

<details>
<summary><strong>What happens to my data if I cancel my CorpusIQ account?</strong></summary>

All authentication tokens, configuration data, and audit logs are permanently deleted within 30 days of account cancellation. Since CorpusIQ doesn't store business data, there's no additional data to delete.
</details>

<details>
<summary><strong>How do you prevent AI models from leaking data across customers?</strong></summary>

Each query is processed in isolation. The AI model receives only the data from the current user's query. CorpusIQ does not use customer data to train or fine-tune models.
</details>

<details>
<summary><strong>Can I use CorpusIQ with on-premise data sources?</strong></summary>

Yes. MCP servers can be deployed on-premise and connect to internal systems. In this configuration, data never leaves your network  --  the MCP server queries internal systems and returns results directly to the AI client.
</details>

<details>
<summary><strong>What security certifications does CorpusIQ hold?</strong></summary>

CorpusIQ maintains SOC 2 Type II certification. Additional certifications are available for Enterprise customers with specific requirements.
</details>

## Internal Links

- [Learn what an MCP server is and how it works](/docs/what-is-an-mcp-server)
- [Understand how MCP servers work with a technical deep dive](/docs/how-mcp-servers-work)
- [Discover the business benefits of MCP servers](/docs/benefits-of-mcp-for-business)
- [Learn about MCP for enterprise-scale deployments](/docs/mcp-for-enterprise)
- [Learn about MCP for financial reporting and compliance](/docs/mcp-for-finance)
- [See how executives use MCP for AI-powered dashboards](/docs/mcp-for-executives)

*[CorpusIQ](https://www.corpusiq.io)  --  AI answers grounded in your business data. 30-day free trial.*

*[CorpusIQ](https://www.corpusiq.io)  --  AI answers grounded in your business data. 30-day free trial.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
