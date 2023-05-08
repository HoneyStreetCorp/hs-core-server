from model.user import User


class UserCreateService:
    def create_user(self, db) -> User:
        user = User()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
