from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class ChatBase(BaseModel):
    name: str
    pinned: bool
    icon_chat: str


class ChatCreate(ChatBase):
    created_at: Optional[datetime] = datetime.now()
    user_id: int


class ChatUpdate(ChatBase):
    pass


class ChatDB(ChatBase):
    id: int
    created_at: Optional[datetime]
    user: int
    messages: List[str]

    class Config:
        orm_mode = True
