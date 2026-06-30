from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test Home API
def test_home():
    respone = client.get("/")

    # Status code check
    assert respone.status_code == 200

    # Response data check
    assert respone.json() == {"message": "Hello Ayush"}

# Test Add API
def test_add():
    respone = client.get("/add?a=5&b=2")

    # Status code check
    assert respone.status_code == 200

    # Response data check
    assert respone.json() == {"return": 9}