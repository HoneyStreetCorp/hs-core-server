from fastapi import APIRouter

from controller import user_create

api_router = APIRouter()

api_router.include_router(user_create.router, prefix="/users", tags=["users"])
