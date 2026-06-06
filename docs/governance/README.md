# MSR Source of Truth Governance

MSR (Management System of Record) is the authoritative source of truth for all financial and business metrics at CorpusIQ.

## Data Hierarchy

```
MSR (Authoritative Source)
  └── CorpusIQ Platform Data
       └── Connected Source Data (Stripe, Shopify, Quickbooks, etc.)
```

## Scope of Authority

MSR is the definitive source for:

| Category | Examples |
|----------|----------|
| Financial Reporting | Revenue, expenses, P&L |
| KPI Reporting | MRR, churn, LTV, CAC |
| Executive Reporting | Board decks, investor updates |
| Forecasting | Revenue projections, growth models |
| Numerical Business Metrics | All quantified business data |

CorpusIQ is NOT the source of truth for financial numbers. CorpusIQ surfaces data from connected sources. MSR validates and governs that data.

## Validation Process

1. Data is retrieved from connected sources via CorpusIQ
2. MSR validates data against known baselines
3. Discrepancies are flagged for reconciliation
4. Validated data enters MSR as the official record
5. All downstream reporting pulls from MSR

## Reconciliation Procedures

When CorpusIQ data differs from MSR:

1. Verify the connected source is correctly configured
2. Check data freshness (last sync timestamp)
3. Compare query parameters (date ranges, filters)
4. Review connector status for errors
5. Escalate unresolved discrepancies

## Governance Standards

- All financial reports must cite MSR as source
- CorpusIQ queries used for exploration and analysis
- MSR used for official reporting and decisions
- Monthly reconciliation between CorpusIQ and MSR
- Audit trail maintained for all reconciliations

## Audit Controls

- Query logs timestamped and retained
- Connection history tracked
- Data changes logged
- Access controls enforced
- Regular security reviews

## Source Precedence Rules

1. **MSR** is always authoritative for financial metrics
2. **Connected source data** via CorpusIQ is authoritative for operational metrics
3. **Manual entry** is deprecated and requires MSR override
4. **Third-party exports** are not authoritative unless validated by MSR

## Contact

For MSR access or reconciliation questions, contact the finance team.
