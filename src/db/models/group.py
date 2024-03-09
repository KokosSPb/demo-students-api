from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID


class GroupModel(SQLModel, table=True):
    __tablename__ = "group"

    id: UUID = Field(
        primary_key=True,
        default_factory=uuid4
    )

    name: str = Field(
        max_length=100,
        unique=True
    )

    chief: str = Field(
        max_length=100
    )
