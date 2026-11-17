# Ternstone ValueOps

### [▶ Open the live application on Render](https://ternstone-valueops-demo.onrender.com/)

**Start here:** [https://ternstone-valueops-demo.onrender.com/](https://ternstone-valueops-demo.onrender.com/) · **No account required for the public demo** · **Optimized for desktop and mobile**

**Operating System for Value Stream SAFe Agile Delivery Tracker**  
Commercial & specialty insurance · Lean Portfolio Management · SAFe-inspired Agile delivery · Evidence-based governance

Ternstone is an interactive portfolio-to-value delivery demonstration. **Visitors should use the application—not just read its documentation.** Choose a stakeholder role, follow a realistic insurance initiative, inspect the value stream maps, and make the role-specific decisions that move work through delivery.

> **Important:** Ternstone is a fictional insurer. Customer/financial figures, KPI targets, stakeholder workshop records and operational scenarios are modeled. Real insurer policy administration, claims, finance and external collaboration systems are not connected by default.

## Quick start — what to click

| Time | In the application | What you will see |
|---|---|---|
| 0:00 | **Open the live demo** and choose **Drew Silva — Program Manager** | A role-aware command center and left-side navigation |
| 0:30 | **Value Streams → Commercial Underwriting → Interactive Value Map** | Define value, meeting agendas, current-state map, wait-time charts, improvement ideas, future-state comparisons and reviewer decisions |
| 1:30 | **Initiative Journeys → Workers' Compensation submission** | Eight delivery stages with owners, contract artifacts, role controls, dependencies and evidence |
| 2:30 | **RACI Matrix** and **RAID Register** | Specific R/A/C/I stakeholder titles, risk owners, actions and due dates |
| 3:00 | Switch to **Tessa Reed — QA Lead**, then **Rowan Ellis — Release Manager** | A different set of allowed actions and independent approvals |
| 4:00 | Scroll the **left menu to its bottom → QA Test Bench** | Test strategy, real execution evidence, component coverage, API/performance data, known gaps, and independently recorded demo Go/No-Go decisions |

**Suggestion:** Start with one value stream and stay with it through its linked initiatives, artifacts, roles and test evidence. Changing personas demonstrates access control and separation of responsibilities.

## Guided tour 1 — From a business problem to a value stream

1. As **Program Manager**, select **Value Streams**, then **Interactive Value Map** on an insurance card.
2. Start with **Define Value**: identify the customer, trigger, accepted outcome, scope and mandatory human review.
3. Use **Meet Stakeholders** to see suggested Business, Product, Underwriting/Claims, Architecture, FDE, DevOps/Integration, QA, Security, Operations and Analytics involvement. Record your own notes and actions; example workshop prompts are not claimed as meetings that occurred.
4. Inspect the **Current State** flow and graphical touch-versus-wait time. Select a process bar to see its owners, source evidence, exceptions and handoffs.
5. Explore **Bottlenecks**, compare **Future State**, and open **Validate & Hand Off** to request information, decline or approve the map in an authorized reviewer role. This map confirmation **does not authorize portfolio funding**.
6. Return to **Initiative Journeys** to see how improvements become governed work.

Six usable insurance maps are included: **Commercial Underwriting, Commercial Claims, Cyber Response, Policy Servicing/Billing, Risk Engineering, and Broker Distribution**. Cycle-time numbers are illustrative hypotheses, not real measured operational results.

## Guided tour 2 — Execute an Agile portfolio initiative

| Stage | Practical work | Who decides? |
|---|---|---|
| 1. Portfolio | Define need, value hypothesis, investment and portfolio priority | Business / Lean Portfolio leadership and Finance, per control |
| 2. Product | Confirm requirements, business rules and acceptance criteria | Product and Business/Insurance SME roles |
| 3. Architecture | Identify interfaces, architecture, dependencies, ART readiness | Architects, integration and RTE stakeholders |
| 4. AI Execution | Build and document the technical implementation and review evidence | FDE / Engineering reviewers |
| 5. QA & Security | Validate requirements, defects, security and independent evidence | QA and Security leads |
| 6. Release | Confirm deployment, change approval and rollback | Release Manager and appropriate operations roles |
| 7. Operations | Confirm runbooks, support ownership and customer care | Operations and Customer Care |
| 8. Benefits | Compare verified outcomes to approved hypotheses | Business/value stream owner and Analytics |

**Try this:** Open a sample initiative, use **Generate Markdown contracts**, review its stage controls, switch to the assigned reviewer using the persona selector, then approve or request changes. Return to the initiative to see what remains before the next gate. Every stage is intended to preserve the record of who did what and why.

## Guided tour 3 — QA Test Bench and Go/No-Go

At the **bottom of the left sidebar**, choose **QA Test Bench**.

- **Start at Current readiness.** A **local demonstration GO candidate** is separate from **NO-GO for insurer production**.
- **Click “Check live readiness”** to run a lightweight, safe check of the current app and evidence files. This is not a traffic generator.
- **Examine Strategy & Adequacy**, component-level coverage, actual start/end and execution duration.
- **Filter the test case table** by passed, failed, blocked, not run, automated or manual. Test IDs link back to the source test names and evidence files in the full source archive.
- **Compare measured local p95 latency** with explicitly defined project test targets. Google Core Web Vitals and Google SRE benchmarks are listed for context but shown as **not measured** where no real field telemetry exists.
- **Review integrations:** simulated provider checks are not called live integration success.
- Switch to **Tessa Reed (QA)** to enter a demo-specific GO/NO-GO/Request Evidence decision; switch to **Rowan Ellis (Release Manager)** to make the independent release decision. All such decisions are audited and scoped **only to the demonstration**.

**Latest isolated QA execution:** 88 recorded cases: **77 passed, 0 failed, 5 blocked, 6 not run**. The 77 passed cases include 34 backend tests, 38 browser interaction checks, 3 bounded local load runs and 2 visual reviews. The blocked cases require real provider credentials; production soak, field Web Vitals, backup/restore and independent security checks are outstanding. See [Final QA evidence and Go/No-Go](docs/RELEASE_QA.md).

## Which stakeholder role should I pick?

| Want to evaluate… | Pick this persona |
|---|---|
| Integrated project/program planning, dependency and RAID tracking | **Drew Silva — Program Manager** |
| Strategic sequencing and investment controls | **Mara Chen — Portfolio Leader** |
| Product requirements and customer acceptance | **Leila Grant — Product Owner** |
| Agile Release Train and PI coordination | **Emerson Gray — Release Train Engineer** |
| Technical execution and implementation evidence | **Noah Park — FDE** |
| Independent test cases, validation and QA readiness | **Tessa Reed — QA Lead** |
| Deployment and release authorization | **Rowan Ellis — Release Manager** |
| Operational handover | **Samir Wells — Operations Lead** |
| Benefits measurement | **Olivia Kerr — Benefits Analyst** |

There are **29 modeled roles**. You can switch roles using the selector at the top of the workspace. Roles receive different documents, financial visibility and allowed actions; selecting a privileged platform role does not bypass business approvals.

## Additional things visitors can try

**Context help:** Select **? Help** on a page or field, or use the floating **Work assistant**. Ask *What should I do next?*, *Which approvals are assigned to me?*, or *Explain this number.* Guided answers work without external AI and do not make business decisions for you.

**RACI / RAID:** Add an assignment or risk with an authorized role. The R/A/C/I columns show the chosen stakeholder titles. Record ownership and review history separately from the author who entered the row.

**Evidence:** Export Markdown contracts or an initiative evidence ZIP. Inspect approvals, revision history and the audit ledger, with appropriate role visibility.

**Insurance data:** The examples are supported by **16 small normalized CSV tables** and six value stream mapping packs rather than arbitrary text on disconnected cards. Schema definitions and record IDs link requirements, rules, KPIs, tests and controls.

## What is working, and what is simulated?

| Capability | Implementation status |
|---|---|
| Role-based workspaces, eight delivery stages, approvals and audit | Functional in-app demonstration |
| Value stream maps, process graphics, stakeholder notes and reviews | Functional using modeled data, with editable records by authorized roles |
| RACI/RAID, contracts, versioning, exported evidence | Functional in-app demonstration |
| Role-aware guided help, QA Test Bench, demo Go/No-Go | Functional, scoped to the demonstration |
| Provider adapters (GitHub, Jira, Confluence, SharePoint, OpenAI) | Default **simulated**; live integration depends on explicitly configured scoped credentials and must be separately verified |
| Production monitoring, real insurer source-system KPIs and actual outcomes | **Not configured or verified** |
| Durable production data, enterprise SSO, formal security certification | **Not available** in the public free-tier demo |

**Persistence warning:** The public Render service uses SQLite on ephemeral storage. Data and demo sign-offs may reset after restart or redeployment. Do not put confidential information into this demo.

## Source, tests and deployment

**Live:** https://ternstone-valueops-demo.onrender.com/  
**GitHub branch:** [ternstone-valueops-deploy](https://github.com/sachintechpro/Project-Program-Manager/tree/ternstone-valueops-deploy)  
**Full source bundle:** [`Ternstone-ValueOps-Final-Source-QA.zip`](Ternstone-ValueOps-Final-Source-QA.zip)  
**Detailed QA results:** [`docs/RELEASE_QA.md`](docs/RELEASE_QA.md)  
**Value mapping guide:** [`docs/VALUE_STREAM_MAPPING.md`](docs/VALUE_STREAM_MAPPING.md)

This deployment branch intentionally keeps the runtime packaged as `ternstone-runtime.tar.xz` to isolate it from other tools in the shared repository. It contains `app/`, `seed/` and `requirements.txt`. The full source ZIP additionally contains the tests, QA evidence, scripts and explanatory documents.

For a local run from the full source bundle:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
export DEMO_MODE=true       # PowerShell: $env:DEMO_MODE="true"
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000`. Run backend tests on an **isolated disposable database**, for example:

```bash
DEMO_MODE=true SECRET_KEY=qa-local DATABASE_URL=sqlite:///./qa_fresh_test.db PYTHONPATH=. pytest -q tests/
```

To test locally, use `scripts/browser_final_qa.py` (Chromium, bridge to in-process FastAPI) and `scripts/performance_final_qa.py` (bounded local ASGI read traffic); neither script stress-tests public Render.

The Render service builds with:

```bash
tar -xJf ternstone-runtime.tar.xz && pip install -r requirements.txt
```

and starts with:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

For production use, implement managed PostgreSQL, migrations, backups and restore verification; SSO/MFA and finer-grained authorization; separate durable audit retention; production-grade security controls and monitoring; actual enterprise connectors; and business-verified source telemetry and benefit measurements.

---

**[▶ Start the interactive Ternstone ValueOps demo](https://ternstone-valueops-demo.onrender.com/)** · **[View the final QA report](docs/RELEASE_QA.md)**