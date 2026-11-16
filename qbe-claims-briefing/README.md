# Value / Delivery — Enterprise Portfolio Workbench

An interactive enterprise program and portfolio delivery demonstration by **SachinTechpro**.

**Live application:** https://claims-delivery-briefing.onrender.com/

## Explore the application

1. **Portfolio Explorer:** Explore seven value streams and 21 strategic initiatives spanning commercial and specialty insurance operations. Select a stream and initiative to update connected views.
2. **Delivery Lifecycle:** Follow ten governed stages from strategic intake and discovery through business case, mobilization, design, Agile execution, controlled release, operational adoption, benefits and closeout. Inspect stage inputs, outputs, PM responsibilities and approval evidence.
3. **Project Manager's Desk:** Explore charter, scope, investment assumptions, schedule, critical-path dependencies, staffing and vendor responsibilities, RAID, decision log examples, testing and operational transition.
4. **Executive Control Room:** Adjust delivery delays, temporary squad capacity, phased rollout and release gates. Examine the changing schedule forecast, estimate at completion, cost variance, RAG status and executive recommendations. Copy an executive brief.
5. **Transformation & LPM:** Compare project-centric change governance with value-stream-oriented prioritization, funding guardrails, operational outcomes and the roles of delivery management, business leadership and PMO.
6. **Delivery Capability Map:** Review program management, financial controls, technical fluency, stakeholder leadership, operational change, ethics and professional operating principles.
7. **Claims Deep Dive:** Open `claims.html` for a focused walkthrough of commercial claims intake and delivery decision-making.

## How the demonstration works

- Seven value streams each offer three initiatives with distinct commercial and specialty business problems, future-state improvements, dependencies and measurements.
- The selected initiative powers the project lifecycle, financial model, stakeholder map, risks, acceptance criteria, quality gates and executive reporting.
- Phase gates may be explored freely; simulated confirmations follow the lifecycle sequence.
- The financial model is a deterministic example of delivery trade-offs; it uses no backend and no live external integrations.
- Business KPI baselines and targets remain separate from actual post-release benefits, which must be measured by the business owner.
- The application supports responsive desktop and mobile layouts, contextual definitions and a guided tour.

## Implementation

- `index.html`, `workbench.css` and `workbench.js` provide the multi-stream workbench.
- `portfolio-data.js` contains the business and project model, lifecycle definitions, capability map and forecast logic.
- `claims.html`, `styles.css`, `app.js` and `model.js` preserve the separate Claims deep dive.
- `tests/` contains regression coverage for project data, lifecycle completeness, scenario math, navigation structure and script syntax.

## Run from the application directory

```sh
node --test tests/model.test.mjs
python -m http.server 8000
```

Open http://localhost:8000/.

## Operating principles

Strong portfolio delivery connects strategy, funding, capacity, iterative delivery and operational results, while retaining clear accountability for approved investments, scope, risk and release controls.

**Data note:** Initiatives, names, budgets, durations and outcome targets are sample data for demonstration.
