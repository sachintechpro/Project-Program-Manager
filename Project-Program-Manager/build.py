# LEGACY GENERATOR — retained for historical traceability only.
# Running this would overwrite the audited v1.4 seed or guidance.
raise SystemExit('Legacy generator disabled: edit the v1.4 source JSON and run make_index.py instead.')

import json, pathlib, html, re
root=pathlib.Path('/mnt/data/safe-agile-end-to-end-tool')
raw=pathlib.Path('/mnt/data/Pasted text(20261112-074815).txt').read_text()
(root/'reference-SAFe-end-to-end-guide.md').write_text(raw)
sections=[
('overview','Executive Command Center','layout-dashboard','Portfolio and project health, commitments, decision requests and training launchpad','Always separate team-level progress from integrated project delivery, financial exposure and measurable customer outcomes.'),
('intake','Demand & Portfolio Kanban','inbox','Ideas, strategic fit, triage and investment decisions','A request is not automatically an approved project. Capture the customer problem, expected value, options, sponsor and portfolio decision.'),
('business','Business Case & Benefits','target','Outcome hypothesis, baseline, measurable target and benefit ownership','Quantify current state, target, operational benefits, cost, evidence and benefit owner. Capacity freed is not automatically cash saved.'),
('charter','Charter & Scope','file-text','Charter, project boundaries, acceptance, exclusions and authorization','A sponsor approves the project mandate and authorized constraints. A date proposed by the business is not automatically a validated baseline.'),
('stakeholders','Stakeholders & RACI','users','Influence, authority, engagement, role boundaries and accountable decisions','RACI clarifies responsibility; decision rights must name the person who can actually authorize funding, risk or release.'),
('roadmap','Integrated Roadmap','calendar-range','Milestones, baseline versus forecast, owners and dependencies','Do not copy sprint tasks into the integrated plan. Manage milestone commitments, external dependencies and release forecasts.'),
('backlog','Agile Epics & Features','layers','Epics, features, stories, acceptance criteria and sprint mapping','PO owns backlog ordering and clarification. Scrum team owns implementation and quality. PM views cross-team commitments.'),
('iterations','Sprint & PI Objectives','repeat-2','Iteration outcomes, PI objectives, confidence and integrated demos','Daily Scrum belongs to Developers; the Scrum Master ensures Scrum effectiveness. PM does not use it for status collection.'),
('dependencies','Cross-Team Dependencies','git-branch','Producer/consumer contracts, handoffs, integration deadlines and escalation','Track exact deliverable, producing team, consuming team, needed-by date, impact, owner and evidence.'),
('capacity','Resources & Capacity','users-round','People, allocation, support reserve, available skill capacity','Availability is not usable delivery capacity. Account for production support, enterprise Okta work, leave and skill bottlenecks.'),
('financials','Budget & Forecast','wallet','Budget, actuals, ETC, EAC, variance, contingency and commitments','EAC = actuals + estimate to complete. A project can be under budget today yet have a projected overrun.'),
('raid','RAID Register','shield-alert','Risks, assumptions, issues and dependencies with mitigation ownership','Risk: may happen. Issue: already happened. Document trigger, consequence, owner, action, due date and escalation.'),
('changes','Change Control','git-pull-request','Scope, schedule and funding changes with impact assessment and approval','PO can reprioritize within delegated scope; material changes to approved baseline require authorized decisions.'),
('decisions','Decision & Escalation Log','gavel','Decision request, tradeoff, authority, due date and evidence','PM coordinates decisions, but does not automatically own all approvals. Escalate outside authority with recommendation.'),
('quality','Quality & Test Management','clipboard-check','SIT, E2E, UAT, defects, nonfunctional controls and evidence','QA Lead owns test execution and quality evidence; PM owns integrated readiness and disposition of blocked milestones.'),
('release','Release Readiness','rocket','Go/no-go controls, deployment, customer exposure and rollback','Distinguish deploying software from exposing a capability to customers. Confirm authority, operational controls and business recovery.'),
('operations','Hypercare & Operations','activity','Support readiness, incidents, stability and operational handover','Code rollback may not undo policy transactions. Plan data reconciliation, support ownership and hypercare exit thresholds.'),
('vendors','Vendors & Contracts','handshake','Contracts, obligations, vendor SLAs and delivery commitments','Vendor milestones need named owners, acceptance evidence, escalation paths and cost consequences.'),
('compliance','Security & Insurance Controls','lock-keyhole','Privacy, access, jurisdiction, audit, underwriting and accessibility','For Add/Replace Vehicle, confirm eligibility, policy effective dates, rating, consent, audit trail and exceptions with control owners.'),
('reports','Status & Governance','presentation','RAG status, steering decisions, evidence and communications','Green sprints can coexist with a Red project. Report integrated forecast, confidence, financials, top blockers and decisions.'),
('recovery','Recovery & Scenarios','life-buoy','Recovery assessment, decision options and controlled rebaselining','Do not change a Red project to Green by changing labels. Diagnose, stabilize, compare options, approve new baseline and track evidence.'),
('program','Program Coordination','network','Related projects, program outcomes, shared dependencies, benefit realization','A program is related initiatives managed together for benefits. Not every collection of teams constitutes a program.'),
('safelp','SAFe & Lean Portfolio','workflow','Portfolio Kanban, value streams, ART, PI planning, WSJF and guardrails','SAFe concepts do not replace actual governance. Operational and development value streams are distinct; funding authority remains explicit.'),
('value','Value Stream Mapping','route','Flow stages, wait time, bottlenecks, handoffs, leading and lagging measures','Map work from customer need to actual value. Distinguish active working time and queue time; measure improvements.'),
('adoption','Organizational Change','refresh-cw','Stakeholder adoption, communication, training, resistance and change outcomes','Transformation is not only new ceremonies. Track whether business roles adopt the changed operating model.'),
('closure','Project Closure','check-check','Acceptance, financial closure, lessons learned and benefits ownership','Separate project closure from ongoing product ownership and long-term benefits measurement.'),
('academy','Learning Academy','graduation-cap','Guided instruction, practice questions, scenarios and answer feedback','Use practice mode to make accountable decisions instead of memorizing definitions.'),
('reference','Full Reference Library','book-open','Complete brand-neutral training guide, design assumptions and help glossary','Reference guide contains an additional FNOL case; primary interactive workspace stays Add/Replace Vehicle.'),
]
fields={
'intake':['title','type','sponsor','value','priority','status','decision'],
'business':['metric','baseline','target','actual','owner','measurement','status'],
'charter':['item','detail','owner','status'],
'stakeholders':['name','role','accountability','authority','engagement','status'],
'roadmap':['milestone','owner','baseline','forecast','status','dependency','evidence'],
'backlog':['key','type','title','owner','pi','sprint','points','status','acceptance'],
'iterations':['iteration','goal','capacity','planned','done','confidence','demo','status'],
'dependencies':['deliverable','producer','consumer','neededBy','forecast','impact','owner','status','escalate'],
'capacity':['team','skill','people','daysPerPerson','leave','support','other','available','owner'],
'financials':['category','baseline','actual','etc','commitments','owner'],
'raid':['id','type','description','impact','likelihood','owner','due','mitigation','status'],
'changes':['id','request','impact','cost','days','sponsor','decision','status'],
'decisions':['id','question','options','recommendation','authority','due','decision','status'],
'quality':['scenario','level','owner','planned','passed','failed','blocked','status','evidence'],
'release':['gate','owner','evidence','due','status','approver'],
'operations':['item','owner','threshold','actual','status','evidence'],
'vendors':['vendor','deliverable','contract','due','owner','status','escalation'],
'compliance':['control','evidence','owner','status','approval'],
'reports':['period','overall','schedule','budget','scope','quality','narrative','decisionNeeded'],
'recovery':['action','owner','due','status','evidence'],
'program':['initiative','manager','businessValue','baseline','forecast','status','sharedDependency'],
'safelp':['epic','valueStream','businessValue','timeCriticality','riskReduction','jobSize','status','decision'],
'value':['stage','workingDays','waitingDays','owner','bottleneck','improvement'],
'adoption':['audience','change','owner','communication','training','adoption','status'],
'closure':['deliverable','owner','acceptance','status','evidence'],
}
data={
'intake':[
['Add/Replace Vehicle','Project','Personal Lines Digital','Self-service policy endorsements','High','Approved','Delivery discovery funded'],
['Enterprise Okta rollout','Enterprise project','Identity Office','Standardize enterprise authentication','High','In progress','Portal integration required'],
['Policy document enhancement','Candidate project','Operations','Reduce paper handling','Medium','Assessing','Await business case'],
['Digital FNOL intake','Portfolio idea','Claims','Improve claim reporting','Medium','Discovery','Separate claims case study'] ],
'business':[
['Eligible vehicle changes completed online','0% (illustrative)','40%','Not measured','Digital Product Owner','Monthly portal analytics','Planning'],
['Average assisted servicing time','18 min (illustrative)','10 min','Not measured','Operations Lead','Monthly operation sample','Planning'],
['Vehicle-change transaction success','Not measured','>= 98%','Not measured','Service Owner','Production telemetry','Planning'],
['Escaped Sev1/Sev2 defects','0 at launch','0','Not measured','QA Lead','Defect and incident reports','Planning']],
'charter':[
['Business objective','Allow eligible policyholders to add or replace insured vehicles in existing portal','Sponsor','Draft'],
['In scope','Add Vehicle; Replace Vehicle; eligibility; premium impact; confirmation; E2E validation','Product Owner','Draft'],
['Out of scope','New policy quote/bind; separate vehicle removal; enterprise Okta implementation itself','Sponsor','Draft'],
['Assumption','Portal remains live; shared team provides BAU support; PolicyCenter provides needed transaction interfaces','PM','Validate'],
['Funding authority','Sponsor / delegated investment forum controls budget and changes','Finance','To confirm']],
'stakeholders':[
['Business sponsor','Personal Lines executive','Business outcome and authorized scope','Funding and tradeoffs','Monthly steering','Engaged'],
['Product Owner','Portal PO','Backlog ordering and requirements','Backlog acceptance','Weekly delivery review','Engaged'],
['Scrum Master','Portal SM','Scrum events and team effectiveness','Scrum process','Scrum events','Engaged'],
['Development lead','Portal engineering','Technical execution and estimates','Technical work','Weekly delivery review','Engaged'],
['QA Lead','Portal QA','Test plan, execution, defect evidence','Quality recommendation','Weekly delivery review','Engaged'],
['PolicyCenter lead','Policy system team','Transaction integration contract','PC delivery commitments','Dependency review','Engaged'],
['Enterprise identity lead','Okta rollout team','Enterprise rollout requirements','Okta rollout decisions','Dependency review','Engaged'],
['Project Manager','Portal initiative','Integrated delivery coordination and governance','Escalation and plan within delegation','Project governance','Engaged']],
'roadmap':[
['Sponsor charter approval','Sponsor','2027-01-15','2027-01-15','Planned','Business case','Draft charter'],
['Scope and API design agreed','PO / Architect','2027-02-12','2027-02-12','Planned','PC interface specification','Backlog and contracts'],
['Portal Add Vehicle feature ready','Portal team','2027-03-26','2027-03-26','Planned','PC rating and policy update','Integrated demo'],
['Replace Vehicle feature ready','Portal team','2027-04-23','2027-04-23','Planned','PC replacement transaction','Integrated demo'],
['Integrated E2E test exit','QA Lead','2027-05-21','2027-05-21','Planned','Stable PC and Okta environment','QA evidence'],
['Business UAT approval','Business Lead','2027-06-11','2027-06-11','Planned','E2E exit','Signed acceptance'],
['Release Go/No-Go','Release Authority','2027-06-18','2027-06-18','Planned','All readiness gates','Decision record']],
'backlog':[
['AV-101','Epic','Add a vehicle to existing auto policy','PO','PI-1','S1','13','Ready','Eligible policy change is confirmed'],
['AV-102','Feature','Retrieve current policy and vehicles','Portal Lead','PI-1','S1','8','Ready','Correct active policy returned'],
['AV-103','Story','Capture VIN, make, model and garaging','Portal Lead','PI-1','S2','5','Draft','Required fields validated'],
['AV-201','Epic','Replace an insured vehicle','PO','PI-1','S4','13','Draft','Original and replacement policy state correct'],
['AV-202','Feature','Calculate premium impact via PolicyCenter','PC Lead','PI-1','S4','8','Blocked','New premium and effective date verified'],
['AV-301','Feature','Authentication regression for Okta integration','QA Lead','PI-1','S3','5','Ready','Login, session, access checks pass'],
['AV-401','Story','Show confirmation and applicable documents','Portal Lead','PI-2','S8','5','Draft','Audit confirmation and documents available']],
'iterations':[
['S1','Confirm vehicle retrieval and baseline capacity','50','34','0','Medium','Policy lookup demo','Planned'],
['S2','Vehicle data capture and validation','50','31','0','Medium','Vehicle entry demo','Planned'],
['S3','Add vehicle transaction and auth regression','45','35','0','Low','Add vehicle E2E slice','Planned'],
['S4','Replace workflow and premium calculation','45','40','0','Low','Replace first integrated slice','Planned'],
['PI-1','Validate Add Vehicle end-to-end','190','140','0','Medium','System demo and PI review','Planning']],
'dependencies':[
['PolicyCenter endorsement / rating API','PolicyCenter Team','Portal Add/Replace','2027-03-01','2027-03-08','Premium and policy transaction blocked','PC Lead','At risk','2027-02-15'],
['Okta portal authentication regression window','Enterprise IAM','Portal QA','2027-03-15','2027-03-15','Capacity competition with functional QA','IAM Lead','Open','2027-03-01'],
['Electronic signature flow review','Document/DocuSign Team','Portal documents','2027-04-15','2027-04-15','Confirmation and consent may be affected','Document Lead','Open','2027-04-01'],
['UAT test accounts and policy data','Test Data Team','Business UAT','2027-05-20','2027-05-20','UAT may slip','QA Lead','Open','2027-05-06']],
'capacity':[
['Portal Dev','Frontend / Full-stack','8','10','8','12','10','50','Engineering Manager'],
['Portal QA','Functional / Integration QA','4','10','4','8','6','22','QA Manager'],
['PolicyCenter','Backend / Guidewire','3','10','2','4','12','12','PC Functional Manager'],
['Business SMEs','UAT / underwriting','2','10','0','3','9','8','Operations Lead']],
'financials':[
['Portal delivery','420000','90000','320000','10000','Engineering Manager'],
['PolicyCenter integration','240000','45000','210000','20000','PC Lead'],
['Quality and test','180000','35000','155000','8000','QA Lead'],
['Architecture / security','120000','40000','85000','10000','Architect'],
['Release and operational readiness','90000','10000','75000','5000','Release Lead'],
['Contingency reserve','150000','0','0','0','PMO / Sponsor']],
'raid':[
['R-001','Risk','PolicyCenter transaction API forecast may slip','High','High','PC Lead','2027-02-15','Agree API contract and workaround milestones','Open'],
['R-002','Risk','Okta rollout consumes shared QA and developer capacity','High','Medium','Portal PM','2027-03-01','Confirm resource allocation and resequence work','Open'],
['A-001','Assumption','Production support reserve is sufficient','Medium','Medium','Scrum Master','2027-01-30','Validate with historical incident trend','Validate'],
['I-001','Issue','UAT data cannot cover midterm endorsements','High','N/A','Test Data Lead','2027-05-01','Secure representative policies and approval','Open'],
['D-001','Dependency','Portal E2E requires PolicyCenter test endpoint','High','N/A','PC Lead','2027-03-01','Confirm readiness evidence and early integration','Open']],
'changes':[
['CR-001','Add stand-alone Remove Vehicle to launch scope','Business, PC, QA and release impact','95000','21','Business Sponsor','Pending analysis','Open']],
'decisions':[
['DEC-001','Can portal retain release date if PC API slips?','Resequence; reduce scope; extend release','Timebox API integration spike, then present revised plan','Sponsor','2027-03-03','Pending','Open'],
['DEC-002','Who approves expanded state eligibility?','Initial states only; broaden with controls','Start limited rollout pending compliance review','Business / Compliance','2027-04-10','Pending','Open']],
'quality':[
['Add Vehicle happy path','E2E','QA Lead','15','0','0','0','Planned','Test run link'],
['Replace Vehicle effective date','E2E','QA Lead','20','0','0','0','Planned','PC policy trace'],
['Okta login / session regression','Integration','QA Lead','18','0','0','0','Planned','Identity test summary'],
['Premium recalculation','Integration','QA Lead','12','0','0','0','Planned','Rating comparison'],
['Authorization and audit trail','Security','Security Lead','8','0','0','0','Planned','Review approval'],
['Business acceptance','UAT','Operations Lead','10','0','0','0','Planned','Signed acceptance']],
'release':[
['Business acceptance criteria met','Business PO','Signed UAT record','2027-06-11','Not started','Business Sponsor'],
['SIT / E2E exit criteria met','QA Lead','QA summary / defect disposition','2027-06-11','Not started','QA / Release'],
['Security, privacy and compliance approvals','Control Owners','Approval record','2027-06-14','Not started','Security / Compliance'],
['Deployment plan and rollback rehearsal','Release Lead','Runbook / rehearsal result','2027-06-15','Not started','Change Authority'],
['Production monitoring and support ready','Service Owner','Dashboard / runbook / contacts','2027-06-15','Not started','Operations'],
['Go/No-Go decision recorded','Release Authority','Decision / exceptions','2027-06-18','Not started','Release Authority']],
'operations':[
['First 48-hour support staffing','Service Owner','Support available','Not yet measured','Planning','Hypercare roster'],
['Failed policy transactions','Engineering Lead','< 2%','Not measured','Planning','Transaction telemetry'],
['Outstanding Sev1 incidents','Incident Commander','0','Not measured','Planning','Incident log'],
['Policy record reconciliation','PC / Operations','100% exceptions reviewed','Not measured','Planning','Reconciliation report'],
['Hypercare exit','Service Owner','Thresholds met for agreed window','Not measured','Planning','Sign-off']],
'vendors':[
['External integration vendor','Integration contract assistance','Statement of work','2027-03-01','Vendor Manager','Draft','Vendor governance'],
['Document services provider','E-signature dependency review','Service agreement','2027-04-15','Vendor Manager','Open','Account representative']],
'compliance':[
['Authenticated customer authorization','Identity test evidence','Security Lead','Open','Security'],
['Vehicle eligibility by state','Product / underwriting rules','Compliance Lead','Open','Business + Compliance'],
['Policy effective dates and premium disclosure','PolicyCenter E2E evidence','PC / PO','Open','Business'],
['Audit events and consent records','Audit specification / logs','Security / Legal','Open','Control Owner'],
['Accessibility and assisted channel','Accessibility testing','UX / QA','Open','Accessibility Lead']],
'reports':[
['Week 1','Amber','Amber','Green','Green','Amber','Planning baseline not yet validated; PolicyCenter API risk','Confirm backend delivery date by Feb 15']],
'recovery':[
['Verify true integrated progress versus reported story completion','PM + QA Lead','2027-03-02','Open','Working E2E demo'],
['Reforecast dependency dates and test windows','PM / PC Lead','2027-03-04','Open','Integrated plan revision'],
['Present options with cost/scope/date tradeoff','PM + Finance','2027-03-08','Open','Sponsor decision memo'],
['Approve recovery baseline if necessary','Sponsor','2027-03-12','Open','Change approval record']],
'program':[
['Add/Replace Vehicle','Portal PM','Digital policy servicing','2027-06-18','2027-06-18','Amber','PolicyCenter interface'],
['Enterprise Okta rollout','IAM Program Lead','Enterprise access modernization','2027-05-28','2027-05-28','Green','Portal regression window'],
['Policy Documents Modernization','Document PM','Reduce manual documents','2027-07-15','2027-07-15','Planning','DocuSign dependency'],
['Digital FNOL','Claims PM','Digital claims intake','2027-09-30','2027-09-30','Discovery','Policy data services']],
'safelp':[
['Digital policy servicing','Policy Servicing','8','8','5','8','Review','Sponsor prioritization'],
['Enterprise identity modernization','Digital Platforms','7','9','7','5','Implementing','Portfolio committed'],
['Digital claim intake','Claims Servicing','8','6','6','13','Analyzing','Need discovery evidence']],
'value':[
['Customer initiates change','0.05','0.1','Portal','Form completion','Simplify intake and help text'],
['Eligibility and policy lookup','0.02','1.5','Policy Services','Queue on backend dependency','Prevalidate eligibility'],
['Vehicle/premium validation','0.06','0.8','PC Team','Rating integration wait','Improve service contract'],
['Customer confirmation','0.01','0.2','Portal','Document handoff','Automate confirmation'],
['Operational completion','0.04','2.0','Operations','Manual exception routing','Automate exception ownership']],
'adoption':[
['Customer service','Self-service changes shift agent workload','Operations Lead','Service bulletin','FAQ and escalation training','Not measured','Planning'],
['Business product teams','Value-stream priority reviews','Transformation Lead','Leadership workshop','LPM decision rights','Not measured','Planning'],
['Support and operations','New exception routing','Service Owner','Runbook review','Hypercare exercises','Not measured','Planning']],
'closure':[
['Business capability accepted','PO / Sponsor','Accepted increment','Pending','Signed acceptance'],
['Operational handover completed','Service Owner','Named ownership','Pending','Handover record'],
['Financials reconciled','Finance','Final cost approved','Pending','Final forecast and commitments'],
['Lessons learned captured','PM','Action owners assigned','Pending','Retrospective summary'],
['Benefits owner assigned','Sponsor','Post-launch measurement cadence','Pending','Benefits plan']],
}
rows={k:[dict(zip(fields[k],x)) for x in v] for k,v in data.items()}
meta={'title':'ValueStream HQ','version':'1.0.0','industry':'Property & Casualty Insurance','case':'Add / Replace Vehicle','portfolio':'Digital Insurance Modernization','projectStart':'2027-01-04','targetRelease':'2027-06-18','budget':1200000,'illustrative':True,'dataSource':'Fictional training records; not sourced from a real insurer','reference':'Full supplied SAFe/FNOL guide retained as separate source'}
(root/'seed-data.json').write_text(json.dumps({'metadata':meta,'modules':rows},indent=2))
(root/'modules.json').write_text(json.dumps([dict(zip(('id','name','icon','description','help'),s)) for s in sections],indent=2))
print(len(sections),'modules',sum(map(len,rows.values())),'seed records')
