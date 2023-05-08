from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application import user_create_service
from dto.response.user_response import UserResponse
from middleware.deps import get_db

router = APIRouter()


@router.post("/")
def create_user(
        db: Session = Depends(get_db)
) -> Any:
    user = user_create_service.create_user(db)
    return UserResponse(user.user_id)
