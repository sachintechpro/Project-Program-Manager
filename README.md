# ValueStream HQ | IT Project & Program Management — v1.5

**Tagline:** tool that helps people learn, practice, and confidently manage real IT projects and programs.

**[Launch the live application](https://project-program-manager.onrender.com/)** · [Project source](https://github.com/sachintechpro/Project-Program-Manager)

A responsive offline learning and delivery-management dashboard for enterprise Agile Project Managers, Program Managers, and transformation leaders. Its primary fictional training case is **Add/Replace Vehicle** in an existing insurance customer portal, alongside PolicyCenter dependencies, enterprise Okta integration work, optional DocuSign, ongoing production support and SAFe/value-stream coordination.

## Run it

Open **`index.html`** in a modern web browser. No backend, external JavaScript packages, subscriptions, internet connection or keys are required. On mobile, use the hamburger navigation and **Tools** menu. On desktop, use the persistent left navigation.

The application contains **30 sections**, including a new **Data Integrity & Verification** section, **26 editable register modules**, **114 illustrated records**, **182 register parameters with contextual guidance**, **7 workspace settings**, **20 explained metrics**, and **10 guided practice scenarios**. The full digital FNOL / SAFe training reference is included in a brand-neutral edition in `reference-SAFe-end-to-end-guide.md` and in the in-app Full Reference Library.

## Verified training snapshot

The corrected training seed represents a fictional snapshot **as of 2027-02-19**, about seven weeks after the simulated project start (2027-01-04). It is explicitly **fictional data, not an assertion about events at any real insurance organization**. The project charter was approved 2027-01-15; 1 of 7 integrated milestones has been completed, earlier Scrum sprints delivered some work, and a PolicyCenter API forecast threatens downstream milestones. The formal test register covers integration/end-to-end/security/UAT cases only; sprint-level story QA is performed by Scrum Developers and is not fully represented in this illustrative register.

### Financials

- Base cost estimate: **$1,050,000**
- Contingency reserve: **$150,000**
- Total authorized budget: **$1,200,000**
- Actual cost: **$220,000**
- Remaining ETC: **$845,000**
- EAC = actual + ETC: **$1,065,000**
- Expected reserve draw = EAC above base costs: **$15,000**
- Remaining reserve: **$135,000**
- Future contractual commitments: **$53,000**, **included** within ETC rather than added to EAC again.

An EAC below authorization is **not automatically realized savings** when authorization includes contingency. The data uses realistic arithmetic but wholly fictional amounts; it is not a benchmark or source-verified financial forecast.

### Effort units

- The **Resources & Capacity** register calculates *person-days per two-week window by skill type*. Its four teams have 50, 22, 12 and 8 available days respectively. The total 92 days are **not interchangeable** across specialties.
- The **Sprint & PI** register uses a separate illustrative relative **planning-point scale**. Do **not** interpret 40 points as 40 person-days or compare point values across independent teams.
- **PI-1** aggregates the sample S1–S4 capacities, plans and delivery totals. S4 deliberately shows a two-point overcommitment for practice.
- The **Value Stream Mapping** register models the **current-state assisted/manual servicing process**, not the not-yet-launched self-service journey. It uses 8-hour business-day equivalents for active and waiting time; 18-minute agent handling time is just one component.

## Audit and verification

Open **Data Integrity & Verification** for live checks on costs, chronology, dates, capacity, iteration rollups, QA counts, WSJF inputs and cross-team dependency forecasts. It distinguishes **data errors** from **management reviews**. The initial data contains **zero internal errors** and **three intentional management-review flags**: forecast use of contingency, a sprint with more planned than available points, and a PolicyCenter interface forecast later than its needed-by date.

For a repeatable independent source-data check, run:

```bash
python verify_workspace.py
```

The bundled audit has **149 assertions** against the seed and does not modify records. See `VALIDATION_REPORT.md` and `validation-results.json`. Browser smoke tests also checked all 29 sections at 320px, 390px, 740px and 1280px, the separate Program view, editable financial baselines, capacity recalculation, rejection of invalid QA counts, tooltip interaction and injected errors.

**What remains unverified:** No source system is connected. Real project spending, approvals, regulatory compliance, people allocations and test execution evidence can only be verified against authoritative owners and source records. The app is an educational prototype, not a certified portfolio governance system or a secured multi-user enterprise platform.

## Practical use

- **Jira / Rally:** Team epics, features, stories, defects and sprint evidence. The integrated dashboard does not replace a Scrum team's backlog or make a Project Manager the Scrum Master.
- **Confluence / SharePoint:** Charter, process, decisions and governance support.
- **Smartsheet / MS Project equivalent:** Integrated roadmap, dependencies, milestone forecasts and decisions.
- **Finance / PMO:** Validates cost baselines, actuals, remaining forecasts and approvals.
- **SAFe:** Portfolio, value-stream, PI and shared planning logic is *illustrated*, not a claim that a named insurer uses these particular structures.

Data edits live in the browser's local storage when supported. Export workspace JSON for backup. To avoid silently replacing prior edits, v1.4 introduced its own storage key; the previous v1 workspace remains in old browser storage and may be opened from the home page where available. Previous records may contain inconsistencies, which the audit will flag.

## Source code and rebuilding

`index.html` embeds the full CSS, JavaScript, records, guidance and reference text. Editable sources are `app.js`, `audit.js`, `styles.css`, `seed-data.json`, `modules.json`, `field-guidance.json` and `reference-SAFe-end-to-end-guide.md`.

Run `python make_index.py` to regenerate the standalone HTML after source edits. `build.py` and `field_help.py` are retained legacy-generation scripts from the earlier sample and **must not be used to replace the reconciled v1.4 dataset/guidance**. They have guards to avoid accidental overwrite. `reconcile_seed.py` and `update_app.py` are historical migration records; they are not part of normal rebuilding. `verify_workspace.py` checks the released seed without changing it.

## Brand-neutral presentation (v1.5)

The shipped application, training seed, field help, learning guide, documentation and source-generation scripts use **no real insurer, employer, recruiting agency or professional-association names**. Names of technologies, software products and frameworks (for example Jira, Confluence, Smartsheet, PolicyCenter, Okta, DocuSign, Guidewire, and SAFe) are retained as product references only. The fictitious sample does not claim affiliation with any software vendor.

Existing browser data, imported workspace JSON and manually entered records belong to the user and may include names the user previously entered. Version 1.4 starts with a distinct storage key so the generic seed does not silently load older content. Use **Reset sample** to return to the supplied generic example.

Repeat the source audit with `python verify_brand_neutral.py` and rebuild using `python make_index.py`.

## Context Help Assistant (v1.5)

Select the **Ask for help** launcher at the lower right on any page. The assistant detects the current module and switches its suggested questions when you navigate. It can explain each module’s objective and management actions, answer questions about fields and KPI parameters using the existing detailed guidance, use the **current local training records** for cost/forecast/RAID/dependency/capacity/QA summaries, and link to a related register. In any parameter tooltip, choose **Ask about this parameter in chat** to transfer its context. Questions remain in this browser session during page navigation.

This is a **deterministic offline contextual assistant**, **not a generative AI service**. It does not invent answers to arbitrary questions, send messages anywhere, fetch live data or change project records. Guidance and calculations are based only on local demo data and should not be mistaken for real business approvals or insurance-system data. The core app remains usable without enabling any API key, internet access or subscription. Source logic: `chat-assistant.js`, included in the standalone `index.html` by `make_index.py`.

### Context assistant regression check

Run `python test_chat.py` (requires Python Playwright and a local Chromium executable). This checks all 30 modules and every section’s three suggested help questions, changes to local financial forecasts, desktop/mobile chat interaction, contextual parameter handoff and display sanitization. Results are written to `chat-test-results.json`.

## Editable project and program examples

Open **Add project or initiative** and load **Personal Auto Modernization** for a SAFe delivery program with three linked projects: Policy Self-Service, Billing & Payments, and Digital Claims Intake. The program overview rolls up costs and forecasts and shows the steering decision about a late premium event. Load **Vehicle Self-Service** to practice with a separate standalone project.

Each project starts mid-delivery on March 5, 2027, with a named team, RACI, PI and iteration records, scope, costs, dependencies, decisions, QA evidence, release and operations plans, and all other management registers populated. To see the linked flow, open Policy Self-Service and adjust the forecast for the endorsement premium event. Then open Billing & Payments or return to Program view to see the downstream readiness impact.

Example sources are under `examples/personal-auto/` in the application directory. After editing these sources, run `python embed-example.py` and `python make_index.py` from that directory. Existing example workspaces stay editable in the browser. The expanded templates load as separate workspaces so prior edits are retained.

For two additional standalone examples, use **Add project or initiative → Choose another project template**:

- **Finance Reporting Migration** — an Amber month-end cutover with two unresolved reconciliation failures and a pending sponsor decision.
- **Mobile Dispatch Pilot** — a Green branch rollout with offline device tests, shift training, and a loaner plan.

Both populate all 26 management registers. The source data is in `Project-Program-Manager/examples/project-templates.json`.
