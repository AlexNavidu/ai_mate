from httpx import AsyncClient


async def test_create_chat(ac: AsyncClient, registered_user_token: str):
    data = {
        "name": 'Новый чат пользователя',
        "pinned": 0,
        "icon_chat": 'Тестовая ссылка',
    }
    headers = {"Authorization": f"Bearer {registered_user_token}"}
    response = await ac.post('api/v1/chats', json=data, headers=headers)
    print(response.json())
    assert response.status_code == 201
