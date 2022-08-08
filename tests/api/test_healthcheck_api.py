from fastapi.testclient import TestClient

from appointment_mail_notifier.api.main_api import app


def test_healthcheck_api():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}
