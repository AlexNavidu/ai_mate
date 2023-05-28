from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.base import Base


class Chat(Base):
    name = Column(String(255), nullable=False)
    pinned = Column(Boolean)
    icon_chat = Column(String(255))
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='chats')
    messages = relationship('Message', back_populates='chat')
