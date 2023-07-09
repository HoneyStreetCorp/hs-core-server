import time

from sqlalchemy.orm import Session

from core.error import CustomException
from dto.error.error_response import ErrorResponse
from model.user import User, create_hash_name


class UserCreateService:
    def create_user(self, db: Session, user_name: str) -> User:
        user = User(name=create_hash_name(user_name))
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception:
            raise CustomException(ErrorResponse(message="[ERROR] Transaction failed", status_code=500))
