import {streams,initiatives,getStream,getInitiative,forStream,totalBudget,phases,tips,roles,jd,scenario} from "./portfolio-data.js";
const $=id=>document.getElementById(id);
const esc=v=>String(v??"").replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[m]));
const money=n=>"$"+Number(n).toFixed(2)+"m";
const pct=(a,b)=>a?Math.round((b-a)/a*100):0;
const selectedFirst=forStream("claims")[0];
const state={
 streamId:"claims",initiativeId:selectedFirst.id,
 stage:0,deskTab:"charter",gates:{},tour:0,
 delay:3,squads:0,phased:true,qa:false,ops:true,vendor:false
};
let toastTimeout;
function current(){return getInitiative(state.initiativeId);}
function stream(){return getStream(state.streamId);}
function gates(){if(!state.gates[state.initiativeId])state.gates[state.initiativeId]=new Set();return state.gates[state.initiativeId];}
function notify(message){
 const node=$("toast");node.textContent=message;node.classList.add("show");
 clearTimeout(toastTimeout);toastTimeout=setTimeout(()=>node.classList.remove("show"),4300);
}
function updateContext(){
 const item=current(),s=stream();
 $("activeTitle").textContent=item.name;
 $("activeStream").textContent=s.name+" / "+item.lob;
}
function selectStream(id){
 if(!streams.some(s=>s.id===id))return;
 state.streamId=id;const first=forStream(id)[0];
 state.initiativeId=first.id;state.stage=0;resetLevers(false);renderAll();
 notify("Value stream selected: "+getStream(id).name+". Choose an initiative below.");
}
function selectInitiative(id){
 const item=initiatives.find(i=>i.id===id);
 if(!item)return;
 state.streamId=item.streamId;state.initiativeId=id;state.stage=0;
 resetLevers(false);renderAll();
 notify(item.name+" selected. Lifecycle, risk and financial controls have updated.");
}
function resetLevers(reRender=true){
 Object.assign(state,{delay:3,squads:0,phased:true,qa:false,ops:true,vendor:false});
 $("delay").value=3;$("squads").value=0;
 $("phased").checked=true;$("qa").checked=false;$("ops").checked=true;$("vendor").checked=false;
 if(reRender){renderControl();notify("Delivery scenario reset.");}
}
function route(page,focus=true){
 if(!["portfolio","journey","desk","control","governance","requirements"].includes(page))page="portfolio";
 document.querySelectorAll(".screen").forEach(s=>{
  const active=s.id===page;s.classList.toggle("active",active);s.setAttribute("aria-hidden",String(!active));
 });
 document.querySelectorAll("[data-route]").forEach(a=>{
  const active=a.dataset.route===page;
  a.classList.toggle("active",active);
  if(active)a.setAttribute("aria-current","page");else a.removeAttribute("aria-current");
 });
 if(location.hash!=="#"+page)history.replaceState(null,"","#"+page);
 window.scrollTo(0,0);
 if(focus){const h=$(page).querySelector("h1");if(h){h.tabIndex=-1;h.focus({preventScroll:true});}}
}
function renderPortfolio(){
 const totals=streams.map(s=>forStream(s.id).reduce((n,i)=>n+i.budget,0));
 $("portfolioStats").innerHTML=[
  ["07","Value streams"],["21","Strategic initiatives"],[money(totalBudget()),"Modeled portfolio investment"],["Value","Outcome-led investment context"]
 ].map(x=>'<div><strong>'+esc(x[0])+'</strong><span>'+esc(x[1])+'</span></div>').join("");
 $("streamCards").innerHTML=streams.map((s,i)=>(
  '<button type="button" class="stream-choice'+(s.id===state.streamId?' selected':'')+'" aria-pressed="'+(s.id===state.streamId)+'" data-stream="'+esc(s.id)+'">'+
   '<span class="stream-top"><span>'+String(i+1).padStart(2,"0")+' / '+esc(s.kind)+'</span><span class="stream-arrow">↗</span></span>'+
   '<strong>'+esc(s.name)+'</strong><span class="stream-under">'+esc(s.goal)+'</span>'+
   '<span class="stream-foot">3 initiatives <span>'+money(totals[i])+' sample</span></span>'+
  '</button>'
 )).join("");
 const s=stream(),arr=forStream(s.id);
 $("initiativeHeading").textContent=s.name+" / 3 initiatives";
 $("streamDescription").textContent=s.goal+". Business owner: "+s.owner+".";
 $("streamType").textContent=s.kind.toUpperCase()+" STREAM";
 $("initiativeCards").innerHTML=arr.map((item,j)=>(
  '<button type="button" class="initiative-choice'+(item.id===state.initiativeId?' selected':'')+'" aria-pressed="'+(item.id===state.initiativeId)+'" data-initiative="'+esc(item.id)+'">'+
  '<span class="init-meta"><span>INITIATIVE 0'+(j+1)+' · '+esc(item.priority)+'</span><span>'+esc(item.lob)+'</span></span>'+
  '<strong>'+esc(item.name)+'</strong><span class="init-problem">'+esc(item.problem)+'</span>'+
  '<span class="init-kpis"><b>'+esc(item.baseline)+' → '+esc(item.target)+'</b><span>'+esc(item.kpi)+'</span></span>'+
  '<span class="init-bottom">'+money(item.budget)+' · '+item.duration+' months <span>SELECT ↗</span></span></button>'
 )).join("");
 $("selectionInsight").textContent="Selected: "+current().name+" ("+current().lob+"). A delivery manager would validate the "+current().baseline+" baseline and "+current().target+" target with "+s.owner+" before committing a plan.";
}
function renderJourney(){
 const x=current(),s=stream(),completed=gates();
 $("journeyContext").innerHTML=
  '<div><small>SELECTED INITIATIVE</small><strong>'+esc(x.name)+'</strong><span>'+esc(x.lob)+'</span></div>'+
  '<div><small>MODEL INVESTMENT</small><strong>'+money(x.budget)+'</strong><span>'+x.duration+' month baseline</span></div>'+
  '<div><small>BUSINESS OUTCOME</small><strong>'+esc(x.baseline)+' → '+esc(x.target)+'</strong><span>'+esc(x.kpi)+'</span></div>';
 $("businessFlow").innerHTML=s.flow.map((step,i)=>'<div class="flow-step"><span>0'+(i+1)+'</span><strong>'+esc(step)+'</strong></div>').join('<span class="flow-arrow" aria-hidden="true">→</span>');
 $("beforeAfter").innerHTML='<div><small>CURRENT STATE / HYPOTHESIS</small><p>'+esc(x.problem)+'</p></div><div><small>FUTURE STATE / PROPOSED</small><p>'+esc(x.future)+'</p></div>';
 $("phaseStepper").innerHTML=phases.map((p,i)=>(
  '<button type="button" data-phase="'+i+'" class="phase-chip'+(state.stage===i?' selected':'')+(completed.has(i)?' done':'')+'" aria-pressed="'+(state.stage===i)+'">'+
  '<small>'+String(i+1).padStart(2,"0")+'</small><b>'+esc(p.short)+'</b><span>'+(completed.has(i)?"✓":"·")+'</span></button>'
 )).join("");
 $("stageProgress").textContent=completed.size+" of "+phases.length+" simulated gates confirmed";
 renderPhase();
}
function currentWindow(index,duration){
 const a=[0,.06,.14,.20,.27,.36,.62,.78,.90,.98][index];
 const b=[.06,.14,.20,.27,.36,.62,.78,.90,.98,1.0][index];
 const start=Math.max(1,Math.floor(a*duration)+1),end=Math.max(start,Math.ceil(b*duration));
 return "Model month "+start+(start===end?"":"–"+end);
}
function perPhaseEvidence(i,x,s){
 const examples=[
  "Investment hypothesis: improve "+x.kpi.toLowerCase()+" from "+x.baseline+" toward "+x.target+".",
  "Observed problem to validate: "+x.problem+" Gap to future state: "+x.future,
  "Initial investment estimate "+money(x.budget)+" for "+x.duration+" months; finance to validate contingency and benefits owner.",
  "Dependencies to baseline: "+x.dependency+"; partner concern: "+x.partners+".",
  "Future-state acceptance: "+x.future+" Systems / data: "+s.systems+".",
  "Demonstrate tested increments for "+x.lob+"; evidence of "+x.dependency+" readiness.",
  "Pilot must test risk scenario: "+x.risk+" and confirm training, access and vendor controls.",
  "Change impact: prepare "+s.owner+" users for "+x.future+".",
  "Benefit: compare post-launch actual "+x.kpi+" with baseline "+x.baseline+" and target "+x.target+". Actual remains unmeasured in this demo.",
  "Financial close and handoff: reconcile "+money(x.budget)+" baseline, vendor commitments, residual risks, lessons and operations ownership."
 ];
 return examples[i];
}
function renderPhase(){
 const p=phases[state.stage],x=current(),s=stream(),completed=gates();
 $("phaseDetail").innerHTML=
  '<div class="detail-top"><span class="overline">STAGE '+String(state.stage+1).padStart(2,"0")+' / 10 · '+currentWindow(state.stage,x.duration)+'</span><span class="stage-badge">'+(completed.has(state.stage)?"DEMO GATE CONFIRMED":"GATE NOT YET CONFIRMED")+'</span></div>'+
  '<h2>'+esc(p.name)+'</h2><p class="detail-purpose">'+esc(p.purpose)+'</p>'+
  '<div class="detail-callout"><span>IN THIS '+esc(x.lob.toUpperCase())+' CASE</span><p>'+esc(perPhaseEvidence(state.stage,x,s))+'</p></div>'+
  '<div class="detail-grid">'+
  '<article><small>WHAT I DO AS PROJECT / DELIVERY MANAGER</small><p>'+esc(p.pm)+'</p></article>'+
  '<article><small>WHAT I NEED FROM THE TEAMS</small><p>'+esc(p.inputs)+'</p></article>'+
  '<article><small>PROJECT ARTIFACTS / EVIDENCE</small><p>'+esc(p.evidence)+'</p></article>'+
  '<article><small>APPROVAL / EXIT CRITERION</small><p>'+esc(p.gate)+'</p></article>'+
  '</div>'+
  '<div class="fine-note"><strong>Governance:</strong> The model simulates a checkpoint only. Real approvals require documented evidence and an authorized business / PMO decision-maker.</div>';
 $("prevStage").disabled=state.stage===0;
 $("nextStage").disabled=state.stage===phases.length-1;
 $("completeStage").textContent=completed.has(state.stage)?"Gate confirmed in demo ✓":"Simulate gate confirmation ✓";
}
function markGate(){
 const completed=gates(),index=state.stage;
 if(completed.has(index)){notify("Gate already simulated. Reset the lifecycle to start again.");return;}
 if(index>0&&!completed.has(index-1)){notify("Governance control: complete preceding stage "+String(index).padStart(2,"0")+" before confirming this gate.");return;}
 completed.add(index);renderJourney();
 notify("Stage gate recorded for "+phases[index].short+". Retain authorized approval evidence.");
}
function charterHtml(x,s){
 const contingency=+(x.budget*.10).toFixed(2),base=+(x.budget-contingency).toFixed(2);
 return '<div class="desk-grid"><article class="paper wide"><span class="overline">INITIATIVE CHARTER / HYPOTHESIS</span><h3>'+esc(x.name)+'</h3>'+
 '<div class="data-lines"><div><b>Business problem</b><p>'+esc(x.problem)+'</p></div><div><b>Future-state opportunity</b><p>'+esc(x.future)+'</p></div><div><b>Executive sponsor</b><p>'+esc(s.owner)+'</p></div><div><b>Success definition</b><p>'+esc(x.kpi)+': validate '+esc(x.baseline)+' baseline, then aim for '+esc(x.target)+'; measure sustained adoption, quality and controls post-release.</p></div></div></article>'+
 '<article class="paper"><span class="overline">BUSINESS CASE / MODEL</span><h3>Investment assumptions <button class="help" data-tip="financial" aria-label="Financial management guidance">i</button></h3><div class="finance-line"><span>Model initiative budget</span><b>'+money(x.budget)+'</b></div><div class="finance-line"><span>Indicative delivery / vendor cost</span><b>'+money(base)+'</b></div><div class="finance-line"><span>Included contingency (10%)</span><b>'+money(contingency)+'</b></div><div class="finance-line"><span>Delivery horizon</span><b>'+x.duration+' months</b></div><p class="small-note">Finance validates cost centers, CapEx / OpEx, estimate assumptions, benefits ownership and approval.</p></article>'+
 '<article class="paper"><span class="overline">SCOPE AND EXCLUSIONS</span><h3>Boundaries and acceptance</h3><ul class="lined"><li>In scope: '+esc(x.future)+'</li><li>In scope: '+esc(x.dependency)+' interfaces and exception handling</li><li>In scope: testing, operational adoption and measured KPI</li><li>Out of scope: enterprise-wide platform replacement without separate authorization</li><li>Acceptance: business owner signs controlled end-to-end scenario and release criteria</li></ul></article></div>';
}
function planHtml(x,s){
 return '<div class="desk-grid"><article class="paper wide"><div class="panel-heading mini"><div><span class="overline">INTEGRATED SCHEDULE</span><h3>Milestones and interdependencies <button class="help" data-tip="cp" aria-label="Critical path explanation">i</button></h3></div><span class="micro-tag">'+x.duration+' MONTH BASELINE</span></div>'+
 '<div class="milestone-table"><table><thead><tr><th>Stage</th><th>Indicative time</th><th>Evidence / output</th><th>Gate owner</th></tr></thead><tbody>'+
 phases.map((p,i)=>'<tr><td>'+esc(p.short)+'</td><td>'+currentWindow(i,x.duration)+'</td><td>'+esc(p.evidence.split(" · ")[0])+'</td><td>'+esc(i===2||i===8?"Sponsor / finance":i===5?"Tech + PO":i===6?"Business + QA":"Delivery + business")+'</td></tr>').join("")+
 '</tbody></table></div><p class="small-note">Phases may overlap; validate milestone dates and dependencies when baselining the integrated plan.</p></article>'+
 '<article class="paper"><span class="overline">CRITICAL PATH / ESCALATION</span><h3>Primary dependency</h3><p>'+esc(x.dependency)+'</p><ul class="lined"><li>Tech lead: integration plan, interface acceptance and fallback</li><li>PM: coordinate upstream dates and escalation threshold</li><li>Product owner: protect release scope if a dependency slips</li><li>Sponsor: decide material scope/date/budget trade-offs</li></ul></article>'+
 '<article class="paper"><span class="overline">SCHEDULE CONTROLS</span><h3>My weekly follow-up</h3><ul class="lined"><li>Deliverables due and accepted vs. plan</li><li>Milestone confidence and look-ahead (2–4 weeks)</li><li>Critical path handoffs across Agile teams and vendors</li><li>People / skill capacity against approved work</li><li>Forecast changes and recovery recommendations</li></ul></article></div>';
}
function peopleHtml(x,s){
 return '<div class="desk-grid"><article class="paper wide"><span class="overline">CONTRIBUTOR MAP / ACCOUNTABILITY</span><h3>'+x.people+' modeled participants across business, IT and partners</h3>'+
 '<div class="role-table"><table><thead><tr><th>Function</th><th>Accountability / expected output</th></tr></thead><tbody>'+
 roles.map(r=>'<tr><td>'+esc(r[0])+'</td><td>'+esc(r[1])+'</td></tr>').join("")+'</tbody></table></div></article>'+
 '<article class="paper"><span class="overline">RESOURCE FORECAST</span><h3>Typical participation</h3><div class="res-list"><div><b>1</b><span>Delivery / Program PM</span></div><div><b>7–10</b><span>Agile feature delivery members</span></div><div><b>3–5</b><span>Claims/UW/business + BAs</span></div><div><b>4–6</b><span>Integration, data, QA and security</span></div><div><b>2–5</b><span>Change and third-party contributors</span></div></div><p class="small-note">Not all work full-time; do not sum these ranges into an exact staffing plan.</p></article>'+
 '<article class="paper"><span class="overline">THIRD-PARTY DELIVERY</span><h3>Named partner dependencies <button class="help" data-tip="vendor" aria-label="Third-party delivery guidance">i</button></h3><p>'+esc(x.partners)+'</p><ul class="lined"><li>Confirm contracted deliverables and acceptance criteria</li><li>Track milestones, escalation and integration SLAs</li><li>Forecast financial commitments / invoice timing</li><li>Record decisions and resolve cross-party handoffs</li></ul></article></div>';
}
function riskHtml(x,s){
 const risks=[
 ["High","RISK",x.risk,"Business / compliance","Validate control scenarios in design; QA tests negative paths and receives formal sign-off."],
 ["High","DEPENDENCY",x.dependency,"Tech / integration lead","Obtain dated interface commitments, contract tests, fallback design and weekly readiness evidence."],
 ["Medium","ISSUE / BLOCKER",x.partners,"Vendor / process owner","Agree accountable owner, due date, alternative workflow and sponsor escalation trigger."],
 ["Medium","CHANGE", "Teams adopt "+x.future,"Operations / change lead","Train role-based journeys, build exception playbook and review post-release adoption."]
 ];
 return '<div class="desk-grid"><article class="paper wide"><div class="panel-heading mini"><div><span class="overline">RAID EXAMPLES FOR THIS INITIATIVE</span><h3>Risks, assumptions, issues and dependencies <button class="help" data-tip="risk" aria-label="Explain RAID categories">i</button></h3></div><span class="micro-tag">WEEKLY REVIEW</span></div>'+
 risks.map((r,i)=>'<div class="risk-item"><span class="risk-flag '+(r[0]==="High"?"high":"med")+'">'+esc(r[0])+'</span><div><small>'+esc(r[1])+' · OWNER: '+esc(r[3])+'</small><b>'+esc(r[2])+'</b><p><strong>Mitigation:</strong> '+esc(r[4])+'</p></div></div>').join("")+'</article>'+
 '<article class="paper"><span class="overline">DECISION LOG EXAMPLES</span><h3>Who decides what?</h3><ul class="lined"><li><strong>Portfolio sponsor:</strong> Approve '+money(x.budget)+' funding limit / contingency use</li><li><strong>Business owner:</strong> Accept '+esc(x.kpi)+' success criteria and pilot adoption</li><li><strong>Tech lead:</strong> Confirm '+esc(x.dependency)+' solution readiness</li><li><strong>QA + operational owner:</strong> Provide test / training evidence for release</li></ul><p class="small-note">Track ID, owner, due date, rationale and signed decision outcome.</p></article>'+
 '<article class="paper"><span class="overline">ESCALATION THRESHOLDS</span><h3>What goes to leadership</h3><ul class="lined"><li>Forecast variance exceeds authorized tolerance</li><li>Regulatory / policy or customer harm risk arises</li><li>Critical path has no credible recovery owner</li><li>Scope reprioritization crosses value-stream guardrails</li><li>Vendor dispute blocks contractual acceptance</li></ul></article></div>';
}
function releaseHtml(x,s){
 return '<div class="desk-grid"><article class="paper wide"><span class="overline">END-TO-END RELEASE CONFIDENCE</span><h3>Quality, UAT and adoption gates <button class="help" data-tip="qa" aria-label="Explain release gates">i</button></h3>'+
 '<div class="release-grid">'+
 [["01","Functional & regression tests","Critical commercial / specialty coverage and workflow variants"],
  ["02","Integration & reconciliation","Policy / claims / billing interfaces, duplicates and audit trail"],
  ["03","Security & permissions","Broker, underwriter, adjuster and vendor role segregation"],
  ["04","Business UAT / exceptions",x.risk],
  ["05","Vendor / SLA acceptance",x.partners],
  ["06","Operations / change readiness","Training, playbooks, rollback and hypercare ownership"]
 ].map(r=>'<div><span>'+r[0]+'</span><b>'+esc(r[1])+'</b><p>'+esc(r[2])+'</p></div>').join("")+'</div></article>'+
 '<article class="paper"><span class="overline">OPERATIONS HANDOVER</span><h3>From project to value stream</h3><ul class="lined"><li>Release and cutover approvals retained</li><li>Claims / underwriting operations lead trained</li><li>Support owner and incident paths confirmed</li><li>Residual defects and known exceptions accepted</li><li>Unfinished improvements moved to owned backlog</li></ul></article>'+
 '<article class="paper"><span class="overline">BENEFITS EVIDENCE</span><h3>Target ≠ actual <button class="help" data-tip="benefits" aria-label="Business value validation">i</button></h3><div class="finance-line"><span>Measure</span><b>'+esc(x.kpi)+'</b></div><div class="finance-line"><span>Baseline hypothesis</span><b>'+esc(x.baseline)+'</b></div><div class="finance-line"><span>Target hypothesis</span><b>'+esc(x.target)+'</b></div><div class="finance-line"><span>Actual / observed</span><b>Not measured</b></div><p class="small-note">Record actuals at agreed post-release intervals and have the benefit owner verify attributable changes.</p></article></div>';
}
function renderDesk(){
 const x=current(),s=stream();
 document.querySelectorAll("[data-desk]").forEach(b=>{
  const active=b.dataset.desk===state.deskTab;
  b.classList.toggle("active",active);b.setAttribute("aria-selected",String(active));
 });
 const render={charter:charterHtml,plan:planHtml,people:peopleHtml,risk:riskHtml,release:releaseHtml};
 $("deskContent").innerHTML=render[state.deskTab](x,s);
}
function readControls(){
 state.delay=Number($("delay").value);state.squads=Number($("squads").value);
 state.phased=$("phased").checked;state.qa=$("qa").checked;
 state.ops=$("ops").checked;state.vendor=$("vendor").checked;
}
function summaryText(){
 const x=current(),m=scenario(x,state),s=stream();
 return [
 "EXECUTIVE DELIVERY BRIEF — Enterprise portfolio scenario",
 "Value stream: "+s.name+" | Initiative: "+x.name+" ("+x.lob+")",
 "Business outcome: "+x.kpi+" from baseline "+x.baseline+" to target "+x.target+" (target outcome)",
 "Schedule: "+m.months.toFixed(1)+" months vs. "+x.duration+" baseline",
 "Financials: "+money(m.eac)+" EAC vs. "+money(x.budget)+" baseline; variance "+money(m.variance),
 "Health: "+m.rag+" | Pilot: "+(m.ready?"All modeled exit controls present":"HOLD — missing QA, operations or partner evidence"),
 "Critical dependency: "+x.dependency,
 "Primary risk: "+x.risk,
 "Decision: "+recommendation(x,m),
 "Cadence: weekly delivery/RAID; monthly finance EAC and business-value report; monthly steering approval review.",
 "Source data: sample records for demonstration."
 ].join("\n");
}
function recommendation(x,m){
 if(!m.ready)return "Do not release pilot before QA, operations and third-party readiness evidence is signed. Review "+x.dependency+" recovery and budget exposure with the sponsor.";
 if(m.rag==="RED")return "Escalate a decision on phased scope, extra capacity or revised schedule/cost. Sponsor approves material change; technical lead assesses feasibility.";
 if(m.rag==="AMBER")return "Keep milestone recovery under weekly review. Confirm integration milestones, scenario cost and business readiness with their respective owners.";
 return "Maintain controls, confirm sponsor approval and use post-release "+x.kpi+" actuals to decide the next value-stream investment.";
}
function renderControl(){
 readControls();const x=current(),m=scenario(x,state);
 $("delayValue").textContent=state.delay+" "+(state.delay===1?"week":"weeks");
 $("squadsValue").textContent=state.squads+" "+(state.squads===1?"squad":"squads");
 $("execTitle").textContent=x.name;
 $("rag").textContent=m.rag;$("rag").className="status-pill "+m.rag.toLowerCase();
 $("forecastMonths").textContent=m.months.toFixed(1);
 $("forecastBasis").textContent="Months vs. "+x.duration+" planned";
 $("forecastEac").textContent=money(m.eac);
 $("budgetBasis").textContent="Against "+money(x.budget)+" baseline";
 $("forecastVariance").textContent=(m.variance>=0?"+":"−")+money(Math.abs(m.variance));
 $("readiness").textContent=m.ready?"READY":"HOLD";
 $("readiness").className=m.ready?"ready":"hold";
 $("recommendation").textContent=recommendation(x,m);
 $("weeklyReport").textContent=m.rag+" status for "+x.name+". Watch "+x.dependency+" and "+x.partners+". "+(m.slippage>0?"Forecast delay "+m.slippage+" months.":"No modeled schedule overrun.");
 $("monthlyReport").textContent="Baseline "+money(x.budget)+"; EAC "+money(m.eac)+"; variance "+(m.variance>=0?"+":"−")+money(Math.abs(m.variance))+". Reconcile finance actuals and resources before executive sign-off.";
 $("benefitReport").textContent=x.kpi+": baseline "+x.baseline+", target "+x.target+". Actual not yet measured. Sponsor to validate operational benefit and adoption.";
}
function renderGovernance(){
 const steps=[
 ["01","Prioritize outcomes","Define business value at the stream, not only project scope."],
 ["02","Set funding guardrails","Leadership sets budget, capacity and approval boundaries."],
 ["03","Visualize demand and WIP","Use portfolio Kanban to expose overloaded teams and pending decisions."],
 ["04","Link to existing Agile teams","Keep delivery rhythms; coordinate backlog dependencies and releases."],
 ["05","Inspect outcomes monthly","Compare cost, risk, progress and operational value—not sprint metrics alone."],
 ["06","Coach and adapt","Improve cross-team handoffs and portfolio decisions; escalate organization-wide changes."]
 ];
 $("adoptionGrid").innerHTML=steps.map(x=>'<article><span>'+x[0]+'</span><h3>'+x[1]+'</h3><p>'+x[2]+'</p></article>').join("");
}
function renderRequirements(){
 $("reqCount").textContent=jd.reduce((n,g)=>n+g.items.length,0);
 $("requirementGroups").innerHTML=jd.map((g,i)=>(
  '<details '+(i===0?'open':'')+'><summary><span><small>SECTION 0'+(i+1)+'</small><b>'+esc(g.title)+'</b></span><span>'+g.items.length+' covered <i>＋</i></span></summary>'+
  '<div class="req-list">'+g.items.map((item,j)=>'<div><span>'+String(j+1).padStart(2,"0")+'</span><p>'+esc(item)+'</p><button type="button" data-jump="'+esc(g.link)+'">View evidence ↗</button></div>').join("")+'</div></details>'
 )).join("");
}
function renderAll(){updateContext();renderPortfolio();renderJourney();renderDesk();renderControl();renderGovernance();renderRequirements();}
document.addEventListener("click",e=>{
 const target=e.target;
 const s=target.closest("[data-stream]");if(s){selectStream(s.dataset.stream);return;}
 const i=target.closest("[data-initiative]");if(i){selectInitiative(i.dataset.initiative);return;}
 const p=target.closest("[data-phase]");if(p){state.stage=Number(p.dataset.phase);renderJourney();return;}
 const tab=target.closest("[data-desk]");if(tab){state.deskTab=tab.dataset.desk;renderDesk();return;}
 const jump=target.closest("[data-jump]");if(jump){route(jump.dataset.jump);return;}
 const page=target.closest("[data-route]");if(page){e.preventDefault();route(page.dataset.route);return;}
 const help=target.closest("[data-tip]");if(help){const key=help.dataset.tip;$("helpTitle").textContent=key.replace(/(^|\s)\S/g,s=>s.toUpperCase());$("helpBody").textContent=tips[key]??"Select a specific context control for details.";$("helpDialog").showModal();return;}
});
window.addEventListener("hashchange",()=>route(location.hash.slice(1),false));
$("closeHelp").addEventListener("click",()=>$("helpDialog").close());
$("helpDone").addEventListener("click",()=>$("helpDialog").close());
$("helpDialog").addEventListener("click",e=>{if(e.target===$("helpDialog"))$("helpDialog").close();});
$("prevStage").addEventListener("click",()=>{state.stage=Math.max(0,state.stage-1);renderJourney();});
$("nextStage").addEventListener("click",()=>{state.stage=Math.min(phases.length-1,state.stage+1);renderJourney();});
$("completeStage").addEventListener("click",markGate);
$("resetProgress").addEventListener("click",()=>{state.gates[state.initiativeId]=new Set();state.stage=0;renderJourney();notify("Simulated gate history reset for this initiative.");});
for(const id of ["delay","squads","phased","qa","ops","vendor"])$(id).addEventListener("input",renderControl);
$("loadScenario").addEventListener("click",()=>resetLevers(true));
$("copySummary").addEventListener("click",async()=>{
 const text=summaryText();
 try{if(navigator.clipboard?.writeText)await navigator.clipboard.writeText(text);
 else{const area=document.createElement("textarea");area.value=text;document.body.appendChild(area);area.select();const ok=document.execCommand("copy");area.remove();if(!ok)throw Error("Copy unavailable");}
 $("copyFeedback").textContent="Copied. Personalize the assumptions before sharing.";
 }catch(_){$("copyFeedback").textContent="Copy unavailable in this browser. You can select the figures directly.";}
});
$("present").addEventListener("click",()=>{
 const now=document.body.classList.toggle("presenting");
 $("present").textContent=now?"Exit presentation ↙":"Present ↗";
 notify(now?"Presentation layout enabled.":"Standard navigation restored.");
});
document.addEventListener("keydown",e=>{
 if(e.key==="Escape"&&document.body.classList.contains("presenting"))$("present").click();
});
const tourPages=["portfolio","journey","desk","control","governance","requirements"];
const tourNotes=[
 "1/6 · Select a stream and one of its three initiatives. All downstream project views update.",
 "2/6 · Explore every delivery gate from initiation to measurable benefits and closeout.",
 "3/6 · Inspect the charter, schedule, team responsibilities, RAID, decisions and release plan.",
 "4/6 · Simulate delays, capacity and release readiness; read the changing executive forecast.",
 "5/6 · Compare waterfall portfolio control with value-stream funding and the first 90 days.",
 "6/6 · Explore enterprise delivery capabilities and professional operating principles."
];
$("startTour").addEventListener("click",()=>{const n=state.tour%tourPages.length;route(tourPages[n]);notify(tourNotes[n]);state.tour=n+1;});
renderAll();route(location.hash.slice(1),false);
