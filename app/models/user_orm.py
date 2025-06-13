from sqlalchemy import Column, Enum, String, UUID, ARRAY
from app.schemas.enums.gender import Gender
from app.schemas.enums.role import Role
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    gender = Column(Enum(Gender), nullable=False)
    roles = Column(ARRAY(Enum(Role)), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id})>"