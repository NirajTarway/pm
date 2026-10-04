from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_returns_hello_world() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "Hello, world" in response.text
    assert response.headers["content-type"].startswith("text/html")


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
