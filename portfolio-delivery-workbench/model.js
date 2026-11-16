/**
 * Independent portfolio delivery simulation with sample business and delivery data.
 * Forecast assumptions are configurable and intended for demonstrating delivery controls.
 */
export const initiatives = [
  {
    id:"property",
    name:"Commercial Property FNOL",
    lob:"Commercial property",
    problem:"Broker-submitted notices arrive through email, forms and catastrophe queues; rekeying delays registration.",
    outcome:"Reduce average first-notice-to-registration time, with auditable broker acknowledgments.",
    baseline:"46 hours",
    target:"4 hours",
    budget:2.8,
    duration:11,
    status:"In delivery",
    lead:"Claims operations + platform delivery"
  },
  {
    id:"workers",
    name:"Workers' Comp Triage",
    lob:"Workers' compensation",
    problem:"State-sensitive injury claims require coverage checks, jurisdiction rules and suitable adjuster assignment.",
    outcome:"Reduce time from registration to appropriate adjuster ownership without bypassing regulatory checks.",
    baseline:"2 days",
    target:"6 hours",
    budget:2.1,
    duration:10,
    status:"Discovery",
    lead:"Claims operations + compliance"
  },
  {
    id:"cyber",
    name:"Cyber Incident Response",
    lob:"Specialty cyber",
    problem:"Breach-response cases require timely authorization and coordination of approved forensics, legal and response vendors.",
    outcome:"Reduce time to authorize and mobilize approved incident-response partners.",
    baseline:"36 hours",
    target:"8 hours",
    budget:1.7,
    duration:12,
    status:"Proposed",
    lead:"Specialty claims + vendor management"
  }
];

export const sample = Object.freeze({
  integrationDelayWeeks:3,
  extraSquads:0,
  phasedRollout:true,
  pilotQaClear:false,
  operationsTrained:true,
  vendorSlaSigned:false
});

export function estimateScenario(values = sample) {
  const delay = limit(values.integrationDelayWeeks,0,8);
  const squads = limit(values.extraSquads,0,2);
  const phased = Boolean(values.phasedRollout);
  const plannedMonths=11;
  // Simulated schedule impact; intentionally does NOT forecast guaranteed business value.
  const months = +(plannedMonths + delay*0.23 - squads*0.65 - (phased?0.6:0)).toFixed(1);
  const eac = +(2.8 + delay*0.055 + squads*0.18 + (phased?0.08:0)).toFixed(2);
  const variance=+(eac-2.8).toFixed(2);
  const gateReady=Boolean(values.pilotQaClear && values.operationsTrained && values.vendorSlaSigned);
  const rag=months>12 || eac>3.15 ? "RED" : months>11 || eac>2.96 || !gateReady ? "AMBER" : "GREEN";
  const rationale = months>12 ? "Forecast exceeds 12-month delivery guardrail" : eac>3.15 ? "Forecast exceeds modeled budget tolerance" : !gateReady ? "Pilot release gate remains open" : months>11||eac>2.96 ? "Schedule or cost requires close attention" : "Within modeled guardrails";
  return {months,eac,variance,rag,gateReady,rationale, plannedMonths, originalBudget:2.8};
}
function limit(v,min,max){return Math.max(min,Math.min(max,Number(v)||0));}
