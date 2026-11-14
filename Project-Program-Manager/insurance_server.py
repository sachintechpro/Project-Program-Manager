"""Server-side workspace and isolated insurance stakeholder lab."""
import csv
import time
import io
import os
import secrets
import sqlite3
import zipfile
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urlparse

from authlib.integrations.flask_client import OAuth
from flask import Flask, abort, jsonify, redirect, request, send_file, session, url_for
from werkzeug.exceptions import HTTPException

ROOT = Path(__file__).resolve().parent
ROLES = {'admin', 'portfolio', 'program', 'project', 'underwriting', 'billing', 'claims', 'qa', 'auditor'}
LAB = {
    'avery.program': ('program', 'auto'), 'morgan.pm': ('project', 'policy'),
    'jordan.underwriting': ('underwriting', 'policy'), 'casey.billing': ('billing', 'billing'),
    'riley.claims': ('claims', 'claims'), 'taylor.qa': ('qa', 'auto'),
    'sam.audit': ('auditor', '*'), 'devon.admin': ('admin', '*'),
    'blair.portfolio': ('portfolio', '*'),
}
MFA_ACR = 'urn:okta:loa:2fa:any'


def create_app(config=None):
    app = Flask(__name__, static_folder=None)
    app.config.update(
        DATABASE=os.environ.get('VSHQ_DATABASE', 'data/workspace.sqlite3'),
        SECRET_KEY=os.environ.get('VSHQ_SESSION_SECRET') or secrets.token_hex(32),
        SESSION_COOKIE_SECURE=True, SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',
        PERMANENT_SESSION_LIFETIME=1800, MAX_CONTENT_LENGTH=128_000,
        OKTA_ISSUER=os.environ.get('OKTA_ISSUER', '').rstrip('/'),
        OKTA_CLIENT_ID=os.environ.get('OKTA_CLIENT_ID', ''),
        OKTA_CLIENT_SECRET=os.environ.get('OKTA_CLIENT_SECRET', ''),
        OKTA_CALLBACK_URL=os.environ.get('OKTA_CALLBACK_URL', ''),
        FIRST_ADMIN_SUB=os.environ.get('VSHQ_FIRST_ADMIN_SUB', ''),
    )
    app.config.update(config or {})
    issuer = app.config['OKTA_ISSUER']
    okta = None
    if any(app.config[k] for k in ('OKTA_ISSUER', 'OKTA_CLIENT_ID', 'OKTA_CLIENT_SECRET', 'OKTA_CALLBACK_URL')):
        if (urlparse(issuer).scheme != 'https' or urlparse(app.config['OKTA_CALLBACK_URL']).scheme != 'https'
                or not all(app.config[k] for k in ('OKTA_CLIENT_ID', 'OKTA_CLIENT_SECRET', 'OKTA_CALLBACK_URL'))
                or not (os.environ.get('VSHQ_SESSION_SECRET') or (config or {}).get('SECRET_KEY'))):
            raise RuntimeError('Complete the Okta HTTPS and session secret configuration.')
        okta = OAuth(app).register(
            'okta', server_metadata_url=f'{issuer}/.well-known/openid-configuration',
            client_id=app.config['OKTA_CLIENT_ID'], client_secret=app.config['OKTA_CLIENT_SECRET'],
            client_kwargs={'scope': 'openid', 'code_challenge_method': 'S256'},
        )

    @contextmanager
    def database(lab=False):
        path = Path(app.config['DATABASE'])
        if lab:
            path = Path(':memory:')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(path, timeout=10)
        connection.row_factory = sqlite3.Row
        connection.execute('PRAGMA foreign_keys=ON')
        try:
            with connection:
                if lab:
                    initialize(connection)
                    seed(connection)
                yield connection
        finally:
            connection.close()

    with database() as connection:
        initialize(connection)
        if app.config['FIRST_ADMIN_SUB']:
            connection.execute('INSERT OR IGNORE INTO members VALUES (?, ?, ?)',
                               (app.config['FIRST_ADMIN_SUB'], 'admin', '*'))

    @app.before_request
    def protect_mutation():
        if request.method == 'POST' and not request.is_json:
            abort(415, 'Send an application/json request.')

    @app.after_request
    def protect_response(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        if request.path.startswith(('/api/', '/okta/')):
            response.headers['Cache-Control'] = 'no-store'
        return response

    @app.errorhandler(HTTPException)
    def report(error):
        return jsonify(error=error.description), error.code

    @app.get('/')
    def home():
        return send_file(ROOT / 'index.html')

    @app.get('/<any("qa-bench.html","insurance-workspace.html","insurance-workspace.js"):asset>')
    def asset_file(asset):
        return send_file(ROOT / asset)

    @app.get('/okta/login')
    def login():
        if not okta:
            abort(503, 'An Okta tenant has not been configured.')
        session.clear()
        return okta.authorize_redirect(app.config['OKTA_CALLBACK_URL'], acr_values=MFA_ACR)

    @app.get('/okta/callback')
    def callback():
        if not okta:
            abort(503)
        try:
            token = okta.authorize_access_token()
        except Exception:
            app.logger.warning('Okta callback validation failed')
            abort(401, 'Okta sign-in could not be verified.')
        claims = token.get('userinfo') or {}
        if claims.get('acr') != MFA_ACR or not claims.get('sub'):
            abort(403, 'Okta did not confirm the required MFA assurance.')
        session.clear()
        session.permanent = True
        session['sub'] = claims['sub']
        return redirect(url_for('asset_file', asset='insurance-workspace.html', mode='live'))

    @app.post('/api/<mode>/session')
    def set_session(mode):
        body = payload()
        if mode == 'live':
            if body.get('action') == 'logout':
                session.pop('sub', None)
                return jsonify(status='signed out')
            abort(400, 'Use Okta sign-in.')
        if mode != 'lab':
            abort(404)
        action = body.get('action')
        if action == 'logout':
            for key in ('lab', 'lab_pending', 'lab_code', 'lab_expiry'):
                session.pop(key, None)
            return jsonify(status='signed out')
        if action == 'sign-in':
            session.pop('lab', None)
            session.pop('lab_pending', None)
            session.pop('lab_code', None)
            if not isinstance(body.get('user'), str) or body['user'] not in LAB:
                abort(400, 'Select a fictional stakeholder.')
            session.permanent = True
            session['lab_pending'] = body['user']
            session['lab_expiry'] = int(time.time()) + 120
            session['lab_code'] = f'{secrets.randbelow(1_000_000):06d}'
            return jsonify(status='simulation challenge', code=session['lab_code']), 202
        if action == 'verify':
            code = session.pop('lab_code', None)
            user = session.pop('lab_pending', None)
            expiry = session.pop('lab_expiry', 0)
            if not code or not user or expiry < time.time() or not secrets.compare_digest(code, str(body.get('code', ''))):
                abort(401, 'Challenge expired or invalid.')
            session['lab'] = user
            return jsonify(status='verified', role=LAB[user][0])
        abort(400, 'Unknown session action.')

    def actor(connection, mode):
        if mode == 'lab':
            user = session.get('lab')
            if user not in LAB:
                abort(401, 'Complete the simulation challenge.')
            role, scope = LAB[user]
        elif mode == 'live':
            user = session.get('sub')
            if not user:
                abort(401, 'Sign in through Okta.')
            member = connection.execute('SELECT role, scope FROM members WHERE subject=?', (user,)).fetchone()
            if not member:
                abort(403, 'Workspace membership is required.')
            role, scope = member
        else:
            abort(404)
        return user, role, scope

    @app.get('/api/<mode>/session')
    def status(mode):
        with database(mode == 'lab') as connection:
            _, role, scope = actor(connection, mode)
            return jsonify(role=role, scope=scope)

    @app.post('/api/live/seed')
    def load_example():
        with database() as connection:
            user, role, _ = actor(connection, 'live')
            if role != 'admin':
                abort(403)
            seed(connection)
            audit(connection, user, 'load example', 'auto')
            return jsonify(status='example loaded')

    @app.post('/api/live/programs')
    def create_program():
        with database() as connection:
            user, role, _ = actor(connection, 'live')
            if role not in {'admin', 'portfolio'}:
                abort(403)
            body = payload()
            program_id = secrets.token_hex(8)
            name = required_text(body, 'name')
            objective = required_text(body, 'objective')
            connection.execute('INSERT INTO programs VALUES (?, ?, ?)', (program_id, name, objective))
            audit(connection, user, 'create program', program_id, after=name)
            return jsonify(id=program_id, name=name), 201

    @app.route('/api/<mode>/projects', methods=['GET', 'POST'])
    def projects(mode):
        with database(mode == 'lab') as connection:
            user, role, scope = actor(connection, mode)
            if request.method == 'GET':
                rows = visible_projects(connection, scope)
                visible_ids = {row['id'] for row in rows}
                dependencies = [dict(row) for row in connection.execute('SELECT * FROM dependencies ORDER BY id')
                                if row['from_project'] in visible_ids and row['to_project'] in visible_ids]
                return jsonify(programs=visible_programs(connection, scope), projects=rows, dependencies=dependencies)
            body = payload()
            program = required_text({'program_id': body.get('program_id', 'auto')}, 'program_id')
            if role not in {'admin', 'program', 'project'} or (scope != '*' and scope != program):
                abort(403, 'Project creation requires an assignment to this program.')
            if not connection.execute('SELECT 1 FROM programs WHERE id=?', (program,)).fetchone():
                abort(404)
            name = required_text(body, 'name')
            project_id = secrets.token_hex(8)
            connection.execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?)',
                               (project_id, program, name, 'project', 0, 'Intake', 1))
            connection.executemany('INSERT INTO register VALUES (?, ?, ?, ?, ?)',
                                   [(project_id, i, kind, detail, 0) for i, (kind, detail) in enumerate(GUIDE, 1)])
            audit(connection, user, 'create project', project_id)
            return jsonify(id=project_id, name=name, version=1, saved=mode == 'live'), 201

    @app.route('/api/<mode>/projects/<project_id>', methods=['GET', 'POST'])
    def project(mode, project_id):
        with database(mode == 'lab') as connection:
            user, role, scope = actor(connection, mode)
            project = next((p for p in visible_projects(connection, scope) if p['id'] == project_id), None)
            if not project:
                abort(404)
            if request.method == 'POST':
                if role not in {'admin', 'program', 'project'}:
                    abort(403, 'Only assigned managers can rename projects.')
                body = payload()
                name = required_text(body, 'name')
                update_name(connection, user, project, name, body.get('version'))
                project['name'] = name
                project['version'] += 1
            return jsonify(project=project, guide=records(connection, project_id), saved=mode == 'live')

    @app.post('/api/<mode>/projects/<project_id>/guide/<int:phase>')
    def complete_step(mode, project_id, phase):
        with database(mode == 'lab') as connection:
            user, role, scope = actor(connection, mode)
            project = next((p for p in visible_projects(connection, scope) if p['id'] == project_id), None)
            if not project:
                abort(404)
            if role not in {'admin', 'program', 'project', project['role']} and not (role == 'qa' and phase == 5):
                abort(403)
            if phase not in range(1, 7):
                abort(404)
            detail = required_text(payload(), 'detail')
            connection.execute('BEGIN IMMEDIATE')
            if connection.execute('SELECT 1 FROM register WHERE project_id=? AND phase<? AND completed=0',
                                  (project_id, phase)).fetchone():
                abort(409, 'Complete the earlier stages first.')
            changed = connection.execute('UPDATE register SET detail=?, completed=1 WHERE project_id=? AND phase=? AND completed=0',
                                         (detail, project_id, phase)).rowcount
            if not changed:
                abort(409, 'This stage has already been completed.')
            connection.execute('UPDATE projects SET status=?, version=version+1 WHERE id=?',
                               (GUIDE[phase][0] if phase < len(GUIDE) else 'Closed', project_id))
            audit(connection, user, f'complete stage {phase}', project_id, after=detail)
            return jsonify(guide=records(connection, project_id), saved=mode == 'live')

    @app.get('/api/<mode>/audit')
    def list_audit(mode):
        with database(mode == 'lab') as connection:
            _, role, _ = actor(connection, mode)
            if role not in {'admin', 'auditor'}:
                abort(403)
            return jsonify(events=[dict(row) for row in connection.execute(
                'SELECT * FROM audit ORDER BY id DESC LIMIT 100')])

    @app.post('/api/live/members')
    def membership():
        with database() as connection:
            user, role, _ = actor(connection, 'live')
            if role != 'admin':
                abort(403)
            body = payload()
            subject, new_role, scope = (required_text(body, key) for key in ('subject', 'role', 'scope'))
            if new_role not in ROLES or (new_role in {'admin', 'auditor', 'portfolio'}) != (scope == '*'):
                abort(400, 'Use a valid role and scope.')
            if subject == user:
                abort(400, 'Another admin must change your role.')
            if scope != '*' and not (connection.execute('SELECT 1 FROM programs WHERE id=?', (scope,)).fetchone()
                                      or connection.execute('SELECT 1 FROM projects WHERE id=?', (scope,)).fetchone()):
                abort(400, 'The scope must be an existing program or project ID.')
            connection.execute('INSERT OR REPLACE INTO members VALUES (?, ?, ?)', (subject, new_role, scope))
            audit(connection, user, 'assign membership', subject, after=f'{new_role}:{scope}')
            return jsonify(status='assigned')

    @app.get('/api/live/csv')
    def export_csv():
        with database() as connection:
            _, role, scope = actor(connection, 'live')
            if role not in {'admin', 'program', 'project', 'portfolio', 'auditor'}:
                abort(403)
            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
                for program in visible_programs(connection, scope):
                    folder = f"ValueStreamHQ/programs/{program['id']}"
                    archive.writestr(f'{folder}/program.csv', csv_text([program]))
                    visible_ids = {row['id'] for row in visible_projects(connection, scope)}
                    dependencies = [dict(row) for row in connection.execute(
                        'SELECT * FROM dependencies WHERE program_id=? ORDER BY id', (program['id'],))
                        if row['from_project'] in visible_ids and row['to_project'] in visible_ids]
                    if dependencies:
                        archive.writestr(f'{folder}/dependencies.csv', csv_text(dependencies))
                for project in visible_projects(connection, scope):
                    folder = f"ValueStreamHQ/projects/{project['id']}"
                    archive.writestr(f'{folder}/project.csv', csv_text([project]))
                    archive.writestr(f'{folder}/guide.csv', csv_text(records(connection, project['id'])))
            buffer.seek(0)
            return send_file(buffer, mimetype='application/zip', as_attachment=True, download_name='ValueStreamHQ.zip')

    @app.post('/api/live/csv')
    def import_csv():
        with database() as connection:
            user, role, scope = actor(connection, 'live')
            if role not in {'admin', 'program', 'project'}:
                abort(403)
            body = payload()
            raw = body.get('csv')
            if not isinstance(raw, str):
                abort(400, 'Provide an edited project.csv.')
            reader = csv.DictReader(io.StringIO(raw, newline=''))
            if reader.fieldnames != ['id', 'program_id', 'name', 'role', 'budget', 'status', 'version']:
                abort(400, 'project.csv row 1 has invalid columns.')
            rows = list(reader)
            if len(rows) != 1:
                abort(400, 'project.csv must contain one project row.')
            row = rows[0]
            project = next((p for p in visible_projects(connection, scope) if p['id'] == row['id']), None)
            if not project:
                abort(404)
            name = required_text(row, 'name')
            if any(row.get(key) != str(project[key]) for key in ('program_id', 'role', 'budget', 'status')):
                abort(400, 'project.csv row 2 supports editing the project name only.')
            version = row.get('version') or ''
            if not version.isascii() or not version.isdecimal() or len(version) > 12:
                abort(400, 'project.csv row 2 has an invalid version.')
            if int(version) != project['version']:
                abort(409, 'This export is stale. Export the current project and try again.')
            if body.get('apply') is True:
                update_name(connection, user, project, name, int(version))
            return jsonify(project_id=project['id'], previous=project['name'], proposed=name,
                           applied=body.get('apply') is True)

    return app


