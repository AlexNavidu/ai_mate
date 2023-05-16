from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_title: str = 'AI Mate - GPT chat'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
