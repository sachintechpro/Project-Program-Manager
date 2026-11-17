import re, os
from pathlib import Path
from fastapi.testclient import TestClient
from playwright.sync_api import sync_playwright
os.environ['DEMO_MODE']='true'; os.environ['SECRET_KEY']='raid-ui'; os.environ['DATABASE_URL']='sqlite:///./raid_ui.db'
from app.main import app
BASE=Path(__file__).resolve().parent.parent
HTML=(BASE/'app/static/index.html').read_text()
HTML=re.sub(r'<script src="/assets/[^"]+"></script>','',HTML).replace('<link rel="stylesheet" href="/assets/style.css">','')
with TestClient(app) as c, sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    p=b.new_page(viewport={'width':1365,'height':900}); errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
    def bridge(source,url,opts=None):
        opts=opts or {}; r=c.request((opts.get('method') or 'GET').upper(),url,content=opts.get('body'),headers=opts.get('headers') or {})
        try: body=r.json()
        except: body={}
        return {'status':r.status_code,'body':body}
    p.expose_binding('__apiBridge',bridge);p.set_content(HTML,wait_until='domcontentloaded')
    p.evaluate("window.EventSource=class{close(){}};window.fetch=async(u,o={})=>{let x=await window.__apiBridge(String(u),{method:o.method||'GET',body:o.body||null,headers:o.headers||{}});return {ok:x.status>=200&&x.status<300,status:x.status,json:async()=>x.body}};")
    p.add_style_tag(content=re.sub(r'^@import[^;]+;','',(BASE/'app/static/style.css').read_text()))
    for f in ('qa_bench.js','map_ui.js','app.js'): p.add_script_tag(content=(BASE/'app/static'/f).read_text())
    p.wait_for_selector('#login-personas button');p.locator('#login-personas button[data-role="program_manager"]').click();p.wait_for_selector('#shell:not(.hidden)')
    p.locator('button[data-page="raid"]').click();p.wait_for_function("document.querySelector('#page-title').textContent==='RAID register'")
    assert p.locator('[data-raid-record]').count()>0
    assert p.locator('#register-form-panel.hidden').count()==1
    assert p.locator('.raid-badge.raid-risk,.raid-badge.raid-issue,.raid-badge.raid-dependency').count()>0
    assert p.locator('.raid-tip[title]').count()>=6
    p.locator('#raid-type-filter').select_option('risk');p.wait_for_timeout(100)
    vals=p.locator('[data-raid-record]:not(.hidden)').evaluate_all("els=>els.map(e=>e.dataset.type)"); assert all(x=='risk' for x in vals)
    p.locator('#raid-search').fill('no-match-xyz');p.wait_for_timeout(100);assert p.locator('[data-raid-record]:not(.hidden)').count()==0
    p.locator('#raid-search').fill('');p.locator('#raid-type-filter').select_option('')
    p.locator('[data-register-new="raid"]').click();p.wait_for_selector('#register-form-panel:not(.hidden)')
    assert p.locator('#register-form-panel label.field').count()>=8
    p.screenshot(path=str(BASE/'qa_evidence/raid_ui_desktop.png'),full_page=True)
    print('RAID UI PASS',p.locator('[data-raid-record]').count(),'records,',p.locator('.raid-tip[title]').count(),'tooltips,',len(errors),'JS errors')
    if errors: raise SystemExit(2)
