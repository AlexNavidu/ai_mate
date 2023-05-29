import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .conftest import client

from httpx import AsyncClient

from app.main import app


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
