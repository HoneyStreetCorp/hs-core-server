from typing import Any, Optional

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from application import user_create_service
from dto.response.user_response import UserResponse
from middleware.deps import get_db

router = APIRouter()


@router.post("/")
def create_user(
        db: Session = Depends(get_db),
        name: str = Query(default=None)
) -> Any:
    if name is None:
        raise HTTPException(
            status_code=400,
            detail="name requried"
        )
    user = user_create_service.create_user(db, name)
    return UserResponse(id=user.user_id, name=user.name)
