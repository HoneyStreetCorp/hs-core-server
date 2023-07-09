import uuid

from sqlalchemy import Column, DateTime, func, String
from sqlalchemy.dialects.postgresql import UUID

from core.session import Base
from util import base64_util


def generate_uuid():
    return str(uuid.uuid1())


def create_hash_name(name: str):
    _hash = base64_util.encode(name)
    return name + '#' + _hash[:4]


class User(Base):
    __tablename__ = 'users'
    user_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=generate_uuid)
    name = Column(String(36), nullable=False)
    created_at = Column(DateTime, default=func.utc_timestamp())
