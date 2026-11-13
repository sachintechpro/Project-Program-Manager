# Data Validation & Verification Report — SAFe Agile Project And Program Management End to End Tool

**Release:** v1.4.0  
**Audit date:** 2026-11-12  
**Training snapshot:** 2027-02-19, explicitly fictional  
**Primary scenario:** Add / Replace Vehicle in an already-live customer self-service portal, with enterprise Okta work, PolicyCenter integration, possible document/e-signature dependencies and BAU support.

## Executive result

| Test category | Result |
|---|---:|
| Independent assertions against bundled seed | **149 passed / 0 failed** |
| Editable data registers | **25** |
| Total navigation sections | **29** (including new Audit) |
| Illustrative starting records | **113** |
| Register field definitions with contextual guidance | **177** |
| Additional workspace-setting guidance | **7** |
| Additional metric explanations | **20** |
| Browser widths checked | **320, 390, 740, 1280 px** |
| Full module rendering | **29 / 29 sections** |
| Built-in audit integrity errors on clean seed | **0** |
| Built-in management-review flags intentionally left visible | **3** |

This is an **internal arithmetic, chronology, structural and operational-consistency audit**, not independent confirmation of real company events. The dates, finances, roles and results are authored training assumptions. No live Jira, Guidewire, Okta, accounting, HR or compliance system was accessed.

## Corrections made

1. **Corrected the sample's time anchor.** The training environment now explicitly states an as-of date of 2027-02-19, after project start (2027-01-04) and charter authorization (2027-01-15). The prior seed reported actual costs while all milestones and sprints appeared not to have begun.
2. **Aligned charter and roadmap status.** The approved charter is completed; API/design forecasts are at risk rather than incorrectly marked done. Original baseline dates remain visible next to reforecasts.
3. **Reconciled sprint and PI figures.** S1–S3 now reflect completed work; S4 is in progress. PI-1 capacity, planned and done totals equal their four sprint components (156 / 140 / 100 relative planning points). The demo deliberately leaves 40 points planned against 38 available in S4, a realistic management-review scenario.
4. **Separated incompatible effort units.** Sprint/PI relative points are **not** resource person-days. Resource capacity uses people × working days − leave − production support − other commitments, with skill groups kept distinct.
5. **Corrected capacity calculation drift.** Available person-days are derived and read-only in the editor; changes in people, leave, support or other allocations recalculate availability. Bad imports are flagged.
6. **Separated base costs from contingency.** $1.05M base + $150k contingency = $1.2M authorized; $220k actual + $845k ETC = $1.065M EAC. This represents **$15k forecast reserve draw**, not $135k of savings. The remaining reserve is $135k.
7. **Clarified committed costs.** $53k future contractual commitments are included within the $845k ETC, not added a second time to EAC. Editor checks reject commitments larger than the remaining forecast for the category.
8. **Corrected dependency-watch logic.** “Open” and “at risk” are no longer treated as identical. The at-risk PolicyCenter API needed March 1 and forecast March 8 is counted as one flagged external dependency; other on-time but open coordination items remain visible without falsely inflating this risk count. RAID and dependency registers may describe the same risk and are not added together as unique events.
9. **Replaced fictional timeline marker spacing.** Milestone bars now reflect their real forecast dates on a shared timeline; original baseline ticks remain separately visible.
10. **Corrected program scope classification.** Enterprise Okta is an **external enterprise program**, not automatically part of a portal program. Claims FNOL is a separate portfolio idea. Related servicing projects are marked as possible **candidates** rather than invented approved program members.
11. **Clarified the quality-test denominator.** The quality register shows formal SIT/E2E/security/UAT release scenarios, not every unit or story-level test run during completed Scrum sprints. Eighty-three formal test cases are planned and three are blocked by integration readiness; completed sprint stories are not represented as untested.
12. **Defined the operational value-stream baseline.** Current time figures describe the **assisted/manual process** before self-service launches, using equivalent eight-hour business days. They are not presented as future-state digital performance or confused with agent-only handling time.
13. **Added validation guardrails.** Negative/invalid numeric inputs, missing/invalid required dates, duplicate IDs, impossible test counts, commitments above ETC and invalid WSJF job sizes are rejected or flagged. Program/Project views now have meaningfully different home summaries.
14. **Maintained the comprehensive SAFe/FNOL learning guide in a brand-neutral edition.** Named professional-organization attributions were generalized without removing the 13 instructional sections; the reference still provides a distinct FNOL training case alongside Add/Replace Vehicle. Text is intentionally not byte-for-byte identical to the original source.

