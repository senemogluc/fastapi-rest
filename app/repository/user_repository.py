from ast import List
from ctypes import Array
from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, UUID, ARRAY
from app.domain.enums import gender, role
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    gender = Column(Enum(gender.Gender), nullable=False)
    roles = Column(ARRAY(Enum(role.Role)), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id})>"