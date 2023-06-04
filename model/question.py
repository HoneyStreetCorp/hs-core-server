import uuid

from sqlalchemy import Column, func, DateTime, String, JSON
from sqlalchemy.dialects.postgresql import UUID, array

from core.session import Base


def generate_uuid():
    return str(uuid.uuid1())


class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid, unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(String(255), nullable=True)
    answer = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.utc_timestamp())

