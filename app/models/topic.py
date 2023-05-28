from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.base import Base


class Topic(Base):
    title = Column(String(255), unique=True, nullable=False)
    context = Column(Text)
    suggestion_id = Column(Integer, ForeignKey('suggestion.id'))
    suggestion = relationship('Suggestion', back_populates="topics")
