from fastapi import APIRouter
from app.domain.models import user
from app.repository.user_repository import User
from app.service import user_service
from app.app import db_dependency


user_router = APIRouter(prefix="/api/users")

@user_router.get("/hello", status_code=200)
def root():
    return {"message": "Hello, World!"}

@user_router.post("/", status_code=200)
async def create_user(user: User, db: db_dependency):
    return user_service.create_user(user, db)

'''
@app.get("/api/v1/users", status_code=200)
async def get_users(db: db_dependency):
    return db



@app.post("/api/v1/user", status_code=201)
async def create_user(user: User):
    return create_user(user)
'''