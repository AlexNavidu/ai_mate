from fastapi import APIRouter

from app.api.endpoints import (user_router, chat_router)

main_router = APIRouter()
main_router.include_router(
    user_router,
    prefix='/api/v1',
)
main_router.include_router(
    chat_router,
    prefix='/api/v1/chats',
)