15. **Removed organization-specific identifiers from the shipped training application.** Enterprise employer and insurer references in the sample banner, metadata, source generators, README and learning guide have been neutralized. Tool and platform terminology remains intact.

## Verified calculations

### Financial dashboard

| Item | Calculation | Result |
|---|---|---:|
| Approved base budget | Five cost-line baselines | $1,050,000 |
| Contingency reserve | Separate authorization line | $150,000 |
| Total authorized budget | Base + contingency | $1,200,000 |
| Actual cost through scenario snapshot | Sum of actuals | $220,000 |
| Estimated remaining cost (ETC) | Sum of ETCs | $845,000 |
| Estimate at completion (EAC) | Actual + ETC | **$1,065,000** |
| Forecast increase vs base | EAC − base | **+$15,000** |
| Forecast vs total authorization | EAC − $1.2M | **−$135,000** |
| Forecast reserve draw | max(0, EAC − base) | **$15,000** |
| Reserve remaining | $150k − draw | **$135,000** |
| Future committed expenditure | Included within ETC | $53,000 |

**Interpretation:** The earlier $1,065,000 EAC was arithmetically correct. The prior dashboard lacked the context that authorization included contingency, so it could incorrectly suggest $135k in genuine savings. The revised view makes that distinction explicit.

### Staffing and Agile delivery

| Group | Person-days per two-week window |
|---|---:|
| Portal development | 50 |
| Portal QA | 22 |
| PolicyCenter | 12 |
| Business SMEs | 8 |
| **Arithmetic total** | **92**, across different non-interchangeable skill groups |

For illustration, PI-1 sums S1–S4: capacity **40 + 40 + 38 + 38 = 156**, planned **34 + 31 + 35 + 40 = 140**, completed **30 + 28 + 32 + 10 = 100**. Those are team-relative planning points, not person-days.

### Quality, prioritization and process flow

- Formal release-oriented QA: **83 planned**, **0 passed so far**, **0 failed**, **3 blocked**, all within the test inventory. Sprint story-level testing is not included in this denominator.
- SAFe WSJF practice scores: policy servicing **2.625**, enterprise identity **4.600**, FNOL **1.538**. These are unitless relative scores, not monetary ROI estimates or automatic investment approvals.
- Manual vehicle-servicing value-stream model: **0.1075 active business days + 4.6 waiting business days = 4.7075 days**, flow efficiency approximately **2.28%**. These figures are **illustrative process-discovery assumptions**, not verified service-level data.

## Module-by-module review

