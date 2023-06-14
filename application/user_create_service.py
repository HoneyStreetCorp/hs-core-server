from sqlalchemy.orm import Session

from model.user import User


class UserCreateService:
    def create_user(self, db: Session) -> User:
        user = User()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
