from app.repository.user_repository import User
from app.app import db_dependency


def create_user(user: User, db: db_dependency):
    db.append(user)
    return {'message': 'User created successfully',
            'user_id': user.id
            }