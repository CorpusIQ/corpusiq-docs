---
title: "ChartAnt MCP - Charts and Maps as Image Links"
description: "A keyless MCP server that turns data into 45 chart types, country and county maps and multi-panel dashboards, returning a PNG link plus editable PowerPoint."

category: "Analytics / Data Visualization"
stars: "0 (hosted, closed source; 51 tools, keyless, 9 of them driven)"
added: 2026-11-15
source: "the mcp.so submission queue entry #7374 filed 2026-11-15T04:44Z, and a driven session against https://chartant.net/mcp on 2026-11-15 in which initialize answered 200 as ChartAnt 0.4.0, tools/list returned 51 schemas and nine tools were called"
relevance: ★★★
tags: [charts, data-visualization, maps, dashboards, reporting, powerpoint, excel, keyless, remote-mcp]
last_updated: "2026-11-15"
---

# ChartAnt MCP

**A number in a chat answer is a claim. A chart is a document.** Every business question an assistant answers ends in the same place: the operator wants to send what they were told to a client, a board or a bank. Text does not travel, and a table pasted into an email travels badly. What travels is an image with a legend, and what survives review is a file somebody downstream can edit.

ChartAnt is a drawing server. It takes rows and returns a link to a rendered image, together with a share page, an editable PowerPoint chart, an Excel workbook and alt text that describes the picture in words so an assistant can talk about it without seeing it. Fifty one tools, no key, no account for the drawing path.

```
Server type:   remote Streamable HTTP, JSON-RPC 2.0, keyless and stateless
Endpoint:      https://chartant.net/mcp
Server:        ChartAnt, version 0.4.0, capabilities tools + resources
Website:       https://chartant.net
Docs:          https://chartant.net/docs
Account tier:  https://chartant.net/mcp/account (optional, for saved
               living charts that keep a fixed link and update)
Auth:          none for the drawing tools
Tools:         51 (39 drawing tools, 1 report builder, 2 place helpers,
               9 account and living-chart tools)
Listed on:     the mcp.so submission queue as #7374
```

## The evidence tier

Driven, not documented. `initialize` answered **200** in 0.89 seconds with no credential and no session identifier on the response, `tools/list` returned **51** schemas, and **nine** tools were called against live data on 2026-11-15: `match_places` at three levels, `locate_points`, `generate_bar_chart`, `generate_world_map`, `generate_country_map`, `generate_dashboard`, `generate_kpi_card`, `create_report` and `create_living_chart`. Every image link below was fetched and its bytes checked, and two of the rendered images were looked at rather than trusted.

## The tool surface

The 39 drawing tools are one shape with different geometry: pass `data`, get an image link back. What matters is which geometries exist, because that is what decides whether a question can be answered in a picture at all.

| Group | Tools |
|---|---|
| Maps | `generate_world_map` (countries coloured by value), `generate_country_map` (first level regions of any country), `generate_county_map` (US counties, all or one state), `generate_pin_map` (labelled lat/lon dots), `generate_map_ranking` (map beside a top-places bar chart), `generate_small_multiples` (one small chart per group on a shared scale) |
| Comparison | `generate_bar_chart`, `generate_column_chart`, `generate_dual_axes_chart`, `generate_bullet_chart` (measure against target), `generate_gauge_chart`, `generate_liquid_chart` |
| Time | `generate_line_chart`, `generate_area_chart`, `generate_candlestick_chart`, `generate_calendar_heatmap`, `generate_gantt_chart` |
| Distribution | `generate_histogram_chart`, `generate_boxplot_chart`, `generate_violin_chart`, `generate_scatter_chart` |
| Composition and flow | `generate_pie_chart` (donut via `innerRadius`), `generate_treemap_chart`, `generate_sankey_chart`, `generate_funnel_chart`, `generate_waterfall_chart`, `generate_venn_chart`, `generate_word_cloud_chart` |
| Structure | `generate_flow_diagram`, `generate_fishbone_diagram`, `generate_mind_map`, `generate_network_graph`, `generate_organization_chart` |
| Tables and compound | `generate_spreadsheet` (plain or pivot), `generate_heatmap_chart`, `generate_radar_chart`, `generate_kpi_card` (1 to 4 numbers), `generate_dashboard` (up to 4 rows of 4 panels), `generate_more_charts` (rose, radial bar, bubble, dumbbell, lollipop, slope, chord, circle packing and others) |
| Places | `match_places` (messy names to ISO codes at country, region or US county level), `locate_points` (lat/lon to country, region and county) |
| Documents | `create_report` (charts, maps, KPI cards and text into one shareable page with PDF and PowerPoint) |
| Account | `create_living_chart`, `update_living_chart`, `list_my_charts`, `list_chart_versions`, `restore_chart_version`, `add_destination`, `send_chart_on_update`, `schedule_chart`, `manage_workspace` |

