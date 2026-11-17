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
