from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.crud.chat import chat_crud
from app.core.user import current_user
from app.models.сhat import Chat
from app.models.user import User
from app.schemas.chat import ChatCreate

router = APIRouter()


@router.post(
    '/',
)
async def create_new_chat(
        chat: ChatCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    # TODO надо проверить, передается ли на id topic. Если передается, то генерируем название чата исходя ис значение
    # TODO топика, если нет, то надо передавать дефолтно значение чата.
    # TODO надо выяснить, как сделаем с картинкой чата. Передам в запросе или берем из Topic
    new_chat = await chat_crud.create(chat, session, user)
    return new_chat
    # TODO также в данных должно прийти первое сообщение, по хорошму, нам надо пойти и создать новые объект этого сообщения.
