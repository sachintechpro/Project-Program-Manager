'use strict';

const LIVE_INDEX = STORE + ':workspaces';
function readLiveIndex() {
  try { return JSON.parse(getStored(LIVE_INDEX)) || []; }
  catch { return []; }
}
function activeWorkspace() {
  return readLiveIndex().find(record => record.id === workspaceId);
}
function workspacePicker() {
  const records = readLiveIndex();
  return `<div class="toolbar workspace-picker"><select class="select" id="workspacePicker" aria-label="Active workspace"><option value="">Training workspace</option>${records.map(r => `<option value="${esc(r.id)}" ${r.id === workspaceId ? 'selected' : ''}>${esc(r.program ? r.program + ' / ' : '')}${esc(r.name)}</option>`).join('')}</select>${btn('＋ Add project or initiative','createWorkspace')}</div>`;
}
function switchWorkspace(id) {
  const next = loadWorkspace(id);
  if (id && !next) { toast('Workspace could not be opened.'); main(); return; }
  workspaceId = id;
  state = next || deep(window.STARTER);
  try { localStorage.setItem(LIVE_INDEX + ':active', id); } catch {}
  tab = 'overview';
  mode = 'project';
  filter = '';
  closeModal();
  main();
}
function openWorkspaceForm() {
  const programs = [...new Set(readLiveIndex().map(r => r.program).filter(Boolean))];
  $('#modal').innerHTML = `<div class="modal" id="modalBg"><form class="dialog" id="newWorkspace" role="dialog" aria-modal="true" aria-labelledby="newWorkspaceTitle">
    <div class="dialog-header"><h2 id="newWorkspaceTitle">Add project or initiative</h2><button type="button" class="btn" data-action="close" aria-label="Close">✕</button></div>
    <div class="dialog-body"><div class="formgrid">
      <label>Type<select class="field" name="kind"><option value="project">Standalone project</option><option value="initiative">Program initiative</option></select></label>
      <label id="programField" hidden>Parent program<input class="field" name="program" list="workspacePrograms" maxlength="100" disabled><datalist id="workspacePrograms">${programs.map(name => `<option value="${esc(name)}"></option>`).join('')}</datalist></label>
      <label>Name<input class="field" name="name" required maxlength="100"></label>
      <label>Owner<input class="field" name="owner" required maxlength="100"></label>
      <label>Sponsor<input class="field" name="sponsor" required maxlength="100"></label>
      <label>Target release<input class="field" name="target" type="date" required></label>
      <label>Business objective<textarea class="field" name="objective" required maxlength="1000"></textarea></label>
    </div><p class="hint" id="workspaceError" role="alert"></p></div>
    <div class="dialog-footer"><span></span><button type="submit" class="btn primary">Create workspace</button></div>
  </form></div>`;
  const form = $('#newWorkspace');
  form.elements.name.focus();
  form.elements.kind.addEventListener('change', () => {
    const initiative = form.elements.kind.value === 'initiative';
    $('#programField').hidden = !initiative;
    form.elements.program.required = initiative;
    form.elements.program.disabled = !initiative;
  });
  form.addEventListener('submit', event => {
    event.preventDefault();
    const input = Object.fromEntries([...new FormData(form)].map(([key, value]) => [key, value.trim()]));
    const error = $('#workspaceError');
    const today = new Date().toLocaleDateString('en-CA');
    if (!['name','owner','sponsor','objective','target'].every(key => input[key]) || (input.kind === 'initiative' && !input.program)) {
      error.textContent = 'Complete all required fields.'; return;
    }
    if (input.target < today) { error.textContent = 'Choose a target release on or after today.'; return; }
    const records = readLiveIndex();
    const program = records.find(r => r.program && r.program.toLowerCase() === input.program?.toLowerCase())?.program || input.program || '';
    const id = crypto.randomUUID();
    const record = {id, name: input.name, owner: input.owner, program};
    const initial = {
      metadata: {case: input.name, portfolio: program, industry: '', projectStart: today, asOfDate: today, targetRelease: input.target, budget: 0, illustrative: false},
      modules: Object.fromEntries(Object.keys(window.STARTER.modules).map(key => [key, []]))
    };
    initial.modules.intake.push({title: input.name, type: program ? 'Program initiative' : 'Standalone project', sponsor: input.sponsor, value: input.objective, priority: '', status: 'Open', decision: ''});
    initial.modules.charter.push({item: 'Business objective', detail: input.objective, owner: input.owner, status: 'Draft'});
    try {
      localStorage.setItem(STORE + ':' + id, JSON.stringify(initial));
      try { localStorage.setItem(LIVE_INDEX, JSON.stringify([...records, record])); }
      catch (err) { localStorage.removeItem(STORE + ':' + id); throw err; }
    } catch { error.textContent = 'Browser storage is unavailable. The workspace could not be created.'; return; }
    switchWorkspace(id);
  });
}

