# Ternstone ValueOps

### 🚀 [Launch the Live Application on Render](https://ternstone-valueops-demo.onrender.com/)

**Live URL:** https://ternstone-valueops-demo.onrender.com/  
**Demo access:** Open the application, select a stakeholder persona, and use **How to use** to follow the guided journey. No external credentials are required for the public demo.

**AI-native value stream delivery · Lean Portfolio Management · Commercial & Specialty Insurance**

Ternstone ValueOps is an interactive enterprise delivery reference application. It connects **portfolio investment decisions → business and product requirements → FDE-assisted implementation → independent assurance → release → operations handover → benefits review** through versioned Markdown contracts, role-specific decisions, linked insurance reference data, and audit history.

It is designed to demonstrate how a SAFe-inspired organization could use AI to accelerate technical work **without removing human decision authority**. It does not use another insurer's proprietary data or branding.

> **Demo scope:** Real, working application workflows with modeled insurance records and simulated third-party integrations. The example investments, approvals, test cases, operational baselines and projected benefits are illustrative—not live insurer outcomes.

---

## Context help and role-aware work assistant

Select **? Help** in the header or the floating **Work assistant** on any page. Small **?** controls beside fields and CSV columns explain what to enter, give an example, and note relevant SAFe or validation rules.

The assistant understands your **signed-in role, current page and selected initiative**. Ask *What should I do next?*, *Which approvals are mine?*, *What evidence is required?*, or *Explain RACI/RAID*. It points to current role decisions and can highlight assigned RAID actions with recorded due dates. Guidance is read-only: it never approves, edits or deploys anything.

**Guided help works immediately without an external model.** Connected AI is optional, enabled only when an organization configures a live OpenAI connector and the user opts in for that request. Minimal role-scoped context is used rather than unrestricted records. See [Context Help and Privacy](./docs/CONTEXT_HELP.md).

---

## Try the complete initiative journey

