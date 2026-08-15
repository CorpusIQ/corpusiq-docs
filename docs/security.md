---
title: "CorpusIQ Security"
description: "CorpusIQ security documentation: CASA Tier 2, SOC 2 aligned controls, AES-256, TLS 1.3, read-only OAuth, and scoped data handling"
category: "Documentation"
tags: ["corpusiq security", "soc 2", "casa tier 2", "data privacy", "encryption", "oauth security", "gdpr compliance", "ai security"]
last_updated: "2026-08-12"
canonical: "https://www.corpusiq.io/docs/security"
robots: "index,follow"
---
# Security

CorpusIQ is designed with data privacy as a foundational principle. This page documents the technical and organizational measures applied to protect user data. CorpusIQ LLC, Scottsdale, Arizona. Last updated: March 24, 2026.

## Certifications & Compliance

| Standard | Status |
|----------|--------|
| **CASA Tier 2** | Certified by DEKRA  --  OWASP Top 10 Verified |
| **SOC 2** | Aligned  --  formal certification is not claimed; controls are reviewed quarterly |
| **GDPR** | Aligned  --  data minimization, user consent, deletion rights |
| **Encryption** | AES-256 at rest, TLS 1.3 in transit |
| **Access Model** | Read-only OAuth  --  no write permissions ever |

Contact: security@corpusiq.io · privacy@corpusiq.io

## 1. Product Scope

**Sources:** Gmail, Google Drive, OneDrive, Dropbox, Outlook, Shopify, QuickBooks, HubSpot, Google Analytics, Google Ads, Meta Ads, YouTube, TikTok, eBay, PostgreSQL, SQL Server, and more. User-authorized only. No device agents. No browser extensions.

**Outputs:** In-chat answers, ranked references, and optional deep search results.

**Storage:** Direct MCP connector requests use live retrieval and do not build embeddings or file indexes. Optional indexed-search features use embeddings and minimal metadata. No raw file bodies are retained.

**Controls:** Per-user namespace, connector revocation, privacy-request handling, and structured audit logging. The Azure Log Analytics workspace retains operational logs for 30 days.

## 2. Data Inventory and Flow

CorpusIQ sits between your tools and the AI assistant. Read-only on one side. Source-backed answers on the other. Every step is logged.

| Data Class | Examples | Encryption | Retention |
|------------|----------|------------|-----------|
| Account | Email, OAuth subject | AES-256 at rest | Until account deletion |
| Optional indexed search | Embeddings, chunk IDs | AES-256 at rest | Until connector revocation or account deletion |
| Operational MCP query logs | Query text, tool metadata, bounded outcome summaries | AES-256 at rest | Up to 30 days |


- **Encrypted retrieval:** Data is encrypted in transit and at rest, scoped per user.
- **User-scoped isolation:** Each account operates in a separate namespace with no cross-access.
- **Scoped MCP logging:** Direct MCP does not retain raw customer files or full connector response payloads. Query text, tool-call metadata, and bounded outcome summaries are kept in operational logs for up to 30 days.

## 3. Security Controls

### Transport
TLS 1.3 only, HSTS, forward secrecy.

### Encryption at Rest
AES-256, managed keys, key rotation every 90 days.

### Network
Private subnets, deny-by-default, WAF and rate limits on all public endpoints.

### Access
Read-only OAuth scopes only. No write permissions on any connector. The specific scopes requested are visible on the OAuth authorization screen during connection setup.

### Authentication
API tokens have 60-minute expiry with server-side refresh detection. Tokens are never embedded in client-side code  --  server-side usage only. Token revocation takes effect immediately across all active sessions.

### Webhook Security
CorpusIQ does not currently publish a customer-facing webhook event contract. Event schemas, authentication, and delivery guarantees will be documented only after their production routes are verified.

## 4. Privacy and Lawful Basis

CorpusIQ processes data under the lawful basis of user consent and legitimate interest (service provision):

