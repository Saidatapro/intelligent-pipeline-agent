
from fastapi.testclient import TestClient
from src.api.main import app
def test_healthz():
    c=TestClient(app); r=c.get('/healthz')
    assert r.status_code==200 and r.json().get('ok') is True
