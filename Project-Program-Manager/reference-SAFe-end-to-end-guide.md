The best way to learn this is to follow one insurance initiative from customer problem to measurable business results—and examine who makes each decision along the way.

For a project or program manager, the central job is not assigning every developer’s work. It is creating a delivery system in which the right people make timely decisions about value, scope, funding, dependencies, risk, and production readiness. In an agile organization, product owners prioritize team backlogs, while delivery leadership coordinates capacity, technical dependencies, and the flow of work across teams.

I’ll interpret “safe agile” as **SAFe**, the Scaled Agile Framework. Below is a practical operating guide using a property-and-casualty insurance example. The company, financial figures, staffing, schedules, and targets are illustrative—not industry benchmarks.

## 1. First understand the roles: project, program, product, and value stream

These are different perspectives on the same investment.

| Perspective | Main question | Example in a P&C insurer |
|---|---|---|
| Project management | How do we deliver a defined change within agreed constraints? | Launch digital auto-claim reporting for an initial customer segment |
| Program management | How do related initiatives, dependencies, and organizational changes combine to produce benefits? | Coordinate digital reporting, claims-system changes, adjuster workflows, analytics, and training |
| Product management | What customer and business problems should we solve next? | Own the ongoing digital claims roadmap |
| Value-stream management | How do we improve the end-to-end flow of value, including building and operating the supporting technology? | Reduce delays from a customer reporting a loss to receiving an appropriate claims response |

