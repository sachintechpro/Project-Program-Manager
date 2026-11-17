# Ternstone ValueOps — Final QA Execution and Go/No-Go Record

**Release:** TERNSTONE-2026-11-17-QA-FINAL-R1

**Environment:** isolated Linux test container; FastAPI TestClient + Chromium 1365px/390px + local ASGI HTTPX

**Run completed:** 2026-11-17T19:36:55+00:00

**Executed / status:** 77 pass, 0 fail, 5 blocked, 6 not run, 88 recorded cases

**Summed measured execution duration:** 16.87 sec (pytest 6.86s; browser 7.09s; local load 2.92s).

## Decision

**Demonstration: GO candidate, subject to independent QA Lead and Release Manager sign-offs in the application.**

**Actual insurer production: NO-GO.** Real provider integrations, persistent database, SSO/MFA, security review, DR/backup verification, production load and availability evidence are missing.

## Scope and evidence

Risk-based smoke, functional, integration-contract simulation, RBAC/CSRF, complete eight-gate delivery, RACI/RAID, all six mapped value streams, usability/responsive layouts, bounded API load, and honest evidence segregation.

| Area | Passed | Failed | Blocked | Not run |
|---|---:|---:|---:|---:|
| Role-aware contextual help | 4 | 0 | 0 | 0 |
| RACI / RAID governance | 3 | 0 | 0 | 0 |
| QA evidence and Go-No-Go | 2 | 0 | 0 | 0 |
| RACI roles and display | 2 | 0 | 0 | 0 |
| Insurance data and role controls | 4 | 0 | 0 | 0 |
| Role-based access and security | 4 | 0 | 0 | 0 |
| Value stream mapping | 6 | 0 | 0 | 0 |
| Value map review and graphics | 4 | 0 | 0 | 0 |
| Lifecycle, contracts and approvals | 5 | 0 | 0 | 0 |
| Browser UX / Accessibility | 38 | 0 | 0 | 0 |
| Local API performance / reliability | 3 | 0 | 0 | 0 |
| Visual exploratory inspection | 2 | 0 | 0 | 0 |
| External provider integrations | 0 | 0 | 5 | 0 |
| Production readiness gaps | 0 | 0 | 0 | 6 |

## Measured local performance and comparison to explicitly scoped SLOs

| Test | p95 (ms) | Proposed local target | Requests | Concurrent readers | Errors |
|---|---:|---:|---:|---:|---:|
| Local API load · 8 concurrent readers | 79.03 | 900 | 320 | 8 | 0 |
| Local API burst · 16 concurrent readers | 282.92 | 1500 | 240 | 16 | 0 |
| Local health endurance sample · 500 queries | 4.78 | 500 | 500 | 8 | 0 |

The API targets above are project-specific, not insurance industry medians. Google Core Web Vitals recommends p75 LCP ≤2.5 seconds, INP ≤200 milliseconds and CLS ≤0.1; these browser field metrics have **not** been measured for this public site. A 99.9% availability goal is only a proposed target and was **not** verified.

## Reviewers and decision rights

QA Lead: can issue demo GO/NO-GO/Request Evidence for this report. Release Manager: separate, independently recorded demo decision. Program Manager and Platform Admin cannot sign for either. All decisions are audited, tied to report ID, and never grant production authorization.

## Known residual risks

- Live external provider authentication, writes, readback, and failure handling remain unverified.
- Free-tier SQLite storage is ephemeral; restart/restore/reliability are not enterprise-grade.
- No real insurer transaction data; business KPIs and approvals are modeled examples.
- Real browser field Web Vitals, multi-day availability and capacity stress tests are not measured.
- No independent penetration test, SSO/MFA or multi-tenant segregation certification.
- No verified end-to-end live Render browser test due automated browser network restrictions.

## Source evidence

- `qa_evidence/pytest_junit.xml` — backend cases
- `qa_evidence/browser_results.json` — browser journeys
- `qa_evidence/qa_bench_desktop.webp` / `qa_bench_mobile.webp` — UI captures
- `qa_evidence/performance_results.json` — local load metrics
- `qa_evidence/test_results.csv` — test case matrix
- `qa_evidence/performance_metrics.csv` — target comparisons

Published general references: https://web.dev/articles/vitals ; https://sre.google/sre-book/service-level-objectives/ ; https://owasp.org/projects/api-security-project/