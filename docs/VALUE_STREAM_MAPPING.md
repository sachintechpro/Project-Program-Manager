# Value Stream Mapping — Ternstone ValueOps

[Launch the live app](https://ternstone-valueops-demo.onrender.com/)

On any value stream card, select **◇ Interactive value map**. This models the **operational flow** from customer request to accepted business outcome; the existing development value stream and ART deliver its improvements.

## Six activities

1. Define customer value, beneficiary, trigger, accepted outcome, start/end boundary, exclusions, and regulatory/human approval constraints.
2. Invite Business, Product, SME, RTE, FDE/Engineering, Integration/DevOps, QA, Operations, Customer Care and Analytics. Record genuine meeting notes, attendees, disputed assumptions, decisions, actions, owners and due dates.
3. Capture current steps, source systems, touch time, waiting time, first-pass quality, rework and handoff pain.
4. Examine top waits and propose improvements tied to evidence, ownership, cost and risk.
5. Edit the proposed future flow, compare current/future modeled lead times and discuss implementation dependencies.
6. Record review decisions by the assigned roles, inspect revisions, export Markdown and propose a funded initiative through the existing Portfolio Kanban.

## Reference insurance process maps

| Stream | Current → future (illustrative) |
| --- | --- |
| Commercial and specialty underwriting: eligible submission to policy binding | 12.4 → 6.7 days |
| Commercial claims: FNOL to settlement/payment confirmation | 18.6 → 11.0 days |
| Cyber incident response: notification to assigned response partner | 9.1 → 3.6 hours |
| Commercial policy servicing and billing: request to confirmation | 5.2 → 2.1 days |
| Risk engineering: inspection referral to approved report | 21 → 12 days |
| Broker and distribution: inquiry to verified response | 4.6 → 1.8 days |

The 6 JSON files in `seed/maps/` are original read-only reference packs. Five derived CSVs (`value_definitions.csv`, `process_steps.csv`, `stakeholder_participation.csv`, `discovery_agenda.csv`, `improvement_candidates.csv`) enable inspection with stable stream keys.

## Permissions and evidence

Map edits are restricted to the original creator or assigned facilitator; each meeting note is editable only by its recorder. Reviews are signed by authorized roles for a **specific revision**, and an actual recorded workshop is required before confirmation. Changes to the map or meeting evidence make previous confirmations stale. Map confirmation does not change the LPM investment or initiative approval state.

The Markdown export includes value definition, process steps, modeled KPI calculations, actual recorded workshop notes, and current revision decisions. Audit events record changes, with historical snapshots retrievable through the API.

## Calculation and production caveats

Elapsed = active touch + waiting **clock hours**. Modeled flow efficiency = touch / elapsed × 100. Modeled first-pass yield multiplies step rates under a simplifying assumption. Do not claim the end-to-end median equals a sum of stage medians; measure actual case start/finish events with source-system telemetry. Monthly volumes, current/future durations, and improvement ideas are *fictional planning assumptions*.

The public Render demonstration uses ephemeral SQLite and simulated third-party data. For real enterprise use, deploy managed Postgres, SSO/ABAC, independent audit retention, secure event integrations and verified financial/operational measurements.

## Evidence-rich graphs and role decisions

Every process step now offers an interactive time bar on the **same scale** for current and future flows, showing active handling separately from waiting time. Select a bar to inspect the business input or outcome, system-of-record source to check, stakeholder handoff, required control, negative path and proposed improvement. An equivalent before/target paired chart highlights potential changes at each handoff. Every chart explicitly distinguishes modeled estimates from measured insurer performance.

The three additional small CSVs in `seed/maps/` are:
- `step_evidence.csv`: **72 rows**, keyed by value stream, current/future state and process-step ID, with operational artifacts, source evidence, handoff and exception.
- `role_review_guidance.csv`: **48 rows**, keyed by value stream and assigned review role, with the reviewer's decision question and required evidence.
- `workshop_questions.csv`: **30 rows**, keyed by value stream and agenda order; these are discussion prompts, not records of meetings held.

Review choices:
- **Approve**: a role-specific, evidence-supported acceptance of the mapping facts. A genuine recorded discovery workshop is required.
- **Decline**: formal rejection with the specific correction needed. A revision is needed before the rejected map can be approved by all.
- **Ask for more information**: an assigned reviewer requests particular data or evidence; the assigned mapping facilitator (never the same reviewer) replies with a traceable answer and optional source. The reviewer then issues a new decision. No automatic acceptance follows an answer.

The server checks assigned roles, evidence comment length, current map version and facilitator/reviewer separation. Each action enters the audit history. A map or meeting edit changes the mapping version and makes earlier role approvals stale. Mapping approvals and **LPM funding approvals remain separate**.

Use `pytest -q tests/` to run the 30 regression tests and `PYTHONPATH=. python scripts/browser_vsm_mobile_review.py` to exercise the mobile graphical views. The application source zip contains these test scripts and the supporting data catalog.

