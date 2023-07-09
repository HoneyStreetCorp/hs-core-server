from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application import question_find_service
from middleware.deps import get_db

router = APIRouter()


@router.get("/")
def get_question(
        db: Session = Depends(get_db)
) -> Any:
    return question_find_service.get_questions(db)
