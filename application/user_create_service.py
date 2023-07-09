import time

from sqlalchemy.orm import Session

from model.user import User, create_hash_name


class UserCreateService:
    def create_user(self, db: Session, user_name: str) -> User:
        user = User(name=create_hash_name(user_name))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
