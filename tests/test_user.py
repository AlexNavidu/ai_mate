from httpx import AsyncClient


async def test_register_user(ac: AsyncClient):
    data = {
        "email": "user23@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False
    }
    response = await ac.post('/api/v1/auth/register', json=data)
    assert response.status_code == 201
