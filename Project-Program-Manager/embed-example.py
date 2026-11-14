"""Refresh the offline worked-example payload from its CSV sources."""
import csv
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
data = {}
for name in ('projects', 'milestones', 'controls'):
    with (root / 'examples' / 'personal-auto' / f'{name}.csv').open(newline='', encoding='utf-8') as source:
        data[name] = list(csv.DictReader(source))
data['registers'] = json.loads((root / 'examples' / 'personal-auto' / 'delivery-registers.json').read_text())
templates = json.loads((root / 'examples' / 'project-templates.json').read_text())
payloads = {'PERSONAL_AUTO': data, 'PROJECT_TEMPLATES': templates}
path = root / 'live-workspace.js'
updated = path.read_text()
for name, source in payloads.items():
    payload = json.dumps(source, ensure_ascii=False).replace('</', '<\\/')
    updated, count = re.subn(rf'(?m)^const {name} = .*;$', lambda _: f'const {name} = {payload};', updated)
    if count != 1:
        raise SystemExit(f'Expected one {name} payload in {path.name}')
path.write_text(updated)
