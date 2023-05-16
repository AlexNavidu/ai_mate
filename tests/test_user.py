from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_user():

    data = {
        "email": "user@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False
    }
    response = client.post('/api/v1/auth/register', json=data)
    print(response.url)
    assert response.status_code == 201
