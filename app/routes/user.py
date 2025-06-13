from fastapi import APIRouter
from app.schemas.user import User
from app.service import user_service
from app.dependencies import db_dependency


user_router = APIRouter(prefix="/api/users", tags=["Users"])

@user_router.get("/hello", status_code=200)
def root():
    return {"message": "Hello, World!"}

@user_router.post("/", status_code=200)
async def create_user(user: User, db: db_dependency):
    return user_service.create_user(user, db)