GUIDE = [
    ('Intake', 'Describe the business problem, value stream, sponsor, and success measure.'),
    ('Charter', 'Confirm scope, funding assumptions, delivery owner, and decision rights.'),
    ('PI planning', 'Agree on PI objectives, capacity, dependencies, and target milestones.'),
    ('Delivery', 'Review delivery status, risks, change requests, and dependency owners.'),
    ('Quality and release', 'Record integration and UAT evidence, approvals, and cutover readiness.'),
    ('Transition', 'Confirm operational ownership, hypercare exit, benefits follow-up, and closure.'),
]


def initialize(connection):
    connection.executescript("""
        CREATE TABLE IF NOT EXISTS programs (id TEXT PRIMARY KEY, name TEXT NOT NULL, objective TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS projects (id TEXT PRIMARY KEY, program_id TEXT REFERENCES programs(id),
            name TEXT NOT NULL, role TEXT NOT NULL, budget INTEGER NOT NULL, status TEXT NOT NULL, version INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS register (project_id TEXT REFERENCES projects(id), phase INTEGER,
            kind TEXT NOT NULL, detail TEXT NOT NULL, completed INTEGER NOT NULL, PRIMARY KEY(project_id, phase));
        CREATE TABLE IF NOT EXISTS dependencies (id TEXT PRIMARY KEY, program_id TEXT REFERENCES programs(id),
            from_project TEXT REFERENCES projects(id), to_project TEXT REFERENCES projects(id), detail TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS members (subject TEXT PRIMARY KEY, role TEXT NOT NULL, scope TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS audit (id INTEGER PRIMARY KEY, happened_at TEXT DEFAULT CURRENT_TIMESTAMP,
            subject TEXT, action TEXT, record_id TEXT, previous TEXT, updated TEXT);
    """)


