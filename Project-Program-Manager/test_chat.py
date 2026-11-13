"""Browser regression checks for offline contextual help and the existing dashboard."""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from functools import partial
import json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
Thread(target=server.serve_forever,daemon=True).start()
URL=f'http://127.0.0.1:{server.server_address[1]}/index.html'
log=[]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for w,h in [(1280,850),(740,940),(390,844),(320,650)]:
  page=browser.new_page(viewport={'width':w,'height':h})
  errors=[]
  page.on('pageerror',lambda e: errors.append(str(e)))
  page.set_content((ROOT/'index.html').read_text(),wait_until='load')
  assert page.locator('#chatLauncher').count()==1,(w, 'chat launcher not present',errors)
  assert page.locator('#main').inner_text().strip(),(w,'main empty')
  for mid in ['overview','audit','intake','business','charter','stakeholders','roadmap','backlog','iterations','dependencies','capacity','financials','raid','changes','decisions','quality','release','operations','vendors','compliance','reports','recovery','program','safelp','value','adoption','closure','academy','reference']:
   r=page.evaluate("(mid)=>{tab=mid;main();return document.getElementById('main').textContent.length}",mid)
   assert r>50,(w,mid,'render empty')
  page.evaluate("()=>{tab='overview';main()}")
  page.locator('#chatLauncher').click()
  assert page.locator('#chatPanel').is_visible(),(w,'not open')
  assert 'Executive Command Center' in page.locator('#chatContext').inner_text()
  page.locator('#chatQuestion').fill('Why is EAC below the approved budget?')
  page.locator('.chat-compose button').click()
  a=page.locator('.chat-msg-assistant').last.inner_text()
  assert '$1,065,000' in a and '$1,200,000' in a,(w,'finance answer missing',a)
  page.evaluate("()=>{tab='dependencies';main()}")
  assert 'Cross-Team Dependencies' in page.locator('#chatContext').inner_text(),(w,'context not updated')
  assert 'Which dependencies are late?' in page.locator('#chatSuggestions').inner_text(),(w,'chips not updated')
  page.locator('button[data-chat-ask="Which dependencies are late?"]').click()
  ans=page.locator('.chat-msg-assistant').last.inner_text()
  assert 'dependencies are currently not marked resolved' in ans,(w,'dependency summary broken',ans)
  assert page.locator('.chat-msg-user').count()==2,(w,'history not preserved')
  page.locator('#chatClose').click()
  assert not page.locator('#chatPanel').is_visible(),(w,'not closed')
  # open a parameter tooltip and transfer that exact field to the assistant
  page.evaluate("()=>{tab='dependencies';main();openEditor(0)}")
  page.locator('#modal .field-help-trigger').first.click()
  assert page.locator('#fieldHelpPopup').is_visible(),(w,'field help did not open')
  assert page.locator('[data-chat-field]').count()==1,(w,'chat CTA missing')
  expected=page.locator('[data-chat-field]').get_attribute('data-chat-field')
  page.locator('[data-chat-field]').click()
  assert page.locator('#chatPanel').is_visible(),(w,'field chat not open')
  assert page.locator('#fieldHelpPopup').count()==0,(w,'tooltip still open')
  assert 'Verify with:' in page.locator('.chat-msg-assistant').last.inner_text(),(w,'field help missing verification')
  # Calculations must read edited workspace data rather than hardcoded seed values.
  dynamic=page.evaluate('''()=>{let old=state.modules.financials[0].actual;state.modules.financials[0].actual=Number(old)+5000;let answer=chatAnswer('Explain EAC').text;state.modules.financials[0].actual=old;return answer}''')
  assert '$1,070,000' in dynamic,(w,'EAC did not track edited data',dynamic)
  # Program view uses program-specific contextual guidance.
  pguide=page.evaluate("()=>{mode='program';tab='overview';main();return chatGuide().purpose}")
  assert 'related projects' in pguide,(w,'program view not contextualized',pguide)
  page.evaluate("()=>{mode='project';tab='dependencies';main()}")
  # User-entered HTML is escaped; never executed or interpreted as markup.
  page.evaluate("()=>{chatAdd('user','<img src=x onerror=alert(1)>')}")
  assert page.locator('#chatLog img').count()==0,(w,'unsafe user HTML rendered')
  # directly verify scoped questions over every section: must not return generic fallback
  no_answer=[]
  for mid in [m['id'] for m in json.loads((ROOT/'modules.json').read_text())]:
   r=page.evaluate("mid=>{tab=mid;return CHAT_PAGES[mid].prompts.map(q=>({q,reply:chatAnswer(q).text}))}",mid)
   for z in r:
    if "I don't have a reliable offline answer" in z['reply']:
     no_answer.append((mid,z['q']))
  log.append({'width':w,'sections':29,'chatMessages':page.locator('.chat-msg').count(),'unansweredPrompts':no_answer,'errors':errors})
  page.screenshot(path=str(ROOT/f'chat-preview-{w}.png'),full_page=False)
  page.close()
 assert not any(l['errors'] for l in log), log
 browser.close()
server.shutdown()
print(json.dumps(log,indent=2))
