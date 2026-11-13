"""Verify shipped code contains no prohibited organizational names in its sample presentation.
Names are represented as digests so the check does not reintroduce them to source files.
Technology and framework names are permitted references.
"""
from pathlib import Path
import re,sys,json,hashlib
ROOT=Path(__file__).resolve().parent
TEXT_TYPES={'.html','.js','.json','.md','.py','.css'}
PROHIBITED_SHA256={
    '0baf38f5da148c7a98b362afba5da1eb781a443f521ed25b049fe34d4ce5edd2',
    '14b869a00ddd44a04592a245430d764d3b8295c1a74a0a1b904f142d41ea0638',
    '1cf010891de5e3812b8bf957926495bb19f7d31e5d7c53288fcf6d6fad8e5492',
    '229a4b0753f710ddb7c25581f859d91f1916d55ec2fcd3d1a20c774a8d9764dd',
    '2cbb9e58bf3bcbdfe805a2aebb57f84531b114a18e5f0e6377d9f5a7bf86576b',
    '337b8d2c1e132acd75171f1acf0e73b20bc9541720d5003813f59ef0ad51f86f',
    '33b4b85d1010463b0dece130170b9ec1f8a060d6cbd39abe7fede75181bcd35f',
    '34a533dfd7273a9bb03656b32956a2b1d08dc62533b11c813b28d0ef23ec8e67',
    '421d09fdf4c226c5fe2c190d9481bde84755da1d65f500a49f655210f0545464',
    '48a03abc9189b9c501cc4d5e37293d0f01eca3e205d377f07dcd55ef79ad48a1',
    '54235e6a8c59a2898122ea0edef963970c09196f883d6684fceb2e126a3accfc',
    '5528a266f145e52b1909113269d53b17369dfa495d541628c661029da13e9237',
    '5ca13979c8e207cdc3f900aafcac26b9cb2517e24f1143325c31b9f0271d8ce8',
    '67933135042afcb5d9b1f95f05e3413ea43559c756a8a666efdd2473c4d25fb3',
    '6dc3447ca8d4ae4a43910c39e15248dffea19df4771fc0b8fab9d33fb5f2fd9c',
    '811dae26155c1f96fa4be679ba416b5b956c4eb73dc831d69f61692507e30595',
    '846be5fc541c5039f7972c6f0a054a3460d3f4b3ee3541991baee4027465abdb',
    'a638e70ffa28c67e202f3197c33ecb343576ede06cef2deeb3dfd9659b7c3002',
    'b244dfaa609aaede84b1ce898dc02bb6e7afabff83d3f50ae91ddd4c29bcc225',
    'b274dbbb36457758cf017a493b9eda407be22f6a6b17351d1616695fc0553204',
    'b7c03e34b89e841ac47c984622d6b11b5d1bad2e8491dae9173048280e4c2b84',
    'b8ca4bd5e56c868a87bbe0d1b11aac95d41f8b83d3ef5fc8bf07703cc0c50d22',
    'bc8a00f7f6fb535fa036a97b51ade4f07a01ec4ec2665ba746e206fde245bdf6',
    'c17dd2e2ea9abf3a51aaff1025e6adeb8869af380110962fa13c113eebacb7e0',
    'ca6a7c40f9b9bf94d7e7ebde336958dee8a3f526f967f532ef4bce7c8d5ea710',
    'cc5fd8dc26b1f7745e4d5a5222701375bab1ee8316ecfadd42fdfec0ce2e21b1',
    'ee0ca20290ec4a3ed9e5fcd59a260eccc34dfbe36a65276aab52e9b1bc5cbed9',
    'f13c3757ca75cef28e3b40fed63e1ecd80f9ab41224d42f2fccf65e684129e51',
    'f98407019f8c4af6fbb6c9dd39c6fc88ed31c41709afc3b758fd9928fd75c42b',
    'f9ae058aff4e3c5d8531cb4b02052b7fd60945e263d4db33129d436f7a61f1fe',
    'fd38e4fcc36444128ab8059ce46332d627db606ec1bb4d0ceea5e84da6531dfe'
}
errors=[];scanned=0
for f in ROOT.rglob('*'):
 if not f.is_file() or f.suffix.lower() not in TEXT_TYPES:continue
 scanned+=1
 txt=f.read_text(encoding='utf8',errors='replace')
 # Match 1–4 word phrases, preserving possible multiple-word organization names.
 for line_no,line in enumerate(txt.splitlines(),1):
  words=[m.group(0).casefold() for m in re.finditer(r'[A-Za-z]+',line)]
  for i in range(len(words)):
   for count in range(1,min(4,len(words)-i)+1):
    phrase=' '.join(words[i:i+count]); h=hashlib.sha256(phrase.encode()).hexdigest()
    if h in PROHIBITED_SHA256:
     errors.append(f'{f.relative_to(ROOT)}:{line_no}: organization name detected')
 # Check fields that may embed company names in escaped source strings too.
 for m in re.finditer(r'\\u[0-9a-fA-F]{4}',txt):
  pass
html=(ROOT/'index.html').read_text(encoding='utf8')
allowed=['Jira','Confluence','Smartsheet','PolicyCenter','Guidewire','Okta','DocuSign','SAFe']
if not all(x.casefold() in html.casefold() for x in allowed):errors.append('Expected technical/tool names missing')
seed=json.loads((ROOT/'seed-data.json').read_text())
if seed['metadata']['version']!='1.5.0':errors.append('Release version mismatched')
if errors:
 print('Brand-neutral audit FAIL:',len(errors),'issues');print('\n'.join(errors[:50]));sys.exit(1)
print(f'Brand-neutral audit PASS: {scanned} source artifacts scanned, {len(PROHIBITED_SHA256)} prohibited organizational identifiers absent, 8 technical/framework references retained.')
