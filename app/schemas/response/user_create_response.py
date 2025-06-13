from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID
from app.schemas.enums.gender import Gender
from app.schemas.enums.role import Role


class CreateUserOut(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]