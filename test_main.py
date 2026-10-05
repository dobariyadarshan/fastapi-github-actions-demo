from fastapi.testclient import TestClient

from main import app


def test_hello():
    with TestClient(app) as client:
        response = client.get("/hello")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Darshan!"}

def test_health():
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}