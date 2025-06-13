from email.policy import HTTP
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from app.models.gender import Gender
from app.models.role import Role
from app.models.user import User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Alice",
        last_name="Smith",
        gender=Gender.FEMALE,
        roles=[Role.USER]
        ),
    User(
        id=uuid4(),
        first_name="Bob",
        last_name="Johnson",
        middle_name="Ben",
        gender=Gender.MALE,
        roles=[Role.STUDENT]
        )
]

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/api/v1/users", status_code=200, response_model=List[User])
async def get_users():
    return db

@app.post("/api/v1/user", status_code=201)
async def create_user(user: User):
    db.append(user)
    return {'message': 'User created successfully',
            'user_id': user.id
            }

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {'message': 'User deleted successfully'}
        else:
            raise HTTPException(
                status_code=404,
                detail=f"User with id: {user_id} not found.")
