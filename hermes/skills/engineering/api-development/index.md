---
title: api-development
description: Pattern for operating a FastAPI backend on Cloud Run as the single token issuer to a multi-service stack. Test fixture traps, self-destructing admin migrations for live DB changes, the JWT JWKS contract with consumers, and how to verify a deploy actually went out.
---

# API Development (Cloud Run + FastAPI)

When your stack has multiple services (MCP servers, frontend, workers) and one of them is the **token issuer** — the FastAPI backend that mints JWTs everything else verifies — the discipline for that service is meaningfully different from the discipline for the consumers.

## The single-token-issuer rule

If you have one auth-issuing API and multiple JWT-consuming services:

- The API publishes `/.well-known/jwks.json` (or equivalent)
- Every consumer fetches the JWKS and verifies tokens locally — no auth round-trip per request
- The API is the ONLY service that knows how to mint tokens; consumers are read-only on auth
- Schema changes to the JWT payload require coordinated deploys across consumers (the API issues new-shape tokens, consumers must handle both shapes during the transition)

This is the boring, correct pattern. The mistake to avoid: scattering token-validation logic so each service does its own (eventually two services drift, and a token works on one but not the other).

## FastAPI test-fixture traps (regression-test recipe)

When you're writing an after-the-fact regression test for a security or auth fix, the test fixture is usually the hardest part. The following five traps each cost an hour on the first encounter:

### 1. JSONB compile hook ordering (SQLite test DB)

If your prod DB is Postgres but your test DB is SQLite, you'll have JSONB columns SQLite doesn't natively support. Most projects solve this with a compile hook (`@compiles(JSONB, "sqlite")`) that maps JSONB to TEXT. **The hook MUST be imported before any model that uses JSONB.** Otherwise the model's `metadata.create_all()` fires before the hook lands and the column gets created with the wrong type.

Recipe: import the hook module at the top of your test conftest.py, BEFORE any model imports.

### 2. UUID type mismatch between raw-SQL inserts and SQLAlchemy column adapters

SQLite stores UUIDs as either TEXT or BLOB depending on the column adapter. If you do a raw SQL `INSERT` for test fixtures and the column was declared as UUID(as_uuid=True), the adapter expects a UUID object — not a string. The raw insert puts a string in; the next ORM read tries to deserialize the string as a UUID and crashes.

Recipe: insert via SQLModel/SQLAlchemy ORM in fixtures, not raw SQL. Or, use `str(uuid.uuid4())` consistently and skip the as_uuid=True.

### 3. `metadata.create_all()` pulling in Postgres-only tables

If your models include something like `audit_logs` declared in a Postgres-only module (because audit is Postgres-only and your test setup imports models broadly), `create_all()` on SQLite will choke on Postgres-specific types like `JSONB[]` or `pg_trgm` indexes.

Recipe: narrow `metadata.create_all()` to the exact tables your test needs. Skip the `auth.users` FK trap by mocking foreign-key-to-Postgres-only-tables, not by creating those tables.

### 4. MCP JWT key bootstrap needs both DEBUG=True AND empty private key file

If your JWKS endpoint reads the signing key from disk in prod but generates an ephemeral one in dev mode, the test fixture needs BOTH `DEBUG=True` AND `MCP_JWT_PRIVATE_KEY_FILE=""` set. Otherwise the test tries to read a non-existent file and crashes during startup, not during the actual test.

Recipe: set both env vars in the test fixture's `monkeypatch.setenv` block before instantiating the app.

### 5. UserSubscription NOT NULL on stripe_customer_id

If your User table joins to UserSubscription and UserSubscription declares `stripe_customer_id` as NOT NULL (because in prod every paying user has one), test fixtures inserting a free-tier user will fail constraint validation.

Recipe: insert UserSubscription with a placeholder stripe_customer_id like `cus_test_<id>` for free-tier fixtures, or make the column nullable if the model supports it.

## Self-destructing admin migration endpoint pattern

For live DB changes that need to run once in prod without a full migration cycle:

```python
@router.post("/admin/migrations/<name>")
async def run_migration_<name>(...):
    # 1. Auth: require admin role + signed migration token
    # 2. Idempotency: read a marker row; if present, return 200 "already ran"
    # 3. Run the migration
    # 4. Write the marker row
    # 5. Log to audit_logs with full context (who, when, rows affected)
    # 6. Return 200 with summary
```

Then delete the endpoint code in the next PR (self-destructing). The migration is recorded in audit logs; the marker row prevents re-runs; the endpoint is gone before the next contributor can re-invoke it.

This pattern beats both "let's run a one-off script with the right env vars" (fragile, no audit trail) and "let's add a proper migration framework" (overkill for a one-off).

## Deploy verification

Cloud Run deploys complete in 2-4 minutes. After a merge, verify the deploy actually shipped your code:

```bash
# 1. Confirm the deploy workflow finished successfully
gh run list --workflow="deploy.yml" --limit 1

# 2. Fetch the live OpenAPI spec
curl -s https://api.<your-domain>/openapi.json | jq '.paths | keys[] | select(test("<new-path>"))'

# 3. If you added a docstring to a new endpoint, the FastAPI-generated spec
#    will surface that docstring. Grep for it as a "yes, the new code is live" probe.
curl -s https://api.<your-domain>/openapi.json | grep "<unique docstring phrase>"
```

The FastAPI docstring trick is the simplest "is my code actually deployed" verification. It works because FastAPI generates the OpenAPI spec from live introspection of the running app, not from a file in the repo. If the docstring is in the response, the new code is running.

## Database backend

When your DB is Supabase-hosted Postgres + GoTrue for auth:

- Your team-lead (or whoever has the Supabase admin grant) is the only one who can do DB-level operations — migrations, role grants, RLS policy changes
- Cloud Run instances connect via DATABASE_URL stored in Secret Manager
- Console-level work (env vars, IAM, Secret Manager provisioning) often happens through the GCP console UI, not gcloud CLI

If you can do GCP-console work but not Supabase-admin work, the boundary matters: route DB-level work (psql migrations against DATABASE_URL, dashboard ops) to whoever owns Supabase admin, keep Cloud Run / env / IAM in your lane.

## Related

- [consultant-connector-audit §14](../consultant-connector-audit/) — when a consultant pushes auth/billing/security code, the same audit discipline applies even though "connector" is in the name
- [mcp-architecture](../mcp-architecture/) — the consumer side of the JWT contract this API issues


*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*


*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
