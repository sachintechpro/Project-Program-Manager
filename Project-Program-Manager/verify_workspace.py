"""Independent, deterministic verification of the bundled illustrative training seed.
Run: python verify_workspace.py. Does not modify project data. Requires Python 3.
"""
from pathlib import Path
from datetime import date
import json, math, re, sys
ROOT=Path(__file__).resolve().parent
S=json.loads((ROOT/'seed-data.json').read_text())
M=S['modules'];MD=S['metadata'];G=json.loads((ROOT/'field-guidance.json').read_text());NAV=json.loads((ROOT/'modules.json').read_text())
checks=[];failures=[]
def check(label,condition):
 checks.append(label)
 if not condition:failures.append(label)
def n(row,key):return float(row[key])
def sumfield(module,key):return sum(n(r,key) for r in M[module])
def iso(x):
 try:return date.fromisoformat(x)
 except:return None
check('Full management navigation present', len(NAV)==30 and {'overview','audit','academy','reference'}<=set(x['id'] for x in NAV))
check('26 editable management registers present',len(M)==26)
check('114 sample records present',sum(map(len,M.values()))==114)
check('Unique section identifiers',len({x['id'] for x in NAV})==len(NAV))
check('Every editable register has sample records',all(len(v)>0 for v in M.values()))
check('No register has heterogeneous fields',all(set(r)==set(v[0]) for v in M.values() for r in v))
check('Every editable register has a tooltip section',all(k in G for k in M))
for k,v in M.items():
 check(f'{k}: every parameter has contextual guidance',set(v[0])<=set(G[k]))
 check(f'{k}: no missing record keys',all(all(str(r.get(field,'')).strip()!='' for field in v[0]) for r in v))
check('Complete brand-neutral training reference preserved', (ROOT/'reference-SAFe-end-to-end-guide.md').stat().st_size>20000 and all(x in (ROOT/'reference-SAFe-end-to-end-guide.md').read_text() for x in ['## 1. First understand the roles','## 6. Plan delivery in a SAFe environment','## 12. How to recover a project']))
check('Scenario snapshot after project commencement',iso(MD['asOfDate'])>=iso(MD['projectStart']))
check('Week-7 progress snapshot aligns with start', (iso(MD['asOfDate'])-iso(MD['projectStart'])).days in range(42,49))
check('All dated baseline and forecast values ISO-valid',all(iso(r[k]) for name,fields in {'roadmap':['baseline','forecast'],'dependencies':['neededBy','forecast','escalate'],'release':['due'],'program':['baseline','forecast'],'decisions':['due'],'raid':['due'],'vendors':['due'],'recovery':['due']}.items() for r in M[name] for k in fields))
check('Charter was approved by snapshot',iso(M['roadmap'][0]['forecast'])<=iso(MD['asOfDate']) and M['roadmap'][0]['status']=='Complete')
check('Charter scope records approved',all(r['status']=='Approved' for r in M['charter'][:3]))
check('Remaining roadmap milestone dates have not arrived as of snapshot',all(iso(r['forecast'])>iso(MD['asOfDate']) for r in M['roadmap'][1:]))
check('Release baseline equals project authorization date',M['roadmap'][-1]['baseline']==MD['targetRelease'])
check('Final release still at risk rather than falsely completed',M['roadmap'][-1]['status']=='At risk')
check('PolicyCenter dependency slips relative to need',iso(M['dependencies'][0]['forecast'])>iso(M['dependencies'][0]['neededBy']) and M['dependencies'][0]['status']=='At risk')
check('PolicyCenter escalation is actionable from snapshot',iso(M['dependencies'][0]['escalate'])>=iso(MD['asOfDate']))
check('Roadmap reflects API slip',iso(M['roadmap'][1]['forecast'])>iso(M['roadmap'][1]['baseline']))
check('Source change out of scope, approval pending', 'separate vehicle removal' in M['charter'][2]['detail'].lower() and M['changes'][0]['status']=='Open')
# Independent financials
res=[r for r in M['financials'] if 'contingency' in r['category'].lower()];base=[r for r in M['financials'] if r not in res]
basebudget=sum(n(r,'baseline') for r in base);reserve=sum(n(r,'baseline') for r in res);baseline=basebudget+reserve;actual=sumfield('financials','actual');etc=sumfield('financials','etc');eac=actual+etc;commitments=sumfield('financials','commitments');draw=max(0,eac-basebudget)
for i,r in enumerate(M['financials']):
 check(f'Financial row {i+1}: values nonnegative',all(n(r,k)>=0 and math.isfinite(n(r,k)) for k in ['baseline','actual','etc','commitments']))
 check(f'Financial row {i+1}: future commitments included in ETC',n(r,'commitments')<=n(r,'etc'))
