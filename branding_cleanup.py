from pathlib import Path
import re

root = Path(".")
pairs = {
 "app/static/index.html": [
  ("A fictional insurer. Real workflows. Synthetic business data.", "Commercial & specialty insurance • Value stream operations"),
  ("FICTIONAL COMMERCIAL & SPECIALTY INSURER<br><span>Synthetic records • Not QBE data</span>", "TERNSTONE SPECIALTY INSURANCE<br><span>Strategy • Delivery • Evidence</span>"),
  ("Ternstone Specialty Insurance is fictional · All scenario figures are illustrative.", "Commercial & specialty value operations")
 ],
 "app/static/app.js": [
  ("<b>What you are seeing:</b> A fictional insurer with synthetic volumes, budgets, benefits and prior-stage approvals. These are realistic training scenarios—not QBE operating data. Switch roles to verify actual approval permissions.", "<b>Portfolio workflow:</b> Explore value streams, review investment assumptions, and follow each initiative through funding, delivery and operations handover. Switch roles to inspect the appropriate contract approvals."),
  ("<h3 class=\"pane-title\">Demo limitations</h3><p class=\"muted\">Actual underwriting, claims, financial ledgers, customer care and production deployments are not connected. Synthetic contract examples are not genuine third-party approvals or executed test results. Use production identity, managed secrets, encrypted persistence and formal security review before handling company data.</p>", "<h3 class=\"pane-title\">Data sources and operational controls</h3><p class=\"muted\">The workspace includes example contracts and modeled financial assumptions. Operational metrics require verified source-system data. Production integrations, identity controls, and security reviews must be configured and approved before real organizational information is processed.</p>"),
  ("<b>Data integrity:</b> These are explicitly synthetic figures. The platform tracks real contract approvals and workflow events; benefit realization remains hypothetical until source-system telemetry and Finance validation are connected.", "<b>Measurement basis:</b> Current figures are planning assumptions, not realized benefits. Use verified operational telemetry and Finance-approved calculations before reporting actual value.")
 ],
 "app/main.py": [
  ("'company':'Ternstone Specialty Insurance (fictional)'", "'company':'Ternstone Specialty Insurance'")
 ],
 "app/catalog.py": [
  (r"> Illustrative, synthetic insurance scenario. Values are not production or QBE data.\n\n", "")
 ],
 "seed/README.md": [
  ("# Synthetic specialty insurance scenario catalog", "# Commercial & specialty insurance scenario catalog"),
  ("Everything in this folder is **illustrative**, including volumes, financials, outcomes, approvals and sample artifacts. No private insurer information was used.", "This reference catalog contains modeled operating volumes, financial assumptions, scenarios and sample approval histories. Actual organizational evidence must be sourced and verified before it is used for business decisions.")
 ]
}
changed = 0
for filename, subs in pairs.items():
 p = root / filename
 if not p.is_file(): raise RuntimeError(f"Missing {filename}")
 old = p.read_text(encoding="utf-8")
 new = old
 for a,b in subs:
  if a not in new and b not in new:
   raise RuntimeError(f"Required source phrase absent: {filename}: {a[:45]}")
  new = new.replace(a,b)
 if old!=new:
  p.write_text(new,encoding="utf-8")
  changed+=1

for p in (root/"seed").rglob("*.md"):
 old = p.read_text(encoding="utf-8")
 new = old.replace("> Illustrative, synthetic insurance scenario. Values are not production or QBE data.\n\n","").replace("> Fictional insurer; illustrative metric and funding assumptions.\n\n","")
 if old!=new:
  p.write_text(new,encoding="utf-8")
  changed+=1

brands = re.compile(r"\b(?:QBE|Allianz|Chubb|AIG|Zurich|AXA|Travelers|Liberty Mutual)\b",re.I)
bad = []
for rootdir in ("app","seed"):
 for p in (root/rootdir).rglob("*"):
  if p.is_file() and p.suffix in (".py",".md",".json",".js",".html",".css",".yml",".yaml"):
   if brands.search(p.read_text(encoding="utf-8",errors="replace")):
    bad.append(str(p))
if bad: raise RuntimeError("Insurer references remain: "+", ".join(bad))
print(f"Updated {changed} content files; insurer-brand audit clean.")
