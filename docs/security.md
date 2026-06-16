# Security

CorpusIQ is designed with data privacy as a foundational principle. This document outlines our security architecture, data handling practices, and compliance posture.

## Core Security Principles

### Read-Only OAuth

Every CorpusIQ connector uses **read-only OAuth scopes**. We never request write permissions for any connected service. The specific scopes requested are visible on the OAuth authorization screen during connection setup, and you can verify the scopes granted at any time in your service provider's account settings.

This means CorpusIQ cannot:
- Create, modify, or delete records in your connected tools
- Send emails, messages, or notifications on your behalf
- Process payments or modify financial data
- Change configurations or permissions

### Zero Data Storage

CorpusIQ operates on a **zero-retention model** for query data:

1. A query is received and translated into read-only API calls
2. Results are fetched from connected tools in real time
3. Temporary embeddings are generated for semantic ranking within the session
4. **All embeddings are deleted immediately after the session completes**

No query results, embeddings, or derived data are persisted on CorpusIQ servers after your query session ends. The encrypted deep search archive stores only vector fingerprints — not raw data — and is purged on account deletion.

### Encryption

| Layer | Standard |
|-------|----------|
| **In Transit** | TLS 1.3 with modern cipher suites. All API traffic is encrypted end-to-end. |
| **At Rest** | AES-256-GCM encryption for all stored data (tokens, archive vectors, configuration). |
| **Archive** | The deep search archive uses per-user encryption keys. Even CorpusIQ cannot read archived content without the user's active token. |

### Token Security

- API tokens have a **60-minute expiry** with server-side refresh detection
- Tokens are never embedded in client-side code — server-side usage only
- Token revocation takes effect immediately across all active sessions
- OAuth tokens are encrypted at rest with per-tenant keys

### Webhook Security

All webhook deliveries are signed with **HMAC-SHA256** using a per-endpoint signing secret. The signature is included in the `CorpusIQ-Signature` header. Your server must verify this signature before processing any payload. See [Webhooks](/docs/api/webhooks) for verification code examples.

Untrusted payloads are rejected before processing, preventing replay attacks and payload tampering.

## Compliance

### SOC 2 Type II

CorpusIQ is actively pursuing SOC 2 Type II certification. The compliance program covers:

- **Security**: Firewalls, access controls, intrusion detection
- **Availability**: Redundant infrastructure, uptime monitoring, disaster recovery
- **Confidentiality**: Encryption, access restrictions, data segregation
- **Privacy**: Data minimization, user consent, deletion rights

Status updates on the certification process are available at [corpusiq.io/trust](https://corpusiq.io/trust).

### Data Processing

- **Data Minimization**: Only data necessary to answer a query is retrieved
- **Purpose Limitation**: Data is used exclusively to fulfill the user's query
- **User Control**: Users can revoke OAuth tokens and delete all data at any time via `/delete_my_data`
- **No Data Sale**: CorpusIQ does not sell, share, or monetize user data

## Infrastructure

- All services run in isolated virtual private clouds
- Network access is restricted by IP allowlisting and security groups
- All access is logged and audited
- DDoS protection and WAF are deployed at the edge
- Regular penetration testing by third-party security firms

## Reporting Vulnerabilities

If you discover a security vulnerability, please report it to:

**security@corpusiq.io**

We follow a coordinated disclosure process and aim to acknowledge reports within 24 hours. Please do not publicly disclose vulnerabilities before we have had an opportunity to address them.

## Security FAQ

**Q: Does CorpusIQ see my data?**
A: CorpusIQ processes your data transiently within a single query session. Results are fetched, ranked, and returned — then discarded. No human at CorpusIQ reviews your query results.

**Q: What happens when I delete my account?**
A: The `/delete_my_data` endpoint permanently removes all OAuth tokens, query history, archive entries, webhook registrations, and profile data. Nothing is retained beyond what the connected tools themselves store independently.

**Q: Can CorpusIQ access my tools when I'm not querying?**
A: No. Every API call to a connected tool is triggered by an explicit user query. There is no background data collection, periodic syncing, or scheduled polling.

**Q: Where is data processed?**
A: US-based infrastructure. For enterprise customers, data residency options are available — contact sales@corpusiq.io.
