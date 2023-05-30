import os
from pydantic import BaseSettings, Field





class Settings(BaseSettings):
    app_title: str = 'AI Mate - GPT chat'
    database_url: str = Field(..., env='DATABASE_URL')
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
