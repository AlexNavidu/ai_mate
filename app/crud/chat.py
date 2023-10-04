from app.crud.base import CRUDBase
from app.models.сhat import Chat


class CRUDChat(CRUDBase):
    pass


chat_crud = CRUDChat(Chat)
