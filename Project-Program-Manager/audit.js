/* v1.4 live, non-destructive internal-consistency checks. Risk flags are not data-entry errors. */
const dateVal=s=>{if(typeof s!=='string'||!/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(s))return NaN;const n=Date.parse(s+'T12:00:00Z');return Number.isFinite(n)&&new Date(n).toISOString().slice(0,10)===s?n:NaN};
const safeN=x=>{if(x===null||x===undefined||String(x).trim()==='')return NaN;const n=Number(x);return Number.isFinite(n)?n:NaN};
const isResolved=s=>/^(complete|completed|done|closed|approved|accepted|validated|resolved|passed)$/i.test(String(s||''));
const availableDays=r=>safeN(r.people)*safeN(r.daysPerPerson)-safeN(r.leave)-safeN(r.support)-safeN(r.other);
const budgetBreakdown=()=>{const R=rows('financials'),res=R.filter(r=>/contingency reserve/i.test(String(r.category||''))),base=R.filter(r=>!/contingency reserve/i.test(String(r.category||''))),sumField=(items,key)=>items.reduce((n,r)=>n+(Number(r[key])||0),0),budget=sumField(R,'baseline'),baseBudget=sumField(base,'baseline'),reserve=sumField(res,'baseline'),actual=sumField(R,'actual'),etc=sumField(R,'etc'),eac=actual+etc,draw=Math.max(0,eac-baseBudget);return {budget,baseBudget,reserve,actual,etc,eac,draw,remaining:Math.max(0,reserve-draw),commitments:sumField(R,'commitments')}};
function auditWorkspace(){
 const items=[],push=(severity,module,code,message)=>items.push({severity,module,code,message});
 const md=state.metadata,asof=dateVal(md.asOfDate),start=dateVal(md.projectStart),target=dateVal(md.targetRelease);
 for(const key of ['asOfDate','projectStart','targetRelease'])if(!Number.isFinite(dateVal(md[key])))push('Error','audit','DATE-'+key,`Workspace ${key} is not a valid ISO date (YYYY-MM-DD).`);
 if(Number.isFinite(asof)&&Number.isFinite(start)&&asof<start&&rows('financials').some(r=>safeN(r.actual)>0))push('Error','financials','FIN-CHRONO','Actual project spending is recorded before the defined project start; verify the snapshot date or cost attribution.');
 const fin=budgetBreakdown();
 for(const [i,r] of rows('financials').entries()){
  for(const fld of ['baseline','actual','etc','commitments']){
   const val=safeN(r[fld]);if(!Number.isFinite(val)||val<0)push('Error','financials','FIN-NUM-'+i+'-'+fld,`${r.category||'Cost category '+(i+1)}: ${fld} must be a nonnegative amount.`);
  }
  if(Number.isFinite(safeN(r.commitments))&&Number.isFinite(safeN(r.etc))&&safeN(r.commitments)>safeN(r.etc))push('Error','financials','FIN-COMMIT-'+i,`${r.category}: commitments exceed ETC. In this model commitments are a subset of future ETC, not an amount added to EAC.`);
  if(/contingency reserve/i.test(String(r.category||''))&&(safeN(r.actual)>0||safeN(r.etc)>0))push('Review','financials','FIN-RESERVE','Contingency is shown as a funding reserve. Charge costs to cost categories and track authorized reserve draw separately.');
 }
 if(Math.abs(fin.budget-safeN(md.budget))>0.005)push('Error','financials','FIN-BASELINE',`Finance baseline ${money(fin.budget)} differs from workspace budget ${money(md.budget)}; budget should be derived from finance register.`);
 if(fin.eac>fin.budget)push('Review','financials','FIN-OVERRUN',`Forecast ${money(fin.eac)} exceeds authorized ${money(fin.budget)} by ${money(fin.eac-fin.budget)}. Prepare funding/scope decision.`);
 else if(fin.eac>fin.baseBudget)push('Review','financials','FIN-RESERVE-USE',`Forecast is ${money(fin.eac-fin.baseBudget)} above base costs and uses that amount of the ${money(fin.reserve)} contingency. Validate assumptions and authorization.`);
 const caps=rows('capacity');for(const [i,r] of caps.entries()){
  for(const k of ['people','daysPerPerson','leave','support','other'])if(!Number.isFinite(safeN(r[k]))||safeN(r[k])<0)push('Error','capacity','CAP-NUM-'+i+'-'+k,`${r.team}: ${k} must be a nonnegative number.`);
  const calc=availableDays(r),saved=safeN(r.available);
  if(!Number.isFinite(calc))continue;
  if(calc<0)push('Error','capacity','CAP-NEG-'+i,`${r.team}: reservations (${safeN(r.leave)+safeN(r.support)+safeN(r.other)}d) exceed gross capacity (${safeN(r.people)*safeN(r.daysPerPerson)}d).`);
  if(!Number.isFinite(saved)||Math.abs(saved-calc)>0.0001)push('Error','capacity','CAP-STALE-'+i,`${r.team}: stored available ${r.available}d differs from calculated ${calc}d. Save or normalize the row.`);
 }
 const itr=rows('iterations'),pi=itr.find(r=>r.iteration==='PI-1'),sprints=itr.filter(r=>/^S[1-4]$/.test(String(r.iteration||'')));
 for(const [i,r] of itr.entries()){
  for(const f of ['capacity','planned','done'])if(!Number.isFinite(safeN(r[f]))||safeN(r[f])<0)push('Error','iterations','SPR-NUM-'+i+'-'+f,`${r.iteration}: ${f} must be a nonnegative relative planning-point value.`);
  if(safeN(r.done)>safeN(r.planned))push('Error','iterations','SPR-DONE-'+i,`${r.iteration}: completed effort exceeds planned effort; confirm whether the plan was reforecast.`);
  if(safeN(r.planned)>safeN(r.capacity))push('Review','iterations','SPR-OVER-'+i,`${r.iteration}: planned ${r.planned} points exceed team forecast capacity ${r.capacity}; revisit sprint commitment.`);
 }
 if(pi&&sprints.length===4)for(const f of ['capacity','planned','done']){
  const total=sprints.reduce((a,r)=>a+(safeN(r[f])||0),0);
  if(Math.abs(total-safeN(pi[f]))>0.0001)push('Error','iterations','PI-ROLLUP-'+f,`PI-1 ${f}=${pi[f]} but S1–S4 totals ${total} (${f} uses relative planning points).`);
 }
 const milestones=rows('roadmap');for(const [i,r] of milestones.entries()){
  const a=dateVal(r.baseline),b=dateVal(r.forecast);
  if(!Number.isFinite(a)||!Number.isFinite(b))push('Error','roadmap','ROAD-DATE-'+i,`${r.milestone}: baseline and forecast must be valid dates.`);
  if(Number.isFinite(asof)&&Number.isFinite(b)&&b<asof&&!isResolved(r.status))push('Review','roadmap','ROAD-OVERDUE-'+i,`${r.milestone}: forecast date passed but status is ${r.status}; verify current estimate and evidence.`);
  if(Number.isFinite(a)&&Number.isFinite(b)&&b>a&&/^(green|on track|complete)$/i.test(String(r.status)))push('Error','roadmap','ROAD-STATUS-'+i,`${r.milestone}: milestone slips after baseline yet is marked ${r.status}.`);
 }
 const go=milestones.find(r=>/Release Go\/No-Go/i.test(r.milestone));if(go&&Number.isFinite(target)&&Number.isFinite(dateVal(go.baseline))&&dateVal(go.baseline)!==target)push('Review','roadmap','ROAD-TARGET',`Workspace target release ${md.targetRelease} differs from original baseline Go/No-Go ${go.baseline}. Keep approved baseline history explicit.`);
 for(const [i,r] of rows('dependencies').entries()){
  const due=dateVal(r.neededBy),fore=dateVal(r.forecast),esc=dateVal(r.escalate);
  if(![due,fore,esc].every(Number.isFinite))push('Error','dependencies','DEP-DATE-'+i,`${r.deliverable}: needed-by, forecast and escalation dates must be valid ISO dates.`);
  if(Number.isFinite(due)&&Number.isFinite(fore)&&fore>due){
   if(/^(green|on track|complete|done)$/i.test(r.status))push('Error','dependencies','DEP-STATUS-'+i,`${r.deliverable}: forecast misses needed-by date yet is green/complete.`);
   else push('Review','dependencies','DEP-SLIP-'+i,`${r.deliverable}: forecast ${r.forecast} is later than needed-by ${r.neededBy}; agree mitigation or revised integration forecast.`);
  }
  if(Number.isFinite(asof)&&Number.isFinite(esc)&&esc<asof&&!isResolved(r.status))push('Review','dependencies','DEP-ESCALATION-'+i,`${r.deliverable}: escalation date ${r.escalate} passed without a resolved status.`);
 }
 for(const [i,r] of rows('quality').entries()){
  for(const f of ['planned','passed','failed','blocked'])if(!Number.isFinite(safeN(r[f]))||safeN(r[f])<0||!Number.isInteger(safeN(r[f])))push('Error','quality','QA-NUM-'+i+'-'+f,`${r.scenario}: ${f} must be a nonnegative whole test count.`);
  if(['planned','passed','failed','blocked'].every(f=>Number.isFinite(safeN(r[f])))&&safeN(r.passed)+safeN(r.failed)+safeN(r.blocked)>safeN(r.planned))push('Error','quality','QA-EXCEED-'+i,`${r.scenario}: passed + failed + blocked exceed planned tests.`);
 }
 for(const [i,r] of rows('release').entries()){
  const due=dateVal(r.due);if(!Number.isFinite(due))push('Error','release','REL-DATE-'+i,`${r.gate}: invalid due date.`);
  if(Number.isFinite(asof)&&Number.isFinite(due)&&due<asof&&!isResolved(r.status))push('Review','release','REL-OVERDUE-'+i,`${r.gate}: readiness item overdue with status ${r.status}.`);
 }
 for(const [i,r] of rows('safelp').entries()){
  for(const f of ['businessValue','timeCriticality','riskReduction','jobSize'])if(!Number.isFinite(safeN(r[f]))||safeN(r[f])<0)push('Error','safelp','WSJF-NUM-'+i+'-'+f,`${r.epic}: ${f} must be a nonnegative relative score.`);
  if(safeN(r.jobSize)===0)push('Error','safelp','WSJF-ZERO-'+i,`${r.epic}: job size must be greater than zero; WSJF cannot silently divide by one.`);
 }
 for(const [i,r] of rows('value').entries())for(const f of ['workingDays','waitingDays'])if(!Number.isFinite(safeN(r[f]))||safeN(r[f])<0)push('Error','value','VALUE-NUM-'+i+'-'+f,`${r.stage}: ${f} must be a nonnegative business-day value.`);
 for(const id of ['backlog','raid','changes','decisions']){
  const key=id==='backlog'?'key':'id',seen=new Set();for(const [i,r] of rows(id).entries()){
   const value=String(r[key]||'').trim();if(!value)push('Error',id,'KEY-MISSING-'+i,`${id} row ${i+1}: missing ${key}.`);
   else if(seen.has(value))push('Error',id,'KEY-DUP-'+i,`${id}: duplicate identifier ${value}.`);
   seen.add(value);
  }
 }
 const oneStatus=rows('reports')[0];if(oneStatus?.overall==='Green'&&items.some(it=>it.code.startsWith('DEP-SLIP')||it.code==='FIN-OVERRUN'))push('Review','reports','RAG-CREDIBILITY','Overall Green should be justified against unresolved critical release dependencies or financial exposure.');
 return items;
}
function auditView(){
 const items=auditWorkspace(),fatal=items.filter(x=>x.severity==='Error'),reviews=items.filter(x=>x.severity==='Review');
 const rowsHtml=items.length?items.map(x=>`<tr><td><span class="status ${x.severity==='Error'?'bad':'warn'}">${esc(x.severity)}</span></td><td>${esc(mMap[x.module]?.name||x.module)}</td><td>${esc(x.code)}</td><td>${esc(x.message)}</td><td>${btn('Open','goto:'+x.module)}</td></tr>`).join(''):'<tr><td colspan="5">No numerical, structural or cross-register flags from the implemented checks.</td></tr>';
 return `${notice()}<div class="help"><strong>Internal validation, not external verification:</strong> Tests check sample chronology, amounts, formulas, dates, status consistency and cross-register logic. They cannot authenticate external budgets, real delivery evidence, regulatory approval or live Jira records.</div>
 <div class="cards"><div class="metric"><label>Validation errors</label><div class="number">${fatal.length}</div><div class="foot">Malformed, inconsistent or stale entries</div></div><div class="metric"><label>Management reviews</label><div class="number">${reviews.length}</div><div class="foot">Delivery, capacity or contingency decisions</div></div><div class="metric"><label>Audited registers</label><div class="number">${Object.keys(state.modules).length}</div><div class="foot">Editable record groups</div></div><div class="metric"><label>As-of date</label><div class="number small">${esc(state.metadata.asOfDate||'Not set')}</div><div class="foot">Illustrative snapshot, not live</div></div></div>
 <section class="panel"><div class="panel-head"><div><h2>Data integrity and delivery review log</h2><p class="muted">Issues are generated from the current local records. Editing underlying values updates these findings.</p></div>${btn('Export audit CSV','auditcsv')}</div><div class="table-wrap"><table><thead><tr><th>Severity</th><th>Module</th><th>Check</th><th>Finding and next action</th><th>Navigate</th></tr></thead><tbody>${rowsHtml}</tbody></table></div></section>
 <section class="panel"><h2>What is not independently verified?</h2><p>Training dates, estimates, funding approvals, test evidence and actual progress were authored as fictional case data. No company finance system, Jira, Confluence, Guidewire, Okta or regulatory source was queried. Your project controls must validate real inputs with responsible owners. This audit prevents misleading internal arithmetic and inconsistency; it is not proof of real-world performance.</p></section>`;
}
function validateEditedRecord(section,data,editingIndex){
 const errors=[];
 const numeric=({financials:['baseline','actual','etc','commitments'],capacity:['people','daysPerPerson','leave','support','other'],iterations:['capacity','planned','done'],quality:['planned','passed','failed','blocked'],changes:['cost','days'],safelp:['businessValue','timeCriticality','riskReduction','jobSize'],value:['workingDays','waitingDays']})[section]||[];
 const dates=({roadmap:['baseline','forecast'],dependencies:['neededBy','forecast','escalate'],raid:['due'],decisions:['due'],release:['due'],recovery:['due'],vendors:['due'],program:['baseline','forecast']})[section]||[];
 for(const field of numeric){let val=safeN(data[field]);if(!Number.isFinite(val)||val<0)errors.push(`${field}: enter a nonnegative number`)}
 for(const field of dates)if(!Number.isFinite(dateVal(data[field])))errors.push(`${field}: enter a valid date`);
 if(section==='capacity'&&Number.isFinite(availableDays(data))&&availableDays(data)<0)errors.push('leave: non-delivery commitments exceed available gross person-days');
 if(section==='financials'&&safeN(data.commitments)>safeN(data.etc))errors.push('commitments: committed future costs must be included within ETC');
 if(section==='quality'&&numeric.every(k=>Number.isFinite(safeN(data[k])))&&safeN(data.passed)+safeN(data.failed)+safeN(data.blocked)>safeN(data.planned))errors.push('planned: combined passed, failed and blocked tests exceed planned');
 if(section==='iterations'&&safeN(data.done)>safeN(data.planned))errors.push('done: completed planning points exceed the planned value');
 if(section==='safelp'&&safeN(data.jobSize)<=0)errors.push('jobSize: job size must be positive');
 const uniqueKey=section==='backlog'?'key':['raid','changes','decisions'].includes(section)?'id':null;
 if(uniqueKey){let v=String(data[uniqueKey]||'').trim();if(!v)errors.push(`${uniqueKey}: record identifier is required`);
  else if(rows(section).some((r,i)=>i!==editingIndex&&r[uniqueKey]===v))errors.push(`${uniqueKey}: identifier already exists`);
 }
 if(section==='raci'){
  if(!String(data.responsible||'').trim())errors.push('responsible: assign at least one responsible person');
  if(!String(data.accountable||'').trim()||/[,;\n]/.test(data.accountable))errors.push('accountable: assign one accountable person');
 }
 if(!String(data[Object.keys(data)[0]]??'').trim())errors.push(`${Object.keys(data)[0]}: record name is required`);
 return errors;
}
