from app.database import engine
from fastapi import Depends, FastAPI
from app.models import user_orm
from app.routes.user import user_router


app = FastAPI()
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

user_orm.Base.metadata.create_all(bind=engine)