1. **Start at the [live application](https://ternstone-valueops-demo.onrender.com/).** Select **Drew Silva — Program / Project Manager**, then open **How to use** for the walkthrough.
2. Open **Value streams** to inspect the six reference streams or create a new one.
3. Open **Initiative journeys → New initiative**. Select a value stream and a commercial or specialty insurance example, or start with a blank initiative.
4. Review **Scenario data**. The example imports linked requirements, business rules, fields, interfaces, test cases, risks, dependencies, cost assumptions, metrics, release checks and handover tasks. The original intake author can edit draft records.
5. Open **RACI matrix** and **RAID register** to create accountable assignments and track risks, assumptions, issues and dependencies. Only the record's author may revise it; authorized other roles have read-only visibility.
6. Open **Contract library / Initiative journey** to produce the stage's Markdown deliverables. Then switch to the relevant persona and use **Approval inbox** and **My role decisions** to approve, confirm, attest or request corrections.
7. Follow the initiative through the eight stage gates to operations handover and benefits closure. Download the initiative's evidence ZIP, review revisions and inspect **Evidence ledger**.

**Recommended first walkthrough:** A Workers' Compensation underwriting submission initiative. Review its business rules, planned QA cases, modeled cycle-time baseline and target, and different underwriting/product/engineering/quality approvals. The sample data is intentionally labeled and should not be confused with real measured business outcomes.

### Eight lifecycle stages

| Stage | Primary output / decision |
|---|---|
| 1. **Portfolio** | Portfolio epic, Lean business case, intake completeness and funding/sequence authorization |
| 2. **Product** | BRD, PRD, acceptance criteria and applicable business/insurance SME decisions |
| 3. **Architecture** | Technical plan, interface/data contract, architecture and ART dependency review |
| 4. **AI execution** | FDE implementation handoff, build evidence and engineering reviews |
| 5. **QA / Security** | Independent validation evidence, defects and applicable security/compliance reviews |
| 6. **Release** | Build-specific release approval, deployment and rollback readiness |
| 7. **Operations** | Runbook, support ownership and Customer Care handover |
| 8. **Benefits** | Measurement evidence, accountable business acceptance and closure |

Every required contract and mandatory role control must be satisfied before advancing. Approvals bind to a particular artifact version; later edits create a revision and can invalidate earlier approvals. Certain specialized reviews are conditional on the type and risk of the initiative.

## What's included

| Area | Capability |
|---|---|
| **Insurance portfolio** | 6 example development value streams and 9 initiatives across commercial and specialty lines |
| **Stakeholders** | 29 modeled roles with role-focused workspaces, information visibility and responsibility-specific control actions |
| **Contracts** | 108 example Markdown contracts with requirement-to-evidence lineage |
| **Reference data** | 16 small, normalized CSV tables; 550 modeled reference rows; schema and plain-English data dictionary |
| **Delivery governance** | Eight sequential stage gates, approval inbox, role decisions, RACI and RAID |
| **Editing** | Authorized creation and draft editing; author-only RACI/RAID updates; protected approved intake |
| **Evidence** | Document revisions, audit events, evidence exports and in-app event updates |
| **Integration center** | Simulated GitHub, Jira Cloud, Confluence Cloud, SharePoint/Microsoft Graph and OpenAI workflows |

### Example value streams

- **Underwriting and Quoting:** submission intake, completeness, underwriting rules and quote turnaround
- **Claims and Recovery:** commercial claims triage, evidence, reserves and coordination
- **Cyber Incident Response:** cyber coverage, response coordination and specialist workflows
- **Policy Servicing and Billing:** endorsements, billing reconciliation and policy service
- **Risk Engineering and Prevention:** commercial property inspections and risk recommendations
- **Broker and Distribution Experience:** broker submission status, document exchange and service transparency

The initiatives span Workers' Compensation, Commercial Property, General Liability, Cyber, Marine Cargo, Commercial Auto, Construction and multi-line distribution. Their modeled counts, budgets, benefit hypotheses and cycle-time targets are examples for evaluating the workflow.

## Roles, permissions and human decisions

The modeled organization includes executive leadership, Lean Portfolio Management, VMO, Finance, business owners, Epic Owners, Product Managers and Product Owners, RTEs, Project/Program Managers, Agile coaches, FDEs, engineers, architects, integration leads, QA, security, risk/legal, insurance SMEs, audit, vendors, release managers, operations, Customer Care, analytics and administrators.

**Roles see only the information needed for their responsibilities.** For example, QA receives test and validation information rather than portfolio budgets; Finance and authorized portfolio roles receive investment information. Platform administration does not automatically grant business-document approval or access.

A role's action may be **Approve**, **Confirm** or **Attest**, according to its authority. It is not a universal approval button. Required controls block the workflow; advisory reviews are recorded but do not independently authorize progression.

These control assignments model one fictional insurer's operating policy; they are **not** universal mandatory SAFe roles or artifacts.

## Editable, linked example data

The reference catalog is deliberately split into small CSVs rather than one large spreadsheet or an opaque JSON fixture:

```text
seed/
  value-streams/           # Markdown value-stream profiles
  scenarios/               # Initiative-specific Markdown contract examples
  contracts/               # Contract schema
  registers/               # RACI and RAID templates
  data/
    schema.json            # Data types, required fields and references
    value_streams.csv
    initiatives.csv
    business_steps.csv
    requirements.csv
    business_rules.csv
    data_fields.csv
    interfaces.csv
    test_cases.csv
    risks.csv
    dependencies.csv
    stakeholder_assignments.csv
    metrics.csv
    cost_estimates.csv
    release_controls.csv
    handover_tasks.csv
    role_approval_controls.csv
```

The reference data uses stable identifiers to link requirements, tests, interfaces, costs, metrics and the originating initiative. Validation checks missing mandatory fields, duplicate IDs, foreign-key references and cost/metric consistency.

**Source examples stay unchanged.** Creating an initiative copies its reference records into the application's versioned working records. The original author can update draft rows during portfolio intake. Once portfolio approval exists, the initial scope and assumptions cannot be silently rewritten. A complete controlled-change workflow remains a future enhancement.

Test cases begin as **not run**, and realized benefits begin as **unmeasured**. Planned evidence is not represented as completed execution.

## Application architecture

```text
Browser: role-specific responsive dashboard
                 |
         FastAPI application
        /      |         \
  Workflow   Contract    Integration
  and RBAC   revisions   adapters
        \      |         /
           SQL database
 Streams, initiatives, documents, approvals,
 role controls, revision history and audit events
                 |
        In-app event updates
```

- **Backend:** Python, FastAPI, SQLAlchemy; PostgreSQL-capable storage, with SQLite for this public demonstration.
- **Frontend:** Responsive HTML/CSS/JavaScript with role-scoped screens and editable forms.
- **Contracts:** Versioned Markdown documents with traceable references and evidence ZIP export.
- **Audit:** Application-level event history, digest checks and version-aware approvals.
- **AI:** Can produce reviewable planning drafts when an authorized provider is configured; it does **not** autonomously modify an enterprise codebase or production data.
- **Integrations:** Default to safe simulation. Live provider configuration supports limited credential verification and publication of approved contracts, **not full bidirectional enterprise synchronization**.

### Integration options

| Provider | Current supported demonstration |
|---|---|
| GitHub | Verify access and create an issue containing an approved contract |
| Jira Cloud | Verify access and create a Task |
| Confluence Cloud | Verify access and publish a Markdown-based page |
| SharePoint / Microsoft Graph | Verify approved access and upload a Markdown document |
| OpenAI | Generate a technical-planning draft for explicit human review |

Provider credentials and permissions must be configured by an authorized administrator; none are bundled with the demo.

## Run locally from this deployment branch

This branch intentionally packages the deployable runtime in **[`ternstone-runtime.tar.xz`](./ternstone-runtime.tar.xz)** to isolate Ternstone from the repository's other application branches.

```bash
git clone --branch ternstone-valueops-deploy --single-branch \
  https://github.com/sachintechpro/Project-Program-Manager.git
cd Project-Program-Manager

tar -xJf ternstone-runtime.tar.xz
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Example on macOS / Linux
export DEMO_MODE=true
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open **http://127.0.0.1:8000**.

The **complete development source package** (including tests, data validation scripts, documents, and Docker configuration) is distributed separately from this deployment-only branch. When using that package, run `pytest -q tests/` and `python scripts/validate_reference_csv.py`. The deployment archive itself contains `app/`, `seed/` and `requirements.txt`, but not the full testing/tooling tree.

### Render deployment

**[Open deployed instance](https://ternstone-valueops-demo.onrender.com/)** · [Render service dashboard](https://dashboard.render.com/web/srv-dbtvhb0u01pc73d7s7eg)

Render extracts the runtime archive, installs requirements and launches `uvicorn app.main:app --host 0.0.0.0 --port $PORT`. The current demonstration uses `DEMO_MODE=true` and SQLite on a free instance.

**Important:** SQLite data on this instance is not durable across restarts or redeployments. Do not rely on the public demonstration for permanent project records.

## Production-readiness boundary

This is a functional, auditable **reference implementation**, not a certified production insurance platform. Before connecting actual company data or operating a real insurer's delivery process, the implementation needs:

- Persistent managed PostgreSQL, schema migrations, backups, restore/DR procedures and monitoring.
- Enterprise SSO/MFA, user lifecycle management, initiative/LOB-level authorization and regular access reviews.
- Hardened secrets, encrypted data handling, rate limits, penetration testing and accessibility validation.
- Independent, durable audit retention beyond application-local event digests.
- Secure, organization-approved integrations, webhook verification, retries, reconciliation and provider-specific scopes.
- Real source-system operational telemetry and Finance-validated financial actuals/realized benefits.
- Production AI execution controls, independent quality evidence and explicit change-management authority.

The application demonstrates **how the governance, role decisions, documents and evidence connect**. It does not claim to be connected to a live carrier's underwriting, claims, billing or financial systems.

---

**[▶ Launch Ternstone ValueOps](https://ternstone-valueops-demo.onrender.com/)** · **[View deployment branch source](https://github.com/sachintechpro/Project-Program-Manager/tree/ternstone-valueops-deploy)**
