from http import HTTPStatus

from fastapi import APIRouter

from src.api.v1.schema.students import StudentSchema, StudentRequestFilter

router = APIRouter()


@router.get(
    "/student",
    status_code=HTTPStatus.OK,
    description="Return list of students",
    response_model=list[StudentSchema]
)
async def get_students(filters: StudentRequestFilter):

    students = [
        {
        "name":'Ваня',
        "group": "123",
        "age": 18
        },
        {
            "name": 'Петя',
            "group": "1234",
            "age": 19
        }
    ]
    return [StudentSchema(**student)
            for student in students if student['age'] < filters.max_age]