| Module | Verified aspect and important limitation |
|---|---|
| Executive Command Center | EAC, milestone count, risk count, reserve breakdown and date-based timeline use same source data. |
| Data Integrity & Verification | Live audit explicitly separates actual field errors from management review flags. |
| Demand & Portfolio Kanban | Add/Replace approved, Okta independent, FNOL separate, Billing candidate. Actual funding decisions are fictional. |
| Business Case & Benefits | Baseline/target/current status separated; no fabricated post-launch actual results. |
| Charter & Scope | Approved charter and scope align with dated approval; removal and enterprise IAM rollout excluded from portal scope. |
| Stakeholders & RACI | Product Owner, Scrum Master, QA, technical teams, PM and sponsor have different authority boundaries. |
| Integrated Roadmap | Baseline/forecast dates consistent; slippage and recovery decisions remain visible. |
| Agile Epics & Features | Sample status aligns with earlier sprint progress, with epics explicitly multi-sprint. Not a full Jira export. |
| Sprint & PI Objectives | Four sprint point totals reconcile with PI-1; S4 overcommitment is intentionally flagged. |
| Cross-Team Dependencies | PolicyCenter required/forecast dates and escalation align with roadmap risk; Okta on-time item not miscounted as late. |
| Resources & Capacity | All four person-day formulas reconcile; current available value derived from source fields. |
| Budget & Forecast | Cost category sums, EAC, reserve use, committed cost inclusion and editable baseline reconciliation pass. |
| RAID Register | Issues, risks, assumptions and dependencies retain distinct categories and owners; overlapping descriptions aren't claimed unique. |
| Change Control | Vehicle removal is proposed but outside approved launch scope, requiring authorization. |
| Decision & Escalation Log | Named authority, options and deadlines; recommendations not treated as already approved. |
| Quality & Test Management | Counts sum correctly; formal test inventory is separate from sprint-level QA evidence. |
| Release Readiness | All future gates incomplete at the snapshot; formal Go/No-Go remains pending. |
| Hypercare & Operations | Thresholds are planned, not reported as actual production results before launch. |
| Vendors & Contracts | Illustrative vendor obligations and escalation paths, without false vendor-verification claims. |
| Security & Insurance Controls | Controls show needed evidence and approvers; no legal approval fabricated. |
| Status & Governance | Amber is consistent with unresolved PC API dependency and conditional downstream milestone forecast. |
| Recovery & Scenarios | Proposed recovery actions are pending, not shown as executed or as an approved rebaseline. |
| Program Coordination | Related candidates, actual project and external enterprise programs clearly distinguished. |
| SAFe & Lean Portfolio | Valid positive WSJF sizes and reproducible relative scores; explicit portfolio decision authority. |
| Value Stream Mapping | Current assisted operational flow and its units stated; not falsely labeled future-state portal performance. |
| Organizational Change | Training/adoption planned; no post-change adoption fabricated. |
| Project Closure | Deliverables remain pending prior to launch; benefits ownership continues beyond project closure. |
| Learning Academy | Ten fictional scenarios and coaching context retained. |
| Full Reference Library | Complete supplied guide preserved without summary replacement. |

## Three open, intentional management-review flags

These represent business situations to manage, **not calculation or data-integrity failures**:

1. **Forecast reserve draw:** EAC is $15,000 above the $1.05M base plan; confirm contingency approval and remaining financial exposure.
2. **Overloaded S4 plan:** Team plans 40 relative points against forecast capacity of 38; renegotiate commitment or validate feasibility.
3. **Late PolicyCenter API:** Interface needed 2027-03-01, currently forecast 2027-03-08; investigate downstream roadmap impact and make the recovery decision.

## Runtime regression tests performed

Browser-based tests rendered every section in Chromium at **320, 390, 740 and 1280px**, with **no page errors** after normalizing denied local-storage access in the sandboxed preview environment. Interactive scenarios tested changing available capacity from 22 to 20 person-days, enforcing read-only derived values, rejecting an invalid QA total, reconciling a changed budget baseline to workspace settings, displaying a distinct program overview, opening contextual mobile tooltips, and detecting deliberately injected invalid dates and QA numbers. The tests exercised the browser app as locally embedded HTML, because the execution environment blocks direct browser navigation to local paths and loopback URLs.

## Residual limitations and verification boundaries

- **Source authenticity:** All training values are hypothetical. No live source of truth was checked for actual costs, staffing, Jira stories, approval evidence, product eligibility, API readiness or insurer compliance rules.
- **Forecast quality:** Arithmetic consistency does not establish that estimates are realistic. Functional leads and Finance must verify assumptions and remaining work.
- **Project/Program governance:** Program relationships and financial approvals are illustrative. A company must formally define scope, roles and decision rights.
- **Persistent storage:** Local browser storage is not an audit trail, secure backend, role-based access system or multi-user database. Previous v1 local records may retain their older inconsistencies; the verified v1.4 training sample is loaded separately.
- **Live integrations and evidence:** No Jira/Confluence/Smartsheet/Guidewire/Okta data synchronization or automated approvals exist in this offline prototype.

**Verdict:** The released v1.4 sample passes its implemented 149 independent structural, numerical, date, cross-register and semantic checks, with 0 data-integrity errors and 3 deliberately visible management-review findings. It is suitable as a **coherent practice simulation**, not validated enterprise production data.
