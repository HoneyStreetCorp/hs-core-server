import uuid

from sqlalchemy import Column, func, DateTime
from sqlalchemy.dialects.postgresql import UUID

from core.session import Base


def generate_uuid():
    return str(uuid.uuid1())


class Answer(Base):
    __tablename__ = "answers"
    answer_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=generate_uuid)
    user_id = Column(UUID(as_uuid=True), foreign_key=True)
    created_at = Column(DateTime, default=func.utc_timestamp())
