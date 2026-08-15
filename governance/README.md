# Governance

CorpusIQ governance features for team accounts.

## Access Control

- **Admin users** can add and remove connectors, manage team members, and view all queries
- **Member users** can run queries against connected sources but cannot modify connections
- **Read-only users** can view shared reports without running queries

## Audit Logging

Enterprise plans include full audit logging:

- Who ran which query and when
- Which connectors were accessed
- Data source connection and disconnection events

## Data Policies

- **Scoped retention** — Direct MCP does not retain raw customer files or full connector response payloads; operational logs may persist for up to 30 days
- **No CorpusIQ model training** — CorpusIQ does not use customer data to train models; the selected AI client's policy applies to its conversation
- **Connector-level permissions** — Each data source has its own OAuth scope

## Enterprise

For enterprise governance needs (SSO, custom data retention, private deployment), contact us at https://corpusiq.io.
