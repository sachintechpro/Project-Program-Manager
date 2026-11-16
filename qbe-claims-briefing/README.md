# Value / Delivery — Enterprise Portfolio Workbench
An independent, interactive Program / Delivery Manager case study by **SachinTechpro**.

**Live demo:** https://claims-delivery-briefing.onrender.com/

This is **not a QBE application**, a simulation of QBE's known internal data or technical environment, a claim of QBE endorsement, or a verified current-state transformation roadmap. The role requirements came from the user's attached *USA – Program Manager* job description and hiring-context notes. All detailed business cases, initiatives, schedule/cost forecasts, teams, role assignments, targets and risks are illustrative.

## 3–5 minute hiring-manager walkthrough
1. **Portfolio explorer:** Select one of **seven** illustrative value streams and one of **21** commercial / specialty insurance initiatives. Six are business-facing; Data & Control Foundations is explicitly an enabling stream.
2. **Delivery lifecycle:** Inspect 10 stages from strategic intake through discovery, business case, approvals, mobilization, design, Agile delivery, quality gates, rollout, benefits and closure. Stage gates can be simulated in sequence; the UI does not pretend to record actual approvals.
3. **PM delivery desk:** Walk through case charter, hypothesis, funding and contingency, integrated timeline, capacity and third-party relationships, risks / dependencies and decision responsibilities, quality and operations readiness.
4. **Executive control room:** Adjust delay, additional squads, phased rollout and release evidence. See schedule, estimate-at-completion, variance, RAG, sponsor decisions and recurring reporting. Copy a summary.
5. **Transformation & LPM:** Examine a move from fixed project approvals toward value-stream priorities, budget guardrails and outcome-oriented portfolio reviews. Distinguish sponsor/PMO authority from project-manager execution.
6. **Role / JD coverage:** Direct topic-by-topic traceability to the provided job description, preferred credentials, skills, cultural values and intake priorities.
7. **Archived original:** The original focused Claims briefing remains at **/claims.html#brief**.

## How data works
- Seven streams, each with three initiatives, are defined in \`portfolio-data.js\`.
- A selected initiative changes the KPI, LOB, process gaps, investment example, target, dependency, vendors, risk, financial model and stage examples.
- Ten phases cover intake through closure; the current phase can be inspected freely, but only sequential gate confirmations can be simulated.
- The forecast calculator is deterministic, illustrative and **not** a predictive model. Business benefits remain explicitly unmeasured.
- No live integrations, analytics, PII, vendor secrets or production customer data.
- Designed for desktop and mobile, with clickable contextual explanations.

## Technical structure
- \`index.html\`: new end-to-end value stream workbench.
- \`workbench.css\`, \`workbench.js\`: responsive UI and live interactions.
- \`portfolio-data.js\`: typed-like semantic domain data and financial model, no external dependencies.
- \`tests/workbench.test.mjs\`: initiative completeness, lifecycle, JD coverage, model logic and basic structural/script checks.
- \`claims.html\`, \`styles.css\`, \`app.js\`, \`model.js\`: preserved original Claims briefing.
- \`tests/model.test.mjs\`: original tests plus enhanced test suite.

## Test locally
From the repository root:

\`\`\`bash
node --test qbe-claims-briefing/tests/model.test.mjs
python -m http.server 8000
\`\`\`

Visit \`http://localhost:8000/qbe-claims-briefing/\`.

## Deployment
Current Render static site: \`claims-delivery-briefing\`.
- Repo: \`sachintechpro/Project-Program-Manager\`
- Branch: \`qbe-claims-delivery-briefing\`
- Publish directory: \`qbe-claims-briefing\`
- Build command: \`node --test qbe-claims-briefing/tests/model.test.mjs\`
- Auto-deploy: enabled

This change **does not** overwrite the original \`main\` branch or alter the separate project management service.

## Authenticity & boundaries
The specific QBE hiring-context notes describe a North American organization already Agile in many delivery areas, a waterfall-style change portfolio, and a movement toward value-stream funding and Lean Portfolio Management. They do not define QBE's actual number of value streams, portfolio operating cadence, project budgets, systems or delivery KPIs. Any example in this app must be validated with the real business sponsor and PMO before being used as a proposal. A candidate's employment history, certifications and measured outcomes require independent evidence.
