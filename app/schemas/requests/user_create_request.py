from typing import List, Optional
from pydantic import BaseModel
from app.schemas.enums.gender import Gender
from app.schemas.enums.role import Role


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]