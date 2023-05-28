from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.base import Base


class Suggestion(Base):
    name = Column(String(255), unique=True, nullable=False)
    position = Column(Integer, nullable=False)
    topics = relationship('Topic', back_populates="suggestion")
