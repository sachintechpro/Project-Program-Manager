# HISTORICAL MIGRATION ONLY — disabled to protect the verified v1.4 brand-neutral release.
raise SystemExit("Historical migration disabled. Edit the current source data and use make_index.py.")

"""One-time reconciliation of the illustrative v1.2 seed to a coherent v1.3 snapshot.
The training figures are intentionally fictional, not claims about actual insurance programs.
"""
import json
from pathlib import Path
p=Path(__file__).with_name('seed-data.json');d=json.loads(p.read_text());m=d['modules']
md=d['metadata'];md.update(version='1.3.0',asOfDate='2027-02-19',snapshotBasis='Illustrative week-7 project status; fictional records only',capacityPeriod='Two-week S4 window, 2027-02-15 to 2027-02-26')
# Sponsor authorized the initial charter, but cross-team planning remains unresolved.
m['intake'][0]['decision']='Charter approved 2027-01-15; current delivery forecasts remain conditional'
for idx in (0,1,2):m['charter'][idx]['status']='Approved'
m['charter'][3]['status']='Under review'
m['charter'][4]['status']='Approved';m['charter'][4]['detail']='Sponsor is accountable for funding decisions; delegated authority follows documented investment controls'
# Define an auditable timeline with approved baseline retained and honest reforecasts.
road=m['roadmap']
updates=[
 ('2027-01-15','Complete','Signed charter approval (sample)'),
 ('2027-03-10','At risk','Scope draft; PolicyCenter interface contract not yet signed'),
 ('2027-04-02','At risk','Portal UI in progress; end-to-end feature not complete'),
 ('2027-04-30','At risk','Replace flow design in progress; PC transaction readiness pending'),
 ('2027-05-28','At risk','Formal E2E exit evidence pending'),
 ('2027-06-15','At risk','Business acceptance not yet obtained'),
 ('2027-06-18','At risk','Release date held as target; recovery decision pending')]
for item,(forecast,stat,evidence) in zip(road,updates):item.update(forecast=forecast,status=stat,evidence=evidence)
# Iteration forecasts use one unit (relative team points), not resource person-days.
it=m['iterations']; vals=[('40','34','30','Complete'),('40','31','28','Complete'),('38','35','32','Complete'),('38','40','10','In progress')]
for row,(capacity,planned,done,status) in zip(it[:4],vals):row.update(capacity=capacity,planned=planned,done=done,status=status)
it[2]['goal']='Add Vehicle portal slice; prepare integration and Okta regression';it[2]['demo']='UI and service stub demonstration; PC interface not yet integrated'
it[3]['goal']='Replace Vehicle UI flow and premium API contract';it[3]['demo']='Replace flow slice; PolicyCenter integration remains pending'
it[4].update(capacity='156',planned='140',done='100',goal='Validate portal flows and integration contracts before end-to-end API readiness',demo='Integrated progress and dependency demonstration',status='In progress')
# Sample Jira backlog is illustrative and incomplete relative to sprint rollups; epics span multiple sprints.
bl=m['backlog'];bl[0].update(sprint='Multiple',status='In progress');bl[1]['status']='Done';bl[2]['status']='Done'
bl[3].update(pi='PI-2',sprint='Multiple',status='Draft')
bl[4].update(pi='PI-2',sprint='S6',status='At risk')
bl[5].update(pi='PI-2',sprint='S6',status='Ready')
# Dependency risk and dates agree with current forecast and future escalation window.
m['dependencies'][0]['escalate']='2027-02-23';m['dependencies'][0]['impact']='Portal premium and policy endorsement integration at risk of seven-day slip'
m['raid'][0]['due']='2027-02-23';m['raid'][2]['due']='2027-02-23'
m['reports'][0].update(period='2027-02-19 (Week 7)',overall='Amber',schedule='Amber',budget='Green',scope='Green',quality='Amber',narrative='Charter approved. PolicyCenter API forecast seven days late; downstream milestones at risk. $15k expected reserve draw. Release target held pending recovery decision.',decisionNeeded='Confirm API delivery/recovery with PC lead by 2027-02-23; sponsor decision if target cannot be protected')
# The formal E2E/UAT register excludes unit/story validation done in prior sprints.
for x in m['quality']:
 x['evidence']='Planned formal test evidence; no execution artifact yet'
m['quality'][0].update(blocked='3',status='Blocked',evidence='Three E2E cases waiting on PolicyCenter API; not counted as passed')
# Consistent business metrics and clear pre-launch baseline.
m['business'][3].update(baseline='N/A — capability not launched',target='0 production Sev1/Sev2 escapes')
# Clarify candidate program membership rather than treating unrelated initiatives as one program.
m['program']=[
 dict(initiative='Add/Replace Vehicle',manager='Portal PM',businessValue='Digital policy servicing',baseline='2027-06-18',forecast='2027-06-18',status='Amber',sharedDependency='PolicyCenter endorsement service',relationship='Illustrative program member'),
 dict(initiative='Policy Document Enhancement',manager='Document PM',businessValue='Electronic policy servicing',baseline='2027-07-15',forecast='2027-07-15',status='Assessing',sharedDependency='Document platform',relationship='Candidate related project; not approved'),
 dict(initiative='Billing Self-Service',manager='Billing Delivery Lead',businessValue='Digital policy servicing',baseline='2027-09-15',forecast='2027-09-15',status='Discovery',sharedDependency='Billing platform',relationship='Candidate related project; not approved'),
 dict(initiative='Enterprise Okta rollout',manager='IAM Program Lead',businessValue='Enterprise access modernization',baseline='2027-05-28',forecast='2027-05-28',status='Green',sharedDependency='Portal regression window',relationship='External enterprise program; not a member'),
 dict(initiative='Digital FNOL',manager='Claims PM',businessValue='Digital claims intake',baseline='2027-09-30',forecast='2027-09-30',status='Discovery',sharedDependency='Policy data services',relationship='Separate portfolio idea; not a member'),
]
m['intake'].append(dict(title='Billing Self-Service',type='Candidate project',sponsor='Digital Operations',value='Online billing servicing',priority='Medium',status='Discovery',decision='Independent approval required before program membership'))
# Operational current-state workflow (assisted channel) is distinct from not-yet-launched digital service.
vals=[
 ('Customer contacts service for vehicle change','0.0375','0.1','Customer Service','Agent intake handling','Future-state portal self-service'),
 ('Policy and eligibility verification','0.02','1.5','Policy Operations','Manual case queue','Automated policy lookup and eligibility checks'),
 ('Vehicle and premium calculation','0.025','0.8','Policy Operations','Manual rating work','PolicyCenter integration'),
 ('Confirmation and documents','0.01','0.2','Document Services','Document handoff','Automate confirmation'),
 ('Policy update and exception closure','0.015','2.0','Operations','Manual exception routing','Exception owner and reconciliation workflow')]
for row,entries in zip(m['value'],vals):
 for k,v in zip(('stage','workingDays','waitingDays','owner','bottleneck','improvement'),entries):row[k]=v
# As-of date: existing original estimates and actuals now correspond to a 7-week project snapshot.
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
print('Reconciled',sum(map(len,m.values())),'records across',len(m),'registers')