- **Data Minimization:** Only data necessary to answer a query is retrieved
- **Purpose Limitation:** Retrieved records fulfill the user's request; retained operational metadata supports service security, reliability, and compliance under the published schedule
- **No Data Sale:** CorpusIQ does not sell or monetize user data; scoped data is shared only with processors required to fulfill the request
- **No CorpusIQ Model Training:** CorpusIQ does not use customer data to train models; each selected AI client's policy applies to its conversation
- **No Background Collection:** Every API call to a connected tool is triggered by an explicit user query. There is no periodic syncing or scheduled polling.

## 5. Retention and Deletion

1. A query is received and translated into read-only API calls
2. Results are fetched from connected tools in real time
3. Direct MCP requests return the result without building embeddings or file indexes; optional indexed search separately retains embeddings and minimal metadata
4. Optional indexed-search features may retain embeddings and minimal metadata while the connector remains active

To request deletion of account data, contact privacy@corpusiq.io. CorpusIQ responds to privacy requests within 30 days. Operational MCP query logs remain subject to the 30-day Azure Log Analytics retention window.

## 6. Subprocessors

Infrastructure: Microsoft Azure (US-based). Enterprise cloud infrastructure. For enterprise customers, data residency options are available  --  contact sales@corpusiq.io.

## 7. Incident Response

- Monitoring and alerting on all production systems
- Defined incident classification and escalation paths
- Post-incident reviews with corrective actions
- User notification for confirmed data exposure events

## 8. Annual Reviews and Audits

- SOC 2 readiness program with quarterly control checks
- Independent pen-testing at least annually
- OWASP Top 10 verified (DEKRA CASA Tier 2 assessment)
- Regular vulnerability scanning and dependency audits

## 9. User Data Rights

Users can:
- Revoke OAuth tokens at any time via account settings
- Request deletion of account data by contacting privacy@corpusiq.io
- Request a data inventory by contacting privacy@corpusiq.io
- Export account data via the dashboard

## 10. Public API and Webhooks

- REST API at `https://mcp2.corpusiq.io/mcp`
- Bearer token authentication with 60-minute expiry
- Rate-limited endpoints with documented quotas
- No public webhook event contract is currently published

## 11. Reporting Vulnerabilities

If you discover a security vulnerability, report to security@corpusiq.io. We follow a coordinated disclosure process and aim to acknowledge reports within 24 hours. Please do not publicly disclose before we have had an opportunity to address them.

## Frequently Asked Questions

**Q: What security certifications does CorpusIQ hold?**  
A: CorpusIQ is CASA Tier 2 certified by DEKRA (OWASP Top 10 verified) and maintains a SOC 2 aligned security posture. The platform uses AES-256 encryption at rest, TLS 1.3 in transit, and read-only OAuth for all data source connections.

**Q: Does CorpusIQ store my business data?**  
A: Direct MCP requests retrieve source records live without retaining raw customer files or full connector response payloads. Operational query text, tool-call metadata, and bounded outcome summaries are retained for up to 30 days. Optional indexed-search features may retain embeddings and minimal metadata while the connector remains active.

**Q: How does CorpusIQ handle data deletion?**
A: Contact privacy@corpusiq.io to request deletion of account data. CorpusIQ responds to privacy requests within 30 days. Operational MCP query logs remain subject to the 30-day Azure Log Analytics retention window.

**Q: Where is CorpusIQ infrastructure hosted?**  
A: Infrastructure runs on Microsoft Azure (US-based). Enterprise customers can request data residency options for specific geographic regions. Contact sales@corpusiq.io for details.

**Q: How do I report a security vulnerability?**  
A: Report to security@corpusiq.io. CorpusIQ follows coordinated disclosure and aims to acknowledge reports within 24 hours. Do not publicly disclose before the team has addressed the issue.

## Internal Links

- **[CorpusIQ Quick Start Guide](/docs/quick-start)**  --  Go from zero to first query in 5 minutes  
- **[API Reference](/docs/api/overview)**  --  Full REST API documentation  
- **[CorpusIQ Connectors](/docs/connectors)**  --  All 40+ supported integrations  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)**  --  SSO, SOC 2, data residency  
- **[CorpusIQ Security Documentation](/docs/security)**  --  Certifications, encryption, and compliance  
- **[CorpusIQ Changelog](/docs/changelog)**  --  API updates and version history  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)**  --  Encryption and network security  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
