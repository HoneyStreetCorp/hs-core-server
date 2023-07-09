from typing import Any

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from application import user_create_service
from core.error import CustomException
from dto.error.error_response import ErrorResponse
from dto.response.user_response import UserResponse
from middleware.deps import get_db

router = APIRouter()


@router.post("/")
def create_user(
        db: Session = Depends(get_db),
        name: str = Query(default=None)
) -> Any:
    if name is None:
        raise CustomException(ErrorResponse(message="[ERROR] name field ommitted. Name required.", status_code=400))
    user = user_create_service.create_user(db, name)
    return UserResponse(id=user.user_id, name=user.name)