Every drawing tool carries MCP annotations: `readOnlyHint` true, `idempotentHint` true, `openWorldHint` false. `create_living_chart` is the only one that writes.

## What the calls returned

**Place resolution is the quiet capability.** This is what makes a map possible at all: a CRM export says `Côte d'Ivoire`, `USA` and `England`, and a choropleth needs `CI`, `US` and `GB`. `match_places` at country level matched **3 of 6** in the sample and said so plainly:

```
Côte d'Ivoire -> Ivory Coast (CI, CIV)
USA           -> United States of America (US, USA)
England       -> United Kingdom (GB, GBR)
Bavaria       -> not found
Ontario       -> not found
São Paulo     -> not found
```

The three misses are not errors, they are the level being wrong, and the schema makes that explicit with a `level` argument that the description does not emphasise. Re-asked at `level: "region"` with `country: "DE"`, the same kind of input matched **3 of 3**: `Bavaria (DE-BY)`, `Baden-Württemberg (DE-BW)`, `Saxony (DE-SN)`. At `level: "county"` with `state: "GA"`: `Fulton (13121, GA)`, `DeKalb (13089, GA)`, `Gwinnett (13135, GA)`, all three FIPS codes correct.

`locate_points` resolves the other direction and does it accurately. Three coordinates, three correct answers: `48.8566, 2.3522` to **France (FR) › Paris (FR-75)**, `33.7490, -84.3880` to **United States (US) › Georgia (US-GA) › Fulton County (13121)**, `-33.8688, 151.2093` to **Australia (AU) › New South Wales (AU-NSW)**.

**A world map with five countries.** Asked for revenue by country in EUR, it returned a PNG link, a share page, alt text naming the highest and lowest, an editable PowerPoint chart and an Excel workbook. The PNG was **1920 by 1080** and **187,175 bytes** at `content-type: image/png`, twice the default 960 by 540 because the renderer outputs at 2x. Fetched and looked at, it is a real Natural Earth choropleth: the United States darkest and labelled **88K EUR**, Germany and France in mid blues, the United Kingdom and Italy pale, everything else grey under a `No data` swatch, and a stepped legend reading **15K, 27K, 31K, 42K, 88K**. The alt text is generated from the data rather than written by the vendor: *World map: Revenue by country. Colours 5 countries by value. Highest: United States of America (88,000 EUR); lowest: Italy (15,000 EUR).*

**A country map where the country is a parameter.** `generate_country_map` with `country: "DE"` and four Bundesländer by revenue returned a **1600 by 1200** PNG and a correct map of all sixteen states, four of them coloured, with a legend from **12K** to **42K EUR**. It also demonstrates the label rule: `labels: "both"` printed **Bavaria 42K EUR** and **Baden-Württemberg 31K EUR** and left North Rhine-Westphalia and Berlin unlabelled, because the schema says *labels that don't fit are left out* and small areas do not fit. A German title over English region names is a mixed language output, and it is the boundary dataset speaking, not a translation step.

**A dashboard from one call.** Two panels, a KPI card and a bar chart, came back as one PNG with alt text that enumerates the panels: *Dashboard: Weekly ops with 2 panels. Panel 1: KPI cards. Sign-ups: 128. Panel 2: Bar chart: Sign-ups by week. 3 categories. Highest: W46 (128); lowest: W44 (102).* That alt text is the difference between an image a blind assistant can describe and an image it has to guess at.

**A report is three files, not one.** `create_report` returned a share page (HTML, 7,338 bytes), a PDF (14,979 bytes) and a PowerPoint deck (50,887 bytes), all three answering **200** when fetched. This is the artifact shape an operator can actually forward.

## The limits, and where they bite

