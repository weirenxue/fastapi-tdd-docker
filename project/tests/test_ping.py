from starlette.testclient import TestClient


def test_ping(test_app: TestClient):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "ping": "pong!",
        "testing": True,
        "database_url": "postgres://postgres:postgres@web-db:5432/web_test",
    }
