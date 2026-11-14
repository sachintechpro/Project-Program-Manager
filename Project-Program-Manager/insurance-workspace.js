const field = id => document.getElementById(id);
const value = id => field(id).value;
let opened = null;
let previewedCsv = null;

async function call(path, body) {
  try {
    const response = await fetch('/api/' + value('mode') + '/' + path, body === undefined ? {} : {
      method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body)
    });
    const result = await response.json();
    field('http').textContent = 'HTTP ' + response.status + ' · ' + response.statusText;
    field('result').textContent = JSON.stringify(result, null, 2);
    return response.ok ? result : null;
  } catch {
    field('http').textContent = 'API unavailable';
    field('result').textContent = 'Open this page through the ValueStream HQ server.';
    return null;
  }
}

function renderGuide(result) {
  if (!result) return;
  opened = result.project || null;
  field('guide').replaceChildren(...result.guide.map(row => {
    const item = document.createElement('li');
    item.textContent = row.kind + ' · ' + (row.completed ? 'Complete' : 'Pending') + ' · ' + row.detail;
    return item;
  }));
  field('guide-note').textContent = result.saved ? 'Shared project guide' : 'Simulation results reset after each request.';
  const next = result.guide.find(row => !row.completed);
  if (next) field('phase').value = next.phase;
}

const projectPath = () => 'projects/' + encodeURIComponent(value('project'));
field('mode').addEventListener('change', () => {
  const live = value('mode') === 'live';
  field('lab-auth').hidden = live;
  field('okta-auth').hidden = field('live-tools').hidden = !live;
  opened = null;
  previewedCsv = null;
  field('apply').disabled = true;
  field('guide').replaceChildren();
  field('guide-note').textContent = 'Open a project to see its milestones from intake through transition.';
});
if (new URLSearchParams(location.search).get('mode') === 'live') {
  field('mode').value = 'live';
  field('mode').dispatchEvent(new Event('change'));
}

const actions = {
  challenge: async () => {
    const result = await call('session', {action:'sign-in', user:value('persona')});
    field('challenge-note').textContent = result ? 'Simulation code: ' + result.code : '';
  },
  verify: () => call('session', {action:'verify', code:value('code')}),
  logout: () => call('session', {action:'logout'}),
  status: () => call('session'),
  projects: () => call('projects'),
  audit: () => call('audit'),
  read: async () => renderGuide(await call(projectPath())),
  create: () => call('projects', {program_id:value('program'), name:value('name')}),
  rename: async () => {
    if (!opened || opened.id !== value('project')) {
      field('http').textContent = 'Open the project before renaming it.';
      return;
    }
    renderGuide(await call(projectPath(), {name:value('name'), version:opened.version}));
  },
  advance: async () => renderGuide(await call(projectPath() + '/guide/' + encodeURIComponent(value('phase')), {detail:value('detail')})),
  seed: () => call('seed', {}),
  'create-program': () => call('programs', {name:value('name'), objective:value('objective')}),
  assign: () => call('members', {subject:value('subject'), role:value('role'), scope:value('scope')}),
  preview: async () => {
    previewedCsv = null;
    field('apply').disabled = true;
    const file = field('csv').files[0];
    if (!file || file.size > 100000) {
      field('http').textContent = 'Select a project.csv file under 100 KB.';
      return;
    }
    const csv = await file.text();
    if (await call('csv', {csv, apply:false})) {
      previewedCsv = csv;
      field('apply').disabled = false;
    }
  },
  apply: () => {
    if (previewedCsv === null) return;
    const csv = previewedCsv;
    previewedCsv = null;
    field('apply').disabled = true;
    return call('csv', {csv, apply:true});
  }
};
for (const [id, action] of Object.entries(actions)) field(id).addEventListener('click', action);