def seed(connection):
    def read(name):
        with (ROOT / 'insurance_data' / name).open(newline='') as source:
            return list(csv.reader(source))[1:]
    connection.executemany('INSERT OR IGNORE INTO programs VALUES (?, ?, ?)', read('programs.csv'))
    connection.executemany('INSERT OR IGNORE INTO projects VALUES (?, ?, ?, ?, ?, ?, 1)', read('projects.csv'))
    progress = {'policy': 3, 'billing': 2, 'claims': 2}
    connection.executemany('INSERT OR IGNORE INTO register VALUES (?, ?, ?, ?, ?)',
                           [(*row, int(int(row[1]) <= progress[row[0]])) for row in read('register.csv')])
    connection.executemany('INSERT OR IGNORE INTO dependencies VALUES (?, ?, ?, ?, ?)', read('dependencies.csv'))


def payload():
    data = request.get_json()
    if not isinstance(data, dict):
        abort(400, 'Provide an object.')
    return data


def required_text(data, key):
    value = data.get(key)
    if not isinstance(value, str) or not 1 <= len(value.strip()) <= 500:
        abort(400, f'{key} must contain 1 to 500 characters.')
    return value.strip()


def visible_projects(connection, scope):
    return [dict(row) for row in connection.execute(
        'SELECT * FROM projects WHERE ?=\'*\' OR id=? OR program_id=? ORDER BY id', (scope, scope, scope))]


