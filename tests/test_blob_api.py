from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_containers():
    response = client.get("/containers")
    assert response.status_code == 200
    assert "containers" in response.json()
    assert isinstance(response.json()["containers"], list)
