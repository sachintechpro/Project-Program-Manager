import {initiatives, sample, estimateScenario} from "./model.js";
const $=(id)=>document.getElementById(id);
const pages=[...document.querySelectorAll(".page")];
const nav=[...document.querySelectorAll("[data-page]")];
function route(name,focus=false){
 const page=pages.find(p=>p.id===name)||pages[0];
 for(const item of pages){
  const active=item===page;
  item.classList.toggle("visible",active);
  item.setAttribute("aria-hidden",String(!active));
 }
 for(const a of nav){
  const active=a.dataset.page===page.id;
  a.classList.toggle("active",active);
  if(active)a.setAttribute("aria-current","page");else a.removeAttribute("aria-current");
 }
 if(location.hash!=="#"+page.id)history.replaceState(null,"","#"+page.id);
 window.scrollTo({top:0,behavior:"instant"});
 if(focus){const h=page.querySelector("h1");if(h){h.tabIndex=-1;h.focus({preventScroll:true});}}
}
window.addEventListener("hashchange",()=>route(location.hash.slice(1),false));
nav.forEach(a=>a.addEventListener("click",e=>{e.preventDefault();route(a.dataset.page,true);}));
document.querySelectorAll("[data-go]").forEach(button=>button.addEventListener("click",()=>route(button.dataset.go,true)));
document.querySelector("footer a[href='#brief']").addEventListener("click",e=>{e.preventDefault();route("brief",true);});
const esc=s=>String(s).replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[m]));
$("initiatives").innerHTML=initiatives.map((item,i)=>(
 '<article class="initiative">'+
 '<span class="init-num">INITIATIVE / 0'+(i+1)+' · '+esc(item.status)+'</span>'+
 '<span class="lob">'+esc(item.lob)+'</span>'+
 '<h3>'+esc(item.name)+'</h3>'+
 '<p>'+esc(item.problem)+'</p>'+
 '<div class="init-outcome"><strong>Intended improvement</strong><br>'+esc(item.outcome)+'</div>'+
 '<div class="init-foot"><span>'+esc(item.baseline)+' → '+esc(item.target)+'</span><span>$'+item.budget.toFixed(1)+'m model</span></div>'+
 '</article>'
)).join("");
const ids={delay:$("delay"),squads:$("squads"),phased:$("phased"),qa:$("qa"),trained:$("trained"),sla:$("sla")};
function state(){
 return {integrationDelayWeeks:Number(ids.delay.value),extraSquads:Number(ids.squads.value),phasedRollout:ids.phased.checked,pilotQaClear:ids.qa.checked,operationsTrained:ids.trained.checked,vendorSlaSigned:ids.sla.checked};
}
function render(){
 const s=state(),m=estimateScenario(s);
 $("delayOut").textContent=s.integrationDelayWeeks+" "+(s.integrationDelayWeeks===1?"week":"weeks");
 $("squadsOut").textContent=s.extraSquads+" "+(s.extraSquads===1?"squad":"squads");
 $("months").textContent=m.months.toFixed(1);
 $("eac").textContent="$"+m.eac.toFixed(2)+"m";
 $("variance").textContent=(m.variance>=0?"+":"-")+"$"+Math.abs(m.variance).toFixed(2)+"m";
 $("gate").textContent=m.gateReady?"READY":"HOLD";
 $("gate").style.color=m.gateReady?"#a5e3c5":"#ffd9a4";
 $("rag").textContent=m.rag;
 $("rag").className="rag "+m.rag.toLowerCase();
 $("rationale").textContent=m.rationale;
 $("decision").textContent=!m.gateReady
   ? "Hold pilot until all exit controls are evidenced. "+(m.months>11||m.eac>2.96?"Review integration mitigation, forecast and accountable approver.":"Continue readiness review.")
   : m.rag==="RED"
     ? "Escalate options to sponsor: phase scope, address the dependency or approve a revised date/cost within governance."
     : m.rag==="AMBER"
       ? "Review the recovery options and EAC with the sponsor; retain a weekly checkpoint on the affected dependency."
       : "Pilot gate is ready in this model. Business owner approves actual release after evidence review.";
}
for(const input of Object.values(ids))input.addEventListener("input",render);
$("reset").addEventListener("click",()=>{
 ids.delay.value=sample.integrationDelayWeeks;ids.squads.value=sample.extraSquads;
 ids.phased.checked=sample.phasedRollout;ids.qa.checked=sample.pilotQaClear;
 ids.trained.checked=sample.operationsTrained;ids.sla.checked=sample.vendorSlaSigned;
 render();
});
$("presentMode").addEventListener("click",()=>{
 const active=document.body.classList.toggle("presentation");
 $("presentMode").textContent=active?"Exit presentation mode ↙":"Presentation mode ↗";
});
window.addEventListener("keydown",e=>{
 if(e.key==="Escape"&&document.body.classList.contains("presentation"))$("presentMode").click();
});
route(location.hash.slice(1),false);render();