def visible_programs(connection, scope):
    return [dict(row) for row in connection.execute(
        "SELECT * FROM programs WHERE ?='*' OR id=? OR id IN (SELECT program_id FROM projects WHERE id=?) ORDER BY id",
        (scope, scope, scope))]


def records(connection, project_id):
    return [dict(row) for row in connection.execute(
        'SELECT phase,kind,detail,completed FROM register WHERE project_id=? ORDER BY phase', (project_id,))]


def audit(connection, user, action, record_id, before=None, after=None):
    connection.execute('INSERT INTO audit(subject,action,record_id,previous,updated) VALUES (?,?,?,?,?)',
                       (user, action, record_id, before, after))


def update_name(connection, user, project, name, version):
    if type(version) is not int or not connection.execute(
            'UPDATE projects SET name=?, version=version+1 WHERE id=? AND version=?',
            (name, project['id'], version)).rowcount:
        abort(409, 'This project changed. Reload it and try again.')
    audit(connection, user, 'rename project', project['id'], project['name'], name)


def csv_text(rows):
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]))
    writer.writeheader()
    for row in rows:
        writer.writerow({key: "'" + value if isinstance(value, str) and value.lstrip().startswith(('=', '+', '-', '@'))
                         else value for key, value in row.items()})
    return buffer.getvalue()
