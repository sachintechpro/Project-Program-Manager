# LEGACY GENERATOR — retained for historical traceability only.
# Running this would overwrite the audited v1.4 seed or guidance.
raise SystemExit('Legacy generator disabled: edit the v1.4 source JSON and run make_index.py instead.')

"""Detailed, context-specific guidance for every editable field in the demo.
Each entry: meaning | realistic example | confirm with | project/program decision impact.
Illustrative examples do not represent any actual insurance organization or project records.
"""
H = {
'intake': {
 'title': 'Short name of the proposed investment or change, not the Jira story title.|Add / Replace Vehicle self-service capability.|Requestor and product management.|Lets portfolio leaders identify and compare demand without confusing an idea with an approved project.',
 'type': 'Level of demand being considered; distinguish portfolio idea, independently managed project, and program.|Project — enhancement to an existing customer portal.|PMO or portfolio intake owner.|Determines which governance and funding path is appropriate; several teams do not automatically make a program.',
 'sponsor': 'Business executive or organization accountable for sponsoring the proposed investment.|Personal Lines Digital sponsor.|Business leadership / portfolio office.|Identifies who must justify value and seek initial funding approval.',
 'value': 'Business problem or outcome expected, not a description of software screens.|Reduce agent-assisted vehicle changes by enabling eligible customers to self-serve.|Business sponsor and Product Owner.|Enables business-value comparison and later benefits measurement.',
 'priority': 'Relative urgency agreed in an intake process; avoid treating requester enthusiasm as a funded commitment.|High — planned digital-servicing objective, subject to capacity review.|Portfolio governance and business owner.|Supports sequencing against competing Okta, portal, and claims initiatives.',
 'status': 'Current intake stage, rather than team sprint status.|Assessing; Approved for discovery; In delivery; Deferred.|Portfolio intake owner.|Distinguishes an idea under evaluation from one authorized for execution.',
 'decision': 'Exact portfolio decision and rationale, with approval scope if known.|Discovery funded; delivery authorization still requires an approved business case.|Named investment authority.|Prevents teams from treating preliminary exploration money as full-project approval.'},
'business': {
 'metric': 'Specific benefit or guardrail that can be measured after release.|Percentage of eligible vehicle-change transactions completed online.|Product analytics and business sponsor.|Determines whether the new capability actually delivers business value.',
 'baseline': 'Measured performance before the change; include units and observation period.|0% digital Add/Replace Vehicle completions in the old portal.|Analytics / operations owners.|Without a credible starting point, improvement cannot be demonstrated.',
 'target': 'Expected improvement by a defined date, agreed as a business hypothesis.|40% of eligible changes completed online six months after launch.|Business sponsor and product leadership.|Supports benefit prioritization and release/rollout decisions; not a guaranteed outcome.',
 'actual': 'Measured result to date using the same definition as baseline and target.|24% digital completion in the first post-release month.|Data analytics / service owner.|Triggers adoption investigation or continued investment if benefits lag.',
 'owner': 'Named person accountable for collecting and interpreting the business measure after project closure.|Digital Product Owner for completion rate.|Sponsor and Product Owner.|Prevents benefit measurement from ending when the temporary project closes.',
 'measurement': 'Source, calculation, frequency and segment used to calculate the metric.|Monthly portal analytics: completed eligible transactions ÷ eligible attempts.|Analytics lead / metric owner.|Makes results reproducible and helps avoid misleading averages.',
 'status': 'State of measurement or benefit realization, not code progress.|Baseline confirmed; Not measured; Improving; Off target.|Benefit owner.|Shows whether evidence supports the investment case.'},
'charter': {
 'item': 'The specific charter element being approved or clarified.|In scope, Out of scope, Funding authority, Business objective.|Project Manager and sponsor.|Organizes the agreement about what the project is and is not authorized to do.',
 'detail': 'Clear, decision-ready statement of the charter element with boundaries.|Replace Vehicle is included; standalone Remove Vehicle is excluded from initial launch.|Sponsor, Product Owner and subject-matter experts.|Avoids ambiguity when a new requirement is later proposed.',
 'owner': 'Person who validates or approves this charter line, not necessarily its author.|Sponsor for scope authority; PO for backlog details.|PMO / sponsor.|Shows where to obtain a binding answer before baseline approval.',
 'status': 'Whether this charter element is drafted, validated, or approved.|Draft pending sponsor sign-off.|Sponsor or delegated approver.|Prevents an unapproved six-month target from being presented as a committed baseline.'},
'stakeholders': {
 'name': 'Specific role, team or person the project depends on.|PolicyCenter transaction lead.|PM and functional manager.|Makes dependency and decision routing explicit.',
 'role': 'Role played in the project, not simply a job title.|Portal Product Owner; enterprise IAM program lead.|Functional lead.|Separates product, Scrum, engineering, PM, and program responsibilities.',
 'accountability': 'Outcome this stakeholder is responsible for delivering or assuring.|PolicyCenter lead owns endorsement API contract and readiness.|Stakeholder being named.|Prevents unclear ownership when a milestone slips.',
 'authority': 'Decisions the stakeholder can actually approve or escalate.|Sponsor approves scope/date tradeoff; PO orders backlog within delegation.|PMO / sponsor / relevant authority.|Avoids sending budget or release decisions to people without approval rights.',
 'engagement': 'How and when the PM should communicate with this stakeholder.|Weekly dependency review; monthly steering meeting.|Stakeholder / PM.|Sets a purposeful cadence rather than adding unnecessary ceremonies.',
 'status': 'Current engagement or decision-readiness level.|Engaged; Awaiting confirmation; Escalation needed.|PM after direct contact.|Reveals absent decision-makers or commitment gaps.'},
'roadmap': {
 'milestone': 'Verifiable integrated delivery outcome across teams, not a sprint task.|PolicyCenter contract approved for Add/Replace transactions.|PO, architect, delivery leads.|Used to test whether the overall release forecast is credible.',
 'owner': 'Single named lead accountable for evidence that this milestone is met.|PolicyCenter technical lead for transaction API readiness.|Producing team / functional manager.|Makes follow-up and escalation traceable.',
 'baseline': 'Original approved milestone date retained for change history.|2027-03-01 for integration contract readiness.|Sponsor-approved integrated plan.|Comparison point for variance; never silently overwrite after a slip.',
 'forecast': 'Most recent credible completion date based on delivery evidence.|2027-03-08 after PolicyCenter revises its estimate.|Accountable delivery lead.|Shows whether a delay moves SIT, UAT or production launch.',
 'status': 'Current milestone condition based on evidence and agreed tolerances.|At risk because test endpoint has no confirmed date.|PM with accountable lead.|Feeds project RAG and targeted management attention.',
 'dependency': 'Specific upstream input that must arrive before milestone completion.|PolicyCenter endorsement API contract and test endpoint.|Consuming and producing teams.|Exposes the true constraint instead of assuming all teams can work independently.',
 'evidence': 'Artifact, demonstration or approval proving milestone completion.|Signed API contract and successful portal contract-test results.|Accountable milestone owner.|Prevents optimistic progress reports based only on verbal assurances.'},
'backlog': {
 'key': 'Unique identifier in Jira or the delivery backlog.|AV-202 (example Jira feature key).|Product Owner / Jira administrator.|Lets the PM trace integrated commitments to detailed delivery evidence.',
 'type': 'Backlog hierarchy level used by this team; not every company uses identical Jira configuration.|Epic, Feature, Story or Enabler.|Product Owner / Agile delivery lead.|Prevents comparing a multi-sprint feature with a single story.',
 'title': 'User- or system-facing capability expressed clearly enough to identify work.|Calculate revised premium when an insured vehicle is replaced.|Product Owner and team.|Connects sprint work to the customer journey and release scope.',
 'owner': 'Person or team accountable for coordinating this backlog item; Jira assignee conventions vary.|PolicyCenter lead for premium calculation feature.|Product Owner / technical lead.|Provides a contact for estimates, blockers and evidence.',
 'pi': 'Planning Interval (PI) in which the feature is forecast or committed at ART level.|PI-1 for initial vehicle-change functionality.|ART / Product management and teams.|Aligns the feature with broader integrated planning, if the organization uses SAFe.',
 'sprint': 'Iteration currently forecast for the work; this can change through team planning.|Sprint 4 for Replace Vehicle calculation.|Scrum team / Product Owner.|Helps forecast feature readiness without directing the team’s Sprint Planning.',
 'points': 'Team-relative story-point estimate; not a universal measure of hours or performance.|8 points estimated by the team for a feature slice.|Developers / Agile team.|Provides local forecasting input; never add points across unrelated teams as standardized effort.',
 'status': 'Current workflow state in the team’s configured Jira process.|Ready, In progress, Blocked, In review, Done.|Team / Product Owner.|Shows delivery progress, but Done stories alone do not prove the release is ready.',
 'acceptance': 'Testable condition that demonstrates the intended capability works.|Replacement premium and effective date agree with PolicyCenter policy record.|Product Owner / QA / business SME.|Links requirements to demonstrable, accepted functionality.'},
'iterations': {
 'iteration': 'Sprint or PI identifier, using the team’s actual cadence and calendar.|S4, or PI-1 for a multi-sprint planning interval.|Scrum Master / RTE / planning coordinator.|Keeps team commitments separate from project milestone governance.',
 'goal': 'Outcome the team intends to demonstrate, not merely a count of tickets.|Customer can review premium impact for a replacement vehicle.|Product Owner and team.|Connects iteration progress to a meaningful capability.',
 'capacity': 'Estimated usable delivery effort for this iteration in the unit consistently used here.|45 team person-days available after planned support and leave.|Delivery lead / Scrum team.|Sets a realistic forecast before work is planned.',
 'planned': 'Amount of work forecast for the iteration, using the same unit as capacity.|40 person-days of planned effort; do not mix with story points.|Scrum team / delivery lead.|Reveals overload assumptions and supports forecast discussion.',
 'done': 'Work meeting the team’s Definition of Done at iteration close, in the same unit used for planned.|35 person-days of validated planned work (illustrative).|Scrum team / Product Owner.|Useful to inspect forecast accuracy; not a substitute for integrated functionality.',
 'confidence': 'Qualitative assessment of ability to meet the iteration or PI objective, backed by risks.|Low because PolicyCenter API is not ready.|Teams during planning and risk review.|Signals where management must remove cross-team obstacles.',
 'demo': 'Specific working behavior to show stakeholders in the review/system demo.|Replace Vehicle journey displays the PolicyCenter premium response.|Product Owner / delivery team.|Provides evidence of integrated outcomes rather than slide-only progress.',
 'status': 'Lifecycle stage of the iteration objective.|Planning, In progress, Achieved, Partially achieved.|Scrum team / RTE as applicable.|Allows inspection and learning without turning the PM into the Scrum Master.'},
'dependencies': {
 'deliverable': 'Exact upstream item another team must provide; avoid a vague label like “API dependency”.|Working PolicyCenter endorsement endpoint in the test environment.|Producing and consuming leads.|Defines what “ready” means for the handoff.',
 'producer': 'Team responsible for providing the deliverable.|PolicyCenter transaction team.|Producing organization lead.|Identifies who can make and fulfill the commitment.',
 'consumer': 'Team or workstream that cannot proceed without the deliverable.|Portal QA integrated-test team.|Consuming delivery lead.|Shows where slippage creates downstream impact.',
 'neededBy': 'Last date the consuming team needs the input to protect its plan.|2027-03-01 before scheduled portal integration tests.|Consuming delivery lead.|Key date for assessing schedule exposure.',
 'forecast': 'Producer’s latest evidence-backed delivery date, separate from the consuming need date.|2027-03-08 after API completion estimate changes.|Producer / delivery lead.|If after needed-by, trigger impact analysis and recovery options.',
 'impact': 'Concrete consequence if the dependency misses its need date.|SIT start moves seven calendar days; release forecast needs revalidation.|Consumer, QA and PM.|Used to prioritize escalations and make tradeoffs visible.',
 'owner': 'Person accountable for tracking and resolving this dependency through agreed channels.|PolicyCenter delivery lead with portal PM coordinating.|Producing/consuming managers.|Keeps the entry actionable; coordination ownership is not coding ownership.',
 'status': 'Current readiness and commitment condition.|At risk — API contract agreed but endpoint not deployed.|Producer and consumer.|Distinguishes a confirmed blocker from a possible late delivery.',
 'escalate': 'Date to raise unresolved risk before the dependency actually blocks the plan.|2027-02-15, ahead of March test need.|PM / dependency owner.|Provides time for staffing, sequencing or governance decisions.'},
'capacity': {
 'team': 'Delivery team or skill pool whose capacity is being forecast.|Portal QA team, PolicyCenter integration specialists.|Functional manager.|Identifies the source of capacity and possible shared allocations.',
 'skill': 'Specialized capability required; headcount alone can hide shortages.|Guidewire endorsement integration or E2E test automation.|Technical / QA lead.|Shows why spare frontend capacity cannot replace an unavailable PC specialist.',
 'people': 'Number of people available in this planning period, adjusted for actual allocation if necessary.|4 QA engineers assigned to portal work.|Functional manager / team lead.|Starting point for available person-day calculation; do not double-count shared people.',
 'daysPerPerson': 'Working days per person in this calculation period before specific leave/support deductions.|10 weekdays in a two-week sprint.|Team planning calendar.|Defines the period and unit; do not mix weeks, hours and person-days.',
 'leave': 'Person-days lost to PTO, holidays, or known absences across the team.|4 person-days of leave for the portal QA team.|Functional manager / team.|Reduces delivery capacity; do not subtract a holiday twice.',
 'support': 'Person-days reserved for production incidents, operations and ongoing portal maintenance.|8 QA person-days reserved for production support.|Service owner and QA lead.|Protects BAU commitments instead of promising all capacity to new features.',
 'other': 'Person-days committed to other initiatives, learning or non-feature duties not already deducted.|6 QA person-days for enterprise Okta regression testing.|IAM program lead / functional manager.|Makes competing enterprise assignments visible in release forecasting.',
 'available': 'Usable delivery person-days calculated from the other capacity fields.|4 × 10 − 4 leave − 8 support − 6 Okta = 22 days.|PM and team lead.|Should match the calculated capacity; validate skill mix and historical throughput.',
 'owner': 'Leader who confirms allocation and resolves staffing decisions within authority.|QA Manager for portal QA resources.|Functional leader / resource manager.|Identifies who can commit capacity; PM does not automatically control staffing.'},
'financials': {
 'category': 'Cost component or ring-fenced reserve being forecast.|Portal delivery; PolicyCenter integration; Contingency reserve.|Finance / PMO.|Allows cost drivers and protected contingency to be distinguished.',
 'baseline': 'Approved cost allowance for this category, using the same currency and period.|$420,000 for portal delivery over the planned project.|Sponsor-approved budget with Finance.|Reference against which forecast variance is calculated.',
 'actual': 'Cost recognized/spent to date, reconciled with Finance; not cash remaining.|$90,000 charged to portal delivery through the reporting cutoff.|Finance business partner.|Helps calculate estimate at completion and assess burn rate.',
 'etc': 'Estimate to complete: realistic remaining cost including future labor and vendor work.|$320,000 required to finish portal delivery.|Functional leads with Finance.|EAC = actual + ETC; do not treat ETC as approved remaining budget.',
 'commitments': 'Unpaid committed obligations already contracted or approved, checked for inclusion in ETC.|$10,000 open integration purchase-order commitment.|Finance / procurement.|Avoids overlooked liabilities and double-counting when forecasting.',
 'owner': 'Manager accountable for providing the cost forecast for this line.|Engineering Manager for portal delivery.|Finance / cost owner.|Ensures the PM can validate estimates and seek approvals.'},
'raid': {
 'id': 'Stable identifier used across status reports and decision logs.|R-002 for potential Okta/portal QA capacity conflict.|PMO / project manager.|Allows traceability and avoids duplicate risk entries.',
 'type': 'Choose Risk, Assumption, Issue or Dependency based on present facts.|Risk: Okta may reduce portal QA capacity; Issue: staff already reassigned.|PM with responsible lead.|Determines whether to mitigate likelihood, validate, resolve, or manage a handoff.',
 'description': 'Objective statement describing trigger or event and consequence; avoid generic “integration risk”.|PolicyCenter endpoint may slip beyond the SIT start date.|Risk or issue owner.|Makes the problem testable and actionable.',
 'impact': 'Consequence severity on schedule, cost, quality, customer or controls; use your organization’s scale.|High because a delayed endorsement API blocks integrated test exit.|PM with affected leads.|Drives escalation and prioritization based on project tolerances.',
 'likelihood': 'Estimated probability of a future risk; not applicable to issues that already occurred.|High after repeated missed API readiness checkpoints.|Risk owner / PM.|Supports mitigation focus; avoid false numerical precision.',
 'owner': 'Single person accountable for mitigation or resolution, even if others perform the work.|PolicyCenter lead for API readiness.|Functional lead / PM.|Prevents risks from sitting unowned in the log.',
 'due': 'Date by which the next mitigation action or evidence is expected.|2027-02-15 to confirm test endpoint availability.|Risk/issue owner.|Allows action follow-up before a release milestone is missed.',
 'mitigation': 'Practical action that reduces probability or impact, with accountable follow-up.|Agree API contract early and schedule contract testing before full SIT.|Technical lead and PM.|Produces a recovery path instead of mere RAG reporting.',
 'status': 'Open, Monitoring, Mitigated, Resolved, Closed or another organization-defined state.|Open — confirmation pending from PolicyCenter.|Risk/issue owner.|Distinguishes ongoing exposure from a closed item supported by evidence.'},
'changes': {
 'id': 'Unique change-control reference linked to approvals and roadmap history.|CR-001.|Change authority / PMO.|Supports traceability across the charter, plan and budget.',
 'request': 'Requested modification to scope, baseline cost, date or acceptance approach.|Include standalone Remove Vehicle in the initial release.|Requester / Product Owner.|Identifies whether this is backlog reprioritization or a material baseline change.',
 'impact': 'Summary of cross-functional scope, cost, technical, schedule, testing and compliance consequences.|Requires new PolicyCenter rules, two E2E paths and additional UAT.|PO, engineering, QA, finance, compliance.|Provides decision-quality tradeoffs instead of approval by enthusiasm.',
 'cost': 'Incremental forecast cost of the change; use currency and clearly distinguish cost from savings.|95000 additional project dollars (illustrative).|Finance and estimating leads.|Determines whether delegated funding thresholds are exceeded.',
 'days': 'Estimated movement to the integrated milestone or release, not raw work effort.|21 calendar days added to release forecast if scope is retained.|PM and delivery leads.|Makes the date tradeoff explicit.',
 'sponsor': 'Business owner/requester advocating the change; not necessarily the financial approver.|Personal Lines Business Sponsor.|Business sponsor / PO.|Connects decision to business justification.',
 'decision': 'Formal disposition and reason from authorized governance.|Deferred to a subsequent release after impact review.|Sponsor / change authority.|Ensures approved changes are reflected in plan and finance.',
 'status': 'Current stage of change analysis and approval.|Pending analysis; Submitted; Approved; Rejected.|PM / change authority.|Prevents implementing material changes without authorization.'},
'decisions': {
 'id': 'Stable decision reference for governance, risks and meeting minutes.|DEC-001.|PM / PMO.|Links the final approval to the issue it resolves.',
 'question': 'Precisely worded decision someone with authority must make.|Do we retain launch date if the Replace Vehicle API slips three weeks?|Project Manager with sponsor.|Focuses governance on a yes/no or explicit option choice.',
 'options': 'Feasible alternatives with clear scope, date, cost and risk consequences.|Resequence tests; split Add/Replace release; extend launch.|Affected delivery and business leads.|Prevents one-sided escalation without meaningful alternatives.',
 'recommendation': 'PM’s supported recommendation and assumptions; do not present as already approved.|Run an API spike, then choose scoped release if integration still slips.|PM after impact assessment.|Lets the authority decide with evidence rather than accept a vague blocker.',
 'authority': 'Person or forum with delegated power to make the decision.|Business Sponsor for scope/date tradeoff; Release Authority for Go/No-Go.|Sponsor / PMO governance map.|Prevents accidental approval by the wrong participant.',
 'due': 'Latest date the decision can be made without causing additional impact.|2027-03-03 before QA test window is lost.|PM and affected leads.|Identifies urgent decisions before the situation becomes irreversible.',
 'decision': 'Actual approved choice and any conditions, not merely what PM recommended.|Approve Add Vehicle first; Replace Vehicle follows after controls pass.|Named decision-maker.|Becomes authoritative input to scope, roadmap and release plan.',
 'status': 'Decision lifecycle: Requested, Pending, Approved, Rejected, Closed.|Pending sponsor review.|PM / decision authority.|Shows outstanding governance debt and aging approvals.'},
'quality': {
 'scenario': 'Insurance journey or control being validated; not simply a test-case count.|Replace Vehicle with future effective date and premium adjustment.|QA Lead and PO.|Shows test coverage for business-critical behavior.',
 'level': 'Type of testing used for this record.|E2E for portal → PolicyCenter → confirmation; UAT for business acceptance.|QA Lead.|Ensures technical and business validation are not conflated.',
 'owner': 'Accountable lead for execution/evidence; not the Project Manager automatically.|QA Lead for E2E; Business Lead for UAT.|QA / business management.|Provides a clear source for readiness reporting.',
 'planned': 'Number of planned scenarios/cases in this test slice with a defined counting method.|20 approved Replace Vehicle effective-date cases.|QA lead / test management tool.|Denominator for interpreting progress and remaining exposure.',
 'passed': 'Number that ran successfully with recorded evidence.|16 cases passed in the integrated environment.|QA lead / test run evidence.|Shows demonstrated coverage, not just attempted execution.',
 'failed': 'Number executed with an unmet expected result.|2 failures caused by incorrect premium effective date.|QA lead / defect tracker.|Feeds severity, re-test demand and release risk.',
 'blocked': 'Number that cannot execute because prerequisite, data or environment is missing.|2 blocked awaiting PolicyCenter test endpoint.|QA / environment owner.|Exposes external constraints affecting test exit.',
 'status': 'Quality readiness condition for this slice based on exit criteria.|At risk — 2 blocked scenarios and one unresolved high-severity defect.|QA Lead and business as applicable.|Informs release readiness without having PM override QA judgment.',
 'evidence': 'Link or reference to the test execution summary, defects and approvals.|Jira test run, defect IDs and PolicyCenter transaction trace.|QA Lead.|Allows sponsor/release authority to verify quality claims.'},
'release': {
 'gate': 'Specific readiness condition to be satisfied before deployment/customer exposure.|E2E exit criteria achieved and critical defects dispositioned.|Release Manager / control owner.|Makes the Go/No-Go checklist auditable.',
 'owner': 'Lead responsible for producing the readiness evidence.|QA Lead for E2E sign-off; Service Owner for monitoring readiness.|Release governance.|Separates test execution, operational readiness and PM coordination.',
 'evidence': 'Document, test result or runbook proving the gate was met.|QA completion report with outstanding defect disposition.|Gate owner / release authority.|Prevents “ready” status without evidence.',
 'due': 'Date readiness evidence must be available before the Go/No-Go meeting.|2027-06-11 for UAT sign-off ahead of release.|Release Manager and gate owner.|Protects time for review and remediation.',
 'status': 'Gate state, including explicit exceptions where allowed.|Not started, In review, Passed, Exception approved.|Gate owner / release governance.|Controls whether release recommendation is supported.',
 'approver': 'Actual authority that accepts this gate or grants an exception.|Security Lead for security finding; Release Authority for final release.|Company approval matrix.|Prevents PM from unilaterally accepting high-risk release conditions.'},
'operations': {
 'item': 'Service readiness or hypercare condition that must be tracked.|Failed policy transaction rate during initial launch.|Service Owner / operations.|Defines safe production operation after deployment.',
 'owner': 'Operational person accountable for monitoring and response.|Service Owner, incident commander or PolicyCenter operations lead.|Operations leadership.|Ensures support is not left with the temporary project team indefinitely.',
 'threshold': 'Agreed measurable exit or alert criterion, with unit and window.|Failed policy transactions below 2% for an agreed monitoring period.|Service/SRE and business owner.|Makes hypercare exit based on service stability rather than calendar alone.',
 'actual': 'Current observed operational measurement from monitoring or incident records.|1.1% failed transactions over the last 24 hours.|Service telemetry owner.|Determines whether rollout should expand, pause or recover.',
 'status': 'Readiness, active monitoring or exit status.|Monitoring; Threshold breached; Handover accepted.|Service Owner.|Provides visible accountability for support transition.',
 'evidence': 'Dashboard, incident review or signed handover supporting the status.|Production telemetry link and reconciled failed-transaction report.|Service Owner / operations.|Enables defensible hypercare exit decision.'},
'vendors': {
 'vendor': 'External company or provider with a documented delivery obligation.|Third-party integration services provider.|Vendor Manager / procurement.|Identifies the contractual counterparty, not an informal internal team.',
 'deliverable': 'Specific product/service the provider must deliver and acceptance criteria.|Integration support package and test evidence for contract milestone.|Vendor lead / delivery owner.|Lets PM compare promised work to actual acceptance evidence.',
 'contract': 'SOW, purchase order or service agreement governing the obligation.|SOW-2027-04, milestone 2.|Procurement / contract owner.|Connects schedule and scope decisions to commercial terms.',
 'due': 'Contractual or negotiated date for a deliverable.|2027-03-01 for approved interface support.|Vendor Manager and project plan.|Allows timely escalation and impact analysis.',
 'owner': 'Internal person accountable for vendor relationship and acceptance coordination.|Vendor Manager with architect verifying technical outputs.|Procurement / delivery lead.|Avoids treating the Project Manager as automatic legal contract owner.',
 'status': 'Current contractual/delivery condition.|On track, Awaiting acceptance, Delayed, Disputed.|Vendor Manager / PM.|Exposes commercial or acceptance blockers.',
 'escalation': 'Named governance/contact path and time limit for unresolved delivery problems.|Escalate missed SOW milestone to vendor account lead within two business days.|Vendor governance owner.|Provides a usable resolution path before cross-project delivery is affected.'},
'compliance': {
 'control': 'Business, security, legal or technical safeguard requiring verification.|Only authorized policyholders can submit a vehicle endorsement.|Security / compliance / underwriting owner.|Defines what risk must be controlled, not a generic “compliance done” checkbox.',
 'evidence': 'Test results, policy rules, audit logs or approved assessment proving the control works.|Okta access test evidence and PolicyCenter audit trail.|Control owner / QA / security.|Gives release authority evidence for acceptance or exception.',
 'owner': 'Named person responsible for verifying the control.|Security Lead for access control; underwriting SME for eligibility.|Compliance and functional management.|Ensures proper specialists interpret applicable requirements.',
 'status': 'Review, test and remediation condition.|Open pending state eligibility review; Verified after test sign-off.|Control owner.|Flags release blockers and unverified assumptions.',
 'approval': 'Recorded approval or exception from the authorized control owner.|Security approval ID SEC-114; conditional exception with expiry.|Control governance authority.|Prevents unsupported claims of regulatory or security clearance.'},
'reports': {
 'period': 'Reporting interval and as-of date; avoid mixing observations from different periods.|Week ending 2027-03-05.|PMO / reporting calendar.|Makes trends and forecasts comparable week to week.',
 'overall': 'Integrated project health against agreed tolerance, not average sprint colors.|Amber: PC integration threatens planned SIT date.|PM using PMO RAG rules.|Triggers visibility and appropriate escalation.',
 'schedule': 'Assessment of approved milestone dates against current forecast.|Red if release will miss baseline beyond agreed tolerance.|PM with milestone owners.|Makes schedule exposure transparent independent of team velocity.',
 'budget': 'Cost forecast versus approved authority, considering ETC and commitments.|Amber if EAC threatens contingency or approval threshold.|Finance / PM.|Warns of future overrun even if current spend is low.',
 'scope': 'Confidence that approved must-have functionality remains deliverable and controlled.|Green if Add/Replace scope unchanged; Amber if removal feature threatens scope.|PO / sponsor / PM.|Identifies uncontrolled expansion or threatened benefits.',
 'quality': 'Readiness trend from testing, defects, control outcomes and operational evidence.|Amber when E2E scenarios remain blocked by PC endpoint.|QA Lead / control owners.|Shows quality exposure, not a cosmetic test-completion percentage.',
 'narrative': 'Two- or three-sentence executive assessment of cause, impact and current action.|Portal sprint delivery on plan; PC endpoint slips one week, threatening SIT; impact assessment underway.|PM based on verified lead inputs.|Explains why RAG changed and what leadership should expect next.',
 'decisionNeeded': 'Exact action or choice requiring authority, with owner and required-by date.|Sponsor to choose phased release versus date extension by March 8.|PM / sponsor.|Turns the weekly status report into an actionable leadership tool.'},
'recovery': {
 'action': 'Concrete diagnostic or stabilization step to restore a credible delivery forecast.|Reassess integrated test readiness rather than counting completed stories.|PM and recovery team.|Moves recovery from blame to verified facts and options.',
 'owner': 'Person accountable for finishing the recovery action.|PM + QA Lead for integrated-state assessment.|Sponsor / functional lead.|Prevents recovery tasks from becoming unassigned suggestions.',
 'due': 'Decision or completion deadline for the recovery action.|2027-03-04 to deliver revised dependency plan.|Recovery lead.|Supports short checkpoints and timely sponsor intervention.',
 'status': 'Current progress and acceptance of the recovery action.|Open; In progress; Evidence reviewed; Complete.|Action owner.|Helps measure whether the recovery plan is actually being executed.',
 'evidence': 'Objective proof of completed assessment or recovery.|Updated integrated forecast with confirmed PC endpoint date and test impact.|Recovery owner / PMO.|Avoids relabeling a Red project Green without real improvement.'},
'program': {
 'initiative': 'Separately governed project or workstream coordinated within the wider business objective.|Add/Replace Vehicle portal project; related enterprise Okta rollout.|Program Manager / relevant PM.|Shows program scope without treating every dependent team as a program.',
 'manager': 'Lead responsible for this initiative’s own delivery commitments.|Portal PM for Add/Replace Vehicle.|Program governance / PMO.|Makes escalations go through appropriate project leadership.',
 'businessValue': 'Benefit the initiative contributes to the broader program, expressed as a business outcome.|Lower assisted policy-servicing effort.|Business sponsor / value owner.|Keeps program coordination focused on benefits rather than project count.',
 'baseline': 'Approved milestone/release date at initiative level.|2027-06-18 for portal release.|Individual Project Manager.|Supports comparison across initiative commitments.',
 'forecast': 'Latest integrated forecast provided by the accountable project lead.|2027-06-25 after portal PC dependency slips.|Project Manager.|Identifies combined program roadmap impact.',
 'status': 'Health of the initiative as agreed in governance.|Amber due to unresolved shared PolicyCenter dependency.|Owning PM / Program Manager.|Shows where program-level intervention is needed.',
 'sharedDependency': 'Resource, technical service, vendor or decision that affects multiple initiatives.|Shared IAM test window across portal and enterprise Okta rollout.|Affected PMs / integration leads.|Justifies program-level priority and capacity coordination.'},
'safelp': {
 'epic': 'Potential major portfolio investment or change initiative; not necessarily a Jira user story.|Digital policy servicing self-service modernization.|Portfolio / product leadership.|Item to analyze in portfolio Kanban and compare against available investment capacity.',
 'valueStream': 'Persistent end-to-end business or development flow that the investment enables.|Policy Servicing development value stream.|LPM / value-stream leadership.|Connects investment to long-lived teams and outcomes rather than temporary departments.',
 'businessValue': 'Relative business value score agreed using consistent local criteria.|8 on a 1–10 relative scale for improved customer servicing.|Business owners / portfolio participants.|One component of WSJF; not a dollar forecast or automatic investment approval.',
 'timeCriticality': 'Relative cost of delaying this investment or missing a window.|9 where regulatory or seasonal timing is important.|Portfolio leaders / business sponsor.|Contributes to Cost of Delay component of WSJF.',
 'riskReduction': 'Relative reduction in risk or creation of future opportunity.|7 where modernization retires a fragile integration.|Architecture, risk, and business stakeholders.|Represents Risk Reduction/Opportunity Enablement in WSJF.',
 'jobSize': 'Relative effort or duration compared with other epics scored using the same approach.|5 for a small initiative; 13 for a larger one.|Architect / delivery leads.|WSJF denominator; smaller size raises priority when other values are equal.',
 'status': 'Portfolio Kanban state and authorization stage.|Review; Analyzing; Implementing; Done.|Portfolio intake authority.|Prevents early-stage epic scores being mistaken for approved funding.',
 'decision': 'Explicit investment or capacity choice, with named authority and conditions.|Approved for discovery only, pending estimates and capacity review.|Investment committee / LPM authority.|Records why an epic was selected, deferred or stopped.'},
'value': {
 'stage': 'One real step in the customer-to-outcome flow; avoid grouping whole departments as stages.|Eligibility lookup before Add Vehicle submission.|Business process owner.|Makes handoffs and bottlenecks observable.',
 'workingDays': 'Active processing/touch time at the stage, measured in days; decimals are allowed.|0.02 days of actual system processing or staff handling.|Process analytics / operations lead.|Used with waiting time to calculate flow efficiency.',
 'waitingDays': 'Elapsed queue or waiting time excluding active work, in the same units.|1.5 days waiting on policy service or manual exception queue.|Process analytics / value-stream owner.|Shows that faster coding may not eliminate customer delay.',
 'owner': 'Business or service owner responsible for the stage’s operating result.|Policy Services owner for eligibility lookup.|Value-stream owner.|Identifies who can improve the bottleneck across functional boundaries.',
 'bottleneck': 'Observed constraint causing wait, rework or failures, supported by evidence.|Backend rating request queues while account eligibility is checked.|Process owner / operational data.|Focuses improvement investment on actual flow constraints.',
 'improvement': 'Proposed measurable change to eliminate or reduce the constraint.|Prevalidate eligibility before requesting a premium quote.|Business/engineering improvement owner.|Creates a testable hypothesis for cycle-time improvement.'},
'adoption': {
 'audience': 'Group whose day-to-day behavior changes when the new capability or operating model launches.|Customer service agents handling exceptions after self-service rollout.|Change lead / business owner.|Defines who needs communication and support.',
 'change': 'Specific process, role or decision behavior expected to change.|Agents handle exceptions rather than routine add-vehicle requests.|Business process owner.|Prevents transformation from being described only as software deployment.',
 'owner': 'Person accountable for adoption within this affected group.|Customer Operations Lead.|Business change sponsor.|Creates ownership beyond sending a training email.',
 'communication': 'Channel, timing and content explaining what changes and why.|Service bulletin and supervisor briefings two weeks before launch.|Communications/change management.|Aligns affected users before rollout.',
 'training': 'Concrete enablement activity tied to changed tasks.|Hands-on walkthrough for a failed endorsement and assisted recovery.|Operations trainer / service owner.|Reduces operational risk and makes training relevant.',
 'adoption': 'Actual usage or observed behavioral measure—not only training attendance.|80% of eligible agents use the new exception workflow after four weeks.|Change lead / analytics.|Provides evidence that the operating model is adopted.',
 'status': 'Readiness and adoption progress for the audience.|Planning, Piloting, At risk, Adopted.|Change owner.|Indicates intervention needs before and after launch.'},
'closure': {
 'deliverable': 'Formal closure condition or handover artifact that must be completed.|Operational handover accepted by the named service owner.|PM / sponsor / operations.|Prevents premature project closure after code deployment.',
 'owner': 'Person responsible for providing closure evidence or accepting transition.|Finance for final cost; Service Owner for production handover.|PMO and functional management.|Clarifies accountability for outstanding work.',
 'acceptance': 'Definition of done or sign-off required for this closure item.|No critical incidents and signed runbook acceptance.|Appropriate business/service authority.|Creates objective completion criteria.',
 'status': 'Current state of the closure action.|Pending, Awaiting approval, Complete.|Closure owner / PM.|Makes remaining handover or contract obligations visible.',
 'evidence': 'Document/reference showing the closure condition is satisfied.|Approved closeout report, final cost reconciliation, signed support handover.|Closure owner.|Supports auditability and future lessons learned.'}
}

