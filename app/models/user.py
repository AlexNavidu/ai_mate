from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    created_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    chats = relationship('Chat',  back_populates="user", lazy="dynamic")