- **The keyless tier expires in an hour.** Every response says it in a sentence: *without an account this link works for 1 hour*. The image, the PowerPoint, the Excel file and the share page all live behind that clock. An assistant that generates a chart on Monday and pastes the link into a client email on Tuesday has produced a broken link, and the server does say so rather than letting it fail silently. The `/keep/` link in the same response is the escape, and an account makes the link permanent.
- **Living charts need an account, and the server says so instead of pretending.** `create_living_chart` keyless answered with `NOT SAVED: this connection has no account, so this is a one-off image with no id and it cannot be updated`, then drew the image anyway. So the five tools that make a chart update from a schedule, post to Slack, Teams, Discord, an email or a webhook, and keep version history are an account feature, reached by connecting `https://chartant.net/mcp/account` instead.
- **Unknown argument names are ignored silently.** `format: "svg"` sent to `generate_pie_chart` returned a PNG with no warning, because that tool has no `format` argument, while `generate_world_map` does. The schema in `tools/list` is the contract and nothing validates against it, so send the names the schema prints.
- **Zero data renders something anyway.** A pie chart with two zero valued rows returned an image with the bare alt text *Pie chart* and no error. A chart of nothing is not a useful chart, and the response does not say it could not draw the data.
- **Label placement is a fit test, not a guarantee.** Only the areas with room carry a name or a value, and the alt text is the reliable place to read the numbers. Do not promise an operator that every region will be printed on the image.
- **Drawing is 2x by default.** The default width of 960 produces a 1920 pixel PNG, so a figure quoted for a fixed layout will be twice what the schema suggested. Pass `width` and `height` explicitly when the destination has a fixed slot.
- **A bad argument type fails loudly, which is the right shape.** `generate_kpi_card` given `value: "18.4%"` answered `MCP error -32602: Invalid input: expected number, received string at items[1].value`. Numbers are numbers; format the percentage in the label instead.

## Frequently asked

### Does it need an API key?

No. `initialize`, `tools/list` and all nine driven `tools/call` requests returned 200 over plain HTTPS with no credential, and the server returns no session identifier, so it is stateless from the client's side and usable from any MCP client that can reach a URL.

### Is anything hosted or stored?

The image is hosted and served from `chartant.net` under an opaque identifier. Without an account that host keeps it for an hour, and with an account the chart can be saved and updated. The vendor states the service is EU hosted. If the data is confidential, the one hour link and the absence of an account are the point: nothing persists unless somebody asks it to.

### Can I get an editable version?

Yes, for every drawing tool tested. Each response carries a `.pptx` link that opens as a native PowerPoint chart and an `.xlsx` link that opens with the data behind it, both fetched and confirmed at the right MIME types in this pass. That is what makes the output usable in a deck that somebody else will edit.

### How does a map get its values?

Two steps, and the first one is the one people skip. Resolve the names with `match_places` at the right `level`, then pass the standard codes to `generate_world_map`, `generate_country_map` or `generate_county_map`. Country names in the data also work directly, as the five country world map showed, but a column of state names needs the region step.

### Where does it fit next to a BI tool?

It does not replace one. A BI tool owns a warehouse and a refresh schedule; this draws one answer as a file at the moment the question is asked, which is what a chat answer needs and what a dashboard does not. Written to the JSON of charts, the same data is the input to both.

## What to check before you build on it

1. Resolve place names with `match_places` at the level you actually need, and read the *X of Y matched* line rather than assuming.
2. Treat every keyless link as a one hour artifact. Generate it when you are about to send it, or connect the account endpoint for anything that has to survive the day.
3. Pass `width` and `height` when the image has a fixed destination, because the default is rendered at 2x.
4. Send only argument names that appear in the `tools/list` schema; anything else is dropped without a warning.
5. Read the numbers from the alt text or the `Description` line rather than off the image, since labels are placed only where they fit.
6. Keep confidential data on the keyless path if it must not persist, and use the account path only when the chart has to keep updating.

## See Also

- [Bannerify MCP](/hermes/mcp/servers/external/bannerify-mcp) - the document rendering class, where an image is the deliverable rather than the input
- [Partsgraph MCP](/hermes/mcp/servers/external/partsgraph-mcp) - another keyless surface that answers a question from its own catalogue rather than from the open web
- [External MCP Server Catalog](/hermes/mcp/servers/external/) - every guide in this catalogue
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - the pass that found this server