METADATA = {
 'industry': 'Industry context used to adapt the training scenario.|Property & Casualty Insurance.|Workspace administrator.|The same delivery practices can be adapted to healthcare, banking or other industries.',
 'case': 'Name of the active sample initiative, independent of the portal product name.|Add / Replace Vehicle.|Workspace administrator / training lead.|Provides context for the registers and examples.',
 'portfolio': 'Strategic grouping within which this project or program is considered.|Digital Insurance Modernization.|Portfolio office / sponsor.|Helps connect work to investment and priority decisions.',
 'projectStart': 'Planning start date of the initiative; not necessarily first coding sprint.|2027-01-04.|Project Manager / sponsor.|Reference for integrated schedule and staffing.',
 'targetRelease': 'Proposed customer release date; clarify whether approved baseline or preliminary target.|2027-06-18.|Sponsor / release authority.|Used to test schedule and dependency consequences.',
 'budget': 'Total illustrative authorized project funding in dollars; the editable financial register separately stores detailed rows.|1200000.|Finance / sponsor.|Used for overall funding context; validate detailed cost baseline separately.'
}

import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
expected=json.loads((ROOT/'seed-data.json').read_text())['modules']
missing=[]
for module, records in expected.items():
    for key in records[0]:
        if module not in H or key not in H[module]:missing.append(f'{module}.{key}')
    if module in H:
        for key in H[module]:
            if key not in records[0]:missing.append(f'extra:{module}.{key}')
assert not missing, f'Uncovered or unrecognized fields: {missing}'
parsed={}
for module,vals in H.items():
    parsed[module]={}
    for field,raw in vals.items():
        parts=raw.split('|')
        assert len(parts)==4,(module,field)
        parsed[module][field]=dict(zip(('meaning','example','verify','impact'),parts))
parsed['__metadata__']={}
for field,raw in METADATA.items():
    parts=raw.split('|');assert len(parts)==4
    parsed['__metadata__'][field]=dict(zip(('meaning','example','verify','impact'),parts))
(ROOT/'field-guidance.json').write_text(json.dumps(parsed,ensure_ascii=False,indent=2))
print('Guidance complete:',sum(map(len,parsed.values())),'field descriptions across',len(parsed),'modules/metadata; unrecognized fields:',len(missing))
