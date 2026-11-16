# Claims / Delivery — executive interview simulation

An independent, interactive portfolio-delivery case study by **SachinTechpro**. It is **not** a QBE system, a claim about QBE's actual technology/financials, or an implementation proposal. Based on the public-facing job description and hiring-context notes provided for interview preparation.

## Purpose
Demonstrate the difference between teams using Agile and portfolio governance using fixed project approvals. Explore how a hands-on Program / Delivery Manager manages an illustrative commercial and specialty insurance **Claims** value stream while transitioning toward outcome-oriented portfolio governance.

## What to show in 3–5 minutes
1. **Context**: currently Agile teams can still receive fixed waterfall project commitments; portfolio success should include business outcomes and guardrails.
2. **Initiatives**: Commercial Property FNOL, Workers' Compensation Triage, Cyber Incident Response. All examples use invented data.
3. **Delivery plan**: 11-month initiative roadmap, dependency map, operating roles and gates.
4. **Executive control room**: adjust integration delays and squad capacity; review schedule, estimate-at-completion (EAC), RAG and pilot gate.
5. **First 90 days**: listen/validate, establish integrated baseline, then pilot/adapt.

## Run locally
Serve the folder via any simple HTTP server:
\`\`\`sh
python -m http.server 8000
\`\`\`
Open http://localhost:8000/qbe-claims-briefing/ if serving from repository root; or http://localhost:8000 if serving within the demo folder.

## Test
\`\`\`sh
node --test qbe-claims-briefing/tests/model.test.mjs
\`\`\`
(From repository root.)

## Deployment
Static site: source branch \`qbe-claims-delivery-briefing\`, publish directory \`qbe-claims-briefing\`, build command \`node --test qbe-claims-briefing/tests/model.test.mjs\`. No runtime environment variables or secrets required.

## Design/assumptions
- Portfolio budgets, metrics, names, projects, team counts and timelines are illustrative.
- The hiring notes describe Agile teams and an existing waterfall-style change portfolio; they do **not** prove the precise current-state process or architecture.
- Financial forecasts are illustrative arithmetic for a delivery discussion, **not** probabilistic forecasts or actual actuarial calculations.
- Business KPIs are measurement *targets* to validate with business sponsors, never claimed outcomes.
- Value-stream leadership, PMO standards and business owners retain decision rights; the delivery manager coordinates execution and escalations.
- Zero customer data, zero external analytics, zero live integrations.
