import test from "node:test";
import assert from "node:assert/strict";
import {estimateScenario,initiatives,sample} from "../model.js";

test("three initiatives are distinct commercial/specialty lines",()=>{
  assert.equal(initiatives.length,3);
  assert.equal(new Set(initiatives.map(x=>x.id)).size,3);
  assert(initiatives.every(x=>x.budget>0&&x.duration>0));
});
test("sample forecast is deterministic",()=>{
  const a=estimateScenario(sample);
  assert.deepEqual(a,estimateScenario({...sample}));
  assert(a.eac>0);
});
test("longer integration delay does not improve schedule or cost",()=>{
  const early=estimateScenario({...sample,integrationDelayWeeks:0});
  const late=estimateScenario({...sample,integrationDelayWeeks:8});
  assert(late.months>early.months);
  assert(late.eac>early.eac);
});
test("additional squads trade cost for speed",()=>{
  const base=estimateScenario({...sample,extraSquads:0});
  const plus=estimateScenario({...sample,extraSquads:2});
  assert(plus.months<base.months);
  assert(plus.eac>base.eac);
});
test("pilot gate requires QA, training and vendor approval",()=>{
  const fail=estimateScenario({...sample,pilotQaClear:true,vendorSlaSigned:false});
  const pass=estimateScenario({...sample,pilotQaClear:true,vendorSlaSigned:true});
  assert.equal(fail.gateReady,false);
  assert.equal(pass.gateReady,true);
});
test("out-of-range inputs are clamped",()=>{
  const a=estimateScenario({...sample,integrationDelayWeeks:200,extraSquads:50});
  const b=estimateScenario({...sample,integrationDelayWeeks:8,extraSquads:2});
  assert.deepEqual(a,b);
});
test("sample does not imply actual insurance-company figures",()=>{
  assert.equal(sample.integrationDelayWeeks,3);
  assert.equal(initiatives[0].lob,"Commercial property");
});

import {readFileSync} from "node:fs";
import {execFileSync} from "node:child_process";
import {fileURLToPath} from "node:url";
test("app script parses before deployment",()=>{
 const file=fileURLToPath(new URL("../app.js",import.meta.url));
 execFileSync(process.execPath,["--check",file]);
});
test("archived Claims presentation retains six original sections and navigation",()=>{
 const html=readFileSync(new URL("../claims.html",import.meta.url),"utf8");
 for(const section of ["brief","portfolio","delivery","control","operating","first90"]){
  assert(html.includes('id="'+section+'"'));
  assert(html.includes('data-page="'+section+'"'));
 }
 assert(html.includes('aria-label="Sections"'));
 assert(html.includes("SAMPLE DATA FOR DEMONSTRATION"));
 assert(html.includes("ENTERPRISE DELIVERY DEEP DIVE"));
 assert(html.includes('href="./index.html#portfolio"'));
 assert(html.includes('class="return-portfolio"'));
});

// Run enhanced workbench regression suite as part of the existing Render build.
import "./workbench.test.mjs";
