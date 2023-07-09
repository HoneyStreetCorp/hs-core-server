from fastapi import APIRouter

from controller import user_create, question_find

api_router = APIRouter()

api_router.include_router(user_create.router, prefix="/users", tags=["users"])
api_router.include_router(question_find.router, prefix="/questions", tags=["questions"])
