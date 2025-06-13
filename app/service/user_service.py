from operator import ge
from uuid import uuid4
from app.schemas.enums.gender import Gender
from app.models.user_orm import User
from sqlalchemy.orm import Session


def create_user(user: User, db: Session):
    db_user = User(
        id=uuid4(),
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        gender = user.gender,
        roles=user.roles
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return f'User is created with id: {db_user.id}'
    