import io
import zipfile

import pytest

from insurance_server import create_app


@pytest.fixture
def app(tmp_path):
    return create_app({'TESTING': True, 'DATABASE': str(tmp_path / 'workspace.db'),
                       'FIRST_ADMIN_SUB': 'test-admin'})


def live_login(client, subject='test-admin'):
    # Inject a verified subject for server authorization tests. Okta remains external.
    with client.session_transaction() as stored:
        stored['sub'] = subject


def lab_login(client, persona):
    response = client.post('/api/lab/session', json={'action': 'sign-in', 'user': persona})
    assert response.status_code == 202
    assert client.get('/api/lab/projects').status_code == 401
    assert client.post('/api/lab/session', json={'action': 'verify',
                       'code': response.json['code']}).status_code == 200


def test_anonymous_and_unconfigured_okta(app):
    client = app.test_client()
    assert client.get('/api/live/projects').status_code == 401
    assert client.get('/okta/login').status_code == 503
    assert client.get('/insurance-workspace.html').status_code == 200
    assert client.post('/api/live/seed', data='unsafe').status_code == 415


@pytest.mark.parametrize(('persona', 'visible'), [
    ('avery.program', {'billing', 'claims', 'policy'}),
    ('jordan.underwriting', {'policy'}), ('casey.billing', {'billing'}),
    ('riley.claims', {'claims'}), ('morgan.pm', {'policy'}),
    ('taylor.qa', {'billing', 'claims', 'policy'}), ('sam.audit', {'billing', 'claims', 'policy'}),
])
def test_lab_roles(app, persona, visible):
    client = app.test_client()
    lab_login(client, persona)
    result = client.get('/api/lab/projects')
    assert {p['id'] for p in result.json['projects']} == visible
    assert client.get('/api/live/projects').status_code == 401
    assert client.get('/api/lab/projects/claims').status_code == (200 if 'claims' in visible else 404)


def test_challenge_and_logout(app):
    client = app.test_client()
    challenge = client.post('/api/lab/session', json={'action':'sign-in', 'user':'sam.audit'}).json
    assert client.post('/api/lab/session', json={'action':'verify','code':'invalid'}).status_code == 401
    assert client.post('/api/lab/session', json={'action':'verify','code':challenge['code']}).status_code == 401
    lab_login(client, 'sam.audit')
    assert client.get('/api/lab/audit').status_code == 200
    assert client.post('/api/lab/projects', json={'name':'No'}).status_code == 403
    assert client.post('/api/lab/session', json={'action':'logout'}).status_code == 200
    assert client.get('/api/lab/audit').status_code == 401


def test_program_and_project_share_persisted_state(app):
    first = app.test_client()
    live_login(first)
    assert first.post('/api/live/seed', json={}).status_code == 200
    assert len(first.get('/api/live/projects').json['dependencies']) == 2
    program = first.post('/api/live/programs', json={'name':'Commercial Lines', 'objective':'Simplify service'}).json
    created = first.post('/api/live/projects', json={'program_id':program['id'], 'name':'Broker Portal'})
    assert created.status_code == 201
    second = app.test_client()
    live_login(second)
    path = '/api/live/projects/' + created.json['id']
    assert len(second.get(path).json['guide']) == 6
    assert second.post(path + '/guide/2', json={'detail':'Evidence'}).status_code == 409
    assert second.post(path + '/guide/1', json={'detail':'Sponsor approved'}).status_code == 200
    assert first.get(path).json['project']['status'] == 'Charter'
    assert first.post(path, json={'name':'Stale rename','version':1}).status_code == 409


def test_cross_project_denials_and_scoped_export(app):
    admin = app.test_client()
    live_login(admin)
    admin.post('/api/live/seed', json={})
    assert admin.post('/api/live/members', json={'subject':'pm', 'role':'project','scope':'policy'}).status_code == 200
    pm = app.test_client()
    live_login(pm, 'pm')
    assert pm.get('/api/live/projects/claims').status_code == 404
    assert pm.post('/api/live/projects/claims', json={'name':'No', 'version':1}).status_code == 404
    assert pm.post('/api/live/members', json={'subject':'other','role':'admin','scope':'*'}).status_code == 403
    assert pm.get('/api/live/audit').status_code == 403
    with zipfile.ZipFile(io.BytesIO(pm.get('/api/live/csv').data)) as exported:
        assert all('/claims/' not in path and '/billing/' not in path for path in exported.namelist())
        assert not any(path.endswith('dependencies.csv') for path in exported.namelist())


def test_csv_preview_apply_and_stale_conflict(app):
    client = app.test_client()
    live_login(client)
    client.post('/api/live/seed', json={})
    with zipfile.ZipFile(io.BytesIO(client.get('/api/live/csv').data)) as exported:
        csv = exported.read('ValueStreamHQ/projects/policy/project.csv').decode().replace('Policy Self-Service','Policy Service')
    assert client.post('/api/live/csv', json={'csv':csv}).json['applied'] is False
    assert client.get('/api/live/projects/policy').json['project']['name'] == 'Policy Self-Service'
    assert client.post('/api/live/csv', json={'csv':csv,'apply':True}).json['applied'] is True
    assert client.get('/api/live/projects/policy').json['project']['name'] == 'Policy Service'
    assert client.post('/api/live/csv', json={'csv':csv,'apply':True}).status_code == 409
    assert any(e['previous'] == 'Policy Self-Service' and e['updated'] == 'Policy Service'
               for e in client.get('/api/live/audit').json['events'])
