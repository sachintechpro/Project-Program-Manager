import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {execFileSync} from "node:child_process";
import {fileURLToPath} from "node:url";
import {streams,initiatives,phases,scenario,forStream,getStream,getInitiative,totalBudget,jd,roles,tips} from "../portfolio-data.js";

test("value stream library has seven distinct realistic business / enabling streams",()=>{
 assert.equal(streams.length,7);
 assert.equal(new Set(streams.map(x=>x.id)).size,7);
 assert.equal(streams.filter(x=>x.kind==="Business").length,6);
 assert.equal(streams.filter(x=>x.kind==="Enabling").length,1);
 assert(streams.every(s=>s.flow.length===5&&s.owner&&s.systems&&s.goal));
});
test("each stream has exactly three complete, distinct commercial / specialty initiatives",()=>{
 assert.equal(initiatives.length,21);
 assert.equal(new Set(initiatives.map(x=>x.id)).size,21);
 assert(streams.every(s=>forStream(s.id).length===3));
 for(const i of initiatives){
  assert(streams.some(s=>s.id===i.streamId));
  assert(i.name&&i.lob&&i.problem&&i.future&&i.kpi&&i.baseline&&i.target);
  assert(i.budget>0&&i.duration>=9&&i.duration<=15);
  assert(i.dependency&&i.partners&&i.risk);
  assert.equal(getInitiative(i.id).id,i.id);
 }
 assert.equal(forStream("claims").length,3);
 assert.equal(getStream("claims").name,"Claims Resolution");
});
test("end-to-end delivery has ten owned gates with team inputs and documented outputs",()=>{
 assert.equal(phases.length,10);
 for(const [n,p] of phases.entries()){
  assert.equal(n,p.index);
  for(const k of ["short","name","purpose","pm","inputs","evidence","gate"])assert(p[k]?.length>(k==="short"?1:12));
 }
 assert(phases[0].short==="Intake");
 assert(phases.at(-1).short==="Close");
});
test("increase in upstream delay cannot improve forecast cost or schedule across all initiatives",()=>{
 for(const i of initiatives){
  const first=scenario(i,{delay:0});
  const later=scenario(i,{delay:7});
  assert(later.months>first.months, i.id);
  assert(later.eac>first.eac, i.id);
 }
});
test("adding squads changes schedule and cost in expected opposite directions",()=>{
 for(const i of initiatives){
  const old=scenario(i,{delay:5,squads:0});
  const newOne=scenario(i,{delay:5,squads:2});
  assert(newOne.months<old.months);
  assert(newOne.eac>old.eac);
 }
});
test("readiness requires all three release control types",()=>{
 const x=initiatives[0];
 for(const key of ["qa","ops","vendor"]){
  const input={qa:true,ops:true,vendor:true};
  input[key]=false;
  assert.equal(scenario(x,input).ready,false);
 }
 assert.equal(scenario(x,{qa:true,ops:true,vendor:true}).ready,true);
});
test("boundaries, health statuses and capital accounting remain finite",()=>{
 for(const i of initiatives){
  const extreme=scenario(i,{delay:999,squads:999});
  const clamped=scenario(i,{delay:10,squads:3});
  assert.deepEqual(extreme,clamped);
  assert(["GREEN","AMBER","RED"].includes(extreme.rag));
  assert.equal(Number((extreme.eac-i.budget).toFixed(2)),extreme.variance);
 }
 assert(totalBudget()>30&&totalBudget()<60);
});
test("coverage matrix accounts for formal competencies, role requirements and culture",()=>{
 assert.equal(jd.length,4);
 assert(jd.reduce((n,g)=>n+g.items.length,0)>=24);
 for(const part of jd)assert(part.items.length>=5);
 assert(roles.length>=8);
 for(const k of ["lpm","eac","rag","risk","cp","qa","coaching","authority"]){
  // "coaching" may be represented as coach in UI.
  if(k==="coaching")assert(tips.coach);else assert(tips[k]);
 }
});
test("workbench HTML contains all six navigable panels and both live selection collections",()=>{
 const html=readFileSync(new URL("../index.html",import.meta.url),"utf8");
 for(const p of ["portfolio","journey","desk","control","governance","requirements"]){
  assert(html.includes('id="'+p+'"'),p);
  assert(html.includes('data-route="'+p+'"'),p);
 }
 for(const id of ["streamCards","initiativeCards","phaseStepper","deskContent","rag","requirementGroups","helpDialog","copySummary"]){
  assert(html.includes('id="'+id+'"'),id);
 }
 assert(html.includes("./claims.html#brief"));
 assert(html.includes("SAMPLE DATA FOR DEMONSTRATION"));
 assert(html.includes("06 / DELIVERY CAPABILITY MAP"));
});
test("JavaScript modules parse, CSS defines responsive mobile navigation, original case remains intact",()=>{
 const dir=new URL("../",import.meta.url);
 for(const file of ["portfolio-data.js","workbench.js","model.js","app.js"]){
  execFileSync(process.execPath,["--check",fileURLToPath(new URL(file,dir))]);
 }
 const css=readFileSync(new URL("../workbench.css",import.meta.url),"utf8");
 assert(css.includes("@media(max-width:720px)"));
 assert(css.includes(".sidebar"));
 const archived=readFileSync(new URL("../claims.html",import.meta.url),"utf8");
 assert(archived.includes('id="brief"')&&archived.includes('id="control"'));
});
