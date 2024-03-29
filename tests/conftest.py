import asyncio
import os
from typing import AsyncGenerator

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

load_dotenv()

from app.core.db import Base, get_async_session
from app.main import app

# DATABASE
DB_HOST_TEST = os.environ.get("DB_HOST")
DB_PORT_TEST = os.environ.get("DB_PORT")
DB_NAME_TEST = os.environ.get("POSTGRES_DB")
DB_USER_TEST = os.environ.get("POSTGRES_USER")
DB_PASS_TEST = os.environ.get("POSTGRES_PASSWORD")

DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# SETUP
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def registered_user_token(ac: AsyncClient) -> str:
    """
    Сreated a user for testing
    """
    register_data = {
        "email": "user24@example.com",
        "password": "xtcnmbolo86",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False
    }
    register_response = await ac.post('/api/v1/auth/register', json=register_data)
    assert register_response.status_code == 201
    login_data = {
        "username": "user23@example.com",
        "password": "xtcnmbolo86"
    }
    login_response = await ac.post('/api/v1/auth/jwt/login', data=login_data)
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]
    return access_token
