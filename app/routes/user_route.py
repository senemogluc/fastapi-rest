from typing import List
from fastapi import APIRouter
from app.schemas.requests.user_create_request import CreateUserRequest
from app.schemas.response.user_create_response import CreateUserOut
from app.service import user_service
from app.dependencies import db_dependency


user_router = APIRouter(prefix="/api/users", tags=["Users"])

@user_router.get("/hello", status_code=200)
def root():
    return {"message": "Hello, World!"}

@user_router.post("/", status_code=201, response_model=CreateUserOut)
async def create_user(user: CreateUserRequest, db: db_dependency):
    return user_service.create(user, db)

@user_router.get("/", status_code=200, response_model=List[CreateUserOut])
async def get_all_users(db: db_dependency):
    return user_service.get_all(db)