function deliverySnapshot(workspace) {
  const m = workspace.modules;
  const open = list => list.filter(r => !isResolved(r.status));
  const dependencies = open(m.dependencies);
  const late = dependencies.filter(r => dateVal(r.forecast) > dateVal(r.neededBy) || /blocked|red|at risk|delayed/i.test(r.status));
  const milestones = m.roadmap.map(row => {
    if (isResolved(row.status)) return row;
    const linked = late.filter(dep => String(dep.deliverable || '').trim().toLowerCase() === String(row.dependency || '').trim().toLowerCase());
    if (!linked.length) return row;
    const forecast = [row.forecast, ...linked.map(dep => dep.forecast)].filter(date => Number.isFinite(dateVal(date))).sort().at(-1) || row.forecast;
    return {...row, forecast, status: 'At risk'};
  });
  const closed = m.closure.length > 0 && open(m.closure).length === 0;
  const report = [...m.reports].sort((a,b) => String(b.period).localeCompare(String(a.period)))[0];
  const blocked = [...late, ...open(m.raid), ...open(milestones)].some(r => bad(r.status));
  const health = closed ? 'Closed' : blocked || report?.overall === 'Red' ? 'Red' : late.length || report?.overall === 'Amber' ? 'Amber' : report?.overall || 'Not assessed';
  const forecast = milestones.map(r => r.forecast).filter(date => Number.isFinite(dateVal(date))).sort().at(-1) || workspace.metadata.targetRelease;
  const stage = closed ? 'Closed' : m.closure.length ? 'Closure' : m.release.length || m.operations.length ? 'Release & operations' : m.backlog.length || m.quality.length ? 'Delivery' : m.roadmap.length || m.financials.length ? 'Planning' : 'Intake';
  return {late, milestones, health, forecast, stage, closed, decisions: open(m.decisions), risks: open(m.raid)};
}
function liveOverview() {
  const snapshot = deliverySnapshot(state);
  const {late, milestones, health, forecast, stage, decisions, risks} = snapshot;
  const fin = budgetBreakdown();
  return `<div class="help"><strong>${esc(state.metadata.case)}</strong> · ${esc(stage)} · ${esc(activeWorkspace()?.owner)}</div>
  <div class="cards">
    <div class="metric"><label>Delivery health</label><div class="number small">${status(health)}</div></div>
    <div class="metric"><label>Milestones complete</label><div class="number">${milestones.filter(r=>isResolved(r.status)).length}/${milestones.length}</div></div>
    <div class="metric"><label>Forecast at completion</label><div class="number">${money(fin.eac)}</div><div class="foot">${money(fin.budget)} authorized</div></div>
    <div class="metric"><label>At-risk dependencies</label><div class="number">${late.length}</div><div class="foot">${risks.length} open RAID records</div></div>
  </div>
  <div class="grid2"><section class="panel"><div class="panel-head"><h2>Integrated delivery milestones</h2>${btn('Open roadmap','goto:roadmap')}</div>
  ${milestones.length ? timeline(milestones) : '<p>Add a milestone to build the delivery forecast.</p>'}
  <p class="hint">Target ${esc(state.metadata.targetRelease)} · Forecast through ${esc(forecast)}. To link a dependency, enter its deliverable name in the roadmap’s Dependency field. The dashboard shows the earliest forecast supported by that dependency.</p></section>
  <section class="panel"><div class="panel-head"><h2>Management attention</h2>${btn('Open decisions','goto:decisions')}</div>
  <div class="mini-list">${late.map(r => `<div class="mini-item"><strong>${esc(r.deliverable)}</strong><small>${esc(r.owner)} · Needed ${esc(r.neededBy)} · Forecast ${esc(r.forecast)} · Escalate ${esc(r.escalate)}</small><small>${esc(r.impact)}</small></div>`).join('')}
  ${decisions.map(r => `<div class="mini-item"><strong>${esc(r.question)}</strong><small>${esc(r.authority)} · Due ${esc(r.due)}</small></div>`).join('')}
  <p class="hint">${decisions.length} pending decisions · ${risks.length} open RAID records</p></div></section></div>
  <section class="panel"><h2>Manage delivery</h2><div class="toolbar">${['intake','charter','dependencies','raid','financials','quality','release','operations','reports','closure'].map(id => btn(esc(mMap[id].name),'goto:'+id)).join('')}</div></section>`;
}
function liveProgramOverview() {
  const active = activeWorkspace();
  if (!active?.program) return '<section class="panel"><h2>Program overview</h2><p>Create a program initiative to track delivery across related workspaces.</p></section>';
  const members = readLiveIndex().filter(r => r.program === active.program).map(r => ({...r, workspace: loadWorkspace(r.id)})).filter(r => r.workspace);
  return `<section class="panel"><h2>${esc(active.program)}</h2><p>${members.length} initiatives</p><div class="table-wrap"><table><thead><tr><th>Initiative</th><th>Owner</th><th>Stage</th><th>Forecast</th><th>Health</th><th>At-risk dependencies</th></tr></thead><tbody>${members.map(r => {
    const summary = deliverySnapshot(r.workspace);
    return `<tr><td>${btn(esc(r.workspace.metadata.case),'workspace:'+r.id)}</td><td>${esc(r.owner)}</td><td>${esc(summary.stage)}</td><td>${esc(summary.forecast)}</td><td>${status(summary.health)}</td><td>${summary.late.length}</td></tr>`;
  }).join('')}</tbody></table></div></section>`;
}
function liveReportDraft() {
  const {health, stage, forecast, late, decisions, risks} = deliverySnapshot(state);
  const fin = budgetBreakdown();
  return {period: state.metadata.asOfDate, overall: health === 'Not assessed' || health === 'Closed' ? '' : health,
    schedule: late.length || dateVal(forecast) > dateVal(state.metadata.targetRelease) ? 'Amber' : '',
    budget: fin.eac > fin.budget ? 'Red' : '',
    narrative: `${stage}. Forecast through ${forecast}. ${late.length} at-risk dependencies and ${risks.length} open RAID records. EAC ${money(fin.eac)} against ${money(fin.budget)} authorized.`,
    decisionNeeded: decisions.map(r => r.question).filter(Boolean).join('; ')};
}
