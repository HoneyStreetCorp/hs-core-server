import uuid

from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

from core.session import Base


def generate_uuid():
    return str(uuid.uuid1())


class User(Base):
    __tablename__ = 'users'
    user_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=generate_uuid)
    name = Column(str, nullable=False)
    created_at = Column(DateTime, default=func.utc_timestamp())
