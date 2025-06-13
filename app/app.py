from app.repository import user_repository
from app.database import SessionLocal, engine
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from app.controller.user_controller import user_router

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

user_repository.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]