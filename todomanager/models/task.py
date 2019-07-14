from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column()

Index('task', Task.id, unique=True, mysql_length=255)
