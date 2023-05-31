from httpx import AsyncClient


async def test_register_user(ac: AsyncClient):
    data = {
        "email": "user23@example.com",
        "password": "xtcnmbolo86",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False
    }
    response = await ac.post('/api/v1/auth/register', json=data)
    assert response.status_code == 201


async def test_auth_user(ac: AsyncClient):
    data = {
        "username": "user23@example.com",
        "password": "xtcnmbolo86"
    }
    response = await ac.post(
        '/api/v1/auth/jwt/login',
        data=data,
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()['token_type'] == 'bearer'
