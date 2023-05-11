# main.py
from app.core.config import settings
from fastapi import FastAPI

app = FastAPI(title=settings.app_title)


@app.get('/')
def read_root():
    return {'Hello': 'FastAPI'}
