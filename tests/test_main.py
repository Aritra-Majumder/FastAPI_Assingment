from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_batch():
    response = client.post("/add", json={"batchid": "id0101", "payload": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data

def test_invalid_payload():
    response = client.post("/add", json={"batchid": "id0101", "payload": "invalid"})
    assert response.status_code == 422