SAFe distinguishes operational value streams—the activities that deliver value to customers—from development value streams, which build, support, and maintain the solutions enabling those activities. Its funding model emphasizes persistent value streams rather than repeatedly assembling temporary project teams. [scaledagileframework](https://scaledagileframework.com/lean-portfolio-management)

For your career, learn to distinguish these responsibilities even when one company combines several into a single job title.

A program manager and a Release Train Engineer, or RTE, may have overlapping responsibilities, but do not assume they are identical. The actual scope depends on the organization: delivery coordination may sit with an RTE while commercial contracts, investment governance, organizational change, and benefit realization sit elsewhere. Project and program responsibilities can overlap, but their authority and scope differ by operating model.

## 2. The running example: digital auto-claim reporting

Imagine an insurer receives this feedback:

> “After an accident, customers wait on the phone, repeat information, and cannot easily upload photos. Adjusters receive incomplete claims and call customers back.”

The proposed initiative is digital **First Notice of Loss**, or FNOL: letting customers report a loss, provide relevant details, upload documents or photos, and receive confirmation.

This is a realistic P&C technology scenario. Claims intake can integrate with policy lookup, assignment, triage, and underwriting or billing interfaces. A digital auto FNOL workflow can include vehicle and injury information, third-party details, photo uploads, and preferred contact methods. [guidewire](https://www.guidewire.com/products/core-products/insurancesuite/claimcenter-claims-management-software)

### Define the outcome before approving the solution

For this hypothetical initiative:

| Dimension | Illustrative baseline | Illustrative target |
|---|---:|---:|
| Median time to complete eligible FNOL | 25 minutes | 10 minutes |
| Eligible claims submitted digitally | 0% | 35% |
| Claims requiring follow-up for missing intake information | 30% | Below 15% |
| Customer experience | Baseline collected during discovery | Meaningful improvement |
| Safety measures | Existing operational baseline | No unacceptable increase in duplicate claims, errors, or service failures |

The point is not that these particular numbers are correct. It is that the sponsor approves a measurable business hypothesis, not merely “build a portal.”

## 3. Who are your stakeholders?

Your stakeholder map should identify four things:

1. Who owns the business outcome?
2. Who can authorize money or accept risk?
3. Who must contribute work or decisions?
4. Who will use, operate, or be affected by the solution?

Here is a proposed stakeholder map for the example. Exact titles and approval authority must be agreed with the insurer.

| Stakeholder | What they care about | What you need from them |
|---|---|---|
| Executive sponsor / claims executive | Claims service, operating cost, customer outcomes | Outcome ownership, funding sponsorship, escalation decisions |
| Portfolio leadership / investment committee | Strategic fit and competing investments | Investment authorization and priority |
| Product manager | Customer problems, roadmap, feature value | Clear priorities and scope trade-offs |
| Product owner | Team backlog and acceptance | Ready stories, acceptance criteria, rapid clarification |
| Claims operations and adjuster representatives | Accurate intake and workable processes | Process design, exceptions, business acceptance |
| Customer-service and agent representatives | Channel continuity and customer communication | Feedback, training needs, escalation paths |
| Engineering leads and teams | Feasible implementation and quality | Estimates, delivery plans, technical execution |
| Enterprise / solution architect | Integration, resilience, technical direction | Architecture decisions and dependency identification |
| Policy-system and claims-system owners | Correct interfaces and reliable operations | Integration capacity and interface commitments |
| Security, privacy, legal, compliance | Appropriate controls and regulatory interpretation | Requirements, reviews, documented approvals |
| Testing and quality specialists | Evidence that the solution works end to end | Test strategy, automation, defect transparency |
| Operations / SRE / service desk | Reliable service and supportability | Monitoring, runbooks, support acceptance |
| Finance and procurement | Cost, forecasts, contracts | Financial controls and vendor arrangements |
| Vendors / systems integrators | Contract scope and delivery obligations | Named deliverables and dependency commitments |
| Data and analytics | Reliable measurement | Instrumentation, baselines, outcome reporting |
| Project / program manager | Integrated delivery and decision flow | A coherent plan, visible risks, resolved dependencies |

The division between product and delivery matters: Backlog sequencing and acceptance sit with product ownership, while program coordination often includes capacity monitoring and alignment across teams.

### Make decision rights explicit

Use a simple decision register—not just a large RACI chart.

| Decision | Proposed accountable authority | Your role as PM / program manager |
|---|---|---|
| Is this investment worth pursuing? | Sponsor / portfolio authority | Present evidence, options, cost range, risks |
| Which features come first? | Product management | Show delivery and dependency consequences |
| How should the system be implemented? | Engineering / architecture authority | Ensure timely decisions and cross-team alignment |
| Can additional spending be authorized? | Delegated financial authority | Produce forecast and decision request |
| Are controls adequate? | Relevant control owner | Track evidence, findings, exceptions |
| Can we release to customers? | Named release authority under company policy | Assemble readiness evidence and recommendation |
| Who owns an incident? | Service owner / incident commander | Coordinate delivery-side support and communications |
| Did the initiative achieve its benefits? | Business outcome owner | Ensure measurement and review happen |

Do not accept “the committee owns it” without knowing who can actually decide.

## 4. How decisions move from feedback to production

SAFe uses portfolio Kanban to make large initiatives visible as they move from ideas through analysis and implementation. Portfolio leadership decides which deserve further investment; smaller improvements need not all become portfolio-level initiatives. [scaledagileframework](https://scaledagileframework.com/portfolio-backlog/)

The following is a proposed practical workflow—not a claim that every insurer uses these exact gates.

| Stage | Main question | Key participants | Evidence / deliverable | Possible decision |
|---|---|---|---|---|
| 1. Intake | Is there a real problem worth examining? | Business, product, customer-facing teams | Problem statement, feedback, initial data | Investigate, merge, defer, reject |
| 2. Discovery | What causes the problem, and who experiences it? | Product, claims SMEs, UX, engineering, analytics | Current process, baseline, options, constraints | Test a hypothesis or stop |
| 3. Investment analysis | Is the expected value worth the cost and risk? | Sponsor, finance, product, architecture, controls | Lean business case, cost range, MVP, risks | Fund discovery/MVP, revise, reject |
| 4. Delivery planning | Can teams deliver a useful increment? | Product, teams, RTE, PM, vendors | Objectives, capacity, dependencies, release forecast | Commit to a realistic plan |
| 5. Build and validate | Does the integrated solution work? | Teams, testers, business users, control owners | Demonstrated increments and test evidence | Accept, adjust, rework |
| 6. Release readiness | Can customers and operations safely use it? | Business, engineering, operations, release authority | Readiness pack, rollout and recovery plans | Go, conditional go, no-go |
| 7. Operate | Is the service stable and supportable? | Service owner, support, engineering | Telemetry, incidents, support metrics | Expand rollout, pause, recover |
| 8. Benefits review | Did the change improve the intended outcome? | Sponsor, product, operations, analytics | Results versus baseline | Expand, improve, stop further investment |

### Example: a genuine scope decision

During discovery, someone proposes automatic claim-payment approval.

That is not simply “one more screen.” It changes the business decision being automated.

For this example, you present two options:

- Initial release: collect claim information, create or update the appropriate intake record, confirm receipt, and route work to an adjuster.
- Later investment: evaluate automated decisions with separate business rules, controls, evidence, and outcome measures.

The sponsor and product leadership choose the business scope; engineering and control owners assess feasibility and safeguards. Your job is to make the consequences visible before the team inherits an unexamined commitment.

## 5. Organize the work around a value stream

For the example, map two connected flows.

### Operational flow

Customer experiences loss → reports loss → insurer captures and checks information → claim is triaged and assigned → investigation and adjustment → resolution.

### Development flow

Feedback → prioritization → discovery → design → implementation → validation → release → operation → measured learning.

These are related but not interchangeable. SAFe’s development value streams create and maintain the solutions used by operational value streams. An Agile Release Train, or ART, is a long-lived team of agile teams delivering—and often operating—solutions within that structure. [scaledagileframework](https://scaledagileframework.com/lean-portfolio-management)

### How to improve the flow

For the FNOL example, run a workshop with business, delivery, and operations:

1. Map the actual steps.
2. Record working time and waiting time separately.
3. Identify handoffs and rework.
4. Locate constraints: policy API access, claims SME availability, test environments, approvals.
5. Choose a small number of improvements.
6. Measure whether end-to-end delivery improves.

For example, faster coding will not materially help if every completed change waits three weeks for an integration environment.

Avoid calling every department a value stream. A useful value-stream view follows value across organizational boundaries rather than stopping at them.

## 6. Plan delivery in a SAFe environment

In SAFe, PI Planning aligns the ART’s teams and stakeholders around a shared mission and objectives. Portfolio priorities, product direction, team capacity, and cross-team dependencies must meet in that planning process. [scaledagileframework](https://scaledagileframework.com/glossary/)

For your example, suppose the insurer chooses a ten-week planning interval. That duration is an illustrative planning choice here.

### Before planning

As PM or program manager, coordinate preparation so that:

- Product priorities are clear.
- Teams have enough discovery to discuss the work meaningfully.
- Architecture and integration uncertainties are visible.
- Capacity reflects leave, support, and shared assignments.
- Vendors and dependent teams can state their commitments.
- Business SMEs have reserved time.
- Release and environment constraints are known.

Do not arrive with a fixed executive scope and ask teams to make the estimates fit.

### During planning

Facilitate agreements about:

- Business objectives.
- Team plans and dependencies.
- Integration milestones.
- Major risks and named owners.
- What can reasonably be forecast.
- What must remain conditional.

### After planning

Manage exceptions and decisions rather than recreating every team’s task board.

A useful dependency entry looks like this:

> Policy-services team must provide a production-representative test endpoint by June 12. Owner: policy-services lead. Consumer: FNOL team. Impact if missed: integrated testing moves two weeks. Escalation date: June 5.

That is more useful than “Policy API dependency—amber.”

### Separate deployment from release

Treat these as two distinct planning questions:

- Can the software be deployed into production safely?
- Should the capability be exposed to a particular customer group now?

For the example, feature flags and a controlled rollout can make those separate decisions possible. Whether the architecture supports that is something engineering must verify.

## 7. Budget planning: turn staffing into a credible forecast

SAFe’s Lean Budgets approach allocates funding to value streams, with guardrails for governance, rather than relying solely on temporary project funding. That does not eliminate the need to understand the cost and expected return of a particular initiative. [scaledagileframework](https://scaledagileframework.com/lean-portfolio-management-discipline)

Use two views:

- Value-stream view: what does it cost to sustain the teams and services?
- Initiative view: what capacity, incremental spending, and operating cost does this change consume?

### Illustrative six-month budget

Assume two teams with 16 full-time-equivalent staff in total. For this exercise, the blended fully loaded cost is $15,000 per FTE-month.

| Cost category | Illustrative amount |
|---|---:|
| Delivery teams: 16 × $15,000 × 6 months | $1,440,000 |
| Specialist vendor support | $180,000 |
| Incremental cloud, environments, and tooling | $90,000 |
| Training and operational readiness | $50,000 |
| Base estimate | $1,760,000 |
| Contingency allowance | $240,000 |
| Total proposed authorization | $2,000,000 |

These are assumptions, not market-rate estimates. State what the blended rate includes so you do not double-count architecture, management, benefits, vendor staff, or overhead.

Also separate one-time delivery expenditure from recurring production costs. Finance should determine the applicable accounting treatment.

### Track forecast, not just spending

Your financial dashboard should include:

- Approved budget.
- Actual cost to date.
- Remaining contractual commitments.
- Estimate to complete.
- Estimate at completion.
- Contingency remaining.
- Assumptions and confidence range.

Use:

\[
\text{Estimate at completion} = \text{Actual cost to date} + \text{Estimate to complete}
\]

A project can be “under budget” today because it is late and has not done the work. That does not make it financially healthy.

### Test the business case honestly

For the FNOL example, distinguish:

- Cash savings.
- Staff capacity released.
- Customer-experience improvements.
- Avoided operational risk.
- New recurring costs.

If employees spend less time on intake but staffing costs do not change, describe that as capacity released—not automatically as cash savings.

## 8. Resource planning: availability is not capacity

A staffing spreadsheet answers “Who is assigned?” A delivery plan must also answer “How much usable capacity exists, with which skills, at what time?”

Program leadership and delivery leads coordinate on capacity planning and monitoring. SAFe portfolio planning also emphasizes matching proposed work against available capacity.

### Illustrative team-capacity calculation

For one two-week iteration:

| Item | Person-days |
|---|---:|
| Eight people × ten working days | 80 |
| Leave and holidays | −8 |
| Expected production-support work | −12 |
| Planning, learning, and other non-feature work | −10 |
| Forecast available for planned delivery | 50 |

This is a local planning model, not a universal formula. Use historical evidence and avoid subtracting the same work twice.

Then check whether those 50 person-days contain the skills actually needed. Ten available frontend days cannot substitute for an unavailable claims-integration specialist.

### Common capacity constraints to investigate

For this case, explicitly check:

- Claims SMEs and business testers.
- Policy and claims integration engineers.
- Security and privacy reviewers.
- Test-data specialists.
- Environment support.
- Vendor specialists.
- Production-support coverage.

Also:

- Avoid treating people assigned to three initiatives as fully available to all three.
- Reserve capacity for production work.
- Do not compare story-point totals across teams as if they were a common productivity currency.
- Do not assume adding people late will immediately increase throughput.
- Preserve stable teams where possible.

Your staffing plan should include required dates and allocation—not just names and job titles.

## 9. P&C-specific questions that change the delivery plan

Claims technology is not only a digital interface. It connects policy information, claims workflows, assignment, data, and operational services. Claims management platforms illustrate these integration and lifecycle concerns. [guidewire](https://www.guidewire.com/products/core-products/insurancesuite/claimcenter-claims-management-software)

Use the following as a proposed discovery and testing checklist. Legal and compliance must identify the rules that actually apply to the product, jurisdiction, and process.

| Area | Questions to resolve |
|---|---|
| Policy context | Can the system retrieve the relevant policy information for the reported loss date? |
| Intake versus coverage decision | Does the interface clearly distinguish receiving a report from confirming coverage? |
| Complex losses | What happens with injuries, multiple vehicles, third parties, or incomplete information? |
| Duplicate reporting | What if the same loss is reported online, by phone, and by an agent? |
| Partial failures | What if the claim is created but photo upload or confirmation fails? |
| Catastrophe demand | Can intake and support operate during unusually high volumes? |
| Privacy and security | Who may access documents, photographs, and personal information? |
| Auditability | Can relevant actions and changes be reconstructed? |
| Accessibility and channels | Can customers complete the process, and is an assisted alternative available? |
| Operational ownership | Who handles records that require manual intervention? |

One especially important boundary: technical policy lookup is not, by itself, a final coverage determination.

## 10. Build production and support into the plan from the beginning

Do not define success as “development finished.”

For the FNOL example, propose explicit release-readiness criteria covering:

### Business readiness

- Agreed scenarios accepted by claims operations.
- Exception handling understood.
- Customer and employee communications prepared.
- Training and support material available.

### Technical readiness

- End-to-end integration demonstrated.
- Security findings resolved or explicitly accepted by authorized owners.
- Performance and resilience evidence reviewed.
- Monitoring and alerts tested.
- Deployment and recovery procedures rehearsed.

### Service readiness

- Named service owner and escalation contacts.
- Service-desk knowledge articles and runbooks.
- Agreed severity levels and response expectations.
- Vendor escalation arrangements.
- Hypercare staffing and exit criteria.
- A plan for incomplete transactions and data reconciliation.

A code rollback does not necessarily reverse business records already created. Ask engineering and operations how they will recover the business process, not merely redeploy an earlier software version.

### Define hypercare exit criteria

For example:

- No unresolved critical incidents.
- Transaction success meets the agreed threshold.
- Manual exception volume is manageable.
- Support can handle routine cases without the project team.
- Monitoring and ownership are operating as intended.

Support feedback should become product input, not disappear into a separate queue forever.

## 11. Your management cadence and dashboard

The following is a suggested starting cadence; adjust it to complexity and avoid duplicating meetings that already work.

| Cadence | Purpose | Expected output |
|---|---|---|
| Team-level, daily as appropriate | Coordinate work and surface blockers | Immediate actions |
| Cross-team, once or twice weekly | Resolve dependencies and integration issues | Owners, commitments, escalation |
| Weekly delivery review | Review forecast, risks, scope, cost | Updated integrated outlook |
| Every iteration | Demonstrate integrated progress and learn | Acceptance and backlog adjustments |
| Monthly steering review | Make investment and cross-functional decisions | Recorded decisions |
| PI boundaries | Align and inspect the broader plan | Objectives and improvement actions |
| Release-specific | Assess readiness | Explicit release decision |

### A one-page executive report

Include:

1. Intended outcome and current evidence.
2. Release forecast and confidence.
3. Financial forecast.
4. Top risks and issues.
5. Dependencies requiring intervention.
6. Decisions needed, by whom, and by when.

Instead of:

> “Testing is amber.”

Write:

> “The planned release is at risk because policy lookup is not integrated. Recommendation: retain the initial customer segment and defer broader rollout. Decision needed from the sponsor by Friday. A two-week extension is the alternative, subject to a revised cost forecast.”

### Measure more than activity

Use a balanced set:

| Dimension | Example |
|---|---|
| Business outcome | Digital completion rate; missing-information follow-up |
| Flow | Lead time, aging work, blocked time, work in progress |
| Predictability | Objectives achieved; forecast changes and causes |
| Quality | Escaped defects and repeat defects |
| Reliability | Failed transactions and service incidents |
| Finance | Estimate at completion and operating-cost trend |
| People | Sustained overload and critical skill concentration |

Avoid letting “tickets closed” replace evidence of working, useful, supportable software.

## 12. How to recover a project that is in bad shape

Start with assessment, not a new promise. Effective recovery requires establishing the current state, identifying root causes, recommending changes, and securing sponsor commitment to a recovery plan.

Suppose our example now has:

- Substantial spending with little integrated functionality.
- A release date six weeks away.
- Unfinished policy integration.
- Rising defects.
- Business testers who are not available.
- Team exhaustion.
- A sponsor who still sees a green status report.

### Step 1: Establish the facts

Create a short, time-boxed assessment:

- What works end to end?
- What is complete only in isolation?
- What remains?
- Which dependencies constrain delivery?
- What has been spent?
- What does the remaining work realistically cost?
- Which controls or operational needs remain unmet?
- Does the business case still justify continuation?

Review evidence and interview the sponsor, business owners, delivery teams, and operations. Do not use a blame exercise as a substitute for diagnosis.

### Step 2: Stabilize the work

Proposed actions:

- Stop uncontrolled scope additions.
- Give the backlog one authoritative priority order.
- Reduce simultaneous work.
- Resolve the highest-impact integration constraint.
- Obtain named business-testing commitments.
- Protect essential production support.
- Replace activity reporting with integrated demonstrations.

### Step 3: Present real options

| Option | What changes | What leadership must understand |
|---|---|---|
| Keep the date, reduce scope | Release a smaller useful capability | Benefits arrive in stages |
| Keep scope, extend time | Allow necessary delivery and validation | Cost and opportunity impact |
| Add targeted expertise | Address a specific skill bottleneck | Benefit is conditional, not guaranteed |
| Pause or stop | Avoid unjustified future investment | Existing expenditure does not justify further waste |

Recovery options can include scope reduction, schedule changes, process improvement, and redefinition of objectives where necessary.

### Step 4: Approve a recovery baseline

Record:

- Revised business objective.
- Retained and removed scope.
- Delivery forecast.
- Cost-to-complete.
- Named dependency commitments.
- Quality and release criteria.
- Escalation rules.
- Sponsor approval.

Do not quietly overwrite the old baseline. Keep the history and explain why the plan changed.

### Step 5: Rebuild trust with evidence

Use short checkpoints:

- Working integrated demonstrations.
- Defect and blocked-work trends.
- Dependency delivery.
- Updated forecast.
- Decisions completed.

Recovery is not making the status green. It is making the outlook credible and the remaining investment defensible.

## 13. A practical learning path for you

Use the FNOL case as a simulation and produce the following artifacts. This will build practical judgment faster than studying terminology alone.

| Phase | Learn | Produce |
|---|---|---|
| 1. Insurance and outcomes | Policy, claims, billing, FNOL, adjuster workflows | Business process map and problem statement |
| 2. Governance | Stakeholders, authority, escalation | Stakeholder map and decision-rights register |
| 3. Discovery | Baselines, hypotheses, options, MVP | Lean business case and scope boundaries |
| 4. Agile delivery | Product backlogs, team planning, integration | Epic-to-feature-to-story example |
| 5. SAFe coordination | Portfolio, ART, PI Planning, dependencies | PI objectives and dependency map |
| 6. Financial management | Cost, capacity, forecasts, benefits | Budget and resource plan |
| 7. Production ownership | Readiness, incidents, support | Release checklist and support model |
| 8. Recovery | Assessment, options, rebaselining | Troubled-project recovery proposal |

A manageable starter toolkit is:

- One-page charter.
- Stakeholder and decision-rights map.
- Prioritized backlog.
- Integrated milestone and dependency plan.
- Risks, assumptions, issues, and dependencies log.
- Budget and staffing forecast.
- Decision log.
- Release and support-readiness checklist.
- Benefits dashboard.
- Recovery plan when needed.

The test of effective management is whether you can answer, with evidence: What outcome are we pursuing? Who can decide? What is blocking flow? What will it cost to finish? Can we operate it safely? And what should we change when reality differs from the plan?