check('Finance authorized baseline matches metadata', baseline==MD['budget']==1200000)
check('Finance base budget',basebudget==1050000)
check('Contingency reserve',reserve==150000)
check('Finance cost actual to date',actual==220000)
check('Finance remaining forecast',etc==845000)
check('EAC actual plus ETC',eac==1065000)
check('Expected reserve usage versus base',draw==15000)
check('Available reserve remaining',reserve-draw==135000)
check('Future contractual commitments',commitments==53000)
check('No contingency costs directly charged',all(n(r,'actual')==0 and n(r,'etc')==0 for r in res))
# Capacity and planning units
avail=[]
for r in M['capacity']:
 val=n(r,'people')*n(r,'daysPerPerson')-n(r,'leave')-n(r,'support')-n(r,'other');avail.append(val)
 check(f'{r["team"]}: available days calculated',n(r,'available')==val and val>=0)
check('92 total nonfungible capacity days',sum(avail)==92 and avail==[50,22,12,8])
check('S1–S4 iteration rollup matches PI-1',all(sum(n(r,k) for r in M['iterations'][:4])==n(M['iterations'][4],k) for k in ['capacity','planned','done']))
check('S1–S3 work actually completed',all(r['status']=='Complete' and n(r,'done')>0 for r in M['iterations'][:3]))
check('S4 remains an in-progress scenario',M['iterations'][3]['status']=='In progress')
check('Overcommitment is visible in the training scenario',n(M['iterations'][3],'planned')>n(M['iterations'][3],'capacity'))
check('Sample backlog does not treat epic as single sprint',all(r['sprint']=='Multiple' for r in M['backlog'] if r['type']=='Epic'))
check('Sample backlog acknowledges prior completed work',sum(r['status']=='Done' for r in M['backlog'])>=2)
# Quality, readiness and benefits
for r in M['quality']:
 for k in ['planned','passed','failed','blocked']:check(f'QA {r["scenario"]}: valid {k}',n(r,k)>=0 and n(r,k).is_integer())
 check(f'QA {r["scenario"]}: totals within planned',n(r,'passed')+n(r,'failed')+n(r,'blocked')<=n(r,'planned'))
check('83 planned formal E2E/SIT/security/UAT tests',sumfield('quality','planned')==83)
check('Three blocked formal tests not represented as passes',sumfield('quality','blocked')==3 and sumfield('quality','passed')==0)
check('All future release gates appropriately not started',all(r['status']=='Not started' and iso(r['due'])>iso(MD['asOfDate']) for r in M['release']))
check('UAT before release authorization',iso(M['roadmap'][5]['forecast'])<=iso(M['roadmap'][6]['forecast']))
check('Postlaunch metric not reported before launch',all(r['actual']=='Not measured' for r in M['business']))
check('Defect baseline is prelaunch not fake zero',M['business'][3]['baseline'].startswith('N/A'))
# Portfolio value and value stream
check('All portfolio WSJF job sizes positive',all(n(r,'jobSize')>0 for r in M['safelp']))
wsjf=[(n(r,'businessValue')+n(r,'timeCriticality')+n(r,'riskReduction'))/n(r,'jobSize') for r in M['safelp']]
check('WSJF reproducible from each score',[round(x,3) for x in wsjf]==[2.625,4.6,round(20/13,3)])
w=sumfield('value','workingDays');q=sumfield('value','waitingDays')
check('Operational current-state active work correct',math.isclose(w,.1075))
check('Operational queue time correct',math.isclose(q,4.6))
check('Operational flow efficiency correct',math.isclose(w/(w+q)*100,2.283589,abs_tol=.01))
check('Operational current-state workflow begins with assisted service','service' in M['value'][0]['stage'].lower())
check('Enterprise Okta not misclassified as member',all(r['relationship'].lower().startswith('external') for r in M['program'] if 'Okta' in r['initiative']))
check('FNOL not classified as policy servicing member',all('separate' in r['relationship'].lower() for r in M['program'] if 'FNOL' in r['initiative']))
check('Program candidates are not preapproved',sum('candidate' in r['relationship'].lower() for r in M['program'])==2)
check('Jira/Confluence and enterprise case represented',any('Okta' in r['title'] for r in M['intake']) and any('PolicyCenter' in r['deliverable'] for r in M['dependencies']))
print(f'Independent verification: {len(checks)} checks, {len(failures)} failures')
for fail in failures:print('FAILED:',fail)
summary={'checks':len(checks),'failures':failures,'registers':len(M),'modules':len(NAV),'records':sum(map(len,M.values())),'fields':sum(len(v[0]) for v in M.values()),'asOf':MD['asOfDate'],'actual':actual,'etc':etc,'eac':eac,'budget':baseline,'baseBudget':basebudget,'contingency':reserve,'reserveUse':draw,'reserveRemaining':reserve-draw,'capacityDays':avail,'formalTestsPlanned':sumfield('quality','planned'),'formalTestsBlocked':sumfield('quality','blocked'),'WSJF':wsjf,'flowActiveDays':w,'flowWaitingDays':q,'flowEfficiencyPercent':w/(w+q)*100}
(ROOT/'validation-results.json').write_text(json.dumps(summary,indent=2)+'\n')
sys.exit(1 if failures else 0)
