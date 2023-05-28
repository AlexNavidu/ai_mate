from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base


class Message(Base):
    text = Column(Text)
    created_at = Column(DateTime)
    sender = Column(String(255))
    chat_id = Column(Integer, ForeignKey('chat.id'))
    chat = relationship('Chat', back_populates="messages")
