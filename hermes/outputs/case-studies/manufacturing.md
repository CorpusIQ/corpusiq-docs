# Manufacturing: Supply Chain & Quality Control Automation

Manufacturing operations span physical and digital domains — production lines, inventory systems, supplier networks, quality data, and maintenance schedules all generate continuous streams of information. Hermes Agent bridges these domains by connecting databases, APIs, and IoT data sources into unified monitoring and alerting workflows.

## The Manufacturing Data Problem

Most manufacturers run excellent systems individually: an ERP for orders and inventory, a MES for production tracking, a CMMS for maintenance, separate quality databases, and supplier portals. The gap isn't data collection — it's data connection. Engineers and managers spend hours each day checking multiple dashboards and reconciling discrepancies between systems.

Hermes Agent automates that cross-system reconciliation and alerting.

## Supply Chain Monitoring

Supply chain disruptions cascade fast. A late shipment from one supplier delays production, which delays customer orders, which triggers penalty clauses. Early warning is everything.

**Supplier Shipment Tracking**

```yaml
- name: supplier-shipment-monitor
  schedule: "0 6,12,18 * * *"  # Three times daily
  skill: supply-chain-monitor
  description: Checks all open purchase orders against supplier confirmations and shipment tracking
```

The skill queries your ERP (via database connector or Odoo/other MCP integration) for open purchase orders, then checks:
- Confirmed ship dates vs. original promise dates
- Carrier tracking status (via shipping API connectors)
- In-transit delays from carrier status codes
- Quantity discrepancies between PO, supplier confirmation, and actual shipment

When a shipment is at risk — late, short-shipped, or stuck in transit — the skill alerts the procurement team through Slack and creates a follow-up task in the project management system with all relevant order details attached.

**Inventory Level Monitoring**

```yaml
- name: inventory-reorder-check
  schedule: "0 7 * * *"  # Daily at 7 AM
  skill: inventory-reorder
  description: Checks inventory against reorder points and production schedule demand
```

This skill goes beyond simple min/max checks. It factors in:
- Current on-hand quantity
- Already-open purchase orders (inbound)
- Production schedule demands for the next 2-4 weeks
- Supplier lead times
- Safety stock requirements

The output is a prioritized replenishment list with recommended order quantities and urgency flags. For items below safety stock with no open PO, Hermes can trigger immediate alerts.

## Quality Control Alerts

Quality data lives in its own systems — inspection databases, lab information management systems (LIMS), statistical process control (SPC) software. Hermes connects to these and applies rules that cross quality data with production data.

**Out-of-Spec Detection**

```yaml
- name: quality-spc-monitor
  schedule: "*/30 * * * *"  # Every 30 minutes during production
  skill: quality-monitor
  description: Checks latest QC measurements against control limits
```

The skill:
1. Queries the quality database for recent measurements
2. Applies Western Electric rules (runs, trends, out-of-control signals)
3. Correlates quality issues with production parameters (which machine, which shift, which material lot)
4. When SPC rules trigger, creates an alert with full context: the measurement, the rule violated, the production batch, and the material lot

**Supplier Quality Trending**

```yaml
- name: supplier-quality-review
  schedule: "0 8 * * 1"  # Weekly Monday at 8 AM
  skill: supplier-quality-trend
  description: Aggregates supplier quality metrics and flags deteriorating trends
```

This skill tracks defect rates by supplier over rolling time windows, flags statistical degradation, and produces a Monday-morning report prioritized by business impact (which suppliers' quality problems are affecting the most production value).

## Equipment Maintenance Scheduling

Reactive maintenance is expensive. Predictive maintenance based on actual equipment data is the goal, but most shops can't afford dedicated predictive analytics platforms. Hermes provides a practical middle ground.

**Maintenance Schedule Coordination**

```yaml
- name: maintenance-scheduler
  schedule: "0 5 * * *"  # Daily at 5 AM
  skill: maintenance-coordinator
  description: Reviews equipment runtime, upcoming maintenance, and production schedule for conflicts
```

The skill:
1. Pulls equipment runtime meters from the CMMS database
2. Calculates remaining hours before next scheduled maintenance
3. Cross-references against the production schedule
4. Flags equipment approaching maintenance thresholds during scheduled production runs
5. Proposes maintenance windows that minimize production disruption

**IoT Sensor Integration**

For manufacturers with IoT sensors on equipment, Hermes can query sensor databases or time-series stores:

```yaml
- name: equipment-health-monitor
  schedule: "*/15 * * * *"
  skill: equipment-health
  description: Monitors IoT sensor data for early warning signs
```

The skill queries sensor readings — vibration, temperature, current draw, pressure — and applies threshold rules. A bearing temperature trending upward across successive readings triggers an alert before the bearing fails, giving maintenance time to schedule replacement during planned downtime rather than reacting to a line stoppage.

## Production Reporting

Shift-by-shift production reporting often involves operators manually entering data that already exists in machine controllers and MES databases. Hermes can automate the aggregation:

```yaml
- name: shift-production-report
  schedule: "0 6,14,22 * * *"  # At each shift change
  skill: shift-report
  description: Aggregates production data by shift and delivers summary
```

## Getting Started in Manufacturing

1. **Connect your ERP database first.** Most manufacturers have a SQL-accessible ERP. Start there — it contains orders, inventory, and supplier data.
2. **Pick one alert that would prevent a recent problem.** Think about the last production delay or quality escape. Build the Hermes automation that would have caught it.
3. **Use database connectors for on-prem systems.** Many manufacturing databases run on MSSQL or PostgreSQL — both directly accessible to Hermes.
4. **Layer in IoT gradually.** Start with thresholds you understand (temperature above X), then refine as you learn what patterns matter.
5. **Route alerts to where action happens.** In manufacturing, that's often a maintenance Slack channel, a production team email, or directly into the CMMS as a work order.

The outcome: fewer surprises, less manual data-gathering, and faster response to the supply chain and quality issues that inevitably arise.
