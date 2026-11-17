# Ternstone ValueOps — Render deployment branch

This isolated branch holds the Ternstone ValueOps source-and-seed deployment archive. It does not alter other Project-Program-Manager branches or applications.

Source package: `ternstone-runtime.tar.xz` (contains `app/`, `seed/`, `requirements.txt`).

Build: `tar -xJf ternstone-runtime.tar.xz && pip install -r requirements.txt`

Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

Environment: `DEMO_MODE=true`, `SECURE_COOKIES=true`. The public demonstration uses synthetic data; changes stored in SQLite on free Render instances may reset on restart. Live connectors are not configured. Production use requires durable Postgres, SSO, security review and protected role provisioning.

Full editable project source is also supplied separately as the Ternstone ValueOps source ZIP in ChatGPT.
