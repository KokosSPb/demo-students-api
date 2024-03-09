from pydantic import BaseModel


class StudentSchema(BaseModel):
    name: str
    group: str
    age: int


class StudentRequestFilter(BaseModel):
    max_age: int
