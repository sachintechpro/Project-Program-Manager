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
payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
for filename in ('live-workspace.js', 'index.html'):
    path = root / filename
    original = path.read_text()
    updated, count = re.subn(r'(?m)^const PERSONAL_AUTO = .*;$', lambda _: f'const PERSONAL_AUTO = {payload};', original)
    if count != 1:
        raise SystemExit(f'Expected one example payload in {filename}')
    path.write_text(updated)
